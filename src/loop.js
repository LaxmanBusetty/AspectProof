// The closed loop, two ways:
//  1. Claude Code Stop hook: when the agent tries to finish, AspectProof runs Kane; if anything fails,
//     the hook blocks the stop and hands Kane's findings back to the agent, which fixes and tries again.
//  2. `aspectproof loop --agent <claude|codex|cmd>`: AspectProof drives a headless agent itself.
import { spawn, execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { writeFile, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { verify, loadState, saveState } from './verify.js';
import { STATE_DIR } from './config.js';

function fingerprint(cwd) {
  try {
    const diff = execFileSync('git', ['diff', 'HEAD', '--', '.', `:(exclude)${STATE_DIR}`], { cwd, encoding: 'utf8', maxBuffer: 64 << 20, stdio: ['ignore', 'pipe', 'ignore'] });
    const untracked = execFileSync('git', ['ls-files', '--others', '--exclude-standard'], { cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] });
    return createHash('sha256').update(diff).update(untracked).digest('hex');
  } catch { return null; }
}

/** One verification pass with "retest failures, then full sweep on green". */
async function verifyCycle(config, { log, reason }) {
  const state = await loadState(config.cwd);
  const hasFailures = Object.values(state.cells).some((c) => c.verdict !== 'pass');
  let res = await verify(config, { only: hasFailures ? 'failed' : undefined, log, reason });
  if (res.ok && hasFailures && config.loop.fullSweepOnGreen) {
    log('AspectProof: failing checks now pass. Running the full matrix to catch regressions.');
    res = await verify(config, { log, reason: 'regression sweep' });
  }
  return res;
}

export async function claudeStopHook(config) {
  let input = {};
  try {
    let raw = '';
    for await (const chunk of process.stdin) raw += chunk;
    input = raw ? JSON.parse(raw) : {};
  } catch { /* not fatal */ }
  const log = (s) => process.stderr.write(s + '\n'); // stdout is reserved for the hook's JSON answer
  const out = (obj) => process.stdout.write(JSON.stringify(obj));
  const cwd = config.cwd;

  const state = await loadState(cwd);
  const fp = fingerprint(cwd);
  if (fp && fp === state.lastGreenFingerprint) {
    return out({ systemMessage: 'AspectProof: no changes since the last green run. Skipping verification.' });
  }

  let res;
  try {
    res = await verifyCycle(config, { log, reason: 'Claude Code Stop hook' });
  } catch (err) {
    // Never trap the agent because of an environment problem; report it instead.
    return out({ systemMessage: `AspectProof could not verify: ${err.message}` });
  }

  const fresh = await loadState(cwd);
  if (res.ok) {
    fresh.loop = { rounds: 0 };
    fresh.lastGreenFingerprint = fingerprint(cwd);
    await saveState(cwd, fresh);
    return out({ systemMessage: `AspectProof verified ✓ ${res.summary.matrixPassed}/${res.summary.matrixTotal} checks pass across ${config.profiles.length} screen sizes. Report: ${res.reportPath}` });
  }

  fresh.loop = { rounds: (fresh.loop?.rounds || 0) + 1 };
  await saveState(cwd, fresh);
  if (fresh.loop.rounds > config.loop.maxRounds) {
    fresh.loop = { rounds: 0 };
    await saveState(cwd, fresh);
    return out({ systemMessage: `AspectProof: still failing after ${config.loop.maxRounds} fix rounds; letting you stop. See ${res.feedbackPath} and ${res.reportPath}.` });
  }
  const feedback = await readFile(join(cwd, res.feedbackPath), 'utf8');
  return out({
    decision: 'block',
    reason: `${feedback}\n\n(AspectProof fix round ${fresh.loop.rounds} of ${config.loop.maxRounds}. Fix the issues above; AspectProof re-verifies when you stop.)`,
  });
}

const PRESETS = {
  claude: (prompt) => ['claude', ['-p', prompt, '--permission-mode', 'acceptEdits']],
  codex: (prompt) => ['codex', ['exec', '--full-auto', prompt]],
};

export async function runLoop(config, { agent = 'claude', maxRounds } = {}) {
  const log = (s) => process.stdout.write(s + '\n');
  const rounds = maxRounds || config.loop.maxRounds;
  log(`AspectProof loop: agent = ${agent}, up to ${rounds} fix rounds.`);
  let res = await verify(config, { log, reason: 'loop start' });
  for (let i = 1; !res.ok && i <= rounds; i++) {
    const feedback = await readFile(join(config.cwd, res.feedbackPath), 'utf8');
    const prompt = `${feedback}\n\nFix these issues in the app now. Do not run AspectProof yourself; it re-verifies after you finish.`;
    const promptFile = join(config.cwd, STATE_DIR, 'agent-prompt.md');
    await writeFile(promptFile, prompt);
    log(`\n── Fix round ${i}: handing ${res.results.filter((r) => r.verdict !== 'pass').length} failing checks to ${agent} ──`);
    await runAgent(agent, prompt, promptFile, config.cwd);
    log(`── ${agent} finished. Re-verifying with Kane. ──\n`);
    res = await verifyCycle(config, { log, reason: `after fix round ${i}` });
  }
  log(res.ok ? `\nAspectProof verified ✓ ${res.summary.matrixPassed}/${res.summary.matrixTotal}. Report: ${res.reportPath}` : `\nStill failing after ${rounds} rounds. Report: ${res.reportPath}`);
  return res.ok;
}

function runAgent(agent, prompt, promptFile, cwd) {
  return new Promise((resolve, reject) => {
    let cmd; let args; let shell = false;
    if (PRESETS[agent]) [cmd, args] = PRESETS[agent](prompt);
    else {
      // Custom command: {prompt_file} is replaced with the path of a file holding the prompt.
      cmd = agent.includes('{prompt_file}') ? agent.replaceAll('{prompt_file}', JSON.stringify(promptFile)) : `${agent} < ${JSON.stringify(promptFile)}`;
      args = []; shell = true;
    }
    const child = spawn(cmd, args, { cwd, stdio: ['ignore', 'inherit', 'inherit'], shell });
    child.on('error', (err) => reject(new Error(`Could not start agent "${agent}": ${err.message}`)));
    child.on('close', (code) => (code === 0 ? resolve() : reject(new Error(`Agent "${agent}" exited with code ${code}`))));
  });
}
