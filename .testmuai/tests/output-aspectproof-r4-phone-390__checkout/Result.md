---
test: ../aspectproof-r4-phone-390__checkout_test.md
status: failed
started: 2026-11-23T08:11:08.105Z
duration_s: 48.4
session_id: cfdee62f-acba-4b92-99a0-6ff4d01e3c9f
---

# Session: aspectproof-r4-phone-390__checkout — Result

## Step 1 ✗ failed (48.4s)
md5: 34325a34e88d2b539693e5b5eeb50677
Reason: Step 3 is blocked: the AspectProof panel reports 4 issues, including Place order extending 45px past the right edge.
You are testing a web app inside the AspectProof harness, which shows the app at "Phone 390×844 (iPhone 14)".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Add 'Trail Runner Shoes' to the cart. Then open the cart using the site's header navigation (open the Menu button first if the links are not visible). Change its quantity to 2, press 'Place order', and confirm an 'Order confirmed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
