---
test: ../aspectproof-r3-laptop-1280__browse_test.md
status: passed
started: 2026-11-23T07:08:23.011Z
duration_s: 64.5
session_id: 3fc09b7b-5b01-450f-9833-9d154957bb25
---

# Session: aspectproof-r3-laptop-1280__browse — Result

## Step 1 ✓ passed (64.5s)
md5: 214e2908fe8ef9a396f793617dce4504
You are testing a web app inside the AspectProof harness, which shows the app at "Laptop 1280×800".
The app fills the window below a thin "AspectProof layout" status bar at the top.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Using the site's header navigation (open the Menu button first if the links are not visible), go to the Shop page. Confirm at least 3 products are listed, each with a price and an 'Add to cart' button.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
