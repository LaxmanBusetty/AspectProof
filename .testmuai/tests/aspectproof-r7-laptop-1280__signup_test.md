---
mode: testing
max_steps: 30
timeout: 300
target: chrome
---

# Session: aspectproof-r7-laptop-1280__signup

## Step 1
You are testing a web app inside the AspectProof harness, which shows the app at "Laptop 1280×800".
The app fills the window below a thin "AspectProof layout" status bar at the top.
Interact only with the app, the way a real user on this screen size would. Do not resize the window and do not interact with the panel.

Task: Fill in the 'Get trail notes' form with name 'Test User' and email 'test@example.com', press 'Subscribe', and confirm a 'You're subscribed' message appears.

Finally, read the "AspectProof layout" panel and confirm it shows "Issues seen this session: 0". Store the full panel text as layout_report.
The test fails if the task cannot be completed at this screen size, or if the panel shows any issues. When it fails, name the exact control or step that was blocked and why.
