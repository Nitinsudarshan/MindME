---
title: Tools Folder Research Kickoff Prompt (Template)
aliases: [Tools Kickoff Prompt]
tags: [template, framework, research, tools]
type: resource
status: growing
created: 2026-08-18
updated: 2026-08-18
related: ["[[Git Repo Research Framework]]", "[[00 - Rules Index]]", "[[Tools]]"]
source: 
---

# Tools Folder Research Kickoff Prompt (Template)

A reusable kickoff prompt for researching one tool/product and filing it under `Tools/`, the way [[Hyvor Relay - Brief|the Hyvor Relay research]] was filed. Unlike [[Repo Research Kickoff Prompt (Template)]] (a broad multi-repo comparative survey), this is scoped to a single tool going into its own `Tools/<Tool Name>/` subfolder.

Fill in the `{bracketed}` fields, then paste this as your opening message.

---

I want you to research **{tool name}** and file the output under `Tools/{Tool Name}/`, following the same pattern as the existing tool folders there — see `Tools/Tools.md` for the index and an existing tool folder for the shape.

**1. What it is / why I'm looking at it**: {one line — e.g. "a self-hosted email API, evaluating as an AWS SES alternative"}

**2. Source material**: {"none — research from scratch" OR paste/attach existing research (an article, a screenshot, a writeup) for me to verify and structure}

**3. Depth**: {quick overview / full comparative deep-dive}

**4. Specific comparisons or angles to include, if any**: {e.g. "compare against X and Y specifically" — or "figure out the closest alternatives yourself"}

---

### Instructions to follow

- Use `Research-Framework/Git Repo Research Framework.md` as the research methodology (metadata, features, architecture, docs/community health, comparison matrix, easy-to-miss checks like abandonment signals and "is it just a wrapper").
- Read `Rules/00 - Rules Index.md` first, then apply every rule note it links to — folder placement, file naming, frontmatter, tagging, linking, note structure, and Mermaid diagram standards. Don't restate those rules here; read them from the source so this prompt doesn't drift out of sync with them.
- File the result under `Tools/{Tool Name}/`, split into atomic notes the way existing tool folders are — a Brief/MOC plus focused detail notes, sized to whatever the tool's actual content calls for, not a fixed count.
- Add the tool to the table in `Tools/Tools.md`.
- Link outward to genuinely related existing notes (a Profile skill note, another Tools entry, an App Ideas brief) — don't force a link that isn't real.
- If a new tag is needed, add it to `05-MOCs/Tag Index.md` in the same pass, per `Rules/04 - Tagging.md`.
- Run `scripts/lint_vault.py` against the new/changed files before calling it done, per `Rules/10 - Agent and AI Assistant Protocol.md`.

## My Take

The point of routing everything through `Rules/00` and `Git Repo Research Framework.md` instead of listing the schema/methodology inline here is that this prompt stays correct even after those files change — it's a pointer, not a copy. If the frontmatter schema or the research framework itself is ever revised, this template doesn't need a matching edit.

## Related

- [[Git Repo Research Framework]]
- [[00 - Rules Index]]
- [[Tools]]
