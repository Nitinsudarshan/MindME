---
title: Hyvor Relay - Licensing and Maturity
aliases: []
tags: [tools, research]
type: resource
status: growing
created: 2026-08-18
updated: 2026-08-18
related: ["[[Hyvor Relay - Comparison]]", "[[Hyvor Relay - Recommendation]]", "[[Hyvor Relay - Brief]]"]
source: https://github.com/hyvor/relay
---

# Hyvor Relay - Licensing and Maturity

## License (AGPL-3.0) and what it means

- Self-hosting is free, no license purchase required, as long as you comply with AGPLv3.
- The AGPL's network clause: if you modify Relay and serve the modified version over a network, you must release your modified source under AGPLv3. Using it unmodified via its API/UI does **not** require open-sourcing your own application.
- HYVOR offers an enterprise license (from **€10,000/year**, per relay.hyvor.com's pricing page — the central hyvor.com/enterprise page carries no figure and routes to a contact form) for organizations needing non-copyleft terms, legal clarity, or priority support/SLAs.
- **Feature parity is identical between AGPL and enterprise** — per HYVOR: *"both the AGPL and Enterprise versions of Hyvor Relay include the same set of features. The only difference is the licensing terms and the support options available."* No functionality is paywalled — a real departure from typical open-core dual-licensing.
- Trademarks: "HYVOR name and logo are trademarks of HYVOR, SARL."

## Maturity and activity

```mermaid
flowchart LR
    A[Sep 16, 2025: beta testers recruited] --> B[Dec 1, 2025: public introduction, AGPLv3]
    B --> C[63 releases]
    C --> D[Jun 4, 2026: v0.0.45]
    D -.->|planned| E[Q1 2026: Cloud public launch]
```

- **Versioning**: still 0.0.x (latest 0.0.45) — the maintainers still consider it pre-1.0.
- **Repo stats** (mid-2026 snapshots, trending upward): ~620–710 stars, ~34–37 forks, ~320 commits, 3 watchers, ~48–51 open issues.
- **Contributors**: a small core team — @Nolab0, @supun-io (HYVOR co-founder Supun Wimalasena), @sakithb are the most active in release notes, roughly 3 primary contributors. **This is a real key-person/small-team risk.**
- **Development activity**: high commit cadence, frequent releases; recent work includes SMTP sending, delayed retry, API-key IP restrictions, telemetry removal, and bounce-state bug fixes — active, responsive maintenance.
- **Roadmap — planned**: incoming email routing, dedicated IPs for users, custom DKIM selectors.
- **Roadmap — explicitly not planned**: built-in auth (OIDC only, by design), open/click tracking, email templates.
- **Cloud**: a managed instance (relay.hyvor.com) is in private beta, public launch planned Q1 2026, estimated pricing ~€30/month for 300,000 emails (+€1 per additional 10,000) — HYVOR explicitly labels this "estimated" and subject to change at launch.

## Known limitations and criticisms

- **IPv4-only** — no IPv6 support for sending (or currently at all), confirmed by the maintainer; blocks IPv6-only deployments.
- **Docker-only** — no non-Docker install path; the maintainer said they "haven't looked into other options so far."
- **Deliverability is still on you** — the single most important caveat, and true of *any* self-hosted email software, not just Relay: fresh VPS IPs start with zero (or negative) reputation, most residential ISPs block port 25, and warming/monitoring/blocklist remediation is ongoing manual work. HYVOR itself acknowledges deliverability "also depends on factors such as email content, recipient engagement, domain age and reputation… which are outside the scope of any email sending service."
- **Early-stage risk** — 0.0.x versioning, small contributor base, no key rotation yet (`APP_SECRET` is fixed at setup).
- **Mandatory OIDC** — an extra setup dependency versus a built-in login.
- **No independent reviews yet** — AlternativeTo lists "No reviews … 0 comments"; most third-party coverage so far is launch coverage or marketing-adjacent (one hands-on article reads as promotional). Independent, critical, production reviews are scarce given the product's youth.

## Documentation quality

Documentation is a genuine strength, cleanly split by audience: **Product Docs** (getting started, API/SMTP sending, Console API reference, domains/DKIM), **Self-Hosting Docs** (architecture diagram, easy/production deploy, scaling math, monitoring), and repo-level docs (README, ROADMAP.md, CONTRIBUTING.md, DEV.md, AGENTS.md), plus a Docker Hub image and a community forum/Discord. The docs are praised for teaching underlying SMTP/deliverability concepts, not just product mechanics — gaps are the lack of non-Docker guidance and some pricing/licensing details living on relay.hyvor.com rather than the central hyvor.com/enterprise page.

## My Take

The "feature-identical AGPL vs. enterprise" licensing stance is worth remembering independent of whether Relay itself gets adopted — it's a cleaner model than the open-core pattern seen across [[Operon - Competitive Research]]'s survey (n8n's Sustainable Use License, Onyx's EE gating), and worth considering if [[Operon - Brief]] ever reaches its own open-source-vs-proprietary decision.

## Related

- [[Hyvor Relay - Comparison]]
- [[Hyvor Relay - Recommendation]]
- [[Hyvor Relay - Brief]]
