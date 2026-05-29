# the_signal_db — Schema Reference
**Status:** Complete — populated S50 (2026-05-29)  
**Priority:** DB-29 (PM05)

---

## Purpose

Single-file schema reference for `the_signal_db`. Eliminates the need for Claude Code and agy to issue exploratory queries (SHOW CREATE TABLE, DESCRIBE, FK checks, sample data pulls) at the start of every DB session. Read this file; skip the exploration.

**Connection — Claude Code:** `mysql the_signal_db` (no flags; ~/.my.cnf configured for claude user)  
**Connection — agy:** `mysql -u gemini -pgemini_password1 the_signal_db`

---

## 1. Critical FK Semantics — Read This First

The most expensive session mistake: assuming `tmp_comp_verb_role.phase_id` references beats. It does not.

**`tmp_comp_verb_role` — 4 FK columns:**

| Column | References | Values | What it means |
|--------|-----------|--------|---------------|
| `component_id` | `tmp_component(id)` | 1–97 | The physical component |
| `verb_id` | `tmp_verb(id)` | 1–17 | The action verb |
| `role_id` | `tmp_player_role(id)` | 1=Faction, 2=ARBITER | **Who** performs this action |
| `phase_id` | `tmp_role_phase(id)` | 1=initiator, 2=executor, 3=fulfiller | **What role** in the action chain |

**`phase_id` does NOT reference beats.** Column name is misleading. `tmp_role_phase` has 3 rows: 1=initiator, 2=executor, 3=fulfiller. This caused multiple rounds of FK constraint errors in S50.

**`tmp_action` subject vs. component:**

| Column | References | What it means |
|--------|-----------|---------------|
| `subject_id` | `tmp_player_role(id)` | Who performs this primitive (Faction=1 or ARBITER=2) |
| `component_id` | `tmp_component(id)` | What component is acted upon (nullable) |
| `destination_component_id` | `tmp_component(id)` | Where the component moves to (nullable — currently unpopulated) |
| `destination_zone_id` | `game_zones(id)` | Destination zone (nullable — legacy schema; currently unpopulated) |
| `prereq_id` | `tmp_action(id)` | Self-referential: prerequisite action in chain (NULL for root actions) |
| `source_action_id` | `tmp_action(id)` | Self-referential: Copy/Invoke source chain (NULL unless Copy) |
| `prereq_beat_id` | `tmp_beat(id)` | Beat in which the prereq fires (nullable) |

**`tmp_beat` is NOT referenced by `tmp_comp_verb_role` at all.** Beat assignments live in `tmp_comp_verb_beat`.

---

## 2. Database Layout

### Two Schema Families

**`tmp_` tables** — Active design workspace. These are the canonical source of truth for action primitives and component taxonomy. All design work happens here.

**Non-`tmp_` tables** (components, game_zones, card_metadata, etc.) — Legacy schema from earlier sessions. Structurally consistent but not actively populated for game logic. Eventually tmp_ tables will be promoted to replace or augment these (DB-14).

### Full Table List

**tmp_ tables (design workspace — active):**
`tmp_action`, `tmp_beat`, `tmp_comp_verb_beat`, `tmp_comp_verb_role`, `tmp_component`, `tmp_component_faction`, `tmp_component_ring`, `tmp_condition`, `tmp_condition_clause`, `tmp_function`, `tmp_function_verb`, `tmp_layer`, `tmp_player_role`, `tmp_role_phase`, `tmp_state_condition`, `tmp_state_condition_clause`, `tmp_subject_target`, `tmp_trigger_type`, `tmp_verb`, `tmp_visibility_scope`, `tmp_category` (deprecated), `tmp_type` (deprecated)

**Legacy tables (structural, not actively used for game logic):**
`action_costs`, `action_restrictions`, `action_valid_targets`, `allocation_types`, `beat`, `card_faction_modifiers`, `card_metadata`, `card_subtypes`, `card_types`, `city_rings`, `component_positions`, `component_valid_zones`, `components`, `district_connections`, `district_metadata`, `factions`, `game_actions`, `game_zones`, `inteltoken_metadata`, `player_metadata`, `resource_types`, `setup_state`

---

## 3. Lookup Tables — Full Values

### tmp_verb (8 rows)

| id | name |
|----|------|
| 1 | Add |
| 2 | Remove |
| 10 | Reveal |
| 13 | Corrupt |
| 14 | Conceal |
| 15 | Flip |
| 16 | Move |
| 17 | Invoke |

*IDs are non-sequential (gaps from deprecated verbs removed in prior sessions).*

### tmp_player_role (2 rows)

| id | name |
|----|------|
| 1 | Faction |
| 2 | ARBITER |

### tmp_role_phase (3 rows)

| id | name | meaning |
|----|------|---------|
| 1 | initiator | Who decides/declares the action |
| 2 | executor | Who physically performs it |
| 3 | fulfiller | Who completes or receives the outcome |

### tmp_beat (20 rows)

| id | name | month | beat_num | primary_agent | description |
|----|------|-------|----------|---------------|-------------|
| 1 | Upkeep | NULL | NULL | Both | World updates, resources, tokens, initiative, Situation Reports |
| 2 | Placement | NULL | NULL | Both | Deployment markers placed; entry requirements enforced; influence levels updated |
| 3 | Month 1 — Dispatch | M1 | NULL | Faction | Operations assembled, sealed, submitted with Dispatch Tokens |
| 4 | Month 1 — Countermeasures | M1 | NULL | Faction | Countermeasure cards deployed; handed to ARBITER for Month 1 application |
| 5 | Month 1 — Beat 0 | M1 | 0 | Both | The Cases Open: ARBITER opens cases, sorts grid; factions validate submissions |
| 6 | Month 1 — Beat 1 | M1 | 1 | ARBITER | Check Active Restrictions: ARBITER removes ops violating restriction cards |
| 7 | Month 1 — Beat 2 | M1 | 2 | Both | The Ground Shifts: modifier cards resolve; ARBITER places modifier tokens |
| 8 | Month 1 — Beat 3 | M1 | 3 | ARBITER | Covert Operations Resolve: ARBITER resolves each op; board effects applied |
| 9 | Month 2 — Dispatch | M2 | NULL | Faction | Second covert pass; remaining Dispatch Tokens used |
| 10 | Month 2 — Countermeasures | M2 | NULL | Faction | Countermeasure cards deployed for Month 2 |
| 11 | Month 2 — Beat 0 | M2 | 0 | Both | The Cases Open: Month 2 grid sorted |
| 12 | Month 2 — Beat 1 | M2 | 1 | ARBITER | Check Active Restrictions: Month 2 grid audited |
| 13 | Month 2 — Beat 2 | M2 | 2 | Both | The Ground Shifts: Month 2 modifier pass |
| 14 | Month 2 — Beat 3 | M2 | 3 | ARBITER | Covert Operations Resolve: Month 2 operations resolved |
| 15 | Month 3 — Declaration | M3 | NULL | Both | Political acts declared face-up in initiative order |
| 16 | Month 3 — Countermeasures | M3 | NULL | Faction | Countermeasure cards deployed for Month 3 |
| 17 | Month 3 — Beat 4 | M3 | 4 | Both | Political Acts Resolve: declared acts resolved; board and resource effects applied |
| 18 | Month 3 — Beat 5 | M3 | 5 | ARBITER | The Table Speaks: ARBITER updates Portrait, Chronicle, Session Timeline, Chorus Activity |
| 19 | Battlefield Strength | NULL | NULL | ARBITER | Contested districts resolved; d10 roll-off; Tension markers cleared |
| 20 | Debrief | NULL | NULL | Both | Resource and Intel trades; ARBITER Debrief observation; Chorus Question window |

### tmp_layer (6 rows)

| id | name |
|----|------|
| 1 | Territory |
| 2 | Economy |
| 3 | Information |
| 4 | Submission |
| 5 | Resolution |
| 6 | Standing |

### tmp_trigger_type (10 rows)

| id | type | subtype | meaning |
|----|------|---------|---------|
| 1 | phase | open | Fires when the beat begins |
| 2 | phase | during | Fires during the beat |
| 3 | phase | closed | Fires when the beat closes |
| 4 | rule | card | Triggered by a card being played |
| 5 | rule | resolution | Triggered by a resolution outcome |
| 6 | player | introduce_card | Player physically introduces a card |
| 7 | player | agreement | Player agrees to a deal/accord |
| 8 | player | verbal_statement | Player makes a verbal declaration |
| 9 | state_condition | NULL | Triggered by a game state condition |
| 10 | cascade | NULL | Downstream trigger from a prior action |

### tmp_function (12 rows) and verb mappings

| id | name | maps to verb | description |
|----|------|-------------|-------------|
| 1 | Add | Add | Brings a new element into active play from supply or off-board |
| 2 | Remove | Remove | Takes an element out of active play |
| 3 | Redirect | Move | Changes ownership, destination, or allegiance of an element |
| 4 | Recover | Add | Returns a spent, removed, or degraded element to active play |
| 5 | Modify | *(no verb)* | Alters a cost, value, or attribute without changing fundamental state |
| 6 | Protect | *(no verb)* | Preserves the current state of a target against a named change |
| 7 | Block | *(no verb)* | Prevents another action from being initiated or resolving |
| 8 | Copy | Invoke | Duplicates another action's effect chain with a new initiating subject |
| 9 | Reveal | Reveal | Makes hidden information visible to a named audience |
| 10 | Conceal | Conceal | Places information or attribution into a hidden state |
| 11 | Shift | Move | Moves a track value up or down |
| 12 | Corrupt | Corrupt | Alters a physically written or recorded value on a component |

*Modify, Protect, Block have no verb mapping — they are abstract constraints on other actions, not physical primitives.*

### tmp_visibility_scope (8 rows)

| id | code | name | status |
|----|------|------|--------|
| 1 | VS-01 | Public | Active |
| 2 | VS-02 | Faction-Only | Active |
| 3 | VS-03 | Bilateral | Active |
| 4 | VS-04 | ARBITER-Only | Active |
| 5 | VS-05 | Player-Only | Active |
| 6 | VS-06 | Conditional | Active |
| 7 | VS-07 | Website-Public | L2+ |
| 8 | VS-08 | Website-Private | L2+ |

---

## 4. Table Schemas (tmp_ tables)

### tmp_component
```sql
CREATE TABLE `tmp_component` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `actionable` tinyint(1) NOT NULL DEFAULT 0,      -- 1 = can be acted upon in tmp_action
  `transformable` tinyint(1) NOT NULL DEFAULT 0,   -- 1 = has at least one transform_ flag set
  `receivable` tinyint(1) NOT NULL DEFAULT 0,      -- 1 = can be a target in tmp_subject_target
  `transform_visibility` tinyint(1) NOT NULL DEFAULT 0,  -- 1 = can be Revealed/Concealed
  `transform_orientation` tinyint(1) NOT NULL DEFAULT 0, -- 1 = can be Flipped
  `transform_data` tinyint(1) NOT NULL DEFAULT 0,        -- 1 = carries written data that can be Corrupted
  PRIMARY KEY (`id`)
)
```
*AUTO_INCREMENT=98 as of S50. Next component will receive id=98.*

### tmp_comp_verb_beat
```sql
CREATE TABLE `tmp_comp_verb_beat` (
  `component_id` int(11) NOT NULL,   -- FK → tmp_component(id)
  `verb_id` int(11) NOT NULL,        -- FK → tmp_verb(id)
  `beat_id` int(11) NOT NULL,        -- FK → tmp_beat(id)
  `notes` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`component_id`,`verb_id`,`beat_id`)
)
```
*Purpose: declares which beats a component×verb combination is valid. Does not specify who or how — that is tmp_comp_verb_role.*

### tmp_comp_verb_role
```sql
CREATE TABLE `tmp_comp_verb_role` (
  `component_id` int(11) NOT NULL,  -- FK → tmp_component(id)
  `verb_id` int(11) NOT NULL,       -- FK → tmp_verb(id)
  `role_id` int(11) NOT NULL,       -- FK → tmp_player_role(id) — 1=Faction, 2=ARBITER
  `phase_id` int(11) NOT NULL,      -- FK → tmp_role_phase(id) — 1=initiator, 2=executor, 3=fulfiller
  `notes` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`component_id`,`verb_id`,`role_id`,`phase_id`)
)
```
**⚠ FK GOTCHA:** `role_id` → `tmp_player_role` (NOT a verb table). `phase_id` → `tmp_role_phase` (NOT a beat table). Column names are counterintuitive and have caused multiple FK constraint failures.

### tmp_action (206 rows as of S50)
```sql
CREATE TABLE `tmp_action` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `beat_id` int(11) NOT NULL,                         -- FK → tmp_beat(id)
  `beat_trigger` enum('during','on_close') NOT NULL DEFAULT 'during',
  `trigger_type_id` int(11) DEFAULT NULL,             -- FK → tmp_trigger_type(id)
  `prereq_id` int(11) DEFAULT NULL,                   -- FK → tmp_action(id) self-ref; NULL = root action
  `prereq_beat_id` int(11) DEFAULT NULL,              -- FK → tmp_beat(id); beat where prereq fires
  `source_action_id` int(11) DEFAULT NULL,            -- FK → tmp_action(id) self-ref; Copy source chain
  `subject_id` int(11) NOT NULL,                      -- FK → tmp_player_role(id) — who performs this
  `verb_id` int(11) NOT NULL,                         -- FK → tmp_verb(id)
  `component_id` int(11) DEFAULT NULL,                -- FK → tmp_component(id) — nullable
  `destination_component_id` int(11) DEFAULT NULL,    -- FK → tmp_component(id) — nullable; currently unpopulated
  `destination_zone_id` bigint(20) DEFAULT NULL,      -- FK → game_zones(id) — nullable; currently unpopulated
  `notes` text DEFAULT NULL,
  PRIMARY KEY (`id`)
)
```
*All 206 rows have `prereq_id IS NULL` (no multi-step chains populated yet).*

### tmp_subject_target
```sql
CREATE TABLE `tmp_subject_target` (
  `subject_id` int(11) NOT NULL,   -- component_id of the acting component (implicit FK → tmp_component)
  `target_id` int(11) NOT NULL,    -- component_id of the valid placement target (implicit FK → tmp_component)
  PRIMARY KEY (`subject_id`,`target_id`)
)
```
*No declared FKs. Used by v_comp_verb_matrix to determine Move=1 for a component.*

### tmp_trigger_type
```sql
CREATE TABLE `tmp_trigger_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  `subtype` varchar(30) DEFAULT NULL,
  `notes` text DEFAULT NULL,
  PRIMARY KEY (`id`)
)
```

### tmp_function / tmp_function_verb
```sql
CREATE TABLE `tmp_function` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`id`), UNIQUE KEY `name` (`name`)
)

CREATE TABLE `tmp_function_verb` (
  `function_id` int(11) NOT NULL,  -- FK → tmp_function(id)
  `verb_id` int(11) NOT NULL,      -- FK → tmp_verb(id)
  PRIMARY KEY (`function_id`,`verb_id`)
)
```

### tmp_layer
```sql
CREATE TABLE `tmp_layer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` text DEFAULT NULL,
  `default_visibility_id` tinyint(3) unsigned NOT NULL,  -- FK → tmp_visibility_scope(id)
  PRIMARY KEY (`id`), UNIQUE KEY `name` (`name`)
)
```

### tmp_state_condition / tmp_state_condition_clause
```sql
CREATE TABLE `tmp_state_condition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` text NOT NULL,
  `logic_operator` enum('AND','OR') NOT NULL DEFAULT 'AND',
  PRIMARY KEY (`id`)
)

CREATE TABLE `tmp_state_condition_clause` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `condition_id` int(11) NOT NULL,     -- FK → tmp_state_condition(id)
  `component_id` int(11) DEFAULT NULL, -- FK → tmp_component(id)
  `state_key` varchar(50) NOT NULL,
  `operator` enum('=','!=','>','<','>=','<=','ALL','ANY') NOT NULL DEFAULT '=',
  `value` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
)
```
*Lightly populated (2 rows each). Used for state-conditional trigger types.*

---

## 5. Component Registry (tmp_component — 57 rows as of S50)

| id | name | act | xfm | rcv | vis | ori | dat |
|----|------|-----|-----|-----|-----|-----|-----|
| 1 | Presence token | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | Deployment marker | 1 | 1 | 0 | 0 | 1 | 0 |
| 3 | Structure block | 1 | 0 | 0 | 0 | 0 | 0 |
| 4 | District tile | 0 | 0 | 1 | 0 | 0 | 0 |
| 5 | Established marker | 1 | 0 | 0 | 0 | 0 | 0 |
| 6 | Control flag | 1 | 0 | 0 | 0 | 0 | 0 |
| 7 | Tension marker | 1 | 0 | 0 | 0 | 0 | 0 |
| 8 | Native resource | 1 | 0 | 0 | 0 | 0 | 0 |
| 9 | Intel token | 1 | 1 | 0 | 1 | 0 | 1 |
| 10 | Accord agreement | 1 | 1 | 0 | 1 | 0 | 1 |
| 11 | Modifier card | 1 | 1 | 0 | 1 | 0 | 0 |
| 12 | Dispatch token | 1 | 0 | 0 | 0 | 0 | 0 |
| 13 | Covert operation | 1 | 1 | 1 | 1 | 0 | 0 |
| 14 | Political act | 1 | 1 | 1 | 1 | 0 | 0 |
| 15 | Operative ability | 1 | 1 | 0 | 1 | 0 | 0 |
| 17 | Classified directives | 1 | 1 | 0 | 1 | 0 | 0 |
| 21 | Public Standing | 0 | 0 | 1 | 0 | 0 | 0 |
| 22 | Chorus Portrait | 0 | 0 | 1 | 0 | 0 | 0 |
| 23 | Session Timeline | 0 | 0 | 1 | 0 | 0 | 0 |
| 24 | Initiative strip | 0 | 0 | 1 | 0 | 0 | 0 |
| 25 | Situation Report card | 1 | 1 | 0 | 1 | 0 | 0 |
| 26 | Faction Terminal | 0 | 0 | 1 | 0 | 0 | 0 |
| 27 | Faction screen | 0 | 0 | 0 | 0 | 0 | 0 |
| 28 | ARBITER screen | 0 | 0 | 0 | 0 | 0 | 0 |
| 29 | The Overview | 0 | 0 | 1 | 0 | 0 | 0 |
| 30 | Arbiter Tableau | 0 | 0 | 1 | 0 | 0 | 0 |
| 31 | Chorus Activity Track | 0 | 0 | 1 | 0 | 0 | 0 |
| 32 | Reservoir | 0 | 0 | 1 | 0 | 0 | 0 |
| 33 | Backlog | 0 | 0 | 1 | 0 | 0 | 0 |
| 34 | Pointer marker | 1 | 0 | 0 | 0 | 0 | 0 |
| 35 | Activity marker | 1 | 0 | 0 | 0 | 0 | 0 |
| 36 | Threshold marker | 1 | 0 | 0 | 0 | 0 | 0 |
| 37 | Standing marker | 1 | 0 | 0 | 0 | 0 | 0 |
| 38 | Faction order marker | 1 | 0 | 0 | 0 | 0 | 0 |
| 42 | ARBITER Dominance Marker | 1 | 0 | 0 | 0 | 0 | 0 |
| 43 | Human player | 0 | 0 | 0 | 0 | 0 | 0 |
| 44 | Dispatch case | 1 | 1 | 1 | 1 | 0 | 0 |
| 47 | Modifier token | 1 | 0 | 0 | 0 | 0 | 0 |
| 48 | Target Profile | 1 | 1 | 0 | 0 | 0 | 1 |
| 49 | Status marker | 1 | 1 | 0 | 0 | 1 | 1 |
| 50 | Portrait track | 0 | 0 | 0 | 0 | 0 | 0 |
| 51 | Portrait marker | 1 | 0 | 0 | 0 | 0 | 0 |
| 52 | Countermeasure card | 1 | 1 | 0 | 1 | 0 | 0 |
| 53 | Ring 1 modifier deck | 1 | 0 | 1 | 0 | 0 | 0 |
| 54 | Ring 2 modifier deck | 1 | 0 | 1 | 0 | 0 | 0 |
| 55 | Ring 3 modifier deck | 1 | 0 | 1 | 0 | 0 | 0 |
| 86 | Situation card deck | 1 | 0 | 1 | 0 | 0 | 0 |
| 87 | Event card deck | 1 | 0 | 1 | 0 | 0 | 0 |
| 88 | Pass card | 1 | 1 | 0 | 1 | 0 | 0 |
| 89 | Faction modifier deck | 1 | 0 | 1 | 0 | 0 | 0 |
| 90 | Political act deck | 1 | 0 | 1 | 0 | 0 | 0 |
| 91 | Political act discard | 1 | 0 | 1 | 0 | 0 | 0 |
| 92 | Covert operation deck | 1 | 0 | 1 | 0 | 0 | 0 |
| 93 | Covert operation discard | 1 | 0 | 1 | 0 | 0 | 0 |
| 94 | Faction hand | 1 | 0 | 1 | 0 | 0 | 0 |
| 95 | Notification Slip | 1 | 0 | 1 | 0 | 0 | 0 |
| 96 | Intel Delivery Slip | 1 | 1 | 1 | 0 | 0 | 1 |
| 97 | Emergency Response card | 1 | 1 | 0 | 1 | 0 | 0 |

*Column key: act=actionable, xfm=transformable, rcv=receivable, vis=transform_visibility, ori=transform_orientation, dat=transform_data*  
*IDs are non-sequential (gaps from deleted rows during schema evolution).*  
*Next AUTO_INCREMENT = 98.*

---

## 6. View Catalog (29 views)

### Gap Analysis Views — Use These First

| View | What it answers |
|------|----------------|
| `v_unlegislated_primitives` | (beat, subject, verb, component) tuples in the taxonomy with no matching root row in tmp_action. Current answer to "what's covered in the design model but not in the action primitive table?" |
| `v_unlegislated_by_trigger` | Same but collapsed to (subject, verb, component) with beat_count — gaps across ALL beats |
| `v_gap_executor_check` | For each unlegislated gap, who is the phase_id=2 executor? ARBITER executor = expected gap (Faction initiates, ARBITER executes physically). Faction executor = true unmodeled gap |
| `v_component_coverage` | Every component with its primitive count. Zero = no actions modeled |
| `v_duplicate_primitives` | Duplicate (beat, subject, verb, component) rows where prereq_id IS NULL |
| `v_unassigned_triggers` | Primitives in tmp_action where trigger_type_id IS NULL |

### Primitive Browse Views

| View | What it answers |
|------|----------------|
| `v_primitives_with_trigger` | Full readable primitive list: beat, trigger_type.subtype, subject, verb, component, notes |
| `v_primitives` | Simplified primitive list (no trigger type) |
| `v_action_by_beat` | Actions grouped by beat |
| `v_faction_primitives` | All Faction-subject primitives |
| `v_arbiter_primitives` | All ARBITER-subject primitives |
| `v_faction_exclusive` | Primitives where only Faction acts |
| `v_arbiter_exclusive` | Primitives where only ARBITER acts |
| `v_arbiter_triggered` | ARBITER-initiated primitives |
| `v_split_agency` | Actions where Faction initiates but ARBITER executes |
| `v_action_chain` | Action prerequisite chains (currently empty — no prereq rows) |

### Coverage Matrix Views

| View | What it answers |
|------|----------------|
| `v_comp_verb_matrix` | Per-component capability grid: Add/Remove/Move/Reveal/Conceal/Flip/Corrupt. **Note: Add and Remove hardcoded to 1 for all actionable components** — not derived from tmp_action. Move=1 if component is in tmp_subject_target. Others derived from transform_ flags |
| `v_placement_matrix` | Which components can be placed on which receivable target components (from tmp_subject_target) |
| `v_beat_subject_coverage` | Per-beat: verb count, component count, primitive count by subject |
| `v_beat_role_matrix` | Role coverage per beat |
| `v_trigger_beat_coverage` | Trigger types present in each beat |
| `v_trigger_summary` | Trigger distribution by subject |
| `v_role_matrix` | Role assignment matrix |
| `v_beat_verb_summary` | Verb usage per beat |
| `v_fulfiller_summary` | Fulfiller role coverage |
| `v_layer_function_coverage` | Every Faction-initiatable Function × Component with beat availability |
| `v_object_from` | Subject-object relationships |
| `v_validact` | Valid action combinations |
| `v_verb` | Verb reference |

---

## 7. Canonical Component Registration Pattern

Use **Countermeasure card (id=52)** as the reference. Full 4-table cascade required for every new component.

### Step 1 — Register in tmp_component
```sql
INSERT INTO tmp_component (name, actionable, transformable, receivable,
  transform_visibility, transform_orientation, transform_data)
VALUES ('Component Name', 1, 1, 0, 1, 0, 0);
-- Next AUTO_INCREMENT = 98 as of S50
```

### Step 2 — Seed beat coverage in tmp_comp_verb_beat
One row per valid (component, verb, beat) combination.
```sql
-- Countermeasure card (id=52) example:
INSERT INTO tmp_comp_verb_beat (component_id, verb_id, beat_id) VALUES
  (52, 1,  2),   -- Add at Placement (beat 2)
  (52, 17, 4),   -- Invoke at M1 Countermeasures (beat 4)
  (52, 10, 4),   -- Reveal at M1 Countermeasures
  (52, 2,  7),   -- Remove at M1 Beat 2
  (52, 10, 8),   -- Reveal at M1 Beat 3
  (52, 17, 10),  -- Invoke at M2 Countermeasures
  (52, 10, 10),  -- Reveal at M2 Countermeasures
  (52, 2,  13),  -- Remove at M2 Beat 2
  (52, 10, 14),  -- Reveal at M2 Beat 3
  (52, 17, 16),  -- Invoke at M3 Countermeasures
  (52, 10, 16),  -- Reveal at M3 Countermeasures
  (52, 2,  17),  -- Remove at M3 Beat 4
  (52, 10, 17);  -- Reveal at M3 Beat 4
```

### Step 3 — Seed role assignments in tmp_comp_verb_role
**⚠ role_id → tmp_player_role (1=Faction, 2=ARBITER); phase_id → tmp_role_phase (1=initiator, 2=executor, 3=fulfiller)**
```sql
-- Countermeasure card (id=52) example:
INSERT INTO tmp_comp_verb_role (component_id, verb_id, role_id, phase_id) VALUES
  (52, 1,  2, 1),  -- Add: ARBITER initiator
  (52, 1,  2, 2),  -- Add: ARBITER executor
  (52, 1,  2, 3),  -- Add: ARBITER fulfiller
  (52, 17, 1, 1),  -- Invoke: Faction initiator
  (52, 17, 2, 2),  -- Invoke: ARBITER executor
  (52, 17, 2, 3),  -- Invoke: ARBITER fulfiller
  (52, 10, 1, 1),  -- Reveal: Faction initiator
  (52, 10, 1, 2),  -- Reveal: Faction executor
  (52, 10, 2, 3),  -- Reveal: ARBITER fulfiller
  (52, 2,  2, 1),  -- Remove: ARBITER initiator
  (52, 2,  2, 2),  -- Remove: ARBITER executor
  (52, 2,  2, 3);  -- Remove: ARBITER fulfiller
```

### Step 4 — Seed action primitives in tmp_action
```sql
-- trigger_type_id reference: 1=phase.open, 2=phase.during, 3=phase.closed,
--   4=rule.card, 5=rule.resolution, 6=player.introduce_card,
--   7=player.agreement, 8=player.verbal_statement, 9=state_condition, 10=cascade
-- subject_id: 1=Faction, 2=ARBITER

INSERT INTO tmp_action (beat_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
  (2,  'during', 4, 2, 1,  52, 'ARBITER distributes Countermeasure cards to Factions'),
  (4,  'during', 6, 1, 10, 52, 'Faction deploys Countermeasure card face-up'),
  (4,  'during', 6, 1, 17, 52, 'Faction invokes Countermeasure card effect'),
  (7,  'during', 4, 2, 2,  52, 'ARBITER discards Countermeasure card after resolution'),
  (10, 'during', 6, 1, 10, 52, 'Faction deploys Countermeasure card face-up'),
  (10, 'during', 6, 1, 17, 52, 'Faction invokes Countermeasure card effect'),
  (13, 'during', 4, 2, 2,  52, 'ARBITER discards Countermeasure card after resolution'),
  (16, 'during', 6, 1, 10, 52, 'Faction deploys Countermeasure card face-up'),
  (16, 'during', 6, 1, 17, 52, 'Faction invokes Countermeasure card effect'),
  (17, 'during', 4, 2, 2,  52, 'ARBITER discards Countermeasure card after resolution');
```

### Step 5 — Seed placement targets in tmp_subject_target
```sql
INSERT INTO tmp_subject_target (subject_id, target_id) VALUES
  (52, 30),  -- Countermeasure card → Arbiter Tableau (id=30)
  (52, 26);  -- Countermeasure card → Faction Terminal (id=26)
```

---

## 8. Row Counts

As of S50:
- `tmp_action`: **206 total rows, all root actions (prereq_id IS NULL)**
- `tmp_component`: **57 rows, next AUTO_INCREMENT = 98**
- `tmp_beat`: **20 rows** (fixed set — not AUTO_INCREMENT)
- `tmp_verb`: **8 rows** (id gaps from deprecated verbs)
- `tmp_trigger_type`: **10 rows**
- `tmp_function`: **12 rows**
- `tmp_layer`: **6 rows**

---

## 9. Open Design Notes / Known Gaps

- **DB-14** (PM05): Decision pending — promote tmp_ tables to permanent schema (drop tmp_ prefix). Evaluate after Art 04b sign-off.
- **DB-18** (PM05): Cross-beat modifier persistence not modeled. C06/C07/C10/C11/C12 play at Beat 2 but modify Beat 3/4 — no deferred-effect mechanism in tmp_action.
- **DB-19** (PM05): Concurrent Political acts (C09) not verified in resolution model.
- **DB-22** (PM05 — agy assigned): Upkeep beat (id=1) missing 3 primitives: Faction Flip Status marker (§7 Step 1), Faction Add Presence token (§7 Step 4), Faction Remove Deployment marker (§7 Step 4).
- **DB-23** (PM05 — agy assigned): Status marker (id=49) `transform_data=1` may be wrong (tracks orientation only, no written data). Debrief Flip Status marker has wrong component_id in tmp_action — uses id=2 (Deployment marker) instead of id=49.
- **DB-24** (PM05 — agy assigned): Portrait marker (id=51) missing from tmp_subject_target — Move=0 in v_comp_verb_matrix despite being its primary action.
- **DB-25** (PM05 — agy assigned): Situation Report card and Target Profile missing Remove primitives.
- **DB-26** (PM05 — agy assigned): Political act, Situation Report card, Target Profile have Move role permissions in tmp_comp_verb_role but zero Move primitives.
- **DB-09** (PM05): district_adjacency table — Art 01 signed off S40; DDL FK references `district_metadata(id)` but PK column name unconfirmed — verify with SHOW CREATE TABLE before executing.
- **tmp_category / tmp_type**: Deprecated. Drop and rebuild after Art 04b sign-off (DB-16).
- **destination_component_id / destination_zone_id** in tmp_action: Unpopulated — destination currently encoded in notes text only.

---

## 10. agy Sharing

This file is at `~/Projects/TheSignal/Database/` alongside all SQL build scripts. agy reads it via `GEMINI_CONTEXT.md` §DB Schema Reference. All schema changes go through dual-authorization: Claude Code proposes → Andy confirms → agy executes. Treat as read-only reference.

---

*Populated S50 — 2026-05-29. Update when schema changes are executed.*
