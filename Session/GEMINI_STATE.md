# GEMINI WORKING STATE: SESSION 104

## 1. Operating and Search Scope Constraints (Session 104 Lock)
To conserve token context and ensure focus on database validation, agy operates under these strict rules:
1.  **Exclusions:** Ignore and do not scan drafts/stubs (05 and beyond) or the PM suite (`PM01`-`PM05`).
2.  **Narrow Search Targets:** Target queries to `README.md`, `00b` (Data Architecture), `03` (Round Structure), `03a` (Game Engine Spec), and `04b` (Action Matrix) first.
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
*   **Flag uncertainty explicitly:** Cite sources with caveats; never fabricate details.
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

## 3. Session 104 Tasks Status
- **ID-01 (Delete G-ext):** Deleted retired G-ext rows from `card_ref`.
- **ID-02 (Reclassify DebriefActionCard & Grant Deed):** Set `parent_component_id` to `NULL` for components 100 and 113.
- **ID-03 (Add Faction Associations):** Added Ghost, Network, Syndicate, Guild, and Directorate rows for components 116, 117, and 118 in `component_faction`.
- **ID-05 (Idempotency Sweep):** Converted 23 sql/sh scripts in `Database/` to idempotent versions and moved original copies to `Database/archive/`.
- **ID-SCHEMA (Document L219 Taxonomy):** Documented card ID format conventions in `schema_reference.md`.
- **Matrix Verification:** Ran `verify_matrix.py` post-execution. Successfully checked 57 components; found **0 mismatches** against `V1/02___Components.md`.

## 4. Past Session Status (Session 102 & 98)
- **S102 Tasks**: Seeding phase/role cleanup (36 action records). `v_unlegislated_primitives` resolved to 0.
- **S98 Tasks**: Lookup and component metadata seeding.
- **S92 Tasks**: Component 36 renamed to "Escalation marker". Component taxonomy redesign implemented.

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
- **ID-01, ID-02, ID-03:** Executed patch script `Database/db_update_session104.sql` (Session 104).
- **DB View Cleanup Script:** Executed `Database/seed_comp_cleanup.sql` (Session 101).
- **DB View Seeding & Prohibited Cleanup Script:** Executed `Database/seed_comp_cleanup_3.sql` (Session 102).

## 7. Session File Location Index
- **Airlock Report:** `~/Projects/TheSignal/Claude_context.md`
- **Working State:** `~/Projects/TheSignal/Session/GEMINI_STATE.md`
- **Session Patch:** `~/Projects/TheSignal/Database/db_update_session104.sql`
- **Schema Reference:** `~/Projects/TheSignal/Database/schema_reference.md`
- **Registry Python Script:** `~/Projects/TheSignal/Database/register_component.py`
- **YAML Component Template:** `~/Projects/TheSignal/Database/component_template.yaml`
