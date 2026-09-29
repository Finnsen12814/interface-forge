---
name: interface-forge
description: Research, design, implement, and audit distinctive production-grade UI/UX for websites and Electron desktop apps. Use for new interfaces, redesigns, component and icon selection, design systems, interaction and motion work, responsive behavior, accessibility, or visual polish. Do not use for backend-only work or generic graphic design unrelated to a product interface.
---

# Interface Forge

Create coherent interfaces that feel designed for the product rather than assembled from fashionable fragments. Treat source sites as research libraries, not as a style to copy. Preserve the user's framework, product intent, brand, and authorization boundaries.

## Route the request

1. Inspect the existing product, repository, screenshots, and constraints before proposing a direction. Do not replace a working stack merely to use a preferred library.
2. Identify the job: `explore`, `specify`, `implement`, `redesign`, or `audit`. If the request spans several, follow that order.
3. Read only the references needed:
   - Every UI task: [design-foundations.md](references/design-foundations.md)
   - External research or component sourcing: [source-research.md](references/source-research.md)
   - Flows, states, forms, navigation, or information architecture: [ux-and-components.md](references/ux-and-components.md)
   - Motion, transitions, 3D, or delight: [motion-and-media.md](references/motion-and-media.md)
   - Website delivery: [web-production.md](references/web-production.md)
   - Electron/desktop delivery: [electron.md](references/electron.md)
   - Final review, redesign, or audit: [quality-gates.md](references/quality-gates.md)
4. For implementation, inspect repository instructions and installed dependencies first. Prefer existing primitives and tokens. Add dependencies only when their value exceeds their cost and installation is authorized.

## Working method

### Frame

Write a compact internal brief: primary user and job; main action and success condition; information hierarchy and states; platform/input modes; brand traits and clichés to avoid; technical, accessibility, performance, and legal constraints. Infer low-risk details. Ask only when a missing decision would materially change the product.

### Research

When current sources can be browsed, visit a small relevant set from the source map. Search by the actual UI problem, not vague adjectives. Record why each reference matters. Check docs, license, accessibility, dependencies, and maintenance before reusing code or assets. Never claim a source was inspected when inaccessible.

Derive an original direction from multiple references. Never reproduce a complete page, brand identity, proprietary asset, or paid component without permission. A screenshot is evidence, not a specification.

### Systematize

Decide one visual concept with 3–5 traits; semantic color, type, spacing, radius, border, elevation, and motion tokens; layout and density; icon family; component variants and states; responsive and window behavior. Repetition creates identity; arbitrary novelty creates noise.

### Build

Build task flow and hierarchy before decoration. Prefer semantic HTML and accessible, composable primitives. Make every visible control functional. Preserve business logic unless explicitly changing it. Use real or credible content. Inspect representative sizes and fix overflow, clipping, wrapping, focus, reduced motion, keyboard use, and empty/loading/error states. Test Electron layouts in compact and large windows.

### Reject generic output

Avoid stacking gradient headlines, purple glow, glass cards, oversized rounded containers, interchangeable feature cards, excessive pills, floating islands, decorative charts, or animation everywhere. Do not place arbitrary icons beside every label. Do not center everything, elevate every surface, or round every corner. Keep at most one memorable motif, supported by disciplined typography, spacing, content, and interaction.

### Verify

Run project checks and relevant quality gates. Report direction, material changes, verification, and limitations. Do not present a mock interaction as implemented behavior.

## Non-negotiables

- Accessibility and legibility outrank spectacle.
- Motion communicates continuity, feedback, or hierarchy.
- Icons supplement meaning and use accessible names.
- Avoid dark patterns, deceptive urgency, obstructive consent, and disguised advertising.
- Do not invent legal compliance; flag jurisdiction-specific decisions for qualified review.
- Respect source licenses and trademarks.
- Research must answer a named design question.

