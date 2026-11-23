---
test: ../aspectproof-r4-phone-landscape__browse_test.md
status: failed
started: 2026-11-23T08:07:32.022Z
duration_s: 45.4
session_id: b92b6b0e-2e01-42f7-8179-cf9ef5b4687b
---

# Session: aspectproof-r4-phone-landscape__browse — Result

## Step 1 ✗ failed (45.4s)
md5: f4cf36056ba2225069401d971dad550f
Reason: Header Shop navigation is covered by the Promotion overlay, while Menu is hidden, so neither control can be used.
You are testing a web app inside the AspectProof harness, which shows the app at "Phone landscape 844×390".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Using the site's header navigation (open the Menu button first if the links are not visible), go to the Shop page. Confirm at least 3 products are listed, each with a price and an 'Add to cart' button.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
