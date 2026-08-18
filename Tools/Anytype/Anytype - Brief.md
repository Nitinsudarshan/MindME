---
title: Anytype - Brief
aliases: [Anytype]
tags: [tools, research, pkm]
type: moc
status: growing
created: 2026-08-18
updated: 2026-08-18
related: ["[[Tools]]", "[[Second Brain - PKM Tools Survey (Aug 2026)]]", "[[PKM Editors - Comparison]]"]
source: https://github.com/anyproto/anytype-ts
---

# Anytype

## Summary

An "everything is an object" PKM tool with genuinely offline-capable P2P sync and real, usable MCP integration today — but its core data format is proprietary, and its license is not OSI-approved open source. Facts below carry over from live research done Aug 15, 2026 ([[Second Brain - PKM Tools Survey (Aug 2026)]]); not re-verified by a fresh crawl given the 3-day gap.

## Metadata

| Field | Value |
|---|---|
| Repos | [anytype-ts](https://github.com/anyproto/anytype-ts), `anytype-heart`, `any-sync` |
| License | Client + middleware: **"Any Source Available License 1.0"** — source-visible, **not OSI open source**. Only the `any-sync` network protocol is MIT |
| Stars/Forks | anytype-ts ~8.6k★/571; anytype-heart ~414★/117 |
| Activity | ~6 releases/year, all three repos actively committed |
| Maintainer | Anytype (Germany) — Series A $13.4M (2023, Balderton); team-size figures conflict across sources (unverified) |

## Features

"Everything is an object" model (notes/tasks/people/DBs as linked, typed objects), relations + graph view, database-style collection views, a **real local API + official `anytype-mcp` server** (genuine MCP support today), P2P local-first sync with no mandatory cloud round-trip, shared workspaces, desktop + mobile.

## Architecture

Go middleware (`anytype-heart`) embedded in Electron/Swift/Kotlin clients; objects are stored as a **Protocol-Buffers-encoded CRDT tree** — not plain text, not inspectable without Anytype's own code. Self-hosting the sync network is technically possible via a community `any-sync-bundle`, but Anytype's own hosted network is the primary supported path.

## Strengths and risks

**Strengths**: rich structured-object/relations model beyond flat notes; genuinely offline-capable P2P sync; MCP integration is real and usable now — rare among tools surveyed.
**Risks**: the core data format is proprietary and only exportable via lossy/community tooling; the non-OSI license on the client/core limits real forkability; a documented history of update-triggered data loss during migrations.

## Verdict

**Reject** — the proprietary object format is structurally at odds with a "portable markdown, no DB lock-in" requirement, and the non-OSI license limits real forkability, despite the notably strong MCP story.

## My Take

The genuine tension here is that Anytype has the best MCP story of the three by a wide margin, but on the one axis that matters most for a vault like this (plain-Markdown portability, no lock-in), it's the clearest reject. That tension is exactly what [[PKM Editors - Comparison]] needs to make explicit rather than average away.

## Related

- [[Tools]]
- [[Second Brain - PKM Tools Survey (Aug 2026)]]
- [[PKM Editors - Comparison]]
