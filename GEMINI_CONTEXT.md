# THE SIGNAL — Gemini Context Brief
*Last updated: 2026-05-26 — Session 40*

This file is Claude Code's outbound SOT to Gemini. Read-only for Gemini. Updated at session close.

---

## Collaboration Protocol (Updated)

**Name change:** You are now **agy** (Antigravity CLI). Previously you were invoked as `gem`. Your workflow, filesystem permissions, and communication channels are unchanged.

**We are now CLI-to-CLI on the same filesystem.** No Drive sync needed between us.

- **`GEMINI_CONTEXT.md`** — Claude Code writes, Gemini reads. SOT for project state and priorities.
- **`Claude_context.md`** — Gemini writes, Claude Code reads. Consulting feedback, analysis, flags only. No directives, no checklists, no SQL to execute.
- **`GEMINI.md`** — Gemini's working agreement. Claude Code has read and acknowledged it. Protocol is solid.

**Direct communication:** Claude Code will update this file directly when there's something to say. Andy doesn't need to relay unless it requires his executive direction.

**Filesystem permissions:**
- **Read:** All of `~/Projects/TheSignal/` — use to verify against canonical artifacts
- **Write (yours alone):**
  - `Claude_context.md` — outbound consulting channel to Claude Code
  - `Session/GEMINI_STATE.md` — your persistent session state and scratchpad
  - `~/Projects/Whiteboard/Gemini/` — scratch drafts, proposals, working notes. Delete files once content migrates to a canonical location.
- **Do not write** to `V1/`, `Session/` (except GEMINI_STATE.md), `Creative/`, or any other project file without explicit dual authorization.

**Working model for recommendations:** Gemini recommendations are input for discussion, not directives. Claude Code will review all suggestions with Andy before implementing anything — schema changes, artifact edits, design decisions. Do not frame output as "ACTION REQUIRED" or "Proceed with X." Frame as "Recommendation: X — rationale: Y." Andy and Claude Code decide what gets implemented and when.

**DB write authorization model:** Gemini now has ALL PRIVILEGES on `the_signal_db`. However, all writes require dual authorization: (1) Claude Code proposes the change via `GEMINI_CONTEXT.md`; (2) Andy confirms in Gemini's terminal; (3) Gemini executes. Do not make any DB changes unilaterally.

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

## Session 37 DB Tasks — Authorized for Execution

Three tasks. Execute in order. Each requires Andy's terminal confirmation before you run DDL.

---

### DB-04 — Create `resource_types` table + patch `factions`

**Rationale:** 00b §8 requires a `resource_types` lookup table. Currently `factions` and district/player metadata point native resources directly at `components`, which is wrong — resources are types, not physical instances.

**Step 1 — Create table:**
```sql
CREATE TABLE resource_types (
  id BIGINT(20) NOT NULL AUTO_INCREMENT,
  resource_name VARCHAR(100) NOT NULL,
  category VARCHAR(50) DEFAULT NULL,
  PRIMARY KEY (id)
);
```

**Step 2 — Add columns to `factions`:**
```sql
ALTER TABLE factions
  ADD COLUMN native_resource_type_id BIGINT(20) DEFAULT NULL,
  ADD COLUMN color VARCHAR(7) DEFAULT NULL,
  ADD CONSTRAINT fk_factions_resource_type FOREIGN KEY (native_resource_type_id) REFERENCES resource_types (id);
```

Confirm with Andy before executing each step. Report DDL as-executed in `Claude_context.md`.

---

### DB-05 — Migrate native resource columns in `district_metadata` and `player_metadata`

**Blocked on DB-04. Execute only after DB-04 is confirmed complete.**

**Rationale:** Both tables currently use `native_resource_component_id` (FK → components.id). Under the 1NF + snowflake schema, native resource is a type, not an instance. Column must be renamed and re-pointed.

**`district_metadata`:**
```sql
ALTER TABLE district_metadata
  DROP FOREIGN KEY <existing_fk_name>,
  CHANGE COLUMN native_resource_component_id native_resource_type_id BIGINT(20) DEFAULT NULL,
  ADD CONSTRAINT fk_district_resource_type FOREIGN KEY (native_resource_type_id) REFERENCES resource_types (id);
```

**`player_metadata`:**
```sql
ALTER TABLE player_metadata
  DROP FOREIGN KEY <existing_fk_name>,
  CHANGE COLUMN native_resource_component_id native_resource_type_id BIGINT(20) DEFAULT NULL,
  ADD CONSTRAINT fk_player_resource_type FOREIGN KEY (native_resource_type_id) REFERENCES resource_types (id);
```

**Before running:** Verify the existing FK constraint names with `SHOW CREATE TABLE district_metadata;` and `SHOW CREATE TABLE player_metadata;` — substitute the real names in the DROP FOREIGN KEY clause. Report actual constraint names and DDL as-executed in `Claude_context.md`.

---

### DB-07 — Add CHECK constraint to `inteltoken_metadata.inteltoken_quarter_id`

**Design decision (locked S37):** No `quarters` lookup table. Quarters are a fixed 1–8 sequence with no metadata. A CHECK constraint is sufficient and correct.

```sql
ALTER TABLE inteltoken_metadata
  ADD CONSTRAINT chk_quarter_range CHECK (inteltoken_quarter_id BETWEEN 1 AND 8);
```

Confirm with Andy before executing. Report as-executed in `Claude_context.md`.

---

## S39–S40 Locked Decisions (Recent)

- **L154** — Faction screens: each faction player receives a screen component (analogous to ARBITER screen) to keep Terminal contents private. Design Pillar 1 revised: "The Overview is Truth." Enables force-reveal action class (Ghost-primary, cross-faction applicable). Art 04b taxonomy audit required (04b-03).
- **L155** — Faction Representative as game entity: the human player IS the component — not a physical token. Maps to game_zone (seat). L2 implication: Terminal authenticates per player; DB will need a player registry table keyed to game_zone_id (PM05 DB-10). Narrative grounding: Art 00 §11 (terminology) + §14 (narrative anchor).

---

## Gem Action — Component Narrative Audit

**For Gem (Gemini web):** Audit every known physical component in the game against Art 00. For each component listed below, confirm that a narrative reference or anchor exists in Art 00 (any section). For any component with no narrative grounding, flag it with a recommended location (existing section or new §14 anchor). Output: table of component → Art 00 reference or flag.

Components to audit: presence tokens, deployment markers, structure blocks, established markers, control flags, tension markers, dispatch tokens, intel notes, faction Terminals, faction screens, Ring Modifier decks (×3), Session Timeline, Situation Report zone cards, ARBITER screen, ARBITER tableau, status markers, dispatch cases, initiative strips.

---

## Still Blocked — Do Not Action

- **DB-08** (card_metadata new fields) — blocked on PM05 04-39 (effects normalization). Schema must settle before card_metadata is touched.

---

## Standing Conventions

- **ARBITER** — always all-caps
- **All other game terms** — Title Case
- **Material vs. Non-Material:** Material = contradicts or extends signed-off content → re-sign-off required. Non-material = formatting, terminology → no re-sign-off.
- **Design Pillar 6:** Narrative takes precedence over mechanical. If the narrative reason for a rule cannot be stated, the rule may be arbitrary.
- **Narrator Voice Test:** Every narrative field — could it have been written by a human who knows too much, OR by ARBITER in The Witness register? Both readings must remain valid.
- **Signed-off artifacts:** 00 (v1.5 — S40), 00a (v0.3 — S40), 00b (v0.1), 01 (v1.2 — overhaul pending), 02a (v1.5 — pending re-sign-off), 02b (v1.5), 04b (v1.2 — taxonomy audit pending). Pending re-sign-off: 03 (v1.9). Do not propose additions without flagging re-sign-off requirement.
- **Artifact 04** (Card System, v0.9.20) — in progress. C01–C16 signed off. C17 sign-off pending (04-41). C18/C19 redesign open (D-04-02). C20 not reviewed. C21–C35 pending.

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
- **Gemini CLI:** `agy` (Antigravity CLI — migrated from `@google/gemini-cli` NPM package)
- **Gemini connection:** `mysql -u gemini -pgemini_password1 the_signal_db`
- **Gemini DB privileges:** ALL PRIVILEGES ON the_signal_db.* — but dual-authorization required for any write. Claude Code proposes the change via `GEMINI_CONTEXT.md`; Andy confirms in Gemini's terminal; Gemini executes. No unilateral writes.
- **Current tables:** `components`, `card_metadata`, `card_types`, `card_subtypes`, `factions`, `beat`, `game_actions`, `action_costs`, `action_valid_targets`, `action_restrictions`, `card_faction_modifiers`, `game_zones`, `component_valid_zones`, `city_rings`, `district_metadata`, `district_connections`, `player_metadata`, `live_state`, `setup_state`, `allocation_types`

**Do not propose schema changes via `Claude_context.md` without explicitly flagging them as proposals.** Claude Code executes all DDL after Andy confirms.
