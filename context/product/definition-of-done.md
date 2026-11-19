---
title: Definition of done (build checklist)
topic: product
sources:
  - _raw/2026-11-19-brief/3-dod-build-pt1.png
  - _raw/2026-11-19-brief/4-dod-build-pt2.png
updated: 2026-11-19
status: stable
---

# Definition of done

## Summary

The build checklist from the brief, consolidated. Spec steps are in
[process-and-spec.md](process-and-spec.md).

## General

- [ ] Panel is a single `index.html`, or multiple linked HTML files (one per section).
- [ ] All styling via Tailwind CSS from CDN. No custom CSS files, no inline `style` attributes.
- [ ] All interactivity in vanilla JS. No frameworks, no jQuery, no build tools.
- [ ] Persistent sidebar linking all six sections, with an active-state indicator.

## Dashboard

- [ ] Four metric cards (total revenue, discount losses, active agents, failing agents), each with icon, label, hardcoded value.
- [ ] Full-width placeholder area below the cards for a weekly activity chart.

## User Management

- [ ] Table with at least 5 users: name, email, plan, status badge.
- [ ] Each row has a `⋮` dropdown with "View detail" and "Delete".
- [ ] "View detail" opens a modal with the full user record; closes via close button and backdrop click.

## Agent Management

- [ ] At least 4 agents, each with name, owner, status badge, collapsed skill list.
- [ ] Expand control reveals skills with a smooth transition; clicking again collapses.
- [ ] `⋮` dropdown with "Configure" and "Delete". "Configure" opens a modal with the system prompt in an editable `<textarea>`.

## Skills

- [ ] At least 4 skills, each with name, description, number of agents with it enabled.
- [ ] Brief in-panel explanation of what a "skill" is in AgentHub.
- [ ] `⋮` dropdown with "View detail" and "Delete".

## Agent Contracts

- [ ] Table with at least 4 contracts: client, agent, contracted skills, start/end dates, amount paid.
- [ ] `⋮` dropdown; "View detail" opens a modal with the full breakdown, itemized skills, and individual prices.

## Error Log

- [ ] At least 6 entries: timestamp, agent name, color-coded error type badge, short description.
- [ ] `⋮` dropdown with "View detail" and "Mark as resolved".

## Global interactions

- [ ] Dark/light toggle in the top bar switches the entire panel using Tailwind `dark:`; mode is preserved across sections.
- [ ] All dropdowns close on outside click.
- [ ] All modals close on backdrop click.

## Related

- [evaluation-criteria.md](evaluation-criteria.md)
- [../technical/constraints.md](../technical/constraints.md)
