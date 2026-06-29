# the_signal_db — Schema Reference
**Status:** Complete — populated S50 (2026-05-29) · updated S117 (2026-06-24)  
**Priority:** DB-29 (PM05)

---

## Purpose

Single-file schema reference for `the_signal_db`. Eliminates the need for Claude Code and agy to issue exploratory queries (SHOW CREATE TABLE, DESCRIBE, FK checks, sample data pulls) at the start of every DB session. Read this file; skip the exploration.

**Connection — Claude Code:** `mysql the_signal_db` (no flags; ~/.my.cnf configured for claude user)  
**Connection — agy:** `mysql -u gemini -pgemini_password1 the_signal_db`

---

## 1. Critical FK Semantics — Read This First

The most expensive session mistake: assuming `comp_verb_role.phase_id` references beats. It does not.

**`comp_verb_role` — 4 FK columns:**

| Column | References | Values | What it means |
|--------|-----------|--------|---------------|
| `component_id` | `component(id)` | 1–97 | The physical component |
| `verb_id` | `verb(id)` | 1–17 | The action verb |
| `role_id` | `player_role(id)` | 1=Faction, 2=ARBITER | **Who** performs this action |
| `phase_id` | `role_phase(id)` | 1=initiator, 2=executor, 3=fulfiller | **What role** in the action chain |

**`phase_id` does NOT reference beats.** Column name is misleading. `role_phase` has 3 rows: 1=initiator, 2=executor, 3=fulfiller. This caused multiple rounds of FK constraint errors in S50.

**`action` subject vs. component:**

| Column | References | What it means |
|--------|-----------|---------------|
| `subject_id` | `player_role(id)` | Who performs this primitive (Faction=1 or ARBITER=2) |
| `component_id` | `component(id)` | What component is acted upon (nullable) |
| `destination_component_id` | `component(id)` | Where the component moves to (nullable — currently unpopulated) |
| `destination_zone_id` | `game_zones(id)` | Destination zone (nullable — legacy schema; currently unpopulated) |
| `prereq_id` | `action(id)` | Self-referential: prerequisite action in chain (NULL for root actions) |
| `source_action_id` | `action(id)` | Self-referential: Copy/Invoke source chain (NULL unless Copy) |

**`beat` is NOT referenced by `comp_verb_role` at all.** Beat assignments live in `comp_verb_phase`.

---

## 2. Core Design Principle — Snowflake Schema

The schema is a snowflake. Three tables are the center registry:

| Core table | Axis | What it registers |
|------------|------|-------------------|
| `components` | **What** | Every physical object in the game — one row per instance (District Tile, card, token, marker, deck, screen) |
| `game_zones` | **Where** | Every named location — districts, tableau areas, Dispatch Cases, the Reservoir, the Dossier |
| `game_actions` | **Verb** | Every action — the grammar of physical interaction (evolving into `action`) |

Every other table in the schema is one of:
- **Dimension** — classifies or describes a core table by its ID (e.g., `district_metadata` → `components`, `component` → `components`, `component_positions` → `components` + `game_zones`)
- **Sub-dimension** — a dimension of a dimension (e.g., `district_adjacency` → `district_metadata` → `components`; `component_dim` → `component` → `components`)
- **Metadata snowflake** — its own branching subtree anchored to a core table ID (e.g., `card_metadata` hangs off `components` via `master_blueprint_id`; `card_types`, `card_subtypes`, `card_faction_modifiers` are sub-dims of that snowflake)

No table should be designed without knowing which core axis it hangs from and at what distance. New tables: identify the core ID they reference (directly or through an intermediate dim), then place them in the snowflake accordingly.

---

## 3. Database Layout

### Two Schema Families

**Promoted design tables** — Active design workspace (formerly `tmp_` tables). These are the canonical source of truth for action primitives and component taxonomy. All design work happens here.

**Permanent manifest and early-schema tables** — Two distinct categories:

- **Physical manifest tables** (`components`, `district_metadata`, `district_adjacency`, `component_positions`, `factions`, `game_zones`, etc.) — Canonical registries of every physical object and location in the game. `components` is the master Bill of Materials: every District Tile, every individual card, every token, every marker — one row per physical thing. Currently seeded with 21 District Tiles; grows to encompass the full game component set. These are permanent-schema tables, not legacy placeholders.
- **Early-schema tables** (`action_costs`, `action_restrictions`, `action_valid_targets`, `game_actions`, `beat`, `card_metadata`, `card_types`, `card_subtypes`, etc.) — Predated the promoted design workspace. Structurally inconsistent with current design; reconciled via DB-14.

### Full Table List

**Promoted design tables (permanent schema):**
`action`, `beat`, `comp_verb_phase`, `comp_verb_role`, `component`, `component_faction`, `component_ring`, `condition`, `condition_clause`, `function`, `function_verb`, `layer`, `player_role`, `role_phase`, `state_condition`, `state_condition_clause`, `subject_target`, `trigger_type`, `verb`, `visibility_scope`, `category` (deprecated), `type` (deprecated)

**Physical manifest tables (permanent schema — active):**
`components`, `district_metadata`, `district_adjacency`, `component_positions`, `component_valid_zones`, `factions`, `game_zones`, `player_metadata`, `resource_types`, `city_rings`, `inteltoken_metadata`, `setup_state`

**Early-schema tables (predates promoted model — being replaced via DB-14):**
`action_costs`, `action_restrictions`, `action_valid_targets`, `allocation_types`, `beat`, `card_faction_modifiers`, `card_metadata`, `card_subtypes`, `card_types`, `district_connections`, `game_actions`

**Design tracking tables (card design workspace — S117):**
`card_status`, `card_subject_map`

---

## 2.5 Table Purposes & Relationships

### The Three-Table Cascade (Core Design Model)

The action primitive model is built from three tables that answer three different questions about the same (component × verb) pair. All three must be populated for a component to be fully modeled.

```
comp_verb_phase   — WHEN is this (component × verb) valid?
                       One row per (component, verb, beat).

comp_verb_role   — WHO performs this (component × verb), and in what role?
                       One row per (component, verb, player_role, action_phase).

action           — WHAT is the specific legal primitive?
                       One row per (beat, subject, verb, component) root action.
```

`comp_verb_phase` + `comp_verb_role` together define the **possibility space** — everything that could in principle be modeled. `action` is the **legal space** — what is actually legislated. The gap between them is visible via `v_unlegislated_primitives`. This relationship is locked as **L166**: taxonomy defines possibility; Art 03 defines legality. Gaps are procedure coverage signals, not errors.

`subject_target` is a fourth table in the cascade for components that Move: it answers WHERE can this component be placed/moved to.

### The Fundamental Snowflake Model (Core Database Schema Pillars)

The permanent layout of `the_signal_db` is architected as a **Snowflake Schema** centered around three fundamental entities that serve as the main anchor points of game state and rules logic. All other tables (metadata registries, logs, and relational staging tables) branch out as satellites from these three core snowflakes:

1. **`components` (The Physical Instance Registry):**
   * *Purpose:* The master Bill of Materials (BOM) tracking every individual physical piece (board, cards, tokens, markers) as a distinct entity instance in the box.
   * *Satellite Tables:*
     * `components` self-references via `parent_component_id` to handle hierarchical nesting.
     * `component` (formerly `component`) acts as the Component Type registry (defining operational properties, transform flags, and capabilities).
     * `district_metadata` extends `components` with district narrative/ring/resource values.
     * `card_metadata` extends `components` with blueprint parameters for coverts and Public Acts.
     * `component_positions` (formerly `live_state`) tracks instance locations.

2. **`game_zones` (The Spatial Grid):**
   * *Purpose:* The universal coordinate system of physical table-space where components can reside (e.g. `zone_overview`, `zone_backlog`, player tableaus).
   * *Satellite Tables:*
     * `component_positions` maps physical component instances directly to a `game_zone_id`.
     * `component_valid_zones` restricts component movements to specific valid physical zones.
     * `district_adjacency` establishes connectivity rules between spatial district zones.

3. **`action` (The Operational Grammar):**
   * *Purpose:* The rules engine registry defining all valid physical moves, phase triggers, prerequisites, and actors (Faction/ARBITER) in the game structure.
   * *Satellite Tables:*
     * `comp_verb_phase` and `comp_verb_role` map taxonomy design space.
     * `trigger_type`, `state_condition`, and `state_condition_clause` define the criteria under which actions fire.
     * `action_costs` and `action_restrictions` outline the mechanical constraints governing each action execution.

This three-snowflake core represents the target state of the permanent schema. The current table promotion (DB-14) dropped the `tmp_` prefixes to establish the permanent taxonomy tables, but does not yet merge the instance registries (`components`/`game_zones`) with the rule catalog (`action`). That unification will occur during L2+ integration.

### Per-Table Purpose

| Table | Purpose | Key question answered |
|-------|---------|----------------------|
| `component` | Component **type** registry. One row per type (not per physical copy). State-machine flags define what can be done to that type. Contains `parent_component_id` (self-referential FK) for hierarchy (e.g. Card -> card types). Classified by `component_type` and described in `component_dim`. | "What component types exist, and what are they capable of?" |
| `component_dim` | Component descriptions. Contains detailed descriptions for each component type. | "What does this component type do / represent?" |
| `component_type` | Component category classifications (e.g., card, token, marker, block, tile, etc.). | "What physical category does this component belong to?" |
| `verb` | Physical verb vocabulary. 8 verbs covering all primitive physical actions. | "What actions can be physically performed?" |
| `quarter_phase` | Beat and phase registry. 20 beats covering a full Quarter from Upkeep through Debrief. | "What are the named game phases, and when do they occur?" |
| `player_role` | Actor lookup. 2 values: Faction and ARBITER. Used as `role_id` in comp_verb_role and `subject_id` in action. | "Who are the two types of actors?" |
| `role_phase` | Action phase lookup. 3 values: initiator / executor / fulfiller. Used as `phase_id` in comp_verb_role — **not a beat reference**. | "What role does an actor play in an action chain?" |
| `comp_verb_phase` | Beat coverage matrix. Declares which beats a component×verb pair is in scope for. Does not specify who or how. | "At which beats is this component×verb combination valid?" |
| `comp_verb_role` | Role assignment matrix. Declares who (Faction or ARBITER) performs a component×verb action and in what phase role. Does not create primitives — only declares the design-space claim. | "Who performs this component×verb action, and as what role?" |
| `action` | Action primitive table. Each root row is one concrete, legally modeled action: (beat + trigger + subject + verb + component). This is the intersection of design space and Art 03 legal space. | "What specific actions are legally modeled in the game?" |
| `subject_target` | Placement target registry. Pairs a component (subject) with valid destination components (targets). Drives `Move=1` in v_comp_verb_matrix. | "Where can this component be placed or moved to?" |
| `trigger_type` | Trigger vocabulary. 10 types classifying what causes an action to fire (phase open/during/close, rule.card, player.introduce_card, state_condition, cascade, etc.). | "What event causes this action to become active?" |
| `function` | Card function vocabulary. 12 abstract functions (Add, Remove, Redirect, Protect, Block, Copy…) used in Art 04b taxonomy. Abstract layer above physical verbs. | "What does this card do in game-design terms?" |
| `function_verb` | Function → verb mapping. Bridges card design language (functions) to physical action language (verbs). Modify/Protect/Block have no verb mapping — they are constraint functions, not physical primitives. | "What physical verb does this card function resolve to?" |
| `layer` | Six-layer taxonomy (Territory / Economy / Information / Submission / Resolution / Standing). Classifies what layer of game reality a card affects. | "Which game layer does this card or action operate on?" |
| `visibility_scope` | VS-xx visibility codes. 8 scopes classifying who can see a piece of information during play. Referenced by layer and Art 04 §6 schema. | "Who can see this?" |
| `state_condition` | State condition header. Groups a set of game-state clauses with a logic operator (AND/OR). Used when trigger_type = state_condition. | "What combination of game state conditions triggers this?" |
| `state_condition_clause` | Individual game-state clause. One testable condition: (component, state_key, operator, value). Multiple clauses per condition combine via the parent's logic_operator. | "What is the specific state test in this condition?" |
| `component_faction` | Faction-specific component assignments. Maps components to factions that own or have special rules for them. | "Which faction owns or has exclusive access to this component?" |
| `component_ring` | Ring-specific component assignments. Maps components to rings where they are available or restricted. | "In which rings is this component valid?" |
| `category` / `type` | **Deprecated.** Old card taxonomy (Board / Resource / Action / Cross-Category). Superseded by the six-layer system (layer). Drop and rebuild after Art 04b sign-off (PM05 DB-16). | — |

### Relationship to Legacy Tables

The promoted model is a **design workspace** that partially overlaps with and partially extends the legacy schema:

| Promoted table | Legacy counterpart | Relationship |
|-----------|-------------------|--------------|
| `component` | `components` | Complementary, not competing. `component` = component **type** registry (what types exist, what they can do — state-machine flags, verb coverage). `components` = physical **instance** manifest (every individual object in the game box — each District Tile, each card, each token, each marker). Both are permanent; neither replaces the other. L169 (DB-32) adds `parent_component_id` to `component` for type hierarchy ("Card" → "Covert Operation Card" → outcome subtypes). `components` already has `parent_component_id` for instance grouping (e.g., individual cards grouped under their deck parent). The `master_blueprint_id` FK on `components` → `card_metadata` links physical card instances to their design blueprint. |
| `action` | `game_actions` | Different structures. `game_actions` = flat verb/definition catalog. `action` = full operational grammar (beat, trigger, subject, verb, component, prereq chain). Migration requires 00b §8 to define the target permanent structure before any DDL. |
| `verb` | `game_actions.action_verb` | Verbs are inline in `game_actions`; `verb` is a normalized lookup. |
| `quarter_phase` | `beat` | Parallel tables with similar purpose. `beat` is more fully populated and has richer metadata (month, beat_num, primary_agent, description). |
| `subject_target` | `action_valid_targets` | Overlapping purpose. `action_valid_targets` predates the promoted model and may be inconsistent with current design. |

**Migration is not ready** until: Art 04b is signed off, DB-22–26 are closed, and 00b §8 is updated with the reconciled permanent schema design. See PM05 DB-14.

### Views — Purpose by Group

Views are the primary interface to the model. They transform raw table data into actionable answers. All views are read-only and auto-update from base tables.

**Gap Analysis — "What's missing or wrong?"**

| View | Purpose |
|------|---------|
| `v_unlegislated_primitives` | Shows (beat, subject, verb, component) tuples that exist in the design space (comp_verb_phase × comp_verb_role phase_id=1) but have no matching root row in action. Primary audit tool. |
| `v_unlegislated_by_trigger` | Collapses v_unlegislated_primitives to (subject, verb, component) with beat_count. Answers: "what gaps exist across ALL beats?" — ignores which specific beat is missing. |
| `v_gap_executor_check` | For each gap in v_unlegislated_by_trigger, shows who the phase_id=2 executor is. ARBITER executor = expected gap (Faction declares, ARBITER executes physically — these are structural). Faction executor = true unmodeled gap requiring a design decision. |
| `v_component_coverage` | Every component with its primitive count. Zero on an actionable=1 component = nothing modeled for it. |
| `v_duplicate_primitives` | Detects duplicate (beat, subject, verb, component) rows where prereq_id IS NULL. Used to catch bulk-insert double-seeding (occurred in S48 — 37 duplicates removed). |
| `v_unassigned_triggers` | Primitives in action where trigger_type_id IS NULL. Used after bulk seeding to find rows that slipped through without a trigger type. |

**Primitive Browsing — "What's modeled?"**

| View | Purpose |
|------|---------|
| `v_primitives_with_trigger` | Full human-readable primitive list: beat name, trigger type, subject, verb, component, notes. The main view for reading what's in the model. |
| `v_primitives` | Simplified version without trigger type. |
| `v_action_by_phase` | Primitives grouped by beat. Useful for reviewing what a specific beat contains. |
| `v_faction_primitives` | All Faction-subject root primitives. |
| `v_arbiter_primitives` | All ARBITER-subject root primitives. |
| `v_faction_exclusive` | Primitives where only Faction acts (no ARBITER row for the same beat/verb/component). |
| `v_arbiter_exclusive` | Primitives where only ARBITER acts. |
| `v_arbiter_triggered` | ARBITER-initiated primitives specifically. |
| `v_split_agency` | Primitives where Faction initiates (phase_id=1) but ARBITER executes (phase_id=2). Captures the "player declares, referee executes" pattern that is structurally common. |
| `v_action_chain` | Prerequisite chains (prereq_id linkage). Currently empty — no multi-step chains are populated yet. |

**Coverage Matrices — "What can what do, and where?"**

| View | Purpose |
|------|---------|
| `v_comp_verb_matrix` | Per-component capability grid (Add / Remove / Move / Reveal / Conceal / Flip / Corrupt). **Important caveat:** Add and Remove are hardcoded to 1 for all actionable=1 components — they are NOT derived from action. Move=1 is derived from subject_target. Reveal/Conceal/Flip/Corrupt are derived from transform_ flags. The view shows design-space capability, not actual primitive coverage. |
| `v_placement_matrix` | Which components can be placed on which receivable target components. Derived from subject_target. Columns are the 13 receivable components; rows are all actionable components. |
| `v_phase_subject_coverage` | Per-beat primitive counts broken down by subject (Faction vs. ARBITER). Shows load ratio and under-populated beats. |
| `v_phase_role_matrix` | Role coverage (initiator/executor/fulfiller) per beat. |
| `v_trigger_phase_coverage` | Trigger types present in each beat. A beat with no `rule.card` or `player.*` triggers may be missing card-driven actions. |
| `v_trigger_summary` | Trigger type distribution across the full model. |
| `v_role_matrix` | Cross-reference of roles across components and verbs. |
| `v_phase_verb_summary` | Verb usage counts per beat. |
| `v_fulfiller_summary` | Fulfiller role coverage across the model. |

**Design-Layer Views — "How does card design connect to primitives?"**

| View | Purpose |
|------|---------|
| `v_layer_function_coverage` | Every Faction-initiatable Function × Component combination with beat availability. Bridges Art 04b taxonomy (functions) to the primitive model (verbs + beats). The design-space view for card design sessions. |
| `v_primitive_actual_coverage` | Actual primitive counts per (component, verb) — only rows with count > 0. Use alongside v_comp_verb_matrix to distinguish design-space capability from implemented primitives. |

**Migration impact on views:** All 27 views reference Promoted tables directly. Migrating to permanent tables requires rewriting every view. The view DDL is the migration's hidden cost — plan for it before executing any table rename.

---

## 3. Lookup Tables — Full Values

### verb (8 rows)

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

### player_role (2 rows)

| id | name |
|----|------|
| 1 | Faction |
| 2 | ARBITER |

### role_phase (3 rows)

| id | name | meaning |
|----|------|---------|
| 1 | initiator | Who decides/declares the action |
| 2 | executor | Who physically performs it |
| 3 | fulfiller | Who completes or receives the outcome |

### quarter_phase (20 rows)

| id | name | month | beat_num | primary_agent | description |
|----|------|-------|----------|---------------|-------------|
| 1 | Upkeep | NULL | NULL | Both | World updates, resources, tokens, initiative, Situation Reports |
| 2 | Placement | NULL | NULL | Both | Deployment Markers placed; entry requirements enforced; influence levels updated |
| 3 | Month 1 — Dispatch | M1 | NULL | Faction | Operations assembled, sealed, submitted with Dispatch Tokens |
| 4 | Month 1 — Countermeasures | M1 | NULL | Faction | Countermeasure Cards deployed; handed to ARBITER for Month 1 application |
| 5 | Month 1 — Beat 0 | M1 | 0 | Both | The Cases Open: ARBITER opens cases, sorts grid; factions validate submissions |
| 6 | Month 1 — Beat 1 | M1 | 1 | ARBITER | Check Active Restrictions: ARBITER removes ops violating restriction cards |
| 7 | Month 1 — Beat 2 | M1 | 2 | Both | The Ground Shifts: Modifier Cards resolve; ARBITER places Modifier Tokens |
| 8 | Month 1 — Beat 3 | M1 | 3 | ARBITER | Covert Operations Resolve: ARBITER resolves each op; board effects applied |
| 9 | Month 2 — Dispatch | M2 | NULL | Faction | Second covert pass; remaining Dispatch Tokens used |
| 10 | Month 2 — Countermeasures | M2 | NULL | Faction | Countermeasure Cards deployed for Month 2 |
| 11 | Month 2 — Beat 0 | M2 | 0 | Both | The Cases Open: Month 2 grid sorted |
| 12 | Month 2 — Beat 1 | M2 | 1 | ARBITER | Check Active Restrictions: Month 2 grid audited |
| 13 | Month 2 — Beat 2 | M2 | 2 | Both | The Ground Shifts: Month 2 modifier pass |
| 14 | Month 2 — Beat 3 | M2 | 3 | ARBITER | Covert Operations Resolve: Month 2 operations resolved |
| 15 | Month 3 — Declaration | M3 | NULL | Both | Public Acts declared face-up in initiative order |
| 16 | Month 3 — Countermeasures | M3 | NULL | Faction | Countermeasure Cards deployed for Month 3 |
| 17 | Month 3 — Beat 4 | M3 | 4 | Both | Political Acts Resolve: declared acts resolved; board and resource effects applied |
| 18 | Month 3 — Beat 5 | M3 | 5 | ARBITER | The Table Speaks: ARBITER updates Portrait, Chronicle, Session Timeline, Chorus Activity |
| 19 | Battlefield Strength | NULL | NULL | ARBITER | Contested districts resolved; d10 roll-off; Tension Markers cleared |
| 20 | Debrief | NULL | NULL | Both | Resource and Intel trades; ARBITER Debrief observation; Chorus Question window |

### layer (6 rows)

| id | name |
|----|------|
| 1 | Territory |
| 2 | Economy |
| 3 | Information |
| 4 | Submission |
| 5 | Resolution |
| 6 | Standing |

### trigger_type (10 rows)

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

### function (12 rows) and verb mappings

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

### visibility_scope (8 rows)

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

## 4. Table Schemas (Permanent tables)

### component
```sql
CREATE TABLE `component` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `actionable` tinyint(1) NOT NULL DEFAULT 0,            -- 1 = can be acted upon in action
  `receivable` tinyint(1) NOT NULL DEFAULT 0,            -- 1 = can be a target in subject_target
  `transformable` tinyint(1) GENERATED ALWAYS AS (`transform_visibility` <> 0 or `transform_orientation` <> 0 or `transform_data` <> 0) VIRTUAL, -- derived; never stored
  `transform_visibility` tinyint(1) NOT NULL DEFAULT 0,  -- 1 = can be Revealed/Concealed
  `transform_orientation` tinyint(1) NOT NULL DEFAULT 0, -- 1 = can be Flipped
  `transform_data` tinyint(1) NOT NULL DEFAULT 0,        -- 1 = carries written data that can be Corrupted
  `parent_component_id` int(11) DEFAULT NULL,            -- self-referential FK for component hierarchy
  PRIMARY KEY (`id`),
  KEY `fk_component_parent` (`parent_component_id`),
  CONSTRAINT `fk_component_parent` FOREIGN KEY (`parent_component_id`) REFERENCES `component` (`id`) ON DELETE SET NULL
)
```
### component_metadata
```sql
CREATE TABLE component_metadata (
  component_id INT NOT NULL,
  physical_form VARCHAR(2048) NOT NULL,
  quantity_expr VARCHAR(255) NOT NULL,
  visibility ENUM('Public', 'Player-private', 'ARBITER-only', 'Variable') NOT NULL,
  states VARCHAR(255) DEFAULT NULL,
  faction_keyed ENUM('Yes', 'No', 'N/A') NOT NULL DEFAULT 'N/A',
  max_placement_count INT DEFAULT NULL,
  max_placement_ref INT DEFAULT NULL,
  privacy_model ENUM('Open', 'Faction-private', 'ARBITER-private') DEFAULT NULL,
  display_fields VARCHAR(2048) DEFAULT NULL,
  back_design ENUM('Faction-keyed', 'Neutral', 'ARBITER-keyed') DEFAULT NULL,
  card_source ENUM('Deck', 'Hand', 'ARBITER supply', 'Sealed') DEFAULT NULL,
  recorded_fields VARCHAR(2048) DEFAULT NULL,
  function_prose VARCHAR(2048) DEFAULT NULL,
  scale_prose VARCHAR(2048) DEFAULT NULL,
  init_value_prose VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (component_id),
  CONSTRAINT fk_metadata_component FOREIGN KEY (component_id)
    REFERENCES component (id) ON DELETE CASCADE,
  CONSTRAINT fk_metadata_max_ref FOREIGN KEY (max_placement_ref)
    REFERENCES component (id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```
*Stores physical metrics, privacy mappings, back designs, and prose descriptions for components. Drops legacy `placement_surface` (resolved in `subject_target`) and `movement_path` (procedural).*

### component_dim
```sql
CREATE TABLE `component_dim` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `component_id` int(11) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comp_dim_component` (`component_id`),
  CONSTRAINT `fk_comp_dim_component` FOREIGN KEY (`component_id`) REFERENCES `component` (`id`) ON DELETE CASCADE
)
```
*Purpose: stores descriptions for each component. Art 02 Design Function text is the source.*

### component_type
```sql
CREATE TABLE `component_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `component_id` int(11) NOT NULL,
  `component_type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comp_type_component` (`component_id`),
  CONSTRAINT `fk_comp_type_component` FOREIGN KEY (`component_id`) REFERENCES `component` (`id`) ON DELETE CASCADE
)
```
*Purpose: stores category classifications (e.g. card, token, marker, block, tile, board, track, strip, screen, container, slip, slider, other).*

### comp_verb_phase
```sql
CREATE TABLE `comp_verb_phase` (
  `component_id` int(11) NOT NULL,   -- FK → component(id)
  `verb_id` int(11) NOT NULL,        -- FK → verb(id)
  `phase_id` int(11) NOT NULL,        -- FK → beat(id)
  `notes` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`component_id`,`verb_id`,`phase_id`)
)
```
*Purpose: declares which beats a component×verb combination is valid. Does not specify who or how — that is comp_verb_role.*

### comp_verb_role
```sql
CREATE TABLE `comp_verb_role` (
  `component_id` int(11) NOT NULL,  -- FK → component(id)
  `verb_id` int(11) NOT NULL,       -- FK → verb(id)
  `role_id` int(11) NOT NULL,       -- FK → player_role(id) — 1=Faction, 2=ARBITER
  `phase_id` int(11) NOT NULL,      -- FK → role_phase(id) — 1=initiator, 2=executor, 3=fulfiller
  `notes` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`component_id`,`verb_id`,`role_id`,`phase_id`)
)
```
**⚠ FK GOTCHA:** `role_id` → `player_role` (NOT a verb table). `phase_id` → `role_phase` (NOT a beat table). Column names are counterintuitive and have caused multiple FK constraint failures.

### action (206 rows as of S50)
```sql
CREATE TABLE `action` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phase_id` int(11) NOT NULL,                         -- FK → beat(id)
  `beat_trigger` enum('during','on_close') NOT NULL DEFAULT 'during',
  `trigger_type_id` int(11) DEFAULT NULL,             -- FK → trigger_type(id)
  `prereq_id` int(11) DEFAULT NULL,                   -- FK → action(id) self-ref; NULL = root action
  `source_action_id` int(11) DEFAULT NULL,            -- FK → action(id) self-ref; Copy source chain
  `subject_id` int(11) NOT NULL,                      -- FK → player_role(id) — who performs this
  `verb_id` int(11) NOT NULL,                         -- FK → verb(id)
  `component_id` int(11) DEFAULT NULL,                -- FK → component(id) — nullable
  `destination_component_id` int(11) DEFAULT NULL,    -- FK → component(id) — nullable; currently unpopulated
  `destination_zone_id` bigint(20) DEFAULT NULL,      -- FK → game_zones(id) — nullable; currently unpopulated
  `notes` text DEFAULT NULL,
  PRIMARY KEY (`id`)
)
```
*All 206 rows have `prereq_id IS NULL` (no multi-step chains populated yet).*

### subject_target
```sql
CREATE TABLE `subject_target` (
  `subject_id` int(11) NOT NULL,   -- component_id of the acting component (implicit FK → component)
  `target_id` int(11) NOT NULL,    -- component_id of the valid placement target (implicit FK → component)
  PRIMARY KEY (`subject_id`,`target_id`)
)
```
*No declared FKs. Used by v_comp_verb_matrix to determine Move=1 for a component.*

### card_ref
```sql
CREATE TABLE card_ref (
    card_id VARCHAR(15) NOT NULL,
    card_name VARCHAR(100) NOT NULL,
    layer VARCHAR(50) NOT NULL,
    function VARCHAR(50) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    PRIMARY KEY (card_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```
*Stores standard card references. Used for mapping card definitions to verbs/components via views.*

**card_ref.card_id format — L219**

Format: `[FAC].[TYPE].n`

| Code | Meaning |
|------|---------|
| FAC | Faction/owner: GHO, NET, SYN, GUI, DIR, STD, ARB, RNG |
| TYPE | Deck/pool code: CA, PA, MOD, OPR, APEX, CDIR, ER, CMA, CMB, BCAST, BCEV |
| n | Sequential integer within FAC+TYPE |

Special cases:
- `STD` = Standard (faction=All) — one spec, five physical copies (one per faction deck of matching type)
- `RNG` ring decks use format `RNG.[1/2/3].n` — ring number replaces TYPE slot
- `[FAC].ER` — Emergency Response has no sequence number; one card per faction IS the deck
- `STD.CMA.1` / `STD.CMB.1` — Countermeasure Cards; one spec each, faction copies (1× CMA, 2× CMB per faction)
- ARBITER card taxonomy = BCAST and BCEV only; ARB domain documents (Accord, Notif Slip, Grant Deed, Debrief Action Card) are NOT cards and have no card_id

`varchar(15)` constraint: all IDs must fit within 15 characters. `ARB.BCEV.99` = 11 chars (safe). Verify any new ID type fits before adding.


### card_status (95 cards as of S117)
```sql
CREATE TABLE `card_status` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `card_id` VARCHAR(15),           -- [FAC].[TYPE].n format; backfilled S117 (was NULL for pre-ID-04 cards)
  `name` VARCHAR(100),
  `faction` VARCHAR(20),
  `card_type` VARCHAR(10),          -- CA | PA | MOD | DA
  `blocked` TINYINT(1) DEFAULT 0,
  `design_pass` TINYINT(1) DEFAULT 0,
  `issues_resolved` TINYINT(1) DEFAULT 0,
  `issues_note` TEXT,
  `signed_off` TINYINT(1) DEFAULT 0,
  `art04_line` INT,
  `notes` TEXT,
  `layer` VARCHAR(30) NULL,         -- Art 04 §8 taxonomy layer (PascalCase) — added S117
  `function` VARCHAR(30) NULL,      -- Art 04 §8 taxonomy function (PascalCase) — added S117
  `subject` VARCHAR(50) NULL,       -- Art 04 §8 taxonomy subject (PascalCase, component name only) — added S117
  `beat` INT NULL,                  -- Resolution beat: 2=early-intervention CA, 3=standard covert grid CA, 4=PA — added S117
  `cost_type` ENUM('mono','cross','free') NULL,  -- native resource axis only; mono=all cost components use acting faction's own native; cross=at least one non-own native type; free=no native resource cost — added S119
  `cost_variable` TINYINT(1) NOT NULL DEFAULT 0, -- 1 if amount is play-determined (declared N, count-based, etc.) — orthogonal to cost_type — added S119
  `cost_primary_amount` INT NULL,   -- own-native units in cost; 0=explicitly none; NULL=variable/unknown — added S119
  `cost_native_count` INT NOT NULL DEFAULT 0,    -- distinct native resource types in cost (0=free, 1=mono or single-type cross, 2+=multi-type cross) — added S119
  `uses_intel_token` TINYINT(1) NOT NULL DEFAULT 0, -- 1 if Intel Token is part of the cost; orthogonal to cost_type — added S119
  `is_ring_modifier` TINYINT(1) DEFAULT 0           -- 1 if the card is a Ring Modifier (public pool, not drafted) — added S130 (DB-47)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```

**card_status — taxonomy field notes (S117):**
- `layer` / `function` / `subject` use PascalCase Art 04 names (not DB component table names). Join to `component` via `card_subject_map`.
- `beat` is the **resolution beat**, not submission beat. CA cards resolve on beat 2 (early-intervention: block/protect/modify/interfere cards) or beat 3 (standard covert grid). PA cards resolve on beat 4. MOD/DA cards have NULL beat.
- 77 of 95 cards have spec-accurate values (parsed from full card specs). 18 cards (stubs / BLOCKED / pre-renumber) have §8-level accuracy only.
- 5 blocked cards (GHO.CA.13/14, DIR.PA.4/5, GUI.MOD.1) carry taxonomy in DB but are excluded from §9-equivalent coverage queries — use `WHERE blocked=0`.
- S117 also corrected 3 `card_type` bugs: Regulatory Downgrade (CA→PA), Regulatory Freeze (CA→PA), Accord Leverage (CA→MOD).

**beat distribution (S117):** 27 CA beat=2 · 35 CA beat=3 · 27 PA beat=4 · 6 MOD/DA NULL

**card_status — cost columns (S119):**
- `cost_type` / `uses_intel_token` are orthogonal axes. Intel Token is not a faction native resource — a card with Intel Token cost and no native cost is `cost_type='free'` + `uses_intel_token=1`.
- `cost_type='mono'` = all native resource components use the acting faction's own native type (including `resource.faction(acting)` without subtype, which is always submitter-relative).
- `cost_type='cross'` = at least one native resource type in the cost is not the acting faction's native (district-native, target-faction-native, or a named type that doesn't match the card's faction native).
- `cost_type='free'` = no native resource cost component (may still have `uses_intel_token=1`).
- `cost_variable=1` = amount is play-determined (declared N, count-based). Orthogonal to `cost_type` — e.g., `capital * declared(N)` = mono + variable.
- `cost_native_count` = distinct native resource types in the cost (0=free, 1=mono or single-cross-type, 2+=multi-type cross).
- STD cards with `resource.faction(acting)` (no subtype) = mono regardless of submitter (submitter-relative). STD cards naming a specific faction's native type (e.g., Exposure, Capital, Mandate) = cross at design level.
- **Distribution (S119, 90 non-blocked cards):** mono/fixed=58 · mono/variable=4 · cross/fixed=14 · free/fixed=14. Intel Token cards=12.

### card_subject_map (S117)
```sql
CREATE TABLE `card_subject_map` (
  `subject`      VARCHAR(50) PRIMARY KEY,  -- PascalCase Art 04 taxonomy subject name
  `component_id` INT NULL,                 -- FK → component(id); NULL for non-component subjects
  FOREIGN KEY (`component_id`) REFERENCES `component`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```

Bridge table linking Art 04 taxonomy subject vocabulary (PascalCase) to the `component` table (spaced lowercase). Enables joins from `card_status` into all 27 gap views via `component_id`.

**26 rows seeded:**

| subject | component_id | component name |
|---------|-------------|----------------|
| Accord | 10 | Accord Agreement |
| AccordAgreement | 10 | Accord Agreement |
| AccordCard | 10 | Accord Agreement |
| BroadcastEffectCard | 98 | Broadcast Effect Card |
| ClassifiedDirective | 17 | Classified Directives |
| CovertOperation | 13 | Covert Operation |
| Debrief Action Card | 100 | Debrief Action Card |
| ModifierCard | 11 | Modifier Card |
| PublicAct | 14 | Public Act |
| DeploymentMarker | 2 | Deployment Marker |
| PresenceToken | 1 | Presence token |
| StandingMarker | 37 | Standing Marker |
| StructureBlock | 3 | Structure Block |
| District | 4 | District Tile |
| IntelDeliverySlip | 96 | Intel Delivery Slip |
| IntelToken | 9 | Intel Token |
| IntelTokensHeld | 9 | Intel Token |
| Exposure | 8 | Native Resource |
| FactionNativeResource | 8 | Native Resource |
| NativeResource | 8 | Native Resource |
| FactionHand | 94 | Faction Hand |
| PublicStanding | 21 | Public Standing |
| ActionAttribution | NULL | (who did what — not a component) |
| Difficulty | NULL | (modifier attribute — not a component) |
| InfluenceTier | NULL | (game state value — not a component) |
| NamedActionType | NULL | (card spec field — not a component) |

**Sample join to gap views:**
```sql
-- Which cards have subjects with no legislated primitives for their function verb?
SELECT cs.card_id, cs.name, cs.function, cs.subject, v.beat_name, v.verb_name
FROM card_status cs
JOIN card_subject_map csm ON cs.subject = csm.subject
JOIN v_unlegislated_primitives v ON csm.component_id = v.component_id
WHERE cs.blocked = 0 AND csm.component_id IS NOT NULL;
```

### trigger_type
```sql
CREATE TABLE `trigger_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  `subtype` varchar(30) DEFAULT NULL,
  `notes` text DEFAULT NULL,
  PRIMARY KEY (`id`)
)
```

### function / function_verb
```sql
CREATE TABLE `function` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`id`), UNIQUE KEY `name` (`name`)
)

CREATE TABLE `function_verb` (
  `function_id` int(11) NOT NULL,  -- FK → function(id)
  `verb_id` int(11) NOT NULL,      -- FK → verb(id)
  PRIMARY KEY (`function_id`,`verb_id`)
)
```

### layer
```sql
CREATE TABLE `layer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` text DEFAULT NULL,
  `default_visibility_id` tinyint(3) unsigned NOT NULL,  -- FK → visibility_scope(id)
  PRIMARY KEY (`id`), UNIQUE KEY `name` (`name`)
)
```

### state_condition / state_condition_clause
```sql
CREATE TABLE `state_condition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` text NOT NULL,
  `logic_operator` enum('AND','OR') NOT NULL DEFAULT 'AND',
  PRIMARY KEY (`id`)
)

CREATE TABLE `state_condition_clause` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `condition_id` int(11) NOT NULL,     -- FK → state_condition(id)
  `component_id` int(11) DEFAULT NULL, -- FK → component(id)
  `state_key` varchar(50) NOT NULL,
  `operator` enum('=','!=','>','<','>=','<=','ALL','ANY') NOT NULL DEFAULT '=',
  `value` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
)
```
*Lightly populated (2 rows each). Used for state-conditional trigger types.*

---

## 4.5. Lookup Tables (Phase 1)

### public_standing_tier, difficulty_tier, resolution_outcome, influence_level
```sql
CREATE TABLE public_standing_tier (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  range_min TINYINT NOT NULL,
  range_max TINYINT NOT NULL,
  drift_delta TINYINT NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO public_standing_tier (id, name, range_min, range_max, drift_delta) VALUES
  (1, 'Celebrated', 18, 20, -1),
  (2, 'Respected',  14, 17, -1),
  (3, 'Neutral',     7, 13,  0),
  (4, 'Suspect',     3,  6,  1),
  (5, 'Discredited', 0,  2,  1);

CREATE TABLE difficulty_tier (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  base_threshold TINYINT NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO difficulty_tier (id, name, base_threshold) VALUES
  (1, 'Easy', 75),
  (2, 'Average', 50),
  (3, 'Challenging', 25);

CREATE TABLE resolution_outcome (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO resolution_outcome (id, name) VALUES
  (1, 'Succeeded'),
  (2, 'Failed'),
  (3, 'Voided'),
  (4, 'Discovered'),
  (5, 'Auto-failed');

CREATE TABLE influence_level (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  chip_threshold TINYINT NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO influence_level (id, name, chip_threshold) VALUES
  (1, 'Dominant',    3),
  (2, 'Established', 2),
  (3, 'Present',     1),
  (4, 'None',        0);
```
*Seeded lookup tables for core rules metrics.*

---

## 4.6. Slip Content Tables (Phase 2)

### notification_slip, intel_delivery_slip
```sql
CREATE TABLE notification_slip (
  id INT NOT NULL AUTO_INCREMENT,
  slip_type VARCHAR(50) NOT NULL DEFAULT 'Target Warning',
  trigger_condition VARCHAR(255) NOT NULL,
  body_text TEXT NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE intel_delivery_slip (
  slip_id INT NOT NULL AUTO_INCREMENT,
  recipient_faction_id BIGINT(20) NOT NULL,
  delivery_quarter TINYINT NOT NULL,
  delivery_month TINYINT NOT NULL,
  submitting_faction_id BIGINT(20) DEFAULT NULL,
  covert_operation_card_id VARCHAR(15) DEFAULT NULL,
  target_faction_id BIGINT(20) DEFAULT NULL,
  target_district_id INT(11) DEFAULT NULL,
  operation_type VARCHAR(50) DEFAULT NULL,
  boost_marker_present CHAR(1) NOT NULL DEFAULT 'N',
  modifier_token_total INT DEFAULT NULL,
  PRIMARY KEY (slip_id),
  CONSTRAINT fk_ids_recipient FOREIGN KEY (recipient_faction_id) REFERENCES factions(id) ON DELETE RESTRICT,
  CONSTRAINT fk_ids_submitting FOREIGN KEY (submitting_faction_id) REFERENCES factions(id) ON DELETE SET NULL,
  CONSTRAINT fk_ids_target_faction FOREIGN KEY (target_faction_id) REFERENCES factions(id) ON DELETE SET NULL,
  CONSTRAINT fk_ids_target_district FOREIGN KEY (target_district_id) REFERENCES component(id) ON DELETE SET NULL,
  CONSTRAINT fk_ids_covert_card FOREIGN KEY (covert_operation_card_id) REFERENCES card_ref(card_id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```
*Stores written and recorded data for Notification and Intel Delivery Slips. Intel Delivery Slips are modeled with explicit foreign keys to track sender, target, and outcome specifics privately.*

---

## 5. Component Registry (component — 77 active rows as of S104; id=1 and id=14 renamed S117)

| id | name | act | xfm | rcv | vis | ori | dat | par |
|----|------|-----|-----|-----|-----|-----|-----|-----|
| 1 | Presence token | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 2 | Deployment Marker | 1 | 1 | 0 | 0 | 1 | 0 | NULL |
| 3 | Structure Block | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 4 | District Tile | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 5 | Established Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 6 | Dominant Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 7 | Tension Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 8 | Native Resource | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 9 | Intel Token | 1 | 1 | 0 | 1 | 0 | 1 | NULL |
| 10 | Accord Agreement | 1 | 1 | 0 | 1 | 0 | 1 | NULL |
| 11 | Modifier Card | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 12 | Dispatch Token | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 13 | Covert Operation | 1 | 1 | 1 | 1 | 0 | 0 | 111 |
| 14 | Public Act | 1 | 1 | 1 | 1 | 0 | 0 | 111 |
| 15 | Operative Card | 1 | 1 | 0 | 1 | 0 | 1 | 111 |
| 17 | Classified Directives | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 21 | Public Standing | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 23 | Session Timeline | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 24 | Initiative Strip | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 25 | Broadcast Card | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 26 | Faction Terminal | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 27 | Faction Screen | 0 | 0 | 0 | 0 | 0 | 0 | NULL |
| 28 | ARBITER Screen | 0 | 0 | 0 | 0 | 0 | 0 | NULL |
| 29 | The Overview | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 30 | ARBITER Tableau | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 31 | Chorus Activity Track | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 32 | Reservoir | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 33 | Backlog | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 34 | Pointer Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 35 | Activity Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 36 | Escalation Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 37 | Standing Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 38 | Faction Order Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 42 | ARBITER Dominance Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 43 | Human Player | 0 | 0 | 0 | 0 | 0 | 0 | NULL |
| 44 | Dispatch Case | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 47 | Modifier Token | 1 | 1 | 0 | 0 | 1 | 0 | NULL |
| 48 | Target Profile | 1 | 1 | 0 | 1 | 0 | 1 | NULL |
| 49 | Status Marker | 1 | 1 | 0 | 0 | 1 | 0 | NULL |
| 50 | Chorus Portrait track | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 51 | Portrait Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 52 | Countermeasure Card | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 53 | Ring 1 Modifier Deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 54 | Ring 2 Modifier Deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 55 | Ring 3 Modifier Deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 86 | Broadcast Deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 87 | Broadcast Effect Deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 88 | Faction Resolution Grid | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 89 | Faction Modifier Deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 90 | Public Act Deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 91 | Public Act Discard | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 92 | Covert Operation Deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 93 | Covert Operation Discard | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 94 | Faction Hand | 1 | 1 | 1 | 1 | 0 | 1 | NULL |
| 95 | Notification Slip | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 96 | Intel Delivery Slip | 1 | 1 | 1 | 1 | 0 | 1 | NULL |
| 97 | Emergency Response card | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 98 | Broadcast Effect Card | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 99 | Sealed Apex ability | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 100 | Debrief Action Card | 1 | 1 | 1 | 1 | 0 | 1 | NULL |
| 102 | Situation Report | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 103 | Visibility Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 104 | Boost Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 105 | ARBITER Covert Resolution Grid | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 106 | ARBITER Threshold Slider | 1 | 1 | 0 | 0 | 0 | 1 | NULL |
| 107 | Faction Threshold Slider | 1 | 1 | 0 | 0 | 0 | 1 | NULL |
| 108 | Dispatch Packet | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 109 | Broadcast Discard | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 110 | Broadcast Effect Discard | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 111 | Card | 0 | 0 | 0 | 0 | 0 | 0 | NULL |
| 113 | Grant Deed | 1 | 1 | 1 | 1 | 0 | 1 | NULL |
| 114 | Covert Operation Card Set | 1 | 1 | 0 | 1 | 0 | 0 | NULL |
| 115 | Public Act Card Set | 1 | 1 | 0 | 1 | 0 | 0 | NULL |
| 116 | Operative Pool | 1 | 1 | 0 | 1 | 0 | 1 | NULL |
| 117 | Apex Ability Pool | 1 | 1 | 0 | 1 | 0 | 0 | NULL |
| 118 | Classified Directives Pool | 1 | 1 | 0 | 1 | 0 | 0 | NULL |
| 119 | d10 | 1 | 1 | 0 | 0 | 1 | 0 | NULL |

*Column key: act=actionable, xfm=transformable, rcv=receivable, vis=transform_visibility, ori=transform_orientation, dat=transform_data, par=parent_component_id*  
*IDs are non-sequential (gaps from deleted rows during schema evolution).*  
*Next AUTO_INCREMENT = 120.*

*Note on ids 100 and 113:* `Debrief Action Card` (100) and `Grant Deed` (113) are physical game documents (ARBITER domain), not card-type components, and thus have `parent_component_id = NULL` (they do not belong to the `Card` hierarchy).
*Note on ids 116, 117, and 118:* `Operative Pool` (116), `Apex Ability Pool` (117), and `Classified Directives Pool` (118) are faction-specific components (one instance per faction) rather than board-level or non-faction components.


---

## 6. View Catalog (27 views)

### Gap Analysis Views — Use These First

| View | What it answers |
|------|----------------|
| `v_unlegislated_primitives` | (beat, subject, verb, component) tuples in the taxonomy with no matching root row in action. Current answer to "what's covered in the design model but not in the action primitive table?" |
| `v_unlegislated_by_trigger` | Same but collapsed to (subject, verb, component) with beat_count — gaps across ALL beats |
| `v_gap_executor_check` | For each unlegislated gap, who is the phase_id=2 executor? ARBITER executor = expected gap (Faction initiates, ARBITER executes physically). Faction executor = true unmodeled gap |
| `v_component_coverage` | Every component with its primitive count. Zero = no actions modeled |
| `v_duplicate_primitives` | Duplicate (beat, subject, verb, component) rows where prereq_id IS NULL |
| `v_unassigned_triggers` | Primitives in action where trigger_type_id IS NULL |

### Primitive Browse Views

| View | What it answers |
|------|----------------|
| `v_primitives_with_trigger` | Full readable primitive list: beat, trigger_type.subtype, subject, verb, component, notes |
| `v_primitives` | Simplified primitive list (no trigger type) |
| `v_action_by_phase` | Actions grouped by beat |
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
| `v_comp_verb_matrix` | Per-component capability grid: Add/Remove/Move/Reveal/Conceal/Flip/Corrupt. **Note: Add and Remove hardcoded to 1 for all actionable components** — not derived from action. Move=1 if component is in subject_target. Others derived from transform_ flags |
| `v_primitive_actual_coverage` | Actual primitive counts per (component, verb) — only rows with count > 0. Use alongside v_comp_verb_matrix to see which design-space capabilities have real primitives in action |
| `v_placement_matrix` | Which components can be placed on which receivable target components (from subject_target) |
| `v_phase_subject_coverage` | Per-beat: verb count, component count, primitive count by subject |
| `v_phase_role_matrix` | Role coverage per beat |
| `v_trigger_phase_coverage` | Trigger types present in each beat |
| `v_trigger_summary` | Trigger distribution by subject |
| `v_role_matrix` | Role assignment matrix |
| `v_phase_verb_summary` | Verb usage per beat |
| `v_fulfiller_summary` | Fulfiller role coverage |
| `v_layer_function_coverage` | Every Faction-initiatable Function × Component with beat availability |
**§9 Faction Coverage Matrix — DB-derivable (S117):** Art 04 §9 is now a live query, not a maintained markdown table. Pivot `card_status` by faction × layer × function × subject (with `blocked=0`) to reproduce it. The `card_status` taxonomy columns are the canonical source; §9 in Art 04 is the documentation snapshot.

---

## 6.5. Component Metadata Views DDL (DB-37)

### v_component_accommodates, v_component_contains, v_component_held_by
```sql
CREATE OR REPLACE VIEW v_component_accommodates AS
SELECT 
  st.target_id AS target_component_id,
  c_target.name AS target_component_name,
  st.subject_id AS placed_component_id,
  c_subject.name AS placed_component_name
FROM subject_target st
JOIN component c_target ON st.target_id = c_target.id
JOIN component c_subject ON st.subject_id = c_subject.id;

CREATE OR REPLACE VIEW v_component_contains AS
SELECT 
  st.target_id AS container_component_id,
  c_target.name AS container_component_name,
  st.subject_id AS contained_component_id,
  c_subject.name AS contained_component_name
FROM subject_target st
JOIN component c_target ON st.target_id = c_target.id
JOIN component c_subject ON st.subject_id = c_subject.id;

CREATE OR REPLACE VIEW v_component_held_by AS
SELECT 
  cm.component_id AS component_id,
  c.name AS component_name,
  cm.max_placement_ref AS placement_surface_id,
  c_ref.name AS placement_surface_name
FROM component_metadata cm
JOIN component c ON cm.component_id = c.id
JOIN component c_ref ON cm.max_placement_ref = c_ref.id;
```
*Derived component metadata views used to traverse placement, containment, and surface relationships. Views depending on legacy movement_path are dropped.*

---

## 6.6. Card Alignment and Coverage Views DDL

### v_card_mechanical_alignment
```sql
CREATE OR REPLACE VIEW v_card_mechanical_alignment AS
SELECT 
  cs.card_id,
  cs.name AS card_name,
  cs.faction,
  cs.card_type,
  cs.blocked,
  cs.layer AS design_layer,
  cs.function AS design_function,
  cs.subject AS design_subject,
  csm.component_id,
  c.name AS component_name,
  v.id AS verb_id,
  v.name AS verb_name,
  cs.beat AS design_beat,
  CASE 
    WHEN cs.subject IS NULL THEN 'Abstract / No Subject'
    WHEN csm.component_id IS NULL THEN 'Non-component Subject'
    WHEN fv.verb_id IS NULL THEN 'Abstract Function (No Mechanical Verb)'
    WHEN cvp.component_id IS NOT NULL THEN 'Legalized'
    ELSE 'Rules Gap (Verb not permitted on component)'
  END AS rules_status,
  IF(a.id IS NULL, 0, 1) AS is_modeled_in_timeline,
  GROUP_CONCAT(DISTINCT a.phase_id ORDER BY a.phase_id) AS timeline_beats
FROM card_status cs
LEFT JOIN card_subject_map csm ON cs.subject = csm.subject
LEFT JOIN component c ON csm.component_id = c.id
LEFT JOIN function f ON cs.function = f.name
LEFT JOIN function_verb fv ON f.id = fv.function_id
LEFT JOIN verb v ON fv.verb_id = v.id
LEFT JOIN comp_verb_phase cvp ON cvp.component_id = c.id AND cvp.verb_id = fv.verb_id
LEFT JOIN action a ON a.verb_id = v.id AND a.component_id = c.id
GROUP BY cs.id, fv.verb_id;
```

### v_card_cost_structural_patterns
```sql
CREATE OR REPLACE VIEW v_card_cost_structural_patterns AS
SELECT 
  cs.card_id,
  cs.name AS card_name,
  cs.faction,
  cs.card_type,
  cs.layer AS design_layer,
  cs.function AS design_function,
  cs.subject AS design_subject,
  cs.cost_type,
  cs.cost_variable,
  cs.cost_primary_amount,
  cs.cost_native_count,
  cs.uses_intel_token,
  CASE 
    WHEN cs.cost_type = 'cross' THEN 'Cross-faction cooperation/trade required'
    WHEN cs.cost_type = 'mono' AND cs.cost_variable = 1 THEN 'Scaling native resource expenditure'
    WHEN cs.cost_type = 'mono' AND cs.cost_variable = 0 THEN 'Standard native resource expenditure'
    WHEN cs.cost_type = 'free' AND cs.uses_intel_token = 1 THEN 'Intel-gated free action'
    ELSE 'Completely free action'
  END AS cost_pattern_description
FROM card_status cs
WHERE cs.blocked = 0;
```

### v_card_subject_action_matrix
```sql
CREATE OR REPLACE VIEW v_card_subject_action_matrix AS
SELECT 
  cs.subject AS design_subject,
  c.name AS component_name,
  SUM(CASE WHEN cs.faction = 'Standard' THEN 1 ELSE 0 END) AS std_count,
  SUM(CASE WHEN cs.faction = 'Directorate' THEN 1 ELSE 0 END) AS dir_count,
  SUM(CASE WHEN cs.faction = 'Ghost' THEN 1 ELSE 0 END) AS gho_count,
  SUM(CASE WHEN cs.faction = 'Guild' THEN 1 ELSE 0 END) AS gui_count,
  SUM(CASE WHEN cs.faction = 'Network' THEN 1 ELSE 0 END) AS net_count,
  SUM(CASE WHEN cs.faction = 'Syndicate' THEN 1 ELSE 0 END) AS syn_count,
  COUNT(*) AS total_cards
FROM card_status cs
LEFT JOIN card_subject_map csm ON cs.subject = csm.subject
LEFT JOIN component c ON csm.component_id = c.id
WHERE cs.blocked = 0
GROUP BY cs.subject;
### v_card_faction_layer_balance
```sql
CREATE OR REPLACE VIEW v_card_faction_layer_balance AS
SELECT 
  cs.layer AS design_layer,
  SUM(CASE WHEN cs.faction = 'Standard' THEN 1 ELSE 0 END) AS std_count,
  SUM(CASE WHEN cs.faction = 'Directorate' THEN 1 ELSE 0 END) AS dir_count,
  SUM(CASE WHEN cs.faction = 'Ghost' THEN 1 ELSE 0 END) AS gho_count,
  SUM(CASE WHEN cs.faction = 'Guild' THEN 1 ELSE 0 END) AS gui_count,
  SUM(CASE WHEN cs.faction = 'Network' THEN 1 ELSE 0 END) AS net_count,
  SUM(CASE WHEN cs.faction = 'Syndicate' THEN 1 ELSE 0 END) AS syn_count,
  COUNT(*) AS total_cards
FROM card_status cs
WHERE cs.blocked = 0 AND cs.layer IS NOT NULL
GROUP BY cs.layer;
```

### v_card_duplication_auditor
```sql
CREATE OR REPLACE VIEW v_card_duplication_auditor AS
SELECT 
  cs_faction.card_id AS faction_card_id,
  cs_faction.name AS faction_card_name,
  cs_faction.faction AS faction_name,
  cs_std.card_id AS std_card_id,
  cs_std.name AS std_card_name,
  cs_faction.layer AS design_layer,
  cs_faction.function AS design_function,
  cs_faction.subject AS design_subject
FROM card_status cs_faction
JOIN card_status cs_std ON 
  cs_faction.layer = cs_std.layer AND 
  cs_faction.function = cs_std.function AND 
  cs_faction.subject = cs_std.subject
WHERE cs_faction.faction <> 'Standard' AND cs_std.faction = 'Standard'
  AND cs_faction.blocked = 0 AND cs_std.blocked = 0;
```
*Analytical views bridging high-level design card status and taxonomy metadata to mechanical action/verb schemas and resource cost patterns.*

---

## 7. Canonical Component Registration Pattern

Use **Countermeasure Card (id=52)** as the reference. Full 4-table cascade required for every new component.

### Step 1 — Register in component
```sql
INSERT INTO component (name, actionable, receivable,
  transform_visibility, transform_orientation, transform_data)
VALUES ('Component Name', 1, 0, 1, 0, 0);
-- transformable is VIRTUAL GENERATED — omit from INSERT
-- Next AUTO_INCREMENT = 98 as of S50
```

### Step 2 — Seed beat coverage in comp_verb_phase
One row per valid (component, verb, beat) combination.
```sql
-- Countermeasure Card (id=52) example:
INSERT INTO comp_verb_phase (component_id, verb_id, phase_id) VALUES
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

### Step 3 — Seed role assignments in comp_verb_role
**⚠ role_id → player_role (1=Faction, 2=ARBITER); phase_id → role_phase (1=initiator, 2=executor, 3=fulfiller)**
```sql
-- Countermeasure Card (id=52) example:
INSERT INTO comp_verb_role (component_id, verb_id, role_id, phase_id) VALUES
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

### Step 4 — Seed action primitives in action
```sql
-- trigger_type_id reference: 1=phase.open, 2=phase.during, 3=phase.closed,
--   4=rule.card, 5=rule.resolution, 6=player.introduce_card,
--   7=player.agreement, 8=player.verbal_statement, 9=state_condition, 10=cascade
-- subject_id: 1=Faction, 2=ARBITER

INSERT INTO action (phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) VALUES
  (2,  'during', 4, 2, 1,  52, 'ARBITER distributes Countermeasure Cards to Factions'),
  (4,  'during', 6, 1, 10, 52, 'Faction deploys Countermeasure Card face-up'),
  (4,  'during', 6, 1, 17, 52, 'Faction invokes Countermeasure Card effect'),
  (7,  'during', 4, 2, 2,  52, 'ARBITER discards Countermeasure Card after resolution'),
  (10, 'during', 6, 1, 10, 52, 'Faction deploys Countermeasure Card face-up'),
  (10, 'during', 6, 1, 17, 52, 'Faction invokes Countermeasure Card effect'),
  (13, 'during', 4, 2, 2,  52, 'ARBITER discards Countermeasure Card after resolution'),
  (16, 'during', 6, 1, 10, 52, 'Faction deploys Countermeasure Card face-up'),
  (16, 'during', 6, 1, 17, 52, 'Faction invokes Countermeasure Card effect'),
  (17, 'during', 4, 2, 2,  52, 'ARBITER discards Countermeasure Card after resolution');
```

### Step 5 — Seed placement targets in subject_target
```sql
INSERT INTO subject_target (subject_id, target_id) VALUES
  (52, 30),  -- Countermeasure Card → ARBITER Tableau (id=30)
  (52, 26);  -- Countermeasure Card → Faction Terminal (id=26)
```

---

## 8. Row Counts

As of S50 (unchanged unless noted):
- `action`: **213 total rows, all root actions (prereq_id IS NULL)**
- `component`: **77 rows, next AUTO_INCREMENT = 120** *(updated — S104 was 77 rows; S117 renamed id=1 and id=14)*
- `beat`: **20 rows** (fixed set — not AUTO_INCREMENT)
- `verb`: **8 rows** (id gaps from deprecated verbs)
- `trigger_type`: **10 rows**
- `function`: **12 rows**
- `layer`: **6 rows**

As of S117 (new):
- `card_status`: **95 rows** (77 with spec-accurate taxonomy; 18 at §8-level accuracy)
- `card_subject_map`: **26 rows** (22 mapped to component_id; 4 NULL for non-component subjects)

---

## 9. Open Design Notes / Known Gaps

- **DB-14** ✅ S50 (agy): Promoted all 20 design tables to permanent schema (dropped tmp_ prefix) and recompiled all 27 views.
- **DB-3NF** ✅ S63 (L184): 3NF applied. `component.transformable` → VIRTUAL GENERATED (derived from transform_ flags). `action.prereq_beat_id` dropped — prereq beat resolved dynamically via `prereq_id → action.phase_id`. `v_action_chain` rewritten. L108 amended (Requirements 6–7). `card_metadata` 3NF deferred to Art 04.6.
- **DB-18** (PM05): Cross-beat modifier persistence not modeled. C06/C07/C10/C11/C12 play at Beat 2 but modify Beat 3/4 — no deferred-effect mechanism in action.
- **DB-19** (PM05): Concurrent Public Acts (C09) not verified in resolution model.
- **DB-22** ✅ S50 (agy): Upkeep primitives seeded — Faction/ARBITER Flip Status Marker (ids 295/296), Faction/ARBITER Add Presence token (ids 297/298), Faction/ARBITER Remove Deployment Marker (ids 299/300), ARBITER Move Situation Report card (id 301).
- **DB-23** ✅ S50 (agy): Status Marker `transform_data` corrected to 0. Debrief Flip Status Marker FK corrected to component id=49.
- **DB-24** ✅ S50 (agy): Portrait Marker (id=51) registered in subject_target. Move primitives seeded.
- **DB-25** ✅ S50 (agy): Design-confirmed — Situation Report cards move to expired area (not removed); Target Profiles returned in Dispatch Case. No Remove primitive needed per Art 03.
- **DB-26** ✅ S50 (agy): Move role permissions verified against Art 03. Public Act, Situation Report card, Target Profile resolved.
- **DB-09** ✅ S50 (agy): district_adjacency created and fully seeded — 21 district components in `components`, 21 rows in `district_metadata`, 104 bidirectional adjacency rows. PKs enforced on district_metadata and player_metadata.
- **category / type**: Deprecated. Drop and rebuild after Art 04b sign-off (DB-16).
- **destination_component_id / destination_zone_id** in action: Unpopulated — destination currently encoded in notes text only.
- **S126 agy audit fixes:** (1) Five cards (STD.CA.13, STD.PA.4, STD.PA.7, DIR.CA.7, NET.CA.7) corrected from `subject = PublicStanding` → `subject = StandingMarker` in `card_status`; `StandingMarker` (id 37) added to `card_subject_map`. (2) NET.CA.1 Leak corrected from `subject = District` → `subject = CovertOperation` — S68 correction was also a mismatch; the card reveals a `CovertOperation`, not the district tile. (3) BroadcastEffectCard (id 98) added to `comp_verb_phase`: Add at phase 2; Remove/Reveal/Invoke at phases 17 and 18 (Beat 4 / Beat 5). All 7 cards now Legalized in `v_card_mechanical_alignment`. Art 04 specs updated to match.

---

## 10. Audit & Maintenance Scripts

### audit_card_alignment.sql

**Purpose:** Identifies active cards whose taxonomy subjects are not legalized in `comp_verb_phase`. The primary diagnostic for card taxonomy health.

**Usage:**
```bash
mysql the_signal_db < Database/audit_card_alignment.sql
```

**When to run:** After any card spec change (new card, subject/function update), after `card_subject_map` additions, or after `comp_verb_phase` updates. Also after agy taxonomy audits to confirm all gaps are closed.

**Output — four sections:**

| Section | rules_status | Meaning | Action |
|---------|-------------|---------|--------|
| 1 | Summary | Count by status | — |
| 2 | Rules Gap (Verb not permitted on component) | Verb mapped but not permitted on this component | Fix: correct `card_status.subject`; ensure subject in `card_subject_map`; add entry to `comp_verb_phase`; update Art 04 spec |
| 3 | Non-component Subject | Subject not in `card_subject_map` or maps to NULL | Fix: add row to `card_subject_map` if component-backed; leave NULL if intentionally abstract |
| 4 | Abstract Function (No Mechanical Verb) | Function has no `function_verb` entry | Design gap — not an error; tracked separately |

**Fix pattern for Rules Gaps (three-table chain):**
```sql
-- Step 1: correct the card's subject in card_status
UPDATE card_status SET subject = 'CorrectSubject' WHERE card_id = 'FAC.TYPE.n';

-- Step 2: ensure subject exists in card_subject_map (add if missing)
INSERT INTO card_subject_map (subject, component_id) VALUES ('CorrectSubject', <component_id>);

-- Step 3: ensure verb is permitted on the component at the relevant phase(s)
INSERT INTO comp_verb_phase (component_id, verb_id, phase_id, notes) VALUES
  (<component_id>, <verb_id>, <phase_id>, '<rationale>');
```
Then update the Art 04 card spec `subject` field to match. Verify with:
```sql
SELECT card_id, rules_status FROM v_card_mechanical_alignment WHERE card_id = 'FAC.TYPE.n';
```

### verify_matrix.py

**Purpose:** Compares `v_comp_verb_matrix` (DB) against `applicable_verbs` in Art 02 component entries. Catches drift between Art 02 design intent and DB capability seeding.

**Usage:**
```bash
python3 Database/verify_matrix.py
```

**Relationship to audit_card_alignment.sql:** Complementary, not overlapping. `verify_matrix.py` checks component verb *capabilities* (can this component be acted on at all?). `audit_card_alignment.sql` checks card *taxonomy subjects* (is this specific card's subject legalized for its function verb?).

---

## 11. agy Sharing

This file is at `~/Projects/TheSignal/Database/` alongside all SQL build scripts. agy reads it via `GEMINI_CONTEXT.md` §DB Schema Reference. All schema changes go through dual-authorization: Claude Code proposes → Andy confirms → agy executes. Treat as read-only reference.

---

*Populated S50 — 2026-05-29. Updated S117 — 2026-06-24: added card_status taxonomy columns (layer/function/subject/beat), new card_subject_map table, component renames (id=1 Presence token, id=14 Public Act), §9 DB-derivable note. Updated S126 — 2026-06-27: StandingMarker (id 37) added to card_subject_map; BroadcastEffectCard (id 98) seeded in comp_verb_phase (phases 2/17/18); 7-card taxonomy subject corrections logged in §9.*
