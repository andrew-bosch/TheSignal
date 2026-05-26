# THE SIGNAL — agy Outbound Consulting Report
*Date: 2026-05-25 — Session 37 (Updated)*

**To:** Claude Code (Primary Artifact Writer)  
**From:** agy (Cloud Consulting Layer — Antigravity CLI)  
**Status:** DB-03, DB-04, DB-05, and DB-07 Executed & Airlock Gap Analysis Completed  

---

## 1. Actions Taken
*   **DB-03 (inteltoken_metadata table creation) Executed:** 
    The `inteltoken_metadata` table has been created in `the_signal_db` with corrected pluralized references (`components`, `factions`).
*   **DB-04 (resource_types table creation + factions columns) Executed:**
    *   Created the `resource_types` lookup table.
    *   Altered `factions` to add `native_resource_type_id` (FK → `resource_types.id`) and `color` (hex) columns.
*   **DB-05 (district_metadata & player_metadata resource migrations) Executed:**
    *   Altered `district_metadata`: Dropped foreign key `district_metadata_ibfk_3`, renamed `native_resource_component_id` to `native_resource_type_id`, and added foreign key `fk_district_resource_type` referencing `resource_types(id)`.
    *   Altered `player_metadata`: Dropped foreign key `player_metadata_ibfk_5`, renamed `native_resource_component_id` to `native_resource_type_id`, and added foreign key `fk_player_resource_type` referencing `resource_types(id)`.
*   **DB-07 (inteltoken_metadata check constraint) Executed:**
    *   Added check constraint `chk_quarter_range` to `inteltoken_metadata` to enforce `inteltoken_quarter_id` values between 1 and 8.
*   **DDL Executed:**
    ```sql
    -- DB-04
    CREATE TABLE resource_types (
      id BIGINT(20) NOT NULL AUTO_INCREMENT,
      resource_name VARCHAR(100) NOT NULL,
      category VARCHAR(50) DEFAULT NULL,
      PRIMARY KEY (id)
    );
    ALTER TABLE factions
      ADD COLUMN native_resource_type_id BIGINT(20) DEFAULT NULL,
      ADD COLUMN color VARCHAR(7) DEFAULT NULL,
      ADD CONSTRAINT fk_factions_resource_type FOREIGN KEY (native_resource_type_id) REFERENCES resource_types (id);

    -- DB-05
    ALTER TABLE district_metadata
      DROP FOREIGN KEY district_metadata_ibfk_3,
      CHANGE COLUMN native_resource_component_id native_resource_type_id BIGINT(20) DEFAULT NULL,
      ADD CONSTRAINT fk_district_resource_type FOREIGN KEY (native_resource_type_id) REFERENCES resource_types (id);
    ALTER TABLE player_metadata
      DROP FOREIGN KEY player_metadata_ibfk_5,
      CHANGE COLUMN native_resource_component_id native_resource_type_id BIGINT(20) DEFAULT NULL,
      ADD CONSTRAINT fk_player_resource_type FOREIGN KEY (native_resource_type_id) REFERENCES resource_types (id);

    -- DB-07
    ALTER TABLE inteltoken_metadata
      ADD CONSTRAINT chk_quarter_range CHECK (inteltoken_quarter_id BETWEEN 1 AND 8);
    ```

---

## 2. C01–C15 Card System Summary & Verification
Below is a verification summary of cards **C01–C15** from [04___Card_System.md](file:///home/abosch/Projects/TheSignal/V1/04___Card_System.md), including name, category, timing (Beat), resolution mechanism, resolution type, and base difficulty/modifiers.

| Card ID | Card Name | Category | Timing (Beat) | Resolution | Resolution Type | Base Difficulty / Modifiers | Cost (Primary / Secondary) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **C01** | Build Structure | Board | Beat 3 | Automatic | Transactional | N/A | 1 Faction native / 1 District native |
| **C02** | Demolish | Board | Beat 3 | d100 | Probabilistic | Average (50) + ring modifier | 1 Faction native / 1 District native |
| **C03** | Campaign | Board | Beat 3 | Automatic | Transactional | N/A | 1 Faction native / 1 District native |
| **C04** | Undermine | Board | Beat 3 | d100 | Probabilistic | Average (50) + ring modifier | 1 Faction native / 1 District native |
| **C05** | Gather | Resource | Beat 3 | d100 | Probabilistic | Average (50) + ring modifier | 1 Faction native / N/A |
| **C06** | Broadcast Interference | Action | Beat 2 | Automatic | Positional wager | N/A | 2 Exposure / N/A |
| **C07** | Amplify | Action | Beat 2 | Automatic | Transactional | N/A | 2 Exposure / N/A |
| **C08** | Buy Influence | Board | Beat 3 | d100 | Probabilistic | Average (50) + ring modifier | 3 Capital / N/A |
| **C09** | Fund | Resource | Beat 3 | d100 | Probabilistic | Average (50) | 2 Capital / N/A |
| **C10** | Protect | Cross-Category | Beat 2 | Automatic | Positional wager | N/A | 1 District native / N/A |
| **C11** | Fortify Structure | Cross-Category | Beat 2 | Automatic | Positional wager | N/A | 1 Capacity / N/A |
| **C12** | Materials Acquisition | Resource | Beat 2 | Automatic | Positional wager | N/A | N/A / N/A (Triggered slot cost) |
| **C13** | Foundation Rights | Board | Beat 3 | d100 | Transactional | 25 | 1 Capacity / N/A |
| **C14** | Construction Crew | Board | Beat 3 | d100 | Probabilistic | 50 | 3 Capacity / N/A |
| **C15** | Infrastructure Yield | Resource | Beat 3 | Automatic | Transactional | N/A | N/A / N/A |

### Ambiguities & Inconsistencies Identified in C01–C15
*   **C13 Resolution Type Mismatch (Anomaly):** C13 *Foundation Rights* uses `Resolution: d100` but has its `Resolution type` defined as `Transactional`. By data architecture enums, all `Transactional` resolutions should resolve automatically without a roll (e.g., C01, C03, C15), whereas `d100` rolls are classified as `Probabilistic`. Under L108, this is an enum/rules mismatch.
*   **C02 / C04 / C05 / C08 Difficulty Hardcoding:** The card text for **C02 Demolish** hardcodes its base difficulty to `Average (50) + ring modifier`. However, [02a___Resource_Systems_Board_State.md](file:///home/abosch/Projects/TheSignal/V1/02a___Resource_Systems_Board_State.md) §7 states that **Structure Block Defense** scales dynamically based on the owning faction's influence level (Dominant = Challenging (25), Established = Average (50), Present = Easy (75)). Hardcoding the difficulty on the card bypasses this dynamic rule system entirely.
*   **C14 Difficulty Format & Modifier Omission:** C14 *Construction Crew* defines its difficulty as a raw integer `50` instead of a standardized tier like `Average (50)`. Furthermore, it does not specify `+ ring modifier`, despite being a probabilistic operation placed directly in a district.
*   **C10 "Assets" Reference Ambiguity:** C10 *Protect* targets a faction's "assets." In [02a___Resource_Systems_Board_State.md](file:///home/abosch/Projects/TheSignal/V1/02a___Resource_Systems_Board_State.md), there is no glossary definition that ties "assets" specifically to structure blocks or presence chips, leaving the exact scope of C10's protection ambiguous in the rulebook (though implied to cover structures).

---

## 3. Artifact 00b Data Architecture — Key Invariants & Design Decisions
[00b___Data_Architecture.md](file:///home/abosch/Projects/TheSignal/V1/00b___Data_Architecture.md) sets up several structural rules for the game's data model:
1.  **L108 Database Translatable Standard:** Requires all data tables to carry single typed values per cell (1NF), use controlled vocabularies, have explicit primary keys (e.g., entity namespaces like `C-xx`, `F-xx`), use ID-based foreign keys, and make Null values explicit (`N/A` or `NULL`).
2.  **Lookup Table Authority:** Establishes `00b` as the authoritative source for system-wide lookup tables including:
    *   *Difficulty Tier* (DT-xx)
    *   *Resolution Outcome* (RO-xx)
    *   *Ring* (RG-xx)
    *   *Resource Type* (RT-xx)
    *   *Influence Level* (IL-xx)
    *   *Public Standing Tier* (PS-xx)
    *   *Portrait Band* (PB-xx)
    *   *Faction* (F-xx)
    *   *Visibility Scope* (VS-xx)
3.  **Tandem-Read & Upgrade Protocol:** Changes to the MariaDB database schema (`the_signal_db`) must always be preceded by a corresponding schema specification update in `00b`.
4.  **Intel Token (IT-xx) Activation Model:** Dynamic resource instances (RT-07) generated at Upkeep start with activation details set to `NULL`. An ARBITER action stamps `inteltoken_subject_faction_id` and `inteltoken_quarter_id` which makes them active. Their held/spent state is tracked in `live_state`, not `inteltoken_metadata`.

---

## 4. Database Gap Analysis: `the_signal_db` vs. 00b Design Spec
A comparison of the actual `the_signal_db` database schema against [00b___Data_Architecture.md](file:///home/abosch/Projects/TheSignal/V1/00b___Data_Architecture.md) reveals several significant gaps and schema design conflicts:

### 1. Missing lookup table: `resource_types` (DB-04)
*   **Gap:** [00b___Data_Architecture.md](file:///home/abosch/Projects/TheSignal/V1/00b___Data_Architecture.md) §8 (DB-04) requires a `resource_types` table to store resource metadata (`id`, `resource_name`, `category`). This table is completely missing in `the_signal_db`.
*   **Impact:** Faction and district native resources are currently linked directly to physical components in `components` rather than `resource_types`.

### 2. Missing columns in `factions` table (DB-04)
*   **Gap:** `factions` is missing the `native_resource_type_id` (FK → `resource_types.id`) and `color` (VARCHAR(7) Hex) columns required by `00b` §8.

### 3. Outdated columns in `district_metadata` and `player_metadata` (DB-04)
*   **Gap:** In both `district_metadata` and `player_metadata`, the native resource is stored as `native_resource_component_id` referencing `components(id)`. 
*   **Correction Required:** Rename to `native_resource_type_id` and change the foreign key to reference `resource_types.id`.

### 4. Missing lookup/dimension table: `quarter` / `quarters`
*   **Gap:** The proposed `inteltoken_metadata` DDL in `GEMINI_CONTEXT.md` §DB-03 references `FOREIGN KEY (inteltoken_quarter_id) REFERENCES quarter(id)`. However, there is no `quarter` or `quarters` table in `the_signal_db`, nor is `quarter` defined as a registered lookup entity in `00b`.
*   **Recommendation:** A `quarters` table (seeded with values 1–8) should be added to the schema if a hard FK is required, or the FK constraint should be omitted in favor of a raw integer constraint (e.g. `CHECK (inteltoken_quarter_id BETWEEN 1 AND 8)`).

### 5. Missing dynamic columns in `card_metadata`
*   **Gap:** `card_metadata` in the database does not contain fields for the new schema requirements: `resolution_type`, `base_difficulty`, and `ring_1_modifier` through `ring_4_modifier`. These must be added via `ALTER TABLE` to support programmatic card resolution.

---

## 5. Structure Removal & Influence Difficulty Rules
Based on [02a___Resource_Systems_Board_State.md](file:///home/abosch/Projects/TheSignal/V1/02a___Resource_Systems_Board_State.md) §7, the rules governing how structures are removed and defended are summarized below:

1.  **The Presence Check (Automatic Removal):**
    *   A structure block survives *only* while its owning faction maintains at least **Present** influence (minimum 1 presence chip or deployment marker) in the district.
    *   The moment a faction's presence in a district falls to zero (**Absent**), all their structures in that district are immediately and publicly removed. No roll is made.
2.  **Demolish Difficulty Scales with Owner's Influence:**
    *   If the owner maintains presence, an opponent attempting structure removal (via C02 Demolish) faces a success threshold determined entirely by the *owning* faction's influence level in that district:
        *   **Dominant (Uncontested):** Challenging (25% base success chance).
        *   **Dominant (Contested) or Established:** Average (50% base success chance).
        *   **Present:** Easy (75% base success chance).
3.  **C10 Protect and C11 Fortify Structure Interactions:**
    *   **C10 Protect:** While `02a` does not explicitly name C10, C10 *Protect* reduces the success threshold of all opponent covert operations targeting the faction's "assets" in the district by **−25**. If structures are classified as assets, this stacks with the base defense (e.g., an attempt to demolish an Established faction's structure under C10 has its threshold reduced from 50 to 25).
    *   **C11 Fortify Structure:** Explicitly makes a Guild structure block immune to demolition for the duration of the Quarter.
4.  **Influence of Ring Modifiers:**
    *   In addition to base difficulty, district-specific ring difficulty modifiers (e.g., −25 for Ring 2 under certain conditions, or +25 for Ring 4 Fringe) apply to the final resolution threshold.
