# AgentHub Dashboard

A graded 4Geeks assignment: an admin-panel prototype for AgentHub, built in
HTML, Tailwind (CDN), and vanilla JS from a spec that is written first.
Everything known about the project is in `context/`: the brief, the definition
of done, mae's decisions, the plan, and the handoff from the last session.

Read these two files in full before doing anything. Links inside them are
relative to `context/`.

@context/README.md
@context/todo.md

Then follow the "Start here" list in the first file. Four things cannot wait
until you have read the rest:

- Never create an `.html` file on any branch until `SPECS.md` has been
  committed alone and that commit is on `main`. The graders read the git
  history, and history cannot be taken back. Only mae can approve an exception.
- Never commit to `main`. Work on a branch and open a pull request; mae merges
  it.
- Run `python3 context/check.py` when you start and before every push. It
  fails on the two mistakes above and on broken references inside `context/`.
- Before you stop, rewrite the "Now" block in `context/todo.md`, commit, and
  push your branch. The next agent starts with no memory of this session and
  sees only what is on GitHub.

The full rules and the session routine are in `context/setup.md`.
