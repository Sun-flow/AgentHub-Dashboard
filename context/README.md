# AgentHub project context

Planning material for the AgentHub admin panel prototype: an HTML, Tailwind,
and vanilla JS admin panel for a platform where companies rent AI agents. This
folder is information and plans only. Nothing here is app code.

**Status:** the current state, the handoff from the last session, and the next
action are in the "Now" block at the top of [todo.md](todo.md). Status is
written nowhere else.

## Start here

Read in this order. This is the only reading list; other files point here.

1. [brief.md](brief.md) — the full client brief. **The brief is law.**
2. [definition-of-done.md](definition-of-done.md) — every brief expectation as a numbered, checkable item.
3. [todo.md](todo.md) — "Now" (where the work stands and the handoff), then the ordered plan.
4. [setup.md](setup.md) — session routine, rules that are easy to break, which source wins, where things go, tools, gotchas.
5. [open-questions.md](open-questions.md) and [decisions/](decisions/) — what is waiting on mae, and what mae has settled.
6. The checklist in [deliverables/](deliverables/) for the deliverable in hand, and [domain.md](domain.md) when writing data or the spec.

Then run `python3 context/check.py` from the repo root and read what it prints.

## Index

| File | What it is |
| --- | --- |
| [brief.md](brief.md) | Complete transcription of the brief (sections B0–B5) |
| [definition-of-done.md](definition-of-done.md) | DoD items P, S, T, L, D1–D6, X, W (accessibility) with source and check |
| [todo.md](todo.md) | "Now" block (state, handoff, next action), then Phases 0–6 with checkboxes |
| [setup.md](setup.md) | Session routine, repo, rules, which source wins, where things go, tools, dark mode, testing, gotchas |
| [domain.md](domain.md) | Entities, relationships, and consistency rules for the hardcoded data |
| [references.md](references.md) | html-hello template, Google Stitch, Tailwind |
| [open-questions.md](open-questions.md) | Questions waiting on mae, each with a proposed default, and the answered ones |
| [deliverables/README.md](deliverables/README.md) | The three deliverables and their order |
| [deliverables/1-specs.md](deliverables/1-specs.md) | SPECS.md outline and completion checklist |
| [deliverables/2-stitch-proposal.md](deliverables/2-stitch-proposal.md) | Stitch proposal steps and checklist |
| [deliverables/3-prototype.md](deliverables/3-prototype.md) | Build order and full completion checklist |
| [deliverables/4-final-review.md](deliverables/4-final-review.md) | Git, static, and manual test script mirroring the evaluation |
| [decisions/](decisions/) | One note per decision or batch of answers from mae |
| `check.py` | Checks the commit-order rule, links, DoD IDs, question numbers, the handoff, and branches. Run at session start and before every push |
| [_templates/context-note.md](_templates/context-note.md) | Template for a new note |

## Ingestion log

| Date | Input | Result |
| --- | --- | --- |
| 2026-11-19 | Brief bundle: 7 screenshots + mae's context message | Transcribed into brief.md |
| 2026-11-19 | 4Geeks html-hello README (link) | references.md, setup.md, Q11 |
| 2026-11-19 | mae: forking not required | decisions/2026-11-19-no-template-fork.md |
| 2026-11-19 | Synthesis pass | Raw screenshots and first-pass notes replaced by the files above (originals are in git history before this commit) |
| 2026-11-19 | mae's answers to Q3–Q13 | decisions/2026-11-19-open-question-answers.md; DoD items D1.5, D2.5, D4.7, D5.7, D6.7, D6.8, X8, X9 added, T1–T3, D5.3 changed; checklists, domain, setup updated |
| 2026-11-19 | mae: no more direct commits to main | decisions/2026-11-19-repo-workflow.md rewritten, setup.md |
| 2026-11-20 | mae's memory bank generator v5.4 (prompt and checker, uploaded) | Assessed against context/; five ideas adopted, see decisions/2026-11-20-keep-context-adopt-memory-bank-ideas.md; the upload is not kept in the repo |
| 2026-11-20 | mae: import the accessibility rules from past builds (TrackFlow-Company-Overhaul, tailwind-dashboard, html-tailwindcss-project) | decisions/2026-11-20-accessibility-from-past-builds.md; DoD items W1–W9 added; checklists, check.py updated |
| 2026-11-20 | mae: agents as a table, not cards; row click and a chevron expand skills; `⋮` keeps Configure and Delete | decisions/2026-11-20-agents-as-table.md; SPECS.md section 8, 12.9, 13.3 and criteria 21, 23, 27, 43, 52, 53 |
