# Domain model and data rules

The things the admin panel shows, how they relate, and the rules the hardcoded
dataset must follow. Fields marked _(brief)_ are required by the brief; others
are proposed and should be confirmed in `SPECS.md`.

## Product in one paragraph

AgentHub is a SaaS platform where companies (clients) rent AI agents. Agents
are equipped with skills (capabilities) and put to work on business tasks.
Clients rent agents through contracts that price each contracted skill. The
admin panel is AgentHub's internal tool for overseeing users, agents, skills,
contracts, revenue, and agent failures.

## Entities

| Entity | Fields | Notes |
| --- | --- | --- |
| User | name, email, plan, status _(brief)_; full record for the detail modal (proposed: id, company, role, signup date, last active) | "Plan" and the link to clients are open (Q2) |
| Client | company name _(brief: appears on contracts)_ | Possibly the same as a user's company (Q2) |
| Agent | name, owner, status `active` / `inactive` / `failing`, skills, system prompt _(brief)_ | "Owner" meaning is open (Q1) |
| Skill | name, short description, number of agents with it enabled _(brief)_; price per contract _(brief, via contracts)_ | Detail modal contents open (Q5) |
| Contract | client, agent, contracted skills, start date, end date, total amount paid, itemized skill prices _(brief)_; active or past _(brief)_ | Discounts possibly here (Q3) |
| Error | timestamp, agent, error type, short description, full trace _(brief)_; severity, resolved flag (proposed) | Types/severities open (Q7) |

## Relationships

```
Client 1──* Contract *──1 Agent
Contract *──* Skill      (each with a price on that contract)
Agent    *──* Skill      (skills enabled on the agent)
Agent    1──* Error
Agent    *──1 Owner      (User, Client, or AgentHub — see Q1)
User     *──1 Client?    (see Q2)
```

## Consistency rules for the hardcoded dataset

The brief grades consistency (B5), so the dataset must obey all of these:

1. Every agent named in Contracts and the Error Log exists in Agent Management.
2. Every skill on an agent or contract exists in the Skills catalog.
3. A skill's "agents enabled" count equals the number of agents listing it.
4. A contract's itemized skill prices sum to its total amount paid (minus any
   discount, if Q3 adds discounts).
5. A contract's skills are a subset of the rented agent's skills.
6. Dashboard "active agents" equals the count of agents with status `active`;
   "failing agents" equals the count with status `failing`.
7. Agents with status `failing` have recent entries in the Error Log.
8. Dashboard "total revenue (this month)" is derivable from contracts active
   this month (or stated as a figure with the rule written in `SPECS.md`).
9. Minimums: 5 users, 4 agents (all three statuses present), 4 skills,
   4 contracts (active and past), 6 errors (more than one type/severity).
