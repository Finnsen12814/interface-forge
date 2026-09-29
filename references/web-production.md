# Website production checklist

Adapt to jurisdiction and hosting; do not equate a checklist with legal compliance.

## Discovery and content

- One clear primary CTA per decision surface.
- Accurate unique titles/descriptions, canonical URLs where needed, intentional social image, favicon/app icons.
- Sitemap for indexable content and deliberate `robots.txt`.
- Useful 404/recovery, broken-link check, working navigation, meaningful alt text.

## Privacy, security, trust

- Real privacy policy and terms with qualified jurisdictional review.
- Consent-dependent tracking loads only after valid consent where required; rejection/revision must not be obstructive.
- Document analytics purpose, events, retention, and consent.
- Force HTTPS; use deliberate HSTS/CSP; minimize unsafe inline/eval.
- Server-side validation, proportionate abuse/rate/bot and CSRF protection, secure sessions.
- Secrets stay server-side. Threat-review external links, embeds, uploads, and rich text.

## Performance and resilience

- Measure representative mobile/desktop pages and current Core Web Vitals when relevant.
- Correctly size/compress images; use modern formats and reserve dimensions.
- Control font payload/display; avoid large libraries for trivial effects.
- Test slow network, cold cache, low-power device, long content, timeout/offline recovery.
- Verify landmarks, headings, labels, errors, keyboard, focus, contrast, zoom/reflow, text spacing, targets, reduced motion, forced colors, mobile safe areas, and no horizontal overflow.

