# Exclusive website source catalog

The user supplied these websites in `Websites.txt` and confirmed that **only these websites** may supply new UI elements or visual design references. Apple Developer HIG is a required **evaluation standard**, not an asset source. This catalog is deliberately exhaustive for the user-provided list. Check each live site again when using it; availability, catalog, prices, and terms change. A link from one of these sites to another domain does **not** add that domain to the allowlist.

## Source roles at a glance

| User-listed website | Use for | Source type | Important boundary |
|---|---|---|---|
| [Skiper UI](https://skiper-ui.com/) | distinctive shadcn-style components and interactions | downloadable/copyable components, some premium | inspect the exact free or Pro page and attribution terms |
| [unDraw illustrations](https://undraw.co/illustrations) | explanatory illustrations and empty states | downloadable SVG/PNG | read the current [license](https://undraw.co/license), especially automated access and redistribution terms |
| [Godly](https://godly.design/) | broad web/app composition, hero, CTA, footer, icon inspiration | curated gallery | linked third-party sites and their assets are **not** allowed sources |
| [Motion Primitives](https://motion-primitives.com/) | component-level motion examples | component gallery | may block automated access; do not invent inspection or bypass restrictions |
| [react-spring](https://www.react-spring.dev/) | spring and gesture behavior in a compatible React app | animation library/documentation | no visual asset by itself; assess runtime cost |
| [unlumen UI components](https://ui.unlumen.com/components) | component ideas and implementations | component gallery | verify exact item, terms, dependencies, and accessibility |
| [Magic UI components](https://magicui.design/docs/components) | selected animated React components | component documentation | distinguish free catalog from Pro offerings |
| [SmoothUI](https://smoothui.dev/) | overall catalog and documentation | component/section provider | use direct component or block page for approval |
| [SmoothUI components](https://smoothui.dev/docs/components) | controls, media, text, data and interaction components | component gallery | avoid installing a large animation stack for a trivial effect |
| [SmoothUI blocks](https://smoothui.dev/docs/blocks) | sections such as hero, FAQ, CTA, footer, pricing | section gallery | replace demo content and avoid wholesale page-template output |
| [Bklit UI](https://bklit.com/) | charts, data graphics, diagram-like views | data visualization components | choose a chart for the actual data question; check chart license and package cost |
| [Refero Styles](https://styles.refero.design/) | typography, palette, spacing, composition references | style gallery | famous brand styles are reference material, not a license to impersonate a brand |
| [Spline](https://spline.design/) | interactive 3D scenes/objects when justified | creation tool/community scenes | check scene ownership, export rights, runtime load and static fallback |
| [Deck Gallery](https://www.deck.gallery/) | editorial rhythm, story, diagram and graphic composition | curated deck/slide gallery | membership and slide copyright; inspiration unless reuse rights are verified |
| [Transitions library](https://transitions.dev/library.html) | transition patterns, button and menu feedback | interaction gallery | link may be unavailable; avoid effects on every control |
| [Motion](https://motion.dev/) | web/React/Vue animation APIs and examples | animation library/documentation | use for purposeful movement; respect reduced motion |
| [KokonutUI](https://kokonutui.com/) | React/Tailwind components and interaction alternatives | component registry/gallery | inspect exact component, dependencies, terms and fit |

`https://smoothui.dev/`, its component index, and its block index are **three URLs from one provider**, not three independent design systems. `Motion.dev` in the user's file is normalized to its official HTTPS home page. Do not treat a provider's outbound GitHub, social, demo, image CDN, or linked showcase as a separate UI source unless it is the official delivery endpoint of the **same approved element** and its rights are verified.

## How to use each provider

### Skiper UI

Look for a specific unusual component only when it solves an actual interaction problem. Examine the source code, demo behavior, mobile layout, keyboard support, and all imported packages. Its catalog distinguishes free and premium content. The provider's quick-start documentation currently says free components require attribution and Pro removes that requirement; re-check before use. A Pro badge is not permission to copy a preview. If the user has legitimate Pro access, propose the exact Pro component, disclose cost/access, and obtain approval before its official install route. Avoid importing visually elaborate effects without a clear purpose.

### unDraw

Search by the product's specific situation: onboarding, offline, no results, permission, success, error, or explanatory content. Inspect the **individual illustration** and whether its style is suitable for the brand. Use only when an illustration helps understanding or warmth; do not scatter generic people drawings across every section. Current license text permits ordinary commercial use and modification but has restrictions concerning redistribution, competing services, AI/ML development, trademarks, and automated linking/scraping/searching/downloading. Verify the current wording and acquisition method; do not automate a prohibited retrieval. Recolor/crop thoughtfully, preserve aspect ratio, compress, and set `alt` according to whether the illustration conveys meaning.

### Godly

Use the gallery to study specific page relationships: content hierarchy, rhythm, navigation density, CTA placement, footer organization, or how a product tells a story. It has filters for website/app work, heroes, calls to action, footers, icons, and social images. Do not download a featured site's logo, screenshot, brand image, or page source as if Godly licensed it. If the good idea is only visible on a linked external site, stay within what can be observed on Godly; that external site is outside this allowlist. Cite the **Godly listing URL** for a chosen reference and describe the pattern to adapt, not a clone to build.

### Motion Primitives

Use direct component pages to assess text, reveal, menu, drag, and feedback motion. A blocked browser or 403 means unavailable for that run. Do not switch to an unofficial mirror or produce copied code from memory. A motion reference should identify trigger, animated property, duration or spring, cancelability, reduced-motion route, and effect on focus or layout.

### react-spring

This is a **motion implementation tool**, not a ready-made illustration or page. Use it only in a compatible React project when a spring or gesture-following interaction clarifies manipulation or continuity better than simple CSS. Propose the exact relevant example/documentation page and the animation's role before bringing the package into a project. Do not add it beside another animation library without a reason. Ensure animations are interruptible and reduced-motion compatible.

### unlumen UI

Inspect exact component demos and code rather than copying the visual mood of the index. Check whether its dependencies and styling match the project. Test focus, keyboard, hover and touch behavior yourself. If only a preview is accessible or rights are unclear, keep it as a visual reference and choose a directly reusable allowed alternative.

### Magic UI

Choose small accents or a particular interface component when they support the product's story. Many animated components are tailored to marketing pages; avoid applying them throughout a dense app. The free catalog and Pro content have different access and licensing. Never imply that a paid section is free. Verify the exact component page, code/install method, and accessibility before proposing it.

### SmoothUI home, components, and blocks

Use the component catalog for a particular control or interaction, and the blocks catalog for a whole section such as FAQ, hero, CTA, footer, stats, or pricing. Compare full blocks to the product's information hierarchy before selecting; section templates are starting points, not finished copy. Check nested dependencies (Motion, GSAP, Tailwind, framework), loaded assets, and keyboard behavior. For approval, link the precise component or block page, **not** one of the three broad catalog URLs.

### Bklit UI

Define the data question before selecting the graphic: comparison, trend, distribution, relationship, composition, map, or flow. Compare the chosen chart with a simple table; a chart is useful only if it accelerates comprehension. Verify axes, scales, labels, units, source data, color distinction, zero baseline where applicable, screen reader alternative, and narrow-screen rendering. Do not display made-up metrics to beautify a dashboard. Propose the exact chart component page.

### Refero Styles

Use as a **reference** for palette, type hierarchy, spacing, and component relationships observed in real products. A generated style file does not automatically license a company's brand identity, trademark, photos, fonts, or assets. Distill general properties and adapt them into an original system. Do not recreate a recognizable named site's exact look. If specific colors or font choices come from a Refero listing, cite its exact URL in the approval proposal and validate any font's actual rights before use.

### Spline

Use a 3D object only when it helps demonstrate a product, teach a spatial concept, or creates a truly justified signature moment. Inspect the exact community scene or user-owned file, license/remix rights, access level, export/embed terms, and mobile/GPU impact. A public preview is not automatically licensed. Create or modify a scene through the permitted tool flow only after the proposed exact scene or object is approved. Provide a static fallback, accessible description, meaningful loading state, and reduced-motion behavior. Keep essential content and actions outside the 3D scene.

### Deck Gallery

Study editorial sequencing, contrast, chart annotation, and story pacing. Slides often have separate copyright and membership limitations. Treat deck/slide imagery as reference-only unless the exact slide's reuse rights are clear. An individual deck or slide link should support a proposal; a gallery home page is insufficient. Adapt composition without reproducing the original brand, copy, charts, or content.

### Transitions library

Study controls as feedback systems: before state, trigger, transition, after state, focus behavior, and reduced-motion alternative. The user's suggested uses include words, buttons, and dropdowns, but this is a menu of possibilities, not a reason to animate every button. If the library URL is inaccessible, mark it unavailable and choose another listed motion source. Do not infer source code from a video or screenshot.

### Motion

Use when controlled animation is needed across states, layout shifts, gestures, or scroll interactions and when the project supports its framework. It is an implementation source, not a requirement to animate. Prefer opacity/transform to costly layout effects, and ensure interaction is immediate and motion can be canceled. Re-check the current API and exact example page at task time.

### KokonutUI

Search its exact component pages for a suitable React/Tailwind component. Preview function and all states, inspect the registry output before installing, and check license and dependencies. Replace demo copy/content and reconcile tokens. Do not install an effect that duplicates a simpler existing control.

## Source selection notes

1. **Direct reuse candidates:** Skiper, unDraw, Motion Primitives, unlumen, Magic UI, SmoothUI, Bklit, Spline scenes with verified rights, KokonutUI.
2. **Implementation tools:** react-spring and Motion. Their examples can be adapted after exact-link approval, but the package alone is not a visual asset.
3. **Reference-first:** Godly, Refero Styles, Deck Gallery, and often Transitions. They can guide a design choice, but a listing or screenshot does not confer rights to included third-party assets.
4. **A source can change category per element.** Verify the exact page and its terms. Do not generalize from a site's marketing claim.
5. **Keep the full scan lightweight, the candidate inspection deep.** Record why a site did or did not matter so the user can see that the selection came from the entire supplied list.
