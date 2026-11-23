---
test: ../aspectproof-r7-phone-375__browse_test.md
status: passed
started: 2026-11-23T08:51:38.252Z
duration_s: 75
session_id: cd5eeeca-bd09-4cba-a410-7639683f2a0d
---

# Session: aspectproof-r7-phone-375__browse — Result

## Step 1 ✓ passed (75s)
md5: f3cb93b992936ecc429a31f258c9a169
You are testing a web app inside the AspectProof harness, which shows the app at "Phone 375×812 (iPhone 11 Pro)".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Using the site's header navigation (open the Menu button first if the links are not visible), go to the Shop page. Confirm at least 3 products are listed, each with a price and an 'Add to cart' button.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
