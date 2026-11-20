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
| User | name, email, plan, status _(brief)_; full record for the detail modal (proposed: id, company, role, signup date, last active) | Plan = subscription tier Starter / Pro / Enterprise (Q2 default) |
| Client | company name _(brief: appears on contracts)_ | Possibly the same as a user's company (Q2) |
| Agent | name, owner, status `active` / `inactive` / `failing`, skills, system prompt _(brief)_ | "Owner" meaning is open (Q1) |
| Skill | name, short description, number of agents with it enabled _(brief)_; minimum subscription tier _(Q5)_; list price _(Q3)_ | Detail modal shows no price or contracts (Q5) |
| Contract | client, agent, start date, end date, total amount paid, active or past _(brief)_; one line per contracted skill with list price and sold price _(brief + Q3)_ | Total paid = sum of sold prices |
| Error | timestamp, agent, error type, short description, full trace _(brief)_; severity, resolved flag _(Q4, Q7)_ | Severities Critical / Error / Warning / Info; types Timeout, API failure, Rate limit, Auth, Invalid output |

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
4. A contract's sold prices sum to its total amount paid. Each sold price is
   at or below the skill's list price.
5. A contract's skills are a subset of the rented agent's skills.
6. Dashboard "active agents" equals the count of agents with status `active`;
   "failing agents" equals the count with status `failing`.
7. Agents with status `failing` have recent entries in the Error Log.
8. Dashboard "total revenue (this month)" is the sum of sold prices on
   contracts billed this month. "Discount and coupon losses" is the sum of
   (list price − sold price) on the same lines.
9. Minimums: 5 users, 4 agents (all three statuses present), 4 skills,
   4 contracts (active and past), 6 errors (more than one type/severity).
10. Locks: a skill whose minimum tier is above a user's plan shows as locked
    for that user. Include at least one locked case so the lock is visible.
11. After a Delete, all derived numbers are recalculated from the remaining
    data; historical records (past contracts, errors) keep their references.
