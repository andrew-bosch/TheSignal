# 03 — Round Structure & Gameplay
## THE SIGNAL P1 — Paper Prototype

**Version:** 1.5  

**Status:** 🔄 Updated — Pending Re-Sign-Off (Beat 2 rename, Step 6 rewrite)  

**Depends on:** 00 — Factions, World & Narrative Context; 01 — Game Board: New Meridian; 02a — Resource Systems: Board State; 02b — Resource Systems: Tracking  

**Supersedes:** round_structure (retired artifact)

---

## 1. Overview

### Problem This Document Solves
Without a precise, ordered description of how each round is structured — what happens, in what sequence, who does it, and what information is available when — no artifact describing specific actions, resolutions, or ARBITER behavior can be written consistently. This document is the skeleton that all subsequent system artifacts attach to.

### Deliverable
The complete structure of a single round of THE SIGNAL: six phases in sequence, the events within each phase in order, who performs each step, and the rules governing timing, priority, and transitions between phases.

### Success Criteria
- ARBITER can follow the sequence of a complete round from this document — knowing what happens in what order and who does it, with references to where specific mechanical details live in subsequent artifacts
- Players know at any point in the round what phase they are in, what is expected of them, and what comes next
- The document contains no undefined terms from prior artifacts (00–02b)
- The round sequence is complete — no phase or transition is missing or ambiguous

---

## 2. Index

1. Overview
2. Index
3. Game Purpose
4. Narrative Function
5. Design Principles
6. Round Overview
7. Phase 1 — Upkeep
8. Phase 2 — Placement
9. Phase 3 — Dispatch
10. Phase 4 — Declaration
11. Phase 5 — Countermeasures
12. Phase 6 — Resolution + Debrief
13. End of Round
14. Special Conditions & Gameplay Impacts
15. Examples & Exceptions

---

## 3. Game Purpose

The round structure is the engine of the session. It defines the rhythm of play — when information is revealed, when commitments are made, when consequences land. Every player decision happens within a specific phase with specific constraints on what they know and what they can do. The sequence is designed so that the most consequential decisions are made after the board state is known but before outcomes are resolved.

Eight rounds constitute a session. The session ends either at the completion of Round 8 or when an Apex ability resolves — whichever comes first.

---

## 4. Narrative Function

Each round represents approximately **one quarter** — three months of real-world time — in New Meridian. Eight rounds constitute roughly two years of operations from The Table's formation to the final vote.

This framing gives the game's events appropriate weight:
- A structure block is not a completed building but an established operational presence — a secured facility, a contracted team, a functioning node. Three months is enough time to establish a foothold; not enough to build a headquarters.
- Influence growth represents sustained organizational investment over a quarter — relationships cultivated, presence consolidated, community engagement maintained.
- A Situation Report represents a significant event at the city or global scale — something meaningful enough to shape a quarter of operations, not a daily news cycle.
- Humanity has been receiving the Chorus for thirty-one years — approximately 124 quarters. The Table's two-year deliberation may be, from the Chorus's perspective, a remarkably compressed response time. Whether the Chorus considers the transmission complete is a question treated fully in Artifact 00. What is relevant to round structure: each quarter carries weight proportional to what it follows. The Table is not working on a human schedule.

The round's internal structure mirrors how organizations operate under pressure: situational awareness first (Upkeep), then positioning (Placement), then committing to action before knowing what others will do (Dispatch and Declaration), then consequences arriving simultaneously (Resolution), then the conversation about what it all meant (Debrief).

ARBITER is present throughout but speaks at specific moments. Between those moments, ARBITER watches.

---

## 5. Design Principles

1. **Information flows in one direction per round.** Players learn the world state at Upkeep, then commit to actions before seeing opponents' choices. Outcomes are revealed simultaneously during Resolution.

2. **Commitment is irreversible.** Once a dispatch case is closed, its contents cannot be changed. Once a political act is declared, it cannot be withdrawn.

3. **The board is always honest.** At every point in the round, the board reflects the true current state. Only dispatch case contents and ARBITER's tableau are private.

4. **Players run their own economy.** Resource collection, marker placement, flag and marker updates, and structure block removal are all performed by players. ARBITER facilitates and resolves disputes.

5. **Speed has consequences.** Dispatch case submission order is the tiebreaker within resolution priority tiers.

---

## 6. Round Overview

```
PHASE 1 — UPKEEP
  Round opens. World updates. Resources collected. Initiative set.

PHASE 2 — PLACEMENT
  Deployment markers placed. Entry requirements enforced.

PHASE 3 — DISPATCH
  Covert operations submitted secretly in dispatch cases.

PHASE 4 — DECLARATION
  Political acts declared publicly in initiative order.

PHASE 5 — COUNTERMEASURES
  Countermeasure cards played openly.

PHASE 6 — RESOLUTION + DEBRIEF
  All actions resolved. Board updated. Table speaks.
```

Phases do not overlap. ARBITER announces the start of each phase.

---

## 7. Phase 1 — Upkeep


- ARBITER announces each step.
- Faction Players perform their own updates.

### Step 1 — Status Marker Reset

Each Faction Player flips their Status marker to the Discussing side (yellow/text).

*This is the physical act that opens the round — a personal acknowledgment that a new quarter of operations has begun and the previous round is fully closed.*

### Step 2 — Initiative

ARBITER determines the round's initiative order.

**Profile Ranking:**

1. The ARBITER Player reads each faction's current Chorus Portrait score from the hidden Portrait track.
2. ARBITER ranks factions 1 (highest) through 5 (lowest).

*Ties broken by Public Standing. Remaining ties by ARBITER discretion.*

**D10 Roll:**

The ARBITER Player rolls 1d10 publicly.

*The D10 decouples the visible initiative order from the hidden Portrait rankings — players cannot reverse-engineer their Portrait standing from their position in the order.*

| Roll | Condition | Order |
|------|-----------|-------|
| 1 | Power order | Rank 1 → 2 → 3 → 4 → 5 |
| 2 | Underdog order | Rank 5 → 4 → 3 → 2 → 1 |
| 3 | Zigzag descending | Rank 1 → 5 → 2 → 4 → 3 |
| 4 | Middle-out down | Rank 3 → 2 → 1 → 4 → 5 |
| 5 | Middle-out up | Rank 3 → 4 → 5 → 2 → 1 |
| 6 | Second leads | Rank 2 → 1 → 5 → 4 → 3 |
| 7 | ARBITER chooses | Clockwise or counterclockwise from ARBITER's position — ARBITER declares which |
| 8 | Reverse last round | Exact reverse of previous round's order |
| 9 | Personal tiebreaker | ARBITER draws a Personal Tiebreaker card; Faction Players sort by that criterion. Detail in Artifact 07 — ARBITER Toolkit. |
| 10 | Table votes | Each Faction Player writes a rank (1–5); most votes wins starting position; proceed descending; ARBITER breaks ties |

*Round 1:* All Portrait and Public Standing scores are equal. Initiative is determined clockwise from The ARBITER Player's left regardless of D10 roll.

ARBITER announces the final order. The ARBITER Player updates the Initiative Strip on the board.

### Step 3 — Situation Report

ARBITER announces: *"Situation Report."*

1. The ARBITER Player draws the top Broadcast Card from the session deck and places it face-up in the Event Zone on The Overview.
2. The ARBITER Player locates the matching Event Card from the Event Card deck and places it on the ARBITER tableau.
3. The ARBITER Player reads the Event Card.
4. As applicable, ARBITER announces Public Standing track changes — reads the indicated narrative on the Event Card aloud.

   *Do not announce difficulty modifiers or hidden mechanical effects.*
5. Each Faction Player moves their Public Standing marker as indicated by ARBITER.
6. If the Event Card specifies a deployment marker cannot convert this round: the ARBITER Player flips the affected marker(s) to the Blocked face.
7. The ARBITER Player reviews all Event Cards on the ARBITER tableau and moves expired cards to the expired area of the ARBITER tableau.

   *No tick-downs or maintenance — duration management occurred at the close of the previous round.*

### Step 4 — Deployment Marker Conversion

ARBITER announces: *"Markers convert."*

1. Each Faction Player checks deployment markers currently on the board.
2. For each marker showing the Converting face: place 1 permanent presence chip in that district and return the marker to hand.
3. For each marker showing the Blocked face: return the marker to hand without placing a chip.
4. Each Faction Player updates Control flags and Tension markers as influence levels shift from new chip placements.

*If no markers are on the board — as is always the case at the start of Round 1 — this step has no effect. Proceed to Step 5.*

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

### Step 6 — Operations Preparation

ARBITER announces: *"Prepare operations."*

*Purpose: ensure all elements needed for Declaration and beyond are assembled and in their correct positions on the tableau. Faction Players complete this step simultaneously before Dispatch opens.*

**Tableau check — standing elements:**

Verify the following elements are already in position before drawing begins:
- Pass cards (4) — beside tableau, always available
- Floor Act — beside tableau, always available to all factions at all times (full design: Artifact 04 D04-13)
- Modifier cards carried from prior rounds — in modifier area
- Operator cards — in their designated area

**Action card draw:**

1. Count covert operation cards currently in hand. Draw from personal draw deck to reach a hand of 6.
2. Count political act cards currently in hand. Draw from personal draw deck to reach a hand of 3.
3. Place all drawn cards in the active hand area of the tableau. Cards are held face-down and private.

*Cards kept from the prior round count toward hand size — a player with 2 kept covert cards draws 4 more to reach 6.*

If a draw deck is exhausted mid-draw, shuffle that deck's discard pile immediately to form a new draw deck and continue.

*Both decks reshuffle independently.*

**Modifier card draw:**

*A faction that has triggered Burst Play this session is exempt from modifier card draws — skip this sub-step.*

Draw and place modifier cards in the tableau modifier area.

**Faction modifier draw:**

Draw from the faction modifier deck in the player's tableau.

| Structure blocks owned | Faction modifier cards drawn |
|------------------------|------------------------------|
| 0–1 | 0 |
| 2–3 | 1 |
| 4–5 | 2 |
| 6+ | 3 (maximum) |

**Ring modifier draw:**

A ring qualifies if the faction meets all of the following conditions:
- At least 1 structure block in that ring
- Established or Dominant presence in at least 1 district in that ring

Draw 1 card for each qualifying ring. A faction may qualify for all three rings.

*Modifier decks (faction and ring) are not reshuffled when exhausted.*

**Burst Play window:**

After completing all draws, before Dispatch opens, a faction may trigger Burst Play. If triggered:

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
| Sprawl | None | None |
| Infrastructure | None | −25 to all operations targeting this district if no adjacent Core district holds Established or Dominant |
| Core | Established or Dominant in an adjacent Infrastructure district (permanent chips or temporary presence from first marker this phase) | None |
| Chorus Node | Established or Dominant in an adjacent Core district (permanent chips or temporary presence from first marker this phase) | See Artifact 02a §10 — standard entry rules do not apply |

3. After each placement, if influence levels change: the placing Faction Player updates the relevant Control flag or Tension marker immediately.

*A Faction Player may pass either or both placements. ARBITER redirects illegal placements.*

---

## 9. Phase 3 — Dispatch

- *Faction Players assemble, seal and transmit their own dispatch cases.* 
- *The ARBITER Player keeps watch on the Dispatch Timer, announces status, and queues cases in the order they are received.*

**1. Open Dispatch**
- ARBITER announces: *"Dispatch is open."*
- The ARBITER Player starts the dispatch timer.

**2. Assemble cases**

 - Faction Players load operations, resources, target slips, and Pass cards into their cases.

  *Assembly should be handled privately and silently.*

*Full dispatch case design, physical format, and component contents: Artifact 06 — Messaging System.*

**3. Seal cases**

 - Faction Players close their cases. 

*No additions or changes permitted after sealing cases.*

**4. Transmit cases**

 - Faction Players place their sealed cases in the ARBITER Player's receive queue. 
 - The ARBITER Player logs each case received, preserving transmission sequence.

*Transmission order is the tiebreaker within priority tiers during Beat 3.*

**5. Close Dispatch (When timer ends)**
- The ARBITER Player announces: *"Timer."*

  *No new additions to any case — sealed or open.*

- The ARBITER Player counts: *"Five. Four. Three. Two. One."*

  *Faction Players who have not transmitted may seal and transmit during the countdown.*

- The ARBITER Player announces: *"Dispatch closed."* 

  *Any case not received is treated as if all actions submitted are Pass. -*

---

## 10. Phase 4 — Declaration


- Faction Players declare in initiative order.
- The ARBITER Player records.

ARBITER announces: *"Declaration is open."*

For each Faction Player in initiative order:

1. Announce the political act being declared.
2. Place the declared card face-up in front of the Faction Player's tableau with the target slip and resource tokens stacked on top.
3. Pay resources directly to the Reservoir.
4. Play any modifier cards modifying the political act face-up alongside.

*A Faction Player passing: place the Pass card face-up on the tableau.*

**Rules:**

- Must target one of the Faction Player's two deployment markers placed this round
- The Operative Card may be used as the political act
- A free Accord card may be declared this round if triggered by C09 Fund resolution — this does not consume a card from the political draw deck; The ARBITER Player delivers the Accord card directly

*Declared political acts cannot be withdrawn or modified after declaration.*

**Ghost's pass:**

Ghost places their Pass card.

*The table knows Ghost passed. They do not know what Ghost submitted.*

---

## 11. Phase 5 — Countermeasures


- Faction Players play their own Countermeasure cards and deliver them to The ARBITER Player.
- The ARBITER Player holds Countermeasures for application during Resolution.

*No initiative constraint.*

ARBITER announces: *"Countermeasures are open."*

For each Countermeasure card played:

1. Play the card face-up in front of the Faction Player's tableau.
2. Declare the card type — Type A or Type B — to The ARBITER Player.
3. Hand the card to The ARBITER Player.

**Card types:**

**Type A — District Block:**

Names a specific district. Blocks all offensive operations (public and private) targeting that district this round.

**Type B — Faction Defense:**

Names the playing faction as defender. All roll targets for any operation targeting anything that faction owns are reduced by 15. Does not block operations — makes them harder to succeed.

**Rules:**

- Countermeasure cards are permanently removed from the game after use
- Each faction has exactly 3 Countermeasure cards for the entire session
- Multiple cards may be played this phase
- *Card count flagged for playtesting validation*

Phase ends when all Faction Players signal done. The ARBITER Player collects all dispatch cases and proceeds to Resolution.

---

## 12. Phase 6 — Resolution + Debrief

Resolution is run by ARBITER. Faction Players receive outcomes, update their own trackers, then participate in Debrief.

### Resolution — Five Beats

ARBITER announces each beat before beginning it.

---

**BEAT 1 — Active Restrictions** *(~30 seconds)*

1. The ARBITER Player checks all currently active Situation Report effects for targeting restrictions or difficulty modifiers.

   *For example, effects that prevent operations in specific districts or rings.*

2. ARBITER announces all active restrictions publicly in The Record register.

   *All restrictions are announced before any operations resolve.*

3. If a Situation Report effect blocks deployment marker conversion in a named district or ring: The ARBITER Player flips the affected marker(s) to the Blocked face.

*No other board changes, track updates, or maintenance occur in this beat.*

---

**BEAT 2 — The Ground Shifts** *(~90 seconds)*

The ARBITER Player processes all condition-setting cards received in the dispatch cases.

*This includes Countermeasure cards, Protect operations, Fortify Structure, Broadcast Interference, Amplify, Open Channel, Sealed Border, Golden Parachute, and any other Beat 2 card submitted this round — cards that modify resolution conditions for subsequent beats before any board state changes occur.*

**For each Type A Countermeasure card (District Block):**

1. The ARBITER Player identifies all operations in dispatch cases targeting the named district.
2. The ARBITER Player places matched operation cards and target slips back into the originating dispatch case with an Operation Blocked resolution card.

   *Resources committed to blocked operations are not refunded — the attempt was made and met resistance.*

3. The ARBITER Player discards all modifier cards attached to blocked operations.

**For each Type B Countermeasure card (Faction Defense):**

The ARBITER Player notes the −15 threshold modifier to be applied to all rolls against that faction's assets in Beat 3.

**For each Protect operation:**

The ARBITER Player notes the target and the defensive modifier to be applied in Beat 3.

**Deployment marker blocking conditions:**

A deployment marker is flipped to the Blocked face when any of the following conditions are met — this happens during the beat in which the condition resolves, not in Beat 2:

1. A Type A Countermeasure card named that district *(Beat 2 — ARBITER flips)*
2. An action or operative ability against the faction that blocks conversion, as defined in Artifact 04 and Artifact 05 *(Beat 3 for covert — The ARBITER Player flips; Beat 4 for public — the acting Faction Player flips)*
3. A World Condition or Situation Report effect blocking conversion in that district or ring *(Beat 1 — ARBITER flips)*

---

**BEAT 3 — Operations Land or Don't** *(~3 minutes)*

ARBITER resolves all covert operations from dispatch cases in submission order.

For each operation:

**Step 1 — Identify the operation. Check for Apex.**

1. Read the operation card and target slip.
2. Check for Apex submission.

   If Apex: resolution is immediately interrupted — see Apex Activation in Section 14 before proceeding.
   If not Apex: continue to Step 2.

**Step 2 — Check Active Restrictions.**

1. Check if the target district has any active Beat 1 restrictions.
2. If restricted: the operation fails.

   Return the operation card and target slip to the dispatch case with an Operation Failed resolution card. Proceed to the next operation.
   If not restricted: continue to Step 3.

**Step 3 — Determine base difficulty.**

Read the base difficulty printed on the operation card. Look up the corresponding threshold in the 2d10 System table below.

**Step 4 — Apply faction-wide Countermeasure modifier.**

1. Check if a Type B Countermeasure is active against the target faction.
2. If active: reduce the roll threshold by 15.

**Step 5 — Apply all other modifiers.**

Apply Public Standing modifier, Modifier card modifiers, active world effect modifiers, and Protect/defend modifiers.

**Step 6 — Roll 2d10.**

The ARBITER Player rolls 2d10, or nominates a Faction Player to roll and call the result aloud.

**Step 7 — Determine outcome.**

1. Compare roll to modified target threshold.
2. Apply Critical Success/Fail rules.

**Step 8 — Flip deployment marker if applicable.**

If this covert operation's outcome blocks the acting faction's deployment marker conversion in the target district, The ARBITER Player flips the relevant marker to the Blocked face.

**Step 9 — Board changes for successes.**

If the operation succeeded:

1. The ARBITER Player makes board changes: presence chips, structure blocks, Control flags, Tension markers.
2. The acting Faction Player performs physical updates for changes resulting from their own action.

**Step 10 — Announce failures and discoveries.**

- If failed: ARBITER announces publicly without naming the faction: *"An operation in [DISTRICT] did not succeed."*
- If Discovery: ARBITER announces: *"An operation in [DISTRICT] was observed."*

The affected Faction Player moves their own Public Standing marker.

**Step 11 — Place resolution card in dispatch case.**

The ARBITER Player places the appropriate Operation Resolution card in the acting faction's dispatch case: Succeeded / Failed / Blocked / Discovered.

**Step 12 — Update Chorus Portrait track.**

The ARBITER Player privately updates the acting faction's Portrait marker on the hidden track.

**Step 13 — Note for Chronicle (optional).**

The ARBITER Player may write a brief note if this operation produced a moment worth preserving.

*At ARBITER's discretion. Detail in Artifact 07 — ARBITER Toolkit.*

**Step 14 — Repeat for all remaining operations.**

---

### The 2d10 System

**Reading the dice:**

*Two ten-sided dice in two distinct colors. One color = tens digit; other = units digit. Together they produce 01–100 (both showing 0 = 100).*

Establish which color is tens at session start. Keep consistent.

**The threshold is a percentage:**

To succeed, the roll must land equal to or below the target threshold.

*The threshold is the percentage chance of success — a threshold of 75 means 75% chance of success.*

**Base Difficulty Threshold:**

| Difficulty (printed on card) | Threshold |
|------------------------------|-------------|
| Automatic | No roll — succeeds |
| Easy | 01–75 |
| Average | 01–50 |
| Challenging | 01–25 |
| Impossible | No roll — fails |

*Difficulty is a property of the operation card. All other conditions — Public Standing, Modifier cards, active world effects — apply as adjustments to the target threshold.*

**Critical Results:**

| Roll | Result | Condition |
|------|--------|-----------|
| 01–05 | Critical Success | Always — regardless of modifiers |
| 96–00 | Critical Fail | Always — regardless of modifiers |

*If modifiers reduce the threshold to 0 or below, the roll still occurs — only a Critical Success (01–05) succeeds. If modifiers raise the threshold to 100 or above, the roll still occurs — only a Critical Fail (96–00) fails. Critical Success and Critical Fail carry additional action-specific consequences noted on individual operation cards (Artifact 09).*

**Difficulty Modifiers:**

| Modifier | Target Threshold Adjustment |
|----------|-----------------------------|
| Public Standing: Celebrated | +20 |
| Public Standing: Respected | +10 |
| Public Standing: Neutral | 0 |
| Public Standing: Suspect | −10 |
| Public Standing: Discredited | −20 |
| Modifier card | As specified on card |
| Active Situation Report effect | As specified on Event Card |
| Protect / Defend operation active | As specified on operation card |
| Type B Countermeasure (attacker) | −15 |
| Infrastructure district — no adjacent Core at Established or Dominant | −25 |

*All active modifiers are cumulative.* Apply all before rolling.

---

**BEAT 4 — Political Acts Resolve** *(~90 seconds)*

Political acts resolve publicly. The acting Faction Player performs all steps.

For each political act in initiative order:

**Step 1 — Identify the political act. Check for Apex.**

1. The acting Faction Player reads their declared card and confirms their target.
2. Check for Apex.

   If Apex: resolution is immediately interrupted — see Apex Activation in Section 14 before proceeding.
   If not Apex: continue to Step 2.

**Step 2 — Determine base difficulty.**

The acting Faction Player reads the base difficulty from the political act card and looks up the corresponding threshold in the 2d10 System table (§12.2).

**Step 3 — Apply all modifiers.**

The acting Faction Player applies all relevant modifiers and announces the modified target threshold aloud.

**Step 4 — Roll 2d10.**

The acting Faction Player rolls publicly and states the result aloud.

**Step 5 — Determine outcome.**

The acting Faction Player compares roll to modified threshold. Critical Success and Critical Fail rules apply.

**Step 6 — Flip deployment marker if applicable.**

If this political act's outcome blocks a deployment marker's conversion, the acting Faction Player flips the relevant marker to the Blocked face.

**Step 7 — Board changes.**

The acting Faction Player makes all board changes: presence chips, structure blocks, Control flags, Tension markers.

**Step 8 — Public Standing update.**

The acting Faction Player moves their own Public Standing marker. Other affected Faction Players move their own markers.

**Step 9 — Update Chorus Portrait track.**

The ARBITER Player privately updates the acting faction's Portrait marker.

**Step 10 — Note for Chronicle (optional).**

The ARBITER Player may note a significant moment at their discretion.

**Step 11 — Repeat for all remaining political acts.**

---

**BEAT 5 — The Table Speaks**

*Everything in the session leads to this beat. Resolution is complete. The board reflects what happened. Now the table processes, reacts, and responds — privately first, then openly.*

**Dispatch Case Return:**

Before Debrief opens, The ARBITER Player returns all dispatch cases to their owners. Each case contains at return:
- Submitted covert operation cards
- Target slips
- Operation Resolution cards (one per operation)
- Any intel notes created for this Faction Player this round

*Not returned: resources (spent), Modifier cards (discarded during resolution).*

Faction Players read their Operation Resolution cards privately.

*This is the moment each faction learns what happened to their covert operations — before the table conversation begins.*

**ARBITER's Round Notes:**

While Faction Players review their dispatch cases, The ARBITER Player makes any final round-level notes — patterns across multiple actions, observations about the round as a whole — that will inform the Debrief observation or Chronicle.

*No mechanical updates occur here.*

---

### Debrief

ARBITER announces: *"The Table is in Debrief."*

Debrief is open.

*No initiative order, no phase timer.*

**Free actions during Debrief:**

- Trade resources between any two factions (free, any terms)
- Trade intel notes between any two factions (free, any terms, examination permitted)
- Accept or decline an Accord proposal (free action for the receiver)
- Counter-propose Accord terms

**ARBITER conversion:**

Available during Debrief and between phases. Not available during Resolution Beats 1–4 or while The ARBITER Player is processing board changes.

*Conversion is the lowest priority item on The ARBITER Player's task list.*

Announced by ARBITER in Round 1 only: *"Resource conversion is available whenever I am not actively resolving actions. The applicable rate is determined by your presence at the Chorus Node."* Rate table: Artifact 02a §8 (D02a-01).

**Chorus Question window:**

If the Chorus Activity track has reached the Question threshold, any faction with at least Present influence at the Chorus Node may propose a question during Debrief — provided the Chorus Node is not Contested. If the Chorus Node is Contested, the window does not open this quarter. Simple majority passes it. ARBITER answers in The Observation register. Full rules in Artifact 07 — ARBITER Toolkit.

**ARBITER's Debrief observation:**

ARBITER delivers one observation in The Observation register — never combining both forms:
- *Form A:* *"A faction at this table has moved into [PORTRAIT STATE]. [STATE LANGUAGE]."*
- *Form B:* *"[FACTION]'s contribution to the Portrait this round was [vague adjective]."*

If Chorus Activity changed this round, ARBITER incorporates this into the Debrief narrative as the track moves on the board. Scripted dialogue for each Chorus Activity level is in Artifact 07 — ARBITER Toolkit.

**Ready to close:**

1. When done with Debrief, a Faction Player flips their Status marker to the Ready side (green).
2. When 3 of 5 Faction Players show green: ARBITER starts a 60-second courtesy timer: *"The majority is ready. Sixty seconds."*
3. When the timer expires or all 5 Faction Players show green — whichever comes first — Debrief closes.

*ARBITER observes who signals ready early, who holds out, and when. The Chorus notes this.*

---

## 13. End of Round

At the close of Debrief, in strict order:

1. **Findings decay:** The Ghost Faction Player checks current Findings total and applies decay publicly (7–12: lose 2; 13+: lose 4). Returns chips to the Reservoir.

2. **Debrief reward:** ARBITER assesses the quality of the Debrief conversation — now that all Status markers show green, the conversation is complete — and selects a Tier A/B/C reward effect to apply before the Round Tracker advances. See Artifact 07 — ARBITER Toolkit for full reward options and effects.

3. **Operation Resolution cards collected:** Faction Players return their Operation Resolution cards to The ARBITER Player.

   *These are reusable components, reset for the next round.*

4. **Round Tracker advances:** The ARBITER Player moves the Round Tracker forward by 1.

   *This is the final action of the round — the moment it is officially closed.*

If the Round Tracker reaches 8 and no Apex has resolved, proceed to Session End per Artifact 10a — Victory System.

---

## 14. Special Conditions & Gameplay Impacts

### Apex Activation

An Apex operation may be submitted as a covert operation (resolved in Beat 3) or as a political act (resolved in Beat 4).

*In either case, identifying it is the first check when that operation or act is processed.*

**Step 1 — ARBITER or acting Faction Player identifies the Apex.**

- In Beat 3: The ARBITER Player identifies the Apex operation card when opening the dispatch case.
- In Beat 4: The acting Faction Player reveals their Apex political act card.

Either way, resolution is immediately interrupted.

ARBITER announces: *"An Apex operation has been submitted. Resolution is suspended."*

**Step 2 — ARBITER confirms resources paid.**

The ARBITER Player counts the resources in the dispatch case (covert) or paid to the Reservoir (public). All five resource types must be present in the required amounts (Artifact 05).

If insufficient: Apex fails immediately. Resources spent. Resolution resumes from where it was interrupted.

**Step 3 — Emergency Responses.**

The ARBITER Player returns all other factions' unresolved dispatch cases unopened. Resources are refunded. Each non-Apex faction submits one Emergency Response. Emergency Responses are submitted simultaneously and resolved by ARBITER in initiative order. They may change board state — presence chips, structure blocks, Public Standing — before the threshold is checked.

*Emergency Response is a single faction-specific action representing each faction's final attempt to influence the outcome before the session potentially ends. Definitions and narrative framing are in Artifact 04 — Action Card System and Artifact 05 — Operative & Apex System.*

**Step 4 — Board Strength threshold check.**

After Emergency Responses resolve, The ARBITER Player counts the Apex faction's total presence chips and structure blocks (Board Strength). If the total no longer meets the threshold specified in Artifact 05, the Apex is cancelled. Resources spent. Operative does not retire. Resolution resumes from where it was interrupted.

*The threshold may have shifted due to Emergency Response effects — this check happens after all Emergency Responses resolve.*

**Step 5 — All conditions met: Apex resolves.**

The ARBITER Player opens the sealed Apex envelope and pauses 5 seconds. ARBITER reads the Apex narrative card aloud. The ARBITER Player applies all public board effects and updates the Chorus Portrait track. The session ends. Proceed to Session End per Artifact 10a — Victory System.

*Full Apex rules in Artifact 05 — Operative & Apex System.*

### ARBITER Conversion

Available during Debrief and between phases. Not available during Resolution Beats 1–4 or while The ARBITER Player is processing board changes. Rate is determined by the requesting faction's presence at the Chorus Node — see Artifact 02a §8. Announced in Round 1 only.

*This is the lowest priority item on The ARBITER Player's task list — Faction Players requesting conversion during resolution are acknowledged and served after the current beat completes.*

---

## 15. Examples & Exceptions

### Initiative — Round 3

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

*Round 5 Beat 3. The Directorate's Detain operative ability successfully resolves against Ghost. Ghost has a deployment marker at Data Exchange showing the Converting face.*

The ARBITER Player flips Ghost's Data Exchange marker to the Blocked face. At Round 5's End of Round, the marker returns to Ghost's hand without converting. Ghost's influence at Data Exchange does not increase.

*Round 6 Upkeep Step 4: Ghost checks markers on the board. The Data Exchange marker is not on the board — it was returned last round. No conversion occurs. Step 4 has no effect for Ghost at Data Exchange this round.*

---

### Countermeasure — Type B Example

*Round 5. The Directorate plays a Type B Countermeasure. All roll thresholds against The Directorate's assets are −15.*

Ghost submits a Gather at Government Citadel (no presence — Challenging base, target 01–25). Public Standing: Neutral (0). Type B modifier: −15. Modified target: 01–10.

Ghost rolls: 18. Target is 10. Fails. The Directorate's defensive preparation made an already difficult operation nearly impossible without being able to block it outright.

---

### Dispatch Case Return — Processing Results

*End of Beat 5. The ARBITER Player returns Ghost's dispatch case.*

Ghost finds:
- Three covert operation cards
- Operation Succeeded card (Gather at Data Exchange)
- Operation Failed card (Undermine at Financial Clearinghouse)
- Operation Blocked card (Build Structure at Government Citadel — Type A Countermeasure)
- One intel note: Faction: The Syndicate / Round: 5

Ghost processes this privately before Debrief opens.

---

### Findings Decay — End of Round

*Ghost ends Debrief holding 9 Findings.*

9 is in the 7–12 bracket. Ghost removes 2 Findings publicly and returns them to the Reservoir. Ghost begins Round 6 Upkeep with 7 Findings before collecting income.

---

### Status Marker — Debrief Close

*Round 6 Debrief. The Network and The Directorate are negotiating. Ghost, The Guild, and The Syndicate have all flipped to green.*

Three of five show green. ARBITER: *"The majority is ready. Sixty seconds."*

The Network and The Directorate reach agreement with 20 seconds remaining. Both flip to green. ARBITER closes Debrief. Accord registered. Round closes.

---

### Apex Interrupted — Beat 3

*Round 7 Beat 3. ARBITER opens The Guild's dispatch case and finds an Apex operation card.*

ARBITER announces: *"An Apex operation has been submitted. Resolution is suspended."*

Two other dispatch cases remain unopened — they are returned to their owners with resources refunded. Each non-Guild faction submits one Emergency Response.

The Network uses their Emergency Response to Undermine The Guild's presence at Power Grid, reducing their chip count. The Directorate Occupies Government Citadel, adding chips to their own position.

After Emergency Responses resolve, The ARBITER Player counts The Guild's Board Strength: 11 chips + 4 structure blocks = 15. Threshold required: 12. Still met.

The ARBITER Player opens the sealed Apex envelope and pauses. ARBITER reads. The session ends.
