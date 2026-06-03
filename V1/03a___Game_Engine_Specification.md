# 03a — GAME ENGINE SPECIFICATION
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.98  
**Status:** 🔄 In Progress — Tiers 1–3 complete; Phase procedures added (Phase_1–Phase_7); Tier 4 stub pending  
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

1. [Overview](#1-overview)
2. [Index](#2-index)
3. [Scope and Tier Structure](#3-scope-and-tier-structure)
4. [State Model](#4-state-model)
5. [Phase & Beat Procedures (Pseudocode)](#5-phase-beat-procedures-pseudocode)
   - Quarter_Flow() — full Quarter entry point
   - Phase_1() through Phase_7() — phase procedures
   - Beat_0() through Beat_5() — Phase 6 detail
6. [Decision Tables & Edge Case Registry](#6-decision-tables-edge-case-registry)
   - DT-01: Card face determination at Beat 0 (non-Apex)
   - DT-02: Card face determination at Beat 0 (Apex)
   - DT-03: Critical Success override (01–05)
   - DT-04: Critical Failure override (96–100)
   - DT-05: Partial payment at Beat 4
   - DT-06: The Mid modifier scope (L107)
   - DT-07: Type B Countermeasure scope
   - DT-08: Apex activation threshold check
   - DT-09: Emergency Response role (assist / thwart)
   - Apex_Activation() procedure
7. [Modifier Stack Reference](#7-modifier-stack-reference)
8. [Design Notes](#8-design-notes)
9. [Modifier Balance Analysis (stub)](#9-modifier-balance-analysis)

---

## 3. Scope and Tier Structure

Art 03a is organized into three tiers of increasing specificity:

| Tier | Contents | Status |
|-------|----------|--------|
| 1 | State Model — formal game state at each beat boundary, using 00b entity IDs as variable vocabulary | ✅ Draft complete — §4 |
| 2 | Phase & Beat Procedures — Quarter_Flow() entry point; Phase_1()–Phase_7() with explicit state mutations for all phases; Beat_0()–Beat_5() as Phase 6 detail (modifier stack summation formula, resolution inequality) | ✅ Draft complete — §5 |
| 3 | Decision Tables — all branching conditions surfaced as tables; edge cases include face-down/face-up, Apex vs. non-Apex, Critical overrides, partial payment, The Mid scope (L107), Type B scope | ✅ Draft complete — §6 |
| 4 | Modifier Balance Analysis — modifier stack mathematics: expected difficulty shift per modifier combination, pathological stack identification, modifier cap recommendations | 🔄 Stub — §9; blocked until all M-xx values fully specified (Art 04 card definitions pending) |

**Modifier balance analysis** (original XA-27 scope) is a derived output of Tier 2 once the modifier stack is formally expressed. Stub in §9 — full population blocked until Art 04 card definitions complete (M-08, M-09, M-10 variable rows).

---

## 4. State Model

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
| `Faction.IntelTokens[F-xx]` | 0 — all factions | Art 02b |

⚠ **Starting resources — open question:** Art 01 §7 "Starting Round 1 Income" projects income from Q1 Upkeep Step 5, calculated from setup chip placement. It is unclear whether factions begin the game with resources in hand (a setup grant before Q1 Upkeep), or at zero (receiving their first income during Q1 Upkeep Step 5 only). If the income table reflects only the Upkeep yield, starting value = 0. If it includes a pre-Upkeep starting grant, the income table values are the combined total. Requires resolution in Art 00 §7 or Art 02b.

#### Quarter Domain at Setup

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `Quarter.Number` | 1 | Setup |
| `Quarter.InitiativeOrder` | Unset — established in Phase 1 Upkeep Step 2 | Phase 1 |
| `Quarter.InitiativePattern` | Unset — established in Phase 1 Upkeep Step 2 | Phase 1 |

#### Event Domain at Setup

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `Event.ActiveCards` | [] — empty | Setup |
| `Event.BroadcastCard` | None | Setup |
| `Chorus.ActivityTrack` | TBD — Art 07 | Art 07 |

#### Card Domain at Setup

All card types follow the same structural model: `Card.Type.Deck` is the active draw deck (selected at session setup); `Card.Type.Hand` is cards in faction possession and available to play. Lifecycle behavior (Recycle / OneShot / Permanent / Deploy) is a card attribute — not encoded in the variable name. Source: Art 04 §3, §11, §12; Art 05.

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `Card.Covert.Deck[F-xx]` | 24 cards — selected from session pool (~30 available); shuffled and placed face-down on tableau | Session setup; Art 04 §3 |
| `Card.Covert.Hand[F-xx]` | [] (0) — drawn to 6 in Phase 1 Upkeep Step 6 | Phase 1 |
| `Card.Political.Deck[F-xx]` | 12 cards — selected from session pool (~20 available); shuffled and placed face-down on tableau | Session setup; Art 04 §3 |
| `Card.Political.Hand[F-xx]` | [] (0) — drawn to 3 in Phase 1 Upkeep Step 6 | Phase 1 |
| `Card.Modifier.Deck[F-xx]` | Faction modifier deck shuffled and placed face-down; applicable ring decks pre-positioned on board | Session setup; Art 04 §11 |
| `Card.Modifier.Hand[F-xx]` | [] (0) — drawn in Phase 1 Upkeep Step 6 | Phase 1 |
| `Card.Countermeasure.Hand[F-xx]` | 3 CC cards — all Active=True; in tableau designated area | Session setup; Art 04 |
| `Card.Pass.Hand[F-xx]` | 4 Pass cards — Lifecycle: Permanent; beside tableau | Session setup; Art 04 §12 |
| `Card.Floor.Hand[F-xx]` | 1 Floor Act — Lifecycle: Permanent; beside tableau | Session setup; Art 04 D04-13 |
| `Card.Operative.Hand[F-xx]` | Operative cards selected at session setup — Lifecycle: Deploy; in Hand, 0 deployed to board | Session setup; Art 05 |
| `Card.ClassifiedDirective.Hand[F-xx]` | Classified directive cards assigned at session setup — Lifecycle: Secret; private to faction; never removed until scored | Session setup; Art 05 |
| `Card.ARBITER.*` | TBD — Art 07 (resolution materials, Apex envelopes, Chronicle cards, Emergency Response set) | Art 07 |

*Deck pool sizes (30 covert / select 24; 20 political / select 12) are working baselines pending validation — Art 04 A-04-01.*

#### ARBITER Domain at Setup

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `ARBITER.ModifierToken[M-xx]` | Provisioned by denomination — full set per Art 07 | Session setup; Art 07 |
| `ARBITER.Resources[RT-06]` | TBD — Art 07 | Art 07 |
| `ARBITER.Notepad` | Empty | Session setup |

#### System Domain at Setup

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `Reservoir[RT-xx]` | 50 per resource type — provisioned at session start | Setup |

*Reservoir is pre-loaded with 50 of each resource type at session start. This represents the city's existing economic base and ensures sufficient supply to sustain Burst Play trades, Translation payouts, and other Reservoir draws across all 8 Quarters. Value is a working baseline pending playtest validation. Resources also enter the Reservoir through faction payments during Resolution (Beat 0 drain, Beat 4 Submit Payment). ARBITER.Resources[RT-06] is ARBITER's own operational resource — separate from the Reservoir.*

#### Case Domain at Setup

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `Case[F-xx].ID` | Assigned at session setup — one case per faction, physical label | Session setup |
| `Case[F-xx].Faction` | F-xx — assigned at session setup | Session setup |
| `Case[F-xx].Packet[n].*` | All empty — no packets loaded; submitted at Phase 3 Dispatch | Phase 3 |

#### Resolution Grid Domain at Setup

| Variable | Starting Value | Source |
|----------|----------------|--------|
| `Grid.*` (ARBITER Resolution Area) | All empty — built at Beat 0 | Beat 0 |
| `Grid.Political[F-xx].*` | All empty — populated at Phase 4 Declaration | Phase 4 |

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

*`Board.InfluenceLevel` and `Board.ControlFlag` are computed views. Physical components (Control flags, Established markers, Tension markers) are player-maintained and must be synchronized immediately after every chip change.*

*ARBITER (F-06) chip placement at D-22 (8 chips) makes ARBITER's Dominant status at the Chorus Node structurally permanent — no playing faction can accumulate enough chips to surpass 8 while holding other board positions. See §4.0 for setup initialization. ARBITER Dominance Marker (Art 02a §10) is the physical representation.*

---

#### Faction Domain

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Faction.Resources[F-xx][RT-xx]` | Integer ≥ 0 | VS-02 | Upkeep Step 5 (income); Beat 0 (covert payment drain to Reservoir); Phase 4 Declaration (tokens moved to Grid.Political.ResourceStake — committed, not yet in Reservoir); Beat 4 Submit Payment (Grid.Political.ResourceStake drained to Reservoir); Beat 3/4 failure conditions (standing/resource penalties per card text); Debrief (trades, conversion) |
| `Faction.PublicStanding[F-xx]` | Integer 0–20 | VS-01 | Upkeep Step 3 (Situation Report effect); Beat 3 Steps 8–9; Beat 4 Step 8 (failure/discovery conditions); Quarter close (natural drift, L13) |
| `Faction.ChorusPortrait[F-xx]` | Integer | VS-04 | Beat 3 Step 11 (per resolved covert operation, privately); Beat 4 Step 10 (per resolved political act, privately) |
| `Faction.StatusMarker[F-xx]` | Discussing \| Operating | VS-01 | Upkeep Step 1 (reset to Discussing) |
| `Faction.BurstPlay[F-xx]` | Boolean | VS-01 | Upkeep Step 6 (set True on trigger — persistent for remainder of session) |
| `Faction.IntelTokens[F-xx]` | Integer ≥ 0 | VS-02 | Beat 5 (incremented by intel tokens received from dispatch case); TBD — Art 02b §8–9 (spending, age rules, scoring) |

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

*Naming convention: `Card.Type.State[F-xx]` — Type identifies the card class; State is `Deck` (the draw pile) or `Hand` (cards in faction possession, available to play — regardless of lifecycle type).*

**Card.Faction attribute:** Every card entity (C-xx, P-xx) carries a `Faction` field (Art 04 §4): `All` (Common — standard cards available to every faction) or `F-xx` (Faction-Specific — exclusive to the owning faction). `Card.Covert.Deck[F-xx]` and `Card.Political.Deck[F-xx]` are built from the faction's session pool, pre-filtered to: `Card.Faction = All` (eligible for any faction) UNION `Card.Faction = F-xx` (eligible for this faction only). This constraint governs deck construction at session setup.

*ARBITER (F-06) has a distinct card set and modifier token provisioning. Variables stubbed below; full definition Art 07.*

**Lifecycle taxonomy:** All card variables use `.Hand` — cards in the faction's possession, available to play. The distinction between card types is in lifecycle behavior, not in the variable name:

| Lifecycle | Cards | Behavior |
|-----------|-------|----------|
| Recycle | Covert, Political | Draw from Deck → Hand → use → discard pile → reshuffle when Deck exhausted |
| OneShot | Modifier, Countermeasure | Drawn or pre-allocated → Hand → used → **Active=False** (removed from game; no reshuffle) |
| Permanent | Pass, Floor Act | Always in Hand; never consumed, never discarded; reusable every Quarter |
| Deploy | Operative | In Hand until deployed → moves to board operative zone; not recycled |
| Secret | Classified Directive | Assigned at session setup → Hand; VS-04 (private to faction); held throughout session; revealed and scored at game end or per Art 05 conditions; full lifecycle TBD |

**Active flag:** Modifier and Countermeasure cards carry `Active: Boolean` on each card instance. `Active=True` = in hand or in play (Countermeasure: including while held by ARBITER after Phase 5 deployment). `Active=False` = removed from game. Covert, Political, Pass, Floor Act, and Operative do not require this flag — their in-play status is determined by their position (Hand vs Deck vs board zone).

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Card.Covert.Deck[F-xx]` | Ordered list of C-xx where C-xx.Faction ∈ {All, F-xx} | VS-02 | Session setup (deck construction); Upkeep Step 6 (top cards drawn; discard shuffled in when exhausted) |
| `Card.Covert.Hand[F-xx]` | List of C-xx | VS-02 | Upkeep Step 6 (draw to 6); Beat 3 Step 10 (returned or discarded per card text) |
| `Card.Political.Deck[F-xx]` | Ordered list of P-xx where P-xx.Faction ∈ {All, F-xx} | VS-02 | Session setup (deck construction); Upkeep Step 6 (top cards drawn; discard shuffled in when exhausted) |
| `Card.Political.Hand[F-xx]` | List of P-xx | VS-02 | Upkeep Step 6 (draw to 3); Beat 4 Step 9 (returned or discarded per card text) |
| `Card.Modifier.Deck[F-xx]` | Ordered list of MC-xx (faction deck + applicable ring decks) | VS-02 | Session setup (shuffled, placed); Upkeep Step 6 (top cards drawn); Burst Play trigger (deck removed from game) |
| `Card.Modifier.Hand[F-xx]` | List of {MC-xx, Active: Boolean} | VS-02 | Upkeep Step 6 (drawn; Active=True); Beat 3/4 (used → Active=False, removed from game); Burst Play (all traded to Reservoir → Active=False) |
| `Card.Countermeasure.Hand[F-xx]` | List of {CC-xx, Active: Boolean} (max 3) | VS-02 | Session setup (3 allocated; Active=True); Phase 5 (deployed to ARBITER; Active=True — in play); Beat 2 (processed → Active=False, removed from game) |
| `Card.Pass.Hand[F-xx]` | Fixed list of 4 Pass — Lifecycle: Permanent | VS-01 (count); VS-02 (usage intent) | Immutable — reusable every Quarter; never removed |
| `Card.Floor.Hand[F-xx]` | Fixed 1 Floor Act — Lifecycle: Permanent | VS-01 (count); VS-02 (usage intent) | Immutable — always available; never removed; full design Art 04 D04-13 |
| `Card.Operative.Hand[F-xx]` | List of operative cards — Lifecycle: Deploy | VS-02 | Session setup (operative set selected; in Hand); Phase 2 (deployed → moves to board operative zone; no longer in Hand); TBD — Art 05 |
| `Card.ClassifiedDirective.Hand[F-xx]` | List of classified directive cards — Lifecycle: Secret | VS-04 | Session setup (assigned; private to faction); Art 05 (scoring conditions, revelation TBD) |
| `Card.ARBITER.*` | TBD — resolution materials, Apex envelopes, Chronicle cards, Emergency Response set | VS-04 | TBD — Art 07 |

---

#### ARBITER Domain

*ARBITER (F-06) holds materials that are not part of the faction card system. Modifier tokens are physical pieces in multiple denominations managed by ARBITER during Resolution. Full denomination set and physical design: Art 07.*

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `ARBITER.ModifierToken[M-xx]` | Integer ≥ 0 (quantity per denomination) | VS-04 | Session setup (provisioned by denomination); Beat 2 (M-11 placed on grid cell); Beat 3/4 (tokens placed and returned to pool per resolution step) |
| `ARBITER.Resources[RT-06]` | Integer ≥ 0 (Resolution resource — RT-06) | VS-04 | TBD — Art 07 (Translation mechanic, income source) |
| `ARBITER.Notepad` | Running record — per-Quarter observations, resolution patterns, portrait notes, Debrief material, Chronicle source | VS-04 | Beat 3 Step 11 (portrait + resolution notes); Beat 4 Step 10 (political act notes); Beat 5 Step 2 (Quarter-level record); Debrief (narrative summary) |

*`ARBITER.Resources[RT-06]` is ARBITER's operational resource (Resolution, generated at Chorus Node). It is distinct from the Reservoir — see System Domain below.*

---

#### System Domain

*System-level state not owned by any faction. The Reservoir is the shared pool of spent faction resources, maintained on the board. It is a separate entity from ARBITER's resources.*

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Reservoir[RT-xx]` | Integer ≥ 0 per resource type | VS-01 | Session setup (pre-loaded 50 per type); Beat 0 (payment drain from dispatch cases); Beat 4 Submit Payment (political act payment drain); Debrief (Burst Play trade-in; Translation payouts) |

*Design decision: Reservoir = System entity (not F-06). ARBITER already has RT-06 (Resolution) as their own resource type, earned operationally. The Reservoir is the collective pool of all spent faction resources — a board-level pool owned by no faction. Conflating it with F-06 would mix ARBITER's operational budget with the city's resource pool. If Tier 2 architecture treats all resource pools under a unified `Resources[Owner][RT-xx]` model, Reservoir maps to `Owner = System.Reservoir`, not `Owner = F-06`.*

*Starting value of 50 per resource type is a working baseline — sufficient to sustain Burst Play trades (modifier cards → Reservoir resources at 1:1), Translation payouts, and any other Reservoir draws across 8 Quarters. Pending playtest validation (PT-xx — to be assigned).*

---

#### Case Domain — physical transport layer between Faction Players and ARBITER

*The dispatch case is the physical container each faction submits at Phase 3. It holds packets — one per submitted action — which ARBITER reads at Beat 0 to build the Resolution Grid. ARBITER loads response cards and intel tokens into each packet during Beats 3–4; the case is returned to the faction at Beat 5. Cases are assigned at session setup and persist for the full session; packet contents are cleared between Quarters.*

*At setup and at the start of each Quarter: all packet fields are empty — cases exist as physical objects but contain no submissions.*

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Case[F-xx].ID` | Physical label — unique case identifier | VS-02 | Session setup (assigned, immutable) |
| `Case[F-xx].Faction` | F-xx | VS-02 | Session setup (assigned, immutable) |
| `Case[F-xx].Packet[n].SequenceID` | Integer — submission order within case (1 = first submitted) | VS-04 | Phase 3 Dispatch (faction loads); Beat 5 (returned to faction → VS-02) |
| `Case[F-xx].Packet[n].Target` | D-xx \| RG-xx | VS-04 | Phase 3 Dispatch (faction loads); Beat 5 (returned → VS-02) |
| `Case[F-xx].Packet[n].CovertCard` | C-xx \| Pass \| None | VS-04 | Phase 3 Dispatch (faction loads); Beat 5 (returned → VS-02) |
| `Case[F-xx].Packet[n].ModifierCards` | List of MC-xx | VS-04 | Phase 3 Dispatch (faction loads); Beat 5 (returned → VS-02) |
| `Case[F-xx].Packet[n].ARBITERResponseCards` | List of RO-xx — resolution cards placed by ARBITER | VS-04 | Beat 3 Step 10 / Beat 4 Step 9 (ARBITER loads); Beat 5 (returned → VS-02) |
| `Case[F-xx].Packet[n].IntelTokens` | List of ARBITER-placed intel tokens | VS-04 | Beat 3–4 (ARBITER loads, per card text or ARBITER discretion); Beat 5 (returned → VS-02); TBD — Art 07 |

*`SequenceID` establishes packet order within the case — the order in which the faction submitted their operations during Phase 3 Dispatch. This order determines lane assignment in the Resolution Grid (Beat 0 Step 2).*

*`ARBITERResponseCards` and `IntelTokens` are empty at Phase 3 close. ARBITER loads them during Beats 3–4 as each operation resolves. At Beat 5, each faction receives their case with both their submitted content and ARBITER's additions.*

*Intel token contents and provisioning: TBD Art 07.*

---

#### Resolution Grid Domain

*The Resolution Grid spans two physical zones, together forming the full resolution workspace for each Quarter.*

*— **ARBITER Resolution Area**: ARBITER's physical workspace — built at Beat 0 from submitted dispatch cases, active through Beats 1–4, cleared at Beat 5. All variables in this area are VS-04.*

*— **Political Act Declaration Area**: each faction's tableau zone — populated at Phase 4 Declaration, resolved in Beat 4, cleared at Beat 5. Declared acts are VS-01 (public) from the moment of Declaration.*

*`Grid.ResolvedCells` spans both areas — it accumulates RO-xx outcomes for covert operations (Beat 3) and political acts (Beat 4).*

**ARBITER Resolution Area** — VS-04

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Grid.Lane[F-xx].Beat2Slot` | CC-xx \| None | VS-04 | Beat 0 (built from Phase 5 countermeasures); Beat 2 (processed, removed) |
| `Grid.Lane[F-xx].Beat3Queue` | Ordered list of GridCell | VS-04 | Beat 0 (built from dispatch case); Beat 1 (cells removed — restriction blocked); Beat 2 (cells removed — CM blocked; modifier tokens added) |
| `Grid.ActiveModifierTokens` | Map of GridCell → List of M-xx | VS-04 | Beat 0 (M-06 partial payment marker attached); Beat 2 (M-11 Type B token placed); Beat 3 Step 4 (consumed in threshold calculation, returned to pool at Step 10) |
| `Grid.ProtectModifiers` | Map of GridCell → modifier value | VS-04 | Beat 2 (noted from Protect operations for Beat 3 application) |
| `Grid.ResolvedCells` | List of {GridCell × RO-xx} | VS-04 → VS-02 (after Beat 5 dispatch case return) | Beat 3 Step 10 (per resolved covert op); Beat 4 Step 9 (per resolved political act) |
| `Grid.ResolutionQueue` | Ordered list of GridCell positions | VS-04 | Beat 0 (established by case receipt order — first action per lane, then second actions per lane, repeating) |

*GridCell = {Lane: F-xx, Row: Beat2 \| Beat3[position], Card: C-xx \| CC-xx \| Pass, Face: Up \| Down, Target: D-xx \| RG-xx \| F-xx \| N/A}*

**Political Act Declaration Area** — VS-01 after Phase 4 Declaration

| Variable | Type | Visibility | Mutates At |
|----------|------|-----------|------------|
| `Grid.Political[F-xx].DeclaredCard` | P-xx \| Pass \| None | VS-01 | Phase 4 Declaration (faction places face-up on tableau); Beat 4 Resolution (cleared) |
| `Grid.Political[F-xx].ModifierCards` | List of MC-xx | VS-01 | Phase 4 Declaration (played alongside declared act); Beat 4 Resolution (removed from game) |
| `Grid.Political[F-xx].ResourceStake[RT-xx]` | Integer ≥ 0 per resource type | VS-01 | Phase 4 Declaration (tokens moved from Faction.Resources, stacked on card — committed, not yet in Reservoir); Beat 4 Submit Payment (drained to Reservoir; partial marker attached if underpayment) |
| `Grid.Political[F-xx].PartialPaymentMarker` | M-07 \| None | VS-01 | Beat 4 Submit Payment (M-07 attached if ResourceStake < card cost); Beat 4 Resolution (cleared) |

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
- `Faction.IntelTokens[F-xx]` — carry forward; age rules TBD (Art 02b §8–9 — decay conditions may apply at Quarter close)
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
- `Grid.Political[F-xx].DeclaredCard` = P-xx or Pass — face-up on faction tableau
- `Grid.Political[F-xx].ResourceStake[RT-xx]` = resource tokens moved from `Faction.Resources` and stacked on card — committed, not yet in Reservoir
- `Grid.Political[F-xx].ModifierCards` = modifier cards played alongside declared act — face-up

**Invariants:**
- Declared political acts are fully public — card identity, target, and modifier count visible to all
- `Grid.Political[F-xx].ResourceStake` is set; payment transferred to Reservoir in Beat 4 Submit Payment only
- Declared acts cannot be withdrawn or modified

---

#### Phase 5 — Countermeasures Complete

**Outputs:**
- `Card.Countermeasure.Hand[F-xx]` — deployed CC-xx cards transferred to ARBITER Player
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
- `Grid.Lane[F-xx].Beat3Queue` = operations targeting restricted D-xx or RG-xx removed; placed in dispatch case with RO-03 (Voided)
- `Board.DeploymentMarker[F-xx][1|2]` = markers in conversion-blocked districts or rings flipped to Blocked face
- Political acts targeting restricted D-xx or RG-xx: cancelled — card returned to faction; resource tokens returned (not spent)

**Invariants:**
- No card remaining in any Beat3Queue targets a district or ring under an active targeting restriction
- No deployment marker in a conversion-blocked district or ring shows Converting face
- Cancelled political act resource tokens are returned — not in Reservoir

---

#### Beat 2 End — Ground Shifts

**Outputs:**
- `Grid.Lane[F-xx].Beat3Queue` = operations targeting Type A-named districts removed; placed in dispatch case with RO-03 (Voided)
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
- `Faction.IntelTokens[F-xx]` = incremented by any intel tokens ARBITER loaded into the faction's dispatch case
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

## 5. Phase & Beat Procedures (Pseudocode)

`Quarter_Flow()` is the entry point — it calls `Phase_1()` through `Phase_7()` in sequence. `Phase_6()` delegates to `Beat_0()` through `Beat_5()`, the high-formalism detail tier for Resolution. Phase procedures capture all state mutations outside Resolution at the level of precision needed for Tier 2 implementation. Beat procedures add the modifier stack summation formula and the resolution check as a formal inequality, plus modifier IDs from §7.

**Notation:**
- `←` assigns to a state variable; `+=` appends to a list or increments
- `M-xx.value` is the Threshold Adjustment from §7 (positive = threshold raised = easier; negative = harder)
- `D100()` is a uniform random integer 01–100
- `DT-xx` defers branching detail to Tier 3 (§6)
- `DESIGN FINDING [DF-xx]` marks an inconsistency surfaced by formalization — requires investigation
- `district_income(d, f)` references the Art 02a §5 influence level income table — values not reproduced here
- `D10()` is a uniform random integer 1–10

---

### Quarter_Flow

```
Quarter_Flow(quarter_number):

  Quarter.Number ← quarter_number

  Phase_1()   // Upkeep — initiative, event, conversion, income, card draw
  Phase_2()   // Placement — deployment markers placed; entry requirements enforced
  Phase_3()   // Dispatch — covert operations submitted in cases
  Phase_4()   // Declaration — political acts declared publicly
  Phase_5()   // Countermeasures — CC-xx cards deployed to ARBITER Player
  Phase_6()   // Resolution — delegates to Beat_0 through Beat_5

  // Session end check: if Apex resolved during Phase_6, Quarter_Flow does not return
  // If Quarter.Number = 8 and no Apex resolved: proceed to Session End (Art 10a)

  Phase_7()   // Debrief — table reflects; Quarter closes
  Quarter.Number += 1
```

---

### Phase_1 — Upkeep

```
Phase_1() → Quarter, Event, Board, Faction, Card state initialized for the Quarter

// Step 1 — Status Marker Reset
FOR EACH faction f ∈ Faction.All:
  Faction.StatusMarker[f] ← Discussing

// Step 2 — Initiative
IF Quarter.Number = 1:
  Quarter.InitiativeOrder ← factions clockwise from ARBITER Player's left
  // All Portrait and Public Standing scores equal at Q1 — D10 result ignored
ELSE:
  portrait_ranks ← SORT Faction.All BY Faction.ChorusPortrait[f] DESC,
                   TIEBREAK BY Faction.PublicStanding[f] DESC,
                   TIEBREAK BY ARBITER discretion
  ip_roll ← D10()
  Quarter.InitiativePattern ← IP-xx(ip_roll)   // pattern table: Art 03 §7 Step 2
  Quarter.InitiativeOrder ← apply(Quarter.InitiativePattern, portrait_ranks)
ARBITER announces Quarter.InitiativeOrder; ARBITER Player updates Initiative Strip

// Step 3 — Situation Report
broadcast_card ← draw top of Broadcast Deck
Event.BroadcastCard ← broadcast_card
Event.ActiveCards += broadcast_card
PLACE broadcast_card face-up in Event Zone on The Overview
ARBITER reads Event Card aloud; announces PS changes only (does not announce difficulty modifiers or hidden effects)
FOR EACH f WHERE event_card specifies PublicStanding change:
  Faction.PublicStanding[f] ← adjusted per event_card
FOR EACH (f, slot) WHERE Board.DeploymentMarker[f][slot].Location ∈ event_card.BlockedDistricts:
  Board.DeploymentMarker[f][slot].Face ← Blocked
// Remove expired cards (duration was decremented at prior Quarter close — Phase 1 cleans up)
Event.ActiveCards ← FILTER Event.ActiveCards WHERE card.Duration > 0

// Step 4 — Deployment Marker Conversion
FOR EACH faction f ∈ Faction.All:
  FOR EACH slot ∈ [1, 2] WHERE Board.DeploymentMarker[f][slot].Location ≠ Hand:
    IF Board.DeploymentMarker[f][slot].Face = Converting:
      d ← Board.DeploymentMarker[f][slot].Location
      Board.PresenceChips[d][f] += 1
      RECALCULATE Board.InfluenceLevel[d][*]
      RECALCULATE Board.ControlFlag[d]
      RECALCULATE Board.TensionMarker[d]
      Faction Player updates Control flag, Established markers, Tension markers immediately
    Board.DeploymentMarker[f][slot] ← {Location: Hand, Face: N/A}

// Step 5 — Resource Collection  (simultaneous; all factions at once)
FOR EACH faction f ∈ Faction.All:
  FOR EACH district d WHERE Board.PresenceChips[d][f] > 0
                         OR Board.DeploymentMarker[f][*].Location = d:
    Faction.Resources[f][*] += district_income(d, f)   // Art 02a §5 — IL modifier × base generation
  FOR EACH structure block s AT district d OWNED BY f:
    resource_type ← f declares aloud: d.NativeResource OR f.NativeResource
    Faction.Resources[f][resource_type] += 1
  Faction.Resources[f][f.NativeResource] += 1   // passive generation — unconditional

// Step 6 — Operations Preparation  (simultaneous; all factions at once)
FOR EACH faction f ∈ Faction.All:
  // Covert and political card draw to hand size
  WHILE Card.Covert.Hand[f].count < 6:
    IF Card.Covert.Deck[f] empty: SHUFFLE discard pile into Deck
    Card.Covert.Hand[f] += draw(Card.Covert.Deck[f])
  WHILE Card.Political.Hand[f].count < 3:
    IF Card.Political.Deck[f] empty: SHUFFLE discard pile into Deck
    Card.Political.Hand[f] += draw(Card.Political.Deck[f])
  // Modifier card draw — skipped if Faction.BurstPlay[f] = True
  IF NOT Faction.BurstPlay[f]:
    faction_draw_count ← modifier_draw_table(Board.StructureBlocks[*][f].total)  // Art 03 §7 table
    Card.Modifier.Hand[f] += draw(Card.Modifier.Deck[f], faction_draw_count)
    FOR EACH ring rg ∈ {RG-01, RG-02, RG-03}:
      IF Board.StructureBlocks[rg districts][f].total ≥ 1
         AND ∃ d ∈ rg districts: Board.InfluenceLevel[d][f] ∈ {IL-01, IL-02}:
        Card.Modifier.Hand[f] += draw(RingDeck[rg], 1)
  // Burst Play window — faction may trigger before Dispatch opens
  IF faction chooses Burst Play:
    FOR EACH mc ∈ Card.Modifier.Hand[f]:
      rt ← f declares any RT-xx
      Faction.Resources[f][rt] += 1   // 1 resource per card traded, type chosen per card
      mc.Active ← False               // removed from game
    Card.Modifier.Hand[f] ← []
    REMOVE Card.Modifier.Deck[f] from game
    Faction.BurstPlay[f] ← True
    ARBITER announces: "[Faction] has liquidated their operational reserve."
    // BurstPlay = True persists for remainder of session; modifier draws skipped all future Q's

STATE MUTATIONS:
  Faction.StatusMarker[F-xx] ← Discussing (all)
  Quarter.InitiativeOrder ← established; Quarter.InitiativePattern ← IP-xx
  Event.BroadcastCard ← current EC-xx
  Event.ActiveCards ← updated (new card added; expired cards removed)
  Faction.PublicStanding[F-xx] ← Situation Report effects applied
  Board.DeploymentMarker[F-xx][1|2] ← {Location: Hand, Face: N/A} (all markers returned)
  Board.PresenceChips[D-xx][F-xx] ← +1 per converted marker
  Board.InfluenceLevel, Board.ControlFlag, Board.TensionMarker ← recalculated (derived)
  Faction.Resources[F-xx][RT-xx] ← income collected (district + structure blocks + passive)
  Card.Covert.Hand[F-xx] ← drawn to 6
  Card.Political.Hand[F-xx] ← drawn to 3
  Card.Modifier.Hand[F-xx] ← drawn per structure block count and ring qualifications
  Faction.BurstPlay[F-xx] ← True if triggered this step (persistent)
```

---

### Phase_2 — Placement

```
Phase_2() → Board.DeploymentMarker placed; derived board state updated after each placement

PRECONDITIONS:
  Phase_1 complete — all markers in Hand; Quarter.InitiativeOrder established

// Snake pattern: forward pass (Rank 1 → n, one marker each); reverse pass (Rank n → 1, second marker each)
FOR EACH (faction f, slot s) IN snake_order(Quarter.InitiativeOrder):
  IF faction passes:
    CONTINUE  // Board.DeploymentMarker[f][s] remains {Location: Hand, Face: N/A}

  d ← faction's chosen target district
  // Verify entry requirement for d — ARBITER redirects illegal placements
  IF d.Ring = RG-03 (Core):
    REQUIRE: ∃ d2 adjacent to d WHERE d2.Ring = RG-02
             AND Board.InfluenceLevel[d2][f] ∈ {IL-01, IL-02}
             // Temporary presence from first marker placed this Phase counts
  IF d = D-22 (Chorus Node):
    REQUIRE: ∃ d2 adjacent to d WHERE d2.Ring = RG-03
             AND Board.InfluenceLevel[d2][f] ∈ {IL-01, IL-02}
             // Additional Chorus Node entry rules: Art 02a §10
  // RG-01 (Baryo) and RG-02 (The Mid): no entry requirement

  Board.DeploymentMarker[f][s] ← {Location: d, Face: Converting}
  // Marker counts as 1 temporary presence chip immediately upon placement
  RECALCULATE Board.InfluenceLevel[d][*]
  RECALCULATE Board.ControlFlag[d]
  RECALCULATE Board.TensionMarker[d]
  Faction Player updates Control flag, Established markers, Tension markers immediately

STATE MUTATIONS:
  Board.DeploymentMarker[F-xx][1|2] ← {Location: D-xx, Face: Converting} per placed marker
  Board.InfluenceLevel, Board.ControlFlag, Board.TensionMarker ← recalculated after each placement (derived)
```

---

### Phase_3 — Dispatch

```
Phase_3() → Case[F-xx].Packet[n].* loaded; Grid lane assignments established

// Physical transmission step — minimal state mutation; no board or resource changes

ARBITER announces: "Dispatch is open." Starts dispatch timer.

// All factions assemble and seal their cases simultaneously and privately
FOR EACH faction f ∈ Faction.All:
  FOR EACH operation packet n faction submits:
    Case[f].Packet[n].SequenceID    ← n                  // submission order within case
    Case[f].Packet[n].CovertCard    ← C-xx | Pass
    Case[f].Packet[n].Target        ← D-xx | RG-xx
    Case[f].Packet[n].ModifierCards ← list of MC-xx (may be empty)
    // Resource tokens enclosed physically — validated and drained at Beat_0
  Faction Player seals Case[f]

// ARBITER Player queues received cases in receipt order (left to right)
lane_counter ← 1
ON EACH case received BY ARBITER Player:
  Grid.ResolutionQueue.LaneAssignment[case.Faction] ← lane_counter
  lane_counter += 1

// Timer expires — Dispatch closed
// Any case not yet received: treated as all-Pass (no submitted operations)

STATE MUTATIONS:
  Case[F-xx].Packet[n].* ← populated by faction
  Grid.ResolutionQueue.LaneAssignment ← established by case receipt order
```

---

### Phase_4 — Declaration

```
Phase_4() → Grid.Political state populated; Faction.Resources committed to ResourceStake

FOR EACH faction f IN Quarter.InitiativeOrder:
  IF faction passes:
    Grid.Political[f].DeclaredCard ← Pass
    CONTINUE

  act ← selected from Card.Political.Hand[f]
  // Must target one of f's two placed deployment marker locations this Quarter
  target ← f's deployment marker location (declared on target slip)
  stake ← resource tokens f places on card — may be any amount ≤ act.BaseCost
           // Partial or zero payment: detected and handled at Beat_4 Submit Payment
  modifiers ← MC-xx cards played alongside (may be empty)

  // Physical placement — face-up, public, irrevocable
  PLACE act face-up on tableau with target slip; PLACE stake tokens on act; PLACE modifiers face-up alongside

  Grid.Political[f].DeclaredCard ← act
  Grid.Political[f].ResourceStake[RT-xx] ← stake  // tokens committed; not yet in Reservoir
  Grid.Political[f].ModifierCards ← modifiers
  Faction.Resources[f][RT-xx] -= stake             // tokens physically move to tableau stake

STATE MUTATIONS:
  Grid.Political[F-xx].DeclaredCard ← P-xx or Pass
  Grid.Political[F-xx].ResourceStake[RT-xx] ← committed tokens
  Grid.Political[F-xx].ModifierCards ← MC-xx list
  Faction.Resources[F-xx][RT-xx] ← reduced by staked amount
  // Note: ResourceStake transfers to Reservoir at Beat_4 Submit Payment only — not here
```

---

### Phase_5 — Countermeasures

```
Phase_5() → CC-xx cards transferred to ARBITER Player

FOR EACH faction f IN Quarter.InitiativeOrder:
  IF faction passes:
    CONTINUE
  FOR EACH cc ∈ CC-xx cards faction chooses to deploy:
    PLACE cc face-up on tableau
    DECLARE cc.Type (Type A or Type B) to ARBITER Player
    HAND cc to ARBITER Player  // identity is VS-04 — not yet public

// ARBITER Player collects all dispatch cases from receive queue
// Phase 6 begins immediately after

STATE MUTATIONS:
  Card.Countermeasure.Hand[F-xx] ← deployed CC-xx cards physically held by ARBITER Player
  // No board or resource changes — Phase 5 is a physical handoff only
```

---

### Phase_6 — Resolution

```
Phase_6()

// Resolution executes across six sequential beats.
// Full specification: Beat procedures below.

Beat_0(dispatch_cases, countermeasures)   // Grid built; payment validated; resources drained
Beat_1(Event.ActiveCards)                 // Restrictions applied; restricted ops/acts removed
Beat_2()                                  // Countermeasures processed; grid cleaned
Beat_3()                                  // Covert operations resolved
Beat_4()                                  // Political acts resolved
Beat_5()                                  // Cases returned; Resolution Grid cleared

// If Apex resolved during Beat_3 or Beat_4: Quarter_Flow does not return from Phase_6
// State mutations: see Beat procedures below
```

---

### Phase_7 — Debrief

```
Phase_7() → Quarter closed; all end-of-Quarter state mutations applied

// Open table — no initiative order, no phase timer
// Free actions throughout (ARBITER observes; no state tracked here):
//   Resource trades between any two factions (any terms)
//   Intel note exchanges between any two factions
//   Accord proposals, counter-proposals, acceptances, declines

// ARBITER conversion — available between phases and throughout Debrief
// Not available during Resolution Beats 1–4 while ARBITER is processing board changes

// Chorus Question window
IF Chorus.ActivityTrack ≥ question_threshold
   AND ∃ f: Board.InfluenceLevel[D-22][f] ∈ {IL-01, IL-02, IL-03}  // at least Present
   AND NOT Board.TensionMarker[D-22]:                                 // Node not Contested
  // Any qualifying faction may propose a Chorus Question; simple majority passes
  // ARBITER answers in The Observation register — Art 07

// ARBITER Debrief observation  (one, in The Observation register)
//   Form A: "[Faction] has moved into [PORTRAIT STATE]. [STATE LANGUAGE]."
//   Form B: "[Faction]'s contribution to the Portrait this Quarter was [vague adjective]."
//   If Chorus.ActivityTrack changed this Quarter: incorporate into observation

// Ready-to-close
// Each Faction Player flips Status marker to Ready (green/Operating) when done with Debrief
// On 3-of-5 green: ARBITER announces and starts 60-second courtesy timer
// Debrief closes when timer expires OR all 5 show green

// Quarter close — strict sequence (Art 03 §15)

// 1. Findings decay — Ghost (F-01) only; applied publicly
IF Faction.Resources[F-01][RT-01] ∈ [7, 12]:
  Faction.Resources[F-01][RT-01] -= 2
  F-01 returns 2 Findings tokens to Reservoir
ELSE IF Faction.Resources[F-01][RT-01] ≥ 13:
  Faction.Resources[F-01][RT-01] -= 4
  F-01 returns 4 Findings tokens to Reservoir
// < 7: no decay

// 2. Debrief reward — ARBITER assesses Debrief quality; applies Tier A/B/C effect — Art 07

// 3. Operation Resolution cards collected
FOR EACH faction f ∈ Faction.All:
  COLLECT RO-xx resolution cards from f → ARBITER Player  // reusable; reset for next Quarter

// 4. Event duration decrement
FOR EACH card ∈ Event.ActiveCards:
  card.Duration -= 1
  // Expired cards (Duration ≤ 0) remain in ActiveCards list until Phase_1 Step 3 cleanup next Quarter

// 5. Natural Public Standing drift (L13)
FOR EACH faction f ∈ Faction.All:
  IF Faction.PublicStanding[f] > 13: Faction.PublicStanding[f] -= 1
  ELSE IF Faction.PublicStanding[f] < 7: Faction.PublicStanding[f] += 1
  // Range 7–12 (PS-03 Neutral bracket): no drift

// 6. Quarter.Number incremented in Quarter_Flow() after Phase_7 returns

STATE MUTATIONS:
  Faction.Resources[F-xx][RT-xx] ← trades (variable); Findings decay on F-01 if applicable
  Faction.IntelTokens[F-xx] ← net change from intel exchanges (variable)
  Event.ActiveCards ← duration decremented; expired cards flagged for Phase_1 cleanup
  Faction.PublicStanding[F-xx] ← natural drift (±1 toward range 7–12; no change if already within)
```

---

### Phase 6 Detail — Beat Procedures

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
        PLACE Voided resolution card → dispatch_case[lane.Faction]
        DISCARD modifier cards from cell — removed from game
        // No resource refund — resources were drained at Beat 0

// DF-01 RESOLVED (L112, Session 22): "Operation Failed" (Beat 1) and "Operation Blocked"
// (Beat 2) unified as "Voided" (RO-03). Art 03 and 00b updated. See §8.

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
  Grid.ResolvedCells ← RO-03 (Voided) entries for restricted covert ops
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
        PLACE Voided resolution card → dispatch_case[target_lane.Faction]
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
  Grid.ResolvedCells ← RO-03 (Voided) entries for Type A voided ops
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
             + (M-12.value  IF cell.Target.Ring = RG-02                              // −25 The Mid
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
  Grid.Political[F-xx].DeclaredCard set for all factions — face-up on faction tableau
  Grid.Political[F-xx].ResourceStake[RT-xx] set — stacked on card, not yet in Reservoir

// Submit Payment phase — initiative order
FOR EACH faction f WHERE Grid.Political[f].DeclaredCard ∉ {Pass, None} (in Quarter.InitiativeOrder):
  act ← Grid.Political[f].DeclaredCard
  actual_payment ← Grid.Political[f].ResourceStake  // total across all RT-xx
  card_cost ← act.BaseThreshold
  DRAIN Grid.Political[f].ResourceStake → Reservoir  // physical token transfer
  IF actual_payment = 0:
    ARBITER announces act invalid
    act.Face ← Down  // Auto-fail when reached in resolution phase
  ELSE IF actual_payment < card_cost:
    Grid.Political[f].PartialPaymentMarker ← M-07
    ARBITER announces additional difficulty
    // M-07 (−50 threshold) applied in modifier stack below

// DF-02 RESOLVED (L113, Session 22): "+50 difficulty marker" (Art 03 Beat 4) and "−50 threshold"
// (§7 modifier table) unified under threshold sign convention throughout. Art 03 Beat 0/4
// updated. Art 07 physical token design note preserved in §8. See §8 Open Design Findings.

// Resolution phase — initiative order
FOR EACH faction f WHERE Grid.Political[f].DeclaredCard ∉ {Pass, None} (in Quarter.InitiativeOrder):
  act ← Grid.Political[f].DeclaredCard

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
             + (M-07.value  IF Grid.Political[f].PartialPaymentMarker = M-07   ELSE 0)  // −50 partial pmt
             + (M-10.value  IF Situation Report effect targets act   ELSE 0)  // Variable; Event
             + (M-12.value  IF act.Target.Ring = RG-02                        // −25 The Mid
                               AND NOT ∃ d ∈ D-xx: d.Ring = RG-03
                                                    AND d.AdjacentTo(act.Target)
                                                    AND Board.InfluenceLevel[d][f] ∈ {IL-01, IL-02}
                               ELSE 0)
             + Σ(card.ModifierValue FOR EACH modifier_card IN Grid.Political[f].ModifierCards)  // M-08; Variable

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
  DISCARD Grid.Political[f].ModifierCards — removed from game
  Grid.Political[f].DeclaredCard ← None
  Grid.Political[f].ModifierCards ← []
  Grid.Political[f].PartialPaymentMarker ← None
  // Grid.Political[f].ResourceStake already 0 — drained at Submit Payment

  // Step 10 — Portrait (private)
  ARBITER privately updates Faction.ChorusPortrait[f]

END FOR

STATE MUTATIONS:
  Grid.Political[F-xx].ResourceStake ← 0 (drained to Reservoir at Submit Payment)
  Grid.Political[F-xx].PartialPaymentMarker ← M-07 where applicable; cleared after resolution
  Grid.Political[F-xx].DeclaredCard ← None (cleared per resolution)
  Grid.Political[F-xx].ModifierCards ← [] (cleared; removed from game)
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

// Step 3 — Clear Resolution Grid (both areas)
Grid.Lane[F-xx].Beat2Slot    ← None  FOR ALL f
Grid.Lane[F-xx].Beat3Queue   ← []    FOR ALL f
Grid.ActiveModifierTokens    ← {}    (empty map)
Grid.ProtectModifiers        ← {}    (empty map)
Grid.ResolvedCells           ← []    (empty list)
Grid.ResolutionQueue         ← []    (empty list)
Grid.Political[F-xx].DeclaredCard          ← None  FOR ALL f  // should already be None from Beat_4
Grid.Political[F-xx].ModifierCards         ← []    FOR ALL f
Grid.Political[F-xx].ResourceStake[RT-xx]  ← 0     FOR ALL f  // should already be 0 from Submit Payment
Grid.Political[F-xx].PartialPaymentMarker  ← None  FOR ALL f

OUTPUT:
  Faction Players hold dispatch cases — each faction's outcomes privately visible
  Resolution Grid cleared — no Grid domain state carries to next Quarter
  Debrief opens

STATE MUTATIONS:
  Faction.IntelTokens[F-xx] ← incremented by intel tokens received from dispatch case
  Grid.* ← all variables cleared to empty state
```

---

## 6. Decision Tables & Edge Case Registry

Decision tables cover all branching points in Beats 0–5, surfacing conditions deferred in Tier 2 via `DT-xx` notation. All tables are L108 compliant — single-typed columns, controlled vocabulary, single condition per row.

| Table | Branch Condition | Status |
|-------|-----------------|--------|
| DT-01 | Card face determination at Beat 0 — non-Apex | ✅ Draft |
| DT-02 | Card face determination at Beat 0 — Apex | ✅ Draft |
| DT-03 | Critical Success override (roll 01–05) | ✅ Draft |
| DT-04 | Critical Failure override (roll 96–100) | ✅ Draft |
| DT-05 | Partial payment at Beat 4 Submit Payment | ✅ Draft |
| DT-06 | The Mid modifier scope (L107) | ✅ Draft |
| DT-07 | Type B Countermeasure scope | ✅ Draft (partial — pending Art 04/05 asset definition) |
| DT-08 | Apex activation threshold check (Step 4) | ✅ Draft (threshold value pending Art 05) |
| DT-09 | Emergency Response — assist / thwart Apex | ✅ Draft (stub — pending Art 04/05) |
| — | Apex_Activation() procedure | ✅ Draft |

---

### DT-01 — Card Face Determination at Beat 0 (Non-Apex)

Applied per non-Apex operation card during Beat_0 Step 2. Face determines whether the card resolves normally or auto-fails at Beat_3.

| ID | Payment State | Amount Condition | Card Face | M-06 Attached | Drain |
|----|---------------|-----------------|-----------|---------------|-------|
| DT-01-A | Full | actual_payment = card_cost | Up | No | Yes — full amount |
| DT-01-B | Partial | 0 < actual_payment < card_cost | Up | Yes (−50) | Yes — submitted amount |
| DT-01-C | None | actual_payment = 0 | Down | No | None |

**Face = Down consequence (DT-01-C):** Card reaches Beat_3 as auto-fail (RO-05). No roll is made. Operation card and target slip returned to dispatch case. No resolution card placed.

---

### DT-02 — Card Face Determination at Beat 0 (Apex)

Applied when `card.IsApex = True` during Beat_0 Step 2. Differs from DT-01: partial payment does not attach M-06 — any shortfall makes the card face-down. A face-down Apex does not trigger Apex_Activation().

| ID | Payment State | Amount Condition | Card Face | M-06 Attached | Drain |
|----|---------------|-----------------|-----------|---------------|-------|
| DT-02-A | Full | actual_payment ≥ card_cost | Up | No | Yes — submitted amount |
| DT-02-B | Partial | 0 < actual_payment < card_cost | Down | No | Yes — submitted amount |
| DT-02-C | None | actual_payment = 0 | Down | No | None |

**Face = Down consequence on Apex (DT-02-B, DT-02-C):** Treated as auto-fail (RO-05) at Beat_3 or as invalid act (RO-05) at Beat_4 Submit Payment. Resources drained are not refunded. Apex_Activation() does not trigger.

---

### DT-03 — Critical Success Override (Roll 01–05)

Applied at Beat_3 Step 6 and Beat_4 Step 6 whenever `roll ∈ [01, 05]`. Overrides threshold regardless of value — a threshold of 0 or lower does not prevent success on this path.

| ID | Roll Range | Threshold | Outcome | crit_success | crit_failure |
|----|------------|-----------|---------|-------------|-------------|
| DT-03-A | 01–05 | Any | RO-01 (Critical Success) | True | False |

**Card text interaction:** Critical Success may trigger bonus effects specified in card text. No other resolution path sets `crit_success = True`. Discovery conditions do not trigger on DT-03-A.

---

### DT-04 — Critical Failure Override (Roll 96–100)

Applied at Beat_3 Step 6 and Beat_4 Step 6 whenever `roll ∈ [96, 100]`. Overrides threshold regardless of value. Discovery conditions may further override RO-02 to RO-04 at Beat_3 Step 9.

| ID | Roll Range | Threshold | Initial Outcome | crit_failure | Discovery Override Available |
|----|------------|-----------|-----------------|-------------|------------------------------|
| DT-04-A | 96–100 | Any | RO-02 (Critical Failure) | True | Yes — if card specifies discovery condition |

**Discovery override path (Beat_3 only):** If `card.DiscoveryCondition` is specified and `crit_failure = True`, outcome becomes RO-04 (Discovered) at Step 9, overriding RO-02. Discovery override does not apply to political acts (Beat_4).

---

### DT-05 — Partial Payment at Beat 4 (Political Acts)

Applied during Beat_4 Submit Payment phase for each declared political act (excludes Pass and None).

| ID | Payment State | Amount Condition | act.Face | M-07 Applied | ARBITER Announcement |
|----|---------------|-----------------|----------|------|---|
| DT-05-A | Full | actual_payment = card_cost | Up (unchanged) | No | None |
| DT-05-B | Partial | 0 < actual_payment < card_cost | Up (unchanged) | Yes (−50) | "Additional difficulty" |
| DT-05-C | None | actual_payment = 0 | Down | No | "Act invalid" |

**Face = Down consequence (DT-05-C):** When reached in resolution phase, act is auto-fail (RO-05). Political act card returned to Faction Player; modifier cards discarded; no roll made.

**Stacking note (DT-05-B):** Modifier cards staked on a partial-payment act remain in play and apply to the threshold. M-07 stacks additively with all other applicable modifiers.

---

### DT-06 — The Mid Modifier Scope (L107)

M-12 (−25 threshold) applies to any covert operation or political act targeting a district in the The Mid (RG-02), unless the acting faction holds Established or Dominant presence in at least one adjacent Core district (RG-03) at time of resolution.

| ID | Target Ring | Faction Influence in Adjacent Core | M-12 Applied |
|----|-------------|-------------------------------------|--------------|
| DT-06-A | The Mid (RG-02) | Established (IL-02) or Dominant (IL-01) in ≥ 1 adjacent RG-03 district | No |
| DT-06-B | The Mid (RG-02) | Present (IL-03), Absent (IL-04), or no adjacent Core district exists | Yes (−25) |
| DT-06-C | Baryo (RG-01) | Any | No |
| DT-06-D | Core (RG-03) | Any | No |

**Scope (L107):** Applies to all action types — covert operations (Beat_3) and political acts (Beat_4).

**Timing:** Influence check evaluated at time of resolution, not at submission. Board state changes from earlier in the same Beat (e.g., a preceding covert operation) apply to the check.

---

### DT-07 — Type B Countermeasure Scope

M-11 (−15 threshold) is attached during Beat_2 Step 2. Applies to covert operations targeting the defending faction's assets, submitted by any faction other than the defending faction.

| ID | Submitting Faction | Operation Target | M-11 Applied |
|----|--------------------|-----------------|--------------|
| DT-07-A | Any faction other than the defending faction | Asset belonging to the defending faction | Yes (−15) |
| DT-07-B | Any faction other than the defending faction | Asset not belonging to the defending faction | No |
| DT-07-C | Defending faction (self) | Any | No — own Type B does not penalise own ops |

**"Defending faction's assets" definition:** Pending Art 04/05. Expected: districts where the defending faction holds Established or Dominant presence, or districts containing their structure blocks.

**Multiple Type B edge case:** If two factions each play a Type B in the same Quarter, they apply independently. An operation targeting assets that satisfy two distinct Type B conditions accumulates M-11 twice (−30 total).

---

### DT-08 — Apex Activation Threshold Check (Step 4)

After all Emergency Responses resolve, ARBITER counts Board Strength for the Apex faction. This check gates whether Apex resolves or is cancelled.

**Board Strength formula:** `Σ Board.PresenceChips[D-xx][apex_faction] + Σ Board.StructureBlocks[D-xx][apex_faction]` (all districts, all types).

| ID | Board Strength vs. Threshold | Outcome |
|----|------------------------------|---------|
| DT-08-A | board_strength ≥ threshold_required | Apex resolves — proceed to Step 5; session ends |
| DT-08-B | board_strength < threshold_required | Apex cancelled — resources spent; Operative does not retire; resolution resumes |

**Threshold source:** `apex_card.ApexThreshold` — defined in Art 05 per Operative. Pending Art 05 completion.

**Resumption after DT-08-B:** Beat_3 resumes from the suspended position in `Grid.ResolutionQueue`; Beat_4 resumes from the suspended faction in initiative order. Board effects from Emergency Responses remain — they are not reversed.

---

### DT-09 — Emergency Response Role (Assist / Thwart Apex)

Each non-Apex faction submits exactly one Emergency Response. All submitted simultaneously, resolved in `Quarter.InitiativeOrder` (excluding the Apex faction). Board state changes apply immediately — each Emergency Response takes effect before the next is resolved. Board Strength is counted once, after all Emergency Responses, at DT-08.

*Full Emergency Response design pending Art 04 / Art 05.*

| ID | Emergency Response Role | Board Effect | Board Strength Impact at DT-08 |
|----|------------------------|-------------|-------------------------------|
| DT-09-A | Assist | Adds presence chips or structure blocks to Apex faction's count | Raises Board Strength |
| DT-09-B | Thwart | Removes presence chips or structure blocks from Apex faction | Lowers Board Strength |
| DT-09-C | Neutral / Other | Affects board state unrelated to Apex faction (own presence, Public Standing, etc.) | No direct Board Strength impact |
| DT-09-D | Pass | No board effect | None |

**Design note (Art 03 §16):** "A faction may use their Emergency Response to assist the Apex (raising Board Strength) or oppose it (reducing Board Strength). This is load-bearing for Emergency Response design in Artifact 04 / Artifact 05."

---

### Apex_Activation() — Procedure

Called from Beat_3 (covert) and Beat_4 (political act) when an Apex card with `card.Face = Up` is reached. Halts the calling Beat — Beat_3 and Beat_4 do not return after this call unless the Apex is cancelled (DT-08-B).

```
Apex_Activation(apex_card, apex_faction):

// Step 1 — Announce
ARBITER announces: "An Apex operation has been submitted. Resolution is suspended."

// Step 2 — Payment confirmation (Beat 4 political act path only)
// Note: Beat 4 apex with Face = Up means payment was validated at Submit Payment.
// The DT-02 face assignment at Beat 0 (covert path) already ensured Face = Up implies full payment.
// No additional payment check needed — guaranteed by DT-01/DT-02 preconditions.

// Step 3 — Emergency Response collection (DT-09)
COLLECT one Emergency Response simultaneously from each faction f WHERE f ≠ apex_faction
FOR EACH f IN Quarter.InitiativeOrder WHERE f ≠ apex_faction:
  RESOLVE Emergency Response[f]
  // Immediately mutates: Board.PresenceChips, Board.StructureBlocks, Faction.PublicStanding
  // per card text; changes applied before next Emergency Response resolves

// Step 4 — Board Strength threshold check (DT-08)
board_strength ←   Σ Board.PresenceChips[D-xx][apex_faction]
                 + Σ Board.StructureBlocks[D-xx][apex_faction]
threshold_required ← apex_card.ApexThreshold  // Art 05

IF board_strength < threshold_required:         // DT-08-B — cancelled
  ARBITER announces: "The threshold was not met. The operation is cancelled."
  // Resources already drained — not refunded; Operative does not retire
  RESUME Beat_3 from current Grid.ResolutionQueue position
      OR Beat_4 from current faction in initiative order
  RETURN

// Step 5 — Apex resolves  (DT-08-A)
ARBITER opens sealed Apex envelope (prepared at session setup — Art 05)
PAUSE 5 seconds
ARBITER reads Apex narrative card aloud (The Witness register)
APPLY all public board effects specified in Apex card
ARBITER privately updates Faction.ChorusPortrait[F-xx] for all factions
SESSION ENDS — proceed to Artifact 10a — Victory System
```

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
| M-12 | District | The Mid — no adjacent Core | All | Persistent | 1 | Fixed | −25 |

*Source: Art 03 §14.*

*M-01–M-05 are mutually exclusive — exactly one Standing modifier applies per faction per resolution, derived from `Faction.PublicStanding[f]` via the `M_standing()` helper in §5.*

*M-08, M-09, M-10, M-12 variable rows are fully specified here for Fixed modifiers; variable values pending Art 04 card definitions. Balance analysis (modifier stack mathematics) is the planned Tier 4 of this artifact, blocked until all M-xx values are defined.*

**Correction note:** The §7 table in v0.2 contained values from a prior design iteration (M-01: "Critical Success −25", M-02: "Critical Failure +25", etc.) that do not match Art 03 §14. Critical Success and Critical Failure are resolution rules, not modifier stack entries. The corrected table above is authoritative. All §5 Beat Procedures reference this version.

---

## 8. Design Notes

**Source of truth:** Art 03 is the current authoritative specification. This document is a formalization layer — where 03a contradicts 03, the inconsistency must be investigated. The conflict may reflect an error in 03a's formalization, or it may surface an ambiguity, edge case, or gap in Art 03 that prose obscured. Either outcome is a design finding requiring resolution and, if necessary, refinement of Art 03.

**Tier 2 implication:** The Beat Procedures in Tier 2 are intended to be directly translatable to a server-side game engine (Tier 2 architecture). The TypeScript schema in Retired/Electronic/old__08_DATA_MODEL.md is the target Tier 2 data model; 00b entity IDs should align to it.

**Modifier balance analysis:** Once all modifier rows (M-01–M-12) are fully specified, the summation formula in Beat_3() enables a full balance analysis: expected difficulty shift per modifier combination, pathological stack identification, and recommendation for modifier caps if needed.

---

### Open Design Findings (surfaced by Tier 2 formalization)

| ID | Section | Finding | Action Required |
|----|---------|---------|-----------------|
| DF-01 | Beat_1/2 | ✅ Resolved — Session 22 (L112). Art 03 Beat 1 used "Operation Failed"; Beat 2 used "Operation Blocked." Both unified as **"Voided"** (RO-03). Verb form chosen: past participle implies ARBITER action without naming cause. Art 03 Beat 1/2, Beat 5 example, and 00b RO-03 all updated. | — |
| DF-02 | Beat_4, §7 | ✅ Resolved — Session 22 (L113). Threshold convention adopted throughout. Art 03 beat prose updated: "+50 difficulty marker" → "−50 threshold marker" in Beat 0 table and Beat 4 prose. Rationale: threshold framing is positively oriented — players think "I need to roll under 69," not "I have a 31% chance to fail." All references now use threshold-subtractive sign convention matching the modifier table (M-06/M-07 = −50). | — |
| DF-03 | §4.1 Faction Domain | ✅ Resolved — Session 22. `Faction.Resources[F-xx][RT-xx]` Mutates At split into five distinct entries: Upkeep Step 5 (income); Beat 0 (covert payment drain); Phase 4 Declaration (tokens → Grid.Political.ResourceStake); Beat 4 Submit Payment (ResourceStake → Reservoir); Beat 3/4 failure conditions (card text penalties); Debrief (trades, conversion). | — |
| DF-04 | §4, §5 | ✅ Resolved — Session 22. (a) Case (CA-xx) added to 00b §4 entity registry and §6 schema status — indexed via F-xx in Tier 1, CA-xx prefix anticipates Tier 2+. (b) Packet and (c) GridCell noted in 00b §4 as internal 03a modeling types (no persistent IDs; not registered entities). (d) IP-xx already registered in 00b §4 and §6 — ID column will be added to Art 03 §7 table at Art 03 sign-off. | — |

---

## 9. Modifier Balance Analysis

*Stub — blocked until all M-xx values fully specified.*

Tier 4 derives from the summation formula in Beat_3() and Beat_4(). Once M-08, M-09, and M-10 variable values are defined by Art 04 card definitions, the following analysis becomes executable:

**Planned output:**

| Analysis | Method | Blocked on |
|----------|--------|-----------|
| Expected threshold shift per modifier combination | Enumerate all valid M-xx combinations; sum Threshold Adjustment values | M-08, M-09, M-10 variable rows (Art 04) |
| Pathological stack identification | Flag combinations where total shift causes threshold ≤ 0 or ≥ 100 (ignoring 01–05 / 96–100 override floors) | Same |
| Modifier cap recommendation | If pathological stacks identified: propose per-resolution cap or interaction rules for 00a | Same |

**Known fixed contributions (already specifiable):**

| Scenario | Modifiers Active | Fixed Threshold Shift |
|----------|-----------------|----------------------|
| Celebrated, full payment, no other modifiers | M-01 | +20 |
| Discredited, partial payment | M-05 + M-06 or M-07 | −70 |
| Discredited, partial payment, Type B target, The Mid | M-05 + M-06 + M-11 + M-12 | −110 (threshold ≤ 0 at most base difficulties) |
| Celebrated, full payment, The Mid mitigated by Core presence | M-01 | +20 (M-12 suppressed by DT-06-A) |

**Pathological stack note:** The −110 scenario above forces threshold below 0 at all base difficulties except Very Easy — the only path to success is the 01–05 Critical Success override (DT-03). This is a known extreme and may be intentional design consequence for discredited factions attempting difficult covert ops under compounded conditions. Flag for playtest validation.

---

*End of Art 03a — Game Engine Specification v0.97*
