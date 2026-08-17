
Fill in the {bracketed} fields, then paste this as your opening message.

---

I want you to do an extended survey/research on the following:

**1. Topic/niche:** { ________________________}

**2. Why I'm researching this:** {e.g., evaluating for adoption, looking for architecture inspiration, deciding build-vs-buy, competitive scan, etc.}

**3. Scope:**

- Number of repos to survey: {10}
- Known repos to include (if any): {list, or "none — please discover them"}
- Repos/tools to explicitly exclude: {if any}
- Must-have constraints: {e.g., must be open source, must self-host, must support Postgres/Supabase, must have had a commit in last 12 months, license must allow commercial use, etc.}

**4. My existing stack/context (for fit-check):** {e.g., Next.js + Supabase + Vercel, Windows dev machine, small team, no dedicated DevOps}

**5. What I need at the end:**

- [ ] Per-repo one-pager (metadata + features + architecture + strengths/risks + verdict)
- [ ] Master comparison matrix (spreadsheet/table) across all repos
- [ ] A recommendation / shortlist with reasoning
- [ ] Something else: {specify}

**6. Depth level:** {quick triage scan / medium — feature+architecture / deep — including reading source code and testing where feasible}

---

### Instructions to follow (framework):

Use the repo research framework we built earlier — for each repo, capture:

1. Basic metadata (link, last commit, license, maturity, maintainer/org, activity signals)
2. Feature list (core functionality, config surface, extensibility, integrations, data model)
3. Architecture (stack, deployment model, scalability approach, security posture, dependency footprint)
4. Docs & community health (README quality, response times, governance)
5. Comparison matrix across all repos on: problem-fit, maturity vs innovation, self-host vs SaaS, TCO, vendor lock-in, migration cost, learning curve, extensibility, security/compliance, community trajectory, stack fit, license compatibility
6. Easy-to-miss checks: fork lineage, "is it just a wrapper," breaking-change history, real production usage evidence, abandonment signals, test coverage, roadmap clarity

Search the web/GitHub as needed rather than relying on memory alone — I want current activity data (last commit, open issues, recent releases), not stale info.

At the end, give me a clear verdict per repo: **adopt / evaluate further / reject**, with one-line reasoning, plus an overall recommendation for my use case.