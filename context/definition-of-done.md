# Definition of Done

Every expectation in the [brief](brief.md), plus mae's decisions in
[decisions/](decisions/), as numbered, checkable items. Items sourced from a
decision are marked `decision Qn`. The
project is done when every item is checked. Nothing here is optional.

- **Source** points to the brief section the item comes from (B1–B5). Items
  marked **derived** follow directly from a brief rule (usually "hardcoded data
  is consistent across sections") rather than being stated word for word.
- **Check** says how a reviewer verifies it.
- Per-deliverable checklists in [deliverables/](deliverables/) reference these
  IDs. When an item changes, change it here first.

## P — Process and repository

| ID | Requirement | Source | Check |
| --- | --- | --- | --- |
| P1 | `SPECS.md` exists at the repository root. | B3 | `ls SPECS.md` at repo root |
| P2 | `SPECS.md` is committed in its own commit, containing no HTML file. | B3 | `git show --stat <commit>` lists only `SPECS.md` (context/ edits belong in separate commits too) |
| P3 | That commit comes before the first commit that adds any `.html` file. | B3, B5 | `git log --diff-filter=A --format='%h %ad' -- '*.html' SPECS.md` |
| P4 | A Google Stitch visual proposal was generated from `SPECS.md` and used as design guidance only. | B2, B3 | Proposal saved or described in `context/`; final UI matches the spec, not Stitch |
| P5 | The final prototype matches the requirements exactly where Stitch differs (structure, components, interactions). | B3 | Review against D-items below |
| P6 | Work happens in this team's own GitHub repo (`Sun-flow/AgentHub-Dashboard`). Forking the template is not required. | B2 + decision | — |
| P7 | Every change reaches `main` through a reviewed pull request; the SPECS.md PR merges before any PR that adds HTML, and its commit is not squashed together with HTML. | decision | PR history |

## S — SPECS.md content

| ID | Requirement | Source | Check |
| --- | --- | --- | --- |
| S1 | Short product description: what AgentHub is and who the admin user is. | B3 | Read |
| S2 | Tech stack and constraints: HTML, Tailwind via CDN, vanilla JS only, no frameworks, no backend. | B3 | Read |
| S3 | At least 3 specifications for **each** of the six sections. | B3, B5 | Count per section |
| S4 | Each spec entry names a component, describes its contents, and defines its behavior, at the detail level of the brief's Dashboard example. | B3 | Read each entry |
| S5 | Component inventory listing at least: sidebar, metric card, action dropdown, modal, badge, collapsible skill list, dark mode toggle. | B3, B5 | Read |
| S6 | Numbered acceptance criteria list of verifiable conditions. | B3, B5 | Read |
| S7 | At least one acceptance criterion per interactive behavior: dropdown, modal, collapsible, dark mode. | B3 | Read |
| S8 | Detailed enough that an AI coding agent could build the panel from `SPECS.md` alone without asking questions (includes the full hardcoded dataset, all labels, all behaviors). | B0, B3 | Hand the spec to a fresh agent; it should need nothing else |

## T — Technical constraints

| ID | Requirement | Source | Check |
| --- | --- | --- | --- |
| T1 | Delivered as a single `index.html` (brief allows one file per section; mae chose single). | B4, decision Q8 | File listing |
| T2 | All styling with Tailwind utility classes, loaded from the Tailwind v4 browser CDN. | B4, B5, decision Q11 | Read `<head>` |
| T3 | No custom CSS files. The only CSS in the page is one `<style type="text/tailwindcss">` block declaring the class-based `dark` variant for Tailwind v4. | B4, B5, decision Q11 | No `.css` files; the one style block contains only the variant line |
| T4 | No inline `style` attributes. | B4, B5 | `grep -n 'style=' *.html` returns nothing |
| T5 | All interactivity in vanilla JavaScript. No frameworks, no jQuery, no build tools. | B4 | Read scripts; no `package.json` build step |
| T6 | All data hardcoded. No API calls, no backend. | B1 | No `fetch`/XHR |
| T7 | Semantic HTML: `header`, `nav`, `main`, `section`, `table`, and similar, used correctly. | B5 | Read markup |
| T8 | Usable on desktop and tablet viewports. | B5 | Manual test at ~1280px and ~768px |
| T9 | Looks professional and is immediately usable as a reference for future development. | B1 | Visual review |

## L — Layout shell

| ID | Requirement | Source | Check |
| --- | --- | --- | --- |
| L1 | Persistent sidebar with navigation links to all six sections. | B1, B4, B5 | Click every link |
| L2 | Sidebar shows an active-state indicator on the current section. | B4 | Visual |
| L3 | Top bar contains the light/dark toggle. | B1, B4 | Visual |

## D1 — Dashboard

| ID | Requirement | Source | Check |
| --- | --- | --- | --- |
| D1.1 | Four metric cards: total revenue (this month), total discount and coupon losses, active agents across all clients, agents currently flagged as failing. | B1, B4 | Visual |
| D1.2 | Each card has an icon, a label, and a hardcoded value. | B4 | Visual |
| D1.3 | A full-width placeholder area below the cards represents a weekly activity chart. | B1, B4 | Visual |
| D1.4 | Active and failing agent counts agree with the Agent Management data. | derived (B5 consistency) | Count agents by status |
| D1.5 | "Discount and coupon losses" = potential revenue at full list price − revenue at prices actually sold, for the month, computed from contract lines. | decision Q3 | Recompute from contracts |

## D2 — User Management

| ID | Requirement | Source | Check |
| --- | --- | --- | --- |
| D2.1 | Table (`<table>`) with at least 5 hardcoded users: name, email, plan, status badge. | B1, B4 | Count rows |
| D2.2 | Each row has a `⋮` action dropdown with "View detail" and "Delete". | B1, B4 | Click |
| D2.3 | "View detail" opens a modal overlay with the full user record. | B1, B4 | Click |
| D2.4 | The modal closes via a close button and via backdrop click. | B1, B4 | Click both |
| D2.5 | The user detail modal lists skills/features; any above the user's plan are greyed out with a lock icon naming the required tier. | decision Q5 | Open a Starter user |

## D3 — Agent Management

| ID | Requirement | Source | Check |
| --- | --- | --- | --- |
| D3.1 | Listing of at least 4 agents: name, owner, status badge (active / inactive / failing), collapsed skill list. | B1, B4 | Count |
| D3.2 | Skill lists are hidden (collapsed) by default. | B1, B5 | Load page |
| D3.3 | Clicking the expand control reveals the agent's skills with a smooth, visible transition; clicking again collapses them. | B1, B4, B5 | Click twice |
| D3.4 | Each agent has a `⋮` dropdown with "Configure" and "Delete". | B1, B4 | Click |
| D3.5 | "Configure" opens a modal with the agent's system prompt in an editable `<textarea>`. | B1, B4 | Click, type |
| D3.6 | The modal closes via a close button and via backdrop click. | B4, B5 | Click both |
| D3.7 | All three statuses appear in the data so every badge color is visible. | derived (B1) | Visual |

## D4 — Skills

| ID | Requirement | Source | Check |
| --- | --- | --- | --- |
| D4.1 | Catalog of at least 4 skills: name, short description, number of agents with it enabled. | B1, B4 | Count |
| D4.2 | Brief in-panel explanation of what a "skill" means on AgentHub. | B1, B4 | Read |
| D4.3 | Each skill has a `⋮` dropdown with "View detail" and "Delete". | B1, B4 | Click |
| D4.4 | "View detail" opens a modal (counts toward the four-section minimum). | B5 | Click |
| D4.5 | The modal closes via a close button and via backdrop click. | B5 | Click both |
| D4.6 | Each skill's "agents enabled" count matches the skill lists in Agent Management. | derived (B5) | Count |
| D4.7 | Each skill shows its minimum subscription tier. The detail modal does **not** show price or contracts. | decision Q5 | Open modal |

## D5 — Agent Contracts

| ID | Requirement | Source | Check |
| --- | --- | --- | --- |
| D5.1 | Table (`<table>`) with at least 4 contracts: client, agent, contracted skills, start/end dates, total amount paid. | B1, B4 | Count |
| D5.2 | Includes both active and past contracts. | B1 | Dates/status |
| D5.3 | Each row has a `⋮` action dropdown with "View detail" (only, unless another option proves necessary). | B1, B4, decision Q6 | Click |
| D5.4 | "View detail" opens a modal with the full contract breakdown, including itemized skills and their individual prices. | B1, B4 | Click |
| D5.5 | The modal closes via a close button and via backdrop click. | B5 | Click both |
| D5.6 | Agent names match agents in Agent Management; skills match the Skills catalog; itemized sold prices add up to the total paid. | B5 + derived | Compare |
| D5.7 | The breakdown shows each skill's list price and sold price, so the discount is visible. | decision Q3 | Open modal |

## D6 — Error Log

| ID | Requirement | Source | Check |
| --- | --- | --- | --- |
| D6.1 | At least 6 hardcoded entries: timestamp, agent name, error type badge, short description. | B1, B4 | Count |
| D6.2 | Errors are visually categorized by type or severity with color-coded badges. | B1, B4 | Visual |
| D6.3 | Each entry has a `⋮` dropdown with "View detail" and "Mark as resolved". | B1, B4 | Click |
| D6.4 | "View detail" opens a modal with the full error trace. | B1 | Click |
| D6.5 | The modal closes via a close button and via backdrop click. | B5 | Click both |
| D6.6 | Agent names match agents in Agent Management. | B5 | Compare |
| D6.7 | "Mark as resolved" darkens the entry in place (dimmed row, stays in the list). | decision Q4 | Click |
| D6.8 | Severities use the agreed colors: Critical red, Error orange, Warning amber, Info blue. | decision Q7 | Visual |

## X — Global interactions

| ID | Requirement | Source | Check |
| --- | --- | --- | --- |
| X1 | The top-bar toggle switches the **entire** panel between light and dark using Tailwind `dark:` utilities. | B1, B4, B5 | Toggle; inspect every section, modal, and dropdown |
| X2 | The chosen mode is preserved while navigating between sections. | B4, B5 | Toggle, navigate all six |
| X3 | Every list row in every section has a working `⋮` dropdown that opens on click and closes on click. | B5 | Click |
| X4 | Every dropdown closes when clicking outside its menu. | B4, B5 | Click elsewhere |
| X5 | Every modal closes via its close button and via backdrop click. | B4, B5 | Click both |
| X6 | "View detail" opens a modal in at least four sections (Users, Skills, Contracts, Error Log). | B5 | Click |
| X8 | "Delete" (Users, Agents, Skills) asks for confirmation in an in-page modal, then removes the entity from the in-memory dataset and the UI; dependent numbers (dashboard counts, skill counts) re-render. | decision Q4 | Delete an agent, check dashboard |
| X9 | Money in USD (`$12,400.00`), dates `Nov 19, 2026`, timestamps `2026-11-19 14:32 UTC`. | decision Q9 | Visual |
| X7 | The same agent names appear consistently in Agent Management, Contracts, and Error Log, and all other hardcoded data agrees across sections. | B5 | Compare |

## Not evaluated (do not spend effort here)

Form submission, live search, and real page navigation (B5). Interactive
behaviors are tested by hand.
