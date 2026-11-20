# To-do

Where the work stands, then the ordered plan.

## Now (updated 2026-11-20)

This block is the only place the project's status is written. Rewrite it
before you stop (routine in [setup.md](setup.md)); do not append to it. On a
branch it describes that branch, so it is already true when the branch merges.

- **State:** `SPECS.md` is on `main` (PR #4), committed alone, and the
  accessibility DoD items W1–W9 are on `main` (PR #5). This branch adds the
  accessibility rules to `SPECS.md` (13.7, acceptance criteria 49–56) in a
  commit of its own. There is no HTML and no automated test.
- **Last session (2026-11-20):** wrote that `SPECS.md` change: skip link, one
  `sr-only` `<h1>`, sections labelled by their `<h2>`, `aria-hidden` on every
  icon, `inert` on collapsed skill lists, `motion-reduce:transition-none`, and
  muted text instead of `opacity-50` for resolved errors (ERR-5) and locked
  skills (USR modal, 12.11) so their text keeps AA contrast. The chart
  placeholder text changed from `slate-400`/`dark:slate-500` to
  `slate-500`/`dark:slate-400` for the same reason.
- **In progress:** nothing half-finished.
- **Next action:** Phase 4, the Stitch proposal from `SPECS.md`. Separately,
  the bookkeeping for PR #4 is still owed: a decision note for mae's "start
  with defaults" (Q1, Q2, Q14, Q15), moving those to Answered in
  [open-questions.md](open-questions.md), and ticking Phases 1–3 below.
- **Waiting on mae:** merging this pull request.
- **Tried and ruled out:** keeping `opacity-50` on dimmed rows: axe-core
  counts opacity in contrast, and half-opacity slate text fails 4.5:1.
- **Last verified:** `python3 context/check.py` printed "0 failed" on this
  branch (2026-11-20). Contrast figures for the muted pairs were judged from
  Tailwind's slate scale, not measured; W9's axe scan at build time measures
  them.

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
- [x] After that pull request is merged, add the accessibility rules (W1–W9) to `SPECS.md` in a new commit of its own (this branch, 2026-11-20)
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
