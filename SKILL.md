---
name: interface-forge
description: Website-first UI/UX research, redesign, and implementation for websites, desktop apps, and mobile apps in Codex or Claude Code. Use for interfaces, flows, components, visual assets, motion, accessibility, and polish. Source all new UI elements only from the allowlist in Websites.txt; propose each exact element URL and obtain the user's approval before importing it. Read Apple's current Human Interface Guidelines as a quality benchmark.
---

# Interface Forge

Build interfaces that feel useful, calm, precise, and human. This skill is for Codex and Claude Code. It supports new interfaces, redesigns, component-level improvements, UX audits followed by implementation, and production reviews for websites, desktop apps, and mobile apps. Preserve the product's purpose, framework, data, business behavior, and brand constraints.

## The contract

1. **Only the websites in the source catalog may supply new UI elements, code, visual assets, animation patterns, colors, typography references, 3D scenes, charts, or page compositions.** The catalog is a maintained transcription of the user's `Websites.txt`: [source-research.md](references/source-research.md). Do not add a stock site, icon library, gallery, AI image generator, search result, linked showcase site, or other visual source. Existing product-owned content and user-provided materials are product inputs; do not present them as sourced from a new site.
2. **Research before selecting.** At the start of every relevant task, scan the entire allowed-source map, inspect relevant categories and exact candidate pages, and compare candidates against the product's real task. A broad inspiration gallery is not an asset license. A library's home page is not an exact component link.
3. **Ask before every external element enters the project.** After finding and vetting a candidate, tell the user: `Ich möchte Name + EXAKTE ELEMENT-URL für konkreten Zweck verwenden und so anpassen: kurze Anpassung. Passt das?` Present the real URL as a clickable link. Include any cost, attribution, license uncertainty, or dependency that matters. Wait for a clear yes **before downloading, copying, installing, embedding, or integrating** that element. Ask again if the element or URL changes. For several candidates, present a compact numbered list with a separate yes/no decision for each; do not interpret silence, a time delay, or approval of one item as approval of another. Continue independent layout, code, and UX work while waiting. See [sourcing-and-approval.md](references/sourcing-and-approval.md).
4. **Read current Apple Developer Human Interface Guidelines** at the start of design work, especially Design principles and the topics matching the task. Use them as criteria for purpose, agency, familiarity, accessibility, feedback, layout, writing, and motion. They are documentation, not an additional asset source or a demand to copy Apple's appearance. See [apple-hig.md](references/apple-hig.md).
5. **Adapt; never drop in a demo unchanged.** After approval, obtain the source through its supported route, record provenance and rights, and integrate it into one coherent visual and interaction system. Replace demo copy/data, reconcile tokens, implement all states, keyboard behavior, responsiveness, reduced motion, performance, and tests. If a site's terms prohibit the proposed download or use, do not bypass them; choose another allowed source and ask again.
6. **Finish production details.** For websites, implement the relevant items from the user's checklist, including custom 404, privacy and terms pages, SEO/social metadata, favicon, sitemap/robots, image and link hygiene, accessible forms, consent-aware analytics, HTTPS and front-end secret review, responsive behavior, and a clear primary call to action. Do not claim legal compliance from a template. See [web-production.md](references/web-production.md).

## How to work

### 1. Understand the product

Inspect repository instructions, app structure, current UI, screenshots, content, target audience, platform, framework, existing dependencies, and current behavior. State the user goal and the primary action on each affected screen. Identify the highest-friction flow, intended tone, device sizes, and constraints. If the task is only an audit, diagnose without importing assets; if the user then wants fixes, follow the sourcing gate.

Do not replace a working stack merely to install a showcase component. Do not remove product behavior or user data for a visual redesign. If a user request conflicts with accessibility, explain the concrete problem and propose the nearest usable version.

### 2. Research all allowed sources, then shortlist

Read [source-research.md](references/source-research.md) and make a source pass across **every listed website**: relevant candidate, reference-only, incompatible, unavailable, or unnecessary, with a reason. Search within relevant sites for the actual problem (`compact sidebar`, `chart with comparisons`, `accessible dropdown`, `empty state illustration`) instead of `modern UI`. Review exact demos, code/docs, supported framework, dependencies, interaction states, responsiveness, license, price, and download method. Keep a record of page URL and access date. If a site is blocked, say so and move to another allowed site; never pretend it was inspected.

Shortlist the best fitting source per role, not the flashiest one. For a high-impact component, compare at least two candidates when available. Prefer a compatible, accessible, light component over a spectacular one that obstructs the task. Prefer direct source pages from an allowed domain. Do not follow outbound gallery links as new sources. If no legal, usable candidate exists, stop that import and tell the user which requirement cannot be met within the allowlist.

### 3. Propose exact sources and wait

Present the intended use in terms the user can evaluate: screenshot or clear description if useful, **exact clickable element URL**, location in the app, adaptation plan, and any meaningful caveat. Ask the exact approval question before touching the project with that source. A page-wide mood board does not approve separate assets. A prior approval applies only to the named candidate and role. Document the answer in the task notes. The full procedure and message pattern are in [sourcing-and-approval.md](references/sourcing-and-approval.md).

### 4. Design one coherent system

Read [design-foundations.md](references/design-foundations.md). Choose an experience appropriate to the product, not a default AI aesthetic. Establish hierarchy, layout, typography, spacing, color roles, surfaces, icon treatment, motion, and component states before integrating imports. Retain recognizability when improving an existing product. Use fewer, stronger decisions; remove redundant panels and actions. Content must sound like a person who knows the product: concrete, concise, helpful, and honest.

### 5. Build the full task flow

Read [ux-and-components.md](references/ux-and-components.md). Implement entry, navigation, primary action, feedback, errors, recovery, and return. Make every visible control perform its apparent task. Use native and semantic controls where possible. Keyboard, screen reader, pointer, touch, zoom, and narrow layouts are first-class. Make motion explain state; consult [motion-and-media.md](references/motion-and-media.md) for imported transitions, Spline, illustration, and animated components. For Electron, also read [electron.md](references/electron.md). For mobile apps, read [mobile.md](references/mobile.md).

### 6. Verify and report

Read [quality-gates.md](references/quality-gates.md). Run meaningful project checks and inspect the UI at representative sizes and states. Verify actual behavior, not just compilation. Check source records, third-party notices, asset sizes, broken links, console errors, contrast, focus, reduced motion, and page speed. State what was verified, what could not be verified, and any unresolved license, legal, or deployment decision. Keep the user informed during long work.

## Routing by task

| Task | Read |
|---|---|
| Every UI/UX task | [source-research.md](references/source-research.md), [sourcing-and-approval.md](references/sourcing-and-approval.md), [apple-hig.md](references/apple-hig.md), [design-foundations.md](references/design-foundations.md) |
| Flow, navigation, forms, states, copy | [ux-and-components.md](references/ux-and-components.md) |
| Import, asset, motion, 3D, animation | [motion-and-media.md](references/motion-and-media.md), [sourcing-and-approval.md](references/sourcing-and-approval.md) |
| Website delivery | [web-production.md](references/web-production.md) |
| Electron or desktop delivery | [electron.md](references/electron.md) |
| iOS, Android, Flutter, or React Native delivery | [mobile.md](references/mobile.md) |
| Final review or audit | [quality-gates.md](references/quality-gates.md) |

## Rules that prevent an "AI-generated" feel

- Let the product's actual content and audience determine visual choices. Do not begin with a gradient hero, floating glass cards, purple glow, fake dashboards, meaningless metrics, generic people art, or interchangeable feature cards.
- Use one clear focal point per view and one obvious primary action per decision point. Align and group before adding borders or containers. Surface only controls needed now; preserve discoverability for secondary actions.
- Build a consistent icon, type, color, spacing, and motion language. Do not compose a page from unrelated library demos. A component earns its place through the user's task, not novelty.
- Prefer specific microcopy, true examples, real data, actionable error text, forgiving interactions, and straightforward consent. Avoid fabricated testimonials, social proof, urgency, and opaque AI-themed decoration.
- Keep intentional character: a useful illustration, a quiet accent, a good transition, or a distinctive data view can be memorable. Do not animate every button or import 3D merely because the catalog offers it.

## Boundaries

- The allowlist governs **new UI sourcing**. Apple's official HIG is the only extra design reference required here. Project files and the user's content are inputs, not a new website catalog.
- Paywalled or premium content requires legitimate access. Do not evade login, copy protected previews, scrape blocked pages, or assume every showcased image is reusable.
- An approved visual choice does not authorize paying, publishing, analytics activation, or other externally consequential actions beyond the user's request.
- A 404 page, privacy page, and terms page must be real routes with usable content and navigation. When business or legal facts are unknown, prepare clearly marked drafts and request the missing facts before asserting them as final.
- If the implementation stack cannot use an approved source directly, explain the adaptation or request a compatible candidate. Do not install a second framework or ship a heavy runtime just to preserve a demo effect.
