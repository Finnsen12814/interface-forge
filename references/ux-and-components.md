# UX, components, and states

Map the shortest successful path, then discovery, interruption, recovery, and return. For each step identify user question, required information, action, feedback, escape, and recovery.

## Navigation

Use top navigation for few public destinations; sidebar for persistent multi-area tools; tabs for sibling views; breadcrumbs for deep hierarchy; command palettes as accelerators; drawers for temporary secondary work. Preserve location/back behavior and align active state, title, and context.

## Components

Use the simplest component that preserves meaning. A select is not automatically a command menu; a tooltip is not documentation; a carousel is not an archive; a modal is not a multi-page workspace. Prefer accessible primitives for dialogs, menus, popovers, comboboxes, tabs, and tooltips.

Interactive components need default, hover where relevant, pressed, focus-visible, disabled, loading, invalid/error, and high-contrast behavior. Add variants only for real contexts.

## Forms and feedback

- Persistent labels; placeholders are examples.
- Match field type/input mode to data.
- Validate near fields without punishing mid-entry; preserve values after errors.
- Summarize long-form errors and manage focus.
- Explain destructive consequences and prevent duplicate submission.
- Use local feedback for local actions; toasts are not for critical information.
- Show honest progress; skeletons approximate final geometry and should not flash.

Design empty, loading, partial, offline, permission-denied, validation, error, success, and stale states. Prefer undo for recoverable destruction; reserve confirmation for meaningful consequences.

## Data visualization

Start with the question: compare, trend, distribute, relate, compose, or locate. Use direct labels, consistent scales, accessible palettes, and text/table alternatives. Avoid 3D charts, misleading axes, and metrics that do not support decisions.

