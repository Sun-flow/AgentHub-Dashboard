---
title: 4Geeks "html-hello" starter template
topic: references
sources:
  - https://github.com/4GeeksAcademy/html-hello/blob/main/README.md
  - mae, chat 2026-11-19
  - _raw/2026-11-19-brief/7-how-to-start.png
updated: 2026-11-19
status: stable
---

# 4Geeks "html-hello" starter template

## Summary

4Geeks Academy names this repo as the base for the project. mae's view: it is
probably largely unnecessary. It is a near-empty boilerplate for a first
website, so there is little to inherit beyond one Tailwind detail.

The brief's setup steps say to **fork** it as step 1. This repo was created
fresh instead, so it is not a fork.

## What the template contains

- A README telling you to create an `index.html` with basic HTML structure.
- A local preview server: `pip3 install flask && python3 server.py`.
- Notes that any number of HTML files can be added, and that CSS files can be
  linked with `<link rel="stylesheet" href="styles.css">`.
- An optional Tailwind CSS **v4** CDN tag:
  `<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>`

## What matters for AgentHub

- **Useful:** it points to the Tailwind v4 browser CDN, which affects how dark
  mode is set up (see [../technical/constraints.md](../technical/constraints.md)).
- **Optional:** the Flask `server.py` is only a convenience for local preview;
  opening `index.html` directly works for a static prototype. _(inferred)_
- **Conflicts with the brief:** the template's `styles.css` suggestion is not
  allowed. The brief forbids custom CSS files.

## Related

- [tools.md](tools.md)
