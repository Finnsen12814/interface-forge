# Mobile app adaptation

This skill's approved websites are largely web-focused. They may supply visual ideas, illustrations, motion patterns, or source assets for mobile, but a React web component is not a native iOS/Android control. Preserve the target platform's framework and interaction conventions. Ask for approval of the exact listed-site element or pattern, then adapt it into the existing mobile stack; do not install a web runtime inside a mobile app simply to retain a demo.

## Platform fit

Read the current Apple HIG pages relevant to an iOS app, especially [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios/), Layout, Accessibility, Buttons, Feedback, Motion, and Writing. The HIG is an evaluation standard, not an Apple asset library. For Android or cross-platform work, keep the app's established navigation, back behavior, permissions, and system controls. A sourced design should feel native enough to be predictable on the target device.

Inspect the existing app on a small phone, a large phone, and tablet if supported. Account for safe areas, camera cutouts, status/navigation bars, keyboard appearance, orientation, one-handed reach, text scaling, and dynamic content. Do not place critical actions under system UI or behind a bottom sheet that cannot be dismissed. Test with actual device or emulator behavior when available; screenshots alone miss keyboard, back, and focus issues.

## Navigation and flows

Use a compact, stable information architecture. Primary destinations should be discoverable; deep tasks need a clear return route. A web hover interaction must become a touch-and-keyboard-compatible action. Long forms should group fields and preserve progress. Show loading, offline, retry, permission denial, and interrupted-task states. Keep touch targets comfortable and avoid adjacent destructive actions.

## Source adaptation

For an approved component from Skiper, Magic UI, SmoothUI, KokonutUI, unlumen, or Motion Primitives, identify the idea being reused: hierarchy, transition, illustration, chart, or interaction. Rebuild it with the native framework's semantics and accessibility APIs. Do not copy web DOM code into a native view hierarchy. For approved unDraw assets, verify export rights and optimize for screen densities. Spline scenes require a clear reason and a strong device fallback. For React Native, verify whether a motion library supports the actual native target rather than assuming its web package works.

Write a short adaptation note: exact source URL, approved role, what was transferred, what was changed for platform fit, how screen reader labels and touch behavior work, and what happens with reduced motion. If adaptation changes the idea enough that the original approval no longer describes it, show the revised proposal to the user.

## Mobile review

Test touch, gesture cancellation, back navigation, keyboard avoidance, rotation, larger text, screen reader focus, dark/light themes if supported, offline recovery, low-power behavior, and long localized strings. Verify that sourced motion does not block taps or consume excessive battery. Preserve user context when an app is backgrounded and resumed. A polished mobile interface should feel fast and forgiving in short, interrupted sessions.
