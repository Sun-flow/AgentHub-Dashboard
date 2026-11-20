# AgentHub Admin Panel — Specification

Version 1.1 · Nov 20, 2026 (1.1 adds accessibility: 13.7 and criteria 49–56)

This document is the contract for the AgentHub admin panel prototype. It is
written to be complete: a developer or an AI coding agent should be able to
build the whole prototype from this file alone, without asking questions.
Where this file gives an exact value (a label, a class, a number, a piece of
data), use exactly that value.

Contents

1. Product description
2. Tech stack and constraints
3. Decisions and assumptions
4. Visual system
5. Layout shell
6. Section 1: Dashboard
7. Section 2: User Management
8. Section 3: Agent Management
9. Section 4: Skills
10. Section 5: Agent Contracts
11. Section 6: Error Log
12. Component inventory
13. Interaction rules (13.7 Accessibility)
14. Hardcoded dataset
15. Derived values and formatting
16. Acceptance criteria
17. Out of scope

---

## 1. Product description

**AgentHub** is a SaaS platform where companies rent AI agents. An agent is
equipped with **skills** (capabilities such as drafting emails or extracting
data from documents) and put to work on business tasks. Client companies rent
an agent through a **contract** that lists the skills they pay for, each with
its own price. Every client company has a **subscription tier** (Starter, Pro,
or Enterprise) that decides which skills its people may use.

The **admin user** is a member of AgentHub's internal operations team. They use
this panel to oversee the platform: revenue and discount losses, the people
registered on the platform, the agents and their skills, rental contracts, and
agent execution errors. The admin in this prototype is **Jordan Lee, Platform
admin**.

**What this prototype is for:** a fully designed, clickable HTML prototype that
AgentHub's team can review, validate, and hand to backend engineers as a
reference. AgentHub already has a backend, but this prototype does not talk to
it: every value is hardcoded.

## 2. Tech stack and constraints

| # | Constraint |
| --- | --- |
| C1 | **One file:** the whole prototype is a single `index.html` at the repository root. All JavaScript is in one inline `<script>` at the end of `<body>` (plus the tiny theme script in `<head>`, see 13.4). No other files. |
| C2 | **HTML5**, `<!doctype html>`, `<html lang="en">`, `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1">`, `<title>AgentHub Admin</title>`. |
| C3 | **Tailwind CSS v4 via CDN only**, pinned: `<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4.3.5"></script>` in `<head>`. |
| C4 | **Class-based dark mode.** Immediately after the CDN script, exactly one style block, containing exactly one line: `<style type="text/tailwindcss">@custom-variant dark (&:where(.dark, .dark *));</style>`. This is the only CSS in the project. |
| C5 | **No custom CSS:** no `.css` files, no `<link rel="stylesheet">` (no web fonts), no `style="..."` attributes in the HTML, and no JavaScript that sets `element.style`. Every visual property is a Tailwind utility class. Arbitrary-value classes such as `grid-rows-[0fr]` are allowed. |
| C6 | **Vanilla JavaScript only:** no frameworks (React, Vue, etc.), no jQuery, no libraries, no npm, no build step. |
| C7 | **No backend:** no `fetch`, no XHR, no API calls. All data is the hardcoded store in section 14, held in memory. |
| C8 | **No browser dialogs:** never use `alert()`, `confirm()`, or `prompt()`. Confirmation uses the in-page modal. |
| C9 | **Semantic HTML:** `<aside>` + `<nav>` for the sidebar, `<header>` for the top bar, `<main>` for content, one `<section>` per panel section, `<table>` with `<thead>`/`<tbody>`/`<th scope="col">` for tabular data, `<article>` for agent and skill cards, `<dl>` for label/value lists in modals, `<button>` for every clickable control that is not a link. |
| C10 | **Viewports:** fully usable at desktop (1280px and wider) and tablet (768px to 1023px) widths with no horizontal page scroll. Narrower than 768px is not required but must not break (same layout as tablet). |
| C11 | **Icons:** inline SVG, outline style from Heroicons v2 (24×24 viewBox, `fill="none"`, `stroke="currentColor"`, `stroke-width="1.5"`), sized with classes (`size-5` unless stated). Every icon is decorative and carries `aria-hidden="true"`: the text or `aria-label` next to it gives the meaning. Icon names used in this spec are Heroicons names; reproduce each path as closely as you can (an equivalent outline icon with the same meaning is acceptable). The `⋮` action button uses the literal character `⋮` (U+22EE), not an icon. |
| C12 | **Font:** Tailwind's default `font-sans` stack. No web fonts. |

## 3. Decisions and assumptions

These were open questions. mae (the project owner) decided Q3–Q13 and told us
to use the proposed defaults for the rest ("start with defaults",
Nov 20, 2026). They are part of the contract.

| # | Assumption or decision | Effect in this spec |
| --- | --- | --- |
| A1 (Q1, default) | An agent's **owner** is the client company currently renting it. An agent with no active rental is owned by **AgentHub**. | Agent cards show the company name, or "AgentHub" for idle agents. |
| A2 (Q2, default) | **Users** are people who work at client companies. A user's **plan** is their company's subscription tier: **Starter**, **Pro**, or **Enterprise** (in that order, lowest to highest). Users at the same company always have the same plan. Contracts name the client company, not a person. | Users table "Plan" column; tier locks. |
| A3 (Q3) | **Discount and coupon losses** = potential revenue (every contract line at full list price) − actual revenue (the prices the lines actually sold at). Every contract line stores a list price and a sold price. | Dashboard card 2; contract breakdown modal. |
| A4 (Q4, Q14 default) | **Delete** is "safe": it always asks for confirmation in an in-page modal, then removes the entity from the in-memory store and the UI, and every view re-renders from the store. Records that reference a deleted entity as history (contracts, errors) are kept unchanged. Derived numbers (dashboard counts, skill "agents enabled" counts) are recalculated. Deletes last until the page is reloaded. | 13.5. |
| A5 (Q4) | **Mark as resolved** dims the error entry in place. It stays in the list. | 11, 13.6. |
| A6 (Q5, Q15 default) | Each skill has a **minimum tier**. The Skills catalog shows it. The user detail modal lists every skill; skills above the user's plan are greyed out with a lock icon that names the tier required. The skill detail modal shows no price and no contracts. | 7, 9. |
| A7 (Q6) | The Contracts dropdown has one option: "View detail". | 10. |
| A8 (Q7) | Error severities and colors: **Critical** red, **Error** orange, **Warning** amber, **Info** blue. Error types: Timeout, API failure, Rate limit, Auth, Invalid output. | 11. |
| A9 (Q9) | Money is USD as `$12,400.00`. Dates are `Nov 19, 2026`. Timestamps are `2026-11-19 14:32 UTC`. | 15. |
| A10 | **"Today" is fixed at Nov 20, 2026.** "This month" is November 2026. The prototype never reads the real clock for data. | Dashboard, contract status. |
| A11 | **Contracts are billed once, in full, on their start date.** "Revenue this month" is the total paid on contracts whose start date is in November 2026. A skill's list price is a monthly price; a contract line's list price is that monthly price × the contract's term in months. | Dashboard, dataset. |
| A12 | A contract is **Active** when its end date is on or after today (A10), otherwise **Past**. The status is stored in the data and agrees with this rule. | Contracts. |
| A13 | Configure → "Save prompt" updates the agent's system prompt in memory only (lost on reload). | 8. |
| A14 | The selected theme is also remembered across reloads in `localStorage` (key `agenthub-theme`), wrapped in `try/catch`; if storage is unavailable the panel starts in light mode. Default is light. | 13.4. |

## 4. Visual system

### 4.1 Colors and surfaces

| Role | Light | Dark |
| --- | --- | --- |
| Page background (`<body>`) | `bg-slate-50 text-slate-900` | `dark:bg-slate-950 dark:text-slate-100` |
| Surface (sidebar, top bar, cards, tables, modals) | `bg-white` | `dark:bg-slate-900` |
| Border | `border-slate-200` | `dark:border-slate-800` |
| Muted text | `text-slate-500` | `dark:text-slate-400` |
| Table header row | `bg-slate-50 text-slate-500` | `dark:bg-slate-800/60 dark:text-slate-400` |
| Row hover | `hover:bg-slate-50` | `dark:hover:bg-slate-800/50` |
| Primary text and icons | `text-indigo-600` | `dark:text-indigo-300` |
| Primary buttons | `bg-indigo-600 hover:bg-indigo-700 text-white` | `dark:bg-indigo-500 dark:hover:bg-indigo-400` |
| Focus ring (every button, link, textarea) | `focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600` | `dark:focus-visible:outline-indigo-400` |
| Danger (delete buttons) | `bg-red-600 hover:bg-red-700 text-white` | same |

Every element that has a light color class also has its `dark:` counterpart.
Nothing may stay light-colored in dark mode. Three elements are intentionally identical in both modes and are the only exceptions: the danger button, the brand tile and `JL` avatar (`bg-indigo-600 text-white`), and the trace `<pre>` (always dark, ERR-4).

### 4.2 Typography and spacing

- Page heading (section `<h2>`): `text-2xl font-semibold tracking-tight`.
- Section intro text: `text-sm text-slate-500 dark:text-slate-400`, one line under the heading.
- Table text: `text-sm`. Header cells: `text-xs font-medium uppercase tracking-wide`, left-aligned except money columns (right-aligned).
- Card and modal corners: `rounded-xl` (cards, tables) and `rounded-2xl` (modals).
- Shadow: cards and tables `shadow-sm`; modals `shadow-xl`; dropdown menus `shadow-lg`.
- Main content padding: `p-6` (desktop and tablet). Gap between blocks: `space-y-6`.

### 4.3 Badge colors

All badges: `inline-flex items-center gap-1 rounded-full px-2.5 py-0.5 text-xs font-medium`.

| Badge | Light classes | Dark classes |
| --- | --- | --- |
| User **Active** / Agent **active** / Contract **Active** | `bg-emerald-100 text-emerald-800` | `dark:bg-emerald-500/15 dark:text-emerald-300` |
| User **Invited** | `bg-sky-100 text-sky-800` | `dark:bg-sky-500/15 dark:text-sky-300` |
| User **Suspended** | `bg-rose-100 text-rose-800` | `dark:bg-rose-500/15 dark:text-rose-300` |
| Agent **inactive** / Contract **Past** / error **Resolved** | `bg-slate-100 text-slate-700` | `dark:bg-slate-700/50 dark:text-slate-300` |
| Agent **failing** / severity **Critical** | `bg-red-100 text-red-800` | `dark:bg-red-500/15 dark:text-red-300` |
| Severity **Error** | `bg-orange-100 text-orange-800` | `dark:bg-orange-500/15 dark:text-orange-300` |
| Severity **Warning** | `bg-amber-100 text-amber-800` | `dark:bg-amber-500/15 dark:text-amber-300` |
| Severity **Info** | `bg-blue-100 text-blue-800` | `dark:bg-blue-500/15 dark:text-blue-300` |
| Plan/tier **Starter** | `bg-slate-100 text-slate-700` | `dark:bg-slate-700/50 dark:text-slate-300` |
| Plan/tier **Pro** | `bg-indigo-100 text-indigo-800` | `dark:bg-indigo-500/15 dark:text-indigo-300` |
| Plan/tier **Enterprise** | `bg-violet-100 text-violet-800` | `dark:bg-violet-500/15 dark:text-violet-300` |
| Skill chip (neutral) | `bg-slate-100 text-slate-700 rounded-md` (not `rounded-full`) | `dark:bg-slate-800 dark:text-slate-300` |

Agent and user status badges start with a 6px dot: `<span class="size-1.5 rounded-full bg-current"></span>`.
Badge text is exactly the status word as written in the dataset (agent
statuses are lowercase: `active`, `inactive`, `failing`).

## 5. Layout shell

**SHELL-1 — Page frame.** The first child of `<body>` is the skip link (13.7). After it, `<body>` holds one `<div class="flex min-h-screen">`
with two children: the sidebar `<aside>` and a content column
`<div class="flex min-w-0 flex-1 flex-col">`. The content column holds the
top bar `<header>` then `<main id="main" class="flex-1 p-6">`. `<main>` starts with
`<h1 class="sr-only">AgentHub Admin</h1>` (the page's only `<h1>`), then holds the six
`<section>` elements in this order, with these ids: `dashboard`, `users`,
`agents`, `skills`, `contracts`, `errors`. Exactly one section is visible at a
time; the others have the `hidden` class. No ancestor of a table or card list
may use `overflow-hidden` or `overflow-auto` (dropdown menus must never be
clipped); the only scroll container besides the page is the modal panel. (`<body>` gets `overflow-hidden` only while a modal is open, 13.2, when every menu is closed.)

**SHELL-2 — Sidebar.** `<aside class="sticky top-0 flex h-screen w-20 shrink-0 flex-col border-r lg:w-64">`
(surface + border colors from 4.1). Top: brand block, height `h-16`, with a
`size-9 rounded-lg bg-indigo-600 text-white` tile showing the `cpu-chip` icon,
and next to it (visible from `lg` only, `hidden lg:block`) the word
**AgentHub** (`font-semibold`) above **Admin** (`text-xs` muted). Below it,
`<nav aria-label="Primary">` with a `<ul>` of six links, in this order:

| # | Label | `href` | Icon |
| --- | --- | --- | --- |
| 1 | Dashboard | `#dashboard` | `squares-2x2` |
| 2 | User Management | `#users` | `users` |
| 3 | Agent Management | `#agents` | `cpu-chip` |
| 4 | Skills | `#skills` | `puzzle-piece` |
| 5 | Agent Contracts | `#contracts` | `document-text` |
| 6 | Error Log | `#errors` | `exclamation-triangle` |

Each link: `flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium`,
icon then label. On tablet (`< lg`) the label is visually hidden
(`sr-only lg:not-sr-only`) and the link is centered (`justify-center
lg:justify-start`), and the link has a `title` attribute equal to its label so
it shows a native tooltip. At the bottom of the sidebar (`mt-auto`, visible
from `lg` only) a muted line: `Prototype · hardcoded data`.

**SHELL-3 — Active state.** The link for the visible section has
`aria-current="page"` and the classes `bg-indigo-50 text-indigo-700
dark:bg-indigo-500/15 dark:text-indigo-300`. Other links use `text-slate-600
hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400
dark:hover:bg-slate-800 dark:hover:text-slate-100`. Exactly one link is active
at any time.

**SHELL-4 — Top bar.** `<header class="sticky top-0 z-20 flex h-16 items-center justify-between border-b px-6 ...">`
(surface + border colors). Left: a breadcrumb, muted `AgentHub Admin`, a `/`,
then the current section's label (same text as its sidebar link) in
`font-medium`, updated on every navigation. Right, in order: the **dark mode
toggle** (12.10) and the admin identity: a `size-8 rounded-full bg-indigo-600
text-white text-xs font-semibold` circle with the initials **JL**, followed (from
`lg` only) by **Jordan Lee** (`text-sm font-medium`) over **Platform admin**
(`text-xs` muted).

**SHELL-5 — Section header.** Each `<section>` has `aria-labelledby="<id>-title"` and starts with a `<div>` holding
its `<h2 id="<id>-title" tabindex="-1">` (the section label) and one line of intro text, listed per section
below. Sections with a list also show a count on the right of that header,
muted `text-sm`, e.g. `6 users`; it re-renders after deletes. Counts use the singular for 1 (`1 user`, `1 agent`, `1 skill`, `1 contract`, `1 error`) and the plural otherwise, including 0.

**SHELL-6 — Navigation.** Clicking a sidebar link calls `event.preventDefault()`, shows its section, hides the
others, moves the active state, updates the breadcrumb, writes the hash with
`history.replaceState(null, "", "#<id>")` (so the browser does not jump to the
element), then calls `window.scrollTo(0, 0)`. On load, and on `hashchange`, the
section named by `location.hash` is shown; an empty or unknown hash shows the
Dashboard. Navigation never reloads the page, so the theme and every in-memory
change (deletes, resolved errors, saved prompts) survive it. Any open dropdown
closes on navigation.

## 6. Section 1: Dashboard

Heading **Dashboard**. Intro: `Platform health for November 2026.`

**DASH-1 — Metric card grid.** A grid of four metric cards
(`grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-4`): 2×2 on tablet, one
row of four at 1280px and wider. Cards, in order:

| # | Label | Value (initial) | Sub-line (initial) | Icon | Accent |
| --- | --- | --- | --- | --- | --- |
| 1 | Total revenue (this month) | `$49,740.00` | `3 contracts billed in November 2026` | `banknotes` | emerald |
| 2 | Discount & coupon losses | `$5,160.00` | `Full price $54,900.00 − sold $49,740.00` | `receipt-percent` | amber |
| 3 | Active agents | `3` | `of 6 agents on the platform` | `bolt` | indigo |
| 4 | Failing agents | `2` | `Flagged as failing right now` | `exclamation-circle` | red |

All four values and sub-lines are computed from the store (section 15), not
typed into the HTML. Cards 3 and 4 change when an agent is deleted. Cards 1 and 2
never change, because contracts are history and cannot be deleted.

**DASH-2 — Metric card anatomy.** Each card is an `<article>` with surface,
border, `rounded-xl p-5 shadow-sm`. Top row: the label (`text-sm font-medium`
muted) on the left and the icon on the right inside a `size-10 rounded-lg`
tile in the accent color (`bg-<accent>-100 text-<accent>-700
dark:bg-<accent>-500/15 dark:text-<accent>-300`, e.g. `bg-emerald-100
text-emerald-700`). Below: the value (`mt-3 text-3xl font-semibold
tracking-tight`), then the sub-line (`mt-1 text-xs` muted). Each card has a
`border-l-4` in its accent color (`border-l-emerald-500`, `border-l-amber-500`,
`border-l-indigo-500`, `border-l-red-500`) so the four metric types are
distinct at a glance. Cards are not clickable.

**DASH-3 — Weekly activity chart placeholder.** Below the grid, a full-width
block (`w-full`): a surface card with the heading **Weekly activity**
(`text-base font-semibold`) and the muted text `Agent runs per day, last 7
days`. Inside it, a placeholder `div` `mt-4 flex h-64 flex-col items-center
justify-center gap-2 rounded-lg border-2 border-dashed border-slate-300
dark:border-slate-700 text-slate-500 dark:text-slate-400`, centered contents:
the `chart-bar` icon (`size-8`), the label `Weekly activity chart` (`text-sm
font-medium`), and `Chart placeholder: Mon–Sun` (`text-xs`). It has no
behavior.

## 7. Section 2: User Management

Heading **User Management**. Intro: `People registered on AgentHub, by client company.`
Count: `<n> users`.

**USR-1 — Users table.** A `<table class="w-full text-sm">` inside a surface
wrapper `rounded-xl border shadow-sm` (no overflow classes; round the header
corners with `rounded-tl-xl` / `rounded-tr-xl` on the first and last `<th>`).
Columns:

| Column | Content | Responsive |
| --- | --- | --- |
| Name | `size-8` circle with the user's initials (`bg-slate-200 text-slate-700 dark:bg-slate-700 dark:text-slate-200 text-xs font-semibold`), then the name (`font-medium`) with the company under it (`text-xs` muted). Under `lg` the email is also shown under the company. | always |
| Email | the email, muted | `hidden lg:table-cell` |
| Plan | plan badge (4.3) | always |
| Status | status badge with dot: Active / Invited / Suspended | always |
| (actions) | `⋮` action dropdown, right-aligned; header cell is empty with `<span class="sr-only">Actions</span>` | always |

Rows are rendered from the store in dataset order (U-101 to U-106). Rows have
`border-t` and the row hover color. If every user has been deleted, the body
shows one row spanning all columns: `No users.` (centered, muted, `py-10`).

**USR-2 — Row action dropdown.** Each row's `⋮` opens a menu (12.4) with two
items: **View detail** (icon `eye`) and **Delete** (icon `trash`, red text
`text-red-600 dark:text-red-400`).

**USR-3 — User detail modal.** "View detail" opens the modal (12.5) titled
with the user's name, with the subtitle `<email>`. Body, a `<dl>` in two
columns (`grid grid-cols-2 gap-4`; `<dt>` `text-xs` muted, `<dd>` `text-sm
font-medium`) with every field of the user record, in this order: User ID,
Company, Role, Plan (badge), Status (badge), Joined (date), Last active
(timestamp, or `Never`), Email. Footer: one secondary button **Close**.

**USR-4 — Skill access with tier locks.** In the same modal, below the `<dl>`,
a block headed **Skill access** (`text-sm font-semibold`) with the muted line
`Skills available on the <Plan> plan.` and a `<ul>` with one row per skill in
the current store, in catalog order. Each row: skill name (`text-sm`) on the
left; on the right either
- **included** (user's plan ≥ skill's minimum tier): `check-circle` icon in
  `text-emerald-600 dark:text-emerald-400` and the text `Included`; or
- **locked** (user's plan < skill's minimum tier): the whole row gets
  muted text `text-slate-500 dark:text-slate-400` (not `opacity-*`, which
  would fail contrast), a `lock-closed` icon, and the text
  `Requires <Tier>` (e.g. `Requires Pro`), plus a `title` of
  `Upgrade to <Tier> to unlock`.
Tier order is Starter < Pro < Enterprise. Example: Sofia Ramirez (Starter) sees
Email Drafting and Scheduling included, and Ticket Triage, Knowledge Base Q&A,
Document Summarization (`Requires Pro`) and Data Extraction (`Requires
Enterprise`) locked.

**USR-5 — Delete user.** "Delete" opens the confirm-delete modal (12.6) with
title `Delete user?` and body `<Name> (<email>) will be removed from AgentHub.
This can't be undone in this prototype.` Confirming removes the user from the
store and re-renders (the row disappears and the count drops). Nothing else
references users, so no other view changes.

## 8. Section 3: Agent Management

Heading **Agent Management**. Intro: `Every agent on the platform, who runs it, and what it can do.`
Count: `<n> agents`.

**AGT-1 — Agent card list.** A `<ul class="grid grid-cols-1 gap-4 xl:grid-cols-2">`;
each `<li>` holds an `<article>` card (surface, border, `rounded-xl p-5
shadow-sm`), in dataset order (A-01 to A-06). Card header row: on the left, a
`size-10 rounded-lg` tile with the `cpu-chip` icon (indigo accent colors as in
DASH-2), the agent name (`text-base font-semibold`), and its purpose under it
(`text-sm` muted); on the right, the status badge then the `⋮` dropdown. Below
the header: a `<dl class="mt-4 grid grid-cols-2 gap-4">` with two items, each a
`<dt>` (`text-xs` muted) above a `<dd>` (`text-sm font-medium`): **Owner** with
the owner name, and **Last run** with the timestamp. If every agent has
been deleted, show a single muted card `No agents.`

**AGT-2 — Status badge.** One of `active` (emerald), `inactive` (slate),
`failing` (red), with dot (4.3). The dataset contains all three. A failing
card also gets `ring-1 ring-red-200 dark:ring-red-500/30` so failing agents
stand out in the list.

**AGT-3 — Collapsible skill list.** At the bottom of each card, separated by
`mt-4 border-t pt-3`, a full-width toggle `<button>` with
`aria-expanded="false"` and `aria-controls="skills-<agentId>"`: text
`Skills (<n>)` on the left, `chevron-down` icon on the right. Below it, the
panel `<div id="skills-<agentId>">`:
- **Collapsed (default on load):** `grid grid-rows-[0fr] opacity-0
  transition-all duration-300 ease-in-out motion-reduce:transition-none`,
  plus the `inert` attribute so the hidden chips are not read by screen readers.
- **Expanded:** `grid-rows-[1fr] opacity-100` in place of `grid-rows-[0fr]
  opacity-0`, and no `inert`.
- The panel's only child is `<div class="overflow-hidden">` containing a
  `<ul class="flex flex-wrap gap-2 pt-3">` of skill chips (4.3), one per skill
  on the agent, in catalog order.
Clicking the toggle swaps those classes, flips `aria-expanded`, and rotates the
chevron (`transition-transform duration-300 motion-reduce:transition-none`, `rotate-180` when expanded).
Clicking again collapses it with the same 300ms transition. Each card toggles
independently; several can be open. Open/closed state is kept per agent id, so
re-rendering after a delete keeps other cards as they were. An agent with no
skills (possible after skill deletes) shows the muted text `No skills enabled.`
inside the panel.

**AGT-4 — Agent action dropdown.** `⋮` opens a menu with **Configure** (icon
`cog-6-tooth`) and **Delete** (icon `trash`, red text).

**AGT-5 — Configure modal.** "Configure" opens the modal titled `Configure
<Agent name>` with subtitle `Owner: <owner> · Status: <status>`. Body: a
`<label for="system-prompt">` reading **System prompt**, then
`<textarea id="system-prompt" rows="10">` prefilled with the agent's system
prompt (section 14.4), classes `mt-2 w-full rounded-lg border border-slate-300
bg-white p-3 font-mono text-sm text-slate-900 focus:border-indigo-500
focus:outline-none focus:ring-2 focus:ring-indigo-500/30 dark:border-slate-700
dark:bg-slate-950 dark:text-slate-100`. The textarea is editable. Under it,
muted `text-xs`: `Changes are kept in memory until the page is reloaded.`
Footer: **Cancel** (secondary; closes and discards edits) and **Save prompt**
(primary; writes the textarea value to the agent in the store, then closes).
Reopening Configure shows the saved text. The modal also closes via the ×
button and the backdrop, discarding unsaved edits.

**AGT-6 — Delete agent.** "Delete" opens the confirm-delete modal: title
`Delete agent?`, body `<Name> will be removed from Agent Management. Its
contracts and error history are kept.` Confirming removes the agent from the
store and re-renders everything: the card disappears, the count drops,
Dashboard cards 3 and 4 and their sub-lines recalculate, and every skill's
"agents enabled" count drops for each skill that agent had. Contracts and
Error Log rows for that agent stay unchanged.

## 9. Section 4: Skills

Heading **Skills**. Intro: `The catalog of capabilities that can be enabled on agents.`
Count: `<n> skills`.

**SKL-1 — "What is a skill?" explainer.** Above the catalog, a callout box
`rounded-xl border border-indigo-200 bg-indigo-50 p-5 dark:border-indigo-500/30
dark:bg-indigo-500/10` with the `light-bulb` icon (`text-indigo-600
dark:text-indigo-400`), the heading **What is a skill?** (`text-sm
font-semibold`), and this text (`text-sm`, `text-slate-700
dark:text-slate-300`):

> A skill is a packaged capability that can be enabled on an agent: the
> instructions, tools, and integrations it needs to do one kind of job, such as
> drafting emails or extracting data from documents. An agent can only do what
> its skills allow. Clients choose skills for each agent they rent, and each
> skill requires a minimum subscription tier.

**SKL-2 — Skill card grid.** `<ul class="grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-3">`,
one `<article>` card per skill in catalog order (S-01 to S-06). Card (surface,
border, `rounded-xl p-5 shadow-sm`): header row with a `size-10 rounded-lg`
indigo icon tile showing the skill's icon (14.3), the skill name (`text-base
font-semibold`) and its category (`text-xs` muted), and the `⋮` dropdown on
the right. Then the short description (`mt-3 text-sm` muted, at most 2 lines
with `line-clamp-2`). Footer row (`mt-4 flex items-center justify-between`):
left, the **agents-enabled indicator**; right, the minimum-tier badge (4.3)
with text `Starter+`, `Pro+` or `Enterprise` (a `lock-closed` icon `size-3.5`
precedes the text on Pro+ and Enterprise). No price is shown anywhere in this
section.

**SKL-3 — Agents-enabled indicator.** The count is rendered as
the `cpu-chip` icon (`size-4`), the number in `font-semibold`, and the text
`agents enabled` (or `agent enabled` when the number is 1), e.g. `4 agents
enabled`. The number is computed from the agents in the store (15.2), so it
drops when an agent is deleted. A skill with 0 agents shows `0 agents enabled`
in muted text.

**SKL-4 — Skill action dropdown.** `⋮` opens a menu with **View detail**
(icon `eye`) and **Delete** (icon `trash`, red text).

**SKL-5 — Skill detail modal.** "View detail" opens the modal titled with the
skill name, subtitle `<Category> skill`. Body: the long description (14.3) as
a paragraph, then a `<dl>`: Skill ID, Category, Minimum tier (badge, e.g.
`Pro`), Available on (comma-separated tiers at or above the minimum, e.g.
`Pro, Enterprise`), Agents enabled (the number). Then a block **Enabled on**
listing the names of the agents that have the skill as skill chips, or muted
`No agents.` The modal shows **no price and no contracts** (A6). Footer:
**Close**.

**SKL-6 — Delete skill.** "Delete" opens the confirm-delete modal: title
`Delete skill?`, body `<Name> will be removed from the catalog and from every
agent that has it. Past contracts keep their records.` Confirming removes the
skill from the store and from every agent's skill list, then re-renders: the
card disappears, the count drops, affected agent cards show one fewer skill
(`Skills (<n>)`), and the user detail modal's Skill access list no longer lists
it. Contract lines that name the skill are unchanged.

## 10. Section 5: Agent Contracts

Heading **Agent Contracts**. Intro: `Active and past rental contracts between clients and agents.`
Count: `<n> contracts · <a> active`.

**CON-1 — Contracts table.** Same table wrapper as USR-1. Rows in dataset
order (C-1001 to C-1007). Columns:

| Column | Content | Responsive |
| --- | --- | --- |
| Client | client company (`font-medium`) with the contract ID under it (`text-xs` muted, `font-mono`) | always |
| Agent | agent name | always |
| Skills | one skill chip per contract line, wrapping (`flex flex-wrap gap-1`) | `hidden lg:table-cell`; under `lg` the text `<n> skills` is shown under the agent name |
| Dates | start date, an en dash, end date: `Nov 1, 2026 – Apr 30, 2027`. Under `lg` the end date wraps to a second line | always |
| Status | badge `Active` (emerald) or `Past` (slate), from the stored status | always |
| Amount paid | total paid, right-aligned, `font-medium tabular-nums` | always |
| (actions) | `⋮` dropdown | always |

**CON-2 — Active vs past.** Past rows additionally use muted text
(`text-slate-500 dark:text-slate-400`) for every text cell; badges and skill chips keep their normal colors.
The dataset holds 5 Active and 2 Past contracts.

**CON-3 — Contract action dropdown.** `⋮` opens a menu with one item:
**View detail** (icon `eye`). There is no Delete for contracts (A7).

**CON-4 — Contract breakdown modal.** "View detail" opens the modal titled
`Contract <ID>`, subtitle `<Client> · <Agent>`, with a status badge next to the
title. Body:
1. A `<dl>` (two columns): Client, Agent, Start date, End date, Term (e.g.
   `6 months`), Billed on (the start date), Status (badge).
2. An itemized `<table>` headed **Contracted skills**, columns: Skill, List
   price, Sold price, Discount. One row per contract line. Discount shows
   `−$1,200.00 (10%)` in `text-amber-700 dark:text-amber-400`, or `—` in muted
   text when list = sold. Money columns are right-aligned, `tabular-nums`.
3. A totals block under the table (right-aligned rows): `Full price` = sum of
   list prices; `Discounts & coupons` = `−` sum of discounts (amber);
   `Total paid` = sum of sold prices, `text-base font-semibold`, with a
   `border-t` above it. Total paid always equals the Amount paid shown in the
   table row.
4. If the contract has a discount note (14.5), it is shown under the totals as
   muted `text-xs`: `Discount note: <note>`.
Footer: **Close**.

## 11. Section 6: Error Log

Heading **Error Log**. Intro: `Execution errors reported by agents, newest first.`
Count: `<n> errors · <u> unresolved`.

**ERR-1 — Error table.** Same table wrapper as USR-1. Rows in dataset order
(newest first, E-5001 to E-5008). Columns:

| Column | Content | Responsive |
| --- | --- | --- |
| Timestamp | `2026-11-19 22:47 UTC`, `font-mono text-xs`; under `lg` the date and the time + `UTC` sit on two lines | always |
| Agent | agent name, `font-medium` | always |
| Type | **error type badge**, text = the type (e.g. `Timeout`), colored by the entry's severity (4.3) | always |
| Severity | **severity badge**, text = severity (e.g. `Critical`), same color | `hidden lg:table-cell` |
| Description | the short description; if resolved, a `Resolved` slate badge after it | always (wraps) |
| (actions) | `⋮` dropdown | always |

**ERR-2 — Color coding.** Both badges use the severity colors: Critical red,
Error orange, Warning amber, Info blue (A8). The Type badge always has a `title`
attribute equal to the severity, which explains the color under `lg`, where
the Severity column is hidden. Above the table, a legend row shows the four
severity badges with their names so the color code is explained.

**ERR-3 — Error action dropdown.** `⋮` opens a menu with **View detail** (icon
`eye`) and **Mark as resolved** (icon `check-circle`). On a resolved entry the
second item reads **Resolved**, is a disabled `<button disabled>` with
`opacity-50 cursor-not-allowed`, and does nothing.

**ERR-4 — Error trace modal.** "View detail" opens the modal titled
`<Error ID> · <Type>`, with the severity badge next to the title and subtitle
`<Agent> · <Timestamp>`. Body: the short description (`text-sm`), a `<dl>` with
Error ID, Agent, Type (badge), Severity (badge), Timestamp, Status (plain text
`Open` or `Resolved`), then
a block headed **Full trace** containing the error's trace (14.6) in a
`<pre class="mt-2 max-h-72 overflow-auto rounded-lg bg-slate-950 p-4 font-mono
text-xs leading-relaxed text-slate-100">` (same classes in dark mode, plus
`dark:ring-1 dark:ring-slate-800`). Footer: **Close**, and, only if the entry
is open, a primary **Mark as resolved** button that resolves it (ERR-5) and
closes the modal.

**ERR-5 — Mark as resolved.** Sets `resolved: true` on the entry in the
store and re-renders: the row stays in its place and is darkened: the `<tr>` gets
`bg-slate-100 dark:bg-slate-950` and every text cell except the actions cell
switches to `text-slate-600 dark:text-slate-400` (no `opacity-*`, so the text
still meets AA contrast), the `Resolved` badge appears after the
description, the dropdown item becomes disabled **Resolved**, and the header
count's unresolved number drops by one. E-5008 starts resolved so the dimmed
state is visible on load. Resolving does not change any agent's status.

## 12. Component inventory

Reusable pieces. Build each once in JS (a function returning markup or wiring
behavior) and use it everywhere listed.

| # | Component | Purpose | Used in |
| --- | --- | --- | --- |
| 12.1 | Sidebar | Persistent navigation to the six sections | Shell |
| 12.2 | Top bar | Breadcrumb, theme toggle, admin identity | Shell |
| 12.3 | Metric card | One headline number | Dashboard |
| 12.4 | Action dropdown | `⋮` row menu | Users, Agents, Skills, Contracts, Errors |
| 12.5 | Modal | Overlay for details and forms | Users, Agents, Skills, Contracts, Errors |
| 12.6 | Confirm-delete modal | Safe delete confirmation | Users, Agents, Skills |
| 12.7 | Badge | Status, plan/tier, severity, type, skill chip | All sections |
| 12.8 | Data table | Tabular list with action column | Users, Contracts, Errors, contract modal |
| 12.9 | Collapsible skill list | Hide/show an agent's skills with a transition | Agents |
| 12.10 | Dark mode toggle | Switch the whole panel between light and dark | Top bar |
| 12.11 | Tier lock indicator | Greyed, locked feature naming the required tier | User modal, Skill cards |
| 12.12 | Empty state | Message when a list is empty | Users, Agents, Skills |

**12.1 Sidebar.** Anatomy and states in SHELL-2 and SHELL-3. States: link
default, hover, active; wide (`lg`, icon + label) and rail (`< lg`, icon only
with `title`). Light/dark per 4.1.

**12.2 Top bar.** Anatomy in SHELL-4. Sticky; light/dark per 4.1.

**12.3 Metric card.** Anatomy in DASH-2: label, icon tile, value, sub-line,
left accent border. Props: label, value, sub-line, icon, accent color. Static
(no hover or click); light/dark per 4.1 and the accent tile classes.

**12.4 Action dropdown.** Anatomy: a wrapper `<div class="relative inline-block text-left">`
holding the trigger and the menu.
- Trigger: `<button type="button" aria-haspopup="menu" aria-expanded="false" aria-label="Actions for <item name>">⋮</button>`,
  classes `inline-flex size-8 items-center justify-center rounded-lg text-lg
  leading-none text-slate-500 hover:bg-slate-100 hover:text-slate-900
  dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-slate-100`.
- Menu: `<div role="menu" class="absolute right-0 top-full z-30 mt-1 w-48 rounded-lg border bg-white py-1 shadow-lg dark:bg-slate-900 ... hidden">`.
  Items are `<button role="menuitem" class="flex w-full items-center gap-2 px-3 py-2 text-left text-sm hover:bg-slate-100 dark:hover:bg-slate-800">`
  with an icon (`size-4`) and label.
- States: closed (`hidden` on the menu, `aria-expanded="false"`), open (no
  `hidden`, `aria-expanded="true"`, trigger keeps `bg-slate-100
  dark:bg-slate-800`). Behavior in 13.1.

**12.5 Modal.** One shared modal root, a direct child of `<body>`:
`<div id="modal-root" class="fixed inset-0 z-50 hidden items-center justify-center p-4" role="dialog" aria-modal="true" aria-labelledby="modal-title">`.
Open state swaps `hidden` for `flex`. Children:
- Backdrop: `<div data-backdrop class="absolute inset-0 bg-slate-900/60 backdrop-blur-sm"></div>`.
- Panel: `<div class="relative flex max-h-[85vh] w-full max-w-lg flex-col rounded-2xl border bg-white shadow-xl dark:bg-slate-900 ...">`
  (`max-w-2xl` for the contract breakdown and error trace modals). Panel
  header (`flex items-start justify-between gap-4 border-b px-6 py-4`): title
  `<h3 id="modal-title" class="text-lg font-semibold">`, optional badge,
  subtitle (`text-sm` muted), and a close button `<button aria-label="Close">`
  with the `x-mark` icon. Body (`overflow-y-auto px-6 py-5 space-y-5`). Footer
  (`flex justify-end gap-3 border-t px-6 py-4`).
- Buttons: secondary `rounded-lg border px-4 py-2 text-sm font-medium
  hover:bg-slate-50 dark:hover:bg-slate-800` (+ border colors); primary
  `rounded-lg bg-indigo-600 px-4 py-2 text-sm font-medium text-white
  hover:bg-indigo-700`; danger per 4.1.
- States: closed / open; light/dark. Behavior in 13.2.

**12.6 Confirm-delete modal.** The modal (12.5) with: `exclamation-triangle`
icon in a `size-10 rounded-full bg-red-100 text-red-600 dark:bg-red-500/15
dark:text-red-400` circle, the title and body given per section, and footer
buttons **Cancel** (secondary) and **Delete** (danger). Cancel, ×, backdrop and
Escape close it without deleting. Delete performs 13.5 and closes it.

**12.7 Badge.** Pill with text and optional dot or icon; variants and colors in
4.3. Static. Light/dark per 4.3.

**12.8 Data table.** Wrapper and header styles in USR-1 and 4.1–4.2. Row
hover, `border-t` between rows, `px-4 py-3` cells, actions column `w-12
text-right`. The last row's first and last cells get `rounded-bl-xl` and
`rounded-br-xl` so hover color follows the wrapper's corners. If a column is
still too wide at 768px its text wraps (`break-words`); tables never scroll
horizontally. Contents are rendered from the store; empty state per 12.12.

**12.9 Collapsible skill list.** Toggle button + panel, classes and behavior in
AGT-3 and 13.3. States: collapsed (default) and expanded; the chevron rotates.

**12.10 Dark mode toggle.** `<button type="button" id="theme-toggle"
aria-pressed="false" aria-label="Switch to dark mode">` with `size-9 rounded-lg
border` (border colors), centered icon. In light mode it shows the `moon`
icon; in dark mode the `sun` icon, `aria-pressed="true"` and `aria-label="Switch
to light mode"`. Behavior in 13.4.

**12.11 Tier lock indicator.** A greyed (muted `text-slate-500 dark:text-slate-400`, no `opacity-*`)
row or element with the `lock-closed` icon and the text `Requires <Tier>`, and
a `title` of `Upgrade to <Tier> to unlock`. In the skill cards, the lock icon
inside the tier badge marks skills that need Pro or Enterprise.

**12.12 Empty state.** Centered muted text in `py-10`: `No users.`, `No
agents.`, `No skills.`

## 13. Interaction rules

### 13.1 Dropdowns

1. Clicking a `⋮` trigger opens its menu. Clicking the same trigger again
   closes it.
2. Only one menu is open at a time: opening a menu closes any other.
3. Clicking anywhere outside the open menu and its trigger closes it (one
   `click` listener on `document`; triggers call `event.stopPropagation()` or
   the listener checks `closest()`).
4. Pressing Escape closes the open menu and returns focus to its trigger.
5. Choosing a menu item closes the menu, then runs the action.
6. Navigating to another section, or opening a modal, closes any open menu.
7. Wire all behavior with one `click` listener on `document` that reads
   `data-action` (plus `data-id` where an item is targeted), so re-rendered rows
   and modal content work without re-binding. The complete list: `nav`,
   `toggle-theme`, `menu`, `view-user`, `delete-user`, `toggle-skills`,
   `configure-agent`, `save-prompt`, `delete-agent`, `view-skill`,
   `delete-skill`, `view-contract`, `view-error`, `resolve-error`,
   `confirm-delete`, `skip` (the skip link, 13.7), and `close-modal` (on ×, Close, Cancel and the backdrop).

### 13.2 Modals

1. A modal opens only from a menu item or a modal button. Opening one fills
   `#modal-root` with that modal's content and shows it.
2. It closes on: the × button, any **Close**/**Cancel** button, a click on the
   backdrop, and the Escape key. A click inside the panel never closes it.
3. While open, `<body>` has `overflow-hidden` (no background scroll). It is
   removed on close.
4. On open, focus moves to the modal's close button (to the textarea for
   Configure). On close, focus returns to the `⋮` trigger that opened it. If that
   trigger no longer exists (after a delete or a resolve re-renders), focus goes
   to the section's `<h2>`, which has `tabindex="-1"`.
5. Only one modal is shown at a time. The confirm-delete modal replaces the
   content of the shared root.

### 13.3 Collapsible skill list

1. Collapsed on page load for every agent.
2. Click toggles between collapsed and expanded with the 300ms row-height and
   opacity transition from AGT-3; the chevron rotates 180°.
3. `aria-expanded` always matches the visible state.

### 13.4 Dark mode

1. The `dark` class on `<html>` controls the theme (C4). Every element styled
   for light mode has matching `dark:` classes, including the sidebar, top bar,
   cards, tables, badges, dropdown menus, modals, textarea, and the chart
   placeholder.
2. Clicking the toggle adds or removes `dark` on `<html>`, swaps the toggle's
   icon, label and `aria-pressed`, and saves `light` or `dark` to
   `localStorage['agenthub-theme']` in `try/catch`.
3. A tiny inline script in `<head>`, before the Tailwind script, reads that key
   in `try/catch` and adds `dark` before first paint when it is `dark`.
   Otherwise the panel starts light. The OS color preference is ignored.
4. Because navigation never reloads the page and never touches `<html>`'s
   class, the chosen mode is preserved across all six sections, and in every
   modal and menu opened in them.

### 13.5 Delete (users, agents, skills)

1. Menu → **Delete** → confirm-delete modal (12.6). Nothing changes until the
   admin clicks **Delete** in it.
2. Confirming removes the record from the in-memory store (and, for a skill,
   removes its id from every agent's `skills`), closes the modal, and calls one
   `renderAll()` that re-renders every section, the section counts, and the
   Dashboard from the store.
3. Contracts and errors are history: they store names as text and are never
   changed by a delete.

### 13.6 Mark as resolved

Menu or modal → **Mark as resolved** sets `resolved: true` and re-renders the
Error Log (ERR-5). No confirmation. It cannot be undone in the prototype.

### 13.7 Accessibility

These rules come from the project's accessibility items (DoD W1–W9). They use
only markup, ARIA, JavaScript and Tailwind classes.

1. **Skip link.** The first focusable element on the page:
   `<a href="#main" data-action="skip" class="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[60] rounded-lg bg-white px-4 py-2 text-sm font-medium text-indigo-700 shadow-lg dark:bg-slate-900 dark:text-indigo-300">Skip to content</a>`.
   It is hidden until it gets focus. Activating it calls
   `event.preventDefault()` (so the hash and the visible section do not change)
   and moves focus to the visible section's `<h2>`.
2. **Keyboard.** Every control is a native `<a>` or `<button>` (or the
   textarea), so Tab, Shift+Tab, Enter and Space work without extra code.
   Focus order follows the DOM: skip link, sidebar, top bar, then the
   section. No positive `tabindex`; the only `tabindex` values are the `-1` on
   section `<h2>`s.
3. **Focus indicator.** Every interactive element keeps the focus ring from
   4.1 in both themes. `outline-none` appears only together with a `ring`
   (the textarea, 8).
4. **Names and states.** Controls with no visible text have an `aria-label`
   (`⋮`, ×, the theme toggle); sidebar links keep their label as `sr-only` text
   on tablet. The Configure textarea has a `<label>`. `aria-current`,
   `aria-expanded`, `aria-pressed`, `role="dialog"` and `aria-modal` follow
   12.4, 12.5, 12.10 and 13.1–13.4.
5. **Not by color alone.** Every status, plan and severity badge shows its
   name as text; the dots and colors only repeat it.
6. **Contrast.** All text meets WCAG 2.2 AA (4.5:1, or 3:1 for text 24px and
   larger) in light and dark, and focus rings meet 3:1. The muted pairs in 4.1
   (`text-slate-500` on white or `slate-50`, `dark:text-slate-400` on
   `slate-900` or `slate-950`) pass. Never use `text-slate-400` on a light
   surface, `dark:text-slate-500` on a dark one, or `opacity-*` on text. The
   only exception is a disabled `<button disabled>` (ERR-3), which WCAG
   exempts.
7. **Reduced motion.** Every class list with a `transition-*` also has
   `motion-reduce:transition-none`. Menus and modals appear without
   animation.
8. **Menus and modals** follow 13.1.4 and 13.2.4: Escape closes them, and focus
   moves into a modal and back to the control that opened it.

## 14. Hardcoded dataset

Define the store once, as `const store = { clients, users, skills, agents, contracts, errors }`
in the inline script. Every section renders from it. Field names below are the
property names to use. Dates are ISO strings `YYYY-MM-DD`; timestamps are
stored exactly as displayed.

### 14.1 Client companies

| id | name | tier |
| --- | --- | --- |
| northwind | Northwind Logistics | Enterprise |
| brightpath | Brightpath Health | Pro |
| cobalt | Cobalt Legal | Pro |
| lumen | Lumen Retail | Starter |

### 14.2 Users (`users`)

`plan` is the company's tier (A2). `lastActive` is `null` for `Never`.

| id | name | email | company | role | plan | status | joined | lastActive |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| U-101 | Maya Chen | maya.chen@northwind.example | Northwind Logistics | Operations Director | Enterprise | Active | 2025-02-03 | 2026-11-19 21:04 UTC |
| U-102 | Priya Nair | priya.nair@northwind.example | Northwind Logistics | Data Analyst | Enterprise | Invited | 2026-11-17 | null |
| U-103 | Daniel Okafor | daniel.okafor@brightpath.example | Brightpath Health | Patient Support Lead | Pro | Active | 2025-06-12 | 2026-11-19 18:30 UTC |
| U-104 | James Whitfield | james.whitfield@cobaltlegal.example | Cobalt Legal | Paralegal Manager | Pro | Suspended | 2025-09-08 | 2026-10-02 10:15 UTC |
| U-105 | Sofia Ramirez | sofia.ramirez@lumenretail.example | Lumen Retail | E-commerce Manager | Starter | Active | 2026-05-20 | 2026-11-19 16:48 UTC |
| U-106 | Tom Becker | tom.becker@lumenretail.example | Lumen Retail | Customer Service Rep | Starter | Active | 2026-07-01 | 2026-11-18 09:12 UTC |

### 14.3 Skills (`skills`)

`monthlyPrice` is data only (used to explain contract list prices); it is
never shown in the Skills section.

| id | name | category | icon | minTier | monthlyPrice | description (short, shown on card) |
| --- | --- | --- | --- | --- | --- | --- |
| S-01 | Email Drafting | Communication | `envelope` | Starter | 1200.00 | Writes and replies to business emails in the client's tone of voice. |
| S-02 | Scheduling | Communication | `calendar-days` | Starter | 900.00 | Books, moves, and confirms meetings through a connected calendar. |
| S-03 | Ticket Triage | Support | `inbox-stack` | Pro | 1800.00 | Reads incoming support tickets, tags them, and routes them to the right queue. |
| S-04 | Knowledge Base Q&A | Support | `book-open` | Pro | 2400.00 | Answers questions from the client's own help-center articles and documents. |
| S-05 | Document Summarization | Documents | `document-text` | Pro | 2000.00 | Turns long contracts, reports, and threads into short, structured summaries. |
| S-06 | Data Extraction | Documents | `table-cells` | Enterprise | 3500.00 | Pulls fields such as totals, dates, and parties out of invoices and forms. |

Long descriptions (`details`, shown in the skill detail modal):

- **S-01 Email Drafting:** Drafts new emails and replies from a short instruction or an incoming message. Matches the client's tone guide, adds the required signature and footer, and leaves every draft for a person to approve unless auto-send is enabled.
- **S-02 Scheduling:** Connects to the client's calendar to find free slots, send invitations, reschedule, and confirm attendance. Respects working hours and time zones, and never double-books a slot.
- **S-03 Ticket Triage:** Classifies each new support ticket by topic, urgency, and sentiment, applies tags, and routes it to the right queue in the client's helpdesk. Flags anything that looks like an outage or a legal risk for a human.
- **S-04 Knowledge Base Q&A:** Answers customer and employee questions using only the client's own knowledge base, with a link to the source article. Says so plainly when the answer is not in the knowledge base instead of guessing.
- **S-05 Document Summarization:** Summarizes long documents such as contracts, reports, and email threads into a headline, key points, and action items, within a target length. Keeps names, numbers, and dates exactly as written.
- **S-06 Data Extraction:** Extracts structured fields from invoices, purchase orders, and forms (PDF or image) into a table that other systems can import. Reports a confidence score per field and marks anything it could not read.

Agents enabled per skill (derived, 15.2; initial values): S-01 **4**, S-02
**3**, S-03 **3**, S-04 **3**, S-05 **2**, S-06 **2**.

### 14.4 Agents (`agents`)

`skills` lists skill ids in catalog order. `owner` follows A1.

| id | name | purpose | owner | status | skills | lastRun |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 | Atlas | Back-office assistant for operations | Northwind Logistics | active | S-01, S-02, S-05, S-06 | 2026-11-19 23:58 UTC |
| A-02 | Beacon | Patient support desk agent | Brightpath Health | failing | S-01, S-03, S-04 | 2026-11-19 22:47 UTC |
| A-03 | Cipher | Legal research and summaries | Cobalt Legal | active | S-04, S-05 | 2026-11-19 20:11 UTC |
| A-04 | Drift | General-purpose agent, unassigned | AgentHub | inactive | S-01, S-02, S-03 | 2026-08-31 17:00 UTC |
| A-05 | Echo | Storefront customer service agent | Lumen Retail | failing | S-01, S-02 | 2026-11-19 21:15 UTC |
| A-06 | Forge | Invoice and order processing | Northwind Logistics | active | S-03, S-04, S-06 | 2026-11-19 23:40 UTC |

System prompts (`systemPrompt`; paragraphs separated by one blank line, `\n\n`):

**A-01 Atlas**
```
You are Atlas, the back-office assistant for Northwind Logistics.

Help the operations team with email, scheduling, document summaries, and data extraction from shipping documents. Write in clear, concise, professional English. Never send an email or accept a meeting without approval from a Northwind employee. When you extract data from invoices or bills of lading, report any field you are less than 90% sure of.
```

**A-02 Beacon**
```
You are Beacon, the patient support agent for Brightpath Health.

Triage incoming support tickets, answer questions using only the Brightpath help center, and draft replies for the support team. Never give medical advice and never ask for or repeat medical record details. If a patient describes an emergency, tell them to call their local emergency number and escalate the ticket as Urgent.
```

**A-03 Cipher**
```
You are Cipher, the legal research assistant for Cobalt Legal.

Summarize case files, contracts, and correspondence, and answer questions from the firm's internal knowledge base. Quote clauses exactly and cite the document and page for every statement. You do not give legal advice; flag anything that needs a lawyer's judgment.
```

**A-04 Drift**
```
You are Drift, a general-purpose AgentHub agent that is not assigned to a client.

Until you are assigned, answer only internal AgentHub test requests. Draft emails, schedule meetings, and triage sample tickets when asked. Do not contact anyone outside AgentHub.
```

**A-05 Echo**
```
You are Echo, the customer service agent for Lumen Retail's online store.

Reply to customer emails about orders, returns, and delivery times, and book callback appointments with the service team. Be warm and brief. Every marketing email must include the unsubscribe footer. Never promise a refund; offer to pass the request to a team member.
```

**A-06 Forge**
```
You are Forge, the order and invoice processing agent for Northwind Logistics.

Extract line items, totals, dates, and parties from invoices and purchase orders, triage incoming order tickets, and answer questions from the Northwind operations handbook. Output extracted data as a table. If totals do not add up, stop and flag the document instead of guessing.
```

### 14.5 Contracts (`contracts`)

Each contract has `lines`: `{ skillId, skillName, listPrice, soldPrice }`.
`skillName` is stored so the contract survives skill deletes (13.5). `term`
is in months. Status follows A12. Sold prices sum to `totalPaid`.

| id | client | agent | start | end | term | status | totalPaid | discountNote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1001 | Northwind Logistics | Atlas | 2026-11-01 | 2027-04-30 | 6 | Active | 36900.00 | Launch promo: 10% off Pro and Enterprise skills |
| C-1002 | Brightpath Health | Beacon | 2026-11-10 | 2027-02-09 | 3 | Active | 10980.00 | Coupon HEALTH15 on Knowledge Base Q&A; 10% loyalty discount on Ticket Triage |
| C-1003 | Cobalt Legal | Cipher | 2026-01-01 | 2026-12-31 | 12 | Active | 47520.00 | Annual commitment: 10% off |
| C-1004 | Lumen Retail | Echo | 2026-11-15 | 2026-12-14 | 1 | Active | 1860.00 | Coupon WELCOME20 on Email Drafting |
| C-1005 | Northwind Logistics | Forge | 2026-08-01 | 2027-01-31 | 6 | Active | 45120.00 | 10% volume discount on Ticket Triage |
| C-1006 | Lumen Retail | Drift | 2026-06-01 | 2026-08-31 | 3 | Past | 5940.00 | Trial discount: 10% off Email Drafting |
| C-1007 | Cobalt Legal | Cipher | 2025-07-01 | 2025-12-31 | 6 | Past | 24960.00 | Coupon LEGAL10 on Knowledge Base Q&A |

Contract lines (list price = skill monthly price × term):

| contract | skill | listPrice | soldPrice | discount |
| --- | --- | --- | --- | --- |
| C-1001 | S-01 Email Drafting | 7200.00 | 7200.00 | — |
| C-1001 | S-05 Document Summarization | 12000.00 | 10800.00 | 1200.00 (10%) |
| C-1001 | S-06 Data Extraction | 21000.00 | 18900.00 | 2100.00 (10%) |
| C-1002 | S-03 Ticket Triage | 5400.00 | 4860.00 | 540.00 (10%) |
| C-1002 | S-04 Knowledge Base Q&A | 7200.00 | 6120.00 | 1080.00 (15%) |
| C-1003 | S-04 Knowledge Base Q&A | 28800.00 | 25920.00 | 2880.00 (10%) |
| C-1003 | S-05 Document Summarization | 24000.00 | 21600.00 | 2400.00 (10%) |
| C-1004 | S-01 Email Drafting | 1200.00 | 960.00 | 240.00 (20%) |
| C-1004 | S-02 Scheduling | 900.00 | 900.00 | — |
| C-1005 | S-03 Ticket Triage | 10800.00 | 9720.00 | 1080.00 (10%) |
| C-1005 | S-04 Knowledge Base Q&A | 14400.00 | 14400.00 | — |
| C-1005 | S-06 Data Extraction | 21000.00 | 21000.00 | — |
| C-1006 | S-01 Email Drafting | 3600.00 | 3240.00 | 360.00 (10%) |
| C-1006 | S-02 Scheduling | 2700.00 | 2700.00 | — |
| C-1007 | S-04 Knowledge Base Q&A | 14400.00 | 12960.00 | 1440.00 (10%) |
| C-1007 | S-05 Document Summarization | 12000.00 | 12000.00 | — |

Per-contract totals (full price / discounts / total paid): C-1001
$40,200.00 / $3,300.00 / $36,900.00 · C-1002 $12,600.00 / $1,620.00 /
$10,980.00 · C-1003 $52,800.00 / $5,280.00 / $47,520.00 · C-1004 $2,100.00 /
$240.00 / $1,860.00 · C-1005 $46,200.00 / $1,080.00 / $45,120.00 · C-1006
$6,300.00 / $360.00 / $5,940.00 · C-1007 $26,400.00 / $1,440.00 / $24,960.00.

### 14.6 Errors (`errors`)

Newest first. `resolved` is `false` unless stated.

| id | timestamp | agent | type | severity | description | resolved |
| --- | --- | --- | --- | --- | --- | --- |
| E-5001 | 2026-11-19 22:47 UTC | Beacon | Timeout | Critical | Knowledge base lookup exceeded the 30s limit; ticket left unanswered. | false |
| E-5002 | 2026-11-19 21:15 UTC | Echo | Auth | Critical | Calendar OAuth token expired; all scheduling requests rejected. | false |
| E-5003 | 2026-11-19 18:02 UTC | Beacon | API failure | Error | Helpdesk API returned 502 Bad Gateway while updating ticket #48213. | false |
| E-5004 | 2026-11-19 14:32 UTC | Atlas | Rate limit | Warning | Email provider throttled outgoing drafts (HTTP 429); retried after 60s. | false |
| E-5005 | 2026-11-19 09:10 UTC | Echo | Invalid output | Error | Marketing email draft was missing the required unsubscribe footer. | false |
| E-5006 | 2026-11-18 16:45 UTC | Forge | Timeout | Warning | Invoice PDF extraction took 41s; completed on the second attempt. | false |
| E-5007 | 2026-11-18 11:20 UTC | Cipher | Invalid output | Info | Summary exceeded the 500-word target and was trimmed automatically. | false |
| E-5008 | 2026-11-17 08:05 UTC | Drift | API failure | Info | Health-check ping failed while the agent was idle; no client impact. | **true** |

Traces (`trace`, shown verbatim in the `<pre>`):

**E-5001**
```
TimeoutError: skill "knowledge-base-qa" exceeded 30000 ms
    at SkillRunner.invoke (runtime/skill-runner.ts:212:15)
    at Agent.handleTicket (agents/beacon/handler.ts:88:22)
    at TicketQueue.process (queues/ticket-queue.ts:141:9)
context:
    agent=A-02 Beacon  client=Brightpath Health
    ticket=#48219  kb_query="change appointment location"
    retries=2/2  elapsed_ms=30004
result: ticket returned to queue "support-urgent" unanswered
```

**E-5002**
```
AuthError: 401 Unauthorized - OAuth token expired (calendar.lumenretail)
    at CalendarClient.request (integrations/calendar/client.ts:77:13)
    at SchedulingSkill.findSlots (skills/scheduling/index.ts:54:28)
    at Agent.handleRequest (agents/echo/handler.ts:63:17)
context:
    agent=A-05 Echo  client=Lumen Retail
    token_expired_at=2026-11-19 21:00 UTC
    failed_requests=17 since 21:00 UTC
action required: client admin must reconnect the calendar integration
```

**E-5003**
```
ApiError: 502 Bad Gateway from helpdesk.brightpath PUT /tickets/48213
    at HttpClient.send (runtime/http.ts:131:11)
    at HelpdeskClient.updateTicket (integrations/helpdesk/client.ts:96:20)
    at TicketTriageSkill.applyTags (skills/ticket-triage/index.ts:118:14)
context:
    agent=A-02 Beacon  client=Brightpath Health
    request_id=req_7f3a91c2  attempts=3
    response_body="<html>502 Bad Gateway</html>"
result: tags not applied; ticket left in "unsorted"
```

**E-5004**
```
RateLimitError: 429 Too Many Requests (mail.northwind)
    at MailClient.createDraft (integrations/mail/client.ts:58:19)
    at EmailDraftingSkill.draft (skills/email-drafting/index.ts:72:25)
    at Agent.runTask (agents/atlas/handler.ts:45:12)
context:
    agent=A-01 Atlas  client=Northwind Logistics
    retry_after_s=60  drafts_in_batch=48
result: batch resumed at 14:33 UTC and completed
```

**E-5005**
```
ValidationError: output failed policy "marketing-email-footer"
    at OutputValidator.check (runtime/validator.ts:39:11)
    at EmailDraftingSkill.finalize (skills/email-drafting/index.ts:131:18)
    at Agent.handleRequest (agents/echo/handler.ts:63:17)
context:
    agent=A-05 Echo  client=Lumen Retail
    campaign="Winter Sale"  draft_id=dr_20261119_0042
    missing_section="unsubscribe footer"
result: draft blocked from sending; held for review
```

**E-5006**
```
TimeoutWarning: skill "data-extraction" took 41200 ms (soft limit 30000 ms)
    at SkillRunner.invoke (runtime/skill-runner.ts:212:15)
    at Agent.processDocument (agents/forge/handler.ts:102:20)
context:
    agent=A-06 Forge  client=Northwind Logistics
    document=INV-2026-11-3391.pdf  pages=14
    attempt=1 timed out, attempt=2 succeeded in 18900 ms
result: extraction completed; no data lost
```

**E-5007**
```
OutputNotice: summary length 612 words exceeds target 500
    at OutputValidator.check (runtime/validator.ts:39:11)
    at SummarizationSkill.finalize (skills/document-summarization/index.ts:88:16)
context:
    agent=A-03 Cipher  client=Cobalt Legal
    document="Master Services Agreement - Halden Corp.pdf"
result: summary trimmed to 498 words; key points preserved
```

**E-5008**
```
ApiError: health check GET /status returned 503 (agent idle)
    at HealthMonitor.ping (runtime/health.ts:24:9)
context:
    agent=A-04 Drift  client=none (AgentHub)
    consecutive_failures=1
result: next ping succeeded at 08:06 UTC; no client impact
```

### 14.7 Consistency (already true of the data above; keep it true)

1. Every agent named in Contracts and the Error Log exists in Agent Management.
2. Every skill on an agent or contract line exists in the Skills catalog.
3. Each skill's "agents enabled" count is the number of agents listing it.
4. Each contract's sold prices sum to its `totalPaid`; every sold price is at
   or below its list price; list price = monthly price × term.
5. Each contract's skills are a subset of the rented agent's skills, and are
   allowed on the client's tier.
6. Every active contract's agent is owned by that contract's client; the idle
   agent (Drift) is owned by AgentHub and has only a past contract.
7. Both failing agents (Beacon, Echo) have Critical errors in the last day.
8. Each user's plan equals their company's tier. Starter users (Sofia Ramirez,
   Tom Becker) see four locked skills; Pro users see Data Extraction locked;
   Enterprise users see none locked.

## 15. Derived values and formatting

### 15.1 Dashboard

- `today = "2026-11-20"`, `currentMonth = "2026-11"` (A10).
- **Revenue this month** = sum of `totalPaid` over contracts whose `start`
  begins with `currentMonth` → C-1001 + C-1002 + C-1004 = **$49,740.00**.
  Sub-line: `<count> contracts billed in November 2026` (count = 3).
- **Discount & coupon losses** = for the same contracts, sum of (listPrice −
  soldPrice) over all lines → $3,300.00 + $1,620.00 + $240.00 =
  **$5,160.00**. Sub-line: `Full price <sum of list> − sold <sum of sold>` →
  `Full price $54,900.00 − sold $49,740.00`.
- **Active agents** = agents with `status === "active"` → **3**. Sub-line:
  `of <total agents> agents on the platform`.
- **Failing agents** = agents with `status === "failing"` → **2**. Sub-line
  fixed: `Flagged as failing right now`.
- Example: after deleting Atlas, card 3 shows `2` and `of 5 agents on the platform`; S-01, S-02, S-05, S-06 each drop by one.

### 15.2 Skill counts

`agentsEnabled(skillId)` = number of agents in the store whose `skills`
includes `skillId`. Never stored; always computed at render.

### 15.3 Formatting

- Money: `new Intl.NumberFormat("en-US", { style: "currency", currency: "USD" })` → `$12,400.00`. Discounts are shown as `−$1,200.00 (10%)`, with `−` (U+2212) and the whole-number percentage `round(discount / listPrice × 100)`.
- Dates: `new Date(iso + "T00:00:00Z").toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric", timeZone: "UTC" })` → `Nov 19, 2026`.
- Date ranges: `<start> – <end>` with an en dash (U+2013) and spaces.
- Timestamps: shown exactly as stored, `2026-11-19 14:32 UTC`.
- Term: `1 month` or `<n> months`.
- Initials: first letter of the first and last word of the name.
- Insert all dataset text as text (escape `<`, `>`, `&`, `"` when building
  markup strings) so trace text like `<html>` renders literally.

## 16. Acceptance criteria

The prototype is complete when every item below is true. Check at 1280px and
768px wide unless an item says otherwise.

**Repository and constraints**

1. `SPECS.md` exists at the repository root and was committed, alone, before
   any `.html` file was ever committed (check with `git log`).
2. The prototype is one `index.html` at the repository root.
3. Tailwind is loaded only from `https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4.3.5`.
4. The only CSS is the single `<style type="text/tailwindcss">` block holding
   the one `@custom-variant dark` line; there is no `.css` file and no
   `<link rel="stylesheet">`.
5. `grep -n 'style=' index.html` and `grep -n '\.style' index.html` find
   nothing.
6. No framework, library, jQuery, `package.json`, or build step is used; all
   behavior is vanilla JavaScript in `index.html`.
7. The page makes no network requests other than the Tailwind CDN script (no
   `fetch`/XHR in the code).
8. The markup uses `aside`, `nav`, `header`, `main`, one `section` per panel
   section, `table`/`thead`/`tbody`/`th` for tables, and `button` for every
   non-link control.
9. At 1280px and at 768px every section is fully usable with no horizontal
   page scroll; at 768px the sidebar is an icon rail and tables fit.
10. No `alert`, `confirm`, or `prompt` dialog ever appears.

**Shell and navigation**

11. The sidebar is visible in every section and lists, in order, Dashboard,
    User Management, Agent Management, Skills, Agent Contracts, Error Log.
12. Clicking each link shows that section only, and its link alone has the
    active style and `aria-current="page"`; the breadcrumb shows its label.
13. Loading `index.html#errors` opens the Error Log; loading with no hash
    opens the Dashboard.

**Dashboard**

14. Four metric cards show, with an icon, a label and a value each: Total
    revenue (this month) `$49,740.00`, Discount & coupon losses `$5,160.00`,
    Active agents `3`, Failing agents `2`, each with its own accent color.
15. A full-width dashed placeholder labeled `Weekly activity chart` sits below
    the cards.
16. The Active and Failing values equal the number of `active` and `failing`
    agents shown in Agent Management.

**User Management**

17. The users table shows 6 rows with name, email (column at 1280px, under
    the name at 768px), plan badge and status badge.
18. Every row's `⋮` dropdown offers View detail and Delete.
19. View detail opens a modal with every field of that user (User ID, Company,
    Role, Plan, Status, Joined, Last active, Email).
20. In Sofia Ramirez's modal, Ticket Triage, Knowledge Base Q&A and Document
    Summarization are greyed out with a lock and `Requires Pro`, and Data
    Extraction with `Requires Enterprise`; in Maya Chen's modal nothing is
    locked.

**Agent Management**

21. Six agent cards show name, owner, status badge (`active`, `inactive` and
    `failing` all appear) and a `Skills (<n>)` toggle.
22. On load every skill list is collapsed (skills not visible).
23. Clicking a toggle expands that agent's skill list with a visible ~300ms
    height and fade transition and a rotating chevron; clicking again
    collapses it the same way; `aria-expanded` matches.
24. Every agent's `⋮` dropdown offers Configure and Delete.
25. Configure opens a modal with the agent's system prompt in an editable
    `<textarea>`; after editing and clicking Save prompt, reopening Configure
    shows the edited text; Cancel discards edits.

**Skills**

26. The Skills section shows the "What is a skill?" explainer above six skill
    cards, each with name, short description, minimum tier, and an "agents
    enabled" count.
27. The counts are 4, 3, 3, 3, 2, 2 for S-01 to S-06 and equal the number of
    agent cards listing each skill.
28. Every skill's `⋮` dropdown offers View detail and Delete; View detail opens
    a modal with the long description, tier info and the agents that have it,
    and with no price and no contract information.

**Agent Contracts**

29. The contracts table shows 7 rows with client, agent, skills, start–end
    dates, an Active or Past badge, and amount paid; 5 are Active and 2 Past.
30. Every row's `⋮` dropdown offers View detail only.
31. View detail opens a breakdown modal listing each contracted skill with its
    list price, sold price and discount, plus Full price, Discounts & coupons
    and Total paid; Total paid equals the row's amount paid (e.g. C-1001:
    $40,200.00 / −$3,300.00 / $36,900.00).

**Error Log**

32. The Error Log shows 8 entries with timestamp, agent name, a color-coded
    type badge and a short description; Critical is red, Error orange,
    Warning amber, Info blue, and a legend explains the colors.
33. Every entry's `⋮` dropdown offers View detail and Mark as resolved.
34. View detail opens a modal with the full trace in a monospace block.
35. Mark as resolved dims that row in place, adds a `Resolved` badge, keeps
    the row in the list, disables the menu item, and lowers the unresolved
    count; E-5008 is already dimmed on load.

**Dropdowns (all sections)**

36. Every row or card in Users, Agents, Skills, Contracts and Error Log has a
    `⋮` button; clicking it opens its menu and clicking it again closes it.
37. Clicking anywhere outside an open menu closes it; opening a second menu
    closes the first; Escape closes it; no menu is ever clipped by its
    container, including on the last row of a table.

**Modals (all sections)**

38. View detail opens a modal in at least four sections: Users, Skills,
    Contracts and Error Log (Agents opens Configure).
39. Every modal (detail, Configure, confirm-delete) closes via its × button,
    via its Close/Cancel button, via a click on the backdrop, and via Escape;
    a click inside the panel does not close it.
40. While a modal is open the page behind it does not scroll.

**Delete**

41. Delete on a user, agent or skill first asks for confirmation in an
    in-page modal; Cancel changes nothing.
42. Confirming removes the item from its list and count. Deleting Atlas makes
    the Dashboard show 2 active agents and lowers Email Drafting, Scheduling,
    Document Summarization and Data Extraction by one; Atlas still appears in
    Contracts (C-1001) and the Error Log (E-5004).
43. Deleting a skill removes it from every agent card's skill list and from
    the user modal's Skill access list; contract breakdowns still show it.

**Dark mode**

44. Clicking the top-bar toggle switches the entire panel (sidebar, top bar,
    every section, tables, badges, menus, modals, textarea, chart placeholder)
    between light and dark; no element stays light in dark mode or dark in light mode, except the three
    fixed elements listed under 4.1.
45. After switching to dark, visiting all six sections and opening a modal and
    a menu in each keeps dark mode; switching back to light behaves the same.
46. The toggle's icon and label reflect the current mode, and the chosen mode
    survives a page reload.

**Data and formatting**

47. The same agent names (Atlas, Beacon, Cipher, Drift, Echo, Forge) appear
    in Agent Management, Contracts and the Error Log, and every number in the
    panel matches section 14 and 15.
48. Money shows as `$12,400.00`, dates as `Nov 19, 2026`, timestamps as
    `2026-11-19 14:32 UTC`.

**Accessibility**

49. From page load, the first Tab shows the `Skip to content` link; Enter on
    it moves focus to the visible section's heading and does not change the
    section.
50. Every control in every section, menu and modal can be reached with Tab
    and used with Enter or Space, in the visual order, with a visible focus
    ring in light and dark.
51. Every `<svg>` has `aria-hidden="true"`; every `⋮`, × and the theme toggle
    has an `aria-label`; the page has exactly one `<h1>`; each `<section>` is
    labelled by its `<h2>`.
52. A collapsed skill list is `inert`; an expanded one is not.
53. With the OS set to reduce motion, the skill list and chevron change
    instantly.
54. No text uses `opacity-*`; resolved errors and locked skills are greyed
    with muted text colors instead.
55. An axe-core scan of every section, with a menu open and with a modal
    open, in light and in dark, reports no violations.
56. Escape closes any open menu or modal, and focus returns to the control
    that opened it (13.2.4).

## 17. Out of scope

Not built, because the brief does not ask for it and it is not evaluated: real
navigation between pages, form submission, live search, filtering or sorting,
pagination, creating or editing records (other than the system prompt),
authentication, persistence of data changes across reloads, toasts, a real
chart, and layouts below 768px beyond "does not break".
