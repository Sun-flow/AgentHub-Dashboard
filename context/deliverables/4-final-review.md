# Final review

Run this before declaring the project done. It mirrors brief B5 ("What We
Will Evaluate") one to one, so a pass here means a pass there.

## 1. Git history

```bash
# First commit that added SPECS.md, and first commit that added any HTML
git log --diff-filter=A --reverse --format='%h %ad %s' --date=iso -- SPECS.md | head -1
git log --diff-filter=A --reverse --format='%h %ad %s' --date=iso -- '*.html' | head -1
# The SPECS.md commit should touch only SPECS.md
git show --stat <specs-commit>
```

- [ ] SPECS.md commit is older than the first HTML commit (P3)
- [ ] SPECS.md commit contains only SPECS.md (P2)

## 2. Spec content

- [ ] ≥3 concrete specs per section, component inventory, numbered acceptance criteria (S3, S5, S6)

## 3. Static checks

```bash
grep -rn 'style=' --include='*.html' .        # expect nothing (T4)
find . -name '*.css' -not -path './.git/*'     # expect nothing (T3)
grep -rnE 'react|vue|jquery' --include='*.html' -i .   # expect nothing (T5)
```

- [ ] Semantic tags: `header`, `nav`, `main`, `section`, `table` present and used for their purpose (T7)

## 4. Manual test script (desktop ~1280px, then tablet ~768px)

1. Load the page. Sidebar shows six sections; the current one is highlighted.
2. Click each sidebar link; each section appears; the highlight follows.
3. Toggle dark mode. Visit all six sections; everything is dark, including
   badges, tables, dropdowns, and modals. Toggle back.
4. In every section with rows, open a `⋮` menu, close it by clicking `⋮` again,
   open it again and close it by clicking elsewhere.
5. Users, Skills, Contracts, Error Log: View detail opens a modal; close with
   the button; reopen; close by clicking the backdrop.
6. Agents: skill lists start collapsed; expand shows a visible transition;
   collapse again. Configure opens a modal with an editable textarea; close both ways.
7. Contracts modal shows itemized skill prices that add up to the total.
8. Check the same agent names appear in Agents, Contracts, and Error Log.
9. Repeat steps 1, 4, 5, 6 at tablet width; nothing overflows or becomes unusable.

- [ ] All steps pass at desktop width
- [ ] All steps pass at tablet width
- [ ] The panel looks professional and reads as a reference for backend engineers (T9)
