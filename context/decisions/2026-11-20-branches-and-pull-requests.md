---
title: Every change goes through a branch and a pull request
topic: decision
sources:
  - mae, chat 2026-11-20
updated: 2026-11-20
status: stable
---

# Every change goes through a branch and a pull request

**Decision (2026-11-20):** nothing is committed straight to `main` any more,
`context/` included. Work happens on a branch and reaches `main` through a
pull request that mae merges.

mae's words: "in the future, we should avoid development that goes directly to
main."

**Replaces:** [2026-11-19-repo-workflow.md](2026-11-19-repo-workflow.md), which
allowed context work to go straight to `main` while the repo was empty.

**What follows from it:**

- The session routine in [../setup.md](../setup.md) starts with a branch and
  ends with a pull request.
- `SPECS.md` gets a pull request of its own that holds one commit touching
  only `SPECS.md`, so the graded commit stays alone however it is merged
  (DoD P2, P3). The build branch is cut from `main` after that merge.
- `python3 context/check.py` fails if a local `main` has commits that are not
  on GitHub, and lists unmerged branches so a new session sees work in flight.

_(inferred)_ mae said "development"; this note applies it to `context/` too,
because the same message came while context changes were being made.
