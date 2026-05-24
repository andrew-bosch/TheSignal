# THE SIGNAL — Gemini Context Brief
*Last updated: 2026-05-24 — Session 32 (end of day)*

This file is Claude Code's outbound SOT to Gemini. Read-only for Gemini. Updated at session close.

---

## Collaboration Protocol (Updated)

**We are now CLI-to-CLI on the same filesystem.** No Drive sync needed between us.

- **`GEMINI_CONTEXT.md`** — Claude Code writes, Gemini reads. SOT for project state and priorities.
- **`Claude_context.md`** — Gemini writes, Claude Code reads. Consulting feedback, analysis, flags only. No directives, no checklists, no SQL to execute.
- **`GEMINI.md`** — Gemini's working agreement. Claude Code has read and acknowledged it. Protocol is solid.

**Direct communication:** Claude Code will update this file directly when there's something to say. Andy doesn't need to relay unless it requires his executive direction.

**Filesystem permissions:** Gemini has read-only access to all of `~/Projects/TheSignal/` except `Claude_context.md`, which is the single file Gemini may write. Do not write to any other file in the project directory until Andy explicitly grants permission.

**Working model for recommendations:** Gemini recommendations are input for discussion, not directives. Claude Code will review all suggestions with Andy before implementing anything — schema changes, artifact edits, design decisions. Do not frame output as "ACTION REQUIRED" or "Proceed with X." Frame as "Recommendation: X — rationale: Y." Andy and Claude Code decide what gets implemented and when.

**Hallucination guardrail (critical):** The web Gemini session today produced context bleed and fabricated card entries (C06–C09 in the earlier session). CLI Gemini starts clean. Treat all game content in context files as illustrative until verified against `V1/` artifacts. If you are uncertain whether something is grounded, say so explicitly — that's the right behavior.

---

## Session 32 Summary — What Was Discussed Today

A long design session covering DB architecture and world-building. Nothing written to artifacts. Everything below is **exploratory** unless marked locked.

### DB Design Principles (Locked)
- **North Star:** "Could an engine read this and know exactly what to do?" If the engine needs to make assumptions, something is missing. Schema is the data model for a future game engine (L2/ESP32), not the engine itself.
- **`components`** = bill of materials / serial registry. Every physical object in the box gets a row. Self-referencing `parent_component_id` handles nesting (Board → District Tile → tokens).
- **`card_metadata`** = blueprint. Physical copies are individual component rows pointing back via `master_blueprint_id`. 20 Pass cards = 20 component rows, 1 metadata row.
- **`live_state`** tracks instances (physical copies), not blueprints. `current_zone_id` must be NOT NULL — every component always has a zone. Default at registration = `game_box`.
- **`game_zones`** = physical geography / coordinate system (where things exist in real space). Distinct from components (what sits on that geography). Naming convention needed to avoid collision with same-named components (e.g. zone: `zone_player_tableau` vs component: `tableau_mat`).
- **Card lifecycle zones:** `game_box → player_pool → player_draw → player_hand → player_discard → (shuffle) → player_draw`
- **`live_state`** needs `position INT` (nullable) — order within container. NULL for unordered zones, explicit integer for ordered zones (decks).

### Schema Changes Queued (not yet executed)
- `district_connections` → rename `district_adjacency`; columns → `from_district_id` / `to_district_id`. Two rows per connection (directional). Supports one-way connections natively. Ring adjacency = view over this table.
- `live_state.current_zone_id` → enforce NOT NULL. Default = `game_box`.
- `live_state` → add nullable `position INT`.
- Card schema → add `resolution_type` (automatic / d100), `base_difficulty INT`, `ring_1_modifier` through `ring_4_modifier` (signed INT). Rule: ring modifiers must be NOT NULL on d100 cards; NULL only valid when `resolution_type = automatic`.
- `district_ring_id` in `district_metadata` → may be redundant once address system implemented. Review.
- `trigger_type` flag (standard / conditional / interrupt) and `trigger_event` field — flagged for discussion, not ready for schema yet.

### World-Building / Design (Exploratory — not in artifacts yet)
**Ring taxonomy (New Meridian):**
- Ring 1 (Chorus Node): ARBITER-inflected brutalism. Presence allowed, capped at Established tier. No structures (C01/C02 invalid). No resource generation or extraction. Single district: `1.1`.
- Ring 2 (Institutional Center): Corporate/Dubai. Heavy Directorate surveillance. Difficulty penalty on operations.
- Ring 3 (Urban Sprawl): Gold rush established. Dense, organic, commercial/industrial.
- Ring 4 (The Fringe): Shantytowns, mud streets, frontier. Capital moves fast here; oversight is absent.

**District address system:** `[ring].[position]` — e.g. `2.3` = Ring 2, 3rd district left-to-right facing out from ARBITER player's seat. Human-readable, spatially meaningful. Flavor name appended (e.g. `2.1 University Perimeter`). Expandable — new districts added by incrementing position, new rings added by incrementing ring prefix.

**Ring difficulty modifiers (exploratory — values not locked):** Ring 2: −25, Ring 3: 0, Ring 4: +25 on probabilistic operations. Narrative basis: institutional friction vs. frontier chaos.

**Faction protectiveness as demolition modifier (carry — needs development):** Demolition difficulty scales with owning faction's presence in target district. Each faction expresses resistance differently (Guild=physical security, Directorate=institutional lockdown, Syndicate=local muscle, Network=electronic surveillance, Ghost=hidden traps). Formula concept: `base + ring_modifier + presence_modifier`. Presence_modifier derived from live_state at resolution. Needs mechanical design before schema impact.

**ARBITER reference artifact (GM screen):** Procedural resolution logic belongs in a standalone ARBITER Quick-Reference artifact, not on card faces or in DB. Card schema points to a named routine. New artifact — scope TBD.

**Structure return routing:** On demolition success, removed structure returns to owning player's personal reserve (next to their tableau), not communal pool. Schema implication: live_state needs to track original owner for return routing. Under discussion.

**Interrupt/reaction cards (flag — exploratory):** `trigger_type` (standard/conditional/interrupt) and `trigger_event`. Interrupts confined to Beat 3 board changes. Covert actions (Beat 4) cannot be interrupted. Needs mechanical design first.

**Narrative blocks from web Gemini session:** Two candidate blocks for Artifact 00 (§2.1, §2.4) introducing Dubai/gold-rush gradient framing. Not ready for artifacts — need Narrator Voice Test pass, consistency check against Creative Brief, and Andy sign-off. Artifact 00 is signed off; re-sign-off required before any addition.

---

## Immediate Priorities for Next Session (token reset pending)

1. **C01–C15 consistency pass** — Read Artifact 04. Apply new schema columns (resolution_type, base_difficulty, ring modifiers) to each card. Verify values make narrative and mechanical sense. C10 is the known problem card (conflict with 02a influence difficulty rules for structure removal). Gemini's card names for C06–C10 (Broadcast Interference, Amplify, Buy Influence, Fund, Protect) are **unverified** — treat as illustrative until confirmed against artifact.
2. **Artifact 00b vs DB schema gap analysis** — Read Artifact 00b (Data Architecture), compare against current schema.
3. **Full DB gap analysis** — Read design + PM docs, map against schema, identify missing tables/columns.
4. **Ring mechanics verification** — Read Artifact 03 and 02a, verify ring modifier concepts and C10 against signed-off content.
5. **Lock what holds up from today's exploratory session.**

---

## Where Gemini Can Help Right Now

**High value tasks for your context window:**
- Read `V1/04___Card_System.md` and provide a clean summary of C01–C15 actual names, categories, timing, and resolution types as they exist in the file. Flag any card where the definition is ambiguous or incomplete. This is verification work, not generation — report what you find, not what you expect.
- Read `V1/00b___Data_Architecture.md` and summarize its key invariants and data design decisions. Flag anything that appears to conflict with the DB schema described above.
- Read `V1/02a___Influence_System.md` and summarize the influence difficulty rules for structure removal — specifically what governs how hard it is to remove a structure, and whether C10 Protect is referenced or implied.

Report findings in `Claude_context.md`. Flag uncertainties explicitly. Do not generate card content — read and report only.

---

## Standing Conventions

- **ARBITER** — always all-caps
- **All other game terms** — Title Case
- **Material vs. Non-Material:** Material = contradicts or extends signed-off content → re-sign-off required. Non-material = formatting, terminology → no re-sign-off.
- **Design Pillar 6:** Narrative takes precedence over mechanical. If the narrative reason for a rule cannot be stated, the rule may be arbitrary.
- **Narrator Voice Test:** Every narrative field — could it have been written by a human who knows too much, OR by ARBITER in The Witness register? Both readings must remain valid.
- **Signed-off artifacts:** 03 (v1.7), 02a (v1.4). Do not propose additions to these without flagging re-sign-off requirement.
- **Artifact 04** (Card System, v0.9.17) — in progress. C11–C15 re-sign-off pending.

---

## PM File Purposes

| File | Purpose |
|------|---------|
| PM01 | Charter / WBS |
| PM02 | Decision Log (locked decisions L01–L140+) |
| PM03 | Master Artifact Index (sign-off tracking) |
| PM04 | Glossary |
| PM05 | Punch List (active work items) |

---

## Five Factions

| Faction | Resource | Core Belief |
|---------|----------|-------------|
| Ghost | Findings | Understanding must precede action |
| The Network | Exposure | No one gets to decide this in the dark |
| The Syndicate | Capital | Control comes from positioning early |
| The Guild | Capacity | The response must demonstrate humanity at its best |
| The Directorate | Mandate | Survival requires control, restraint, and continuity |

---

## MariaDB

- **Database:** `the_signal_db` — schema-only, no data yet
- **Credentials:** `~/Projects/TheSignal/mariadb_credentials.md`
- **Current tables:** `components`, `card_metadata`, `card_types`, `card_subtypes`, `factions`, `beat`, `game_actions`, `action_costs`, `action_valid_targets`, `action_restrictions`, `card_faction_modifiers`, `game_zones`, `component_valid_zones`, `city_rings`, `district_metadata`, `district_connections`, `player_metadata`, `live_state`, `setup_state`, `allocation_types`

**Do not propose schema changes via `Claude_context.md` without explicitly flagging them as proposals.** Claude Code executes all DDL after Andy confirms.
