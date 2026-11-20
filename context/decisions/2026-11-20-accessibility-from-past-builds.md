---
title: Accessibility rules carried over from mae's past builds
topic: decision
sources:
  - mae, project thread 2026-11-20 ("in some of our past frontend builds, we had strict accessibility guidelines. can you find references to those, and import some of them here?")
  - Sun-flow/TrackFlow-Company-Overhaul: uis/AGENTS.md "Accessibility"; docs/milestones/milestone-1/definition-of-done.md items A1–A5, V10
  - Sun-flow/tailwind-dashboard: resources/design-spec.md §3 "Contrast", §10 "Accessibility and semantics"
  - Sun-flow/html-tailwindcss-project: .agents/rules/accessibility.md
updated: 2026-11-20
status: stable
---

# Accessibility rules carried over from mae's past builds

## Summary

mae asked for the accessibility rules from earlier front-end builds to apply
here. The three repos above share one rule set; the parts that fit a
single-page Tailwind admin panel became DoD items W1–W9 in
[../definition-of-done.md](../definition-of-done.md). The brief does not grade
accessibility (B5), so these are mae's own bar on top of it. None of them needs
custom CSS: every one is markup, ARIA, JS behavior, or a Tailwind utility.

## Details

**Adopted** (DoD ID, then where it came from):

| ID | Rule | From |
| --- | --- | --- |
| W1 | Keyboard reachable in natural order; `tabindex` only when necessary | all three |
| W2 | Visible focus indicator on every interactive element; never `outline-none` alone | TrackFlow, tailwind-dashboard |
| W3 | `aria-label` on controls with no visible text; state ARIA matches the UI | all three |
| W4 | Decorative icons, SVGs and emoji `aria-hidden="true"`; meaningful images get `alt` | all three |
| W5 | Text meets WCAG AA contrast (4.5:1) in every theme | TrackFlow, tailwind-dashboard |
| W6 | Reduced motion respected (`motion-reduce:transition-none`) | TrackFlow |
| W7 | Skip link to `<main>`; one `<h1>`; labelled landmarks and sections | TrackFlow, tailwind-dashboard |
| W8 | Escape closes menus and modals; focus moves in and back | TrackFlow (mobile menu, dialog) |
| W9 | axe-core finds no violations, plus a keyboard walk | TrackFlow, tailwind-dashboard |

**Not carried over:** form labels tied to errors with `aria-describedby` and
`aria-live` error messages (the brief does not evaluate form submission, B5;
the one form control, the Configure textarea, is covered by W3), Schema.org
markup, and Lighthouse score targets (SEO and performance rules, not
accessibility).

**Interpretations** _(inferred)_: W5 also asks 3:1 for focus rings and badge
outlines, the WCAG 2.2 AA figure for non-text contrast, because the past builds
stated text contrast only and the badges carry the status colors. W9 loads
axe-core from a CDN inside a Playwright run so no `package.json` is added.

The IDs use W (for WCAG), not TrackFlow's A, because `SPECS.md` already
numbers its assumptions A1, A2 and so on.

## Related

- [../definition-of-done.md](../definition-of-done.md) section W
- `SPECS.md` (pending in its own pull request) already covers most of W2, W3
  and W8. The gaps are listed in the "Now" block of [../todo.md](../todo.md).
