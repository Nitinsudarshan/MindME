---
title: Note Structure and Templates
aliases: [Note Body Structure, Templates]
tags: [rules, template, structure]
type: resource
status: evergreen
created: 2026-08-17
updated: 2026-08-17
related: ["[[00 - Rules Index]]", "[[03 - Frontmatter and Metadata]]", "[[07 - Mermaid Diagram Standards]]"]
source: 
---

# Note Structure and Templates

Frontmatter (see [[03 - Frontmatter and Metadata]]) says what a note *is*; this note says what its *body* has to contain. Required sections differ by `type` — a template per type lives in `06-Templates/` and is linked below.

---

## 1. Required sections by `type`

| `type` | Required body sections |
|---|---|
| `moc` | Purpose (one paragraph) → linked cluster (grouped list/table) → a structure diagram (see [[07 - Mermaid Diagram Standards]]) |
| `project` | Goal/outcome → current status → key decisions → open questions → links to related Area/Resource notes |
| `area` | Scope (what's in/out of this responsibility) → current state → links to active Project notes under it |
| `resource` | Summary (2–3 sentences) → body → **My Take** → Related |
| `fleeting` | Just the raw capture — no required structure. It exists to be processed into one of the other types during the weekly Inbox review, not to be polished in place |
| `daily` | What happened → notes touched today (links) → open loops for tomorrow |

## 2. The "My Take" section

Every `resource` note ends with **My Take**: the idea restated in your own words, not the source's. This is the actual second-brain mechanism — it's what lets you rebuild the reasoning later instead of re-reading someone else's summary and hoping it still makes sense. A resource note without a My Take section is functionally a bookmark, not a second-brain note.

## 3. Templates

Plain-markdown templates live in `06-Templates/`, written in Templater syntax (see [[09 - Plugin Stack]]) so they work as-is once Templater is configured, and are still readable as copy-paste starting points if it isn't:

- `06-Templates/Template - MOC.md`
- `06-Templates/Template - Project.md`
- `06-Templates/Template - Area.md`
- `06-Templates/Template - Resource.md`
- `06-Templates/Template - Fleeting.md`
- `06-Templates/Template - Daily.md`

`06-Templates/` is exempt from the frontmatter schema check (see [[03 - Frontmatter and Metadata]] §5) since these files contain placeholder syntax, not real values.

## 4. Length and atomicity

One idea per note (see [[02 - File Naming]]). A note that's grown three unrelated sections under one title should be split — link the pieces instead of nesting them under one header, so each is independently linkable and shows up as its own graph node.
