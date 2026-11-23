---
test: ../aspectproof-r3-phone-landscape__checkout_test.md
status: failed
started: 2026-11-23T07:15:59.744Z
duration_s: 37.6
session_id: 9628e983-3d40-4705-b15d-8860b872ff42
---

# Session: aspectproof-r3-phone-landscape__checkout — Result

## Step 1 ✗ failed (37.6s)
md5: 348fd98fded27950fe8c2d9a76474924
Reason: Step 1 is blocked: the promotion overlay covers the Trail Runner Shoes Add to cart control, and the AspectProof panel reports issues.
You are testing a web app inside the AspectProof harness, which shows the app at "Phone landscape 844×390".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Add 'Trail Runner Shoes' to the cart. Then open the cart using the site's header navigation (open the Menu button first if the links are not visible). Change its quantity to 2, press 'Place order', and confirm an 'Order confirmed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
