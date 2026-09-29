# Design foundations

Choose a direction without naming a framework. Define useful tensions: calm/energetic, dense/spacious, editorial/utilitarian, warm/technical, familiar/expressive. Pick a dominant side for each relevant axis. Choose one signature composition or interaction tied to the product; do not stack signatures.

## Tokens

Use semantic variables for background, surface, elevated surface, text, muted text, border, focus, primary/foreground, destructive, warning, success, and selection. Add dark mode only when required or existing.

- Keep body and muted text readable.
- Derive spacing from a small scale with optical exceptions.
- Use radii by role; inputs, cards, dialogs, and badges need not match.
- Borders structure; shadows indicate elevation. Avoid heavy use of both.
- Define display, page title, section title, body, label, caption, and code/data roles.
- Limit font families and weights; use tabular figures for numeric data.

## Hierarchy

Start with content order and reading path. Use whitespace to group before adding boxes. Density follows task frequency. Keep readable line lengths. Favor progressive disclosure. Responsive design is content reflow, not merely smaller type.

## Icons

Use one family unless a second has a defined role. Match stroke, optical size, corners, and fill. Use familiar symbols for common actions. Pair ambiguous icons with text/tooltips; icon-only controls need accessible names and adequate targets. Prefer the project's existing set. Custom icons suit product-specific objects, not standard actions.

## Content and platform

Use specific action labels. Errors say what happened and how to recover. Empty states explain and offer a useful next action. Avoid fake metrics. Web UI respects URLs, history, scrolling, and form semantics. Electron UI supports keyboards, resizing, dense work, and clear navigation/workspace/transient-panel separation.

## A design brief that prevents collage

Before choosing sourced elements, write a five-line brief in task notes: (1) who uses this screen and why, (2) primary job and success signal, (3) desired feeling, (4) density and platform constraints, (5) motifs or clichés to avoid. State one visual concept in ordinary language, such as "quiet research desk with strong data hierarchy" or "warm local-service booking flow." The concept should help reject attractive but mismatched catalog items.

Create a **component role map**. For each screen, identify: page frame, navigation, primary action, content unit, input, feedback, and secondary action. An element from an allowed website must fill one of those roles. If it fills none, it is decoration and should usually be omitted. A source choice should be explainable as `this element helps people do X because Y`; "it looks modern" is insufficient.

## Information architecture and hierarchy

Audit the current screen before styling. List every visible block and control. Merge duplicates, move secondary information closer to where it is needed, and remove empty containers. Order content by the user's decision sequence, not by which imported block is most visually striking. Make the primary action visible at the point of decision. Repeated primary CTAs on one short screen often compete rather than help.

Use a clear reading path: heading that names the task, short context when required, decisive content, primary action, supporting detail, and escape/recovery. Align elements that belong together. Use whitespace, typography, and shared edges before adding cards. Limit card nesting; a page of cards inside cards destroys hierarchy. Group by meaning rather than equal box dimensions. Let dense tools be appropriately dense; do not turn a productivity app into a sparse marketing page.

Treat mobile as a different available space, not a scaled desktop screenshot. Decide what stays visible, what reflows, what becomes a menu, and what can move lower without hiding the main action. Long titles, translation expansion, large text, empty results, and error messages are normal content, not edge decorations. Avoid arbitrary fixed heights that clip real content.

## A coherent token system

Use a small number of semantic tokens and explain where each applies. Typical roles: canvas, surface, raised surface, text, muted text, border, strong divider, focus, primary action, selection, success, warning, danger. Tokens should express **meaning**, not provider names. Imported components must map to these roles instead of carrying their own unrelated palette.

Create a disciplined type hierarchy: display only when the product needs it; page title; section title; body; label; caption; numeric/data style. Choose fonts from rights-cleared sources and existing product assets; a Refero style listing alone does not grant a font license. Use weight and size for priority, not seven competing fonts. Make line length comfortable, especially for legal and help pages. Give numerals tabular alignment when comparisons matter.

Define spacing as a repeatable rhythm. Start with consistent steps, then use optical corrections for alignment. Use surface elevation sparingly: borders for grouping, shadows for layers, color for state. Consistent radius is useful, but not every item needs the same soft pill. Verify contrast in every state, including disabled and muted text. A brand color that fails contrast can remain an accent while text/actions use an accessible shade.

## Human rather than generated

Generic UI is often caused by repeated defaults: centered headline, vague subtitle, three equal feature cards, fake dashboard, purple-to-blue glow, glass panel, star field, and a gradient button. Remove these unless the product's audience and content actually justify them. Distinctiveness usually comes from specificity: a real workflow, useful content, considered proportion, product language, and a few well-made details.

Write interface copy from the user's point of view. Button labels should name the action (`Save invoice`, `Invite teammate`) rather than marketing fluff (`Unlock potential`). Empty states should explain what is empty and the first useful move. Success should confirm the actual result. Error text should give the next step. Avoid fabricated reviews, metrics, avatars, company logos, and chart data from demos; they reduce trust even when the layout is attractive.

Use one icon family or one coherent custom set, not whatever each imported component shipped with. Standard actions benefit from standard metaphors. Icons should not replace clear text where ambiguity matters. If an illustration or 3D scene is present, it should communicate something the copy alone would struggle to make clear. Do not insert an image into every section to satisfy a visual quota.

## Design-system integration of sourced elements

After exact-link approval, strip provider demo styling down to the meaningful behavior and structure. Map its colors, type, spacing, radii, shadows, z-index, and motion to product tokens. Check interaction contract: default, hover if useful, pressed, focus-visible, disabled, loading, invalid, success, and high-contrast where applicable. Remove incidental package logos, sample content, hardcoded IDs, external tracking, and unsupported variants.

If two approved components have incompatible visual languages, choose one as the baseline and adapt the other. If their APIs or styles cannot be reconciled without breaking the interaction, propose a different allowed source rather than shipping a collage. Document meaningful deviations from the source so future maintainers understand the component.

## Visual review loop

Inspect the rendered result at a narrow phone, a common laptop width, and a wide desktop width. Also inspect long content, empty content, error state, loading state, and zoomed text. Temporarily remove animation and view in grayscale: if hierarchy disappears, fix layout and type before restoring effects. Compare the UI against the five-line brief and the Apple HIG review questions. Remove any flourish that slows the main task.
