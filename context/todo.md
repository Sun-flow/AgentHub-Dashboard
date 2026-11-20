# To-do

Where the work stands, then the ordered plan.

## Now (updated 2026-11-20)

This block is the only place the project's status is written. Rewrite it
before you stop (routine in [setup.md](setup.md)); do not append to it. On a
branch it describes that branch, so it is already true when the branch merges.

- **State:** `SPECS.md` is on `main`: first version in PR #4 (commit
  `4811646`, alone and before any HTML), accessibility rules added in PR #7
  (13.7, acceptance criteria 49–56). The DoD has accessibility items W1–W9
  (PR #5). All open questions are settled: Q1, Q2, Q14 and Q15 took their
  defaults ([decisions/2026-11-20-defaults-accepted.md](decisions/2026-11-20-defaults-accepted.md)).
  Phases 1–3 are done. There is no HTML and no automated test.
- **Last sessions (2026-11-20):** wrote `SPECS.md` with the full dataset in
  section 14, so `context/dataset.md` was never created. A script checked the
  data: contract totals, list price = monthly price × term, skill counts
  4/3/3/3/2/2, tier rules, and dashboard values $49,740.00 / $5,160.00 / 3 / 2.
  A fresh agent then cold-read the spec. A second session added the
  accessibility rules: skip link, `sr-only` `<h1>`, `aria-labelledby`,
  `aria-hidden` icons, `inert` collapsed lists, `motion-reduce`, and muted text
  instead of `opacity-50` for contrast. This branch records the defaults and
  ticks the checklists.
- **In progress:** nothing half-finished.
- **Next action:** Phase 4, the Google Stitch proposal from `SPECS.md`
  ([deliverables/2-stitch-proposal.md](deliverables/2-stitch-proposal.md)).
  It needs mae or an agent with browser access.
- **Waiting on mae:** merging this pull request.
- **Tried and ruled out:** a separate `context/dataset.md`, because it would
  have needed a deletion PR later. Keeping `opacity-50` on dimmed rows: axe-core
  counts opacity in contrast, and half-opacity slate text fails 4.5:1.
- **Last verified:** `python3 context/check.py` printed "0 failed" on this
  branch after merging `main` (2026-11-20). The muted-text contrast figures
  were judged from Tailwind's slate scale, not measured; W9's axe scan at
  build time will measure them.

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
- [x] Q1 (agent owner) and Q2 (users vs clients, plan = tier) answered, or defaults accepted (defaults, 2026-11-20)
- [x] Q14 and Q15 (the two interpretations recorded with mae's answers) confirmed, or defaults accepted (defaults, 2026-11-20)

## Phase 2 — Plan the hardcoded dataset

- [x] Draft the canonical dataset (written straight into `SPECS.md` section 14, PR #4) following the rules in [domain.md](domain.md):
      ≥5 users, ≥4 agents (covering active, inactive, failing), ≥4 skills,
      ≥4 contracts (active and past), ≥6 errors (several types/severities)
- [x] Give each skill a list price and minimum tier; give each contract line a list and sold price
- [x] Derive dashboard values from it (active agents, failing agents, monthly revenue, discount losses = full price − sold)
- [x] Cross-check consistency (agent names, skill counts, contract totals)

## Phase 3 — Write and commit SPECS.md

- [x] Write `SPECS.md` at the repo root following [deliverables/1-specs.md](deliverables/1-specs.md)
- [x] Cold-read test with a fresh agent
- [x] Commit `SPECS.md` **alone**, before any HTML file exists, in a pull request that holds only that commit (PR #4, commit `4811646`, merged 2026-11-20)
- [x] After that pull request is merged, add the accessibility rules (W1–W9) to `SPECS.md` in a new commit of its own (PR #7, 2026-11-20)
- [x] ~~Delete `context/dataset.md`~~: not needed, the file was never created

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
