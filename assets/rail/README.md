# Iron Corridor media and map

- `rail-vision-1800.webp`, `rail-vision-1000.webp`, `rail-vision-640.webp`: responsive encodings of the user-supplied `image(1).png`, originally 1800 × 1013. The original author, production method and location were not independently established. Captions identify the image as illustrative and do not claim UAF ownership, real UAF construction, endorsement or a partnership. Visible third-party train branding remains part of the supplied illustration.
- `network-concept.svg`: newly authored concept map. It corrects the working sketch's duplicate Dallas/Fort Worth label and uses only Denver, Chicago and Houston as potential hub markers. Approximate city centers and illustrative connection lines do not select sites, routes, service speeds or infrastructure.
- `land-outline.json`: United States/Canada/Mexico subset of Natural Earth's `ne_110m_admin_0_countries.geojson`, source Git blob `1e6ab74c7042f97013be69ceec798be8e1aff27d`. [Source dataset](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_110m_admin_0_countries.geojson). [Natural Earth terms](https://www.naturalearthdata.com/about/terms-of-use/) place its map data in the public domain. This is general land geometry, not railway/property data.

The user's original map and source image/text are retained unchanged in the private program source materials. Original image provenance is not upgraded into a verified photography, infrastructure, rights-clearance or institutional claim by conversion or publication.

Regenerate the concept map from the repository root with `python3 tools/build-rail-map.py` (Python standard library only).
