# Open questions

Gaps in the brief. Each open one has a **proposed default** that stays within
the brief, so work is never blocked: if mae hasn't answered by the time it
matters, use the default and say so in `SPECS.md`.

## Open

| # | Question | Proposed default | Affects |
| --- | --- | --- | --- |
| — | None open. | — | — |

## Answered

Q3–Q13 were all answered by mae on 2026-11-19. Q1, Q2, Q14 and Q15 took their proposed defaults on 2026-11-20, see [decisions/2026-11-20-defaults-accepted.md](decisions/2026-11-20-defaults-accepted.md). Full wording and the interpretations made
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
| Q1 | Agent owner | Default: the renting client company; "AgentHub" for idle agents. |
| Q2 | Users vs clients, plan | Default: users work at client companies; plan = company tier Starter / Pro / Enterprise. |
| Q14 | Meaning of "safely deletes" | Default: in-page confirm, remove, keep history, recalculate derived numbers. |
| Q15 | How tier locks work | Default: skills carry a minimum tier; locked skills greyed with a lock naming the tier in the user modal. |
