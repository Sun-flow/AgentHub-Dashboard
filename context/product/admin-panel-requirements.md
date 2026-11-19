---
title: Admin panel requirements (the six sections)
topic: product
sources:
  - _raw/2026-11-19-brief/1-project-brief.png
  - _raw/2026-11-19-brief/3-dod-build-pt1.png
  - _raw/2026-11-19-brief/4-dod-build-pt2.png
updated: 2026-11-19
status: stable
---

# Admin panel requirements

## Summary

Six sections reached from a persistent sidebar, with a light/dark toggle in the
top bar. Every list row has a `⋮` action dropdown; most "View detail" actions
open a modal. Minimum hardcoded row counts are set per section.

## Shell (applies everywhere)

- **Persistent sidebar** with links to all six sections and an active-state
  indicator on the current one.
- **Top bar** with a light/dark toggle that switches the whole interface via
  Tailwind `dark:` utilities. The chosen mode persists while moving between
  sections.
- **Action dropdowns** (`⋮` button) open and close on click, and close on any
  outside click.
- **Modals** close via a close button and via a backdrop click.

## Sections

| # | Section | Content | Min. data | Row actions | Modal |
| --- | --- | --- | --- | --- | --- |
| 1 | Dashboard | 4 metric cards: total revenue (this month), discount and coupon losses, active agents across all clients, agents flagged as failing. Each card has an icon, label, hardcoded value. Full-width placeholder below for a weekly activity chart. | 4 cards | none | none |
| 2 | User Management | Table of users: name, email, plan, status badge | 5 rows | View detail, Delete | Full user record |
| 3 | Agent Management | Listing of agents: name, owner, status badge (active / inactive / failing), collapsed skill list. Expand control reveals skills with a smooth transition; click again collapses. | 4 agents | Configure, Delete | Configure: agent's system prompt in an editable `<textarea>` |
| 4 | Skills | Catalog of skills: name, short description, count of agents with it enabled. Includes a brief in-panel explanation of what a "skill" is on AgentHub. | 4 skills | View detail, Delete | Skill detail _(contents not specified)_ |
| 5 | Agent Contracts | Table of active and past rental contracts: client, rented agent, contracted skills, start/end dates, total amount paid | 4 rows | View detail (others unspecified) | Full contract breakdown with itemized skills and individual prices |
| 6 | Error Log | Agent execution errors: timestamp, agent name, color-coded error type/severity badge, short description | 6 entries | View detail, Mark as resolved | Full error trace |

## Data consistency

Hardcoded data must agree across sections: the same agent names appear in
Agent Management, Contracts, and the Error Log. See
[../domain/entities.md](../domain/entities.md).

## Related

- [definition-of-done.md](definition-of-done.md)
- [evaluation-criteria.md](evaluation-criteria.md)
