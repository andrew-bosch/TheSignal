# 03a — GAME ENGINE SPECIFICATION
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.8  
**Status:** 🔄 In Progress — Layer 1 (State Model) complete; Layer 2 (Beat Procedures) drafted  
**Last Updated:** 2026-05-18  
**Companion to:** [Artifact 03 — Round Structure & Gameplay](03___Round_Structure___Gameplay.md)  
**Depends on:** [00b — Data Architecture](00b___Data_Architecture.md)

---

## 1. Overview

Art 03a is the code-lite technical companion to Art 03. Where Art 03 describes the round structure in design language, Art 03a formalizes the same content as a runnable specification: explicit game state variables, structured beat procedures, and exhaustive decision tables.

**Purpose:** Surface edge cases invisible in prose, enable mechanical balance analysis (modifier stack mathematics), and provide the formal specification from which a digital game engine could be built without ambiguity.

**Relationship to Art 03:** Art 03a does not introduce new mechanics. Every branch and decision here is derivable from Art 03 + 00b. Conflicts between this document and Art 03 surface a genuine design problem — the inconsistency may indicate an ambiguity or gap in Art 03 that requires refinement, not simply an error in 03a.

**L108 compliance:** All tables in this artifact follow the L108 Database Translatable Data Design standard (single-typed columns, controlled vocabulary, explicit ID primary keys).

---

## 2. Index

1. Overview
2. Index
3. Scope and Layer Structure
4. Layer 1 — State Model
5. Layer 2 — Beat Procedures (Pseudocode)
6. Layer 3 — Decision Tables & Edge Case Registry
7. Modifier Stack Reference
8. Design Notes

---

## 3. Scope and Layer Structure

Art 03a is organized into three layers of increasing specificity:

| Layer | Contents | Status |
|-------|----------|--------|
| 1 | State Model — formal game state at each beat boundary, using 00b entity IDs as variable vocabulary | ✅ Draft complete — §4 |
| 2 | Beat Procedures — each beat as a structured pseudocode function (Beat_0() through Beat_5()) with explicit IF/THEN/ELSE branches, named inputs/outputs, modifier stack as summation formula, resolution check as formal inequality | ✅ Draft complete — §5 |
| 3 | Decision Tables — all branching conditions surfaced as tables; edge cases include face-down/face-up, Apex vs. non-Apex, Critical overrides, partial payment, Infrastructure scope (L107), Type B scope | 🔄 Pending content pass |

**Modifier balance analysis** (original XA-27 scope) is a derived output of Layer 2 once the modifier stack is formally expressed. It will be appended here as Layer 4 when Layer 2 is complete.

---

## 4. Layer 1 — State Model

The State Model defines every variable in the game system — its type, visibility scope, and the beat boundaries at which its value may change. Variable names follow the pattern `Domain.Field[index]`. Index variables in square brackets reference 00b entity IDs.

**Derived vs. stored:** Variables marked *Derived* are computed from other variables and must be synchronized immediately after their inputs change. They have no independent physical component — they are recalculated. Stored variables are maintained as physical components on the board or tableau.

---

### 4.0 Setup State — Pre-Quarter 1

The physical state of the game immediately after setup and before Quarter 1 Phase 1 begins. This is not a reset — Quarter 1 is the first increment from this configuration. §4.2 "Start of Quarter" applies to Quarters 2–8 (carry-forward), not Quarter 1.

**ARBITER as faction:** ARBITER (F-06) participates in the Board domain as a standard faction entry, not a special exception. At setup, F-06 holds 8 presence chips at the Chorus Node (D-22). All derived values — InfluenceLevel, ControlFlag, TensionMarker — follow normal derivation from those chips. The ARBITER Dominance Marker (Art 02a §10) is the physical component representing this placement; it replaces standard chip stacks on the board.

#### Board Domain at Setup

Presence chip placement per Art 01 §7 Starting Configuration. F-06 (ARBITER) added: 8 chips at D-22 only, 0 elsewhere.

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `Board.PresenceChips[D-xx][F-01..F-05]` | Per Art 01 §7 Starting Configuration | Art 01 §7 |
| `Board.PresenceChips[D-22][F-06]` | 8 — Chorus Node only | Art 02a §10 |
| `Board.PresenceChips[D-xx][F-06]` where D-xx ≠ D-22 | 0 | Setup |
| `Board.InfluenceLevel[D-xx][F-xx]` | Derived from PresenceChips per normal rules | Derived |
| `Board.ControlFlag[D-22]` | F-06 — derived (8 chips > F-05's 1 chip; ARBITER Dominant) | Derived |
| `Board.ControlFlag[D-xx]` where D-xx ≠ D-22 | Per Art 01 §7 Starting Level notations | Derived |
| `Board.TensionMarker[D-xx]` | False — no Contested conditions exist at setup chip counts | Derived |
| `Board.StructureBlocks[D-xx][F-xx]` | 0 — all districts, all factions | Setup |
| `Board.DeploymentMarker[F-xx][1\|2]` | {Location: Hand, Face: N/A} — all factions | Setup |

*Chorus Node at setup: F-06 = IL-01 (Dominant), F-05 = IL-03 (Present). ControlFlag = F-06. No other faction has chips there.*

#### Faction Domain at Setup

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `Faction.Resources[F-xx][RT-xx]` | ⚠ Open question — see note below | Art 00 §7, Art 01 §7 |
| `Faction.PublicStanding[F-01..F-05]` | 10 (PS-03 — Neutral) | L48 |
| `Faction.PublicStanding[F-06]` | TBD — Art 07 | Art 07 |
| `Faction.ChorusPortrait[F-xx]` | 0 — all factions | Setup |
| `Faction.StatusMarker[F-xx]` | Discussing — all factions | Setup |
| `Faction.BurstPlay[F-xx]` | False — all factions | Setup |

⚠ **Starting resources — open question:** Art 01 §7 "Starting Round 1 Income" projects income from Q1 Upkeep Step 5, calculated from setup chip placement. It is unclear whether factions begin the game with resources in hand (a setup grant before Q1 Upkeep), or at zero (receiving their first income during Q1 Upkeep Step 5 only). If the income table reflects only the Upkeep yield, starting value = 0. If it includes a pre-Upkeep starting grant, the income table values are the combined total. Requires resolution in Art 00 §7 or Art 02b.

#### Card Domain at Setup

All card types follow the same structural model: `Card.Type.Deck` is the active draw deck (selected at session setup); `Card.Type.Hand` is cards currently drawn to hand; `Card.Type.Zone` is a standing tableau area for non-deck cards. Source: Art 04 §3, §11, §12; Art 05.

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `Card.Covert.Deck[F-xx]` | 24 cards — selected from session pool (~30 available); shuffled and placed face-down on tableau | Session setup; Art 04 §3 |
| `Card.Covert.Hand[F-xx]` | [] (0) — drawn to 6 in Phase 1 Upkeep Step 6 | Phase 1 |
| `Card.Political.Deck[F-xx]` | 12 cards — selected from session pool (~20 available); shuffled and placed face-down on tableau | Session setup; Art 04 §3 |
| `Card.Political.Hand[F-xx]` | [] (0) — drawn to 3 in Phase 1 Upkeep Step 6 | Phase 1 |
| `Card.Modifier.Deck[F-xx]` | Faction modifier deck shuffled and placed face-down; applicable ring decks pre-positioned on board | Session setup; Art 04 §11 |
| `Card.Modifier.Hand[F-xx]` | [] (0) — drawn in Phase 1 Upkeep Step 6 | Phase 1 |
| `Card.Countermeasure.Zone[F-xx]` | 3 CC cards — in tableau designated area | Session setup; Art 04 |
| `Card.Pass.Hand[F-xx]` | 4 Pass cards — beside tableau, permanent, reusable every Quarter | Session setup; Art 04 §12 |
| `Card.Floor.Hand[F-xx]` | 1 Floor Act — beside tableau, always available | Session setup; Art 04 D04-13 |
| `Card.Operative.Zone[F-xx]` | Operative cards selected at session setup — in operator zone, 0 deployed | Session setup; Art 05 |

*Deck pool sizes (30 covert / select 24; 20 political / select 12) are working baselines pending validation — Art 04 A-04-01.*

#### ARBITER and System Domains at Setup

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `ARBITER.ModifierToken[M-xx]` | Provisioned by denomination — full set per Art 07 | Session setup; Art 07 |
| `ARBITER.Resources[RT-06]` | TBD — Art 07 | Art 07 |
| `Reservoir[RT-xx]` | 50 per resource type — provisioned at session start | Setup |

*Reservoir is pre-loaded with 50 of each resource type at session start. This represents the city's existing economic base and ensures sufficient supply to sustain Burst Play trades, Translation payouts, and other Reservoir draws across all 8 Quarters. Value is a working baseline pending playtest validation. Resources also enter the Reservoir through faction payments during Resolution (Beat 0 drain, Beat 4 Submit Payment). ARBITER.Resources[RT-06] is ARBITER's own operational resource — separate from the Reservoir.*

#### Quarter, Event, and Grid Domains at Setup

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `Quarter.Number` | 1 | Setup |
| `Quarter.InitiativeOrder` | Unset — established in Phase 1 Upkeep Step 2 | Phase 1 |
| `Quarter.InitiativePattern` | Unset — established in Phase 1 Upkeep Step 2 | Phase 1 |
| `Event.ActiveCards` | [] — empty | Setup |
| `Event.BroadcastCard` | None | Setup |
| `Chorus.ActivityTrack` | TBD — Art 07 | Art 07 |
| `Grid.*` | All empty — Grid instantiated at Beat 0 | Beat 0 |

---

### 4.1 State Variable Registry

#### Board Domain — public, player-maintained

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Board.PresenceChips[D-xx][F-xx]` | Integer ≥ 0 | VS-01 | Upkeep Step 4 (marker conversion); Beat 3 Step 7; Beat 4 Step 7 |
| `Board.InfluenceLevel[D-xx][F-xx]` | IL-xx | VS-01 | **Derived** — recalculated from `PresenceChips` after any chip change |
| `Board.ControlFlag[D-xx]` | F-xx \| IL-04 \| None | VS-01 | **Derived** — recalculated from `InfluenceLevel` after any chip change |
| `Board.TensionMarker[D-xx]` | Boolean | VS-01 | Upkeep Step 4; Beat 3 Step 7; Beat 4 Step 7 (when influence shifts) |
| `Board.StructureBlocks[D-xx][F-xx]` | Integer ≥ 0 | VS-01 | Beat 3 Step 7; Beat 4 Step 7 (op success — structure placement) |
| `Board.DeploymentMarker[F-xx][1\|2]` | {Location: D-xx \| Hand, Face: Converting \| Blocked \| N/A} | VS-01 | Phase 2 (placed on board); Upkeep Step 3 (Blocked face from Situation Report); Upkeep Step 4 (returned to hand); Beat 1 (Blocked face from conversion restriction); Beat 2 (Blocked face from Type A CM); Beat 3 Step 7; Beat 4 Step 7 (Blocked face from op outcome) |

*`Board.InfluenceLevel` and `Board.ControlFlag` are computed views. Physical components (Control flags, Tension markers) are player-maintained and must be synchronized immediately after every chip change.*

*ARBITER (F-06) chip placement at D-22 (8 chips) makes ARBITER's Dominant status at the Chorus Node structurally permanent — no playing faction can accumulate enough chips to surpass 8 while holding other board positions. See §4.0 for setup initialization. ARBITER Dominance Marker (Art 02a §10) is the physical representation.*

---

#### Faction Domain

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Faction.Resources[F-xx][RT-xx]` | Integer ≥ 0 | VS-02 | Upkeep Step 5 (income); Beat 0 (payment drain); Beat 3/4 failure conditions; Debrief (trades, conversion) |
| `Faction.PublicStanding[F-xx]` | Integer 0–20 | VS-01 | Upkeep Step 3 (Situation Report effect); Beat 3 Steps 8–9; Beat 4 Step 8 (failure/discovery conditions); Quarter close (natural drift, L13) |
| `Faction.ChorusPortrait[F-xx]` | Integer | VS-04 | Beat 3 Step 11 (per resolved covert operation, privately); Beat 4 Step 10 (per resolved political act, privately) |
| `Faction.StatusMarker[F-xx]` | Discussing \| Operating | VS-01 | Upkeep Step 1 (reset to Discussing) |
| `Faction.BurstPlay[F-xx]` | Boolean | VS-01 | Upkeep Step 6 (set True on trigger — persistent for remainder of session) |

---

#### Quarter Domain

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Quarter.Number` | Integer 1–8 | VS-01 | Start of each Quarter |
| `Quarter.InitiativeOrder` | Ordered list of F-xx (length 1–5) | VS-01 | Upkeep Step 2 |
| `Quarter.InitiativePattern` | IP-xx | VS-01 | Upkeep Step 2 (D10 result) |

---

#### Event Domain

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Event.ActiveCards` | List of EC-xx | VS-01 (existence); VS-04 (mechanical effects) | Upkeep Step 3 (draw new, expire old by duration) |
| `Event.BroadcastCard` | EC-xx \| None | VS-01 | Upkeep Step 3 (placed in Event Zone on The Overview) |
| `Chorus.ActivityTrack` | Integer | VS-01 | TBD — Art 07 |

*Situation Report mechanical effects (difficulty modifiers, targeting restrictions, conversion blocks) are VS-04 at point of draw. Targeting restrictions are announced publicly in Beat 1. Difficulty modifiers are applied and announced during Beat 3 Step 3 or Beat 4 Step 3.*

---

#### Card Domain

*Naming convention: `Card.Type.State[F-xx]` — Type identifies the card class; State is `Deck` (the draw pile), `Hand` (cards drawn to hand), or `Zone` (standing tableau area for non-deck cards).*

**Card.Faction attribute:** Every card entity (C-xx, P-xx) carries a `Faction` field (Art 04 §4): `All` (Common — standard cards available to every faction) or `F-xx` (Faction-Specific — exclusive to the owning faction). `Card.Covert.Deck[F-xx]` and `Card.Political.Deck[F-xx]` are built from the faction's session pool, pre-filtered to: `Card.Faction = All` (eligible for any faction) UNION `Card.Faction = F-xx` (eligible for this faction only). This constraint governs deck construction at session setup.

*ARBITER (F-06) has a distinct card set and modifier token provisioning. Variables stubbed below; full definition Art 07.*

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Card.Covert.Deck[F-xx]` | Ordered list of C-xx where C-xx.Faction ∈ {All, F-xx} | VS-02 | Session setup (deck construction); Upkeep Step 6 (top cards drawn; discard shuffled in when exhausted) |
| `Card.Covert.Hand[F-xx]` | List of C-xx | VS-02 | Upkeep Step 6 (draw to 6); Beat 3 Step 10 (returned or discarded per card text) |
| `Card.Political.Deck[F-xx]` | Ordered list of P-xx where P-xx.Faction ∈ {All, F-xx} | VS-02 | Session setup (deck construction); Upkeep Step 6 (top cards drawn; discard shuffled in when exhausted) |
| `Card.Political.Hand[F-xx]` | List of P-xx | VS-02 | Upkeep Step 6 (draw to 3); Beat 4 Step 9 (returned or discarded per card text) |
| `Card.Modifier.Deck[F-xx]` | Ordered list of MC-xx (faction deck + applicable ring decks) | VS-02 | Session setup (shuffled, placed); Upkeep Step 6 (top cards drawn); Burst Play trigger (deck removed from game) |
| `Card.Modifier.Hand[F-xx]` | List of MC-xx | VS-02 | Upkeep Step 6 (drawn by structure count + ring qualification); Beat 3/4 (discarded on use); Burst Play (all traded to Reservoir) |
| `Card.Countermeasure.Zone[F-xx]` | List of CC-xx (max 3) | VS-02 | Session setup (3 allocated); Phase 5 (deployed — each card handed to ARBITER); Beat 2 (processed, removed from game) |
| `Card.Pass.Hand[F-xx]` | Fixed list of 4 Pass | VS-01 (count); VS-02 (usage intent) | Immutable — reusable every Quarter; never discarded |
| `Card.Floor.Hand[F-xx]` | Fixed 1 Floor Act | VS-01 (count); VS-02 (usage intent) | Immutable — always beside tableau; full design Art 04 D04-13 |
| `Card.Operative.Zone[F-xx]` | List of operative cards in operator zone | VS-02 | Session setup (operative set selected); Phase 2 (deployed — card moves to board zone); TBD — Art 05 |
| `Card.ARBITER.*` | TBD — resolution materials, Apex envelopes, Chronicle cards, Emergency Response set | VS-04 | TBD — Art 07 |

---

#### ARBITER Domain

*ARBITER (F-06) holds materials that are not part of the faction card system. Modifier tokens are physical pieces in multiple denominations managed by ARBITER during Resolution. Full denomination set and physical design: Art 07.*

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `ARBITER.ModifierToken[M-xx]` | Integer ≥ 0 (quantity per denomination) | VS-04 | Session setup (provisioned by denomination); Beat 2 (M-11 placed on grid cell); Beat 3/4 (tokens placed and returned to pool per resolution step) |
| `ARBITER.Resources[RT-06]` | Integer ≥ 0 (Resolution resource — RT-06) | VS-04 | TBD — Art 07 (Translation mechanic, income source) |

*`ARBITER.Resources[RT-06]` is ARBITER's operational resource (Resolution, generated at Chorus Node). It is distinct from the Reservoir — see System Domain below.*

---

#### System Domain

*System-level state not owned by any faction. The Reservoir is the shared pool of spent faction resources, maintained on the board. It is a separate entity from ARBITER's resources.*

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Reservoir[RT-xx]` | Integer ≥ 0 per resource type | VS-01 | Session setup (pre-loaded 50 per type); Beat 0 (payment drain from dispatch cases); Beat 4 Submit Payment (political act payment drain); Debrief (Burst Play trade-in; Translation payouts) |

*Design decision: Reservoir = System entity (not F-06). ARBITER already has RT-06 (Resolution) as their own resource type, earned operationally. The Reservoir is the collective pool of all spent faction resources — a board-level pool owned by no faction. Conflating it with F-06 would mix ARBITER's operational budget with the city's resource pool. If L2 architecture treats all resource pools under a unified `Resources[Owner][RT-xx]` model, Reservoir maps to `Owner = System.Reservoir`, not `Owner = F-06`.*

*Starting value of 50 per resource type is a working baseline — sufficient to sustain Burst Play trades (modifier cards → Reservoir resources at 1:1), Translation payouts, and any other Reservoir draws across 8 Quarters. Pending playtest validation (PT-xx — to be assigned).*

---

#### Resolution Grid Domain — VS-04 during Resolution

*The Resolution Grid exists only during Beats 0–4. Built at Beat 0; cleared at Beat 5 when dispatch cases are returned.*

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Grid.Lane[F-xx].Beat2Slot` | CC-xx \| None | VS-04 | Beat 0 (built from Phase 5 countermeasures); Beat 2 (processed, removed) |
| `Grid.Lane[F-xx].Beat3Queue` | Ordered list of GridCell | VS-04 | Beat 0 (built from dispatch case); Beat 1 (cells removed — restriction blocked); Beat 2 (cells removed — CM blocked; modifier tokens added) |
| `Grid.ActiveModifierTokens` | Map of GridCell → List of M-xx | VS-04 | Beat 0 (M-06 partial payment marker attached); Beat 2 (M-11 Type B token placed); Beat 3 Step 4 (consumed in threshold calculation, returned to pool at Step 10) |
| `Grid.ProtectModifiers` | Map of GridCell → modifier value | VS-04 | Beat 2 (noted from Protect operations for Beat 3 application) |
| `Grid.ResolvedCells` | List of {GridCell × RO-xx} | VS-04 → VS-02 (after Beat 5 dispatch case return) | Beat 3 Step 10 (per resolved covert op); Beat 4 Step 9 (per resolved political act) |
| `Grid.ResolutionQueue` | Ordered list of GridCell positions | VS-04 | Beat 0 (established by case receipt order — first action per lane, then second actions per lane, repeating) |

*GridCell = {Lane: F-xx, Row: Beat2 \| Beat3[position], Card: C-xx \| CC-xx \| Pass, Face: Up \| Down, Target: D-xx \| RG-xx \| F-xx \| N/A}*

*Political acts (P-xx) are not placed in the Resolution Grid — they remain on faction tableaux after Phase 4 Declaration and are resolved in Beat 4 by the acting Faction Player. The Grid contains covert operations and countermeasure cards only.*

---

### 4.2 Beat Boundary State Snapshots

A beat boundary snapshot defines the invariants — what must be true at the exact moment each beat ends and the next begins. All **Outputs** listed for a beat must be fully applied before the next beat begins.

---

#### Start of Quarter (prior to Phase 1)

**Inputs carried forward from prior Quarter:**
- `Board.PresenceChips`, `Board.StructureBlocks` — no reset; carry forward
- `Faction.PublicStanding[F-xx]` — carry forward; natural drift already applied at prior Quarter close
- `Faction.ChorusPortrait[F-xx]` — carry forward; never resets
- `Faction.Resources[F-xx][RT-xx]` — carry forward; no reset between Quarters
- `Event.ActiveCards` — carry forward; duration decremented at prior Quarter close

**Invariants:**
- `Board.DeploymentMarker[F-xx][1|2]` = {Location: Hand, Face: N/A} for all factions — all markers returned at prior Upkeep Step 4
- `Quarter.Number` = prior + 1

*Quarter 1: initial values from §4.0 State Initialization, not carry-forward. Phase 1 Upkeep runs normally from that base.*

---

#### Phase 1 — Upkeep Complete

**Outputs:**
- `Faction.StatusMarker[F-xx]` = Discussing (all)
- `Quarter.InitiativeOrder` = established; `Quarter.InitiativePattern` = IP-xx result
- `Event.ActiveCards` = updated (new EC-xx drawn; expired EC-xx removed)
- `Event.BroadcastCard` = current EC-xx in Event Zone
- `Board.DeploymentMarker[F-xx][1|2]` = {Location: Hand, Face: N/A} — all markers returned or converted
- `Board.PresenceChips[D-xx][F-xx]` = updated for all markers that converted
- `Board.InfluenceLevel`, `Board.ControlFlag`, `Board.TensionMarker` = recalculated after conversions
- `Faction.Resources[F-xx][RT-xx]` = income collected
- `Card.Covert.Hand`, `Card.Political.Hand`, `Card.Modifier.Hand` = drawn to hand size

**Invariants:**
- No deployment markers on board — all in Hand
- `Card.Covert.Hand` count ≤ 6; `Card.Political.Hand` count ≤ 3 per faction
- Initiative order publicly announced and recorded on Initiative Strip

---

#### Phase 2 — Placement Complete

**Outputs:**
- `Board.DeploymentMarker[F-xx][1|2]` for placed markers = {Location: D-xx, Face: Converting}
- `Board.InfluenceLevel`, `Board.ControlFlag`, `Board.TensionMarker` = updated immediately after each placement (marker counts as 1 temporary presence chip)

**Invariants:**
- Each faction has placed 0–2 markers; each is on the board (Converting face) or in Hand
- All placements are valid — entry requirements per RG-xx table satisfied at time of placement
- Placement order: snake pattern in initiative order

---

#### Phase 3 — Dispatch Complete

**Outputs:**
- ARBITER Player holds all received dispatch cases, ordered left-to-right by receipt time
- `Grid.ResolutionQueue` lane assignments established by receipt order

**Invariants:**
- No additions to any case permitted after Dispatch closed
- No board, resource, or card state changes — Dispatch is a physical transmission step only

---

#### Phase 4 — Declaration Complete

**Outputs:**
- Each faction's declared political act (P-xx) or Pass card is face-up on their tableau
- Resource tokens for each declared act are stacked on the card — not yet transferred to Reservoir
- Modifier cards played alongside declared acts are face-up

**Invariants:**
- Declared political acts are fully public — card identity, target, and modifier count visible to all
- Resource tokens are with the declaring faction; payment transferred in Beat 4 Submit Payment only
- Declared acts cannot be withdrawn or modified

---

#### Phase 5 — Countermeasures Complete

**Outputs:**
- `Faction.CountermeasureHand[F-xx]` — deployed CC-xx cards transferred to ARBITER Player
- CC-xx type (Type A: District Block / Type B: Faction Defense) held by ARBITER for Beat 2

**Invariants:**
- ARBITER Player holds all deployed CC-xx cards
- Countermeasure card identities are VS-04 — not yet public

---

#### Beat 0 End — Grid Built

**Outputs:**
- `Grid.Lane[F-xx].Beat2Slot` = CC-xx cards from Phase 5 placed in Beat 2 row per lane
- `Grid.Lane[F-xx].Beat3Queue` = all covert operations placed (face-up or face-down per Payment Validation table)
- `Grid.ActiveModifierTokens` = M-06 partial payment markers attached to applicable face-up cards
- `Grid.ResolutionQueue` = established — first action per lane in receipt order, then second actions, repeating
- `Faction.Resources[F-xx][RT-xx]` = reduced by all payment drained to Reservoir

**Invariants:**
- Every submitted covert operation is in the grid with a determined face (Up or Down)
- Face-down cards: zero payment (non-Apex) or Apex payment shortfall — auto-fail at Beat 3 Step 1 with no roll
- Face-up cards: full or partial payment — partial payment marker M-06 attached where applicable
- Resources drained to Reservoir match validated payment amounts — no resource can remain with a submitted operation

---

#### Beat 1 End — Restrictions Applied

**Outputs:**
- `Grid.Lane[F-xx].Beat3Queue` = operations targeting restricted D-xx or RG-xx removed; placed in dispatch case with RO-03 (Blocked)
- `Board.DeploymentMarker[F-xx][1|2]` = markers in conversion-blocked districts or rings flipped to Blocked face
- Political acts targeting restricted D-xx or RG-xx: cancelled — card returned to faction; resource tokens returned (not spent)

**Invariants:**
- No card remaining in any Beat3Queue targets a district or ring under an active targeting restriction
- No deployment marker in a conversion-blocked district or ring shows Converting face
- Cancelled political act resource tokens are returned — not in Reservoir

---

#### Beat 2 End — Ground Shifts

**Outputs:**
- `Grid.Lane[F-xx].Beat3Queue` = operations targeting Type A-named districts removed; placed in dispatch case with RO-03 (Blocked)
- `Board.DeploymentMarker[F-xx][1|2]` = markers in Type A-named districts flipped to Blocked face
- `Grid.ActiveModifierTokens` = M-11 Type B modifier tokens (−15) placed on operations targeting defending faction's assets
- `Grid.ProtectModifiers` = Protect operation defensive modifiers noted for Beat 3 application

**Invariants:**
- No card remaining in any Beat3Queue targets a district blocked by an active Type A CC-xx card
- Resources committed to Blocked operations are not returned — spent on the attempt
- M-11 Type B tokens are on the card in the grid; they are applied during Beat 3 Step 3 modifier calculation, not here

---

#### Beat 3 End — Covert Operations Resolved

**Outputs:**
- `Board.PresenceChips[D-xx][F-xx]` = updated for all successful covert operations
- `Board.StructureBlocks[D-xx][F-xx]` = updated for all successful covert operations placing structure blocks
- `Board.InfluenceLevel`, `Board.ControlFlag`, `Board.TensionMarker` = recalculated after each chip change
- `Board.DeploymentMarker[F-xx][1|2]` = markers blocked by covert op outcomes flipped to Blocked face
- `Faction.PublicStanding[F-xx]` = updated for failure/discovery conditions
- `Faction.ChorusPortrait[F-xx]` = privately updated per Beat 3 Step 11 for each resolved operation
- `Grid.ResolvedCells` = each cell marked with RO-xx; dispatch case updated with resolution card per op
- `Card.Covert.Hand[F-xx]` = resolved cards returned to faction (per card text)
- `Grid.ActiveModifierTokens` = all tokens returned to pool

**Invariants:**
- `Grid.Lane[F-xx].Beat3Queue` is empty for all lanes — every card resolved (RO-01–RO-05) or previously removed (Beat 1/2)
- All board changes from covert resolutions are physically applied
- Portrait track updated but hidden — no faction knows their current score from this beat
- Each faction's dispatch case contains one RO-xx resolution card per submitted covert operation

---

#### Beat 4 End — Political Acts Resolved

**Outputs:**
- `Faction.Resources[F-xx][RT-xx]` = reduced by payment transferred to Reservoir (Submit Payment step)
- `Board.PresenceChips[D-xx][F-xx]` = updated for all successful political acts
- `Board.StructureBlocks[D-xx][F-xx]` = updated for all successful political acts placing structure blocks
- `Board.InfluenceLevel`, `Board.ControlFlag`, `Board.TensionMarker` = recalculated after each chip change
- `Board.DeploymentMarker[F-xx][1|2]` = markers blocked by political act outcomes flipped to Blocked face
- `Faction.PublicStanding[F-xx]` = updated for failure/discovery conditions
- `Faction.ChorusPortrait[F-xx]` = privately updated per Beat 4 Step 10

**Invariants:**
- All political act payments transferred to Reservoir — or partial payment marker attached — or card flipped face-down (zero payment, auto-fail)
- All board changes from political act resolutions are physically applied
- Portrait track privately updated for all political act resolutions

---

#### Beat 5 End — Table Speaks

**Outputs:**
- Dispatch cases returned to faction owners
- `Grid.ResolvedCells` outcomes (RO-xx per operation) visible to each faction via their dispatch case
- ARBITER Player's Quarter-level notes recorded for Debrief

**Invariants:**
- Each faction knows the outcome of their own covert operations — private to that faction until voluntarily shared
- No board state changes occur in Beat 5
- Resolution Grid cleared — all Grid domain variables reset to empty state

---

#### Debrief End — Quarter Closed

**Outputs:**
- `Faction.Resources[F-xx][RT-xx]` = updated for any trades or resource conversion conducted during Debrief
- `Event.ActiveCards` = duration decremented; expired cards moved to ARBITER tableau expired area
- `Faction.PublicStanding[F-xx]` = natural drift applied at Quarter close for factions above 13 or below 7 (L13)
- Findings decay check applied for F-01 (Ghost) per Art 03 §15

**Invariants:**
- All trades completed; all Accord proposals resolved (accepted, declined, or countered)
- All State Model variables in clean end-of-Quarter state — ready for `Quarter.Number++`
- `Grid` domain variables are all empty — no Resolution Grid state carries between Quarters

---

## 5. Layer 2 — Beat Procedures (Pseudocode)

Each beat is expressed as a structured procedure with explicit branching, named state mutations, and — for Beats 3 and 4 — the modifier stack as a summation formula and the resolution check as a formal inequality. Procedures use the State Variable vocabulary from §4 and modifier IDs from §7.

**Notation:**
- `←` assigns to a state variable; `+=` appends to a list or increments
- `M-xx.value` is the Threshold Adjustment from §7 (positive = threshold raised = easier; negative = harder)
- `D100()` is a uniform random integer 01–100
- `DT-xx` defers branching detail to Layer 3 (§6)
- `DESIGN FINDING [DF-xx]` marks an inconsistency surfaced by formalization — requires investigation

---

### Beat_0 — The Cases Open

```
Beat_0(
  dispatch_cases: Map[F-xx → DispatchCase],
  countermeasures: Map[F-xx → CC-xx | None]
) → Grid (built)

PRECONDITIONS:
  Phase 3 Dispatch closed — no additions permitted to any dispatch case
  Phase 4 political acts declared — face-up on faction tableaux
  Phase 5 countermeasures transferred to ARBITER Player

PROCEDURE:

// Step 1 — Build countermeasure row (Beat 2)
FOR EACH faction f ∈ Faction.All:
  Grid.Lane[f].Beat2Slot ← countermeasures[f]  // CC-xx or None

// Step 2 — Lane assignment and payment validation (DT-01, DT-02)
FOR EACH dispatch_case IN dispatch_cases (in case receipt order, Lane 1 → Lane n):
  lane ← dispatch_case.Faction
  FOR EACH operation_packet IN dispatch_case (in submission order):
    card ← operation_packet.ActionCard
    actual_payment ← resources enclosed with card in packet
    card_cost ← base cost printed on card
    IF card = Pass:
      APPEND Pass → Grid.Lane[lane].Beat3Queue  // No payment; no drain
    ELSE IF card.CardType = Beat2:
      Grid.Lane[lane].Beat2Slot ← card  // Faction-submitted CC-xx
      DRAIN actual_payment → Reservoir
    ELSE:  // Beat3 covert operation
      IF card.IsApex:  // DT-02 — Apex payment rule
        card.Face ← IF actual_payment ≥ card_cost THEN Up ELSE Down
        DRAIN actual_payment → Reservoir  // Any shortfall: drain what was submitted, no refund
      ELSE:  // Non-Apex — DT-01
        IF actual_payment = 0:
          card.Face ← Down; // Nothing to drain
        ELSE IF actual_payment = card_cost:
          card.Face ← Up
          DRAIN actual_payment → Reservoir
        ELSE:  // 0 < actual_payment < card_cost — partial payment
          card.Face ← Up
          DRAIN actual_payment → Reservoir
          Grid.ActiveModifierTokens[card.ID] += [M-06]
          // M-06 (−50 threshold) applied in Beat_3 Step 3, not here
      APPEND card → Grid.Lane[lane].Beat3Queue

// Step 3 — Establish Resolution Queue
// One card per lane per pass, in lane receipt order; lanes exhausted mid-pass are skipped
Grid.ResolutionQueue ←
  PASS 1: first card from Lane 1, Lane 2, ..., Lane n (in receipt order)
  PASS 2: second card from Lane 1, Lane 2, ..., Lane n
  REPEAT until all Beat3Queue positions assigned

STATE MUTATIONS:
  Grid.Lane[F-xx].Beat2Slot ← built
  Grid.Lane[F-xx].Beat3Queue ← built (face-up or face-down per payment validation)
  Grid.ActiveModifierTokens ← M-06 on partial-payment covert ops
  Grid.ResolutionQueue ← established
  Faction.Resources[F-xx][RT-xx] ← reduced by all validated payments
```

---

### Beat_1 — Check Active Restrictions

```
Beat_1(event_cards: Event.ActiveCards) → Grid, Board

PRECONDITIONS:
  Beat_0 complete — Grid fully built
  Event.ActiveCards = current active Situation Reports (set in Phase 1 Upkeep)

PROCEDURE:

// Step 1 — Announce all active Situation Report effects aloud
restrictions ← targeting restriction effects from Event.ActiveCards
conversion_blocks ← conversion-blocking effects from Event.ActiveCards

// Step 2 — Remove restricted covert operations
FOR EACH restriction r ∈ restrictions:
  FOR EACH lane ∈ Grid.Lanes:
    FOR EACH cell ∈ Grid.Lane[lane].Beat3Queue:
      IF cell.Target ∈ r.RestrictedDistricts OR cell.Target ∈ r.RestrictedRings:
        REMOVE cell from Grid.Lane[lane].Beat3Queue
        INSERT {cell.ID, RO-03} → Grid.ResolvedCells
        PLACE operation card + target slip → dispatch_case[lane.Faction]
        PLACE Operation Blocked resolution card → dispatch_case[lane.Faction]
        DISCARD modifier cards from cell — removed from game
        // No resource refund — resources were drained at Beat 0

DESIGN FINDING [DF-01]:
  Art 03 Beat 1 specifies "Operation Failed" resolution card for covert operations removed
  by targeting restrictions. Art 03 Beat 2 specifies "Operation Blocked" for Type A CC-xx
  removals. Both map to RO-03 (Blocked) per 00b §5.2. The label discrepancy ("Failed" vs.
  "Blocked") is inconsistent — both are pre-resolution cancellations, not failure outcomes.
  This specification uses "Operation Blocked" for both. Art 03 §12 may require amendment.

// Step 3 — Cancel restricted political acts
FOR EACH restriction r ∈ restrictions:
  FOR EACH faction f ∈ Faction.All:
    IF Faction.DeclaredAct[f].Target ∈ r.RestrictedDistricts:
      ARBITER announces restriction
      RETURN political act card → Faction Player  // Cancelled — not resolved
      RETURN resource tokens → Faction Player  // NOT transferred to Reservoir
      DISCARD modifier cards — removed from game
      // No RO-xx entry — political act was cancelled before entering resolution

// Step 4 — Apply conversion blocks
FOR EACH block b ∈ conversion_blocks:
  FOR EACH faction f ∈ Faction.All:
    FOR EACH slot ∈ [1, 2]:
      IF Board.DeploymentMarker[f][slot].Location ∈ b.BlockedDistricts
         OR Board.DeploymentMarker[f][slot].Location ∈ b.BlockedRings:
        Board.DeploymentMarker[f][slot].Face ← Blocked

STATE MUTATIONS:
  Grid.Lane[F-xx].Beat3Queue ← restriction removals
  Grid.ResolvedCells ← RO-03 entries for restricted covert ops
  Board.DeploymentMarker[F-xx][1|2].Face ← Blocked (conversion-blocked districts/rings)
```

---

### Beat_2 — The Ground Shifts

```
Beat_2() → Grid, Board

PRECONDITIONS:
  Beat_1 complete — restriction sweep applied

PROCEDURE:

// Step 1 — Type A Countermeasure cards (District Block)
FOR EACH lane ∈ Grid.Lanes WHERE Grid.Lane[lane].Beat2Slot.Type = TypeA:
  named_district ← Grid.Lane[lane].Beat2Slot.NamedDistrict
  FOR EACH target_lane ∈ Grid.Lanes:
    FOR EACH cell ∈ Grid.Lane[target_lane].Beat3Queue:
      IF cell.Target = named_district:
        REMOVE cell from Grid.Lane[target_lane].Beat3Queue
        INSERT {cell.ID, RO-03} → Grid.ResolvedCells
        PLACE operation card + target slip → dispatch_case[target_lane.Faction]
        PLACE Operation Blocked resolution card → dispatch_case[target_lane.Faction]
        DISCARD modifier cards — removed from game
        RETURN modifier tokens (M-06 if attached) → pool
        // Resources committed to blocked ops are NOT refunded — attempt was made
  FOR EACH faction f ∈ Faction.All:
    FOR EACH slot ∈ [1, 2]:
      IF Board.DeploymentMarker[f][slot].Location = named_district:
        Board.DeploymentMarker[f][slot].Face ← Blocked

// Step 2 — Type B Countermeasure cards (Faction Defense)
FOR EACH lane ∈ Grid.Lanes WHERE Grid.Lane[lane].Beat2Slot.Type = TypeB:
  defending_faction ← Grid.Lane[lane].Beat2Slot.DefendingFaction
  FOR EACH target_lane ∈ Grid.Lanes WHERE target_lane.Faction ≠ defending_faction:
    FOR EACH cell ∈ Grid.Lane[target_lane].Beat3Queue:
      IF cell.Target ∈ defending_faction.Assets:
        Grid.ActiveModifierTokens[cell.ID] += [M-11]
        // M-11 (−15 threshold) applied in Beat_3 Step 3, not here

// Step 3 — Protect operations
FOR EACH lane ∈ Grid.Lanes:
  FOR EACH cell ∈ Grid.Lane[lane].Beat3Queue:
    IF cell.Card.OperationType = Protect:
      Grid.ProtectModifiers[cell.Target] ← cell.Card.DefensiveModifier
      // Applied to opposing covert ops targeting this district in Beat_3 Step 3

// Step 4 — Clear Beat 2 row
FOR EACH lane ∈ Grid.Lanes:
  Grid.Lane[lane].Beat2Slot ← None  // CC-xx cards processed; removed from game

STATE MUTATIONS:
  Grid.Lane[F-xx].Beat3Queue ← Type A removals
  Grid.ResolvedCells ← RO-03 entries for Type A blocked ops
  Grid.ActiveModifierTokens ← M-11 tokens on Type B targeted ops
  Grid.ProtectModifiers ← Protect defensive modifier values
  Grid.Lane[F-xx].Beat2Slot ← cleared
  Board.DeploymentMarker[F-xx][1|2].Face ← Blocked (Type A named district)
```

---

### Beat_3 — Covert Operations Resolve

```
Beat_3() → Resolved covert operations

PRECONDITIONS:
  Beat_2 complete — countermeasures processed; M-11 tokens placed; Protect modifiers noted
  Grid.ResolutionQueue established; every remaining card in Beat3Queue is a valid unblocked op

// Standing modifier helper — exactly one M-01–M-05 applies per faction per resolution
M_standing(f):
  IF Faction.PublicStanding[f] ∈ [17, 20]: RETURN +20  // M-01 Celebrated  (PS-01)
  IF Faction.PublicStanding[f] ∈ [13, 16]: RETURN +10  // M-02 Respected   (PS-02)
  IF Faction.PublicStanding[f] ∈ [ 7, 12]: RETURN   0  // M-03 Neutral      (PS-03)
  IF Faction.PublicStanding[f] ∈ [ 3,  6]: RETURN −10  // M-04 Suspect      (PS-04)
  IF Faction.PublicStanding[f] ∈ [ 0,  2]: RETURN −20  // M-05 Discredited  (PS-05)

FOR EACH position p IN Grid.ResolutionQueue (in established order):
  lane ← p.Lane
  cell ← Grid.Lane[lane].Beat3Queue[p.Index]
  f ← lane.Faction

  // Step 1 — Identify
  IF cell.Card = Pass: CONTINUE  // No resolution; advance

  IF cell.Face = Down:
    INSERT {cell.ID, RO-05} → Grid.ResolvedCells
    PLACE operation card + target slip → dispatch_case[f]
    // No resolution card for auto-fail — card returned, no roll made
    DISCARD modifier cards from stack — removed from game
    CONTINUE

  IF cell.Card.IsApex:
    // Interrupt — Apex Activation always ends the session (§16, DT-08, DT-09)
    RUN Apex_Activation(cell, f)
    // Beat_3 does not return — session ends

  // Step 2 — Base difficulty
  base_threshold ← cell.Card.BaseThreshold

  // Step 3 — Modifier stack (summation formula)
  threshold ←  base_threshold
             + M_standing(f)
             + (M-06.value  IF M-06 ∈ Grid.ActiveModifierTokens[cell.ID]   ELSE 0)  // −50 partial pmt
             + (M-09.value  IF cell.Target ∈ Grid.ProtectModifiers          ELSE 0)  // Variable; Protect
             + (M-10.value  IF Situation Report difficulty effect targets op ELSE 0)  // Variable; Event
             + (M-11.value  IF M-11 ∈ Grid.ActiveModifierTokens[cell.ID]   ELSE 0)  // −15 Type B CM
             + (M-12.value  IF cell.Target.Ring = RG-02                              // −25 Infrastructure
                               AND NOT ∃ d ∈ D-xx: d.Ring = RG-03
                                                    AND d.AdjacentTo(cell.Target)
                                                    AND Board.InfluenceLevel[d][f] ∈ {IL-01, IL-02}
                               ELSE 0)
             + Σ(card.ModifierValue FOR EACH modifier_card IN cell.ModifierCards)    // M-08; Variable

  // threshold may be ≤ 0 or ≥ 100 — no clamping; 01–05 floor and 96–00 ceiling still active
  ARBITER announces final threshold aloud — all parties know before roll

  // Step 5 — Roll
  roll ← D100()

  // Step 6 — Determine outcome (formal resolution check)
  IF roll ∈ [01, 05]:
    outcome ← RO-01  // Critical Success — always, regardless of threshold
    crit_success ← True; crit_failure ← False
  ELSE IF roll ∈ [96, 100]:
    outcome ← RO-02  // Critical Failure — always, regardless of threshold
    crit_success ← False; crit_failure ← True
  ELSE IF roll ≤ threshold:
    outcome ← RO-01  // Succeeded  (roll ∈ [06, threshold])
    crit_success ← False; crit_failure ← False
  ELSE:
    outcome ← RO-02  // Failed  (roll ∈ [threshold+1, 95])
    crit_success ← False; crit_failure ← False

  // Step 7 — Apply results
  IF outcome = RO-01:
    ARBITER directs; acting Faction Player applies:
      Board.PresenceChips[cell.Target][f] ← per card text
      Board.StructureBlocks[cell.Target][f] ← per card text
    RECALCULATE Board.InfluenceLevel[cell.Target][*]
    RECALCULATE Board.ControlFlag[cell.Target]
    RECALCULATE Board.TensionMarker[cell.Target]
    IF card text specifies conversion block:
      Board.DeploymentMarker[f][*].Face ← Blocked

  // Step 8 — Failure conditions (per card text)
  IF outcome = RO-02:
    APPLY failure conditions from card text
    Faction.PublicStanding[f] ← adjusted per card text

  // Step 9 — Discovery conditions (per card text)
  IF card text specifies discovery condition:
    IF crit_failure = True OR roll ∈ card.DiscoveryRange:
      outcome ← RO-04  // Discovered — overrides RO-02
      APPLY discovery conditions from card text

  // Step 10 — Clean up grid cell
  INSERT {cell.ID, outcome} → Grid.ResolvedCells
  PLACE operation card + target slip → dispatch_case[f]
  PLACE resolution card (Succeeded / Failed / Discovered) → dispatch_case[f]
  DISCARD modifier cards from cell — removed from game
  RETURN Grid.ActiveModifierTokens[cell.ID] → pool
  Card.Covert.Hand[f] ← per card text (return to hand or discard)

  // Step 11 — Portrait (private)
  ARBITER privately updates Faction.ChorusPortrait[f]

END FOR

STATE MUTATIONS:
  Grid.ResolvedCells ← RO-01, RO-02, RO-04, RO-05 per op
  Board.PresenceChips ← success outcomes
  Board.StructureBlocks ← success outcomes
  Board.InfluenceLevel ← recalculated (derived)
  Board.ControlFlag ← recalculated (derived)
  Board.TensionMarker ← recalculated
  Board.DeploymentMarker ← Blocked per card text
  Faction.PublicStanding ← failure/discovery conditions
  Faction.ChorusPortrait ← private, per op
  Grid.ActiveModifierTokens ← cleared (all tokens returned to pool)
  Card.Covert.Hand ← per card text
```

---

### Beat_4 — Political Acts Resolve

```
Beat_4() → Resolved political acts

PRECONDITIONS:
  Beat_3 complete — all covert operations resolved
  Each faction's declared political act (or Pass) is face-up on their tableau
  Resource tokens for each declared act are stacked on the card — not yet in Reservoir

// Submit Payment phase — initiative order
FOR EACH faction f ∈ Faction.All WITH declared political act (in Quarter.InitiativeOrder):
  act ← Faction.DeclaredAct[f]
  actual_payment ← resource tokens on act card
  card_cost ← base cost on card
  Faction Player transfers resource tokens → Reservoir
  IF actual_payment = 0:
    ARBITER announces act invalid
    act.Face ← Down  // Auto-fail when reached in resolution phase
  ELSE IF actual_payment < card_cost:
    ARBITER attaches M-07 marker to act card and announces additional difficulty
    // M-07 (−50 threshold) applied in modifier stack below

DESIGN FINDING [DF-02]:
  Art 03 Beat 4 Submit Payment describes the marker as "+50 difficulty marker." The
  modifier table (§7, Art 03 §14) lists M-06 and M-07 as Threshold Adjustment −50.
  These are equivalent but expressed with opposite signs: "+50 difficulty" (difficulty
  additive) vs. "−50" (threshold subtractive). The physical token face label and the
  table value are inverse representations of the same penalty. Art 07 (ARBITER Toolkit)
  physical token design should clarify this to prevent table play confusion.

// Resolution phase — initiative order
FOR EACH faction f ∈ Faction.All WITH declared political act (in Quarter.InitiativeOrder):
  act ← Faction.DeclaredAct[f]

  // Step 1 — Identify; Apex check
  IF act.IsApex:
    // Interrupt — Apex Activation always ends the session (§16, DT-08, DT-09)
    RUN Apex_Activation(act, f)
    // Beat_4 does not return — session ends

  IF act.Face = Down:
    INSERT {act.ID, RO-05} → Grid.ResolvedCells
    DISCARD modifier cards — removed from game
    RETURN political act card → Faction Player
    CONTINUE

  // Step 2 — Base difficulty
  base_threshold ← act.BaseThreshold

  // Steps 3-4 — Modifier stack; Faction Player calculates and declares aloud
  threshold ←  base_threshold
             + M_standing(f)
             + (M-07.value  IF M-07 attached to act                 ELSE 0)  // −50 partial pmt
             + (M-10.value  IF Situation Report effect targets act   ELSE 0)  // Variable; Event
             + (M-12.value  IF act.Target.Ring = RG-02                        // −25 Infrastructure
                               AND NOT ∃ d ∈ D-xx: d.Ring = RG-03
                                                    AND d.AdjacentTo(act.Target)
                                                    AND Board.InfluenceLevel[d][f] ∈ {IL-01, IL-02}
                               ELSE 0)
             + Σ(card.ModifierValue FOR EACH modifier_card IN act.ModifierCards)  // M-08; Variable

  // Note: M-06, M-09, M-11 do not apply to political acts
  Faction Player announces final threshold aloud

  // Step 5 — Roll (Faction Player rolls publicly)
  roll ← D100()

  // Step 6 — Determine outcome
  IF roll ∈ [01, 05]:    outcome ← RO-01  // Critical Success
  ELSE IF roll ∈ [96, 100]: outcome ← RO-02  // Critical Failure
  ELSE IF roll ≤ threshold: outcome ← RO-01  // Succeeded
  ELSE:                   outcome ← RO-02  // Failed

  // Step 7 — Apply results
  IF outcome = RO-01:
    Faction Player applies board changes:
      Board.PresenceChips[act.Target][f] ← per card text
      Board.StructureBlocks[act.Target][f] ← per card text
    RECALCULATE Board.InfluenceLevel[act.Target][*]
    RECALCULATE Board.ControlFlag[act.Target]
    RECALCULATE Board.TensionMarker[act.Target]
    IF card text specifies conversion block:
      Board.DeploymentMarker[f][*].Face ← Blocked

  // Step 8 — Failure conditions (per card text)
  IF outcome = RO-02:
    APPLY failure conditions from card text
    Faction.PublicStanding[f] ← adjusted per card text

  // Step 9 — Clean up
  Card.Political.Hand[f] ← per card text (return to hand or discard)
  DISCARD modifier cards — removed from game

  // Step 10 — Portrait (private)
  ARBITER privately updates Faction.ChorusPortrait[f]

END FOR

STATE MUTATIONS:
  Faction.Resources[F-xx][RT-xx] ← reduced (Submit Payment drain)
  Grid.ResolvedCells ← RO-01, RO-02, RO-05 per act
  Board.PresenceChips ← success outcomes
  Board.StructureBlocks ← success outcomes
  Board.InfluenceLevel ← recalculated (derived)
  Board.ControlFlag ← recalculated (derived)
  Board.TensionMarker ← recalculated
  Board.DeploymentMarker ← Blocked per card text
  Faction.PublicStanding ← failure conditions
  Faction.ChorusPortrait ← private, per act
  Card.Political.Hand ← per card text
```

---

### Beat_5 — The Table Speaks

```
Beat_5() → Quarter resolution complete

PRECONDITIONS:
  Beat_4 complete — all political acts resolved
  Grid.ResolvedCells contains RO-xx outcome for every submitted operation this Quarter

PROCEDURE:

// Step 1 — Return dispatch cases
FOR EACH faction f ∈ Faction.All:
  RETURN dispatch_case[f] → Faction Player
  // Contents: operation cards, target slips, resolution cards (RO-xx), ARBITER intel notes
  // Outcome visibility: VS-04 → VS-02 (faction-only) — each faction sees only their own ops

// Step 2 — ARBITER Quarter notes
ARBITER records Quarter-level observations (patterns, notable moments)
// Informs Debrief ARBITER statement — Art 07; Chronicle — Art 10

// Step 3 — Clear Resolution Grid
Grid.Lane[F-xx].Beat2Slot    ← None  FOR ALL f
Grid.Lane[F-xx].Beat3Queue   ← []    FOR ALL f
Grid.ActiveModifierTokens    ← {}    (empty map)
Grid.ProtectModifiers        ← {}    (empty map)
Grid.ResolvedCells           ← []    (empty list)
Grid.ResolutionQueue         ← []    (empty list)

OUTPUT:
  Faction Players hold dispatch cases — each faction's outcomes privately visible
  Resolution Grid cleared — no Grid domain state carries to next Quarter
  Debrief opens

STATE MUTATIONS:
  Grid.* ← all variables cleared to empty state
```

---

## 6. Layer 3 — Decision Tables & Edge Case Registry

*Pending content pass.*

Decision tables cover all branching points in Beats 0–5. Confirmed scope:

| Table | Branch Condition | Status |
|-------|-----------------|--------|
| DT-01 | Card orientation at Beat 0 (face-down / face-up) | 🔄 Pending |
| DT-02 | Apex card detection at Beat 0 | 🔄 Pending |
| DT-03 | Critical Success (01–05) override path | 🔄 Pending |
| DT-04 | Critical Failure (96–00) override path | 🔄 Pending |
| DT-05 | Partial payment at Beat 4 | 🔄 Pending |
| DT-06 | Infrastructure modifier scope (L107 — all action types) | 🔄 Pending |
| DT-07 | Type B card scope (Faction Player only vs. all) | 🔄 Pending |
| DT-08 | Apex activation threshold check (Step 4) | 🔄 Pending |
| DT-09 | Emergency Response — assist / thwart Apex (Board Strength delta before Step 4) | 🔄 Pending |

---

## 7. Modifier Stack Reference

Canonical source for all `M-xx.value` references in §5 Beat Procedures. L108 compliant — single-typed columns, controlled vocabulary.

**Sign convention:** Positive Threshold Adjustment = threshold raised = success more likely. Negative = threshold lowered = harder. (Source: Art 03 §14.) Physical modifier tokens may express this inversely as "+N difficulty" — see [DF-02].

| ID | Category | Modifier | Scope | Applied | Instance Limit | Value Type | Threshold Adjustment |
|----|----------|----------|-------|---------|----------------|------------|---------------------|
| M-01 | Standing | Celebrated | All | Persistent | 1 | Fixed | +20 |
| M-02 | Standing | Respected | All | Persistent | 1 | Fixed | +10 |
| M-03 | Standing | Neutral | All | Persistent | 1 | Fixed | 0 |
| M-04 | Standing | Suspect | All | Persistent | 1 | Fixed | −10 |
| M-05 | Standing | Discredited | All | Persistent | 1 | Fixed | −20 |
| M-06 | Payment | Partial payment marker | Covert | Beat 0 | 1 per submitted card | Fixed | −50 |
| M-07 | Payment | Partial payment marker | Political | Beat 4 | 1 per submitted card | Fixed | −50 |
| M-08 | Card Effect | Modifier card | All | Pre-Resolution | Unlimited | Variable | See card |
| M-09 | Card Effect | Protect / Defend operation | Covert | Beat 2 | 1 per Protect submitted | Variable | See card |
| M-10 | Situation Report | Difficulty effect | All | Beat 1 | 1 per active Event Card | Variable | See Event Card |
| M-11 | Countermeasure | Type B — target faction assets | Covert | Beat 2 | 1 per defending faction | Fixed | −15 |
| M-12 | District | Infrastructure — no adjacent Core | All | Persistent | 1 | Fixed | −25 |

*Source: Art 03 §14.*

*M-01–M-05 are mutually exclusive — exactly one Standing modifier applies per faction per resolution, derived from `Faction.PublicStanding[f]` via the `M_standing()` helper in §5.*

*M-08, M-09, M-10, M-12 variable rows are fully specified here for Fixed modifiers; variable values pending Art 04 card definitions. Balance analysis (modifier stack mathematics) is the planned Layer 4 of this artifact, blocked until all M-xx values are defined.*

**Correction note:** The §7 table in v0.2 contained values from a prior design iteration (M-01: "Critical Success −25", M-02: "Critical Failure +25", etc.) that do not match Art 03 §14. Critical Success and Critical Failure are resolution rules, not modifier stack entries. The corrected table above is authoritative. All §5 Beat Procedures reference this version.

---

## 8. Design Notes

**Source of truth:** Art 03 is the current authoritative specification. This document is a formalization layer — where 03a contradicts 03, the inconsistency must be investigated. The conflict may reflect an error in 03a's formalization, or it may surface an ambiguity, edge case, or gap in Art 03 that prose obscured. Either outcome is a design finding requiring resolution and, if necessary, refinement of Art 03.

**L2 implication:** The Beat Procedures in Layer 2 are intended to be directly translatable to a server-side game engine (L2 architecture). The TypeScript schema in Retired/Electronic/old__08_DATA_MODEL.md is the target L2 data model; 00b entity IDs should align to it.

**Modifier balance analysis:** Once all modifier rows (M-01–M-12) are fully specified, the summation formula in Beat_3() enables a full balance analysis: expected difficulty shift per modifier combination, pathological stack identification, and recommendation for modifier caps if needed.

---

### Open Design Findings (surfaced by Layer 2 formalization)

| ID | Section | Finding | Action Required |
|----|---------|---------|-----------------|
| DF-01 | Beat_1 | Art 03 Beat 1 uses "Operation Failed" resolution card for restriction removals; Beat 2 uses "Operation Blocked." Both are RO-03 (Blocked) per 00b. Label inconsistency — pre-resolution cancellations should not carry "Failed" label. | Confirm "Operation Blocked" for both; amend Art 03 §12 Beat 1 if agreed |
| DF-02 | Beat_4, §7 | Partial payment marker described as "+50 difficulty" in beat prose (Art 03 Beat 0, Beat 4) but listed as "−50" Threshold Adjustment in modifier table. Inverse representations of same penalty. Physical token label may confuse table players. | Clarify notation in Art 07 physical token design; consider aligning prose to table sign convention |

---

*End of Art 03a — Game Engine Specification v0.8*
