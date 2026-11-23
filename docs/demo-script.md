# 3-minute demo script

Judges stop watching at 3:00 and watch the video first, so the loop comes first.

**Before recording:** `npm run reset-demo`, `npm run demo` in one terminal, Claude Code open in another, the report closed. Run one Kane check beforehand so login and Chrome are warm. Do a full rehearsal: a full matrix plus fixes takes a while, so record the real run and speed up the waiting parts (label them "2× speed").

| Time | On screen | Say |
|---|---|---|
| 0:00–0:15 | The demo shop at 1920px, looking fine. | "This store looks done. The agent that built it only checked it on a desktop." |
| 0:15–0:35 | `node bin/aspectproof.js serve`, open the phone-375 frame: the cart overflows and the panel shows red issues. Then the tablet frame: no menu. | "AspectProof puts the app at eight screen sizes inside Kane's browser. On a phone the checkout button is cut off. On a tablet there's no way to reach the cart at all." |
| 0:35–1:10 | In Claude Code: "Make sure the shop works on phones and tablets." Claude edits, then tries to stop. The Stop hook fires: Kane runs, the terminal fills with ✗ lines, and the hook blocks with the feedback (show `feedback.md` briefly: selector, px overflow, Kane's one-liner). | "When Claude says it's done, the hook runs Kane on every size. It isn't done: 10 of 24 checks fail. Kane's findings go straight back to Claude, with the exact element and how far it overflows." |
| 1:10–2:00 | Claude reads the failure, fixes the cart, the promo overlay, and the tablet nav. It tries to stop again; the hook re-runs only the failing cells, then the full sweep. ✗ turns to ✓. | "Claude fixes it, tries to stop again, and Kane re-checks only what failed, then the whole matrix to make sure nothing else broke. Nobody opened a browser." |
| 2:00–2:30 | `report --open`: the matrix going red to green, round bars, the "AspectProof verified" badge. Click a Kane run link. | "Every cell is a real Kane run with evidence. Desktop passed from the start; the rest went red to green in four rounds." |
| 2:30–2:55 | The tablet-landscape cell: "caught by Kane", 0 layout issues. | "My favorite catch: the probe saw nothing wrong on the tablet, but Kane, acting like a user, couldn't find a way to the cart. Measurement plus a real user, at every size." |
| 2:55–3:00 | `npx aspectproof init --claude` | "One command adds it to your project." |

## Submission paragraph (draft)

AspectProof is a responsive-verification loop for AI coding agents. Agents build and check at desktop width, so layouts quietly break on phones and tablets. AspectProof runs your key user flows, described in plain English, at eight screen sizes from 320px phones to 1920px desktops. Every check is a Kane CLI run in real Chrome. Kane's window can't go below 800px, so phone and portrait-tablet sizes run inside a same-origin device frame where the app's real mobile layout renders, and a layout probe in the same browser measures overflow, off-screen and covered controls for Kane to assert. It's built with Claude Code, and a Claude Code Stop hook closes the loop: when Claude tries to finish, AspectProof runs Kane; if any size fails, the hook blocks the stop and feeds Claude Kane's verdict plus the exact failing selectors. Claude fixes the code, and Kane re-verifies the failures, then the full matrix, until every size is green. It's for teams shipping web apps with AI agents and no dedicated QA.
