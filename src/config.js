import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';

export const STATE_DIR = '.aspectproof';

export async function loadConfig(cwd = process.cwd(), file = 'aspectproof.config.json') {
  const path = resolve(cwd, file);
  let raw;
  try { raw = await readFile(path, 'utf8'); } catch {
    throw new Error(`No ${file} in ${cwd}. Run "aspectproof init" first.`);
  }
  const config = JSON.parse(raw);
  config.harnessPort ||= 4400;
  config.frameWindow ||= '1280x800';
  config.kane = { command: 'kane-cli', headless: true, maxSteps: 30, timeoutSeconds: 300, concurrency: 1, extraArgs: [], ...(config.kane || {}) };
  config.loop = { maxRounds: 4, fullSweepOnGreen: true, ...(config.loop || {}) };
  if (!config.app) throw new Error('aspectproof.config.json needs "app": the URL of your running app, e.g. http://localhost:3000');
  if (!Array.isArray(config.profiles) || !config.profiles.length) throw new Error('aspectproof.config.json needs at least one profile');
  if (!Array.isArray(config.flows) || !config.flows.length) throw new Error('aspectproof.config.json needs at least one flow');
  for (const p of config.profiles) {
    if (p.mode === 'window') checkWindow(`${p.width}x${p.height}`, `profile "${p.id}"`);
  }
  checkWindow(config.frameWindow, 'frameWindow');
  config.cwd = cwd;
  return config;
}

// Kane CLI's Chrome window must be 800–3840 wide and 600–2160 tall.
export function checkWindow(size, where) {
  const [w, h] = String(size).split('x').map(Number);
  if (!(w >= 800 && w <= 3840 && h >= 600 && h <= 2160)) {
    throw new Error(`${where}: window ${size} is outside Kane CLI's supported range (800–3840 × 600–2160). Use mode "frame" for smaller screens.`);
  }
}

export function windowFor(profile, config) {
  return profile.mode === 'window' ? `${profile.width}x${profile.height}` : config.frameWindow;
}

export const cellKey = (profileId, flowId) => `${profileId}__${flowId}`;
