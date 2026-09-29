# Electron application guidance

Design for resizable windows, keyboard/pointer, dense repeated work, multiple displays, scaling, and long sessions. Define minimum useful dimensions and narrow/normal/wide behavior. Support standard shortcuts and menus. Custom title bars require explicit draggable/interactive regions and platform-safe controls.

Persist window size, position, theme, and workspace conservatively; recover off-screen windows. Make updates, offline status, conflicts, long tasks, and restart requirements visible and recoverable.

## Security

- Keep renderers unprivileged: context isolation on, sandbox when feasible, Node integration off for remote/untrusted content.
- Expose a narrow typed preload API; validate IPC sender/channel/payload/response.
- Never interpolate untrusted input into shell commands or open arbitrary external URLs.
- Restrict navigation/window creation and use a deliberate CSP.
- Keep secrets out of renderer bundles/logs and verify update provenance.

Virtualize large lists/tables/logs/trees. Distinguish selection, focus, hover, and active-window state. Test high DPI, scaling, themes, reduced motion, long filenames, localization expansion, clipboard, drag/drop, native menus, permissions, and quit/relaunch recovery.

## Desktop-specific design pass

Desktop apps often support long sessions and repeated actions. Design for a compact window and a maximized window, not only one screenshot size. Define how sidebar, content, inspector, and transient panels behave at minimum, normal, and wide widths. Preserve the user's location and selection while resizing. Avoid mobile-scale whitespace that forces unnecessary scrolling, but keep text legible and groups clear.

Use familiar shortcuts and application menus for frequent work. A command palette can accelerate expert use but must not be the only route to an action. Clarify global versus workspace-specific commands. Support keyboard traversal, focus visibility, Escape/Enter conventions, and predictable context menus. Drag-and-drop needs an equivalent non-drag route. Show clear feedback for long-running tasks, sync, conflicts, and offline mode; prevent losing work on close or reload.

Imported web components need desktop adaptation. A showy marketing hover state can be distracting in a work tool. A custom title bar must not block window dragging or controls. An animated drawer should not trap focus or alter layout unpredictably. Charts should support precise pointer inspection without relying on hover alone. A Spline scene should never consume resources needed for the primary work surface.

## External UI source gate

Only the websites in [source-research.md](source-research.md) may provide new visual elements or component ideas. Even if Electron can load arbitrary web content, do not embed a linked gallery site or remote component as a shortcut. Propose the exact listed-site element and wait for approval before import. Then inspect network calls, font/image URLs, script execution, package dependencies, and CSP impact. Prefer local, reviewed code and assets where rights permit.

## Verification

Check minimum window size, live resizing, maximized and high-DPI displays, light/dark modes if available, OS scaling, narrow sidebars, long names, dense tables, menu/shortcut access, keyboard-only completion of the main flow, screen-reader labels, and recovery after restart. Test active/inactive window styling and focus restoration when dialogs close. Confirm that any imported animation does not lower performance during long sessions.
