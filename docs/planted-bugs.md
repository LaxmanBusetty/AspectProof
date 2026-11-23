# Planted bugs in the demo shop (spoilers)

The demo shop ships with three responsive bugs so the loop has something real to catch.
Keep this file out of the coding agent's context during the demo, or the "fix" is just reading the answer.

| # | Where it breaks | What a user sees | Who catches it |
|---|---|---|---|
| 1 | Widths 601–1100px (tablet landscape 1024, tablet portrait 768, phone landscape 844) | The nav links are hidden at ≤1100px, but the Menu button only appears at ≤600px. There is no way to reach the Shop or Cart from the header. | **Kane** (the flow can't navigate). The layout probe sees nothing wrong: hidden links are not a layout error. |
| 2 | Phones ≤480px (390, 375, 320) | `.cart-summary { min-width: 440px }` pushes the summary and the "Place order" button off the right edge. | **Both**: the probe measures the overflow; Kane can't press the button or sees it clipped. |
| 3 | Short screens ≤500px tall (phone landscape 844×390) | The promo bar turns into a full-screen overlay with its close button hidden. Everything is covered. | **Both**: the probe reports covered controls; Kane can't interact. |

Desktop (1920×1080) and laptop (1280×800) pass, which is the "works on my machine" starting point.

Expected fixes (any equivalent change is fine):
1. Show `.menu-toggle` at ≤1100px (and move the `.site-nav.open` dropdown styles to that breakpoint).
2. Remove `min-width: 440px` from `.cart-summary` (or use `min-width: 0; width: 100%`).
3. Keep the promo bar as a bottom bar on short screens and keep its close button visible.

To reset the demo, run `git checkout demo-shop/styles.css` (after committing the buggy version once).
