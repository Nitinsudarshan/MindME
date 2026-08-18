---
title: Tools Comparison Kickoff Prompt (Template)
aliases: [Tools Comparison Prompt]
tags: [template, framework, research, tools]
type: resource
status: growing
created: 2026-08-18
updated: 2026-08-18
related: ["[[Tools Folder Research Kickoff Prompt (Template)]]", "[[Git Repo Research Framework]]", "[[Tools]]"]
source: 
---

# Tools Comparison Kickoff Prompt (Template)

Use this when you already have (or want) two or more tools researched and need them set side by side for a decision — as opposed to [[Tools Folder Research Kickoff Prompt (Template)]], which is for researching one tool on its own.

Fill in the `{bracketed}` fields, then paste this as your opening message.

---

I want a comparison across these tools, all solving the same problem: **{tool A}, {tool B}, {tool C, ...}**

**1. Why I'm comparing them**: {the decision this serves — e.g. "picking an execution backend for Operon" — or "no specific decision, just want the landscape clear"}

**2. Which already have research in `Tools/`**: {list any that do, or "check yourself against `Tools/Tools.md`"}

**3. Depth**: {quick triage table only / full comparison with verdicts and a recommendation}

**4. Dimensions to weight most, if any**: {e.g. "cost and self-hosting matter most to me" — or "use your judgment"}

---

### Instructions to follow

- Check `Tools/Tools.md` first. For any tool already researched there, reuse and link to its existing Brief note rather than re-researching it. For any tool not yet covered, research it fresh — following [[Tools Folder Research Kickoff Prompt (Template)]]'s methodology — and give it its own `Tools/<Tool Name>/` folder before comparing.
- Build the comparison itself using the Comparison Matrix approach in `Research-Framework/Git Repo Research Framework.md` (section 5) — one matrix, one row per tool, across whichever dimensions actually matter for this decision, not a fixed generic list.
- File the result under `Tools/Comparison/`, named for the comparison topic — e.g. `Tools/Comparison/{Category} Comparison.md`. This keeps every cross-tool comparison in one place, distinct from the individual tool folders. Use `type: moc`, since it links out to each tool's own Brief note rather than standing alone.
- Read `Rules/00 - Rules Index.md` first and apply the relevant rule notes — frontmatter, tagging, linking, note structure, Mermaid diagram standards — same as any other note.
- End with a clear verdict: which tool wins for the stated use case, and why — not a table left for the reader to interpret alone.
- Add the new comparison note to the index in `Tools/Tools.md`.
- Run `scripts/lint_vault.py` before calling it done.

## My Take

The reuse-don't-re-research step matters most here — a comparison prompt that re-derives a tool's metadata/features from scratch every time it's compared against something new will drift from its own Brief note over time. Pointing back at the existing `Tools/<Tool>/` folder keeps one tool's facts in one place, with the comparison note only adding the relative judgment on top.

## Related

- [[Tools Folder Research Kickoff Prompt (Template)]]
- [[Git Repo Research Framework]]
- [[Tools]]
