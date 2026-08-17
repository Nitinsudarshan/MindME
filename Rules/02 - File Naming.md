---
title: File Naming
aliases: [Naming Convention]
tags: [rules, naming, structure]
type: resource
status: evergreen
created: 2026-08-17
updated: 2026-08-17
related: ["[[00 - Rules Index]]", "[[01 - Folder Structure]]", "[[03 - Frontmatter and Metadata]]"]
source: 
---

# File Naming

The filename **is** the note title **is** the link text everywhere it's referenced. There is no separate "display title" to hide behind a bad filename — get it right once.

---

## 1. Rules

- **Descriptive, atomic titles.** One idea per file — this is what keeps graph view meaningful instead of a hairball.
  - Good: `Zettelkasten Method.md`, `Mnemos — Dev Startup Steps.md`
  - Bad: `notes3.md`, `Untitled.md`, `New note.md`, `misc.md`
- **No placeholder titles ever get committed.** If a note is still unnamed, it belongs in `00-Inbox/`, not committed under a placeholder name.
- **No dates in filenames**, except daily/log notes, which use `YYYY-MM-DD.md`.
- **Title Case for multi-word titles** (`Repo Research Kickoff Prompt`), not `snake_case` or `kebab-case` — filenames are prose here, not code identifiers.
- **Cross-platform-safe characters only** — this vault syncs across machines (the Mnemos dev notes reference a Windows box). Avoid `: * ? " < > | \` entirely, and never end a filename in a space or period. An em dash (`—`) is fine and already used in this vault (`Mnemos — Dev Startup Steps.md`).

## 2. The one sanctioned exception: numbered sequences

Files under `Rules/` use a `NN - Title.md` numeric prefix (`01 - Folder Structure.md`) purely to keep an intentional reading order in the file explorer. This is only for a deliberately ordered reference series like the rule set itself — **not** for ordinary atomic notes, which should never need a number to make sense.

## 3. Good vs. bad, side by side

| Good | Bad | Why |
|---|---|---|
| `Zettelkasten Method.md` | `notes3.md` | Descriptive vs. meaningless |
| `Mnemos — Dev Startup Steps.md` | `mnemos_dev_startup_steps_FINAL_v2.md` | No version cruft in the name — that's what `updated:` frontmatter and git history are for |
| `2026-08-17.md` (daily note) | `Aug 17.md` | Consistent, sortable date format |
| `Repo Research Kickoff Prompt (Template).md` | `template.md` | Specific enough to be unambiguous in a flat link list |

## 4. Renaming existing notes

Obsidian's rename updates all `[[links]]` automatically — don't be precious about existing filenames if a better one becomes obvious later. Renaming is cheap; a vague title that never gets fixed is not.
