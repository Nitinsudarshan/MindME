---
title: Operon - MVP and Recommendation
aliases: [Operon Recommendation, Operon MVP]
tags: [app-ideas, operon, product]
type: resource
status: growing
created: 2026-08-17
updated: 2026-08-17
related: ["[[Operon - Technology Stacks]]", "[[Operon - Competitive Research]]", "[[Operon - Brief]]"]
source: 
---

# Operon - MVP and Recommendation

## MVP definition (~50–60% usability)

The user describes **one reasonably well-scoped process type** in plain English — the trigger→approval→notification shape already validated in the builder's own n8n/Apps Script work (Travel Desk, alumni workflows). Operon parses it into the IR, shows a readable plan for review/approval, generates a working Windmill script from it, deploys to a self-hosted Windmill instance, executes, and logs results to a simple dashboard.

```mermaid
flowchart LR
    A[Describe a process] --> B[Parse to IR]
    B --> C[Show readable plan for approval]
    C --> D[Generate Windmill script]
    D --> E[Validate]
    E --> F[Deploy + execute]
    F --> G[Record result]
```

## Tiers

| Tier | Scope |
|---|---|
| **MVP** | Single linear process type (trigger → step → step → notify), IR schema, parser/planner, plan-preview/approval UI, IR→Windmill compiler, validation pass, execution logging |
| **Post-MVP** | Branching/conditional steps (approval patterns), n8n export as an alternate target, a real monitoring dashboard with re-run capability, IR versioning/diffing |
| **Later** | RAG over past processes for pattern reuse, cost prediction, auto-generated process documentation, multi-user/team support, a template marketplace |
| **Experimental** | Process mining over Operon's own execution logs (PM4Py), heavyweight multi-agent "crew" planning for complex processes, Temporal migration for enterprise-grade durability, a hosted SaaS tier |

## Free / open source / paid matrix

| Component | Classification | Note |
|---|---|---|
| Windmill | Free, open source (self-hosted) | Dual AGPLv3/Apache-2.0 core |
| LangGraph | Free, open source | MIT |
| LLM | Free (Ollama, local) or optional paid (cheap API) | $0 possible, a few $/mo for quality |
| Supabase | Free tier | DB + Auth; watch the auto-pause-after-idle-week behavior |
| Deployment/hosting | Free (local) or free-tier VPS | Oracle Cloud Free Tier, Fly.io free tier |
| Monitoring | Free | Windmill's built-in logs + a simple table |

**The MVP can run at $0 recurring cost** using a fully local LLM, or a few dollars a month for better-quality cloud LLM calls at personal usage volume.

**What can be open sourced**: the parser/planner/IR-compiler layer — this is also where the real differentiation lives, so open-sourcing it is an adoption asset, not a giveaway. **What could stay proprietary later**: hosted execution at scale, team/enterprise features (RBAC, audit trails, marketplace) if a SaaS layer is ever pursued.

## USPs (5)

1. **Owns a small, versioned, LLM-legible workflow IR** rather than being a thin wrapper around n8n/Zapier/Make's JSON — survives any one competitor's API or license change, a real architectural moat rather than a UI difference.
2. **Validation-first execution model** — treats "does the generated workflow actually make sense before it runs" as a first-class MVP feature, directly targeting the exact reliability complaints (non-deterministic failures under production load) that plague the closest funded competitor, Lindy.ai.
3. **Code-first generation target** (Windmill/Python) instead of a visual canvas — matches how LLMs actually generate reliably, and gives a technical user an inspectable, git-diffable artifact instead of an opaque no-code blob.
4. **Genuinely self-hostable at $0 recurring cost** (Windmill + local LLM + free-tier Supabase) at a moment when the entire funded competitive set (Coworker.ai, Lindy.ai, Gumloop, Relevance AI) is closed-source, SaaS-only, and credit-metered.
5. **Built around the builder's strongest actual skill** — translating an ambiguous business process into a structured system design (see [[Product & Systems Design]]) — rather than being a generic AI wrapper optimized for a demo.

## Final Recommendation

**What Operon should be**: a narrow, code-generating process-to-automation compiler — not a general visual workflow builder, not an autonomous digital-coworker agent, not a process-mining platform, not an enterprise iPaaS replacement.

**Who it should initially serve**: the builder themselves and similarly-scoped solo operators/small teams who already run manual or semi-automated business processes (forms, approvals, notifications) and want them turned into real, inspectable automations without adopting an enterprise platform.

**Core problem**: turning an ambiguous, plain-English process description into a working, validated, deployed automation — reliably, not just plausibly.

**Core workflow**: describe → parse to IR → plan/approve → generate → validate → deploy → execute → record (see the MVP diagram above).

**Recommended architecture**: own the IR; compile it to Windmill as the primary execution target; validate before every execution; treat n8n export and Temporal-grade durability as later upgrades, not MVP dependencies.

**Recommended stack**: Stack A from [[Operon - Technology Stacks]] — Next.js + FastAPI/Python + LangGraph + Windmill + Supabase.

**Recommended MVP**: the single-process-type loop defined above, validated against the builder's own real historical automations as acceptance tests.

**What to build**: the IR schema, the parser/planner, the plan-preview/approval UI, the IR→Windmill compiler, the validation pass, execution logging.

**What to reuse**: Windmill itself, LangGraph, Supabase, and — per [[Operon - Competitive Research]] — don't rebuild an execution engine, agent orchestration framework, or database layer from scratch.

**What NOT to build**: a visual workflow canvas (n8n/Windmill/Activepieces already solved this), autonomous multi-app agent behavior (Coworker.ai/Lindy.ai's crowded, complaint-prone lane), process mining infrastructure (no data to mine pre-launch), enterprise SSO/RBAC/marketplace (premature before there's a single real user beyond the builder).

**Open-source strategy**: open the parser/IR/compiler core (MIT/Apache-2.0); keep any future hosted-execution-at-scale or team/enterprise layer proprietary, mirroring n8n's and AFFiNE's open-core split.

**Biggest technical risks**: LLM reliability/hallucination in generating correct IRs from ambiguous natural language (the validation pass is what has to catch this, not an afterthought); Windmill being a fast-moving young project whose API/schema may shift; scope creep into full agent autonomy (the exact trap Lindy.ai's reviews warn against).

**Biggest product risks**: a crowded, well-funded competitive set (Coworker.ai's $16.5M, Lindy.ai, and n8n/Zapier/Make's own native AI builders) — differentiation has to stay sharp on "owns the IR + validation-first + self-hostable," not drift into "yet another wrapper"; solo-builder bandwidth against a genuinely broad problem space.

**Competitive differentiation**: see the USPs above — the throughline is owning the intermediate representation and taking validation seriously as a first-class feature, in a market where every funded competitor has picked either "visual builder" (n8n/Zapier/Make/Activepieces) or "autonomous agent" (Coworker.ai/Lindy.ai) and left "validated, inspectable, code-first automation compiler" open.

### First 10 development milestones

1. Define the workflow IR/spec schema (actors, triggers, steps, decisions, data contracts) as a versioned JSON/YAML schema.
2. Build the NL → IR parser (LangGraph + structured-output LLM calls), tested against 5–10 hand-written example processes reusing the builder's own real automations (Travel Desk, alumni workflows) as test cases.
3. Build a human-readable "plan preview" renderer (IR → readable summary) for user review/approval before generation.
4. Build the IR → Windmill script/flow compiler for a single narrow pattern: linear trigger → step → step → notify, no branches yet.
5. Stand up a self-hosted Windmill instance (Docker) and wire up deployment of generated flows via its API.
6. Add a validation pass — schema check plus an LLM self-critique step — before deployment, with clear error surfacing back to the user.
7. Add execution logging: capture Windmill run results into a Supabase table, surfaced in a minimal dashboard.
8. Expand the IR/compiler to support one branch type (approval/conditional step) — the single most common pattern in the builder's own automation history.
9. Dogfood: rebuild one of the builder's own real existing automations (a simplified Travel-Desk-style approval flow) end-to-end through Operon as the MVP acceptance test.
10. Build the process-documentation auto-generator (IR → readable Markdown doc) as the first genuine post-MVP differentiator, then decide — based on real usage — whether n8n export or multi-step branching is the next priority.

## My Take

The milestone list above is deliberately grounded in automations the builder has already actually built by hand (Travel Desk, alumni workflows) — using those as the acceptance test means Operon's first real success criterion is "can it reproduce something I know works," not "does it look impressive in a demo." That's the more honest bar, and it's the one worth holding to before any of the Later/Experimental tier gets touched.

## Related

- [[Operon - Technology Stacks]]
- [[Operon - Competitive Research]]
- [[Operon - Brief]]
