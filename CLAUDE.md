# MindME — Obsidian Vault

This repository is nitinsudarshan's personal Obsidian vault. Every `.md` file here is a real note, not source code — read before you edit, don't rewrite tone/voice, don't delete content to "clean up" unless asked.

## Before creating, editing, or committing any `.md` file

Read `Rules/00 - Rules Index.md` first, then whichever specific rule note under `Rules/` applies to the change. These rules exist so Obsidian's graph view stays meaningful and notes stay easy to re-read later — skipping them produces orphaned notes and a hairball graph.

Minimum bar before committing a note:

- Correct top-level folder, max 2 levels deep (`Rules/01 - Folder Structure.md`)
- Descriptive filename, no placeholder titles (`Rules/02 - File Naming.md`)
- Complete YAML frontmatter: `title, aliases, tags, type, status, created, updated, related, source` (`Rules/03 - Frontmatter and Metadata.md`)
- 1–7 tags drawn from `05-MOCs/Tag Index.md` (`Rules/04 - Tagging.md`)
- At least 2 outgoing `[[links]]` to existing notes (`Rules/05 - Linking and Graph Discipline.md`)
- Required body sections for that note's `type` (`Rules/06 - Note Structure and Templates.md`)
- A Mermaid diagram if the note is a MOC, or documents architecture/process/comparison (`Rules/07 - Mermaid Diagram Standards.md`)

`Clippings/` and `06-Templates/` are exempt from the frontmatter schema (web-clipper output and templates, respectively).

## Enforcement — don't rely on memory alone

`scripts/lint_vault.py` checks the above mechanically and is wired into:

- `.githooks/pre-commit` (run `bash scripts/setup-hooks.sh` once per clone to enable)
- `.github/workflows/vault-lint.yml` (runs on every push/PR regardless of local setup)

If a commit is about to fail lint, fix the note rather than bypassing the hook.

## Full rule set

See `Rules/00 - Rules Index.md` for the complete rule set, and `Rules/10 - Agent and AI Assistant Protocol.md` for the enforcement mechanics in detail.
