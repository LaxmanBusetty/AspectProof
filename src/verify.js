// Runs the profile × flow matrix through Kane CLI and the layout probe, and records the results.
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { createHarness } from './harness.js';
import { runKane, setWindow } from './kane.js';
import { STATE_DIR, cellKey, windowFor } from './config.js';
import { writeFeedback } from './feedback.js';
import { writeReport } from './report.js';

export async function loadState(cwd) {
  try { return JSON.parse(await readFile(join(cwd, STATE_DIR, 'state.json'), 'utf8')); }
  catch { return { round: 0, cells: {}, rounds: [], loop: { rounds: 0 }, lastGreenFingerprint: null }; }
}

export async function saveState(cwd, state) {
  await mkdir(join(cwd, STATE_DIR), { recursive: true });
  await writeFile(join(cwd, STATE_DIR, 'state.json'), JSON.stringify(state, null, 2));
}

export function buildObjective(profile, flow) {
  const framed = profile.mode !== 'window';
  return [
    `You are testing a web app inside the AspectProof harness, which shows the app at "${profile.label}".`,
    framed
      ? 'The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.'
      : 'The app fills the window below a thin "AspectProof layout" status bar at the top.',
    'Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.',
    '',
    `Task: ${flow.objective}`,
    '',
    'Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.',
    'The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.',
  ].join('\n');
}

/**
 * @param {object} config
 * @param {{ only?: 'failed', profiles?: string[], flows?: string[], log?: (s: string) => void, reason?: string }} opts
 */
export async function verify(config, opts = {}) {
  const log = opts.log || ((s) => process.stdout.write(s + '\n'));
  const cwd = config.cwd;
  const state = await loadState(cwd);

  let cells = [];
  for (const profile of config.profiles) {
    if (opts.profiles?.length && !opts.profiles.includes(profile.id)) continue;
    for (const flow of config.flows) {
      if (opts.flows?.length && !opts.flows.includes(flow.id)) continue;
      cells.push({ profile, flow, key: cellKey(profile.id, flow.id) });
    }
  }
  if (opts.only === 'failed') {
    const prev = cells.filter((c) => state.cells[c.key] && state.cells[c.key].verdict !== 'pass');
    if (!prev.length && Object.keys(state.cells).length) {
      log('AspectProof: no failing checks from the last run; running the full matrix instead.');
    } else if (prev.length) cells = prev;
  }

  await assertAppUp(config);
  const round = state.round + 1;
  const roundDir = join(cwd, STATE_DIR, 'rounds', String(round));
  await mkdir(join(roundDir, 'logs'), { recursive: true });

  const harness = createHarness(config);
  try { await harness.listen(); } catch (err) {
    if (err.code === 'EADDRINUSE') throw new Error(`Port ${config.harnessPort} is busy. Stop "aspectproof serve" (or change harnessPort) before running verify.`);
    throw err;
  }

  log(`AspectProof round ${round}: ${cells.length} check${cells.length === 1 ? '' : 's'} (${opts.only === 'failed' ? 'previously failing' : (opts.profiles?.length || opts.flows?.length) ? 'selected' : 'full matrix'})${opts.reason ? ` · ${opts.reason}` : ''}`);
  const results = [];
  const started = Date.now();
  try {
    // Group by Chrome window size: Kane's window is a saved setting, so each size runs as a batch.
    const groups = new Map();
    for (const c of cells) {
      const size = windowFor(c.profile, config);
      if (!groups.has(size)) groups.set(size, []);
      groups.get(size).push(c);
    }
    for (const [size, group] of groups) {
      await setWindow(config, size);
      await pool(group, Math.max(1, config.kane.concurrency || 1), async (c) => {
        const r = await runCell(config, harness, c, round, roundDir);
        results.push(r);
        log(`  ${icon(r.verdict)} ${c.profile.id.padEnd(18)} × ${c.flow.id.padEnd(10)} ${describeVerdict(r)}`);
      });
    }
  } finally {
    await harness.close();
  }

  for (const r of results) {
    const prev = state.cells[r.key];
    state.cells[r.key] = { ...r, history: [...(prev?.history || []), { round, verdict: r.verdict }] };
  }
  const all = Object.values(state.cells);
  const summary = {
    round,
    at: new Date().toISOString(),
    scope: opts.only === 'failed' ? 'failed' : (opts.profiles?.length || opts.flows?.length) ? 'selected' : 'full',
    reason: opts.reason || null,
    ran: results.length,
    passed: results.filter((r) => r.verdict === 'pass').length,
    matrixPassed: all.filter((c) => c.verdict === 'pass').length,
    matrixTotal: config.profiles.length * config.flows.length,
    seconds: Math.round((Date.now() - started) / 1000),
  };
  state.round = round;
  state.rounds.push(summary);
  await writeFile(join(roundDir, 'results.json'), JSON.stringify({ summary, results }, null, 2));
  await saveState(cwd, state);
  const feedbackPath = await writeFeedback(config, state, results);
  const reportPath = await writeReport(config, state);

  const failing = results.filter((r) => r.verdict !== 'pass');
  log(`AspectProof round ${round}: ${summary.passed}/${summary.ran} passed this round · matrix ${summary.matrixPassed}/${summary.matrixTotal} · ${summary.seconds}s`);
  log(`  report:   ${reportPath}`);
  if (failing.length) log(`  feedback: ${feedbackPath}`);
  return { ok: failing.length === 0, round, results, summary, state, feedbackPath, reportPath };
}

async function runCell(config, harness, { profile, flow, key }, round, roundDir) {
  const runId = `r${round}-${key}`;
  harness.reports.delete(runId);
  const url = harness.frameUrl(profile.id, runId, flow.start || '/');
  let kane;
  try {
    kane = await runKane(config, {
      objective: buildObjective(profile, flow),
      url,
      name: `aspectproof-${runId}`,
      logPath: join(roundDir, 'logs', `${key}.ndjson`),
    });
  } catch (err) {
    kane = { exitCode: -1, status: 'error', started: false, errors: [String(err.message || err)], steps: [] };
  }
  const probe = harness.reports.get(runId) || null;
  const layout = {
    issues: probe?.issuesSeen || [],
    warnings: probe?.warnings || [],
    probeError: probe ? probe.probeError : 'The layout probe never reported. Kane may not have loaded the harness page.',
    scans: probe?.scans || 0,
    lastUrl: probe?.url || null,
  };
  let verdict;
  if (!kane.started || kane.exitCode === -1) verdict = 'error';
  else if (kane.exitCode === 0 && layout.issues.length === 0 && !layout.probeError) verdict = 'pass';
  else verdict = 'fail';
  const failedBy = [];
  if (verdict === 'fail' && kane.exitCode !== 0) failedBy.push('kane');
  if (layout.issues.length) failedBy.push('layout');
  return {
    key, round, verdict, failedBy,
    profile: { id: profile.id, label: profile.label, width: profile.width, height: profile.height, mode: profile.mode },
    flow: { id: flow.id, name: flow.name, objective: flow.objective },
    kane, layout,
    harnessUrl: url,
    log: join(STATE_DIR, 'rounds', String(round), 'logs', `${key}.ndjson`),
  };
}

async function assertAppUp(config) {
  try {
    const res = await fetch(config.app, { signal: AbortSignal.timeout(5000) });
    if (res.status >= 500) throw new Error(`HTTP ${res.status}`);
  } catch (err) {
    const e = new Error(`The app at ${config.app} is not reachable (${err.cause?.code || err.message}). Start it first (for the demo: npm run demo).`);
    e.code = 'APP_DOWN';
    throw e;
  }
}

async function pool(items, size, fn) {
  const queue = [...items];
  await Promise.all(Array.from({ length: Math.min(size, queue.length) }, async () => {
    while (queue.length) await fn(queue.shift());
  }));
}

const icon = (v) => (v === 'pass' ? '✓' : v === 'fail' ? '✗' : '!');
function describeVerdict(r) {
  if (r.verdict === 'pass') return `passed (${r.kane.durationS ?? '?'}s)`;
  if (r.verdict === 'error') return `error: ${(r.kane.errors || [])[0] || r.kane.stderrTail || `kane exit ${r.kane.exitCode}`}`;
  const parts = [];
  if (r.failedBy.includes('kane')) parts.push(`Kane: ${r.kane.oneLiner || r.kane.reason || 'flow failed'}`);
  if (r.layout.issues.length) parts.push(`${r.layout.issues.length} layout issue${r.layout.issues.length === 1 ? '' : 's'}`);
  if (r.layout.probeError && !r.layout.issues.length) parts.push('probe did not report');
  return parts.join(' · ');
}
