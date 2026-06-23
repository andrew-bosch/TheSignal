# Reference — Component Registry (00b)
*Load when: component registration questions, lifecycle rules, DB schema, visibility classifications.*

---

## Purpose of 00b

Schema index for the entire game system. Registers every named entity, assigns ID namespaces, defines cross-artifact lookup tables, maps FK relationships. Long-term role: DDL layer the Tier 2+ code engine reads first. All data tables must satisfy the L108 Data Table Standard (single-typed cells, enum vocabulary, explicit PKs, ID-based cross-refs, explicit nulls).

---

## Additional Registered Components (beyond design_reference.md list)

| ID Prefix | Entity | Physical Form | Notes |
|-----------|--------|---------------|-------|
| CA-xx | Dispatch Case | Physical container | Holds op cards, Target Profile (DB:48), resource tokens (DB:8, DB:12), Intel tokens (DB:9) submitted at §9.1. One per Faction Player — same physical object resets each month at Beat 0 (ARBITER opens and processes contents). |
| NS-xx | Notification Slip | Pre-printed ARBITER slip | Fixed text: "A covert operation was conducted against your interests this round." Delivered to target faction when they are targeted by a covert op — not conditional on the op failing. No faction identified; no op type disclosed. Full schema in Art 02. |
| O-xx | Operative | Not yet designed | Faction operative records, tiers T1/T2/T3/Apex. Art 05 not yet designed. |
| EC-xx | Broadcast Card / Broadcast Effect Card | Dual-card | Broadcast Card (DB:25) public, Situation Report Zone; Broadcast Effect Card (DB:98) ARBITER-only, Arbiter Tableau. Linked at §7.2.1. Full schema in Art 02. DB: 25/86/87/98. |
| CC-xx | Countermeasure Card (DB:52) | Card | Fully signed off (Art 02). CM-A: blocks all covert operations targeting keyed faction; CM-B: adds modifier to targeted op. 15 total; submitted at §9.3. Full schema in Art 02. |
| ER-xx | Emergency Response Card (DB:97) | Card | Fully signed off (Art 02). Faction-specific. Full schema in Art 02. |

*IS-xx (IntelDeliverySlip) registered here as authoritative source.*

---

## Component Lifecycle Rules

- Dispatch Cases (CA-xx): one per Faction Player; same physical object resets at Beat 0 each month when ARBITER opens and processes contents.
- IS-xx slips: written by ARBITER per-incident at resolution time (not pre-printed); delivered at Beat 2 or Beat 3 per card procedure.
- All physical state is considered resident in `component_positions` — no separate tracking tables store derived state.

---

## `component_positions` Table (§8)

Operational DB table tracking real-time physical location of every in-play component. Renamed from `live_state` — DB-11 complete (S46).

| Column | Type | Null | Purpose |
|--------|------|------|---------|
| `component_id` | bigint | NOT NULL (PK) | FK → components.id |
| `current_zone_id` | bigint | NOT NULL | Primary zone component occupies; FK → game_zones.id |
| `on_component_id` | bigint | NULL | Parent component this rests on (NULL = sits directly in a zone) |
| `on_game_zone_id` | bigint | NULL | Sub-zone context within physical layout |

**Design principle (L156):** All logical game state is derived from component positions. Resource counts, influence levels, PS, Portrait score, Quarter/Phase, active Accords, initiative — all derived by querying `component_positions`, not stored separately.

---

## Pending / Stub Flags

- CA-xx, NS-xx, IS-xx: schemas fully in Art 02; ref entries are abbreviated — query Art 02 or DB for full field detail
- O-xx: not yet designed (Art 05 not yet scoped)
- CC-xx (DB:52), ER-xx (DB:97): fully signed off in Art 02
- EC-xx: Broadcast Card / Broadcast Effect Card — registered (DB: 25/86/87/98)
