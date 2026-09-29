# Apple Human Interface Guidelines as a quality benchmark

The user explicitly requires reading the **current Apple Developer Human Interface Guidelines**. Read the official overview and Design principles for every design task, then the topic pages relevant to the affected screen. Use Apple's guidance to evaluate usability and craft; do **not** import Apple artwork, system assets, trademarks, screenshots, fonts, or styles into a web/Electron app. Apple documentation is the one source outside `Websites.txt` allowed for **evaluation**, never for new UI assets.

## Official reading map

| Always or when relevant | Official Apple Developer page | What to extract |
|---|---|---|
| Every design task | [HIG overview](https://developer.apple.com/design/human-interface-guidelines/) and [Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles) | purpose, agency, responsibility, familiarity, flexibility, simplicity, craft, delight |
| Page and screen layout | [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | visual hierarchy, alignment, grouping, progressive disclosure, adaptation and safe areas |
| Reading and UI text | [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) and [Writing](https://developer.apple.com/design/human-interface-guidelines/writing) | readable hierarchy, concise labels, consistent voice, error and action text |
| Any interactive surface | [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) and [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) | perceivability, adaptable text, labels, adequate targets, clear button roles and feedback |
| Status, errors, saving, destructive action | [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback) | proportional feedback, status without unnecessary interruption, recovery |
| Animation or 3D | [Motion](https://developer.apple.com/design/human-interface-guidelines/motion) | purposeful, brief, optional motion with alternatives and cancelability |
| Sensitive data, permissions, consent | [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) | clear purpose, minimal collection, understandable permission timing |
| macOS-like desktop or Electron | [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos/) | resizable windows, keyboard and pointer use, familiar commands, comfortable density |
| iPhone-oriented website or responsive app | [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios/) | small-screen context, touch, legible content, platform expectations |

Apple's pages may require JavaScript. Use an actual browser when available. If a page cannot be loaded, use official Apple-indexed documentation or official Apple search results for that topic and say what could not be inspected. Never substitute a third-party HIG summary as if it were the official page. Recheck current guidance; a copied snapshot in this skill can become stale.

## Turn principles into product decisions

### Purpose and simplicity

Identify the most important job the person came to do. Put the information and action needed for that job in the strongest visual position. Remove decorative interface pieces and options that do not support it. Simplicity means an intelligible path, not a blank screen. If the task is complex, reveal supporting detail in the order it becomes useful.

### Agency and forgiveness

Keep people in control. Make navigation, cancel, undo, and recovery available where actions have meaningful consequences. Avoid trapping people in guided flows, locking them behind animation, or hiding what an action will do. Preserve entered work when validation fails. Confirm destructive actions only when undo cannot provide sufficient safety.

### Familiarity and consistency

Use familiar interaction meanings and consistent placement. A button acts, a link navigates, a toggle changes a persistent state, and a menu reveals choices. If a sourced component has unfamiliar behavior, simplify or adapt it. A beautiful demo interaction that conflicts with expectations does not pass this test.

### Flexibility and accessibility

Support keyboard, pointer, touch, screen readers, zoom, larger text, reduced motion, varied viewport sizes, and content growth. Do not rely on color or movement alone. Provide visible focus, meaningful labels, logical reading/focus order, and generous targets. Verify on actual rendered UI, not by assuming a component library handles it.

### Responsibility and trust

Explain data collection, permissions, external navigation, and destructive consequences clearly. Ask for permission in context, when the need is apparent. Avoid manipulative consent and false scarcity. Keep the product's claims and data real. The site's privacy and terms pages need business facts; do not invent them to make a checklist look complete.

### Craft and delight

Care for details that people feel: alignment, typography, predictable transition, precise feedback, honest loading, gentle empty states, and polished error recovery. Distinctiveness should serve the brand and task. Apple's current principles explicitly frame delight as a human feeling from the overall experience, not added decoration.

## Apply Apple guidance appropriately to web and Electron

Apple HIG is primarily platform guidance. A web app still needs web conventions: URLs, history, semantic HTML, browser focus behavior, scrolling, links, and responsive reflow. An Electron app still needs desktop conventions for its host operating system. Do not imitate Apple-only materials or native components where doing so makes the product feel alien on other platforms. Translate the **underlying rationale**: clear hierarchy, control, feedback, adaptability, and detail.

When a source from `Websites.txt` looks attractive but conflicts with the HIG principle needed here, adapt it. Examples: add a visible label to an icon-only control, disable perpetual animation for reduced motion, convert a hover-only menu into keyboard/touch access, or make a chart readable without color. If adaptation destroys the component's core idea, choose another allowed candidate.

## Review questions

Before approval and again after implementation, ask:

1. Can a first-time user say what this view is for and what to do next?
2. Does the interface react immediately and truthfully to each action?
3. Can people leave, undo, retry, and return without losing context?
4. Are controls understandable without hover or visual motion?
5. Does the same flow work with keyboard, touch, screen reader, zoom, and narrow widths?
6. Does each animation communicate state or continuity, and can it be skipped?
7. Are privacy and consent choices clear and proportionate?
8. Does the sourced element feel like part of this product after adaptation?
