# To-do

Where the work stands, then the ordered plan.

## Now (updated 2026-11-20)

This block is the only place the project's status is written. Rewrite it
before you stop (routine in [setup.md](setup.md)); do not append to it. On a
branch it describes that branch, so it is already true when the branch merges.

- **State:** `SPECS.md` is on `main`: first version in PR #4 (commit
  `4811646`, alone and before any HTML), accessibility rules in PR #7. This
  branch changes Agent Management from cards to a table: clicking a row, or
  the chevron at its far right, opens a full-width skills row under it; the
  `⋮` menu (Configure, Delete) is the only other row action
  ([decisions/2026-11-20-agents-as-table.md](decisions/2026-11-20-agents-as-table.md)).
  There is no HTML and no automated test.
- **Last sessions (2026-11-20):** mae tried a Google Stitch proposal and
  disliked its agent cards. This session summarized the agent spec, agreed
  the table and its row buttons with mae, and rewrote AGT-1 to AGT-4, 12.9,
  13.3 and acceptance criteria 21, 23, 27, 43, 52 and 53 in one `SPECS.md`
  commit.
- **In progress:** nothing half-finished.
- **Next action:** finish Phase 4 (save the Stitch screenshots and note under
  `context/design/`, list its divergences), then Phase 5, the build.
- **Waiting on mae:** merging this pull request.
- **Tried and ruled out:** a card grid for agents (mae prefers a table).
  Sortable columns, Pause/Activate and "View errors" row actions (mae chose
  none of the optional extras). A ring on a failing `<tr>` (rings do not draw
  on table rows; an inset left bar on the first cell is used instead).
- **Last verified:** `python3 context/check.py` printed "0 failed" on this
  branch (2026-11-20).

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
