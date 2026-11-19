# Deliverable 3: HTML prototype

Build strictly against `SPECS.md`. If the spec turns out wrong or incomplete,
fix the spec first (new commit), then build.

## Build order (suggested)

1. Page shell: `<header>` top bar, `<nav>` sidebar, `<main>`, Tailwind CDN,
   dark-mode setup. (T1–T7, L1–L3)
2. Shared components in vanilla JS: dropdown, modal, collapsible, theme
   toggle. (X1–X5)
3. Hardcoded data from the spec, defined once and reused across sections. (X7)
4. Sections in order: Dashboard, Users, Agents, Skills, Contracts, Error Log.
5. Tablet pass and visual polish. (T8, T9)

## Completion checklist

**Constraints**
- [ ] T1 one `index.html` or one linked file per section
- [ ] T2 Tailwind via CDN only
- [ ] T3 no custom CSS files
- [ ] T4 `grep -rn 'style=' --include='*.html' .` returns nothing
- [ ] T5 vanilla JS only, no frameworks, jQuery, or build tools
- [ ] T6 no network calls for data
- [ ] T7 semantic tags used correctly

**Shell**
- [ ] L1 sidebar links to all six sections
- [ ] L2 active-section indicator
- [ ] L3 dark/light toggle in the top bar

**Dashboard**
- [ ] D1.1 four metric cards with the four required metrics
- [ ] D1.2 each card has icon, label, value
- [ ] D1.3 full-width weekly chart placeholder below cards
- [ ] D1.4 counts match agent data

**User Management**
- [ ] D2.1 table, ≥5 users, name/email/plan/status badge
- [ ] D2.2 `⋮` dropdown: View detail, Delete
- [ ] D2.3 View detail → full user record modal
- [ ] D2.4 modal closes via button and backdrop

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

**Agent Contracts**
- [ ] D5.1 table, ≥4 contracts, all required columns
- [ ] D5.2 active and past contracts both present
- [ ] D5.3 `⋮` dropdown with View detail
- [ ] D5.4 View detail → breakdown modal with itemized skill prices
- [ ] D5.5 modal closes via button and backdrop
- [ ] D5.6 names, skills, and totals consistent

**Error Log**
- [ ] D6.1 ≥6 entries with timestamp, agent, type badge, description
- [ ] D6.2 color-coded badges by type or severity
- [ ] D6.3 `⋮` dropdown: View detail, Mark as resolved
- [ ] D6.4 View detail → full error trace modal
- [ ] D6.5 modal closes via button and backdrop
- [ ] D6.6 agent names match

**Global**
- [ ] X1 dark mode covers everything (sections, tables, badges, dropdowns, modals)
- [ ] X2 mode persists across all six sections
- [ ] X3 every row's dropdown opens and closes on click
- [ ] X4 every dropdown closes on outside click
- [ ] X5 every modal closes via button and backdrop
- [ ] X6 View detail modal works in Users, Skills, Contracts, Error Log
- [ ] X7 data consistent everywhere
