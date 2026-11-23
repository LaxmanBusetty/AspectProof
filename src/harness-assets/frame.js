// AspectProof device frame + layout probe.
// Runs in the harness page inside Kane's browser. The app loads in a same-origin iframe sized
// to the device profile; the probe measures the app's DOM and shows the result in a panel that
// Kane reads, and posts the same data to the harness so the coding agent gets exact selectors.
(() => {
  const boot = window.__AP_BOOT;
  const { profile, runId, start } = boot;
  const iframe = document.getElementById('ap-app');
  const device = document.getElementById('ap-device');
  const stage = document.getElementById('ap-stage');
  const $ = (id) => document.getElementById(id);

  const windowMode = profile.mode === 'window';
  document.body.classList.toggle('ap-window', windowMode);
  $('ap-profile').textContent = windowMode
    ? `${profile.label} (full window)`
    : `${profile.label} · ${profile.width > profile.height ? 'landscape' : 'portrait'}`;

  // ---- Device sizing ----
  function layout() {
    if (windowMode) return;
    const pad = 36;
    const scale = Math.min(1, (stage.clientWidth - pad) / profile.width, (stage.clientHeight - pad) / profile.height);
    iframe.style.width = `${profile.width}px`;
    iframe.style.height = `${profile.height}px`;
    iframe.style.transform = scale < 1 ? `scale(${scale})` : '';
    device.style.width = `${Math.floor(profile.width * scale)}px`;
    device.style.height = `${Math.floor(profile.height * scale)}px`;
    device.dataset.scale = scale.toFixed(3);
  }
  window.addEventListener('resize', layout);
  layout();
  iframe.src = start;

  // ---- Probe ----
  const persistent = new Map(); // key -> issue (overflow / offscreen: kept once seen)
  const coverStats = new Map(); // key -> { covered, clear, issue }
  const smallTargets = new Map();
  let scans = 0;
  let probeError = null;
  let lastPosted = '';

  const INTERACTIVE = 'a[href], button, input:not([type=hidden]), select, textarea, [role=button], [onclick], summary';

  function describe(el) {
    const parts = [];
    let node = el;
    for (let depth = 0; node && node.nodeType === 1 && depth < 3; depth++, node = node.parentElement) {
      if (node.tagName === 'BODY' || node.tagName === 'HTML') break;
      let part = node.tagName.toLowerCase();
      if (node.id) { parts.unshift(`${part}#${node.id}`); break; }
      const classes = [...node.classList].slice(0, 2);
      if (classes.length) part += '.' + classes.join('.');
      parts.unshift(part);
    }
    return parts.join(' > ') || el.tagName.toLowerCase();
  }

  function label(el) {
    const t = (el.getAttribute('aria-label') || el.innerText || el.value || el.placeholder || el.name || '').trim().replace(/\s+/g, ' ');
    return t.length > 40 ? t.slice(0, 39) + '…' : t;
  }

  function isVisible(el, win) {
    if (typeof el.checkVisibility === 'function') {
      if (!el.checkVisibility({ checkOpacity: true, checkVisibilityCSS: true })) return false;
    } else {
      const cs = win.getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden' || Number(cs.opacity) === 0) return false;
    }
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  }

  function scan() {
    let doc, win;
    try {
      doc = iframe.contentDocument;
      win = iframe.contentWindow;
      if (!doc || !doc.documentElement) return;
    } catch (err) {
      probeError = 'The app is on a different origin, so the layout probe cannot read it. Load it through the AspectProof harness.';
      render([]);
      return;
    }
    probeError = null;
    scans++;
    const now = [];
    const vw = doc.documentElement.clientWidth;
    const vh = win.innerHeight;

    // 1. Horizontal overflow of the whole page.
    const sw = Math.max(doc.documentElement.scrollWidth, doc.body ? doc.body.scrollWidth : 0);
    if (sw > vw + 1) {
      const issue = { kind: 'horizontal-overflow', selector: 'page', text: '', detail: `page is ${sw}px wide in a ${vw}px viewport (+${sw - vw}px, sideways scrolling)` };
      persistent.set('overflow:page', issue);
      now.push(issue);
    }

    // 2. Find where the overflow starts: overflowing elements whose parent fits. Elements with a
    //    fixed width or min-width are listed first, since that is usually the culprit.
    if (sw > vw + 1 && doc.body) {
      const roots = [];
      for (const el of doc.body.querySelectorAll('*')) {
        const r = el.getBoundingClientRect();
        if (!(r.right > vw + 1 && r.width > 0) || !isVisible(el, win)) continue;
        const pr = el.parentElement ? el.parentElement.getBoundingClientRect() : null;
        if (pr && pr.right > vw + 1) continue;
        const cs = win.getComputedStyle(el);
        const sizing = [];
        if (/px$/.test(cs.minWidth) && parseFloat(cs.minWidth) > 0) sizing.push(`min-width: ${cs.minWidth}`);
        if (el.style.width || /px$/.test(cs.width) && parseFloat(cs.width) > vw) sizing.push(`width: ${cs.width}`);
        roots.push({ el, r, sizing, fixed: sizing.some((s) => s.startsWith('min-width')) });
      }
      roots.sort((a, b) => (b.fixed - a.fixed) || (b.r.right - a.r.right));
      for (const { el, r, sizing } of roots.slice(0, 3)) {
        const sel = describe(el);
        const issue = { kind: 'overflow-source', selector: sel, text: label(el), detail: `${Math.round(r.width)}px wide, right edge at ${Math.round(r.right)}px (viewport ${vw}px)${sizing.length ? `; computed ${sizing.join(', ')}` : ''}` };
        persistent.set('source:' + sel, issue);
        now.push(issue);
      }
    }

    // 3. Interactive elements: off-screen, covered, too small to tap.
    for (const el of doc.querySelectorAll(INTERACTIVE)) {
      if (!isVisible(el, win)) continue;
      const r = el.getBoundingClientRect();
      const sel = describe(el);
      const text = label(el);

      if (r.right > vw + 1 || r.left < -1) {
        const off = r.right > vw + 1 ? `extends ${Math.round(r.right - vw)}px past the right edge` : `starts ${Math.round(-r.left)}px past the left edge`;
        const issue = { kind: 'offscreen', selector: sel, text, detail: off };
        persistent.set('off:' + sel + text, issue);
        now.push(issue);
      }

      // Coverage: only judge elements fully inside the vertical viewport.
      if (r.top >= 0 && r.bottom <= vh && r.left >= 0 && r.right <= vw) {
        const cx = r.left + r.width / 2;
        const cy = r.top + r.height / 2;
        const top = doc.elementFromPoint(cx, cy);
        const key = 'cover:' + sel + text;
        const stat = coverStats.get(key) || { covered: 0, clear: 0, issue: null };
        if (top && top !== el && !el.contains(top) && !top.contains(el) && !scrollsClear(el, r, top, doc, win, vh)) {
          stat.covered++;
          stat.issue = { kind: 'covered', selector: sel, text, detail: `covered by ${describe(top)}${label(top) ? ` ("${label(top)}")` : ''}` };
        } else {
          stat.clear++;
        }
        coverStats.set(key, stat);
        // Counted only when covered on repeated scans and never seen clear (filters scroll-past overlaps).
        if (stat.covered >= 2 && stat.clear === 0 && top && top !== el && !el.contains(top) && !top.contains(el)) now.push(stat.issue);
      }

      if (profile.touch && (r.width < 24 || r.height < 24)) {
        smallTargets.set(sel + text, { selector: sel, text, size: `${Math.round(r.width)}×${Math.round(r.height)}` });
      }
    }

    render(now);
  }

  // A fixed/sticky bar (cookie banner, promo bar, sticky header) that the user can scroll the
  // element out from under is normal, not a bug. Returns true when scrolling would uncover it.
  function scrollsClear(el, r, coverer, doc, win, vh) {
    let fixed = null;
    for (let n = coverer; n && n !== doc.body; n = n.parentElement) {
      const pos = win.getComputedStyle(n).position;
      if (pos === 'fixed' || pos === 'sticky') { fixed = n; break; }
    }
    if (!fixed) return false;
    const c = fixed.getBoundingClientRect();
    const freeAbove = c.top;          // space above a bottom bar
    const freeBelow = vh - c.bottom;  // space below a top bar
    const docTop = r.top + win.scrollY;
    const maxScroll = Math.max(0, doc.documentElement.scrollHeight - vh);
    // Can the element scroll up into the free space above the bar?
    if (freeAbove >= r.height) {
      const needed = docTop + r.height - freeAbove;
      if (needed <= maxScroll + 1) return true;
    }
    // Or scroll down into the free space below a top bar?
    if (freeBelow >= r.height && docTop >= c.bottom - 1) return true;
    return false;
  }

  function seenIssues() {
    const out = [...persistent.values()];
    for (const stat of coverStats.values()) if (stat.covered >= 2 && stat.clear === 0 && stat.issue) out.push(stat.issue);
    return out;
  }

  function render(now) {
    const seen = seenIssues();
    const probe = $('ap-probe');
    probe.textContent = probeError ? `Probe: unavailable. ${probeError}` : `Probe: active (${scans} scans)`;
    probe.classList.toggle('error', Boolean(probeError));
    $('ap-now').textContent = String(now.length);
    $('ap-seen').textContent = probeError ? 'unknown' : String(seen.length);
    const counts = document.querySelector('.ap-counts');
    counts.classList.toggle('bad', seen.length > 0 || Boolean(probeError));
    counts.classList.toggle('good', seen.length === 0 && !probeError && scans > 0);

    const list = $('ap-issues');
    list.replaceChildren(...seen.slice(0, 12).map((i) => {
      const li = document.createElement('li');
      const kind = document.createElement('span'); kind.className = 'ap-kind'; kind.textContent = i.kind;
      const code = document.createElement('code'); code.textContent = i.selector;
      li.append(kind, ' ', code,document.createTextNode(`${i.text ? ` "${i.text}"` : ''}: ${i.detail}`));
      return li;
    }));
    $('ap-warnings').textContent = smallTargets.size ? `Warnings: ${smallTargets.size} tap target${smallTargets.size === 1 ? '' : 's'} smaller than 24×24px` : '';

    window.__AP_REPORT = {
      runId, profile: profile.id, scans, probeError,
      url: safeAppUrl(),
      issuesNow: now, issuesSeen: seen,
      warnings: [...smallTargets.values()].map((t) => ({ kind: 'small-tap-target', ...t })),
    };
    post();
  }

  function safeAppUrl() {
    try { return iframe.contentWindow.location.pathname + iframe.contentWindow.location.hash; } catch { return null; }
  }

  function post(force) {
    const body = JSON.stringify(window.__AP_REPORT);
    const sig = body.replace(/"scans":\d+,/, '');
    if (!force && sig === lastPosted) return;
    lastPosted = sig;
    fetch(`/__ap/report?run=${encodeURIComponent(runId)}`, { method: 'POST', headers: { 'content-type': 'application/json' }, body, keepalive: true }).catch(() => {});
  }

  iframe.addEventListener('load', () => scan());
  setInterval(scan, 600);
  setInterval(() => post(true), 4000);
  window.addEventListener('pagehide', () => post(true));
})();
