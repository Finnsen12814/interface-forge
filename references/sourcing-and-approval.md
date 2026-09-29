# Sourcing, approval, download, and provenance

This is the operational gate for every **new external UI element**. It applies in Codex and Claude Code even when the user asked for a full redesign. Research, inspect, compare, sketch, and prepare integration plans without approval. Obtain approval for a specific element before copying code, downloading a file, invoking a registry command, embedding a scene, or integrating it into the app.

## 1. Turn the request into component needs

Record the screen or flow, its audience, its primary action, and the current defect. Break the UI into needed roles: navigation, action, input, feedback, data view, media, explanation, and supporting page structure. Avoid inventing roles merely to fill a catalog. For each role, note interaction requirements, viewport, framework, complexity ceiling, reduced-motion route, and whether the product already has a useful component.

Examples of useful questions:

- What decision should this chart help the person make? Which comparison, trend, or distribution matters?
- Is the illustration explaining an empty state, or merely decorating whitespace?
- Does an animated button make state clearer, or will repeated motion slow the task?
- Can the current framework implement this source without an unnecessary runtime?

## 2. Scan the entire allowlist

Read the current [source-research.md](source-research.md) map. Go through **every entry** for each design task. Mark each entry `candidate`, `reference only`, `irrelevant`, `incompatible`, `blocked`, or `license unresolved`, with a short reason. This is a source coverage pass, not a mandate to use every website or inspect every page on every website. Search deeply within entries marked candidate. Multiple URLs belonging to one provider still need their relevant component and block catalogs checked.

For promising candidates, inspect the **exact element page** and, where offered, live behavior and source/install documentation. Do not use search snippets alone to claim an element exists. Record current price/free status, license, attribution, access conditions, dependency graph, framework, and official acquisition method. Distinguish an inspiration gallery from a downloadable library. A gallery listing a third-party site does not make that linked domain an allowed source.

## 3. Compare candidates

Use a simple decision table. Prioritize task fit and rights over spectacle:

| Criterion | Question |
|---|---|
| Task fit | Does the element make the requested action easier or clearer? |
| Interaction | Does it support the required states, input modes, and recovery? |
| Framework fit | Can it be adapted without changing the app's stack? |
| Accessibility | Are semantics, focus, contrast, labels, and reduced motion feasible? |
| Cohesion | Will it match the chosen system after adaptation? |
| Cost and rights | Can this project legally obtain and ship it? What attribution is needed? |
| Performance | What will it add to transfer size, CPU/GPU work, and startup? |
| Maintenance | Can the team understand, update, and test it? |

For a high-impact surface, compare two or more real candidates if available. If only one qualifies, state why. Keep a small shortlist, usually one recommended option per role. Do not present a paid option as ready to download when no legitimate access exists.

## 4. Ask the user with an exact link

Use a direct page for the candidate element, not a vendor home page or a broken search URL. If the site offers only a broad gallery page, say that no exact reusable element has been found yet. The request must identify the **element**, **role**, **planned adaptation**, and **material terms**.

Preferred German wording:

> Ich möchte KONKRETES ELEMENT (als klickbaren Link auf die exakte Element-URL aus der erlaubten Liste) für KONKRETE STELLE UND ZWECK verwenden. Ich passe FARBEN, TYPOGRAFIE, VERHALTEN ODER INHALT an unser Design an. Falls relevant: PREIS, ATTRIBUTION, ZUSÄTZLICHE BIBLIOTHEK ODER LIZENZUNSICHERHEIT. Passt das?

For multiple candidates, one message may contain several numbered proposals, each with its own exact URL and a clear request for yes/no per number. An approval of the overall design direction, of a vendor, or of the first item is not approval of every separate element. Never auto-select a preselected UI choice or treat missing reply as consent. If the user changes the request while approval is pending, reassess the candidate.

An approval belongs to `(exact source URL, element, intended role, important usage terms)`. It does not cover another item on the same site, a premium upgrade, or a different download endpoint with materially different content. An alternate official file or registry URL for the **same approved element** may be used after checking it matches the approved page and terms.

## 5. Download only through the supported route

After approval, use the provider's official download, copy, registry, or embed method. Prefer a local, versioned asset or component over a live third-party dependency when the license and architecture allow it. If a registry command may install transitive dependencies, inspect the manifest first. Do not run arbitrary install scripts blindly. Avoid hotlinking images unless the source explicitly permits it and the runtime dependency is acceptable.

Never evade paywalls, access controls, rate limits, robots rules, or terms. If automated scraping or downloading is forbidden, stop that method; a user-provided, legitimately acquired file or another allowed candidate may resolve the gap. If a source lacks a clear license or usable export, treat it as research-only until rights are clear. An AI can be technically able to fetch a file while still lacking permission to reuse it.

## 6. Adapt the source thoroughly

Build the adaptation in the product's component and token system. Replace demo copy, placeholder metrics, fake avatars, stock-looking screenshots, sample imagery, and needless effects. Preserve source attribution and copyright notices where required. Verify that code and assets have no unwanted tracking, remote fonts, external requests, environment assumptions, secrets, or insecure HTML handling.

Treat source code as a starting point, not a guarantee of accessibility or quality. Add focus-visible states, labels, semantic structure, Escape behavior, focus restoration, loading/error/disabled states, responsive rules, reduced-motion alternatives, and tests as needed. Keep the original component's useful idea while making its expression belong to this product.

## 7. Record provenance

For each imported item, add a short project note or manifest entry near the asset/component or in the project's existing attribution file. Record: source page URL, acquisition URL if different, author/provider, retrieval date, license/terms URL and key obligations, original filename or component name, version if any, local destination, modifications, and where it appears. Do not fabricate author or license data. Preserve source files and notices when required.

Suggested compact record:

```text
Role: Empty-state illustration on /projects
Element: [exact title]
Source: [exact URL]
Retrieved: YYYY-MM-DD via [official route]
Rights: [verified license/terms + obligations]
Local file: [path]
Adaptation: palette, crop, alt treatment
Approval: user approved this element for this role on [date]
```

## 8. When approval or sourcing fails

- **No answer yet:** Keep working on product structure, semantics, data, copy, and local components that do not import a new external element. Leave the candidate unimported.
- **No approval:** Remove the candidate from the plan and research the next allowed option. Ask again with its exact URL.
- **Unreachable site:** State what could not be inspected. Use another allowlisted site; do not invent the component or silently switch domains.
- **License conflict:** Do not import it, even if the user likes its appearance. Explain the concrete issue and offer a licensed candidate or request that the user supplies valid rights.
- **No suitable element:** Implement the functional behavior with existing product code, explain that the requested new sourced visual cannot be completed from the allowlist, and ask whether the user wants to expand the allowlist.
