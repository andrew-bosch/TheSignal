# 03 — Quarter Structure & Gameplay
## THE SIGNAL P1 — Paper Prototype

**Version:** 4.2

**Status:** Rubric pass in progress — S86 entry at §9.4.2 Beat 2. Pending grip review and full sign-off.  

**Depends on:** 00 — Factions, World & Narrative Context; 01 — Game Board: New Meridian; 02a — Resource Systems: Board State; 02b — Resource Systems: Tracking  

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
     - [Beat 2: Conditions Set](#942-beat-2-conditions-set)
     - [Beat 3: Covert Operations Resolve](#943-beat-3-covert-operations-resolve)
     - [Beat 4: Public Acts Resolve](#944-beat-4-public-acts-resolve)
     - [Beat 5: Close Month](#945-close-month)
10. [Resolve District Tension](#10-resolve-district-tension)
11. [Quarterly Debrief](#11-quarterly-debrief)
12. [Quarter Close](#12-quarter-close)

**Reference Material**

13. [The Operation System](#13-the-operation-system)
14. [Special Conditions](#14-special-conditions)
15. [Duration Taxonomy](#15-duration-taxonomy)
16. [Public Act Placement Rules](#16-public-act-placement-rules)
17. [Countermeasure Card Rules](#17-countermeasure-card-rules)
18. [React Card Rules](#18-react-card-rules)
19. [Examples & Exceptions](#19-examples--exceptions)

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
  Deployment markers placed. Entry requirements enforced.

§9 MONTHLY ACTIVITIES  ×3
  §9.0  Start of Month — PA obligations checked.
  §9.1  Covert Dispatch — cases assembled, sealed, transmitted.
  §9.2  Public Declaration — public acts declared in initiative order; placed face-up on Overview.
  §9.3  Countermeasures — CM cards submitted; may target queued covert ops or placed public acts.
  §9.4  Resolution:
    §9.4.0  Beat 0: The Cases Open
    §9.4.1  Beat 1: Read Board State
    §9.4.2  Beat 2: Conditions Set
    §9.4.3  Beat 3: Covert Operations Resolve
    §9.4.4  Beat 4: Public Acts Resolve
    §9.4.5  Close Month
  Repeat for Months 2 and 3. Month 3 Beat 5: do not advance month — proceed to §10.

§10 RESOLVE DISTRICT TENSION
  Contested districts resolve. d10 roll-off per district. Tension markers cleared.

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

Each Faction Player flips their Status marker to the Discussing side (yellow/text).

*This is the physical act that opens the Quarter — a personal acknowledgment that a new quarter of operations has begun and the previous Quarter is fully closed.*

---

### §7.1 Initiative

ARBITER determines initiative order and announces the final order. The ARBITER Player updates the Initiative Strip on the board.

*Full procedure: Artifact 07 — ARBITER Toolkit.*

---

### §7.2 Situation Report

*The Situation Report is ARBITER's public act for the Quarter. The Broadcast Card placed on the Overview is a standing public act with Seasonal duration by default (active until End of Quarter) unless the card specifies otherwise. It is a valid target for faction public acts and countermeasures once placed. Beat 1 reads SitRep effects as standing public acts each month.*

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

Each Faction Player moves their Public Standing marker as indicated by ARBITER.

#### §7.2.5 Step 5: Apply Blocked Markers

If the Event Card specifies a deployment marker cannot convert this Quarter: The ARBITER Player flips the affected marker(s) to the Blocked face.

#### §7.2.6 Step 6: Expire Previous Broadcast Effect Cards

The ARBITER Player reviews all Broadcast Effect Cards on the ARBITER Tableau and moves expired cards to the expired area.

*No tick-downs or maintenance — duration management occurred at the close of the previous Quarter.*

---

### §7.3 Deployment Marker Conversion

ARBITER announces: *"Markers convert."*

#### §7.3.0 Step 0: Check Marker Faces

Each Faction Player checks deployment markers currently on the board.

#### §7.3.1 Step 1: Convert Markers

For each marker showing the Converting face: place 1 permanent presence chip in that district and return the marker to hand.

#### §7.3.2 Step 2: Return Blocked Markers

For each marker showing the Blocked face: return the marker to hand without placing a presence chip.

#### §7.3.3 Step 3: Update Board State

Each Faction Player updates Control flags, Established markers, and Tension markers as influence levels shift from new presence chip placements.

*If no markers are on the board — as is always the case at the start of Quarter 1 — this section has no effect. Proceed to §7.4.*

---

### §7.4 Resource Collection

ARBITER announces: *"Collect income."*

Each Faction Player simultaneously calculates and collects their own resources. Other Faction Players observe and may challenge calculations. ARBITER resolves disputes in The Record register.

#### §7.4.0 Step 0: Calculate District Income

For each district with presence chips or deployment markers: apply influence level modifier to base generation value.

#### §7.4.1 Step 1: Apply Affinity Bonus

Add affinity bonus where applicable (Dominant in native resource district: +1).

#### §7.4.2 Step 2: Declare Structure Block Resources

For each structure block: declare resource type publicly (district resource or faction native resource), collect +1.

*If The Network has any presence at University Perimeter: The Network Faction Player declares whether Exposure or the district native resource will be collected from the virtual structure block.*

#### §7.4.3 Step 3: Collect Passive Generation

Add passive generation (1 unit of faction native resource, unconditional).

---

### §7.5 Operations Preparation

ARBITER announces: *"Prepare operations."*

*Purpose: ensure all elements needed for the Quarter are assembled and in their correct positions on the tableau. Faction Players complete this step simultaneously.*

#### §7.5.0 Dispatch Token Distribution

Each Faction Player collects 4 Dispatch Tokens from The Backlog.

*Tokens are held beside the tableau. They are spent across Months 1, 2, and 3 as the player chooses.*

#### §7.5.1 Tableau Verification

Verify the following elements are already in position before drawing begins:

- Floor Act — beside tableau, always available to all factions at all times (full design: Artifact 04 D04-13)
- Countermeasure cards — in their designated area (3 per session total; deployed across Monthly Countermeasure phases)
- Modifier cards carried from prior Quarters — in modifier area
- Operator cards — in their designated area

#### §7.5.2 Action Card Draw

##### §7.5.2.0 Step 0: Draw Covert Cards

Count covert operation cards currently in hand. Draw from personal draw deck to reach a hand of 6.

##### §7.5.2.1 Step 1: Draw Public Act Cards

Count public act cards currently in hand. Draw from public act draw deck to reach starting hand size.

*[Open question: public act hand size under monthly play. Current default: 3. May require revision — see PM05.]*

##### §7.5.2.2 Step 2: Place Drawn Cards

Place all drawn cards in the active hand area of the tableau. Cards are held face-down and private.

*Cards kept from the prior Quarter count toward hand size — a player with 2 kept covert cards draws 4 more to reach 6.*

*Covert operation hand is drawn here only. No additional covert cards are drawn during Monthly Dispatch. Discard down if hand size exceeds maximum at any point.*

*If a draw deck is exhausted mid-draw, shuffle that deck's discard pile immediately to form a new draw deck and continue. Both decks reshuffle independently.*

#### §7.5.3 Modifier Card Draw

*A faction that has triggered Burst Play this session is exempt from modifier card draws — skip this sub-section.*

Draw and place modifier cards in the tableau modifier area.

##### §7.5.3.0 Step 0: Faction Modifier Draw

Draw from the faction modifier deck in the player's tableau.

| Structure blocks owned | Faction modifier cards drawn |
|------------------------|------------------------------|
| 0–1 | 0 |
| 2–3 | 1 |
| 4–5 | 2 |
| 6+ | 3 (maximum) |

*The Network's virtual structure block at University Perimeter counts toward this total while Network holds any presence in that district.*

##### §7.5.3.1 Step 1: Ring Modifier Draw

A ring qualifies if the faction meets all of the following conditions:
- At least 1 structure block in that ring
- Established or higher presence in at least 1 district in that ring

Draw 1 card for each qualifying ring. A faction may qualify for all three rings.

*The Network's virtual structure block at University Perimeter counts toward the structure block condition for its ring while Network holds any presence in that district.*

*Modifier decks (faction and ring) are not reshuffled when exhausted.*

##### §7.5.3.2 Step 2: Burst Play Window

After completing all draws, before Dispatch opens, a faction may trigger Burst Play. If triggered:

1. Declare Burst Play to ARBITER.
2. Trade ALL held modifier cards to the Reservoir — 1 resource of any type per card, chosen independently per card.
3. ARBITER announces publicly: *"[Faction] has liquidated their operational reserve."* Resource gain is private.
4. Remove the faction modifier deck from the tableau. It does not return for the remainder of the session.

*Modifier draws are skipped at all future Hand Assembly steps for this faction.*

*Full card draw rules, deck construction, hand size, modifier card rules, and Burst Play are specified in Artifact 04 §12.*

Upkeep complete. Proceed to §8 Placement.

---

## §8 Placement

*Entry: §7 Upkeep complete.*

Faction Players place their own markers. ARBITER enforces entry requirements.

ARBITER announces: *"Placement is open."*

### §8.0 Step 0: Place Markers in Initiative Order

Faction Players place their two deployment markers in initiative order, snake pattern:

- **Forward pass:** Rank 1 through Rank 5, one marker each
- **Reverse pass:** Rank 5 through Rank 1, second marker each

*All deployment markers are placed with the Converting face showing by default.*

*A deployment marker counts as 1 temporary presence chip immediately upon placement.*

### §8.1 Step 1: Verify Entry Requirements

Before placing in each district:

| Ring | Entry Requirement |
|------|-------------------|
| Baryo | None |
| The Mid | None |
| Core | Established or higher in an adjacent The Mid district (permanent presence chips or temporary presence from first marker this phase) |
| Chorus Node | Established or higher in an adjacent Core district (permanent presence chips or temporary presence from first marker this phase) |

*Ring adjacency penalties apply during operation resolution, not placement. See §13 M-12.*

### §8.2 Step 2: Update Board State

After each placement, if influence levels change: the placing Faction Player updates the relevant Control flag, Established marker, or Tension marker immediately.

*Both deployment markers must be placed each Placement phase, beginning Q1M1. Both may be placed in the same district. ARBITER redirects illegal placements.*

Placement complete. Proceed to §9 Monthly Activities.

---

## §9 Monthly Activities

*Entry: Month 1 — §8 Placement complete; Months 2–3 — §9.4.5 complete. Repeats three times; exit via §9.4.5 each month.*

**Dispatch Token rule:** Each action requires 1 Dispatch Token. Covert operations: token placed in the dispatch case with the operation card (§9.1). Public acts: token placed on the declared card on the Overview (§9.2). A covert operation card submitted without a token is rejected by ARBITER at Beat 0 without resolution and returned to the faction. A public act declared without a token is invalid.

*Faction Players budget their Dispatch Tokens across Months 1, 2, and 3, split between covert operations and public acts as they choose. Not spending a token is a pass for that action.*

---

### §9.0 Start of Month

*Entry: §9 Monthly Activities opens (Month 1) or §9.4.5 complete (Months 2–3).*

Before §9.1 Covert Dispatch opens, ARBITER checks for active public acts with Covert Dispatch obligations. If none: proceed to §9.1.

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

Faction Players assemble, seal, and transmit their own dispatch cases. The ARBITER Player keeps watch on the Dispatch Timer, announces status, and queues cases in the order received.

#### §9.1.0 Step 0: Open Dispatch

ARBITER announces: *"Dispatch is open."* The ARBITER Player starts the dispatch timer.

#### §9.1.1 Step 1: Assemble Cases

Faction Players load operation cards, Dispatch Tokens (1 per operation card), resources, Target Profiles, and any Modifier Cards being assigned to specific operations into their cases.

*Modifier Cards (drawn at §7.5.3) are assigned to operations by placing each card in the case with that operation's packet. A faction may assign Modifier Cards to some, all, or none of their submitted operations. Unassigned Modifier Cards remain in the tableau modifier area and are not submitted.*

*Assembly should be handled privately and silently.*

*Full dispatch case design, physical format, and component contents: Artifact 06 — Messaging System.*

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

*Any case not received is treated as containing no covert operations.*

§9.1 closed. Proceed to §9.2 Public Declaration.

---

### §9.2 Public Declaration

*Entry: §9.1 Covert Dispatch closed.*

Faction Players declare publicly, in initiative order. The ARBITER Player records declarations.

ARBITER announces: *"Public Declaration is open."*

#### §9.2.0 Step 0: Declare in Initiative Order

For each Faction Player in initiative order, one of:

**Pass** — verbally declare no public act will be played this phase.

**Declare** — name the public act and place it on the board:

1. Announce the public act being declared.
2. Place the declared card face-up in the PA area on the Overview (in front of faction tableau), with the target profile, 1 Dispatch Token, and resource tokens on the card. Resource tokens remain with the declared card — payment submitted to the Reservoir at Beat 4.
3. Play any modifier cards modifying the public act face-up alongside the card on the Overview.

*Once placed, the card is a valid target for countermeasures (§9.3) and other public acts.*

*Declared public acts cannot be withdrawn or modified after placement.*

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

**Pass** — verbally declare no Countermeasure card will be played.

**Deploy** — declare "Countermeasure" and choose one play mode for each card:

- **Submit to ARBITER** — hand the card face-down to the ARBITER Player. Applies to all covert operations targeting your faction; ARBITER matches to all relevant operations at Beat 0 (§9.4.0.1).
- **Play publicly** — place the card face-up in your PA area on the Overview. Applies at the appropriate resolution beat to all operations targeting your faction.

*CMs are keyed to the playing faction. CM-A voids operations; CM-B applies a −15 modifier. Full CM card rules: §17.*

*Each faction has 3 Countermeasure cards per session total across all three Monthly windows. Cards spent here are unavailable in Months 2 and 3.*

#### §9.3.1 Step 1: Confirm Countermeasure Placement

**Submitted CMs:** The ARBITER Player attaches each received card to the relevant faction's dispatch case in the receive queue. ARBITER matches to all targeted operations within sealed cases at Beat 0 (§9.4.0.1).

**Publicly played CMs:** Already in position on the Overview. No further placement required.

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

**Beat Summary:** ARBITER positions and opens all dispatch cases, validates payment, and builds the Resolution Grid.

##### §9.4.0.0 Step 0: Position and Open Cases

Cases are in receipt order from §9.1.3. Position each case above its assigned lane and open.

##### §9.4.0.1 Step 1: Process Cases Lane by Lane

From left to right, lane by lane:

0. If any Countermeasure cards are attached to this case (§9.3.1): place each in the Beat 1 row of this lane.

   *At Beat 1, each CM applies to all operations in the grid whose target profile matches the CM's keyed faction.*

1. Remove the first operation packet from the case.

2. For each card in the packet, validate payment:

   | Payment | Applies to | Resources | Card Placement |
   |---------|------------|-----------|----------------|
   | Full | All | Drain to Reservoir | Face-up in grid |
   | Partial | Non-Apex | Drain to Reservoir; attach −50 threshold marker to stack | Face-up in grid |
   | Zero | Non-Apex | None to drain | Face-down in grid |
   | Any shortfall | Apex | Drain any submitted resources to Reservoir | Face-down in grid |
   | Retained | Resource-retaining cards | Validate resource count matches declared value on target profile; resources declared are placed on card — do not drain to Reservoir. Any unallocated resources are placed in target_faction's dispatch case. | Face-up in grid |

   *If any Intel Token is submitted as part of payment, calculate age for each token: current Quarter number − Quarter number written on token.*

   | Age | Status | Effect |
   |-----|--------|--------|
   | 0–2 | Fresh | No modifier |
   | 3 | Stale | Attach −25 Intel freshness modifier to stack (M-13) |
   | 4+ | Expired | Counts as partial payment |

   *All submitted Intel Tokens are reset (erased) and returned to The Dossier, or discarded if single-use.*

   *Quarter number and faction are written on each token by ARBITER at issuance. Physical form TBD — see PM05 03-13. Expired tokens not submitted have no payment value but may be held and traded — age is visible on the token.*

3. Drain resources to the Reservoir as directed.

   *For each card with a `boost` field (value ≠ None): after base cost is drained, count any excess resources remaining in the packet. Calculate n = floor(excess ÷ boost unit cost). If n > 0: place n BM-xx tokens on the card's grid slot. Drain all remaining excess to the Reservoir. No excess is returned to the faction.*

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
   | Beat 2 row | | | | | |
   | Beat 3 card 1 | | | | | |
   | Beat 3 target 1 | | | | | |
   | Beat 3 card 2 | | | | | |
   | Beat 3 target 2 | | | | | |
   | *(up to 4 pairs — Ghost)* | | | | | |

   *Beat 4 processes placed public acts on the Overview — public acts do not appear in the Resolution Grid.*

   *Modifier cards in a stack peek out at the bottom to display their values during resolution. Modifier card physical design must support cascade orientation — value printed prominently at both top and bottom edge. (XA-22, Art 11)*

5. If a Dispatch Token accompanies the card: set aside the token. If no Dispatch Token accompanies the card: flip the operation card face-down; remove attached modifier cards from the game.

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
2. If the card includes a **targeting restriction**: scan the Resolution Grid for covert operations targeting the restricted district or ring. For each match: place the operation card and Target Profile face-down in the acting faction's dispatch case; discard modifier cards from that stack. Scan placed public acts on the Overview for matches. For each match: return the card face-down, Target Profile, and resource tokens to the declaring faction; discard modifier cards; return the Dispatch Token to the acting faction.

   *Modifier cards on voided operations and voided public acts are consumed without effect. Public act tokens are refunded — resources are not committed until Beat 4.*

3. If the card includes a **conversion block**: flip affected deployment markers to the Blocked face.

##### §9.4.1.1 Step 1: Process Broadcast Effect Cards

The ARBITER Player applies effects from each active Broadcast Effect Card in turn, without announcement. The table observes outcomes but is not told their source. Repeat for all active Broadcast Effect Cards.

##### §9.4.1.2 Step 2: Process CM Cards

The ARBITER Player processes the Beat 1 row lane by lane, left to right. For each lane containing a CM card:

1. Identify the submitting faction from the CM card.
2. Scan the Resolution Grid for all covert operation cards targeting that faction.
3. Apply by card type:
   - **Type A (CM-A):** Flip each targeted covert operation card face-down. Discard modifier cards from those stacks.
   - **Type B (CM-B):** Place a −15 modifier token on each targeted covert operation card.
4. Discard the CM card.

5. Repeat until all CM cards in the Beat 1 row(s) have been resolved.

*No other board changes, track updates, or maintenance occur in this beat.*

Beat 1 complete. Proceed to §9.4.2 Beat 2.

---

#### §9.4.2 Beat 2: Conditions Set

*Entry: §9.4.1 complete. CM cards processed; targeting restrictions and conversion blocks applied.*

**Beat Summary:** ARBITER resolves all Beat 2 cards left to right, one card at a time. When all Beat 2 cards have resolved, proceed to Beat 3.

*All Beat 2 cards carry a `beat = 2` field. All Beat 2 cards resolve before any Beat 3 operations.*

*C06 Broadcast Interference and C07 Amplify are redesigned as Seasonal public acts — see Art 04.*

*[flag: Deferred Effect (C11 Fortify Structure) and Resource Allocation (C34 Golden Parachute) procedures pending redesign.]*

*[flag: Type B CM cards attached to placed public acts — sweep timing TBD.]*

For each card in the Beat 2 row, left to right:

##### §9.4.2.0 Step 0: Identify Operation

Read the card in the current Beat 2 slot.

If face-down: no resolution. Return card to acting faction's dispatch case. Advance to next cell. No further steps apply.

###### §9.4.2.0.0 Step 0.0: Apex Check

Not applicable at Beat 2.

###### §9.4.2.0.1 Step 0.1: VM-xx Check

If VM-xx is attached: this operation resolves publicly. Announce the card name, type, and declared targets aloud to all players before proceeding. Remove VM-xx to ARBITER supply at Step 3.

###### §9.4.2.0.2 Step 0.2: Base Difficulty

Read the base difficulty from the card spec.

If automatic (no threshold roll): skip to §9.4.2.2 Step 2: Apply Outcome.

If D100: continue to §9.4.2.1 Step 1: Die Roll.

##### §9.4.2.1 Step 1: Die Roll

###### §9.4.2.1.0 Step 1.0: Apply Modifiers

Apply all active modifiers:
- Partial payment threshold marker (if attached at Beat 0)
- Modifier Cards in cascade
- Ring Modifier Card calculation (Art 07 — ARBITER Toolkit)
- Public Standing modifier
- Active board state effects (Situation Report + standing public acts)
- Ring adjacency penalty (The Mid: no adjacent Core presence; Core: no Chorus Node presence)

###### §9.4.2.1.1 Step 1.1: Calculate Threshold

Total the base difficulty plus all active modifier adjustments.

If VM-xx: announce the final threshold aloud.

###### §9.4.2.1.2 Step 1.2: Roll d100

The ARBITER Player rolls d100.

If VM-xx: call the die roll aloud.

###### §9.4.2.1.3 Step 1.3: Determine Outcome

Compare roll to the declared threshold. Apply Critical Success/Fail rules.

01–05 = Crit Success (`success` + `successcrit`); 06–threshold = Success; threshold+1–95 = Fail; 96–00 = Crit Fail (`fail` + `failcrit`).

If VM-xx: announce outcome aloud.

##### §9.4.2.2 Step 2: Apply Outcome

*If VM-xx: announce the effect aloud.*

###### §9.4.2.2.0 Succeeded

ARBITER directs all board changes per the card spec. The acting Faction Player physically applies them.

If the card's success outcome specifies a Notification Slip or Intel Delivery Slip: ARBITER writes and places it in the indicated faction's dispatch case.

###### §9.4.2.2.1 Failed

ARBITER applies the failure conditions specified on the card. If the card specifies a Notification Slip, ARBITER places it in the target faction's dispatch case.

###### §9.4.2.2.1.1 Discovered

ARBITER announces the discovery to all players: acting faction, operation name, and declared target. The affected Faction Player applies their own board changes as directed.

##### §9.4.2.3 Step 3: Clean Up Grid Cell

1. Place the operation card and Target Profile back in the acting faction's dispatch case.
2. Discard modifier cards from the grid cell — removed from the game.
3. Return modifier tokens to ARBITER tableau.

##### §9.4.2.4 Step 4: ARBITER Private Tracking

###### §9.4.2.4.0 Update Chorus Portrait Track

The ARBITER Player privately updates the acting faction's Portrait marker on the hidden track.

###### §9.4.2.4.1 Note for Chronicle (optional)

The ARBITER Player may write a brief note if this operation produced a moment worth preserving.

*At ARBITER's discretion. Detail in Art 07 — ARBITER Toolkit.*

##### §9.4.2.5 Step 5: Advance

Move to the next cell right. When the Beat 2 row is complete: Beat 2 complete. Proceed to §9.4.3 Beat 3.

---

#### §9.4.3 Beat 3: Covert Operations Resolve

*Entry: §9.4.2 complete. All Beat 2 cards resolved.*

**Beat Summary:** ARBITER resolves all covert operations from the Resolution Grid, row by row, left to right. When all operations have resolved, the grid is cleared and dispatch cases are returned.

*The grid is pre-cleaned by Beats 1 and 2 — every face-up card reached is a valid, unblocked operation.*

*A card is only a valid target while it occupies a slot in the Resolution Grid. Once an operation resolves and its card is returned to the dispatch case, it is no longer a valid target for any action.*

For each card in the Beat 3 rows, left to right:

##### §9.4.3.0 Step 0: Identify Operation

Read the card in the current grid slot.

If face-down: no resolution. Discard all modifier cards from the stack. Return the action card to the acting faction's dispatch case. Advance to next cell. No further steps apply.

###### §9.4.3.0.0 Step 0.0: Apex Check

If Apex: resolution is immediately interrupted — see Apex Activation before proceeding.

###### §9.4.3.0.1 Step 0.1: VM-xx Check

If VM-xx is attached: this operation resolves publicly. Announce the card name, type, and declared targets aloud to all players before proceeding. Remove VM-xx to ARBITER supply at Step 3.

###### §9.4.3.0.2 Step 0.2: Base Difficulty

Read the base difficulty from the card spec.

If automatic (no threshold roll): skip to §9.4.3.2 Step 2: Apply Outcome.

If D100: continue to §9.4.3.1 Step 1: Die Roll.

##### §9.4.3.1 Step 1: Die Roll

###### §9.4.3.1.0 Step 1.0: Apply Modifiers

Apply all active modifiers:
- Partial payment threshold marker (if attached at Beat 0 or Beat 2)
- Type B Countermeasure token (if placed in Beat 2)
- Modifier Cards in cascade
- Ring Modifier Card calculation (Art 07 — ARBITER Toolkit)
- Public Standing modifier
- Active board state effects (Situation Report + standing public acts)
- Protect modifier token (placed by ARBITER in Beat 2)
- Ring adjacency penalty (The Mid: no adjacent Core presence; Core: no Chorus Node presence)
- BM-xx tokens on this card's grid slot: if the card spec defines a threshold modifier per boost count, apply n × that modifier, where n = BM-xx count.

###### §9.4.3.1.1 Step 1.1: Calculate Threshold

The ARBITER Player totals the base difficulty plus all active modifier adjustments.

If VM-xx: announce the final threshold aloud.

###### §9.4.3.1.2 Step 1.2: Roll d100

The ARBITER Player rolls d100.

If VM-xx: call the die roll aloud.

###### §9.4.3.1.3 Step 1.3: Determine Outcome

Compare roll to the declared threshold. Apply Critical Success/Fail rules.

01–05 = Crit Success (`success` + `successcrit`); 06–threshold = Success; threshold+1–95 = Fail; 96–00 = Crit Fail (`fail` + `failcrit`).

If VM-xx: announce outcome aloud.

##### §9.4.3.2 Step 2: Apply Outcome

*If VM-xx: announce the effect aloud.*

*If BM-xx tokens are present on this card's grid slot (count = n): all outcome effects execute (1+n) times in sequence. If the outcome specifies a Notification Slip: deliver one slip only, regardless of n.*

*If this operation's outcome blocks the acting faction's deployment marker conversion: The ARBITER Player flips the relevant marker to the Blocked face.*

###### §9.4.3.2.0 Succeeded

The ARBITER Player directs all board changes. The acting Faction Player physically applies them: presence chips, structure blocks, Control flags, Established markers, Tension markers.

If the card's success outcome specifies an Intel Delivery Slip: ARBITER writes the specified intelligence and places it in the indicated faction's dispatch case.

If the card's success outcome specifies a Notification Slip: ARBITER places it in the target faction's dispatch case.

*Successful covert operations do not produce Standing marker moves — the action is unobserved. Any Standing marker move occurs only as a card-specified failure or discovery condition.*

###### §9.4.3.2.1 Failed

ARBITER applies the failure conditions specified on the card. If the card specifies an announcement, ARBITER makes it. If the card specifies a Notification Slip, ARBITER places it in the target faction's dispatch case.

###### §9.4.3.2.1.1 Discovered

ARBITER announces the discovery to all players: acting faction, operation name, and declared target. ARBITER advises the affected Faction Player of the board changes required per the card-specified discovery conditions. The affected Faction Player applies their own board changes as directed.

*[flag: 04-n37 — formal discovery procedure block pending.]*

##### §9.4.3.3 Step 3: Clean Up Grid Cell

1. Place the operation card and Target Profile back in the acting faction's dispatch case.
2. Discard modifier cards from the grid cell — removed from the game.
3. Return modifier tokens to ARBITER tableau.
4. Return any BM-xx tokens on this grid slot to ARBITER supply.

##### §9.4.3.4 Step 4: ARBITER Private Tracking

###### §9.4.3.4.0 Update Chorus Portrait Track

The ARBITER Player privately updates the acting faction's Portrait marker on the hidden track.

###### §9.4.3.4.1 Note for Chronicle (optional)

The ARBITER Player may write a brief note if this operation produced a moment worth preserving.

*At ARBITER's discretion. Detail in Art 07 — ARBITER Toolkit.*

##### §9.4.3.5 Step 5: Advance

Move to the next cell right. Carriage return to the leftmost cell of the next row when the current row is complete.

When all Beat 3 rows have resolved, proceed to Step 6.

##### §9.4.3.6 Step 6: Return Dispatch Cases

###### §9.4.3.6.0 Return Cases

The ARBITER Player returns all dispatch cases to their owners. Each case contains: submitted covert operation cards, Target Profiles, any IS-xx or NS-xx placed in this case by ARBITER during this Month's resolution, and any Intel Tokens issued to this faction this Month.

*Not returned: resources (spent), Modifier cards (discarded during resolution), Countermeasure cards (removed from game when played).*

###### §9.4.3.6.1 Faction Players Read Results

Faction Players open their returned case and review contents privately.

###### §9.4.3.6.2 Proceed to Beat 4

Beat 3 complete. Proceed to §9.4.4 Beat 4.

---

#### §9.4.4 Beat 4: Public Acts Resolve

*Entry: §9.4.3 complete. Covert operations resolved; grid cleared.*

**Beat Summary:** Each Faction Player resolves their declared public acts in initiative order. Resolution is fully public — all players observe the process.

*Public acts have been on the board as valid targets since declaration in §9.2. Beat 4 fires every month.*

For each public act in initiative order:

##### §9.4.4.0 Step 0: Identify Operation

###### §9.4.4.0.0 Step 0.0: Submit Payment and Validate

The acting Faction Player transfers resource tokens from the declared card stack to the Reservoir. Remove the Dispatch Token — return to the faction.

The ARBITER Player verifies payment against the cost printed on the card:
- **Full payment:** ARBITER acknowledges.
- **Partial payment:** ARBITER attaches a −50 threshold marker to the card.
- **Zero payment:** ARBITER announces the act is invalid. The Faction Player flips the public act card face-down.

If any Intel Token is submitted as part of payment, calculate token age: current Quarter − Quarter generated (written on token).
- Age 0–2: fresh — no modifier applied.
- Age 3: stale — attach a −25 Intel freshness modifier to the stack (M-13).
- Age 4 or more: expired — counts as partial payment.

Reset (erase) and return all submitted Intel Tokens to The Dossier, or discard if single-use.

###### §9.4.4.0.1 Step 0.1: Apex Check

If face-down: auto-fail. Discard all modifier cards. Return the public act card to the faction. Advance to the next Faction Player. No further steps apply.

Read the public act card and Target Profile.

If Apex: resolution is immediately interrupted — see Apex Activation before proceeding.

###### §9.4.4.0.2 Step 0.2: VM-xx Check

Not applicable at Beat 4. All public acts resolve publicly by default.

###### §9.4.4.0.3 Step 0.3: Validate Board State

Check that the current board state still satisfies the declared public act's play conditions. Play conditions are those required at declaration (§9.2) that may have been altered by covert operations resolving in Beats 2–3.

- If conditions are met: proceed.
- If conditions are no longer met: ARBITER announces the invalidation. The Faction Player flips the public act card face-down. Discard all modifier cards. Return the public act card to the faction. Advance to the next Faction Player. No further steps apply.

###### §9.4.4.0.4 Step 0.4: Base Difficulty

The acting Faction Player reads the base difficulty aloud from the public act card.

If automatic (no threshold roll): skip to §9.4.4.2 Step 2: Apply Outcome.

If D100: continue to §9.4.4.1 Step 1: Die Roll.

##### §9.4.4.1 Step 1: Die Roll

###### §9.4.4.1.0 Step 1.0: Apply Modifiers

The acting Faction Player applies all active modifiers:
- Partial payment threshold marker (if placed by ARBITER at Step 0.0)
- Modifier Cards in cascade
- Ring Modifier Card calculation (Art 07 — ARBITER Toolkit)
- Public Standing modifier
- Active board state effects (Situation Report + standing public acts)
- Ring adjacency penalty (The Mid: no adjacent Core presence; Core: no Chorus Node presence)

###### §9.4.4.1.1 Step 1.1: Calculate Threshold

The acting Faction Player totals the base difficulty plus all active modifier adjustments and announces the final threshold aloud.

###### §9.4.4.1.2 Step 1.2: Roll d100

The acting Faction Player rolls d100 publicly and states the result aloud.

###### §9.4.4.1.3 Step 1.3: Determine Outcome

Compare roll to the declared threshold. Apply Critical Success/Fail rules.

01–05 = Crit Success (`success` + `successcrit`); 06–threshold = Success; threshold+1–95 = Fail; 96–00 = Crit Fail (`fail` + `failcrit`).

##### §9.4.4.2 Step 2: Apply Outcome

*If this public act's outcome blocks a deployment marker's conversion: The acting Faction Player flips the relevant marker to the Blocked face.*

###### §9.4.4.2.0 Succeeded

The acting Faction Player makes all board changes: presence chips, structure blocks, Control flags, Established markers, Tension markers. If the card specifies a Standing marker move, apply it.

If the card's success outcome specifies a Notification Slip: ARBITER writes and places it in the indicated faction's dispatch case.

###### §9.4.4.2.1 Failed

Apply the failure conditions specified on the card. If the card specifies a Standing marker move, apply it. The affected Faction Player applies their own board changes.

If the card specifies a Notification Slip: ARBITER places it in the target faction's dispatch case.

##### §9.4.4.3 Step 3: Clean Up

1. Modifier cards placed alongside the public act are discarded — removed from the game.
2. The public act card remains on the Overview per its duration type. Immediate cards only: remove from the board and discard or remove from game per card text.

*No pool modifier tokens are used in Beat 4. Modifier cards placed alongside a public act in §9.2 carry modifier values through resolution. Pool tokens (placed by ARBITER in Beat 2) apply to covert operations in the Resolution Grid only.*

##### §9.4.4.4 Step 4: ARBITER Private Tracking

###### §9.4.4.4.0 Update Chorus Portrait Track

The ARBITER Player privately updates the acting faction's Portrait marker on the hidden track.

###### §9.4.4.4.1 Note for Chronicle (optional)

The ARBITER Player may write a brief note if this operation produced a moment worth preserving.

*At ARBITER's discretion. Detail in Art 07 — ARBITER Toolkit.*

##### §9.4.4.5 Step 5: Advance

Proceed to the next public act in initiative order. When all public acts have resolved: Beat 4 complete. Proceed to §9.4.5 Close Month.

---

#### §9.4.5 Close Month

*Entry: §9.4.4 complete. All public acts resolved.*

##### §9.4.5.0 Step 0: Cleanup

###### §9.4.5.0.0 Step 0.0: Remove Transient Cards

Remove all Transient cards from the board — public acts, modifier cards, or any board state card with Transient duration. Cards are discarded or removed from game per card text.

###### §9.4.5.0.1 Step 0.1: No Other Board Changes

No other board changes occur at Close Month.

##### §9.4.5.1 Step 1: Month Advance

*[flag: Round Track physical component — validate presence in L1.0 component list.]*

If this is Month 1 or Month 2: advance the Round Track pointer to the next month. Return to §9.0 Start of Month.

If this is Month 3: do not advance the month pointer. Proceed to §10 Resolve District Tension. Quarter advance occurs at the end of the quarter close procedure.

---

## §10 Resolve District Tension

*Entry: Month 3 §9.4.5 complete.*

### §10.0 Step 0: Scan for Tension Markers

The ARBITER Player scans the Overview for Tension markers.

If none: proceed to §11 Quarterly Debrief.

If one or more: select the outermost contested district (Baryo first, inward to Chorus Node). Proceed to §10.1.

### §10.1 Step 1: Resolve Contested District

#### §10.1.0 Step 1.0: Declare Contest

ARBITER announces: *"Contest [District Name] — declare Battlefield Strength."*

#### §10.1.1 Step 1.1: Identify Contesting Factions

All factions at Dominant influence in the contested district are contesting factions. More than two factions may contest a single district.

#### §10.1.2 Step 1.2: Calculate and Declare Totals (simultaneously)

Each contesting Faction Player:
1. Counts all presence chips and structure blocks in the contested district and in each adjacent district. Deployment markers count as 1 presence chip.
2. Plays any Battlefield Modifier Cards face-up. Each card's +n bonus added to the total.
3. Plays any fresh Intel Tokens (age 0–2) targeting an opposing faction face-up. Each token adds +2 to the total.
4. Announces their full total aloud.

Battlefield Modifier Cards are discarded immediately — may not be replayed in this contest or any subsequent district contest this Quarter.

Intel Tokens played are reset and returned to The Dossier, or discarded if single-use.

*Adjacency map: Art 01 §[City] — District Adjacency.*
*Battlefield Modifier Card design: Art 04 — Action Card System.*
*Intel Token Battlefield modifier: +2 per fresh token — L163.*

#### §10.1.3 Step 1.3: Roll d10

Each contesting Faction Player rolls d10 and adds it to their declared total. Announces final result aloud.

#### §10.1.4 Step 1.4: Resolve Outcome

Compare totals. If tied: proceed to §10.1.4.1.

##### §10.1.4.0 Winner

ARBITER announces: *"[Faction] holds [District Name]."* The winning Faction Player removes 1 presence chip belonging to a contesting faction of their choice from the contested district. Remove the Tension marker. Return chip and marker to ARBITER for pool return.

The losing faction moves the winning faction's PS marker −1.

###### §10.1.4.0.1 Will You Press?

ARBITER asks the losing faction: *"[Faction] — will you press?"*

If yes: proceed to §10.1.4.0.2.

If no: proceed to §10.1.5.

###### §10.1.4.0.2 Press

The losing Faction Player removes 1 presence chip from an adjacent district of their choice and returns it to the pool. The winning faction moves the losing faction's PS marker −1.

Return to §10.1.2.

##### §10.1.4.1 Tie

Each tied Faction Player removes 1 presence chip — from the contested district or an adjacent district of their choice (no adjacent chips: must remove from the contested district) — and returns it to the pool. Each faction moves the other's PS marker −1.

Check the Dominant condition:
- One faction Dominant, the other not: settled in that faction's favor. Remove Tension marker. Proceed to §10.1.5.
- Both remain Dominant: return to §10.1.2.
- Neither Dominant: no dominant presence remains. Remove Tension marker. Proceed to §10.1.5.

#### §10.1.5 Step 1.5: Update Board

All contesting Faction Players update Control flags, Established markers, and Tension markers as influence levels shift — in the contested district and in any adjacent districts from which chips were removed.

### §10.2 Step 2: Advance

If Tension markers remain on the Overview: return to §10.0.

Proceed to §11 Quarterly Debrief.

---

## §11 Quarterly Debrief

*Entry: §10 Resolve District Tension complete.*

### §11.0 Step 0: Open Debrief

ARBITER announces: *"The Table is in Debrief."*

*No initiative order, no phase timer.*

Free actions available throughout Debrief:
- Trade resources between any two factions (any terms)
- Trade Intel Tokens between any two factions (any terms, examination permitted)
- Accept or decline an Accord proposal
- Counter-propose Accord terms

ARBITER conversion available during Debrief and between phases. Not available during active resolution beats (Beats 0–5) or while ARBITER is processing board changes. Requests during resolution are served after the current beat completes.

*Quarter 1 only — ARBITER announces: "Resource conversion is available whenever I am not actively resolving actions. The rate is determined by your presence at the Chorus Node." Rate table: Art 02a §8 (D02a-01).*

### §11.1 Step 1: Chorus Question Window

If the Chorus Activity track has reached the Question threshold and the Chorus Node is not Contested: any faction with at least Present influence at the Chorus Node may propose a question. Simple majority passes it. ARBITER answers in The Observation register.

If the threshold has not been reached, or the Chorus Node is Contested: no window this Quarter. Proceed to §11.2.

*Full rules: Art 07 — ARBITER Toolkit.*

### §11.2 Step 2: Debrief Actions

If any faction holds a Debrief Action card: resolve in initiative order.

1. The holding Faction Player announces the card name.
2. The Faction Player executes the card's Debrief instruction.
3. ARBITER confirms the effect.
4. The card is removed from the game or returned to the ARBITER pool.

If no faction holds a Debrief Action card: skip to §11.3.

*Physical form TBD.*

### §11.3 Step 3: ARBITER Debrief

ARBITER addresses The Table in three components, in order:

#### §11.3.0 Summary

Factual account of Quarter resolution outcomes. The Record register.

##### §11.3.0.1 Annual Report (Q4 only)

At the close of Quarter 4, ARBITER delivers an Annual Report following the Summary: a narrative account of the full game arc to date — patterns, shifts, and consequences across Q1–Q4. The Record register. Scripted structure: Art 07 — ARBITER Toolkit.

#### §11.3.1 Observation

ARBITER delivers one observation in The Observation register — never combining both forms:
- *Form A:* *"A faction at this table has moved into [PORTRAIT STATE]. [STATE LANGUAGE]."*
- *Form B:* *"[FACTION]'s contribution to the Portrait this Quarter was [vague adjective]."*

If Chorus Activity changed this Quarter, ARBITER incorporates it as the track moves on the board. Scripted dialogue for each Chorus Activity level: Art 07 — ARBITER Toolkit.

### §11.4 Step 4: Ready to Close

1. When done with Debrief, a Faction Player flips their Status marker to the Ready side.
2. When 3 of 5 Faction Players show Ready: ARBITER starts a 60-second courtesy timer: *"The majority is ready. Sixty seconds."*
3. When the timer expires or all 5 show Ready — whichever comes first — Debrief closes. Proceed to §12 Quarter Close.

*ARBITER observes who signals ready early, who holds out, and when. The Chorus notes this.*

---

## §12 Quarter Close

*Entry: §11 Quarterly Debrief complete.*

At Debrief close, in strict order:

### §12.0 Step 0: Seasonal Card Cleanup

Remove all Seasonal public acts, modifier cards, and any board state cards with Seasonal duration from the board and the Overview. Cards are discarded or removed from game per card text. ARBITER's Situation Report Broadcast Card is removed here if its duration is Seasonal.

### §12.1 Step 1: Findings Decay

The Ghost Faction Player privately calculates their current Findings total and applies decay:
- 7–12: lose 2
- 13+: lose 4

Ghost returns the appropriate number of Findings tokens to the Reservoir and declares the resulting total to ARBITER. ARBITER records the declared total.

*[V1: honor system — Ghost's Findings total is not publicly verifiable. Mechanical enforcement deferred to L2.]*

### §12.2 Step 2: Debrief Reward

ARBITER assesses the Quarter and distributes rewards before the Session Timeline advances.

*Full procedure: Art 07 — ARBITER Toolkit (pending design).*

### §12.3 Step 3: Return Notification Slips

Faction Players return all NS-xx Notification Slips from hand to the ARBITER supply pool.

### §12.4 Step 4: Advance Quarter/Month Tracker

The ARBITER Player advances the Quarter/Month tracker: Quarter +1, Month reset to 1 (M1/Q+1).

If Q1–Q7: proceed to §7 Upkeep, Quarter N+1.

If the tracker reaches Q8 and no Apex has resolved: proceed to Session End per Art 10a — Victory System.

---

## Reference Material

## §13 The Operation System

The Operation System governs resolution for all committed actions: covert operations (Beat 3) and public acts (Beat 4).

*Every committed action resolves with a roll. Submitting an operation or declaring a public act is a commitment — ARBITER renders a judgment on all of them.*

---

### The d100 Roll

A d100 is produced by two ten-sided dice (d10) in two distinct colors. One color is designated as the tens digit; the other as the units digit. Together they produce a result from 01 to 100. Both dice showing 0 = 100.

Establish which color is tens at session start. Keep consistent throughout the session.

If d10 dice are unavailable, any device capable of generating a random integer from 1 to 100 produces an identical result.

*The d100 produces a flat uniform distribution — every result from 01 to 100 is equally likely. A threshold of 50 is a genuine 50% chance of success; a modifier of +15 shifts that probability by exactly 15 points. Probability is transparent: players can calculate exact odds before committing to an operation.*

---

### How to Read the Roll

To succeed, the roll must land equal to or below the target threshold.

*The threshold is the probability of success expressed as a percentage — a threshold of 75 means a 75% chance of success.*

---

### Base Difficulty

Base difficulty is printed on the operation card or public act card. It represents conditions for a competent operative under neutral circumstances.

| Difficulty | Threshold |
|------------|-----------|
| Easy | 75 |
| Average | 50 |
| Challenging | 25 |

*Automatic and Impossible do not appear as base difficulty values. Every committed action resolves with a roll. Automatic and Impossible may appear as explicit card text for specific designed exceptions — they are not base states of the system.*

---

### Critical Results

| Roll | Result | Condition |
|------|--------|-----------|
| 01–05 | Critical Success | Always — regardless of threshold or modifiers |
| 96–00 | Critical Fail | Always — regardless of threshold or modifiers |

*If modifiers reduce the threshold to 0 or below, the roll still occurs — only a Critical Success (01–05) succeeds. If modifiers raise the threshold to 100 or above, the roll still occurs — only a Critical Fail (96–00) fails. The 5% critical floor means no committed action is truly hopeless; the 5% critical ceiling means no action is guaranteed. Critical Success and Critical Fail carry additional action-specific consequences noted on individual operation cards (Artifact 04).*

---

### Difficulty Modifiers

| ID | Category | Name | Scope | Applied | Instance Limit | Value Type | Threshold Adjustment |
|----|----------|------|-------|---------|----------------|------------|----------------------|
| M-01 | Standing | Celebrated | All | Persistent | 1 | Fixed | +20 |
| M-02 | Standing | Respected | All | Persistent | 1 | Fixed | +10 |
| M-03 | Standing | Neutral | All | Persistent | 1 | Fixed | 0 |
| M-04 | Standing | Suspect | All | Persistent | 1 | Fixed | −10 |
| M-05 | Standing | Discredited | All | Persistent | 1 | Fixed | −20 |
| M-06 | Payment | Partial payment marker | Covert | Beat 0 | 1 per submitted card | Fixed | −50 |
| M-07 | Payment | Partial payment marker | Public | Beat 4 | 1 per submitted card | Fixed | −50 |
| M-08 | Card Effect | Modifier card | All | Pre-Resolution | Unlimited | Variable | See card |
| M-09 | Card Effect | Protect / Defend operation | Covert | Beat 2 | 1 per Protect submitted | Variable | See card |
| M-10 | Situation Report | Difficulty effect | All | Beat 1 | 1 per active Event Card | Variable | See Event Card |
| M-11 | Countermeasure | Type B — target faction assets | Covert | Beat 2 | 1 per defending faction | Fixed | −15 |
| M-12 | Ring | No adjacent inward-ring presence | All | Persistent | 1 | Fixed | −25 |
| M-13 | Intel | Stale Intel Token (age 3) | All | Beat 0 / Beat 4 | 1 per stale token | Fixed | −25 |

*All active modifiers are cumulative. Apply all before rolling.*

*Scope: "All" covers all currently defined action types (covert and public). Extends to operative actions when Artifact 05 is designed.*

*Sign convention: positive Threshold Adjustment values raise the threshold (success more likely); negative values lower it (success harder). The partial payment penalty (−50) and ring adjacency penalty (−25) are the largest single Fixed modifiers in the system — a faction simultaneously facing both plus Discredited (−20) and a Type B Countermeasure (−15) is reduced by 110 points, leaving only a Critical Success (01–05) viable on any difficulty tier.*

*Variable modifiers are unbounded by this table — balance analysis across all defined modifier values is maintained in Artifact 03a.*

---

## §14 Special Conditions

### §14.1 Apex Activation

An Apex operation may be submitted as a covert operation (resolved in Beat 3) or as a public act (resolved in Beat 4).

**Step 1 — Identify the Apex.**

When an Apex card is encountered, the current procedure immediately suspends and subroutines to Apex resolution (Steps 2–5). If the Apex is cancelled at Step 4, the procedure resumes from the exact point it was suspended.

- In Beat 3 (covert): suspension occurs when the Apex card is reached in the resolution queue. On return from a failed Apex: continue from the next operation in queue.
- In Beat 4 (public): suspension occurs when the Apex public act is reached in initiative order. The card has been face-up on the Overview since §9.2 Public Declaration. On return from a failed Apex: continue from the next Faction Player in initiative order.

ARBITER announces: *"An Apex operation has been submitted. Resolution is suspended."*

**Step 2 — Confirm resources paid.**

*Covert:* Resources were confirmed at Beat 0. If this step is reached, the card was face-up and payment is already in the Reservoir.

*Public:* The ARBITER Player confirms resources were transferred to the Reservoir at Beat 4 Submit Payment. If payment is incomplete: Apex fails. Resources spent. Resolution resumes.

**Step 3 — Process Emergency Responses.**

Resolution is suspended at the current position. Each non-Apex faction submits one Emergency Response. Emergency Responses are submitted simultaneously and resolved by ARBITER in initiative order. They may change board state — presence chips, structure blocks, Public Standing — before the threshold check in Step 4.

*Resources committed to submitted operations are not refunded.*

*Emergency Response design is pending Artifact 04 / Artifact 05. Design note: Emergency Responses may be used to assist or thwart the Apex — Board Strength may increase or decrease before Step 4's threshold check.*

**Step 4 — Check Board Strength threshold.**

After Emergency Responses resolve, the ARBITER Player counts the Apex faction's total presence chips and structure blocks (Board Strength). If the total does not meet the threshold specified in Artifact 05, the Apex is cancelled. Resources spent. Operative does not retire. Resolution resumes from the suspended position.

*Board Strength is checked here — after all Emergency Responses — not at submission. A faction may use their Emergency Response to assist the Apex (raising Board Strength) or oppose it (reducing Board Strength). This is load-bearing for Emergency Response design in Artifact 04 / Artifact 05.*

**Step 5 — Resolve Apex.**

The ARBITER Player opens the sealed Apex envelope and pauses 5 seconds. ARBITER reads the Apex narrative card aloud. The ARBITER Player applies all public board effects and updates the Chorus Portrait track. The session ends. Proceed to Session End per Artifact 10a — Victory System.

*Operations remaining in the suspended queue do not resolve. Resources committed to submitted operations are not refunded.*

*Full Apex rules in Artifact 05 — Operative & Apex System.*

---

## §15 Duration Taxonomy

All public acts, modifier cards, and board state cards carry one of four duration types. Duration is printed on the card. Cleared behavior (return to discard pile vs. remove from game) is specified per card text.

| Type | Duration | Cleared |
|------|----------|---------|
| Immediate | Placed on the board; resolves immediately upon placement. Must move from hand to board to trigger. Cannot be returned to hand, discarded, or removed from game until placed on the board. | Per card text after resolution — removed from board (discard or remove from game) |
| Transient | Active for this month only | Beat 5 cleanup of the month in which it was played |
| Seasonal | Active for this Quarter | End of Quarter — §12.0 Seasonal Card Cleanup |
| Permanent | Active until a named action or condition removes it — including a self-clearing trigger on the card | Per card text (discard or remove from game) |

*ARBITER's Situation Reports carry Seasonal duration by default. Card text may specify otherwise.*

*Modifier react cards may carry any duration type — a react that creates a persistent board state remains on the board with its stated duration.*

---

## §16 Public Act Placement Rules

1. Public acts are declared during §9.2 (Public Declaration), in initiative order.
2. The declaring Faction Player places the card face-up on the Overview in the target district (or in the relevant zone for non-district acts).
3. Attach the Target Profile and 1 Dispatch Token on top of the card. Resource tokens remain with the card — payment is submitted to the Reservoir at Beat 4.
4. Modifier cards modifying the public act are placed face-up alongside the card on the Overview.
5. Once placed, the card is a valid target for Countermeasure cards (§9.3 Countermeasures) and other public acts.
6. Public acts cannot be withdrawn or modified after placement.
7. ARBITER's Situation Reports are placed in the Event Zone during Upkeep (§7.2) and follow the same duration and targeting rules as faction public acts.
8. A public act card remains on the board until its duration expires. Beat 4 resolution does not necessarily remove the card — duration governs removal.
   - Transient cards are removed at Beat 5 of the month in which they were played.
   - Seasonal cards remain on the board until End of Quarter.
   - Permanent cards remain until a named action or condition removes them.

---

## §17 Countermeasure Card Rules

1. Each faction receives 3 Countermeasure cards at game start. They are issued, not drawn.
2. Countermeasure cards are removed from the game when used — they do not return to hand or discard pile.
3. Countermeasure cards are submitted during the Countermeasure Window each month (§9.3).
4. A Countermeasure card may target either:
   - A queued covert operation in a submitted dispatch case, or
   - A placed public act currently on the Overview.

   Type A Countermeasures (CM-A) void their target at Beat 1. Type B Countermeasures (CM-B) apply a modifier token to their target at Beat 2 (covert operations; public act timing TBD).
5. Unused Countermeasure cards carry forward to the next Monthly window. A faction may hold all 3 through Month 3 or spend them early.
6. Full Countermeasure card types and effects: Artifact 04 — Action Card System.

---

## §18 React Card Rules

React cards fire in response to publicly visible board state changes. They are held in hand until their trigger condition is met.

1. A React card may only fire on a publicly visible board state change. It cannot fire on ARBITER-internal state changes such as the Resolution Grid.
2. When a trigger condition is met: the holding Faction Player announces *"React"*, presents the card, and states the trigger condition listed on the card. ARBITER confirms the trigger is valid and pauses the quarter procedure.

    2a. First to announce pauses play. ARBITER decides tiebreakers. Only one React resolves at a time — a second React may only fire in response to the new board state produced after the first resolves.

    2b. A React must be announced at the moment the triggering board state change occurs. It cannot be declared retroactively — once the procedure moves past the trigger point, the window closes.

3. The React card resolves per its stated effect.
4. Once the React has resolved, the original procedure resumes from the point it paused.

### §18.1 Modifier React Cards

If a modifier react card creates a persistent board state (a card placed on the board), the card remains with its duration type per §15.

---

## §19 Examples & Exceptions

### Initiative — Quarter 3

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

*Quarter 5 Beat 3. The Directorate's Detain operative ability successfully resolves against Ghost. Ghost has a deployment marker at Data Exchange showing the Converting face.*

The ARBITER Player flips Ghost's Data Exchange marker to the Blocked face. The marker remains at Data Exchange through the end of Quarter 5.

*Quarter 6 Upkeep Step 4: Ghost checks markers on the board. The Data Exchange marker shows the Blocked face. Ghost returns the marker to hand without placing a presence chip. Ghost's influence at Data Exchange does not increase.*

---

### Countermeasure — Type B Example

*Quarter 5. The Directorate plays a Type B Countermeasure. All target thresholds against The Directorate's assets are −15.*

Ghost submits a Gather at Government Citadel (no presence — Challenging base, target 01–25). Public Standing: Neutral (0). Type B modifier: −15. Modified target: 01–10.

Ghost rolls: 18. Target is 10. Fails. The Directorate's defensive preparation made an already difficult operation nearly impossible without being able to block it outright.

---

### Dispatch Case Return — Processing Results

*Beat 3 complete. The ARBITER Player returns Ghost's dispatch case.*

Ghost finds:
- Gather at Data Exchange — returned face-up
- Undermine at Financial Clearinghouse — returned face-down (voided at Beat 1; targeting restriction)
- Build Structure at Government Citadel — returned face-down (voided at Beat 1; Type A Countermeasure)
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

The Network and The Directorate reach agreement with 20 seconds remaining. Both flip to green. ARBITER closes Debrief. Accord registered. Quarter closes.

---

### Apex Interrupted — Beat 3

*Quarter 7 Beat 0. ARBITER opens The Guild's dispatch case, encounters an Apex operation card, and verifies resources. Resources from all dispatch cases are drained to the Reservoir. Beat 3: The Guild's Apex card is reached in the resolution queue.*

ARBITER announces: *"An Apex operation has been submitted. Resolution is suspended."*

The operation queue is suspended. Resources committed to all submitted operations were drained in Beat 0 and are not refunded. Each non-Guild faction submits one Emergency Response.

The Network uses their Emergency Response to Undermine The Guild's presence at Power Grid, reducing their presence chip count. The Directorate Occupies Government Citadel, adding presence chips to their own position.

After Emergency Responses resolve, the ARBITER Player counts The Guild's Board Strength: 11 presence chips + 4 structure blocks = 15. Threshold required: 12. Still met.

The ARBITER Player opens the sealed Apex envelope and pauses. ARBITER reads. The session ends.
