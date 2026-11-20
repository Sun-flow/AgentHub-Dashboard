# Deliverable 1: SPECS.md

The contract with the codebase. Written and committed **before any HTML exists**.
Quality bar from the brief: an AI coding agent reads `SPECS.md` and builds the
panel without asking a single question.

## Before writing

- [ ] Read [../brief.md](../brief.md) end to end.
- [ ] Every open question in [../open-questions.md](../open-questions.md) is
      answered by mae or uses its proposed default (only Q1 and Q2 remain).
      Record each choice in the spec.
- [x] Tailwind CDN version chosen: v4 browser CDN (Q11).
- [x] File structure chosen: single `index.html` (Q8).

## Required outline

`SPECS.md` should follow this outline so every DoD item has an obvious home.

1. **Product description** (S1): what AgentHub is, who the admin user is, what
   the prototype is for.
2. **Tech stack and constraints** (S2, T1–T8): HTML, Tailwind CDN (exact URL
   and dark-mode setup), vanilla JS, no frameworks, no build tools, no backend,
   no custom CSS files, no inline `style`, semantic tags, desktop + tablet.
3. **Layout shell** (L1–L3): sidebar items in order with icons, active-state
   styling, top bar contents, main content area, tablet behavior of the sidebar.
4. **Sections 1–6**, each with **at least 3 numbered specs** (S3, S4). Each spec
   names a component, lists its contents, and defines its behavior. Minimum
   coverage per section:
   - Dashboard: card grid layout; card anatomy and accent colors; chart
     placeholder (D1.1–D1.3).
   - User Management: table columns; status badge colors; row dropdown;
     user detail modal fields and close behavior (D2.1–D2.4).
   - Agent Management: agent card/row layout; status badges; collapsible skill
     list and its transition; Configure modal with textarea (D3.1–D3.6).
   - Skills: "what is a skill" explainer; skill card/row anatomy with
     agents-enabled indicator; dropdown; detail modal fields (D4.1–D4.5).
   - Agent Contracts: table columns; active vs past indicator; dropdown
     options; breakdown modal with itemized skill prices and total (D5.1–D5.5).
   - Error Log: entry columns; badge color per type/severity; dropdown;
     trace modal; resolved entries darkened in place (D6.1–D6.8).
5. **Component inventory** (S5): sidebar, top bar, metric card, data table,
   action dropdown, modal, confirm-delete modal, badge, collapsible skill list,
   dark mode toggle, tier lock indicator. For
   each: purpose, anatomy, states (open/closed, light/dark), where it is used.
6. **Interaction rules** (X1–X5): exactly how dropdowns open/close (including
   outside click and only one open at a time), how modals open/close (button,
   backdrop, optionally Escape), how dark mode toggles and persists, how the
   skill list animates.
7. **Hardcoded dataset** (S8, X7): the complete data, written out as tables:
   every user, agent (with owner, status, skills, system prompt), skill (with
   description, price, agents-enabled count), contract (with itemized skills,
   prices, dates, total), error (with timestamp, type, severity, description,
   trace), and the four dashboard values. Must satisfy the consistency rules in
   [../domain.md](../domain.md).
8. **Acceptance criteria** (S6, S7): a numbered list. At least one per
   interactive behavior (dropdown, modal, collapsible, dark mode), plus one per
   evaluation bullet in brief B5.

## Completion checklist

- [ ] S1 product description present
- [ ] S2 tech stack and constraints present
- [ ] S3 at least 3 specs in each of the six sections (count them)
- [ ] S4 every spec names a component, its contents, and its behavior
- [ ] S5 component inventory includes all seven required components
- [ ] S6 acceptance criteria are a numbered list of verifiable conditions
- [ ] S7 at least one criterion each for dropdown, modal, collapsible, dark mode
- [ ] S8 full hardcoded dataset included and internally consistent
- [ ] Every DoD item in L, D1–D6, X, T is covered somewhere in the spec
- [ ] Cold-read test: a fresh agent given only `SPECS.md` lists no questions
- [ ] P1 file is at the repo root, named exactly `SPECS.md`
- [ ] P2 committed alone (the commit touches only `SPECS.md`)
- [ ] P3 no `.html` file exists anywhere in the repo history before this commit
- [ ] Pushed to `main`

Later edits to `SPECS.md` are allowed in later commits, but the first version
must land before any HTML.
