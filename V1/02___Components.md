# 02 — Components
## THE SIGNAL P1 — Paper Prototype

**Version:** 2.2
**Status:** ✅ Signed Off — S98 (L213)
**Depends on:** 00 — Factions, World & Narrative Context; 01 — Game Board: New Meridian
**DB Anchor:** `the_signal_db.component` — canonical component registry. Names and IDs from that registry are authoritative.
**DB Sync:** Changes to component schema design or any component entry fields must be coordinated with corresponding DB updates. Art 02 and `the_signal_db` must remain in sync.
**Feeds:** 03-init (starting positions); 03 (procedures)

---

## 1. Overview

This document enumerates every physical component in The Signal — its gameplay design function, physical requirements, and gameplay requirements. The `component` table in `the_signal_db` is the canonical completeness anchor.

---

## 2. Index

| Section | Content |
|---------|---------|
| [§3 Design Principles](#3-design-principles) | Meta-design principles and entry rubric |
| [§4 Grouping Taxonomy and Component Schema](#4-grouping-taxonomy-and-component-schema) | Section grouping rationale and entry field definitions |
| [§5 Playing Surface](#5-playing-surface) | Shared board surfaces, player stations, screens, grids |
| [§6 Faction Influence](#6-faction-influence) | Presence chips, deployment markers, influence markers, structures |
| [§7 Resources](#7-resources) | Native resources, Reservoir, Backlog, Dispatch tokens |
| [§8 Covert Messaging System](#8-covert-messaging-system) | Dispatch case, Target Profile, delivery slips, Debrief cards |
| [§9 Intel & Information](#9-intel-information) | Intel tokens, Accord agreements |
| [§10 Card Systems](#10-card-systems) | All card types organized by system (6 subgroups) |
| [§11 Resolution Tools](#11-resolution-tools) | Threshold sliders, visibility/boost markers, modifier tokens |
| [§12 Tracking Systems](#12-tracking-systems) | Score, Initiative, Round/Quarter trackers; Status marker |

---

## 3. Design Principles

**DB registry as completeness anchor.** Every entry corresponds to a component registered in `the_signal_db.component`. The registry defines what components exist; this document specifies what each requires.

**Per-component structure.** The standard artifact template sections — Game Purpose, Narrative Function, Rules & Constraints, Component Description, Special Conditions, Examples — are addressed per-component within §§5–12, not as standalone sections. Each entry is self-contained.

**Function over form.** Entries lead with Design Function before physical requirements. Physical requirements must be derivable from design function — this is the evaluation order.

**Scope discipline.** This document specifies what components are and what they need. How they are used → Art 03. Where they start → Art 03-init. Governing rules → Art 00a.

**Narrative as anchor, not canon.** Narrative Anchors are brief orienting frames. Art 00 is the source of all canonical narrative.

**Calculation over count.** Where a component quantity is derived from a game parameter (faction count, district count, per-unit design rule), the Quantity field expresses the calculation rather than a static number. Reserve literal counts only for design parameters not derivable from another parameter. This keeps physical component totals auditable against game parameter changes.

**Procedurally auditable structure.** Each component group defines a metadata schema specific to that group's design role. Every entry within a group must populate every field in that group's schema. The schema is the verification procedure — a reviewer can mechanically follow it to confirm an entry is complete and correct. This document is the source of truth for component metadata; downstream DB schemas (e.g., `component_metadata`) are derived from it, never the reverse.

**Verb coverage as design completeness test.** Populating `applicable_verbs` requires a true/false determination for each §4.2 verb against this component. Each answer — inclusion and exclusion — must be derivable from and justifiable by the component's Design Function, Gameplay Requirements, and other schema fields. If any verb cannot be clearly determined true or false from the existing design, that is a design gap, not a data entry problem. Physical possibility only — game legality is defined in Art 03 §22.

---

### Entry Rubric

| Check | Passes If |
|-------|-----------|
| **DB Registration** | Heading includes the component's `the_signal_db.component` ID |
| **Structural Consistency** | Prose block (Design Function → Narrative Anchor → Gameplay Requirements) followed by Metadata block (all fields per §4.1 group schema) |
| **Design Function** | States why the component exists and what game system it enables |
| **Narrative Anchor** | Provides brief fictional grounding; or explicitly states `N/A —` with justification per 00a §4.6 |
| **Gameplay Requirements** | Specifies text, markings, or form required; or explicitly states "None" |
| **Metadata — db_id / component_name** | Matches `component.id` and `component.name` in the DB |
| **Metadata — physical_form / quantity / visibility** | `quantity` labeled `(gameplay requirement)` or `(pre-production estimate)`; `visibility` from Enum(visibility) |
| **Metadata — group fields** | All group-specific fields populated per §4.1; no field left blank — `N/A` if not applicable |
| **Metadata — applicable_verbs** | Each listed verb can physically be applied to this component per §4.2 definitions; each verb holds across ALL states declared in the `states` field; if the physical design must be adjusted to support a verb in all states, the adjustment is noted in `physical_form`; no physically possible verb is omitted; `N/A` only if no §4.2 verb can physically be applied |
| **Scope Discipline** | Entry contains no procedural rules, starting positions, or governing rules |

---

## 4. Grouping Taxonomy and Component Schema

Components are organized by primary function within the game system. Where a component serves multiple systems, its primary group is determined by its design function.

### Component Groups

| Group | Primary Function | Subgroups |
|-------|-----------------|-----------|
| **Playing Surface** | Physical geography and player station surfaces — the board space, screens, grids, and terminals that constitute the game table | — |
| **Faction Influence** | Presence, control, and structural markers placed on the playing surface to record faction activity | — |
| **Resources** | Economy tokens representing extractable and convertible value | — |
| **Covert Messaging System** | Components comprising the covert dispatch channel (submission side) and ARBITER return channel | — |
| **Intel & Information** | Intelligence tokens, accords, and classified records held or exchanged by factions | — |
| **Card Systems** | All card types, organized by system | Covert Operations · Countermeasures · Political Acts · Broadcasts · Classified Directives · Modifier |
| **Resolution Tools** | Instruments used to measure, flag, and resolve actions (sliders, VM/BM cards, modifier tokens, status markers) | — |
| **Tracking Systems** | Markers and trackers recording game state across beats, rounds, and quarters | Score · Initiative · Round/Quarter |

### §4.1 — Universal Component Schema

#### Entry Structure

Each component entry in §§5–12 follows this structure. Prose sections serve the human reader; not DB-imported. The **Metadata** block is the canonical source for the `component_metadata` DB table. Every entry populates all fields listed in its group schema (§§5–12 group headers). Fields with no applicable value state `N/A` explicitly — never blank.

```
**Design Function:** [why the component exists; the game system it enables]

**Narrative Anchor:** [fictional grounding] — or — `N/A —` [justification per 00a §4.6]

**Gameplay Requirements:** [physical and functional constraints on the component]

**Metadata:**
| Field | Value |
|-------|-------|
| [fields per group schema] | |
```

---

#### Field Registry

Universal fields appear in every entry. Group fields appear only in entries of the specified group.

| Field | Type | Applies To | Definition |
|-------|------|------------|------------|
| `db_id` | Integer | Universal | Primary key — `component.id` in the DB |
| `component_name` | Prose | Universal | Canonical component name — must match `component.name` in the DB |
| `physical_form` | Prose | Universal | Shape, material, and face-states |
| `quantity` | Expr | Universal | Count during play; suffix `(gameplay requirement)` or `(pre-production estimate)` |
| `visibility` | Enum(visibility) | Universal | Who can observe this component during play |
| `states` | Prose | Universal | Enumerated face-states or board conditions; `N/A` if single-state |
| `faction_keyed` | Enum(yes_no_na) | Universal | Whether faction-colored or faction-specific; `N/A` if not applicable |
| `placement_surface` | Prose | Universal | Where this component legally resides during play; format: `Art 01 zone / component.zone.sub-zone`; semicolon-separated if multiple valid locations; `N/A` if fixed infrastructure |
| `max_placement_count` | Integer | Universal | Maximum simultaneous instances on the component named in `max_placement_ref`; `N/A` if unbounded |
| `max_placement_ref` | ID Reference | Universal | Component against which `max_placement_count` applies; `N/A` if unbounded |
| `movement_path` | Prose | Universal | All legal transitions between placement positions; format: `from → to : trigger`; semicolon-separated; `N/A` if component does not move during play. The `: trigger` slot names the board event or player action that causes the move — not procedural timing (beat numbers, phase names); timing belongs in Art 03. |
| `applicable_verbs` | Enum(verb) | Universal | Semicolon-separated subset of §4.2 verbs that can physically be applied to this component; reflects physical possibility only — game legality is defined in Art 03 §22; `N/A` if no §4.2 verb can physically be applied |
| `display_fields` | Prose | Playing Surface, Card Systems | Required printed or marked information on the component face; semicolon-separated; `N/A` if none |
| `display_component` | ID Reference | Playing Surface | Semicolon-separated list of `component.id` values with a dedicated labeled area on this surface; `N/A` if no specific components are labeled |
| `privacy_model` | Enum(privacy) | Playing Surface | Visibility boundary this surface creates. For flat surfaces (mats, tiles), this describes the surface's own visibility. For physical dividers (screens), this describes the privacy of the space behind them — the divider itself is always visible; the enum captures what it conceals. |
| `recorded_fields` | Prose | Intel | Information written or marked at creation; semicolon-separated; `N/A` if none |
| `back_design` | Enum(back_design) | Card Systems | Card back visual pattern |
| `card_source` | Enum(card_source) | Card Systems | Where this card type enters play from |
| `function` | Prose | Resolution Tools, Tracking Systems | What this component measures, records, flags, or accumulates |
| `scale` | Prose | Resolution Tools, Tracking Systems | Numeric range or discrete position count; `N/A` if not scalar |
| `init_value` | Prose | Resolution Tools, Tracking Systems | Scale value this pointer or marker is set to at session setup; `N/A` for instruments placed or set by procedure rather than preset to a named value |

*Note: `placement_surface` and `movement_path` normalize to junction tables in the DB — not single columns. DB normalization is DB-37's concern. `max_placement_count` and `max_placement_ref` normalize to a single `component_max_placement` row.*

---

#### Data Dictionary

**Types** *(L123 vocabulary; Expr flagged for L123 extension — already in use in Art 04 §6)*

| Type | Format | Notes |
|------|--------|-------|
| `Prose` | Free-form string | No controlled vocabulary; structure defined per field |
| `Integer` | Whole number | |
| `Enum(set)` | Single value from named set | Set defined below |
| `ID Reference` | DB-registered component id | Maps to `component.id`; human-readable name used in Art 02 entries for readability |
| `Expr` | Integer or computed expression | e.g., `5` or `1 per faction × 5 = 5`; vocabulary defined in Art 04 §6.3 *(L123 extension pending)* |

**ENUM Sets**

`visibility:` `Public` · `Player-private` · `ARBITER-only` · `Variable`

`yes_no_na:` `Yes` · `No` · `N/A`

`privacy_model:` `Open` · `Faction-private` · `ARBITER-private`

`back_design:` `Faction-keyed` · `Neutral` · `ARBITER-keyed`

`card_source:` `Deck` · `Hand` · `ARBITER supply` · `Sealed`

`verb:` `Add` · `Remove` · `Move` · `Reveal` · `Conceal` · `Flip` · `Corrupt`

---

#### Group Field Summary

Groups with no group-specific fields are fully covered by universal fields.

| Group | Group-specific fields |
|-------|-----------------------|
| Playing Surface | `display_fields` · `privacy_model` |
| Faction Influence | — |
| Resources | — |
| Covert Messaging | — |
| Intel | `recorded_fields` |
| Card Systems | `back_design` · `card_source` |
| Resolution Tools | `function` · `scale` · `init_value` |
| Tracking Systems | `function` · `scale` · `init_value` |

---

### §4.2 — Physical Action Verbs

| Verb | Primitive | Definition |
|------|-----------|------------|
| **Add** | Place | A component enters active play from supply or off-board |
| **Remove** | Remove | A component exits active play to supply or off-board |
| **Move** | Remove + Place | A component relocates from one on-board location to another |
| **Reveal** | Transform | A component's face or contents become visible to named recipients |
| **Conceal** | Transform | A component is placed or returned face-down or closed |
| **Flip** | Transform | A component's physical orientation is changed — not an information state change |
| **Corrupt** | Transform | A physically written or recorded value on a component is altered |

*Every game action is a sequence of one or more of these primitives: Remove → Transform? → Place. The human hand is the implicit intermediary — not modeled.*

---

## 5. Playing Surface

Components that constitute the physical game table — shared board surfaces, player stations, screens, grids, and the abstract player agent registered for system completeness.

---

### The Overview  (DB: 29)

**Design Function:** The central game mat occupying the Central Area during play. Hosts district tiles, tracking components, the Reservoir, The Backlog, and the Situation Report Zone. The primary shared table surface.

**Narrative Anchor:** The physical table is not an abstraction of New Meridian — it is the room in the story. What MIRROR projects is not geography; it is the Security Liaison's map: accurate not to how the city was built, but to how it can be partitioned, locked down, and controlled. *→ Art 00 §8.1 for full narrative.*

**Gameplay Requirements:** Must accommodate: all 21 district tiles in their ring-zone structure; Reservoir area; Backlog area; Situation Report Zone; Broadcast Card display area; Session Timeline; Initiative Strip; Chorus Activity Track. Full layout: Art 01 §6.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 29 |
| `component_name` | The Overview |
| `physical_form` | Large game mat; flat; single face |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Central Area (Art 01) |
| `max_placement_count` | 1 |
| `max_placement_ref` | Central Area (Art 01) |
| `movement_path` | N/A — fixed infrastructure |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |
| `display_fields` | Ring and zone delineations; labeled areas for Reservoir, Backlog, Situation Report Zone, Session Timeline, Initiative Strip, Chorus Activity Track; Ring 1 modifier deck area; Ring 2 modifier deck area; Ring 3 modifier deck area; Faction Threshold Slider area |
| `display_component` | 32; 33; 25; 23; 24; 31; 53; 54; 55; 107 |
| `privacy_model` | Open |

---

### District tile  (DB: 4)

**Design Function:** Defines the zones of New Meridian where factions contest for influence. Each tile is a named district with a fixed resource type, ring classification, and district zone. The tile is the target surface for all presence, structure, and tension markers.

**Narrative Anchor:** A named district — a specific place with a specific character, held by whoever has built deep enough there to make it theirs. New Meridian's districts are each something specific. A financial corridor generates Capital. A broadcast network generates Exposure. A research installation generates Findings. What a district generates is not assigned — it is what the district does. The tile is that fact, printed. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Each tile must display: district name; grid coordinate in [ring, address] format; native resource type (border color or equivalent); base generation value; 5 faction-keyed structure block areas printed in one of three states — outline (accepts block), outline-with-X (blocked), filled (virtual structure; counts as structure, no physical block placed); state configuration per district metadata table (Art 03). Chorus Node tile must be visually distinct from all faction districts.

Tile surface must physically accommodate during play without obscuring printed information: up to 5 presence chip stacks (1 per faction, up to 6 chips each); up to 5 deployment markers (1 per faction); up to 5 Established markers (simultaneous); 1 Dominant marker (exclusive with Tension marker); 1 Tension marker (exclusive with Dominant marker); up to 5 Structure blocks (1 per faction).

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 4 |
| `component_name` | District tile |
| `physical_form` | Flat tile or card; unique label per district; single face; face-up during all play |
| `quantity` | 21 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | District Zone (Art 01) |
| `max_placement_count` | 21 |
| `max_placement_ref` | District Zone (Art 01) |
| `movement_path` | N/A — fixed at setup |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |
| `display_fields` | District name; grid coordinate [ring, address]; native resource type (border color or symbol); base generation value; 5 faction-keyed presence chip areas; 5 faction-keyed deployment marker areas; 5 faction-keyed structure block areas (per faction: outline = accepts physical block; outline-with-X = blocked; filled square = virtual structure, counts as structure, no block placed — configuration per district metadata table, Art 03); 1 tension marker area (visual design: Art 11) |
| `display_component` | 1; 2; 3; 7 |
| `privacy_model` | Open |

---

### Situation Report  (DB: 102)

**Design Function:** Physical board object in the Situation Report Zone. Hosts Broadcast Cards during play — the display surface for public global events. Analogous to a district tile in that it anchors a zone and receives cards placed on it during resolution.

**Narrative Anchor:** Situation Reports are not local events. They are global shockwaves — market collapses, atmospheric anomalies, intercepted diplomatic transmissions, mass migrations. They reach the table because New Meridian is not isolated; it is the point through which everything else is being filtered. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must provide a clear surface for Broadcast Card placement; must accommodate multiple simultaneous Broadcast Cards (max count TBD — pending Broadcast Card design). Must be visually distinct from district tiles.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 102 |
| `component_name` | Situation Report |
| `physical_form` | Tile or mat; flat; single face; face-up in Situation Report Zone during all play |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Situation Report Zone (Art 01) |
| `max_placement_count` | 1 |
| `max_placement_ref` | Situation Report Zone (Art 01) |
| `movement_path` | N/A — fixed infrastructure |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |
| `display_fields` | Zone designation label; Broadcast Card placement area; visually distinct from district tiles |
| `display_component` | 25 |
| `privacy_model` | Open |

---

### Faction Terminal  (DB: 26)

**Design Function:** The player tableau behind the Faction Screen. Organizes a faction's private workspace — hand, resources, dispatch tokens, operative cards, and private tracking components.

**Narrative Anchor:** A personal interface that connects to MIRROR privately. The Terminal is where a faction holds what has not yet been committed — the inside of the room, before any decision crosses to the open side. *→ Art 00 §8.1 for full narrative.*

**Gameplay Requirements:** Must organize the following components in an accessible layout: faction hand, dispatch case, Dispatch Tokens, resource holdings, operative cards, private tracking components. Full spec: Art 08 (planned).

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 26 |
| `component_name` | Faction Terminal |
| `physical_form` | Game mat or surface; flat; single face; positioned behind Faction Screen |
| `quantity` | 1 per faction × 5 factions = 5 (gameplay requirement) |
| `visibility` | Player-private |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Zone (Art 01) — behind Faction Screen |
| `max_placement_count` | 5 |
| `max_placement_ref` | Faction Zone (Art 01) |
| `movement_path` | N/A — fixed at setup |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |
| `display_fields` | Faction identifier; labeled zones for: faction hand; Dispatch Case; resource holdings; Dispatch Tokens; Operative cards; Intel tokens; CO deck (draw and discard); PA deck (draw and discard); Faction modifier deck; Emergency Response card; Classified Directives; Sealed Apex; Debrief Action Card; Intel Delivery Slip; Notification Slip; Target Profile (blanks) |
| `display_component` | 94; 44; 8; 12; 15; 9; 92; 93; 90; 91; 89; 97; 17; 99; 100; 96; 95; 48 |
| `privacy_model` | Faction-private |

---

### Faction screen  (DB: 27)

**Design Function:** Upright divider at each faction position. Conceals the Faction Terminal — hand, resources, and operational planning — from all other players.

**Narrative Anchor:** The boundary between the closed room and the face a faction turns toward The Table. One side holds what is being considered; the other holds what has been committed. *→ Art 00 §8.1 for full narrative.*

**Gameplay Requirements:** Must conceal the entire Faction Terminal from all other player viewpoints. Faction-labeled or faction-colored for identification.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 27 |
| `component_name` | Faction screen |
| `physical_form` | Upright opaque divider; faction-labeled or faction-colored |
| `quantity` | 1 per faction × 5 factions = 5 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Zone (Art 01) — forward boundary |
| `max_placement_count` | 5 |
| `max_placement_ref` | Faction Zone (Art 01) |
| `movement_path` | N/A — fixed at setup |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |
| `display_fields` | Faction name and/or color on exterior face |
| `display_component` | N/A |
| `privacy_model` | Faction-private |

---

### Faction Resolution Grid  (DB: 88)

**Design Function:** Public-facing playing surface at each faction position. Hosts PA declarations, publicly-played CMs, and standing effects.

**Narrative Anchor:** The face a faction turns toward The Table — where what was decided in the closed room becomes declared and visible. *→ Art 00 §8.1 for full narrative.*

**Gameplay Requirements:** Must accommodate: PA Declaration lanes (up to 4) — each holding PA card, Dispatch Token, Target Profile, submitted resources; CM cards (up to 3, front row); standing effects area (TBD max ~7, back row, symmetric); Status marker area. Resources placed in PA lanes as cost drain to the Reservoir on resolution.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 88 |
| `component_name` | Faction Resolution Grid |
| `physical_form` | Flat surface or mat; public-facing at each faction position |
| `quantity` | 1 per faction × 5 factions = 5 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Zone (Art 01) — public-facing side |
| `max_placement_count` | 5 |
| `max_placement_ref` | Faction Zone (Art 01) |
| `movement_path` | N/A — fixed at setup |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |
| `display_fields` | Faction identifier; PA Declaration lanes (up to 4): each lane accommodates PA card, Dispatch Token, Target Profile, submitted resources; CM Card area (up to 3 cards, front row); Standing effects area (TBD max ~7, back row, symmetric); Status marker area; Layout: front row = CM cards + active PA lanes; row 2 = Target Profile + Dispatch Token per lane; row 3 = submitted resources per lane; back row = standing effects |
| `display_component` | 14; 52; 12; 48; 8; 49; TBD (standing effects components — Art 08) |
| `privacy_model` | Open |

---

### ARBITER screen  (DB: 28)

**Design Function:** Upright divider at ARBITER's position (P6). Conceals ARBITER's private workspace — Portrait tracks, resolution materials, and operational records. Private side may carry printed reference tables and other ARBITER-relevant material.

**Narrative Anchor:** Not concealment in the way the factions use the term — the threshold of a system operating. What is behind it is ARBITER processing in full, not deliberation in progress. *→ Art 00 §9.6 for full narrative.*

**Gameplay Requirements:** Must conceal all private ARBITER materials from all faction positions. Must accommodate the Chorus Portrait tracks and resolution workspace behind it.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 28 |
| `component_name` | ARBITER screen |
| `physical_form` | Upright opaque divider |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | ARBITER Zone (Art 01) — forward boundary |
| `max_placement_count` | 1 |
| `max_placement_ref` | ARBITER Zone (Art 01) |
| `movement_path` | N/A — fixed at setup |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |
| `display_fields` | TBD (Art 07; Art 11) |
| `display_component` | TBD (Art 07; Art 11) |
| `privacy_model` | ARBITER-private |

---

### Arbiter Tableau  (DB: 30)

**Design Function:** ARBITER's private operational workspace, positioned behind the ARBITER screen. Organizes component supplies, reference decks, tracking surfaces, and active game state materials available to ARBITER during play.

**Narrative Anchor:** The inside of ARBITER's awareness — where the full picture sits before any of it becomes signal. The table sees what ARBITER surfaces. This is what ARBITER sees. *→ Art 00 §9.6 for full narrative.*

**Gameplay Requirements:** Must accommodate: Broadcast Card supply; Broadcast Deck and discard; Broadcast Effect Deck and discard; active Broadcast Effect Card(s); blank Intel tokens; blank Accord agreements; Presence chips (supply); Established markers (supply); Dominant markers (supply); Tension markers (supply); Structure blocks (supply); Notification Slips (NS-xx); blank Intel Delivery Slips (IS-xx); Debrief Action Cards (blanks); Visibility Markers (VM-xx); Boost Markers (BM-xx); Modifier tokens; ARBITER Threshold Slider; Chorus Portrait tracks.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 30 |
| `component_name` | Arbiter Tableau |
| `physical_form` | Game mat or surface; flat; single face; behind ARBITER screen |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | ARBITER Zone (Art 01) — behind ARBITER screen |
| `max_placement_count` | 1 |
| `max_placement_ref` | ARBITER Zone (Art 01) |
| `movement_path` | N/A — fixed at setup |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |
| `display_fields` | Labeled areas for: Broadcast Card supply; Broadcast Deck; Broadcast Deck discard; Broadcast Effect Deck; Broadcast Effect Deck discard; active Broadcast Effect Card(s); blank Intel tokens; blank Accord agreements; Presence chips (supply); Established markers (supply); Dominant markers (supply); Tension markers (supply); Structure blocks (supply); Notification Slips (NS-xx); blank Intel Delivery Slips (IS-xx); Debrief Action Cards (blanks); Visibility Markers (VM-xx); Boost Markers (BM-xx); Modifier tokens; ARBITER Threshold Slider; Chorus Portrait tracks |
| `display_component` | 25; 86; TBD (Broadcast Discard — unregistered); 87; TBD (Broadcast Effect Discard — unregistered); 98; 9; 10; 1; 5; 6; 7; 3; 95; 96; 100; 103; 104; 47; 106; 50 |
| `privacy_model` | ARBITER-private |

---

### ARBITER Covert Resolution Grid  (DB: 105)

**Design Function:** Dedicated resolution workspace at ARBITER's position. Five independent lanes provide isolated processing space for each covert submission received in a Quarter.

**Narrative Anchor:** N/A — ARBITER operational surface; players have no knowledge of this component during play. Narrative embedded in covert resolution system (Art 07; Art 00 §9.6).

**Gameplay Requirements:** Must provide 5 distinct, labeled lanes corresponding to case receipt order. Each lane must accommodate stacked cards across Beat 1, Beat 2, and Beat 3 resolution. Lane identity must be unambiguous to ARBITER during processing. *Physical spec: Art 07.*

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 105 |
| `component_name` | ARBITER Covert Resolution Grid |
| `physical_form` | 5-lane grid mat or surface; behind ARBITER screen |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | ARBITER Zone (Art 01) — behind ARBITER screen |
| `max_placement_count` | 1 |
| `max_placement_ref` | ARBITER Zone (Art 01) |
| `movement_path` | N/A — fixed infrastructure |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |
| `display_fields` | 5 labeled lanes (receipt order); Dispatch Case area per lane (×5); printed grid template sized to accommodate: max Beat 1 components per lane; max Beat 2 components + Target Profile per lane; max Beat 3 components + Target Profiles per lane — full dimensional analysis: Art 07 |
| `display_component` | 44; TBD (Art 07) |
| `privacy_model` | ARBITER-private |

---

### Human player  (DB: 43)

**Design Function:** The Faction Representative seated at The Table — the physical agent who holds the faction's cards, manages its Terminal, makes its decisions, and whose choices at this deliberation become the faction's record for the session.

**Narrative Anchor:** Each faction arrives at The Table as a specific person in a specific seat. The faction's history predates them; its future may outlast them. At The Table, they are what the faction is right now. *→ Art 00 §14.1 for full narrative.*

**Gameplay Requirements:** One human player per faction position. Five faction players total, plus one player at the ARBITER position. Human players are the physical actors for all component movement during play.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 43 |
| `component_name` | Human player |
| `physical_form` | Human player — physically present at assigned position |
| `quantity` | 6 (gameplay requirement) — 5 faction players + 1 ARBITER player |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Zone (Art 01); ARBITER Zone (Art 01) |
| `max_placement_count` | 6 |
| `max_placement_ref` | Faction Zone (Art 01); ARBITER Zone (Art 01) |
| `movement_path` | N/A — agent, not a movable component |
| `applicable_verbs` | N/A — agent, not a physical component |
| `display_fields` | N/A — agent, not a physical surface |
| `display_component` | N/A — agent, not a physical surface |
| `privacy_model` | N/A — agent, not a surface |

---

### Reservoir  (DB: 32)

**Design Function:** The shared pool holding all unspent faction resources during play. Distinct from The Backlog, which holds only Dispatch Tokens.

**Narrative Anchor:** The Reservoir is a vast pool of unallocated capital, dormant infrastructure, and political credit accumulated outside New Meridian. Drawing income at Upkeep is not creation. It is activation — converting latent potential into working assets. *→ Art 00 §7 for full narrative.*

**Gameplay Requirements:** Must be physically distinct from The Backlog and from faction tableau resource areas. All 5 resource types must be legibly organized and accessible. Factions draw resources at Upkeep and return them when spending.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 32 |
| `component_name` | Reservoir |
| `physical_form` | Designated area on The Overview; holds all 5 resource types |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | The Overview (Art 01) |
| `max_placement_count` | 1 |
| `max_placement_ref` | The Overview (Art 01) |
| `movement_path` | N/A — fixed infrastructure |
| `applicable_verbs` | N/A — designated zone on The Overview (DB:29); not a separable physical component |
| `display_fields` | Five labeled resource areas — one per type (Findings, Exposure, Capital, Capacity, Mandate); resource type identified by color or label; quantity of each type visible at all times |
| `display_component` | 8 |
| `privacy_model` | Open |

---

### Backlog  (DB: 33)

**Design Function:** Shared pool holding all unissued Dispatch Tokens. The public pool of operational authorization. Distinct from the Reservoir, which holds faction resources.

**Narrative Anchor:** N/A — operational pool area; narrative context embedded in Dispatch Token entry.

**Gameplay Requirements:** Must be physically distinct from the Reservoir. The Dispatch Token supply must be visible — players can observe how many tokens remain in the pool. Factions draw their quarterly Dispatch Token allocation from The Backlog at Upkeep.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 33 |
| `component_name` | Backlog |
| `physical_form` | Designated area on The Overview |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | The Overview (Art 01) |
| `max_placement_count` | 1 |
| `max_placement_ref` | The Overview (Art 01) |
| `movement_path` | N/A — fixed infrastructure |
| `applicable_verbs` | N/A — designated zone on The Overview (DB:29); not a separable physical component |
| `display_fields` | Dispatch Token pool area; token count visible to all players |
| `display_component` | 12 |
| `privacy_model` | Open |

---

## 6. Faction Influence

Components that represent and evaluate each faction's operational depth in districts.

---

### Presence chip  (DB: 1)

**Design Function:** Represents a faction's operational depth in a district.

**Narrative Anchor:** Ghost analysts embedded in research facilities, Syndicate operators running financial infrastructure, Guild engineers maintaining power systems — presence chips represent operational depth: relationships cultivated, systems maintained, people deployed. *→ Art 00 §14 for full narrative.*

**Gameplay Requirements:** Chip count determines influence level (Dominant / Established / Present) and drives resource generation. Faction color must be unambiguous across all five faction colors plus ARBITER white. Must be stackable to 6 without falling.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 1 |
| `component_name` | Presence chip |
| `physical_form` | Small flat disc; faction-colored; stackable; uniform — both faces identical; ARBITER uses white |
| `quantity` | 6 per district × 21 districts = 126 per faction; 5 factions = 630 total (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | District Tile (Art 01) |
| `max_placement_count` | 6 |
| `max_placement_ref` | District Tile (Art 01) |
| `movement_path` | Arbiter Tableau (DB:30) → District Tile (Art 01) : placement; District Tile (Art 01) → Arbiter Tableau (DB:30) : removal |
| `applicable_verbs` | Add; Remove; Move |

---

### Deployment marker  (DB: 2)

**Design Function:** Temporary presence marker placed during the Placement phase.

**Narrative Anchor:** Whatever the doctrine requires — a job fair in the Baryo, a rally in the Core, a demonstration outside the Financial Clearinghouse. The faction is not yet installed. It is present, making the case. The marker is where the argument is being made right now. *→ Art 00 §14 for full narrative.*

**Gameplay Requirements:** Counts as 1 presence chip for all purposes during the Quarter placed. Binary state: Converting (face-up) — marker creates +1 presence chip in its district at Upkeep (Quarter > 1) before being removed; Blocked (face-down) — marker does not create a presence chip at Upkeep and is returned to hand. Two readable face-states required. Must be clearly distinguishable from a standard presence chip by size or form. Faction color must be unambiguous.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 2 |
| `component_name` | Deployment marker |
| `physical_form` | Double-sided chit; larger than presence chip; faction-colored; face-up = Converting / face-down = Blocked |
| `quantity` | TBD (pre-production estimate) |
| `visibility` | Public |
| `states` | Converting (face-up) / Blocked (face-down) |
| `faction_keyed` | Yes |
| `placement_surface` | District Tile (Art 01) |
| `max_placement_count` | TBD |
| `max_placement_ref` | District Tile (Art 01) |
| `movement_path` | Faction Terminal (Art 08 — subzone TBD) → District Tile (Art 01) : faction deploys to district; District Tile (Art 01) → Faction Terminal (Art 08 — subzone TBD) : deployment expires |
| `applicable_verbs` | Add; Remove; Move; Flip |

---

### Established marker  (DB: 5)

**Design Function:** Signals that a faction holds Established influence in a district.

**Narrative Anchor:** They are no longer noticed because they are no longer new. The faction's people move through the district without friction — known at the checkpoint, accounted for in the scheduling, factored into the calculation. Not in control. Present enough that control is the next conversation. *→ Art 00 §14 for full narrative.*

**Gameplay Requirements:** Placed when a faction holds 2nd place with 2+ chips in a district. Multiple factions can hold Established simultaneously — each places their own marker. Placed and removed by the player whose action causes the change. Must be visually distinct from Dominant marker (silver vs. gold). Must be placeable on top of a presence chip stack without obscuring chip count. Quantity driven by maximum simultaneous board state: up to 5 factions can hold Established across all 20 non-Chorus Node districts; Chorus Node permits only 1 Established marker (ARBITER Dominance is permanent; human factions cannot reach Dominant there).

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 5 |
| `component_name` | Established marker |
| `physical_form` | Silver marker; uniform — both faces identical |
| `quantity` | (factions × (districts − 1)) + 1 = (5 × 20) + 1 = 101 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | District Tile (Art 01) |
| `max_placement_count` | 5 |
| `max_placement_ref` | District Tile (Art 01) |
| `movement_path` | Arbiter Tableau (DB:30) → District Tile (Art 01) : Established influence achieved; District Tile (Art 01) → Arbiter Tableau (DB:30) : Established influence lost |
| `applicable_verbs` | Add; Remove; Move |

---

### Dominant marker  (DB: 6)

**Design Function:** Signals that a faction holds Dominant influence in a district.

**Narrative Anchor:** When a faction reaches Dominance, MIRROR formally registers the shift — the faction now controls the traffic routing, municipal drone corridors, and utility outputs of that zone. Dominance is not occupation. It is operation. *→ Art 00 §14.2 for full narrative.*

**Gameplay Requirements:** Placed when a faction holds 1st place with 3+ chips and no tie. One per district at any time. Placed and removed by the player whose action causes the change. Must be visually distinct from Established marker (gold vs. silver). Form should make it obvious only one is placed per district. Not placed at the Chorus Node — ARBITER Dominance is permanent and structurally enforced by DB:42.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 6 |
| `component_name` | Dominant marker |
| `physical_form` | Gold marker; uniform — both faces identical |
| `quantity` | 1 per district × 20 districts = 20 (gameplay requirement; Chorus Node excluded) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | District Tile (Art 01) — excludes Chorus Node |
| `max_placement_count` | 1 |
| `max_placement_ref` | District Tile (Art 01) |
| `movement_path` | Arbiter Tableau (DB:30) → District Tile (Art 01) : Dominant control achieved; District Tile (Art 01) → Arbiter Tableau (DB:30) : control lost or superseded |
| `applicable_verbs` | Add; Remove; Move |

---

### Tension marker  (DB: 7)

**Design Function:** Marks the Contested board state in a district.

**Narrative Anchor:** New Meridian runs a city-wide surveillance mesh. When the system detects localized threshold breaches — acoustic signatures of violence, crowd biometric spikes, encrypted radio bursts — it flags the district on The Overview. The Tension marker is MIRROR's notation that a district's equilibrium has broken. *→ Art 00 §14.2 for full narrative.*

**Gameplay Requirements:** While present, no faction can hold Dominant influence in that district. Placement trigger (non-Chorus Node districts): two or more factions tie for highest chip count at 3+ chips. Placement trigger (Chorus Node): two or more factions tie for highest chip count at 2+ chips. Placed by the player whose action creates the tie; removed by the player whose action resolves it. Must read unambiguously as a board state marker — not a faction piece. Color must be distinct from all faction colors, presence chips, district tiles, and other markers. No required text.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 7 |
| `component_name` | Tension marker |
| `physical_form` | Chip; color distinct from all faction colors, presence chips, district tiles, and other markers; uniform — both faces identical |
| `quantity` | 1 per district × 21 districts = 21 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | District Tile (Art 01) |
| `max_placement_count` | 1 |
| `max_placement_ref` | District Tile (Art 01) |
| `movement_path` | Arbiter Tableau (DB:30) → District Tile (Art 01) : Contested state triggered; District Tile (Art 01) → Arbiter Tableau (DB:30) : Contested state resolved |
| `applicable_verbs` | Add; Remove; Move |

---

### Structure block  (DB: 3)

**Design Function:** Represents a faction's physical facility in a district.

**Narrative Anchor:** A Guild structure block at the Power Grid is a substation. A Syndicate structure block at the Financial Clearinghouse is a trading desk. A Ghost structure block at the Data Exchange is a signal analysis node. They generate resources because they are doing something — not because they exist on paper. *→ Art 00 §14.3 for full narrative.*

**Gameplay Requirements:** Generates additional resources for the owning faction each Quarter. Modifies the difficulty of actions targeting that district. Maximum 1 per faction per district. Removed immediately if the owning faction becomes Absent in that district. Must be visually distinguishable from presence chips and markers. Faction color must be unambiguous. No required text.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 3 |
| `component_name` | Structure block |
| `physical_form` | Small square chit or wooden cube; faction-colored; uniform — both faces identical |
| `quantity` | 1 per faction per district × 21 districts = 21 per faction; 21 per faction × 5 factions = 105 total (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | District Tile (Art 01) |
| `max_placement_count` | 1 |
| `max_placement_ref` | District Tile (Art 01) |
| `movement_path` | Arbiter Tableau (DB:30) → District Tile (Art 01) : structure placement action; District Tile (Art 01) → Arbiter Tableau (DB:30) : removed on faction Absence |
| `applicable_verbs` | Add; Remove; Move |

---

### ARBITER Dominance Marker  (DB: 42)

**Design Function:** Establishes ARBITER's permanent, constitutive presence at the Chorus Node.

**Narrative Anchor:** N/A — constitutive setup piece; narrative embedded in Art 00 Chorus Node entry.

**Gameplay Requirements:** Placed at setup and never moved or removed. Structurally prevents human factions from reaching Dominant at the Chorus Node — not prohibited by rule, made impossible by the board (8 ARBITER tokens exceed the human faction maximum of 6). Must be visually distinct from all faction components. Must read as 8 presence tokens + 1 dominance marker. Fused/inseparable construction is a gameplay requirement — the piece cannot be disassembled during play.

*(Component specification: PM01 §2.08a.)*

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 42 |
| `component_name` | ARBITER Dominance Marker |
| `physical_form` | Single fused piece: 8 ARBITER-keyed presence tokens topped by ARBITER dominance marker; inseparable |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | N/A |
| `placement_surface` | Chorus Node (Art 01) |
| `max_placement_count` | 1 |
| `max_placement_ref` | Chorus Node (Art 01) |
| `movement_path` | N/A — placed at setup; never moved or removed |
| `applicable_verbs` | Add; Remove; Move |

---

## 7. Resources

Token components of the game's economic and operational systems: faction resources and Dispatch Tokens.

---

### Native resource  (DB: 8)

**Design Function:** The five physical resources factions generate, hold, and spend. Each resource embodies its faction's theory of power.

**Narrative Anchor:** Resources represent each faction's theory of power made tangible. Findings accumulates and decays because intelligence must be acted on or it becomes worthless. Capital accrues because the Syndicate's financial systems are always running. Mandate flows from institutional authority exercised every day. *→ Art 00 §7 for full narrative.*

**Gameplay Requirements:** Each resource type must be unambiguously distinct from all other types by color and/or form. Held publicly on player tableaux except during specific phases. All factions can hold and spend any resource type. Most naturally generated through affinity districts and passive generation. 30 per type is a prototype quantity — subject to Art 11 calibration.

| Resource | Faction | Proposed Form |
|----------|---------|---------------|
| Findings | Ghost | Translucent layered chips |
| Exposure | The Network | Bright sharp tokens, ray or broadcast symbol |
| Capital | The Syndicate | Metallic coins or bars |
| Capacity | The Guild | Industrial blocks or plates |
| Mandate | The Directorate | Stamped seal or insignia tokens |

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 8 |
| `component_name` | Native resource |
| `physical_form` | Five distinct token types — one per faction resource; faction-distinct form per type (see variant table above); uniform — both faces identical; any printed markings must appear on both faces |
| `quantity` | 30 per type, 150 total (pre-production estimate) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Reservoir (The Overview); Faction Terminal (Art 08 — subzone TBD) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | a) Reservoir (The Overview) → Faction Terminal (Art 08 — subzone TBD) : income distribution; b) Faction Terminal (Art 08 — subzone TBD) → Faction Resolution Grid (DB: 88) → Reservoir (The Overview) : PA cost; c) Faction Terminal (Art 08 — subzone TBD) → Dispatch Packet (DB: 108) → Dispatch Case (DB: 44) → Arbiter Tableau (DB: 30) — resolution workspace subzone → Reservoir (The Overview) : covert action cost; d) Faction Terminal (Art 08 — subzone TBD) → Faction Terminal (Art 08 — subzone TBD) : faction-to-faction transfer; e) Faction Terminal (Art 08 — subzone TBD) → Arbiter Tableau (DB: 30) — resolution workspace subzone → Reservoir (The Overview) → Faction Terminal (Art 08 — subzone TBD) : trade at exchange rate (4:1, 3:1, or 2:1); resource type changes on return |
| `applicable_verbs` | Add; Remove; Move |

---

### Dispatch token  (DB: 12)

**Design Function:** Operational authorization — the capacity unit enabling a faction to submit a covert operation.

**Narrative Anchor:** A Dispatch Token is the authorization that converts planned work into active production for this Quarter — the executive order that takes a theoretical project off the backlog and commits the organization to it. *→ Art 00 §14.5 for full narrative.*

**Gameplay Requirements:** Must be clearly distinguishable from resource tokens and from dispatch cases. No required text. Not a faction resource. Does not generate through districts, accumulate across Quarters, or carry affinity. One accompanies each covert operation card submitted in a dispatch case.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 12 |
| `component_name` | Dispatch token |
| `physical_form` | Small token or chit; copper; uniform — both faces identical |
| `quantity` | 4 per faction × 5 factions = 20 total (gameplay requirement); 4 allocated per faction per Quarter |
| `visibility` | Public (in Backlog or Faction Resolution Grid); private (in Dispatch Packet) |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Backlog (The Overview); Faction Terminal (Art 08 — subzone TBD); Faction Resolution Grid (DB: 88); Dispatch Packet (DB: 108) |
| `max_placement_count` | 4 |
| `max_placement_ref` | Faction Terminal (Art 08 — subzone TBD) |
| `movement_path` | a) Backlog (The Overview) → Faction Terminal (Art 08 — subzone TBD) : dispatch allocation; b) Faction Terminal (Art 08 — subzone TBD) → Faction Resolution Grid (DB: 88) → Backlog (The Overview) : PA cost; c) Faction Terminal (Art 08 — subzone TBD) → Dispatch Packet (DB: 108) → Dispatch Case (DB: 44) → Arbiter Tableau (DB: 30) — resolution workspace subzone → Backlog (The Overview) : covert action cost |
| `applicable_verbs` | Add; Remove; Move |

---

## 8. Covert Messaging System

Physical infrastructure of the covert dispatch and return channel — submission vessels and operational tracking documents.

---

### Dispatch case  (DB: 44)

**Design Function:** The faction's sealed covert submission vessel — the channel through which committed covert operations pass to ARBITER.

**Narrative Anchor:** Where a faction's committed covert operations leave the private room and enter resolution — sealed, sequenced, anonymous to everyone except the faction that sealed it. *→ Art 00 §14.5 for full narrative.*

**Gameplay Requirements:** Must be fully opaque. Must accommodate 4 Dispatch Packets simultaneously. Faction-labeled or faction-colored for identification. One case submitted per faction per Month.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 44 |
| `component_name` | Dispatch case |
| `physical_form` | Sealed envelope or small box; opaque |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Terminal (Art 08 — subzone TBD); ARBITER Covert Resolution Grid (DB: 105) |
| `max_placement_count` | 1 |
| `max_placement_ref` | Faction Terminal (Art 08 — subzone TBD) |
| `movement_path` | Faction Terminal (Art 08 — subzone TBD) → ARBITER Covert Resolution Grid (DB: 105) : submission; ARBITER Covert Resolution Grid (DB: 105) → Faction Terminal (Art 08 — subzone TBD) : return after resolution |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Dispatch Packet  (DB: 108)

**Design Function:** Ordered sub-container within the Dispatch Case. Groups a single covert operation and its accompanying components for submission.

**Narrative Anchor:** Four committed operations, sequenced before the case seals. What order they go in is the last decision a faction makes in private. *→ Art 00 §14.5 for full narrative.*

**Gameplay Requirements:** Must hold and group: 1 covert operation card, 1 Dispatch Token, resource tokens (variable), 1 Target Profile, Modifier Cards (variable). 4 per case, ordered 1–4. Must maintain submission sequence and keep contents grouped during case transit.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 108 |
| `component_name` | Dispatch Packet |
| `physical_form` | Small envelope, sleeve, or insert within Dispatch Case; ordered 1–4 per case |
| `quantity` | 4 per faction × 5 factions = 20 total (gameplay requirement) |
| `visibility` | Player-private |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Dispatch Case (DB: 44); Faction Terminal (Art 08 — subzone TBD); ARBITER Covert Resolution Grid (DB: 105) |
| `max_placement_count` | 4 |
| `max_placement_ref` | Dispatch Case (DB: 44) |
| `movement_path` | a) Faction Terminal (Art 08 — subzone TBD) → Dispatch Case (DB: 44) : faction loads packet; b) Dispatch Case (DB: 44) → ARBITER Covert Resolution Grid (DB: 105) : ARBITER extracts for resolution; c) ARBITER Covert Resolution Grid (DB: 105) → Dispatch Case (DB: 44) → Faction Terminal (Art 08 — subzone TBD) : return after resolution |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Target Profile  (DB: 48)

**Design Function:** Tracking document completed by a faction to identify the target of a covert operation or public act. Used by ARBITER during resolution.

**Narrative Anchor:** N/A — operational tracking record; no narrative element.

**Gameplay Requirements:** Must record one or more of: target faction, target district, operation type. Completed by the submitting faction before submission. Erased or disposed of after use — physical design pending Art 08.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 48 |
| `component_name` | Target Profile |
| `physical_form` | Document or card; printed field labels on obverse (face valid for Reveal/Conceal in all states — Blank and Filled); erasable or single-use — physical spec pending Art 08 |
| `quantity` | Variable — 1 per active operation in resolution (pre-production estimate) |
| `visibility` | ARBITER-only (covert path, during resolution); public (PA path, on Faction Resolution Grid) |
| `states` | Blank; Filled |
| `faction_keyed` | No |
| `placement_surface` | Faction Terminal (Art 08 — subzone TBD); Dispatch Packet (DB: 108); ARBITER Covert Resolution Grid (DB: 105); Faction Resolution Grid (DB: 88) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | a) Covert: Faction Terminal (blank) → Dispatch Packet (DB: 108) → Dispatch Case (DB: 44) → ARBITER Covert Resolution Grid (DB: 105) → Dispatch Packet (DB: 108) → Dispatch Case (DB: 44) → Faction Terminal : covert op resolution; b) PA: Faction Terminal (blank) → Faction Resolution Grid (DB: 88) → Faction Terminal : PA or standing effects resolution |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal; Corrupt |
| `recorded_fields` | One or more of: target faction; target district; operation type |

---

## 9. Intel & Information

Components carrying recorded content — intelligence, agreements, and ARBITER-dispatched information delivered to or held by factions.

---

### Intel token  (DB: 9)

**Design Function:** A discrete intelligence record one faction holds about another. Carries the subject faction and Quarter gathered.

**Narrative Anchor:** An Intel Token is discrete, specific, time-stamped, and targeted. Knowledge is power — but it expires, can be traded, can be bluffed about, can be disclosed strategically, and can be turned against the faction it describes. *→ Art 00 §14.9 for full narrative.*

**Gameplay Requirements:** ARBITER records at creation: (1) faction the intelligence concerns, (2) Quarter gathered. Must accommodate handwritten notation. Enables targeted actions and powers the Denounce political act. Created by ARBITER on a successful gather action; delivered privately to the receiving faction. Holder may disclose at any time by any method.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 9 |
| `component_name` | Intel token |
| `physical_form` | Small token or chit; obverse: printed "Intel" label; reverse: printed field labels "Quarter ____ \| Faction ____" with blank lines for handwritten content (ARBITER fills at creation); physical spec: Art 11 |
| `quantity` | Variable — created during play (pre-production estimate for supply) |
| `visibility` | Player-private |
| `states` | Blank; Fresh; Stale; Expired (per Art 03 §13.6) |
| `faction_keyed` | No |
| `placement_surface` | Arbiter Tableau (DB: 30); Dispatch Packet (DB: 108); Dispatch Case (DB: 44); Faction Terminal (Art 08 — subzone TBD); Faction Resolution Grid (DB: 88) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | a) Receipt: Arbiter Tableau (DB: 30) [blank] → resolution workspace subzone [written] → Dispatch Packet (DB: 108) → Dispatch Case (DB: 44) → Faction Terminal (Art 08 — subzone TBD) : gather action delivery; b) Covert spend: Faction Terminal (Art 08 — subzone TBD) → Dispatch Packet (DB: 108) → Dispatch Case (DB: 44) → Arbiter Tableau (DB: 30) — resolution workspace subzone [erased or discarded] → Arbiter Tableau (DB: 30) if recycled : covert action spend; c) Public spend: Faction Terminal (Art 08 — subzone TBD) → Faction Resolution Grid (DB: 88) → Arbiter Tableau (DB: 30) — resolution workspace subzone [erased or discarded] → Arbiter Tableau (DB: 30) if recycled : PA spend; d) Faction Terminal (Art 08 — subzone TBD) → Faction Terminal (Art 08 — subzone TBD) : faction-to-faction trade |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal; Corrupt |
| `recorded_fields` | Faction the intelligence concerns; Quarter gathered (handwritten by ARBITER at creation) |

---

### Accord agreement  (DB: 10)

**Design Function:** Biometric contract between two or more factions registering an agreed arrangement in ARBITER's canonical record.

**Narrative Anchor:** Accord Documents are biometric smart-paper. When placed face-up on the scanner beds of The Overview, MIRROR reads the signatures of the parties and registers the agreement into ARBITER's canonical record. ARBITER does not negotiate terms. It records what was signed. *→ Art 00 §8.1 for full narrative.*

**Gameplay Requirements:** Must display: parties to the Accord, agreed terms. Face-up placement in Accord Placement Area is binding and registers the agreement with ARBITER.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 10 |
| `component_name` | Accord agreement |
| `physical_form` | Document or card; obverse: printed Accord form fields (Art 06 §9); reverse: blank; placed face-up in Accord Placement Area when active |
| `quantity` | Variable — 1 per active Accord (pre-production estimate for supply) |
| `visibility` | Player-private (Blank; Draft — at Faction Terminal); public (Active/Executed — at Accord Placement Area) |
| `states` | Blank; Active (Draft); Active (Executed); Breach / Dissolved |
| `faction_keyed` | No |
| `placement_surface` | Arbiter Tableau (DB: 30); Faction Terminal (Art 08 — subzone TBD); Accord Placement Area (Art 01) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | a) Arbiter Tableau (DB: 30) → Faction Terminal (Art 08 — subzone TBD) : ARBITER delivers blank form; b) Faction Terminal (Art 08 — subzone TBD) → Accord Placement Area (Art 01) : faction places drafted Accord [Draft → Executed state change at Accord Placement Area]; c) Accord Placement Area (Art 01) → Arbiter Tableau (DB: 30) : Breach or Dissolution |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal; Corrupt |
| `recorded_fields` | Full field set defined in Art 06 §9 |

---

### Notification Slip (NS-xx)  (DB: 95)

**Design Function:** Pre-printed ARBITER notification slip delivered privately to a faction when a covert operation targeted their assets. Content is fixed: "An operation targeting your assets occurred."

**Narrative Anchor:** N/A — private delivery mechanism; narrative is in the event, not the slip itself.

**Gameplay Requirements:** Pre-printed; no handwritten content required. Faction-addressed. Corresponding event logged in ARBITER observation register.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 95 |
| `component_name` | Notification Slip (NS-xx) |
| `physical_form` | Pre-printed slip or small card; faction-addressed; obverse: printed content; reverse: blank |
| `quantity` | Variable — created by ARBITER as needed (pre-production estimate) |
| `visibility` | Player-private |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Arbiter Tableau (DB: 30) — resolution workspace subzone; Dispatch Case (DB: 44) after delivery |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Arbiter Tableau (DB: 30) — resolution workspace subzone → Dispatch Case (DB: 44) : ARBITER delivery; Dispatch Case (DB: 44) → Faction Terminal (Art 08 — subzone TBD) : faction receipt |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |
| `recorded_fields` | Hardcoded — "An operation targeting your assets occurred." |

---

### Intel Delivery Slip (IS-xx)  (DB: 96)

**Design Function:** ARBITER-dispatched intelligence delivery to a faction. The physical mechanism by which ARBITER delivers intel content privately.

**Narrative Anchor:** N/A — private delivery mechanism; narrative is in the intelligence content, not the slip itself.

**Gameplay Requirements:** Must accommodate handwritten content. Faction-addressed. Must be distinguishable from Notification Slips.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 96 |
| `component_name` | Intel Delivery Slip (IS-xx) |
| `physical_form` | Slip or small card; obverse: printed field labels (Recipient; Quarter/Month; Submitting Faction; Covert Operation; Target Faction; Target District; Operation Type; Boost Marker Y/N; Modifier Total); reverse: blank; faction-addressed; distinguishable from Notification Slip |
| `quantity` | Variable — created by ARBITER as needed (pre-production estimate) |
| `visibility` | Player-private |
| `states` | Blank; Filled |
| `faction_keyed` | Yes |
| `placement_surface` | Dispatch Packet (DB: 108); Dispatch Case (DB: 44); Faction Terminal (Art 08 — subzone TBD) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Arbiter Tableau (DB: 30) — resolution workspace subzone → Dispatch Packet (DB: 108) → Dispatch Case (DB: 44) → Faction Terminal (Art 08 — subzone TBD) : placed in corresponding CA packet; returned via case at resolution |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal; Corrupt |
| `recorded_fields` | Recipient faction; Quarter/Month of delivery; Submitting faction; Covert operation; Target faction; Target district; Operation type; Boost Marker present (Y/N); Modifier token total (+/− n) — handwritten by ARBITER at delivery |

---

### Grant Deed  (DB: 113)

**Design Function:** ARBITER-issued title card recording a faction's capital claim on a named district. Functions as a React card: the holding faction plays it immediately when any faction places a structure block in the named district, placing their own structure block there. The deed may be traded between factions; the `owner` field is updated by the new holder and the claim transfers with the card.

**Narrative Anchor:** *A filed claim is not the same as a built presence — but it changes what can be built there.*

**Gameplay Requirements:** Must be writable — ARBITER fills `district` and `owner` fields at issuance. `owner` field is mutable: any faction receiving the deed by trade may overwrite it with their own name. Must be distinguishable from Intel Delivery Slips (IS-xx) and other ARBITER-issued slips. Blank supply stored in ARBITER Tableau. Multiple Grant Deeds may exist simultaneously (same or different districts). Played from holding faction's hand as a React card; consumed on trigger fire. No board marker placed by this card. Governed by GR 8.2 (structure placement). React timing: Art 03 §18. Art 04 spec: 04-n99.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 113 |
| `component_name` | Grant Deed |
| `physical_form` | Standard card; obverse: printed field labels (`district`, `owner`), writable fields (dry-erase preferred — ARBITER fills at issuance); reverse: blank |
| `quantity` | Variable — ARBITER issues from tableau supply as needed (pre-production estimate) |
| `visibility` | Player-private |
| `states` | Blank (ARBITER Tableau) → Filled (Dispatch Case / hand) → Fired (React triggered; consumed) \| Expired (held to game end; if dry-erasable: wiped and returned blank to ARBITER Tableau; otherwise discarded — pending physical design) |
| `faction_keyed` | No — issued to any faction by ARBITER |
| `placement_surface` | ARBITER Tableau (DB: 30); Dispatch Packet (DB: 108); Dispatch Case (DB: 44); Faction Tableau — hand; Faction Resolution Grid (DB: 88) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | a) Creation: ARBITER Tableau (DB: 30) — blank supply → ARBITER Tableau (DB: 30) — resolution subzone [write `district` + `owner`] → Dispatch Packet (DB: 108) → Dispatch Case (DB: 44) → Faction Tableau — hand ; b) Trade: Faction Tableau — hand → Faction Tableau — hand : faction-to-faction trade; new holder updates `owner` field; c) React (on trigger): Faction Tableau — hand → Faction Resolution Grid (DB: 88) — modifier/permanent row → effect resolves → ARBITER Tableau (DB: 30) : structure block placed in named district; erase and return blank to supply OR discard (pending physical design) |
| `recorded_fields` | `district` (named target district); `owner` (faction currently holding the claim — mutable, updated by new holder on trade) |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal; Corrupt |

---

### DebriefActionCard  (DB: 100)

**Design Function:** Card type carrying ARBITER-issued instructions or outcomes for processing in the Debrief phase.

**Narrative Anchor:** Some things ARBITER determines do not surface at The Table. They arrive in the return channel — placed in the case, opened at Debrief, resolved in private. *→ Art 00 §9.6 for full narrative.*

**Gameplay Requirements:** Must be distinguishable from covert operation cards and political act cards. Placed by ARBITER in a faction's dispatch case during resolution. Processed at Debrief start.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 100 |
| `component_name` | DebriefActionCard |
| `physical_form` | Standard card; obverse: printed field labels (variable — ARBITER fills at issuance); reverse: blank |
| `quantity` | Variable — placed by ARBITER as needed (pre-production estimate) |
| `visibility` | Player-private |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Dispatch Packet (DB: 108); Dispatch Case (DB: 44); Faction Terminal (Art 08 — subzone TBD) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Arbiter Tableau (DB: 30) — resolution workspace subzone → Dispatch Packet (DB: 108) → Dispatch Case (DB: 44) → Faction Terminal (Art 08 — subzone TBD) : placed in corresponding CA packet; returned via case at resolution |
| `recorded_fields` | Variable |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal; Corrupt |

---

## 10. Card Systems

Individual action and event cards — the operational content of card-based gameplay. Container components (hands, draw decks, discard piles) are in §10.1.

---

**Operative**

### Classified directives  (DB: 17)

**Design Function:** A faction-specific directive tied to the faction's operative. Multiple versions exist per operative; the faction player selects or draws one at initialization. The chosen directive is held privately for the duration of the arc.

**Narrative Anchor:** The mission beneath all other missions — not the Chorus's directive, but the operative's own: the private ambition pursued beneath every public act. At session's end, the agenda surfaces. *→ Art 00 §14.7 for full narrative.*

**Gameplay Requirements:** Distributed at game initialization from a faction-specific init-only deck (external to the game area; companion deck component pending registration — PM05 02-n20). Multiple directive variants exist per operative; faction player selects or draws one matched to their chosen or randomly drawn operative (selection mechanic TBD — Art 05); remaining directives returned to storage. Private to the faction player; must not be disclosed before session end. ARBITER may receive a companion tracking card at initialization (component not yet registered — TBD Art 05); if present, ARBITER monitors progress privately. Revealed publicly at session end. Success condition measured against board state or private component counts — examples: total Modifier cards held, Modifier cards by deck, Intel Tokens, native resources, Intel Delivery Slips. Full mechanics TBD — Art 05.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 17 |
| `component_name` | Classified directives |
| `physical_form` | Standard card (TBD — Art 11); obverse: directive content (faction/operative-specific, pre-printed); reverse: faction- and operative-keyed back |
| `quantity` | TBD — multiple variants per operative (Art 05) |
| `visibility` | Player-private |
| `states` | Private (active) / Revealed (session end) |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Hand (DB:94) |
| `max_placement_count` | 1 per faction player |
| `max_placement_ref` | Faction Hand (DB:94) |
| `movement_path` | Init-only deck (external) → Faction Hand (DB:94) : one selected at initialization; remaining variants → returned to storage; Faction Hand (DB:94) → public disclosure : at session end |
| `back_design` | Faction-keyed and operative-keyed |
| `card_source` | Classified Directives Pool (DB:118) — init only; external to game area |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Operative card  (DB: 15)

**Design Function:** The faction's named operative — a personal asset card that can be played on the Faction Resolution Grid directly or as a covert act. Usage is tracked directly on the card; each use enhances the operative's effect and escalates toward an Apex trigger.

**Narrative Anchor:** Each faction enters the deliberation with one named Field Operative — not a resource, not a deployment, but a person prepared for the Apex: the moment The Table stops calculating what the Chorus expects and chooses, instead, to answer freely. The operative is the one who makes that play; what they spend is total and unrepeatable. *→ Art 00 §14.8 for full narrative. Individual operative card designs carry operative-specific narrative.*

**Gameplay Requirements:** Selected from a faction-specific init-only variant pool deck at initialization (selection mechanic TBD — Art 05). Two play modes: (1) played directly onto the Faction Resolution Grid (DB:88) as a resolution asset; (2) played as a covert act via the standard dispatch procedure. Returned to hand after resolution in either mode — not discarded. Usage tracked by writing directly on the card; each use has a distinct cost and an enhanced effect. On the 4th use, if all criteria are met, the Apex triggers — DB:99 Sealed Apex ability revealed and activated. Full mechanics TBD — Art 04/05.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 15 |
| `component_name` | Operative card |
| `physical_form` | Standard card; obverse: operative content (printed) + writable usage tracking fields; reverse: faction- and operative-keyed back (TBD — Art 11) |
| `quantity` | TBD — one per faction player (selected at init) |
| `visibility` | Player-private |
| `states` | In hand / Active (on Faction Resolution Grid) / Usage marks (1–4) |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Hand (DB:94); Faction Resolution Grid (DB:88) when played |
| `max_placement_count` | 1 per faction player |
| `max_placement_ref` | Faction Hand (DB:94) |
| `movement_path` | Operative Pool (DB:116) → Faction Hand (DB:94) : selected at init; *Resolution asset mode:* Faction Hand (DB:94) → Faction Resolution Grid (DB:88) : played directly; Faction Resolution Grid → Faction Hand (DB:94) : returned after resolution; *Covert act mode:* Faction Hand (DB:94) → Dispatch Packet (DB:108) → Dispatch Case (DB:44) → Arbiter Tableau (DB:30) : ARBITER opens case and packet; Arbiter Tableau → Faction Resolution Grid (DB:88) : placed in resolution grid; Faction Resolution Grid → Dispatch Packet (DB:108) → Dispatch Case (DB:44) → Faction Hand (DB:94) : returned after resolution |
| `back_design` | Faction-keyed and operative-keyed |
| `card_source` | Operative Pool (DB:116) — init only |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal; Corrupt |

---

### Sealed Apex ability  (DB: 99)

**Design Function:** Per-faction sealed card unlocked when the faction's operative completes their 4th action and all Apex criteria are met. Contents remain private until triggered; presented publicly on activation. Successfully playing this card triggers the end of game sequence.

**Narrative Anchor:** The Apex is the final act of the answer window — the moment The Table stops calculating what the Chorus expects and chooses, instead, to answer freely. Not a positioning move. A declaration. What the Chorus makes of it, on whatever terms it actually holds, the Chronicle cannot know — only that it happened: humanity, given the chance to answer correctly, chose instead to answer freely. *→ Art 00 §14.8 for full narrative.*

**Gameplay Requirements:** Provided to Faction Terminal at initialization; remains sealed until trigger. Trigger: DB:15 Operative card takes its 4th action with all Apex criteria validated. On trigger: opened, unlocked, and presented publicly per Art 03 §14 (Apex Activation procedure). Masking component required to prevent reading before unlock — design TBD Art 05. Full rules and card design TBD Art 05.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 99 |
| `component_name` | Sealed Apex ability |
| `physical_form` | Sealed card; masking component TBD Art 05; TBD — Art 11 |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private (sealed) / Public (on trigger) |
| `states` | Sealed (pre-trigger) / Revealed (on trigger) |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Hand (DB:94) |
| `max_placement_count` | 1 |
| `max_placement_ref` | Faction Hand (DB:94) |
| `movement_path` | Apex Ability Pool (DB:117) → Faction Hand (DB:94) : provided at initialization (sealed); Faction Hand (DB:94) : held sealed until DB:15 4th action trigger; → public presentation : opened and revealed per Art 03 §14 on trigger |
| `back_design` | Faction-keyed |
| `card_source` | Apex Ability Pool (DB:117) — init only |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Emergency Response card  (DB: 97)

**Design Function:** A unique faction card held at the Faction Terminal from initialization. When any operative moves to complete their 4th action, every faction has the opportunity to play their Emergency Response ahead of the Apex unlock — potentially helping or hindering the trigger. Full rules TBD — Art 05.

**Narrative Anchor:** At the moment any operative moves to complete the Apex, every faction at The Table is given one final opportunity to act — to shape, block, or enable what is about to happen. The Emergency Response is that act: a single intervention, prepared at the start and held until it may be necessary. *→ Art 00 §14.8 for full narrative context.*

**Gameplay Requirements:** 1 unique card per faction; provided at initialization and held at Faction Terminal — not drawn from a deck. Opportunity to play is triggered when any operative (any faction) takes their 4th action. Played publicly to Faction Resolution Grid (DB:88) ahead of Apex unlock. If Apex does not trigger: returned to Faction Terminal. If Apex triggers: end of game sequence begins; no cleanup required. Full mechanics TBD — Art 05.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 97 |
| `component_name` | Emergency Response card |
| `physical_form` | Standard card (TBD — Art 11); obverse: response content (faction-specific, pre-printed); reverse: faction-keyed back |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private (at terminal) / Public (when played) |
| `states` | Held / Played / Returned |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Hand (DB:94); Faction Resolution Grid (DB:88) when played |
| `max_placement_count` | 1 per faction |
| `max_placement_ref` | Faction Resolution Grid (DB:88) |
| `movement_path` | Game initialization → Faction Hand (DB:94) : placed at setup; Faction Hand (DB:94) → Faction Resolution Grid (DB:88) : played publicly on Apex trigger opportunity; Faction Resolution Grid → Faction Hand (DB:94) : returned if Apex does not trigger; Faction Resolution Grid : remains if Apex triggers (end of game) |
| `back_design` | Faction-keyed |
| `card_source` | Provided at initialization (no source deck) |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

**Operations Resolution**

### Covert operation  (DB: 13)

**Design Function:** The primary covert action card. The operative instruction a faction submits for resolution each Month.

**Narrative Anchor:** A covert operation is submitted in a dispatch case — sealed, placed without announcement, given over to ARBITER before the world has had a chance to respond. Each faction has its own form: Ghost submits operation orders, the Syndicate submits terms, the Guild submits work orders. What every submission shares is that it exists before the action — the plan committed before the result is known. *→ Art 00 §14.6 for full narrative.*

**Gameplay Requirements:** Must display: action name, cost, resolution threshold, target requirements, effect on success, effect on failure, and burst indicator (recognizable at Beat 0 so ARBITER can apply BM-xx to downstream cards in the resolution grid). Must not be readable through the dispatch case when submitted. Submitted secretly each Month via Dispatch Packet and Dispatch Case. Drives the Beat 0–3 resolution sequence. Receivable — ARBITER receives and manages submitted operations during resolution.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 13 |
| `component_name` | Covert operation |
| `physical_form` | Standard card; faction back; submitted face-down; held by ARBITER during resolution |
| `quantity` | Variable per faction deck (pre-production estimate) |
| `visibility` | Player-private in hand; ARBITER-only during resolution |
| `states` | Face up (active) / Face down (void) |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Hand (DB:94); Dispatch Packet (DB:108); ARBITER Covert Resolution Grid (DB:105) |
| `max_placement_count` | 6 (in hand) |
| `max_placement_ref` | Faction Hand (DB:94) |
| `movement_path` | Covert Operation Card Set (DB:114) → Faction Hand (DB:94) : selected subset at init; forms Covert operation deck (DB:92); Covert operation deck (DB:92) → Faction Hand (DB:94) : drawn to hand; Faction Hand (DB:94) → Dispatch Packet (DB:108) → Dispatch Case (DB:44) → ARBITER Covert Resolution Grid (DB:105) : ARBITER opens case and packet, places card in grid; ARBITER Covert Resolution Grid (DB:105) → Dispatch Packet (DB:108) → Dispatch Case (DB:44) → Faction Hand (DB:94) → Covert operation discard (DB:93) : post-resolution |
| `back_design` | Faction-keyed |
| `card_source` | Covert Operation Card Set (DB:114) → Covert operation deck (DB:92) — subset selected at init |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Political act  (DB: 14)

**Design Function:** Public action card representing a faction's overt political move.

**Narrative Anchor:** A public act is declared at The Table — witnessed, placed in the open, the faction's intention made visible at the moment of commitment. Both covert and public submissions authorize an attempt, not a guaranteed outcome; the difference is who observes the commitment being made. *→ Art 00 §14.6 for full narrative.*

**Gameplay Requirements:** Must display: act name, cost, effect, targeting requirements. Must be distinguishable from covert operation cards by back design. Declared openly at The Table during Phase B; played face-up at declaration. Requires no Dispatch Token. Receivable — ARBITER and all factions observe.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 14 |
| `component_name` | Political act |
| `physical_form` | Standard card; distinctive back; played face-up at declaration |
| `quantity` | Variable per faction deck (pre-production estimate) |
| `visibility` | Player-private in hand; Public when declared |
| `states` | Face up (active) / Face down (void) |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Hand (DB:94); Faction Resolution Grid (DB:88) |
| `max_placement_count` | 4 in hand (3 drawn + 1 Floor Act — returns to hand per card spec) |
| `max_placement_ref` | Faction Hand (DB:94) |
| `movement_path` | Political Act Card Set (DB:115) → Faction Hand (DB:94) : selected subset at init; forms Political act deck (DB:90); Political act deck (DB:90) → Faction Hand (DB:94) : drawn to hand; Faction Hand (DB:94) → Faction Resolution Grid (DB:88) : public declaration (face-up); Faction Resolution Grid (DB:88) → Political act discard (DB:91) : after resolution |
| `back_design` | Faction-keyed |
| `card_source` | Political Act Card Set (DB:115) → Political act deck (DB:90) — subset selected at init |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Modifier card  (DB: 11)

**Design Function:** Represents assets, equipment, and specialized tactics employed by the card's source — each ring and faction produces unique modifier cards reflecting the operational capabilities of that area. Drawn at upkeep; supports covert operations, public acts, react plays, and district tension resolution. Removed from game after use in all modes.

**Narrative Anchor:** Each ring and faction produces its own assets, equipment, and tactics — the material conditions of a district, or the operational culture of a faction, expressed as support for the operations underway. A modifier card is that resource in motion. *→ Art 00 §14.6 (addition pending — PM05 02-n23).*

**Gameplay Requirements:** Sourced from 8 decks: Ring 1 (DB:53), Ring 2 (DB:54), Ring 3 (DB:55), and 5 faction modifier decks (DB:89). Ring deck cards are ring-keyed; faction deck cards are faction-keyed. Drawn at upkeep from the applicable deck to Faction Terminal. Four play modes: (1) Covert support — included with CO submission, follows covert path to ARBITER resolution, removed from game after resolution; (2) Public play — played with PA submission, follows PA path to Faction Resolution Grid, removed from game after resolution; (3) React — played on board state trigger from Faction Terminal to Faction Resolution Grid; may persist as a standing effect before resolution; removed from game when resolved; (4) Tension resolution — played from Faction Terminal to open table area to modify district tension battle outcome; removed from game immediately after. Full card design and value range: Art 04 §11.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 11 |
| `component_name` | Modifier card |
| `physical_form` | Standard card; faction-keyed back (faction decks) or ring-keyed back (ring decks) |
| `quantity` | TBD — varies per deck (pre-production estimate) |
| `visibility` | Player-private at terminal; ARBITER-only during covert resolution; Public when played in all other modes |
| `states` | In hand / Played (removed from game) |
| `faction_keyed` | Faction-keyed (faction modifier decks DB:89) / Ring-keyed (ring modifier decks DB:53/54/55) |
| `placement_surface` | Faction Hand (DB:94); Dispatch Packet (DB:108) for covert play; ARBITER Covert Resolution Grid (DB:105) during covert resolution; Faction Resolution Grid (DB:88) for PA/react play; table surface for tension resolution |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Modifier deck (DB:53/54/55/89) → Faction Hand (DB:94) : faction draws from modifier deck; *Covert play:* Faction Hand (DB:94) → Dispatch Packet (DB:108) → Dispatch Case (DB:44) → ARBITER Covert Resolution Grid (DB:105) : included with CO submission; follows covert path; → removed from game after resolution; *Public play:* Faction Hand (DB:94) → Faction Resolution Grid (DB:88) : played with PA submission; follows PA path; → removed from game after resolution; *React play:* Faction Hand (DB:94) → Faction Resolution Grid (DB:88) : played on board state trigger; may persist as standing effect; → removed from game when resolved; *Tension resolution:* Faction Hand (DB:94) → table surface (open area) : modifies district tension battle outcome; → removed from game |
| `back_design` | Faction-keyed (faction decks) / Ring-keyed (ring decks) |
| `card_source` | 8 source decks: Ring 1 (DB:53) · Ring 2 (DB:54) · Ring 3 (DB:55) · Faction modifier decks ×5 (DB:89) |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Countermeasure card  (DB: 52)

**Design Function:** A reactive card type issued at initialization in a fixed set of three per faction — one CM-A and two CM-B. CM-A blocks all actions against the faction for the month played; CM-B adds a modifier to all actions against the faction for the month played. Played covertly or publicly; removed from game after use.

**Narrative Anchor:** N/A — narrative support not yet established. PM05 02-n22 flagged for Art 00 grounding.

**Gameplay Requirements:** Issued at initialization as a fixed set; not drawn from a deck during play. Two subtypes: CM-A (1 per faction — blocks all actions against faction for the month); CM-B (2 per faction — adds modifier to all actions against faction for the month). Cards are identical within each subtype — not faction-specific. Two play modes: covert (placed on top of Dispatch Case, not inside packet) or public (declared on Faction Resolution Grid). Procedures: Art 03 §8, §9, §13.5. Removed from game after resolution in either mode.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 52 |
| `component_name` | Countermeasure card |
| `physical_form` | Standard card; neutral back; two subtypes (CM-A, CM-B) |
| `quantity` | 5 CM-A + 10 CM-B = 15 total (gameplay requirement; identical within subtype) |
| `visibility` | Player-private at terminal; Public when played |
| `states` | In hand / Played (removed from game) |
| `faction_keyed` | No |
| `placement_surface` | Faction Hand (DB:94); top of Dispatch Case (DB:44) when played covertly; Faction Resolution Grid (DB:88) when played publicly |
| `max_placement_count` | 3 in hand (1 CM-A + 2 CM-B) |
| `max_placement_ref` | Faction Hand (DB:94) |
| `movement_path` | Game initialization → Faction Hand (DB:94) : issued as fixed set (1 CM-A + 2 CM-B per faction); *Covert play:* Faction Hand (DB:94) → top of Dispatch Case (DB:44) → Arbiter Tableau (DB:30) : ARBITER resolves → removed from game; *Public play:* Faction Hand (DB:94) → Faction Resolution Grid (DB:88) : declared openly → removed from game |
| `back_design` | Neutral |
| `card_source` | Provided at initialization (fixed set: 1 CM-A + 2 CM-B per faction; no source deck) |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

**Broadcasts**

### Broadcast Card  (DB: 25)

**Design Function:** The public-facing card placed in the Situation Report Zone during Situation Report resolution. Paired with a Broadcast Effect Card held privately by ARBITER.

**Narrative Anchor:** The world does not pause for The Table. Broadcast Cards are the world breaking through — news from New Meridian and beyond: public statements, natural disasters, riots, unrest, fire, the ambient disruptions of a city under pressure. They arrive without warning and land on the table as fact, shaping the conditions under which every operation must resolve. *→ Art 00 [section TBD — PM05 02-n24].*

**Gameplay Requirements:** Must display: event name, public description legible from all player positions. Must be clearly paired with its Broadcast Effect Card.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 25 |
| `component_name` | Broadcast Card |
| `physical_form` | Standard card; displayed face-up in Situation Report Zone during active event |
| `quantity` | TBD (pre-production estimate) |
| `visibility` | Public |
| `states` | Active (in Situation Report Zone) / Resolved (in discard) |
| `faction_keyed` | No |
| `placement_surface` | Situation Report Zone (Art 01); Broadcast Deck (DB:86) and Broadcast Discard (DB:109) — both at Arbiter Tableau (DB:30), subzone TBD Art 07 |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Broadcast Deck (DB:86) → Situation Report Zone (Art 01) : Situation Report resolution; Situation Report Zone → Broadcast Discard (DB:109) : after event resolves |
| `back_design` | Neutral |
| `card_source` | Broadcast Deck (DB:86) — Arbiter Tableau (DB:30), subzone TBD Art 07 |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Broadcast Effect Card  (DB: 98)

**Design Function:** ARBITER-held companion to a Broadcast Card. Carries the mechanical effect of the Broadcast event — not revealed to players until ARBITER chooses to apply it. The silent half of the two-card Broadcast set.

**Narrative Anchor:** What the world makes of an event is not always what it appears to be. The Broadcast Effect Card is ARBITER's read on what a world event actually means for the operations at The Table — the consequence held privately until ARBITER surfaces it. *→ Art 00 [section TBD — PM05 02-n24].*

**Gameplay Requirements:** Must not be readable when face-down. Must be clearly paired with its Broadcast Card.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 98 |
| `component_name` | Broadcast Effect Card |
| `physical_form` | Standard card; obverse: broadcast effect content (printed); reverse: ARBITER-keyed back; held face-down by ARBITER |
| `quantity` | TBD, 1 per Broadcast Card (pre-production estimate) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Broadcast Effect Deck (DB:87) and Broadcast Effect Discard (DB:110) — both at Arbiter Tableau (DB:30), subzone TBD Art 07 |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Broadcast Effect Deck (DB:87) → Arbiter Tableau (DB:30) — subzone TBD Art 07 : drawn paired with Broadcast Card; Arbiter Tableau (DB:30) — subzone TBD Art 07 → Broadcast Effect Discard (DB:110) : after event resolves |
| `back_design` | ARBITER-keyed |
| `card_source` | Broadcast Effect Deck (DB:87) — Arbiter Tableau (DB:30), subzone TBD Art 07 |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---


## 10.1 Card Containers

Card containers organized by card type: source decks, discard piles, and player hands.

---

**Faction Hand**

### Faction hand  (DB: 94)

**Design Function:** The logical set of cards held by a faction behind the Faction Screen. Not a discrete physical object — the collection of all cards in active private possession.

**Narrative Anchor:** N/A — logical construct, not a physical object; narrative embedded in individual card type entries.

**Gameplay Requirements:** No additional form requirement. Privacy is enforced by the Faction Screen — card fronts must not be visible to other players. Receivable and actionable in aggregate.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 94 |
| `component_name` | Faction hand |
| `physical_form` | Not a discrete physical object — collection of cards held behind Faction Screen |
| `quantity` | N/A |
| `visibility` | Player-private |
| `states` | N/A |
| `faction_keyed` | N/A |
| `placement_surface` | N/A — behind Faction Screen |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — logical construct |
| `back_design` | N/A |
| `card_source` | N/A |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal; Corrupt |

---

**Covert Operation**

### Covert operation deck  (DB: 92)

**Design Function:** Per-faction source deck for covert operation cards.

**Narrative Anchor:** N/A — container component; narrative embedded in Covert Operation card entry.

**Gameplay Requirements:** Faction identity clearly marked. Must be distinguishable from political act deck.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 92 |
| `component_name` | Covert operation deck |
| `physical_form` | Card deck; faction identity marked on back |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Terminal (Art 08 — subzone TBD) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Faction Terminal |
| `back_design` | N/A |
| `card_source` | N/A |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Covert operation discard  (DB: 93)

**Design Function:** Per-faction discard pile for played or expired covert operation cards.

**Narrative Anchor:** N/A — container component; narrative embedded in Covert Operation card entry.

**Gameplay Requirements:** Must be physically distinct from the source deck.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 93 |
| `component_name` | Covert operation discard |
| `physical_form` | Discard pile area; held behind Faction Screen |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Terminal (Art 08 — subzone TBD) — behind Faction Screen |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Faction Terminal |
| `back_design` | N/A |
| `card_source` | N/A |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Covert Operation Card Set  (DB: 114)

**Design Function:** Full faction-specific set of Covert Operation cards from which the faction player selects their in-play deck (DB:92) at initialization.

**Narrative Anchor:** N/A — container component; narrative embedded in Covert Operation card entry.

**Gameplay Requirements:** Contains the complete faction CO card set. Used at game initialization only — player selects a subset to form DB:92; remaining cards returned to storage. Lives external to the game area during normal play. Selection mechanic TBD — Art 05.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 114 |
| `component_name` | Covert Operation Card Set |
| `physical_form` | Card deck; faction identity marked on back |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private (init only) |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | External to game area (init only) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Storage → Faction Terminal (Art 08) : at initialization for deck selection; Faction Terminal → storage : after DB:92 is built |
| `back_design` | Faction-keyed |
| `card_source` | N/A — this is the source |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

**Political Act**

### Political act deck  (DB: 90)

**Design Function:** Per-faction source deck for political act cards.

**Narrative Anchor:** N/A — container component; narrative embedded in Political Act card entry.

**Gameplay Requirements:** Faction identity clearly marked. Must be distinct from covert operation deck.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 90 |
| `component_name` | Political act deck |
| `physical_form` | Card deck; faction identity marked |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Terminal (Art 08 — subzone TBD) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Faction Terminal |
| `back_design` | N/A |
| `card_source` | N/A |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Political act discard  (DB: 91)

**Design Function:** Per-faction discard pile for played or expired political act cards.

**Narrative Anchor:** N/A — container component; narrative embedded in Political Act card entry.

**Gameplay Requirements:** Distinct from source deck.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 91 |
| `component_name` | Political act discard |
| `physical_form` | Discard pile area; held behind Faction Screen |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Terminal (Art 08 — subzone TBD) — behind Faction Screen |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Faction Terminal |
| `back_design` | N/A |
| `card_source` | N/A |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Political Act Card Set  (DB: 115)

**Design Function:** Full faction-specific set of Political Act cards from which the faction player selects their in-play deck (DB:90) at initialization.

**Narrative Anchor:** N/A — container component; narrative embedded in Political Act card entry.

**Gameplay Requirements:** Contains the complete faction PA card set. Used at game initialization only — player selects a subset to form DB:90; remaining cards returned to storage. Lives external to the game area during normal play. Selection mechanic TBD — Art 05.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 115 |
| `component_name` | Political Act Card Set |
| `physical_form` | Card deck; faction identity marked on back |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private (init only) |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | External to game area (init only) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Storage → Faction Terminal (Art 08) : at initialization for deck selection; Faction Terminal → storage : after DB:90 is built |
| `back_design` | Faction-keyed |
| `card_source` | N/A — this is the source |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

**Broadcast**

### Broadcast Deck  (DB: 86)

**Design Function:** ARBITER-held source deck for Broadcast Cards. 1 total.

**Narrative Anchor:** N/A — source deck container; narrative embedded in Broadcast Card entry.

**Gameplay Requirements:** Must be distinct from Broadcast Effect Deck. ARBITER-held.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 86 |
| `component_name` | Broadcast Deck |
| `physical_form` | Card deck |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Arbiter Tableau (DB:30) — subzone TBD Art 07 |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Arbiter Tableau (DB:30) — subzone TBD Art 07 |
| `back_design` | N/A |
| `card_source` | N/A |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Broadcast Effect Deck  (DB: 87)

**Design Function:** ARBITER-held source deck for Broadcast Effect Cards. 1 total.

**Narrative Anchor:** N/A — source deck container; narrative embedded in Broadcast Effect Card entry.

**Gameplay Requirements:** Must be distinct from Broadcast Deck. ARBITER-held.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 87 |
| `component_name` | Broadcast Effect Deck |
| `physical_form` | Card deck |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Arbiter Tableau (DB:30) — subzone TBD Art 07 |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Arbiter Tableau (DB:30) — subzone TBD Art 07 |
| `back_design` | N/A |
| `card_source` | N/A |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Broadcast Discard  (DB: 109)

**Design Function:** ARBITER-held discard pile for played Broadcast Cards. Receives cards after the associated event resolves.

**Narrative Anchor:** N/A — container component; narrative embedded in Broadcast Card entry.

**Gameplay Requirements:** ARBITER-managed. Must be distinct from Broadcast Deck.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 109 |
| `component_name` | Broadcast Discard |
| `physical_form` | Discard pile area; ARBITER-held |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Arbiter Tableau (DB:30) — subzone TBD Art 07 |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Arbiter Tableau (DB:30) — subzone TBD Art 07; receives cards from Situation Report Zone after event resolves |
| `back_design` | N/A |
| `card_source` | N/A |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Broadcast Effect Discard  (DB: 110)

**Design Function:** ARBITER-held discard pile for played Broadcast Effect Cards. Receives cards after the associated event resolves.

**Narrative Anchor:** N/A — container component; narrative embedded in Broadcast Effect Card entry.

**Gameplay Requirements:** ARBITER-managed. Must be distinct from Broadcast Effect Deck.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 110 |
| `component_name` | Broadcast Effect Discard |
| `physical_form` | Discard pile area; ARBITER-held |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Arbiter Tableau (DB:30) — subzone TBD Art 07 |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Arbiter Tableau (DB:30) — subzone TBD Art 07; receives cards from resolution workspace after event resolves |
| `back_design` | N/A |
| `card_source` | N/A |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

**Init-Only Decks (Variant Pools)**

Init-only decks that live external to the game area. Used at initialization only — faction player selects or draws one card from the deck; remaining variants returned to storage.

### Operative Pool  (DB: 116)

**Design Function:** Full set of Operative card variants for a faction. Faction player selects or draws one at initialization to assign their operative for the arc.

**Narrative Anchor:** N/A — container component; narrative embedded in Operative card entry (DB:15).

**Gameplay Requirements:** Multiple variants per faction; one selected at initialization (selection mechanic TBD — Art 05); remaining variants returned to storage. External to game area during play.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 116 |
| `component_name` | Operative Pool |
| `physical_form` | TBD — Art 11 |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private (init only) |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | External to game area (init only) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Storage → Faction Terminal (Art 08) : at initialization; Faction Terminal → storage : after operative selected |
| `back_design` | Faction-keyed and operative-keyed |
| `card_source` | N/A — this is the source |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal; Corrupt |

---

### Classified Directives Pool  (DB: 118)

**Design Function:** Full set of Classified Directive variants for a faction, keyed by operative. Faction player selects or draws one at initialization matched to their chosen operative.

**Narrative Anchor:** N/A — container component; narrative embedded in Classified Directives entry (DB:17).

**Gameplay Requirements:** Multiple directive variants per operative; one selected at initialization (selection mechanic TBD — Art 05); remaining variants returned to storage. External to game area during play.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 118 |
| `component_name` | Classified Directives Pool |
| `physical_form` | TBD — Art 11 |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private (init only) |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | External to game area (init only) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Storage → Faction Terminal (Art 08) : at initialization; Faction Terminal → storage : after directive selected |
| `back_design` | Faction-keyed and operative-keyed |
| `card_source` | N/A — this is the source |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Apex Ability Pool  (DB: 117)

**Design Function:** Full set of Sealed Apex ability variants for a faction. Faction player selects or draws one at initialization.

**Narrative Anchor:** N/A — container component; narrative embedded in Sealed Apex ability entry (DB:99).

**Gameplay Requirements:** Multiple variants per faction; one selected at initialization (selection mechanic TBD — Art 05); remaining variants returned to storage. External to game area during play.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 117 |
| `component_name` | Apex Ability Pool |
| `physical_form` | TBD — Art 11 |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private (init only) |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | External to game area (init only) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Storage → Faction Terminal (Art 08) : at initialization; Faction Terminal → storage : after Apex ability selected |
| `back_design` | Faction-keyed |
| `card_source` | N/A — this is the source |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

**Modifier**

### Ring 1 modifier deck  (DB: 53) · Ring 2 modifier deck  (DB: 54) · Ring 3 modifier deck  (DB: 55)

**Design Function:** Three shared modifier card decks, each keyed to a city ring (Baryo / The Mid / Core). Drawn during Debrief to apply ring-keyed modifiers to covert operations. Shared across factions — not faction-specific.

**Narrative Anchor:** N/A — shared mechanical decks; narrative context embedded in district ring system (Art 01) and modifier card designs (Art 04 §11).

**Gameplay Requirements:** Each deck must clearly display its ring designation. Must be distinguishable from Faction modifier decks and from action card decks.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 53 · 54 · 55 |
| `component_name` | Ring 1 modifier deck · Ring 2 modifier deck · Ring 3 modifier deck |
| `physical_form` | Card decks; ring designation marked on back |
| `quantity` | 1 per ring × 3 rings = 3 total (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Central Area (Art 01) — shared modifier supply; location TBD (Art 07/08) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at shared modifier supply; individual cards drawn as needed |
| `back_design` | N/A |
| `card_source` | N/A |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

### Faction modifier deck  (DB: 89)

**Design Function:** Per-faction modifier card deck drawn during Debrief. Applies faction-specific modifiers to operations. One per faction.

**Narrative Anchor:** N/A — container component; narrative embedded in modifier card designs (Art 04 §11).

**Gameplay Requirements:** Faction identity clearly marked. Must be distinguishable from Ring modifier decks.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 89 |
| `component_name` | Faction modifier deck |
| `physical_form` | Card deck; faction-keyed back |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Player-private |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Faction Terminal (Art 08 — subzone TBD) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Faction Terminal; individual cards drawn as needed |
| `back_design` | N/A |
| `card_source` | N/A |
| `applicable_verbs` | Add; Remove; Move; Reveal; Conceal |

---

## 11. Resolution Tools

Instruments used to measure, flag, and resolve actions — threshold sliders, visibility/boost markers, and modifier tokens.

---

### Visibility Marker (VM-xx)  (DB: 103)

**Design Function:** ARBITER-held token marking that an associated covert operation resolves publicly.

**Narrative Anchor:** N/A — resolution state marker; operational instrument with no player-facing narrative identity.

**Gameplay Requirements:** Must be clearly distinguishable from Boost Marker. Placed by ARBITER on the target operation card in the ARBITER Covert Resolution Grid (DB: 105) when public resolution is triggered (e.g., C28 Breaking News success). Presence requires public announcement before Beat 3 Step 2, visible dice roll at Step 5, announced result at Step 6, and removal at Step 8. ARBITER-managed.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 103 |
| `component_name` | Visibility Marker (VM-xx) |
| `physical_form` | Token; uniform — both faces identical; TBD — Art 11 |
| `quantity` | TBD (pre-production estimate) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Arbiter Tableau (DB: 30) — resolution workspace subzone / ARBITER Covert Resolution Grid (DB: 105) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Arbiter Tableau (DB: 30) → Arbiter Tableau (DB: 30) — resolution workspace subzone → ARBITER Covert Resolution Grid (DB: 105) : placed on target operation card when public resolution triggered; ARBITER Covert Resolution Grid (DB: 105) → Arbiter Tableau (DB: 30) : public resolution concludes |
| `function` | Flags that the associated operation resolves publicly; marks public vs. covert resolution state at Beat 3 |
| `scale` | N/A — binary marker (present or absent) |
| `init_value` | N/A |
| `applicable_verbs` | Add; Remove; Move |

---

### Boost Marker (BM-xx)  (DB: 104)

**Design Function:** ARBITER-held token marking an active boost declaration on a covert operation.

**Narrative Anchor:** N/A — resolution state marker; operational instrument with no player-facing narrative identity.

**Gameplay Requirements:** Must be clearly distinguishable from Visibility Marker. Placed by ARBITER on the associated submitted card in the resolution workspace when a faction declares a boost at Beat 0. Moves with the card when it is placed in the ARBITER Covert Resolution Grid (DB: 105) at Beat 2 or 3. Removed after the operation resolves. ARBITER-managed.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 104 |
| `component_name` | Boost Marker (BM-xx) |
| `physical_form` | Token; uniform — both faces identical; TBD — Art 11 |
| `quantity` | TBD (pre-production estimate) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Arbiter Tableau (DB: 30) — resolution workspace subzone / ARBITER Covert Resolution Grid (DB: 105) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Arbiter Tableau (DB: 30) → Arbiter Tableau (DB: 30) — resolution workspace subzone : placed on submitted card when faction submits boost resources; Arbiter Tableau (DB: 30) — resolution workspace subzone → ARBITER Covert Resolution Grid (DB: 105) : moves with card when placed in resolution grid; ARBITER Covert Resolution Grid (DB: 105) → Arbiter Tableau (DB: 30) : removed after operation resolves |
| `function` | Tracks that a faction has declared a boost on the associated covert operation in the current resolution cycle |
| `scale` | N/A — binary marker (present or absent) |
| `init_value` | N/A |
| `applicable_verbs` | Add; Remove; Move |

---

### Modifier token  (DB: 47)

**Design Function:** Token holding the numeric modifier value contributed by a resolved modifier card on a target covert operation during resolution.

**Narrative Anchor:** N/A — modifier effect embodiment; narrative embedded in Modifier Card entry.

**Gameplay Requirements:** Denominations 5, 10, 15. Obverse face (positive value) color-keyed green; reverse face (negative value) color-keyed red. Must be placeable on a card without obscuring card content. Starts in Arbiter Tableau. Placed by ARBITER when a modifier card resolves — modifier card exits the resolution queue, its value recorded on the token and placed on the affected card. Covert modifier resolution: placed on the affected card in the ARBITER Covert Resolution Grid (DB: 105); returned to Arbiter Tableau after covert operation resolves. PA modifier resolution: placed on the affected card in the Faction Resolution Grid (DB: 88); returned to Arbiter Tableau after PA resolves. ARBITER totals all modifier tokens on an operation to calculate cumulative threshold modification. ARBITER-managed.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 47 |
| `component_name` | Modifier token |
| `physical_form` | Token; denominations 5, 10, 15; obverse positive (green) / reverse negative (red) |
| `quantity` | TBD (pre-production estimate) |
| `visibility` | Variable — ARBITER-only during covert resolution (DB: 105); Public during PA resolution (DB: 88) |
| `states` | Obverse (positive, green) / Reverse (negative, red) — static once placed |
| `faction_keyed` | No |
| `placement_surface` | ARBITER Covert Resolution Grid (DB: 105) / Faction Resolution Grid (DB: 88) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Arbiter Tableau (DB: 30) → ARBITER Covert Resolution Grid (DB: 105) : placed on affected card when covert modifier resolves; ARBITER Covert Resolution Grid (DB: 105) → Arbiter Tableau (DB: 30) : removed after covert operation resolves \| Arbiter Tableau (DB: 30) → Faction Resolution Grid (DB: 88) : placed on affected card when PA modifier resolves; Faction Resolution Grid (DB: 88) → Arbiter Tableau (DB: 30) : removed after PA resolves |
| `function` | Accumulates modifier values on a target covert operation during resolution; ARBITER totals all tokens on the operation to calculate cumulative threshold modification |
| `scale` | N/A — value is set at transfer from modifier card; not a graduated scale |
| `init_value` | N/A |
| `applicable_verbs` | Add; Remove; Move; Flip |

---

### ARBITER Threshold Slider  (DB: 106)

**Design Function:** Calibrated 0–100 measurement instrument at ARBITER's position for setting and reading covert operation difficulty thresholds.

**Narrative Anchor:** N/A — ARBITER operational instrument; players have no knowledge of this component during play. Narrative TBD pending Art 07 design.

**Gameplay Requirements:** Must display a clear 0–100 scale readable to ARBITER at a glance. Crit success zone (1–5) highlighted green; crit fail zone (96–00) highlighted red. Must hold position when set or adjusted. ARBITER sets slider to the base threshold of the operation card at the start of each resolution instance; slider is then adjusted up or down per modifier tokens, modifier cards, and other modifier types (Art 03 §13.5). *Note: may comprise 2 sub-components — see PM05 03-n11. Physical spec: Art 07.*

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 106 |
| `component_name` | ARBITER Threshold Slider |
| `physical_form` | Slider or dial; 0–100 scale; increments of 5 (20 ticks); crit success zone 1–5 (green highlight); crit fail zone 96–00 (red highlight); permanently on Arbiter Tableau |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | N/A |
| `placement_surface` | Arbiter Tableau (DB: 30) — permanent |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — permanently at Arbiter Tableau; slider position adjusted by ARBITER during resolution |
| `function` | Set to the base threshold value of the operation card at resolution start; adjusted up or down by modifier tokens, modifier cards, and other modifier types (Art 03 §13.5) |
| `scale` | 0–100 in increments of 5 (20 ticks) |
| `init_value` | Base threshold value of the operation card being resolved (set per resolution instance) |
| `applicable_verbs` | Add; Remove; Move; Corrupt |

---

### Faction Threshold Slider  (DB: 107)

**Design Function:** Shared calibrated 0–100 measurement instrument for Political Act declaration and resolution, passed between faction players during Beat 4.

**Narrative Anchor:** N/A — shared measurement instrument; narrative TBD pending Art 07 design.

**Gameplay Requirements:** Must display a clear 0–100 scale readable to faction players at a glance. Crit success zone (1–5) highlighted green; crit fail zone (96–00) highlighted red. Must be physically passable between player positions during play. Must hold position when set or adjusted. Starts on The Overview in any open area. During Beat 4 PA resolution, the faction player with initiative takes control of the slider and sets it to the base threshold of the PA card being resolved; adjusted per modifier types (Art 03 §13.5). Passed in initiative order to each faction player for their PA resolution. Returned to The Overview after all PA resolution is complete. *Note: may comprise 2 sub-components — see PM05 03-n12.*

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 107 |
| `component_name` | Faction Threshold Slider |
| `physical_form` | Slider or dial; 0–100 scale; increments of 5 (20 ticks); crit success zone 1–5 (green highlight); crit fail zone 96–00 (red highlight) |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | The Overview (DB: 29) — open area / Player positions (in use) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | The Overview (DB: 29) → Player position : initiative player takes control at PA resolution start; Player position → Player position : passed in initiative order for each PA resolution; Player position → The Overview (DB: 29) : returned after all PA resolution complete |
| `function` | Set to the base threshold value of the PA card being resolved; adjusted up or down by modifier tokens, modifier cards, and other modifier types (Art 03 §13.5); passed in initiative order between faction players during Beat 4 |
| `scale` | 0–100 in increments of 5 (20 ticks) |
| `init_value` | Base threshold value of the PA card being resolved (set per PA declaration) |
| `applicable_verbs` | Add; Remove; Move; Corrupt |

---

### d10  (DB:119)

**Design Function:** Standard 10-sided die used as a percentile pair for threshold resolution. Two dice rolled together — one tens digit, one units digit — produce a d100 result (01–100; 00 = 100).

**Narrative Anchor:** N/A — resolution instrument; narrative embedded in covert operation resolution sequence (Art 03 §13, §13.5).

**Gameplay Requirements:** Used in pairs for all d100 threshold resolution events. Each die in a pair is a different color — which color represents units and which represents tens is agreed upon by all players at game setup and held constant for the arc. ARBITER-rolled during covert resolution; rolled at The Overview when VM-xx is present (public resolution). Minimum 1 pair required; additional pairs per simultaneous resolution count TBD (Art 03).

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 119 |
| `component_name` | d10 |
| `physical_form` | 10-sided die; numbered 0–9; each die in a pair is a different color; color spec TBD — Art 07/11 |
| `quantity` | TBD — minimum 2 (1 pair); additional pairs per simultaneous resolution count (Art 03) |
| `visibility` | Variable — ARBITER-only during covert resolution; Public during public resolution (VM-xx active) |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Arbiter Tableau (DB: 30) — resolution workspace; The Overview (DB: 29) during public resolution |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | Arbiter Tableau (DB: 30) — supply → Arbiter Tableau (DB: 30) — resolution workspace : rolled for threshold resolution; → The Overview (DB: 29) : public resolution (VM-xx active); → Arbiter Tableau (DB: 30) — supply : returned after resolution |
| `function` | Generates d100 result for threshold resolution (Art 03 §13.5); rolled as a pair — tens die + units die = 01–100 (00 = 100) |
| `scale` | 0–9 per die; pair reads 01–100 (00 = 100) |
| `init_value` | N/A — rolled fresh per resolution instance |
| `applicable_verbs` | Add; Remove; Move; Flip |

---

## 12. Tracking Systems

Markers and trackers recording game state across beats, rounds, and quarters. Status marker is ungrouped — it tracks a single cross-phase state function not captured by the three subgroups.

---

**Score**

### Public Standing  (DB: 21)

**Design Function:** Track recording New Meridian's collective public perception of each faction.

**Narrative Anchor:** Public Standing is what New Meridian thinks — the cumulative signal produced by social media, opinion polls, public commentary, art, music, graffiti. It is volatile and reactive. Public memory is short. *→ Art 00 §6.6 for full narrative.*

**Gameplay Requirements:** Fully visible to all players at all times. Position modifies d100 difficulty thresholds per band; affects voting weight at session end. Must display: 0–20 numbered scale; five named band labels (Discredited / Suspect / Neutral / Respected / Celebrated); target modifier labels beneath each band (−20 / −10 / — / +10 / +20 to target); starting position marked at 10.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 21 |
| `component_name` | Public Standing |
| `physical_form` | Laminated strip |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Public Standing Track Area (Art 01) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed in Public Standing Track Area; marker rides the strip |
| `function` | Tracks New Meridian's public perception of each faction; position modifies difficulty thresholds on d100 rolls and voting weight at session end |
| `scale` | 0–20 (five named bands: Discredited / Suspect / Neutral / Respected / Celebrated; target modifiers −20 / −10 / — / +10 / +20) |
| `init_value` | 10 |
| `applicable_verbs` | N/A — printed zone on The Overview; not a separable physical component |

---

### Standing marker  (DB: 37)

**Design Function:** Rider marker tracking a faction's current position on the Public Standing track.

**Narrative Anchor:** N/A — rider marker; narrative context embedded in Public Standing track entry.

**Gameplay Requirements:** Must remain readable on the track strip. Faction color must be unambiguous. Moved by ARBITER or the faction player whose action causes a Public Standing change.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 37 |
| `component_name` | Standing marker |
| `physical_form` | Clip or bead; faction-colored |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Public Standing strip (DB: 21) |
| `max_placement_count` | 1 |
| `max_placement_ref` | Public Standing strip (DB: 21) |
| `movement_path` | Public Standing strip position → adjacent position : changed by action that modifies Public Standing |
| `function` | Marks a faction's current Public Standing position on the track |
| `scale` | N/A — rider marker |
| `init_value` | 10 (starting position on 0–20 scale) |
| `applicable_verbs` | Add; Remove; Move |

---

### Chorus Portrait track  (DB: 50)

**Design Function:** ARBITER's private record of the Chorus's cumulative assessment of each faction's behavior across the session.

**Narrative Anchor:** The Chorus Portrait is what the Chorus observes — permanent, cumulative, and indifferent to performance or appearance. One action is enough to begin forming a pattern. The Portrait is not a score. It is a record. The same ruler; a different observer. *→ Art 00 §9.6 for full narrative.*

**Gameplay Requirements:** Single physical strip containing 5 parallel faction-keyed tracks; behind ARBITER screen — visible to ARBITER at all times. Must display: −20 to +20 numbered scale; eleven named band labels (Void / Collapsed / Fractured / Dissonant / Uncertain / Ambiguous / Observed / Legible / Coherent / Aligned / Resonant); starting position marked at 0. Band labels are canonical (proposed); band score ranges are TBD pending Art 07 Portrait design (PM05 07-13). Physical privacy solution: Art 07.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 50 |
| `component_name` | Chorus Portrait track |
| `physical_form` | Laminated strip; 5 parallel faction-keyed tracks on one physical component; behind ARBITER screen |
| `quantity` | 1 physical component (5 parallel faction tracks; registered as 5 DB components) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Arbiter Tableau (DB: 30) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed in ARBITER Tableau; marker rides the strip |
| `function` | Records the Chorus's cumulative assessment of each faction's behavior; inputs to final scoring procedure (Art 10a); ARBITER-only |
| `scale` | −20 to +20 (eleven named bands: Void · Collapsed · Fractured · Dissonant · Uncertain · Ambiguous · Observed · Legible · Coherent · Aligned · Resonant; band score ranges TBD — PM05 07-13) |
| `init_value` | 0 |
| `applicable_verbs` | N/A — printed zone on Arbiter Tableau; not a separable physical component |

---

### Portrait marker  (DB: 51)

**Design Function:** Rider marker tracking a faction's current position on the Chorus Portrait track.

**Narrative Anchor:** N/A — rider marker managed by ARBITER; narrative context embedded in Chorus Portrait track entry.

**Gameplay Requirements:** Must remain readable on the track strip. Faction color must be unambiguous. ARBITER-managed — never moved by players.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 51 |
| `component_name` | Portrait marker |
| `physical_form` | Clip or bead; faction-colored; held in ARBITER's tableau |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | ARBITER-only |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Chorus Portrait track (DB: 50) |
| `max_placement_count` | 1 |
| `max_placement_ref` | Chorus Portrait track (DB: 50) |
| `movement_path` | Chorus Portrait track position → adjacent position : ARBITER moves per Portrait field on card, Accord violation, or Apex trigger |
| `function` | Marks a faction's current Portrait position on the Chorus Portrait track |
| `scale` | N/A — rider marker |
| `init_value` | 0 (starting position on −20 to +20 scale) |
| `applicable_verbs` | Add; Remove; Move |

---

**Initiative**

### Initiative strip  (DB: 24)

**Design Function:** Ranked display holding Faction Order Markers to track faction initiative order for the current Quarter.

**Narrative Anchor:** The Initiative Strip is ARBITER's real-time ranking of each faction's operational capacity — drawn from supply chain throughput, operative response times, resource allocation speed, leadership decision latency. A faction may believe it is executing at full capacity and find itself ranked last. The ranking is not punitive. It is observational. *→ Art 00 §9 for full narrative.*

**Gameplay Requirements:** Must provide 5 clearly ranked positions (1st through 5th). Must be publicly readable from all player positions. Initiative order determines the sequence of faction actions each Month.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 24 |
| `component_name` | Initiative strip |
| `physical_form` | Laminated strip or card |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Initiative Strip Area (Art 01) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Initiative Strip Area; markers ride the strip |
| `function` | Tracks faction initiative order for the current Quarter; holds Faction Order Markers in ranked sequence; determines faction action sequence each Month |
| `scale` | 1st–5th (5 discrete ranked positions) |
| `init_value` | Set at initialization per Art 03-init §2 |
| `applicable_verbs` | N/A — printed zone on The Overview; not a separable physical component |

---

### Faction order marker  (DB: 38)

**Design Function:** Rider marker tracking a faction's current ranked position on the Initiative Strip.

**Narrative Anchor:** N/A — rider marker; narrative context embedded in Initiative Strip entry.

**Gameplay Requirements:** Faction color must be unambiguous. Must fit clearly within Initiative Strip position slots. ARBITER-managed.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 38 |
| `component_name` | Faction order marker |
| `physical_form` | Wooden block; same physical form as Structure Block (DB: 4); faction-colored |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | Yes |
| `placement_surface` | Initiative strip (DB: 24) |
| `max_placement_count` | 1 |
| `max_placement_ref` | Initiative strip (DB: 24) |
| `movement_path` | Initiative strip position → adjacent position : initiative reorder action or initiative setup |
| `function` | Marks a faction's current initiative position on the Initiative Strip |
| `scale` | N/A — rider marker |
| `init_value` | Set at initialization per Art 03-init §2 |
| `applicable_verbs` | Add; Remove; Move |

---

**Round/Quarter**

### Session Timeline  (DB: 23)

**Design Function:** Track marking the full 8-Quarter arc of the session; records the current Quarter.

**Narrative Anchor:** ARBITER is not counting down. It is counting up toward Integration — the threshold at which humanity's aggregate response to the Chorus reaches the point where the return channel opens. Quarter 8 marks that moment, whatever position the factions hold. *→ Art 00 §8 for full narrative.*

**Gameplay Requirements:** Must clearly mark 8 Quarter sections (Q1–Q8), each subdivided into 3 Month positions (M1–M3), for 24 positions total. Current Quarter and Month must both be unambiguous when pointer marker is placed.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 23 |
| `component_name` | Session Timeline |
| `physical_form` | Strip with 8 Quarter sections (Q1–Q8), each subdivided into 3 Month positions (M1–M3); 24 positions total; displayed publicly |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Session Timeline Area (Art 01) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Session Timeline Area; pointer marker advances through Month positions within each Quarter, then to next Quarter |
| `function` | Tracks the current Quarter (Q1–Q8) and Month (M1–M3) across the session; pointer advances at end of each Month |
| `scale` | Q1–Q8 × M1–M3 (24 positions: 8 quarters, 3 months each; months repeat per quarter) |
| `init_value` | Q1 M1 |
| `applicable_verbs` | N/A — printed zone on The Overview; not a separable physical component |

---

### Pointer marker  (DB: 34)

**Design Function:** Rides the Session Timeline. Marks the current Quarter.

**Narrative Anchor:** N/A — rider marker; narrative context embedded in Session Timeline entry.

**Gameplay Requirements:** Must be clearly readable at each of the 24 positions on the Session Timeline. ARBITER-managed.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 34 |
| `component_name` | Pointer marker |
| `physical_form` | Marker; uniform — both faces identical; TBD — Art 11 |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Session Timeline (DB: 23) |
| `max_placement_count` | 1 |
| `max_placement_ref` | Session Timeline (DB: 23) |
| `movement_path` | Session Timeline position M1 → M2 → M3 → next Quarter M1 : Month concludes |
| `function` | Marks the current Quarter and Month position on the Session Timeline |
| `scale` | N/A — rider marker |
| `init_value` | Q1 M1 |
| `applicable_verbs` | Add; Remove; Move |

---

### Chorus Activity Track  (DB: 31)

**Design Function:** Graduated track recording cumulative Chorus activity across the session; holds two distinct marker positions (current level and threshold line).

**Narrative Anchor:** ARBITER added this display to MIRROR's interface without being asked. No label. No unit of measurement. No explanation. The factions named it the Seismograph. Every faction has a theory. ARBITER provides no reason for the correlation. It projects the data and waits. *→ Art 00 §9.6 for full narrative.*

**Gameplay Requirements:** Must show a graduated scale readable from all player positions. Two distinct marker positions required: Activity marker (current level) and Escalation marker (escalation line). Responds to operations executed, resources concentrated, and tensions escalated. Full design pending.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 31 |
| `component_name` | Chorus Activity Track |
| `physical_form` | Graduated strip; displayed publicly |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Chorus Activity Track Area (Art 01) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — fixed at Chorus Activity Track Area |
| `function` | Records cumulative Chorus activity across the session; activity marker tracks current level; escalation marker marks the escalation line for Chorus response |
| `scale` | TBD (full design pending — Art 07) |
| `init_value` | 0 |
| `applicable_verbs` | N/A — printed zone on The Overview; not a separable physical component |

---

### Activity marker  (DB: 35)

**Design Function:** Rides the Chorus Activity Track. Marks the current activity level.

**Narrative Anchor:** N/A — rider marker; narrative context embedded in Chorus Activity Track entry.

**Gameplay Requirements:** Must be clearly distinguishable from the Escalation marker when both are on the track. ARBITER-managed.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 35 |
| `component_name` | Activity marker |
| `physical_form` | Marker; uniform — both faces identical; TBD — Art 11 |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Chorus Activity Track (DB: 31) |
| `max_placement_count` | 1 |
| `max_placement_ref` | Chorus Activity Track (DB: 31) |
| `movement_path` | Chorus Activity Track position → adjacent position : activity level changes per operations executed, resources concentrated, or tensions escalated |
| `function` | Marks the current activity level on the Chorus Activity Track |
| `scale` | N/A — rider marker |
| `init_value` | 0 |
| `applicable_verbs` | Add; Remove; Move |

---

### Escalation marker  (DB: 36)

**Design Function:** Rides the Chorus Activity Track. Marks the escalation line — the level at which Chorus activity triggers a Chorus response.

**Narrative Anchor:** N/A — rider marker; narrative context embedded in Chorus Activity Track entry.

**Gameplay Requirements:** Must be clearly distinguishable from the Activity marker when both are on the track. ARBITER-managed.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 36 |
| `component_name` | Escalation marker |
| `physical_form` | Marker; uniform — both faces identical; TBD — Art 11 |
| `quantity` | 1 (gameplay requirement) |
| `visibility` | Public |
| `states` | N/A |
| `faction_keyed` | No |
| `placement_surface` | Chorus Activity Track (DB: 31) |
| `max_placement_count` | 1 |
| `max_placement_ref` | Chorus Activity Track (DB: 31) |
| `movement_path` | N/A — set at initialization; adjusted by ARBITER per escalation events (Art 03/07) |
| `function` | Marks the escalation line on the Chorus Activity Track — the level at which activity triggers a Chorus response |
| `scale` | N/A — rider marker |
| `init_value` | 6 (default; from Art 03-init) |
| `applicable_verbs` | Add; Remove; Move |

---

### Status marker  (DB: 49)

**Design Function:** Two-state marker tracking each faction's discussion status during Quarter-end negotiation.

**Narrative Anchor:** N/A — mechanical readiness indicator; no in-world narrative element.

**Gameplay Requirements:** Two readable states required: Active (faction still in discussion) / Ready (faction done talking, ready to end Quarter). Faction player-managed — each faction player changes their own marker state.

**Metadata:**
| Field | Value |
|-------|-------|
| `db_id` | 49 |
| `component_name` | Status marker |
| `physical_form` | Two-state flip marker (Active / Ready); TBD — Art 11 |
| `quantity` | 1 per faction × 5 factions = 5 total (gameplay requirement) |
| `visibility` | Public |
| `states` | Active / Ready |
| `faction_keyed` | Yes |
| `placement_surface` | Faction position (placement TBD — Art 03/08) |
| `max_placement_count` | N/A |
| `max_placement_ref` | N/A |
| `movement_path` | N/A — state changes between Active and Ready; transitions triggered by negotiation outcome |
| `function` | Tracks each faction's binary readiness state during Quarter-end negotiation (Active = in discussion; Ready = done talking / ready to end Quarter) |
| `scale` | N/A — binary state |
| `init_value` | Active |
| `applicable_verbs` | Add; Remove; Move; Flip |

---

*Component quantity and aesthetics confirmed in Art 11 — Visual Design System. Component stubs S89 — design passes tracked in PM05 02-n01 through 02-n04.*
