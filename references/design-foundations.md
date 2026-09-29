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

