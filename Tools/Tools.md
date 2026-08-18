---
title: Tools
aliases: [Tools MOC]
tags: [tools, research, meta]
type: moc
status: growing
created: 2026-08-18
updated: 2026-08-18
related: ["[[Git Repo Research Framework]]", "[[App Ideas]]", "[[Active Projects]]"]
source: 
---

# Tools

Hub for single-tool deep-dive research — evaluating one specific existing tool/product for possible adoption, as distinct from [[App Ideas]] (concepts I might build) and [[Active Projects]] (infrastructure I already reuse). Each tool gets its own subfolder, researched using [[Git Repo Research Framework]] and the [[Repo Research Kickoff Prompt (Template)]] methodology.

## Structure

```mermaid
flowchart TD
    A[Tools]
    A --> B["Hyvor Relay/"]
    B --> B1[Brief]
    B --> B2[Features and Architecture]
    B --> B3[Comparison]
    B --> B4[Licensing and Maturity]
    B --> B5[Recommendation]
    A --> C["Logseq/, AFFiNE/, Anytype/"]
    C --> D[PKM Editors - Comparison]
```

## Tools researched

| Tool | What it is | Verdict |
|---|---|---|
| [[Hyvor Relay - Brief\|Hyvor Relay]] | Self-hosted, open-source transactional email API (SES/Mailgun/SendGrid alternative) | Pilot-worthy above ~50k emails/month with ops capacity; not worth it below that |
| [[Logseq - Brief\|Logseq]] | Block-outliner PKM tool, mid-transition to a SQLite-backed DB version | Evaluate further — file version only |
| [[AFFiNE - Brief\|AFFiNE]] | Unified doc-editor + whiteboard, open-core | Evaluate further — EE-gated backend |
| [[Anytype - Brief\|Anytype]] | "Everything is an object" PKM tool with real MCP support | Reject — proprietary object format |

## Cross-tool comparisons

| Comparison | Tools covered | Verdict |
|---|---|---|
| [[PKM Editors - Comparison]] | Logseq, AFFiNE, Anytype | No tool wins on both portability and AI/MCP readiness; Logseq (file version) ranks first for a portability-first vault |

## Related

- [[Git Repo Research Framework]]
- [[App Ideas]]
- [[Active Projects]]
