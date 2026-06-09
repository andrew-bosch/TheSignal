# 03 — Quarter Structure & Gameplay
## THE SIGNAL P1 — Paper Prototype

**Version:** 3.3  

**Status:** ✅ Signed Off — S68 (L189).  

**Depends on:** 00 — Factions, World & Narrative Context; 01 — Game Board: New Meridian; 02a — Resource Systems: Board State; 02b — Resource Systems: Tracking  

**Supersedes:** round_structure (retired artifact)

---

## 1. Overview

### Problem This Document Solves
Without a precise, ordered description of how each Quarter is structured — what happens, in what sequence, who does it, and what information is available when — no artifact describing specific actions, resolutions, or ARBITER behavior can be written consistently. This document is the skeleton that all subsequent system artifacts attach to.

### Deliverable
The complete structure of a single Quarter of THE SIGNAL: six phases in sequence, the events within each phase in order, who performs each step, and the rules governing timing, priority, and transitions between phases.

### Success Criteria
- ARBITER can follow the sequence of a complete Quarter from this document — knowing what happens in what order and who does it, with references to where specific mechanical details live in subsequent artifacts
- Players know at any point in the Quarter what phase they are in, what is expected of them, and what comes next
- The document contains no undefined terms from prior artifacts (00–02b)
- The Quarter sequence is complete — no phase or transition is missing or ambiguous

---

## 2. Index

1. [Overview](#1-overview)
2. [Index](#2-index)
3. [Game Purpose](#3-game-purpose)
4. [Narrative Function](#4-narrative-function)
5. [Design Principles](#5-design-principles)
6. [Quarter Overview](#6-quarter-overview)

**Gameplay Procedure**

7. [Phase 1 — Upkeep](#7-phase-1-upkeep)
8. [Phase 2 — Placement](#8-phase-2-placement)
9. [Month 1 — Dispatch](#9-month-1-dispatch)
10. [Month 1 — Countermeasures](#10-month-1-countermeasures)
11. [Month 1 — Resolution](#11-month-1-resolution)
12. [Month 2 — Dispatch](#12-month-2-dispatch)
13. [Month 2 — Countermeasures](#13-month-2-countermeasures)
14. [Month 2 — Resolution](#14-month-2-resolution)
15. [Month 3 — Dispatch](#15-month-3-dispatch)
16. [Month 3 — Countermeasures](#16-month-3-countermeasures)
17. [Contested District Resolution](#17-contested-district-resolution)
18. [Month 3 — Quarter Notes](#18-month-3-quarter-notes)
19. [Debrief](#19-debrief)
20. [End of Quarter](#20-end-of-quarter)

**Reference Material**

21. [The Operation System](#21-the-operation-system)
22. [Special Conditions & Gameplay Impacts](#22-special-conditions-gameplay-impacts)
23. [Duration Taxonomy](#23-duration-taxonomy)
24. [Public Act Placement Rules](#24-public-act-placement-rules)
25. [Modifier React Card Rules](#25-modifier-react-card-rules)
26. [Countermeasure Card Rules](#26-countermeasure-card-rules)
27. [Examples & Exceptions](#27-examples-exceptions)
28. [React Card Rules](#28-react-card-rules)

---

## 3. Game Purpose

The Quarter structure is the engine of the session. It defines the rhythm of play — when information is revealed, when commitments are made, when consequences land. Every player decision happens within a specific phase with specific constraints on what they know and what they can do. The sequence is designed so that the most consequential decisions are made after the board state is known but before outcomes are resolved.

Eight Quarters constitute a session. The session ends either at the completion of Quarter 8 or when an Apex ability resolves — whichever comes first.

---

## 4. Narrative Function

The temporal grounding of the Quarter — its real-world equivalence and its relationship to the Chorus timeline — is defined in 00a §3.1. Each Quarter carries weight proportional to what it follows; The Table is not working on a human schedule. That weight is expressed in what each Quarter action means at scale:

- A structure block is not a completed building but an established operational presence — a secured facility, a contracted team, a functioning node. Three months is enough time to establish a foothold; not enough to build a headquarters.
- Influence growth represents sustained organizational investment over a quarter — relationships cultivated, presence consolidated, community engagement maintained.
- A Situation Report represents a significant event at the city or global scale — something meaningful enough to shape a quarter of operations, not a daily news cycle.
- A faction operating in The Mid or Core without a foothold in the adjacent inward ring is working without local networks, cover, or intelligence — the infrastructure of operational presence. That exposure doesn't block an attempt. It makes it harder.
- A fresh Intel Token targeting the opposing faction adds +2 to Battlefield Strength. Intelligence on your opponent — their movements, their assets, their exposed positions — is not merely informational. At the moment of contested ground, it is force.

The Quarter's three active Months each carry both covert and public operations. The covert work of Month 1 and Month 2 shapes what public acts are viable by Month 3 — but all three months offer both modes of play. Factions choose how to allocate their Dispatch Tokens each month: operations sealed in a case, or acts declared openly on the board. The sequence is not arbitrary; it is how organizations actually work under pressure.

The Quarter's internal structure mirrors how organizations operate under pressure: situational awareness first (Upkeep), then positioning (Placement), then three months each with covert and public acts (Month 1 → Month 2 → Month 3), then a reckoning between contested factions, then the conversation about what it all meant (Debrief).

Where two factions have contested the same ground for the full Quarter, the board forces a reckoning before the Table convenes. Battlefield Strength is the Quarter's final act of consequence — decided not by cards or resources but by who committed more deeply to the district and its surroundings.

ARBITER is present throughout but speaks at specific moments. Between those moments, ARBITER watches.

---

## 5. Design Principles

1. **Information flows forward, never backward.** Players learn the board state at Upkeep, then commit to each pass with what that moment offers — no prior commitment can be revised. Covert outcomes from Month 1 are available before Month 2 dispatches; covert and public outcomes from both prior months inform Month 3. The sequence is intentional: the highest-stakes commitment is always made with the most information.

2. **Commitment is irreversible.** Once a dispatch case is closed, its contents cannot be changed. Once a public act is declared on the board, it cannot be withdrawn.

3. **The board is always honest.** At every point in the Quarter, the board reflects the true current state. Only dispatch case contents and ARBITER's tableau are private.

4. **Players run their own economy.** Resource collection, marker placement, flag and marker updates, and structure block removal are all performed by players. ARBITER facilitates and resolves disputes.

5. **Speed has consequences.** Dispatch case submission order is the tiebreaker within resolution priority tiers.

6. **ARBITER executes procedures, not exceptions.** All ARBITER-facing content in this artifact is written as generalizable rules applicable uniformly across all game states within their phase. No phase-specific or context-specific exception procedures. Complexity is managed through physical tools and reference materials, not through ARBITER memorization. *Governing Rule 6.1.*

---

## 6. Quarter Overview

```
PHASE 1 — UPKEEP
  Quarter opens. World updates. Resources collected. Tokens distributed. Initiative set.

PHASE 2 — PLACEMENT
  Deployment markers placed. Entry requirements enforced.

MONTH 1 — DISPATCH
  Phase A: Covert Dispatch — cases assembled, sealed, transmitted.
  Phase B: Public Declaration — public acts declared in initiative order; placed face-up on the Overview.

MONTH 1 — COUNTERMEASURES
  Countermeasure Window — countermeasure cards submitted; may target queued covert ops or placed public acts.

MONTH 1 — RESOLUTION (Month1.Week1–4, Beats 0–5)
  Beat 0 (cases open) → Beat 1 (board state read) → Beat 2 (conditions set) →
  Beat 3 (covert ops resolve) → Beat 4 (public acts resolve) → Beat 5 (cleanup).

MONTH 2 — DISPATCH
  Phase A / Phase B — follows Month 1 Dispatch structure. Remaining Dispatch Tokens used.

MONTH 2 — COUNTERMEASURES
  Follows Month 1 Countermeasures structure.

MONTH 2 — RESOLUTION (Month2.Week1–4, Beats 0–5)
  Follows Month 1 Resolution structure.

MONTH 3 — DISPATCH
  Phase A / Phase B — follows Month 1 Dispatch structure. Final Dispatch Token use.

MONTH 3 — COUNTERMEASURES
  Follows Month 1 Countermeasures structure.

MONTH 3 — RESOLUTION (Month3.Week1–4, Beats 0–5)
  Follows Month 1 Resolution structure.
  Beat 3 Step 12: dispatch cases returned. Debrief follows.

CONTESTED DISTRICT RESOLUTION
  Contested districts resolve. d10 roll-off per district. Tension markers cleared.

DEBRIEF
  Table reflects on outcomes. Quarter closes.
```

Phases do not overlap. ARBITER announces the start of each phase.

---

## Gameplay Procedure

## 7. Phase 1 — Upkeep


- ARBITER announces each step.
- Faction Players perform their own updates.

### Step 1 — Status Marker Reset

Each Faction Player flips their Status marker to the Discussing side (yellow/text).

*This is the physical act that opens the Quarter — a personal acknowledgment that a new quarter of operations has begun and the previous Quarter is fully closed.*

### Step 2 — Initiative

- ARBITER determines initiative order. (Full procedure: Artifact 07 — ARBITER Toolkit)
- ARBITER announces the final order.
- The ARBITER Player updates the Initiative Strip on the board.

### Step 3 — Situation Report

*The Situation Report is ARBITER's public act for the Quarter. The Broadcast Card placed on the Overview is a standing public act with Seasonal duration by default (active until End of Quarter) unless the card specifies otherwise. It is a valid target for faction public acts and countermeasures once placed. Beat 1 reads SitRep effects as standing public acts each month.*

ARBITER announces: *"Situation Report."*

1. The ARBITER Player draws the top Broadcast Card from the session deck and places it face-up in the Event Zone on The Overview.
2. The ARBITER Player locates the matching Event Card from the Event Card deck and places it on the ARBITER tableau.
3. The ARBITER Player reads the Event Card.
4. As applicable, ARBITER announces Public Standing track changes — reads the indicated narrative on the Event Card aloud.

   *Do not announce difficulty modifiers or hidden mechanical effects.*
5. Each Faction Player moves their Public Standing marker as indicated by ARBITER.
6. If the Event Card specifies a deployment marker cannot convert this Quarter: The ARBITER Player flips the affected marker(s) to the Blocked face.
7. The ARBITER Player reviews all Event Cards on the ARBITER tableau and moves expired cards to the expired area of the ARBITER tableau.

   *No tick-downs or maintenance — duration management occurred at the close of the previous Quarter.*

### Step 4 — Deployment Marker Conversion

ARBITER announces: *"Markers convert."*

1. Each Faction Player checks deployment markers currently on the board.
2. For each marker showing the Converting face: place 1 permanent presence chip in that district and return the marker to hand.
3. For each marker showing the Blocked face: return the marker to hand without placing a presence chip.
4. Each Faction Player updates Control flags, Established markers, and Tension markers as influence levels shift from new presence chip placements.

*If no markers are on the board — as is always the case at the start of Quarter 1 — this step has no effect. Proceed to Step 5.*

### Step 5 — Resource Collection

ARBITER announces: *"Collect income."*

Each Faction Player simultaneously calculates and collects their own resources:

1. For each district with presence chips or deployment markers: apply influence level modifier to base generation value
2. Add affinity bonus where applicable (Dominant in native resource district: +1)
3. For each structure block: declare resource type publicly (district resource or faction native resource), collect +1
4. Add passive generation (1 unit of faction native resource, unconditional)

Other Faction Players observe and may challenge calculations. ARBITER resolves disputes in The Record register.

*If The Network has any presence at University Perimeter:*
The Network Faction Player declares whether Exposure or the district native resource will be collected from the virtual structure block.

---

### Step 6 — Operations Preparation

ARBITER announces: *"Prepare operations."*

*Purpose: ensure all elements needed for the Quarter are assembled and in their correct positions on the tableau. Faction Players complete this step simultaneously.*

**Distribute Dispatch Tokens:**

Each Faction Player collects 4 Dispatch Tokens from The Backlog.

*Tokens are held beside the tableau. They are spent across Months 1, 2, and 3 as the player chooses.*

**Tableau check — standing elements:**

Verify the following elements are already in position before drawing begins:
- Floor Act — beside tableau, always available to all factions at all times (full design: Artifact 04 D04-13)
- Countermeasure cards — in their designated area (3 per session total; deployed across Monthly Countermeasure phases, §10/§13/§16)
- Modifier cards carried from prior Quarters — in modifier area
- Operator cards — in their designated area

**Action card draw:**

1. Count covert operation cards currently in hand. Draw from personal draw deck to reach a hand of 6.
2. Count public act cards currently in hand. Draw from public act draw deck to reach starting hand size.

   *[Open question: public act hand size under monthly play. Current default: 3. May require revision — see PM05.]*

3. Place all drawn cards in the active hand area of the tableau. Cards are held face-down and private.

*Cards kept from the prior Quarter count toward hand size — a player with 2 kept covert cards draws 4 more to reach 6.*

*Covert operation hand is drawn here only. No additional covert cards are drawn during Monthly Dispatch. Discard down if hand size exceeds maximum at any point.*

If a draw deck is exhausted mid-draw, shuffle that deck's discard pile immediately to form a new draw deck and continue.

*Both decks reshuffle independently.*

**Modifier card draw:**

*A faction that has triggered Burst Play this session is exempt from modifier card draws — skip this sub-step.*

Draw and place modifier cards in the tableau modifier area.

1. **Faction modifier draw:** Draw from the faction modifier deck in the player's tableau.

   | Structure blocks owned | Faction modifier cards drawn |
   |------------------------|------------------------------|
   | 0–1 | 0 |
   | 2–3 | 1 |
   | 4–5 | 2 |
   | 6+ | 3 (maximum) |

2. **Ring modifier draw:** A ring qualifies if the faction meets all of the following conditions:
   - At least 1 structure block in that ring
   - Established or higher presence in at least 1 district in that ring

   Draw 1 card for each qualifying ring. A faction may qualify for all three rings.

   *Modifier decks (faction and ring) are not reshuffled when exhausted.*

3. **Burst Play window:** After completing all draws, before Dispatch opens, a faction may trigger Burst Play. If triggered:

   1. Declare Burst Play to ARBITER.
   2. Trade ALL held modifier cards to the Reservoir — 1 resource of any type per card, chosen independently per card.
   3. ARBITER announces publicly: *"[Faction] has liquidated their operational reserve."* Resource gain is private.
   4. Remove the faction modifier deck from the tableau. It does not return for the remainder of the session.

   *Modifier draws are skipped at all future Hand Assembly steps for this faction.*

*Full card draw rules, deck construction, hand size, modifier card rules, and Burst Play (§11.6) are specified in Artifact 04 §12.*

---

## 8. Phase 2 — Placement


- Faction Players place their own markers.
- ARBITER enforces entry requirements.

ARBITER announces: *"Placement is open."*

1. Faction Players place their two deployment markers in initiative order, snake pattern:
   - **Forward pass:** Rank 1 through Rank 5, one marker each
   - **Reverse pass:** Rank 5 through Rank 1, second marker each

   *All deployment markers are placed with the Converting face showing by default.*

   *A deployment marker counts as 1 temporary presence chip immediately upon placement.*

2. Before placing in each district, verify entry requirements:

| Ring | Entry Requirement | Threshold Modifier |
|------|-------------------|--------------------|
| Baryo | None | None |
| The Mid | None | −25 to all operations targeting this district if no presence in any adjacent Core district |
| Core | Established or higher in an adjacent The Mid district (permanent presence chips or temporary presence from first marker this phase) | −25 to all operations targeting this district if no presence at the Chorus Node |
| Chorus Node | Established or higher in an adjacent Core district (permanent presence chips or temporary presence from first marker this phase) | −25 to all operations targeting this district |

3. After each placement, if influence levels change: the placing Faction Player updates the relevant Control flag, Established marker, or Tension marker immediately.

*A Faction Player may pass either or both placements. ARBITER redirects illegal placements.*

---

## 9. Month 1 — Dispatch

**Dispatch Token rule:** Each action requires 1 Dispatch Token. Covert operations: token placed in the dispatch case with the operation card (Phase A). Public acts: token placed on the declared card on the Overview (Phase B). A covert operation card submitted without a token is rejected by ARBITER at Beat 0 without resolution and returned to the faction. A public act declared without a token is invalid.

*Faction Players budget their Dispatch Tokens across Months 1, 2, and 3, split between covert operations and public acts as they choose. Not spending a token is a pass for that action.*

---

### Phase A — Covert Dispatch

- *Faction Players assemble, seal and transmit their own dispatch cases.*
- *The ARBITER Player keeps watch on the Dispatch Timer, announces status, and queues cases in the order they are received.*

**1. Open Dispatch**
- ARBITER announces: *"Month 1 Dispatch is open."*
- The ARBITER Player starts the dispatch timer.

**2. Assemble cases**

- Faction Players load operation cards, Dispatch Tokens (1 per operation card), resources, target slips, and any Modifier Cards being assigned to specific operations into their cases.

*Modifier Cards (Faction Modifier Cards and Ring Modifier Cards, drawn at Upkeep §7 Step 6) are assigned to operations by placing each card in the case with that operation's packet. A faction may assign Modifier Cards to some, all, or none of their submitted operations. Unassigned Modifier Cards remain in the tableau modifier area and are not submitted.*

*Assembly should be handled privately and silently.*

*Full dispatch case design, physical format, and component contents: Artifact 06 — Messaging System.*

**3. Seal cases**

- Faction Players close their cases.

*No additions or changes permitted after sealing cases.*

**4. Transmit cases**

- Faction Players place their sealed cases in the ARBITER Player's receive queue.
- The ARBITER Player places each received case left to right in the receive queue, establishing lane order for the Month 1 Resolution Grid.

*Case receipt order determines lane assignment in the Resolution Grid and governs Beat 3 operation sequence.*

**5. Close Dispatch (When timer ends)**
- The ARBITER Player announces: *"Timer."*

  *No new additions to any case — sealed or open.*

- The ARBITER Player counts: *"Five. Four. Three. Two. One."*

  *Faction Players who have not transmitted may seal and transmit during the countdown.*

- The ARBITER Player announces: *"Month 1 Dispatch closed."*

  *Any case not received is treated as containing no covert operations.*

---

### Phase B — Public Declaration

- *Faction Players declare publicly, in initiative order.*
- *The ARBITER Player records declarations.*

ARBITER announces: *"Public Declaration is open."*

For each Faction Player in initiative order:

- **Pass** — verbally declare no public act will be played this phase, or
- **Declare** — name the public act and place it on the board:

1. Announce the public act being declared.
2. Place the declared card face-up on the Overview in the target district, with the target slip and 1 Dispatch Token stacked on top. Resource tokens remain with the declared card — payment is submitted to the Reservoir at Beat 4.
3. Play any modifier cards modifying the public act face-up alongside the card on the Overview.

*Once placed, the card is a valid target for countermeasures (Countermeasure Window, §10) and other public acts.*

*Declared public acts cannot be withdrawn or modified after placement.*

*Public acts resolve in initiative order at Beat 4. Full placement rules: §24.*

ARBITER announces: *"Public Declaration closed."*

---

## 10. Month 1 — Countermeasures

### Countermeasure Window

- Faction Players deploy or pass in initiative order.
- The ARBITER Player holds Countermeasures for application during Month 1 Resolution.

ARBITER announces: *"Countermeasure Window is open."*

Each Faction Player, in initiative order:

- **Pass** — verbally declare no Countermeasure card will be played this phase, or
- **Deploy** — play one or more Countermeasure cards. For each card deployed:

1. Play the card face-up in front of the Faction Player's tableau.
2. Declare the card type and target to the ARBITER Player. Countermeasures may target:
   - A queued covert operation in a submitted dispatch case, or
   - A placed public act currently on the Overview.
3. Hand the card to the ARBITER Player.

*Each faction has 3 Countermeasure cards per session total across all three Monthly windows. Cards spent here are unavailable in Month 2 and Month 3. Full Countermeasure card rules: §26.*

When all Faction Players have had a chance to deploy or pass, the ARBITER Player collects all dispatch cases.

Phase ends.

---

## 11. Month 1 — Resolution

### Resolution

- The ARBITER Player runs Month 1 Resolution in six sequential beats (Month1.Week1–4, Beats 0–5).
- Faction Players receive outcomes and apply their own board updates.

*The Resolution Grid is built fresh for Month 1 and cleared at end of Beat 3. Month 2 builds a new grid.*

*ARBITER announces each beat before beginning it.*

---

**Beat 0 (Month1.Week1): The Cases Open**

The ARBITER Player:
- Arranges Dispatch cases left to right in numbered lanes above the top of the resolution grid in the order received.
- Opens all cases and builds the Resolution Grid.

From left to right, lane by lane:

1. Remove the first operation packet from the dispatch case.
2. For each card in the packet, validate payment using the Payment Validation table below.
3. Drain resources to the Reservoir as directed.
4. If a Dispatch Token is present with the card: set aside the token. If no Dispatch Token accompanies the card: the card is rejected by ARBITER without resolution. Return the operation card to the acting faction. No Operation Resolution card issued.
5. Place each validated card in the grid based on what Beat is indicated on the card:
   - Beat 2 card: place in the Beat 2 row of the resolution grid for the lane being processed.
   - Beat 3 card or Pass: place in the uppermost vacant space in the Beat 3 section of the resolution grid for the lane being processed.
     - Stack bottom to top: target slip, Modifier Cards (if any), operation card (or pass).

     *Cards are placed face-up or face-down per Payment Validation.*
     *Overlap so each card beneath shows its resolution data block.*
     *(Modifier Card application procedure and ring modifier per-token rate calculation: Art 07 — ARBITER Toolkit.)*
6. Repeat steps 1–5 for each remaining lane in receipt order (Lane 2 through Lane 5).
7. Collect all Dispatch Tokens from this Month. Return to The Backlog.
8. When complete, move to Beat 1.

*If card order within a case was disrupted in transit, the order ARBITER encounters the cards is the resolution order.*

**Payment Validation**

| Payment | Applies to | Resources | Card Placement |
|---------|------------|-----------|----------------|
| Full | All | Drain to Reservoir | Face-up in grid |
| Partial | Non-Apex | Drain to Reservoir; attach −50 threshold marker to stack | Face-up in grid |
| Zero | Non-Apex | None to drain | Face-down in grid |
| Any shortfall | Apex | Drain any submitted resources to Reservoir | Face-down in grid |
| Retained | Resource-retaining cards | Validate Resource count matches declared value on target profile; resources declared are placed on card — do not drain to Reservoir. Any unallocated resources (not placed on Beat 3 cards in Beat 2) are placed in target_faction's dispatch case. | Face-up in grid |

**Resolution Grid layout:**

| | Lane 1 | Lane 2 | Lane 3 | Lane 4 | Lane 5 |
|---|--------|--------|--------|--------|--------|
| *(case receipt order →)* | first received | | | | last received |
| Beat 2 row | | | | | |
| Beat 3 card 1 | | | | | |
| Beat 3 target 1 | | | | | |
| Beat 3 card 2 | | | | | |
| Beat 3 target 2 | | | | | |
| *(up to 4 pairs — Ghost)* | | | | | |

*Beat 4 processes placed public acts on the Overview — public acts do not appear in the Resolution Grid.*

*Beat 3 processes row-first across all lanes: all card-1 pairs resolve left to right before any card-2 pair begins. Round-robin initiative by case receipt — submission speed rewards getting your first operation in, not locking in a full sequence before others act. (L102)*

*Modifier cards in a stack peek out at the bottom to display their values during resolution. Modifier card physical design must support cascade orientation — value printed prominently at both top and bottom edge. (XA-22, Art 11)*

**Intel Token Freshness**

If any Intel Token is submitted as part of payment, for each token calculate age: current Quarter number − Quarter number written on the token.

1. Age 0–2: fresh — no modifier applied.
2. Age 3: stale — attach a −25 Intel freshness modifier to the stack (M-13).
3. Age 4 or more: expired — counts as partial payment (see Payment Validation table above).

All submitted Intel Tokens are reset (erased) and returned to The Dossier, or discarded if single-use.

*Quarter number and faction are written on each token by ARBITER at issuance. Physical form TBD — reusable erasable medium (erased on return) or single-use paper chit (discarded on use); see PM05 03-13. Expired tokens not submitted have no payment value but may be held and traded — age is visible on the token.*

---

**Beat 1 (Month1.Week2): Read Board State**

The ARBITER Player reads all currently active board effects aloud — Situation Report effects, standing public acts on the Overview (including tripwires and Permanent cards placed in prior months), and any other active world effects.

**Targeting restrictions** — effects that prevent operations in specific districts or rings:

1. The ARBITER Player identifies all targeting restrictions from active board state.
2. For each targeting restriction: scan the Beat 3 rows of the Resolution Grid for covert operations targeting the restricted district or ring. For each match:
   - Place the operation card and target slip face-down in the acting faction's dispatch case. Face-down operation cards are void.
   - Discard any modifier cards from the grid cell — removed from the game.

   *Modifier Cards on voided operations are consumed without effect.*

3. For each targeting restriction: scan placed public acts on the Overview targeting the restricted district or ring. For each match:
   - Return the public act card face-down, target slip, and resource tokens to the Faction Player. Face-down action cards are void.
   - Discard any modifier cards placed alongside the act — removed from the game.
   - Return the Dispatch Token to the acting faction.

   *Public act resources are not committed until Beat 4 Submit Payment — voiding before Beat 4 refunds all tokens.*

**Conversion blocks** — effects that prevent deployment marker conversion in specific districts or rings:

1. The ARBITER Player identifies any conversion-blocking effects on active Event Cards.
2. The ARBITER Player flips any affected deployment markers to the Blocked face.

*No other board changes, track updates, or maintenance occur in this beat.*

---

**Beat 2 (Month1.Week3): Conditions Set**

Beat 2 is the condition-setting beat. All cards with `beat = 2` are processed before any Beat 3 operations resolve. Current Beat 2 cards: Type A/B Countermeasures, C10 Protect, C11 Fortify Structure. Cards C21, C25, C28, C34, C35 are pending design — any card with `beat = 2` is processed here when defined.

*C06 Broadcast Interference and C07 Amplify are redesigned as Seasonal public acts — see Art 04.*

The ARBITER Player processes the Beat 2 row of the Resolution Grid left to right, then processes any Countermeasure cards held targeting placed public acts.

**For each Type A Countermeasure card (District Block):**

1. The ARBITER Player identifies all operation cards in the Beat 3 rows of the grid targeting the named district.
2. For each matching covert operation:
   - Place the operation card and target slip face-down in the acting faction's dispatch case. Face-down operation cards are void.
   - Discard any modifier cards from the grid cell — removed from the game.
   - Return any modifier tokens placed on the card to the pool.

   *Modifier Cards on voided operations are consumed without effect.*

   *Resources committed to blocked operations are not refunded — the attempt was made and met resistance.*

3. The ARBITER Player identifies any placed public act on the Overview targeting the named district.
4. For each matching public act:
   - Return the public act card face-down, target slip, and resource tokens to the Faction Player. Face-down action cards are void.
   - Discard any modifier cards placed alongside the act — removed from the game.
   - Return the Dispatch Token to the acting faction.

   *Public act resources are not committed until Beat 4 Submit Payment — voiding before Beat 4 refunds all tokens.*

5. The ARBITER Player flips any deployment markers in the named district to the Blocked face.
6. Discard the Type A Countermeasure card — removed from the game.

**For each Type B Countermeasure card (Faction Defense):**

1. The ARBITER Player identifies all operation cards in the Beat 3 rows targeting that faction's assets.
2. The ARBITER Player places a −15 modifier token on each identified operation card in the grid.
3. Discard the Type B Countermeasure card — removed from the game.

*Physical modifier token design: Artifact 07 — ARBITER Toolkit.*

**For each Protect operation:**

1. The ARBITER Player identifies the target operation cards in the Beat 3 rows.
2. Calculate the defensive modifier total: Protect base value + any Modifier Card value submitted with this Protect.
3. Place a modifier token on each target operation card equal to the total defensive modifier.
4. Discard any Modifier Cards submitted with the Protect — removed from the game.
5. Return the Protect card to the acting faction's dispatch case.

**For each Fortify Structure operation (Guild only):**

1. The ARBITER Player identifies the target structure — the Guild structure token in the named district.
2. ARBITER retains awareness — no grid effect at Beat 2.
3. At Beat 3: if any Demolish operation in the grid targets the fortified structure, ARBITER intercepts at Step 1 of that operation's resolution. The Demolish has no effect. ARBITER announces: *"The structure in [DISTRICT] is reinforced. Demolition has no effect this Quarter."* Place the Demolish operation card and target slip face-down in the Demolish submitter's dispatch case. Face-down operation cards are void.
4. Return the card to the acting faction's dispatch case.

**For each Golden Parachute card:**

1. Identify the Beat 3 column belonging to `target_faction` in the Resolution Grid. Apex is not a valid target.
2. Scan that column top to bottom (submission order). For each **face-up** operation card in the column that names Syndicate as target:
   a. Place resources from the card's retained stack onto that operation — amount equal to the operation's cost value — until the retained stack is exhausted.
   b. If the retained stack is exhausted before all qualifying operations are covered, remaining operations receive no resources.
3. Any cards in Beat 3 where resources placed on the Beat 3 card equal the total resource cost on that card: flip the Beat 3 card face-down, then place those resources into target_faction's dispatch case.
   3a. Any cards in Beat 3 where resources placed on the Beat 3 card are less than the total resource cost on that card: place a partial payment modifier token on the Beat 3 card, then place those resources into target_faction's dispatch case.
4. Discard the target profile slip and any modifier cards submitted with Golden Parachute.
5. Return the Golden Parachute card to Syndicate's return case.

---

**Beat 3 (Month1.Week4): Covert Operations Resolve**

Resolve all covert operations from the Resolution Grid in queue order: the first action for each faction fires in case receipt order, then the second action for each faction, repeating until the operation queue is empty.

*The grid is pre-cleaned by Beats 1 and 2 — every card reached is a valid, unblocked operation.*

For each card in queue order:

**Step 1 — Identify the operation.**

1. Read the card in the current grid slot.
2. If face-down: auto-fail. Discard all modifier cards from the stack. Return the action card to the faction. Advance to the next operation. No further steps apply to this slot.
3. Check for Apex submission. If Apex: resolution is immediately interrupted — see Apex Activation in §22 before proceeding.

**Step 2 — Determine base difficulty.**

Read the base difficulty printed on the operation card. Look up the corresponding threshold in the Operation System (§21).

**Step 3 — Apply all modifiers.**

Apply all active modifiers:
- Partial payment threshold marker (if attached in Beat 0 or Beat 2)
- Type B Countermeasure token (if placed on this card in Beat 2)
- Modifier Cards in cascade
- Ring Modifier Card calculation (see Artifact 07 — ARBITER Toolkit)
- Public Standing modifier
- Active Situation Report effects
- Protect modifier token (placed by ARBITER in Beat 2)
- Ring adjacency penalty (The Mid: no adjacent Core presence; Core: no Chorus Node presence)

**Step 4 — Calculate and declare threshold.**

The ARBITER Player totals the base threshold plus all active modifier adjustments and announces the final target threshold aloud.

*All parties know the threshold before the roll is made.*

**Step 5 — Roll d100.**

The ARBITER Player rolls d100, or nominates a Faction Player to roll and call the result aloud.

**Step 6 — Determine outcome.**

1. Compare roll to the declared threshold.
2. Apply Critical Success/Fail rules.

**Step 7 — Apply outcome.**

If this operation's outcome blocks the acting faction's deployment marker conversion: The ARBITER Player flips the relevant marker to the Blocked face.

**Step 7a — Succeeded.**

The ARBITER Player directs all board changes. The acting Faction Player physically applies them: presence chips, structure blocks, Control flags, Established markers, Tension markers.

If the card's success outcome specifies an Intel Delivery Slip: ARBITER writes the specified intelligence onto a blank Intel Delivery Slip from their tableau and places it in the indicated faction's dispatch case.

If the card's success outcome specifies a Notification Slip delivered to another faction: ARBITER places the pre-written Notification Slip in that faction's dispatch case.

*Successful covert operations do not produce Standing marker moves — the action is unobserved. Any Standing marker move in this section occurs only as a card-specified failure (Step 7b) or discovery (Step 7b.i) condition.*

**Step 7b — Failed.**

Apply the failure conditions specified on the operation card. If the card specifies an announcement, ARBITER makes it. If the card specifies a Standing marker move, apply it.

If the card's failure outcome specifies a Notification Slip delivered to another faction: ARBITER places the pre-written Notification Slip in that faction's dispatch case.

The affected Faction Player applies their own board changes.

**Step 7b.i — Discovered.**

Apply the discovery conditions specified on the operation card. If the card specifies an announcement, ARBITER makes it. If the card specifies a Standing marker move, apply it.

The affected Faction Player applies their own board changes.

**Step 8 — Clean up the grid cell.**

1. Place the operation card and target slip back in the acting faction's dispatch case.
2. Place the appropriate Operation Resolution card in the dispatch case: Succeeded / Failed / Blocked / Discovered.
3. Discard modifier cards from the grid cell — removed from the game.
4. Return modifier tokens to the pool.

*Modifier token pool location: TBD — Artifact 07.*

**Step 9 — Update Chorus Portrait track.**

The ARBITER Player privately updates the acting faction's Portrait marker on the hidden track.

**Step 10 — Note for Chronicle (optional).**

The ARBITER Player may write a brief note if this operation produced a moment worth preserving.

*At ARBITER's discretion. Detail in Artifact 07 — ARBITER Toolkit.*

**Step 11 — Repeat for all remaining operations.**

*Note — A card is only a valid target while it occupies a slot in the Resolution Grid. Once an operation resolves and its card is returned to the dispatch case, it is no longer a valid target for any action.*

**Clear the Resolution Grid.**

When all operations have resolved, the ARBITER Player clears the Resolution Grid. The grid is rebuilt fresh for Month 2.

**Step 12 — Dispatch Case Return.**

After all operations have resolved and the Resolution Grid is cleared:

The ARBITER Player returns all dispatch cases to their owners. Each case contains at return:
- Submitted covert operation cards
- Target slips
- Operation Resolution cards (one per operation)
- Any Intel Tokens created for this Faction Player this Quarter

*Not returned: resources (spent), Modifier cards (discarded during resolution), Countermeasure cards (removed from the game when played).*

Faction Players read their Operation Resolution cards privately.

---

**Deployment Marker Blocking**

A deployment marker is flipped to the Blocked face when a blocking condition resolves. The flip occurs in the beat in which the condition arises.

| Beat | Month | Condition | Who Flips |
|------|-------|-----------|-----------|
| Beat 1 | Any month | Board state effect blocks conversion in that district or ring | The ARBITER Player |
| Beat 2 | Any month | Type A Countermeasure card names that district | The ARBITER Player |
| Beat 3 | Any month | Covert operation outcome blocks conversion | The ARBITER Player |
| Beat 4 | Any month | Public act outcome blocks conversion | The acting Faction Player |

---

**Beat 4: Public Acts Resolve**

*Public acts are declared in Phase B and resolve with full transparency. They have been on the board — valid targets — since declaration.*

*Beat 4 fires every month. The procedure below applies to Month 1, Month 2, and Month 3 equally.*

**Step 1 — Submit Payment.**

In initiative order, for each Faction Player with a declared public act on the Overview (that has not been voided):

1. The Faction Player transfers resource tokens from the declared card stack to the Reservoir.
2. Remove the Dispatch Token — return to the faction.
3. The ARBITER Player verifies payment against the cost printed on the card:
   - **Full payment:** ARBITER acknowledges.
   - **Partial payment:** The ARBITER Player attaches a −50 threshold marker to the card. ARBITER announces the adjusted threshold.
   - **Zero payment:** ARBITER announces the act is invalid. The Faction Player flips their public act card face-down.

**Intel Token Freshness**

If any Intel Token is submitted as part of payment, for each token calculate age: current Quarter − Quarter generated (written on token).

1. Age 0–2: fresh — no modifier applied.
2. Age 3: stale — attach a −25 Intel freshness modifier to the stack (M-13).
3. Age 4 or more: expired — counts as partial payment.

Reset (erase) and return all submitted Intel Tokens to The Dossier, or discard if single-use.

*Face-down cards auto-fail when their turn is reached in initiative order: modifier cards are discarded and the public act card is returned to the faction.*

**Step 2 — Identify the public act. Check for Apex.**

1. Check for Apex. If Apex: resolution is immediately interrupted — see Apex Activation in §22 before proceeding.
2. If face-down: auto-fail. Discard all modifier cards. Return the public act card to the faction. Advance to the next Faction Player. No further steps apply.
3. Read the public act card and target slip.

**Step 3 — Validate board state conditions.**

Check that the current board state still satisfies the declared public act's play conditions. Play conditions are those required at the point of declaration (Phase B) that may have been altered by covert operations resolving in Beat 3.

- If conditions are met: proceed to Step 4.
- If conditions are no longer met: The ARBITER Player announces the invalidation. The Faction Player flips the public act card face-down. Discard all modifier cards. Return the public act card to the faction. Advance to the next Faction Player. No further steps apply.

**Step 4 — Determine base difficulty.**

The acting Faction Player reads the base difficulty and target threshold aloud from the public act card.

**Step 5 — Apply all modifiers.**

The acting Faction Player applies all active modifiers:
- Partial payment threshold marker (if placed by ARBITER at Submit Payment)
- Modifier Cards in cascade
- Ring Modifier Card calculation (see Artifact 07 — ARBITER Toolkit)
- Public Standing modifier
- Active board state effects (Situation Report + standing public acts)
- Ring adjacency penalty (The Mid: no adjacent Core presence; Core: no Chorus Node presence)

**Step 6 — Calculate and declare threshold.**

The acting Faction Player totals the base threshold plus all active modifier adjustments and states the final target threshold aloud.

**Step 7 — Roll d100.**

The acting Faction Player rolls publicly and states the result aloud.

**Step 8 — Determine outcome.**

1. Compare roll to the declared threshold.
2. Apply Critical Success/Fail rules.

**Step 9 — Apply outcome.**

If this public act's outcome blocks a deployment marker's conversion: The acting Faction Player flips the relevant marker to the Blocked face.

**Step 9a — Succeeded.**

The acting Faction Player makes all board changes — presence chips, structure blocks, Control flags, Established markers, Tension markers. If the card specifies a Standing marker move, apply it.

**Step 9b — Failed.**

Apply the failure conditions specified on the card. If the card specifies an announcement, ARBITER makes it. If the card specifies a Standing marker move, apply it. The affected Faction Player applies their own board changes.

**Step 10 — Clean up.**

1. Modifier cards placed alongside the public act are discarded — removed from the game.
2. The public act card remains on the Overview per its duration type (§23). Immediate cards only: remove from the board and discard or remove from game per card text.

*No pool modifier tokens are used in Beat 4. Modifier cards placed alongside a public act in Phase B serve as their own tracking mechanism — the card itself carries the modifier value through resolution. Pool tokens (placed by ARBITER in Beat 2) apply to covert operations in the Resolution Grid only.*

**Step 11 — Update Chorus Portrait track.**

The ARBITER Player privately updates the acting faction's Portrait marker.

**Step 12 — Note for Chronicle (optional).**

The ARBITER Player may note a significant moment at their discretion.

**Step 13 — Repeat for all remaining public acts.**

---

**Beat 5: Cleanup**

1. Remove all Transient cards from the board — public acts, modifier cards, or any board state card with Transient duration. Cards are discarded or removed from game per card text (§23 Duration Taxonomy).
2. No other board changes.

*Month 3 Beat 3 Step 12 handles dispatch case return before Beat 4. After Beat 5, proceed to Contested District Resolution (§17), then Debrief (§19).*

---

## 12. Month 2 — Dispatch

Follows the same procedure as Month 1 — Dispatch (§9), with these differences:

- ARBITER announces: *"Month 2 Dispatch is open."*
- Faction Players use their **remaining** Dispatch Tokens across Phase A (covert) and Phase B (public acts).
- A faction that spent all tokens in Month 1 may not submit covert operations or declare public acts in Month 2.

*GATHER→SYNTHESIZE combo: submitting GATHER in Month 1 and SYNTHESIZE in Month 2 is a valid Ghost strategy — both consume a Dispatch Token. Card design details: Art 04.*

---

## 13. Month 2 — Countermeasures

Follows the same procedure as Month 1 — Countermeasures (§10), with these differences:

- ARBITER announces: *"Countermeasures may be deployed for Month 2."*
- Cards spent in Month 1 are unavailable. Remaining session supply applies.

---

## 14. Month 2 — Resolution

Follows the same procedure as Month 1 — Resolution (§11), with these differences:

- ARBITER announces each beat with "Month 2" prefix: *"Month 2. Beat 0."*
- Beats are labeled Month2.Week1–4 (Beats 0–5) for design reference.
- Dispatch Tokens from Phase A cases are collected at Beat 0.

---

## 15. Month 3 — Dispatch

Follows the same procedure as Month 1 — Dispatch (§9), with these differences:

- ARBITER announces: *"Month 3 Dispatch is open."*
- Faction Players use any remaining Dispatch Tokens across Phase A (covert) and Phase B (public acts).
- A faction that has spent all tokens in Months 1 and 2 may not submit covert operations or declare public acts in Month 3.

---

## 16. Month 3 — Countermeasures

Follows the same procedure as Month 1 — Countermeasures (§10), with these differences:

- ARBITER announces: *"Month 3 Countermeasure Window is open."*
- Cards used in Months 1 and 2 are already spent. Any remaining supply applies here.

---

## 17. Contested District Resolution

*Runs after Beat 5, before Debrief. Contested districts do not carry forward across Quarters.*

The ARBITER Player scans The Overview for Tension markers. If none are present, proceed to Debrief.

For each district showing a Tension marker, resolving from Ring 3 (Baryo) inward to Ring 0 (Chorus Node):

**Step 1 — Announce the district.**

ARBITER announces: *"[District Name] — Battlefield Strength."*

**Step 2 — Identify contesting factions.**

All factions at Dominant influence in the contested district are contesting factions. More than two factions may contest a single district.

**Step 3 — Calculate and declare totals (simultaneously).**

Each contesting Faction Player:
1. Counts all presence chips and structure blocks in the contested district and in each adjacent district. Deployment markers count as 1 presence chip.
2. Plays any Battlefield Modifier Cards face-up. Each card's +n bonus is added to the total.
3. Plays any fresh Intel Tokens (age 0–2) targeting the opposing faction face-up. Each token adds +2 to the total.
4. Announces their full total (presence count + all Modifier Card and Intel Token bonuses) aloud.

Battlefield Modifier Cards are discarded immediately — they may not be replayed within this contest or used in any subsequent district contest this Session.

Intel Tokens played are reset and returned to The Dossier, or discarded if single-use — same restriction applies.

*Adjacency map: Art 01 §[City] — District Adjacency.*
*(Battlefield Modifier Card design: Art 04 — Action Card System.)*
*(Intel Token Battlefield modifier: +2 per fresh token — L163.)*

**Step 4 — Roll (simultaneously).**

Each contesting Faction Player rolls a d10 and adds it to their declared total. Announces the final result aloud.

**Step 5 — Resolve outcome.**

Highest total wins. ARBITER announces: *"[Faction] holds [District Name]."* The winning Faction Player removes 1 presence chip belonging to a contesting faction of their choice from the contested district, then removes the Tension marker. Both are handed to the ARBITER Player for return to their respective pools.

ARBITER announces: *"[Faction] — will you press?"*

**Press the Battle (optional):** The losing Faction Player may press as long as they hold chips in adjacent districts. To press:
1. Remove 1 presence chip from an adjacent district of their choice and hand it to the ARBITER Player for return to the pool.
2. Return to Step 3 — both factions recalculate and re-declare totals with updated chip counts. Unspent Battlefield Modifier Cards from hand may be played.
3. Re-roll (Step 4).

**On a tie:** Each tied Faction Player removes 1 presence chip — from the contested district or an adjacent district of their choice (a faction with no chips in adjacent districts must remove from the contested district) — and hands it to the ARBITER Player for return to the pool.

After chip removal, check the Dominant condition:
- If one faction remains at Dominant and the other has dropped to Established or below: the contest is settled in that faction's favor.
- If both factions have dropped to Established or below: no Dominant presence remains.

The battle does not continue. Remove the Tension marker. Proceed to Step 6.

**Step 6 — Update board.**

All contesting Faction Players update Control flags, Established markers, and Tension markers as influence levels shift — in the contested district and in any adjacent districts from which chips were removed during the conflict.

When all contested districts are resolved, the ARBITER Player scans The Overview and confirms no Tension markers remain. Proceed to Debrief.

---

## 18. Month 3 — Quarter Notes

Follows §11 Month 1 — Resolution procedure with ARBITER "Month 3" prefix. At end of Beat 3, execute Step 12 (Dispatch Case Return) before clearing the grid.

After Beat 5 completes, the ARBITER Player compiles Quarter-level notes — patterns across multiple actions, observations about the Quarter as a whole — in preparation for §19 Debrief.

*No mechanical updates occur during this period.*

---

## 19. Debrief

ARBITER announces: *"The Table is in Debrief."*

Debrief is open.

*No initiative order, no phase timer.*

**Free actions during Debrief:**

- Trade resources between any two factions (free, any terms)
- Trade Intel Tokens between any two factions (free, any terms, examination permitted)
- Accept or decline an Accord proposal (free action for the receiver)
- Counter-propose Accord terms

**ARBITER conversion:**

Available during Debrief and between phases. Not available during active Resolution beats (Beats 0–5) or while the ARBITER Player is processing board changes. Faction Players requesting conversion during resolution are acknowledged and served after the current beat completes.

*Conversion is the lowest priority item on the ARBITER Player's task list.*

Announced by ARBITER in Quarter 1 only: *"Resource conversion is available whenever I am not actively resolving actions. The applicable rate is determined by your presence at the Chorus Node."* Rate table: Artifact 02a §8 (D02a-01).

**Chorus Question window:**

If the Chorus Activity track has reached the Question threshold, any faction with at least Present influence at the Chorus Node may propose a question during Debrief — provided the Chorus Node is not Contested. If the Chorus Node is Contested, the window does not open this Quarter. Simple majority passes it. ARBITER answers in The Observation register. Full rules in Artifact 07 — ARBITER Toolkit.

**Debrief Actions:**

After the Chorus Question window resolves (or immediately at Debrief open if no Chorus window triggers), any faction holding a Debrief Action card in hand resolves it now. In initiative order:

1. The holding Faction Player announces the card name.
2. The Faction Player executes the card's Debrief instruction.
3. ARBITER confirms the effect.
4. The Debrief Action card is removed from the game or returned to the ARBITER pool — physical form TBD.

*If no faction holds a Debrief Action card, this step is skipped.*

---

**Debrief structure:**

ARBITER addresses The Table in three components, in order:
1. **Summary** — factual account of Quarter resolution outcomes. The Record register.
2. **Observation** — one or two pattern observations ARBITER has noted from the Quarter. The Observation register.
3. **Distribution** — ARBITER distributes Quarter-end rewards (see §20).

**ARBITER's Debrief observation:**

ARBITER delivers one observation in The Observation register — never combining both forms:
- *Form A:* *"A faction at this table has moved into [PORTRAIT STATE]. [STATE LANGUAGE]."*
- *Form B:* *"[FACTION]'s contribution to the Portrait this Quarter was [vague adjective]."*

If Chorus Activity changed this Quarter, ARBITER incorporates this into the Debrief narrative as the track moves on the board. Scripted dialogue for each Chorus Activity level is in Artifact 07 — ARBITER Toolkit.

**Ready to close:**

1. When done with Debrief, a Faction Player flips their Status marker to the Ready side (green).
2. When 3 of 5 Faction Players show green: ARBITER starts a 60-second courtesy timer: *"The majority is ready. Sixty seconds."*
3. When the timer expires or all 5 Faction Players show green — whichever comes first — Debrief closes.

*ARBITER observes who signals ready early, who holds out, and when. The Chorus notes this.*

---

## 20. End of Quarter

At the close of Debrief, in strict order:

1. **Seasonal card cleanup:** Remove all Seasonal public acts, modifier cards, and any other board state cards with Seasonal duration from the board and the Overview. Cards are discarded or removed from game per card text (§23 Duration Taxonomy). ARBITER's Situation Report Broadcast Card is removed here if its duration is Seasonal.

2. **Findings decay:** The Ghost Faction Player checks current Findings total and applies decay publicly (7–12: lose 2; 13+: lose 4). Returns the Findings tokens to the Reservoir.

3. **Debrief reward:** ARBITER assesses the Quarter and distributes rewards before the Session Timeline advances. Reward candidates *(TBD — design pending)*:
   - Intelligence Token distributed to the faction with the highest net information gain this Quarter
   - Bonus resource distributed for Accord compliance (ARBITER discretion)
   - Situation Report (world event card) revealed — sets the world event for the following Quarter

   *[TBD — are Debrief rewards fixed (every Quarter, same structure) or variable (ARBITER discretion)?]*

4. **Operation Resolution cards collected:** Faction Players return their Operation Resolution cards to the ARBITER Player.

   *These are reusable components, reset for the next Quarter.*

5. **Session Timeline advances:** The ARBITER Player moves the Session Timeline forward by 1.

   *This is the final action of the Quarter — the moment it is officially closed.*

If the Session Timeline reaches 8 and no Apex has resolved, proceed to Session End per Artifact 10a — Victory System.

---

## Reference Material

## 21. The Operation System

The Operation System governs resolution for all committed actions: covert operations (Beat 3) and public acts (Beat 4).

*Every committed action resolves with a roll. Submitting an operation or declaring a public act is a commitment — ARBITER renders a judgment on all of them.*

---

### The d100 Roll

A d100 is produced by two ten-sided dice (d10) in two distinct colors. One color is designated as the tens digit; the other as the units digit. Together they produce a result from 01 to 100. Both dice showing 0 = 100.

Establish which color is tens at session start. Keep consistent throughout the session.

The game includes two d10 dice. If d10 dice are unavailable, any device capable of generating a random integer from 1 to 100 produces an identical result.

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

*If modifiers reduce the threshold to 0 or below, the roll still occurs — only a Critical Success (01–05) succeeds. If modifiers raise the threshold to 100 or above, the roll still occurs — only a Critical Fail (96–00) fails. The 5% critical floor means no committed action is truly hopeless; the 5% critical ceiling means no action is guaranteed. Critical Success and Critical Fail carry additional action-specific consequences noted on individual operation cards (Artifact 09).*

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

## 22. Special Conditions & Gameplay Impacts

### Apex Activation

An Apex operation may be submitted as a covert operation (resolved in Beat 3) or as a public act (resolved in Beat 4).

**Step 1 — Identify the Apex.**

When an Apex card is encountered, the current procedure immediately suspends and subroutines to Apex resolution (Steps 2–5). If the Apex is cancelled at Step 4, the procedure resumes from the exact point it was suspended.

- In Beat 3 (covert): suspension occurs when the Apex card is reached in the resolution queue. On return from a failed Apex: continue from the next operation in queue.
- In Beat 4 (public): suspension occurs when the Apex public act is reached in initiative order. The card has been face-up on the Overview since Phase B. On return from a failed Apex: continue from the next Faction Player in initiative order.

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

## 23. Duration Taxonomy

All public acts, modifier cards, and board state cards carry one of four duration types. Duration is printed on the card. Cleared behavior (return to discard pile vs. remove from game) is specified per card text.

| Type | Duration | Cleared |
|------|----------|---------|
| Immediate | Placed on the board; resolves immediately upon placement. Must move from hand to board to trigger. Cannot be returned to hand, discarded, or removed from game until placed on the board. | Per card text after resolution — removed from board (discard or remove from game) |
| Transient | Active for this month only | Beat 5 cleanup of the month in which it was played |
| Seasonal | Active for this Quarter | End of Quarter §20 Seasonal card cleanup |
| Permanent | Active until a named action or condition removes it — including a self-clearing trigger on the card | Per card text (discard or remove from game) |

*ARBITER's Situation Reports carry Seasonal duration by default. Card text may specify otherwise.*

*Modifier react cards may carry any duration type — a react that creates a persistent board state remains on the board with its stated duration.*

---

## 24. Public Act Placement Rules

1. Public acts are declared during Phase B (Monthly Dispatch), in initiative order.
2. The declaring Faction Player places the card face-up on the Overview in the target district (or in the relevant zone for non-district acts).
3. Attach the target slip and 1 Dispatch Token on top of the card. Resource tokens remain with the card — payment is submitted to the Reservoir at Beat 4.
4. Modifier cards modifying the public act are placed face-up alongside the card on the Overview.
5. Once placed, the card is a valid target for Countermeasure cards (Countermeasure Window, §10) and other public acts.
6. Public acts cannot be withdrawn or modified after placement.
7. ARBITER's Situation Reports are placed in the Event Zone during Upkeep (Step 3) and follow the same duration and targeting rules as faction public acts.
8. A public act card remains on the board until its duration expires. Beat 4 resolution does not necessarily remove the card — duration governs removal.
   - Transient cards are removed at Beat 5 of the month in which they were played.
   - Seasonal cards remain on the board until End of Quarter.
   - Permanent cards remain until a named action or condition removes them.

---

## 25. Modifier React Card Rules

Modifier react cards follow the general React Card procedure (§28). The following rule applies specifically to modifier react cards:

1. If a modifier react card creates a persistent board state (a card placed on the board), the card remains with its duration type per §23.

---

## 26. Countermeasure Card Rules

1. Each faction receives 3 Countermeasure cards at game start. They are issued, not drawn.
2. Countermeasure cards are removed from the game when used — they do not return to hand or discard pile.
3. Countermeasure cards are submitted during the Countermeasure Window each month (§10/§13/§16).
4. A Countermeasure card may target either:
   - A queued covert operation in a submitted dispatch case (processed at Beat 2), or
   - A placed public act currently on the Overview (processed at Beat 2).
5. Unused Countermeasure cards carry forward to the next Monthly window. A faction may hold all 3 through Month 3 or spend them early.
6. Full Countermeasure card types and effects: Artifact 04 — Action Card System.

---

## 27. Examples & Exceptions

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

*End of Beat 5. The ARBITER Player returns Ghost's dispatch case.*

Ghost finds:
- Three covert operation cards
- Operation Succeeded card (Gather at Data Exchange)
- Voided card (Undermine at Financial Clearinghouse — targeting restriction)
- Voided card (Build Structure at Government Citadel — Type A Countermeasure)
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

---

## 28. React Card Rules

React cards fire in response to publicly visible board state changes. They are held in hand until their trigger condition is met.

1. A React card may only fire on a publicly visible board state change (Governing Rule 7.2a). It cannot fire on ARBITER-internal state changes such as the Resolution Grid.
2. When a trigger condition is met: the holding Faction Player announces *"React"*, presents the card, and states the trigger condition listed on the card. ARBITER confirms the trigger is valid and pauses the quarter procedure.

    2a. First to announce pauses play. ARBITER decides tiebreakers. Only one React resolves at a time — a second React may only fire in response to the new board state produced after the first resolves.

    2b. A React must be announced at the moment the triggering board state change occurs. It cannot be declared retroactively — once the procedure moves past the trigger point, the window closes.

3. The React card resolves per its stated effect.
4. Once the React has resolved, the original procedure resumes from the point it paused.
