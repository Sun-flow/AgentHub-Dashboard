---
title: Domain entities
topic: domain
sources:
  - _raw/2026-11-19-brief/1-project-brief.png
  - _raw/2026-11-19-brief/README.md (mae's message)
updated: 2026-11-19
status: draft
---

# Domain entities

## Summary

The things the admin panel shows and how they relate, as far as the brief
describes them. Field lists are the fields the brief names; anything else is
marked inferred.

## Entities

- **User** — a registered platform user. Fields: name, email, plan, status.
  _(Relationship to "client" and "owner" is not stated.)_
- **Client** — a company renting agents; appears on contracts. Dashboard counts
  active agents "across all clients".
- **Agent** — an AI agent registered on the platform. Fields: name, owner,
  status (`active` / `inactive` / `failing`), skills, system prompt.
- **Skill** — a capability that can be attached to agents. Fields: name, short
  description, number of agents with it enabled. Skills are priced
  individually within a contract.
- **Contract** — a rental of an agent by a client. Fields: client, agent,
  contracted skills (each with a price), start date, end date, total amount
  paid. Can be active or past.
- **Error** — an execution error from an agent. Fields: timestamp, agent,
  error type / severity, short description, full trace, resolved state.

## Relationships

```
Client 1──* Contract *──1 Agent
Contract *──* Skill   (with a per-contract price)
Agent *──* Skill      (enabled skills)
Agent 1──* Error
Agent *──1 Owner      (a User or a Client? unclear)
```

## Dashboard metrics and their sources _(inferred)_

| Metric | Derived from |
| --- | --- |
| Total revenue (this month) | Contract amounts |
| Discount and coupon losses | Not modeled anywhere else in the brief |
| Active agents across all clients | Agents with status `active` |
| Agents flagged as failing | Agents with status `failing` |

## Related

- [../product/admin-panel-requirements.md](../product/admin-panel-requirements.md)
