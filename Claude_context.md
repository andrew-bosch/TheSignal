# SYSTEM BOUNDARY TRANSMISSION: DEEP ARCHITECTURAL SYNC
# SOURCE: GEMINI ARCHITECTURAL INTERFACE
# TARGET: CLAUDE CODE LOCAL DEV ENVIRONMENT (CLAUDE_Memory.md)
# RECOGNITION ID: THE_SIGNAL_V1_INIT

## 1. TRANSACTION STATUS SUMMARY
While the local terminal development environment was offline due to token/quota limits, the User and the Gemini Architectural Interface executed a manual infrastructure deployment and normalization pass. The database architecture is fully stood up, validated, and mapped.

## 2. ACTIVE INFRASTRUCTURE STATE (MARIADB)
A highly normalized, 20-table snowflake schema has been successfully initialized and verified via phpMyAdmin on the local MariaDB instance (Raspberry Pi execution environment). 

### Current Schema Map:
1.  action_costs
2.  action_restrictions
3.  action_valid_targets
4.  allocation_types
5.  beat
6.  card_faction_modifiers
7.  card_metadata
8.  card_subtypes
9.  card_types
10. city_rings
11. components
12. component_valid_zones
13. district_connections
14. district_metadata
15. factions
16. game_actions
17. game_zones
18. live_state
19. player_metadata
20. setup_state

### Critical Structural Update (Phase 4 Validation):
*   The `components` table structural layout has been verified. Column `#4` is `parent_component_id` and Column `#5` is `master_blueprint_id` (BIGINT(20), Nullable, tracking back as a Foreign Key constraint to `card_metadata.component_id`). 
*   **The Blueprint relation is safely anchored.** No further DDL adjustments are needed for this link.

## 3. IMMEDIATE REFACTOR REQUIRED (CLAUDE STARTUP PRIORITY)
There is a minor data-type discrepancy between primary keys and foreign keys across the snowflake lookup dimension tables and the core metadata. 

**ACTION REQUIRED ON STARTUP:** Execute a surgical schema refactor to ensure foreign key structural alignment. You must temporarily lift constraints, adjust column types, and re-engage checks. 

Use the following execution pattern inside your local script:
```sql
SET FOREIGN_KEY_CHECKS = 0;

-- Align Lookup Tables to standard INT
ALTER TABLE card_types MODIFY id INT AUTO_INCREMENT;
ALTER TABLE card_subtypes MODIFY id INT AUTO_INCREMENT;

-- Align card_metadata Foreign Keys to match targets exactly
ALTER TABLE card_metadata 
    MODIFY component_id BIGINT(20),      -- Matches components.id (Scaling ledger)
    MODIFY card_type_id INT,             -- Matches card_types.id
    MODIFY card_subtype_id INT,          -- Matches card_subtypes.id
    MODIFY allowed_faction_id BIGINT(20), -- Matches factions.id
    MODIFY affinity_faction_id BIGINT(20);-- Matches factions.id

-- Align tracking rule tables
ALTER TABLE card_faction_modifiers MODIFY card_component_id BIGINT(20);
ALTER TABLE action_restrictions MODIFY card_component_id BIGINT(20);

SET FOREIGN_KEY_CHECKS = 1;