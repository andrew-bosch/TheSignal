# 00b — Analysis Readiness
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.3
**Status:** ✅ Signed Off — S45 (restructured S83)

**Purpose:** The game system needs to be fully modeled in the DB to enable deep analysis and computational balance work. This document tracks what remains to be migrated. `Database/schema_reference.md` is the authoritative source for migrated entities. This document provides: (1) a pointer to the L108 standard (§3); (2) lookup tables for entities not yet in the DB (§4); (3) the migration punchlist (§5).

**Relationship to source artifacts:** Source artifacts remain the canonical design documents. Game-purpose definitions live in source artifacts; this document tracks migration status only.

**Depends on:** 00 — Factions, World & Narrative Context; 00a — Governing Rules & Design Policy

---

## 2. Index

1. [Overview](#1--data-architecture)
2. [Index](#2-index)
3. [L108 Data Table Standard](#3-l108-data-table-standard-extends-3nf)
4. [Lookup Tables Pending Migration](#4-lookup-tables-pending-migration)
5. [Migration Punchlist](#5-migration-punchlist)
6. [Entity Relationships](#6-entity-relationships)
7. [Design Notes](#7-design-notes)

---

## 3. L108 Data Table Standard

See **00a §11** for the full L108 standard and column type vocabulary. Compliance status tracked in §5 Migration Punchlist.

---

## 4. Lookup Tables Pending Migration

### 4.1 Difficulty Tier (DT-xx)

| ID | Name | Base Threshold | Notes |
|----|------|----------------|-------|
| DT-01 | Easy | 75 | 75% base probability of success |
| DT-02 | Average | 50 | 50% base probability of success |
| DT-03 | Challenging | 25 | 25% base probability of success |

*Automatic and Impossible are not base difficulty values (L101). They may appear as explicit card text only.*

*Source: Art 03 §13. Foreign key: C-xx.Difficulty → DT-xx.ID; P-xx.Difficulty → DT-xx.ID*

---

### 4.2 Resolution Outcome (RO-xx)

| ID | Name | Trigger |
|----|------|---------|
| RO-01 | Succeeded | Roll ≤ threshold; success conditions apply |
| RO-02 | Failed | Roll > threshold; failure conditions apply |
| RO-03 | Voided | Operation removed in Beat 1 or Beat 2 before resolution — targeting restriction or Type A Countermeasure |
| RO-04 | Discovered | Roll outcome triggers discovery condition on card |
| RO-05 | Auto-failed | Face-down card — no roll made; zero or shortfall payment |

*Source: Art 03 §12 Beats 1–4. Foreign key: C-xx references RO-xx in card failure/discovery fields.*

**4.2.a Crit Flag**

Critical rolls set a `crit: true` modifier alongside the base RO-xx outcome — crit is not a standalone outcome type. Critical Success (01–05): RO-01 + crit flag — success effects and crit delta both execute. Critical Fail (96–00): RO-02 + crit flag — fail effects and crit delta both execute. (L202)

---

### 4.3 Influence Level (IL-xx)

| ID | Name | Chip Threshold | Notes |
|----|------|----------------|-------|
| IL-01 | Dominant | 3+ chips, strictly more than all others | Max 1 faction per district |
| IL-02 | Established | 2+ chips AND second-highest count | — |
| IL-03 | Present | 1+ chip | Minimum meaningful presence |
| IL-05 | None | 0 chips | No presence |

*Source: Art 02a §6. Chorus Node exception: Dominant structurally unreachable due to ARBITER Dominance Marker (02a §10).*

**4.3.a Contested Flag**

Contested is a board-state flag, not an influence level. Set when two or more factions are tied for the highest chip count and are both temporarily set to IL-01. `contested: true` is applied to the affected district alongside those factions' IL-01 values. Condition cannot persist beyond Month 3 resolution. (L203)

---

### 4.4 Public Standing Tier (PS-xx)

*⭐ Ready to model in DB.*

| ID | Name | Track Range | Modifier ID | Drift Rule |
|----|------|-------------|-------------|------------|
| PS-01 | Celebrated | 17–20 | M-01 | Natural drift: −1 per Quarter above 13 (L13) |
| PS-02 | Respected | 13–16 | M-02 | Natural drift: −1 per Quarter above 13 (L13) |
| PS-03 | Neutral | 7–12 | M-03 | No natural drift |
| PS-04 | Suspect | 3–6 | M-04 | Natural drift: +1 per Quarter below 7 (L13) |
| PS-05 | Discredited | 0–2 | M-05 | Natural drift: +1 per Quarter below 7 (L13) |

*Source: Art 02b §7. Starting position: 10 / Neutral (L48). Foreign key: PS-xx.ModifierID → M-xx.ID*

---

### 4.5 Portrait Band (PB-xx)

*Band labels canonical (proposed) per Art 02 §12. Score ranges TBD pending Art 07 Portrait design (PM05 07-13). Art 02 §12 is authoritative once Art 07 design is complete.*

| ID | Name | Score Range | Notes |
|----|------|-------------|-------|
| PB-01 | Resonant | +18 to +20 | L42 — compressed to width 3 to preserve ±20 track limits |
| PB-02 | Aligned | TBD — Art 07 | — |
| PB-03 | Coherent | TBD — Art 07 | — |
| PB-04 | Legible | TBD — Art 07 | — |
| PB-05 | Observed | TBD — Art 07 | — |
| PB-06 | Ambiguous | −1 to 0 | L42 — zero line band |
| PB-07 | Uncertain | TBD — Art 07 | — |
| PB-08 | Dissonant | TBD — Art 07 | — |
| PB-09 | Fractured | TBD — Art 07 | — |
| PB-10 | Collapsed | TBD — Art 07 | — |
| PB-11 | Void | TBD — Art 07 | Lowest — furthest from Chorus alignment |

*Source: Art 02 §12. Foreign key: Faction Portrait score maps to PB-xx at session end for VP calculation.*

---

## 5. Migration Punchlist

| Entity | ID Prefix | Status | Notes |
|--------|-----------|--------|-------|
| Public Standing Tier | PS-xx | ⭐ Ready to model | §4.4 |
| Difficulty Tier | DT-xx | 🔄 Pending migration | §4.1 |
| Resolution Outcome | RO-xx | 🔄 Pending migration | §4.2 |
| Influence Level | IL-xx | 🔄 Pending migration | §4.3 |
| Portrait Band | PB-xx | 🔄 Pending migration | 11 bands in §4.5; ranges TBD pending Art 07 Portrait design (PM05 07-13) |
| Visibility Marker | VM-xx | 🔄 Pending migration | S81 registration |
| BoostMarker | BM-xx | 🔄 Pending migration | S79 draft |
| Notification Slip | NS-xx | 🔄 Pending schema | Text/format: Art 07 |
| Intel Delivery Slip | IS-xx | 🔄 Pending schema | Content fields: Art 07 |
| Case (Dispatch Case) | CA-xx | 🔄 Verify in DB | May be covered by game_zones |
| Operative | O-xx | ⬜ Pending design | Art 05 not started |
| Initiative Pattern | IP-xx | ⬜ Pending design | Procedure in Art 07 |
| Modifier Card | MC-xx | ⬜ Pending design | D04-08 / D04-07 |
| Event Card | EC-xx | ⬜ Pending design | Art 07 / Art 09 |
| Countermeasure Card | CC-xx | ⬜ Pending design | Art 04 / Art 09 |
| Emergency Response | ER-xx | ⬜ Pending design | Art 04 / Art 05 |

---

## 6. Entity Relationships

See `Database/schema_reference.md §2.5` for the full entity relationship map and FK semantics.

---

## 7. Design Notes

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
