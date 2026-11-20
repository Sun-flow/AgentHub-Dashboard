# To-do

Where the work stands, then the ordered plan.

## Now (updated 2026-11-20)

This block is the only place the project's status is written. Rewrite it
before you stop (routine in [setup.md](setup.md)); do not append to it. On a
branch it describes that branch, so it is already true when the branch merges.

- **State:** planning is complete. `SPECS.md` is written and waits in its own
  pull request (#4, branch `claude/project-thread-kng3jc`, one commit). There
  is no HTML and no automated test. This branch adds the accessibility items
  W1–W9 to the DoD and does not touch `SPECS.md`.
- **Last session (2026-11-20):** at mae's request, imported the accessibility
  rules from mae's past builds (TrackFlow-Company-Overhaul, tailwind-dashboard,
  html-tailwindcss-project) as DoD section W; see
  [decisions/2026-11-20-accessibility-from-past-builds.md](decisions/2026-11-20-accessibility-from-past-builds.md).
  `check.py` now knows the W IDs.
- **In progress:** nothing half-finished.
- **Next action:** once PR #4 is merged, cover the W items `SPECS.md` does
  not yet state, in a new commit to `SPECS.md` on its own branch: a skip link
  (W7), `aria-hidden="true"` on the Heroicons SVGs (W4),
  `motion-reduce:transition-none` on the skill-list, chevron and menu
  transitions (W6), `aria-labelledby` on each section (W7), and a check that
  the palette's muted text and badges reach AA contrast in both themes (W5).
  The pending spec already covers focus rings, `aria-*` states, Escape and
  focus return (W2, W3, W8). Do not add these to PR #4: it must stay one commit.
- **Waiting on mae:** merging PR #4 and this pull request; Q1, Q2, Q14, Q15 in
  [open-questions.md](open-questions.md) (none blocks).
- **Tried and ruled out:** prefix A for the new items, because `SPECS.md`
  already uses A1–A14 for its assumptions.
- **Last verified:** `python3 context/check.py` printed "0 failed, 0 to look
  at" on this branch (2026-11-20).

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
- [ ] After that pull request is merged, add the accessibility gaps listed in "Now" (W4–W7) to `SPECS.md` in a new commit of its own
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
