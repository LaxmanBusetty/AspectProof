---
test: ../aspectproof-r3-tablet-portrait__checkout_test.md
status: failed
started: 2026-11-23T07:12:52.485Z
duration_s: 43.7
session_id: f4f48ba8-5664-465a-8f52-9158bd4f13a5
---

# Session: aspectproof-r3-tablet-portrait__checkout — Result

## Step 1 ✗ failed (43.7s)
md5: a93ceb1cf5e0d5d651ed3b5a9fd61b8a
Reason: The current header shows only Northtrail; no Menu or Cart navigation control is present.
You are testing a web app inside the AspectProof harness, which shows the app at "Tablet portrait 768×1024".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Add 'Trail Runner Shoes' to the cart. Then open the cart using the site's header navigation (open the Menu button first if the links are not visible). Change its quantity to 2, press 'Place order', and confirm an 'Order confirmed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
