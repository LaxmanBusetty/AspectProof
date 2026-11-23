---
test: ../aspectproof-r4-tablet-landscape__browse_test.md
status: failed
started: 2026-11-23T08:03:22.269Z
duration_s: 57.3
session_id: 8bd7ee34-e353-4c2e-a066-d4f596d3fbab
---

# Session: aspectproof-r4-tablet-landscape__browse — Result

## Step 1 ✗ failed (57.3s)
md5: bacdcd78d6cd4747eb47f0aefa1be54c
Reason: Child agent failed: No Menu button is present in the app header or page controls at this tablet layout.
You are testing a web app inside the AspectProof harness, which shows the app at "Tablet landscape 1024×768".
The app fills the window below a thin "AspectProof layout" status bar at the top.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Using the site's header navigation (open the Menu button first if the links are not visible), go to the Shop page. Confirm at least 3 products are listed, each with a price and an 'Add to cart' button.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
