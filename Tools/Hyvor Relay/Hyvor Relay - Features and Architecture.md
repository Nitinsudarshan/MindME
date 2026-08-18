---
title: Hyvor Relay - Features and Architecture
aliases: []
tags: [tools, research, dev]
type: resource
status: growing
created: 2026-08-18
updated: 2026-08-18
related: ["[[Hyvor Relay - Brief]]", "[[n8n]]", "[[Hyvor Relay - Recommendation]]"]
source: https://github.com/hyvor/relay
---

# Hyvor Relay - Features and Architecture

## Summary

The full feature set and self-hosting requirements behind [[Hyvor Relay - Brief]] — deliberately close to what a commercial ESP offers, minus the per-message fee.

## Key features

- **Self-hosting**: Docker Compose (single server) or Docker Swarm (HA/scale); one self-contained image holds email workers, the bounce SMTP server, webhooks, and DNS.
- **Email API**: scope-based REST API for HTML/plain-text with attachments and custom headers. Defaults: 100 requests/min per API key, 10 sends/sec per project (429 on exceed); max 10 API keys/project, with IP restrictions supported.
- **SMTP submission**: port 587 (or 25) accepts messages and converts them into internal API calls — idempotency is not supported over SMTP.
- **Send states**: `queued` → `accepted` → possibly `bounced`/`complained`; hard bounces (5xx) auto-add to the suppression list.
- **Logs & SMTP conversations**: searchable delivery logs with headers, status, and full SMTP traces, retained 30 days.
- **Multi-tenancy & projects**: multiple tenants with scoped access; multiple isolated projects per tenant, each with its own domains/keys/webhooks.
- **Queues**: separate transactional and distributional queues to protect IP reputation; IPs are assigned per queue.
- **Greylisting & retries**: automatic handling, with configurable delayed retry.
- **Bounce/complaint/suppression handling**: automatic, via the incoming SMTP server.
- **DNS automation**: a built-in DNS server manages the instance domain and automates DKIM, SPF, PTR, MX, and TLS records via NS delegation.
- **Webhooks**: signed, tracked HTTP callbacks for deliveries, bounces, complaints, domain verifications.
- **Observability**: Prometheus metrics (port 9667, private/CGNAT only) + a pre-built Grafana dashboard; health checks across components; alerts for server issues, DNS errors, IP reputation drops.

## Technology stack

| Layer | Choice | Share (per repo language stats) |
|---|---|---|
| API backend | PHP + Symfony | 62.9% |
| Frontend | SvelteKit + Hyvor Design System | 22.6% |
| Workers (email/webhooks/DNS/SMTP) | Go, compiled to a single binary | 12.0% |
| — | TypeScript / JS / Dockerfile | 2.1% / 0.1% / 0.1% |
| Database + queue | PostgreSQL (only external dependency) | — |

An official JS/TS SDK exists at `hyvor/relay-js`.

## Self-hosting requirements

```mermaid
flowchart LR
    A[Rent server(s), static IPv4] --> B[Provide PostgreSQL]
    B --> C[Deploy via Docker Compose/Swarm, host network mode]
    C --> D[Point web-domain DNS at Relay's HTTP server]
    D --> E[Delegate NS for instance domain to Relay's DNS server]
```

- **Server**: min 1GB RAM/1 vCPU; 2GB/2 vCPU recommended for production. 4GB/2 vCPU can "easily send more than 1,000,000 emails per day" (~11.57/sec).
- **OS**: Linux, tested on Ubuntu 24.04 LTS in production.
- **IPs**: at least one static IPv4 (more IPs = more queues); **no IPv6 support for sending**, a deliberate choice since most providers don't reliably support inbound IPv6.
- **Ports**: 80/443 (API/web), 25 (incoming SMTP for bounces/complaints), 587 (SMTP submission), 53 (DNS), 9667 (Prometheus, private only).
- **Auth**: OIDC is mandatory — issuer URL, client ID/secret, callback at `/api/oidc/callback`. No built-in login system exists.
- **Setup**: download `deploy.tar.gz` from the latest release, edit `.env` (`APP_SECRET`, `POSTGRES_PASSWORD`, `WEB_URL`, `INSTANCE_DOMAIN`, OIDC vars), `docker compose up`. **`APP_SECRET` cannot be rotated yet** ("planned") — treat it as a one-time, unchangeable value at setup.
- Only host network mode is supported — no bridge/overlay networking.

## My Take

The self-containment is the most notable architectural choice here — one Docker image, one external dependency (Postgres), no RabbitMQ/MariaDB like Postal needs (see [[Hyvor Relay - Comparison]]). That's a meaningfully lower ops surface than most self-hosted MTAs, which matters directly for a solo operator's realistic maintenance budget — the same consideration that shaped the Windmill-over-heavier-alternatives call in [[Operon - Competitive Research]].

## Related

- [[Hyvor Relay - Brief]]
- [[n8n]]
- [[Hyvor Relay - Recommendation]]
