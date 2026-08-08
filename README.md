# United American Future

Multi-page static nonprofit website optimized for Vercel.

## Architecture
- `/` Home
- `/about` Mission and governance
- `/initiatives` Program roadmap
- `/impact` Measurement and outcomes
- `/transparency` Governance/compliance/public documents
- `/get-involved` Volunteer and partnership pathways
- `/donate` Conversion-ready donation placeholder (payments intentionally disabled)
- `/contact` Inquiry hub

## Performance approach
The site is pure static HTML/CSS/JS. This is the equivalent of full pre-rendering/SSG without framework runtime overhead. ISR is intentionally not enabled because there is no frequently changing server-rendered data yet. Add ISR or an API only when real impact/news data requires scheduled regeneration.

Static assets use long-lived immutable caching through `vercel.json`; HTML remains deployment-controlled. JavaScript is intentionally tiny and shared.

## SEO
Every route has a unique title, description, canonical URL, Open Graph data, and JSON-LD. `sitemap.xml` and `robots.txt` list all public routes.

## Compliance note
Donation processing is intentionally disabled until legal entity, banking, payment, registration, tax-status, privacy, and disclosure requirements are verified.

## Domain
Canonical domain currently configured as `https://unitedamericanfuture.org`. Update canonical URLs and sitemap if the final production domain differs.
