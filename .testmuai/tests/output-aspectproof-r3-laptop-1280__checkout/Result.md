---
test: ../aspectproof-r3-laptop-1280__checkout_test.md
status: passed
started: 2026-11-23T07:09:40.230Z
duration_s: 62.5
session_id: 8cd0e339-ef10-4c89-b75e-0516d7a54522
---

# Session: aspectproof-r3-laptop-1280__checkout — Result

## Step 1 ✓ passed (62.5s)
md5: 8aac656d39f570d2855f57d26aac1ab2
You are testing a web app inside the AspectProof harness, which shows the app at "Laptop 1280×800".
The app fills the window below a thin "AspectProof layout" status bar at the top.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Add 'Trail Runner Shoes' to the cart. Then open the cart using the site's header navigation (open the Menu button first if the links are not visible). Change its quantity to 2, press 'Place order', and confirm an 'Order confirmed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
