// Thin wrapper around `kane-cli run ... --agent`, which streams NDJSON events on stdout.
// Event contract (v1): stream_start, step lines {step,status,remark}, warning, error, run_end.
import { spawn } from 'node:child_process';
import { createWriteStream } from 'node:fs';

export function kaneExec(config, args, { logPath, onEvent } = {}) {
  return new Promise((resolve, reject) => {
    const child = spawn(config.kane.command, args, { cwd: config.cwd, stdio: ['ignore', 'pipe', 'pipe'], env: process.env });
    const log = logPath ? createWriteStream(logPath) : null;
    const events = [];
    let buf = '';
    let stderr = '';
    child.stdout.on('data', (chunk) => {
      log?.write(chunk);
      buf += chunk;
      let i;
      while ((i = buf.indexOf('\n')) >= 0) {
        const line = buf.slice(0, i).trim();
        buf = buf.slice(i + 1);
        if (!line) continue;
        try { const ev = JSON.parse(line); events.push(ev); onEvent?.(ev); } catch { events.push({ type: 'text', text: line }); }
      }
    });
    child.stderr.on('data', (c) => { stderr += c; if (stderr.length > 20000) stderr = stderr.slice(-20000); });
    child.on('error', (err) => {
      log?.end();
      if (err.code === 'ENOENT') reject(new Error(`"${config.kane.command}" was not found. Install it with: npm install -g @testmuai/kane-cli, then run: kane-cli login`));
      else reject(err);
    });
    child.on('close', (code) => {
      if (buf.trim()) { try { events.push(JSON.parse(buf)); } catch { events.push({ type: 'text', text: buf.trim() }); } }
      log?.end();
      resolve({ exitCode: code, events, stderr });
    });
  });
}

export async function setWindow(config, size) {
  const { exitCode, stderr, events } = await kaneExec(config, ['config', 'set-window', size]);
  if (exitCode !== 0) {
    const msg = stderr.trim() || events.map((e) => e.text || e.message).filter(Boolean).join(' ');
    throw new Error(`kane-cli config set-window ${size} failed (exit ${exitCode}): ${msg}`);
  }
}

export async function runKane(config, { objective, url, name, logPath, onEvent }) {
  const k = config.kane;
  const args = ['run', objective, '--url', url, '--agent', '--max-steps', String(k.maxSteps), '--timeout', String(k.timeoutSeconds)];
  if (name) args.push('--name', name.replace(/[^a-zA-Z0-9_-]/g, '-'));
  if (k.headless) args.push('--headless');
  args.push(...(k.extraArgs || []));
  const started = Date.now();
  const { exitCode, events, stderr } = await kaneExec(config, args, { logPath, onEvent });
  return summarize(exitCode, events, stderr, Date.now() - started);
}

export function summarize(exitCode, events, stderr, elapsedMs) {
  const runEnd = [...events].reverse().find((e) => e.type === 'run_end') || null;
  const steps = events.filter((e) => e.type === undefined && 'step' in e);
  // Keep the final status of each step number.
  const byStep = new Map();
  for (const s of steps) byStep.set(s.step, s);
  const errors = events.filter((e) => e.type === 'error').map((e) => e.message);
  const warnings = events.filter((e) => e.type === 'warning').map((e) => e.message);
  const status = runEnd?.status || (exitCode === 0 ? 'passed' : 'failed');
  return {
    exitCode,
    status,
    started: exitCode !== 2,
    timedOut: exitCode === 3,
    oneLiner: runEnd?.one_liner || null,
    summary: runEnd?.summary || null,
    reason: runEnd?.reason || null,
    resultCode: runEnd?.result_code ?? null,
    finalState: runEnd?.final_state || null,
    testUrl: runEnd?.test_url || null,
    sessionDir: runEnd?.session_dir || null,
    durationS: runEnd?.duration ?? Math.round(elapsedMs / 100) / 10,
    credits: runEnd?.credits_consumed ?? runEnd?.credits ?? null,
    steps: [...byStep.values()].map((s) => ({ step: s.step, status: s.status, remark: s.remark })),
    errors,
    warnings,
    stderrTail: exitCode === 0 ? '' : stderr.trim().split('\n').slice(-8).join('\n'),
  };
}
