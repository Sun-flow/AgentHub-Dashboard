---
title: Technical constraints
topic: technical
sources:
  - _raw/2026-11-19-brief/2-spec-guidelines.png
  - _raw/2026-11-19-brief/3-dod-build-pt1.png
  - _raw/2026-11-19-brief/4-dod-build-pt2.png
  - _raw/2026-11-19-brief/5-evaluation-criteria.png
  - _raw/2026-11-19-brief/6-brief-closing.png
  - references/html-hello-template.md
updated: 2026-11-19
status: stable
---

# Technical constraints

## Summary

Static HTML, Tailwind from a CDN, vanilla JS, hardcoded data, no backend.

## Hard rules

- **Markup:** HTML. One `index.html`, or one linked HTML file per section.
  Semantic tags (`header`, `nav`, `main`, `section`, `table`, ...).
- **Styling:** Tailwind CSS via CDN only. No custom CSS files, no inline
  `style` attributes. Dark mode through Tailwind `dark:` utilities.
- **Behavior:** vanilla JavaScript only. No React, Vue, jQuery, or build tools.
- **Data:** hardcoded and consistent across sections. No backend calls and no API
  connections (even though AgentHub has a real backend); the team is not
  expecting either at this stage.
- **Viewports:** usable on desktop and tablet.
- **Repo:** `SPECS.md` at the repo root, committed alone before any HTML.

## Implementation notes _(inferred, not from the brief)_

- **Tailwind version matters for dark mode.** The 4Geeks starter template
  points to the v4 browser CDN (`@tailwindcss/browser@4`). Both v3 and v4 CDNs
  default to media-query dark mode, so a manual toggle needs opting in to
  class-based dark mode, then toggling a `dark` class on `<html>`:
  - v3 Play CDN (`cdn.tailwindcss.com`): `tailwind.config = { darkMode: 'class' }` in a script tag.
  - v4 browser CDN: `@custom-variant dark (&:where(.dark, .dark *));` inside a
    `<style type="text/tailwindcss">` block. Whether that block counts as
    "custom CSS" under the brief is an open question.
- If the panel is split into several HTML files, keeping the dark mode choice
  between pages needs `localStorage` (or similar). A single-page `index.html`
  with section switching avoids that.
- "Smooth transition" on the skill list can be done with Tailwind transition
  utilities on `max-height` / `grid-template-rows`, toggled by JS classes.

## Related

- [../product/definition-of-done.md](../product/definition-of-done.md)
