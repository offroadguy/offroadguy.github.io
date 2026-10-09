# Venkata Ganji — Engineering Portfolio

Public portfolio: https://offroadguy.github.io/

Four case studies covering enterprise GenAI, cyber telemetry, mission-critical data migration, and cloud infrastructure/identity/recovery. Includes twelve sanitized architecture views, a nine-page case-study PDF, and PDF/Word resumes.

## Update the site

1. Edit `content.json` for case-study narratives. Preserve employment relationships, attribution and metric scope.
2. Run `python3 scripts/build.py` to rebuild HTML and supporting SVGs. The detailed GenAI SVG is a separately maintained sanitized artifact.
3. Preview with `python3 -m http.server 8765`; check desktop, mobile, links, downloads and diagram controls.
4. To regenerate the PDF pack, render SVGs to PNGs in `.build/` using Sharp, then run `scripts/build_pack.py` with Python, ReportLab and Pillow. The PDF builder uses Arial from macOS.
5. Publish changes to the configured GitHub Pages branch.

The site is static HTML/CSS/JavaScript and has no runtime dependencies, analytics, forms or third-party assets. Diagrams are editable SVGs. The site includes simplified reconstructions and eleven low-resolution previews of the supplied original diagrams. Preview exports are limited to 640 pixels on the longest edge and compressed as JPEG quality 22. Full-resolution originals are excluded from the current site. Low resolution discourages detailed reuse but is not a security control. Private repository evidence is not included.

## Attribution and scope

Experience and outcomes are based on Venkata Ganji's resume and confirmations. Apple was a contract through Mphasis; Freddie Mac and other client work was through Cloudwick. The later Amorphic architecture is explicitly team context. The 40 Gb/s label denotes capture technology, not a measured end-to-end benchmark. The 30 PB headline denotes total capacity across the earlier Hadoop environments.

Version 1.6.0 · October 2026

## Resume alignment v1.6.0

Downloads match resume v3.8.0. Technology strips and role ownership grids mirror the latest resume. The $500K+ metric is combined Solr and Mac savings, not an annual total. Next Inference Focus is aspirational; it does not claim completed GenAI-Perf, SGLang or LMCache projects. Locally hosted logo sources are recorded in `assets/technologies/sources.json`; generic symbols represent DR and HA.

Validation: desktop 1440px and mobile 390px on all five pages, local links/images, ownership toggle, diagram dialogs, reduced motion; refreshed nine-page PDF pack visually reviewed.
