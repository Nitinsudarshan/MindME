---
title: Relay - Technology Stacks
aliases: []
tags: [app-ideas, relay, product]
type: resource
status: growing
created: 2026-08-17
updated: 2026-08-17
related: ["[[Relay - Implementation Options]]", "[[Relay - MVP and Recommendation]]", "[[Relay - Brief]]"]
source: 
---

# Relay - Technology Stacks

## Summary

Three candidate stacks, mapped to [[Relay - Implementation Options]]. Dimensions are chosen for what a voice/memory assistant actually needs, not forced into a generic template.

## Stack A — Meetily-forked core

| Layer | Choice | Why |
|---|---|---|
| Shell / frontend | Tauri (or Meetily's existing Next.js) | Matches target packaging; Meetily already ships this |
| Backend | Rust | Meetily's existing pipeline |
| STT | Parakeet / Whisper (local) | Already validated, fast |
| TTS | Piper (add on top — Meetily doesn't ship this) | Free, matches Mnemos precedent |
| LLM layer | Meetily's provider abstraction: Ollama / Claude / Groq / OpenRouter | Runtime-swappable, already built |
| Vector store | LanceDB | Validated by Reor, Mnemos, and this research |
| Memory format | Obsidian-style markdown + YAML | Consistent with the rest of this vault's philosophy |
| MCP integrations | `nspady/google-calendar-mcp`, `makenotion/notion-mcp-server`, `isaacphi/mcp-gdrive` | All reusable, none need building |
| Kanban/task output | New module (not in Meetily) — generate cards, push to a local board or Notion/Trello | The genuine whitespace feature |
| Database | SQLite / local files | Matches Meetily's existing approach |
| Auth | Not required for local-only MVP | |
| Deployment | Desktop app (Tauri/Meetily packaging) | |
| Monitoring | Local logs | |

## Stack B — Mnemos-native extension

| Layer | Choice | Why |
|---|---|---|
| Shell / frontend | Tauri + React (Mnemos's existing shell) | Direct reuse, zero new packaging work |
| Backend | Python / FastAPI (Mnemos's existing pattern) | Matches [[Python]]'s growing-skill trajectory directly |
| STT | Whisper (local, already integrated in Mnemos) | Reuse |
| TTS | Piper (already integrated in Mnemos) | Reuse |
| LLM layer | Ollama (local) with a hybrid toggle to a cheap cloud API | New: the hybrid layer Mnemos itself doesn't have |
| Vector store | LanceDB (already integrated in Mnemos) | Reuse |
| Memory format | Obsidian vault (already Mnemos's source of truth) | Reuse |
| MCP integrations | Same three community/official servers as Stack A | Reuse |
| Kanban/task output | New module | The differentiator feature |
| Database | LanceDB + markdown vault | Reuse |
| Auth | Not required for local-only MVP; Supabase Auth if cloud sync is enabled | |
| Deployment | Tauri desktop app (existing Mnemos build pipeline) | Reuse |
| Monitoring | Local logs, extend Mnemos's existing patterns | Reuse |

## Stack C — n8n-orchestrated, thin shell

| Layer | Choice | Why |
|---|---|---|
| Shell / frontend | Minimal Tauri/Electron capture widget | Only handles push-to-talk + on-screen toggle |
| Backend | n8n (self-hosted) | Matches [[n8n]], the single strongest existing skill |
| STT | Local Whisper in the thin shell, sent to n8n as text | Keeps raw audio local |
| TTS | Piper node or skip for v1 | Optional |
| LLM layer | n8n's LLM/AI nodes (Ollama or cloud) | Visual, fast to iterate |
| Vector store | Not required for MVP; add LanceDB later if retrieval becomes a need | Matches the "ship plain RAG later" finding in [[Relay - Competitive Research]] |
| Memory format | Markdown file writes via an n8n node | Simple, matches the vault philosophy |
| MCP integrations | n8n's own Notion/Google nodes, or the same MCP servers as Stacks A/B | Either path works |
| Kanban/task output | n8n workflow: LLM structuring → Notion/Trello API node | Visual, fastest to build given existing fluency |
| Database | n8n's own Postgres/SQLite | Reuse |
| Auth | n8n's own auth | Reuse |
| Deployment | Docker (n8n) + separately-packaged thin shell | Two-part deployment, a real packaging cost |
| Monitoring | n8n's built-in execution log viewer | Reuse |

## My Take

Stack B is the right target — it's the only one that keeps Relay as a single, cleanly packaged Tauri app while reusing real, already-working code rather than someone else's Rust codebase or a second running service (n8n) that complicates final Windows packaging. Stack A is worth a short spike specifically to benchmark Meetily's Rust/Parakeet transcription speed against a Python/Whisper equivalent before committing to Stack B's backend language. Stack C remains the fastest way to prototype the Kanban/trigger-word logic itself, independent of which stack it eventually gets ported into.

## Related

- [[Relay - Implementation Options]]
- [[Relay - MVP and Recommendation]]
- [[Relay - Brief]]
