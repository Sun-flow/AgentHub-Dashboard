---
title: Project overview
topic: product
sources:
  - _raw/2026-11-19-brief/README.md (mae's message)
  - _raw/2026-11-19-brief/1-project-brief.png
updated: 2026-11-19
status: stable
---

# Project overview

## Summary

AgentHub is a SaaS platform where companies rent AI agents. Each agent can be
equipped with skills and put to work on business tasks. This project is an
**HTML prototype of AgentHub's internal admin panel**, built by a freelance
developer so the team can review it, validate it, and hand it off to backend
engineers.

## Details

- **The business:** companies (clients) rent agents through contracts. Agents
  carry skills, and contracts price those skills individually.
- **What already exists:** a backend, and a rough idea of the admin panel.
- **What is being delivered:** a fully designed, front-end-only HTML prototype
  with hardcoded data. No backend integration.
- **Who uses the panel:** an internal AgentHub admin who oversees users,
  agents, skills, rental contracts, revenue, and agent failures. _(inferred
  from the six sections; the brief does not describe the admin further)_
- **Purpose of the prototype:** a reviewable artifact and a handoff reference
  for backend engineers, not production code.
- **Working method:** spec first. A `SPECS.md` is written and committed before
  any HTML. See [process-and-spec.md](process-and-spec.md).

## Related

- [admin-panel-requirements.md](admin-panel-requirements.md)
- [process-and-spec.md](process-and-spec.md)
- [definition-of-done.md](definition-of-done.md)
- [../technical/constraints.md](../technical/constraints.md)
- [../domain/entities.md](../domain/entities.md)
