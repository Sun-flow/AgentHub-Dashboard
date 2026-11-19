---
title: Evaluation criteria
topic: product
sources:
  - _raw/2026-11-19-brief/5-evaluation-criteria.png
updated: 2026-11-19
status: stable
---

# Evaluation criteria

## Summary

How the deliverable will be judged. Interactive behaviors are tested by hand.
Form submission, live search, and real page navigation are **not** evaluated.

## Criteria

1. `SPECS.md` was committed before any HTML file (checked in Git history).
2. The spec has at least 3 concrete specifications per section, a component inventory, and a numbered acceptance criteria list.
3. All six sections are present and reachable from the sidebar.
4. Tailwind utility classes are used consistently; no inline styles, no external CSS files.
5. Every list row has a working `⋮` dropdown that opens, closes on click, and closes on outside click.
6. "View detail" opens a modal in **at least four** sections.
7. Modals close via the close button and via backdrop click.
8. Agent skill lists are collapsed by default and expand/collapse on click with a visible transition.
9. The dark/light toggle switches the full panel, and the state is kept between sections.
10. Hardcoded data is consistent across sections (the same agent name appears in Agent Management, Contracts, and Error Log).
11. HTML uses semantic tags correctly: `section`, `table`, `nav`, `header`, `main`, and similar.
12. The layout is usable on desktop and tablet viewports.

## Notes

- Criterion 6: Users, Skills, Contracts, and Error Log each have "View detail",
  which makes exactly four. Agent Management uses "Configure" instead. _(inferred)_

## Related

- [definition-of-done.md](definition-of-done.md)
- [process-and-spec.md](process-and-spec.md)
