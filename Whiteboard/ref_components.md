# Reference — Component Registry (00b)
*Load when: component registration questions, lifecycle rules, DB schema, visibility classifications.*

---

## Purpose of 00b

Schema index for the entire game system. Registers every named entity, assigns ID namespaces, defines cross-artifact lookup tables, maps FK relationships. Long-term role: DDL layer the Tier 2+ code engine reads first. All data tables must satisfy the L108 Data Table Standard (single-typed cells, enum vocabulary, explicit PKs, ID-based cross-refs, explicit nulls).

---

## Additional Registered Components (beyond design_reference.md list)

| ID Prefix | Entity | Physical Form | Notes |
|-----------|--------|---------------|-------|
| CA-xx | Dispatch Case | Physical container | Submitted at Phase 3 close; holds op cards, target slips, resource tokens. Transient — reset at Beat 5 Step 1. Schema pending. |
| NS-xx | Notification Slip | Pre-printed ARBITER slip | Fixed text: "A covert operation was conducted against your interests this round." Dropped into target faction's Dispatch Case on covert op fail conditions only. No faction identified; no op type disclosed. Schema pending. |
| O-xx | Operative | (not yet designed) | Faction operative records, tiers T1/T2/T3/Apex. Art 05 not yet designed. |
| EC-xx | Broadcast Card / Broadcast Effect Card | Dual-card | Broadcast Card (public, Situation Report Zone) + Broadcast Effect Card (ARBITER-only, Arbiter Tableau). DB: 25/86/87/98. |
| CC-xx | Countermeasure Card | (not yet designed) | Type A and Type B. Not yet designed. |
| ER-xx | Emergency Response Card | (not yet designed) | Faction-specific. 5 cards. Not yet designed. |

*IS-xx (IntelDeliverySlip) and VS-xx (visibility classification) also registered here as authoritative source.*

---

## Component Lifecycle Rules

- Dispatch Cases (CA-xx): transient — reset at Beat 5 Step 1; one per Faction Player per Quarter.
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

- CA-xx, NS-xx, IS-xx schemas: pending
- O-xx, CC-xx, ER-xx: not yet designed (blocked on source artifact)
- EC-xx: Broadcast Card / Broadcast Effect Card — registered (DB: 25/86/87/98)
