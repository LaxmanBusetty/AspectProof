---
test: ../aspectproof-r7-desktop-1920__browse_test.md
status: failed
started: 2026-11-23T08:30:46.875Z
duration_s: 90.8
session_id: dc62609a-bd24-4d53-a65c-667f2f2ed52b
---

# Session: aspectproof-r7-desktop-1920__browse — Result

## Step 1 ✗ failed (90.8s)
md5: cc4dd553a34c007e9283814c5c4d55e0
Reason: Child agent failed: No control was blocked: Shop has four priced products with enabled Add to cart buttons, and the layout panel reports zero issues.
You are testing a web app inside the AspectProof harness, which shows the app at "Desktop 1920×1080".
The app fills the window below a thin "AspectProof layout" status bar at the top.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Using the site's header navigation (open the Menu button first if the links are not visible), go to the Shop page. Confirm at least 3 products are listed, each with a price and an 'Add to cart' button.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
