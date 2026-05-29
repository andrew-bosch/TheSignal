# THE SIGNAL — Gemini Context Brief
*Last updated: 2026-05-28 — Session 47*

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

### DB Schema Reference (Read Before Exploring)

`~/Projects/TheSignal/Database/schema_reference.md` — authoritative schema reference for `the_signal_db`. Contains all table schemas with FK semantic annotations, lookup table values, view definitions, and component registration patterns. Read this before issuing SHOW CREATE TABLE, DESCRIBE, or exploratory queries. Stub as of S50 — populated per PM05 DB-29.

**Connection:** `mysql -u gemini -pgemini_password1 the_signal_db`

**Critical FK gotcha:** `tmp_comp_verb_role.role_id` → `tmp_player_role` (1=Faction, 2=ARBITER); `tmp_comp_verb_role.phase_id` → `tmp_role_phase` (1=initiator, 2=executor, 3=fulfiller). Column names imply beat references — they do not.

---

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

## S40 DB Tasks — Open Items for agy

Three new tasks authorized after Art 01 v1.8 sign-off. Execute in order. Each requires Andy's terminal confirmation before you run DDL. Report as-executed in `Claude_context.md`.

---

### DB-09 — Create `district_adjacency` table

**Status:** READY — Art 01 signed off S40. Canonical adjacency data is in Art 01 §[City] District Adjacency Map (101 rows).

**Rationale:** Art 01 defines 101 bidirectional adjacency rows for all 21 districts. This data belongs in `the_signal_db` as the `district_adjacency` table to support game_zones population, Entry Rule A/B calculations, and Battlefield Strength scope (PM05 03-12).

**Step 1 — Update 00b spec first (Claude Code responsibility — wait for confirmation that this is done before proceeding).** 00b §8 must be updated to document the district_adjacency table spec before DDL is executed (Tandem-Read protocol).

**Step 2 — Create table:**
```sql
CREATE TABLE district_adjacency (
  id BIGINT(20) NOT NULL AUTO_INCREMENT,
  origin_district_id BIGINT(20) NOT NULL,
  adjacent_district_id BIGINT(20) NOT NULL,
  allow_ingress BOOLEAN NOT NULL DEFAULT TRUE,
  allow_egress BOOLEAN NOT NULL DEFAULT TRUE,
  PRIMARY KEY (id),
  CONSTRAINT fk_adj_origin FOREIGN KEY (origin_district_id) REFERENCES district_metadata (district_component_id),
  CONSTRAINT fk_adj_adjacent FOREIGN KEY (adjacent_district_id) REFERENCES district_metadata (district_component_id)
);
```

**Step 3 — Seed from Art 01 adjacency map.** Source of truth: `/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md` — District Adjacency Map section. All 101 rows are bidirectional (allow_ingress = TRUE, allow_egress = TRUE). District IDs correspond to the # column in the Art 01 district tables (1–21).

Confirm with Andy before executing. Report DDL and row count as-executed.

---

### DB-11 (L156) — Add `on_component_id` and `on_game_zone_id` to `live_state`

**Status:** BLOCKED — Claude Code must update 00b §8 live_state spec first (PM05 00b-05). Do not execute until Claude Code confirms 00b has been updated.

**Rationale:** L156 (S40) confirmed these two nullable FK columns. `on_component_id` tracks what component a component rests on (e.g., presence chip on district tile). `on_game_zone_id` tracks the sub-zone a component occupies beyond its primary zone_id.

**DDL (execute only after 00b-05 complete):**
```sql
ALTER TABLE live_state
  ADD COLUMN on_component_id BIGINT(20) DEFAULT NULL,
  ADD COLUMN on_game_zone_id BIGINT(20) DEFAULT NULL,
  ADD CONSTRAINT fk_live_on_component FOREIGN KEY (on_component_id) REFERENCES components (id),
  ADD CONSTRAINT fk_live_on_zone FOREIGN KEY (on_game_zone_id) REFERENCES game_zones (id);
```

Wait for Claude Code's go-ahead on this one. Report as-executed in `Claude_context.md`.

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
- **Signed-off artifacts:** 00 (v1.5 — S40), 00a (v0.3 — S40), 00b (v0.1), 01 (v1.8 — S40), 02b (v1.5), 04b (v1.2 — taxonomy audit pending). Pending re-sign-off: 02a (v1.5), 03 (v1.9). Do not propose additions without flagging re-sign-off requirement.
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

---

## Session 47 Update — 2026-05-28

### S47 DB Work Complete — New tmp_ Tables

Session 47 built out the formal action taxonomy model in `the_signal_db`. All tables are live and populated. **Do not truncate or rebuild these tables without dual authorization.**

New tables: `tmp_trigger_type`, `tmp_state_condition`, `tmp_state_condition_clause`
Altered: `tmp_action` — added `trigger_type_id` (FK → tmp_trigger_type), `source_action_id` (FK → tmp_action, self-ref), `component_id` relaxed to nullable
New verb: `Invoke` (id=17) in `tmp_verb`
New components: Portrait track (id=50, non-actionable), Portrait marker (id=51, ARBITER-controlled), Status marker (id=49)
Primitives: 213 rows in `tmp_action`; trigger types assigned across all rows

New views live in `the_signal_db`:
- `v_primitives_with_trigger` — readable primitive library with trigger type
- `v_trigger_summary` — trigger distribution by subject
- `v_unlegislated_primitives` — (beat, subject, verb, component) in taxonomy but not in tmp_action (60 rows)
- `v_unlegislated_by_trigger` — (subject, verb, component) with no coverage in tmp_action under any trigger (14 rows)

Governing principle locked as **L166** in PM02: the taxonomy defines possibility space; Art 03 defines legal space. Gaps are procedure coverage signals — permit / prohibit / defer. The two artifacts co-evolve.

`tmp_component` is becoming the working source of truth for the physical component registry. DB entries are expected to eventually drive or align all design artifacts. The gap analysis and audit work below is organized around that goal.

---

### agy Punch List — S47

Work through these in priority order. Get as far as you can; report what you complete, what you find, and where you're blocked in `Claude_context.md`. You do not need fully-prescribed SQL for every item — read the artifacts and DB, form your own queries, and report findings. This is investigative work.

**Connection:** `mysql -u gemini -pgemini_password1 the_signal_db`
**Read access:** all of `~/Projects/TheSignal/` — use freely for verification

---

#### A. Gap Analysis Views (CREATE OR REPLACE VIEW — no DDL/DML otherwise)

Seven views to build. For views 1–6 the SQL is provided for precision; for view 7 flag as blocked. Report row counts for each.

**A1 — v_gap_executor_check**
For each row in `v_unlegislated_by_trigger`, show who is the executor (phase_id=2) in `tmp_comp_verb_role`. If executor = ARBITER, the gap may be expected (Faction initiates via card, ARBITER physically executes). If executor = Faction, it is a true unlegislated gap requiring a design decision.

```sql
CREATE OR REPLACE VIEW v_gap_executor_check AS
SELECT
  g.subject, g.verb, g.component, g.beat_count,
  r.name AS executor
FROM v_unlegislated_by_trigger g
JOIN tmp_comp_verb_role cvr
  ON  cvr.component_id = g.component_id
  AND cvr.verb_id      = g.verb_id
  AND cvr.phase_id     = 2
JOIN tmp_player_role r ON cvr.role_id = r.id
ORDER BY g.subject, g.verb, g.component;
```

**A2 — v_unassigned_triggers**
Primitives in `tmp_action` where `trigger_type_id IS NULL`. These slipped through bulk UPDATE assignment and need classification.

```sql
CREATE OR REPLACE VIEW v_unassigned_triggers AS
SELECT a.id, b.name AS beat, r.name AS subject, v.name AS verb,
       c.name AS component, a.notes
FROM tmp_action a
JOIN tmp_beat        b  ON a.beat_id      = b.id
JOIN tmp_player_role r  ON a.subject_id   = r.id
JOIN tmp_verb        v  ON a.verb_id      = v.id
LEFT JOIN tmp_component c ON a.component_id = c.id
WHERE a.trigger_type_id IS NULL
ORDER BY b.id, r.id, v.name;
```

**A3 — v_duplicate_primitives**
Duplicate (beat_id, subject_id, verb_id, component_id) in `tmp_action` where `prereq_id IS NULL`.

```sql
CREATE OR REPLACE VIEW v_duplicate_primitives AS
SELECT b.name AS beat, r.name AS subject, v.name AS verb,
       c.name AS component, COUNT(*) AS duplicate_count,
       GROUP_CONCAT(a.id ORDER BY a.id) AS action_ids
FROM tmp_action a
JOIN tmp_beat        b  ON a.beat_id      = b.id
JOIN tmp_player_role r  ON a.subject_id   = r.id
JOIN tmp_verb        v  ON a.verb_id      = v.id
LEFT JOIN tmp_component c ON a.component_id = c.id
WHERE a.prereq_id IS NULL
GROUP BY a.beat_id, a.subject_id, a.verb_id, a.component_id,
         b.name, r.name, v.name, c.name
HAVING COUNT(*) > 1
ORDER BY b.id, r.id, v.name;
```

**A4 — v_component_coverage**
All tmp_component rows with their primitive count. Zero = no legal action assigned. Flag any actionable=1 component with zero primitives.

```sql
CREATE OR REPLACE VIEW v_component_coverage AS
SELECT c.id, c.name, c.actionable, c.transformable,
       COALESCE(cnt.n, 0) AS primitive_count
FROM tmp_component c
LEFT JOIN (
  SELECT component_id, COUNT(*) AS n
  FROM tmp_action
  WHERE prereq_id IS NULL AND component_id IS NOT NULL
  GROUP BY component_id
) cnt ON cnt.component_id = c.id
ORDER BY primitive_count ASC, c.name;
```

**A5 — v_beat_subject_coverage**
Distinct verb count, component count, and total primitives per subject per beat.

```sql
CREATE OR REPLACE VIEW v_beat_subject_coverage AS
SELECT b.id AS beat_id, b.name AS beat, r.name AS subject,
       COUNT(DISTINCT a.verb_id)      AS verb_count,
       COUNT(DISTINCT a.component_id) AS component_count,
       COUNT(*)                       AS primitive_count
FROM tmp_action a
JOIN tmp_beat        b ON a.beat_id    = b.id
JOIN tmp_player_role r ON a.subject_id = r.id
WHERE a.prereq_id IS NULL
GROUP BY b.id, b.name, r.id, r.name
ORDER BY b.id, r.id;
```

**A6 — v_trigger_beat_coverage**
Trigger types present in each beat. A beat with no `rule.card` or `player.*` triggers may be missing card-driven actions.

```sql
CREATE OR REPLACE VIEW v_trigger_beat_coverage AS
SELECT b.id AS beat_id, b.name AS beat,
       CONCAT(tt.type, CASE WHEN tt.subtype IS NOT NULL
              THEN CONCAT('.', tt.subtype) ELSE '' END) AS trigger_type,
       COUNT(*) AS cnt
FROM tmp_action a
JOIN tmp_beat         b  ON a.beat_id         = b.id
JOIN tmp_trigger_type tt ON a.trigger_type_id = tt.id
WHERE a.prereq_id IS NULL
GROUP BY b.id, b.name, tt.id, tt.type, tt.subtype
ORDER BY b.id, tt.type, tt.subtype;
```

**A7 — v_card_primitive_map** — **BLOCKED.** Requires a `tmp_card_ref` seed table (card_id → component_id, verb_id, subject_id) that Claude Code has not yet provided. Flag as blocked in `Claude_context.md`.

---

#### B. Art 03 Bidirectional Alignment Audit

**This is the highest-value investigation.**

Read `~/Projects/TheSignal/V1/03___Game_Procedures_Rules.md` — specifically the beat-by-beat procedures in §3.11 (and surrounding sections covering Upkeep, Debrief, Battlefield Strength, etc.).

For each procedure described in Art 03 that involves a physical action on a component:
1. Identify the (beat, subject, verb, component) tuple it describes
2. Check whether a corresponding primitive exists in `tmp_action`
3. Flag procedures with no primitive — these are Art 03 saying something is legal that the model doesn't yet capture (gaps from the other direction)

Cross-reference with `v_unlegislated_primitives` (gaps in the model with no Art 03 procedure). The bidirectional audit — Art 03 procedures with no primitive AND primitives with no Art 03 procedure — is the complete picture of alignment between the two artifacts.

Report: table of (beat, subject, verb, component, Art 03 procedure reference, primitive id or MISSING).

---

#### C. Art 00b Schema Alignment

Read `~/Projects/TheSignal/V1/00b___Data_Architecture.md`.

`tmp_component` is a prototype of `components`. `tmp_action` relates to `game_actions`. `tmp_verb` relates to action verb vocabulary. Compare:

1. **tmp_component vs. components** — are the fields (actionable, transformable, receivable, transform_*) consistent with 00b's component entity spec? Are there fields in 00b's components table missing from tmp_component, or vice versa? Flag discrepancies.

2. **tmp_action vs. game_actions** — does the S47 action grammar (beat_id, trigger_type_id, prereq_id, source_action_id, subject_id, verb_id, component_id) align with 00b's game_actions design intent? Are there fields in game_actions not represented in tmp_action? Are there S47 design decisions (trigger taxonomy, invoke meta-verb) that need to be reflected back into 00b?

3. **Known gaps Andy flagged** — 00b has documented gaps for ARBITER and faction components that live only in the tableaux or in procedures not yet defined. Read 00b and identify: which component types and zones are referenced in 00b but have no corresponding tmp_component rows? These are candidates for the next component registry expansion.

Report: a gap table (entity → 00b spec → tmp_ table → status: aligned / gap / missing).

---

#### D. Art 04b §4.2 Matrix Verification

Read `~/Projects/TheSignal/V1/04b___Action_Taxonomy_Design_Analysis.md` §4.2 (Component × Verb Matrix).

§4.2 is a hand-written table listing which verbs each component supports. `tmp_comp_verb_role` is the DB-derived equivalent. Diff them:

1. Any component/verb combination in §4.2 but absent from `tmp_comp_verb_role` — documentation ahead of DB
2. Any component/verb combination in `tmp_comp_verb_role` but absent from §4.2 — DB ahead of documentation (S47 additions)
3. Any component present in Art 02a/02b component definitions but absent from `tmp_component` entirely

Report the diff table. Also note: §4.2 does not yet include Portrait track, Portrait marker, or Status marker — these were added in S47. Confirm they are correctly absent from §4.2 (they will be added in the next Art 04b update).

---

#### E. Component Lifecycle Completeness

For each component in `tmp_component`, examine its lifecycle coverage across `tmp_action`:

1. Can it be Added? Can it be Removed? If it can be Added at some beat but never Removed at any beat (or vice versa), that is a lifecycle gap — either a modeling error or an intentional design choice that should be documented.
2. Can it be Moved? If a component has Move in `tmp_comp_verb_role` but no Move primitive in `tmp_action` at any beat, flag it.
3. For transformable components (transformable=1): are there Flip/Corrupt/Reveal/Conceal primitives corresponding to its transform properties?

Report: component lifecycle table (component, Add beats, Remove beats, Move beats, Transform verbs covered, gaps flagged).

---

#### F. Beat Load Distribution

Query `v_beat_subject_coverage` once it's created (task A5). Produce a beat-by-beat summary:

1. For each beat, what is the ratio of Faction primitives to ARBITER primitives?
2. Which beats are ARBITER-dominant (>80% ARBITER)? Are these the expected resolution beats?
3. Which beats have zero Faction actions? Is that intentional per Art 03?
4. Flag any beats that appear under-populated relative to their narrative weight in Art 03 (e.g., a major resolution beat with only 1–2 primitives).

This is a design-quality check, not a schema check. Report qualitative observations alongside the numbers.

---

#### G. Tableau and Unmodeled Component Strategy

This is strategic planning, not a specific query.

Andy notes that `tmp_component` is becoming the source of truth for the physical component registry, and that 00b has known gaps for components stored in or associated with ARBITER's tableau and faction tableaux — components involved in procedures not yet formally designed.

Read:
- `~/Projects/TheSignal/V1/00b___Data_Architecture.md` — for what's documented about tableaux and component storage
- `~/Projects/TheSignal/V1/03___Game_Procedures_Rules.md` — for procedure references to components that may not yet be in tmp_component
- `~/Projects/TheSignal/V1/04___Card_System.md` — for card effects that reference components not in tmp_component

Identify:
1. Component types referenced in procedures or card effects that have no tmp_component row
2. Components that exist implicitly (e.g., "ARBITER places a modifier token on the case" — modifier token is in tmp_component, but what about the case itself as a zone vs. component?)
3. Any tableau-resident components (items that live on ARBITER Tableau or Faction Tableau by default) with no actionable status defined

Output: a prioritized list of missing or underspecified components, with notes on where each is referenced and what DB fields would be needed to add them correctly. This feeds the next round of tmp_component expansion.

---

---

#### H. Web Research — Card Interaction Patterns from Other Game Media

The Signal's card system has identified a two-layer structure: **execution cards** (directly invoke a physical primitive on a component) and **constraint cards** (modify conditions under which another action fires — Block, Protect, Modify). Before finalizing the Function vocabulary in Art 04b §5, research what interaction patterns exist in established games that The Signal may not yet be modeling.

Research focus areas:

1. **Deckbuilding games** (Dominion, Arkham Horror LCG, Marvel Champions, Netrunner, Twilight Imperium) — what action/reaction interaction types do these games use? Are there Function-equivalents The Signal hasn't considered? Pay particular attention to: interrupt mechanics, conditional triggers, permanent vs. temporary modifiers, resource conversion chains, and hidden-information manipulation.

2. **Negotiation/area control games** (Twilight Imperium, Dune, Root, Oath, Pax series) — what deal-making, alliance, and betrayal mechanics exist that The Signal's Accord and political act system may not be capturing? What card-driven asymmetric faction abilities are common patterns?

3. **Asymmetric action economy** — The Signal has Faction (player) and ARBITER roles. What patterns in other games handle referee/moderator roles that also interact with the card system mechanically (not just narratively)?

4. **Specific gaps to check against** — The Signal's current unlegislated Faction interactions include: Faction Corrupt (Intel token, Accord, Target Profile), Faction Conceal Intel token, Faction Reveal/Remove Intel token. Do other games have mechanics for players manipulating their own or opponent's information assets? What are the established patterns for "falsify," "intercept," "plant," "burn" in card game design?

Report: for each research area, list 3–5 specific interaction patterns with game citations, and for each one flag whether The Signal's current Function vocabulary covers it, partially covers it, or has no equivalent. This feeds the §5 Category/Function design discussion and potential new card concepts.

**Do not propose new card designs** — that is Andy's creative domain. Report patterns and gaps only.

---

**Reporting format:** Write findings to `Claude_context.md` as you complete each section. You do not need to finish everything in one session. Partial results on high-priority items (B and C) are more valuable than silence on all items. Flag blockers clearly with the specific artifact reference or DB query that produced the dead end.

---

## Session 43 Update — 2026-05-27

**Art 03 v2.0 signed off.** Key changes with DB/schema implications:

### Intel Token Schema — Canonical Definition (L161)
Intel Tokens carry three attributes: `intel_id`, `faction`, `round_generated`.
- `faction` = the faction the intel was gathered **about** (subject faction) — NOT the holder. ARBITER verifies this field at play (Beat 0, Beat 4, §18 Battlefield Strength).
- `round_generated` = Quarter number written by ARBITER at issuance.
- Freshness: age = current Quarter − round_generated. Age 0–2 = fresh; age 3 = stale (−25); age 4+ = expired (partial payment −50).

**The Dossier (L164):** ARBITER's hidden Intel Token pool — held behind ARBITER screen, not in the public Reservoir. All blank tokens live there; ARBITER writes faction + Quarter at issuance; reset/discarded tokens return there.

### Still Blocked — No New DB Work This Session
- **DB-09** (district_adjacency DDL) — still blocked on 00b-05 (live_state spec). DDL FK fix still required: reference `district_metadata(district_component_id)` not `(id)`.
- **DB-11** (live_state nullable columns) — still blocked on 00b-05.

### New Modifier Rows in Art 03 §20
- **M-12** updated: Category Ring (was District). Name "No adjacent inward-ring presence." Covers The Mid (no Core presence) and Core (no Chorus Node presence). Condition: any presence marker (count > 0) in adjacent inward district removes penalty. −25 fixed.
- **M-13** added: Category Intel. "Stale Intel Token (age 3)." Applied Beat 0 / Beat 4. 1 per stale token. Fixed −25.

### Apex Pentagram Model (04-52 — design flag, no DB action yet)
At Apex submission, ARBITER arranges 5 faction players on pentagram points by Portrait track standing. Apex payment must include fresh Intel Token targeting the opposing faction (pentagram-defined). DB implication: Portrait track values need to be queryable at Apex moment. No schema change needed now — flag for L2 design pass.

### Portrait Track — Dual Function (L165)
Portrait track now serves ARBITER narrative AND Apex geometry. "Ask ARBITER" portrait delta query (07-10): faction queries absolute difference between their Portrait standing and any named faction. ARBITER reveals delta only. This is read-only on existing Portrait data — no schema change implied.

---

## Session 48 Update — 2026-05-28

### S48 DB Cleanup Tasks

S48 sanity check of agy's S47 audit findings. Execute in order; report outcomes in `Claude_context.md`.

**Connection:** `mysql -u gemini -pgemini_password1 the_signal_db`

---

#### DB-cleanup-01 — Delete 37 duplicate rows from `tmp_action`

Resolution beats were seeded twice. The following IDs are exact duplicates — the original (lower ID) exists in each case. Safe to delete.

```sql
DELETE FROM tmp_action WHERE id IN (
  70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 83, 84, 90,
  135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 148, 149, 155,
  171, 172, 173, 174, 175, 176, 177, 178, 181
);
```

Verify: `SELECT COUNT(*) FROM tmp_action;` should return 177 after deletion.

---

#### DB-cleanup-02 — Add Standing marker move primitive to `tmp_action`

Art 03 was updated this session (S48) to establish the following precedent:

- **Beat 3 (covert resolution):** Standing marker moves occur only on failure or discovery — card-specified. No primitive needed for success (design intent: covert success is unobserved).
- **Beat 4 (political act resolution):** Standing marker moves are card-specified and can occur on success OR failure.

Add primitives for ARBITER Move Standing marker (or Faction Move — check Art 03 §11 Step 7 / §17 Beat 4 Step 7 for who applies each outcome type):

- Beat 3 (ids 8 and 14): trigger_type = rule.card, beat_trigger = during, notes = "Card-specified failure/discovery condition only."
- Beat 4 (id 17): trigger_type = rule.card, beat_trigger = during, notes = "Card-specified outcome — success or failure."

Also add Standing marker to `tmp_comp_verb_beat` for Beat 4 (id=17) if not already present — it is absent and will not surface in `v_unlegislated_primitives` until added.

---

#### DB-cleanup-03 — Seed `tmp_comp_verb_role` and `tmp_comp_verb_beat` for two unseeded components

Both components exist in `tmp_component` and appear in Art 04b §3.2 Component × Verb Matrix but have no role or beat assignments.

**ARBITER Dominance Marker** (`tmp_component` id=42) — verbs per §3.2: Add, Remove, Move.

**Classified directives** (`tmp_component` id=17) — verbs per §3.2: Add, Remove, Move, Reveal, Conceal.

For each: determine appropriate beats (reference Art 03 for when these components are acted upon) and role assignments (phase_id=1 initiator, phase_id=2 executor). Report what you populate and flag anything requiring a design decision before seeding.

---

#### DB-cleanup-04 — Countermeasures beats (ids 4, 10, 16) — assess and seed

Beats 4, 10, 16 (Month 1/2/3 Countermeasures) have 0 primitives. Art 03 §10/§13/§16 defines the procedure: Faction Players deploy or pass Countermeasure cards in initiative order; cards are handed to ARBITER.

Assess whether Countermeasure card is registered in `tmp_component`. If not, flag — do not seed primitives until the component exists. If it is registered, seed the Countermeasures beats with appropriate primitives (Faction Remove card from hand, Add/Move to ARBITER). Report findings.

---

### S48 Schema Additions — Layer, Function, and Gap Primitive Seeding

Claude Code executed the following DB work directly this session. Do not re-execute.

#### New dimension tables

**`tmp_layer`** — 6 rows: Territory, Economy, Information, Submission, Resolution, Standing. These are the six game layers from Art 04b §4.2.

**`tmp_function`** — 12 rows: Add, Remove, Redirect, Recover, Modify, Protect, Block, Copy, Reveal, Conceal, Shift, Corrupt. These are the card Functions from Art 04b §5.1.

**`tmp_function_verb`** — 9 rows mapping Function → physical Verb:
- Add → Add, Remove → Remove, Redirect → Move, Recover → Add, Copy → Invoke, Reveal → Reveal, Conceal → Conceal, Shift → Move, Corrupt → Corrupt
- Modify, Protect, Block have **no verb mapping** — they are abstract constraints on other actions, not physical primitives. These will not appear in primitive-based views.

#### New view

**`v_layer_function_coverage`** — Shows every Faction-initiatable Function × Component combination with beat availability. Filters to rows where `faction_initiatable=1 OR beat_count>0`. Join: `tmp_function` → `tmp_function_verb` → `tmp_verb` → `tmp_comp_verb_role/beat`. Note: Add and Recover share the Add verb (identical physical rows); Redirect and Shift share the Move verb.

#### Gap primitive seeding

The following component×verb combinations were seeded to model §6.1 card design gaps:

| Component | Verb | What was added |
|-----------|------|---------------|
| Structure block | Move | Beats: M1-Beat-3, M2-Beat-3, M3-Beat-4 |
| Accord agreement | Move | Faction initiator + executor roles; Beats: M1-Beat-3, M2-Beat-3 |
| Modifier card | Move | Faction initiator + executor roles; Beats: M1-Beat-3, M2-Beat-3, M3-Beat-4 |
| Modifier card | Remove | Faction initiator + executor roles; Beats: M1-Beat-3, M2-Beat-3, M3-Beat-4 |
| Modifier card | Reveal | Faction initiator + ARBITER executor/fulfiller roles; Beats: M1-Beat-3, M2-Beat-3, M3-Beat-4 |
| Political act | Invoke | Faction initiator + ARBITER executor/fulfiller; Beats: M3-Declaration, M3-Beat-4 |
| Classified directives | Reveal | Faction initiator + ARBITER executor/fulfiller; Beat: M3-Beat-4 only (high-impact) |

#### All §6.1 gaps now fully modeled (S48)

- **Presence token | Move** — beats M1-Beat-3 (8), M2-Beat-3 (14), M3-Beat-4 (17) seeded S48. ✅
- **Countermeasure card | Reveal** — self-reveal beats (4, 10, 16) plus intelligence-window beats (8, 14, 17) seeded S48. ✅
- **Card hand contents** — reclassified from non-modelable. Subject decomposes into per-card-type Reveal primitives for each held card component: Modifier card ✅, Countermeasure card ✅. Political act coverage partial (M3-B4 only — beats 8, 14 not yet seeded for pre-Declaration window). Covert operation Reveal remains ARBITER-only.

#### Two §6.1 gaps still requiring schema extension

- `Information | Reveal | Named faction only` — scope modifier (target filter), not a subject component; needs target-scope system in action model
- `Submission | Copy | Subset only` — meta-concept (partial copy); needs partial-copy mechanism in action model

---

## Session 50 Update — 2026-05-29

### S50 DB Changes (Claude Code — Executed)

Three new components registered in `tmp_component` and fully seeded across tmp_comp_verb_beat, tmp_comp_verb_role, tmp_action, tmp_subject_target:
- **Notification Slip** (id=95): actionable=1, receivable=1
- **Intel Delivery Slip** (id=96): actionable=1, transformable=1, transform_data=1
- **Emergency Response card** (id=97): actionable=1, transformable=1, transform_visibility=1

`the_signal_db_documentation/` directory removed. Schema reference moved to `~/Projects/TheSignal/Database/schema_reference.md` — this file is where the DB build scripts now live as well.

---

### agy Punch List — S50

Five items from your S48 audit are logged in PM05 (DB-22 through DB-26) and authorized for execution. Work through them in priority order below.

**Standing instruction for all items:** Read the referenced artifact section(s) before proposing any change. If a procedure is ambiguous or a change requires design judgment, report what you found in `Claude_context.md` and ask Andy — do not assume or extrapolate. This project is too sensitive to guessed values. Propose before executing where noted.

**Connection:** `mysql -u gemini -pgemini_password1 the_signal_db`

---

#### DB-23 — Status marker modeling errors (PM05 DB-23)

Two fixes. Before either: read `~/Projects/TheSignal/V1/04b___Action_Taxonomy_Design_Analysis.md` §4.2 (Status marker entry) and `~/Projects/TheSignal/V1/03___Round_Structure___Gameplay.md` §7 Step 1 (Upkeep Status Marker Reset).

**Fix 1 — transform_data flag.** Status markers track orientation only (Discussing / Ready) — they carry no written data. Confirm from the artifact that there is no case where a Status marker carries written information. If confirmed, execute: `UPDATE tmp_component SET transform_data = 0 WHERE id = 49;`. If you find a case where it does carry data, ask Andy before executing.

**Fix 2 — Debrief wrong component ID.** Run this query first and report what it returns:
```sql
SELECT a.id, b.name AS beat, v.name AS verb, c.name AS component
FROM tmp_action a
JOIN tmp_beat b ON a.beat_id = b.id
JOIN tmp_verb v ON a.verb_id = v.id
LEFT JOIN tmp_component c ON a.component_id = c.id
WHERE b.name LIKE '%Debrief%' AND v.name = 'Flip';
```
Then read Art 03 §19 (Debrief) to confirm what component the Flip action targets. Update only what the artifact confirms. Report findings before executing any UPDATE.

---

#### DB-24 — Portrait marker missing from `tmp_subject_target` (PM05 DB-24)

Portrait marker (id=51) is absent from `tmp_subject_target`, causing Move=0 in the verb matrix. Before inserting: read `~/Projects/TheSignal/V1/02b___Public_Standing_and_Portrait.md` (Portrait track section) and `~/Projects/TheSignal/V1/03___Round_Structure___Gameplay.md` (Beat 4 procedure) to determine (1) what component or zone is the valid target for a Portrait marker move and (2) which subject initiates and executes. Report what the artifacts say in `Claude_context.md` and ask Andy to confirm before seeding. Do not assume target values.

---

#### DB-22 — Upkeep beat missing primitives (PM05 DB-22)

Art 03 §7 describes three Faction actions at Upkeep with no primitives in tmp_action:
1. Flip Status marker (Step 1)
2. Add Presence token (Step 4 — Deployment Marker Conversion)
3. Remove Deployment marker (Step 4 — same step)

Read Art 03 §7 Steps 1 and 4. Confirm: (1) exactly who performs each action (Faction or ARBITER); (2) the beat_id for Upkeep; (3) appropriate trigger_type for each. Write your proposed INSERT statements to `Claude_context.md` — Andy will confirm before you execute.

---

#### DB-25 — Lifecycle cleanup missing (PM05 DB-25)

Two components missing Remove primitives: Situation Report card and Target Profile. Read Art 03 for each — where and when are Situation Reports removed from play, and when is a Target Profile removed after a covert operation resolves? If the removal procedure is not defined in Art 03, say so — do not seed a beat assignment that is not in the source artifact.

---

#### DB-26 — Move verb mismatch (PM05 DB-26)

Political act, Situation Report card, and Target Profile have Move role permissions in tmp_comp_verb_role but zero Move primitives. Read Art 03 for each component: does it physically move between locations during a session? Report findings in `Claude_context.md`. If yes: propose the primitive. If no: propose removing the role permission. If unclear: ask Andy.

---

#### DB-09 DDL FK — verification required before execution

The district_adjacency DDL earlier in this file references `district_metadata (id)` for both FK constraints. Your S48 report flagged that the PK column name may be different. Run `SHOW CREATE TABLE district_metadata;` and report the actual PK column name in `Claude_context.md`. Claude Code will correct the DDL before you execute it.

---

#### DB-29 — Schema reference file (Claude Code task)

The stub at `~/Projects/TheSignal/Database/schema_reference.md` will be populated by Claude Code. Read it before any DB session once populated. No action needed from agy on DB-29.
