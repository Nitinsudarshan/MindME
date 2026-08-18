---
title: Logseq - Brief
aliases: [Logseq]
tags: [tools, research, pkm]
type: moc
status: growing
created: 2026-08-18
updated: 2026-08-18
related: ["[[Tools]]", "[[Second Brain - PKM Tools Survey (Aug 2026)]]", "[[PKM Editors - Comparison]]"]
source: https://github.com/logseq/logseq
---

# Logseq

## Summary

A block-outliner PKM tool (Roam-style), mid-transition from a genuinely local-first, plain-Markdown file format to a new SQLite-backed "DB version" with real-time collaboration — a breaking architectural change that trades away its own portability story. Facts below carry over from live research done Aug 15, 2026 ([[Second Brain - PKM Tools Survey (Aug 2026)]]); not re-verified by a fresh crawl given the 3-day gap.

## Metadata

| Field | Value |
|---|---|
| Repo | [github.com/logseq/logseq](https://github.com/logseq/logseq) |
| License | AGPL-3.0 |
| Stars/Forks | ~44.5k / ~2.8k |
| Latest release | 2.0.1 "DB beta" (Jul 13, 2026); file-based stable frozen at 0.10.15 (Dec 2025) |
| Maintainer | Logseq Inc. (NYC) — $4.1M seed 2022 (a16z, Craft, Day One), no confirmed later round; small team (~5, unverified precisely) |
| Open issues | ~898, some long-open with no maintainer response |

## Features

Block outliner, backlinks, graph view, Datalog query system, whiteboards, spaced-repetition flashcards, PDF/Zotero integration, ~486 community plugins, community-built `mcp-logseq` MCP server plus `ollama-logseq`/AssistSeq local-LLM plugins (no first-party AI yet), paid Sync ($5/mo) or self-hosted Git/Syncthing (file version only).

## Architecture

Clojure/ClojureScript + React + Electron. The stable file-based product is genuinely local-first (plain Markdown/Org files as truth, loaded into an in-memory DataScript graph). Mid-transition to a new SQLite-backed "DB version" (2.0, beta) with real-time collaboration — official docs warn of data-loss risk during migration.

## Strengths and risks

**Strengths**: mature outliner/query/plugin stack with existing Ollama/MCP community tooling; genuinely local-first file version; large active community despite a small core team.
**Risks**: small VC-backed team with stale public funding data — sustainability unclear; the DB-version rewrite undercuts the plain-text promise and is still beta; Clojure codebase raises the bar for contribution or forking.

## Verdict

**Evaluate further** — adopt only the file-based (OG) version deliberately; treat the DB rewrite as a separate, riskier product line to watch, not build on yet.

## My Take

Logseq's own MCP/Ollama tooling exists only as community plugins, not first-party — a real gap against [[Anytype]]'s official `anytype-mcp` server. Worth revisiting if the DB-version rewrite stabilizes past beta, since that's the one thing standing between Logseq and a stronger position in [[PKM Editors - Comparison]].

## Related

- [[Tools]]
- [[Second Brain - PKM Tools Survey (Aug 2026)]]
- [[PKM Editors - Comparison]]
