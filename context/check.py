#!/usr/bin/env python3
"""Check context/ and the graded commit-order rule.

Usage, from anywhere:  python3 context/check.py

Needs only Python 3 and git. Changes nothing. Exit 1 when anything FAILS;
WARN lines need a look but do not fail. What it checks:

1. Commit order (graded): no .html file in the working tree or in history
   unless SPECS.md was first committed alone, earlier. No .css files at all.
2. Every relative Markdown link in context/, and every @import line in the
   root AGENTS.md and CLAUDE.md, points at a file or folder that exists.
3. Every file in context/ is listed in context/README.md (directly, or
   through its folder).
4. Every DoD ID (P1, D2.4, X8 ...) mentioned anywhere is defined in
   definition-of-done.md, is defined once, and is ticked off by some
   checklist in deliverables/.
5. Every question number (Q1 ...) mentioned anywhere has a row in
   open-questions.md.
6. todo.md has a dated "Now" block, and no commits have landed since it
   was last updated.
7. Nothing is committed on a local main that is not on origin/main: work
   goes on a branch and reaches main through a pull request.

It also lists (INFO) every branch on GitHub that has not been merged into
main, so a new session sees work in flight. Run `git fetch origin --prune`
first, or the list and the history checks can be out of date.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
CTX = ROOT / "context"

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
IMPORT = re.compile(r"^@(\S+)$")
FENCE = re.compile(r"^\s*(```|~~~)")
DOD_ID = re.compile(r"\b(?:[PSTLX]\d+|D\d\.\d+)\b")
DOD_ROW = re.compile(r"^\|\s*([PSTLX]\d+|D\d\.\d+)\s*\|")
Q_ID = re.compile(r"\bQ\d+\b")
Q_ROW = re.compile(r"^\|\s*(Q\d+)\s*\|")
CHECKBOX = re.compile(r"^\s*- \[[ xX]\]")
NOW = re.compile(r"^## Now\b.*\b\d{4}-\d{2}-\d{2}\b", re.MULTILINE)

fails, warns, infos = [], [], []


def git(*args):
    """Run git in the repo; return stdout, or None if git fails."""
    try:
        out = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True)
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def rel(path):
    return path.relative_to(ROOT).as_posix()


def prose(path):
    """Yield (line number, line) outside fenced code blocks."""
    fenced = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced:
            yield number, line


def tree(*suffixes):
    return sorted(p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts and p.suffix.lower() in suffixes)


def check_commit_order():
    for path in tree(".css"):
        fails.append(f"{rel(path)}: CSS files are not allowed (DoD T3). Remove it; style with Tailwind classes.")
    html_now = [rel(p) for p in tree(".html", ".htm")]
    added = git("log", "--all", "--diff-filter=A", "--format=%H", "--", "*.html", "*.htm")
    spec = git("log", "--diff-filter=A", "--reverse", "--format=%H", "--", "SPECS.md")
    if added is None or spec is None:
        warns.append("git history is not readable here, so the commit-order rule was checked on files only.")
        added, spec = "", ""
    if git("rev-parse", "--is-shallow-repository") == "true":
        warns.append("Shallow clone: history is incomplete. Run `git fetch --unshallow`, then run this again.")
    html_commits = added.split()
    first_spec = spec.split()[0] if spec else None
    if not first_spec:
        if html_now or html_commits:
            where = ", ".join(html_now) or "commit " + html_commits[-1][:7]
            fails.append(f"HTML exists ({where}) but SPECS.md has never been committed. This breaks the graded "
                         "commit-order rule (DoD P3). Do not commit or push; remove the file. If it is already "
                         "pushed, stop and tell mae.")
        return
    touched = (git("show", "--name-only", "--format=", first_spec) or "").split("\n")
    if touched != ["SPECS.md"]:
        fails.append(f"The commit that added SPECS.md ({first_spec[:7]}) also touched other files (DoD P2): "
                     f"{', '.join(t for t in touched if t != 'SPECS.md')}. Tell mae.")
    for commit in html_commits:
        if commit == first_spec or git("merge-base", "--is-ancestor", first_spec, commit) is None:
            fails.append(f"Commit {commit[:7]} added HTML without the SPECS.md commit before it (DoD P3). Tell mae.")


def check_links(files):
    linked = set()
    for path in files:
        for number, line in prose(path):
            targets = LINK.findall(line)
            if path.parent == ROOT and (found := IMPORT.match(line.strip())):
                targets.append(found.group(1))
            for target in targets:
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                dest = (path.parent / target.split("#")[0]).resolve()
                if dest.exists():
                    linked.add((path, dest))
                else:
                    fails.append(f"{rel(path)}:{number}: {target} points at nothing. Fix or remove it.")
    return linked


def check_index(files, linked):
    readme = CTX / "README.md"
    listed = {dest for source, dest in linked if source == readme}
    for path in files:
        if path == readme or CTX not in path.parents:
            continue
        if path not in listed and not any(parent in listed for parent in path.parents if parent != CTX):
            fails.append(f"{rel(path)} is not in the index in context/README.md. Add a row for it.")


def check_ids(files):
    dod = CTX / "definition-of-done.md"
    defined = [m.group(1) for _, line in prose(dod) if (m := DOD_ROW.match(line))]
    for dup in sorted({i for i in defined if defined.count(i) > 1}):
        fails.append(f"definition-of-done.md defines {dup} more than once.")
    ticked = set()
    for path in files:
        for number, line in prose(path):
            ids = set(DOD_ID.findall(line))
            for unknown in sorted(ids - set(defined)):
                fails.append(f"{rel(path)}:{number}: {unknown} is not defined in definition-of-done.md.")
            if path.parent.name == "deliverables" and CHECKBOX.match(line):
                ticked |= ids
    missing = [i for i in defined if i not in ticked]
    if missing:
        warns.append(f"No checklist in deliverables/ has a box for: {', '.join(missing)}. Add one, or the item can "
                     "be forgotten.")

    questions = CTX / "open-questions.md"
    rows = [m.group(1) for _, line in prose(questions) if (m := Q_ROW.match(line))]
    for dup in sorted({q for q in rows if rows.count(q) > 1}):
        fails.append(f"open-questions.md lists {dup} more than once (a question is either open or answered).")
    for path in files:
        for number, line in prose(path):
            for unknown in sorted(set(Q_ID.findall(line)) - set(rows)):
                fails.append(f"{rel(path)}:{number}: {unknown} has no row in open-questions.md.")


def check_handoff():
    todo = CTX / "todo.md"
    if not NOW.search(todo.read_text(encoding="utf-8")):
        warns.append('context/todo.md has no dated "## Now (updated YYYY-MM-DD)" block. Write one before you stop.')
    last = git("log", "-1", "--format=%H", "--", "context/todo.md")
    since = git("log", "--no-merges", "--format=%h %s", f"{last}..HEAD") if last else None
    if since:
        subjects = since.splitlines()
        warns.append(f"{len(subjects)} commit(s) since context/todo.md was last updated: "
                     + "; ".join(subjects[:5]) + ("; ..." if len(subjects) > 5 else "")
                     + ". Check that its Now block and checkboxes still describe the repo.")


def check_branches():
    """Fail on local commits to main; list branches not yet merged into it."""
    if git("rev-parse", "--verify", "-q", "origin/main") is None:
        warns.append("origin/main is not known here, so branches were not checked. Run `git fetch origin --prune`.")
        return
    here = git("rev-parse", "--abbrev-ref", "HEAD")
    if here == "main" and git("rev-list", "origin/main..HEAD"):
        fails.append("Local main has commits that are not on origin/main. Nothing is committed straight to main: "
                     "move them to a branch (`git switch -c <branch>`) and open a pull request.")
    unmerged = git("for-each-ref", "--no-merged", "origin/main",
                   "--format=%(refname)|%(committerdate:short)|%(subject)", "refs/remotes/origin") or ""
    for line in unmerged.splitlines():
        ref, date, subject = line.split("|", 2)
        name = ref.removeprefix("refs/remotes/")
        if name in ("origin/HEAD", f"origin/{here}"):
            continue
        infos.append(f"Unmerged branch {name} (last commit {date}: {subject}). If it covers your task, continue "
                     f"it; its handoff is `git show {name}:context/todo.md`.")


def main():
    if not CTX.is_dir():
        print(f"FAIL  No context/ folder in {ROOT}.")
        return 1
    files = sorted(p for p in CTX.rglob("*.md"))
    pointer = [p for p in (ROOT / "AGENTS.md", ROOT / "CLAUDE.md") if p.is_file()]
    notes = [p for p in files if "_templates" not in p.parts]
    check_commit_order()
    linked = check_links(pointer + files)
    check_index(files, linked)
    check_ids(notes)
    check_handoff()
    check_branches()
    for line in fails:
        print(f"FAIL  {line}")
    for line in warns:
        print(f"WARN  {line}")
    for line in infos:
        print(f"INFO  {line}")
    print(f"{len(fails)} failed, {len(warns)} to look at.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
