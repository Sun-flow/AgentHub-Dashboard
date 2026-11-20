---
title: Proposed defaults accepted for Q1, Q2, Q14, Q15
topic: decision
sources:
  - mae, chat 2026-11-20 ("start with defaults")
updated: 2026-11-20
status: stable
---

# Proposed defaults accepted for Q1, Q2, Q14, Q15

## Summary

When asked whether to start writing `SPECS.md`, mae said "start with
defaults". The four open questions therefore take their proposed defaults.
`SPECS.md` section 3 states them as assumptions A1, A2, A4 and A6.

## Details

| # | Decision | In SPECS.md |
| --- | --- | --- |
| Q1 | An agent's owner is the client company currently renting it. An agent with no active rental is owned by "AgentHub". | A1 |
| Q2 | Users are people at client companies. A user's plan is the company's tier: Starter < Pro < Enterprise. | A2 |
| Q14 | "Safely deletes" means confirm in an in-page modal, then remove the entity. Contracts and errors that reference it are kept as history, and derived numbers are recalculated. | A4 |
| Q15 | Each skill has a minimum tier, shown in the Skills catalog. The user detail modal greys out skills above the user's plan behind a lock that names the tier. | A6 |

mae has not discussed these beyond accepting the defaults. If mae later
answers one differently, write a new note that supersedes this one and change
`SPECS.md` in its own commit.

## Related

- [2026-11-19-open-question-answers.md](2026-11-19-open-question-answers.md)
- [../open-questions.md](../open-questions.md)
