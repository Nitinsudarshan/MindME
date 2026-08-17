---
title: APIs & Integrations
aliases: []
tags: [profile, skills, automation]
type: resource
status: growing
created: 2026-08-17
updated: 2026-08-17
related: ["[[Technical Skills & Technology Stack]]", "[[Automation & Workflow Engineering]]", "[[Web Application & Full-Stack Exposure]]"]
source: 
---

# APIs & Integrations

## Summary

This is the capability underneath all of my automation work — I understand systems as connected components rather than isolated applications. **Intermediate practical** level.

## Core concepts

APIs, REST concepts, webhooks, authentication concepts, request/response flows, data mapping, integration triggers, API-driven automation, system synchronization.

## Systems I've worked around

Supabase, Google Workspace, n8n, GitHub, Vercel, email, Amazon SES, internal applications, WhatsApp Business API, SMS systems.

```mermaid
flowchart LR
    N[n8n] <--> S[Supabase]
    N <--> G[Google Workspace]
    N <--> E[Email / SES]
    N -.-> W[WhatsApp Business API]
    N -.-> SMS[SMS providers]
    App[Web app] <--> S
    App <--> GH[GitHub / Vercel]
```

## My strength

I'm particularly good at asking: **"What system should own this data, and what event should cause another system to act on it?"** — that question is worth more at the systems level than knowing any individual API's syntax.

## My Take

APIs & Integrations is less a standalone skill and more the connective tissue between [[n8n]], [[Databases & Data Architecture]], and [[Web Application & Full-Stack Exposure]] — I don't think of it as "I know REST," I think of it as "I know which system should be the source of truth for this piece of data, and which event should notify the others."

## Related

- [[Automation & Workflow Engineering]]
- [[Web Application & Full-Stack Exposure]]
- [[Technical Skills & Technology Stack]]
