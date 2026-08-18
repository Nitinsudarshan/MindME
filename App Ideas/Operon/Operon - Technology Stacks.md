---
title: Operon - Technology Stacks
aliases: []
tags: [app-ideas, operon, product]
type: resource
status: growing
created: 2026-08-17
updated: 2026-08-17
related: ["[[Operon - Implementation Options]]", "[[Operon - MVP and Recommendation]]", "[[Operon - Brief]]"]
source: 
---

# Operon - Technology Stacks

## Summary

Three candidate stacks, mapped to [[Operon - Implementation Options]]. Components are marked N/A where the research concluded they're unnecessary for an MVP — not every row needs an entry.

## Stack A — Windmill-centric (recommended)

| Layer | Choice | Why |
|---|---|---|
| Frontend | Next.js + Tailwind | Already a known skill (see [[Web Application & Full-Stack Exposure]]) |
| Backend | Python / FastAPI | Growing skill, and the natural home for the LangGraph planner |
| AI/LLM layer | Ollama (local, $0) or a cheap API (GPT-4o-mini/Gemini Flash) | Matches Mnemos's existing local-first pattern; cheap fallback for quality |
| Agent orchestration | LangGraph | Most credible production-adopted foundation found in research (Klarna, Replit, Elastic cited) |
| Workflow engine | Windmill (self-hosted) | Code-first, matches how an LLM actually generates reliably; dual-licensed open core |
| Database | Supabase / Postgres (free tier) | Already a known tool ([[Databases & Data Architecture]]) |
| Vector search | Not required for MVP | RAG over past processes is a "useful later" capability per research |
| Knowledge graph | Not required for MVP | Same reasoning — no corpus to search yet |
| RAG | Deferred | Add once there's a real corpus of past processes/executions |
| Process graph | The IR itself (custom, versioned JSON/YAML schema) | This is the actual owned asset — not a third-party format |
| Code generation | IR → Windmill Python/TS script | The compiler step |
| APIs | Windmill REST API for deployment; target-app APIs the generated workflow calls | |
| Auth | Supabase Auth (free tier) | |
| Deployment | Docker Compose, local machine or free-tier VPS | |
| Monitoring | Windmill's built-in execution logs + a simple Postgres audit table | |
| Desktop/web | Web app (Next.js); no desktop packaging needed for MVP | |

## Stack B — n8n-leverage

| Layer | Choice | Why |
|---|---|---|
| Frontend | Minimal Next.js UI, or a chat interface embedded in n8n | Fastest path, reuses existing n8n familiarity |
| Backend | Python / FastAPI microservice for the planner | Same as Stack A |
| AI/LLM layer | Same as Stack A | |
| Agent orchestration | LangGraph, or simpler structured-output calls | n8n handles execution, so orchestration needs are lighter |
| Workflow engine | n8n (self-hosted) | Deep existing skill match ([[n8n]]) |
| Database | n8n's own Postgres + a small Supabase table for IR history | |
| Vector search / Knowledge graph / RAG | Not required for MVP | Same reasoning as Stack A |
| Process graph | The IR (custom schema) | Same principle — don't skip owning this even when targeting n8n |
| Code generation | IR → n8n workflow JSON | |
| APIs | n8n REST API for workflow creation/import | |
| Auth | n8n's own auth, or Supabase Auth for the planner UI | |
| Deployment | Docker, same free-tier options | |
| Monitoring | n8n's built-in execution log viewer | |
| Desktop/web | Web app | |

## Stack C — Minimal CLI (zero infra)

| Layer | Choice | Why |
|---|---|---|
| Frontend | None, or a simple Streamlit/Textual interface | Fast to build, low priority for a proof-of-concept |
| Backend | Python script/CLI | Directly matches the learning goal in [[Python]] |
| AI/LLM layer | Ollama or a direct LLM API call with structured output (Pydantic) | No orchestration framework needed yet |
| Agent orchestration | Not required | A single parse step, no multi-stage state machine yet |
| Workflow engine | None | Generated scripts run via cron/Task Scheduler |
| Database | SQLite, flat files, or the Obsidian vault itself | Zero setup, synergy with the existing MindME/Mnemos approach |
| Vector search / Knowledge graph / RAG | Not required | |
| Process graph | The IR, stored as plain YAML/JSON | |
| Code generation | IR → standalone Python script | |
| APIs | Whatever the generated script calls directly | |
| Auth | Not required (local, single-user) | |
| Deployment | None — a local CLI | |
| Monitoring | Manual / simple log file | |
| Desktop/web | CLI now; optional Tauri wrapper later | |

## My Take

Stack A is the one to actually build toward — it's the only one of the three whose components (Windmill, LangGraph, Supabase) all map onto capabilities the research validated as real and durable, rather than betting on a competitor's schema. Stack C is worth building first as a throwaway proof-of-concept regardless of which stack wins, since it validates the riskiest assumption (can the parser reliably produce a correct IR) before any infrastructure investment.

## Related

- [[Operon - Implementation Options]]
- [[Operon - MVP and Recommendation]]
- [[Operon - Brief]]
