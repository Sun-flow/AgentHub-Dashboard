---
title: Process and SPECS.md requirements
topic: product
sources:
  - _raw/2026-11-19-brief/README.md (mae's message, Guidelines)
  - _raw/2026-11-19-brief/2-spec-guidelines.png
updated: 2026-11-19
status: stable
---

# Process and SPECS.md requirements

## Summary

"Vision to spec": define the rules before building. A `SPECS.md` at the repo
root is the contract with the codebase. It must be committed in its own commit
before any HTML file exists, and it must be detailed enough that an AI coding
agent could build the panel from it without asking questions.

## Required order of work

1. Write `SPECS.md` at the **root of the repository**.
2. Commit it in a **separate commit, before the first HTML file**. Git history
   is checked.
3. Feed `SPECS.md` to **Google Stitch** to get a visual proposal, and use that
   only as design guidance. Structure, components, and interactions must be
   adapted to match the requirements exactly.
4. Build the prototype from the spec.

## What SPECS.md must contain

1. **Product description:** what AgentHub is and who the admin user is.
2. **Tech stack and constraints:** HTML, Tailwind via CDN, vanilla JS only, no
   frameworks, no backend.
3. **At least 3 specifications per section** (all six). Each one names a
   component, describes its contents, and defines its behavior. The brief's
   own example for the Dashboard sets the expected detail:
   - four metric cards in a responsive 2×2 grid, each with an icon, a label,
     and a hardcoded value;
   - cards use distinct accent colors per metric type and a subtle shadow;
   - below the cards, a full-width placeholder div with a dashed border and a
     centered label represents the weekly activity chart.
4. **Component inventory:** reusable components shared across sections, at
   least sidebar, metric card, action dropdown, modal, badge, collapsible skill
   list, dark mode toggle.
5. **Acceptance criteria:** a numbered list of verifiable conditions, with at
   least one per interactive behavior (dropdown, modal, collapsible, dark mode).

## Quality bar

An AI coding agent reads `SPECS.md` and builds the panel without asking
anything.

## Related

- [definition-of-done.md](definition-of-done.md)
- [evaluation-criteria.md](evaluation-criteria.md)
- [../references/tools.md](../references/tools.md)
