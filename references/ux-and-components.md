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

## Map the journey before selecting components

For the core task, write the shortest complete path: entry point → understand options → act → receive feedback → confirm outcome → return or continue. Then map two disruptions: an invalid input and a failed network/data operation. At every step ask what the person is trying to know, what they can do, whether the next step is obvious, and how they recover. A component from an allowed site is good only when it improves one of these steps.

For an existing app, walk the real flow rather than relying on a screenshot. Note dead controls, hidden prerequisites, confusing labels, repeated choices, context loss, surprising navigation, and missing response. Improve the highest-friction path first. Do not redesign a settings icon while checkout, saving, or onboarding remains broken.

## Navigation patterns and orientation

Navigation should make location, available destinations, and return path clear. Choose top navigation for a few public sections, sidebar for persistent multi-area work, tabs for sibling content, breadcrumbs for depth, and a command palette for expert acceleration. Do not use all of them at once. A floating dock or animated menu from a catalog must still explain destinations and support keyboard/touch.

On narrow screens, decide how the information architecture compresses. Preserve the primary destination and action. Avoid a hidden menu containing the only way to complete the task. Use URLs and history meaningfully on the web; reloading or sharing a route should restore the expected view where feasible. In Electron, preserve workspace and selection where it helps long sessions.

## Choosing controls by meaning

Use a button for an action and a link for navigation. Use a checkbox for independent options, radio group for one of several explicit choices, toggle for an immediate persistent setting, select for a compact known list, combobox for searchable or creatable choices, dialog for a short focused interruption, and a full page for long multi-step work. Do not style a control so heavily that people cannot tell what it is. A sourced animation cannot change the control's basic meaning.

For every interaction, document: trigger, state change, success feedback, failure feedback, dismiss/escape, keyboard path, focus destination, and touch path. A component with a beautiful default state but no credible error/disabled state is unfinished. Hover is an enhancement, never the only way to reveal essential information.

## Forms that help completion

Put labels outside fields so meaning survives typed content. Mark required fields and format expectations before submission. Validate when the person can act on the message; do not show red errors at the first keystroke. Pair invalid fields with specific, nearby explanations and a summary for long forms. Preserve all values after failure. Move focus to the problem when it is otherwise hard to find. Do not clear a form on a server error.

For asynchronous submission, show progress without changing button width or losing focus. Prevent accidental duplicate submission. Explain delayed completion and whether it is safe to leave. For risky actions, state consequences in plain language and offer undo where possible. Confirmation dialogs are for meaningful irreversible outcomes, not every save.

## State design inventory

Each meaningful content view should account for:

- **First use / empty:** Explain what belongs here, why it matters, and one useful next action.
- **Loading:** Preserve layout or display proportionate progress; avoid flashing skeletons for very short waits.
- **Partial data:** Show what is available and what is missing; avoid implying completeness.
- **Offline / timeout:** Preserve work and provide retry or local continuation where possible.
- **Permission denied:** Explain the reason and how to request or change access.
- **Validation error:** Keep values, show specific corrections, and re-run the action without extra friction.
- **System error:** Say what failed, whether data was saved, and what to do next.
- **Success:** Confirm the real outcome and provide a sensible next step.
- **Stale or conflicting data:** Make recency and conflict resolution understandable.

Do not use an illustration as a substitute for an explanation. An unDraw image can soften an empty state, but the action and copy must still work without it.

## Feedback and notifications

Match feedback to impact. A small local action needs local response. A background save can use a subtle status indicator. A critical failure needs an explanation near the affected content, not an ephemeral toast that disappears. Use toasts for supplementary confirmation and provide enough time to read them. Do not make animations the only evidence of success. Announce significant state changes accessibly.

## Data and charts

Choose a Bklit or other allowed chart only after naming the question. A trend should show time units and notable changes; a comparison should use aligned scales; a distribution should expose range and outliers; a relationship chart should not imply causation. Label directly where possible. Provide text or table access to values. Show uncertainty or missing data honestly. Test small screens and color-independent reading. If the chart does not help a decision, use a simple number or table instead.

## Copy and trust

Use the product's actual vocabulary. Prefer short, concrete sentences, especially for actions and errors. Explain limits and costs before commitment. Avoid fake social proof and urgency. Write 404 and empty-state copy that sounds like a helpful product, not a joke the user must decode. For privacy and consent, tell people what happens if they agree or decline. Do not imply analytics or third-party scripts are active when they are not.

## Data visualization

Start with the question: compare, trend, distribute, relate, compose, or locate. Use direct labels, consistent scales, accessible palettes, and text/table alternatives. Avoid 3D charts, misleading axes, and metrics that do not support decisions.
