---
test: ../aspectproof-r4-phone-320__checkout_test.md
status: failed
started: 2026-11-23T08:13:26.059Z
duration_s: 74.2
session_id: f6dd9b1f-2d77-42b4-ae88-1d53272358b8
---

# Session: aspectproof-r4-phone-320__checkout — Result

## Step 1 ✗ failed (74.2s)
md5: a27185bbfd91437ef89b30472fe013f1
Reason: Step 3 is blocked: Place order is offscreen; panel reports 4 issues including cart overflow.
You are testing a web app inside the AspectProof harness, which shows the app at "Phone 320×568 (small Android)".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Add 'Trail Runner Shoes' to the cart. Then open the cart using the site's header navigation (open the Menu button first if the links are not visible). Change its quantity to 2, press 'Place order', and confirm an 'Order confirmed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
