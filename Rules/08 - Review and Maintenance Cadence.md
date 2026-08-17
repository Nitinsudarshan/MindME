---
title: Review and Maintenance Cadence
aliases: [Vault Maintenance, Review Cadence]
tags: [rules, review, maintenance]
type: resource
status: evergreen
created: 2026-08-17
updated: 2026-08-17
related: ["[[00 - Rules Index]]", "[[05 - Linking and Graph Discipline]]", "[[04 - Tagging]]"]
source: 
---

# Review and Maintenance Cadence

Rules 01–07 keep a note correct *at the moment it's committed*. This note is about what keeps the vault correct *over time* — without a review cadence, `00-Inbox/` becomes a graveyard and every tag from [[04 - Tagging]] slowly drifts.

---

## 1. Weekly — Inbox pass

- Process every note in `00-Inbox/`: give it real frontmatter (see [[03 - Frontmatter and Metadata]]), the right `type`, and move or link it into its real home.
- Nothing lives in `00-Inbox/` for more than a week unprocessed.

## 2. Monthly — structural audit

- **Orphan sweep**: any note with no links in or out (see [[05 - Linking and Graph Discipline]]) either gets linked from somewhere real or moved to an archive state.
- **Status promotion**: `seedling → growing → evergreen` for notes that have held up on rereading — see [[03 - Frontmatter and Metadata]] for the enum.
- **Tag audit**: check `05-MOCs/Tag Index.md` against actual tag usage; merge near-duplicates with Tag Wrangler (see [[09 - Plugin Stack]]) rather than letting variants coexist.
- **Global graph view pass**: this is the one time global graph (rather than local graph) is the right tool — look for unexpected disconnected clusters.

## 3. As-needed — MOC upkeep

Whenever a topic folder or tag cluster grows past a handful of notes without a hub, that's the trigger to create a MOC (see [[05 - Linking and Graph Discipline]] §2), not a fixed schedule.

## 4. Dataview-powered review queries

Since every note carries `type` and `status` in frontmatter, review passes can be driven by query instead of manual scanning, e.g. "all `fleeting` notes older than 7 days" for the weekly Inbox pass, or "all `seedling` notes untouched for 30+ days" for the monthly audit.
