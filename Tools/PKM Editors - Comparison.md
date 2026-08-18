---
title: PKM Editors - Comparison
aliases: [Logseq vs AFFiNE vs Anytype]
tags: [tools, research, pkm]
type: moc
status: growing
created: 2026-08-18
updated: 2026-08-18
related: ["[[Logseq - Brief]]", "[[AFFiNE - Brief]]", "[[Anytype - Brief]]"]
source: 
---

# PKM Editors - Comparison

## Summary

Logseq, AFFiNE, and Anytype compared head-to-head — no specific adoption decision behind this one, just landscape clarity. All three were already researched live on Aug 15, 2026 as part of [[Second Brain - PKM Tools Survey (Aug 2026)]]; this note pulls just these three out for a direct comparison rather than re-deriving their facts (see [[Logseq - Brief]], [[AFFiNE - Brief]], [[Anytype - Brief]] for the full per-tool detail).

## Comparison matrix

| Dimension | Logseq | AFFiNE | Anytype |
|---|---|---|---|
| License | AGPL-3.0 | Open-core: MIT client + proprietary EE server | Any Source Available 1.0 — **not OSI open source** |
| Data format | Plain Markdown/Org (file version) — **portable** | Yjs CRDT native; per-doc Markdown export only, no bulk export | Protobuf CRDT object store — **proprietary, lossy export** |
| Local-first | Yes (file version); DB version adds real-time collab, still beta | Yes, offline-capable core | Yes, genuine P2P sync, no mandatory cloud |
| AI/MCP readiness | Community-only (`mcp-logseq`, `ollama-logseq`) — no first-party AI | Cloud Copilot (paid); local Ollama community/experimental only | **Official `anytype-mcp` server** — real, usable today |
| Funding/backing | $4.1M seed (2022), no confirmed later round | $8M pre-Series A (2023) | $13.4M Series A (2023) |
| Stars (repo) | ~44.5k | ~71.6k | ~8.6k (ts) / ~414 (heart) |
| Biggest risk | Breaking DB-version rewrite undercuts its own portability story | Self-hostable piece you'd actually need (sync server) is proprietary EE | Core format is proprietary; non-OSI license blocks real forkability |
| Verdict | Evaluate further (file version only) | Evaluate further | **Reject** |

## Where each one actually wins

```mermaid
quadrantChart
    title Data portability vs. AI/MCP readiness
    x-axis Locked-in --> Portable
    y-axis Weak AI/MCP --> Strong AI/MCP
    quadrant-1 Best of both (none land here)
    quadrant-2 Portable, AI-weak
    quadrant-3 Locked-in, AI-weak
    quadrant-4 Locked-in, AI-strong
    Logseq: [0.7, 0.25]
    AFFiNE: [0.35, 0.3]
    Anytype: [0.15, 0.75]
```

No tool here is strong on both axes at once — that's the actual finding, not a gap in the research. Logseq (file version) leads on portability; Anytype leads on AI/MCP readiness by a wide margin; AFFiNE sits in the middle on both, ahead of neither.

## Verdict

For this vault's own priorities (plain-Markdown source of truth, no DB lock-in, MCP-based AI integration per [[00 - Rules Index|the vault's own rules]] and the Mnemos/Relay pattern) — **none of the three is a clean adoption**, and that's consistent with the original PKM survey's own conclusion. If forced to rank for a portability-first workflow: **Logseq's file version first** (genuinely portable, if you accept its DB-rewrite is a separate, riskier track to ignore for now), **AFFiNE second** (best UX, but the self-hostable piece that matters is EE-gated), **Anytype last** despite its best-in-class MCP story — the proprietary object format is disqualifying for a vault built on "plain files, no lock-in."

If the priority were flipped to "best AI-agent integration right now, portability secondary," Anytype would win outright — its official MCP server is real and shipping, while Logseq's and AFFiNE's AI stories are both community-plugin-or-cloud-paid-tier stopgaps.

## My Take

The quadrant makes the actual trade-off visible in a way the matrix alone doesn't: there's no tool here trying to be both portable *and* AI-native at once — each picked one axis to win on. That's worth remembering the next time a "does everything" PKM tool gets pitched; on this evidence, that combination doesn't exist yet among mainstream options.

## Related

- [[Logseq - Brief]]
- [[AFFiNE - Brief]]
- [[Anytype - Brief]]
