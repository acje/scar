---
name: scar-html
description: Inspect HTML semantics, adopted access criteria and exercised delivery.
---
# HTML pages subject profile

## Applicability
Use for web pages, including static HTML. Name audience/tasks, browsers/output modes, local style and adopted accessibility level/criteria; a profile is not an automatic WCAG conformance contract.

## Techniques
1. Inspect meaningful headings, tables, relationships and reading sequence in markup and delivered representation; compare non-text alternatives with purpose and content.
2. Inspect information conveyed by color and supply equivalent non-color cues. Map each adopted criterion to a witness rather than treating semantics alone as conformance.
3. Exercise declared navigation/interactions, keyboard, assistive technology, zoom/reflow and print/output paths when required. Record exact environments; check links and content claims separately from visual behavior.

## Evidence and output
Record DOM/content identity, element locator, adopted criterion, observed browser/AT or static inspection, reasoning and unknowns. Use audience for task access and security for relevant input/trust boundaries; core remains applicable.

## Limitations
HTMLParser/link checking is not full HTML validation, browser rendering or accessibility certification. Later WCAG requirements were not substantively audited here; obtain their exact adopted text before using thresholds. No universal pixel/contrast/reflow cutoff is supplied.

## Sources
[WCAG 2.2 Recommendation](https://www.w3.org/TR/2024/REC-WCAG22-20241212/), Layers of Guidance, 1.1.1, 1.3.1, 1.3.2, 1.4.1; [WAI complex images](https://www.w3.org/WAI/tutorials/images/complex/), Long Descriptions; [audit](../../SOURCE-AUDIT.md) N2–N3.
