# 00b — Analysis Readiness
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.3
**Status:** ✅ Signed Off — S45 (restructured S83)

**Purpose:** The game system needs to be fully modeled in the DB to enable deep analysis and computational balance work. This document tracks what remains to be migrated. `Database/schema_reference.md` is the authoritative source for migrated entities. This document provides: (1) a pointer to the L108 standard (§3); (2) the migration punchlist (§4).

**Relationship to source artifacts:** Source artifacts remain the canonical design documents. Game-purpose definitions live in source artifacts; this document tracks migration status only.

**Depends on:** 00 — Factions, World & Narrative Context; 00a — Governing Rules & Design Policy

---

## 2. Index

1. [Overview](#1--data-architecture)
2. [Index](#2-index)
3. [L108 Data Table Standard](#3-l108-data-table-standard-extends-3nf)
4. [Migration Punchlist](#4-migration-punchlist)
5. [Entity Relationships](#5-entity-relationships)
6. [Design Notes](#6-design-notes)

---

## 3. L108 Data Table Standard

See **00a §11** for the full L108 standard and column type vocabulary. Compliance status tracked in §5 Migration Punchlist.

---

## 4. Migration Punchlist

All component types (VM-xx, BM-xx, NS-xx, IS-xx, CA-xx, Operative, Modifier Card, Broadcast Card, Countermeasure Card, Emergency Response) are registered in the DB `component` table. Art 02 is the canonical component design list; `schema_reference.md` is the authoritative DB source.

**Lookup tables pending DB migration:** Difficulty Tier (DT-xx), Resolution Outcome (RO-xx), Influence Level (IL-xx), Public Standing Tier (PS-xx), and Portrait Band (PB-xx) are canonically defined in Art 03 reference sections (PS-xx/PB-xx also in Art 07). These tables must be migrated to the DB before game modeling analysis can proceed — probability calculations, balance modeling, and outcome queries all depend on them. No action until tables are finalized in Art 03. Covered by PM05 02-n08.

---

## 5. Entity Relationships

See `Database/schema_reference.md §2.5` for the full entity relationship map and FK semantics.

---

## 6. Design Notes

**Initiative Pattern (IP-xx):** Initiative procedure migrated to Art 07 (PM05 03-11). Schema to be defined there — ID column (IP-01 through IP-10) and full table structure pending Art 07 draft.

**Modifier Card schema (MC-xx):** Will require at minimum: ID, Faction (F-xx | All), Ring (RG-xx | N/A), Value Rating (1–3 per L67), Targeting Constraint (ring-native per L66), Threshold Adjustment. Full design pending D04-08 (modifier card content) and D04-07 (in-world name).

**Event Card schema (EC-xx):** Dual-card system (Broadcast Card public + Event Card ARBITER-only). Schema will need: ID, Public Narrative, Difficulty Modifier (M-xx | N/A), Targeting Restriction (D-xx | RG-xx | N/A), Conversion Block (D-xx | RG-xx | N/A), Public Standing Effect (faction + delta), Duration (quarters). Full design pending Art 07 and Art 09.

**`component_positions` table (component location registry):** Tracks the real-time physical location of every in-play component. One row per active component. `component_positions` is an operational DB table — not a named game entity — and is not registered in §5. Formerly `live_state` (renamed DB-11).

| Column | Type | Null | FK Target | Purpose |
|--------|------|------|-----------|---------|
| `component_id` | bigint | NOT NULL (PK) | components.id | The tracked component |
| `current_zone_id` | bigint | NOT NULL | game_zones.id | Primary zone the component currently occupies |
| `on_component_id` | bigint | NULL | components.id | Parent component this physically rests on. NULL when the component sits directly in a zone rather than on another component. Renamed from `anchored_to_component_id`; constraint changed NOT NULL → NULL. |
| `on_game_zone_id` | bigint | NULL | game_zones.id | Specific zone this component occupies within the physical layout; used when `on_component_id` is NULL. |

*L156 (S40). Locked: option B — component_positions carries both nullable FK columns rather than dual-representing container components as zones. Pending: agy DB-11 — RENAME TABLE `live_state` → `component_positions`; RENAME COLUMN `anchored_to_component_id` → `on_component_id` (change NOT NULL → NULL); ADD COLUMN `on_game_zone_id` (bigint, NULL, FK → game_zones.id). Unblocked after this spec update (PM05 00b-05).*

---

**Running game state — derivation architecture:** All logical game state in THE SIGNAL is physically represented on the table. `component_positions` is therefore the universal state source — logical state is derived from component positions rather than stored in separate tracking tables.

*Derivation map below is unconfirmed — must be verified before PM05 DB-13 work begins.*

| State Dimension | Derivation from `component_positions` |
|-----------------|--------------------------------------|
| Faction resource counts | COUNT resource tokens by faction reserve zone |
| Influence level per faction per district | COUNT presence chips by district zone + faction |
| Public Standing per faction | Position of PS marker on Public Standing track |
| Portrait score per faction | Position of Portrait marker on Portrait track |
| Tension level | COUNT tension markers in play |
| Current Quarter / Phase | Position of Quarter marker on Session Timeline + `beat` table |
| Active Accords | Accord Document components whose zone = Accord Placement Area |
| Initiative pattern for current quarter | Position of initiative markers on Initiative Strip |

---
