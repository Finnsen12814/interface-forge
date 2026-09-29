# Quality gates

## Design and interaction

- Purpose and primary action are quickly identifiable.
- Hierarchy survives grayscale and removal of animation.
- Spacing, type, icons, surfaces, and states form one system rather than a library collage.
- Real content handles length variation.
- Every visible control works; keyboard, focus, Escape, Enter/Space, containment, and return focus behave.
- Hover is not required; loading, empty, partial, offline, stale, validation, error, success, and destructive states work.
- Motion is interruptible with intentional reduced-motion behavior.

## Matrix and release

Inspect narrow/common phone, tablet/narrow desktop, standard and wide desktop. For Electron also minimum/maximized windows, scaling, and live resize. Find clipping, overflow, bad reordering, unreachable controls, long lines, tiny targets, and escaped overlays.

Run formatter, type check, lint, tests, and production build where available. Inspect console/network errors, bundle/media cost, semantics, accessible names, contrast, zoom/reflow, and announcements. Apply the web or Electron checklist.

Handoff: direction/rationale; key flow decisions; sources actually consulted; files changed; viewports/interactions checked; automation run; known limitations. Separate verification from inference.

## Source and approval gate

- The full `Websites.txt` catalog was considered, and relevant candidates were inspected at exact pages.
- Every imported external element has an exact allowed-source URL, a documented role, a verified acquisition method, and a clear user approval obtained **before** download/copy/install/embed/integration.
- The approved candidate still matches the implemented item. A replacement or premium upgrade received its own approval.
- A gallery reference was not mistaken for rights to use a linked site's logo, screenshot, photography, font, or code.
- Current license, cost, attribution, dependencies, and automated retrieval terms were reviewed. Required notices and provenance are retained.
- No unapproved stock source, generated visual asset, third-party gallery destination, or copied brand identity entered the product.

## Usability gate

Ask a first-time-user question on each important screen: What is this, what can I do here, what happens next, and how do I recover? If the answers require explanation outside the UI, revise hierarchy or copy. Walk the primary task start to finish. Confirm the main CTA does something real, the result is visible, and failure leaves a path forward. Then check a secondary task and a disrupted path.

Inspect every visible control. It needs a real outcome or should be removed. Check default, hover where relevant, pressed, focus-visible, disabled, loading, validation, error, and success states. Menus and dialogs need logical focus entry, Escape, focus return, and touch behavior. Undo or confirmation should match the actual risk of the action. Ensure all important messages are perceivable without color, hover, or animation.

## Visual cohesion gate

Compare imported components side by side. Type, spacing, corners, border weight, icon style, colors, shadows, and timing must belong to one system. Remove provider demo content and meaningless decoration. Inspect page rhythm: not every section should have the same three-card grid, and not every action should be a glowing pill. Check the interface in grayscale and without motion; hierarchy should remain. Evaluate whether the page still looks specific to the product when brand words are temporarily hidden.

## Apple HIG application gate

Record which official HIG topics were read for this task and the concrete decisions they influenced. At minimum check purpose, agency, familiarity, flexibility, simplicity, craft, and delight. For interaction work also check feedback, accessibility, layout, writing, buttons, and motion as relevant. Do not claim Apple compliance merely because the interface resembles an Apple screenshot; evaluate the reasons behind the guidance.

## Technical and performance gate

Build and run the app. Inspect runtime logs, network requests, missing assets, console errors, large dependencies, and unintentional external calls. Test a realistic slow or offline path if the flow depends on the network. Check image dimensions, compression, lazy loading, font loading, and whether imported motion stresses CPU/GPU. Confirm responsive reflow and no clipping or horizontal overflow.

For accessibility, combine automated checks with keyboard and rendered inspection. Test visible focus, semantic order, labels, status announcements, contrast, text scaling/zoom, target size, reduced motion, and screen reader where possible. Automated scores cannot prove a useful interaction. Report observed results and gaps precisely.

## Release-specific gate

For a whole website, use [web-production.md](web-production.md) as the release checklist: policy/terms, consent, metadata, favicon, social preview, sitemap, robots, 404, links, forms, abuse protection, media, HTTPS, secrets, speed, mobile, and CTA. For mobile, use [mobile.md](mobile.md). For desktop, use [electron.md](electron.md). Do not mark a hosting-dependent item verified from local code alone. Do not fabricate legal or business facts to complete a checklist.

## Handoff template

Keep the final report concise but concrete:

1. **What changed and why:** main flow, visual system, and specific user benefit.
2. **Sources:** exact imported element links, what was adapted, approval and any attribution obligation; distinguish reference-only sites.
3. **Verification:** viewports/devices, states and interactions, build/tests, accessibility/performance checks actually run.
4. **Open items:** missing business facts, deployment checks, inaccessible source, unclear license, or other limitation with a next action.

Do not equate a passing build with a finished UI. A design is ready only when the intended task is usable and the source, legal, and production gates applicable to it are satisfied.
