---
test: ../aspectproof-r3-phone-390__checkout_test.md
status: failed
started: 2026-11-23T07:18:31.890Z
duration_s: 77.1
session_id: a2086b28-667a-4b54-ab44-9e4ba7e1ddac
---

# Session: aspectproof-r3-phone-390__checkout — Result

## Step 1 ✗ failed (77.1s)
md5: 34325a34e88d2b539693e5b5eeb50677
Reason: Step 3 is blocked: Place order extends 45px past the right edge and the panel reports 4 issues.
You are testing a web app inside the AspectProof harness, which shows the app at "Phone 390×844 (iPhone 14)".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Add 'Trail Runner Shoes' to the cart. Then open the cart using the site's header navigation (open the Menu button first if the links are not visible). Change its quantity to 2, press 'Place order', and confirm an 'Order confirmed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
