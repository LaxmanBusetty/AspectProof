# AspectProof

Prove your web app works at every screen size, not just the one your coding agent happened to check.

I built this for the KaneCLI Online Hackathon. The idea came from something that keeps happening to me: I ask an AI agent to build or fix a page, it says "done", it looks great on my laptop, and then I open it on my phone and the checkout button is hanging off the side of the screen. The agent never looked at a phone. Nobody did.

AspectProof makes the agent look. It runs your real user flows (browse, checkout, sign up, whatever matters) at 8 screen sizes, from a 320px phone up to a 1920px desktop. Every single check is a Kane CLI run in a real Chrome browser. When something breaks, the details go straight back to the coding agent, it fixes the code, and Kane checks again. The agent isn't allowed to say it's finished until every size passes.

## What actually happened when I ran it

The repo includes a small demo store called Northtrail with three responsive bugs I planted on purpose:

1. On tablets (601 to 1100px wide) the nav links get hidden, but the Menu button only shows up below 600px. So there's no way to reach the shop or the cart.
2. On phones, the cart summary has a `min-width: 440px`, which pushes the "Place order" button off the right edge.
3. On a phone held sideways, the promo bar turns into a full-screen overlay with its close button hidden.

Desktop and laptop look perfect, which is exactly why bugs like these ship.

Here's the real run, with real Kane and Claude Code doing the fixing:

| Round | What happened | Passing |
|---|---|---|
| 3 | First full run of all 24 checks | 14 / 24 |
| 4 | Claude tried to finish. The Stop hook ran Kane, found 10 failures, and blocked it | 14 / 24 |
| 5 | Claude fixed things based only on Kane's reports. Re-checked the 10 | 23 / 24 |
| 6 | Last one fixed | 24 / 24 |
| 7 | Full regression sweep. One desktop check failed, but Kane's own triage said it was a test hiccup, not an app bug | 23 / 24 |
| 8 | Re-run of that check passed | 24 / 24 |
| 9 | Final full sweep | **24 / 24** |

Claude never saw the list of planted bugs (it's blocked from reading that file). Everything it knew came from Kane. Its whole fix was 10 lines added and 16 removed in one CSS file.

In total that was 97 Kane runs, about 65 seconds and roughly 25 credits each, around 2,400 credits for the whole thing. The final report is in [`docs/report-verified-24-of-24.html`](docs/report-verified-24-of-24.html), and the exact message the hook sent to Claude in round 4 is in [`docs/evidence/`](docs/evidence/).

My favorite moment: on the tablet sizes, my layout checker saw nothing wrong. Technically nothing *was* overflowing or overlapping; the links were just hidden. Kane caught it anyway, because it tried to use the site like a person would and reported "the header provides neither visible Shop navigation nor a Menu button." That's the kind of bug you only find by actually using the thing.

## How it works

Kane CLI can't make its Chrome window smaller than 800×600, and its mobile mode only drives native apps, not websites. So I couldn't just tell Kane "be an iPhone."

Instead, AspectProof runs a small local server that does two things:

- It serves a "device frame" page that loads your app in a frame at the exact phone or tablet size. Your CSS sees a 375px-wide screen, so the real mobile layout renders, and Kane uses it like a user would. Laptop and tablet-landscape sizes skip the frame and use a real Kane window size.
- It proxies your app through the same address, so a small script on the frame page can measure the app from inside the same browser Kane is using. It looks for sideways scrolling (and which element is causing it), buttons pushed off-screen, controls covered by overlays, and tap targets that are too small. Results show up in a panel next to the device, and Kane is asked to confirm that panel says 0 issues.

```
Kane CLI (real Chrome)
   └─ localhost:4400/__ap/frame?profile=phone-375
        ├─ your app, in a 375×812 frame (proxied from localhost:3000)
        └─ layout panel: "Issues seen this session: 0"
                 │
                 ▼
results ─▶ feedback for the agent ─▶ Claude Code fixes ─▶ Kane checks again
```

A check only passes if Kane completed the flow and the layout panel stayed clean. The two catch different things, which is the point: the measurements catch a half-clipped button that Kane might still manage to tap, and Kane catches things like a missing menu that no measurement would flag.

When a check fails, the agent gets a plain report: what Kane was trying to do, where it got stuck, Kane's own bug verdict, and the exact element that overflowed and by how many pixels. For example, `.cart-summary` with `min-width: 440px`, 81px too wide.

One more thing I added after the real run: if Kane says a failure was its own automation problem rather than an app bug (it reports this in its result), AspectProof quietly retries that check once instead of sending the agent on a wild goose chase.

## Try it

You need Node 18+, Chrome, and a free TestMu AI account (it comes with 10,000 Kane credits).

```bash
npm install -g @testmuai/kane-cli
kane-cli login

git clone https://github.com/LaxmanBusetty/AspectProof.git
cd AspectProof
npm run demo          # starts the demo store on localhost:3000, leave it running
```

In a second terminal:

```bash
# one check first, about a minute
node bin/aspectproof.js verify --profiles phone-375 --flows checkout

# the whole thing: 8 sizes × 3 flows, about 25 minutes
node bin/aspectproof.js verify
npm run report
```

Want to see what Kane sees? `npm run serve` prints a link for each screen size you can open in your browser. Add `--headed --live` to `verify` to watch Kane's Chrome window and its steps as it works, or run `npm run watch` in another terminal.

To start over with the buggy store: `npm run reset-demo`.

## Running the loop with Claude Code

```bash
npm install -g @anthropic-ai/claude-code
npm run setup-claude      # installs the Stop hook into .claude/settings.json
claude
```

Then ask it something like "make sure the shop works well on phones and tablets."

From there it's hands-off. Every time Claude thinks it's done, the hook runs Kane. If anything fails, Claude gets the report and keeps going. Once the failures pass, the hook runs all 24 checks one more time to make sure nothing else broke. A few safety valves: it gives up after 4 rounds, it skips the check if nothing changed since the last green run, and if the app isn't running it just tells you instead of trapping the agent.

The settings also stop Claude from reading `docs/planted-bugs.md` or editing AspectProof itself. It has to fix the app, not the test.

If you use a different agent, `node bin/aspectproof.js loop --agent codex` (or any command that takes a prompt file) does the same loop without hooks.

## Using it on your own app

```bash
npx aspectproof init --app http://localhost:5173 --claude
```

Then edit `aspectproof.config.json`. The flows are just plain English, written the way you'd explain a task to a tester:

```json
{
  "id": "checkout",
  "name": "Checkout",
  "start": "/#shop",
  "objective": "Add 'Trail Runner Shoes' to the cart, open the cart, change the quantity to 2, press 'Place order', and confirm an 'Order confirmed' message appears."
}
```

Screen sizes live in the same file. Anything 800px wide or more can use a real Kane window (`"mode": "window"`); anything smaller goes in the frame (`"mode": "frame"`).

`verify` exits with 0 when everything passes and 1 when something fails, so it can run in CI too.

## What's in here

| | |
|---|---|
| `bin/aspectproof.js` | The CLI: `init`, `serve`, `verify`, `loop`, `watch`, `report` |
| `src/harness.js` | The local server: device frame, proxy, layout reports |
| `src/harness-assets/frame.js` | Frame sizing and the layout checker |
| `src/kane.js` | Runs `kane-cli run --agent` and reads its output |
| `src/verify.js` | Runs the matrix, decides pass/fail, retries Kane hiccups |
| `src/feedback.js` | Writes the report the agent reads |
| `src/loop.js` | The Claude Code Stop hook and the `loop` command |
| `src/report.js` | The HTML report |
| `demo-shop/` | Northtrail, the demo store |
| `docs/` | Planted bugs (spoilers), demo script, final report, evidence |
| `.testmuai/tests/` | Every Kane run saved as a reusable test, written by Kane itself |

## Limitations

I'd rather be upfront about these:

- The frame gets the screen size and layout right, but it isn't a real phone. No touch events, no mobile browser identity, no pixel density. For a real device you'd want Kane's native mobile support, which means wrapping the site in an app.
- Your app runs through a proxy on port 4400. Apps that hard-code their own full URL or rely on cookies for a specific domain may need some setup.
- Kane is an AI agent, so it doesn't behave identically every run. That's part of why the layout checker exists: its measurements are the same every time.
- A full run of 24 checks takes about 25 minutes. While you're iterating, use `--profiles` and `--flows`; the hook only re-runs what failed until the final sweep.

## What I'd do next

- Run the same flows on a real Android emulator by wrapping the site in a Capacitor shell.
- A GitHub Action that posts the pass/fail grid on every pull request.
- Run checks in parallel. Sizes that share a window size could run side by side and cut the 25 minutes down a lot.

---

Built with Claude Code, verified with Kane CLI.
