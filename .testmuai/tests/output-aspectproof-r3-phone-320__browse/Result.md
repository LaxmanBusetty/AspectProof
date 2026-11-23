---
test: ../aspectproof-r3-phone-320__browse_test.md
status: passed
started: 2026-11-23T07:24:50.755Z
duration_s: 93.6
session_id: 243ac84a-2875-4f33-bb65-59d83f25b897
---

# Session: aspectproof-r3-phone-320__browse — Result

## Step 1 ✓ passed (93.6s)
md5: b519d97d457211059fca4dd545411ae8
You are testing a web app inside the AspectProof harness, which shows the app at "Phone 320×568 (small Android)".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Using the site's header navigation (open the Menu button first if the links are not visible), go to the Shop page. Confirm at least 3 products are listed, each with a price and an 'Add to cart' button.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
