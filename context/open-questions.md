# Open questions

Gaps in the brief. Each has a **proposed default** that stays within the
brief, so work is never blocked: if mae hasn't answered by the time a question
matters, use the default and say so in `SPECS.md`. When mae answers, record it
in `decisions/` and update this file.

| # | Question | Proposed default | Affects |
| --- | --- | --- | --- |
| Q1 | Who is an agent's "owner"? | The client company that rents it (for idle agents, "AgentHub"). | Agents, Contracts |
| Q2 | Are users people at client companies, and is "plan" a subscription tier? | Yes: each user belongs to a client company; plan is the company's tier (e.g. Starter / Pro / Enterprise). | Users, data |
| Q3 | Where do "discount and coupon losses" come from? | Contracts may carry a discount line; the dashboard figure is their sum for the month. Shown in the contract breakdown modal. | Dashboard, Contracts |
| Q4 | What do "Delete" and "Mark as resolved" do? | Delete removes the row from the page (in memory, no confirmation dialog). Mark as resolved changes the entry's badge to "Resolved" and dims it. Not persisted. Form submission is not evaluated, so keep it simple. | Users, Agents, Skills, Error Log |
| Q5 | What does the Skill "View detail" modal show? | Name, full description, price, the list of agents that have it enabled, and the contracts that include it. | Skills |
| Q6 | Which actions does the Contracts dropdown have besides "View detail"? | "View detail" and "Cancel contract" (behaves like Delete for active contracts). | Contracts |
| Q7 | Which error types/severities and colors? | Severity: Critical (red), Error (orange), Warning (amber), Info (blue). Types: Timeout, API failure, Rate limit, Auth, Invalid output. | Error Log |
| Q8 | One `index.html` or one file per section? | Single `index.html` with JS section switching. Simpler dark-mode persistence, one place for shared data. | Structure |
| Q9 | Currency and date formats? | USD (`$12,400.00`), dates `Nov 19, 2026`, timestamps `2026-11-19 14:32 UTC`. | All |
| Q10 | Does `context/` in the repo conflict with the commit-order rule? | No. It holds only markdown. Never put an `.html` file in it before `SPECS.md` is committed. | Process |
| Q11 | Tailwind v3 or v4 CDN? | v3 Play CDN with `darkMode: 'class'` in JS config. Avoids any `<style>` block, so "no custom CSS" holds under the strictest reading. | Setup, dark mode |
| Q13 | Where does the brief's "Follow these instructions" link go? | Ignore unless mae provides it; the rest of the brief is complete without it. | Setup |

## Resolved

- **Q12 — Must the repo be a fork of html-hello?** No. See
  [decisions/2026-11-19-no-template-fork.md](decisions/2026-11-19-no-template-fork.md).
