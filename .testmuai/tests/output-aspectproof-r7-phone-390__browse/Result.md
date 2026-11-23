---
test: ../aspectproof-r7-phone-390__browse_test.md
status: passed
started: 2026-11-23T08:47:31.109Z
duration_s: 62.4
session_id: 449c289b-cc8e-47b4-8643-822c5e556433
---

# Session: aspectproof-r7-phone-390__browse — Result

## Step 1 ✓ passed (62.4s)
md5: 90900f1885bdec338d6b57a06713673d
You are testing a web app inside the AspectProof harness, which shows the app at "Phone 390×844 (iPhone 14)".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Using the site's header navigation (open the Menu button first if the links are not visible), go to the Shop page. Confirm at least 3 products are listed, each with a price and an 'Add to cart' button.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
