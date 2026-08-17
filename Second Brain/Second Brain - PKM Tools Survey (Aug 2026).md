
---
A structured survey of open-source/self-hostable "second brain" and PKM tools, done to evaluate build-vs-adopt-vs-extend options ahead of continued work on **Mnemos** (this repo: Obsidian vault as source of truth + LanceDB local embeddings + Ollama-grounded RAG + Whisper/Piper voice + Tauri shell + MCP connectors). Research was done live via GitHub/web search on 2026-08-15 — treat "last commit"/"stars"/"funding" figures as a snapshot of that date, not evergreen facts.

**Hard constraints applied:** open source or inspectable repo; prefer self-hostable/local-first; commit within the last 12 months (i.e. since ~Aug 2025); portable note format (markdown/plain text preferred).

**Candidates researched:** 10 — the 8 the brief named explicitly (Obsidian, Logseq, AFFiNE, Anytype, Trilium, Foam, Athens Research, Dendron) plus two AI-native entrants (Reor, Khoj).

---

## 1. Screening Pass — Metadata at a Glance

| Project | License | Stars/Forks | Last commit (as of Aug 2026) | Passes 12-mo rule? | Note format | Screening result |
|---|---|---|---|---|---|---|
| **Obsidian** | Proprietary freeware (core); plugin API/community plugins are open | n/a (no core repo); releases repo 20.8k★ | Active (v1.11, Jan 2026) | Yes | Markdown + YAML (native) | Excluded from shortlist — core app not open source |
| **Logseq** | AGPL-3.0 | 44.5k★ / 2.8k | Active (2.0.1 DB beta, Jul 2026) | Yes | Markdown/Org (file version); SQLite (new DB version) | **Shortlisted** |
| **AFFiNE** | MIT (client) + proprietary EE (server) — open-core | 71.6k★ / 5.1k | Active (near-daily canary) | Yes | Yjs CRDT (native); Markdown per-doc export only | **Shortlisted** |
| **Anytype** | "Any Source Available 1.0" (client/core, not OSI) + MIT (sync protocol only) | 8.6k★ (ts) / 414★ (heart) | Active (~2-month release cycle) | Yes | Protobuf CRDT object store (proprietary) | Excluded — not OSI open source + weak portability |
| **Trilium → TriliumNext** | AGPL-3.0 | 37.4k★ / 2.5k (carried over via repo transfer) | Active (v0.104.1, Jul 2026) | Yes | SQLite + HTML (native); Markdown export/import | **Shortlisted** |
| **Foam** | MIT | 17.4k★ / 774 | **2026-08-13** (days old) | Yes, easily | Markdown (native, zero lock-in) | **Shortlisted** |
| **Athens Research** | EPL-1.0 | 6.3k★ / 396 | 2022-12-12 | **No — 44 months stale** | n/a | Rejected — abandoned |
| **Dendron** | Apache-2.0 | 7.5k★ / 303 | 2025-06-01 | **No — ~14 months, just outside window** | Markdown + YAML (native, otherwise strong) | Rejected — de facto abandoned |
| **Reor** | AGPL-3.0 | 8.6k★ / 532 | 2025-05-13 (repo **archived** 2026-03-07) | No — archived, read-only | Markdown (native) | Excluded from adoption — kept as architecture reference |
| **Khoj** | AGPL-3.0 | 36.5k★ / 2.4k | Active (beta releases into Aug 2026) | Yes | N/A — augments existing vault, doesn't own storage | **Shortlisted** |

**Shortlist after screening (6, matching the requested 6–8 scope): Logseq, AFFiNE, TriliumNext, Foam, Khoj**, plus Obsidian retained as the ecosystem baseline. Anytype, Athens Research, Dendron, and Reor are documented in full below but excluded from the "adopt/evaluate" running for the reasons in the table.

---

## 2. Per-Repo One-Pagers

### Obsidian (obsidian.md) — *reference baseline, not open source*

| Field | Value |
|---|---|
| Repo | No single core repo — [obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases) (20.8k★), [obsidianmd/obsidian-api](https://github.com/obsidianmd/obsidian-api) |
| License | **Core app: proprietary freeware.** EULA bars reverse-engineering except for plugin dev. Plugin API/community plugins are separately open (many MIT) |
| Maturity | Beta Mar 2020 → v1.0 Oct 2022 → v1.11 Jan 2026 |
| Maintainer | Obsidian.md (Dynalist Inc's founders), ~7-person team, **bootstrapped, zero VC funding**, reported ~$25M ARR |
| Activity | Continuous — ~6,680 community plugins, 695 themes as of Aug 2026 |

**Features:** bidirectional links/backlinks, graph view, canvas, ~6,680-plugin marketplace (Dataview, Templater, Excalidraw), AI only via plugins (Smart Connections, Copilot for Obsidian — both support local Ollama), several community **MCP-server plugins** already exist, paid E2E-encrypted Sync ($4/mo) with free Git/Syncthing workarounds, full mobile parity, vault = plain Markdown + YAML (best-in-class portability).

**Architecture:** Electron desktop, vault is just a folder of `.md` files + a hidden `.obsidian/` JSON config folder. Plugins run **unsandboxed** with full Node/Electron privileges — a real security surface, mitigated only by manual review of the official directory.

**Strengths:** unmatched plugin ecosystem depth (including AI/MCP plugins already built by others); genuinely portable data; sustainable, funding-independent business.
**Risks:** zero code auditability/forkability of the core app; unsandboxed plugin model; paid official Sync/Publish are proprietary hosted services.

**Verdict: Reject** on the strict open-source constraint — but it's already Mnemos's own assumed vault editor, so treat it as the fixed ecosystem to interoperate with, not a candidate to replace or fork.

---

### Logseq (github.com/logseq/logseq)

| Field | Value |
|---|---|
| License | AGPL-3.0 |
| Stars/Forks | ~44.5k / ~2.8k |
| Last release | 2.0.1 "DB beta" (Jul 13, 2026); file-based stable frozen at 0.10.15 (Dec 2025) |
| Maintainer | Logseq Inc. (NYC), $4.1M seed 2022 (a16z, Craft, Day One) — no confirmed later round; small team (~5, unverified precisely) |
| Open issues | ~898, some long-open with no maintainer response |

**Features:** block outliner, backlinks, graph view, Datalog query system, whiteboards, spaced-repetition flashcards, PDF/Zotero integration, ~486 community plugins, **community-built `mcp-logseq` MCP server + `ollama-logseq`/AssistSeq local-LLM plugins** (no first-party AI yet), paid Sync ($5/mo) or self-hosted Git/Syncthing (file version only).

**Architecture — flag this clearly:** Clojure/ClojureScript + React + Electron. The stable product is genuinely local-first (plain Markdown/Org files as truth, loaded into an in-memory DataScript graph). But Logseq is mid-transition to a **new SQLite-backed "DB version" (2.0, beta)** with real-time collaboration — a breaking architectural change that trades away the "just Markdown files" portability story the file version is known for. Official docs warn of data-loss risk during migration.

**Strengths:** mature outliner/query/plugin stack with existing Ollama/MCP community tooling; genuinely local-first file version; large active community despite a small core team.
**Risks:** small VC-backed team with stale public funding data — sustainability unclear; DB-version rewrite undercuts the plain-text promise and is still beta; Clojure codebase raises the bar for a Node/Next.js-comfortable team to contribute or fork.

**Verdict: Evaluate further** — adopt only the file-based (OG) version deliberately; treat the DB rewrite as a separate, riskier product line to watch, not build on yet.

---

### AFFiNE (github.com/toeverything/AFFiNE)

| Field | Value |
|---|---|
| License | **Open-core**: everything except `packages/backend/server` is MIT; the sync/collab server is under a proprietary "AFFiNE Enterprise Edition" license (production self-host beyond free seat limits requires a paid subscription) |
| Stars/Forks | ~71.6k / ~5.1k |
| Activity | Near-daily canary builds; stable 0.27.3/0.27.4-beta (Aug 2026) |
| Maintainer | Toeverything Pte Ltd (Singapore), $8M pre-Series A (2023, Redpoint/Sinovation/MiraclePlus) |

**Features:** unified doc-editor + infinite-canvas whiteboard (BlockSuite engine), Notion-like database/table views, backlinks/tags/journals, AI Copilot (cloud-hosted, paid tier — **local Ollama support is community/experimental only**, tracked in an open issue, not first-class), mobile apps (iOS/Android, since Jul 2025), per-document Markdown export (no bulk workspace export yet — a recurring unresolved request).

**Architecture:** TS/React + BlockSuite + Yjs CRDTs for local-first offline editing; Rust for perf-critical native bindings. Self-hosted server (the EE-licensed piece) ships via Docker Compose (Postgres + Redis) and free self-hosted real-time collab is **capped at 10 seats** by default — classic open-core gating.

**Strengths:** genuinely local-first/offline core; distinctive unified doc+whiteboard UX; well-funded, fast-shipping team.
**Risks:** the server/sync code you'd actually self-host is proprietary EE, not open source; plugin system and local-LLM story are both still immature; no bulk data export at the workspace level yet (real migration-cost concern); one past licensing-terms correction (MPL→EE) after community pushback.

**Verdict: Evaluate further** — compelling local-first UX and active engineering, but the EE-licensed backend and immature local-LLM/plugin story make it premature to depend on for an Ollama/MCP-centric workflow today.

---

### Anytype (github.com/anyproto/anytype-ts, anytype-heart, any-sync)

| Field | Value |
|---|---|
| License | Client + middleware: **"Any Source Available License 1.0"** — source-visible, **not OSI open source**. Only the `any-sync` network protocol is MIT |
| Stars/Forks | anytype-ts ~8.6k★/571; anytype-heart ~414★/117 |
| Activity | ~6 releases/year, all three repos actively committed |
| Maintainer | Anytype (Germany), Series A $13.4M (2023, Balderton); team-size figures conflict wildly across sources (unverified) |

**Features:** "everything is an object" model (notes/tasks/people/DBs as linked, typed objects), relations + graph view, database-style collection views, a **real local API + official `anytype-mcp` server** (genuine MCP support today), P2P local-first sync with no mandatory cloud round-trip, shared workspaces, desktop + mobile.

**Architecture:** Go middleware (`anytype-heart`) embedded in Electron/Swift/Kotlin clients; objects are stored as a **Protocol-Buffers-encoded CRDT tree** — not plain text, not inspectable without Anytype's own code. Self-hosting the sync network is technically possible via a community `any-sync-bundle`, but Anytype's own hosted network is clearly the primary supported path.

**Strengths:** rich structured-object/relations model beyond flat notes; genuinely offline-capable P2P sync; MCP integration is real and usable now (a rare thing on this list).
**Risks:** core data format is proprietary and only exportable via lossy/community tooling; the license on the code that matters most is not actually open source; **documented history of update-triggered data loss** during migrations.

**Verdict: Reject** — the proprietary object format is structurally at odds with the "portable markdown, no DB lock-in" requirement, and the non-OSI license on the client/core limits any real forkability, despite the notably strong MCP story.

---

### Trilium Notes → TriliumNext (github.com/TriliumNext/trilium)

| Field | Value |
|---|---|
| Fork lineage | **Resolved cleanly**: original maintainer zadam formally transferred the repo to the community-led TriliumNext org (Jan 2024); the interim `TriliumNext/Notes` repo is now archived (Jun 2025) — a decoy for stale links |
| License | AGPL-3.0 (unchanged through the transfer) |
| Stars/Forks | ~37.4k / ~2.5k (carried over) |
| Last release | v0.104.1 (Jul 25, 2026), roughly monthly cadence |

**Features:** hierarchical note tree with "cloning" (a note can live in multiple tree locations), relation/link maps (linking-adjacent, but tree-first, not a true bidirectional graph), attributes for tagging/scripting, canvas (Excalidraw) and mind-map notes, **built-in JS note-scripting + REST API**, per-note encryption, self-hosted server mode for web/mobile access, and **native pluggable LLM providers — OpenAI, Anthropic, Ollama, LM Studio — plus vector-embedding semantic search and agent tools**, all first-party.

**Architecture:** Node/Electron client with an optional self-hosted server, everything backed by **SQLite**. Important portability caveat: notes are stored natively as **HTML** (CKEditor-based), not Markdown — Markdown is an import/export conversion, not the source of truth.

**Strengths:** cleanest governance story on this list (real handoff, not a fork race); the richest first-party AI/LLM integration surveyed (native Ollama support out of the box); active monthly releases with visible bug-fix velocity.
**Risks:** native format is HTML/SQLite, not plain Markdown — a real portability cost if that's a hard requirement; "graph view" is really tree + relation maps, not a Roam/Obsidian-style graph; mobile is web-only officially (native apps are unofficial third-party).

**Verdict: Evaluate further** — the best "batteries-included local-LLM" experience surveyed, but weigh the HTML-native storage against the plain-text-portability priority before treating it as a daily driver.

---

### Foam (github.com/foambubble/foam)

| Field | Value |
|---|---|
| License | MIT |
| Stars/Forks | ~17.4k / 774, 134 contributors |
| Last commit | **2026-08-13** — two days before this survey, near-daily cadence through Jul–Aug 2026 including an active performance-optimization sprint |
| Maintainer | Community-led (Jani Eväkallio, founder; Riccardo Ferretti doing most recent commits — a bus-factor flag despite 134 total contributors) |

**Features:** wiki-links with autocompletion/diagnostics, backlinks, a **self-built graph visualization webview** (Lit + d3-force — not borrowed from VS Code), tags, daily notes, templates, embeddings-based "related notes," and — added mid-2026 — **`@foam/mcp`, a dedicated Model Context Protocol server exposing the Foam knowledge graph to AI agents**. Publishing to static sites via `foam-cli`.

**Architecture — "is it just a wrapper?" check:** Foam runs entirely inside VS Code and stores nothing but plain Markdown files (zero proprietary storage; sync is whatever the user already does — Git/Syncthing/Dropbox). But it is **not** a thin config layer: the monorepo (`foam-core`, `foam-graph`, `foam-vscode`, `foam-cli`, `foam-mcp`) contains a real parsing/data-model layer and an originally-built graph engine and UI. VS Code supplies the editor/file-watching substrate; Foam supplies the PKM-specific logic on top.

**Strengths:** most active repo surveyed by a wide margin, with a real, current commit history to prove it; substantial original engineering (graph engine, AI/embeddings, MCP server), not glue code; zero lock-in — MIT, plain Markdown, any sync method.
**Risks:** effectively single-maintainer-driven recent activity despite 134 historical contributors; hard-dependent on VS Code (no standalone app); Discord/Discussions responsiveness unverified in this pass.

**Verdict: Adopt for evaluation** — the dormancy risk this project is often perceived to carry is factually false as of Aug 2026 (days-old commits, active AI/MCP feature work); the closest thing on this list to "small, portable, MCP-native, zero lock-in."

---

### Athens Research (github.com/athensresearch/athens)

| Field | Value |
|---|---|
| License | EPL-1.0 |
| Stars/Forks | 6.3k / 396 |
| Last commit | **2022-12-12** |
| Status | Not GitHub-archived, but README/description state verbatim: *"Athens is no longer being actively maintained... backed by YC W21"* |

**Features (as it existed):** Roam-style block outliner, bidirectional links, block refs/embeds, graph view, DataScript/Datalog query layer, self-hostable Electron client.
**Architecture:** Clojure/ClojureScript + DataScript in-memory graph DB.

**Strengths:** novel Datascript-graph architecture; fully open EPL-1.0 license; strong Roam-like UX in its day.
**Risks:** 44 months with zero commits; explicit maintainer abandonment statement; no active community fork found; ClojureScript limits pickup even if revived.

**Verdict: Reject** — fails the 12-month activity constraint by nearly four years; confirmed dead, not just quiet.

---

### Dendron (github.com/dendronhq/dendron)

| Field | Value |
|---|---|
| License | Apache-2.0 (changed from GPLv3 specifically to ease community forking, Feb 2023) |
| Stars/Forks | 7.5k / 303, 244 contributors |
| Last commit | 2025-06-01 |
| Status | Official Feb 2023 statement from creator Kevin Lin: the venture-backed team "were ultimately not able to find product-market fit," moving to best-effort "maintenance mode"; 780 open issues with no dedicated triage as of Aug 2026 |

**Features:** hierarchical note "schemas" enforcing structure, static-site publishing (Next.js pipeline), note-graph visualization, backlinks, deep VS Code integration, multi-vault support, plain Markdown + YAML storage. No native AI/LLM integration found.

**Architecture:** VS Code extension, local-first plain Markdown files, more structurally opinionated than Foam via its schema system.

**Strengths:** durable plain-Markdown+YAML storage; mature schema/publishing feature set; permissive license explicitly meant to invite forks.
**Risks:** commit cadence down to sporadic single commits per year; large, untriaged issue backlog; no successor maintainer or fork has emerged despite the license change inviting one.

**Verdict: Reject** — last commit ~14 months before this survey (just outside the 12-month window), and the 2023 "maintenance mode" announcement plus stalled backlog confirm de facto abandonment; worth re-checking if a fresh commit lands.

---

### Reor (github.com/reorproject/reor) — *AI-native entrant, architecture reference*

| Field | Value |
|---|---|
| License | AGPL-3.0 |
| Stars/Forks | ~8.6k / ~532 |
| Status | **Repo archived by the owner on 2026-03-07** (read-only); last commit 2025-05-13 |
| Maintainer | Effectively two people (samlhuillier, milaiwi) drove the large majority of commits; no VC/YC backing found |

**Features:** Markdown editor (BlockNote/Tiptap), **auto-suggested related notes via embedding similarity** rather than manual wikilinks, chat/RAG over your note corpus, hybrid keyword+vector search, Ollama or OpenAI-compatible endpoints. No graph view, no plugin system, no mobile, no MCP.

**Architecture — directly relevant to Mnemos:** Electron + TS + React; markdown vault as source of truth; notes chunked and embedded locally via **Transformers.js** (ONNX) into a **LanceDB**-backed store — the same embedded vector-DB choice Mnemos itself uses — with a direct **Ollama** integration (including auto-managing the Ollama binary) and optional cloud LLM fallback via `@ai-sdk`.

**Strengths:** validates the exact local-markdown + local-embeddings(LanceDB) + local-LLM(Ollama) pattern this project is already built on; real, readable reference implementation of that embed/RAG pipeline; no vendor lock-in in its data model.
**Risks:** archived/dormant, not a living dependency; bus-factor risk fully realized (a two-person effort that stopped); missing table-stakes features (plugins, graph, mobile, MCP) relative to Obsidian/Logseq/Foam.

**Verdict: Evaluate further — as source-code reference only, not adoptable.** Worth reading `reorproject/reor`'s embedding/RAG code directly since it's the closest architectural sibling to Mnemos surveyed, even though the project itself is dead.

---

### Khoj (github.com/khoj-ai/khoj) — *AI-native entrant*

| Field | Value |
|---|---|
| License | AGPL-3.0 |
| Stars/Forks | ~36.5k / ~2.4k, ~57 contributors |
| Activity | Beta releases continuing into Aug 2026 (`2.0.0-beta.28`+), roughly biweekly/monthly |
| Maintainer | Khoj AI (YC S23), tiny team (~3, unverified precisely) |
| **Major 2026 event** | **Khoj Cloud (the paid hosted tier) was deprecated Apr 15, 2026** — self-host is now the only option. Company attention has visibly shifted to a sibling product, **Pipali**, an MCP-native "AI coworker" (Slack/Linear/Notion/Google Workspace tool-use) |

**Features:** chat with notes/docs/web simultaneously across Markdown, org-mode, PDF, Word, Notion; semantic search; custom agents (persona + scope + tools + model); scheduled automations ("research mode"); voice input, image generation; **direct Obsidian plugin and Emacs plugin** for ingesting an existing vault; runs against Ollama, llama.cpp, vLLM (any OpenAI-compatible local server) or cloud LLMs.

**Architecture — the key positioning point:** Python/Django backend that sits **on top of** an existing vault rather than replacing the editor — your Obsidian/Emacs/filesystem notes stay the source of truth, Khoj adds RAG/agents/automation via Postgres+pgvector, self-hosted via Docker. This "augmentation layer over an existing vault" model is architecturally the closest match to what Mnemos itself already does.

**Strengths:** genuinely complements an existing Obsidian vault instead of demanding migration; first-class local-model support (Ollama/llama.cpp/vLLM) with no forced cloud dependency; real differentiated engineering (agents, scheduled automations, multi-source RAG), not a thin LLM-API wrapper.
**Risks:** the company's only monetization (Khoj Cloud) just shut down and its MCP/agentic engineering investment has visibly moved to a separate product (Pipali) — Khoj's own future feature velocity is an open question; MCP support inside Khoj proper is nascent/unclear (a maintainer thread shows this was still being scoped); still shipping as `2.0.0-beta.x` after a long stretch, signaling schema/API instability.

**Verdict: Evaluate further (narrow pilot, not full adopt)** — the closest architectural sibling to Mnemos among actively-maintained projects (Ollama-first, augments an Obsidian vault, doesn't own the storage format); pilot it in Docker against a copy of the vault specifically to check sync reliability and current MCP depth before relying on it daily.

---

## 3. Master Comparison Matrix

| Dimension | Obsidian | Logseq | AFFiNE | Anytype | TriliumNext | Foam | Reor | Khoj |
|---|---|---|---|---|---|---|---|---|
| **Problem-fit** | Editor + ecosystem | Outliner/graph note-taking | Docs + whiteboard hybrid | Object/relation PKM | Hierarchical notes + scripting | Markdown linking/graph in VS Code | AI-native note editor | AI/RAG layer *over* existing notes |
| **Maturity vs. innovation** | Very mature | Mature core, beta rewrite | Mature UX, immature plugins/AI | Mature core, evolving format | Very mature (6+ yrs incl. predecessor) | Mature, actively evolving | Was early-stage; now dead | Mature-ish, beta-labeled |
| **Local-first vs. cloud-dependent** | Local-first, paid cloud sync optional | Local-first (file ver.); DB ver. adds RTC | Local-first core; paid EE server for scale sync | Local-first w/ P2P sync | Local-first + optional self-hosted server | Fully local (VS Code + files) | Fully local, optional cloud LLM | Local-first layer, self-host only now |
| **TCO** | Free personal use; $4-8/mo for Sync/Publish | Free; $5/mo Sync optional | Free MIT core; EE licensing costs at scale (>10 seats) | Free; hosted network is default path | Free, self-host infra only | Free (VS Code + extension) | Free (moot — archived) | Free (self-host infra + compute) |
| **Vendor/format lock-in risk** | Low (data) / med (workflow, plugins) | Low (file ver.) / med (DB ver.) | Medium — CRDT native, per-doc export only | **High** — proprietary protobuf object store | Medium — HTML/SQLite native, MD is export-only | **Very low** — plain MD, MIT | Low — plain MD | None — doesn't own storage |
| **Migration cost (getting notes out)** | Very low | Low (file ver.) / unclear (DB ver., beta) | Medium-high (no bulk export yet) | High (lossy without community tools) | Medium (HTML→MD export works but isn't native) | Very low | Very low | N/A (never owns the data) |
| **Learning curve** | Low-medium | Medium (outliner/query paradigm) | Low (Notion-like) | Medium-high (object model) | Medium (tree + scripting) | Low if already in VS Code | Low | Low (bolt-on to existing workflow) |
| **Extensibility/plugin depth** | **Very high** (~6,680 plugins) | High (486 plugins + Datalog queries) | Low/immature | Medium (API/MCP, no plugin marketplace) | Medium (built-in scripting + REST API) | Medium (VS Code ecosystem + own graph/MCP code) | None | Medium (agents, custom personas) |
| **AI/LLM integration readiness** | High via plugins (Ollama-capable, MCP plugins exist) | Medium, community-plugin only | Low (cloud-first, local experimental) | Medium-high (official MCP server) | **High — native Ollama/OpenAI/Anthropic/LM Studio providers** | **High — native `@foam/mcp` server** | High pattern, but project dead | **High — Ollama/llama.cpp/vLLM native, but MCP depth unclear** |
| **Community trajectory** | Growing, funding-independent | Stable-to-uncertain (small team, DB pivot) | Growing, well-funded | Growing, funding disputed | Stable, healthy post-transfer | **Growing, very active** | Declining → archived | Uncertain (cloud shutdown, focus shift to Pipali) |
| **License compatibility** | Proprietary — least compatible for redistribution/forking | AGPL-3.0 | Mixed MIT + proprietary EE | Non-OSI (source-available) | AGPL-3.0 | **MIT — most permissive** | AGPL-3.0 (moot, archived) | AGPL-3.0 |

---

## 4. Verdicts at a Glance

| Project | Verdict | One-line reasoning |
|---|---|---|
| **Obsidian** | Reject (adopt as ecosystem, not a candidate) | Closed-source core disqualifies it on the strict constraint, but it's already Mnemos's assumed vault editor and worth mining for plugin/MCP patterns |
| **Logseq** | Evaluate further | Strong ecosystem and community MCP/Ollama plugins, but small VC-backed team and a breaking SQLite rewrite in progress |
| **AFFiNE** | Evaluate further | Genuinely local-first and well-funded, but the self-hostable sync server is proprietary EE-licensed and local-LLM/plugin support is still immature |
| **Anytype** | Reject | Proprietary protobuf object format plus a non-OSI license make it the worst fit on portability and openness, despite real MCP support |
| **TriliumNext** | Evaluate further | Best first-party local-LLM integration surveyed, but native HTML/SQLite storage (not Markdown) costs real portability |
| **Foam** | **Adopt for evaluation** | Most active repo surveyed, MIT, zero lock-in, and ships its own MCP server — closest fit to "extend, don't replace" |
| **Athens Research** | Reject | Dead since Dec 2022, explicit maintainer abandonment statement |
| **Dendron** | Reject | De facto abandoned since a 2023 "no PMF" announcement; last commit just outside the 12-month window |
| **Reor** | Evaluate further (reference only) | Archived, but its Ollama+LanceDB+Markdown pipeline is the closest architectural twin to Mnemos surveyed — read the code, don't depend on the project |
| **Khoj** | Evaluate further (narrow pilot) | Closest living architectural sibling to Mnemos (augments an existing Obsidian vault, Ollama-first), but its company just killed its only revenue stream and shifted AI/MCP investment to a separate product |

---

## 5. Recommendation

**Don't replace Mnemos's foundation — it's already ahead of the field on the specific axis this survey was scoped around** (local Markdown vault as truth, local embeddings via LanceDB, local LLM via Ollama, MCP connectors). None of the 10 surveyed projects combine all of those with a mature plugin ecosystem *and* a healthy, well-funded team *and* a fully portable format — every one of them trades off at least one.

Concretely, for the Windows/Ollama/Antigravity/MCP stack described:

1. **Keep Obsidian as the human-facing vault editor** (as the README already assumes) — don't try to build a competing editor. Its plugin ecosystem already has working Ollama- and MCP-based tools worth studying (Smart Connections, Copilot for Obsidian, community MCP plugins) even though the app itself isn't open source.
2. **Treat Foam as the primary "evaluate further" candidate for direct adoption or code borrowing.** It's MIT, actively developed (commits from this week), has zero data lock-in, and — notably — already shipped its own MCP server (`@foam/mcp`) exposing a note graph to AI agents, which is exactly the kind of connector Mnemos's Step 6 (MCP connectors) is heading toward. Read its `foam-graph`/`foam-mcp` packages before building Mnemos's own MCP-exposed graph server.
3. **Mine Reor's source for the embedding/RAG pipeline**, since it used the identical Ollama + LanceDB + local-Markdown stack Mnemos already runs — even though the project is archived, its code is a validated reference implementation, not a hypothetical.
4. **Pilot Khoj in Docker against a copy of the vault**, specifically to test whether its scheduled-automations/multi-source-ingestion model (Obsidian + Notion + filesystem) could shortcut Mnemos's own Step 6+ connector roadmap — but don't commit to it as infrastructure until its post-cloud-shutdown trajectory and MCP maturity are clearer (re-check in 3–6 months).
5. **Avoid Anytype and Trilium/TriliumNext as full migrations** — both would mean giving up the plain-Markdown-vault foundation Mnemos is built on (protobuf CRDT for Anytype; HTML/SQLite for Trilium), even though Trilium's native multi-provider local-LLM support is worth copying as a pattern (provider abstraction over Ollama/OpenAI/Anthropic/LM Studio).
6. **AFFiNE and Logseq are worth periodic re-checks** but not urgent: AFFiNE's local-LLM story needs another 6–12 months to mature past "experimental," and Logseq's SQLite rewrite needs to stabilize before its plugin/MCP ecosystem is worth building on top of.

**Bottom line for local-LLM/MCP readiness specifically:** Foam (native MCP server, zero lock-in, MIT) and Khoj (Ollama-native, vault-augmenting architecture) are the two best-aligned living projects with your Ollama + Antigravity + MCP setup — but both are better treated as *sources of ideas and code to fold into Mnemos* than as replacements for it, given how closely Mnemos's own architecture already matches the direction this space is moving.
