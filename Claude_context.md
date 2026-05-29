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
    *   `v_card_primitive_map`: **BLOCKED** (flagged below; requires `tmp_card_ref` seed table)

---

## 2. DB Schema Status & Critical Flags

### 🚫 DB-09 — Create `district_adjacency` Table (STILL BLOCKED & DDL ERROR)
1.  **Blocked on Spec:** Remains blocked until Claude Code updates the `00b` §8 specification to include the `district_adjacency` table.
2.  **DDL Constraint Conflict:** The proposed DDL references `district_metadata(id)` for foreign keys, which fails since `district_metadata` has no `id` column (only `district_component_id`). Change the references to `district_metadata(district_component_id)`.

### 🚫 v_card_primitive_map View (BLOCKED)
This view requires `tmp_card_ref` (mapping `card_id` $\rightarrow$ `component_id`, `verb_id`, `subject_id`). This seed data table has not yet been defined or populated.

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

