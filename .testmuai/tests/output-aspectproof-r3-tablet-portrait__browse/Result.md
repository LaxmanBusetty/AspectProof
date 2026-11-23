---
test: ../aspectproof-r3-tablet-portrait__browse_test.md
status: failed
started: 2026-11-23T07:11:50.136Z
duration_s: 56.1
session_id: 97487264-fd89-4ade-be69-9fc505eb6bca
---

# Session: aspectproof-r3-tablet-portrait__browse — Result

## Step 1 ✗ failed (56.1s)
md5: c74c118246b47596942d3943a358f958
Reason: Child agent failed: No Menu button is present in the app header at this tablet portrait size.
You are testing a web app inside the AspectProof harness, which shows the app at "Tablet portrait 768×1024".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Using the site's header navigation (open the Menu button first if the links are not visible), go to the Shop page. Confirm at least 3 products are listed, each with a price and an 'Add to cart' button.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
