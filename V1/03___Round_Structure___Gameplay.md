# 03 — Quarter Structure & Gameplay
## THE SIGNAL P1 — Paper Prototype

**Version:** 4.11

**Status:** Signed off S110 (L232). Prior: Signed off S104 (L217). S109–S110: VM-xx lifecycle formalised — §9.4.1.1 VM-xx check added to BEC step; §9.4.2.2.0 VM-xx placement clause; §9.4.3.0.1 renamed Initiative Loop (BEC application moved to per-PA step); §9.4.3.1.3 Apply BEC Modifiers added (mirrors §9.4.1.1 language); §9.4.3.1.4 Base Difficulty (renumbered from 1.3); §9.4.3.3.0 generic VM-xx placement clause. Beat 4 boost detection clause added to §9.4.3.1.0.0 (S109). §9.4.3.3.0 BEC-specific reveal clause removed — VM-xx model supersedes. §9.2.0 Target Profile placed face-down at declaration; §9.4.3.1.1 Target Profile flipped face-up at Apex Check step.

**Depends on:** 00 — Factions, World & Narrative Context; 01 — Game Board: New Meridian; 02 — Components

**Supersedes:** round_structure (retired artifact)

---

## 1. Overview

### Problem This Document Solves
Without a precise, ordered description of how each Quarter is structured — what happens, in what sequence, who does it, and what information is available when — no artifact describing specific actions, resolutions, or ARBITER behavior can be written consistently. This document is the skeleton that all subsequent system artifacts attach to.

### Deliverable
The main game loop of THE SIGNAL: the repeatable quarterly sequence that frames all downstream procedures. Six sections — Upkeep, Placement, three Monthly Activity loops (each containing six resolution beats), Resolve District Tension, Quarterly Debrief, and Quarter Close. For each step: who acts, what the action is, and what sequencing constraints apply. Specific procedures — card resolution, ARBITER scripts, component mechanics — live in downstream artifacts and are called from this loop.

### Success Criteria
- The quarterly sequence is complete — every section, beat, and transition has a defined actor and a clear entry/exit condition
- Any downstream procedure can identify its entry point in this document
- This document frames the loop; it does not implement the subroutines — no specific card procedure, ARBITER script, or component mechanic is hardcoded here
- Players and ARBITER can always locate themselves in the Quarter and know what comes next
- No undefined terms from prior artifacts (00–02b)

---

## 2. Index

1. [Overview](#1-overview)
2. [Index](#2-index)
3. [Game Purpose](#3-game-purpose)
4. [Narrative Function](#4-narrative-function)
5. [Design Principles](#5-design-principles)
6. [Quarter Overview](#6-quarter-overview)

**Quarterly Loop**

7. [Upkeep](#7-upkeep)
8. [Placement](#8-placement)
9. [Monthly Activities](#9-monthly-activities)
   - [§9.0 Start of Month](#90-start-of-month)
   - [§9.1 Covert Dispatch](#91-covert-dispatch)
   - [§9.2 Public Declaration](#92-public-declaration)
   - [§9.3 Countermeasures](#93-countermeasures)
   - [§9.4 Resolution](#94-resolution)
     - [Beat 0: The Cases Open](#940-beat-0-the-cases-open)
     - [Beat 1: Read Board State](#941-beat-1-read-board-state)
     - [Beats 2 and 3: Covert Operations Resolve](#942-beats-2-and-3-covert-operations-resolve)
     - [Beat 4: Public Acts Resolve](#943-beat-4-public-acts-resolve)
     - [Close Month](#944-close-month)
10. [Resolve District Tension](#10-resolve-district-tension)
11. [Quarterly Debrief](#11-quarterly-debrief)
12. [Quarter Close](#12-quarter-close)

**Reference Material**

13. [The Operation System](#13-the-operation-system)
14. [Apex Activation](#14-apex-activation)
15. [Duration Taxonomy](#15-duration-taxonomy)
16. [Public Act Placement Rules](#16-public-act-placement-rules)
17. [Countermeasure Card Rules](#17-countermeasure-card-rules)
18. [React Card Rules](#18-react-card-rules)
19. [Influence Level Reference](#19-influence-level-reference)
20. [Resource Generation Reference](#20-resource-generation-reference)
21. [Card Economy Reference](#21-card-economy-reference)
22. [Board State Update Rules](#22-board-state-update-rules)
23. [Public Standing Scale](#23-public-standing-scale)
24. [Resolution State Reference](#24-resolution-state-reference)

**Appendices**

[§ Primitive Action Model](#primitive-action-model-taxonomy-reference)
[§ Examples & Exceptions](#examples-exceptions)

---

## 3. Game Purpose

The Quarter is the unit of consequence in THE SIGNAL. It gives the session its rhythm — a repeatable loop that moves from situational awareness to positioning to committed action to reckoning, then pauses for the table to assess what the cycle produced before the next one begins.

The loop's structure determines when information flows and when it locks. Every downstream system — card resolution, district contests, ARBITER judgment — operates within a moment this loop defines.

Eight Quarters constitute a session. The session ends at the completion of Quarter 8 or when an Apex ability resolves — whichever comes first.

---

## 4. Narrative Function

The narrative function of the game loop is to give the fiction of THE SIGNAL its temporal and operational shape. A Quarter represents three months of real-world operation — long enough for faction strategies to take hold, short enough that each Quarter's outcome reshapes the terms of the next.

The loop's sequence mirrors how organizations actually operate under pressure: situational awareness before commitment, action conducted across both the covert and public register, a reckoning over contested ground, then the conversation about what it meant. The structure is not arbitrary — it is the shape of how power moves.

ARBITER is present throughout but speaks at specific moments. Between those moments, ARBITER watches.

Full narrative grounding — what each action means at scale, faction doctrine, the Chorus timeline — is in Art 00.

---

## 5. Design Principles

1. **One actor per step.** Each step names exactly one actor type — ARBITER or Faction Player. Steps requiring both are split. No step leaves ambiguity about who acts.

2. **Loop over procedure.** This document defines sequence and transitions. Where a subroutine exists — card resolution, ARBITER scripts, component mechanics — this document names the entry point and references the downstream artifact. No subroutine detail belongs here.

3. **Every exit has an entry.** Each section and beat names its successor explicitly. The loop has no implicit transitions or dead ends.

4. **Linearly executable by ARBITER.** Sections are ordered so ARBITER can follow them without backtracking or holding memorized state. Complexity lives in reference tools, not in memory. *(→ 00a §4.7 ARBITER Cognitive Efficiency; 00a §8 Footprint Rules)*

5. **Scope discipline.** Content that belongs to a downstream artifact is not reproduced here. A persistent stub in this document is a scope violation, not an open question — resolve it by writing the downstream artifact, not by expanding this one.

6. **Component and state traceability.** Every component and game state touched by the loop has a traceable path — where it enters, where it changes, and where it exits. Initial entry points are defined in 03-init; the loop accounts for all subsequent transitions. *(Full validation of this principle gates on 03-init design pass.)*

7. **Step 0 convention.** All procedural step sequences begin at Step 0. This applies uniformly across sections, beats, and subroutines — including Apex, React, and any referenced downstream procedures. Step 0 represents the first executable action in the sequence.

---

### Section Review Rubric

Apply to each section before sign-off:

- [ ] Every step has a named actor
- [ ] The section has a named entry point and explicitly names its successor
- [ ] No subroutine procedure is implemented here — downstream callouts are references, not stubs
- [ ] A player or ARBITER reading this section knows where they are in the Quarter and what comes next
- [ ] ARBITER can execute this section without holding memorized state from prior sections beyond what is physically on the board
- [ ] Every component introduced or modified in this section has a traceable source and destination *(gate: 03-init design pass)*

---

## 6. Quarter Overview

The complete quarterly loop — six sections in sequence. Each line is an entry point; full procedures are in the sections that follow.

```
§7 UPKEEP
  Quarter opens. World updates. Resources collected. Tokens distributed. Initiative set.

§8 PLACEMENT
  Deployment Markers placed. Entry requirements enforced.

§9 MONTHLY ACTIVITIES  ×3
  §9.0  Start of Month — PA obligations checked.
  §9.1  Covert Dispatch — cases assembled, sealed, transmitted.
  §9.2  Public Declaration — Public Acts declared in initiative order; placed face-up on Overview.
  §9.3  Countermeasures — CM cards submitted; may target queued covert ops or placed Public Acts.
  §9.4  Resolution:
    §9.4.0  Beat 0: The Cases Open
    §9.4.1  Beat 1: Read Board State
    §9.4.2  Beats 2 and 3: Covert Operations Resolve
    §9.4.3  Beat 4: Public Acts Resolve
    §9.4.4  Close Month
  Repeat for Months 2 and 3. Month 3 Close Month: do not advance month — proceed to §10.

§10 RESOLVE DISTRICT TENSION
  Contested districts resolve. d10 roll-off per district. Tension Markers cleared.

§11 QUARTERLY DEBRIEF
  Table reflects on outcomes. ARBITER delivers Summary, Observation. Ready-to-close mechanic.

§12 QUARTER CLOSE
  Seasonal cleanup. Findings decay. Debrief reward. NS-xx returned. Quarter/Month tracker advanced.
```

Sections do not overlap. ARBITER announces the start of each section.

---

## Quarterly Loop

## §7 Upkeep

*Entry: Q1 — 03-init complete; Q2–Q8 — §12.4 Quarter Close complete.*

ARBITER announces each step. Faction Players perform their own updates.

### §7.0 Status Marker Reset

Each Faction Player flips their Status Marker to the Discussing side (yellow/text).

*This is the physical act that opens the Quarter — a personal acknowledgment that a new quarter of operations has begun and the previous Quarter is fully closed.*

---

### §7.1 Initiative

ARBITER determines initiative order and announces the final order. The ARBITER Player updates the Initiative Strip on the board.

*Full procedure: Artifact 07 — ARBITER Toolkit.*

---

### §7.2 Situation Report

*The Situation Report is ARBITER's Public Act for the Quarter. The Broadcast Card placed on the Overview is a standing Public Act with Seasonal duration by default (active until End of Quarter) unless the card specifies otherwise. It is a valid target for faction Public Acts and countermeasures once placed. Beat 1 reads SitRep effects as standing Public Acts each month.*

ARBITER announces: *"Situation Report."*

#### §7.2.0 Step 0: Draw Broadcast Card

The ARBITER Player draws the top Broadcast Card from the Broadcast Deck and places it face-up in the Situation Report Zone on The Overview.

#### §7.2.1 Step 1: Locate Broadcast Effect Card

The ARBITER Player locates the matching Broadcast Effect Card from the Broadcast Effect Deck and places it on the ARBITER Tableau.

#### §7.2.2 Step 2: Read Broadcast Effect Card

The ARBITER Player reads the Broadcast Effect Card.

#### §7.2.3 Step 3: Announce Standing Track Changes

ARBITER reads the indicated narrative on the Broadcast Card aloud.

*Do not announce difficulty modifiers or hidden mechanical effects.*

#### §7.2.4 Step 4: Update Faction Markers

Each Faction Player moves their Public Standing Marker as indicated by ARBITER.

#### §7.2.5 Step 5: Apply Blocked Markers

If the Event Card specifies a Deployment Marker cannot convert this Quarter: The ARBITER Player flips the affected marker(s) to the Blocked face.

#### §7.2.6 Step 6: Expire Previous Broadcast Effect Cards

The ARBITER Player reviews all Broadcast Effect Cards on the ARBITER Tableau and moves expired cards to the expired area.

*No tick-downs or maintenance — duration management occurred at the close of the previous Quarter.*

---

### §7.3 Deployment Marker Conversion

ARBITER announces: *"Markers convert."*

#### §7.3.0 Step 0: Check Marker Faces

Each Faction Player checks Deployment Markers currently on the board.

#### §7.3.1 Step 1: Convert Markers

For each marker showing the Converting face: place 1 permanent Presence Token in that district and return the marker to hand.

#### §7.3.2 Step 2: Return Blocked Markers

For each marker showing the Blocked face: return the marker to hand without placing a Presence Token.

#### §7.3.3 Step 3: Update Board State

Each Faction Player updates Dominant Markers, Established Markers, and Tension Markers as influence levels shift from new Presence Token placements. Any marker removed in this update is returned to ARBITER supply. See §22 for placement and removal triggers.

*If no markers are on the board — as is always the case at the start of Quarter 1 — this section has no effect.*

Proceed to §7.4.

---

### §7.4 Resource Collection

ARBITER announces: *"Collect income."*

Each Faction Player simultaneously calculates and collects their own resources. Other Faction Players observe and may challenge calculations. ARBITER resolves disputes in The Record register.

**The Network — University Perimeter Virtual Structure:** The Network faction has a virtual Structure Block at University Perimeter from session start. It cannot be demolished and does not count toward the one-structure-per-faction-per-district limit. It functions as a Structure Block for all game purposes — income, Modifier Card draw threshold, ring modifier eligibility, and any mechanic referencing owned Structure Blocks. It generates income only while The Network has any presence (chip or Deployment Marker) at University Perimeter; if The Network holds no presence there, the virtual structure produces nothing that Quarter.

#### §7.4.0 Step 0: Calculate District Income

For each district with Presence Tokens or Deployment Markers: apply influence level modifier to base generation value.

#### §7.4.1 Step 1: Apply Affinity Bonus

Add affinity bonus where applicable — per §20.

#### §7.4.2 Step 2: Declare Structure Block Resources

For each Structure Block: declare resource type publicly (district resource or faction Native Resource), collect income per §20.

*If The Network has any presence at University Perimeter: The Network Faction Player declares whether Exposure or the district Native Resource will be collected from the virtual Structure Block.*

#### §7.4.3 Step 3: Collect Passive Generation

Add passive generation per §20.

---

### §7.5 Operations Preparation

ARBITER announces: *"Prepare operations."*

*Purpose: ensure all elements needed for the Quarter are assembled and in their correct positions on the tableau. Faction Players complete this step simultaneously.*

#### §7.5.0 Dispatch Token Distribution

Each Faction Player collects Dispatch Tokens from The Backlog — per §21 Dispatch Token Allotment.

*Tokens are held beside the tableau. They are spent across Months 1, 2, and 3 as the player chooses.*

#### §7.5.1 Tableau Verification

Verify the following elements are already in position before drawing begins:

- Floor Act — beside tableau, always available to all factions at all times (full design: Artifact 04 D04-13)
- Countermeasure Cards — in their designated area (3 per session total; deployed across Monthly Countermeasure phases)
- Modifier Cards carried from prior Quarters — in modifier area
- Operator cards — in their designated area

#### §7.5.2 Action Card Draw

##### §7.5.2.0 Step 0: Draw Covert Cards

Count Covert Operation Cards currently in hand. Draw from personal draw deck to reach covert hand size — per §21.

##### §7.5.2.1 Step 1: Draw Public Act Cards

Count Public Act Cards currently in hand. Draw from Public Act draw deck to reach Public Act hand size — per §21.

##### §7.5.2.2 Step 2: Place Drawn Cards

Place all drawn cards in the active hand area of the tableau. Cards are held face-down and private.

*Cards kept from the prior Quarter count toward hand size — a player with kept cards draws only enough to reach the hand size limit (per §21).*

*Covert Operation hand is drawn here only. No additional covert cards are drawn during Monthly Dispatch. Discard down if hand size exceeds maximum at any point.*

*If a draw deck is exhausted mid-draw, shuffle that deck's discard pile immediately to form a new draw deck and continue. Both decks reshuffle independently.*

#### §7.5.3 Modifier Card Draw

*A faction that has triggered Burst Play this session is exempt from Modifier Card draws — skip this sub-section.*

Draw and place Modifier Cards in the tableau modifier area.

##### §7.5.3.0 Step 0: Faction Modifier Draw

Draw from the Faction Modifier Deck in the player's tableau — per §21 Modifier Card Draw table.

*The Network's virtual Structure Block at University Perimeter counts toward this total while Network holds any presence in that district.*

##### §7.5.3.1 Step 1: Ring Modifier Draw

A ring qualifies if the faction meets all of the following conditions:
- At least 1 Structure Block in that ring
- Established or higher presence in at least 1 district in that ring

Draw 1 card for each qualifying ring. A faction may qualify for all three rings.

*The Network's virtual Structure Block at University Perimeter counts toward the Structure Block condition for its ring while Network holds any presence in that district.*

*Modifier Decks (faction and ring) are not reshuffled when exhausted.*

##### §7.5.3.2 Step 2: Burst Play Window

After completing all draws, before Dispatch opens, a faction may trigger Burst Play. If triggered:

1. Declare Burst Play to ARBITER.
2. Trade ALL held Modifier Cards to the Reservoir — 1 resource of any type per card, chosen independently per card.
3. ARBITER announces publicly: *"[Faction] has liquidated their operational reserve."* Resource gain is private.
4. Remove the Faction Modifier Deck from the tableau. It does not return for the remainder of the session.

*Modifier draws are skipped at all future Hand Assembly steps for this faction.*

*Full card draw rules, deck construction, hand size, Modifier Card rules, and Burst Play are specified in Artifact 04 §12.*

Upkeep complete. Proceed to §8 Placement.

---

## §8 Placement

*Entry: §7 Upkeep complete.*

Faction Players place their own markers. ARBITER enforces entry requirements.

ARBITER announces: *"Placement is open."*

### §8.0 Step 0: Place Markers in Initiative Order

Faction Players place their two Deployment Markers in initiative order, snake pattern:

- **Forward pass:** Rank 1 through Rank 5, one marker each
- **Reverse pass:** Rank 5 through Rank 1, second marker each

*All Deployment Markers are placed with the Converting face showing by default.*

*A Deployment Marker counts as 1 temporary Presence Token immediately upon placement.*

### §8.1 Step 1: Verify Entry Requirements

Before placing in each district:

| Ring | Entry Requirement |
|------|-------------------|
| Baryo | None |
| The Mid | None |
| Core | Established or higher in an adjacent The Mid district (permanent Presence Tokens or temporary presence from first marker this phase) |
| Chorus Node | Established or higher in an adjacent Core district (permanent Presence Tokens or temporary presence from first marker this phase) |

*Ring adjacency penalties apply during operation resolution, not placement. See §13 M-12.*

### §8.2 Step 2: Update Board State

After each placement, if influence levels change: the placing Faction Player updates the relevant Dominant Marker, Established Marker, or Tension Marker immediately. Any marker removed in this update is returned to ARBITER supply. See §22 for placement and removal triggers.

*Both Deployment Markers must be placed each Placement phase, beginning Q1M1. Both may be placed in the same district. ARBITER redirects illegal placements.*

Placement complete. Proceed to §9 Monthly Activities.

---

## §9 Monthly Activities

*Entry: Month 1 — §8 Placement complete; Months 2–3 — §9.4.4 complete. Repeats three times; exit via §9.4.4 each month.*

**Dispatch Token rule:** Each action requires 1 Dispatch Token. Covert Operations: token placed in the Dispatch Case with the operation card (§9.1). Public Acts: token placed on the declared card on the Overview (§9.2). A Covert Operation Card submitted without a token is rejected by ARBITER at Beat 0 without resolution and returned to the faction. A Public Act declared without a token is invalid.

*Faction Players budget their Dispatch Tokens across Months 1, 2, and 3, split between Covert Operations and Public Acts as they choose. Not spending a token is a pass for that action.*

---

### §9.0 Start of Month

*Entry: §9 Monthly Activities opens (Month 1) or §9.4.4 complete (Months 2–3).*

Before §9.1 Covert Dispatch opens, ARBITER checks for active Public Acts with Covert Dispatch obligations. If none: proceed to §9.1.

For each active card with a Covert Dispatch obligation:

#### §9.0.0 Step 0: Announce Obligation

ARBITER announces: card name, declaring faction, target faction, and the required election.

#### §9.0.1 Step 1: Elect

Target faction elects comply or resist.

#### §9.0.2 Step 2: Execute

ARBITER executes per the card spec:

- **Comply:** apply comply effect. If the card's `persistence_condition` is now satisfied, card clears after §9.1 closes.
- **Resist:** apply resist effect. Card remains in play. If resist disables covert dispatch: that faction skips §9.1 Steps 1–3 and submits no case this Month.

§9.0 complete. Proceed to §9.1 Covert Dispatch.

---

### §9.1 Covert Dispatch

*Entry: §9.0 complete.*

Faction Players assemble, seal, and transmit their own Dispatch Cases. The ARBITER Player keeps watch on the Dispatch Timer, announces status, and queues cases in the order received.

#### §9.1.0 Step 0: Open Dispatch

ARBITER announces: *"Dispatch is open."* The ARBITER Player starts the dispatch timer.

#### §9.1.1 Step 1: Assemble Cases

Faction Players load operation cards, Dispatch Tokens (1 per operation card), resources, Target Profiles, and any Modifier Cards being assigned to specific operations into their cases.

*Modifier Cards (drawn at §7.5.3) are assigned to operations by placing each card in the case with that operation's packet. A faction may assign Modifier Cards to some, all, or none of their submitted operations. Unassigned Modifier Cards remain in the tableau modifier area and are not submitted.*

*Assembly should be handled privately and silently.*

*Full Dispatch Case design, physical format, and component contents: Artifact 06 — Messaging System.*

#### §9.1.2 Step 2: Seal Cases

Faction Players close their cases. No additions or changes permitted after sealing.

#### §9.1.3 Step 3: Transmit Cases

Faction Players place their sealed cases in the ARBITER Player's receive queue. The ARBITER Player places each received case left to right in the receive queue, establishing lane order for the Resolution Grid.

*Case receipt order determines lane assignment in the Resolution Grid and governs Beat 3 operation sequence.*

#### §9.1.4 Step 4: Close Dispatch

The ARBITER Player announces: *"Timer."*

*No new additions to any case — sealed or open.*

The ARBITER Player counts: *"Five. Four. Three. Two. One."*

*Faction Players who have not transmitted may seal and transmit during the countdown.*

The ARBITER Player announces: *"Dispatch closed."*

*Any case not received is treated as containing no Covert Operations.*

§9.1 closed. Proceed to §9.2 Public Declaration.

---

### §9.2 Public Declaration

*Entry: §9.1 Covert Dispatch closed.*

Faction Players declare publicly, in initiative order. The ARBITER Player records declarations.

ARBITER announces: *"Public Declaration is open."*

#### §9.2.0 Step 0: Declare in Initiative Order

For each Faction Player in initiative order, one of:

**Pass** — verbally declare no Public Act will be played this phase.

**Declare** — name the Public Act and place it on the board:

1. Announce the Public Act being declared.
2. Place the declared card face-up in the unresolved PA zone of the Faction Resolution Grid, with 1 Dispatch Token and resource tokens on the card. Place the Target Profile face-down on the card. Resource tokens remain with the declared card — payment submitted to the Reservoir at Beat 4.
3. Play any Modifier Cards modifying the Public Act face-up alongside the card in the Faction Resolution Grid.

*Once placed, the card is a valid target for countermeasures (§9.3) and other Public Acts.*

*Declared Public Acts cannot be withdrawn or modified after placement.*

#### §9.2.1 Step 1: Close Declaration

ARBITER announces: *"Public Declaration closed."*

§9.2 closed. Proceed to §9.3 Countermeasures.

---

### §9.3 Countermeasures

*Entry: §9.2 Public Declaration closed.*

Faction Players deploy or pass in initiative order. The ARBITER Player holds Countermeasures for application during Resolution (§9.4).

ARBITER announces: *"Countermeasure Window is open."*

#### §9.3.0 Step 0: Deploy in Initiative Order

For each Faction Player in initiative order, one of:

**Pass** — verbally declare no Countermeasure Card will be played.

**Deploy** — declare "Countermeasure" and choose one play mode for each card:

- **Submit to ARBITER** — hand the card face-down to the ARBITER Player. Applies to all Covert Operations targeting your faction; ARBITER matches to all relevant operations at Beat 0 (§9.4.0.1).
- **Play publicly** — place the card face-up in the CM zone of your Faction Resolution Grid. Applies at the appropriate resolution beat to all operations targeting your faction.

*CMs are keyed to the playing faction. Full CM card rules: §17.*

*Each faction has 3 Countermeasure Cards per session total across all three Monthly windows. Cards spent here are unavailable in Months 2 and 3.*

#### §9.3.1 Step 1: Confirm Countermeasure Placement

**Submitted CMs:** The ARBITER Player attaches each received card to the relevant faction's Dispatch Case in the receive queue. ARBITER matches to all targeted operations within sealed cases at Beat 0 (§9.4.0.1).

**Publicly played CMs:** Already in position on the Faction Resolution Grid. No further placement required.

ARBITER announces: *"Countermeasure Window closed."*

§9.3 closed. Proceed to §9.4 Resolution.

---

### §9.4 Resolution

The ARBITER Player runs Resolution in six sequential beats. Faction Players receive outcomes and apply their own board updates.

*The Resolution Grid is built fresh each month and cleared at end of Beat 3.*

*Beat 3 processes row-first across all lanes: all card-1 pairs resolve left to right before any card-2 pair begins. Round-robin initiative by case receipt — submission speed rewards getting your first operation in, not locking in a full sequence before others act. (L102)*

*ARBITER announces each beat before beginning it.*

---

#### §9.4.0 Beat 0: The Cases Open

*Entry: §9.3 Countermeasures closed.*

**Beat Summary:** ARBITER positions and opens all Dispatch Cases, validates payment, and builds the Resolution Grid.

##### §9.4.0.0 Step 0: Position and Open Cases

Cases are in receipt order from §9.1.3. Position each case above its assigned lane and open.

##### §9.4.0.1 Step 1: Process Cases Lane by Lane

From left to right, lane by lane:

0. If any Countermeasure Cards are attached to this case (§9.3.1): place each in the Beat 1 row of this lane.

   *At Beat 1, each CM applies to all operations in the grid whose Target Profile matches the CM's keyed faction.*

1. Remove the first operation packet from the case.

2. For each card in the packet, validate payment:

   | Payment | Applies to | Resources | Card Placement |
   |---------|------------|-----------|----------------|
   | Full | All | Drain to Reservoir | Face-up in grid |
   | Partial | Non-Apex | Drain to Reservoir; attach partial payment threshold marker (M-06) to stack | Face-up in grid |
   | Zero | Non-Apex | None to drain | Face-down in grid |
   | Any shortfall | Apex | Drain any submitted resources to Reservoir | Face-down in grid |
   | Retained | Resource-retaining cards | Validate resource count matches declared value on Target Profile; resources declared are placed on card — do not drain to Reservoir. Any unallocated resources are placed in target_faction's Dispatch Case. | Face-up in grid |

   *If any Intel Token is submitted as part of payment, calculate age for each token — per §13 Intel Token Age table.*

   *All submitted Intel Tokens are reset (erased) and returned to The Dossier, or discarded if single-use.*

   *Quarter number and faction are written on each token by ARBITER at issuance. Physical form TBD — see PM05 03-13. Expired tokens not submitted have no payment value but may be held and traded — age is visible on the token.*

3. Drain resources to the Reservoir as directed.

   *For each card with a `boost` field (value ≠ None): after base cost is drained, count any excess resources remaining in the packet. Calculate n = floor(excess ÷ boost unit cost). If n > 0: retrieve n BM-xx tokens from ARBITER supply and place them on the card's grid slot. Drain all remaining excess to the Reservoir. No excess is returned to the faction.*

4. Place each validated card in the grid:
   - Beat 2 card: place in the Beat 2 row of the lane being processed.
   - Beat 3 card or Pass: place in the uppermost vacant space in the Beat 3 section of the lane. Stack bottom to top: Target Profile, Modifier Cards (if any), operation card (or pass). Overlap so each card beneath shows its resolution data block.

   *Cards are placed face-up or face-down per Payment Validation.*

   *(Modifier Card application procedure and ring modifier per-token rate: Art 07 — ARBITER Toolkit.)*

   **Resolution Grid layout:** *[flag: detail work pending — row definitions, stack orientation, physical format TBD]*

   | | Lane 1 | Lane 2 | Lane 3 | Lane 4 | Lane 5 |
   |---|--------|--------|--------|--------|--------|
   | *(case receipt order →)* | first received | | | | last received |
   | Beat 1 row (CM cards) | | | | | |
   | Beat 2 — op | | | | | |
   | Beat 2 — target | | | | | |
   | Beat 3 — op | | | | | |
   | Beat 3 — target | | | | | |
   | *(one op+target pair per card submitted; Beat 2 + Beat 3 pairs ≤ 4 per lane — one per Dispatch Token)* | | | | | |

   *Beat 4 processes placed Public Acts on the Overview — Public Acts do not appear in the Resolution Grid.*

   *Modifier Cards are splayed beneath the operation card to display their values during resolution. Modifier Card physical design must support cascade orientation — value printed prominently at both top and bottom edge. (XA-22, Art 11)*

5. If a Dispatch Token accompanies the card: set aside the token. If no Dispatch Token accompanies the card: flip the operation card face-down; remove attached Modifier Cards from the game.

6. Repeat sub-steps 0–5 for each remaining packet in the lane, then advance to the next lane. Repeat until all lanes are processed.

   *If card order within a case was disrupted in transit, the order ARBITER encounters the cards is the resolution order.*

##### §9.4.0.2 Step 2: Collect Dispatch Tokens

Collect all Dispatch Tokens from this Month. Return to The Backlog.

Beat 0 complete. Proceed to §9.4.1 Beat 1.

---

#### §9.4.1 Beat 1: Read Board State

*Entry: §9.4.0 complete. Resolution Grid built; CM cards in Beat 1 rows.*

**Beat Summary:** ARBITER processes standing board effects one by one — clockwise from ARBITER's left — then Broadcast Effect Cards, then CM cards.

##### §9.4.1.0 Step 0: Process Standing Board Effects

Starting from ARBITER's left, proceeding clockwise around the table, process each standing card in the PA areas:

1. ARBITER announces the card name and active effect(s).
2. If the card includes a **targeting restriction**: scan the Resolution Grid for Covert Operations targeting the restricted district or ring. For each match: flip the operation card face-down; discard Modifier Cards from that stack. Scan placed Public Acts on the Overview for matches. For each match: return the card face-down, Target Profile, and resource tokens to the declaring faction; discard Modifier Cards; return the Dispatch Token to the acting faction.

   *Modifier Cards on face-down Covert Operations and cancelled Public Acts are consumed without effect. Public Act tokens are refunded — resources are not committed until Beat 4.*

3. If the card includes a **conversion block**: flip affected Deployment Markers to the Blocked face.

##### §9.4.1.1 Step 1: Process Broadcast Effect Cards

For each active Broadcast Effect Card in ARBITER Tableau: ARBITER applies effects privately. If VM-xx is attached: ARBITER resolves publicly — reads effects aloud to all players; removes VM-xx.

##### §9.4.1.2 Step 2: Process CM Cards

The ARBITER Player processes the Beat 1 row lane by lane, left to right. For each lane containing a CM card:

1. Identify the submitting faction from the CM card.
2. Scan the Resolution Grid for all Covert Operation Cards targeting that faction.
3. Apply by card type:
   - **Type A (CM-A):** Flip each targeted Covert Operation Card face-down. Discard Modifier Cards from those stacks.
   - **Type B (CM-B):** Place a CM-B Modifier Token (M-11; value on token) on each targeted Covert Operation Card.
4. Discard the CM card.

5. Repeat until all CM cards in the Beat 1 row(s) have been resolved.

*No other board changes, track updates, or maintenance occur in this beat.*

Beat 1 complete. Proceed to §9.4.2 Beat 2.

---

#### §9.4.2 Beats 2 and 3: Covert Operations Resolve

*Entry: §9.4.1 complete. CM cards processed; targeting restrictions and conversion blocks applied.*

**Beat Summary:** ARBITER resolves all Covert Operations left to right — Beat 2 row(s) first, then Beat 3 rows. When all rows have resolved, proceed to Step 6.

*The ARBITER Player executes all steps in this section unless a step names a different actor.*

*Beat 2 cards resolve before any Beat 3 operations. Each beat's rows are pre-cleaned by the beats before it — every face-up card reached is valid for resolution.*

*A card is only a valid target while it occupies a slot in the Resolution Grid — once resolved and returned to the Dispatch Packet, it cannot be targeted.*

*[flag: Deferred Effect (C11 Fortify Structure) and Resource Allocation (C34 Golden Parachute) — Beat 2 procedures pending redesign.]*

For each card in the current row, left to right:

##### §9.4.2.0 Step 0: Identify Operation

Read the card in the current grid slot.

If face-down: no resolution. Advance to Step 3.

###### §9.4.2.0.0 Step 0.0: Apex Check

If Apex: resolution is immediately interrupted — see §14 Apex Activation before proceeding.

###### §9.4.2.0.1 Step 0.1: VM-xx Check

If VM-xx is attached: this operation resolves publicly. Announce the card name, type, and declared targets aloud to all players before proceeding.

###### §9.4.2.0.2 Step 0.2: Base Difficulty

Read the base difficulty from the card spec.

If automatic (no threshold roll): skip to Step 2: Apply Outcome.

If D100: continue to Step 1: Die Roll.

##### §9.4.2.1 Step 1: Die Roll

###### §9.4.2.1.0 Step 1.0: Set Threshold

Set the threshold slider to the base difficulty listed on the operation card.

**Modifier Tokens** (placed physically on the card — for each, read the modifier value, adjust the slider, and set the token aside for Step 3 cleanup):
- Partial payment threshold marker
- Type B Countermeasure token
- Protect Modifier Token
- BM-xx tokens: apply n × the card's specified threshold modifier (n = BM-xx count)

**Modifier Cards** (splayed beneath the operation card — leave in place for Step 3 discard):
- Faction Modifier Cards: read modifier value, adjust slider.
- Ring Modifier Cards: confirm the operation's Target Profile is within the card's ring constraints. If true: apply modifier value to slider. If false: no adjustment.

**Board state** (environmental — read from board; adjust the slider for each that applies):
- Public Standing modifier
- Active board state effects (Situation Report + standing Public Acts)
- Ring adjacency penalty

All modifier sources captured. Slider shows the final threshold.

###### §9.4.2.1.1 Step 1.1: Read Threshold

Read the final threshold from the slider. If VM-xx: announce the threshold aloud.

###### §9.4.2.1.2 Step 1.2: Roll d100

Roll d100. If VM-xx: call the die roll aloud.

###### §9.4.2.1.3 Step 1.3: Determine Outcome

Compare roll to threshold — apply Critical Success/Fail rules per §13. If VM-xx: announce outcome aloud.

##### §9.4.2.2 Step 2: Apply Outcome

*If VM-xx: announce the effect aloud.*

*If BM-xx tokens are present (count = n): all outcome effects execute (1+n) times in sequence. If the outcome specifies a Notification Slip: deliver one slip only, regardless of n.*

*If this operation's outcome blocks the acting faction's Deployment Marker conversion: flip the relevant marker to the Blocked face.*

###### §9.4.2.2.0 Succeeded

ARBITER applies all board changes per the card spec: Presence Tokens, Structure Blocks, Dominant Markers, Established Markers, Tension Markers. If VM-xx: ARBITER directs board changes aloud; the acting Faction Player physically applies them.

If the outcome specifies VM-xx placement on another card in the Resolution Grid: ARBITER retrieves VM-xx from supply and places it on that card.

If the card specifies a Notification Slip or Intel Delivery Slip: ARBITER writes and places it in the Dispatch Packet.

*Successful Covert Operations do not produce Standing Marker moves — the action is unobserved. Any Standing Marker move occurs only as a card-specified failure or discovery condition.*

###### §9.4.2.2.1 Failed

ARBITER applies the failure conditions specified on the card. If VM-xx: ARBITER directs board changes aloud; the acting Faction Player physically applies them. If the card specifies an announcement, ARBITER makes it. If the card specifies a Notification Slip: ARBITER writes and places it in the Dispatch Packet.

###### §9.4.2.2.1.1 Discovered

ARBITER announces the discovery to all players: acting faction, operation name, and declared target. ARBITER advises the affected Faction Player of the board changes required per the card-specified discovery conditions. The affected Faction Player applies their own board changes as directed.

*[flag: 04-n37 — formal discovery procedure block pending.]*

##### §9.4.2.3 Step 3: Clean Up Grid Cell

Complete the Dispatch Packet for the acting faction:
1. Place the operation card in the Dispatch Packet.
2. Place the Target Profile in the Dispatch Packet.
3. Discard Modifier Cards from the grid cell — removed from the game.
4. Return Modifier Tokens, BM-xx tokens, and VM-xx (if present) to ARBITER supply.

###### §9.4.2.3.1 Step 3.1: Return Packet

Place the completed Dispatch Packet in the acting faction's Dispatch Case.

##### §9.4.2.4 Step 4: ARBITER Private Tracking

###### §9.4.2.4.0 Update Chorus Portrait Track

The ARBITER Player privately updates the acting faction's Portrait Marker on the hidden track.

###### §9.4.2.4.1 Note for Chronicle (optional)

The ARBITER Player may write a brief note if this operation produced a moment worth preserving.

*At ARBITER's discretion. Detail in Art 07 — ARBITER Toolkit.*

##### §9.4.2.5 Step 5: Advance

Advance to the next grid slot, left to right, row by row within the current beat.

**Beat 2 complete** (all Beat 2 rows resolved): move to the first slot of the first Beat 3 row and return to Step 0.

**Beat 3 complete** (all Beat 3 rows resolved): proceed to Step 6.

##### §9.4.2.6 Step 6: Return Dispatch Cases

###### §9.4.2.6.0 Return Cases

The ARBITER Player returns all Dispatch Cases to their owners. Each case contains all Dispatch Packets from this Month's covert resolution, and any Intel Tokens issued to this faction this Month.

*Not returned: resources (spent), Modifier Cards (discarded at Step 3), Countermeasure Cards (removed from game when played).*

###### §9.4.2.6.1 Faction Players Read Results

Faction Players open their returned case and review contents privately.

###### §9.4.2.6.1.0 Target Profile Return

*[flag: procedure depends on Target Profile physical design — erasable/reusable vs. single-use — see PM05 03-n16.]*

Faction Players extract used covert Target Profiles from their Dispatch Packets:
- If reusable: erase and return to faction supply.
- If single-use: discard or dispose per component text.

###### §9.4.2.6.1.1 Process Case Contents

Faction Players sort remaining case contents:
- Used Covert Operation Cards: place in CA discard deck.
- Intel Tokens or resources received: place in faction supply on tableau.
- Anything else: return to its designated location.

###### §9.4.2.6.2 Proceed to Beat 4

Covert resolution complete. Proceed to §9.4.3 Beat 4.

---

#### §9.4.3 Beat 4: Public Acts Resolve

*Entry: §9.4.2 complete. Covert Operations resolved; grid cleared.*

**Beat Summary:** Faction Players execute all steps unless noted. ARBITER steps are explicitly attributed.

*Public Acts have been on the board as valid targets since declaration in §9.2. Beat 4 fires every month.*

##### §9.4.3.0 Step 0: Pre-Resolution Setup

*(Executes once before the initiative loop begins.)*

###### §9.4.3.0.0 Retrieve Faction Threshold Slider

The first Faction Player in initiative order retrieves the Faction Threshold Slider from the Overview.

###### §9.4.3.0.1 Initiative Loop

*Public Acts resolve one per player per pass in initiative order. After resolving (or passing if no PA remains), the acting player passes the Faction Threshold Slider to the next player. A player with no remaining unresolved Public Act passes the slider without resolving. Continue until all Public Acts across all factions are resolved.*

For each turn in initiative order:

##### §9.4.3.1 Step 1: Identify Operation

###### §9.4.3.1.0 Step 1.0: Submit Payment

*(Acting Faction Player is holding the Faction Threshold Slider.)*

**§9.4.3.1.0.0 Transfer Tokens**

Acting Faction Player transfers resource tokens from the declared card stack to the Reservoir. Return the Dispatch Token to the Backlog.

For each Public Act with a `boost` field (value ≠ None): after base cost is transferred, count any submitted boost resources of the specified type. Calculate n = floor(count ÷ boost unit cost). If n > 0: ARBITER retrieves n BM-xx tokens from supply and places them on the card. Boost resources are processed normally — Native Resources drain to the Reservoir; Intel Tokens are handled per §9.4.3.1.0.1.

If the operation card or an active card effect specifies BM-xx: ARBITER retrieves BM-xx tokens from the ARBITER supply and hands them to the Acting Faction Player. Acting Faction Player places them on the card.

**§9.4.3.1.0.1 Intel Tokens**

Acting Faction Player hands all submitted Intel Tokens to ARBITER. ARBITER calculates token age and applies effects per §13 Intel Token Age table.

ARBITER resets (erases) and deposits all Intel Tokens to The Dossier, or discards if single-use.

**§9.4.3.1.0.2 Verify Payment**

ARBITER verifies total payment against the cost printed on the card:
- Full payment: ARBITER acknowledges.
- Partial payment: ARBITER attaches the partial payment threshold marker (M-06) to the card.
- Zero payment: no marker applied.

Proceed to Step 1.0.3.

**§9.4.3.1.0.3 Route**

If zero payment: ARBITER announces act invalid. Acting Faction Player flips the Public Act Card face-down. Advance to Step 4.

Otherwise: continue to Step 1.1.

###### §9.4.3.1.1 Step 1.1: Apex Check

Acting Faction Player flips the Target Profile face-up. Reads the Public Act Card and Target Profile.

If Apex: resolution is immediately interrupted — see §14 Apex Activation before proceeding.

###### §9.4.3.1.2 Step 1.2: Validate Board State

Acting Faction Player checks that the current board state still satisfies the declared Public Act's play conditions. Play conditions are those required at declaration (§9.2) that may have been altered by Covert Operations resolving in Beats 2–3.

- If conditions are no longer met: ARBITER announces the invalidation. Acting Faction Player flips the Public Act Card face-down. Advance to Step 4.

If a public CM-A is present on the target faction's Faction Resolution Grid: Acting Faction Player flips the Public Act Card face-down. Advance to Step 4.

Otherwise: continue to Step 1.3.

###### §9.4.3.1.3 Step 1.3: Apply BEC Modifiers

For each active Broadcast Effect Card in ARBITER Tableau that modifies Public Acts: ARBITER applies effects privately. If VM-xx is attached: ARBITER resolves publicly — reads effects aloud to all players; removes VM-xx.

Continue to Step 1.4.

###### §9.4.3.1.4 Step 1.4: Base Difficulty

Acting Faction Player reads the base difficulty aloud from the Public Act Card.

If automatic (no threshold roll): skip to §9.4.3.3 Step 3: Apply Outcome.

If D100: continue to §9.4.3.2 Step 2: Set Threshold.

##### §9.4.3.2 Step 2: Set Threshold

###### §9.4.3.2.0 Step 2.0: Set Threshold Slider

Set the Faction Threshold Slider to the base difficulty listed on the Public Act Card.

**Modifier Tokens** (placed physically on the card — for each, read the modifier value, adjust the slider, and set the token aside for Step 4 cleanup):
- Partial payment threshold marker
- BM-xx tokens: apply n × the card's specified threshold modifier (n = BM-xx count)

**Modifier Cards** (splayed beneath the operation card — leave in place for Step 4 discard):
- Faction Modifier Cards: read modifier value, adjust slider.
- Ring Modifier Cards: confirm the operation's Target Profile is within the card's ring constraints. If true: apply modifier value to slider. If false: no adjustment.

**Board state** (environmental — read from board; adjust the slider for each that applies):
- Public Standing modifier
- Active board state effects (Situation Report + standing Public Acts)
- Ring adjacency penalty
- Type B Countermeasure: if a CM-B targeting this operation is in effect, read the modifier value from the CM-B card and adjust the slider.

All modifier sources captured. Slider shows the final threshold.

###### §9.4.3.2.1 Step 2.1: Read Threshold

Read the final threshold from the slider. Announce aloud.

###### §9.4.3.2.2 Step 2.2: Roll d100

Roll d100 publicly. State the result aloud.

###### §9.4.3.2.3 Step 2.3: Determine Outcome

Compare roll to threshold — apply Critical Success/Fail rules per §13.

##### §9.4.3.3 Step 3: Apply Outcome

*If BM-xx tokens are present (count = n): all outcome effects execute (1+n) times in sequence. If the outcome specifies a Notification Slip: deliver one slip only, regardless of n.*

*If this Public Act's outcome blocks the acting faction's Deployment Marker conversion: Acting Faction Player flips the relevant marker to the Blocked face.*

###### §9.4.3.3.0 Succeeded

Acting Faction Player makes all board changes: Presence Tokens, Structure Blocks, Dominant Markers, Established Markers, Tension Markers. If the card specifies a Standing Marker move, apply it.

If the card specifies a Notification Slip: ARBITER writes and places it in the indicated faction's Dispatch Case.

If the outcome specifies VM-xx placement: ARBITER retrieves VM-xx from supply and places it on the specified target.


###### §9.4.3.3.1 Failed

Acting Faction Player applies the failure conditions specified on the card. If the card specifies a Standing Marker move, apply it.

If the card specifies a Notification Slip: ARBITER writes and places it in the target faction's Dispatch Case.

##### §9.4.3.4 Step 4: Clean Up

Acting Faction Player:
1. Set aside Modifier Tokens (partial payment marker, BM-xx tokens if present) — return to ARBITER supply.
2. Discard Modifier Cards splayed beneath the Public Act Card — removed from the game.
3. If the card is face-down (invalidated) or Immediate: remove from the Overview; return to the acting faction's PA discard deck.
4. If the Public Act Card is Standing Effect: move to the standing effect zone on the acting faction's Faction Resolution Grid.
5. Return the Target Profile: if reusable, erase and return to faction supply; if single-use, discard or dispose per component text. *[flag: depends on Target Profile physical design — see PM05 03-n16.]*

##### §9.4.3.5 Step 5: ARBITER Private Tracking

###### §9.4.3.5.0 Update Chorus Portrait Track

ARBITER Player privately updates the acting faction's Portrait Marker on the hidden track.

###### §9.4.3.5.1 Note for Chronicle (optional)

ARBITER Player may write a brief note if this operation produced a moment worth preserving.

*At ARBITER's discretion. Detail in Art 07 — ARBITER Toolkit.*

##### §9.4.3.6 Step 6: Advance

Acting Faction Player passes the Faction Threshold Slider to the next Faction Player in initiative order.

If the next player has no remaining unresolved Public Act: that player passes the slider to the following player without entering the resolution loop.

When no unresolved Public Acts remain across all factions: the player currently holding the slider returns it to the Overview. Beat 4 complete. Proceed to §9.4.4 Close Month.

---

#### §9.4.4 Close Month

*Entry: §9.4.3 complete. All Public Acts resolved.*

##### §9.4.4.0 Step 0: Cleanup

###### §9.4.4.0.0 Step 0.0: Remove Transient Cards

ARBITER announces: *"Close Month — remove Transient cards."*

Each Faction Player removes all Transient-duration cards from their Faction Resolution Grid and any other play areas. Cards are discarded per card text.

##### §9.4.4.1 Step 1: Month Advance

*[flag: Round Track physical component — validate presence in L1.0 component list.]*

ARBITER advances the Round Track pointer:
- Month 1 or 2: advance to the next month. Return to §9.0 Start of Month.
- Month 3: do not advance. Proceed to §10 Resolve District Tension. Quarter advance occurs at the end of the quarter close procedure.

---

## §10 Resolve District Tension

*Entry: Month 3 §9.4.4 complete.*

### §10.0 Step 0: Scan for Tension Markers

The ARBITER Player scans the Overview for Tension Markers.

If none: proceed to §11 Quarterly Debrief.

If one or more: select the outermost contested district (Baryo first, inward to Chorus Node). Proceed to §10.1.

### §10.1 Step 1: Resolve Contested District

#### §10.1.0 Step 1.0: Declare Contest

ARBITER announces: *"Contest [District Name] — declare Battlefield Strength."*

#### §10.1.1 Step 1.1: Identify Contesting Factions

ARBITER identifies all factions at Dominant influence in the contested district as contesting factions. More than two factions may contest a single district.

#### §10.1.2 Step 1.2: Calculate and Declare Totals (simultaneously)

Each contesting Faction Player:
1. Counts all Presence Tokens and Structure Blocks in the contested district and in each adjacent district. Deployment Markers count as 1 Presence Token.
2. Plays any Battlefield Modifier Cards face-up. Each card's +n bonus added to the total.
3. Plays any fresh Intel Tokens (age 0–2) targeting an opposing faction face-up. Each token adds +2 to the total.
4. Announces their full modifier total aloud.

Battlefield Modifier Cards are removed from the game upon use — may not be replayed in this contest or any subsequent district contest this Quarter.

Intel Tokens played are handed to ARBITER. ARBITER resets (erases) and returns them to The Dossier, or discards if single-use.


#### §10.1.3 Step 1.3: Roll d10

Each contesting Faction Player rolls d10. Announces the sum of their modifier total (Step 1.2) and the d10 result aloud.

#### §10.1.4 Step 1.4: Resolve Outcome

ARBITER compares totals. If tied: proceed to §10.1.4.1.

##### §10.1.4.0 Winner

ARBITER announces: *"[Faction] holds [District Name]."* The winning Faction Player removes 1 Presence Token belonging to a contesting faction of their choice from the contested district. Return chip and Tension Marker to ARBITER for pool return.

The faction that had their Presence Token removed moves the winning faction's PS marker −1.

###### §10.1.4.0.1 Will You Press?

ARBITER asks the faction that had their Presence Token removed: *"[Faction] — will you press?"*

If yes: proceed to §10.1.4.0.2.

If no: proceed to §10.1.5.

###### §10.1.4.0.2 Press

The losing Faction Player removes 1 Presence Token from an adjacent district of their choice and moves it to the contested district. The winning faction moves the losing faction's PS marker −1.

Return to §10.1.2.

##### §10.1.4.1 Tie

Applies when two or more factions share the highest total. No press on a tie.

Each tied Faction Player removes 1 Presence Token — from the contested district or an adjacent district of their choice (no adjacent chips: must remove from the contested district) — and returns it to the pool.

ARBITER checks the Dominant condition across all contesting factions:
- Exactly one faction is Dominant: settled in that faction's favor. ARBITER removes the Tension Marker. Proceed to §10.1.5.
- No faction Dominant: no dominant presence remains. ARBITER removes the Tension Marker. Proceed to §10.1.5.
- Multiple factions remain Dominant; no non-tied factions in the contest: return to §10.1.2.
- Multiple factions remain Dominant; non-tied factions remain: tied factions step out. Remaining factions return to §10.1.2.

#### §10.1.5 Step 1.5: Update Board

All contesting Faction Players update Dominant Markers, Established Markers, and Tension Markers as influence levels shift — in the contested district and in any adjacent districts from which chips were moved. Return any removed components to ARBITER supply.

### §10.2 Step 2: Advance

ARBITER checks for remaining Tension Markers on the Overview.

If Tension Markers remain: return to §10.0.

Proceed to §11 Quarterly Debrief.

---

## §11 Quarterly Debrief

*Entry: §10 Resolve District Tension complete.*

### §11.0 Step 0: Open Debrief

ARBITER announces: *"The Table is in Debrief."*

*No initiative order, no phase timer.*

Any Faction Player may:
- Trade resources with any other faction (any terms)
- Trade Intel Tokens with any other faction (any terms, examination permitted)
- Accept or decline an Accord proposal
- Counter-propose Accord terms

ARBITER conversion available during Debrief and between phases. Not available during active resolution beats (Beats 0–5) or while ARBITER is processing board changes. Requests during resolution are served after the current beat completes.

*Quarter 1 only — ARBITER announces: "Resource conversion is available whenever I am not actively resolving actions. The rate is determined by your presence at the Chorus Node." Rate table: §19.1 — Chorus Node Benefits & The Translation.*

### §11.1 Step 1: Debrief Actions

If any faction holds a Debrief Action card: resolve in initiative order.

1. The holding Faction Player announces the card name.
2. The Faction Player executes the card's Debrief instruction.
3. ARBITER confirms the effect.
4. The holding Faction Player returns the card to ARBITER. ARBITER removes it from the game or returns it to supply per card text.

If no faction holds a Debrief Action card: skip to §11.2.

*Physical form TBD.*

### §11.2 Step 2: Chorus Question Window

If the Chorus Activity track has reached the Question threshold and the Chorus Node is not Contested: any faction with at least Present influence at the Chorus Node may propose a question. Simple majority passes it; ARBITER declares the question adopted. ARBITER answers in The Observation register.

If the threshold has not been reached, or the Chorus Node is Contested: no window this Quarter. Proceed to §11.3.

*Full rules: Art 07 — ARBITER Toolkit.*

### §11.3 Step 3: Ready to Close

*[flag: majority threshold (3 of 5) assumes full 6-player configuration. Sub-6 threshold TBD — see PM01-02.]*

1. When done with Debrief, a Faction Player flips their Status Marker to the Ready side.
2. When 3 of 5 Faction Players show Ready: ARBITER starts a 60-second courtesy timer: *"The majority is ready. Sixty seconds."*
3. When the timer expires or all 5 show Ready — whichever comes first — proceed to §11.4.

*ARBITER observes who signals ready early, who holds out, and when. The Chorus notes this.*

### §11.4 Step 4: ARBITER Debrief

ARBITER addresses The Table in three components, in order:

#### §11.4.0 Summary

Factual account of Quarter resolution outcomes. The Record register.

##### §11.4.0.1 Annual Report (Q4 only)

At the close of Quarter 4, ARBITER delivers an Annual Report following the Summary: a narrative account of the full game arc to date — patterns, shifts, and consequences across Q1–Q4. The Record register. Scripted structure: Art 07 — ARBITER Toolkit.

#### §11.4.1 Observation

ARBITER delivers one observation in The Observation register — never combining both forms:
- *Form A:* *"A faction at this table has moved into [PORTRAIT STATE]. [STATE LANGUAGE]."*
- *Form B:* *"[FACTION]'s contribution to the Portrait this Quarter was [vague adjective]."*

If Chorus Activity changed this Quarter, ARBITER incorporates it as the track moves on the board. Scripted dialogue for each Chorus Activity level: Art 07 — ARBITER Toolkit.

Debrief closes. Proceed to §12 Quarter Close.

---

## §12 Quarter Close

*Entry: §11 Quarterly Debrief complete.*

### §12.0 Step 0: Seasonal Card Cleanup

Each Faction Player removes all Seasonal-duration cards from their play area. ARBITER removes any remaining Seasonal Broadcast Cards from the Situation Report Zone. Cards discarded or removed from game per card text. Broadcast Effect Cards on the ARBITER Tableau expire per §7.2.6 at the start of the next Quarter — §12.0 does not govern ARBITER Tableau cleanup.

Proceed to §12.1.

### §12.1 Step 1: Findings Decay

The Ghost Faction Player privately calculates their current Findings total and applies decay:
- 7–12: lose 2
- 13+: lose 4

Ghost returns the appropriate number of Findings tokens to the Reservoir and declares the resulting total to ARBITER. ARBITER records the declared total.

*[V1: honor system — Ghost's Findings total is not publicly verifiable. Mechanical enforcement deferred to L2.]*

Proceed to §12.2.

### §12.2 Step 2: Debrief Reward

ARBITER assesses the Quarter and distributes rewards before the Session Timeline advances.

*Full procedure: Art 07 — ARBITER Toolkit (pending design).*

Proceed to §12.3.

### §12.3 Step 3: Return Notification Slips

Faction Players return all NS-xx Notification Slips from hand to ARBITER supply.

Proceed to §12.4.

### §12.4 Step 4: Advance Session Timeline

ARBITER advances the Session Timeline: Quarter +1, Month reset to 1 (M1/Q+1).

If Q1–Q7: proceed to §7 Upkeep, Quarter N+1.

If the tracker reaches Q8 and no Apex has resolved: proceed to Session End per Art 10a — Victory System.

---

## Reference Material

## §13 The Operation System

The Operation System governs resolution for all committed actions: Covert Operations (Beat 3) and Public Acts (Beat 4).

*Every committed action resolves with a roll. Submitting an operation or declaring a Public Act is a commitment — ARBITER renders a judgment on all of them.*

---

### §13.1 The d100 Roll

A d100 is produced by two ten-sided dice (d10) in two distinct colors. One color is designated as the tens digit; the other as the units digit. Together they produce a result from 01 to 100. Both dice showing 0 = 100.

Establish which color is tens at session start. Keep consistent throughout the session.

If d10 dice are unavailable, any device capable of generating a random integer from 1 to 100 produces an identical result.

*The d100 produces a flat uniform distribution — every result from 01 to 100 is equally likely. A threshold of 50 is a genuine 50% chance of success; a modifier of +15 shifts that probability by exactly 15 points. Probability is transparent: players can calculate exact odds before committing to an operation.*

---

### §13.2 How to Read the Roll

To succeed, the roll must land equal to or below the target threshold. The threshold is the probability of success expressed as a percentage.

| Outcome | Condition |
|---------|-----------|
| Succeeded | Roll ≤ threshold |
| Failed | Roll > threshold |
| Critical Success | Roll 01–05 — always, regardless of threshold or modifiers |
| Critical Fail | Roll 96–00 — always, regardless of threshold or modifiers |

*If modifiers reduce the threshold to 0 or below, the roll still occurs — only a Critical Success (01–05) succeeds. If modifiers raise the threshold to 100 or above, the roll still occurs — only a Critical Fail (96–00) fails. The 5% critical floor means no committed action is truly hopeless; the 5% critical ceiling means no action is guaranteed. Critical Success and Critical Fail carry additional action-specific consequences noted on individual operation cards (Artifact 04).*

---

### §13.3 Base Difficulty

Base difficulty is printed on the operation card or Public Act Card. It represents conditions for a competent operative under neutral circumstances.

| Difficulty | Threshold |
|------------|-----------|
| Easy | 75 |
| Average | 50 |
| Challenging | 25 |

*Automatic and Impossible do not appear as base difficulty values. Every committed action resolves with a roll. Automatic and Impossible may appear as explicit card text for specific designed exceptions — they are not base states of the system.*

---

### §13.4 Difficulty Modifiers

| ID | Category | Name | Scope | Applied | Instance Limit | Value Type | Threshold Adjustment |
|----|----------|------|-------|---------|----------------|------------|----------------------|
| M-01 | Standing | Celebrated | All | Persistent | 1 | Fixed | +20 |
| M-02 | Standing | Respected | All | Persistent | 1 | Fixed | +10 |
| M-03 | Standing | Neutral | All | Persistent | 1 | Fixed | 0 |
| M-04 | Standing | Suspect | All | Persistent | 1 | Fixed | −10 |
| M-05 | Standing | Discredited | All | Persistent | 1 | Fixed | −20 |
| M-06 | Payment | Partial payment marker | All | Beat 0 (covert) / Beat 4 (public) | 1 per submitted card | Fixed | −50 |
| M-08 | Card Effect | Modifier Card | All | Pre-Resolution | Unlimited | Variable | See card |
| M-09 | Card Effect | Protect-type operation card | Covert | Beat 2 | 1 per submitted | Variable | See card |
| M-10 | Situation Report | Difficulty effect | All | Beat 1 | 1 per active Broadcast Effect Card | Variable | See Broadcast Effect Card |
| M-11 | Countermeasure | Type B Countermeasure (CM-B) | All | Beat 2 / Beat 4 | 1 per defending faction | Fixed | −15 |
| M-12 | Ring | No adjacent inward-ring presence | All | Persistent | 1 | Fixed | −25 |
| M-13 | Intel | Stale Intel Token (age 3) | All | Beat 0 / Beat 4 | 1 per stale token | Fixed | −25 |

*All active modifiers are cumulative. Apply all before rolling.*

*Scope: "All" covers all currently defined action types (covert and public). Extends to operative actions when Artifact 05 is designed.*

*Sign convention: positive Threshold Adjustment values raise the threshold (success more likely); negative values lower it (success harder). The partial payment penalty (−50) and ring adjacency penalty (−25) are the largest single Fixed modifiers in the system — a faction simultaneously facing both plus Discredited (−20) and a Type B Countermeasure (−15) is reduced by 110 points, leaving only a Critical Success (01–05) viable on any difficulty tier.*

*Variable modifiers are unbounded by this table — balance analysis across all defined modifier values is maintained in Artifact 03a.*

### §13.5 Intel Token Age

Token age = current Quarter − Quarter generated (written on token by ARBITER at issuance).

| Age | Status | Effect |
|-----|--------|--------|
| 0–2 | Fresh | No modifier |
| 3 | Stale | −25 threshold modifier (M-13) applied at Beat 0 (covert) or Beat 4 (public) |
| 4+ | Expired | Counts as partial payment |

---

## §14 Apex Activation

*Entry: called from covert or public resolution (§9.4.2.0.0 or §9.4.3.1.1).*

An Apex operation may be submitted as a Covert Operation or as a Public Act.

**Step 0 — Identify the Apex.**

When an Apex card is encountered, the current procedure immediately suspends and subroutines to Apex resolution (Steps 1–4). If the Apex is cancelled at Step 3, the procedure resumes from the exact point it was suspended.

- Covert resolution: suspension occurs when the Apex card is reached in the resolution queue. On return from a failed Apex: continue from the next operation in queue.
- Public resolution: suspension occurs when the Apex Public Act is reached in initiative order. The card has been face-up on the Faction Resolution Grid since §9.2 Public Declaration. On return from a failed Apex: continue from the next Faction Player in initiative order.

ARBITER announces: *"An Apex operation has been submitted. Resolution is suspended."*

**Step 1 — Confirm resources paid.**

*Covert:* Resources were confirmed at case opening. If this step is reached, the card was face-up and payment is already in the Reservoir.

*Public:* The ARBITER Player confirms resources were transferred to the Reservoir at Submit Payment (§9.4.3.1.0). If payment is incomplete: Apex fails. Resources spent. Resolution resumes.

**Step 2 — Process Emergency Responses.**

Resolution is suspended at the current position. Each non-Apex faction submits one Emergency Response. Emergency Responses are submitted simultaneously and resolved by ARBITER in initiative order. They may change board state — Presence Tokens, Structure Blocks, Public Standing — before the threshold check in Step 3.

*Emergency Response design is pending Artifact 04 / Artifact 05. Design note: Emergency Responses may be used to assist or thwart the Apex — Board Strength may increase or decrease before Step 3's threshold check.*

**Step 3 — Check Board Strength threshold.**

After Emergency Responses resolve, the ARBITER Player counts the Apex faction's total Presence Tokens and Structure Blocks (Board Strength). If the total does not meet the threshold specified in Artifact 05, the Apex is cancelled. Resources spent. Operative does not retire. Resolution resumes from the suspended position.

*Board Strength is checked here — after all Emergency Responses — not at submission. A faction may use their Emergency Response to assist the Apex (raising Board Strength) or oppose it (reducing Board Strength). This is load-bearing for Emergency Response design in Artifact 04 / Artifact 05.*

**Step 4 — Resolve Apex.**

The ARBITER Player opens the Sealed Apex ability and pauses 5 seconds. ARBITER reads the Apex narrative card aloud. The ARBITER Player applies all public board effects and updates the Chorus Portrait track. The session ends. Proceed to Session End per Artifact 10a — Victory System.

*Operations remaining in the suspended queue do not resolve.*

*Full Apex rules in Artifact 05 — Operative & Apex System.*

---

## §15 Duration Taxonomy

All Public Acts, Modifier Cards, and board state cards carry one of four duration types. Duration is printed on the card. Cleared behavior (return to discard pile vs. remove from game) is specified per card text.

| Type | Duration | Cleared |
|------|----------|---------|
| Immediate | Placed on the board; resolves immediately upon placement. Must move from hand to board to trigger. Cannot be returned to hand, discarded, or removed from game until placed on the board. | Per card text after resolution — removed from board (discard or remove from game) |
| Transient | Active for this month only | Close Month of the month in which it was played |
| Seasonal | Active for this Quarter | End of Quarter |
| Permanent | Active until a named action or condition removes it — including a self-clearing trigger on the card | Per card text (discard or remove from game) |

*ARBITER's Situation Reports carry Seasonal duration by default. Card text may specify otherwise.*

*Modifier react cards may carry any duration type — a react that creates a persistent board state remains on the board with its stated duration.*

---

## §16 Public Act Placement Rules

*[flag: items 2–3 placement procedures depend on Faction Resolution Grid physical layout. Update after Art 08 design is complete — see PM05 03-n14.]*

1. Public Acts are declared during §9.2 (Public Declaration), in initiative order.
2. The declaring Faction Player places the card face-up in the unresolved PA zone of their Faction Resolution Grid, with the Target Profile and 1 Dispatch Token on the card. Resource tokens remain with the card — payment is submitted to the Reservoir at public resolution.
3. Modifier Cards modifying the Public Act are placed face-up alongside the card in the Faction Resolution Grid.
4. Once placed, the card is a valid target for Countermeasure Cards (§9.3 Countermeasures) and other Public Acts.
5. Public Acts cannot be withdrawn or modified after placement.
6. ARBITER's Situation Reports are placed in the Situation Report Zone during Upkeep (§7.2) and follow the same duration and targeting rules as faction Public Acts.
7. A Public Act Card remains in play until its duration expires. Resolution does not necessarily remove the card — duration governs removal.
   - Transient cards are removed at Close Month of the month in which they were played.
   - Seasonal cards remain until End of Quarter.
   - Permanent cards remain until a named action or condition removes them.

---

## §17 Countermeasure Card Rules

1. Each faction receives Countermeasure Cards at game start — issued, not drawn. Count per 03-init §2.7.
2. Countermeasure Cards are removed from the game when used — they do not return to hand or discard pile.
3. Countermeasure Cards are deployed during the Countermeasure Window each month (§9.3).
4. Countermeasure Cards protect the submitting faction from all operations targeting them. Protection type depends on how the card is played:
   - Submitted to ARBITER (§9.3.0): protects against all Covert Operations targeting the submitting faction.
   - Played publicly on the Faction Resolution Grid (§9.3.0): protects against all Public Acts targeting the submitting faction.

   CM-A voids all matching operations. CM-B adds a difficulty modifier (M-11) to all matching operations.
5. Unused Countermeasure Cards carry forward to the next Monthly window.
6. CM-A and CM-B are the complete set of Countermeasure Card types. Physical design: Artifact 04 — Action Card System.

---

## §18 React Card Rules

React cards fire in response to publicly visible board state changes. They are held in hand until their trigger condition is met.

### §18.0 Fire Condition

A React card may only fire on a publicly visible board state change. It cannot fire on ARBITER-internal state changes such as the covert resolution queue.

#### §18.0.1 Timing Window

The React window opens when the triggering board state change occurs and closes when the next board state change occurs or the procedure advances. A React cannot be declared once the window has closed.

### §18.1 Trigger Announcement

When a trigger condition is met: the holding Faction Player announces *"React"*, presents the card, and states the trigger condition listed on the card. ARBITER confirms the trigger is valid and pauses the procedure.

#### §18.1.0 Tiebreaker

First to announce pauses play. ARBITER decides tiebreakers. Only one React resolves at a time — a second React may only fire in response to the new board state produced after the first resolves.

### §18.2 Resolution

The React card resolves per its stated effect.

#### §18.2.1 Persistent React Card Effects

If a modifier react card creates a persistent board state (a card placed on the board), the card remains with its duration type per §15.

### §18.3 Resume

ARBITER resumes the original procedure from the point it paused.

---

## §19 Influence Level Reference

### §19.0 Influence Level Thresholds

| Level | Chip minimum | Rank condition |
|-------|-------------|----------------|
| Dominant | 3+ | Strictly more chips than all others in district |
| Established | 2+ | Second place by chip count |
| Present | 1+ | Third place or lower by chip count |
| None | 0 | No chips or Deployment Markers |

- Maximum 6 Presence Tokens per faction per district at any time.
- Deployment Markers count toward chip count and toward the 6-chip limit during the Quarter placed.
- Multiple factions may hold Established simultaneously; up to 4–5 may coexist in a district.
- A faction at None immediately loses all Structure Blocks in that district. The player who caused the last chip removal removes them publicly.

### §19.1 Chorus Node Benefits & The Translation

| Presence level at Chorus Node | Benefits | Translation rate |
|-------------------------------|---------|-----------------|
| ARBITER (constitutive — 8 tokens, Dominance Marker) | Controls Node narrative | — |
| Established (one faction, no tie) | Chorus Activity suppression + Portrait amplifier + Chorus Question access | 2:1 |
| Present | Chorus Question access | 3:1 |
| Tied at Established / Contested (Tension Marker placed) | No other Node benefits | 5:1 |
| None | — | 4:1 |

**The Translation:** Any resource converts to any other at the applicable rate. No action slot required. No limit per Quarter. Announce to ARBITER; ARBITER states the rate in The Record register; take tokens from the Reservoir directly. Timing: ARBITER must not be actively processing a resolution beat or delivering narrative. *The Contested rate is not a balancing mechanism — it is ARBITER's response to factions bringing conflict into the Chorus Node.*

**Portrait amplifier:** Each Quarter a faction holds Established at the Chorus Node, their Chorus Portrait score moves further in its current direction — +1 if currently positive, −1 if currently negative. At exactly 0 (Ambiguous), no movement. ARBITER moves the Portrait Marker at Quarter close (§12).

**Dominant is structurally unreachable at the Chorus Node.** ARBITER's permanent presence is 8 tokens; faction maximum is 6. The Dominant Marker is not placed at the Chorus Node. Only one faction may hold Established at the Chorus Node at a time — if two or more factions reach 2+ chips and tie, the Tension Marker is placed and all tied factions drop to Present-equivalent benefits.

**No Structure Blocks at the Chorus Node.** The Node's space is entirely occupied by receiving infrastructure that predates every faction's presence.

---

## §20 Resource Generation Reference

*Values that feed §7.4 Resource Collection.*

### Ring Base Values

| Ring | Base resource value per Quarter |
|------|---------------------------------|
| Baryo | 1 unit |
| The Mid | 2 units |
| Core | 3 units |
| Chorus Node | 0 — no resource generation |

### Resource Generation by Influence Level

| Level | Generation |
|-------|-----------|
| Dominant | Full (×1) |
| Established | Full (×1) |
| Present | Half, round down (minimum 0) |
| None | Zero |
| Contested (3+ chips, tied) | 1 unit flat regardless of base value |

### Affinity Bonus

Faction holding Dominant presence in their Native Resource district: +1 resource of that type.

### Structure Block Income

Each Structure Block generates +1 resource per Quarter. Faction Player declares type at §7.4.2 (district resource or faction Native Resource).

### Passive Generation

Each faction generates 1 unit of their Native Resource each Quarter, unconditional.

---

## §21 Card Economy Reference

*Temporary home — values migrate to Art 04 §12 when deck construction is finalized.*

### Hand Sizes

| Card Type | Hand Size |
|-----------|-----------|
| Covert Operations | 6 |
| Public Acts | 3 (proposed — open question; see PM05) |

### Modifier Card Draw

| Structure Blocks owned | Faction Modifier Cards drawn |
|------------------------|------------------------------|
| 0–1 | 0 |
| 2–3 | 1 |
| 4–5 | 2 |
| 6+ | 3 (maximum) |

### Dispatch Token Allotment

4 per Faction Player per Quarter (§7.5.0). Tokens budgeted across three Monthly windows.

*[flag: register in 03-init as a game parameter.]*

---

## §22 Board State Update Rules

These rules apply at every step where influence marker or Structure Block changes occur: §7.3.3, §8.2, §9.4.2.2.0, §9.4.3.3.0, §10.1.5, and any card-effect board change.

**Tension Marker placement:** Whenever a board state update results in two or more factions tied at IL-01 (Dominant) in a district, place 1 Tension Marker on that district from ARBITER supply. Cross-reference: 00b §4.3 Contested flag.

**Tension Marker removal:** When the tie is broken by any means — chip removal, card effect, contest resolution — ARBITER removes the Tension Marker and returns it to ARBITER supply.

**Dominant and Established Marker updates:** When a faction's influence level in a district reaches the threshold for Dominant (IL-01) or Established (IL-02), the corresponding marker is placed. When a faction's influence level falls below that threshold, the marker is removed and returned to ARBITER supply.

**Structure Block removal:** When a faction's influence marker count in a district drops to zero, any Structure Blocks belonging to that faction in that district are removed and returned to ARBITER supply.

---

## §23 Public Standing Scale

Public Standing (PS) runs from 0 to 20. All factions start at 10. Difficulty modifiers by band: §13.4 (M-01–M-05).

| Band | Range | PS drift per Quarter |
|------|-------|----------------------|
| Celebrated | 18–20 | −1 |
| Respected | 14–17 | −1 |
| Neutral | 7–13 | 0 |
| Suspect | 3–6 | +1 |
| Discredited | 0–2 | +1 |

*Drift applied at §12.0 Quarter Close after all other PS changes.*

---

## §24 Resolution State Reference

Every committed action resolves to one of three states.

| State | When |
|-------|------|
| Succeeded | Roll ≤ threshold, or Critical Success (01–05) |
| Failed | Roll > threshold, or Critical Failure (96–00) |
| Voided | Card is face-down at resolution: targeting restriction, Type A Countermeasure, zero payment, or no Dispatch Token |

Critical Success (01–05) and Critical Failure (96–00) apply additional card-specified effects alongside the base Succeeded or Failed state.

Voided cards do not roll. No card effects apply. The operation card and Target Profile return to the acting faction's Dispatch Case; no resolution card is placed.

**Resolution Effects**

A resolution effect fires alongside a state rather than producing a separate state. Currently one is defined:

**Discovered** — fires when a Failed operation meets a card-specified discovery condition (Critical Failure, or roll within a card-specified range). ARBITER announces: acting faction, operation name, declared target. Card-specified discovery consequences apply. See §9.4.2.2.1.1.

*The outcome is Failed. Discovered is an additional consequence, not a parallel state.*

*Other resolution effects (Detected, Exposed, and others) may be defined in future card design passes.*

---

## Appendices

<a id="examples-exceptions"></a>

## § Examples & Exceptions

### Initiative — Quarter 3

*Illustrates §7.1 — full procedure: Art 07 — ARBITER Toolkit.*

*The ARBITER Player reads Portrait scores:*

| Faction | Portrait Score | Rank |
|---------|---------------|------|
| The Guild | +4 | 1 |
| The Directorate | +2 | 2 |
| Ghost | +1 | 3 |
| The Network | 0 | 4 |
| The Syndicate | −2 | 5 |

*D10 roll: 4 — Middle-out down: Rank 3 → 2 → 1 → 4 → 5*

Initiative: Ghost → The Directorate → The Guild → The Network → The Syndicate.

The Guild, highest by Portrait, goes third. No Faction Player can determine Portrait rank from position in the order.

---

### Deployment Marker — Blocked Face

*Quarter 5 Beat 3. The Directorate's Detain operative ability successfully resolves against Ghost. Ghost has a Deployment Marker at Data Exchange showing the Converting face.*

The ARBITER Player flips Ghost's Data Exchange marker to the Blocked face. The marker remains at Data Exchange through the end of Quarter 5.

*Quarter 6 §7.3 Deployment Marker Conversion: Ghost checks markers on the board. The Data Exchange marker shows the Blocked face. Ghost returns the marker to hand without placing a Presence Token. Ghost's influence at Data Exchange does not increase.*

---

### Countermeasure — Type B Example

*Quarter 5. The Directorate plays a Type B Countermeasure. All operations targeting The Directorate take a −15 threshold modifier (M-11).*

Ghost submits a Gather at Government Citadel (no presence — Challenging base, target 01–25). Public Standing: Neutral (0). Type B modifier: −15. Modified target: 01–10.

Ghost rolls: 18. Target is 10. Fails. The Directorate's defensive preparation made an already difficult operation nearly impossible without being able to block it outright.

---

### Dispatch Case Return — Processing Results

*Beat 3 complete. The ARBITER Player returns Ghost's Dispatch Case.*

Ghost retrieves their Dispatch Case. Contents per NS-xx Notification Slips:
- Gather at Data Exchange — resolved
- Undermine at Financial Clearinghouse — voided (Beat 1; targeting restriction)
- Build Structure at Government Citadel — voided (Beat 1; Type A Countermeasure)
- One Intel Token: Faction: The Syndicate / Quarter: 5

Ghost processes this privately before Debrief opens.

---

### Findings Decay — End of Quarter

*Ghost ends Debrief holding 9 Findings.*

9 is in the 7–12 bracket. Ghost removes 2 Findings publicly and returns them to the Reservoir. Ghost begins Quarter 6 Upkeep with 7 Findings before collecting income.

---

### Status Marker — Debrief Close

*Quarter 6 Debrief. The Network and The Directorate are negotiating. Ghost, The Guild, and The Syndicate have all flipped to green.*

Three of five show green. ARBITER: *"The majority is ready. Sixty seconds."*

The Network and The Directorate reach agreement with 20 seconds remaining. Both flip to green. All five show Ready — proceed to §11.4. ARBITER delivers Summary and Observation. Debrief closes. Accord registered. Quarter closes.

---

### Apex Interrupted — Beat 3

*Quarter 7 Beat 0. ARBITER opens The Guild's Dispatch Case, encounters an Apex operation card, and verifies resources. Resources from all Dispatch Cases are drained to the Reservoir. Beat 3: The Guild's Apex card is reached in the resolution queue.*

ARBITER announces: *"An Apex operation has been submitted. Resolution is suspended."*

The operation queue is suspended. Resources committed to all submitted operations were drained in Beat 0 and are not refunded. Each non-Guild faction submits one Emergency Response.

The Network uses their Emergency Response to Undermine The Guild's presence at Power Grid, reducing their Presence Token count. The Directorate Occupies Government Citadel, adding Presence Tokens to their own position.

After Emergency Responses resolve, the ARBITER Player counts The Guild's Board Strength: 11 Presence Tokens + 4 Structure Blocks = 15. Threshold required: 12. Still met.

The ARBITER Player opens the Sealed Apex ability and pauses. ARBITER reads. The session ends.


---

## § Primitive Action Model — Taxonomy Reference

The Primitive Action Model is the formal intersection of component and verb — every combination of *what* can be physically acted on, *by whom*, *when*, and *why*. It lives in `the_signal_db` as a relational model; this section is the design-facing interface to that model and the source of truth for subject × verb × component legality.

Art 02 §13 defines the physical possibility space: which verbs each component can receive, based on its physical form. This section extends that into a four-axis model and legislates the result.

### Governing Principle

The model distinguishes two spaces:

**Possibility space** — every valid combination of component × verb × beat × role that the physical game system can support. Defined in `the_signal_db` from Art 02 §13 inputs.

**Legal space** — the subset of those combinations that the rules actually permit and describe a procedure for. Defined here in Art 03.

A primitive present in `action` with no corresponding Art 03 procedure is not a modeling error — it is an open design question. Every gap is routed to Art 03 for one of three resolutions: **permit** (write the procedure), **prohibit** (annotate as explicitly illegal), or **defer**. The model and this artifact co-evolve iteratively.

### Methodology

The model answers four questions simultaneously: **what** can be acted on, **how**, **when**, and **who** acts. Each axis is a separate dimension table; legal actions are defined by their intersection.

**Dimension tables:**

| Table | Axis | Content |
|-------|------|---------|
| `component` | What | 76 registered physical components |
| `verb` | How | 7 physical verbs (+ Invoke meta-verb) |
| `quarter_phase` | When | 20 beats across the full Quarter structure |
| `player_role` | Who | Faction / ARBITER |
| `role_phase` | Role phase | Initiator / Executor / Fulfiller |
| `trigger_type` | Why | 10 trigger classifications |

**Junction tables** (`comp_verb_phase`, `comp_verb_role`) define valid combinations. A valid *primitive* is any row in both junction tables for the same component × verb pair — the intersection of what is possible by timing AND by role.

**Primitives are derived** as: `comp_verb_phase × comp_verb_role (phase_id=1)`. Phase_id=1 (Initiator) captures who calls for the action; the Executor (phase_id=2) is tracked separately in `comp_verb_role`. Result: 225 primitives in `action`.

### Trigger Taxonomy

Every primitive in `action` carries a `trigger_type_id` classifying what causes the action to fire:

| Type | Subtype | Definition |
|------|---------|------------|
| phase | open | Action fires at beat entry |
| phase | during | Action is valid throughout a beat window |
| phase | closed | Action fires at beat transition |
| rule | card | Card text mandates the action |
| rule | resolution | Quarter resolution procedure mandates the action |
| player | introduce_card | Player submits or declares a card |
| player | agreement | Bilateral consent (trade, Accord) |
| player | verbal_statement | Player declaration with game effect |
| state_condition | — | Compound board/game state check |
| cascade | — | Prior action must have occurred (prereq_id) |

ARBITER-initiated actions concentrate in `phase.during` (ongoing custodial activity) and `rule.card` (card-mandated effects). Faction-initiated actions concentrate in `player.introduce_card` (dispatch) and `rule.resolution` (board state obligations). *(Query `v_trigger_phase_coverage` for current distribution.)*

### Gap Analysis Views

Two views provide the ongoing procedure coverage audit:

**`v_unlegislated_by_trigger`** — All (subject, verb, component) tuples with zero coverage in `action` under any trigger type or beat. Primary use: legalization decision queue — for each row, route to permit / prohibit / defer. Post-S101: **0 rows**.

**`v_unlegislated_primitives`** — All (beat, subject, verb, component) combinations valid in the taxonomy but absent from `action`. Primary use: beat-by-beat procedure review. Post-S101: **52 rows** — beat-specific repetitions of already-permitted combinations; no unresolved design decisions remain.

Six supporting views completed at model build: `v_gap_executor_check`, `v_unassigned_triggers`, `v_duplicate_primitives`, `v_component_coverage`, `v_phase_subject_coverage`, `v_trigger_phase_coverage`. View `v_card_primitive_map` remains blocked — requires `card_ref` seed table.

### Known Gaps

All legalization decisions complete as of S101. `v_unlegislated_by_trigger` = 0 rows. Remaining `v_unlegislated_primitives` rows are beat-specific seeding gaps for already-permitted combinations — data completeness tasks, not design decisions.

**Container/set components** (Faction Hand, decks, discards, card sets, pools) are excluded from primitive junction tables by design. The primitive subject is the individual card, not the container.

Any future component registration or verb addition opens a new gap analysis cycle: seed `comp_verb_phase` and `comp_verb_role`, query `v_unlegislated_by_trigger`, then route each new row to permit / prohibit / defer in Art 03.
