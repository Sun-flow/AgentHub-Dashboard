---
title: Keep context/ and adopt five ideas from mae's memory bank
topic: decision
sources:
  - mae, chat 2026-11-20
  - mae's memory bank generator v5.4 (uploaded prompt and checker; not kept in the repo)
updated: 2026-11-20
status: stable
---

# Keep context/ and adopt five ideas from mae's memory bank

**Decision (2026-11-20):** `context/` stays this project's only system for project
knowledge. It is not converted into a `memory-bank/` folder. Five ideas from
the memory bank mae uses on other projects are folded into it.

mae's words: "I think the setup we've done here is also quite good, so I'd like
you to read over the memory bank generation and consider what you would
integrate into our setup". The choice of what to adopt was made by an agent at
mae's request; mae accepted it by merging the pull request that added this
note.

| Idea | Where it lives here |
| --- | --- |
| A root file that agents load automatically | `AGENTS.md` and `CLAUDE.md` at the repo root, which load [../README.md](../README.md) and [../todo.md](../todo.md) |
| One dated place for the current state and the handoff | The "Now" block at the top of [../todo.md](../todo.md) |
| A session routine with a fixed last step | "Session routine" in [../setup.md](../setup.md) |
| A rule for which source wins, and one home per kind of fact | "Which source wins" and "Where things go" in [../setup.md](../setup.md) |
| A check that a tool runs | `context/check.py` |

**Why:** the gaps were all about handoff between sessions that share no
memory. Nothing loaded `context/` automatically, status was written in five
places, there was no end-of-session step, and nothing enforced the graded
commit order.

**Left out, and why:**

- Separate `status.md`, `context.md`, and `notes.md` files: todo.md, README.md,
  and setup.md already hold what they would hold.
- Word limits per file: `context/` is about 9,000 words and the project ends
  after six phases.
- A work file per branch: the "Now" block travels with each branch, and the
  check lists unmerged branches, which is enough for one or two sessions at a
  time.
- A log folder: git history, pull requests, the todo.md checkboxes, and the
  README ingestion log already record what happened.
- Scheduled cleanup passes and 14-day staleness warnings: the project is too
  short to need them. The check warns instead when commits land without the
  "Now" block being updated.
- Undated decision file names and the proposed/active statuses: dated names
  have not collided, and open-questions.md already tracks what is still a
  default.
- The memory bank's own checker: it is built around a `memory-bank/` folder
  and would fail this repo's dated decision names and its mentions of files
  that do not exist yet, such as `SPECS.md`.
