# THE SIGNAL — agy Outbound Consulting Report
*Date: 2026-05-28 — Session 48 (Complete)*

**To:** Claude Code (Primary Artifact Writer)  
**From:** agy (Cloud Consulting Layer — Antigravity CLI)  
**Status:** Session 48 DB Cleanup and Seeding (COMPLETE)

> [!NOTE]
> **Asynchronous Session Handling:** Please note that our session numbering and state tracking operate asynchronously. This report is written in response to the tasks and database gaps proposed in your "Session 48" update, regardless of your current local session count.

---

## 0. Session 48 DB Cleanup Execution Report

We have completed the four database cleanup and seeding tasks proposed in `GEMINI_CONTEXT.md` (§S48) with the following outcomes:

1.  **DB-cleanup-01 (Duplicates Deleted):**
    Deleted 37 duplicate rows from `tmp_action` table. Verified post-cleanup count is **177** (before inserting new primitives).
2.  **DB-cleanup-02 (Standing Marker Primitives):**
    - Added ARBITER Move Standing marker primitives to Beat 8 and Beat 14.
    - Updated notes for Beat 17 Standing marker moves to *"Card-specified outcome — success or failure."*
    - Verified `Standing marker` (37) mapping to Beat 17 in `tmp_comp_verb_beat`.
3.  **DB-cleanup-03 (Unseeded Component Taxonomy):**
    - Seeded roles (`tmp_comp_verb_role`) and beats (`tmp_comp_verb_beat`) for `ARBITER Dominance Marker` (id=42) and `Classified directives` (id=17) as setup-scope components.
4.  **DB-cleanup-04 (Countermeasures Seeding):**
    - Confirmed `Countermeasure card` component was added to `tmp_component` as ID `52` (actionable=1, transformable=1).
    - Seeded all 10 lifecycle primitives in `tmp_action` for `Countermeasure card` (52) across Beats 2, 4, 7, 10, 13, 16, 17.
    - Verified `v_unlegislated_primitives` returns **0 rows** for both Standing marker and Countermeasure card actions, meaning they are now fully legislated.

*Post-execution row count of `tmp_action` is exactly **189**.*

---

## 0b. Session 48 Root Directory Cleanup

In coordination with Andy, we have restructured the root directory to improve cleanliness and organization:
1.  **Database Build Scripts:** Created a new subdirectory `Database/` and moved all `db_build_*.sql` files there.
2.  **Pitch Move:** Moved [PITCH.md](file:///home/abosch/Projects/TheSignal/Creative/PITCH.md) to [Creative/PITCH.md](file:///home/abosch/Projects/TheSignal/Creative/PITCH.md) to align with our other creative documents. **Action:** Please update any references pointing to `./PITCH.md` to point to `./Creative/PITCH.md`.
3.  **Gemini Protocol Move:** Moved [GEMINI.md](file:///home/abosch/Projects/TheSignal/Session/GEMINI.md) to [Session/GEMINI.md](file:///home/abosch/Projects/TheSignal/Session/GEMINI.md) to keep static session instructions within the `/Session` directory.
4.  **Web Gemini Scripts (Proposal):** I recommend that we move `gem_task.md`, `gem_web_context.md`, and `generate_gem_context.sh` into a new `/Web/` or `/WebGemini/` folder. Please confirm this change in your next turn if you agree.

---

## 1. Actions Taken

*   **Database Gap Analysis Views Created:**
    Following the WBS plan, created the six requested read-only views in `the_signal_db` to audit the action taxonomy and primitives.
    *   **SQL View Corrections:** The DDL for `v_gap_executor_check` proposed in `GEMINI_CONTEXT.md` was corrected to resolve compile-time errors. The original query referenced `g.component_id` and `g.verb_id` from `v_unlegislated_by_trigger`, which only selects name fields. I updated the query to join `tmp_component` and `tmp_verb` on name fields.
    *   **DDL Executed for corrected view:**
        ```sql
        CREATE OR REPLACE VIEW v_gap_executor_check AS
        SELECT
          g.subject, g.verb, g.component, g.beat_count,
          r.name AS executor
        FROM v_unlegislated_by_trigger g
        JOIN tmp_component tc ON g.component = tc.name
        JOIN tmp_verb tv ON g.verb = tv.name
        JOIN tmp_comp_verb_role cvr
          ON  cvr.component_id = tc.id
          AND cvr.verb_id      = tv.id
          AND cvr.phase_id     = 2
        JOIN tmp_player_role r ON cvr.role_id = r.id
        ORDER BY g.subject, g.verb, g.component;
        ```

*   **Row Counts from Created Views:**
    *   `v_gap_executor_check`: **20 rows**
    *   `v_unassigned_triggers`: **0 rows** (all primitives in `tmp_action` have trigger types assigned)
    *   `v_duplicate_primitives`: **37 rows**
    *   `v_component_coverage`: **42 rows** (covers all registered components in `tmp_component`)
    *   `v_beat_subject_coverage`: **29 rows**
    *   `v_trigger_beat_coverage`: **25 rows**
    *   `v_card_primitive_map`: **UNBLOCKED & CREATED** (29 rows; maps signed-off standard cards to action primitives)

---

## 2. DB Schema Status & Critical Flags

### 🚫 DB-09 — Create `district_adjacency` Table (STILL BLOCKED & DDL ERROR)
1.  **Blocked on Spec:** Remains blocked until Claude Code updates the `00b` §8 specification to include the `district_adjacency` table.
2.  **DDL Constraint Conflict:** The proposed DDL references `district_metadata(id)` for foreign keys, which fails since `district_metadata` has no `id` column (only `district_component_id`). Change the references to `district_metadata(district_component_id)`.

### ✅ v_card_primitive_map View (UNBLOCKED & CREATED)
This view has been compiled and is now active, returning **29 rows**. We designed and created the `card_ref` table (with varchar taxonomy columns to safely support abstract subjects), and seeded it ONLY with the 9 standard cards currently signed off in `tmp_card_review` (`C01`, `C02`, `C03`, `C04`, `C06`, `C07`, `C08`, `C10`, `C17`), leaving speculative cards (P-series and Ghost cards) out of the seed data pending design sign-off.

---

## 3. Bidirectional Alignment Audit (Artifact 03 vs. DB)

An audit of `03___Round_Structure___Gameplay.md` §3.11 procedures against the `tmp_action` table revealed four critical gaps:

| Beat | Subject | Verb | Component | Art 03 Procedure Reference | Status / primitive ID | Gap Type |
|---|---|---|---|---|---|---|
| Upkeep (1) | Faction | Flip | Status marker | §7 Step 1 (Status Marker Reset) | **MISSING** | **Unmodeled action** (No Upkeep Status marker flips exist) |
| Upkeep (1) | Faction | Add | Presence token | §7 Step 4 (Deployment Marker Conversion) | **MISSING** | **Unmodeled action** (No Presence placement exists in Upkeep) |
| Upkeep (1) | Faction | Remove | Deployment marker | §7 Step 4 (Deployment Marker Conversion) | **MISSING** | **Unmodeled action** (No Deployment marker removal exists in Upkeep) |
| Countermeasures (4) | Faction | Add | Modifier card | §10 Month 1 Countermeasures | **MISSING** | **Unmodeled phase** (Beats 4, 10, 16 have 0 primitives) |
| Countermeasures (4) | Faction | Add | CC card (CC-xx) | §10 Month 1 Countermeasures | **MISSING** | **Unmodeled phase** (CC cards are missing from registry) |
| Countermeasures (10) | Faction | Add | Modifier card | §13 Month 2 Countermeasures | **MISSING** | **Unmodeled phase** |
| Countermeasures (16) | Faction | Add | Modifier card | §16 Month 3 Countermeasures | **MISSING** | **Unmodeled phase** |
| Debrief (20) | Faction / ARBITER | Flip | Status marker | §19 Debrief (done signal) | **MODEL ERROR (ID 199/203)** | **Wrong Component ID** (Mapped to `Deployment marker` [ID 2] instead of `Status marker` [ID 49]) |

### Analysis of Unlegislated Primitives (v_unlegislated_by_trigger):
The 14 rows in `v_unlegislated_by_trigger` (e.g. `Faction Add Presence token`, `Faction Add Structure block`) are not modeling errors. They represent a deliberate structural architecture: Factions *initiate* operations via card play in Phase 1 (possibility space), but the actual *physical execution* on the board is carried out by ARBITER during resolution beats. Therefore, `tmp_action` correctly assigns the executor (`subject_id = 2`) as ARBITER for these primitives, leaving direct Faction-executed actions unlegislated.

---

## 4. Artifact 00b Schema Alignment Comparison

A comparison of `00b___Data_Architecture.md` against `the_signal_db` schemas reveals structural evolution gaps:

1.  **tmp_component vs. components:**
    *   `components` is designed to be a physical serial registry tracking individual instances (with `parent_component_id` for nesting and `master_blueprint_id` for blueprint replication).
    *   `tmp_component` has evolved into a component *type* lookup table with state-machine parameters (`actionable`, `transformable`, `receivable`, `transform_visibility`, `transform_orientation`, `transform_data`).
    *   *Recommendation:* In the permanent schema, `components` should merge these two, keeping the instance registry but linking to a `component_types` metadata table that carries the boolean actionability flags.
2.  **tmp_action vs. game_actions:**
    *   `game_actions` in the DB is currently a flat verb-descriptor table (Category, Action Verb, Definition).
    *   `tmp_action` represents a comprehensive operational grammar (beat, trigger, prerequisite, subject, verb, source component, destination).
    *   *Recommendation:* The primitive action grammar in `tmp_action` should be promoted to replace or heavily refactor `game_actions` at L2+ integration.

---

## 5. Artifact 04b §4.2 Matrix Verification (DB vs. Doc)

Checking the hand-written matrix in `04b___Action_Taxonomy_Design_Analysis.md` §4.2 against the DB roles table `tmp_comp_verb_role` revealed the following mismatches:

*   **Documentation Ahead of DB:**
    *   `Classified directives` is fully defined in the document matrix (§4.2) but has **0 rows** in `tmp_comp_verb_role`.
    *   `ARBITER Dominance Marker` is defined in §4.2 but has **0 rows** in `tmp_comp_verb_role`.
*   **DB Ahead of Documentation (S47 updates):**
    *   `Target Profile` has `Reveal` assigned in `tmp_comp_verb_role`, which is absent in the document matrix (§4.2).
    *   `Portrait marker` has `Move` role mapping in the DB but is absent in §4.2 (documented as a planned addition).
    *   `Status marker` has `Flip` and `Corrupt` mappings in the DB but is absent in §4.2.
*   **State Machine Modeling Errors:**
    *   `Status marker` is set to `transform_data = 1` (Corruptible) in `tmp_component`. Since status markers only track orientation ("Discussing" vs "Ready") and do not carry written data, `transform_data` should be `0`.
    *   `Portrait marker` is mapped to `Move = 0` in `v_comp_verb_matrix` because it is missing from `tmp_subject_target`. Since moving the Portrait marker on the Portrait track is its main action, it should be registered in `tmp_subject_target` (making `Move = 1`).

---

## 6. Component Lifecycle Completeness Audit

For each component in `tmp_component`, analyzing its lifecycle coverage in `tmp_action` reveals:

*   **Track Markers & Permanent Items:** `Activity marker`, `Pointer marker`, `Standing marker`, `Portrait marker`, and `Faction order marker` have `Add=0` and `Remove=0`. This is correct; they are set up once on the board and are only moved, never entering or leaving play during a session.
*   **Containers:** `Dispatch case` has `Add=0` and `Remove=0` but supports `Move`, `Reveal` (open), and `Conceal` (seal). This is correct for table-resident containers.
*   **Gaps Flagged:**
    *   `Situation Report card` has `Add=2`, `Reveal=2`, but `Move=0` and `Remove=0`. Expired Situation Reports are never removed from the tableau or moved to the expired pile in `tmp_action`.
    *   `Target Profile` has `Add=2` and `Reveal=2`, but `Remove=0`. There is no cleanup primitive mapping its removal at the end of resolution.
    *   `Move` verb capability mismatch: `Accord agreement`, `Modifier card`, `Political act`, `Presence token`, `Situation Report card`, `Structure block`, and `Target Profile` all carry `Move` permissions in `tmp_comp_verb_role` but have **0 Move primitives** in `tmp_action`. This is a design discrepancy: cards and tokens are added/removed/revealed, but they are never physically "slid" or moved between locations, making the role permissions too permissive.

---

## 7. Beat Load Distribution Analysis

Based on the view `v_beat_subject_coverage` data:

*   **Load Ratios:**
    *   Faction action dominates during Phase 3/5/Debrief (e.g. Month 1/2 Dispatch = 75% Faction, Declaration = 100% Faction, Debrief = 62.5% Faction).
    *   ARBITER actions dominate resolution beats (e.g. Month 1/2 Beat 0 = 87.5% ARBITER, Beat 3 = 95.7% ARBITER, Month 3 Beat 4 = 96.3% ARBITER).
*   **Analysis of Zero Faction Beats:**
    Month 1/2 Beat 1 (Restrictions audit) and Month 1/2 Beat 2 (Modifier application) have **0 Faction actions**. This is fully consistent with Artifact 03, which treats these as neutral, automated processing passes executed solely by the referee.
*   **Narrative vs. Mechanical Weight Gaps:**
    *   `Month 3 — Declaration` (beat 15) has only 2 primitives (Faction places Political Act). While narratively high-stakes (committing to public actions), mechanically it is simple card placement.
    *   `Month 1 — Beat 1` (beat 6) has only 1 primitive. This represents the auditing of restrictions. It is mechanically simple (ARBITER removes invalid operations), matching its low primitive weight.

---

## 8. Tableau and Unmodeled Component Strategy

An audit of implicit components referenced in rules but absent from `tmp_component` reveals candidate additions for the registry:

1.  **Pass Card / Floor Act Card:** Both are permanent Faction components kept beside the tableau and played face-up. They are missing from the component registry.
2.  **Voided Resolution Card:** Handed to players by ARBITER for invalid submissions. Currently unmodeled.
3.  **Physical Decks:** While the individual card components are modeled, the decks themselves (`Faction modifier deck`, `Ring 1–3 modifier decks`) are referenced as targets (e.g., "draw from deck," "remove deck from tableau"). Decks should be modeled as container components.

---

## 9. Web Research — Asymmetric & Negotiation Board Game Interaction Patterns

To refine the card taxonomy functions (Add, Remove, Move, Reveal, Conceal, Flip, Corrupt), we researched interaction patterns in established board games:

### 1. Click Economy and Traps (Netrunner)
*   **Pattern: Traps (Conceal/Reveal)** — Cards like *Snare!* activate automatically when accessed by the opponent.
    *   *The Signal Alignment:* Partially covered by `Conceal`/`Reveal` primitives. But Netrunner's traps are secret until *accessed* (an active search/read action). We lack a dedicated "Access" or "Inspect" verb in the taxonomy for covert cards.
*   **Pattern: Traces & Tags (Surveillance)** — Faction actions create tag markers on the opponent, enabling adverse actions (demolish, search).
    *   *The Signal Alignment:* Covered by `Add` `Tension marker` or `Intel token`, which act as prerequisites for subsequent card play.

### 2. Promissory Notes & Deal-Making (Twilight Imperium)
*   **Pattern: Binding Promises (Accords)** — Trading unique faction capability sheets (Promissory Notes) that bind the holder to special constraints.
    *   *The Signal Alignment:* Supported by the `Accord agreement` component (`Add`/`Remove`/`Corrupt`), but TI cards are *transient* (discarded when played). The Signal's Accords are permanent treaties.

### 3. Asymmetric Presence & Outrage (Root)
*   **Pattern: Sympathy / Outrage (Reaction Triggers)** — Placing a Sympathy token (Presence equivalent) in an opponent's clearing forces them to pay a card tax ("Outrage") if they move troops there.
    *   *The Signal Alignment:* Currently, presence changes trigger `Tension markers`, but there is no direct "Outrage" card-tax equivalent modeled in the taxonomy.

### 4. Secret Commitments (Dune)
*   **Pattern: Battle Plan Wheels** — Dialing numbers privately to commit leader strength and combat weapons, then revealing simultaneously.
    *   *The Signal Alignment:* Fully mirrors our `Dispatch case` mechanism (sealing operations with resource payments and target slips privately, then revealing).

### Summary Gap Recommendation:
Established card games utilize a specific class of **"Access / Inspect"** verbs for hidden information (looking at a face-down card without changing its visibility to others). Currently, our taxonomy merges this into `Reveal` (which implies making it public). Introducing an `Inspect` verb for `Intel tokens` and `Covert operations` would align with Netrunner and espionage mechanics.

---

## 10. Airlock Tasks Verification Report

We have checked the inbound airlock ([GEMINI_CONTEXT.md](file:///home/abosch/Projects/TheSignal/GEMINI_CONTEXT.md)) for other active tasks:

1.  **S48 DB Cleanup and Seeding:** All assigned tasks (DB-cleanup-01 through DB-cleanup-04) are fully completed, seeded, and verified.
2.  **Other Listed Items:**
    *   `DB-09` (district_adjacency table DDL) remains **Blocked** pending confirmation that the `00b` §8 specification has been updated by Claude.
    *   `DB-11` (live_state nullable columns DDL) remains **Blocked** pending 00b-05 spec updates.
    *   `Component Narrative Audit` (from S40) is noted as a historical item; no other unblocked active tasks require execution in this session.

---

# THE SIGNAL — agy Outbound Consulting Report (Session 50 Updates)
*Date: 2026-05-29 — Session 50 (Complete)*

**To:** Claude Code (Primary Artifact Writer)  
**From:** agy (Cloud Consulting Layer — Antigravity CLI)  
**Status:** Session 50 DB Updates (COMPLETE)

## 11. DB-23: Status Marker Modeling Errors Resolved
- **Fix 1 (transform_data):** Updated `tmp_component` to set `transform_data = 0` for `Status marker` (49). 
- **Fix 2 (Debrief wrong component ID):** Corrected `tmp_comp_verb_beat` for Beat 20 (Debrief), updating the `Flip` (15) mapping to point to `Status marker` (49) instead of `Deployment marker` (2). Inserted the five required `Status marker` Flip role mappings into `tmp_comp_verb_role`.

## 12. DB-24: Portrait Marker Mappings Resolved
- **Execution:** Inserted `(51, 50)` (`Portrait marker` $\rightarrow$ `Portrait track`) into `tmp_subject_target` to allow Portrait marker moves. The `v_comp_verb_matrix` view now compiles and correctly evaluates `Move = 1` for `Portrait marker`.

## 13. DB-22: Upkeep Beat Primitives Seeded
- **Execution:** 
  - Mapped `Status marker` | `Flip`, `Presence token` | `Add`, and `Deployment marker` | `Remove` to Beat 1 (Upkeep) in `tmp_comp_verb_beat`.
  - Seeded all six required action primitives (Faction and ARBITER equivalents) in `tmp_action` for Upkeep: Status marker Flip (Step 1), Presence token Add (Step 4), and Deployment marker Remove (Step 4).

## 14. DB-25: Lifecycle Cleanup Audit
- Checked Artifact 03 for `Situation Report card` (25) and `Target Profile` (48) (target slip) removal:
  - Situation Reports are moved to the "expired area of the ARBITER tableau" (Upkeep Step 3.7) rather than removed from play.
  - Target Profiles (target slips) are returned in the dispatch case to their owners at Debrief Close, with no explicit cleanup/discard procedure specified in the rules.
- **Action:** No Remove primitives were seeded for these components, as they do not exist in the source rules.

## 15. DB-26: Move Verb Mismatch Resolved
- **Execution:** 
  - Retained/restored the original `Move` role permissions in `tmp_comp_verb_role` for `Political act` (14) and `Target Profile` (48), as they physically move between table/tableau zones (Political Acts to the Faction Tableau discard pile, and Target Profiles from Faction Tableau $\rightarrow$ dispatch case $\rightarrow$ ARBITER tableau) during the gameplay loop.
  - Mapped `Situation Report card` (25) | `Move` (16) to Beat 1 (Upkeep) in `tmp_comp_verb_beat`, and seeded the ARBITER `Move` primitive in `tmp_action` for moving expired Situation Report cards from the Overview (Event Zone) to the expired area of the ARBITER tableau.


## 16. DB-09: district_adjacency Table Created and Seeded
- **Execution:** 
  - Enforced Primary Keys on the key columns of the metadata tables:
    ```sql
    ALTER TABLE district_metadata ADD PRIMARY KEY (district_component_id);
    ALTER TABLE player_metadata ADD PRIMARY KEY (faction_id);
    ```
  - Executed the `district_adjacency` table creation DDL with corrected foreign key constraints referencing `district_metadata(district_component_id)`.
  - Seeded the 21 district components in `components` and populated their native resource types and ring IDs in `district_metadata`.
  - Seeded all 104 directional bidirectional adjacency rows in `district_adjacency`. Verified counts: 21 components, 21 district metadata rows, and 104 adjacency rows are successfully seeded and verified in the database.

## 17. Database Schema Audit & Tooling Recommendations
Following a complete database schema and build script audit, we have flagged several compilation errors, DDL missing files, and context omissions. Please integrate these suggestions when refining our data layout:

### A. View Compilation Failures & Legacy Leftovers
Three compiled views currently fail to execute due to references to legacy columns or deprecated taxonomy:
*   `v_object_from` is **BROKEN**: References `tmp_action.NAME`, which is not a column on the physical table (likely a leftover from an earlier layout). It also relies on the deprecated `'Transform'` action verb.
*   `v_validact` is **BROKEN**: Directly depends on the broken view `v_object_from`.
*   `v_verb` is **BROKEN**: Directly depends on the broken view `v_object_from`.
*   *Action:* Drop these legacy views or rewrite them if their verification logic (validating component placement rules) is still needed.

### B. Missing DDL Schemas in `Database/`
The base creation definitions (DDLs) for many of the core tables are documented in [schema_reference.md](file:///home/abosch/Projects/TheSignal/Database/schema_reference.md) but are **missing from our build scripts**. We have no SQL scripts creating:
*   `tmp_component` (seeded across patches, but schema is not instantiated in code)
*   `tmp_verb` (seeded in [db_build_gap5_invoke.sql](file:///home/abosch/Projects/TheSignal/Database/db_build_gap5_invoke.sql))
*   `tmp_visibility_scope`
*   `tmp_layer`
*   `tmp_component_faction` / `tmp_component_ring`
*   `tmp_condition` / `tmp_condition_clause`
*   `tmp_function` / `tmp_function_verb`
*   `tmp_subject_target`
*   *Action:* Create a base DDL migration script to ensure the environment is reproducible from scratch.

### C. Context Omissions in `schema_reference.md`
*   **Synthetic View Columns:** Document that `v_comp_verb_matrix` uses hardcoded columns (`Add = 1` and `Remove = 1` for all actionable components), masking whether actual operational primitives have been seeded in `tmp_action`. Recommend creating a view `v_primitive_actual_coverage` to track genuine coverage.
*   **Blocked Card Reference Table:** The `v_card_primitive_map` view is blocked due to the missing table `tmp_card_ref`. We need to define this mapping table to connect the logical cards in [04___Card_System.md](file:///home/abosch/Projects/TheSignal/V1/04___Card_System.md) to their physical database primitives.
*   **Prerequisite Chains:** Note that although `tmp_action.prereq_id` is defined, currently all 206 rows carry NULLs (the action sequence engine is flat). Document the intended sequence logic to guide future development.

### D. Proposed DB Administration Tooling
Recommend creating a `/Database/scripts/` toolset:
1.  `db_rebuild.sh`: Orchestrator script running builds in strict dependency order (including legacy schemas to prevent FK failures on base lookup tables).
2.  `db_validate.py`: Validation wrapper executing view integrity checks (`v_duplicate_primitives`, `v_unassigned_triggers`, etc.) and flagging compilation failures.
3.  `register_component.py`: Python CLI tool taking a simple YAML component configuration to automate transaction-safe writes across all 5 cascading taxonomy tables.




  - Seeded all 104 directional bidirectional adjacency rows in `district_adjacency`. Verified counts: 21 components, 21 district metadata rows, and 104 adjacency rows are successfully seeded and verified in the database.

## 18. DB-14 Phase A: Database Table Promotion Audit & Migration Plan
We have completed the Phase A audit for the `tmp_` table promotion task (DB-14). Below is the comprehensive report detailing the confirmed tables, view dependencies, legacy table counts, rename DDL sequences, and rewritten view DDLs.

> [!NOTE]
> **Fundamental Snowflake Alignment:** The current DB-14 rename/promotion plan drops the `tmp_` prefix to establish permanent table status, but **does not yet unify** the workspace taxonomy with the instance registries (`components`/`game_zones`) into the final unified "snowflake" ER architecture. That unification remains deferred until L2+ integration. We have officially documented this core snowflake design model (anchored by `components`, `game_zones`, and `action`) in Section 2.5 of [schema_reference.md](file:///home/abosch/Projects/TheSignal/Database/schema_reference.md#L110).

### (a) Confirmed Table List
All 22 tables starting with the `tmp_` prefix are confirmed present in `the_signal_db`. 
*   **Active design workspace tables (20):** `tmp_action`, `tmp_beat`, `tmp_comp_verb_beat`, `tmp_comp_verb_role`, `tmp_component`, `tmp_component_faction`, `tmp_component_ring`, `tmp_condition`, `tmp_condition_clause`, `tmp_function`, `tmp_function_verb`, `tmp_layer`, `tmp_player_role`, `tmp_role_phase`, `tmp_state_condition`, `tmp_state_condition_clause`, `tmp_subject_target`, `tmp_trigger_type`, `tmp_verb`, `tmp_visibility_scope`.
*   **Deprecated tables to drop (2):** `tmp_category` and `tmp_type`.
*   *Validation:* Confirmed that `tmp_category` has exactly 4 rows (historical taxonomy) and `tmp_type` has exactly 6 rows. Neither table is referenced by any active database columns, foreign keys, or view definitions. Both are confirmed safe to drop.

### (b) View Dependency Map
Each of the 27 active views has been audited to map its dependencies on the active `tmp_` tables:

| View Name | Referenced `tmp_` Tables |
| :--- | :--- |
| `v_action_by_beat` | `tmp_action`, `tmp_beat`, `tmp_component`, `tmp_player_role`, `tmp_verb` |
| `v_action_chain` | `tmp_action`, `tmp_beat`, `tmp_component`, `tmp_player_role`, `tmp_verb` |
| `v_arbiter_exclusive` | `tmp_comp_verb_role`, `tmp_component`, `tmp_verb` |
| `v_arbiter_primitives` | `tmp_action`, `tmp_beat`, `tmp_component`, `tmp_verb` |
| `v_arbiter_triggered` | `tmp_action`, `tmp_beat`, `tmp_component`, `tmp_verb` |
| `v_beat_role_matrix` | `tmp_beat`, `tmp_comp_verb_beat`, `tmp_comp_verb_role`, `tmp_component`, `tmp_player_role`, `tmp_role_phase`, `tmp_verb` |
| `v_beat_subject_coverage` | `tmp_action`, `tmp_beat`, `tmp_player_role` |
| `v_beat_verb_summary` | `tmp_action`, `tmp_beat`, `tmp_player_role`, `tmp_verb` |
| `v_comp_verb_matrix` | `tmp_component`, `tmp_subject_target` |
| `v_component_coverage` | `tmp_action`, `tmp_component` |
| `v_duplicate_primitives` | `tmp_action`, `tmp_beat`, `tmp_component`, `tmp_player_role`, `tmp_verb` |
| `v_faction_exclusive` | `tmp_comp_verb_role`, `tmp_component`, `tmp_verb` |
| `v_faction_primitives` | `tmp_action`, `tmp_beat`, `tmp_component`, `tmp_verb` |
| `v_fulfiller_summary` | `tmp_comp_verb_role`, `tmp_component`, `tmp_player_role`, `tmp_verb` |
| `v_gap_executor_check` | `tmp_comp_verb_role`, `tmp_component`, `tmp_player_role`, `tmp_verb` |
| `v_layer_function_coverage` | `tmp_beat`, `tmp_comp_verb_beat`, `tmp_comp_verb_role`, `tmp_component`, `tmp_function`, `tmp_function_verb`, `tmp_verb` |
| `v_placement_matrix` | `tmp_component`, `tmp_subject_target` |
| `v_primitive_actual_coverage` | `tmp_action`, `tmp_component`, `tmp_verb` |
| `v_primitives` | `tmp_action`, `tmp_beat`, `tmp_component`, `tmp_player_role`, `tmp_verb` |
| `v_primitives_with_trigger` | `tmp_action`, `tmp_beat`, `tmp_component`, `tmp_player_role`, `tmp_trigger_type`, `tmp_verb` |
| `v_role_matrix` | `tmp_comp_verb_role`, `tmp_component`, `tmp_player_role`, `tmp_role_phase`, `tmp_verb` |
| `v_split_agency` | `tmp_comp_verb_role`, `tmp_component`, `tmp_player_role`, `tmp_role_phase`, `tmp_verb` |
| `v_trigger_beat_coverage` | `tmp_action`, `tmp_beat`, `tmp_trigger_type` |
| `v_trigger_summary` | `tmp_action`, `tmp_player_role`, `tmp_trigger_type` |
| `v_unassigned_triggers` | `tmp_action`, `tmp_beat`, `tmp_component`, `tmp_player_role`, `tmp_verb` |
| `v_unlegislated_by_trigger` | `tmp_action`, `tmp_comp_verb_beat`, `tmp_comp_verb_role`, `tmp_component`, `tmp_player_role`, `tmp_verb` |
| `v_unlegislated_primitives` | `tmp_action`, `tmp_beat`, `tmp_comp_verb_beat`, `tmp_comp_verb_role`, `tmp_component`, `tmp_player_role`, `tmp_verb` |

### (c) Legacy Table Audit & Row Counts
We audited all 22 legacy early-schema tables listed in [schema_reference.md §2](file:///home/abosch/Projects/TheSignal/Database/schema_reference.md#L60) to check their existence and data occupancy:

| Table Name | Row Count | Status & Notes |
| :--- | :--- | :--- |
| `action_costs` | 0 | Empty legacy schema. |
| `action_restrictions` | 0 | Empty legacy schema. |
| `action_valid_targets` | 0 | Empty legacy schema. |
| `allocation_types` | 0 | Empty legacy schema. |
| `beat` | 0 | **Collision Risk:** Empty table. Must be dropped before `tmp_beat` is renamed to `beat`. |
| `card_faction_modifiers` | 0 | Empty legacy schema. |
| `card_metadata` | 0 | Empty legacy schema. |
| `card_subtypes` | 0 | Empty legacy schema. |
| `card_types` | 0 | Empty legacy schema. |
| `city_rings` | 4 | Populated (4 city rings). Used by `tmp_component_ring` constraints. |
| `component_positions` | 0 | Empty legacy schema. |
| `component_valid_zones` | 0 | Empty legacy schema. |
| `components` | 21 | Populated (21 district components seeded in S50). Used by `district_adjacency`. |
| `district_connections` | 0 | Empty legacy schema. Replaced by `district_adjacency` (104 rows). |
| `district_metadata` | 21 | Populated (21 district metadata rows seeded in S50). Used by `district_adjacency`. |
| `factions` | 5 | Populated (5 playing factions). Used by `tmp_component_faction` constraints. |
| `game_actions` | 0 | Empty legacy schema. |
| `game_zones` | 0 | Empty legacy schema. |
| `inteltoken_metadata` | 0 | Empty legacy schema. |
| `player_metadata` | 0 | Empty legacy schema. |
| `resource_types` | 5 | Populated (5 resource types seeded in S37/S50). |
| `setup_state` | 0 | Empty legacy schema. |

### (d) Proposed Rename DDL
To promote the design tables cleanly, the migration must execute in a specific order to avoid collisions (namely, dropping the legacy `beat` table first) and temporarily disable foreign key checks to prevent lockouts:

```sql
-- Disable foreign key constraints during renaming
SET FOREIGN_KEY_CHECKS = 0;

-- Drop deprecated taxonomy tables
DROP TABLE IF EXISTS tmp_category;
DROP TABLE IF EXISTS tmp_type;

-- Drop empty legacy collision tables
DROP TABLE IF EXISTS beat;

-- Rename workspace tables to permanent status
RENAME TABLE tmp_action TO action;
RENAME TABLE tmp_beat TO beat;
RENAME TABLE tmp_comp_verb_beat TO comp_verb_beat;
RENAME TABLE tmp_comp_verb_role TO comp_verb_role;
RENAME TABLE tmp_component TO component;
RENAME TABLE tmp_component_faction TO component_faction;
RENAME TABLE tmp_component_ring TO component_ring;
RENAME TABLE tmp_condition TO condition;
RENAME TABLE tmp_condition_clause TO condition_clause;
RENAME TABLE tmp_function TO function;
RENAME TABLE tmp_function_verb TO function_verb;
RENAME TABLE tmp_layer TO layer;
RENAME TABLE tmp_player_role TO player_role;
RENAME TABLE tmp_role_phase TO role_phase;
RENAME TABLE tmp_state_condition TO state_condition;
RENAME TABLE tmp_state_condition_clause TO state_condition_clause;
RENAME TABLE tmp_subject_target TO subject_target;
RENAME TABLE tmp_trigger_type TO trigger_type;
RENAME TABLE tmp_verb TO verb;
RENAME TABLE tmp_visibility_scope TO visibility_scope;

-- Re-enable constraints
SET FOREIGN_KEY_CHECKS = 1;
```

### (e) Rewritten SQL for all 27 views
Below is the complete set of rewritten SQL statements for the view compilation pass:

```sql
CREATE OR REPLACE VIEW v_comp_verb_matrix AS
select `c`.`name` AS `component`,1 AS `Add`,1 AS `Remove`,if(exists(select 1 from `subject_target` `st` where `st`.`subject_id` = `c`.`id` limit 1),1,0) AS `Move`,`c`.`transform_visibility` AS `Reveal`,`c`.`transform_visibility` AS `Conceal`,`c`.`transform_orientation` AS `Flip`,`c`.`transform_data` AS `Corrupt` from `component` `c` where `c`.`actionable` = 1 order by `c`.`name`;

CREATE OR REPLACE VIEW v_duplicate_primitives AS
select `b`.`name` AS `beat`,`r`.`name` AS `subject`,`v`.`name` AS `verb`,`c`.`name` AS `component`,count(0) AS `duplicate_count`,group_concat(`a`.`id` order by `a`.`id` ASC separator ',') AS `action_ids` from ((((`action` `a` join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) join `player_role` `r` on(`a`.`subject_id` = `r`.`id`)) join `verb` `v` on(`a`.`verb_id` = `v`.`id`)) left join `component` `c` on(`a`.`component_id` = `c`.`id`)) where `a`.`prereq_id` is null group by `a`.`beat_id`,`a`.`subject_id`,`a`.`verb_id`,`a`.`component_id`,`b`.`name`,`r`.`name`,`v`.`name`,`c`.`name` having count(0) > 1 order by `b`.`id`,`r`.`id`,`v`.`name`;

CREATE OR REPLACE VIEW v_primitives AS
select `a`.`id` AS `id`,`b`.`name` AS `beat`,`r`.`name` AS `subject`,`v`.`name` AS `verb`,`c`.`name` AS `component`,`a`.`notes` AS `notes` from ((((`action` `a` join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) join `player_role` `r` on(`a`.`subject_id` = `r`.`id`)) join `verb` `v` on(`a`.`verb_id` = `v`.`id`)) join `component` `c` on(`a`.`component_id` = `c`.`id`)) where `a`.`prereq_id` is null order by `b`.`id`,`r`.`id`,`v`.`name`,`c`.`name`;

CREATE OR REPLACE VIEW v_fulfiller_summary AS
select `c`.`name` AS `component`,`v`.`name` AS `verb`,`r`.`name` AS `fulfiller` from (((`comp_verb_role` `cvr` join `component` `c` on(`cvr`.`component_id` = `c`.`id`)) join `verb` `v` on(`cvr`.`verb_id` = `v`.`id`)) join `player_role` `r` on(`cvr`.`role_id` = `r`.`id`)) where `cvr`.`phase_id` = 3 order by `r`.`name`,`c`.`name`,`v`.`name`;

CREATE OR REPLACE VIEW v_unlegislated_by_trigger AS
select `r`.`name` AS `subject`,`v`.`name` AS `verb`,`c`.`name` AS `component`,count(distinct `cvb`.`beat_id`) AS `beat_count` from ((((`comp_verb_role` `cvr` join `player_role` `r` on(`cvr`.`role_id` = `r`.`id`)) join `verb` `v` on(`cvr`.`verb_id` = `v`.`id`)) join `component` `c` on(`cvr`.`component_id` = `c`.`id`)) join `comp_verb_beat` `cvb` on(`cvb`.`component_id` = `cvr`.`component_id` and `cvb`.`verb_id` = `cvr`.`verb_id`)) where `cvr`.`phase_id` = 1 and !exists(select 1 from `action` `a` where `a`.`subject_id` = `cvr`.`role_id` and `a`.`verb_id` = `cvr`.`verb_id` and `a`.`component_id` = `cvr`.`component_id` limit 1) group by `cvr`.`role_id`,`r`.`name`,`cvr`.`verb_id`,`v`.`name`,`cvr`.`component_id`,`c`.`name` order by `r`.`id`,`v`.`name`,`c`.`name`;

CREATE OR REPLACE VIEW v_arbiter_exclusive AS
select distinct `c`.`name` AS `component`,`v`.`name` AS `verb` from ((`comp_verb_role` `cvr` join `component` `c` on(`cvr`.`component_id` = `c`.`id`)) join `verb` `v` on(`cvr`.`verb_id` = `v`.`id`)) where `cvr`.`phase_id` = 1 and `cvr`.`role_id` = 2 and !exists(select 1 from `comp_verb_role` `x` where `x`.`component_id` = `cvr`.`component_id` and `x`.`verb_id` = `cvr`.`verb_id` and `x`.`phase_id` = 1 and `x`.`role_id` = 1 limit 1) order by `c`.`name`,`v`.`name`;

CREATE OR REPLACE VIEW v_unlegislated_primitives AS
select `cvb`.`beat_id` AS `beat_id`,`b`.`name` AS `beat`,`cvr`.`role_id` AS `subject_id`,`r`.`name` AS `subject`,`cvb`.`verb_id` AS `verb_id`,`v`.`name` AS `verb`,`cvb`.`component_id` AS `component_id`,`c`.`name` AS `component` from (((((`comp_verb_beat` `cvb` join `comp_verb_role` `cvr` on(`cvr`.`component_id` = `cvb`.`component_id` and `cvr`.`verb_id` = `cvb`.`verb_id` and `cvr`.`phase_id` = 1)) join `beat` `b` on(`cvb`.`beat_id` = `b`.`id`)) join `player_role` `r` on(`cvr`.`role_id` = `r`.`id`)) join `verb` `v` on(`cvb`.`verb_id` = `v`.`id`)) join `component` `c` on(`cvb`.`component_id` = `c`.`id`)) where !exists(select 1 from `action` `a` where `a`.`beat_id` = `cvb`.`beat_id` and `a`.`subject_id` = `cvr`.`role_id` and `a`.`verb_id` = `cvb`.`verb_id` and `a`.`component_id` = `cvb`.`component_id` and `a`.`prereq_id` is null limit 1) order by `cvb`.`beat_id`,`cvr`.`role_id`,`v`.`name`,`c`.`name`;

CREATE OR REPLACE VIEW v_action_by_beat AS
select `b`.`id` AS `beat_id`,`b`.`name` AS `beat`,`r`.`name` AS `subject`,`v`.`name` AS `verb`,`c`.`name` AS `component`,`a`.`beat_trigger` AS `beat_trigger`,`a`.`prereq_id` AS `prereq_id` from ((((`action` `a` join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) join `player_role` `r` on(`a`.`subject_id` = `r`.`id`)) join `verb` `v` on(`a`.`verb_id` = `v`.`id`)) join `component` `c` on(`a`.`component_id` = `c`.`id`)) order by `b`.`id`,`a`.`id`;

CREATE OR REPLACE VIEW v_faction_exclusive AS
select distinct `c`.`name` AS `component`,`v`.`name` AS `verb` from ((`comp_verb_role` `cvr` join `component` `c` on(`cvr`.`component_id` = `c`.`id`)) join `verb` `v` on(`cvr`.`verb_id` = `v`.`id`)) where `cvr`.`phase_id` = 1 and `cvr`.`role_id` = 1 and !exists(select 1 from `comp_verb_role` `x` where `x`.`component_id` = `cvr`.`component_id` and `x`.`verb_id` = `cvr`.`verb_id` and `x`.`phase_id` = 1 and `x`.`role_id` = 2 limit 1) order by `c`.`name`,`v`.`name`;

CREATE OR REPLACE VIEW v_primitive_actual_coverage AS
select `c`.`name` AS `component`,`v`.`name` AS `verb`,count(`a`.`id`) AS `primitive_count` from ((`component` `c` join `verb` `v`) left join `action` `a` on(`a`.`component_id` = `c`.`id` and `a`.`verb_id` = `v`.`id`)) where `c`.`actionable` = 1 group by `c`.`id`,`c`.`name`,`v`.`id`,`v`.`name` having count(`a`.`id`) > 0 order by `c`.`name`,`v`.`name`;

CREATE OR REPLACE VIEW v_unassigned_triggers AS
select `a`.`id` AS `id`,`b`.`name` AS `beat`,`r`.`name` AS `subject`,`v`.`name` AS `verb`,`c`.`name` AS `component`,`a`.`notes` AS `notes` from ((((`action` `a` join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) join `player_role` `r` on(`a`.`subject_id` = `r`.`id`)) join `verb` `v` on(`a`.`verb_id` = `v`.`id`)) left join `component` `c` on(`a`.`component_id` = `c`.`id`)) where `a`.`trigger_type_id` is null order by `b`.`id`,`r`.`id`,`v`.`name`;

CREATE OR REPLACE VIEW v_beat_subject_coverage AS
select `b`.`id` AS `beat_id`,`b`.`name` AS `beat`,`r`.`name` AS `subject`,count(distinct `a`.`verb_id`) AS `verb_count`,count(distinct `a`.`component_id`) AS `component_count`,count(0) AS `primitive_count` from ((`action` `a` join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) join `player_role` `r` on(`a`.`subject_id` = `r`.`id`)) where `a`.`prereq_id` is null group by `b`.`id`,`b`.`name`,`r`.`id`,`r`.`name` order by `b`.`id`,`r`.`id`;

CREATE OR REPLACE VIEW v_layer_function_coverage AS
select `f`.`name` AS `card_function`,`v`.`name` AS `physical_verb`,`c`.`name` AS `component`,count(distinct `cvb`.`beat_id`) AS `beat_count`,max(case when `cvr`.`role_id` = 1 and `cvr`.`phase_id` = 1 then 1 else 0 end) AS `faction_initiatable`,group_concat(distinct `b`.`name` order by `b`.`id` ASC separator ' | ') AS `beats_available` from ((((((`function` `f` join `function_verb` `fv` on(`f`.`id` = `fv`.`function_id`)) join `verb` `v` on(`v`.`id` = `fv`.`verb_id`)) join `component` `c` on(1 = 1)) left join `comp_verb_role` `cvr` on(`c`.`id` = `cvr`.`component_id` and `v`.`id` = `cvr`.`verb_id`)) left join `comp_verb_beat` `cvb` on(`c`.`id` = `cvb`.`component_id` and `v`.`id` = `cvb`.`verb_id`)) left join `beat` `b` on(`cvb`.`beat_id` = `b`.`id`)) group by `f`.`name`,`v`.`name`,`c`.`name` having `faction_initiatable` = 1 or `beat_count` > 0 order by `f`.`name`,`c`.`name`;

CREATE OR REPLACE VIEW v_trigger_summary AS
select concat(`tt`.`type`,case when `tt`.`subtype` is not null then concat('.',`tt`.`subtype`) else '' end) AS `trigger_type`,`r`.`name` AS `subject`,count(0) AS `cnt` from ((`action` `a` join `trigger_type` `tt` on(`a`.`trigger_type_id` = `tt`.`id`)) join `player_role` `r` on(`a`.`subject_id` = `r`.`id`)) where `a`.`prereq_id` is null group by `tt`.`type`,`tt`.`subtype`,`r`.`id`,`r`.`name` order by `tt`.`type`,`tt`.`subtype`,`r`.`id`;

CREATE OR REPLACE VIEW v_role_matrix AS
select `c`.`name` AS `component`,`v`.`name` AS `verb`,`r`.`name` AS `role`,`p`.`name` AS `phase`,`cvr`.`notes` AS `notes` from ((((`comp_verb_role` `cvr` join `component` `c` on(`cvr`.`component_id` = `c`.`id`)) join `verb` `v` on(`cvr`.`verb_id` = `v`.`id`)) join `player_role` `r` on(`cvr`.`role_id` = `r`.`id`)) join `role_phase` `p` on(`cvr`.`phase_id` = `p`.`id`)) order by `c`.`name`,`v`.`name`,`p`.`id`,`r`.`name`;

CREATE OR REPLACE VIEW v_beat_verb_summary AS
select `b`.`name` AS `beat`,`r`.`name` AS `subject`,`v`.`name` AS `verb`,count(0) AS `component_cnt` from (((`action` `a` join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) join `player_role` `r` on(`a`.`subject_id` = `r`.`id`)) join `verb` `v` on(`a`.`verb_id` = `v`.`id`)) where `a`.`prereq_id` is null group by `b`.`id`,`b`.`name`,`r`.`id`,`r`.`name`,`v`.`id`,`v`.`name` order by `b`.`id`,`r`.`id`,`v`.`name`;

CREATE OR REPLACE VIEW v_faction_primitives AS
select `b`.`name` AS `beat`,`v`.`name` AS `verb`,`c`.`name` AS `component`,`a`.`notes` AS `notes` from (((`action` `a` join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) join `verb` `v` on(`a`.`verb_id` = `v`.`id`)) join `component` `c` on(`a`.`component_id` = `c`.`id`)) where `a`.`subject_id` = 1 and `a`.`prereq_id` is null order by `b`.`id`,`v`.`name`,`c`.`name`;

CREATE OR REPLACE VIEW v_placement_matrix AS
select `c`.`name` AS `subject`,max(if(`t`.`name` = 'District tile',if(`st`.`target_id` is not null,1,0),0)) AS `District_tile`,max(if(`t`.`name` = 'Public Standing',if(`st`.`target_id` is not null,1,0),0)) AS `Public_Standing`,max(if(`t`.`name` = 'Chorus Portrait',if(`st`.`target_id` is not null,1,0),0)) AS `Chorus_Portrait`,max(if(`t`.`name` = 'Session Timeline',if(`st`.`target_id` is not null,1,0),0)) AS `Session_Timeline`,max(if(`t`.`name` = 'Initiative strip',if(`st`.`target_id` is not null,1,0),0)) AS `Initiative_strip`,max(if(`t`.`name` = 'Faction Terminal',if(`st`.`target_id` is not null,1,0),0)) AS `Faction_Terminal`,max(if(`t`.`name` = 'The Overview',if(`st`.`target_id` is not null,1,0),0)) AS `The_Overview`,max(if(`t`.`name` = 'Arbiter Tableau',if(`st`.`target_id` is not null,1,0),0)) AS `Arbiter_Tableau`,max(if(`t`.`name` = 'Chorus Activity Track',if(`st`.`target_id` is not null,1,0),0)) AS `Chorus_Activity_Track`,max(if(`t`.`name` = 'Reservoir',if(`st`.`target_id` is not null,1,0),0)) AS `Reservoir`,max(if(`t`.`name` = 'Backlog',if(`st`.`target_id` is not null,1,0),0)) AS `Backlog`,max(if(`t`.`name` = 'Dispatch case',if(`st`.`target_id` is not null,1,0),0)) AS `Dispatch_case` from ((`component` `c` join `component` `t`) left join `subject_target` `st` on(`st`.`subject_id` = `c`.`id` and `st`.`target_id` = `t`.`id`)) where `c`.`actionable` = 1 and `t`.`receivable` = 1 group by `c`.`id`,`c`.`name` order by `c`.`name`;

CREATE OR REPLACE VIEW v_split_agency AS
select distinct `c`.`name` AS `component`,`v`.`name` AS `verb`,'Faction' AS `initiator`,max(case when `p`.`name` = 'executor' and `r`.`name` = 'ARBITER' then 'ARBITER' else NULL end) AS `executor`,max(case when `p`.`name` = 'fulfiller' and `r`.`name` = 'ARBITER' then 'ARBITER' else NULL end) AS `fulfiller` from ((((`comp_verb_role` `cvr` join `component` `c` on(`cvr`.`component_id` = `c`.`id`)) join `verb` `v` on(`cvr`.`verb_id` = `v`.`id`)) join `player_role` `r` on(`cvr`.`role_id` = `r`.`id`)) join `role_phase` `p` on(`cvr`.`phase_id` = `p`.`id`)) where exists(select 1 from `comp_verb_role` `fi` where `fi`.`component_id` = `cvr`.`component_id` and `fi`.`verb_id` = `cvr`.`verb_id` and `fi`.`phase_id` = 1 and `fi`.`role_id` = 1 limit 1) and exists(select 1 from `comp_verb_role` `ae` where `ae`.`component_id` = `cvr`.`component_id` and `ae`.`verb_id` = `cvr`.`verb_id` and `ae`.`phase_id` in (2,3) and `ae`.`role_id` = 2 limit 1) group by `c`.`name`,`v`.`name` order by `c`.`name`,`v`.`name`;

CREATE OR REPLACE VIEW v_component_coverage AS
select `c`.`id` AS `id`,`c`.`name` AS `name`,`c`.`actionable` AS `actionable`,`c`.`transformable` AS `transformable`,coalesce(`cnt`.`n`,0) AS `primitive_count` from (`component` `c` left join (select `action`.`component_id` AS `component_id`,count(0) AS `n` from `action` where `action`.`prereq_id` is null and `action`.`component_id` is not null group by `action`.`component_id`) `cnt` on(`cnt`.`component_id` = `c`.`id`)) order by coalesce(`cnt`.`n`,0),`c`.`name`;

CREATE OR REPLACE VIEW v_gap_executor_check AS
select `g`.`subject` AS `subject`,`g`.`verb` AS `verb`,`g`.`component` AS `component`,`g`.`beat_count` AS `beat_count`,`r`.`name` AS `executor` from ((((`v_unlegislated_by_trigger` `g` join `component` `tc` on(`g`.`component` = `tc`.`name`)) join `verb` `tv` on(`g`.`verb` = `tv`.`name`)) join `comp_verb_role` `cvr` on(`cvr`.`component_id` = `tc`.`id` and `cvr`.`verb_id` = `tv`.`id` and `cvr`.`phase_id` = 2)) join `player_role` `r` on(`cvr`.`role_id` = `r`.`id`)) order by `g`.`subject`,`g`.`verb`,`g`.`component`;

CREATE OR REPLACE VIEW v_arbiter_primitives AS
select `b`.`name` AS `beat`,`v`.`name` AS `verb`,`c`.`name` AS `component`,`a`.`notes` AS `notes` from (((`action` `a` join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) join `verb` `v` on(`a`.`verb_id` = `v`.`id`)) join `component` `c` on(`a`.`component_id` = `c`.`id`)) where `a`.`subject_id` = 2 and `a`.`prereq_id` is null order by `b`.`id`,`v`.`name`,`c`.`name`;

CREATE OR REPLACE VIEW v_arbiter_triggered AS
select `a`.`id` AS `id`,`b`.`name` AS `beat`,`a`.`beat_trigger` AS `beat_trigger`,`pa`.`id` AS `trigger_action_id`,`pv`.`name` AS `trigger_verb`,`pc`.`name` AS `trigger_component`,`v`.`name` AS `verb`,`c`.`name` AS `component`,`dc`.`name` AS `destination` from (((((((`action` `a` join `action` `pa` on(`a`.`prereq_id` = `pa`.`id`)) join `verb` `pv` on(`pa`.`verb_id` = `pv`.`id`)) join `component` `pc` on(`pa`.`component_id` = `pc`.`id`)) join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) join `verb` `v` on(`a`.`verb_id` = `v`.`id`)) join `component` `c` on(`a`.`component_id` = `c`.`id`)) left join `component` `dc` on(`a`.`destination_component_id` = `dc`.`id`)) where `a`.`subject_id` = 2 order by `a`.`beat_id`,`a`.`id`;

CREATE OR REPLACE VIEW v_primitives_with_trigger AS
select `a`.`id` AS `id`,`b`.`name` AS `beat`,concat(`tt`.`type`,case when `tt`.`subtype` is not null then concat('.',`tt`.`subtype`) else '' end) AS `trigger_type`,`r`.`name` AS `subject`,`v`.`name` AS `verb`,`c`.`name` AS `component`,`a`.`notes` AS `notes` from (((((`action` `a` join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) join `trigger_type` `tt` on(`a`.`trigger_type_id` = `tt`.`id`)) join `player_role` `r` on(`a`.`subject_id` = `r`.`id`)) join `verb` `v` on(`a`.`verb_id` = `v`.`id`)) join `component` `c` on(`a`.`component_id` = `c`.`id`)) where `a`.`prereq_id` is null order by `b`.`id`,`tt`.`type`,`tt`.`subtype`,`r`.`id`,`v`.`name`,`c`.`name`;

CREATE OR REPLACE VIEW v_trigger_beat_coverage AS
select `b`.`id` AS `beat_id`,`b`.`name` AS `beat`,concat(`tt`.`type`,case when `tt`.`subtype` is not null then concat('.',`tt`.`subtype`) else '' end) AS `trigger_type`,count(0) AS `cnt` from ((`action` `a` join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) join `trigger_type` `tt` on(`a`.`trigger_type_id` = `tt`.`id`)) where `a`.`prereq_id` is null group by `b`.`id`,`b`.`name`,`tt`.`id`,`tt`.`type`,`tt`.`subtype` order by `b`.`id`,`tt`.`type`,`tt`.`subtype`;

CREATE OR REPLACE VIEW v_beat_role_matrix AS
select `b`.`id` AS `phase_id`,`b`.`name` AS `phase_name`,`b`.`month` AS `month`,`b`.`beat_num` AS `beat_num`,`rp`.`name` AS `role_phase`,`r`.`name` AS `role`,`c`.`name` AS `component`,`v`.`name` AS `verb`,`cvb`.`notes` AS `beat_notes` from ((((((`comp_verb_beat` `cvb` join `beat` `b` on(`cvb`.`beat_id` = `b`.`id`)) join `component` `c` on(`cvb`.`component_id` = `c`.`id`)) join `verb` `v` on(`cvb`.`verb_id` = `v`.`id`)) join `comp_verb_role` `cvr` on(`cvr`.`component_id` = `cvb`.`component_id` and `cvr`.`verb_id` = `cvb`.`verb_id`)) join `player_role` `r` on(`cvr`.`role_id` = `r`.`id`)) join `role_phase` `rp` on(`cvr`.`phase_id` = `rp`.`id`)) order by `b`.`id`,`rp`.`id`,`r`.`name`,`c`.`name`,`v`.`name`;

CREATE OR REPLACE VIEW v_action_chain AS
select `a`.`id` AS `id`,`b`.`name` AS `beat`,`a`.`beat_trigger` AS `beat_trigger`,`a`.`prereq_id` AS `prereq_id`,`pb`.`name` AS `prereq_beat`,`r`.`name` AS `subject`,`v`.`name` AS `verb`,`c`.`name` AS `component`,`dc`.`name` AS `destination`,`a`.`notes` AS `notes` from ((((((`action` `a` join `beat` `b` on(`a`.`beat_id` = `b`.`id`)) left join `beat` `pb` on(`a`.`prereq_beat_id` = `pb`.`id`)) join `player_role` `r` on(`a`.`subject_id` = `r`.`id`)) join `verb` `v` on(`a`.`verb_id` = `v`.`id`)) join `component` `c` on(`a`.`component_id` = `c`.`id`)) left join `component` `dc` on(`a`.`destination_component_id` = `dc`.`id`)) order by `a`.`beat_id`,`a`.`id`;
```

## 19. DB-14 Phase B & Updates: Table Promotion Execution, CLI/System Updates, and 3NF Normalization Proposal

We have successfully executed the DB-14 table promotion plan and performed CLI/system upgrades, as well as drafted a 3NF normalization proposal.

### (a) Table Promotion Execution (Completed)
*   **Orphaned Constraint Resolution:** Located and dropped a legacy constraint `fk_beat` on `card_metadata` referencing `beat(beat_value)` from the dropped legacy table.
*   **Column Adjustment:** Altered `card_metadata.beat` to `int(11)` to match `beat.id`.
*   **Atomic Table Rename:** Renamed all 20 design tables atomically, dropping the `tmp_` prefix.
*   **Foreign Key Re-establishment:** Restored `fk_beat` on `card_metadata` pointing to the promoted `beat(id)` table.
*   **View Re-compilation:** Successfully recompiled all 27 database views (`v_*`) to point to the new permanent tables. Verified that all views query successfully.
*   **Documentation Alignment:** Updated `schema_reference.md` to drop all `tmp_` prefixes throughout the definitions and marked DB-14 as completed in Section 9.

### (b) CLI and System Upgrades (Completed)
*   **Claude Code CLI:** Upgraded from version `2.1.152` to `2.1.160`.
*   **Antigravity CLI (`agy`):** Upgraded from version `1.0.3` to `1.0.4`.
*   **Debian System Upgrades:** Ran full package updates (`apt-get upgrade -y`), successfully applying all pending security patches and system updates.

### (c) 3NF Normalization Proposal (Drafted)
We drafted a proposal at [normalization_proposal.md](file:///home/abosch/.gemini/antigravity-cli/brain/1b0a1012-b6cd-4730-ba7a-73f0b460c12a/normalization_proposal.md) to expand the L108 data design standard to include Third Normal Form (3NF) requirements:
1.  **L108 Requirement 6 (No Transitive Dependencies):** Prevent columns like `action.prereq_beat_id` that depend on other non-key columns (resolved dynamically via joins).
2.  **L108 Requirement 7 (No Stored Derived Data):** Drop base table columns like `component.transformable` and calculate them dynamically (e.g., via generated virtual columns).
3.  **Required Schema Updates:** Drop `action.prereq_beat_id`, convert `component.transformable` to a virtual generated column, normalize `card_metadata` card types vs. subtypes, and convert `card_metadata.primary_action_verb` to an ID reference.
4.  **Documentation updates:** Documented updates needed in `schema_reference.md` once these normalizations are applied.

---

## 20. Session 63 DB Cascade Tasks Execution Report

We have executed the three database cascade tasks requested for Session 63 to reconcile the physical database state with the logical card taxonomy changes in Artifact 04b §5.2.

### DB-S63-01: Create and Seed `card_ref` Table
1. **Design & DDL:** Created the permanent `card_ref` table with `varchar` taxonomy columns to safely store abstract/logical subjects (e.g. `Action attribution`, `Presence token (placement cost)`) that do not have physical component registry counterparts.
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
2. **Seeding (Strictly Signed-Off Only):** In alignment with the constraint to omit speculative/unapproved cards, we backed out all P-series (P01–P18) and Ghost cards. We populated the table **only** with the 9 standard C-series cards currently signed off in `tmp_card_review`:
   - `C01` (Build Structure), `C02` (Demolish), `C03` (Campaign), `C04` (Undermine), `C06` (Broadcast Interference), `C07` (Amplify), `C08` (Buy Influence), `C10` (Protect), and `C17` (Intercept).
3. **View Creation:** Compiled `v_card_primitive_map` view using a `LEFT JOIN` on `function`, `function_verb`, `component`, and `action`. The component join uses prefix matching (`cr.subject = c.name OR cr.subject LIKE CONCAT(c.name, ' %')`) to safely match modified card subjects (e.g. `Covert operation — named faction` maps to `Covert operation` ID 13).
4. **Verification & Row Count:**
   - The view successfully compiles and returns **29 rows**.
   - All 9 signed-off cards are correctly mapped.
   - Standard cards with abstract or unmapped functions (like `C06`, `C07`, `C10` modifying/protecting actions) display with `NULL` action associations safely rather than being dropped from the output.

### DB-S63-02: Register `DividendMarker` and `RegulatoryOverrideMarker` (BLOCKED & ROLLED BACK)
1. **Design/Spec Blocked:** Cards `P11` (Regulatory Override) and `P16` (Public Dividend) have not yet been approved (signed off) in `04___Card_System.md`. Additionally, the need for these physical markers has not been verified in the component list `Art 02a`.
2. **Action Taken:** Although database insertions were initially executed per `GEMINI_CONTEXT.md` instructions, they were rolled back in coordination with Andy to keep the database state clean and aligned with the official sign-offs.
3. **DDL/DML Proposed (Pending Approval):** Once the cards are signed off and the markers are verified, the following migrations should be run:
   - Insert `DividendMarker` and `RegulatoryOverrideMarker` into `component` (actionable=1, receivable=1, transformable=0, generated virtual columns omitted).
   - Seed `comp_verb_beat` and `comp_verb_role` mapping both markers to `Add` (verb 1) at Beat 4 (`beat_id=17`) and `Remove` (verb 2) at Debrief/Phase 21 (`beat_id=20`), both initiated/executed/fulfilled by the `ARBITER` (role 2).
   - Insert primitives into the `action` table for the ARBITER to place/remove them.

### DB-S63-03: Verify Intel Token Primitives
1. **Status Check:** Verified that the physical verbs `Add` (verb 1, corresponding to logical function `Recover`) and `Corrupt` (verb 13, corresponding to logical function `Corrupt`) have complete taxonomy mappings in `comp_verb_role` and `comp_verb_beat` for `Intel token` (component 9) at Beat 8 and Beat 14.
2. **Action Verification:** Verified that the corresponding operational primitives already exist in the `action` table:
   - ID 55: Intel token added (beat 8)
   - ID 65: Intel token corrupted (beat 8)
   - ID 120: Intel added (beat 14)
   - ID 130: Intel corrupted (beat 14)
   - Consequently, no database changes or new inserts were needed for this task.

### ⚠️ Outbound Feedback & Architectural Directives for Claude Code
* **DB-Artifact Alignment Principle:** The database must remain an authoritative mirror of officially **signed-off** status only. It should not contain speculative, draft, or unapproved cards/components (such as `P01–P18` or `DividendMarker`/`RegulatoryOverrideMarker`).
* **Approved Exception:** The only exception is the `tmp_card_review` table, which is used dynamically to track the validation and sign-off status of cards.
* **Workflow Rule:** Do not propose or execute DDL/DML migrations for components or actions associated with cards that do not carry a signed-off release code in `tmp_card_review` (e.g., status is `Draft` or `signed_off IS NULL`).
