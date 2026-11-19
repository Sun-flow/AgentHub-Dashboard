# Open questions

Questions raised while ingesting materials, and contradictions between inputs.
Each entry names the source that raised it. Move an entry to `decisions/` once
it is answered.

## From the project brief bundle (2026-11-19)

1. **Who is an agent's "owner"?** A user, a client company, or AgentHub
   itself? It affects how Users, Agents, and Contracts link up.
   _(1-project-brief.png)_
2. **Users vs clients.** Is a "user" a person at a client company, and is
   "plan" a client's subscription tier? _(1-project-brief.png)_
3. **Discount and coupon losses** appear on the Dashboard but nowhere else.
   Should contracts carry discounts so the number is traceable?
   _(1-project-brief.png)_
4. **What should "Delete" and "Mark as resolved" do** in the prototype? Remove
   the row / change the badge in the DOM, show a confirmation, or do nothing?
   Form submission is not evaluated, so this is open. _(5-evaluation-criteria.png)_
5. **Skill "View detail" modal contents** are not specified. _(1-project-brief.png)_
6. **Contract row actions** besides "View detail" are not named.
   _(4-dod-build-pt2.png)_
7. **Error types / severity levels** and their colors are not listed.
   _(1-project-brief.png)_
8. **Single file or one file per section?** Both are allowed. Single file makes
   dark-mode persistence simpler. _(3-dod-build-pt1.png)_
9. **Currency and date format** for revenue, prices, and timestamps.
10. **Repo layout vs the brief.** `SPECS.md` must sit at the repo root and be
    committed before any HTML. This repo's `main` already has the `context/`
    folder (markdown only, no HTML), which should be fine, but worth confirming.

## From the html-hello template (2026-11-19)

11. **Tailwind v3 or v4 CDN?** The 4Geeks template uses v4. In v4, class-based
    dark mode needs a `<style type="text/tailwindcss">` block with
    `@custom-variant`. That is not a CSS file or an inline `style` attribute,
    but a strict reader of "no custom CSS" might object. The v3 Play CDN avoids
    it with a JS config. _(references/html-hello-template.md)_
12. **Start from the template or not?** mae thinks it is largely unnecessary;
    this repo currently does not include it.
