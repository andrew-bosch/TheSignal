# the_signal_db — Schema Reference
**Status:** STUB — to be completed after token reset (S50, ~45 min)**  
**Priority:** DB-29 (PM05) — complete before Art 03 re-sign-off (03-14)

---

## Purpose

Single-file schema reference for `the_signal_db`. Eliminates the need for Claude Code and agy to issue exploratory queries (SHOW CREATE TABLE, DESCRIBE, FK checks, sample data pulls) at the start of every DB session. Read this file; skip the exploration.

**Sharing:** Claude Code reads this at session open when DB work is in scope. agy reads this via its project memory. Both agents should treat this as the authoritative schema reference between sessions.

---

## What Needs to Be Documented Here

### 1. FK Semantics (Critical — most expensive to rediscover)

The most costly session mistake: assuming `phase_id` in `tmp_comp_verb_role` referenced `tmp_beat` when it actually references `tmp_role_phase`. Document **what each FK column means semantically**, not just where it points. For every FK column that could be ambiguous, add a plain-English note.

Tables requiring FK semantic annotation:
- `tmp_comp_verb_role` — 4 FK columns, 2 of which caused confusion this session
- `tmp_comp_verb_beat` — FK column names vs actual reference targets
- `tmp_action` — multiple FK columns including destination_component_id, destination_zone_id, prereq_id
- `tmp_subject_target` — subject vs target semantics

### 2. All Table Schemas

For each table: columns, types, nullable, FK reference (table + column), semantic note.

Tables to document (in dependency order):

**Lookup / reference tables (seed once, rarely change):**
- `tmp_verb` — verb vocabulary (7 verbs: Add, Remove, Reveal, Corrupt, Conceal, Flip, Move, Invoke)
- `tmp_beat` — beat/phase registry (20 beats, Upkeep through Debrief)
- `tmp_player_role` — player types (1=Faction, 2=ARBITER)
- `tmp_role_phase` — action phases (1=initiator, 2=executor, 3=fulfiller)
- `tmp_function` / `tmp_function_verb` — function vocabulary
- `tmp_layer` — six-layer taxonomy (Territory / Economy / Information / Submission / Resolution / Standing)
- `tmp_type` / `tmp_category` — card type/category (note: may be deprecated per DB-14)
- `tmp_trigger_type` — trigger type vocabulary
- `tmp_condition` / `tmp_condition_clause` — condition modeling
- `tmp_state_condition` / `tmp_state_condition_clause` — state condition modeling

**Core component tables:**
- `tmp_component` — component registry (8 columns including 6 boolean flags)
- `tmp_comp_verb_beat` — component × verb × beat coverage matrix
- `tmp_comp_verb_role` — component × verb × player role × action phase
- `tmp_action` — action primitives (13 columns — the most complex table)
- `tmp_subject_target` — valid physical placement targets

**Supplementary component tables:**
- `tmp_component_faction` — faction-specific component assignments
- `tmp_component_ring` — ring-specific component assignments

### 3. Lookup Table Values

Capture the actual data rows for all lookup tables — these are small, stable, and expensive to re-query:
- `tmp_verb` — all 7 rows
- `tmp_beat` — all 20 rows
- `tmp_player_role` — all 2 rows
- `tmp_role_phase` — all 3 rows
- `tmp_layer` — all 6 rows
- `tmp_function` — all rows
- `tmp_trigger_type` — all rows
- `tmp_component` — full list with IDs (55+ rows as of S50)

### 4. View Definitions and What They Compute

Document each view: what it selects, what it's useful for, what question it answers. Views auto-update from base tables — no direct writes needed.

Key views to document:
- `v_comp_verb_matrix` — component coverage matrix (what verbs each component can perform)
- `v_component_coverage` — summary coverage per component
- `v_unlegislated_primitives` — components with actions not covered by tmp_action
- `v_gap_executor_check` — executor gaps (where actions have no valid executor)
- `v_primitives` / `v_primitives_with_trigger` — full action primitive list with context
- `v_action_by_beat` — actions grouped by beat
- `v_beat_role_matrix` — role coverage per beat
- `v_placement_matrix` — valid placements
- `v_faction_primitives` / `v_arbiter_primitives` — player-specific action views
- `v_arbiter_exclusive` / `v_faction_exclusive` — exclusive action sets
- `v_duplicate_primitives` — duplicate detection

### 5. Component Modeling Pattern

Document the canonical pattern for registering a new component, using Countermeasure card (id=52) as the reference. Step-by-step with example SQL — so any future component registration can follow the pattern without exploration.

**Key gotcha to capture:** `tmp_comp_verb_role.role_id` → `tmp_player_role` (Faction/ARBITER), `tmp_comp_verb_role.phase_id` → `tmp_role_phase` (initiator/executor/fulfiller). These column names are counterintuitive and caused multiple rounds of debugging this session.

### 6. Open Design Notes / Known Gaps

- DB-14: decision pending — promote tmp_ tables to permanent schema (drop tmp_ prefix) or keep as workspace
- DB-18: cross-beat modifier persistence not modeled in tmp_action
- DB-19: concurrent Political acts (C09) not verified in resolution model
- District adjacency table: DB-09, pending Art 01 sign-off
- component_positions table: DB-11 rename pending agy execution

---

## How to Generate This Document

Run the following queries against `the_signal_db` to populate each section. Connection: `mysql the_signal_db` (Claude Code: ~/.my.cnf configured; agy: `mysql -u gemini -pgemini_password1 the_signal_db`).

```sql
-- Lookup table values
SELECT * FROM tmp_verb ORDER BY id;
SELECT * FROM tmp_beat ORDER BY id;
SELECT * FROM tmp_player_role ORDER BY id;
SELECT * FROM tmp_role_phase ORDER BY id;
SELECT * FROM tmp_layer ORDER BY id;
SELECT * FROM tmp_function ORDER BY id;
SELECT * FROM tmp_trigger_type ORDER BY id;

-- Component list
SELECT id, name, actionable, transformable, receivable,
       transform_visibility, transform_orientation, transform_data
FROM tmp_component ORDER BY id;

-- Table schemas with FK constraints
SHOW CREATE TABLE tmp_component\G
SHOW CREATE TABLE tmp_comp_verb_role\G
SHOW CREATE TABLE tmp_comp_verb_beat\G
SHOW CREATE TABLE tmp_action\G
SHOW CREATE TABLE tmp_subject_target\G
-- (repeat for all tables)

-- View definitions
SHOW CREATE VIEW v_comp_verb_matrix\G
-- (repeat for key views)
```

---

## agy Sharing

Once this document is populated:
1. Add a reference to it in `GEMINI_CONTEXT.md` under the DB section so agy reads it at session start
2. Confirm agy's connection string: `mysql -u gemini -pgemini_password1 the_signal_db`
3. agy should treat this file as read-only reference — all schema changes go through Claude Code + Andy confirmation per the dual-authorization model in GEMINI_CONTEXT.md

---

*Stub created S50. Populated by Claude Code after token reset.*
