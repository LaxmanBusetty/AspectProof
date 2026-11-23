---
test: ../aspectproof-r9-desktop-1920__checkout_test.md
status: passed
started: 2026-11-23T09:09:04.917Z
duration_s: 62.6
session_id: 14990d23-020d-4297-9b5d-8d229a4633d9
---

# Session: aspectproof-r9-desktop-1920__checkout — Result

## Step 1 ✓ passed (62.6s)
md5: b6a798f5eea63625b4437bd8923881ba
You are testing a web app inside the AspectProof harness, which shows the app at "Desktop 1920×1080".
The app fills the window below a thin "AspectProof layout" status bar at the top.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Add 'Trail Runner Shoes' to the cart. Then open the cart using the site's header navigation (open the Menu button first if the links are not visible). Change its quantity to 2, press 'Place order', and confirm an 'Order confirmed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
