---
title: Plugin Stack
aliases: [Obsidian Plugins]
tags: [rules, obsidian, tooling]
type: resource
status: evergreen
created: 2026-08-17
updated: 2026-08-17
related: ["[[00 - Rules Index]]", "[[06 - Note Structure and Templates]]", "[[10 - Agent and AI Assistant Protocol]]"]
source: 
---

# Plugin Stack

The rules in this folder assume a minimal, specific plugin set — enough to make them low-effort to follow, not a plugin-collecting habit.

---

## 1. Core stack

| Plugin | Job |
|---|---|
| **Dataview** | Query notes by frontmatter (`type`, `status`, `tags`) — turns [[08 - Review and Maintenance Cadence]] from manual scanning into a query |
| **Templater** | Auto-fills the frontmatter template from [[03 - Frontmatter and Metadata]] and the body structure from [[06 - Note Structure and Templates]] on note creation |
| **Tag Wrangler** | Merges/renames tags without breaking links — the actual tool behind the monthly tag audit in [[08 - Review and Maintenance Cadence]] |
| **Excalidraw / Canvas** (built-in) | Freeform visual MOC diagramming beyond what Mermaid's fixed layouts can do — use for spatial/whiteboard thinking, Mermaid (see [[07 - Mermaid Diagram Standards]]) for structured diagrams that live inside a note |

## 2. Why this vault is also a git repo

Unlike most Obsidian vaults, this one's source of truth is a GitHub repository — which is what makes mechanical rule enforcement possible at all (see [[10 - Agent and AI Assistant Protocol]]). That has one practical consequence: **Obsidian Sync is not needed here.** Git already is the sync/versioning layer. If a plugin for editing-on-mobile-while-offline is ever needed, prefer something that commits to the same repo (Obsidian Git) over a second, separate sync mechanism — two sources of truth is exactly the failure mode the rest of this rule set exists to avoid.

## 3. Deliberately not adopted

- Any AI-chat-in-Obsidian plugin that phones out to a cloud model by default — this vault backs the Mnemos project, whose entire premise (see `Mnemos/App Scope.md`) is local-first AI. Bringing in a cloud-dependent plugin here would be a quiet contradiction of that.
- Anything that stores its own state outside plain Markdown + YAML (proprietary databases, closed sync formats) — for the same portability reasons the [[00 - Rules Index]] lifecycle diagram assumes plain files all the way through.
