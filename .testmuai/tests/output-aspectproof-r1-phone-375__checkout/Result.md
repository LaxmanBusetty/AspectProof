---
test: ../aspectproof-r1-phone-375__checkout_test.md
status: failed
started: 2026-11-22T22:55:47.580Z
duration_s: 50.4
session_id: 71679e53-5da3-4bef-aeb5-ec60ea3bb64f
---

# Session: aspectproof-r1-phone-375__checkout — Result

## Step 1 ✗ failed (50.4s)
md5: f3d71dba9a99f94203933d37a2d3bd33
Reason: Step 3 is blocked: Place order is offscreen 60px, and AspectProof reports four layout issues at this screen size.
You are testing a web app inside the AspectProof harness, which shows the app at "Phone 375×812 (iPhone 11 Pro)".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Add 'Trail Runner Shoes' to the cart. Then open the cart using the site's header navigation (open the Menu button first if the links are not visible). Change its quantity to 2, press 'Place order', and confirm an 'Order confirmed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
