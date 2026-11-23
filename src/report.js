// Self-contained HTML report: profiles × flows, red-to-green history per cell, Kane + probe evidence.
import { writeFile, mkdir } from 'node:fs/promises';
import { join } from 'node:path';
import { STATE_DIR, cellKey } from './config.js';

const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

export function renderReport(config, state) {
  const total = config.profiles.length * config.flows.length;
  const cells = config.profiles.flatMap((p) => config.flows.map((f) => state.cells[cellKey(p.id, f.id)])).filter(Boolean);
  const passed = cells.filter((c) => c.verdict === 'pass').length;
  const verified = passed === total && cells.length === total;
  const firstFull = state.rounds.find((r) => r.scope === 'full');
  const caught = Object.values(state.cells).reduce((acc, c) => {
    if ((c.history || []).some((h) => h.verdict !== 'pass')) acc.fixed += c.verdict === 'pass' ? 1 : 0;
    return acc;
  }, { fixed: 0 });

  const head = config.flows.map((f) => `<th scope="col">${esc(f.name)}</th>`).join('');
  const rows = config.profiles.map((p) => {
    const tds = config.flows.map((f) => renderCell(state.cells[cellKey(p.id, f.id)])).join('');
    return `<tr><th scope="row"><div class="pname">${esc(p.label)}</div><div class="pmeta">${p.width}×${p.height} · ${p.mode === 'window' ? 'Kane window' : 'device frame'}</div></th>${tds}</tr>`;
  }).join('');

  const maxBar = Math.max(1, total);
  const timeline = state.rounds.map((r) => `
    <div class="tl-round" title="Round ${r.round}: ${r.passed}/${r.ran} passed this round; matrix ${r.matrixPassed}/${r.matrixTotal}">
      <div class="tl-bar"><div class="tl-fill ${r.matrixPassed === r.matrixTotal ? 'ok' : ''}" style="height:${Math.round((r.matrixPassed / maxBar) * 100)}%"></div></div>
      <div class="tl-label">R${r.round}</div><div class="tl-sub">${r.matrixPassed}/${r.matrixTotal}</div>
      <div class="tl-scope">${r.scope === 'failed' ? 'retest' : 'full'}</div>
    </div>`).join('');

  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>AspectProof report: ${passed}/${total}</title>
<style>
  :root { --ok:#1f8a4c; --ok-bg:#e7f5ec; --bad:#c62828; --bad-bg:#fdecea; --err:#8a6d00; --err-bg:#fff6d6; --ink:#1b1f24; --muted:#5f6b7a; --line:#e3e6ea; }
  * { box-sizing: border-box; }
  body { margin:0; font:14px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; color:var(--ink); background:#f7f8fa; }
  header { padding:28px 32px 8px; display:flex; flex-wrap:wrap; gap:24px; align-items:center; justify-content:space-between; }
  h1 { margin:0; font-size:24px; } .sub { color:var(--muted); margin-top:4px; }
  .badge { display:inline-flex; align-items:center; gap:10px; padding:10px 16px; border-radius:999px; font-weight:800; font-size:16px; }
  .badge.ok { background:var(--ok); color:#fff; } .badge.no { background:#fff; color:var(--bad); border:2px solid var(--bad); }
  .stats { display:flex; gap:12px; flex-wrap:wrap; padding:8px 32px 0; }
  .stat { background:#fff; border:1px solid var(--line); border-radius:12px; padding:12px 16px; min-width:150px; }
  .stat b { display:block; font-size:22px; }
  .timeline { display:flex; gap:14px; align-items:flex-end; padding:16px 32px 0; }
  .tl-round { text-align:center; font-size:12px; color:var(--muted); }
  .tl-bar { width:34px; height:70px; background:#e9ecef; border-radius:6px; display:flex; align-items:flex-end; overflow:hidden; margin:0 auto 4px; }
  .tl-fill { width:100%; background:#e0a33a; } .tl-fill.ok { background:var(--ok); }
  .tl-label { font-weight:700; color:var(--ink); } .tl-scope { font-size:11px; }
  main { padding:20px 32px 40px; overflow-x:auto; }
  table { border-collapse:separate; border-spacing:8px; min-width:720px; }
  th[scope=col] { text-align:left; font-size:13px; color:var(--muted); padding:0 4px; }
  th[scope=row] { text-align:left; vertical-align:top; padding:10px 12px; background:#fff; border:1px solid var(--line); border-radius:10px; min-width:190px; }
  .pname { font-weight:700; } .pmeta { color:var(--muted); font-size:12px; }
  td { vertical-align:top; background:#fff; border:1px solid var(--line); border-radius:10px; padding:10px 12px; width:280px; }
  td.pass { background:var(--ok-bg); border-color:#bfe3cc; } td.fail { background:var(--bad-bg); border-color:#f3c2bd; } td.error { background:var(--err-bg); border-color:#f0dc9a; }
  .verdict { font-weight:800; } td.pass .verdict { color:var(--ok); } td.fail .verdict { color:var(--bad); } td.error .verdict { color:var(--err); }
  .hist { display:flex; gap:4px; margin:6px 0; flex-wrap:wrap; }
  .pill { font-size:11px; font-weight:700; padding:1px 6px; border-radius:999px; background:#fff; border:1px solid var(--line); }
  .pill.pass { color:var(--ok); border-color:#9fd3b3; } .pill.fail { color:var(--bad); border-color:#efa59d; } .pill.error { color:var(--err); }
  .by { font-size:11px; font-weight:700; text-transform:uppercase; color:#fff; background:#6b4fbb; border-radius:4px; padding:1px 5px; margin-right:4px; }
  .by.layout { background:#0b7285; } .by.bug { background:#b3261e; }
  .msg { margin-top:4px; font-size:13px; }
  details { margin-top:6px; font-size:12px; } summary { cursor:pointer; color:var(--muted); }
  details ul { padding-left:18px; margin:6px 0; } code { font-size:11.5px; background:rgba(0,0,0,.05); padding:0 3px; border-radius:3px; word-break:break-all; }
  .links { margin-top:6px; font-size:12px; } .links a { color:#2457c5; margin-right:8px; }
  footer { color:var(--muted); font-size:12px; padding:0 32px 32px; }
</style></head>
<body>
<header>
  <div><h1>AspectProof report</h1><div class="sub">${esc(config.app)} · ${config.profiles.length} screen profiles × ${config.flows.length} user flows · every check run by Kane CLI</div></div>
  <div class="badge ${verified ? 'ok' : 'no'}">${verified ? '✓ AspectProof verified' : `${passed}/${total} checks passing`}</div>
</header>
<section class="stats">
  <div class="stat"><b>${passed}/${total}</b>passing now</div>
  <div class="stat"><b>${firstFull ? `${firstFull.ran - firstFull.passed}` : '–'}</b>failing in first full run</div>
  <div class="stat"><b>${caught.fixed}</b>fixed by the agent and re-verified</div>
  <div class="stat"><b>${state.rounds.length}</b>verification rounds</div>
</section>
<section class="timeline" aria-label="Rounds">${timeline}</section>
<main><table><thead><tr><th></th>${head}</tr></thead><tbody>${rows}</tbody></table></main>
<footer>Generated ${esc(new Date().toISOString())} by AspectProof. Kane CLI drives a real Chrome browser; phone and tablet-portrait sizes run inside the AspectProof device frame because Kane's window minimum is 800×600. The layout probe runs inside the same browser as Kane.</footer>
</body></html>`;
}

function renderCell(c) {
  if (!c) return '<td><span class="verdict" style="color:#8a94a3">not run</span></td>';
  const hist = (c.history || []).map((h) => `<span class="pill ${h.verdict}">R${h.round} ${h.verdict === 'pass' ? '✓' : h.verdict === 'fail' ? '✗' : '!'}</span>`).join('');
  const by = (c.failedBy || []).map((b) => `<span class="by ${b}">${b === 'kane' ? 'Kane' : 'Layout'}</span>`).join('')
    + (c.verdict !== 'pass' && c.kane?.bugVerdict?.confirmed ? `<span class="by bug">${esc(c.kane.bugVerdict.severity || 'confirmed')} bug</span>` : '');
  let msg = '';
  if (c.verdict === 'pass') msg = esc(c.kane.oneLiner || 'Flow completed and layout clean.');
  else if (c.verdict === 'error') msg = esc((c.kane.errors || [])[0] || c.kane.stderrTail || 'Kane could not run this check');
  else msg = esc(c.kane.exitCode !== 0 ? (c.kane.oneLiner || c.kane.reason || 'Flow failed') : 'Flow completed, but the layout is broken');
  const issues = c.layout?.issues?.length
    ? `<details><summary>${c.layout.issues.length} layout issue${c.layout.issues.length === 1 ? '' : 's'}</summary><ul>${c.layout.issues.map((i) => `<li><b>${esc(i.kind)}</b> <code>${esc(i.selector)}</code> ${esc(i.text ? `"${i.text}"` : '')} ${esc(i.detail)}</li>`).join('')}</ul></details>` : '';
  const steps = c.verdict !== 'pass' && c.kane?.steps?.length
    ? `<details><summary>Kane's last steps</summary><ul>${c.kane.steps.slice(-5).map((s) => `<li>[${esc(s.status)}] ${esc(s.remark)}</li>`).join('')}</ul></details>` : '';
  const links = [c.kane?.testUrl && `<a href="${esc(c.kane.testUrl)}" target="_blank" rel="noopener">Kane run ↗</a>`, `<a href="${esc(String(c.log).replace(STATE_DIR + '/', ''))}">NDJSON log</a>`].filter(Boolean).join('');
  return `<td class="${c.verdict}"><div class="verdict">${c.verdict === 'pass' ? '✓ Pass' : c.verdict === 'fail' ? '✗ Fail' : '! Error'} ${by}</div><div class="hist">${hist}</div><div class="msg">${msg}</div>${issues}${steps}<div class="links">${links}</div></td>`;
}

export async function writeReport(config, state) {
  const dir = join(config.cwd, STATE_DIR);
  await mkdir(dir, { recursive: true });
  await writeFile(join(dir, 'report.html'), renderReport(config, state));
  return join(STATE_DIR, 'report.html');
}
