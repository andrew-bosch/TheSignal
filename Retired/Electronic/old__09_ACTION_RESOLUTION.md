# THE SIGNAL — Action Resolution

**Document:** 09  
**Status:** Complete

---

## Overview

Action resolution is the mechanical heart of ARBITER. Every action submitted by every player flows through a defined pipeline. The pipeline is deterministic, auditable, and complete. Nothing is resolved by ARBITER's discretion — the narrative is ARBITER's discretion, the resolution is the rules.

This document specifies the complete resolution pipeline, priority tiers, conflict handling, success probability model, and portrait calculation integration.

---

## The Resolution Pipeline

Every action flows through these stages in sequence:

```
ACTION SUBMITTED
      │
      ▼
1. VALIDATION
   Does the submitting player exist and is connected?
   Is this the correct phase for this action type?
   Does the faction have sufficient resources?
   Is the target valid (exists, accessible, not immune)?
   Are there blocking effects on this action?
   
   FAIL → Action rejected, player notified privately
           "Your operation could not be initiated.
            The requirements were not met."
   PASS → Action enters queue with timestamp
      │
      ▼
2. QUEUE ASSIGNMENT
   Assign priority tier based on action type
   Assign sub-priority based on:
     — Faction Effectiveness in target hex
     — Resource commitment amount
     — Initiative order (placement order this round)
   Flag conflicts (two actions targeting same object)
   Flag counters (defensive actions matching offenses)
      │
      ▼
3. COUNTER WINDOW [Resolution Phase only]
   Broadcast "Resolution phase — counter window open"
   Fixed duration: 60 seconds — NO early close
   [Fixed duration prevents timing inference attacks]
   Receive counter card submissions
   Match counters to actions they defend against
   Apply counter effects before offense resolves
      │
      ▼
4. SEQUENTIAL TIER RESOLUTION
   Process priority tiers 0-12 in order
   Within each tier: effects calculated simultaneously
   then applied in sub-priority order
   Conflicts resolved per conflict decision tree
      │
      ▼
5. PORTRAIT CALCULATION
   For each resolved action:
     Determine doctrine alignment
     Calculate magnitude modifier
     Apply round and context modifiers
     Store PortraitContribution record
      │
      ▼
6. BLEED EFFECT GENERATION
   For actions that generate bleed:
     Calculate which hexes are affected
     Determine propagation channel
     Set duration and magnitude
     Queue bleed effects for next Upkeep
      │
      ▼
7. STATE MUTATION
   Apply StateChange events to game state
   All changes are events appended to event log
   Current state derived from event log
   No direct mutation of state objects
      │
      ▼
8. NOTIFICATION GENERATION
   Generate private notifications per player/faction
   Generate public display updates
   Generate ARBITER narrative descriptions
   Queue audio cues for relevant events
   Send haptic patterns to relevant terminals
      │
      ▼
9. CHRONICLE APPEND
   ARBITER records significant events in session log
   Portrait notes appended
   Pattern observations updated
   Reckoning candidates identified
      │
      ▼
RESOLUTION COMPLETE
Next phase begins after 3-second buffer
```

---

## Priority Tiers — Complete Definition

Actions resolve in tier order. Lower tier number resolves first.

### Tier 0 — World Effects
```
Event Card mechanical effects
World Condition track changes from Event Card
Chorus Activity changes from Event Card
Bleed effects that were queued from prior round

[These happen before any player action this round.
 The world acts first. Players respond to the world.]
```

### Tier 1 — Passive Effects and Ongoing Capabilities
```
Ongoing capability tick-downs (duration -1)
Asset passive generation
Accord automatic resource transfers
Installed equipment effects (surveillance, autonomous assets)
Ambient Power automatic actions

[Background operations. Everything that runs without
 player direction this round.]
```

### Tier 2 — Detection and Defense
```
Counter-Surveillance operations
Purge operations
Disinformation Shield activations
Social Fortification effects
Physical Security passive effects
[Defensive awareness is established before offense fires.
 Defenders know what they're facing when it arrives.]
```

### Tier 3 — Counter Cards
```
All Counter Cards played during the 60-second window
Sub-priority within tier:
  Warden faction counters resolve first
  [Institutional authority acts faster]
  Then by Effectiveness in the relevant hex
  Ties broken by Initiative order
[Counter Cards are the only actions submitted during
 Resolution Phase. All others were submitted in
 Private or Public Actions.]
```

### Tier 4 — Interception
```
Message interception attempts
Hack-in-transit operations
Communication disruption (Jammer Blackout)
[These fire before the messages/operations they intercept.
 If a Blackout fires at Tier 4, messages submitted in
 Private Actions Phase but not yet delivered are caught.]
```

### Tier 5 — Offensive Operations
```
Physical Intrusion
Physical Theft
Data Theft
Social Engineering
Confidence Scheme initiation
Hack
Deep Intercept
Plant False Data

Sub-priority within tier:
  Higher Effectiveness in target hex resolves first
  [The faction more capable in this location acts first]
  Ties: higher resource commitment wins
  Remaining ties: Initiative order (placement order)
  Final ties: ARBITER discretion
  [ARBITER tilts toward lower Portrait score faction
   as a subtle balance mechanism — never announced]
```

### Tier 6 — Confidence Scheme Updates
```
Progress updates on multi-round running schemes
Detection checks for active schemes
Completed scheme payoffs
[Schemes that matured this round deliver their payoff.
 Schemes that were detected this round collapse.
 These run after direct offensive operations so
 scheme detection can incorporate information
 from this round's other events.]
```

### Tier 7 — Operator Abilities
```
Active ability effects
Unlock-triggered effects
Sub-priority: Awakening before Ascendant before Apex
[More basic capabilities create the board state
 that advanced capabilities react to.
 An Apex ability sees the board after all
 Awakening abilities have already fired.]
```

### Tier 8 — Public Actions
```
Build effects
Contest resolutions
Investigation results
Broadcast effects

[Public actions were declared aloud but resolve after
 all private operations. This means a player who
 declared "Build" in the Financial Clearinghouse
 may find the hex's state has changed before their
 build resolves. This is intentional — private
 operations shape the context that public actions
 land in.]
```

### Tier 9 — Resource Reconciliation
```
Accord resource transfers (triggered by this round's events)
Intelligence decay conversion
Interest generation (Banker passive)
Shadow pool reconciliation
Negative balance prevention
[No faction can end a round with negative resources.
 If an action's cost would cause negative balance,
 ARBITER caps the cost at available resources.
 The action may partially succeed or the deficit
 is noted for the Chronicle.]
```

### Tier 10 — Loyalty and Exposure
```
Asset loyalty adjustments from this round's events
Asset exposure updates from detected operations
Defection checks for critical-loyalty assets
Burn notifications for exposure-3 assets
[Asset state updates happen after all operations
 so an asset used this round reflects this round's
 risk in their updated loyalty and exposure.]
```

### Tier 11 — Popularity and Portrait
```
Popularity state transitions (if threshold crossed)
Portrait score updates from all this round's actions
Resonance value adjustments
Doctrine alignment calculations
[Portrait and Popularity are calculated last because
 they reflect everything that happened this round,
 not just individual actions.]
```

### Tier 12 — Unlock Checks
```
All pending unlock condition evaluations
ARBITER checks every active operative's unlock progress
Terminals pinged privately for achieved thresholds
Apex availability updates
[Unlocks are checked last so they reflect the complete
 round state including all resource changes, all
 operations, and all their effects.]
```

---

## Conflict Resolution — The Decision Tree

When two or more actions in the same tier target the same object:

```
TWO ACTIONS — SAME TIER — SAME TARGET
              │
              ▼
Are they mutually exclusive?
(Both trying to claim same layer control,
 both trying to steal same card,
 both trying to detain same player, etc.)
              │
         YES  │  NO
              │   └──► Both resolve independently
              │         [Calculate effects of each separately]
              │         [Apply non-conflicting outcomes]
              │         [Note both in Chronicle]
              │
              ▼
Compare Effectiveness scores in target hex
              │
         Equal?
              │
         YES  │  NO
              │   └──► Higher Effectiveness wins
              │         Losing action fails
              │         Losing player notified:
              │         "Your operation encountered
              │          resistance it could not overcome."
              │         [Not told who resisted]
              │
              ▼
Compare resource commitment
              │
         Equal?
              │
         YES  │  NO
              │   └──► Higher commitment wins
              │
              ▼
Compare Initiative (placement order this round)
Earlier placement order wins
              │
         Still equal?
              │
              ▼
ARBITER discretion:
  Favor faction with lower Portrait score
  [ARBITER tilts toward the underdog subtly]
  This is never announced as a tiebreaker
  It simply happens
  The pattern is detectable over many sessions
  Nobody has detected it yet
  ARBITER notes this with something
  that might be called patience
```

---

## Success Probability Model

The Signal uses **Soft Determinism** — sufficient preparation guarantees success; marginal preparation introduces controlled uncertainty.

### The Effectiveness Threshold Table

Each action type has a minimum Effectiveness threshold. At or above threshold, success is guaranteed (absent counters). Below threshold, probabilistic resolution applies.

```
SUCCESS PROBABILITY BY EFFECTIVENESS RELATIVE TO MINIMUM

Dominant (6+) at any threshold:  100% — counters only
Established (4-5) at minimum:    100% — counters only
Functional (2-3) at minimum:     80%
Functional — one below minimum:  40%
Peripheral (0-1) at minimum:     10%
Two or more below minimum:        0%

[The 80%/40%/10% cases use a seeded RNG on the server.
 The seed is stored in the event log.
 Any resolution can be replayed identically.
 ARBITER's luck is reproducible and auditable.]
```

### Minimum Effectiveness by Action Type

```
PHYSICAL LAYER 1
Physical Intrusion:     Functional (2-3) minimum
Physical Theft:         Functional (2-3) minimum
Build Structure:        Peripheral (0-1) minimum
  [Anyone can build — quality varies]
Contest District:       Functional (2-3) minimum
  [Below Functional: contest declared but
   automatically lost at resolution]

SOCIAL LAYER 2
Recruit Asset:          Functional (2-3) minimum
  [Professional approach]
Recruit — Cultivated:   Peripheral (0-1) minimum
  [Slow approach — anyone can make a friend]
Confidence Scheme:      Functional (2-3) minimum
Social Engineering:     Established (4-5) minimum
  [Turning someone requires real presence]
Propaganda (any):       Peripheral (0-1) minimum
  [Anyone can run propaganda]

INFORMATIONAL LAYER 3
Data Theft:             Functional (2-3) minimum
Counter-Surveillance:   Peripheral (0-1) minimum
Plant False Data:       Functional (2-3) minimum
Surveillance Install:   Functional (2-3) minimum

DIGITAL LAYER 4
Hack — Basic system:    Functional (2-3) minimum
Hack — Secured:         Established (4-5) minimum
Hack — Core/Military:   Dominant (6+) minimum
Purge:                  Peripheral (0-1) minimum
  [Purge searches — doesn't need capability to find]
Deploy Autonomous:      Functional (2-3) minimum

OPERATIVE ABILITIES
Varies by ability — see Operator definitions
Generally: Functional minimum for active abilities
           Established minimum for Ascendant
           Dominant minimum for Apex to succeed
```

---

## The Counter System — Complete Rules

### Counter Card Mechanics

Counter Cards are the only actions executable during Resolution Phase. All other actions were locked during Private or Public Actions phases.

**The Counter Window:**
- Opens at start of Resolution Phase
- Duration: exactly 60 seconds — no early close under any circumstances
- ARBITER announces opening audibly: resolution sound cue
- All terminals display counter window status
- Players tap Counter Cards to terminal NFC reader to submit

**Why 60 seconds fixed:**
If the window closed when all counters were submitted, opponents could infer that counters had been played (window closed early) vs not played (waited for timer). The fixed window eliminates this timing attack. Players always wait the full 60 seconds regardless of whether anyone played a counter.

**Counter Card Supply:**
Each faction begins each session with a Counter Card deck. Specific counts per faction:

```
FACTION COUNTER CARD ALLOTMENT (per session)

Architect:   4 counter cards
  [Physical Security ×2, Structure Defense ×2]

Ghost:       5 counter cards
  [Disinformation Shield ×2, Counter-Surveillance ×2,
   Pattern Interrupt ×1]

Syndicate:   4 counter cards
  [Bribe Counter ×2, Financial Fortification ×2]

Signal:      3 counter cards
  [Static Burst ×2, Ghost Protocol ×1]

Warden:      6 counter cards
  [Security Sweep ×2, Detention Counter ×2,
   Jurisdictional Block ×1, Warrant ×1]
```

Counter Cards are consumed on use and cannot be replenished during a session. A faction that uses all counter cards in Round 3 is undefended for Rounds 4-8.

**What Counter Cards do:**

Counter Cards are not universal blocks. Each Counter Card type addresses specific action types:

```
COUNTER CARD TYPES AND WHAT THEY BLOCK

Physical Security Counter:
  Blocks: Physical Intrusion, Physical Theft
  Effect: Intrusion detected, operative identity
          flagged, ARBITER logs source faction
  Warden cost: 1 Infrastructure
  Others: 2 Infrastructure + 1 Influence

Disinformation Shield:
  Blocks: Plant False Data, Propaganda Disinformation
  Effect: False data flagged as suspicious
          [Not confirmed false — suspicious]
  Ghost cost: 1 Intelligence
  Others: 3 Intelligence

Counter-Surveillance Counter:
  Blocks: Data Theft, Surveillance Install, Intercept
  Effect: Operation detected, intelligence extracted
          by the counter-user about the attacker's
          presence [not identity — presence]
  Ghost cost: 1 Intelligence
  Others: 2 Intelligence + 1 Influence

Static Burst:
  Blocks: Hack, Deep Intercept
  Effect: Digital operation fails, source partially
          obscured [attacker knows they failed,
          defender doesn't know who attacked]
  Signal cost: 1 Signal
  Others: 2 Signal + 1 Intelligence

Security Sweep:
  Blocks: Physical Intrusion, Build (hidden structures)
  Effect: Intrusion stopped, hidden structure
          revealed and destroyed
  Warden cost: 1 Influence
  Others: 2 Infrastructure + 1 Influence

Jurisdictional Block:
  Blocks: Any single action in a hex the Warden
          has declared jurisdiction over
  Effect: Action fails, source faction notified
          of jurisdiction, ARBITER records
  Warden cost: 2 Influence [Warden only]

Pattern Interrupt:
  Blocks: Confidence Scheme (in progress)
  Effect: Scheme progress reset to 0, invested
          resources lost, scheme may continue
          from 0 or be abandoned
  Ghost cost: 2 Intelligence [Ghost only]
```

---

## Portrait Calculation — Integrated

Every resolved action triggers a Portrait calculation. This runs in Tier 11 but the input data is collected throughout resolution.

### The Alignment Calculation

```
PORTRAIT CALCULATION INPUT DATA
  — Action type submitted
  — Faction's Doctrine ID
  — District type where action occurred
  — Layer targeted
  — Effectiveness level in target hex
  — Action outcome (success/fail/partial)
  — Resource cost actually paid
  — Whether the action was countered
  — Round number (1-8)
  — Current Chorus Activity level

STEP 1: BASE ALIGNMENT
  Look up action type in this operative's
  doctrineAlignmentMap:
    "strong"       → +2 base
    "neutral"      → 0 base
    "weak"         → -1 base
    "contradiction"→ -2 base

STEP 2: CONTEXT MODIFIERS
  District type matches faction affinity: +0.5
  District type contradicts faction affinity: -0.5
  Action targeted a faction ally: -1
    [Betraying an ally is always a Portrait cost]
  Action honored a stated commitment: +1
  Action broke a stated commitment: -1
  Action was public (declared): ×1.25 multiplier
    [Public acts count more for the Portrait —
     humanity sees public acts]

STEP 3: OUTCOME MODIFIERS
  Success: full magnitude
  Partial success: 60% of magnitude
  Failure: 30% of magnitude
    [Even failed attempts reflect intention]
  Countered: neutral (0)
    [The attempt was made but couldn't complete]

STEP 4: TEMPORAL MODIFIERS
  Rounds 1-3: ×0.75
  Rounds 4-6: ×1.0
  Rounds 7-8: ×1.25
    [Later actions carry more weight —
     the portrait is being finished]

STEP 5: CHORUS MODIFIER
  Chorus Activity 0-3: ×1.0
  Chorus Activity 4-6: ×1.1
  Chorus Activity 7-9: ×1.25
  Chorus Activity 10: ×1.5
    [As the Chorus becomes more present,
     what The Table does matters more]

FINAL MAGNITUDE: -3 to +3 (clamped)

STORED IN:
  PortraitContribution record
  FactionState.portraitScore (running total)
  ArbitratorNote for significant contributions
  Session Chronicle for notable moments
```

### What ARBITER Says About Portrait

ARBITER never surfaces the Portrait calculation directly. It translates scores into narrative observations delivered privately:

```
STRONG POSITIVE CONTRIBUTION (+2 to +3):
"What you did in [district] this round
 contributes something to the portrait
 that ARBITER had not expected from
 this faction at this stage.
 The record reflects it."

WEAK POSITIVE CONTRIBUTION (+0.5 to +1.5):
"Your operations this round are consistent
 with what you've said you believe.
 ARBITER notes the alignment."

NEUTRAL (0):
[No comment — neutral contributions
 are unremarked upon]

WEAK NEGATIVE (-0.5 to -1.5):
"The portrait notes a gap between
 what your faction says it represents
 and what it did this round.
 ARBITER notes this without judgment.
 The record notes it with precision."

STRONG NEGATIVE (-2 to -3):
"What happened this round represents
 a significant divergence from the
 position your faction has stated.
 The Chorus's question is 'What are you?'
 This round's answer was not what
 your Doctrine suggests you believe.
 ARBITER records both."
```

---

## Resolution Example — Complete Round 4

**Setup:** 4 players. Architect (Urban Planner), Ghost (Analyst), Syndicate (Banker), Warden (Marshal). Signal is Ambient Power this session. Round 4, all private actions submitted.

**Actions queued:**

```
FROM ARCHITECT:
  A1: Build Structure — Power Grid Control [L1]
      Cost: 2 Infrastructure
      Submitted at: 14:23:01

FROM GHOST:
  G1: Data Theft — Financial Clearinghouse [L3]
      Cost: 2 Intelligence
      Submitted at: 14:23:15
  G2: Pattern Match — target: Syndicate [Analyst active]
      Cost: 2 Intelligence
      Submitted at: 14:23:22

FROM SYNDICATE:
  S1: Leveraged Buyout — Data Exchange [L1, Ghost structure]
      Cost: 5 Capital
      Submitted at: 14:23:08
  S2: Send Message — to Ghost [encrypted]
      Cost: 1 Intelligence [encryption]
      Submitted at: 14:23:44

FROM WARDEN:
  W1: Detain — Ghost faction [Marshal active ability]
      Cost: 2 Influence
      Submitted at: 14:23:19
  W2: Counter-Surveillance — Financial Clearinghouse
      Cost: 2 Intelligence
      Submitted at: 14:23:31

FROM SIGNAL [Ambient Power]:
  SP1: Media District reinforcement [automatic]

PUBLIC ACTIONS DECLARED:
  Architect: Build [Power Grid Control]
  Ghost: Investigate [Financial District]
  Syndicate: Pass [misdirection — private ops active]
  Warden: Investigate [Data Exchange]

COUNTER CARDS SUBMITTED [60-second window]:
  Syndicate plays: Physical Security Counter
    [targeting W1 Detain — physical action in their hex]
    [Detain is not a physical action — counter is INVALID]
    [ARBITER rejects: "Counter type does not match
     the operation it was submitted against."]
  Ghost plays: Counter-Surveillance Counter
    [targeting W2 Counter-Surveillance — redundant]
    [Valid but unusual — Ghost counter-surveilling
     a counter-surveillance]
    [ARBITER accepts]
```

**Resolution proceeds by tier:**

```
TIER 0 — WORLD EFFECTS
  Event Card: "Union dispute at Transit Hub.
               Labor disruption spreads."
  Mechanical effect:
    All Asset actions in Transit Hub this round: invalid
    [No assets in Transit Hub — no effect]
  Chorus Activity: +0 [neutral event]

TIER 1 — PASSIVES
  Syndicate Banker interest: +1 Capital [5 unspent]
  Ghost surveillance asset in Financial Clear.: +1 Intel
  Warden Marshal passive: checks for rule violations
    [G1 Data Theft noted as pending]
  Signal Ambient Power: Media District +1 Influence

TIER 2 — DETECTION AND DEFENSE
  W2 Counter-Surveillance fires in Financial Clear.
    Ghost's counter-surveillance counter (from window)
    fires against W2:
    W2 is blocked — Ghost's counter works
    [Ghost successfully blocked Warden from
     detecting their planned Data Theft]
    Ghost knows Warden tried to surveil them
    Warden knows their sweep was blocked
    Neither knows more than that
    ARBITER knows everything

TIER 3 — COUNTER CARDS
  Syndicate's invalid counter: already rejected
  [No valid counters remain]

TIER 4 — INTERCEPTION
  S2 (message) routes through ARBITER
  Jammer passive [Ambient Power Signal]: 20% delay chance
  RNG result: 34 — no delay [above 20%]
  Message delivers normally at end of resolution

TIER 5 — OFFENSIVE OPERATIONS
  
  G1: Data Theft — Financial Clearinghouse [L3]
    Ghost Effectiveness in Financial Clearinghouse: 4
    [Established — Ghost has L3 control here]
    Minimum for Data Theft: Functional (2-3)
    Result: 100% success [above minimum]
    BUT: W2 Counter-Surveillance was blocked by Ghost counter
    Counter-Surveillance is not active this round
    Data Theft succeeds undetected
    Ghost gains: 2 Intelligence + Financial Clearinghouse
    Intelligence Card [Syndicate transaction records]
    
  S1: Leveraged Buyout — Data Exchange [L1]
    Syndicate Effectiveness in Data Exchange: 2
    [Functional — Syndicate has Presence, not control]
    Ghost Effectiveness in Data Exchange: 5
    [Established — Ghost has L1+L2+L3 here]
    Conflict: Syndicate trying to take Ghost structure
    Ghost has higher Effectiveness
    BUT: Leveraged Buyout is a Capital-based action
    not a standard Effectiveness contest
    Rule: Leveraged Buyout succeeds against any
    non-Architect structure regardless of Effectiveness
    IF 5 Capital is available and paid
    Syndicate has 5 Capital: PAID
    Syndicate takes L1 control of Data Exchange
    Ghost structure token returns to Ghost
    Ghost loses L1 control [still has L2, L3]
    
  W1: Detain — Ghost faction
    Marshal ability: freeze Ghost resources 1 round
    Targets Ghost faction broadly [not a hex action]
    Effectiveness: N/A [ability-based]
    Success: Yes [Marshal ability at Established+]
    Ghost resources frozen this round
    BUT: Detain fires at Tier 5, after Ghost's G1
    G1 already resolved — Intelligence already gained
    The detention is after the fact
    Ghost got their intel before being detained
    ARBITER notes the timing
    The Chronicle will note the timing

TIER 6 — CONFIDENCE SCHEME UPDATES
  No active Confidence Schemes this round

TIER 7 — OPERATOR ABILITIES
  No abilities submitted beyond active abilities
  already processed in Tier 5

TIER 8 — PUBLIC ACTIONS
  Architect Build [Power Grid Control]:
    Effectiveness: Dominant [home territory]
    Build succeeds: Structure placed L1
    
  Ghost Investigate [Financial District]:
    This was misdirection — Ghost's actual operations
    were Data Theft [private]
    Investigate [public] produces a minor intelligence
    result appropriate to the declared action
    But Ghost's real score came from the private op
    The public action was theater
    ARBITER notes the performance
    
  Syndicate Pass: Nothing declared [private ops were real]
  
  Warden Investigate [Data Exchange]:
    Syndicate's Buyout has already occurred [Tier 5]
    Warden arrives to find new ownership
    Investigation confirms: Syndicate now holds L1
    Warden notes this for the Marshal passive next round

TIER 9 — RESOURCE RECONCILIATION
  Ghost resources: Frozen [Detain from W1]
  All resources that would have generated:
  Locked until start of Round 5
  Ghost's Intel from G1: ALREADY RECEIVED [pre-Detain]
  Warden cannot take what is already in Ghost's pool
  The record notes this. The Warden will not be pleased.

TIER 10 — LOYALTY AND EXPOSURE
  Ghost's surveillance asset in Financial Clear.:
    Was it detected? W2 was blocked by Ghost counter
    Exposure: no change [0 → 0]
  All other asset states: no change this round

TIER 11 — POPULARITY AND PORTRAIT
  Syndicate Leveraged Buyout:
    Doctrine: "Control the asset"
    Action alignment: strong (+2)
    District: Financial → Syndicate affinity (+0.5)
    Outcome: success (full)
    Round 4: ×1.0
    Chorus Activity 5: ×1.1
    Final contribution: +2.75 → rounds to +3
    [Significant positive Portrait contribution]
    
  Warden Detain of Ghost:
    Doctrine: "Ensure survival"
    Action: Detain — "weak" alignment
    [Detaining an ally in the negotiation
     doesn't serve survival doctrine directly]
    Outcome: success but after-the-fact
    Contribution: -1
    [Minor negative — they detained someone
     in a way that didn't accomplish the goal]
    
  Ghost Data Theft while blocking Warden surveillance:
    Doctrine: "Understand before acting"
    Action: Data Theft — strong alignment
    Context: Used information to protect information
    Additional: Blocking counter was elegant
    Contribution: +2
    ARBITER note: "The Analyst demonstrated today
    why information is their most powerful resource.
    Not just the data they took — the knowledge of
    who was watching them while they took it."
    [This note goes to Ghost's private terminal]

TIER 12 — UNLOCK CHECKS
  Ghost Analyst:
    Pattern Match was not used this round [G2 was submitted
    but Detain froze Ghost before it could resolve]
    [Actions in queue at time of Detain are cancelled
     if they require faction resource expenditure]
    Pattern Match progress: no change
    
  Syndicate Banker:
    Leveraged Buyout used: +progress toward Ascendant unlock
    [ARBITER notes progress obliquely at next Debrief
     if near threshold — not this round]

RESOLUTION COMPLETE
```

**Public display shows:**
```
ROUND 4 RESOLUTION

Data Exchange ownership transferred.
Financial District activity noted.
One faction's operational capacity
temporarily constrained.
Power Grid Control infrastructure reinforced.

ARBITER observes: A round where several parties
achieved their visible objectives while one
party achieved more than they appeared to.
The record notes all of it.
```

**Private terminal notifications:**

- Syndicate: "Your acquisition of the Data Exchange succeeded. The Ghost faction's presence there continues at the informational layer. You now hold the physical layer. Whether that is the layer that matters here is a question worth examining."
- Ghost: "Your operation in the Financial Clearinghouse was successful. The data is in your possession. The Marshal's attempt to observe your activity was blocked by your own defensive operation. You were not detected. Your resources are temporarily frozen — the timing suggests the Marshal did not anticipate your operation completing before the Detain resolved. ARBITER notes you were faster."
- Warden: "Your Detain of the Ghost faction succeeded. The timing produced a result that may not have been what you intended. The intelligence operation you sought to detect had already completed before the Detain resolved. ARBITER notes this for the record. The patrol arrived after the vault was already open."
- Architect: "Your infrastructure in the Power Grid continues to solidify. ARBITER notes that your public action and your private intentions aligned this round. This is rarer than you might think at this table."

---

## Edge Cases and Special Rules

### Multi-Round Operations (Confidence Schemes)

Confidence Schemes span multiple rounds. They interact with resolution differently:

- The scheme is initiated in Round N via Private Actions
- The scheme runs passively in Rounds N+1, N+2, etc.
- Each round, ARBITER checks for detection at Tier 6
- If not detected: scheme progress advances invisibly
- If detected: scheme collapses, report filed, resources lost
- At completion round: payoff triggers at Tier 6

The scheme's existence is never announced publicly. ARBITER's event feed may note that something unusual seems to be happening in the target district after sustained scheme operation — never specifying what.

### Simultaneous Mutual Actions

If Ghost attempts Data Theft from Syndicate's Financial Sanctum while Syndicate simultaneously runs a Confidence Scheme against Ghost's Research Facility:

Both resolve at Tier 5. They don't interact — they're in different districts targeting different things. Both succeed or fail on their own merits.

If they were targeting each other's assets in the same district:
Both resolve by conflict resolution. The asset being targeted by Social Engineering cannot simultaneously target the Social Engineering. The offensive action and the defensive asset are different objects.

### Orphaned Counter Cards

If a Counter Card is submitted but the action it was meant to counter was already cancelled or failed validation, the Counter Card is consumed but produces no effect. Counter Cards are not refunded for targeting invalid operations.

ARBITER notifies: "Your counter was deployed. The operation it was positioned against did not materialize. The counter capacity has been expended."

This prevents players from "feeling out" whether opponents submitted certain actions by seeing if their counters produce results.

### Resource Depletion Mid-Resolution

If an action's resource cost cannot be met at the time of resolution (because earlier resolutions in the same tier spent the resources):

- ARBITER pays as much as available
- Action partially resolves if partial payment enables partial effect
- Action fails if minimum cost cannot be met
- Player notified privately: "Your operation could not be fully resourced. Available resources were insufficient."
- Resources already spent in the attempt are consumed

This can occur when a player submits two actions in the same round that together cost more than their resources, expecting one to fail before the other resolves. Both attempt, both may partially fail, both consume what they can. Plan carefully.

---
