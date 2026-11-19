# AgentHub project context

This folder holds the source materials and distilled context for AgentHub, a
dashboard for managing agents, their skills, and their actions. It is
information only: nothing here has been acted on yet, and nothing here changes
app code.

## How ingestion works

1. An input arrives (a file, a note, a link, a transcript).
2. If it is a file worth keeping verbatim, it is saved unchanged in `_raw/`.
3. Its content is distilled into one or more context notes in the topic folder
   that fits, using `_templates/context-note.md`. A note that already covers the
   subject is updated rather than duplicated.
4. Anything unclear or contradictory goes into `open-questions.md`.
5. The index below is updated in the same commit.

## Layout

| Folder | What goes there |
| --- | --- |
| `_raw/` | Original inputs, unchanged, named `YYYY-MM-DD-short-name.ext` |
| `product/` | Vision, goals, users, use cases, requirements, scope |
| `domain/` | The model of agents, skills, actions, and how they relate |
| `technical/` | Architecture, stack, data, integrations, constraints |
| `references/` | External links, prior art, comparable tools |
| `decisions/` | Decisions made, with date and reasoning |
| `_templates/` | Templates for new notes |
| `open-questions.md` | Unresolved questions and contradictions across inputs |

## Index

| Note | Summary | Sources | Updated |
| --- | --- | --- | --- |
| [product/overview.md](product/overview.md) | What AgentHub is and what this prototype is for | brief bundle | 2026-11-19 |
| [product/admin-panel-requirements.md](product/admin-panel-requirements.md) | The six sections, shell, row actions, modals | brief bundle | 2026-11-19 |
| [product/process-and-spec.md](product/process-and-spec.md) | Spec-first process and what SPECS.md must contain | brief bundle | 2026-11-19 |
| [product/definition-of-done.md](product/definition-of-done.md) | Build checklist per section | brief bundle | 2026-11-19 |
| [product/evaluation-criteria.md](product/evaluation-criteria.md) | The 12 criteria the deliverable is judged on | brief bundle | 2026-11-19 |
| [domain/entities.md](domain/entities.md) | Users, clients, agents, skills, contracts, errors and how they relate | brief bundle | 2026-11-19 |
| [technical/constraints.md](technical/constraints.md) | HTML, Tailwind CDN, vanilla JS, no backend | brief bundle | 2026-11-19 |
| [references/tools.md](references/tools.md) | Tailwind, Google Stitch, Git | brief bundle | 2026-11-19 |
| [references/html-hello-template.md](references/html-hello-template.md) | 4Geeks starter repo: what it has and what matters | GitHub link | 2026-11-19 |
| [decisions/2026-11-19-no-template-fork.md](decisions/2026-11-19-no-template-fork.md) | Forking html-hello is not required | mae, chat | 2026-11-19 |
| [decisions/2026-11-19-repo-workflow.md](decisions/2026-11-19-repo-workflow.md) | Context goes straight to main | mae, chat | 2026-11-19 |
| [open-questions.md](open-questions.md) | 13 open questions (1 resolved) | brief bundle, template | 2026-11-19 |

## Ingestion log

| Date | Input | Notes created or updated |
| --- | --- | --- |
| 2026-11-19 | Project brief bundle: 5 screenshots + context message ([_raw/2026-11-19-brief/](_raw/2026-11-19-brief/README.md)) | All notes above created |
| 2026-11-19 | Brief closing lines (`_raw/2026-11-19-brief/6-brief-closing.png`) | product/overview.md, technical/constraints.md |
| 2026-11-19 | 4Geeks html-hello template README (link) | references/html-hello-template.md (new), technical/constraints.md, open-questions.md |
| 2026-11-19 | "How to Start the Project" (`_raw/2026-11-19-brief/7-how-to-start.png`) | product/process-and-spec.md, references/html-hello-template.md, open-questions.md |
| 2026-11-19 | mae: evaluators don't care about forking | decisions/2026-11-19-no-template-fork.md (new), open-questions.md, product/process-and-spec.md |
