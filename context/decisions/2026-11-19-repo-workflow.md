---
title: All changes go through a branch and pull request
topic: decision
sources:
  - mae, chat 2026-11-19
updated: 2026-11-19
status: stable
---

# All changes go through a branch and pull request

**Decision (2026-11-19, 7:09 PM ET):** no development goes directly to `main`.
Every change, including `context/` updates, is made on a branch and merged
through a pull request that mae reviews.

**History:** earlier the same day the repo was empty, and mae allowed context
work to be committed straight to `main`. Everything up to commit `c666a98`
landed that way. That permission is withdrawn.

**Note for the graded commit-order rule:** the `SPECS.md` commit must still
reach `main` before any HTML commit. Merge the SPECS.md PR (without squashing
it together with HTML work) before opening any PR that adds HTML.
