# United American Future

Static, multi-page civic-organization concept website served through the existing GitHub/Vercel workflow.

## Public routes

- `/`: civic mission and initiative introductions.
- `/about`: mission and organizational context.
- `/initiatives`: civic program areas and six national capacity concepts.
- `/initiatives/iron-corridor`: United American High-Speed Rail Network concept and map.
- `/initiatives/keystone-foundry`, `/initiatives/connected-communities`, `/initiatives/skyway`, `/initiatives/watershed`, `/initiatives/heritage-ecosystems`: public visions and illustrative imagery.
- `/impact`, `/transparency`: honest project status and organizational reporting context.
- `/get-involved`, `/contact`, `/donate`: participation, introductory inquiries, and existing contribution information.

Canonical domain: https://unitedamericanfuture.josephjilovec.com

## Maintenance

Buildless HTML/CSS/JavaScript. No dependency installation is needed to serve the site. Preserve accessible navigation, responsive layouts, image labels, canonical URLs, and the existing form and payment destinations. `initiative-contact.js` selects one of six inquiry topics from a whitelisted fragment or query parameter; general contact defaults to Volunteer.

`site.css` and `site.js` provide the shared design and behavior. `rail.css`, `initiatives.css`, and `concepts.css` extend the initiative presentation. Local preview configuration and a `dist` QA harness are not publication files.

## Imagery

See [rail attribution](assets/rail/README.md), [initiative imagery](assets/initiatives/README.md), and [image provenance](assets/initiatives/images.json). Preserve the source assets and responsive variants. All images and the rail map are illustrative; they do not document UAF facilities, employees, partnerships, or delivered projects.

The rail concept map can be regenerated with `python3 tools/build-rail-map.py`. Its geography and connections are illustrative, not surveyed routes or approved station sites.

## Public content

The initiative pages present purpose, intended public value, visuals, current concept status, and a way to get in touch. They do not publish internal execution or acquisition strategy. No legal/tax status, active project, government affiliation, award, or measured result is established by this source. Public reporting must remain accurate and meet applicable disclosure obligations.
