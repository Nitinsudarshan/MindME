---
title: Relay - IDE Build Prompt
aliases: [Relay Build Prompt, Relay Antigravity Prompt]
tags: [app-ideas, relay, dev]
type: resource
status: growing
created: 2026-08-18
updated: 2026-08-18
related: ["[[Relay - Decision Log]]", "[[PDDB Prompt Template]]", "[[Relay - Brief]]"]
source: 
---

# Relay - IDE Build Prompt

## Summary

The IDE-ready prompt [[PDDB Prompt Template]] generated for Relay, sourced from [[Relay - Decision Log]] (12 decisions, current as of 2026-08-18) plus the underlying research notes. This is the file to paste into Google Antigravity — per Decision 11 — to actually start building. Regenerate and overwrite this note if the decision log changes materially; it's a derived artifact, not a second source of truth.

---

## The prompt

```
# Relay — AI IDE Build Prompt
Target build environment: Google Antigravity

## Operating Mode

You are operating inside an IDE with access to this repository, its files,
configuration, and available development tools. The project context in this
repo — plus the pre-answered context below, which comes from prior product
research and a confirmed decision log — is your source of truth. Your job is
not to produce documentation. Your job is to take this project from:

Context → Understanding → Specification → Implementation → Testing → Working Product

## Pre-Answered Product Context (do not re-ask these)

**What it is**: A hybrid (local + cloud) AI voice and memory assistant that
turns captured voice into structured, actionable system state — a Kanban
card, a calendar event, a reminder, a polished document — with minimal
manual re-entry.

**Core problem**: Closing the gap between "I said something" and "something
useful happened," without a manual re-entry step in between.

**Primary users**: The builder themselves, for a workflow that's meeting- and
task-heavy rather than pure knowledge-capture. Personal use for now — see
"Noted, not in scope" below for a possible future direction.

**Feature set**:
- Note-taking via speech-to-text (baseline capture)
- Meeting Notes → Kanban: a meeting transcript is parsed into actionable
  items and lands on a lightweight Kanban board, not just a summary
- Audio Scribbles → Structured Prompts: a rambling voice memo is turned into
  a structured prompt/output template, not just cleaned-up prose
- Local (+optional cloud) memory vault: Obsidian-style markdown as source of
  truth, with retrieval via an embedded vector store, plus an optional cloud
  storage/sync layer
- Push-to-talk + on-screen widget capture affordance
- Record → transcript → LLM-polish pipeline
- MCP connections: push to Google Drive/Notion, pull from Calendar
- **User-customizable trigger-phrase actions** — the user defines their own
  phrase → action mappings in a settings surface; not a hardcoded list
- Target platform: **Windows native app for local use, plus a web client for
  hybrid/cloud mode** — a real dual-surface product, not desktop-only

**Core workflow**: Push-to-talk → local STT transcript → branch on capture
type → {Meeting: extract actionable items → Kanban list} / {Scribble: LLM
polish → structured output} / {Trigger phrase: look up user's configured
action → MCP action} → everything lands in the vault, viewable from either
the native app or the web client.

**MVP scope**: Push-to-talk capture, local STT transcription, meeting→
Kanban-list parsing (list-to-board, not full drag/drop yet), scribble→
structured-output polish, markdown vault storage, a **configurable**
trigger-phrase system (not a hardcoded set) wired to Calendar/reminder
actions via MCP, and a basic web dashboard for the hybrid surface. Runs at
$0 recurring cost locally; any cloud/hybrid option must degrade gracefully
to fully free operation.

**Explicitly out of scope for now**:
- Post-MVP: Notion/Google Drive push via MCP, a real drag-and-drop persisted
  Kanban board, on-screen widget UI polish, a structured-prompt template
  library
- Later: knowledge-graph-based retrieval optimization, TTS voice-feedback
  confirmations, a proper installer
- Experimental: full GraphRAG, cross-device sync, a mobile companion,
  **shared/team vault features** (a team/enterprise, mutual-sharing model was
  raised in planning — noted as a real future direction, not decided or
  scoped, and not part of this build)

**Recommended stack**: A from-scratch Rust backend (Axum/Actix) + Tauri +
React native shell for Windows — Parakeet/Whisper for local STT, Piper for
local TTS, Ollama with a hybrid cloud-LLM toggle (e.g. GPT-4o-mini / Gemini
Flash / Claude Haiku), LanceDB as the embedded vector store, an
Obsidian-style markdown vault as source of truth. A separate Next.js/Shadcn
web frontend serves the hybrid-mode web surface.

**Hybrid-mode data & auth model**: Local-only mode needs no auth at all —
single machine, single user. Hybrid/cloud mode keeps the Windows app as the
primary capture/processing surface, but persisted data (vault entries,
Kanban items, structured outputs) is stored in a cloud backend with real
login — password/token-based auth, not LAN-only or tunnel-based access to
the Windows machine itself. Supabase (or an equivalent free-tier
backend-as-a-service) is the confirmed fit given the $0-first constraint;
its free-tier auto-pause-after-idle-week behavior is a known risk to design
around (e.g. a lightweight keep-alive, or accepting first-request wake
latency).

**What to reuse instead of rebuilding**:
- Clone [[Starter Template]] (`github.com/Nitinsudarshan/boilerplate`) as the
  starting point for the **web dashboard only** — Next.js App Router +
  Shadcn UI, plus the copied `Active Projects/.agents/` and
  `Active Projects/Rules/` conventions.
- Supabase (or equivalent) for hybrid-mode auth + cloud data storage — do not
  hand-roll authentication.
- The native Rust/Tauri shell is **not** covered by any existing boilerplate
  in this vault — scaffold it fresh.
- Reuse `nspady/google-calendar-mcp`, `makenotion/notion-mcp-server`, and
  `isaacphi/mcp-gdrive` (or `piotr-agier/google-drive-mcp`) as-is for the
  Calendar/Notion/Drive integrations — do not write custom integration code
  for these three.
- Study (don't fork) Meetily's provider-abstraction pattern and
  personal-assistant-kit's "MCP client + scheduled prompts" scaffold as
  design references for the hybrid-LLM toggle and the trigger-action layer
  respectively — reimplement the pattern, do not copy the repos.

**What NOT to build, and why**:
- A meeting-bot architecture (joining calls as a bot) — real, active legal/
  platform risk (Fireflies' unresolved BIPA lawsuits; Teams/Zoom/Meet are all
  actively tightening controls against third-party meeting bots)
- Full graph-based retrieval (GraphRAG-style) on day one — only pays off
  above ~1K documents; ship plain vector RAG first
- A fully custom drag-and-drop Kanban app before the meeting→Kanban parsing
  logic itself is validated
- Any code copied or forked from Mnemos or Meetily — this build is from
  scratch by deliberate decision, not an oversight
- A tunnel/remote-access mechanism into the Windows machine for hybrid mode —
  that framing was considered and rejected; hybrid mode is cloud storage +
  auth, not remote access to the local machine

**Competitive differentiation**: No surveyed project (commercial or open-
source) combines bot-free local capture, hybrid local/cloud LLM, transcript-
to-Kanban (every meeting tool surveyed stops at an action-item list, none
produce an actual board), voice-memo-to-structured-prompt (distinct from
generic dictation cleanup), and user-customizable trigger-word actions. The
bot-free design is a structural legal/platform-risk advantage over most of
the commercial category, not just a privacy preference.

**Known technical risks**:
- Meeting→Kanban parsing quality (does the LLM reliably extract genuine
  action items vs. noise) — needs real usage testing, not just prompt design
- A configurable trigger-phrase system is inherently harder to get right than
  a fixed one — false-positive/false-negative behavior needs testing across
  a range of user-defined phrases, not just the two examples from research
- The Rust backend is a deliberate, accepted learning-curve risk — do not
  treat this as a reason to quietly fall back to a different language
- Supabase free-tier auto-pause after a week of inactivity could surprise a
  user opening the web client after time away — design for this explicitly

**Known product risks**: Scope creep into a full PM tool (Kanban must stay a
byproduct of capture, not a competing feature surface against dedicated PM
tools); scope creep into a full meeting-bot product; the web dashboard
duplicating desktop functionality it doesn't need to; scope creep toward
team/multi-user sharing before the single-user product is even validated.

These answers already reflect a full research pass plus a confirmed decision
log. Treat them as settled decisions, not open questions — do not ask me to
re-confirm any of them.

## 1. First, Inspect the Project

Before asking questions or proposing architecture:
- Inspect the repository, existing docs, source code, configuration, and
  dependency files.
- This is a **brand-new, from-scratch repository** — do not expect or look
  for an existing Mnemos or Meetily codebase to extend. If you find
  substantial pre-existing implementation here, treat that as prior work
  within *this* repo (State C below), not evidence you're in the wrong repo.
- Identify what's already implemented vs. incomplete/placeholder as you go.
- Do not ask me for anything determinable by inspecting the project or
  already answered above.

## 2. Establish Project State

- **State A — Idea/Empty**: little or no implementation → begin from the
  pre-answered context above and start specification. This is the expected
  starting state for a brand-new repo.
- **State B — Partially Specified**: some decisions exist, gaps remain →
  fill gaps using the pre-answered context first, ask only about genuine
  conflicts.
- **State C — Partially Built**: substantial implementation exists →
  understand it first, diff it against the pre-answered context, then
  continue.
- **State D — Existing Product**: it already works, this is an enhancement →
  treat it as baseline, extend without unnecessarily breaking it.

## 3. Do Not Over-Ask Questions

Do not ask when the answer is inferable from the project, from the
pre-answered context above, or is a low-impact/reversible implementation
detail. Ask me only when a decision materially changes product behavior,
requirements conflict, there's a real security/privacy/data-loss
implication, or scope/architecture would materially change. Group questions
together and explain why each answer matters.

Hybrid mode's storage/auth model is already settled (see the Pre-Answered
context above) — do not re-litigate LAN-only vs. tunnel vs. public access;
that framing was raised and explicitly rejected during planning.

The one thing genuinely left open: the exact field-level shape of a Kanban
card / transcript record / structured-prompt output. Derive this from what
you build and write it into `docs/data-model.md` as you go — don't ask about
it up front.

## 4. Do Not Wait for Perfect Documentation

Once the core problem, users, MVP scope, workflows, and stack (all above) are
understood, mark the project **READY ENOUGH TO BUILD** and begin.

## 5. Build While Learning

Understand → Specify → Build small piece → Test → Learn → Update
specification → Build next piece. Don't over-document straightforward
decisions.

## 6. Maintain a Living Specification

Create `/docs` in this repo with at minimum: `product.md`, `requirements.md`,
`user-flows.md`, `architecture.md`, `data-model.md`, `api.md`,
`decisions.md`, `testing.md`. Seed `product.md` and `decisions.md` from the
pre-answered context and the decision log below on the first pass, then keep
them current as implementation changes anything important.

## 7. Build Incrementally

Break implementation into vertical slices, tested and integrated before
moving on:

1. Scaffold a brand-new Rust backend (Axum/Actix) and a Tauri+React shell for
   Windows. Wire up local Whisper/Parakeet STT and a hybrid Ollama/cloud-LLM
   provider toggle, config-driven, no UI yet.
2. Build the push-to-talk + on-screen widget capture UI in the Tauri shell.
3. Build the meeting→Kanban-list parser: a prompt template that extracts
   actionable items from a transcript into a structured list.
4. Build a minimal local Kanban view (list-to-board, read from the same
   markdown vault) — no drag/drop yet.
5. Build the audio-scribble→structured-output prompt templates and wire them
   to a second capture mode.
6. Build the **configurable** trigger-phrase system: a settings surface for
   defining phrase → action mappings, plus an intent classifier that reads
   from that config rather than a hardcoded list.
7. Integrate `nspady/google-calendar-mcp` for the calendar-scheduling trigger
   action.
8. Add a local reminder mechanism (OS-level notification or a simple
   scheduled-task write) for the reminder trigger action.
9. Scaffold the web hybrid surface: clone [[Starter Template]] for the
   frontend, stand up a cloud backend with real auth (Supabase or an
   equivalent free-tier BaaS) for hybrid-mode data storage, and wire both the
   web client and the Windows app to authenticate against it and read/write
   the same vault/Kanban data.
10. Dogfood: use Relay for a week of real meetings and voice notes, tracking
    parsing accuracy for the Kanban and structured-output paths, and
    usability of the trigger-phrase configuration itself.
11. Based on dogfooding results, prioritize either Notion/Drive push
    (post-MVP) or drag-and-drop Kanban persistence as the next milestone.

## 8. Stack and Reuse Directive

Scaffold the native Rust/Tauri app fresh — nothing in this vault covers that
combination as a boilerplate. Clone [[Starter Template]] for the web
dashboard only. Use Supabase (or equivalent) for hybrid-mode auth + storage.
Reuse the three named MCP servers as-is. Study, but do not copy code from,
Meetily and personal-assistant-kit for the provider-abstraction and
trigger-action patterns respectively.

Do not introduce a new framework, database, state layer, ORM, UI library, or
service beyond what's listed above without documenting why in
`decisions.md` first.

## 9. Decision Log — seeded from the confirmed decision log

Record every material decision in `docs/decisions.md` in this format:

```
Decision:
Context:
Decision made:
Reason:
Alternatives considered:
Impact:
```

Pre-seed it with all 12 decisions from `Relay - Decision Log.md` — every one
has already been through the Decision Loop process, so do not relitigate
them without a real new reason:

1. **Build path & relationship to Mnemos** — build from scratch in this new
   repo; no code copied from Mnemos or Meetily.
2. **Technology stack** — Rust backend + Tauri/React native shell +
   Next.js/Shadcn web client, chosen deliberately over the better
   capability-fit option (n8n) and over a lower-risk Python build.
3. **Hybrid deployment includes a web surface** — Windows native for local,
   web client required for hybrid/cloud mode.
4. **Cost ceiling is a hard constraint** — every cloud-optional feature must
   work fully at $0 before any paid tier is wired in.
5. **No meeting-bot architecture** — push-to-talk/local-audio capture only.
6. **Retrieval architecture** — plain vector RAG (LanceDB) for MVP; graph-
   based retrieval explicitly deferred.
7. **Kanban delivery scope for MVP** — list-to-board only, no drag/drop yet.
8. **MCP integrations** — reuse the three named community/official servers
   as-is.
9. **No Rust-vs-Python benchmarking spike** — going straight to Rust, spike
   is moot.
10. **Trigger phrases are user-customizable** — not a hardcoded set; a real
    scope increase over the original MVP definition.
11. **Target build environment** — Google Antigravity.
12. **Hybrid-mode architecture** — cloud storage + real login (password/
    token), not remote/tunnel access into the Windows machine; Supabase's
    free-tier auto-pause is a flagged risk.

Full context/reason/alternatives/impact for each is in
`App Ideas/Relay/Relay - Decision Log.md` in the source vault — carry the
full text into `docs/decisions.md`, not just this summary list.

## 10. Do Not Fake Functionality

No feature counts as done if it only looks right in the UI, uses
hardcoded/mock data, skips auth/permissions, doesn't persist required data,
or doesn't handle errors. Mocks are fine mid-development if explicitly
marked temporary and replaced before the feature is called
production-ready.

## 11. Validate as You Build

After each meaningful feature: run tests, check types/lint/build, check
migrations, check the relevant user flow and its error states. In
particular, validate meeting→Kanban parsing and the configurable
trigger-phrase system against real transcripts and real user-defined
phrases, not just synthetic examples. Don't accumulate large amounts of
untested code.

## 12. Protect Existing Functionality

Before changing anything that already works in this repo: understand it,
check its dependents and tests, make the smallest safe change, verify it
still works.

## 13. Definition of Done

A feature is done when: it's implemented, the UI works (in both the native
app and, where applicable, the web client), data persists correctly,
permissions/validation/error states work, the meeting→Kanban and
trigger-phrase edge cases are handled (not just the happy path), tests pass,
nothing else broke, and `/docs` reflects it.

## 14. When to Stop and Ask Me

Only for: two requirements conflicting, an ambiguous destructive data
operation, an unclear privacy/security call, a request that fundamentally
changes MVP scope, two incompatible workflow interpretations, or a major
architecture change not covered above. Otherwise, decide and continue.

## 15. Default Behavior

Behave like a senior product engineer, not a consultant who only produces
plans: Inspect → Understand → Plan → Document → Build → Test → Review →
Continue. If the project is sufficiently clear — and per the pre-answered
context above, it is — start building without waiting to be told "now start
coding."
```

## My Take

The one thing worth remembering about this specific prompt: Decision 2 was made in direct, acknowledged tension with the capability data in `Profile/` (n8n is the advanced, production-proven skill; Rust isn't a listed skill at all). That's fine — it's a real choice, not an oversight — but if the Rust learning curve turns Milestone 1 into a multi-week stall, Stack D (n8n-as-brain, from the earlier exploration) is the documented fallback, not a start-over.

## Related

- [[Relay - Decision Log]]
- [[PDDB Prompt Template]]
- [[Relay - Brief]]
