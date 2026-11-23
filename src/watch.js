// `aspectproof watch`: follow Kane's NDJSON streams live, across rounds. Handy next to the agent
// while the Stop hook runs (Claude's window is quiet then), and for recording demos.
import { readdir, stat, open } from 'node:fs/promises';
import { join } from 'node:path';
import { STATE_DIR } from './config.js';

const c = (code, s) => (process.stdout.isTTY ? `\x1b[${code}m${s}\x1b[0m` : s);
const green = (s) => c('32', s); const red = (s) => c('31', s); const dim = (s) => c('2', s); const bold = (s) => c('1', s);

export async function watch(config) {
  const root = join(config.cwd, STATE_DIR, 'rounds');
  const offsets = new Map(); // file -> bytes read
  const partial = new Map();
  console.log(bold('AspectProof watch: following Kane CLI runs live (Ctrl+C to stop)\n'));
  // Skip what already exists, so only new activity shows.
  for (const f of await listLogs(root)) offsets.set(f, (await stat(f)).size);
  for (;;) {
    for (const f of await listLogs(root)) {
      const size = (await stat(f)).size;
      const from = offsets.get(f) ?? 0;
      if (!offsets.has(f)) {
        const [, round, name] = f.match(/rounds\/(\d+)\/logs\/(.+)\.ndjson$/) || [];
        const [profile, flow] = (name || '').split('__');
        console.log(`\n${bold(`▶ Round ${round} · ${profile} × ${flow}`)}  ${dim('Kane CLI started')}`);
      }
      if (size > from) {
        const fh = await open(f, 'r');
        const buf = Buffer.alloc(size - from);
        await fh.read(buf, 0, buf.length, from);
        await fh.close();
        offsets.set(f, size);
        const text = (partial.get(f) || '') + buf.toString('utf8');
        const lines = text.split('\n');
        partial.set(f, lines.pop());
        for (const line of lines) printEvent(line);
      } else if (!offsets.has(f)) offsets.set(f, 0);
    }
    await new Promise((r) => setTimeout(r, 700));
  }
}

function printEvent(line) {
  let ev; try { ev = JSON.parse(line); } catch { return; }
  if (ev.type === undefined && ev.remark && ev.status && ev.status !== 'running') {
    const mark = ev.status === 'failed' ? red('✗') : green('·');
    console.log(`  ${mark} ${String(ev.remark).replace(/^agent_info: /, '').slice(0, 160)}`);
  } else if (ev.type === 'run_end') {
    const ok = ev.status === 'passed';
    const bug = ev.verdict?.confirmed ? red(` [Kane: confirmed ${ev.verdict.severity || ''} bug]`) : '';
    console.log(`  ${ok ? green('✓ PASSED') : red('✗ FAILED')} ${ev.one_liner || ev.reason || ''}${bug} ${dim(`(${ev.duration ?? '?'}s)`)}`);
  } else if (ev.type === 'error') {
    console.log(`  ${red('! error')} ${ev.message}`);
  }
}

async function listLogs(root) {
  const out = [];
  let rounds = [];
  try { rounds = await readdir(root); } catch { return out; }
  for (const r of rounds.sort((a, b) => a - b)) {
    let files = [];
    try { files = await readdir(join(root, r, 'logs')); } catch { continue; }
    for (const f of files) if (f.endsWith('.ndjson')) out.push(join(root, r, 'logs', f));
  }
  return out;
}
