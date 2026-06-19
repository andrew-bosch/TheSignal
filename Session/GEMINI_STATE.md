# GEMINI WORKING STATE: SESSION 102

## 1. Operating and Search Scope Constraints (Session 102 Lock)
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

## 3. Session 102 Tasks Status
- **DB View Cleanup Script (Session 101):** Executed `Database/seed_comp_cleanup.sql` successfully.
- **DB View Seeding & Prohibited Cleanup Script (Session 102):** Executed `Database/seed_comp_cleanup_3.sql` successfully.
  - Prohibited combinations cleaned from `comp_verb_phase` and `comp_verb_role`.
  - Missing phase associations for permitted combinations registered in `comp_verb_phase`.
  - 36 action records successfully seeded across all monthly/debrief phases in `action`.
- **Verification of views:**
  - `v_unlegislated_by_trigger` count: **0 rows** (successfully resolved to zero gaps).
  - `v_unlegislated_primitives` count: **0 rows** (successfully resolved to zero gaps).
- **GEMINI_CONTEXT.md Pruning:** Completed. All tasks and seed task sections from Session 32 through Session 102 have been pruned.
- **Outbound Report:** Logged all execution results, counts, and confirmation in `Claude_context.md`.

## 4. Past Session Status (Session 98 & 92)
- **S98 Tasks**: Completed Lookup and component metadata seeding.
- **S92 Tasks**: Completed rename of component 36 to `"Escalation marker"` (**DB-38**). Implemented component taxonomy redesign.

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
