---
test: ../aspectproof-r4-phone-landscape__signup_test.md
status: failed
started: 2026-11-23T08:09:12.348Z
duration_s: 108.5
session_id: 3a1249e7-5ad7-4c02-97f0-2b3f2a33ab0f
---

# Session: aspectproof-r4-phone-landscape__signup — Result

## Step 1 ✗ failed (108.5s)
md5: f36fecd8d91c9b9683a8370ce36fc7fd
Reason: The AspectProof panel shows Issues seen this session: 7, not 0, and the panel cannot be interacted with.
You are testing a web app inside the AspectProof harness, which shows the app at "Phone landscape 844×390".
The page has the app inside a device frame on the left and an "AspectProof layout" panel on the right.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Fill in the 'Get trail notes' form with name 'Test User' and email 'test@example.com', press 'Subscribe', and confirm a 'You're subscribed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
