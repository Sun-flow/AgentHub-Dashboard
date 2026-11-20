# Deliverable 3: HTML prototype

Build strictly against `SPECS.md`. If the spec turns out wrong or incomplete,
fix the spec first (new commit), then build.

## Build order (suggested)

1. Page shell in a single `index.html`: `<header>` top bar, `<nav>` sidebar,
   `<main>`, Tailwind v4 CDN, dark-mode variant. (T1–T7, L1–L3)
2. Shared components in vanilla JS: dropdown, modal, confirm-delete modal,
   collapsible, theme toggle, tier lock. (X1–X5, X8)
3. Hardcoded data from the spec, defined once as an in-memory store; every
   section renders from it so deletes propagate. (X7, X8)
4. Sections in order: Dashboard, Users, Agents, Skills, Contracts, Error Log.
5. Tablet pass and visual polish. (T8, T9)

## Completion checklist

**Constraints**
- [ ] T1 single `index.html`
- [ ] T2 Tailwind v4 browser CDN only
- [ ] T3 no CSS files; one `text/tailwindcss` block with only the dark variant
- [ ] T4 `grep -rn 'style=' --include='*.html' .` returns nothing
- [ ] T5 vanilla JS only, no frameworks, jQuery, or build tools
- [ ] T6 no network calls for data
- [ ] T7 semantic tags used correctly
- [ ] T8 usable at desktop (~1280px) and tablet (~768px) widths

**Shell**
- [ ] L1 sidebar links to all six sections
- [ ] L2 active-section indicator
- [ ] L3 dark/light toggle in the top bar

**Dashboard**
- [ ] D1.1 four metric cards with the four required metrics
- [ ] D1.2 each card has icon, label, value
- [ ] D1.3 full-width weekly chart placeholder below cards
- [ ] D1.4 counts match agent data
- [ ] D1.5 discount losses = full-price total − sold total

**User Management**
- [ ] D2.1 table, ≥5 users, name/email/plan/status badge
- [ ] D2.2 `⋮` dropdown: View detail, Delete
- [ ] D2.3 View detail → full user record modal
- [ ] D2.4 modal closes via button and backdrop
- [ ] D2.5 tier-locked skills greyed with lock icon + tier name

**Agent Management**
- [ ] D3.1 ≥4 agents with name, owner, status badge, skill list
- [ ] D3.2 skill lists collapsed on load
- [ ] D3.3 expand/collapse with visible smooth transition
- [ ] D3.4 `⋮` dropdown: Configure, Delete
- [ ] D3.5 Configure → modal with editable `<textarea>` system prompt
- [ ] D3.6 modal closes via button and backdrop
- [ ] D3.7 active, inactive, and failing all appear

**Skills**
- [ ] D4.1 ≥4 skills with name, description, agents-enabled count
- [ ] D4.2 in-panel "what is a skill" explanation
- [ ] D4.3 `⋮` dropdown: View detail, Delete
- [ ] D4.4 View detail → modal
- [ ] D4.5 modal closes via button and backdrop
- [ ] D4.6 counts match agent skill lists
- [ ] D4.7 minimum tier shown; modal has no price or contracts

**Agent Contracts**
- [ ] D5.1 table, ≥4 contracts, all required columns
- [ ] D5.2 active and past contracts both present
- [ ] D5.3 `⋮` dropdown with View detail only
- [ ] D5.4 View detail → breakdown modal with itemized skill prices
- [ ] D5.5 modal closes via button and backdrop
- [ ] D5.6 names, skills, and totals consistent
- [ ] D5.7 list price and sold price per skill shown

**Error Log**
- [ ] D6.1 ≥6 entries with timestamp, agent, type badge, description
- [ ] D6.2 color-coded badges by type or severity
- [ ] D6.3 `⋮` dropdown: View detail, Mark as resolved
- [ ] D6.4 View detail → full error trace modal
- [ ] D6.5 modal closes via button and backdrop
- [ ] D6.6 agent names match
- [ ] D6.7 resolved entries darkened in place
- [ ] D6.8 severity colors as agreed

**Global**
- [ ] X1 dark mode covers everything (sections, tables, badges, dropdowns, modals)
- [ ] X2 mode persists across all six sections
- [ ] X3 every row's dropdown opens and closes on click
- [ ] X4 every dropdown closes on outside click
- [ ] X5 every modal closes via button and backdrop
- [ ] X6 View detail modal works in Users, Skills, Contracts, Error Log
- [ ] X7 data consistent everywhere
- [ ] X8 Delete confirms in-page, removes from data + UI, dependent numbers update
- [ ] X9 USD and agreed date formats
