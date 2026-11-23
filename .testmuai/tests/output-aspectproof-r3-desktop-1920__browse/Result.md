---
test: ../aspectproof-r3-desktop-1920__browse_test.md
status: passed
started: 2026-11-23T07:05:04.692Z
duration_s: 50.1
session_id: 95e5b669-c6c8-4d2a-9db7-dd18d390edaa
---

# Session: aspectproof-r3-desktop-1920__browse — Result

## Step 1 ✓ passed (50.1s)
md5: cc4dd553a34c007e9283814c5c4d55e0
You are testing a web app inside the AspectProof harness, which shows the app at "Desktop 1920×1080".
The app fills the window below a thin "AspectProof layout" status bar at the top.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Using the site's header navigation (open the Menu button first if the links are not visible), go to the Shop page. Confirm at least 3 products are listed, each with a price and an 'Add to cart' button.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
