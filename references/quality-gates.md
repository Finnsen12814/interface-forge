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

