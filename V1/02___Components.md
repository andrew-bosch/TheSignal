# 02 — Components
## THE SIGNAL P1 — Paper Prototype

**Version:** 2.0
**Status:** 🔄 In Progress — S90: Full scope rewrite. v1.1 content was S88 merge of 02a v1.6 + 02b v1.5.
**Depends on:** 00 — Factions, World & Narrative Context; 01 — Game Board: New Meridian
**DB Anchor:** `the_signal_db.component` — canonical component registry. Names and IDs from that registry are authoritative.
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
| [§9 Intel & Information](#9-intel--information) | Intel tokens, Accord agreements |
| [§10 Card Systems](#10-card-systems) | All card types organized by system (6 subgroups) |
| [§11 Resolution Tools](#11-resolution-tools) | Threshold sliders, visibility/boost markers, modifier tokens |
| [§12 Tracking Systems](#12-tracking-systems) | Score, Initiative, Round/Quarter trackers; Status marker |

---

## 3. Design Principles

**DB registry as completeness anchor.** Every entry corresponds to a component registered in `the_signal_db.component`. The registry defines what components exist; this document specifies what each requires.

**Per-component structure.** The standard artifact template sections — Game Purpose, Narrative Function, Rules & Constraints, Component Description, Special Conditions, Examples — are addressed per-component within §§5–12, not as standalone sections. Each entry is self-contained.

**Function over form.** Entries lead with Design Function before Physical Form. Physical requirements must be derivable from design function — this is the evaluation order.

**Scope discipline.** This document specifies what components are and what they need. How they are used → Art 03. Where they start → Art 03-init. Governing rules → Art 00a.

**Narrative as anchor, not canon.** Narrative Anchors are brief orienting frames. Art 00 is the source of all canonical narrative.

---

### Entry Rubric

| Check | Passes If |
|-------|-----------|
| **DB Registration** | Heading includes the component's `the_signal_db.component` ID |
| **Structural Consistency** | Prose block (Design Function → Narrative Anchor → Gameplay Requirements) followed by Physical Form table (Physical Form · Quantity · Visibility) |
| **Design Function** | States why the component exists and what game system it enables |
| **Narrative Anchor** | Provides brief fictional grounding; or explicitly states `N/A —` with justification per 00a §4.6 |
| **Gameplay Requirements** | Specifies text, markings, or form required; or explicitly states "None" |
| **Physical Form** | Table: specifies shape and face-states |
| **Quantity** | Table: count labeled `(gameplay requirement)` or `(pre-production estimate)` |
| **Visibility** | Table: `Public` / `Player-private` / `ARBITER-only` |
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

### Component Schema

Each component entry in §§5–12 follows this structure:

**Design Function:** [why the component exists; the game system it enables]

**Narrative Anchor:** [brief fictional grounding] — or — `N/A —` [justification per 00a §4.6]

**Gameplay Requirements:** [required text, markings, or form; or explicitly "None"]

| Physical Form | Quantity | Visibility |
|---|---|---|
| [shape and face-states] | [count] `(gameplay requirement)` or TBD `(pre-production estimate)` | `Public` / `Player-private` / `ARBITER-only` |

---

## 5. Playing Surface

Components that constitute the physical game table — shared board surfaces, player stations, screens, grids, and the abstract player agent registered for system completeness.

---

### The Overview  (DB: 29)

**Design Function:** The central game mat occupying the Central Area during play. Hosts district tiles, tracking components, the Reservoir, The Backlog, and the Situation Report Zone. The primary shared table surface.

**Narrative Anchor:** The physical table is not an abstraction of New Meridian — it is the room in the story. What MIRROR projects is not geography; it is the Security Liaison's map: accurate not to how the city was built, but to how it can be partitioned, locked down, and controlled. *→ Art 00 §8.1 for full narrative.*

**Gameplay Requirements:** Must accommodate: all 21 district tiles in their ring-zone structure; Reservoir area; Backlog area; Situation Report Zone; Broadcast Card display area; Session Timeline; Initiative Strip; Chorus Activity Track. Full layout: Art 01 §6.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Large game mat; Central Area placement | 1 (gameplay requirement) | Public |

---

### District tile  (DB: 4)

**Design Function:** Defines the zones of New Meridian where factions contest for influence. Each tile is a named district with a fixed resource type, ring classification, and district zone. The tile is the target surface for all presence, structure, and tension markers.

**Narrative Anchor:** A named district — a specific place with a specific character, held by whoever has built deep enough there to make it theirs. New Meridian's districts are each something specific. A financial corridor generates Capital. A broadcast network generates Exposure. A research installation generates Findings. What a district generates is not assigned — it is what the district does. The tile is that fact, printed. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Each tile must display: district name; grid coordinate in [ring, address] format; border color indicating native resource type; base generation value. Chorus Node tile must be visually distinct from all faction districts.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Flat tile or card; unique label per district; face-up during all play | 21 (gameplay requirement) | Public |

---

### Situation Report  (DB: 102)

**Design Function:** Physical board object in the Situation Report Zone. Hosts Broadcast Cards during play — the display surface for public global events. Analogous to a district tile in that it anchors a zone and receives cards placed on it during resolution.

**Narrative Anchor:** Situation Reports are not local events. They are global shockwaves — market collapses, atmospheric anomalies, intercepted diplomatic transmissions, mass migrations. They reach the table because New Meridian is not isolated; it is the point through which everything else is being filtered. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must provide a clear surface for Broadcast Card placement. Must be visually distinct from district tiles.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Tile or mat; face-up in Situation Report Zone during all play | 1 (gameplay requirement) | Public |

---

### Faction Terminal  (DB: 26)

**Design Function:** The player tableau behind the Faction Screen. Organizes a faction's private workspace — hand, resources, dispatch tokens, operative cards, and private tracking components.

**Narrative Anchor:** A personal interface that connects to MIRROR privately. The Terminal is where a faction holds what has not yet been committed — the inside of the room, before any decision crosses to the open side. *→ Art 00 §8.1 for full narrative.*

**Gameplay Requirements:** Must organize the following components in an accessible layout: faction hand, dispatch case, Dispatch Tokens, resource holdings, operative cards, private tracking components. Full spec: Art 08 (planned).

| Physical Form | Quantity | Visibility |
|---|---|---|
| Game mat or surface; behind Faction Screen at each player position | 1 per faction, 5 total (gameplay requirement) | Player-private |

---

### Faction screen  (DB: 27)

**Design Function:** Upright divider at each faction position. Conceals the Faction Terminal — hand, resources, and operational planning — from all other players.

**Narrative Anchor:** The boundary between the closed room and the face a faction turns toward The Table. One side holds what is being considered; the other holds what has been committed. *→ Art 00 §8.1 for full narrative.*

**Gameplay Requirements:** Must conceal the entire Faction Terminal from all other player viewpoints. Faction-labeled or faction-colored for identification.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Upright opaque divider; faction-labeled or faction-colored | 1 per faction, 5 total (gameplay requirement) | Public |

---

### Faction Resolution Grid  (DB: 88)

**Design Function:** Public-facing playing surface at each faction position. Hosts PA declarations, publicly-played CMs, and standing effects during Beat 4 PA resolution. One per faction (5 total).

**Narrative Anchor:** The face a faction turns toward The Table — where what was decided in the closed room becomes declared and visible. *→ Art 00 §8.1 for full narrative.*

**Gameplay Requirements:** Must accommodate PA declaration markers, publicly-played CM cards, and standing effect tokens during Beat 4.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Flat surface or mat at each faction position; public-facing | 1 per faction, 5 total (gameplay requirement) | Public |

---

### ARBITER screen  (DB: 28)

**Design Function:** Upright divider at ARBITER's position (P6). Conceals ARBITER's private workspace — Portrait tracks, resolution materials, and operational records.

**Narrative Anchor:** Not concealment in the way the factions use the term — the threshold of a system operating. What is behind it is ARBITER processing in full, not deliberation in progress. *→ Art 00 §9.6 for full narrative.*

**Gameplay Requirements:** Must conceal all private ARBITER materials from all faction positions. Must accommodate the Chorus Portrait tracks and resolution workspace behind it.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Upright opaque divider | 1 (gameplay requirement) | Public |

---

### Arbiter Tableau  (DB: 30)

**Design Function:** Face-up reference surface at ARBITER's position. Visible to all players. Displays ARBITER's public-facing state and reference materials — not private resolution materials.

**Narrative Anchor:** What ARBITER has chosen to surface — Portrait records, accumulated observations, the running account. Accurate. Not complete. *→ Art 00 §9.6 for full narrative.*

**Gameplay Requirements:** Must display publicly accessible reference information. Visible from all player positions. Full spec: Art 08 (planned).

| Physical Form | Quantity | Visibility |
|---|---|---|
| Game mat or surface; face-up at ARBITER position | 1 (gameplay requirement) | Public |

---

### ARBITER Covert Resolution Grid  (DB: 105)

**Design Function:** Dedicated resolution workspace at ARBITER's position. Five independent lanes provide isolated processing space for each covert submission received in a Quarter. ARBITER-only; not visible to faction players.

**Narrative Anchor:** N/A — ARBITER operational surface; players have no knowledge of this component during play. Narrative embedded in covert resolution system (Art 07; Art 00 §9.6).

**Gameplay Requirements:** Must provide 5 distinct, labeled lanes corresponding to case receipt order. Each lane must accommodate stacked cards across Beat 1, Beat 2, and Beat 3 resolution. Lane identity must be unambiguous to ARBITER during processing. *Physical spec: Art 07.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| 5-lane grid mat or surface; behind ARBITER screen | 1 (gameplay requirement) | ARBITER-only |

---

### Human player  (DB: 43)

**Design Function:** The Faction Representative seated at The Table — the physical agent who holds the faction's cards, manages its Terminal, makes its decisions, and whose choices at this deliberation become the faction's record for the session.

**Narrative Anchor:** Each faction arrives at The Table as a specific person in a specific seat. The faction's history predates them; its future may outlast them. At The Table, they are what the faction is right now. *→ Art 00 §14.1 for full narrative.*

**Gameplay Requirements:** One human player per faction position. Five faction players total, plus one player at the ARBITER position.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Human player — physically present at faction position | 5 faction players + 1 ARBITER (gameplay requirement) | Public |

---

## 6. Faction Influence

Components that represent and evaluate each faction's operational depth in districts.

---

### Presence chip  (DB: 1)

**Design Function:** Represents a faction's operational depth in a district. Chip count determines influence level (Dominant / Established / Present) and drives resource generation. The primary unit of board control.

**Narrative Anchor:** Ghost analysts embedded in research facilities, Syndicate operators running financial infrastructure, Guild engineers maintaining power systems — presence chips represent operational depth: relationships cultivated, systems maintained, people deployed. *→ Art 00 §14 for full narrative.*

**Gameplay Requirements:** Faction color must be unambiguous across all five faction colors plus ARBITER white. Must be stackable to 6 without falling.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Small flat disc; faction-colored; stackable; ARBITER uses white | 15 per faction, 75 total (gameplay requirement) | Public |

---

### Deployment marker  (DB: 2)

**Design Function:** Temporary presence placed during the Placement phase. Counts as 1 presence chip for all purposes during the Quarter placed. Converts to 1 permanent presence chip at the following Upkeep if not blocked. Two face-states distinguish active from converting.

**Narrative Anchor:** N/A — tactical state marker; narrative context embedded in Presence chip entry.

**Gameplay Requirements:** Two readable face-states required: active (face-up) and converting (face-down). Must be clearly distinguishable from a standard presence chip by size or form. Faction color must be unambiguous.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Double-sided chit; larger than presence chip; faction-colored; face-up = active / face-down = converting | TBD (pre-production estimate) | Public |

---

### Established marker  (DB: 5)

**Design Function:** Signals that a faction holds Established influence (2nd place, 2+ chips) in a district. Multiple factions can hold Established simultaneously — each places their own marker. Placed and removed by the player whose action causes the change.

**Narrative Anchor:** N/A — influence state marker; narrative context embedded in Presence chip entry.

**Gameplay Requirements:** Must be visually distinct from Dominant marker (silver vs. gold). Must be placeable on top of a presence chip stack without obscuring chip count.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Silver marker | TBD (pre-production estimate) | Public |

---

### Dominant marker  (DB: 6)

**Design Function:** Signals that a faction holds Dominant influence (1st place, 3+ chips, no tie) in a district. One per district at any time. Placed and removed by the player whose action causes the change. Not placed at the Chorus Node.

**Narrative Anchor:** When a faction reaches Dominance, MIRROR formally registers the shift — the faction now controls the traffic routing, municipal drone corridors, and utility outputs of that zone. Dominance is not occupation. It is operation. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must be visually distinct from Established marker (gold vs. silver). Form should make it obvious only one is placed per district.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Gold marker | 21 (gameplay requirement) | Public |

---

### Tension marker  (DB: 7)

**Design Function:** Marks the Contested board state — triggered when two or more factions tie for highest chip count at 3+ chips in a district. Signals that no faction can hold Dominant while the marker is present. Placed by the player whose action creates the tie; removed by the player whose action resolves it.

**Narrative Anchor:** New Meridian runs a city-wide surveillance mesh. When the system detects localized threshold breaches — acoustic signatures of violence, crowd biometric spikes, encrypted radio bursts — it flags the district on The Overview. The Tension marker is MIRROR's notation that a district's equilibrium has broken. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must read unambiguously as a board state marker — not a faction piece. Color must contrast with both presence chips and district tiles. No required text.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Neutral-colored chip; distinct from all faction colors | 6 (pre-production estimate) | Public |

---

### Structure block  (DB: 3)

**Design Function:** Represents a faction's physical facility in a district. Generates additional resources each Quarter and modifies the difficulty of actions targeting it. Requires maintained presence — removed immediately if the owning faction becomes Absent. Maximum 1 per faction per district.

**Narrative Anchor:** A Guild structure block at the Power Grid is a substation. A Syndicate structure block at the Financial Clearinghouse is a trading desk. A Ghost structure block at the Data Exchange is a signal analysis node. They generate resources because they are doing something — not because they exist on paper. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must be visually distinguishable from presence chips and markers. Faction color must be unambiguous. No required text.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Small square chit or wooden cube; faction-colored | 6 per faction, 30 total (pre-production estimate) | Public |

---

### ARBITER Dominance Marker  (DB: 42)

**Design Function:** Establishes ARBITER's permanent, constitutive presence at the Chorus Node. Placed at setup and never removed. Signals that Dominant status is structurally impossible for human factions at the Node — not prohibited by rule, made impossible by the board (8 ARBITER tokens exceed the human faction maximum of 6).

**Narrative Anchor:** N/A — constitutive setup piece; narrative embedded in Art 00 Chorus Node entry.

**Gameplay Requirements:** Must be visually distinct from all faction components. Must read as 8 presence tokens + 1 dominance marker. Fused/inseparable construction is a gameplay requirement — the piece cannot be disassembled during play.

*(Component specification: PM01 §2.08a.)*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Single fused piece: 8 ARBITER-keyed presence tokens topped by ARBITER dominance marker; inseparable | 1 (gameplay requirement) | Public |

---

## 7. Resources

Components that constitute and move the game's five-resource economic system and operational authorization.

---

### Native resource  (DB: 8)

**Design Function:** The five physical resources factions generate, hold, and spend. Each resource embodies its faction's theory of power. All factions can hold and spend any resource type; native resources are most naturally generated through affinity districts and passive generation.

**Narrative Anchor:** Resources represent each faction's theory of power made tangible. Findings accumulates and decays because intelligence must be acted on or it becomes worthless. Capital accrues because the Syndicate's financial systems are always running. Mandate flows from institutional authority exercised every day. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Each resource type must be unambiguously distinct from all other types by color and/or form. Held publicly on player tableaux except during specific phases. 30 per type is a prototype quantity — subject to Art 11 calibration.

| Resource | Faction | Proposed Form |
|----------|---------|---------------|
| Findings | Ghost | Translucent layered chips |
| Exposure | The Network | Bright sharp tokens, ray or broadcast symbol |
| Capital | The Syndicate | Metallic coins or bars |
| Capacity | The Guild | Industrial blocks or plates |
| Mandate | The Directorate | Stamped seal or insignia tokens |

| Physical Form | Quantity | Visibility |
|---|---|---|
| Five distinct token types — one per faction resource | 30 per type, 150 total (pre-production estimate) | Public |

---

### Reservoir  (DB: 32)

**Design Function:** The shared pool holding all unspent faction resources during play. Factions take resources from and return resources to the Reservoir at Upkeep and when spending. Distinct from The Backlog (which holds only Dispatch Tokens).

**Narrative Anchor:** The Reservoir is a vast pool of unallocated capital, dormant infrastructure, and political credit accumulated outside New Meridian. Drawing income at Upkeep is not creation. It is activation — converting latent potential into working assets. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must be physically distinct from The Backlog and from faction tableau resource areas. All 5 resource types must be legibly organized and accessible.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Designated area or container on The Overview; holds all 5 resource types | 1 (gameplay requirement) | Public |

---

### Dispatch token  (DB: 12)

**Design Function:** Operational authorization — the internal capacity unit that allows a faction to run a covert operation this Quarter. Not a faction resource. Does not generate through districts, accumulate across Quarters, or carry affinity. One accompanies each covert operation card submitted in a dispatch case.

**Narrative Anchor:** A Dispatch Token is the authorization that converts planned work into active production for this Quarter — the executive order that takes a theoretical project off the backlog and commits the organization to it. *→ Art 00 §14 for full narrative.*

**Gameplay Requirements:** Must be clearly distinguishable from resource tokens and from dispatch cases. No required text.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Small token or chit; neutral or faction color (TBD Art 11) | 20 total, 4 per faction per Quarter (gameplay requirement) | Player-private |

---

### Backlog  (DB: 33)

**Design Function:** Shared pool holding all unissued Dispatch Tokens. Factions draw their quarterly allocation from The Backlog at Upkeep. Distinct from the Reservoir (which holds faction resources). The public pool of operational authorization.

**Narrative Anchor:** N/A — operational pool area; narrative context embedded in Dispatch Token entry.

**Gameplay Requirements:** Must be physically distinct from the Reservoir. The Dispatch Token supply must be visible — players can observe how many tokens remain in the pool.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Designated area or container on The Overview | 1 (gameplay requirement) | Public |

---

## 8. Covert Messaging System

Components comprising the covert dispatch channel (faction submission side) and ARBITER return channel — the physical infrastructure of covert communication.

---

### Dispatch case  (DB: 44)

**Design Function:** The faction's sealed covert submission vessel each Month. Holds 4 Dispatch Packets submitted secretly before resolution. One per faction.

**Narrative Anchor:** Where a faction's committed covert operations leave the private room and enter resolution — sealed, sequenced, anonymous to everyone except the faction that sealed it. *→ Art 00 §14.5 for full narrative.*

**Gameplay Requirements:** Must be fully opaque. Must accommodate 4 Dispatch Packets simultaneously. Faction-labeled or faction-colored for identification.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Sealed envelope or small box; opaque | 1 per faction, 5 total (gameplay requirement) | Player-private |

---

### Dispatch Packet  (DB: 108)

**Design Function:** Ordered sub-container within the Dispatch Case. Each case holds 4 Dispatch Packets, numbered 1–4 by submission sequence.

**Narrative Anchor:** Four committed operations, sequenced before the case seals. What order they go in is the last decision a faction makes in private. *→ Art 00 §14.5 for full narrative.*

**Gameplay Requirements:** Must hold and group: 1 covert operation card, 1 Dispatch Token, resource tokens (variable), 1 Target Profile, Modifier Cards (variable). 4 per case, ordered 1–4. Must maintain submission sequence and keep contents grouped during case transit.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Small envelope, sleeve, or insert within Dispatch Case; ordered 1–4 per case | 4 per faction, 20 total (gameplay requirement) | Player-private |

---

### Target Profile  (DB: 48)

**Design Function:** ARBITER-held document tracking the target faction for an active covert operation in resolution. Created and managed by ARBITER during Beats 0–3; returned to ARBITER's workspace at dispatch case return.

**Narrative Anchor:** N/A — ARBITER operational tracking record; no narrative element.

**Gameplay Requirements:** Must record: submitting faction, target faction, target district, operation type. Returned to ARBITER workspace after resolution.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Document or card; ARBITER-held | Variable — 1 per active covert operation in resolution (pre-production estimate) | ARBITER-only |

---

### Notification Slip (NS-xx)  (DB: 95)

**Design Function:** ARBITER-dispatched private notification to a faction. Carries information ARBITER must convey privately — outcomes, observations, or instructions that cannot be communicated at the open table.

**Narrative Anchor:** N/A — private delivery mechanism; narrative is in the content delivered, not the slip itself.

**Gameplay Requirements:** Must accommodate handwritten content. Faction-addressed.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Slip or small card; faction-addressed | Variable — created by ARBITER as needed (pre-production estimate) | Player-private |

---

### Intel Delivery Slip (IS-xx)  (DB: 96)

**Design Function:** ARBITER-dispatched intelligence delivery to a faction. The physical mechanism by which ARBITER delivers intel content privately. Transformable — carries state that may change during the delivery process.

**Narrative Anchor:** N/A — private delivery mechanism; narrative is in the intelligence content, not the slip itself.

**Gameplay Requirements:** Must accommodate handwritten content. Faction-addressed. Must be distinguishable from Notification Slips.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Slip or small card; faction-addressed; distinguishable from Notification Slip | Variable — created by ARBITER as needed (pre-production estimate) | Player-private |

---

### DebriefActionCard  (DB: 100)

**Design Function:** Placed by ARBITER in a faction's dispatch case during resolution. Processed at Debrief start. Carries an instruction or outcome that resolves during the Debrief phase rather than at the resolution table.

**Narrative Anchor:** Some things ARBITER determines do not surface at The Table. They arrive in the return channel — placed in the case, opened at Debrief, resolved in private. *→ Art 00 §9.6 for full narrative.*

**Gameplay Requirements:** Must be distinguishable from covert operation cards and political act cards. ARBITER-placed.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Standard card; receivable; ARBITER-placed in faction dispatch case | Variable — placed by ARBITER as needed (pre-production estimate) | Player-private |

---

### SCIFRecord (SR-xx)  (DB: 101)

**Design Function:** DebriefActionCard subtype specific to Ghost's SCIF debrief process. Carries Ghost's private SCIF debrief record. Transformable — state changes during the SCIF process.

**Narrative Anchor:** N/A — Ghost-specific record; narrative embedded in Ghost faction design (Art 00) and Art 03 §11.

**Gameplay Requirements:** Must be clearly distinguishable from standard DebriefActionCard. Ghost-addressed. *Full design: Art 03 §11; Art 04 (SCIF card).*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Standard card; Ghost-specific; distinguishable from DebriefActionCard; state-transformable | Variable — created by ARBITER as needed (pre-production estimate) | Player-private |

---

## 9. Intel & Information

Components representing intelligence tokens, accords, and classified records held or exchanged by factions.

---

### Intel token  (DB: 9)

**Design Function:** Represents actionable intelligence one faction holds about another. Enables targeted actions, powers the Denounce political act, and drives a secondary economy of information running alongside the resource economy. Created by ARBITER on a successful gather action; delivered privately to the receiving faction.

**Narrative Anchor:** An Intel Token is discrete, specific, time-stamped, and targeted. Knowledge is power — but it expires, can be traded, can be bluffed about, can be disclosed strategically, and can be turned against the faction it describes. *→ Art 00 for full narrative.*

**Gameplay Requirements:** ARBITER records at creation: (1) faction the intelligence concerns, (2) Quarter gathered. Must accommodate handwritten notation. Holder may disclose at any time by any method.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Small token or chit; must accommodate handwritten notation; physical spec: Art 11 | Variable — created during play (pre-production estimate for supply) | Player-private |

---

### Accord agreement  (DB: 10)

**Design Function:** Biometric contract between two or more factions. Placed face-up in the Accord Placement Area to register the agreement in ARBITER's canonical record. The act of placement is binding. Transformable — carries state (negotiated / active / expired).

**Narrative Anchor:** Accord Documents are biometric smart-paper. When placed face-up on the scanner beds of The Overview, MIRROR reads the signatures of the parties and registers the agreement into ARBITER's canonical record. ARBITER does not negotiate terms. It records what was signed. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must display: parties to the Accord, agreed terms. Face-up placement is a gameplay requirement — the physical act of placing registers the agreement. *Full design: Art 06 §9.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Document or card; placed face-up in Accord Placement Area when active | Variable — 1 per active Accord (pre-production estimate for supply) | Public |

---

## 10. Card Systems

All card types organized by system. Faction hand and Sealed Apex ability are listed first as cross-system and unlock-gated entries that precede the subgroup structure.

---

### Faction hand  (DB: 94)

**Design Function:** The logical set of cards held by a faction behind the Faction Screen. Not a discrete physical object — it is the collection of covert operation, political act, countermeasure, and other cards in active private possession. Receivable and actionable in aggregate.

**Narrative Anchor:** N/A — logical construct, not a physical object; narrative embedded in individual card type entries.

**Gameplay Requirements:** No additional form requirement. Privacy is enforced by the Faction Screen — card fronts must not be visible to other players.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Not a discrete physical object — collection of cards held behind Faction Screen | N/A | Player-private |

---

### Sealed Apex ability  (DB: 99)

**Design Function:** Per-faction sealed card opened when a faction reaches a specific unlock condition during the session. Grants a special ability not available at session start. The unlock condition is faction-specific and known to the faction from session setup.

**Narrative Anchor:** N/A — sealed card; faction-specific narrative embedded in individual card designs (Art 04, pending).

**Gameplay Requirements:** Must be sealed in a way that prevents reading before unlock — contents private until condition is met. Physical spec: Art 11.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Sealed card; sealed at session start; opened on unlock condition | 1 per faction, 5 total (gameplay requirement) | Player-private |

---

**Covert Operations**

### Covert operation  (DB: 13)

**Design Function:** The primary covert action card. Submitted secretly in the dispatch case each Month with an accompanying Dispatch Token. Drives the Beat 0–3 resolution sequence. Receivable — ARBITER receives and manages submitted operations during resolution.

**Narrative Anchor:** N/A — card type; narrative embedded in individual card designs and Art 00 §14.

**Gameplay Requirements:** Must display: action name, target requirements, effect on success, effect on failure. Must not be readable through the dispatch case when submitted. *Full design: Art 04.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Standard card; faction back; submitted face-down; held by ARBITER during resolution | Variable per faction deck (pre-production estimate) | Player-private |

---

### Covert operation deck  (DB: 92)

**Design Function:** Per-faction source deck for covert operation cards.

**Narrative Anchor:** N/A — container component; narrative embedded in Covert Operation card entry.

**Gameplay Requirements:** Faction identity clearly marked. Must be distinguishable from political act deck. *Full design: Art 04.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Card deck; faction identity marked on back | 1 per faction, 5 total (gameplay requirement) | Player-private |

---

### Covert operation discard  (DB: 93)

**Design Function:** Per-faction discard pile for played or expired covert operation cards.

**Narrative Anchor:** N/A — container component; narrative embedded in Covert Operation card entry.

**Gameplay Requirements:** Must be physically distinct from the source deck. *Full design: Art 04.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Discard pile area; held behind Faction Screen | 1 per faction, 5 total (gameplay requirement) | Player-private |

---

### Operative card  (DB: 15)

**Design Function:** Faction-specific character card representing a named operative. Modifies covert operation outcomes based on the operative's skills and role. Transformable — carries active/exhausted state.

**Narrative Anchor:** N/A — pending Art 04 design; narrative embedded in individual operative card designs.

**Gameplay Requirements:** Must display operative name, faction, and relevant modifiers or abilities. Readable state required (active vs. exhausted). *Full design: Art 04 (pending).*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Card; two face-states: active / exhausted; TBD — Art 11 | TBD (pre-production estimate) | Player-private |

---

**Countermeasures**

### Countermeasure card  (DB: 52)

**Design Function:** Reactive card held in the faction hand and played in response to an opponent's covert submission. Modifies or blocks operation resolution. Transformable.

**Narrative Anchor:** N/A — reactive card type; narrative embedded in individual CM card designs (Art 04).

**Gameplay Requirements:** Must be clearly distinguishable from covert operation cards and political act cards by back design. *Full design: Art 04.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Standard card; faction back | Variable per faction hand (pre-production estimate) | Player-private |

---

### Emergency Response card  (DB: 97)

**Design Function:** Reactive card type played in response to a specific trigger condition during resolution. Transformable.

**Narrative Anchor:** N/A — pending Art 04 design; narrative TBD.

**Gameplay Requirements:** TBD. *Full design: Art 04.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| TBD — Art 11 | TBD (pre-production estimate) | Player-private |

---

**Political Acts**

### Political act  (DB: 14)

**Design Function:** Public action card declared openly at The Table during Phase B. Represents a faction's overt political move. Unlike covert operations, political acts require no Dispatch Token and are played face-up at declaration. Receivable — ARBITER and all factions observe.

**Narrative Anchor:** N/A — card type; narrative embedded in individual PA card designs (Art 04).

**Gameplay Requirements:** Must display: act name, cost, effect, targeting requirements. Must be distinguishable from covert operation cards by back design. *Full design: Art 04.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Standard card; distinctive back; played face-up at declaration | Variable per faction deck (pre-production estimate) | Public |

---

### Political act deck  (DB: 90)

**Design Function:** Per-faction source deck for political act cards.

**Narrative Anchor:** N/A — container component; narrative embedded in Political Act card entry.

**Gameplay Requirements:** Faction identity clearly marked. Must be distinct from covert operation deck. *Full design: Art 04.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Card deck; faction identity marked | 1 per faction, 5 total (gameplay requirement) | Player-private |

---

### Political act discard  (DB: 91)

**Design Function:** Per-faction discard pile for played or expired political act cards.

**Narrative Anchor:** N/A — container component; narrative embedded in Political Act card entry.

**Gameplay Requirements:** Distinct from source deck. *Full design: Art 04.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Discard pile area; held behind Faction Screen | 1 per faction, 5 total (gameplay requirement) | Player-private |

---

**Broadcasts**

### Broadcast Card  (DB: 25)

**Design Function:** The public-facing card placed in the Situation Report Zone during Situation Report resolution. Visible to all players. Paired with a Broadcast Effect Card held privately by ARBITER. Transformable.

**Narrative Anchor:** N/A — event card; narrative embedded in individual Broadcast Card designs and Situation Report entry.

**Gameplay Requirements:** Must display: event name, public description legible from all player positions. Must be clearly paired with its Broadcast Effect Card.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Standard card; displayed face-up in Situation Report Zone during active event | TBD (pre-production estimate) | Public |

---

### Broadcast Effect Card  (DB: 98)

**Design Function:** ARBITER-held companion to a Broadcast Card. Carries the mechanical effect of the Broadcast event — not revealed to players until ARBITER chooses to apply it. The silent half of the two-card Broadcast set.

**Narrative Anchor:** N/A — ARBITER-held mechanical companion; narrative embedded in paired Broadcast Card.

**Gameplay Requirements:** Must not be readable when face-down. Must be clearly paired with its Broadcast Card.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Standard card; held face-down by ARBITER | TBD, 1 per Broadcast Card (pre-production estimate) | ARBITER-only |

---

### Broadcast Deck  (DB: 86)

**Design Function:** ARBITER-held source deck for Broadcast Cards. 1 total.

**Narrative Anchor:** N/A — source deck container; narrative embedded in Broadcast Card entry.

**Gameplay Requirements:** Must be distinct from Broadcast Effect Deck. ARBITER-held.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Card deck | 1 (gameplay requirement) | ARBITER-only |

---

### Broadcast Effect Deck  (DB: 87)

**Design Function:** ARBITER-held source deck for Broadcast Effect Cards. 1 total.

**Narrative Anchor:** N/A — source deck container; narrative embedded in Broadcast Effect Card entry.

**Gameplay Requirements:** Must be distinct from Broadcast Deck. ARBITER-held.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Card deck | 1 (gameplay requirement) | ARBITER-only |

---

**Classified Directives**

### Classified directives  (DB: 17)

**Design Function:** Faction-specific secret objective component. Carries a private directive that shapes a faction's session goals without disclosure to other players.

**Narrative Anchor:** The mission beneath all other missions — each faction's sealed interpretation of what the Chorus requires, held privately across the full arc. At session's end, the directive surfaces. *→ Art 00 §14.7 for full narrative.*

**Gameplay Requirements:** Must be fully private before disclosure. *Full design: Art 04 (pending).*

| Physical Form | Quantity | Visibility |
|---|---|---|
| TBD — Art 11 | TBD (pre-production estimate) | Player-private |

---

**Modifier**

### Modifier card  (DB: 11)

**Design Function:** Drawn from modifier decks and applied to covert operations during Debrief. Carries a modifier value that adjusts an operation's outcome. Transformable.

**Narrative Anchor:** N/A — modifier value carrier; narrative embedded in individual modifier card designs (Art 04 §11).

**Gameplay Requirements:** Must display modifier value clearly. Value range: Art 04 §11. *Full design: Art 04 §11.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Standard card; faction-neutral back; modifier value on face | TBD (pre-production estimate) | Public |

---

### Ring 1 modifier deck  (DB: 53) · Ring 2 modifier deck  (DB: 54) · Ring 3 modifier deck  (DB: 55)

**Design Function:** Three shared modifier card decks, each keyed to a city ring (Baryo / The Mid / Core). Drawn during Debrief to apply ring-keyed modifiers to covert operations. Shared across factions — not faction-specific.

**Narrative Anchor:** N/A — shared mechanical decks; narrative context embedded in district ring system (Art 01) and modifier card designs (Art 04 §11).

**Gameplay Requirements:** Each deck must clearly display its ring designation. Must be distinguishable from Faction modifier decks and from action card decks. *Full design: Art 04 §11.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Card decks; ring designation marked on back | 3 total, 1 per ring (gameplay requirement) | Public |

---

### Faction modifier deck  (DB: 89)

**Design Function:** Per-faction modifier card deck drawn during Debrief. Applies faction-specific modifiers to operations. One per faction.

**Narrative Anchor:** N/A — container component; narrative embedded in modifier card designs (Art 04 §11).

**Gameplay Requirements:** Faction identity clearly marked. Must be distinguishable from Ring modifier decks. *Full design: Art 04 §11.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Card deck; faction-keyed back | 1 per faction, 5 total (gameplay requirement) | Player-private |

---

## 11. Resolution Tools

Instruments used to measure, flag, and resolve actions — threshold sliders, visibility/boost markers, and modifier tokens.

---

### Visibility Marker (VM-xx)  (DB: 103)

**Design Function:** ARBITER-held token placed on a Beat 3 grid card to flag that the operation resolves publicly. Marks visibility state during resolution — distinguishes public from covert resolution.

**Narrative Anchor:** N/A — resolution state marker; operational instrument with no player-facing narrative identity.

**Gameplay Requirements:** Must be clearly distinguishable from Boost Marker. ARBITER-managed.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Token; TBD — Art 11 | TBD (pre-production estimate) | ARBITER-only |

---

### Boost Marker (BM-xx)  (DB: 104)

**Design Function:** ARBITER-held token tracking submitted boost declarations at Beat 0. Marks that a faction has declared a boost on a covert operation in the current resolution cycle.

**Narrative Anchor:** N/A — resolution state marker; operational instrument with no player-facing narrative identity.

**Gameplay Requirements:** Must be clearly distinguishable from Visibility Marker. ARBITER-managed.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Token; TBD — Art 11 | TBD (pre-production estimate) | ARBITER-only |

---

### Modifier token  (DB: 47)

**Design Function:** Physical modifier accumulator placed on a target covert operation during resolution. When a modifier card resolves, its value is transferred to a token on the target operation and the generating card is removed from the resolution queue. When the target operation resolves, ARBITER totals all tokens on it to calculate cumulative threshold modification.

**Narrative Anchor:** N/A — modifier effect embodiment; narrative embedded in Modifier Card entry.

**Gameplay Requirements:** Must carry a legible modifier value. Must be placeable on a card without obscuring card content. ARBITER-placed and managed during resolution.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Token; TBD — Art 11 | TBD (pre-production estimate) | Public |

---

### ARBITER Threshold Slider  (DB: 106)

**Design Function:** Measurement instrument permanently at ARBITER's position. Provides a 0–100 calibrated scale used by ARBITER during Beat 2 and Beat 3 covert operation resolution (§9.4.2.1.0). ARBITER-only — faction players do not interact with or see this component.

**Narrative Anchor:** N/A — ARBITER operational instrument; players have no knowledge of this component during play. Narrative TBD pending Art 07 design.

**Gameplay Requirements:** Must display a clear 0–100 scale readable to ARBITER at a glance. Must remain stable and not shift during play. *Note: may comprise 2 sub-components — see PM05 03-n11. Physical spec: Art 07.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Slider or dial; 0–100 scale; permanently on Arbiter Tableau | 1 (gameplay requirement) | ARBITER-only |

---

### Faction Threshold Slider  (DB: 107)

**Design Function:** Shared measurement instrument used during Beat 4 PA resolution (§9.4.3.0.0). Provides a 0–100 calibrated scale for declaring and resolving Political Acts. Passed between players in initiative order during Beat 4. 1 total — shared across all factions.

**Narrative Anchor:** N/A — shared measurement instrument; narrative TBD pending Art 07 design.

**Gameplay Requirements:** Must display a clear, readable 0–100 scale. Must be physically passable between player positions during play. *Note: may comprise 2 sub-components — see PM05 03-n12.*

| Physical Form | Quantity | Visibility |
|---|---|---|
| Slider or dial; 0–100 scale | 1 (gameplay requirement) | Public |

---

## 12. Tracking Systems

Markers and trackers recording game state across beats, rounds, and quarters. Status marker is ungrouped — it tracks a single cross-phase state function not captured by the three subgroups.

---

**Score**

### Public Standing  (DB: 21)

**Design Function:** Tracks New Meridian's collective public perception of each faction. Fully visible to all players at all times. Position modifies difficulty thresholds on all d100 rolls and affects voting weight at session end.

**Narrative Anchor:** Public Standing is what New Meridian thinks — the cumulative signal produced by social media, opinion polls, public commentary, art, music, graffiti. It is volatile and reactive. Public memory is short. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must display: 0–20 numbered scale; five named band labels (Discredited / Suspect / Neutral / Respected / Celebrated); target modifier labels beneath each band (−20 / −10 / — / +10 / +20 to target); starting position marked at 10.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Laminated strip; standing marker rides the strip | 1 per faction, 5 total (gameplay requirement) | Public |

---

### Standing marker  (DB: 37)

**Design Function:** Rides the Public Standing track. Marks a faction's current Public Standing position. Moved by the player whose action causes a change.

**Narrative Anchor:** N/A — rider marker; narrative context embedded in Public Standing track entry.

**Gameplay Requirements:** Must remain readable on the track strip. Faction color must be unambiguous.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Clip or bead; faction-colored | 1 per faction, 5 total (gameplay requirement) | Public |

---

### Chorus Portrait track  (DB: 50)

**Design Function:** ARBITER's private record of the Chorus's cumulative assessment of each faction's behavior. Identical in format to the Public Standing track but kept hidden in ARBITER's tableau. The same ruler; a different observer.

**Narrative Anchor:** The Chorus Portrait is what the Chorus observes — permanent, cumulative, and indifferent to performance or appearance. One action is enough to begin forming a pattern. The Portrait is not a score. It is a record. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must display: −20 to +20 numbered scale; eleven named band labels (Void / Collapsed / Fractured / Dissonant / Uncertain / Ambiguous / Observed / Legible / Coherent / Aligned / Resonant); starting position marked at 0. Physical privacy solution specified in Art 07.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Laminated strip; face-down in ARBITER's tableau; portrait marker rides the strip | 1 per faction, 5 total (gameplay requirement) | ARBITER-only |

---

### Portrait marker  (DB: 51)

**Design Function:** Rides the Chorus Portrait track. Marks a faction's current Portrait position. Managed by ARBITER — never moved by players.

**Narrative Anchor:** N/A — rider marker managed by ARBITER; narrative context embedded in Chorus Portrait track entry.

**Gameplay Requirements:** Must remain readable on the track strip. Faction color must be unambiguous.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Clip or bead; faction-colored; held in ARBITER's tableau | 1 per faction, 5 total (gameplay requirement) | ARBITER-only |

---

**Initiative**

### Initiative strip  (DB: 24)

**Design Function:** Tracks faction initiative order for the current Quarter. Holds Faction Order Markers in ranked sequence. Initiative order determines the sequence of faction actions each Month.

**Narrative Anchor:** The Initiative Strip is ARBITER's real-time ranking of each faction's operational capacity — drawn from supply chain throughput, operative response times, resource allocation speed, leadership decision latency. A faction may believe it is executing at full capacity and find itself ranked last. The ranking is not punitive. It is observational. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must provide 5 clearly ranked positions (1st through 5th). Must be publicly readable from all player positions.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Laminated strip or card; holds 5 Faction Order Markers | 1 (gameplay requirement) | Public |

---

### Faction order marker  (DB: 38)

**Design Function:** Placed on the Initiative Strip to mark a faction's current initiative position. 1 per faction.

**Narrative Anchor:** N/A — rider marker; narrative context embedded in Initiative Strip entry.

**Gameplay Requirements:** Faction color must be unambiguous. Must fit clearly within Initiative Strip position slots.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Faction-colored chit | 1 per faction, 5 total (gameplay requirement) | Public |

---

**Round/Quarter**

### Session Timeline  (DB: 23)

**Design Function:** Tracks the current Quarter (1–8). Visible to all players. The pointer marker rides it to mark the current Quarter. Eight positions mark the full arc of the session.

**Narrative Anchor:** ARBITER is not counting down. It is counting up toward Integration — the threshold at which humanity's aggregate response to the Chorus reaches the point where the return channel opens. Quarter 8 marks that moment, whatever position the factions hold. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must clearly mark 8 discrete positions labeled Quarter 1–8. Current Quarter must be unambiguous when pointer marker is placed.

| Physical Form | Quantity | Visibility |
|---|---|---|
| 8-position strip; displayed publicly | 1 (gameplay requirement) | Public |

---

### Pointer marker  (DB: 34)

**Design Function:** Rides the Session Timeline. Marks the current Quarter.

**Narrative Anchor:** N/A — rider marker; narrative context embedded in Session Timeline entry.

**Gameplay Requirements:** Must be clearly readable at each of the 8 positions on the Session Timeline strip.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Marker; TBD — Art 11 | 1 (gameplay requirement) | Public |

---

### Chorus Activity Track  (DB: 31)

**Design Function:** Graduated track recording cumulative Chorus activity across the session. Activity marker marks current level; Threshold marker marks the threshold line. Responds to operations executed, resources concentrated, and tensions escalated.

**Narrative Anchor:** ARBITER added this display to MIRROR's interface without being asked. No label. No unit of measurement. No explanation. The factions named it the Seismograph. Every faction has a theory. ARBITER provides no reason for the correlation. It projects the data and waits. *→ Art 00 for full narrative.*

**Gameplay Requirements:** Must show a graduated scale readable from all player positions. Two distinct marker positions required: Activity marker (current level) and Threshold marker (threshold line). Full design pending.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Graduated strip; displayed publicly; two distinct marker positions | 1 (gameplay requirement) | Public |

---

### Activity marker  (DB: 35)

**Design Function:** Rides the Chorus Activity Track. Marks the current activity level.

**Narrative Anchor:** N/A — rider marker; narrative context embedded in Chorus Activity Track entry.

**Gameplay Requirements:** Must be clearly distinguishable from the Threshold marker when both are on the track.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Marker; TBD — Art 11 | 1 (gameplay requirement) | Public |

---

### Threshold marker  (DB: 36)

**Design Function:** Rides the Chorus Activity Track. Marks the threshold line — the level at which activity triggers a Chorus response.

**Narrative Anchor:** N/A — rider marker; narrative context embedded in Chorus Activity Track entry.

**Gameplay Requirements:** Must be clearly distinguishable from the Activity marker when both are on the track.

| Physical Form | Quantity | Visibility |
|---|---|---|
| Marker; TBD — Art 11 | 1 (gameplay requirement) | Public |

---

### Status marker  (DB: 49)

**Design Function:** Tracks each faction's binary discussion state during Quarter-end negotiation. Active = faction is still in discussion; Ready = faction is done talking and ready to end the Quarter. One per faction.

**Narrative Anchor:** N/A — per-faction state marker; narrative context embedded in Quarter-end procedure (Art 03).

**Gameplay Requirements:** Two readable states required: active / ready.

| Physical Form | Quantity | Visibility |
|---|---|---|
| TBD — Art 11 | 1 per faction, 5 total (gameplay requirement) | Public |

---

*Component quantity and aesthetics confirmed in Art 11 — Visual Design System. Component stubs S89 — design passes tracked in PM05 02-n01 through 02-n04.*
