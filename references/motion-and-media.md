# Motion, media, illustration, and 3D

Motion clarifies cause/effect, continuity, status, emphasis, or manipulation. Otherwise remove it. Define micro feedback, component transitions, and rare signature moments; most screens use only the first two.

- Keep frequent feedback fast; use consistent easing/duration tokens.
- Prefer transform/opacity and interruptible interactions.
- Never delay primary actions for entrance animation.
- Respect `prefers-reduced-motion`; replace spatial movement when needed.
- Pause autonomous media and avoid control-impairing parallax/cursor effects.

Use Motion for general orchestration, React Spring when gesture continuity or physics matters, and CSS for simple transitions. Choose capability, not demo spectacle. Buttons/menus need stable geometry, immediate feedback, focus visibility, Escape, and predictable focus.

Use imagery to explain, establish tone, or show product—not fill space. Provide meaningful alt text or empty alt for decoration, responsive formats, compression, reserved dimensions, and lazy loading below the fold.

Use Spline/3D only when it materially explains the product or creates a justified signature. Provide a static poster, loading state, reduced-motion route, non-3D alternative, and low-power/mobile budget. Never make critical content depend on 3D.

