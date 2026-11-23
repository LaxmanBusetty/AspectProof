# AspectProof

**Prove your product works everywhere.**

AI coding agents build and check at desktop width. Then the "Place order" button disappears on a phone, the menu vanishes on a tablet, and nobody notices until a customer does.

AspectProof runs your key user flows at every screen size, from a 320px phone to a 1920px desktop, with **Kane CLI** driving a real Chrome browser. Failures go back to your coding agent, which fixes the code, and Kane re-verifies until every size is green.

```
desktop works → phone breaks → Kane catches it → the agent fixes it → every profile passes
```

Every check is a Kane CLI run. No Playwright, no Selenium, no selectors to maintain.

---

## How it works

```
                 ┌──────────────────────── AspectProof harness (localhost:4400) ────────────────────────┐
 Kane CLI  ───▶  │  /__ap/frame?profile=phone-375                                                          │
 (real Chrome)   │  ┌──────────── device frame 375×812 ───────────┐   ┌─ AspectProof layout panel ─┐      │
                 │  │  your app (same-origin proxy of :3000)      │   │ Issues seen this session: 2│      │
                 │  │  responds to the frame width, so its        │◀──│ [offscreen] #place-order … │      │
                 │  │  phone layout really renders                │   │ (layout probe, live)       │      │
                 │  └─────────────────────────────────────────────┘   └────────────────────────────┘      │
                 └────────────────────────────────────────────────────────────────────────────────────────┘
                         │ NDJSON (--agent)                                │ probe report (exact selectors)
                         ▼                                                 ▼
                 results.json ──▶ feedback.md ──▶ coding agent (Claude Code hook / loop) ──▶ fix ──▶ re-verify
                                                                        └──▶ report.html (red → green matrix)
```

1. **Laptop and tablet-landscape sizes run in a real Kane window.** `kane-cli config set-window 1024x768`, then the flow.
2. **Phone and tablet-portrait sizes run in the device frame.** Kane's window has a minimum of 800×600, so AspectProof serves a page that loads your app in a frame at the exact device size (320×568, 375×812, 390×844, 768×1024, and landscape). The app sees a 375px-wide viewport, so its media queries fire and its real mobile layout renders, inside Kane's browser.
3. **The layout probe measures what users can't do.** Inside the same browser, it detects horizontal overflow (and the element causing it), controls pushed off-screen, controls covered by overlays (ignoring bars you can scroll past), and tap targets under 24×24px. It shows them in a panel that Kane reads and asserts on, and posts them to AspectProof with exact selectors for the agent.
4. **Kane verifies the user flow.** Each flow is plain English ("add Trail Runner Shoes to the cart, check out…"). Kane runs it with `--agent` and AspectProof parses the NDJSON `run_end` event: status, one-liner, steps, Test Manager link.
5. **The agent closes the loop.** Failures become `.aspectproof/feedback.md`: what Kane couldn't do, which element overflowed and by how much, which sizes still pass. The agent fixes the code, AspectProof re-runs only the failing checks, then sweeps the full matrix for regressions.

A cell passes only when **Kane completed the flow** *and* **the probe saw 0 layout issues**. The two catch different things. The probe can't tell that a tablet user has no way to reach the cart (hidden links aren't a layout error), but Kane can. Kane may still manage to tap a half-clipped button, but the probe reports the clipping.

## Quick start (about 5 minutes)

Requirements: Node 18+, Chrome, a TestMu AI account ([free 10,000 Kane credits](https://www.testmuai.com/kane-cli/)).

```bash
npm install -g @testmuai/kane-cli
kane-cli login                      # opens your browser once

git clone <this repo> aspectproof && cd aspectproof
npm run demo                        # terminal 1: the demo shop on http://localhost:3000

# terminal 2: one check first, to confirm Kane is wired up
node bin/aspectproof.js verify --profiles phone-375 --flows checkout

# the full matrix: 8 screen profiles × 3 flows = 24 Kane runs
node bin/aspectproof.js verify
node bin/aspectproof.js report --open
```

Want to see what Kane sees? `node bin/aspectproof.js serve` prints a frame URL per profile. Open one in Chrome.

## Close the loop with an agent

### Option A: Claude Code Stop hook (tightest loop)

Run `npm run setup-claude` once. It installs `hooks/claude-settings.json` as `.claude/settings.json`, which adds a **Stop hook**. When Claude Code tries to finish a task, the hook runs AspectProof:

- **Any check fails:** the hook blocks the stop and returns Kane's findings as the reason. Claude reads them, fixes the CSS, and tries to stop again, which re-runs only the failing checks.
- **Everything passes:** a full regression sweep, then Claude is allowed to stop with "AspectProof verified ✓ 24/24".
- **Nothing changed since the last green run** (git fingerprint): the stop is allowed instantly.
- **Still red after 4 rounds** (configurable): Claude is allowed to stop, and the report shows what's left.
- **App not running:** the hook reports it and never traps the agent.

```bash
npm install -g @anthropic-ai/claude-code
npm run setup-claude                # once
npm run demo                        # keep the app running
claude                              # in this folder
> The shop needs to look right on phones and tablets. Review the responsive CSS and fix anything broken.
```

For your own project: `npx aspectproof init --app http://localhost:5173 --claude`.

The shipped settings also stop Claude from reading `docs/planted-bugs.md` (the answer key) and from editing AspectProof itself, so it can't "fix" a test by changing it.

### Option B: `aspectproof loop` (any headless agent)

```bash
node bin/aspectproof.js loop --agent claude                         # claude -p, edits auto-accepted
node bin/aspectproof.js loop --agent codex                          # codex exec --full-auto
node bin/aspectproof.js loop --agent "my-agent --prompt-file {prompt_file}"
```

AspectProof verifies, hands the failures to the agent, re-verifies the failing cells, sweeps the full matrix when they're green, and stops at all-green or after `loop.maxRounds`.

## Configuration: `aspectproof.config.json`

```jsonc
{
  "app": "http://localhost:3000",          // your running app
  "harnessPort": 4400,
  "frameWindow": "1280x800",               // Kane window used for device-frame profiles
  "profiles": [
    { "id": "tablet-landscape", "label": "Tablet landscape 1024×768", "mode": "window", "width": 1024, "height": 768 },
    { "id": "phone-375", "label": "Phone 375×812", "mode": "frame", "width": 375, "height": 812, "touch": true }
  ],
  "flows": [
    { "id": "checkout", "name": "Checkout", "start": "/#shop",
      "objective": "Add 'Trail Runner Shoes' to the cart, open the cart, … confirm an 'Order confirmed' message appears." }
  ],
  "kane": { "command": "kane-cli", "headless": true, "maxSteps": 30, "timeoutSeconds": 300, "concurrency": 1, "extraArgs": [] },
  "loop": { "maxRounds": 4, "fullSweepOnGreen": true }
}
```

- `mode: "window"` needs a size Kane supports (800–3840 × 600–2160). Anything smaller uses `mode: "frame"`.
- Flows are plain English, written the way you'd brief a QA tester. AspectProof wraps each one with instructions to use only the app and to assert the layout panel.
- `kane.extraArgs` passes straight to `kane-cli run`, e.g. `["--bug-detection", "continue"]`.
- Exit codes: `0` all pass, `1` something failed, `2` setup error. Usable in CI.

## What's in the repo

| Path | What it is |
|---|---|
| `bin/aspectproof.js` | CLI: `init`, `serve`, `verify`, `loop`, `report`, `hook claude-stop` |
| `src/harness.js` | Same-origin proxy + device-frame server + probe report receiver |
| `src/harness-assets/frame.js` | Device frame sizing and the layout probe |
| `src/kane.js` | `kane-cli run --agent` wrapper and NDJSON parser (`run_end`, steps, errors) |
| `src/verify.js` | Profile × flow matrix, window grouping, verdicts, state |
| `src/feedback.js` | Turns failures into an agent-ready prompt |
| `src/report.js` | Self-contained HTML report with red → green history |
| `src/loop.js` | Claude Code Stop hook and the `loop` driver |
| `hooks/claude-settings.json` | Claude Code settings: Stop hook + read/edit guards (`npm run setup-claude`) |
| `demo-shop/` | Northtrail Outfitters, a demo store with 3 planted responsive bugs |
| `.aspectproof/` | Run output (git-ignored): `state.json`, `feedback.md`, `report.html`, per-run NDJSON logs |

## Honest limits

- The device frame reproduces **viewport size and layout** (media queries, overflow, stacking). It does not emulate touch events, a mobile user-agent, or device pixel ratio. Kane CLI's mobile targets run native apps on the iOS Simulator and Android Emulator, not mobile web pages, so the frame is the only way to put phone-width web layouts in front of Kane today.
- The frame proxies your app through `localhost:4400`. Apps that hard-code absolute URLs to their own origin, or that need cookies scoped to a different domain, may need `app` pointed at a local build.
- Kane's on-screen judgment can vary between runs. The probe's measurements are deterministic and are what the agent fixes against.
- A full matrix is 24 Kane runs. Use `--profiles`/`--flows` while iterating; the hook and `loop` only re-run failing cells until the final sweep.

## Roadmap

- Real Android emulator pass: wrap the app in a Capacitor WebView shell and run the same flows with `--target emulator` on Apple Silicon.
- Save each green flow as a Kane `_test.md` so it replays in CI at zero credits.
- A GitHub Action that posts the red/green matrix on every pull request preview.

## Built for the KaneCLI Online Hackathon

AspectProof was built with Claude Code (the coding agent) and is verified with Kane CLI. See `docs/demo-script.md` for the 3-minute demo outline.
