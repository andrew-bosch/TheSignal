# 03a — GAME ENGINE SPECIFICATION
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.2  
**Status:** 🔄 In Progress — Layer 1 (State Model) drafted  
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
| 2 | Beat Procedures — each beat as a structured pseudocode function (Beat_0() through Beat_5()) with explicit IF/THEN/ELSE branches, named inputs/outputs, modifier stack as summation formula, resolution check as formal inequality | 🔄 Pending content pass |
| 3 | Decision Tables — all branching conditions surfaced as tables; edge cases include face-down/face-up, Apex vs. non-Apex, Critical overrides, partial payment, Infrastructure scope (L107), Type B scope | 🔄 Pending content pass |

**Modifier balance analysis** (original XA-27 scope) is a derived output of Layer 2 once the modifier stack is formally expressed. It will be appended here as Layer 4 when Layer 2 is complete.

---

## 4. Layer 1 — State Model

The State Model defines every variable in the game system — its type, visibility scope, and the beat boundaries at which its value may change. Variable names follow the pattern `Domain.Field[index]`. Index variables in square brackets reference 00b entity IDs.

**Derived vs. stored:** Variables marked *Derived* are computed from other variables and must be synchronized immediately after their inputs change. They have no independent physical component — they are recalculated. Stored variables are maintained as physical components on the board or tableau.

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

*Chorus Node exception: `Board.InfluenceLevel[D-22][F-06]` = IL-01 (Dominant) at all times via ARBITER Dominance Marker — structurally unreachable by any playing faction (Art 02a §10).*

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

#### Card Domain — Faction-Only

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Faction.CovertHand[F-xx]` | List of C-xx | VS-02 | Upkeep Step 6 (draw to 6); Beat 3 Step 10 (card returned or discarded per card text) |
| `Faction.PoliticalHand[F-xx]` | List of P-xx | VS-02 | Upkeep Step 6 (draw to 3); Beat 4 Step 9 (card returned or discarded per card text) |
| `Faction.ModifierHand[F-xx]` | List of MC-xx | VS-02 | Upkeep Step 6 (draw by structure count + ring qualification); Beat 3/4 (discarded on use) |
| `Faction.CountermeasureHand[F-xx]` | List of CC-xx | VS-02 | Phase 5 (deployed — handed to ARBITER); Beat 2 (processed, removed from game) |

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

*Quarter 1 exception: `Board.PresenceChips` all zero; `Faction.Resources` at faction starting values (Art 00 §7); `Faction.PublicStanding[F-xx]` all = 10 (PS-03 / Neutral); no active Event Cards.*

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
- `Faction.CovertHand`, `Faction.PoliticalHand`, `Faction.ModifierHand` = drawn to hand size

**Invariants:**
- No deployment markers on board — all in Hand
- `Faction.CovertHand` count ≤ 6; `Faction.PoliticalHand` count ≤ 3 per faction
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
- `Faction.CovertHand[F-xx]` = resolved cards returned to faction (per card text)
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

*Pending content pass.*

Each beat is expressed as a structured function:

```
Beat_N(inputs) → outputs
  // Preconditions
  // Procedure steps (IF/THEN/ELSE)
  // Modifier stack (summation formula)
  // Resolution check (formal inequality)
  // State mutations
  // Output
```

Beat functions to define: `Beat_0()`, `Beat_1()`, `Beat_2()`, `Beat_3()`, `Beat_4()`, `Beat_5()`.

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

*Pending content pass.*

Variable modifier rows are stubbed pending Art 04:

| ID | Modifier Name | Type | Value | Dependency |
|----|--------------|------|-------|------------|
| M-01 | Critical Success | Fixed | −25 | Art 03 §14 |
| M-02 | Critical Failure | Fixed | +25 | Art 03 §14 |
| M-03 | Untrained | Fixed | +25 | Art 03 §14 |
| M-04 | Infrastructure | Fixed | −25 | Art 03 §14, L107 |
| M-05 | Partial Payment | Fixed | +50 | Art 03 §14 |
| M-06 | Experienced | Fixed | −15 | Art 03 §14 |
| M-07 | Known Operative | Fixed | +15 | Art 03 §14 |
| M-08 | Modifier Card | Variable | TBD | Blocked — Art 04 |
| M-09 | Protect | Variable | TBD | Blocked — Art 04 |
| M-10 | Situation Report | Variable | TBD | Blocked — Art 04 |
| M-11 | Type A | Fixed | 0 | Art 03 §14 |
| M-12 | Type B | Variable | TBD | Blocked — Art 04 |

---

## 8. Design Notes

**Source of truth:** Art 03 is the current authoritative specification. This document is a formalization layer — where 03a contradicts 03, the inconsistency must be investigated. The conflict may reflect an error in 03a's formalization, or it may surface an ambiguity, edge case, or gap in Art 03 that prose obscured. Either outcome is a design finding requiring resolution and, if necessary, refinement of Art 03.

**L2 implication:** The Beat Procedures in Layer 2 are intended to be directly translatable to a server-side game engine (L2 architecture). The TypeScript schema in Retired/Electronic/old__08_DATA_MODEL.md is the target L2 data model; 00b entity IDs should align to it.

**Modifier balance analysis:** Once all modifier rows (M-01–M-12) are fully specified, the summation formula in Beat_3() enables a full balance analysis: expected difficulty shift per modifier combination, pathological stack identification, and recommendation for modifier caps if needed.

---

*End of Art 03a — Game Engine Specification v0.1*
