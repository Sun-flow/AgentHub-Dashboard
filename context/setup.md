# Setup and working rules

What a future agent needs to know before touching this repo.

## Read first, in this order

1. [brief.md](brief.md) — the law.
2. [definition-of-done.md](definition-of-done.md) — the brief as checkable items.
3. [todo.md](todo.md) — where the work stands.
4. [open-questions.md](open-questions.md) and [decisions/](decisions/) — what is settled and what is not.
5. The checklist in [deliverables/](deliverables/) for the deliverable you are working on.
6. [domain.md](domain.md) when writing data or the spec.

## Repository

- GitHub: `Sun-flow/AgentHub-Dashboard`. Default branch: `main`.
- Created fresh, not forked from `4GeeksAcademy/html-hello` (allowed, see
  [decisions/2026-11-19-no-template-fork.md](decisions/2026-11-19-no-template-fork.md)).
- **Never commit directly to `main`.** Work on a branch and open a pull
  request for mae to review, including for `context/` updates
  ([decisions/2026-11-19-repo-workflow.md](decisions/2026-11-19-repo-workflow.md)).
- `context/` holds planning material.
- As of 2026-11-19 the repo holds only `context/`. No `SPECS.md`, no HTML.
- The prototype will be a single `index.html` at the repo root (Q8).

## Rules that are easy to break

- **Commit order is graded.** `SPECS.md` must be committed, alone, before any
  `.html` file is ever committed. Do not add HTML (even a scratch file, even in
  `context/`) until that commit is on `main`.
- **No CSS files, no `style="..."` attributes.** Tailwind classes only. The
  single exception is the dark-variant `text/tailwindcss` block below.
- **Vanilla JS only.** No React, Vue, jQuery, npm build steps.
- **Hardcoded data only.** No `fetch`, no backend, even though AgentHub has one.
- **The brief wins.** If a Stitch design, a habit, or another note conflicts
  with [brief.md](brief.md), follow the brief.

## Tools

| Tool | Use | Notes |
| --- | --- | --- |
| Tailwind CSS via CDN | All styling | See dark mode setup below |
| Vanilla JS | All interactivity | Inline `<script>` or a linked `.js` file are both fine (`.js` files are not banned) |
| Google Stitch | Visual proposal from `SPECS.md` | Google web tool; needs a person or an agent with browser access |
| A local static server (optional) | Preview | `python3 -m http.server` from the repo root, or just open `index.html`. The template's Flask `server.py` is not needed |
| GitHub Codespaces or a local clone | Editing | Either is fine per the brief |

## Tailwind CDN and dark mode (decided: v4, Q11)

Load the Tailwind v4 browser CDN and switch dark mode from OS preference to a
class, so the toggle can control it:

```html
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<style type="text/tailwindcss">
  @custom-variant dark (&:where(.dark, .dark *));
</style>
```

That style block is the **only** CSS allowed in the page. It holds the one
variant line and nothing else; every other style is a utility class. The
toggle adds or removes the `dark` class on `<html>`. Because the prototype is a
single `index.html` (Q8), the class stays put while switching sections, which
satisfies "mode preserved between sections". Pin an exact v4 version in the
URL when writing `SPECS.md`.

## Testing

- Manual, in a browser, at desktop (~1280px) and tablet (~768px) widths. The
  script is in [deliverables/4-final-review.md](deliverables/4-final-review.md).
- Playwright with Chromium is available in cloud sessions if an agent wants to
  automate the same clicks.

## Adding new material to `context/`

1. Distill it into the doc it belongs in (brief additions go into
   [brief.md](brief.md) only if they come from the client's brief).
2. If it adds a requirement, add a DoD item and update the affected checklist.
3. If it raises a question, add it to [open-questions.md](open-questions.md).
4. Update [README.md](README.md) (index and ingestion log) in the same commit,
   on a branch, and open a PR.
5. Raw inputs may be kept in `_raw/` while being worked on; remove them once
   synthesized (git history keeps them).
