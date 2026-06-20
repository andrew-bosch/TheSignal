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
| `components` | **What** | Every physical object in the game — one row per instance (district tile, card, token, marker, deck, screen) |
| `game_zones` | **Where** | Every named location — districts, tableau areas, dispatch cases, the Reservoir, the Dossier |
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

- **Physical manifest tables** (`components`, `district_metadata`, `district_adjacency`, `component_positions`, `factions`, `game_zones`, etc.) — Canonical registries of every physical object and location in the game. `components` is the master Bill of Materials: every district tile, every individual card, every token, every marker — one row per physical thing. Currently seeded with 21 district tiles; grows to encompass the full game component set. These are permanent-schema tables, not legacy placeholders.
- **Early-schema tables** (`action_costs`, `action_restrictions`, `action_valid_targets`, `game_actions`, `beat`, `card_metadata`, `card_types`, `card_subtypes`, etc.) — Predated the promoted design workspace. Structurally inconsistent with current design; reconciled via DB-14.

### Full Table List

**Promoted design tables (permanent schema):**
`action`, `beat`, `comp_verb_phase`, `comp_verb_role`, `component`, `component_faction`, `component_ring`, `condition`, `condition_clause`, `function`, `function_verb`, `layer`, `player_role`, `role_phase`, `state_condition`, `state_condition_clause`, `subject_target`, `trigger_type`, `verb`, `visibility_scope`, `category` (deprecated), `type` (deprecated)

**Physical manifest tables (permanent schema — active):**
`components`, `district_metadata`, `district_adjacency`, `component_positions`, `component_valid_zones`, `factions`, `game_zones`, `player_metadata`, `resource_types`, `city_rings`, `inteltoken_metadata`, `setup_state`

**Early-schema tables (predates promoted model — being replaced via DB-14):**
`action_costs`, `action_restrictions`, `action_valid_targets`, `allocation_types`, `beat`, `card_faction_modifiers`, `card_metadata`, `card_subtypes`, `card_types`, `district_connections`, `game_actions`

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
     * `card_metadata` extends `components` with blueprint parameters for coverts and political acts.
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
| `component` | `components` | Complementary, not competing. `component` = component **type** registry (what types exist, what they can do — state-machine flags, verb coverage). `components` = physical **instance** manifest (every individual object in the game box — each district tile, each card, each token, each marker). Both are permanent; neither replaces the other. L169 (DB-32) adds `parent_component_id` to `component` for type hierarchy ("Card" → "Covert operation card" → outcome subtypes). `components` already has `parent_component_id` for instance grouping (e.g., individual cards grouped under their deck parent). The `master_blueprint_id` FK on `components` → `card_metadata` links physical card instances to their design blueprint. |
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
*AUTO_INCREMENT=120 as of S98. 77 registered components (max id=119 — d10 added S98). Next component will receive id=120.*

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
- `STD.CMA.1` / `STD.CMB.1` — Countermeasure cards; one spec each, faction copies (1× CMA, 2× CMB per faction)
- ARBITER card taxonomy = BCAST and BCEV only; ARB domain documents (Accord, Notif Slip, Grant Deed, DebriefActionCard) are NOT cards and have no card_id

`varchar(15)` constraint: all IDs must fit within 15 characters. `ARB.BCEV.99` = 11 chars (safe). Verify any new ID type fits before adding.


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

## 5. Component Registry (component — 77 active rows as of S104)

| id | name | act | xfm | rcv | vis | ori | dat | par |
|----|------|-----|-----|-----|-----|-----|-----|-----|
| 1 | Presence chip | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 2 | Deployment marker | 1 | 1 | 0 | 0 | 1 | 0 | NULL |
| 3 | Structure block | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 4 | District tile | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 5 | Established marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 6 | Dominant marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 7 | Tension marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 8 | Native resource | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 9 | Intel token | 1 | 1 | 0 | 1 | 0 | 1 | NULL |
| 10 | Accord agreement | 1 | 1 | 0 | 1 | 0 | 1 | NULL |
| 11 | Modifier card | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 12 | Dispatch token | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 13 | Covert operation | 1 | 1 | 1 | 1 | 0 | 0 | 111 |
| 14 | Political act | 1 | 1 | 1 | 1 | 0 | 0 | 111 |
| 15 | Operative card | 1 | 1 | 0 | 1 | 0 | 1 | 111 |
| 17 | Classified directives | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 21 | Public Standing | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 23 | Session Timeline | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 24 | Initiative strip | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 25 | Broadcast Card | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 26 | Faction Terminal | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 27 | Faction screen | 0 | 0 | 0 | 0 | 0 | 0 | NULL |
| 28 | ARBITER screen | 0 | 0 | 0 | 0 | 0 | 0 | NULL |
| 29 | The Overview | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 30 | Arbiter Tableau | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 31 | Chorus Activity Track | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 32 | Reservoir | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 33 | Backlog | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 34 | Pointer marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 35 | Activity marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 36 | Escalation marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 37 | Standing marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 38 | Faction order marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 42 | ARBITER Dominance Marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 43 | Human player | 0 | 0 | 0 | 0 | 0 | 0 | NULL |
| 44 | Dispatch case | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 47 | Modifier token | 1 | 1 | 0 | 0 | 1 | 0 | NULL |
| 48 | Target Profile | 1 | 1 | 0 | 1 | 0 | 1 | NULL |
| 49 | Status marker | 1 | 1 | 0 | 0 | 1 | 0 | NULL |
| 50 | Chorus Portrait track | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 51 | Portrait marker | 1 | 0 | 0 | 0 | 0 | 0 | NULL |
| 52 | Countermeasure card | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 53 | Ring 1 modifier deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 54 | Ring 2 modifier deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 55 | Ring 3 modifier deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 86 | Broadcast Deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 87 | Broadcast Effect Deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 88 | Faction Resolution Grid | 0 | 0 | 1 | 0 | 0 | 0 | NULL |
| 89 | Faction modifier deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 90 | Political act deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 91 | Political act discard | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 92 | Covert operation deck | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 93 | Covert operation discard | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 94 | Faction hand | 1 | 1 | 1 | 1 | 0 | 1 | NULL |
| 95 | Notification Slip | 1 | 1 | 1 | 1 | 0 | 0 | NULL |
| 96 | Intel Delivery Slip | 1 | 1 | 1 | 1 | 0 | 1 | NULL |
| 97 | Emergency Response card | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 98 | Broadcast Effect Card | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 99 | Sealed Apex ability | 1 | 1 | 0 | 1 | 0 | 0 | 111 |
| 100 | DebriefActionCard | 1 | 1 | 1 | 1 | 0 | 1 | NULL |
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
| 115 | Political Act Card Set | 1 | 1 | 0 | 1 | 0 | 0 | NULL |
| 116 | Operative Pool | 1 | 1 | 0 | 1 | 0 | 1 | NULL |
| 117 | Apex Ability Pool | 1 | 1 | 0 | 1 | 0 | 0 | NULL |
| 118 | Classified Directives Pool | 1 | 1 | 0 | 1 | 0 | 0 | NULL |
| 119 | d10 | 1 | 1 | 0 | 0 | 1 | 0 | NULL |

*Column key: act=actionable, xfm=transformable, rcv=receivable, vis=transform_visibility, ori=transform_orientation, dat=transform_data, par=parent_component_id*  
*IDs are non-sequential (gaps from deleted rows during schema evolution).*  
*Next AUTO_INCREMENT = 120.*

*Note on ids 100 and 113:* `DebriefActionCard` (100) and `Grant Deed` (113) are physical game documents (ARBITER domain), not card-type components, and thus have `parent_component_id = NULL` (they do not belong to the `Card` hierarchy).
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

---

## 7. Canonical Component Registration Pattern

Use **Countermeasure card (id=52)** as the reference. Full 4-table cascade required for every new component.

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
-- Countermeasure card (id=52) example:
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
-- Countermeasure card (id=52) example:
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

### Step 5 — Seed placement targets in subject_target
```sql
INSERT INTO subject_target (subject_id, target_id) VALUES
  (52, 30),  -- Countermeasure card → Arbiter Tableau (id=30)
  (52, 26);  -- Countermeasure card → Faction Terminal (id=26)
```

---

## 8. Row Counts

As of S50:
- `action`: **213 total rows, all root actions (prereq_id IS NULL)**
- `component`: **58 rows, next AUTO_INCREMENT = 98**
- `beat`: **20 rows** (fixed set — not AUTO_INCREMENT)
- `verb`: **8 rows** (id gaps from deprecated verbs)
- `trigger_type`: **10 rows**
- `function`: **12 rows**
- `layer`: **6 rows**

---

## 9. Open Design Notes / Known Gaps

- **DB-14** ✅ S50 (agy): Promoted all 20 design tables to permanent schema (dropped tmp_ prefix) and recompiled all 27 views.
- **DB-3NF** ✅ S63 (L184): 3NF applied. `component.transformable` → VIRTUAL GENERATED (derived from transform_ flags). `action.prereq_beat_id` dropped — prereq beat resolved dynamically via `prereq_id → action.phase_id`. `v_action_chain` rewritten. L108 amended (Requirements 6–7). `card_metadata` 3NF deferred to Art 04.6.
- **DB-18** (PM05): Cross-beat modifier persistence not modeled. C06/C07/C10/C11/C12 play at Beat 2 but modify Beat 3/4 — no deferred-effect mechanism in action.
- **DB-19** (PM05): Concurrent Political acts (C09) not verified in resolution model.
- **DB-22** ✅ S50 (agy): Upkeep primitives seeded — Faction/ARBITER Flip Status marker (ids 295/296), Faction/ARBITER Add Presence token (ids 297/298), Faction/ARBITER Remove Deployment marker (ids 299/300), ARBITER Move Situation Report card (id 301).
- **DB-23** ✅ S50 (agy): Status marker `transform_data` corrected to 0. Debrief Flip Status marker FK corrected to component id=49.
- **DB-24** ✅ S50 (agy): Portrait marker (id=51) registered in subject_target. Move primitives seeded.
- **DB-25** ✅ S50 (agy): Design-confirmed — Situation Report cards move to expired area (not removed); Target Profiles returned in dispatch case. No Remove primitive needed per Art 03.
- **DB-26** ✅ S50 (agy): Move role permissions verified against Art 03. Political act, Situation Report card, Target Profile resolved.
- **DB-09** ✅ S50 (agy): district_adjacency created and fully seeded — 21 district components in `components`, 21 rows in `district_metadata`, 104 bidirectional adjacency rows. PKs enforced on district_metadata and player_metadata.
- **category / type**: Deprecated. Drop and rebuild after Art 04b sign-off (DB-16).
- **destination_component_id / destination_zone_id** in action: Unpopulated — destination currently encoded in notes text only.

---

## 10. agy Sharing

This file is at `~/Projects/TheSignal/Database/` alongside all SQL build scripts. agy reads it via `GEMINI_CONTEXT.md` §DB Schema Reference. All schema changes go through dual-authorization: Claude Code proposes → Andy confirms → agy executes. Treat as read-only reference.

---

*Populated S50 — 2026-05-29. Update when schema changes are executed.*
