---
title: Relay - Competitive Research
aliases: []
tags: [app-ideas, relay, research]
type: resource
status: growing
created: 2026-08-17
updated: 2026-08-17
related: ["[[Relay - Brief]]", "[[Git Repo Research Framework]]", "[[Relay - Implementation Options]]"]
source: 
---

# Relay - Competitive Research

## Summary

Live research (Aug 17, 2026) across commercial meeting-notes tools, open-source meeting/transcript projects, voice-command/MCP agent projects, and cost paths for the underlying components, following [[Git Repo Research Framework]]. Cross-checked against a prior 10-project survey of the dictation/notetaking/context-capture landscape (AnythingLLM, Onyx, PrivateGPT, Reor, OpenWhispr, Handy, VoiceInk, espanso, Screenpipe, OpenRecall). The single most important finding: **Microsoft Teams, Zoom, and Google Meet are all actively tightening controls against third-party meeting bots in 2026** — Relay's push-to-talk/local-audio-capture design sidesteps this entire risk category by never joining a call as a bot.

## Commercial meeting-notes-to-action-items tools

| Tool | Open source? | Pricing | Kanban/task output? | Standout | Real weakness |
|---|---|---|---|---|---|
| Fireflies.ai | No | Free–$39/user/mo | Action items list, not Kanban | Deep CRM/integration ecosystem | **Two active BIPA biometric-privacy lawsuits** (consolidated N.D. Illinois, Jun 2026, unresolved) |
| Otter.ai | No | Free–$30/user/mo | Assignable action items, not Kanban | Cross-meeting NL search | Same meeting-bot detection friction as the category |
| Fathom | No | Free (5/mo)–$34/user/mo | Action items + follow-up emails | Sub-30-second summaries | Free tier crippled fast |
| **Granola** | No | Free–$35/user/mo | Personal API (paid tiers) | **No meeting bot** — local device audio capture while typing rough notes | Needs active participation, not fire-and-forget |
| tl;dv | No | Free–$59/user/mo | No dedicated Kanban despite marketing | 5,000+ integrations | — |
| Read.ai | No | Free (5/mo)–$39.75/user/mo | Via daily briefing | Proprietary engagement scoring | Video-based scoring raises its own privacy questions |

**Category-wide risk**: every bot-based tool above (Fireflies, Otter, Fathom, tl;dv, Read.ai) is exposed to an escalating platform-vs-bot arms race — Teams labels external bots "Unverified" and requires host admission; Meet flags custom bots as "Potential Risk." **Granola's bot-free model, and Relay's push-to-talk design, sidestep this entirely.**

## Open-source meeting/transcript projects

| Project | License | Activity | Verdict |
|---|---|---|---|
| **Meetily** | MIT, ~29.3k★ | Active (Jun 2026 release) | **Adopt/study directly** — Rust + Next.js, Parakeet/Whisper STT, Ollama/Claude/Groq/OpenRouter provider abstraction, markets itself as a Granola/Otter alternative. Closest living open-source sibling to Relay's record→transcript→LLM-polish pipeline. |
| **Vexa** | Apache-2.0, ~2.7k★ | Very active (days-old commits) | **Evaluate as a dependency** — ships its own MCP server exposing transcripts to AI agents, self-hosted, air-gap-ready. But it's a meeting-*bot* architecture (joins Meet/Teams/Zoom), inheriting the same platform-detection risk even though self-hosted. |
| **Amurex** | AGPL-3.0, ~2.9k★ | **~14 months stale** despite marketing pages calling it "actively developed" | **Reject** — a real abandonment case study. Third-party summaries trust 2024–2025 launch buzz over the actual repo state. Confirms: always verify commit/issue dates directly, never trust aggregator copy. |

## Voice-command / MCP agent projects

| Project | License | Voice? | MCP? | Notes |
|---|---|---|---|---|
| **GAIA** | PolyForm Noncommercial (not OSI) | Yes — Deepgram STT + ElevenLabs TTS + LiveKit | Yes, plug-in servers | Closest full-stack match to Relay's ambition (proactive assistant, smart todos, cross-tool memory), but noncommercial license and a heavy stack (Next.js+FastAPI+LangGraph+Postgres+Mongo+Redis+RabbitMQ) block it as a base to fork — study the design, don't build on the license. |
| **Leon AI** | MIT, ~17.3k★ | Yes, new engines being added | Yes, documented MCP connection | Mid-transition 2.0 rewrite — same "rewrite in progress" caution as Logseq's DB migration in the earlier PKM survey. |
| **personal-assistant-kit** | MIT | No native voice | Yes — sits on Claude Desktop/Code/Kiro's MCP layer | Validates a **pattern, not a dependency**: "MCP client + scheduled prompts" needs near-zero custom code for trigger-word-style actions — fits the builder's automation strength directly. |
| **Omi** | MIT, ~13.2k★ | Yes, wearable + phone | Own integration framework, not MCP | Real open-source "voice memo → action items → memory" product, positioned against Granola/Limitless/Mem — but cloud-first backend (Deepgram/Pinecone/Firebase), so it's a **behavior/UX reference**, not a local-first dependency. |

## Previously-surveyed items (status confirmed, not re-researched)

Whispering (archived, folded into epicenter), Handy (~29.6k★, active), VoiceInk (active, v1.72 Mar 2026), espanso (14,018★, active, healthiest governance of anything surveyed across both passes), **Reor (archived Mar 2026 — several 2026 aggregator pages still wrongly call it "actively maintained," the same stale-marketing trap as Amurex)**, Khoj (self-host-only since cloud deprecation, still shipping betas). **OpenWhispr** (from the prior 10-project survey) remains the closest direct feature-level competitor — dictation + meeting transcription/diarization + an "AI agent" mode, hybrid local/cloud, MIT core + paid cloud tier.

## Cost-path findings

| Component | Free/local path | Cheap cloud path |
|---|---|---|
| STT | Whisper, local, free | Groq cheapest at scale (~$400 vs. OpenAI's $3,600 per 10K hrs/mo); OpenAI Whisper API ~$0.003–0.006/min |
| LLM | Ollama, $0 | GPT-4o-mini ($0.15/$0.60 per M tok), Gemini 2.5 Flash ($0.30/$2.50), Claude Haiku 4.5 (~$1/$5) — a handful of dollars/month at personal volume |
| TTS | Piper, free | ElevenLabs free tier only 10K chars/mo; Coqui XTTS v2 free but **non-commercial license only** |
| Vector store | LanceDB (embedded, validated by Reor and Mnemos already) | — |
| Cloud sync hosting | — | Supabase free tier (500MB DB, 1GB storage) — **auto-pauses after a week idle**, needs a keep-alive or accept wake latency |
| MCP servers (reuse, don't build) | `nspady/google-calendar-mcp` (Calendar), official `makenotion/notion-mcp-server` (Notion), `isaacphi/mcp-gdrive` or `piotr-agier/google-drive-mcp` (Drive) | All three of Relay's named integrations already have usable servers |

## Knowledge-graph-to-reduce-retrieval-cost: real prior art

**Microsoft GraphRAG** (full entity/relationship graph + community summaries) costs ~$33K to index a large corpus — expensive, overkill for a personal vault. **LightRAG** (HKUDS, EMNLP 2025) skips the expensive summarization step, does dual-level retrieval, updates incrementally, reports up to ~100x cheaper indexing while keeping multi-hop quality. Rule of thumb: graph-based RAG pays off above ~1K documents; below that, plain vector RAG wins on cost/complexity. **For an MVP-stage personal vault, ship plain LanceDB vector RAG first (matches Mnemos), treat a LightRAG-style graph as a v2 optimization once retrieval cost is a measured problem, not a day-one requirement.**

## Synthesis

**Copy**: Granola's bot-free local-audio-capture model (sidesteps the entire platform-bot arms race); Meetily's provider-abstraction pattern (Ollama/Claude/Groq/OpenRouter chosen at runtime); Vexa's decision to expose its own MCP server outward; personal-assistant-kit's scaffold-not-app "MCP client + scheduled prompts" pattern for trigger-word actions.

**Avoid**: any meeting-bot-joins-the-call architecture (live legal/platform risk — Fireflies' BIPA lawsuits, Teams/Zoom/Meet bot crackdowns); full GraphRAG on day one; trusting marketing/aggregator pages over actual repo state (Reor and Amurex both show this trap); non-OSI or noncommercial-licensed dependencies (GAIA) if Relay is ever shared or monetized.

**Real whitespace**: no surveyed project combines bot-free local capture, hybrid local/cloud LLM, **transcript-to-Kanban** (every meeting tool stops at a list, none produce an actual board), **voice-memo-to-structured-prompt** (distinct from generic voice-to-text cleanup), and direct trigger-word actions. This is a genuine, validated gap, not a marketing angle.

**Dependencies to reuse, not rebuild**: Meetily's pipeline code (MIT, directly borrowable), Vexa if bot-ingestion is ever added as a secondary connector, the three named MCP servers, and LanceDB as the vector store.

## My Take

The bot-vs-no-bot distinction turned out to be the load-bearing finding here, more than any feature comparison — Relay's push-to-talk design wasn't chosen for privacy reasons alone, it turns out to be a structural legal/platform-risk advantage over almost the entire commercial category. Combined with the fact that no one has actually shipped transcript-to-Kanban, that's a stronger differentiation story than I expected going in.

## Related

- [[Relay - Brief]]
- [[Relay - Implementation Options]]
- [[Git Repo Research Framework]]
