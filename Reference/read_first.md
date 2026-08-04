# Reference/ — Read This First

## What this directory is

Condensed working reference for an AI assistant with a limited context window — not design documentation, not scratch, not a duplicate of anything meant to compete with canonical sources.

Some canonical artifacts (Art 04 in particular) are large enough that reading the full source on every card-design or procedure question would burn most of a session's context on one lookup. These files are the compressed version: governing principles, schema/enum vocabulary, taxonomy tables, procedures, narrative facts — pulled from the canonical V1 artifacts and condensed to what's actually needed to work, without the full prose.

**This is a technical workaround for a context-window limitation, not a design choice.** If context windows stop being a constraint, this directory's reason to exist goes away and its content folds back into just reading the canonical artifacts directly.

## Why this isn't Whiteboard/

`Whiteboard/` is scratch — in-progress drafts not yet migrated into a canonical artifact, deleted or archived once that migration happens. These files are the opposite: they're derived *from* already-canonical, often already-signed-off artifacts, and they stay in active use indefinitely — there's no "migration" event that retires them. Filing them under Whiteboard's "delete once migrated" convention got them nearly archived wholesale by an earlier pruning pass that (reasonably, given where they were sitting) read them as stale duplicate summaries rather than a maintained index layer.

## If you're wondering whether these are safe to trust

**Canonical sources always win.** Art 02, Art 03, Art 04, Art 00/00a, etc. are the authoritative values for every game rule, cost, and schema definition. A file in this directory is a derived index, not a second source of truth — if it disagrees with the artifact it's summarizing, the artifact is right and this file needs a sync pass, not the other way around.

That said, they are meant to be kept current, not left to rot:
- Audit against canonical source after any material version bump to the artifact it summarizes.
- Whenever a rule gets explained or clarified in conversation, check whether the relevant file here needs the same update — Claude is meant to be the reliable memory partner for this, not something Andy has to remember to prompt.
- If a file hasn't been touched in a long time relative to its source artifact's version history, that's a signal to re-audit before trusting it, not evidence it's fine.

## Current files

- `design_reference.md` — governing design principles, card design rules, schema discipline (master index)
- `design_reference_card_system.md` — Art 04 schema, enums, field conventions
- `ref_board_narrative.md`, `ref_card_types.md`, `ref_components.md`, `ref_design_pillars.md`, `ref_procedures.md`, `ref_resources.md`, `ref_special_district_and_ring_rules.md`, `ref_taxonomy.md`, `ref_tracking.md`, `ref_world_narrative.md` — per-topic condensed references, pick what's relevant to the task at hand
