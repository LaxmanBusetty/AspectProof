---
test: ../aspectproof-r3-tablet-landscape__checkout_test.md
status: failed
started: 2026-11-23T07:29:34.813Z
duration_s: 56.2
session_id: 30295976-a78e-4355-86ac-5c516186867c
---

# Session: aspectproof-r3-tablet-landscape__checkout — Result

## Step 1 ✗ failed (56.2s)
md5: 388f45ffd6986f71552c5eb49642610f
Reason: Child agent failed: No Menu button or other header navigation control is present in the current app view.
You are testing a web app inside the AspectProof harness, which shows the app at "Tablet landscape 1024×768".
The app fills the window below a thin "AspectProof layout" status bar at the top.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Add 'Trail Runner Shoes' to the cart. Then open the cart using the site's header navigation (open the Menu button first if the links are not visible). Change its quantity to 2, press 'Place order', and confirm an 'Order confirmed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
