# United American Future

Multi-page static civic-organization website deployed through the existing GitHub/Vercel workflow. Legal and tax status are not established by this repository.

## Public routes

- `/`: existing civic homepage with a featured Iron Corridor introduction.
- `/about`: mission, governance and proposed public-interest infrastructure role.
- `/initiatives`: civic program areas and all six national-capacity concepts.
- `/initiatives/iron-corridor`: detailed concept brief for the proposed United American High-Speed Rail Network.
- `/impact`: measurement framework and actual concept-stage rail milestone status.
- `/transparency`: governance, evidence limits and media/source information.
- `/get-involved`, `/contact`, `/donate`: existing participation and contribution routes.

Canonical domain: https://unitedamericanfuture.josephjilovec.com

## Implementation

Buildless HTML/CSS/JavaScript. The original homepage hero, shared visual design and other initiative concepts are retained. `rail.css` contains the added feature, program, responsive and accessibility styling. The new contact helper selects the Iron Corridor inquiry option when `#iron-corridor` (or `?program=iron-corridor`) is supplied; the form's existing delivery endpoint is unchanged. No inquiry, appointment, payment or bid was submitted during validation.

The contribution page contains existing external Stripe links. Earlier documentation called payment processing disabled; that statement did not match the HTML at the reviewed baseline. This update preserves those payment destinations and does not certify organizational registration, tax status, deductibility, fundraising eligibility or payment availability.

## Rail media and map

See `assets/rail/README.md` for provenance. Supplied rail imagery is illustrative, not a UAF asset, construction record or announced partnership. Responsive optimized WebP files avoid serving the multi-megabyte uploaded original on the website.

`tools/build-rail-map.py` regenerates `assets/rail/network-concept.svg` using the public-domain land-outline subset in `assets/rail/land-outline.json`. Approximate city centers are used for concept cartography only. The map has exactly three potential hub styles and one Dallas/Fort Worth label in Texas. Drawn connections are research hypotheses, not selected alignments, station sites, engineering designs or an operating service.

## Public/private boundary

This public source contains truthful positioning, concept descriptions, evidence limits, media attribution and maintenance code. Internal business plans, budget assumptions, bid strategy, governance/IP planning, blank work instruments and unchanged original user materials are maintained in the private venture repository. No private operating engine or sensitive client dataset is added to this public site.

No build dependencies are required to serve the website. Use standard HTML/asset/anchor, CSS/JavaScript syntax and responsive browser checks after edits. A local preview configuration and `dist` QA harness are not publication files.
