---
title: AFFiNE - Brief
aliases: [AFFiNE]
tags: [tools, research, pkm]
type: moc
status: growing
created: 2026-08-18
updated: 2026-08-18
related: ["[[Tools]]", "[[Second Brain - PKM Tools Survey (Aug 2026)]]", "[[PKM Editors - Comparison]]"]
source: https://github.com/toeverything/AFFiNE
---

# AFFiNE

## Summary

A unified doc-editor + infinite-canvas whiteboard, open-core with a genuinely local-first/offline editing core — but the self-hostable sync/collab server is proprietary EE-licensed, and its local-LLM story remains immature. Facts below carry over from live research done Aug 15, 2026 ([[Second Brain - PKM Tools Survey (Aug 2026)]]); not re-verified by a fresh crawl given the 3-day gap.

## Metadata

| Field | Value |
|---|---|
| Repo | [github.com/toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) |
| License | **Open-core**: everything except `packages/backend/server` is MIT; the sync/collab server is under a proprietary "AFFiNE Enterprise Edition" license |
| Stars/Forks | ~71.6k / ~5.1k |
| Activity | Near-daily canary builds; stable 0.27.3/0.27.4-beta (Aug 2026) |
| Maintainer | Toeverything Pte Ltd (Singapore) — $8M pre-Series A (2023, Redpoint/Sinovation/MiraclePlus) |

## Features

Unified doc-editor + infinite-canvas whiteboard (BlockSuite engine), Notion-like database/table views, backlinks/tags/journals, AI Copilot (cloud-hosted, paid tier — local Ollama support is community/experimental only, tracked in an open issue, not first-class), mobile apps (iOS/Android since Jul 2025), per-document Markdown export (no bulk workspace export yet — a recurring unresolved request).

## Architecture

TS/React + BlockSuite + Yjs CRDTs for local-first offline editing; Rust for perf-critical native bindings. The self-hosted server (the EE-licensed piece) ships via Docker Compose (Postgres + Redis), and free self-hosted real-time collab is capped at 10 seats by default — classic open-core gating.

## Strengths and risks

**Strengths**: genuinely local-first/offline core; distinctive unified doc+whiteboard UX; well-funded, fast-shipping team.
**Risks**: the server/sync code you'd actually self-host is proprietary EE, not open source; plugin system and local-LLM story are both still immature; no bulk workspace-level export yet (a real migration-cost concern); one past licensing-terms correction (MPL→EE) after community pushback.

## Verdict

**Evaluate further** — compelling local-first UX and active engineering, but the EE-licensed backend and immature local-LLM/plugin story make it premature to depend on for an Ollama/MCP-centric workflow today.

## My Take

AFFiNE's UX is the strongest of the three on its own terms, but the EE-gated backend is the same open-core trade-off Operon's own research flagged with n8n and Onyx (see [[Operon - Competitive Research]]) — a free core that looks complete until the piece you'd actually need to self-host at scale turns out to be the paid one.

## Related

- [[Tools]]
- [[Second Brain - PKM Tools Survey (Aug 2026)]]
- [[PKM Editors - Comparison]]
