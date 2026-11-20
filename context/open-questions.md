# Open questions

Gaps in the brief. Each open one has a **proposed default** that stays within
the brief, so work is never blocked: if mae hasn't answered by the time it
matters, use the default and say so in `SPECS.md`.

## Open

| # | Question | Proposed default | Affects |
| --- | --- | --- | --- |
| Q1 | Who is an agent's "owner"? | The client company that rents it (for idle agents, "AgentHub"). | Agents, Contracts |
| Q2 | Are users people at client companies, and is "plan" a subscription tier? | Yes: each user belongs to a client company; plan is the company's tier: Starter / Pro / Enterprise. Tier locks (see Q5 answer) depend on this. | Users, Skills, data |

## Answered

All answered by mae on 2026-11-19. Full wording and the interpretations made
are in [decisions/2026-11-19-open-question-answers.md](decisions/2026-11-19-open-question-answers.md).

| # | Question | Answer |
| --- | --- | --- |
| Q3 | Discount and coupon losses | Potential revenue at full price minus revenue at prices actually sold. Contract lines carry list and sold price. |
| Q4 | Delete / Mark as resolved | Delete safely removes the entity from the in-memory data and the UI, with dependent views re-rendered. Resolved errors are darkened in place. |
| Q5 | Skill detail modal | No price or contracts. New rule: features above a user's tier are greyed out with a lock icon naming the tier. |
| Q6 | Contracts dropdown | "View detail" only. |
| Q7 | Error severities/types | Critical (red), Error (orange), Warning (amber), Info (blue); types Timeout, API failure, Rate limit, Auth, Invalid output. |
| Q8 | File structure | Single `index.html`. |
| Q9 | Formats | USD `$12,400.00`; dates `Nov 19, 2026`; timestamps `2026-11-19 14:32 UTC`. |
| Q10 | `context/` vs commit order | No conflict, as long as no `.html` lands before `SPECS.md`. |
| Q11 | Tailwind version | v4 browser CDN, one `text/tailwindcss` style block for the dark variant only. |
| Q12 | Fork the template? | Not required. See [decisions/2026-11-19-no-template-fork.md](decisions/2026-11-19-no-template-fork.md). |
| Q13 | "Follow these instructions" link | Ignore. |
