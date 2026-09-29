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

## Full website completion standard

The user's `Websites.txt` includes an explicit production checklist. For a **new site, complete site redesign, or release-readiness task**, address every item below. For a narrow component edit, preserve existing site behavior and inspect affected items; do not rewrite unrelated policy or hosting settings. Mark each item done, not applicable with a reason, or blocked by missing business/hosting facts. A visual preview does not prove a site is production-ready.

### 1. Clear purpose and one main call to action

The home page should state what the product does for whom, with one strong next step. Supporting CTAs can exist but must not compete. Use specific verbs and destinations. The main CTA must work; do not link it to `#`, an empty form, or a dead route. Follow the CTA through completion and error recovery. Do not use fake testimonials or metrics to fill space.

### 2. Privacy Policy and Terms and Conditions

Create discoverable, readable routes linked from appropriate navigation/footer areas. The Privacy Policy needs the actual organization, data collected, purposes, processors, retention, contact details, and rights relevant to the business. The Terms need the actual product, contracting party, service scope, pricing or subscription terms if any, limitations, cancellation/termination, contact and jurisdiction-specific provisions. These facts cannot be invented. If the user has not provided them, implement a clearly marked draft route and request missing facts before publication. Get qualified legal review where needed; a template is not proof of compliance.

### 3. Cookie consent and analytics

Audit cookies, storage, embedded content, and analytics scripts before showing a banner. Do not add a cookie banner when there is no consent-triggering use simply for decoration. Where consent is required, explain categories and purposes, offer a clear reject choice, avoid prechecked optional categories, delay optional scripts until valid consent, and let people revisit or change the choice. Define analytics events tied to useful product questions, avoid sensitive data in event payloads, and verify no third-party network requests occur before the required choice. Do not activate analytics without the user's provider and data-handling decisions.

### 4. Front-end secrets and secure transport

Search the client bundle and public files for private API keys, tokens, service credentials, and internal endpoints. Public configuration may be exposed by design; secrets belong on the server or in a secure backend service. Do not trust front-end validation for security. Configure HTTPS and HTTP-to-HTTPS redirects at the actual host; check mixed content. Review security headers such as CSP and HSTS in the hosting context, plus secure cookie settings where applicable. Never claim HTTPS or headers are active based only on local code.

### 5. Metadata and previews

Set an accurate, distinct title and description for indexable pages. Add canonical URLs when necessary to prevent duplicate variants. Configure social preview title, description, and an intentional preview image from a rights-cleared source or user-provided brand content. Add a proper favicon and app icons for the relevant platforms. Check how previews render on at least one share target if possible. Do not ship a framework's default icon, title, or placeholder OG image.

### 6. Sitemap and robots.txt

Generate a sitemap of public canonical routes and keep it updated as pages change. Add deliberate `robots.txt` behavior: allow useful public pages; keep private, staging, or irrelevant routes out of indexing as appropriate. `robots.txt` is not access control. Verify that policy, terms, and any public content intended for search are discoverable as the product requires. Avoid indexing placeholder drafts or error routes.

### 7. Useful custom 404 and broken-link handling

Create a real not-found route with the site's visual language, a clear explanation, and a working route home or to search/navigation. Preserve the incorrect URL long enough for diagnosis; return an actual 404 status where the stack supports it. Test direct navigation, client-side navigation, refresh, and unknown nested routes. Check internal links, footer links, anchor targets, external links, and links in legal pages. Fix or remove broken links rather than hiding them.

### 8. Forms and spam/bot/bandwidth protection

Implement client-side validation for helpful immediate feedback and **server-side validation** for trust. Use suitable input types, persistent labels, clear error messages, focus management, success/failure responses, and duplicate submission prevention. If a form sends data, verify the actual destination. Add proportionate spam, bot, rate, and bandwidth-abuse protection where needed; do not punish ordinary users with unnecessary captchas. Protect state-changing endpoints against CSRF where relevant. Do not claim protection from a visual form alone.

### 9. Images, alt text, and media efficiency

Every imported image needs provenance and appropriate rights. Compress and resize to its display role, serve modern formats when compatible, include dimensions/aspect ratio to prevent layout shift, and lazy load noncritical media. The primary above-the-fold image should not be lazily delayed. Write concise alt text for informative images; use empty alt for decoration; give complex diagrams nearby explanation. Avoid remote assets that become broken when a gallery changes.

### 10. Accessibility and contrast

Verify headings, landmarks, reading order, semantic links/buttons, form labels, focus visibility, keyboard access, dialogs, menus, error association, status announcements, contrast, zoom/reflow, target size, reduced motion, and color-independent meaning. Test with actual content and a keyboard, not just an automated score. Fix color contrast in normal and interactive states. The Apple HIG benchmark complements web accessibility requirements; it does not replace them.

### 11. Mobile friendliness and page speed

Inspect narrow and wide phones, tablet, laptop, and large desktop widths. Check safe areas, touch targets, sticky controls, long text, orientation, font scaling, and horizontal overflow. Measure representative pages on realistic mobile conditions. Optimize the largest assets, font loading, script weight, third-party embeds, and animation runtime. Assess current Core Web Vitals when available, but focus on observable loading and interaction quality, not only a score. Provide sensible fallbacks for slow networks and failed media.

### 12. Final site walk-through

Open each public route, follow every primary CTA, submit valid and invalid forms, view policy and terms, load an unknown URL, inspect metadata and social image, check sitemap/robots, test consent behavior, scan the client build for exposed secrets, inspect HTTPS in the deployed environment, and run link and performance checks. Report which checks were performed locally and which require deployment or business facts. Do not silently mark unverified items complete.
