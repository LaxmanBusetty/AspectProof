---
test: ../aspectproof-r7-phone-320__signup_test.md
status: passed
started: 2026-11-23T09:00:03.092Z
duration_s: 41.2
session_id: eda443a7-ddee-4b3d-a544-57e591c835ee
---

# Session: aspectproof-r7-phone-320__signup — Result

## Step 1 ✓ passed (41.2s)
md5: 8c92351d450424bd59b1361c6348fa05
You are testing a web app inside the AspectProof harness, which shows the app at "Phone 320×568 (small Android)".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Fill in the 'Get trail notes' form with name 'Test User' and email 'test@example.com', press 'Subscribe', and confirm a 'You're subscribed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
