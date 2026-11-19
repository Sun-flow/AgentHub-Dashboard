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
| _No notes yet._ | | | |

## Ingestion log

| Date | Input | Notes created or updated |
| --- | --- | --- |
| _Nothing ingested yet._ | | |
