#rules #obsidian #pkm #second-brain #structure #reference

Standard rule set for structuring an Obsidian vault so graph view stays meaningful and the vault works as an actual second brain (rederivable reasoning, not just stored facts) — not tied to any single project, applies as a baseline for MindME/Mnemos work and general PKM.

---

## 1. Folder Structure — Keep It Flat, Use PARA

Graph view rewards **links over folder nesting**. Folders separate by *function*, not topic — topics live in tags/links.

```
00-Inbox/          # unsorted capture, processed weekly
01-Projects/        # active, time-bound outcomes
02-Areas/           # ongoing responsibilities (no end date)
03-Resources/       # reference material, topic notes
04-Archive/         # completed/inactive
05-MOCs/            # Maps of Content (index/hub notes)
06-Templates/       # note templates
07-Daily/           # daily notes (journal)
Attachments/         # images, PDFs — keep out of the way
```

Rule: **max 2 folder levels deep.** Nesting deeper is a signal the content should be a tag or a link instead.

---

## 2. File Naming

- Descriptive, atomic titles — the filename IS the note title IS the link text.
  - Good: `Zettelkasten Method.md`
  - Bad: `notes3.md`, `untitled 2.md`
- No dates in filenames unless it's a daily/log note (`2026-08-18.md`).
- One idea per file (atomicity) — this is what makes graph view meaningful instead of a hairball.

---

## 3. YAML Frontmatter (required on every note)

```yaml
---
title: 
aliases: []
tags: []
type: moc | project | area | resource | daily | fleeting
status: seedling | growing | evergreen
created: 2026-08-18
updated: 2026-08-18
related: []
source: 
---
```

|Field|Purpose|
|---|---|
|**type**|Filter/query notes structurally (via Dataview) independent of topic tags|
|**status**|Andy Matuschak-style note maturity — tracks raw vs refined ideas, so rederiving later shows what's trustworthy vs half-baked|
|**aliases**|Lets other notes link under different phrasing without spawning duplicate/orphan nodes|
|**related**|Manual cross-links beyond body text — deliberately improves graph density|

---

## 4. Tagging Rules

Tags ≠ folders. Tags answer "what kind of thing / what domain"; folders answer "where does this live in my workflow."

- Flat, controlled vocabulary — maintain a running list in `05-MOCs/Tag Index.md` so `#llm`, `#LLMs`, `#large-language-models` don't fragment into three tags.
- Nested tags for hierarchy are fine: `#tool/pkm`, `#tool/dev`, `#status/wip`.
- 3–7 tags per note max — beyond that, tags stop being useful filters.
- Reserve tags for **cross-cutting categories** (domain, status, type). Use `[[links]]` for **specific relationships** between ideas — links build the graph, tags don't.

---

## 5. Linking Discipline

- Every note should have **at least 2–3 outgoing links** to existing notes. An unlinked note is a dead node.
- Link liberally even to notes that don't exist yet — unresolved links become a natural to-do list of ideas to flesh out.
- Avoid over-linking common words — link only where the connection is *meaningful*, or graph view becomes noise.
- Use **MOCs (Maps of Content)** as hub notes — one per major domain (e.g., `MOC - PKM Tools.md`) linking out to all related atomic notes. MOCs become the graph's visual anchors/clusters.

---

## 6. Graph View Hygiene

- Tag colors by group in graph settings — visually separates domains at a glance.
- Filter `06-Templates/` and `Attachments/` out of graph view (`-path:Templates -path:Attachments`).
- Use **local graph** (per-note) daily — global graph is for occasional structural audits, not navigation.
- Orphan notes (no links in/out) trigger a weekly review — either link them or archive them.

---

## 7. Rederiving Information (the actual second-brain function)

- Every resource note ends with a **"My Take" section** — restate the idea in your own words. This is what lets you rederive reasoning later instead of just re-reading facts.
- Daily notes link back to the atomic notes they touched — builds a timeline of when/why an idea resurfaced.
- Use Dataview queries to auto-generate lists like "all evergreen notes tagged #llm" — turns the vault into a queryable database, not just a wiki.
- Review cadence: weekly pass over `00-Inbox`, monthly pass promoting `seedling → growing → evergreen`.

---

## 8. Minimal Plugin Stack

- **Dataview** — query notes by frontmatter (type, status, tags)
- **Templater** — enforce the frontmatter template automatically on new notes
- **Tag Wrangler** — merge/rename tags without breaking links
- **Excalidraw / Canvas** (built-in) — visual MOC diagramming beyond graph view
