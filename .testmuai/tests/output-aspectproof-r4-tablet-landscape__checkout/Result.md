---
test: ../aspectproof-r4-tablet-landscape__checkout_test.md
status: failed
started: 2026-11-23T08:04:27.681Z
duration_s: 39.8
session_id: b771e5f7-be11-4b13-bf47-3ea88c3941e6
---

# Session: aspectproof-r4-tablet-landscape__checkout — Result

## Step 1 ✗ failed (39.8s)
md5: 388f45ffd6986f71552c5eb49642610f
Reason: Step 2 is blocked: the tablet header shows only Northtrail, with no Menu button or cart link.
You are testing a web app inside the AspectProof harness, which shows the app at "Tablet landscape 1024×768".
The app fills the window below a thin "AspectProof layout" status bar at the top.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Add 'Trail Runner Shoes' to the cart. Then open the cart using the site's header navigation (open the Menu button first if the links are not visible). Change its quantity to 2, press 'Place order', and confirm an 'Order confirmed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
