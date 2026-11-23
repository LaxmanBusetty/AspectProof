// Turns failing checks into a prompt the coding agent can act on.
import { writeFile, mkdir } from 'node:fs/promises';
import { join } from 'node:path';
import { STATE_DIR } from './config.js';

export function buildFeedback(config, state, results) {
  const failing = results.filter((r) => r.verdict !== 'pass');
  const all = Object.values(state.cells);
  const passing = all.filter((c) => c.verdict === 'pass');
  const total = config.profiles.length * config.flows.length;
  const lines = [];

  if (!failing.length) {
    lines.push(`# AspectProof: all ${results.length} checks in round ${state.round} passed`, '', `Matrix: ${passing.length}/${total} passing.`);
    return lines.join('\n');
  }

  lines.push(
    `# AspectProof: ${failing.length} of ${results.length} checks failed (round ${state.round})`,
    '',
    'Kane CLI ran each user flow in a real Chrome browser at each screen size, through the AspectProof device frame.',
    'The layout probe measured the app inside that same browser. Fix the app so every flow works and the probe reports 0 issues at every size.',
    '',
    'Rules:',
    '- Change the app code (HTML, CSS, JS). Do not edit aspectproof.config.json, the flows, or anything in src/ or .aspectproof/.',
    '- Keep the sizes that pass working. Prefer targeted responsive fixes (media queries, flexible widths) over rewrites.',
    `- Currently passing: ${passing.length ? summarizeCells(passing) : 'none'}.`,
    '',
  );

  // Group failures by profile so related breakpoint bugs sit together.
  const byProfile = new Map();
  for (const r of failing) {
    if (!byProfile.has(r.profile.id)) byProfile.set(r.profile.id, []);
    byProfile.get(r.profile.id).push(r);
  }
  for (const [, group] of byProfile) {
    const p = group[0].profile;
    lines.push(`## ${p.label} (${p.width}×${p.height}, ${p.mode === 'window' ? 'real Chrome window' : 'device frame'})`);
    for (const r of group) {
      lines.push('', `### ${r.flow.name} — ${r.verdict.toUpperCase()}${r.failedBy.length ? ` (caught by: ${r.failedBy.join(' + ')})` : ''}`);
      lines.push(`Flow: ${r.flow.objective}`);
      if (r.verdict === 'error') {
        lines.push(`Kane could not run this check: ${(r.kane.errors || []).join('; ') || r.kane.stderrTail || `exit ${r.kane.exitCode}`}`);
        continue;
      }
      if (r.kane.exitCode !== 0) {
        lines.push(`Kane verdict: ${r.kane.status}${r.kane.timedOut ? ' (timed out)' : ''}${r.kane.reason ? `, reason: ${r.kane.reason}` : ''}`);
        if (r.kane.oneLiner) lines.push(`Kane says: ${r.kane.oneLiner}`);
        if (r.kane.bugVerdict?.confirmed) lines.push(`Kane bug verdict: confirmed ${r.kane.bugVerdict.severity || ''} ${r.kane.bugVerdict.category || 'product bug'}${r.kane.bugVerdict.rootCause ? `. Root cause: ${truncate(r.kane.bugVerdict.rootCause, 300)}` : ''}`);
        if (r.kane.summary && r.kane.summary !== r.kane.oneLiner) lines.push(`Kane summary: ${truncate(r.kane.summary, 600)}`);
        const lastSteps = (r.kane.steps || []).filter((s) => s.remark).slice(-5);
        if (lastSteps.length) {
          lines.push('Last steps:');
          for (const s of lastSteps) lines.push(`  - step ${s.step} [${s.status}] ${truncate(s.remark, 200)}`);
        }
        if (r.kane.errors?.length) lines.push(`Kane errors: ${r.kane.errors.join('; ')}`);
      } else {
        lines.push('Kane verdict: the flow itself completed.');
      }
      if (r.layout.issues.length) {
        lines.push('Layout probe (measured in Kane\'s browser):');
        for (const i of r.layout.issues) lines.push(`  - [${i.kind}] \`${i.selector}\`${i.text ? ` "${i.text}"` : ''}: ${i.detail}`);
      } else if (r.layout.probeError) {
        lines.push(`Layout probe: ${r.layout.probeError}`);
      }
      const evidence = [r.kane.testUrl && `Test Manager: ${r.kane.testUrl}`, r.kane.sessionDir && `evidence: ${r.kane.sessionDir}/evidence`, `log: ${r.log}`].filter(Boolean);
      lines.push(`Evidence: ${evidence.join(' · ')}`);
    }
    lines.push('');
  }

  lines.push(
    '## When you are done',
    'Stop and AspectProof re-runs the failing checks automatically (Claude Code hook), or run:',
    '  npx aspectproof verify --only failed',
  );
  return lines.join('\n');
}

export async function writeFeedback(config, state, results) {
  const dir = join(config.cwd, STATE_DIR);
  await mkdir(dir, { recursive: true });
  const path = join(dir, 'feedback.md');
  await writeFile(path, buildFeedback(config, state, results));
  return join(STATE_DIR, 'feedback.md');
}

function summarizeCells(cells) {
  const byProfile = new Map();
  for (const c of cells) {
    if (!byProfile.has(c.profile.id)) byProfile.set(c.profile.id, []);
    byProfile.get(c.profile.id).push(c.flow.id);
  }
  return [...byProfile].map(([p, flows]) => `${p} (${flows.join(', ')})`).join('; ');
}

const truncate = (s, n) => (s && s.length > n ? s.slice(0, n - 1) + '…' : s);
