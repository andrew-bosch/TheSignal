# GEMINI WORKING STATE: SESSION 97

## 1. Operating and Search Scope Constraints (Session 97 Lock)
To conserve token context and ensure focus on database validation, agy operates under these strict rules:
1.  **Exclusions:** Ignore and do not scan drafts/stubs (05 and beyond) or the PM suite (`PM01`-`PM05`).
2.  **Narrow Search Targets:** Target queries to `README.md`, `00b` (Data Architecture), `03` (Round Structure), `03a` (Engine Spec), and `04b` (Action Matrix) first.
3.  **Search Escalation:**
    - Level 1: Core narrow set.
    - Level 2: Expand only to signed-off V1 artifacts (00–04b).
    - Level 3: Stop and request user/Claude clarification if a term remains unfindable.
4.  **Git Operations:** Do **not** execute `git pull` or any remote git commands. The repository is entirely local, and git is strictly used for local tracking and player viewing.

### Output Standards
*   **Explain reasoning:** Show the logic chain; cite specific sections for inconsistencies.
*   **Structured output:** Use tables for audits/analysis; keep prose dense with no padding.
*   **Do not summarize:** Deliver complete inventories (no representative examples), flag all instances of X.
*   **Verify work:** Double-check claims, quotes, rule numbers, and file references against source files before submitting.
*   **Flag uncertainty explicitly:** Cite sources with caveats (e.g., *"I believe I saw X in Y — recommend Claude verify before actioning"*); never fabricate details.
*   **Complete the task:** Deliver full output in a single pass without stopping halfway.

### Working with Andy
*   **Tone:** High-value, densely informational, no warm framing. Structured lists for status/data; prose for narrative strategy.
*   **Confirmations:** Treat brief confirmations ("yes", "agree", "good") as complete authorizations.
*   **Answering style:** Address specific questions directly first, then address the deeper philosophical framing. Follow generative spirals and develop deeper implications.
*   **Offhand comments:** Treat mid-work remarks as creative/worldbuilding direction.
*   **Blocked decisions:** Treat "we can develop it further when we get to that review" as complete direction, not ambiguity.
*   **No recapping:** Do not recap what was done. End responses with what's next. Andy reads the artifacts.


## 2. Latest Alignment
- Nickname: agy
- Filesystem: CLI-to-CLI local sync
- Role: Cloud Consultant (Validator/Research)
- Environment: Antigravity CLI (migrated)

## 3. Session 98 Tasks Status
- **DB-43 Seeding (Phase 1 Lookups):** Completed.
  - Created and seeded `public_standing_tier` (5 rows), `difficulty_tier` (3 rows), `resolution_outcome` (5 rows), and `influence_level` (4 rows).
- **DB-42 Seeding (component_metadata):** Completed.
  - Created table `component_metadata` using Option A (hybrid wide table) with TEXT columns to support large string values.
  - Parsed `02___Components.md` and successfully seeded 74 rows of metadata using `seed_component_metadata.py`.
- **DB-41 Seeding (Verb Additions):** Completed.
  - Executed `seed_comp_verbs.py` to seed comp_verb_phase and comp_verb_role entries for d10 (119), Modifier token (47) Flip, Sliders (106, 107), card containers, Faction hand (94), and Operative Pool (116).
  - Also seeded missing DB-40 Reveal additions: DebriefActionCard (100), Intel Delivery Slip (96), Notification Slip (95), Grant Deed (113).
  - Updated transform flags in `component` table for components 42, 108, 48, 95, 96.
  - Added missing `subject_target` records for components 49, 98, 108.
  - Verified view matrix: **0 mismatches** found across all actionable components. All 28 views compile successfully.
- **Outbound Report:** Logged all execution results, counts, and schemas to `Claude_context.md`.

## 4. Past Session Status (Session 92 & 50)
- **S92 Tasks**: Completed rename of component 36 to `"Escalation marker"` (**DB-38**). Implemented component taxonomy redesign (**DB-32**), adding `parent_component_id` to `component` table and creating/seeding `component_dim` and `component_type` tables (70 rows each). Handled pushback for 5 Operation Resolution grandchildren. Updated registry tools and documentation.
- **S50 agy Punch List**: Completed. Executed all database updates for DB-22 through DB-26. Resolved DB-09 DDL block by adding Primary Key constraints to `district_metadata` and `player_metadata`. Verified all views and view compiling.

## 5. Current Investigations
### 1. The Ring Numbering Discrepancy
- **Artifact SOT (00b, 01):** Outside-In (RG-01=Sprawl, RG-04=Chorus Node).
- **Session 32 Narrative:** Inside-Out (Ring 1=Chorus Node, Ring 4=Fringe).
- *Strategy:* Flag this to Claude and Andy. The artifacts need an update if the "Dubai/Inside-Out" framing is locked.

### 2. The Apex Source
- Found in **Art 05 (Operative/Apex System)** and **Art 03a (Game Engine Spec)**.
- `is_apex` is a required boolean for the `Payment_Validation` procedure (Art 03a §6).

### 3. C13 Anomaly
- Confirmed: `Resolution: d100` paired with `Resolution Type: Transactional`. 
- Every other `Transactional` card is `Automatic`.
- Every other `d100` card is `Probabilistic`.

### 4. Card System Audit (C16–C35, P01–P18)
- **Ghost (C16–C20):** High-complexity mechanics. C16 (Pattern Match) is a unique "Prediction" card (no roll). C18/C19 flagged for duplication.
- **Directorate (C21–C25):** Focus on "Blocking" (C21, C25) and "Permanent State" (C22, C23, C24).
- **Network (C26–C30):** Focus on disclosure. C27 (Source Protection) flagged as doctrinally misaligned.
- **Syndicate (C31–C35):** Resource-heavy. C31 (Leveraged Acquisition) gain without presence. C33 (Hostile Acquisition) flips color.
- **Political Acts (P01–P18):** All Beat 4. Categories and affinities verified. P01–P08 standard, P09–P18 faction-specific.

### 5. Data Right-Sizing
- Need to convert `BIGINT(20)` to `INT` or `SMALLINT` for Pi hardware.
- `current_value` on tracks (0-20) can be `TINYINT`.
- `component_id` may still need `BIGINT` if the serial registry is massive.

## 6. Completed DB Execution Tasks
- **DB-03:** Created `inteltoken_metadata` (Session 36).
- **DB-04:** Created `resource_types` and patched `factions` columns (Session 37).
- **DB-05:** Migrated native resource columns in `district_metadata` and `player_metadata` (Session 37).
- **DB-07:** Added check constraint to `inteltoken_metadata.inteltoken_quarter_id` (Session 37).
- **DB-11:** Renamed `live_state` to `component_positions`, renamed `anchored_to_component_id` to `on_component_id` (nullable), and added `on_game_zone_id` (Session 43).
- **DB-16 (tmp_component updates):** Populated missing physical components in the `tmp_component` table and updated "Operational marker" to "Deployment marker" (Session 46/47).

## 7. Session File Location Index
- **Airlock Report:** `~/Projects/TheSignal/Claude_context.md`
- **Working State:** `~/Projects/TheSignal/Session/GEMINI_STATE.md`
- **Session Brief:** `~/Projects/TheSignal/Session/SESSION_BRIEF.md`
- **Schema Reference:** `~/Projects/TheSignal/Database/schema_reference.md`
- **Registry Python Script:** `~/Projects/TheSignal/Database/register_component.py`
- **YAML Component Template:** `~/Projects/TheSignal/Database/component_template.yaml`
