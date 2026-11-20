# References

External things the brief mentions, and what matters about each.

## 4Geeks `html-hello` template

https://github.com/4GeeksAcademy/html-hello — the brief's suggested starting
repo. Not used: mae judged it largely unnecessary and the evaluators don't
require a fork. It contains only a README, a Flask `server.py` for local
preview, and two tips:

- Link CSS files with `<link rel="stylesheet">`. **Not allowed here** (no custom CSS).
- Load Tailwind v4 from `https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4`.
  This is the version chosen (Q11); setup in [setup.md](setup.md).

## Google Stitch

Google's AI UI design tool. The brief requires feeding `SPECS.md` to it to get
an initial visual proposal, then adapting that proposal by hand. Design
guidance only. See [deliverables/2-stitch-proposal.md](deliverables/2-stitch-proposal.md).

## Tailwind CSS

The only allowed styling method, via CDN, with `dark:` utilities for the theme
toggle. Setup details in [setup.md](setup.md).

## "Follow these instructions" link

The brief's setup steps end with "Need help getting started? Follow these
instructions." The link target was not captured (Q13).
