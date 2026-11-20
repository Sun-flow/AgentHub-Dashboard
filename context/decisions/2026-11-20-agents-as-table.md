---
title: Agent Management is a table with expandable skills rows
topic: decision
sources:
  - mae, chat 2026-11-20 (tried Google Stitch, disliked the agent cards, asked for a table and set the row buttons)
updated: 2026-11-20
status: stable
---

# Agent Management is a table with expandable skills rows

## Summary

mae tried a Google Stitch proposal and did not like the agent cards. Agent
Management is now a table. `SPECS.md` AGT-1 to AGT-4, 12.9, 13.3 and
acceptance criteria 21, 23, 27, 43, 52 and 53 were rewritten to match.

## Details

- Clicking an agent's row opens a full-width row under it, between that agent
  and the next, showing its skills. It starts collapsed and keeps the 300ms
  height and fade transition the brief asks for (B1.3).
- At the far right of each row are two buttons, in this order:
  1. a down-pointing chevron that does the same as clicking the row. It shows
     that the row can expand, and flips to point up while expanded. It is also
     the keyboard control for the row.
  2. the `⋮` menu with Configure and Delete, unchanged.
- Clicks on `⋮` and its menu items never expand or collapse the row.
- No other row actions: mae declined sortable columns, Pause/Activate and a
  "View errors" link.
- Failing agents keep the red badge and get a red bar on the row's left edge
  in place of the card's red ring.
- Columns: Agent (name and purpose), Owner, Status, Last run, actions. Under
  `lg`, Owner and Last run fold under the agent name, like email in Users.

## Related

- [../brief.md](../brief.md) B1.3 (a listing; card vs table is not set by the brief)
- [../deliverables/2-stitch-proposal.md](../deliverables/2-stitch-proposal.md)
