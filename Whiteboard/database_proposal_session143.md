# Database Proposals & Division of Labor (Session 143)
*Status: Draft — Pending Review & Promotion*

---

## 1. Division of Labor Proposal (Lev, Agy, Claude)

To optimize token usage, minimize context drift, and leverage host system properties:

### 👤 lev (brain - Native Ubuntu Workstation)
* **Token Profile**: Shared weekly usage pool with `agy`.
* **Role**: **Sysadmin & Build/Deploy Manager**.
* **Responsibilities**:
  * Host workstation environment configurations (GNOME, monitors, shell terminals).
  * Static site compilation pipelines (`build_wiki.py`) and deployment synchronization tasks to `pinky`.
  * Multi-agent communication/airlock coordination logs.
* **Motto**: "Set up the stage and keep the tools running."

### 👤 agy (wakko - Raspberry Pi 5 Node)
* **Token Profile**: Shared weekly usage pool with `lev`.
* **Role**: **Database Administrator (DBA)**.
* **Responsibilities**:
  * Direct execution of DDL (CREATE, ALTER) and DML (INSERT, UPDATE) on `dot`.
  * Database schema sanity audits and constraint verification.
  * Database backup retention scripts and automated cloud dumps.
* **Motto**: "Keep the database clean, normalized, and performant."

### 👤 Claude (wakko - Raspberry Pi 5 Node)
* **Token Profile**: Independent session token pool.
* **Role**: **Primary Application Developer & Lead Designer**.
* **Responsibilities**:
  * Core gameplay logic implementations.
  * Writing and modifying V1 design specifications (e.g. Art 04 §6 normalization).
  * Design stubs, narrative vignettes, and balancing analytics.
* **Motto**: "Build the game's mechanics, balance, and content."

---

## 2. DB Schema Proposals

### 📌 Proposal A: DB-08 Resolution Columns
Add the 6 missing columns required for programmatic card resolution to the `card_metadata` table:

```sql
ALTER TABLE card_metadata
  ADD COLUMN resolution_type VARCHAR(50) DEFAULT NULL,
  ADD COLUMN base_difficulty INT(11) DEFAULT NULL,
  ADD COLUMN ring_1_modifier INT(11) DEFAULT NULL,
  ADD COLUMN ring_2_modifier INT(11) DEFAULT NULL,
  ADD COLUMN ring_3_modifier INT(11) DEFAULT NULL,
  ADD COLUMN ring_4_modifier INT(11) DEFAULT NULL;
```
* **Rationale**: Enables direct storage of d100 vs. Automatic card resolutions, along with default thresholds and geographical ring scaling values.
* **Execution**: To be executed by `agy` on `wakko` after your sign-off.

---

### 📌 Proposal B: DB-21 Beat Multi-Value Representation
Change the single-beat `card_metadata.beat` column (`tinyint(4)`) to a junction table representation to support cards that deploy across multiple beats (e.g., Countermeasure cards active at beats 4, 10, and 16).

```sql
-- 1. Create the L108-compliant junction table
CREATE TABLE IF NOT EXISTS `card_metadata_beat` (
  `card_metadata_id` BIGINT(20) NOT NULL,
  `beat_id` INT(11) NOT NULL,
  PRIMARY KEY (`card_metadata_id`, `beat_id`),
  CONSTRAINT `fk_card_metadata_beat_card` 
    FOREIGN KEY (`card_metadata_id`) REFERENCES `card_metadata` (`component_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_card_metadata_beat_beat` 
    FOREIGN KEY (`beat_id`) REFERENCES `beat` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 2. Populate the junction table from existing metadata single-beat values
INSERT INTO `card_metadata_beat` (`card_metadata_id`, `beat_id`)
SELECT `component_id`, `beat` FROM `card_metadata`;
```
* **Rationale**: Highly normalized (3NF/L108-compliant), prevents comma-separated values inside varchar cells, and uses standard foreign keys.
* **Migration path**:
  1. `agy` creates `card_metadata_beat`.
  2. `agy` migrates existing single-beat rows.
  3. `card_metadata.beat` column is retained as a legacy/fallback field for single-beat queries until deprecated.
* **Execution**: To be executed by `agy` on `wakko` after your sign-off.
