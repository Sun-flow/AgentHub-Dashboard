# Setup and working rules

What a future agent needs to know before touching this repo. The reading order
is the "Start here" list in [README.md](README.md).

## Session routine

When you start:

1. Run `git fetch origin --prune` and work on a branch cut from the current
   `origin/main` (or continue an unmerged branch that covers your task). Never
   commit to `main`.
2. Read the files in the "Start here" list in [README.md](README.md).
3. From the repo root, run `python3 context/check.py` and read what it prints,
   including the unmerged branches it lists. If it fails on something you did
   not cause, fix it before starting; if the failure is the commit-order rule,
   stop and tell mae.

While you work:

4. Write a fact down in the turn you learn it, in the place "Where things go"
   names. A session can end without warning.
5. Commit and push unfinished work to your branch. The next agent has no
   memory of this session, so anything not pushed is lost.

Before you stop:

6. Tick what is finished in [todo.md](todo.md) and rewrite its "Now" block so
   a stranger could continue: the state, what is half-finished and where it
   is, the next action, what you tried that did not work, what is waiting on
   mae, and the last thing you verified, with today's date.
7. Run `python3 context/check.py` again, commit, push the branch, and open a
   pull request (or update the open one) that says what it changes and what
   is left. mae reviews and merges; do not merge it yourself.

## Repository

- GitHub: `Sun-flow/AgentHub-Dashboard`. Default branch: `main`.
- Created fresh, not forked from `4GeeksAcademy/html-hello` (allowed, see
  [decisions/2026-11-19-no-template-fork.md](decisions/2026-11-19-no-template-fork.md)).
- Nothing is committed straight to `main`, `context/` included. Every change
  goes on a branch and reaches `main` through a pull request that mae merges
  ([decisions/2026-11-20-branches-and-pull-requests.md](decisions/2026-11-20-branches-and-pull-requests.md)).
- `context/` holds planning material: Markdown plus the one script `check.py`.
- `AGENTS.md` and `CLAUDE.md` at the repo root are pointers that load
  [README.md](README.md) and [todo.md](todo.md) for agents. They hold no
  project facts.
- The prototype will be a single `index.html` at the repo root (Q8).

## Rules that are easy to break

- **Commit order is graded.** `SPECS.md` must be committed, alone, before any
  `.html` file is ever committed. Do not add HTML (even a scratch file, even in
  `context/`, even on a branch) until that commit is on `main`. `SPECS.md`
  goes in its own pull request holding that one commit and nothing else, so the
  commit stays alone however the pull request is merged. Cut the build branch
  from `main` after that merge. `python3 context/check.py` fails if this is
  broken. Only mae can approve an exception.
- **No CSS files, no `style="..."` attributes.** Tailwind classes only. The
  single exception is the dark-variant `text/tailwindcss` block below.
- **Vanilla JS only.** No React, Vue, jQuery, npm build steps.
- **Hardcoded data only.** No `fetch`, no backend, even though AgentHub has one.
- **The brief wins.** If a Stitch design, a habit, or another note conflicts
  with [brief.md](brief.md), follow the brief.

## Which source wins

- **On what to build:** [brief.md](brief.md) first; then mae's decisions in
  [decisions/](decisions/), which fill gaps in the brief (the only approved
  departures from it are listed at the top of brief.md); then
  [definition-of-done.md](definition-of-done.md); then `SPECS.md`; then the
  checklists in [deliverables/](deliverables/). A Stitch design or a habit has
  no say.
- **On what exists and what is done:** git and the files themselves. If a note
  here says `SPECS.md` does not exist and `ls` shows it, the note is stale.
- When two sources disagree, correct the lower one in the same session and say
  so in the "Now" block of [todo.md](todo.md). Never change the brief to match
  another file.

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

## Where things go

Each kind of fact has one home. Other files link to it instead of repeating it.

| You have | Put it in | Also update |
| --- | --- | --- |
| New material from mae or the client (file, link, message) | The doc it belongs in, distilled. [brief.md](brief.md) only if it comes from the client's brief | README ingestion log. Raw files may sit in `_raw/` while being worked on; remove them once synthesized (git history keeps them) |
| A new or changed requirement | [definition-of-done.md](definition-of-done.md) first | The affected checklist in [deliverables/](deliverables/) |
| A decision or answer from mae | A new note in [decisions/](decisions/), in mae's words, from the template | Move the question to Answered in [open-questions.md](open-questions.md); the DoD if a requirement changed. If it replaces an earlier decision, mark the old note `superseded by <file>` |
| A question only mae can answer | [open-questions.md](open-questions.md), with a proposed default | The "Now" block if it blocks work |
| Progress, half-finished work, what you tried | The "Now" block and checkboxes in [todo.md](todo.md) | Nothing else: status is written nowhere else |
| A trap, a tool quirk, or a preference of mae's | "Gotchas and preferences" below, dated | — |
| A new file or folder in `context/` | — | A README index row in the same commit |

## Gotchas and preferences

Things learned while working that the brief and the files will not tell you.
Add an item in the turn you learn it, with the date. Remove it when it stops
being true.

- A cloud session's clone can be behind `origin/main`: on 2026-11-20 one
  started at the repo's first commit, seven commits back. Fetch before you
  read anything. (2026-11-20)
- Each session starts with no memory of earlier ones. Unpushed work is lost.
  (2026-11-20)
- The commit that adds `SPECS.md` must touch only `SPECS.md` (P2), and its
  pull request must hold only that commit. Tick todo.md and rewrite "Now" in a
  separate pull request after it. (2026-11-20)
- The two `@context/...` lines in the root `AGENTS.md` must each stay alone on
  a line with no backticks, or Claude Code will not load them. (2026-11-20)
- Dates in `context/` are UTC (`date -u +%F`). mae writes in US Eastern time,
  so an evening message from mae carries the next day's UTC date. (2026-11-20)
- If two branches both rewrote the "Now" block, do not merge the two texts:
  write it again from what is true after the merge. (2026-11-20)
- mae likes `context/` lean: change an existing file before adding a new one,
  and add no file or routine that a short-lived session will not keep up.
  (2026-11-20)
