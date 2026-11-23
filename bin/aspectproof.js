#!/usr/bin/env node
// AspectProof: prove your product works at every screen size. Every check is a Kane CLI run.
import { readFile, writeFile, mkdir, access } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';
import { loadConfig } from '../src/config.js';
import { createHarness } from '../src/harness.js';
import { verify, loadState } from '../src/verify.js';
import { writeReport } from '../src/report.js';
import { claudeStopHook, runLoop } from '../src/loop.js';
import { watch } from '../src/watch.js';

const pkgRoot = join(dirname(fileURLToPath(import.meta.url)), '..');
const [cmd, ...rest] = process.argv.slice(2);
const flags = parseFlags(rest);

const HELP = `AspectProof: prove your product works at every screen size, with Kane CLI.

Usage:
  aspectproof init [--app http://localhost:3000] [--claude]   create config (and Claude Code Stop hook)
  aspectproof serve                      open the device frames yourself (prints a URL per profile)
  aspectproof verify [--only failed] [--profiles a,b] [--flows x,y] [--headed] [--live]
                                         run every profile × flow through Kane CLI + layout probe
  aspectproof loop [--agent claude|codex|"<cmd {prompt_file}>"] [--rounds N]
                                         verify → hand failures to a coding agent → re-verify, until green
  aspectproof watch                      follow Kane's steps live (e.g. while the Claude hook runs)
  aspectproof report [--open]            rebuild .aspectproof/report.html
  aspectproof hook claude-stop           (used by the Claude Code Stop hook)

Exit code: 0 when every check passes, 1 when any fails, 2 on setup errors.`;

try {
  switch (cmd) {
    case 'init': await init(); break;
    case 'serve': await serve(); break;
    case 'verify': {
      const config = applyViewFlags(await loadConfig());
      const res = await verify(config, { only: flags.only, profiles: list(flags.profiles), flows: list(flags.flows), live: Boolean(flags.live) });
      process.exitCode = res.ok ? 0 : 1;
      break;
    }
    case 'loop': {
      const config = applyViewFlags(await loadConfig());
      const ok = await runLoop(config, { agent: flags.agent || 'claude', maxRounds: flags.rounds ? Number(flags.rounds) : undefined });
      process.exitCode = ok ? 0 : 1;
      break;
    }
    case 'watch': await watch(await loadConfig()); break;
    case 'report': {
      const config = await loadConfig();
      const path = await writeReport(config, await loadState(config.cwd));
      console.log(path);
      if (flags.open) spawn(process.platform === 'darwin' ? 'open' : 'xdg-open', [path], { stdio: 'ignore', detached: true }).unref();
      break;
    }
    case 'hook': {
      if (rest[0] !== 'claude-stop') throw new Error('Unknown hook. Supported: claude-stop');
      const config = await loadConfig(process.env.CLAUDE_PROJECT_DIR || process.cwd());
      await claudeStopHook(config);
      break;
    }
    case undefined: case '-h': case '--help': case 'help':
      console.log(HELP); break;
    default:
      console.error(`Unknown command "${cmd}".\n\n${HELP}`); process.exitCode = 2;
  }
} catch (err) {
  console.error(`AspectProof: ${err.message}`);
  process.exitCode = 2;
}

async function serve() {
  const config = await loadConfig();
  const harness = createHarness(config);
  await harness.listen();
  console.log(`AspectProof harness on ${harness.origin}, proxying ${config.app}\n`);
  for (const p of config.profiles) console.log(`  ${p.id.padEnd(18)} ${harness.frameUrl(p.id, 'manual', config.flows[0]?.start || '/')}`);
  console.log('\nOpen a URL above in Chrome to see the app and the layout panel at that size. Ctrl+C to stop.');
}

async function init() {
  const cwd = process.cwd();
  const cfgPath = join(cwd, 'aspectproof.config.json');
  if (await exists(cfgPath)) {
    console.log('aspectproof.config.json already exists; leaving it as is.');
  } else {
    const template = JSON.parse(await readFile(join(pkgRoot, 'aspectproof.config.json'), 'utf8'));
    if (flags.app) template.app = flags.app;
    await writeFile(cfgPath, JSON.stringify(template, null, 2) + '\n');
    console.log(`Created aspectproof.config.json (app: ${template.app}). Edit "flows" to describe your app's key user journeys in plain English.`);
  }
  const gi = join(cwd, '.gitignore');
  const giText = (await exists(gi)) ? await readFile(gi, 'utf8') : '';
  if (!giText.split('\n').some((l) => l.trim() === '.aspectproof/')) {
    await writeFile(gi, `${giText}${giText && !giText.endsWith('\n') ? '\n' : ''}.aspectproof/\n.testmuai/evidence/\n`);
    console.log('Added .aspectproof/ to .gitignore.');
  }
  if (flags.claude) {
    const dir = join(cwd, '.claude');
    await mkdir(dir, { recursive: true });
    const sp = join(dir, 'settings.json');
    const settings = (await exists(sp)) ? JSON.parse(await readFile(sp, 'utf8')) : {};
    settings.hooks ||= {};
    settings.hooks.Stop ||= [];
    const command = 'npx --no-install aspectproof hook claude-stop';
    const already = JSON.stringify(settings.hooks.Stop).includes('aspectproof hook claude-stop');
    if (!already) settings.hooks.Stop.push({ hooks: [{ type: 'command', command, timeout: 3600 }] });
    await writeFile(sp, JSON.stringify(settings, null, 2) + '\n');
    console.log(already ? 'Claude Code Stop hook already installed.' : 'Installed the Claude Code Stop hook in .claude/settings.json.');
  }
}

// --headed shows Kane's Chrome window; --live prints Kane's steps as they happen.
function applyViewFlags(config) {
  if (flags.headed) config.kane.headless = false;
  if (flags.live) config.live = true;
  return config;
}

function parseFlags(args) {
  const out = {};
  for (let i = 0; i < args.length; i++) {
    const a = args[i];
    if (!a.startsWith('--')) continue;
    const [k, v] = a.slice(2).split('=');
    if (v !== undefined) out[k] = v;
    else if (args[i + 1] && !args[i + 1].startsWith('--')) out[k] = args[++i];
    else out[k] = true;
  }
  return out;
}
function list(v) { return typeof v === 'string' ? v.split(',').map((s) => s.trim()).filter(Boolean) : undefined; }
async function exists(p) { try { await access(p); return true; } catch { return false; } }
