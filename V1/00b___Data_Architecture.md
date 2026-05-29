# 00b — Data Architecture
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.2
**Status:** ✅ Signed Off — S45

**Purpose:** This document is the schema index for THE SIGNAL data architecture. It defines every named entity in the game system, assigns ID namespaces, maintains all lookup/enum tables, and maps relationships between entities. It is the primary reference for L108 compliance — all data tables across all design artifacts are registered here.

**Relationship to source artifacts:** Source artifacts remain the canonical design documents. This artifact does not duplicate their content — it indexes it. When a source artifact defines a data table (e.g., Art 03 §13 Modifier table), the table lives in the source artifact; 00b registers the entity, assigns the ID prefix, and maps its relationships.

**Future state:** At Tier 2+ code engine development, this document becomes the master database design document — the DDL (data definition layer) that the game engine reads first. The paper prototype data structures are designed to be ingested directly, without structural transformation (L108).

**Depends on:** 00 — Factions, World & Narrative Context; 00a — Governing Rules & Design Policy; all design artifacts (as schemas are defined)

---

## 2. Index

1. Overview (§1 above)
2. [Index](#2-index)
3. [L108 Data Table Standard](#3-l108-data-table-standard-extends-1nf)
4. [Entity Registry](#4-entity-registry)
5. [Lookup Tables](#5-lookup-tables)
6. [Entity Relationship Map](#6-entity-relationship-map)
7. [Schema Reference Index](#7-schema-reference-index)
8. [Design Notes & Known Gaps](#8-design-notes--known-gaps)

---

## 3. L108 Data Table Standard (extends 1NF)

All data tables in THE SIGNAL artifact suite must satisfy the following five requirements (L108 — Database Translatable Data Design). Requirements 1 and 3 correspond to standard First Normal Form (1NF); Requirements 2, 4, and 5 are project-specific extensions.

| # | Requirement | Test |
|---|-------------|------|
| 1 | Each column carries a single typed value — no compound cells | No cell contains "A / B" or mixed types |
| 2 | Values from controlled vocabulary (enum) where possible | Column values are drawn from a defined set, not freeform prose |
| 3 | Every table has an explicit primary key (ID column) | First column is always a unique ID |
| 4 | Cross-references use ID-based keys, not prose descriptions | Foreign references name an ID (e.g., F-01), not a label (e.g., "Ghost") |
| 5 | Null / N/A is explicit, never absent | Empty cells use N/A; omission is not a valid null |

*These requirements apply to all data tables in all V1 artifacts, retroactively. Compliance status is tracked in §7 Schema Reference Index below.*

**Column type vocabulary (L123):** All schema documents in the artifact suite must declare column types using the canonical type vocabulary: **String** (short text), **Semver** (version identifier), **Integer** (non-negative count), **Enum** (controlled vocabulary), **Prose** (long-form text), **±Integer** (signed integer), **ID Reference** (foreign key to an entity ID namespace — governed by Req 4; the type name formalizes the implicit requirement). New types require a locked decision to extend the vocabulary. Source: L121 (Art 04 §6 first application), L123 (promoted to suite-wide standard).

---

## 4. Entity Registry

Every named entity type in the game system. ID prefixes establish the primary key namespace for each entity. IDs are zero-padded two-digit integers (e.g., F-01, D-22).

| ID Prefix | Entity | Description | Source Artifact | L108 Status |
|-----------|--------|-------------|----------------|-------------|
| F-xx | Faction | The six parties at The Table (five playing factions + ARBITER) | Art 00 §7 | ⬜ Schema pending |
| D-xx | District | The 22 districts of New Meridian (D-01–D-21 named districts + D-22 Chorus Node) | Art 01 §7 | ⬜ Schema pending — adjacency table queued (D04-09) |
| RG-xx | Ring | The four geographic rings (Baryo / The Mid / Core / Chorus Node) | Art 01 §6, Art 02a | ⬜ Schema pending |
| RT-xx | Resource Type | The six resource types (five faction-native + Resolution) | Art 00 §7, Art 02a | ⬜ Schema pending |
| IL-xx | Influence Level | The presence states at a district (Dominant / Established / Present / Contested / None) | Art 02a §6 | ⬜ Schema pending |
| PS-xx | Public Standing Tier | The five named positions on the Public Standing track | Art 02b §7 | ⬜ Schema pending |
| PB-xx | Portrait Band | The five Chorus Portrait evaluation bands | Art 02b §6 | ⬜ Schema pending |
| DT-xx | Difficulty Tier | The three base difficulty levels (Easy / Average / Challenging) | Art 03 §13 | ⬜ Schema pending |
| M-xx | Modifier | Threshold modifiers applied during resolution (M-01–M-12) | Art 03 §13 | ✅ Complete — see Art 03 §13 |
| RO-xx | Resolution Outcome | The outcome states for a resolved action | Art 03 §12 | ⬜ Schema pending |
| IP-xx | Initiative Pattern | The ten D10 initiative order patterns | Art 07 | ⬜ Schema pending — Art 07 draft required |
| C-xx | Action Card — Covert Operation | Covert operation cards C-01–C-35 | Art 04 §6 | 🔄 Schema exists; L108 audit pending (XA-28) |
| P-xx | Action Card — Political Act | Political act cards P-01–P-18 | Art 04 §6 | 🔄 Schema exists; L108 audit pending (XA-28) |
| O-xx | Operative | Faction operative records (tiers T1/T2/T3/Apex) | Art 05 | ⬜ Art 05 not yet designed |
| EC-xx | Event Card / Situation Report | Dual-card Situation Report records (Broadcast Card + Event Card) | Art 07, Art 09 | ⬜ Not yet designed |
| MC-xx | Modifier Card | Faction and ring modifier card records | Art 09 | ⬜ Not yet designed |
| CC-xx | Countermeasure Card | Type A and Type B countermeasure card records | Art 04, Art 09 | ⬜ Not yet designed |
| ER-xx | Emergency Response Card | Faction-specific Emergency Response cards | Art 04, Art 05 | ⬜ Not yet designed |
| CA-xx | Case (Dispatch Case) | Physical container submitted by each Faction Player at Phase 3 close. Contains operation cards, target slips, and resource tokens for that faction's covert submissions. In V1, indexed via Faction ID (F-xx) — `dispatch_case[F-xx]`. CA-xx prefix anticipates L2+ per-case record tracking. One per Faction Player per Quarter; transient (reset at Beat_5 Step 1). | Art 03 §7, Art 06, 03a §4 | ⬜ Schema pending |
| VS-xx | Visibility Scope | Information visibility classification — controls which parties can see a given field | 00b §5.9 (defined here) | ✅ Complete (§5.9) |
| NS-xx | Notification Slip | Pre-written ARBITER delivery slip placed in a targeted faction's dispatch case when a covert operation against them fails. Text and format defined in Art 07. | Art 04, Art 07 | ⬜ Schema pending |
| IS-xx | Intel Delivery Slip | Blank slip on ARBITER's tableau. At Beat 3, ARBITER writes the collected intelligence onto the slip and places it in the acting faction's dispatch case. Content determined by the resolving card's success outcome. | Art 04, Art 07 | ⬜ Schema pending |

*22 entity types. 9 fully L108-compliant. 3 with existing schemas pending further work (PB-xx: ranges pending; C-xx + P-xx: L108 audit pending XA-28). 10 schemas pending source artifact design. 1 cross-artifact standard defined here (VS-xx).*

*Internal 03a modeling types — not registered entities (no persistent IDs, no independent physical components):*
- *Packet — sub-structure within a Case (one operation card + submitted resources + target slip). Indexed by submission order within the Case. No CA-sub-ID scheme needed.*
- *GridCell — position reference in the Resolution Grid (Lane: F-xx, Queue index: integer). Identified by compound key; not a named game object.*

---

## 5. Lookup Tables

Small enum tables that span multiple artifacts and have no single canonical source artifact. These are defined here as the authoritative reference.

---

### 5.1 Difficulty Tier (DT-xx)

| ID | Name | Base Threshold | Notes |
|----|------|----------------|-------|
| DT-01 | Easy | 75 | 75% base probability of success |
| DT-02 | Average | 50 | 50% base probability of success |
| DT-03 | Challenging | 25 | 25% base probability of success |

*Automatic and Impossible are not base difficulty values (L101). They may appear as explicit card text only.*

*Source: Art 03 §13. Foreign key: C-xx.Difficulty → DT-xx.ID; P-xx.Difficulty → DT-xx.ID*

---

### 5.2 Resolution Outcome (RO-xx)

| ID | Name | Trigger | Physical Component |
|----|------|---------|-------------------|
| RO-01 | Succeeded | Roll ≤ threshold; or Critical Success (01–05) | Operation Resolution card: Succeeded |
| RO-02 | Failed | Roll > threshold; failure conditions apply | Operation Resolution card: Failed |
| RO-03 | Voided | Operation removed in Beat 1 or Beat 2 before resolution — targeting restriction or Type A Countermeasure | Operation Resolution card: Voided |
| RO-04 | Discovered | Roll outcome triggers discovery condition on card | Operation Resolution card: Discovered |
| RO-05 | Auto-failed | Face-down card — no roll made; zero or shortfall payment | No resolution card — action card returned |

*Source: Art 03 §12 Beats 1–4. Foreign key: C-xx references RO-xx in card failure/discovery fields.*

---

### 5.3 Ring (RG-xx)

| ID | Name | Entry Requirement | Threshold Modifier | Notes |
|----|------|------------------|-------------------|-------|
| RG-01 | Baryo | None | None | — |
| RG-02 | The Mid | None | −25 (M-12) if no adjacent Core at Established or Dominant | Modifier M-12 |
| RG-03 | Core | Established or Dominant in adjacent The Mid district | None | — |
| RG-04 | Chorus Node | Established or Dominant in adjacent Core district | See Art 02a §10 | Special rules apply |

*Source: Art 03 §8 Phase 2 Placement, Art 02a §10. Foreign key: D-xx.Ring → RG-xx.ID*

---

### 5.4 Resource Type (RT-xx)

| ID | Name | Faction | Notes |
|----|------|---------|-------|
| RT-01 | Findings | F-01 (Ghost) | Ghost native resource |
| RT-02 | Exposure | F-02 (The Network) | Network native resource |
| RT-03 | Capital | F-03 (The Syndicate) | Syndicate native resource |
| RT-04 | Capacity | F-04 (The Guild) | Guild native resource |
| RT-05 | Mandate | F-05 (The Directorate) | Directorate native resource |
| RT-06 | Resolution | F-06 (ARBITER) | ARBITER resource — Chorus Node only; full design pending D07-01 |

*Source: Art 00 §7, Art 02a §5. Foreign key: D-xx.NativeResource → RT-xx.ID; F-xx.NativeResource → RT-xx.ID*

---

### 5.5 Influence Level (IL-xx)

| ID | Name | Type | Chip Threshold | Notes |
|----|------|------|----------------|-------|
| IL-01 | Dominant | Level | 3+ chips, strictly more than all others | Max 1 faction per district |
| IL-02 | Established | Level | 2+ chips AND second-highest count | — |
| IL-03 | Present | Level | 1+ chip | Minimum meaningful presence |
| IL-04 | Contested | Condition | N/A — applied when Dominant is disputed | Not a presence level; a board state condition |
| IL-05 | None | Level | 0 chips | No presence |

*Source: Art 02a §6. Chorus Node exception: Dominant structurally unreachable due to ARBITER Dominance Marker (02a §10).*

---

### 5.6 Public Standing Tier (PS-xx)

| ID | Name | Track Range | Modifier ID | Drift Rule |
|----|------|-------------|-------------|------------|
| PS-01 | Celebrated | 17–20 | M-01 | Natural drift: −1 per Quarter above 13 (L13) |
| PS-02 | Respected | 13–16 | M-02 | Natural drift: −1 per Quarter above 13 (L13) |
| PS-03 | Neutral | 7–12 | M-03 | No natural drift |
| PS-04 | Suspect | 3–6 | M-04 | Natural drift: +1 per Quarter below 7 (L13) |
| PS-05 | Discredited | 0–2 | M-05 | Natural drift: +1 per Quarter below 7 (L13) |

*Source: Art 02b §7. Starting position: 10 / Neutral (L48). Foreign key: PS-xx.ModifierID → M-xx.ID*

---

### 5.7 Portrait Band (PB-xx)

*Score ranges are defined in Art 02b §6. Exact ranges to be confirmed during Art 02b re-sign-off. Band names and ordering are locked.*

| ID | Name | Score Range | Notes |
|----|------|-------------|-------|
| PB-01 | Resonant | +18 to +20 | L42 — compressed to width 3 to preserve ±20 track limits |
| PB-02 | Aligned | See Art 02b §6 | — |
| PB-03 | Ambiguous | −1 to 0 | L42 — zero line band |
| PB-04 | Divergent | See Art 02b §6 | — |
| PB-05 | Dissonant | See Art 02b §6 | Lowest — furthest from Chorus alignment |

*Source: Art 02b §6. Foreign key: Faction Portrait score maps to PB-xx at session end for VP calculation.*

---

### 5.8 Faction (F-xx)

| ID | Name | Native Resource | Color | Type |
|----|------|----------------|-------|------|
| F-01 | Ghost | RT-01 (Findings) | Charcoal green | Playing faction |
| F-02 | The Network | RT-02 (Exposure) | Bright signal green | Playing faction |
| F-03 | The Syndicate | RT-03 (Capital) | Metallic gold | Playing faction |
| F-04 | The Guild | RT-04 (Capacity) | Industrial orange | Playing faction |
| F-05 | The Directorate | RT-05 (Mandate) | Deep institutional blue | Playing faction |
| F-06 | ARBITER | RT-06 (Resolution) | White (provisional) | Non-playing — constitutive presence |

*Source: Art 00 §7, Art 11 §6.*

---

### 5.9 Visibility Scope (VS-xx)

Information visibility classification. Used as a field tag on any data element in the game system to define which parties may observe it. Enforced by human ARBITER discipline in Tier 1; enforced by server-side API scoping in Tier 2+.

| ID | Scope | Visible To | V1 Usage |
|----|-------|-----------|---------|
| VS-01 | Public | All players, spectators, public display | Active — default for board state (token counts, Public Standing, declaration outcomes) |
| VS-02 | Faction-Only | All players of that faction | Active — exact resource amounts, internal faction decisions |
| VS-03 | Bilateral | Two specific parties + ARBITER | Active — Accord terms, direct Dispatch Case messages |
| VS-04 | ARBITER-Only | ARBITER only; never surfaced directly | Active — Chorus Portrait scores, operation failure outcomes, loyalty tracking |
| VS-05 | Player-Only | Single player within a multi-player faction | Active — individual operative assignments when factions field multiple players |
| VS-06 | Conditional | After a specific reveal mechanism triggers | Active — e.g., hidden operation card revealed upon resolution; card effect on activation |
| VS-07 | Website-Public | Any authenticated player via website | Tier 2+ — Chronicles, Founding Figures, historical session records |
| VS-08 | Website-Private | Authenticated player only; personal records | Tier 2+ — personal ARBITER messages, private faction records |

*Design principle: default is private. If a field is not explicitly tagged VS-01 (Public), it is restricted. This principle governs all entity field definitions at Tier 2+. In Tier 1, ARBITER is the enforcement layer. Source: Retired/Electronic/old__10_INFORMATION_HIERARCHY.md (visibility design principles). Foreign key: any entity field may reference VS-xx.ID to declare its visibility scope.*

---

## 6. Entity Relationship Map

Key foreign key relationships between entities. Read as: **Entity.Field → Entity.ID**.

```
F-xx.NativeResource    → RT-xx.ID
D-xx.Ring              → RG-xx.ID
D-xx.NativeResource    → RT-xx.ID
D-xx.AdjacentDistricts → D-xx.ID  (self-referencing — adjacency list)
C-xx.Faction           → F-xx.ID
C-xx.Difficulty        → DT-xx.ID
C-xx.Modifier          → M-xx.ID  (modifiers applied by this card)
C-xx.Target            → D-xx.ID | RG-xx.ID | F-xx.ID
P-xx.Faction           → F-xx.ID
P-xx.Difficulty        → DT-xx.ID
P-xx.Modifier          → M-xx.ID
O-xx.Faction           → F-xx.ID
M-xx.Scope             → [Covert | Political | All]  (enum)
M-xx.Applied           → [Beat 0 | Beat 1 | Beat 2 | Beat 4 | Persistent | Pre-Resolution]
PS-xx.ModifierID       → M-xx.ID
EC-xx.PublicStanding   → F-xx.ID  (which factions are affected)
EC-xx.TargetRestriction → D-xx.ID | RG-xx.ID
Action resolution      → RO-xx.ID
[any entity field]     → VS-xx.ID  (visibility scope declaration — applies to any field in any entity)
```

*Adjacency list (D-xx.AdjacentDistricts → D-xx.ID) is the self-referencing relationship required by cards C-02, C-04, C-05, C-14, C-29, C-30. Full adjacency table pending D04-09.*

---

## 7. Schema Reference Index

Status of every entity schema against L108 requirements. Updated as source artifacts are designed and audited.

| Entity | ID Prefix | Row Count | L108 Status | Blocker |
|--------|-----------|-----------|-------------|---------|
| Modifier | M-xx | 12 | ✅ Complete | — |
| Difficulty Tier | DT-xx | 3 | ✅ Complete (§5.1) | — |
| Resolution Outcome | RO-xx | 5 | ✅ Complete (§5.2) | — |
| Ring | RG-xx | 4 | ✅ Complete (§5.3) | — |
| Resource Type | RT-xx | 6 | ✅ Complete (§5.4) | — |
| Influence Level | IL-xx | 5 | ✅ Complete (§5.5) | — |
| Public Standing Tier | PS-xx | 5 | ✅ Complete (§5.6) | — |
| Portrait Band | PB-xx | 5 | 🔄 Names locked; ranges pending | Art 02b re-sign-off |
| Faction | F-xx | 6 | ✅ Complete (§5.8) | — |
| Action Card — Covert | C-xx | 35 | 🔄 Schema exists in Art 04 §6; L108 audit pending | XA-28 |
| Action Card — Political | P-xx | 18 | 🔄 Schema exists in Art 04 §6; L108 audit pending | XA-28 |
| District | D-xx | 22 | ⬜ Schema not yet defined | D04-09 (adjacency) |
| Initiative Pattern | IP-xx | 10 | ⬜ Schema pending — procedure migrated to Art 07 | Art 07 draft |
| Operative | O-xx | TBD | ⬜ Art 05 not yet designed | Art 05 |
| Event Card | EC-xx | TBD | ⬜ Not yet designed | Art 07 / Art 09 |
| Modifier Card | MC-xx | TBD | ⬜ Not yet designed | Art 09 |
| Countermeasure Card | CC-xx | TBD | ⬜ Not yet designed | Art 04 / Art 09 |
| Emergency Response | ER-xx | 5 | ⬜ Not yet designed | Art 04 / Art 05 |
| Case (Dispatch Case) | CA-xx | 5 (1 per Faction Player per Quarter; transient) | ⬜ Schema pending | Art 03 §7, Art 06 |
| Visibility Scope | VS-xx | 8 | ✅ Complete (§5.9) | — |
| Notification Slip | NS-xx | TBD | ⬜ Schema pending — text/format: Art 07 | Art 04, Art 07 |
| Intel Delivery Slip | IS-xx | TBD | ⬜ Schema pending — content fields: Art 07 | Art 04, Art 07 |

*9 of 22 entity schemas fully L108-compliant. 3 with schemas in progress. 10 pending source artifact design.*

---

## 8. Design Notes & Known Gaps

**District adjacency (D04-09):** The District entity requires a self-referencing adjacency list — a separate junction table mapping D-xx to adjacent D-xx values. This is the most complex relationship in the entity model. Cannot be completed until Art 01 adjacency table is designed and the full card set is locked (cards reference adjacency).

**Initiative Pattern (IP-xx):** Initiative procedure migrated to Art 07 (PM05 03-11). Schema to be defined there — ID column (IP-01 through IP-10) and full table structure pending Art 07 draft.

**Portrait Band score ranges (PB-xx):** PB-01 (Resonant: +18–+20) and PB-03 (Ambiguous: −1–0) are confirmed by L42. PB-02, PB-04, PB-05 ranges are defined in Art 02b §6 but not reproduced here pending verification during Art 02b re-sign-off.

**Modifier Card schema (MC-xx):** Will require at minimum: ID, Faction (F-xx | All), Ring (RG-xx | N/A), Value Rating (1–3 per L67), Targeting Constraint (ring-native per L66), Threshold Adjustment. Full design pending D04-08 (modifier card content) and D04-07 (in-world name).

**Event Card schema (EC-xx):** Dual-card system (Broadcast Card public + Event Card ARBITER-only). Schema will need: ID, Public Narrative, Difficulty Modifier (M-xx | N/A), Targeting Restriction (D-xx | RG-xx | N/A), Conversion Block (D-xx | RG-xx | N/A), Public Standing Effect (faction + delta), Duration (quarters). Full design pending Art 07 and Art 09.

**Faction perspectives field — known L108 Requirement 1 exception (deliberate, revisable):** The "Faction perspectives" field in Art 04 §6 is typed as String but contains five per-faction sub-values (one sentence per faction). This is structurally a compound cell (L108 Req 1 violation). Documented as a deliberate exception rather than deferred: the field is narrative design reference with no resolution consequence and no structural inconsistency between sub-values (all homogeneous Strings). No individual faction value is queried at resolution. If a future use case requires querying individual faction perspectives (e.g., cross-card analysis by faction voice), decompose into five faction-keyed fields (Faction perspectives — Ghost / Network / Syndicate / Guild / Directorate), analogous to Portrait decomposition (L119). That decision is post-design and does not block current card passes. See PM05 04-18.

**Compound effect text — known L108 Requirement 1 violation (deferred):** The Effect on success/failure/crit fields in Art 04 §6 carry multi-effect prose strings that violate L108 Requirement 1 (no compound cells). Example: C01's Effect on success encodes two distinct effects in one string — an immediate board placement and a persistent upkeep generator. These cannot be individually queried or programmatically enforced. The taxonomy triple (Category/Function/Target) is the correct decomposition model; the gap is that effect values (quantity, target ID, condition, duration) are not decomposed as typed sub-fields. Deferral rationale: decomposing effect fields requires card content to be locked first — restructuring before lock wastes effort. Action when ready: extend the taxonomy triple to carry effect quantity, target ID, and condition as typed sub-fields per card. See PM05 XA-30.

**`component_positions` table (component location registry):** Tracks the real-time physical location of every in-play component. One row per active component. `component_positions` is an operational DB table — not a named game entity — and is not registered in §4. Formerly `live_state` (renamed DB-11).

| Column | Type | Null | FK Target | Purpose |
|--------|------|------|-----------|---------|
| `component_id` | bigint | NOT NULL (PK) | components.id | The tracked component |
| `current_zone_id` | bigint | NOT NULL | game_zones.id | Primary zone the component currently occupies |
| `on_component_id` | bigint | NULL | components.id | Parent component this physically rests on. NULL when the component sits directly in a zone rather than on another component (e.g., The Overview mat: `on_component_id` = NULL, `on_game_zone_id` = Table Center). Renamed from `anchored_to_component_id`; constraint changed NOT NULL → NULL. |
| `on_game_zone_id` | bigint | NULL | game_zones.id | Specific zone this component occupies within the physical layout; used when `on_component_id` is NULL. Expresses sub-zone context beyond `current_zone_id`. |

*L156 (S40). Locked: option B — component_positions carries both nullable FK columns rather than dual-representing container components as zones. Pending: agy DB-11 — RENAME TABLE `live_state` → `component_positions`; RENAME COLUMN `anchored_to_component_id` → `on_component_id` (change NOT NULL → NULL); ADD COLUMN `on_game_zone_id` (bigint, NULL, FK → game_zones.id). Unblocked after this spec update (PM05 00b-05).*

---

**Running game state — derivation architecture:** All logical game state in THE SIGNAL is physically represented on the table. `component_positions` is therefore the universal state source — logical state is derived from component positions rather than stored in separate tracking tables. Derivation map:

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

*Derivation queries to be documented in PM05 DB-13 once component registry and game_zones are fully seeded.*

---

**Code engine note:** When the Tier 2+ game engine is built, this document is read first. The entity registry (§4) provides the entity list and ID namespaces. The lookup tables (§5) are ingested as reference data. The relationship map (§6) defines the joins. Source artifacts provide the full field definitions for each entity.

**L2 TypeScript schema (reference):** A complete TypeScript game state schema (v0.2) exists in `Retired/Electronic/old__08_DATA_MODEL.md`. It defines the full entity model for the electronic version, including enumerations (ResourceType, PopularityState, CardType, DistrictType, LoyaltyLevel, UnlockTier, VisibilityScope, Layer, ActionType, StateChangeType), complete interfaces for all game objects, an event-sourcing architecture (every state change is an event appended to an event log), and a visibility-scoped API contract. V1 entities in this document are designed as conceptual subsets of that schema's types. When defining new V1 entities, check old__08 for corresponding TypeScript types — alignment avoids structural transformation at L2 ingestion. The VS-xx Visibility Scope table (§5.9) is drawn directly from that schema.

**Information hierarchy reference (Tier 2+):** A complete 12-category information visibility specification exists in `Retired/Electronic/old__10_INFORMATION_HIERARCHY.md`. It defines visibility rules for all game state — Player Identity, Faction State, Operative/Unlock, Board/District, Asset, Card, Action, Alliance/Accord, World Condition, ARBITER Internal, Table Question, and Legacy. This is the Tier 2 server-side enforcement specification. In Tier 1, these rules are enforced by ARBITER discipline. VS-xx (§5.9) provides the vocabulary; old__10 provides the application.

---

*00b v0.1 — established session 20. Schema index only; source artifacts remain canonical for all field definitions.*
