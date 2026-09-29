# Electron application guidance

Design for resizable windows, keyboard/pointer, dense repeated work, multiple displays, scaling, and long sessions. Define minimum useful dimensions and narrow/normal/wide behavior. Support standard shortcuts and menus. Custom title bars require explicit draggable/interactive regions and platform-safe controls.

Persist window size, position, theme, and workspace conservatively; recover off-screen windows. Make updates, offline status, conflicts, long tasks, and restart requirements visible and recoverable.

## Security

- Keep renderers unprivileged: context isolation on, sandbox when feasible, Node integration off for remote/untrusted content.
- Expose a narrow typed preload API; validate IPC sender/channel/payload/response.
- Never interpolate untrusted input into shell commands or open arbitrary external URLs.
- Restrict navigation/window creation and use a deliberate CSP.
- Keep secrets out of renderer bundles/logs and verify update provenance.

Consult current official Electron security docs because recommendations evolve.

Virtualize large lists/tables/logs/trees. Distinguish selection, focus, hover, and active-window state. Test high DPI, scaling, themes, reduced motion, long filenames, localization expansion, clipboard, drag/drop, native menus, permissions, and quit/relaunch recovery.

