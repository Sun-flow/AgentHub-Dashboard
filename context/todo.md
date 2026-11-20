# To-do

Where the work stands, then the ordered plan.

## Now (updated 2026-11-20)

This block is the only place the project's status is written. Rewrite it
before you stop (routine in [setup.md](setup.md)); do not append to it. On a
branch it describes that branch, so it is already true when the branch merges.

- **State:** planning is complete and no deliverable has been started. The
  repo holds `context/`, `AGENTS.md`, and `CLAUDE.md`. There is no `SPECS.md`,
  no HTML, and no dataset draft.
- **Last session (2026-11-20):** added the root pointer files, this block, the
  session routine in setup.md, and `context/check.py`, and moved the repo to
  branches and pull requests. No project work.
- **In progress:** nothing. There is no half-finished work to pick up.
- **Next action:** Phase 2 below. Draft the dataset in a new
  `context/dataset.md` (add its row to the README index), following
  [domain.md](domain.md), and push it so it survives the session. It moves
  into `SPECS.md` in Phase 3.
- **Waiting on mae:** Q1, Q2, Q14, Q15 in [open-questions.md](open-questions.md).
  None of them blocks: use the proposed defaults and say so in `SPECS.md`.
- **Tried and ruled out:** nothing yet.
- **Last verified:** `python3 context/check.py` passed with no failures and no
  warnings (2026-11-20).

## Plan

Check items off as they are done and note the commit, pull request, or
decision that closed them. Work top to bottom: each phase depends on the one
before it.

## Phase 0 — Organize (done)

- [x] Set up `context/` and ingest the brief (2026-11-19)
- [x] Transcribe the brief into [brief.md](brief.md) as the source of truth
- [x] Write [definition-of-done.md](definition-of-done.md), deliverable checklists, setup guide, domain model

## Phase 1 — Settle open questions

- [x] mae answered Q3–Q13 (2026-11-19), recorded in `decisions/` and folded into the DoD
- [x] Tailwind v4 CDN (Q11) and single `index.html` (Q8) chosen
- [ ] Q1 (agent owner) and Q2 (users vs clients, plan = tier) answered, or defaults accepted
- [ ] Q14 and Q15 (the two interpretations recorded with mae's answers) confirmed, or defaults accepted

## Phase 2 — Plan the hardcoded dataset

- [ ] Draft the canonical dataset following the rules in [domain.md](domain.md):
      ≥5 users, ≥4 agents (covering active, inactive, failing), ≥4 skills,
      ≥4 contracts (active and past), ≥6 errors (several types/severities)
- [ ] Give each skill a list price and minimum tier; give each contract line a list and sold price
- [ ] Derive dashboard values from it (active agents, failing agents, monthly revenue, discount losses = full price − sold)
- [ ] Cross-check consistency (agent names, skill counts, contract totals)

## Phase 3 — Write and commit SPECS.md

- [ ] Write `SPECS.md` at the repo root following [deliverables/1-specs.md](deliverables/1-specs.md)
- [ ] Cold-read test with a fresh agent
- [ ] Commit `SPECS.md` **alone**, before any HTML file exists, in a pull request that holds only that commit
- [ ] After that pull request is merged, delete `context/dataset.md` in a separate pull request (the spec is then the only home for the data)

## Phase 4 — Stitch visual proposal

- [ ] Generate the proposal from `SPECS.md` ([deliverables/2-stitch-proposal.md](deliverables/2-stitch-proposal.md))
- [ ] Record divergences and adopted visual direction; update `SPECS.md` in a new commit if needed

## Phase 5 — Build the prototype

- [ ] Build against `SPECS.md` following [deliverables/3-prototype.md](deliverables/3-prototype.md)
- [ ] Keep `SPECS.md` and the build in sync (spec changes first, in their own commits)

## Phase 6 — Final review and handoff

- [ ] Run [deliverables/4-final-review.md](deliverables/4-final-review.md) at desktop and tablet widths
- [ ] Fix anything that fails; re-run only the failing checks
- [ ] Tell mae the prototype is ready for review
