---
title: Frontmatter and Metadata
aliases: [YAML Frontmatter, Metadata Schema]
tags: [rules, metadata, frontmatter]
type: resource
status: evergreen
created: 2026-08-17
updated: 2026-08-17
related: ["[[00 - Rules Index]]", "[[04 - Tagging]]", "[[06 - Note Structure and Templates]]"]
source: 
---

# Frontmatter and Metadata

Frontmatter is what makes the vault **queryable** (via Dataview) rather than just readable one note at a time. It also carries the metadata that tags and body text shouldn't have to — note maturity, dates, aliases.

---

## 1. Required schema — every note, no exceptions except §5

```yaml
---
title: 
aliases: []
tags: []
type: moc | project | area | resource | daily | fleeting
status: seedling | growing | evergreen
created: 2026-08-17
updated: 2026-08-17
related: []
source: 
---
```

| Field | Purpose |
|---|---|
| `title` | Usually matches the filename; exists as a field so Dataview can query on it independent of the file path |
| `aliases` | Alternate phrasings that should resolve to this note — prevents duplicate/orphan notes from someone linking under different wording |
| `tags` | Cross-cutting domain/category labels — see [[04 - Tagging]] for the taxonomy and the 1–7 tag limit |
| `type` | Structural role, independent of topic — filterable via Dataview regardless of what the note is *about* |
| `status` | Andy Matuschak-style note maturity: raw vs. refined, so rereading later shows what's trustworthy vs. half-baked |
| `created` / `updated` | `YYYY-MM-DD`, both required, updated on every substantive edit |
| `related` | Manual cross-links beyond what's in the body — deliberately improves graph density |
| `source` | URL or reference this note derives from, if any; blank is fine, the key must still exist |

## 2. `type` values

| Value | Meaning |
|---|---|
| `moc` | Map of Content — a hub note that links out to a cluster |
| `project` | Time-bound outcome with an end state (e.g. a Mnemos milestone) |
| `area` | Ongoing responsibility with no end date (e.g. PKM research as a standing interest) |
| `resource` | Reference material, templates, rule docs — this note's own type |
| `daily` | Daily/journal note |
| `fleeting` | Raw, unprocessed capture — the frontmatter equivalent of `00-Inbox/` |

## 3. `status` values

`seedling` → `growing` → `evergreen`, promoted during review (see [[08 - Review and Maintenance Cadence]]). A `fleeting` note is almost always `seedling`; a well-linked `resource` or `moc` note earns `evergreen` once it's been revisited and holds up.

## 4. Filled example

```yaml
---
title: Mnemos — Dev Startup Steps
aliases: [Mnemos Dev Setup]
tags: [mnemos, dev, runbook]
type: resource
status: evergreen
created: 2026-08-17
updated: 2026-08-17
related: ["[[App Scope]]"]
source: 
---
```

## 5. Exemptions

Notes produced by the web-clipper plugin (`Clippings/`) keep the clipper's own frontmatter shape (`title, source, author, published, created, description, tags`) rather than this schema — that format is generated automatically and isn't worth fighting. `06-Templates/` is also exempt, since template files intentionally contain placeholder syntax instead of valid values.

A third case: folders holding **operational configuration copied verbatim from another repository**, meant to be reused as-is rather than read as vault knowledge — e.g. `Active Projects/.agents/` and `Active Projects/Rules/` (copied from an external project's agent/rule config). These stay in the source project's own format; rewriting them into this vault's schema would break their ability to be dropped back into a real codebase unchanged. A note *describing* such a copied folder (see `Active Projects/Starter Template/Starter Template.md` for the pattern) still follows the full schema — the exemption covers the copied source files themselves, not notes written about them.

All exempted folders are excluded from the automated lint described in [[10 - Agent and AI Assistant Protocol]] — see `scripts/lint_vault.py`'s `EXEMPT_PREFIXES` for the exact list.

## 6. Validation

`scripts/lint_vault.py` checks every field in §1 is present, `type`/`status` are one of the allowed values, dates match `YYYY-MM-DD`, and `tags` stays within the 1–7 range from [[04 - Tagging]]. See [[10 - Agent and AI Assistant Protocol]] for how this is wired into commits and CI.
