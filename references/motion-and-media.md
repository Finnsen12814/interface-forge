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

## Source-to-product motion specification

For each approved motion pattern from Motion Primitives, Transitions, SmoothUI, Magic UI, Skiper, Motion, or react-spring, write a tiny specification: trigger, visual property, meaning, expected duration/spring feel, interrupt behavior, focus behavior, reduced-motion behavior, and performance budget. If the meaning field is empty, remove the effect. Repeated controls deserve less motion than a rare transition between major states.

Do not attach the same flourish to every button, dropdown, heading, and card. This creates fatigue and an obvious component-demo appearance. Motion should follow cause and effect: a pressed button responds immediately; a panel appears from where the user opened it; a saved state settles rather than celebrating forever. Animations must not delay navigation or form submission.

Respect `prefers-reduced-motion`, but consider the *purpose* rather than merely setting duration to zero. Replace spatial movement with opacity or direct state change where needed. Keep focus order and screen-reader announcements independent of animation timing. Make auto-playing media pausable, and do not use scroll-jacking or cursor-following as a basic navigation mechanism.

## Illustrations, icons, and images

Before proposing an image, define its job: explain a concept, show real product content, establish an appropriate tone, or support memory. Search allowed sources for that job. For unDraw, use a particular illustration page and review its current license and retrieval rules. For gallery screenshots, distinguish inspiration from rights to ship. Do not hotlink an asset from an unrelated site found through a gallery.

After approval, obtain the original through an allowed official method, keep provenance, choose a responsive size, compress without losing useful detail, and reserve dimensions to avoid layout shifts. Use `alt` text for information the image conveys; use empty `alt` for purely decorative images. Provide a visible text alternative when a diagram carries essential relationships. Ensure crops do not hide the subject on mobile.

Use a consistent icon treatment. Imported components frequently bring separate icon sets; normalize stroke, optical size, alignment, and accessible names. Do not add an icon merely to make each list item look decorated. If a provider's component includes proprietary logos or external images, replace them with approved assets or remove them.

## Spline and interactive 3D

3D is a significant runtime choice. Verify exact scene ownership, remix/export rights, interaction model, load weight, GPU impact, keyboard/touch accessibility, and whether the experience remains useful if the scene fails. Avoid making the main CTA or required information part of the canvas. Provide a static poster from a permitted route, a loading/error state, a low-power fallback, and reduced-motion handling. If a scene is hosted remotely, document the external request and privacy impact.

An existing product may need only a small 3D accent; do not use a full-screen scene to conceal weak content. If the same message can be communicated more clearly with text and a simple sourced illustration, choose the simpler path.

## Technical integration checks

Review copied component code and installation output before accepting it. Remove demo analytics, remote fonts, placeholder images, unsafe raw HTML, hardcoded credentials, intrusive observers, and package duplication. Avoid loading a second large animation library for one effect. Use stable layout dimensions, transform/opacity where possible, and lazy load below-the-fold media. Test repeated interaction, interruption, rapid clicks, background tabs, and slow devices.

Record the exact source page, retrieval method, local file, modification, and license in the project's provenance note. Every approved external element should be traceable later. The approval procedure is in [sourcing-and-approval.md](sourcing-and-approval.md).
