---
title: Hyvor Relay - Comparison
aliases: []
tags: [tools, research]
type: resource
status: growing
created: 2026-08-18
updated: 2026-08-18
related: ["[[Hyvor Relay - Brief]]", "[[AWS & Amazon SES]]", "[[Hyvor Relay - Licensing and Maturity]]"]
source: https://github.com/hyvor/relay
---

# Hyvor Relay - Comparison

## Summary

Cost model is the core differentiator: commercial ESPs charge per message; Relay charges nothing in software fees (AGPL) — you pay only for a VPS plus your own ops time. This note lays out that trade against SES/SendGrid/Mailgun and against Postal, the closest self-hosted peer.

## Cost comparison at ~1M emails/month

| Provider | Cost at ~1M/month | Notes |
|---|---|---|
| **AWS SES** | ~$107.70/mo (shared IP) → ~$182.55/mo (dedicated IP) | $0.10/1,000 emails + ~$7.20 data transfer; dedicated IPs $24.95/IP/mo standard or $15/account/mo managed + volume fees; new accounts (Jul 2025+) get $200 credit then standard rates |
| **SendGrid** | ~$399.95/mo (estimated) | Essentials: $19.95/mo up to 50k, then $34.95/mo; Pro (~$89.95/mo) adds dedicated IPs — roughly 89% more expensive than SES at 100k/month |
| **Mailgun** | ~$400–800/mo (estimated) | Developer-focused, tiered, custom pricing at high volume |
| **Hyvor Relay** | ~$20–50/mo (VPS only) | $0 software (AGPL); savings compound at higher volume, but deliverability/reputation management is entirely on you |

**Rule of thumb from self-hosting guides**: self-hosting outbound email starts clearly winning on cost above ~50,000 messages/month, rarely below ~25,000 — below ~50k/month the engineering time usually outweighs the savings.

```mermaid
quadrantChart
    title Cost vs. operational ownership
    x-axis Low ops burden --> High ops burden
    y-axis Low cost at scale --> High cost at scale
    quadrant-1 Managed, expensive
    quadrant-2 Self-hosted, expensive (rare)
    quadrant-3 Managed, cheap at low volume
    quadrant-4 Self-hosted, cheap at scale
    AWS SES: [0.3, 0.55]
    SendGrid: [0.25, 0.8]
    Mailgun: [0.3, 0.75]
    Hyvor Relay: [0.7, 0.15]
    Postal: [0.85, 0.1]
```

## Vs. Postal (closest self-hosted peer)

| Dimension | Hyvor Relay | Postal |
|---|---|---|
| License | AGPL-3.0 | MIT |
| Language | PHP + Go + Svelte | Ruby |
| Created | 2025 (public Dec 2025) | Apr 2017 |
| Stars/Forks | ~620–710 / ~34–37 | ~16.6–16.7k / ~1.2k |
| Contributors | ~3 | 51 |
| Dependencies | PostgreSQL only | MariaDB/MySQL + RabbitMQ (typically ≥4GB RAM) |
| Extras | Built-in DNS server, automatic IP config, health checks, Prometheus/Grafana | Inbound routing to webhooks, years of production hardening |

Both handle outbound transactional/bulk sending, SMTP + HTTP APIs, multi-org/tenant, queues, DKIM, bounce handling, and webhooks. Postal is far more battle-tested with a much larger community; Relay is lighter on dependencies and more automation-focused out of the box.

## Vs. other adjacent tools

- **useSend / Plunk** — open-source dashboards/APIs that wrap AWS SES; they still depend on SES for delivery and reputation, so they don't remove the underlying deliverability responsibility.
- **Postfix / Haraka / Exim / OpenSMTPD** — lower-level MTAs with no API/console/multi-tenant layer.
- **Mailcow / Mailu / iRedMail / WildDuck / Stalwart** — mailbox servers (IMAP/POP3), a different category entirely (human mailboxes, not app-sending APIs).

## Net assessment

Relay's advantages: data sovereignty/privacy (no tracking, logs stay on your own Postgres), predictable cost at scale, modern developer experience, minimal dependencies, strong automation. Its disadvantages vs. commercial ESPs: you inherit deliverability/reputation risk and operational burden, with no managed support unless you buy enterprise. Vs. Postal: far less battle-tested, tiny community.

## My Take

The direct, checkable link to my own experience is the SES comparison — [[AWS & Amazon SES]] documents working through the economics of roughly 45,000 emails/month, which sits right at the edge of the ~25k–50k breakeven band this research surfaces. That's not a coincidence worth ignoring: if that volume grows past 50k/month, Relay (or Postal) becomes a genuine reconsideration, not just a curiosity.

## Related

- [[Hyvor Relay - Brief]]
- [[AWS & Amazon SES]]
- [[Hyvor Relay - Licensing and Maturity]]
