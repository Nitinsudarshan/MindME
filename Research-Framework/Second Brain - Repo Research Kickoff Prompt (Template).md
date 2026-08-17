I want you to do an extended survey/research on the following:

**1. Topic/niche:** Second Brain / Personal Knowledge Management (PKM) tools — repos and projects for capturing, linking, and retrieving personal notes/knowledge (e.g., Obsidian-style, Zettelkasten, note-linking, AI-augmented recall systems)

**2. Why I'm researching this:** Exploring this as a new personal productivity area — evaluating existing open-source/self-hostable options before deciding whether to adopt one, extend one, or build something custom.

**3. Scope:**

- Number of repos to survey: 6–8 (mix of established + newer/AI-native entrants)
- Known repos to include: Obsidian (if open-core parts exist), Logseq, AFFiNE, Anytype, Trilium, Foam, Athens Research, Dendron — plus any newer AI-native "second brain" projects (e.g., Reor, Khoj, self-hosted RAG-over-notes tools)
- Repos to explicitly exclude: pure note-taking apps with no linking/graph/knowledge-network capability (e.g., plain Notion clones without backlinks)
- Must-have constraints: must be open source or have an inspectable repo; prefer self-hostable/local-first; must have had a commit in the last 12 months; note format should ideally be portable (markdown/plain text preferred over proprietary DB lock-in)

**4. My existing stack/context (for fit-check):** Windows Dell G15 machine, comfortable with Next.js/Supabase/Node-based stacks, actively experimenting with local LLMs (Ollama) and agentic IDEs (Antigravity) via MCP — so extra interest in tools that support local-LLM/AI integration or MCP-style extensibility

**5. What I need at the end:**

- [x]  Per-repo one-pager (metadata + features + architecture + strengths/risks + verdict)
- [x]  Master comparison matrix (spreadsheet/table) across all repos
- [x]  A recommendation/shortlist with reasoning
- [ ]  Something else:

**6. Depth level:** Medium — feature + architecture, with source-code spot-checks where verdicts are close

---

### Instructions to follow (framework):

Use the repo research framework — for each repo, capture:

1. Basic metadata (link, last commit, license, maturity, maintainer/org, activity signals)
2. Feature list (linking/backlinks, graph view, tagging, plugin/extension system, AI features, sync mechanism, mobile support, data portability)
3. Architecture (local-first vs cloud, storage format — markdown/SQLite/custom DB, sync engine design, encryption, plugin architecture, dependency footprint)
4. Docs & community health (README quality, plugin ecosystem activity, Discord/forum vibrancy, response times)
5. Comparison matrix across all repos on: problem-fit, maturity vs innovation, local-first vs cloud-dependent, TCO, vendor/format lock-in risk, migration cost (getting notes out), learning curve, extensibility/plugin depth, AI/LLM integration readiness, community trajectory, license compatibility
6. Easy-to-miss checks: fork lineage, "is it just a wrapper" around another editor/engine, breaking format changes across versions, real production/daily-driver usage evidence (not just demo usage), abandonment signals, how "open" the open source actually is (open-core traps, paid sync as the only viable sync option)

Search the web/GitHub as needed rather than relying on memory alone — I want current activity data (last commit, release cadence, open issues) and current AI/LLM integration status, since this space is moving fast.

At the end, give me a clear verdict per repo: **adopt / evaluate further / reject**, with one-line reasoning, plus an overall recommendation for my use case — specifically noting which option(s) best support local-LLM/AI-augmented workflows given my existing Ollama/Antigravity setup.