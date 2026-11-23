// AspectProof harness server.
//
// Serves the device-frame page at /__ap/frame and proxies every other path to the app
// under test, so the frame page and the app share one origin. That lets the layout probe
// (running in the frame page, inside Kane's browser) measure the app's DOM directly.
import http from 'node:http';
import https from 'node:https';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const assetsDir = fileURLToPath(new URL('./harness-assets/', import.meta.url));
const assetTypes = { 'frame.js': 'text/javascript', 'frame.css': 'text/css' };

export function createHarness(config) {
  const app = new URL(config.app);
  const reports = new Map(); // runId -> latest probe report
  const profiles = new Map(config.profiles.map((p) => [p.id, p]));

  const server = http.createServer(async (req, res) => {
    const url = new URL(req.url, 'http://harness');
    try {
      if (url.pathname === '/__ap/frame') return await serveFrame(url, res);
      if (url.pathname.startsWith('/__ap/assets/')) return await serveAsset(url.pathname.slice('/__ap/assets/'.length), res);
      if (url.pathname === '/__ap/report' && req.method === 'POST') return await receiveReport(url, req, res);
      if (url.pathname === '/__ap/health') return json(res, 200, { ok: true, app: config.app });
      return proxy(req, res);
    } catch (err) {
      json(res, 500, { error: String(err && err.message || err) });
    }
  });

  async function serveFrame(url, res) {
    const profile = profiles.get(url.searchParams.get('profile'));
    if (!profile) return json(res, 404, { error: 'unknown profile', known: [...profiles.keys()] });
    const runId = url.searchParams.get('run') || 'manual';
    const start = url.searchParams.get('start') || '/';
    if (!start.startsWith('/') || start.startsWith('//')) return json(res, 400, { error: 'start must be a path on the app' });
    const template = await readFile(assetsDir + 'frame.html', 'utf8');
    const boot = JSON.stringify({ profile, runId, start }).replace(/</g, '\\u003c');
    const html = template
      .replace('/*__AP_BOOT__*/null', boot)
      .replaceAll('__AP_TITLE__', escapeHtml(`AspectProof · ${profile.label}`));
    res.writeHead(200, { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' });
    res.end(html);
  }

  async function serveAsset(name, res) {
    if (!assetTypes[name]) return json(res, 404, { error: 'not found' });
    const body = await readFile(assetsDir + name);
    res.writeHead(200, { 'content-type': assetTypes[name], 'cache-control': 'no-store' });
    res.end(body);
  }

  async function receiveReport(url, req, res) {
    const runId = url.searchParams.get('run') || 'manual';
    let body = '';
    for await (const chunk of req) { body += chunk; if (body.length > 1e6) break; }
    try { reports.set(runId, { ...JSON.parse(body), receivedAt: Date.now() }); } catch { return json(res, 400, { error: 'bad json' }); }
    json(res, 204);
  }

  function proxy(req, res) {
    const lib = app.protocol === 'https:' ? https : http;
    const headers = { ...req.headers, host: app.host };
    delete headers['accept-encoding']; // keep bodies plain; we don't rewrite them, but it keeps things simple
    const upstream = lib.request({
      protocol: app.protocol, hostname: app.hostname, port: app.port || (app.protocol === 'https:' ? 443 : 80),
      method: req.method, path: req.url, headers,
    }, (up) => {
      const out = { ...up.headers };
      // Allow the app to be framed by the harness page (same origin).
      delete out['x-frame-options'];
      if (out['content-security-policy']) {
        out['content-security-policy'] = String(out['content-security-policy'])
          .split(';').filter((d) => !/^\s*frame-ancestors/i.test(d)).join(';');
      }
      // Keep redirects on the harness origin.
      if (out.location) out.location = String(out.location).replace(app.origin, '');
      res.writeHead(up.statusCode || 502, out);
      up.pipe(res);
    });
    upstream.on('error', (err) => {
      json(res, 502, { error: `AspectProof could not reach the app at ${config.app}: ${err.code || err.message}. Is it running?` });
    });
    req.pipe(upstream);
  }

  return {
    server,
    reports,
    origin: `http://localhost:${config.harnessPort}`,
    listen() {
      return new Promise((resolve, reject) => {
        server.once('error', reject);
        server.listen(config.harnessPort, () => resolve());
      });
    },
    close() { return new Promise((resolve) => server.close(() => resolve())); },
    frameUrl(profileId, runId, start = '/') {
      const q = new URLSearchParams({ profile: profileId, run: runId, start });
      return `http://localhost:${config.harnessPort}/__ap/frame?${q}`;
    },
  };
}

function json(res, status, body) {
  if (res.headersSent) return res.end();
  res.writeHead(status, { 'content-type': 'application/json' });
  res.end(body === undefined ? '' : JSON.stringify(body));
}

function escapeHtml(s) {
  return s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
}
