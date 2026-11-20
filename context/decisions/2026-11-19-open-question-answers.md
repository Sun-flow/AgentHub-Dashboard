---
title: Answers to open questions Q3–Q13
topic: decision
sources:
  - mae, chat 2026-11-19 7:03 PM ET
updated: 2026-11-19
status: stable
---

# Answers to open questions Q3–Q13

mae answered these on 2026-11-19. Q1 and Q2 were not addressed and keep their
proposed defaults in [../open-questions.md](../open-questions.md).

| # | Decision | mae's words (paraphrased where noted) |
| --- | --- | --- |
| Q3 | **Discount and coupon losses = potential revenue − actual revenue.** Potential revenue is what everything sold would have earned at full list price; actual revenue is what it sold for. Each contract line therefore carries a list price and a sold price. | "any potential revenue reduced via discounts and coupons … the delta between potential revenue if all items sold at full price vs revenue generated based on the prices actually sold at" |
| Q4a | **Delete** safely removes the entity from the data store and from the UI. In the prototype the "database" is the in-memory JS dataset; after a delete, every view that depends on it re-renders so data stays consistent. | "delete safely deletes its relevant entity from the database (and UI)" |
| Q4b | **Mark as resolved** darkens the error entry (dims the whole row, the way resolved threads look in mae's projects interface). It stays in the list. | "Mark as resolved darkens a thread, the same way our projects interface works" |
| Q5 | **Skill detail modal** does not show price or contracts. **New requirement:** features unavailable on a user's subscription tier are greyed out with a lock icon that names the tier needed. | "no need for price and contracts in descriptions. IF there are features that are unavailable for a user's tier, we should grey them out with a lock icon that indicates the subscription tier" |
| Q6 | **Contracts dropdown** has only "View detail". Add other options only if clearly needed. | "don't add another dropdown, unless it seems necessary" |
| Q7 | Error severities and types confirmed as proposed. | "confirmed" |
| Q8 | **Single `index.html`.** | "single index" |
| Q9 | USD and the proposed date/timestamp formats approved. | "approved" |
| Q10 | `context/` in the repo does not conflict with the commit-order rule. | "agree" |
| Q11 | **Tailwind v4 browser CDN**, with one `<style type="text/tailwindcss">` block holding only the dark-mode variant line. mae allowed relaxing the custom-CSS rule for this unless the benefit was marginal; the benefit is real (4Geeks' own template points to v4, so it is what graders expect, and it is the current version), and the block is neither a CSS file nor an inline `style` attribute, so it meets the brief's wording. | "okay with lightening the custom CSS restriction for the more modern tailwind version, unless you think the benefit is marginal" |
| Q13 | Ignore the "Follow these instructions" link. | "dont worry about it" |

## Interpretations made while recording (open as Q14 and Q15)

- **Q4a "safely":** Delete asks for confirmation in an in-page modal (not a
  browser `confirm()` dialog), then removes the entity. Records that reference
  a deleted entity (e.g. a past contract or an error for a deleted agent) are
  kept as history; derived numbers (dashboard counts, skill "agents enabled")
  are recalculated.
- **Q5 tier locks:** each skill has a minimum subscription tier. The Skills
  catalog shows that tier, and the user detail modal lists skills with any
  above the user's plan greyed out behind a lock icon naming the required tier.
