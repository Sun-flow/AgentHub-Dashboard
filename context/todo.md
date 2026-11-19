# To-do

The ordered plan of work. Check items off as they are done and note the commit
or decision that closed them. Work top to bottom: each phase depends on the one
before it.

## Phase 0 — Organize (done)

- [x] Set up `context/` and ingest the brief (2026-11-19)
- [x] Transcribe the brief into [brief.md](brief.md) as the source of truth
- [x] Write [definition-of-done.md](definition-of-done.md), deliverable checklists, setup guide, domain model

## Phase 1 — Settle open questions

- [ ] mae answers or accepts the proposed defaults in [open-questions.md](open-questions.md)
- [ ] Record each answer in `decisions/` and update affected docs
- [ ] Choose Tailwind CDN version (Q11) and file structure (Q8)

## Phase 2 — Plan the hardcoded dataset

- [ ] Draft the canonical dataset following the rules in [domain.md](domain.md):
      ≥5 users, ≥4 agents (covering active, inactive, failing), ≥4 skills,
      ≥4 contracts (active and past), ≥6 errors (several types/severities)
- [ ] Derive dashboard values from it (active agents, failing agents, monthly revenue, discount losses)
- [ ] Cross-check consistency (agent names, skill counts, contract totals)

## Phase 3 — Write and commit SPECS.md

- [ ] Write `SPECS.md` at the repo root following [deliverables/1-specs.md](deliverables/1-specs.md)
- [ ] Cold-read test with a fresh agent
- [ ] Commit `SPECS.md` **alone**, before any HTML file exists, and push

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
