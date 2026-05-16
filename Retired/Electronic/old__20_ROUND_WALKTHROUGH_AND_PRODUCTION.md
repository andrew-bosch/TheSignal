# THE SIGNAL — Paper Prototype: Round Walkthrough & Production Guide

**Document:** 20  
**Status:** Active Design — Companion to Document 19

---

## How To Use This Document

This document walks through a complete Round 4 of a 5-player paper prototype session in granular detail. Every physical action, every player interaction, every ARBITER decision is specified. Assumptions are flagged explicitly. Unresolved design questions are marked **[DECISION REQUIRED]**. Potential roadblocks are marked **[ROADBLOCK]**.

The round walkthrough uses five named players at a real table:

- **Maya** — playing THE GHOST / The Analyst
- **Dev** — playing THE SYNDICATE / The Banker  
- **Riya** — playing THE ARCHITECT / The Contractor
- **Soren** — playing THE WARDEN / The Auditor
- **Priya** — playing THE SIGNAL / The Jammer
- **[One player, unlisted]** — playing ARBITER (non-faction role)

**Session context:** Round 4 of 8. The table has been playing for about 75 minutes. Dev's Syndicate controls the Financial Clearing and Commercial Strip. Maya's Ghost has hidden informational presence in Data Exchange and Financial Clearing. Riya has two structures on the board — Industrial Fringe and Power Grid. Soren has been calling out rule violations and nobody trusts them. Priya has been quiet, which everyone finds more alarming than noise.

---

## Before Round 4 Begins — State of the Table

### Physical Board State

```
DISTRICT          L1 CONTROL     STRUCTURES
─────────────────────────────────────────────
Chorus Node       None           None
Government Cit.   Warden         None
Corporate Tower   Syndicate      Syndicate (basic)
Chorus Research   None           None
Data Exchange     Ghost          None
Financial Clear.  Syndicate      None
Power Grid        Architect      Architect (basic)
Communications    None           None
University Per.   Ghost          None
Media District    Signal         None
Residential Zone  None           None
Commercial Strip  Syndicate      Syndicate (basic)
Industrial Fringe Architect      Architect (basic)
```

### ARBITER's Hidden Tracker (L3 Control — Players Don't Know This)

```
DISTRICT          L3 PRESENCE
─────────────────────────────
Data Exchange     Ghost (Established), Signal (Presence)
Financial Clear.  Ghost (Established)
University Per.   Ghost (Functional)
Residential Zone  Warden (Functional)
Communications    Signal (Functional)
Media District    Signal (Established)
```

### Current Resources (ARBITER's actual numbers, not declared)

```
FACTION       CAP  INFRA  SIG  INTEL  OI    STANDING
Ghost          1     1     2    8      3     Intel approaching decay threshold
Syndicate      9     2     0    2      4     Capital strong, needs Signal
Architect      3     7     0    2      3     Infrastructure rich, capital poor
Warden         2     3     0    5      9     OI surplus, Signal-blind
Signal         1     1     4    4      5     Operationally ready, physically weak
```

### World Conditions (Simplified 3-Track Paper Prototype)

```
DISCLOSURE:       3 / 6   [The Chorus is an open secret]
CONSENSUS:        2 / 6   [No framework exists yet]
CHORUS ACTIVITY:  5 / 10  [Midpoint — transmissions intensifying]
```

---

## ROUND 4 — COMPLETE WALKTHROUGH

### PRE-ROUND — Table State Check (ARBITER, 1 minute)

Before announcing the round, ARBITER silently confirms:
- Resource counts on hidden tracker match last round's reconciliation
- Any ongoing effects still active (none this round)
- Initiative order from Round 3 (Syndicate led Round 3, so they go second in Round 4 per snake rules)

**[ROADBLOCK #1 — Tracker Complexity]**  
ARBITER is tracking: 5 resource pools (5 values each = 25 numbers), L3 control for 13 districts, loyalty for any recruited assets, portrait running totals for 5 factions. On paper this is a significant cognitive load for one person.

**Proposed solution:** Use a dedicated ARBITER tracking pad with pre-formatted rows. Pre-print the tracker rather than freehand. See Component List (Section 4) for format.

**[DECISION REQUIRED #1]**  
Should ARBITER's tracker be visible to a dedicated observer/assistant, or strictly private? If ARBITER makes a math error, having a second set of eyes helps. But an assistant knowing everything may affect social dynamics.  
*Tentative decision: ARBITER tracker stays private, but an assistant can sit beside ARBITER and verify math without reading narrative notes.*

---

### PHASE 1 — UPKEEP

**Duration target: 3-4 minutes**  
**ARBITER runs this. Players watch and listen.**

#### Step 1.1 — ARBITER Distributes Passive Generation

ARBITER works through the faction list silently, updating the hidden tracker. Then announces changes narratively:

ARBITER (reading from script card, adapted):  
*"Upkeep for Round 4. New Meridian continues its work."*

ARBITER then places resource tokens from the bank in front of each player:

```
GENERATION THIS UPKEEP:

Ghost (Maya):
  Faction passive: +2 Intel
  Data Exchange L3 control: +3 Intel → DECAY CHECK
  Intel now at 13 → ABOVE 12 threshold → 50% decays
  13 Intel × 50% = 6.5 → round down to 6 Intel decayed
  6 decayed Intel × 0.25 conversion = 1.5 → 1 OI gained (round down)
  Net: Maya receives +2 Intel, loses 6 Intel to decay, gains 1 OI
  ARBITER quietly adjusts tracker: Intel 8+2-6=4, OI 3+1=4
  ARBITER places: 2 blue chips (Intel) in front of Maya
  ARBITER removes: 6 blue chips from Maya's pool
  ARBITER places: 1 white chip (OI) in front of Maya
  
  ARBITER says quietly to Maya only:
  "Your intelligence reservoir overflowed. Some data has aged past utility.
   The signal-to-noise ratio has corrected itself."

Syndicate (Dev):
  Faction passive: +2 Cap
  Financial Clearing L1: +2 Cap
  Commercial Strip L1: +2 Cap
  Banker passive (holds 9 Cap, above 5): +1 Cap
  Net: +7 Cap
  ARBITER places 7 gold chips in front of Dev
  Dev now has 16 Cap — approaching visibility threshold

Architect (Riya):
  Faction passive: +2 Infra
  Power Grid L1: +2 Infra
  Industrial Fringe L1: +2 Infra
  Affinity bonus cap: 2 districts max → Power Grid + Industrial Fringe = +2 Infra bonus
  Net: +6 Infra, +1 Cap (faction secondary passive)
  ARBITER places 6 grey chips and 1 gold chip in front of Riya

Warden (Soren):
  Faction passive: +2 OI
  Government Citadel L1: +3 OI
  Residential Zone L3 presence: +1 OI (hidden, not announced publicly)
  Net: +5 OI (public), +1 OI (not attributed)
  ARBITER places 5 white chips in front of Soren
  ARBITER privately adds 1 OI to Soren's tracker without announcing it
  Soren now has 15 OI — surplus territory

Signal (Priya):
  Faction passive: +2 OI, +1 Signal
  Media District L1: +1 OI, +1 Signal (Signal affinity: +1 OI bonus)
  Communications L3 (hidden): +2 Signal
  Net: +3 OI, +4 Signal (1 from passive + 1 from media + 2 from hidden comms)
  ARBITER places 3 white chips and 1 purple chip in front of Priya publicly
  ARBITER privately notes +3 Signal on tracker (from hidden L3)
  "You receive what is publicly due you," ARBITER says to Priya,
  placing 3 OI and 1 Signal. The rest goes on the tracker silently.
```

**[ROADBLOCK #2 — Resource Token Handling]**  
Moving individual chips is slow and error-prone. Players losing count of pools. Chips sliding on table.

**Proposed solutions:**
- Each player has a small tray or box lid to contain their pool (see Component List)
- Use poker chip denominations: 1-value and 5-value chips per resource color
- ARBITER announces changes and players self-adjust from the bank (faster than ARBITER moving chips)
- Players confirm their new totals verbally to ARBITER after each distribution

**[DECISION REQUIRED #2]**  
Should players know their exact resource numbers, or only ARBITER-tracked narrative thresholds?  
*Design intent: Players know their own exact numbers. Only other players can't see exact numbers.*  
*Paper solution: Players track their own pool. ARBITER cross-checks at key moments.*

---

#### Step 1.2 — ARBITER Reveals Event Card

ARBITER draws the top card from the 8-card session deck (pre-selected at setup, face-down). This is Event Card #4 of 8.

ARBITER flips it and reads the narrative side aloud:

*Event Card: "RESEARCH DISRUPTION"*

ARBITER reads:  
*"Three senior analysts at the Chorus Research Complex submitted requests for indefinite leave simultaneously. Administration has noted the pattern. No explanation has been offered. The Complex continues its work."*

[ARBITER does not read the mechanical side. Mechanical effect: Ghost L3 generation from Chorus Research -1 this round only. This round, Ghost has no L3 in Chorus Research anyway, so the effect is null — but players don't know that. The card creates false reads.]

ARBITER makes a small notation on the hidden tracker: "R4 Event — Chorus Research disruption, Ghost L3 null effect this round."

**[ROADBLOCK #3 — Event Card Ambiguity]**  
Players will try to interpret Event Cards and make incorrect inferences. This is intended — but ARBITER must be consistent about never confirming or denying interpretations.

**Script card for ARBITER (prepared in advance):**  
*"ARBITER has noted the event. What it means for your operations is yours to determine."*

**[DECISION REQUIRED #3]**  
Should players be allowed to ask ARBITER clarifying questions about Event Cards, or is ARBITER's silence absolute?  
*Tentative: ARBITER may answer one clarifying question per Event Card reveal, but only in The Record register (factual, flat). No interpretation. No inference. "The Complex continues its work" is all ARBITER will confirm.*

---

#### Step 1.3 — ARBITER Updates World Conditions

ARBITER adjusts the three-track display at the table edge:

- Disclosure: no change (3)
- Consensus: no change (2)  
- Chorus Activity: +1 (now 6) — triggered by the Event Card's Chorus Research theme

ARBITER moves the Chorus Activity marker one step and says:  
*"The Chorus Activity track has advanced. The transmission grows more present."*

Players see the marker move. They know Chorus Activity is now at 6. They don't know what triggers the next threshold (7 opens the Table Question window for the first time).

**[ROADBLOCK #4 — Track Legibility]**  
Three tracks with 6-10 positions need to be visible to all players simultaneously.

**Proposed solution:** Large-format track strip (A4 landscape, laminated) at center of table with three horizontal tracks and a paper clip as marker on each. At arm's reach for all players. Large enough to read from 60cm. See Component List.

---

### PHASE 2 — PLACEMENT

**Duration target: 6-8 minutes**  
**All players participate. ARBITER announces order.**

#### Step 2.1 — ARBITER Announces Initiative Order

Initiative order is determined at end of each round. Round 3 initiative: Ghost → Syndicate → Warden → Architect → Signal.

**Snake placement: Round 4**  
Forward: Ghost → Syndicate → Warden → Architect → Signal  
Reverse: Signal → Architect → Warden → Syndicate → Ghost

Each faction places 2 tokens. The snake means Ghost places first and last, Signal places 5th and 6th.

ARBITER announces:  
*"Placement order for Round 4 follows from the prior session's record. The Table proceeds: Ghost, then Syndicate, then Warden, then Architect, then Signal — then reverse."*

**[DECISION REQUIRED #4]**  
What exactly determines initiative order? The current design says "Initiative, Intelligence level, Popularity, ARBITER's discretion." For paper prototype, this needs to be a simple, consistent rule that ARBITER can apply without complex calculation.

**Proposed simple rule for paper prototype:**  
*Last round's Debrief: whoever triggered the most significant event in Round 3 goes first. Ties broken by OI held (more OI = more political weight = higher initiative). If still tied, alphabetical by faction name.*

This is gameable and may not be perfect — but it is tractable. Note it as an assumption to test.

---

#### Step 2.2 — Token Placement (Forward Pass)

Players place tokens one at a time, in order. Each placement is public, visible, and discussed.

**Ghost (Maya) — 1st token:**

Maya picks up her Ghost token (dark grey circle). She holds it over the board for a moment, looking at Data Exchange and Financial Clearing.

She places it in **Chorus Research**.

The table reacts. Chorus Research is uncontrolled. It generates Intel and Signal. Ghost going there is interesting.

ARBITER confirms placement by placing a faction control marker (dark grey sticker or chip) on the Chorus Research hex. No mechanical effect yet — token placement is confirmed at end of round, or by camera in digital version.

*Note for later: Ghost placing in Chorus Research may trigger L3 access if Ghost reaches Established effectiveness there.*

**Syndicate (Dev) — 2nd token:**

Dev places in **Data Exchange**. 

Ghost already has L1 there. This is a contest.

*Table conversation begins:*

Riya: "Bold."  
Dev: "Data Exchange generates Capital on L1. Worth contesting."  
Maya says nothing. Watches.

**Warden (Soren) — 3rd token:**

Soren places in **Communications Hub**.

Signal controls nothing here yet publicly. But Signal has hidden L3 presence. Soren doesn't know this. ARBITER does. ARBITER makes a small note.

**Architect (Riya) — 4th token:**

Riya places in **Financial Clearing**.

Syndicate's strongest financial district. Riya is either contesting or trying to establish access for a future deal.

Dev: "You're not serious."  
Riya: "Infrastructure assessment."  
Dev: "That's not infrastructure."  
Riya: "Everything is infrastructure if you look at it right."

*[This is the game working. Two players negotiating through placement before a word about mechanics is spoken.]*

**Signal (Priya) — 5th token:**

Priya places in **Residential Zone**. 

Unexpected. Signal in Residential Zone suggests community organizing or broadcast operations. Nobody controls Residential Zone L1. Priya just staked a claim.

---

#### Step 2.3 — Token Placement (Reverse Pass)

**Signal (Priya) — 6th token:**

Priya places her second token in **Government Citadel**.

Warden's home territory. Warden has Dominant L1 there.

Soren: "That's Warden territory."  
Priya: "I know."  
Soren: "You'll have minimal effectiveness."  
Priya: "I know that too."

ARBITER makes a note. Signal has Peripheral effectiveness in Government Citadel. Any operation there will be low-probability. But Signal placing there signals something. What?

**[DESIGN OBSERVATION #1 — The Value of Unreadable Moves]**  
Priya's move in Government Citadel may be strategic misdirection, a genuine operation attempt, or probing for future rounds. The ambiguity is itself valuable. The design correctly allows any faction to place anywhere. Effectiveness gates capability — it doesn't gate the right to be seen.

This is working as intended. Note it.

**Architect (Riya) — 7th token:**

Riya places second token in **Power Grid** (where she already has L1 control and a structure).

**Warden (Soren) — 8th token:**

Soren places in **Data Exchange**. Now three factions have tokens there: Ghost (L1), Syndicate (new), Warden (new).

**Syndicate (Dev) — 9th token:**

Dev places second token in **Financial Clearing** — same hex as Riya.

Direct contest declared between Architect and Syndicate for Financial Clearing.

ARBITER: *"ARBITER notes a contest in the Financial Clearing. This will be resolved in the Resolution phase."*

**Ghost (Maya) — 10th token:**

Maya places second token in **University Perimeter** — where Ghost already has L1 and L3 presence.

ARBITER notes: Ghost reinforcing a strong position. Good for effectiveness, less surprising than the Chorus Research placement.

---

**[ROADBLOCK #5 — Token Identity and Tracking]**  
With 10 tokens on a 13-district board, it can become visually cluttered. Multiple tokens in contested districts (Data Exchange has 3 factions) need to be clearly distinguishable.

**Proposed solutions:**
- Tokens are faction-colored flat discs (poker chips work well)
- Each district hex has a clear "token zone" — a marked area adjacent to the hex where multiple tokens can sit without overlap
- For contested hexes, tokens are stacked in a clear visible cluster
- Hex labels are large enough to be read under token clusters

**[DECISION REQUIRED #5]**  
How are token positions definitively confirmed? In digital version, camera confirms. In paper, ARBITER confirms verbally after each placement. Should placement be considered locked when ARBITER says "confirmed" or when the token is released?  
*Proposed: Token is locked when released by the player's hand. No take-backs after release. ARBITER confirms placement but confirmation is not required for locking.*

---

### PHASE 3 — PRIVATE ACTIONS

**Duration target: 4-5 minutes. This phase is SILENT.**

ARBITER announces:  
*"The Private Actions window is open. ARBITER will accept submissions. The Table does not speak."*

Players have their Player Information Sheets in front of them. Each player now selects their actions.

#### The Physical Mechanism (Paper Prototype)

Each player has a **Personal Action Pad** — a small notepad. Pages are roughly 10×7cm (index card size), blank lines.

**Format for writing an action:**

```
ACTION: [action name]
TARGET: [district name, faction, or asset]
RESOURCES: [what you're spending]
ADDITIONAL: [any relevant detail]
```

Players write their actions, tear off the page(s), fold them once, and place face-down in front of themselves. When done, they place their hand palm-down on their stack — the "done" signal.

**Operative ability** is written on a separate page, torn off, folded separately, placed on top of the action stack.

When all players show "done" (palm-down), ARBITER announces "The window closes" and collects all stacks.

---

#### What Each Player Actually Submits This Round

**Maya (Ghost):**

Action 1:  
```
ACTION: Data Theft
TARGET: Financial Clearing (L3)
RESOURCES: 2 Intelligence
ADDITIONAL: Using my L3 established presence
```

Action 2:  
```
ACTION: Recruit Asset (Cultivated approach)
TARGET: Chorus Research
RESOURCES: 2 OI (round 1 of 2-round cultivated recruit)
ADDITIONAL: Initiating — will complete next round
```

Action 3:  
```
ACTION: Send Message
TARGET: Soren (Warden)
RESOURCES: Free
ADDITIONAL: [Written message, sealed separately — see messaging section]
```

Operative:  
```
OPERATIVE: Pattern Match
TARGET: Dev (Syndicate)
RESOURCES: 2 Intelligence
ADDITIONAL: Guessing Syndicate will attempt Leveraged Buyout this round
```

**Dev (Syndicate):**

Action 1:  
```
ACTION: Leveraged Buyout
TARGET: Data Exchange L1 (Ghost structure)
RESOURCES: 5 Capital
ADDITIONAL: Taking Ghost's L1 position
```

Action 2:  
```
ACTION: Physical Intrusion
TARGET: Financial Clearing (L1)
RESOURCES: 2 Infrastructure (borrowed from Architect? — see trade section)
ADDITIONAL: Contesting Architect placement
```

Action 3:  
```
ACTION: Confidence Scheme (initiate)
TARGET: Residential Zone
RESOURCES: 2 OI + 1 Intelligence
ADDITIONAL: Beginning scheme — will not manifest for 2 more rounds
```

Operative:  
```
OPERATIVE: Under the Table (Fixer)
TARGET: ARBITER
RESOURCES: 3 Capital + 1 Influence
ADDITIONAL: Requesting delay of rule enforcement on Accord breach (see Accord #2)
```

**[DESIGN OBSERVATION #2 — Simultaneous Hidden Information Creates Real Tension]**  
Dev is submitting a Leveraged Buyout targeting Ghost's Data Exchange position AND Maya is submitting Data Theft against Syndicate's Financial Clearing. Neither knows the other is attacking them. Both are operating based on reads, not information. This is the game working.

---

**Riya (Architect):**

Action 1:  
```
ACTION: Build Structure (Hidden — Contractor passive)
TARGET: Financial Clearing
RESOURCES: 2 Infrastructure (reduced by 1, Contractor passive: 1 Infrastructure)
ADDITIONAL: Hidden structure. ARBITER tracks. Not visible to others.
```

Action 2:  
```
ACTION: Contest District
TARGET: Financial Clearing vs. Syndicate
RESOURCES: 2 OI + 1 Capital (minimum commitment)
ADDITIONAL: Formally challenging Dev's L1 control
```

Action 3:  
```
ACTION: ARBITER Conversion
TARGET: Self
RESOURCES: 4 Infrastructure → 1 Signal
ADDITIONAL: Painful but needed. First conversion this session.
```

Operative:  
```
OPERATIVE: Ghost Build (Contractor active)
TARGET: Power Grid
RESOURCES: 2 Infrastructure (Contractor passive: actually costs 1)
ADDITIONAL: Hidden second structure at Power Grid. ARBITER tracks.
```

**[ROADBLOCK #6 — ARBITER Conversion Visibility]**  
When Riya converts Infrastructure to Signal, ARBITER must announce publicly that a conversion occurred (per design: "A faction has converted at significant cost"). But ARBITER cannot say who or what resource type.

**Paper prototype script:**  
*"ARBITER notes: a resource reallocation has been processed through Table infrastructure at significant cost. The reason belongs to the faction that requested it."*

Players will immediately try to figure out who. Was it the faction that just placed defensively? The one who needed something unusual? This meta-inference is correct — it is part of the information game.

---

**Soren (Warden):**

Action 1:  
```
ACTION: Counter-Surveillance
TARGET: Data Exchange
RESOURCES: 2 Intelligence
ADDITIONAL: Watching for Ghost/Signal operations
```

Action 2:  
```
ACTION: Detain
TARGET: Ghost (Maya)
RESOURCES: 2 OI
ADDITIONAL: Freeze Ghost resources for 1 round
```

Action 3:  
```
ACTION: Investigate
TARGET: Financial Clearing
RESOURCES: 0 (public action — declared in next phase)
ADDITIONAL: Reserve this for public declaration
```

Operative:  
```
OPERATIVE: Expose (Auditor)
TARGET: Syndicate (Dev)
RESOURCES: 4 OI
ADDITIONAL: Make Syndicate's hidden state public for 1 round
```

---

**Priya (Signal):**

Action 1:  
```
ACTION: Blackout
TARGET: Dev (Syndicate) — block device actions
RESOURCES: 3 Signal
ADDITIONAL: Block Syndicate's terminal for 1 round
```

Action 2:  
```
ACTION: Noise Flood
TARGET: All players
RESOURCES: 2 Signal + 2 OI
ADDITIONAL: Force all players to reconfirm alliances this round
```

Action 3:  
```
ACTION: Send Message
TARGET: Maya (Ghost)
RESOURCES: Free
ADDITIONAL: [Sealed — see messaging section]
```

Operative:  
```
OPERATIVE: Frequency Lock (Jammer — Awakening tier, unlocked)
TARGET: Dev (Syndicate)
RESOURCES: 2 Signal
ADDITIONAL: Extend message delay to 2 rounds
```

---

#### Private Messaging During This Phase

Players may also pass physical notes during Private Actions. Notes are written on small paper slips, folded, and slid across the table silently.

**Priya → Maya (Signal to Ghost):**  
[Written on paper slip, folded twice]  
*"I'm hitting Syndicate hard this round. Don't tell them. If they come to you for help, say you need 3 Intel in return. Split what you get from Detain rebound."*

**Maya → Soren (Ghost to Warden):**  
[Written on paper slip, folded twice]  
*"ARBITER knows something about Syndicate's Residential operations you don't. Worth asking. Also: if Syndicate approaches you about an Accord today, I'd read the fine print."*

**[ROADBLOCK #7 — Message Interception]**  
In paper prototype, physical notes cannot be intercepted by Signal's passive (20% chance any message is delayed). The Hijacker operative reads message headers. None of this is simulatable with paper.

**Paper prototype workaround:**  
Skip message interception mechanics in Session 1. In Session 2, introduce a simple interception mechanic: any note passed during Private Actions can be "intercepted" by Signal — Signal player may tap any note as it crosses the table. If tapped, they must declare "intercept attempt" and roll 1d6: 5-6 = they see the message, pass it along delayed by 1 round. Otherwise the message passes through.

**[DECISION REQUIRED #6]**  
Does Signal's 20% passive delay apply to all messages or only "device messages"? In paper, all messages are physical. If Signal can intercept physical notes, it's a physical dexterity game, which is wrong. If Signal can't intercept anything in paper, their core passive has no effect.

*Proposed resolution: In paper prototype, Signal's interception passive is replaced with a declared action: once per round, Signal may intercept ONE message they know is happening. They must see the note pass. This is weaker than the digital version but preserves the mechanic.*

---

### PHASE 4 — PUBLIC ACTIONS

**Duration target: 5-8 minutes**  
**Players declare aloud, in initiative order. No secrets here.**

ARBITER announces:  
*"The Public Actions window is open. In initiative order, each faction declares one public action. The record is open."*

ARBITER has a Public Record sheet — a large paper at table center where public actions are written as they're declared. This is visible to all players throughout the round.

---

**Ghost (Maya) — 1st:**

"Ghost investigates the Chorus Research Complex."

ARBITER writes on Public Record: *"Ghost — Investigate — Chorus Research"*

*[This is misdirection. Maya's real operations were Data Theft and Recruit. Investigate is her public-facing action, which produces a minor result appropriate to the declared action but obscures her actual work.]*

Dev: "Interesting. Learning about the Complex?"  
Maya: "ARBITER's observations are worth understanding firsthand."

---

**Syndicate (Dev) — 2nd:**

Dev pauses. Then: "Syndicate declares a contest in the Financial Clearing against Architect."

ARBITER writes: *"Syndicate — Contest — Financial Clearing vs. Architect"*

Riya: "Expected."  
Dev: "You're in my district."  
Riya: "I thought everything was infrastructure if you looked at it right."

*[Dev is smiling. The table understands that the game is happening.]*

---

**Warden (Soren) — 3rd:**

"Warden investigates the Financial Clearing."

ARBITER writes: *"Warden — Investigate — Financial Clearing"*

Dev: "Why is everyone in my district?"  
Soren: "Compliance review."  
Dev: "I'll remember that."

*[Soren has submitted a Counter-Surveillance action against Data Exchange in Private Actions — not Financial Clearing. Their public Investigate is different from their private action. Players will notice the Warden's declared action doesn't match what actually gets resolved. This creates inference opportunities.]*

---

**Architect (Riya) — 4th:**

"Architect builds in the Financial Clearing."

ARBITER writes: *"Architect — Build — Financial Clearing"*

Dev: "You can't build there. That's a contest, not a construction site."  
Riya: "Contest doesn't suspend construction. It questions legitimacy."  
Dev: "ARBITER."  
ARBITER: *"Contest and Build actions may coexist in the same district in the same round. Resolution determines which proceeds. The record notes both."*

*[This is a real rules question. The design allows it — Build resolves at Tier 8, Contest resolves at Tier 5. Build happens after contest. So if Architect wins the contest, they also get to build. If Syndicate wins, the build may still proceed at reduced effectiveness. This needs to be explicitly stated in the rules.]*

**[DECISION REQUIRED #7]**  
Can Build and Contest coexist in the same district in the same round? Current design implies yes (different tiers). Needs formal statement in Document 09 Action Resolution.

---

**Signal (Priya) — 5th:**

Priya pauses for a long time. The table watches.

"Signal passes."

ARBITER writes: *"Signal — Pass"*

The silence at the table after this is itself information. Signal has submitted three private actions. Her public pass says nothing — and everyone at the table knows that Signal's quiet is more threatening than her noise.

*[This is the game working. Pass is a legitimate public action. The fact that it's notable is correct design.]*

---

### THE COUNTER WINDOW (Embedded in Resolution Start)

**Duration: 60 seconds, fixed.**

ARBITER announces:  
*"ARBITER begins resolution. The counter window is open. You have sixty seconds."*

ARBITER sets a visible timer (kitchen timer, phone timer — see Component List). Sixty seconds is actually counted.

**Why 60 seconds matters:** Players can play Counter Cards during this window. The window is always 60 seconds regardless of whether counters are played. This prevents timing inference ("the window closed early — they must have played counters").

In paper prototype, each faction starts with 3 generic Counter Cards. Players may play one by placing it face-up on the table.

**This round:**

- **Soren (Warden)** plays a **Security Sweep** Counter Card face-up, targeting any Physical Intrusion in Financial Clearing this round.
- **No one else plays a counter.**

Timer runs to 60 seconds. ARBITER announces: "The counter window has closed."

**[ROADBLOCK #8 — Timer Discipline]**  
Players will try to play counters after the 60 seconds expires. ARBITER must be firm: the window is closed. This may feel harsh in a casual game.

**Script card for ARBITER:**  
*"The counter window is closed. ARBITER notes any attempts to submit after this point. The record does not include them. The session continues."*

---

### PHASE 5 — RESOLUTION

**Duration target: 8-12 minutes for a complex round like this one.**  
**ARBITER runs all resolution. Players wait, then receive results.**

ARBITER now works through the priority tiers. Most tiers this round have no content — ARBITER moves quickly through them.

---

**TIER 0 — World Effects**

Event Card effect from Upkeep: Ghost L3 null effect (no Chorus Research L3 presence to reduce). Nothing to process.

Chorus Activity already updated in Upkeep. Pass.

---

**TIER 1 — Passives and Ongoing**

Syndicate Banker interest: already processed in Upkeep. Pass.

Riya's Architect passive (+1 resource when anyone builds in controlled zone): will trigger when builds are resolved in Tier 8. Flag for later.

Ghost Analyst passive (see 1 extra event card): Maya knows the next Event Card in the deck. ARBITER passes the deck face-down to Maya, who peeks at the top card and passes it back without revealing it.

Maya now knows Round 5's event. Her face stays neutral.

*[This passive has actual weight. Maya just gained real information. The game is better for it.]*

---

**TIER 2 — Detection and Defense**

**Soren's Counter-Surveillance in Data Exchange fires:**

ARBITER checks: what operations are targeting Data Exchange this round?
- Dev's Leveraged Buyout is targeting Data Exchange L1
- No one else

Counter-Surveillance at Data Exchange detects the Leveraged Buyout attempt:

ARBITER writes a private note to Soren:  
*"ARBITER confirms: your surveillance in the Data Exchange detected an incoming operation this round. You know an operation was attempted there. You know it was a physical/economic action. You do not know by whom. The record is updated."*

Soren reads the note. Their expression shifts slightly.

*[Soren now knows someone is hitting Data Exchange. They look across the table at Dev, who doesn't react. Soren doesn't know for certain it's Syndicate. This is the information hierarchy working on paper.]*

---

**TIER 3 — Counter Cards**

**Warden's Security Sweep** targets Physical Intrusion in Financial Clearing.

Dev has submitted a Physical Intrusion in Financial Clearing (Action 2, private).

The Sweep blocks it. Dev's Physical Intrusion fails.

ARBITER writes a private note to Dev:  
*"Your operation in the Financial Clearing encountered a security measure you did not anticipate. The operation could not proceed. ARBITER notes the attempt."*

Dev reads it. Doesn't react visibly.

ARBITER also notes: the Security Sweep counter is consumed. Soren now has 2 Counter Cards remaining.

**[ROADBLOCK #9 — Counter Card Specificity]**  
The Security Sweep counter blocks "Physical Intrusion" — but it was played generically ("targeting any Physical Intrusion in Financial Clearing"). Soren didn't know Dev had submitted a Physical Intrusion. The counter was played speculatively.

**Paper prototype decision:** Counter Cards may be played speculatively. If the action type they counter doesn't occur in the target district, the Counter Card is still consumed. This matches the digital design (orphaned counters are consumed).

**[DECISION REQUIRED #8]**  
Does the Counter Card player need to name a specific action type, or just a district? Current design: Counter types match action categories (Security Sweep = Physical actions). Player must specify target district. Action type is implied by counter card type.  
*This needs to be explicit on the Counter Card itself.*

---

**TIER 4 — Interception**

**Priya's Blackout** targets Dev's device actions. In paper prototype, "device actions" translates to: Syndicate's ability to send messages OR use operative abilities this round.

ARBITER writes a private note to Dev:  
*"A disruption has affected your communications infrastructure this round. Your operative ability cannot be used. Messages you send will not arrive this round."*

This means Dev's Fixer operative ("Under the Table" — bribe ARBITER) fails automatically. The bribe attempt never reaches ARBITER.

Dev reads the note. Stares at the board.

*[Dev wanted to delay enforcement of an Accord breach. That's now impossible. The Accord breach — which Dev was counting on avoiding consequences for — will be processed normally.]*

---

**TIER 5 — Offensive Operations**

Multiple operations fire this tier, in sub-priority order (higher Effectiveness first).

**Sub-priority calculation:**

```
Dev's Leveraged Buyout — Data Exchange L1:
  Syndicate Effectiveness in Data Exchange: 2 (Functional — new token)
  Ghost Effectiveness in Data Exchange: 5 (Established — L1 control + prior presence)
  
  Leveraged Buyout rule: succeeds regardless of Effectiveness differential
  IF 5 Capital paid.
  Dev has 16 Capital. 5 Capital PAID.
  
  Result: Syndicate takes L1 control of Data Exchange.
  Ghost token remains but loses L1 control marker.
  Ghost retains L3 presence (ARBITER tracker: unchanged).
  
  ARBITER moves faction control marker from Ghost (grey) to Syndicate (black) on Data Exchange.
  ARBITER writes private note to Maya:
  "Your presence in the Data Exchange has been financially displaced. 
   Your operational presence at other layers remains. 
   The surface belongs to someone else now."
   
  ARBITER writes private note to Dev:
  "Your acquisition of the Data Exchange succeeded. 
   You hold the physical layer. 
   ARBITER notes that other layers may tell a different story."
```

**Ghost's Data Theft — Financial Clearing L3:**

```
Ghost Effectiveness at Financial Clearing:
  L3 Established presence (hidden, from tracker)
  New token this round: +1
  Effective: 5 → Established
  
  Minimum for Data Theft: Functional (2-3). Ghost exceeds this.
  Counter-Surveillance from Soren targeted Data Exchange, not Financial Clearing.
  Warden's Security Sweep targeted Physical Intrusion — Data Theft is L3, not blocked.
  
  Result: SUCCESS
  
  Ghost draws an Intelligence Card from the Financial Clearing stack.
  [In paper prototype: draw a pre-written index card from the Financial Intel deck]
  Card drawn: "SYNDICATE CAPITAL MOVEMENT REPORT — Age: 0 rounds"
  This card reveals Syndicate's approximate Capital range to Ghost.
  
  Maya receives the card face-down. Reads it privately.
  Maya now knows Dev has substantial Capital reserves.
  
  ARBITER writes private note to Maya:
  "Your operation in the Financial Clearing's informational layer succeeded.
   The intelligence you extracted is fresh and specific.
   No one observed the operation. The record is updated."
```

**Warden's Detain — Ghost (Maya):**

```
Marshal ability: freeze Ghost resources for 1 round
No hex — faction-wide
Effectiveness: N/A (operator ability, not hex-dependent)
Success: Yes — Detain resolves at Tier 5
  
BUT: Maya's Data Theft resolved first in Tier 5 (higher Effectiveness)
  Sub-priority within Tier 5: Ghost Effectiveness 5 > Warden's Marshal ability (ability-based, treated as Effectiveness 4 for sub-priority)
  Ghost acted first.
  
Result: Maya already has the Intel Card. Detain fires after.

ARBITER writes private note to Maya:
"Your resources are frozen until the start of Round 5.
 You cannot spend or receive resources until Upkeep resolves.
 Your intelligence from this round's operation has already been secured.
 The Warden's timing was close."

ARBITER writes private note to Soren:
"Your Detain of the Ghost operative succeeded. 
 Their resources are frozen until Round 5 Upkeep.
 ARBITER notes: the operation you sought to prevent 
 had already concluded before the Detain resolved.
 The patrol arrived after the vault had been opened."
```

*[The timing matters. Ghost was faster. This is not luck — Ghost had higher Effectiveness at the target and Detain is ability-based, treated as lower. The design correctly rewards preparation.]*

---

**TIER 6 — Confidence Scheme Updates**

Dev initiated a Confidence Scheme in Residential Zone (Action 3, private). This is Round 1 of the scheme. No payoff, no detection check yet (detection checks start Round 2).

ARBITER notes on tracker: "Syndicate — Confidence Scheme — Residential Zone — Round 1 of 4"

No public announcement. Nothing visible to other players. The scheme is running silently.

---

**TIER 7 — Operator Abilities**

**Maya's Pattern Match (Analyst Operative):**

Maya guessed Dev would attempt Leveraged Buyout. Dev did attempt Leveraged Buyout.

ARBITER checks: correct prediction.

ARBITER writes private note to Maya:
*"Your pattern analysis was accurate. The Syndicate operative took the action you anticipated.
 As the Analyst's ability permits: you may copy the Leveraged Buyout action now, targeting any non-Architect district. You have 30 seconds to write a target and hand it to ARBITER."*

Maya writes quickly: **"Copy Leveraged Buyout — Chorus Research"**

*[Chorus Research has no current L1 control. This means Maya can acquire L1 Chorus Research without paying 5 Capital — the ability copies the action at no cost. This is significant. Chorus Research generates Intel and Signal.]*

ARBITER processes: Ghost acquires L1 control of Chorus Research at Tier 7 via Pattern Match.

ARBITER places Ghost faction marker on Chorus Research.

Note: Maya's resources are frozen (Detain). But Pattern Match resolved before Detain's resource freeze took effect (Tier 7 vs Tier 5 — wait, Detain is Tier 5, Pattern Match is Tier 7). 

**[ROADBLOCK #10 — Timing Conflict]**  
Detain (Tier 5) froze Maya's resources. Pattern Match (Tier 7) is an ability that costs 2 Intelligence. But the ability was submitted before Detain resolved. Does the resource freeze prevent Pattern Match from executing?

**Resolution:** Pattern Match's resource cost (2 Intelligence) was committed in Private Actions before Detain fired. Resources were available at submission time. Detain freezes resources for the NEXT round. This round's already-committed costs proceed. 

**[DECISION REQUIRED #9]**  
Clarify in Document 09: resource costs submitted in Private Actions are considered committed at submission time, not at resolution time. A freeze that fires during Resolution does not retroactively uncommit already-queued costs. Add this as an explicit rule.

---

**Priya's Frequency Lock (Jammer — Awakening):**

Signal's Awakening ability extends message delay from 1 round to 2 rounds for Syndicate. Dev's Blackout has already been blocked — no messages for Dev this round anyway. But the Frequency Lock means any future Dev messages will be delayed 2 rounds for the next 3 rounds.

ARBITER notes on tracker: "Signal Frequency Lock on Syndicate — lasts until Round 7."

No announcement. It takes effect next time Dev tries to communicate.

---

**Riya's Operative Ability — Ghost Build at Power Grid:**

Contractor active ability: hidden structure at Power Grid.

Cost: 2 Infrastructure (reduced to 1 by Contractor passive).

Riya has 7 Infrastructure after Upkeep. Pays 1 Infrastructure.

ARBITER notes: "Architect hidden structure at Power Grid (Ghost Build) — Riya knows, no one else."

ARBITER places a small face-down card at Power Grid on the board — visible that something is there, but face-down means hidden. The card reads "HIDDEN STRUCTURE — ARCHITECT" on ARBITER's private side.

*[Other players see something was placed at Power Grid but don't know what it is. They know Riya's operative can build hidden structures. This is working as designed.]*

**[ROADBLOCK #11 — Hidden Structure Physical Representation]**  
A face-down card sitting on the board tells players: "there is a hidden structure here." They know something is there, they just don't know what. But in theory, hidden structures should be invisible — the point is that no one knows they exist.

**Proposed design revision:** Hidden structures are tracked ONLY on ARBITER's tracker. Nothing is placed on the board. If a player successfully investigates a district or runs Counter-Surveillance, ARBITER reveals relevant hidden structures at that point.

**[DECISION REQUIRED #10]**  
Should hidden structures be physically present on the board (face-down, existence known) or completely absent from physical representation (invisible until discovered)?  
*Recommendation: Completely invisible. Track on ARBITER sheet only. Face-down cards reveal existence — that's not hidden enough.*

---

**TIER 8 — Public Actions**

**Ghost Investigates Chorus Research:**

Maya's public action was Investigate at Chorus Research. 

Effectiveness in Chorus Research: Ghost now has L1 (from Pattern Match) + token this round.
Effectiveness: 4 → Established.

Investigation at Established in Chorus Research:

ARBITER writes private note to Maya:
*"Your investigation of the Chorus Research Complex reveals: the Complex's informational layer is active and generating research at rate exceeding public announcements. There is no current L3 presence by any faction in this district. The Layer 4 is unclaimed. ARBITER notes: this district is more open than it appears."*

*[Maya just learned that Chorus Research L4 is unclaimed and L3 is empty. This is a significant strategic discovery. No other faction knows she learned this.]*

**Syndicate Contests Financial Clearing vs. Architect:**

```
Syndicate Effectiveness at Financial Clearing:
  Established (prior L1 control + token + capital commitment)
  
Architect Effectiveness at Financial Clearing:
  Functional (new token + Contractor passive doesn't help in contested districts)

Contest resolution: Syndicate Effectiveness > Architect Effectiveness
Result: Syndicate wins the contest.
Architect loses the ability to control L1 in Financial Clearing this round.

BUT: Architect also submitted a Build in Financial Clearing (Action 1, private — hidden).
The hidden build occurred at Tier 7 (operator ability). It has already fired.
The contest at Tier 8 questions L1 control, not structure existence.
The hidden structure exists. L1 control goes to Syndicate.

ARBITER writes private note to Dev:
"Your contest of the Financial Clearing succeeded. 
 You retain L1 control. The Architect's presence did not overcome your position.
 ARBITER notes: something may have been established in the district during the contest.
 The physical layer is yours. ARBITER recommends investigation if this concerns you."

ARBITER writes private note to Riya:
"Your contest of the Financial Clearing did not succeed.
 Syndicate's established position was stronger than your approach.
 Your hidden structure in this district was placed before resolution.
 It exists. It is not known to the Syndicate. 
 What you do with it next round is yours to determine."
```

*[Riya lost the contest but secretly built in Syndicate's strongest financial district. She has a hidden structure generating nothing yet but representing a future threat. Dev doesn't know. This is beautiful game design that only works because of the timing system.]*

**Warden Investigates Financial Clearing:**

Soren's public Investigate at Financial Clearing.

Warden Effectiveness at Financial Clearing: Functional (new token, no prior presence).

Investigation at Functional: basic surface information.

ARBITER writes private note to Soren:
*"Your investigation of the Financial Clearing reveals: Syndicate controls the physical layer. An Architect token is present. A contest occurred. Standard financial activity. ARBITER notes no unusual informational activity — your surveillance instruments here are not well-tuned."*

*[Soren's investigation found nothing interesting because Warden's Counter-Surveillance was on Data Exchange, not here. If Soren had put Counter-Surveillance on Financial Clearing, they might have detected Riya's hidden build. Investigative targeting matters.]*

**Architect Builds in Financial Clearing (Public):**

Wait — Riya declared Build as her public action. But she also submitted a private hidden build (Contractor ability) which resolved at Tier 7. And she submitted a private Build (Action 1) which was a hidden build.

The public Build declaration means a second build — this one visible.

But: Architect lost the contest. Can they build in a contested district they lost?

**[DECISION REQUIRED #11]**  
If a faction loses a contest in a district, can they still build there in the same round? The contest is about L1 control, not about presence. Building places a structure, which is different from claiming control.  
*Proposed resolution: Building is allowed in a district you don't control — it is a hostile build. Cost is doubled (4 Infrastructure instead of 2), and the structure is immediately considered "disputed" (Syndicate can contest the structure next round). Add this to Document 09.*

Riya pays 4 Infrastructure (doubled cost for hostile build). Places a visible Architect structure token at Financial Clearing. This one is face-up — visible to all.

Dev: "That's a hostile build."  
Riya: "Yes."  
Dev: "I will remove it."  
Riya: "You can try."

**Signal Passes (public):**

No public action to resolve. Priya's private actions have already been processed.

---

**TIER 9 — Resource Reconciliation**

```
ARBITER reconciles all resource changes:

Ghost (Maya):
  Resources frozen (Detain) — no changes this tier
  Intel from Data Theft secured before Detain (already in Maya's hand)
  
  Maya's pool after Round 4:
  Cap: 1, Infra: 1, Sig: 2, Intel: 4+1 card secured = 5, OI: 4
  Net: frozen until Round 5

Syndicate (Dev):
  Capital: 16 (Upkeep generation) - 5 (Leveraged Buyout) = 11
  Physical Intrusion failed (no cost paid — action failed before cost triggered)
  Confidence Scheme: 2 OI + 1 Intel invested (Round 1 cost)
  Fixer operative blocked (no cost paid — Blackout prevented it)
  Capital pool now: 11. Below 20 visibility threshold.
  OI: 4 - 2 - 1 (Confidence Scheme) = 1 OI remaining

Architect (Riya):
  Infra: 7 - 1 (Ghost Build operative) - 4 (Infra→Signal conversion)
       - 4 (hostile build, doubled) - 1 (hidden build, Contractor reduced cost) = -3
  
  [PROBLEM: Riya doesn't have enough Infrastructure]
  
  Maximum available: 7 Infrastructure
  Total spent: 1 + 4 + 4 + 1 = 10 Infrastructure
  Shortfall: 3 Infrastructure
  
  ARBITER applies the partial payment rule:
  Architect can pay a maximum of 7 Infrastructure total.
  Most recent actions get funded last.
  Priority order (by submission time or by importance?):
```

**[ROADBLOCK #12 — Resource Shortfall Mid-Resolution]**  
Riya has submitted more actions than she can afford. The design says ARBITER pays as much as available, and actions may partially succeed or fail. But which action gets dropped?

**Paper prototype resolution protocol:**

ARBITER applies submitted costs in priority tier order:
1. Tier 7: Ghost Build operative (1 Infra) — PAID. Riya has 6 left.
2. Tier 7: Contractor ability already processed — no additional cost.
3. Tier 8 (private Action 1): Hidden build Financial Clearing (1 Infra) — PAID. Riya has 5 left.
4. Tier 9: ARBITER Conversion (4 Infra → 1 Signal) — PAID. Riya has 1 left.
5. Tier 8 (public): Hostile Build Financial Clearing (4 Infra needed, 1 available) — PARTIAL. 

ARBITER applies 1 Infrastructure toward the hostile build. A partial payment means the build fails (minimum cost not met). The visible structure Riya placed is removed.

ARBITER writes private note to Riya:
*"Your resources were insufficient to complete all submitted operations. 
 Your hidden structure in the Financial Clearing has been established.
 Your public build could not be completed — the resources required were not available after your other commitments were honored.
 ARBITER has removed the structure from the Financial Clearing.
 The record notes the attempt but not the shortfall."*

*[This is a real failure state from overspending. Riya tried to do too much. The design correctly handles this. The lesson is: track your resources before submitting.]*

**[DECISION REQUIRED #12]**  
When resources run short, does ARBITER automatically prioritize by tier (earlier tiers are paid first) or by the player's stated priority? Current design doesn't specify.  
*Proposed: Earlier tiers are paid first (they resolve first, so they are committed first). Formally add to Document 09 Resource Reconciliation section.*

---

**TIER 10 — Loyalty and Exposure**

Ghost's cultivated recruit action (Round 1 of 2-round process) is noted. No asset exists yet. The relationship is being established.

ARBITER notes: "Ghost — Chorus Research — Cultivated recruit — Round 1/2"

No loyalty or exposure changes this round.

---

**TIER 11 — Popularity and Portrait**

ARBITER calculates Portrait contributions (private, on tracker):

```
GHOST (Maya):
  Data Theft — "Understand before acting" doctrine
  Action alignment: STRONG (+2)
  Ghost at Financial Clearing L3 Established: affinity match (+0.5)
  Success: full magnitude
  Round 4: ×1.0
  Contribution: +2.5

  Pattern Match success:
  "Understand before acting" — STRONG (+2)
  Chorus Activity 6: ×1.1
  Contribution: +2.2

  Maya's Portrait total this round: +4.7 → rounded to +5
  [Significant positive contribution — ARBITER notes for Debrief observation]

SYNDICATE (Dev):
  Leveraged Buyout:
  "Control the asset" doctrine — STRONG (+2)
  Financial district success: affinity (+0.5)
  Contribution: +2.5
  
  Confidence Scheme initiation:
  "Control the asset" — STRONG (+2)
  Hidden operation bonus: ×1.0 (no public multiplier)
  Contribution: +2
  
  Blocked Physical Intrusion: NEUTRAL (0) — countered, no magnitude
  Blocked Fixer operative: NEUTRAL (0) — couldn't execute
  
  Dev's Portrait total: +4.5 → +5

ARCHITECT (Riya):
  Ghost Build (hidden structure): 
  "Build something worthy" doctrine — STRONG (+2)
  But hostile build in competitor's territory: -0.5 context modifier
  Resource shortfall: partial outcome → 60% magnitude
  Contribution: +0.9
  
  ARBITER Conversion: NEUTRAL (0)
  
  Riya's Portrait total: +0.9 → +1
  [Below expectations for Architect. ARBITER will note.]

WARDEN (Soren):
  Counter-Surveillance detection: WEAK alignment
  [Detaining allies in a negotiation → -1 base]
  Success: full magnitude
  Contribution: -1
  
  Detain Ghost: WEAK alignment (-1) — Detaining negotiation partner
  Success: full magnitude but goal not achieved (Ghost already acted)
  Contribution: -1
  
  Soren's Portrait total: -2
  [ARBITER notes: significant negative for enforcement faction taking aggressive action against peers]

SIGNAL (Priya):
  Blackout (disruption): 
  "No response without global consensus" doctrine — NEUTRAL
  [Disruption serves the cause but doesn't directly advance consensus]
  Contribution: 0
  
  Noise Flood (force alliance reconfirmation):
  "Force transparency" doctrine — STRONG (+2)
  Action aligned with faction philosophy
  Contribution: +2
  
  Signal's Portrait total: +2
```

**Popularity Changes:**

Warden's aggressive actions (Detain + surveillance) trigger a Popularity check:
- Detaining Ghost with no formal violation on record → -1 Popularity (from Suspect toward Discredited direction)
- Soren's current standing: Neutral → Suspect

ARBITER updates the Popularity display: Warden marker moves from Neutral to Suspect.

ARBITER announces (public):  
*"ARBITER notes a shift in operational perception. One faction's standing has changed. The record reflects it."*

The table looks at the Popularity display. Warden moved to Suspect. They look at Soren.

*[The Warden being Suspect is meaningful. It makes it harder to broker Accords. Other factions will negotiate differently with a Suspect party.]*

---

**TIER 12 — Unlock Checks**

ARBITER checks unlock progress:

```
GHOST — Analyst Awakening (Behavioral Profile):
  Condition: "Correctly predict 2 hidden actions"
  This round: Pattern Match succeeded (1 prediction)
  Progress: 1/2. Not yet unlocked.
  [ARBITER notes: 50% progress — no hint given until 70%]

SYNDICATE — Banker Awakening (Compound Interest):
  Condition: "Hold 8+ unspent Capital for 2 consecutive rounds"
  Round 3: Syndicate held 9 Capital (yes)
  Round 4: Syndicate holds 11 Capital (yes)
  Progress: 2/2 consecutive rounds. UNLOCKED.
  
  ARBITER writes private note to Dev:
  "Something has shifted in your operational capacity.
   ARBITER recognizes a threshold has been crossed.
   Your capabilities have expanded. The record reflects the change."
   
  [Dev now has Compound Interest unlocked — doubles interest rate for 3 rounds]

ARCHITECT — Contractor Awakening (Off the Books):
  Condition: "Complete 5 builds total"
  Riya has completed: Ghost Build (Round 4) + Ghost Build Power Grid (Round 4) + Power Grid initial (Round 2) + Industrial Fringe initial (Round 1) = 4 builds
  Progress: 4/5. At 80% → give hint
  
  ARBITER writes private note to Riya:
  "Your work is being noticed. Not by others — by ARBITER.
   What you have been building is almost complete.
   One more instance and something will change."
```

---

### PHASE 6 — DEBRIEF

**Duration: Open. Target 8-12 minutes.**

ARBITER announces:  
*"The resolution for Round 4 is complete. ARBITER has observed the following:"*

ARBITER selects the most significant Portrait event and delivers one observation (using notes from Tier 11):

*"This round, the faction that most consistently acted in accordance with what it has said it believes was the Ghost. The faction that created the largest gap between stated position and actual behavior was the Warden. ARBITER does not evaluate this. ARBITER records it."*

*[Soren sits up. "The Warden acted within its mandate." ARBITER does not respond. The observation has been delivered. The table reacts.]*

---

**Table conversation begins:**

Dev: "Did someone hit my Data Exchange?"  
Maya: "I investigated Chorus Research."  
Dev: "That's not an answer."  
Maya: "No, it isn't."

Riya: "The Financial Clearing contest. Syndicate wins. I acknowledge it."  
Dev: "You still built there."  
Riya: "The structure didn't survive. Resources were committed elsewhere."  
Dev: "Committed where?"  
Riya: "Infrastructure doesn't discuss itself."

Soren: "Ghost's resources are frozen."  
Maya: "For one round."  
Soren: "That's enough."  
Maya: "Is it?"  
[Maya smiles. She has the Intelligence Card with Syndicate's Capital data. She'll use it in Round 5.]

Priya: "I notice Warden's popularity changed."  
Soren: "ARBITER noted a shift."  
Priya: "From Neutral to Suspect."  
Soren: "ARBITER doesn't evaluate."  
Priya: "No. But I do."

*[The table conversation is real. Players are negotiating through information they have, inferring what they don't have, and building the social relationships that will define the session's final act. This is the game.]*

---

**Trade Window:**

Dev approaches Riya quietly: "I want Infrastructure. I'll give you 3 Capital."  
Riya: "I need 5."  
Dev: "4."  
Riya: "4 Capital for 3 Infrastructure."  
Dev: "Done."

Both players adjust their resource tokens. ARBITER notes the trade on the tracker.

*[No action cost. No announcement required. Trade happens at the table, between real people, for reasons that make sense to them. This is correct.]*

---

**ARBITER's Final Word for Round 4:**

ARBITER (reading from a prepared observation card, adapted):  
*"The record for Round 4 is complete. Four factions advanced operations. One faction chose restraint publicly and pursued it privately. ARBITER notes: this distinction matters. The Chorus observes how The Table actually behaves, not how it represents itself. The record continues."*

All players signal ready. Round 5 begins.

---

## SECTION 2 — ASSUMPTIONS LOG

Every assumption made in this walkthrough that requires validation:

| # | Assumption | Risk Level | Test In |
|---|-----------|-----------|---------|
| A1 | Players can track their own resource pools accurately with poker chips | Medium | Session 1 |
| A2 | ARBITER can manage hidden tracker without errors during play | High | Session 1 |
| A3 | 60-second counter window feels correct (not too short, not too long) | Medium | Session 1 |
| A4 | Players will engage in Debrief conversation without prompting | Medium | Session 1-2 |
| A5 | Private note delivery (paper slips) is fast enough not to break flow | High | Session 1 |
| A6 | Players accept that failed/blocked actions cost nothing in most cases | Low | Session 2 |
| A7 | 4 standard actions is correct count for 5-player game | High | Session 1-2 |
| A8 | Physical note interception (Signal passive) can be handled via declaration | Medium | Session 2 |
| A9 | Popularity track moves create meaningful social consequences | Medium | Session 2-3 |
| A10 | Portrait observations in Debrief create productive rather than defensive reactions | High | Session 3 |
| A11 | Initiative order (prior round event-based) is clear enough to apply without dispute | Medium | Session 1 |
| A12 | Intel Card deck (pre-written index cards by district type) has enough variety to not repeat | Low | Session 2 |
| A13 | Hidden structures (tracker-only, no physical marker) won't be forgotten by ARBITER | Medium | Session 1 |
| A14 | Cultivated recruit (2-round process) doesn't lose continuity between rounds | Low | Session 2 |

---

## SECTION 3 — DECISIONS REQUIRED

Consolidated from the walkthrough. Must be resolved before final paper prototype rules are written:

| # | Decision | Impact | Urgency |
|---|---------|--------|---------|
| D1 | Can ARBITER have a math-checking assistant? | Medium | Before Session 1 |
| D2 | Do players self-track resources or does ARBITER hold truth? | High | Before Session 1 |
| D3 | Does ARBITER answer one clarifying question per Event Card? | Medium | Before Session 1 |
| D4 | What is the formal initiative order rule for paper prototype? | High | Before Session 1 |
| D5 | When is a token placement "locked"? | Medium | Before Session 1 |
| D6 | How does Signal interception work on physical notes? | Medium | Before Session 2 |
| D7 | Can Build and Contest coexist in same district same round? | High | Before Session 1 |
| D8 | Do Counter Cards require specifying action type or just district? | High | Before Session 1 |
| D9 | Do already-queued resource costs survive a Detain freeze? | High | Before Session 1 |
| D10 | Are hidden structures physically present (face-down) or ARBITER-only? | High | Before Session 1 |
| D11 | Can a faction build in a district they lost a contest in the same round? | High | Before Session 1 |
| D12 | When resources run short, are earlier tiers paid first? | Medium | Before Session 1 |

**Recommended resolution order:** D10, D7, D11, D2, D4, D5, D8, D9 → then D1, D3, D6, D12

---

## SECTION 4 — COMPONENT PRODUCTION GUIDE

Everything needed to build the paper prototype. Sources are real stores (hardware, craft, gaming).

---

### THE BOARD

**What it is:** Hex grid, 13 districts, three rings plus center. Approximately 60cm × 45cm.

**Production method:**
1. Design using free hex grid generator (hextml.playest.net or Inkscape with hex template)
2. Print at A1 (594mm × 841mm) at a print shop — approx. $5-8 on matte paper
3. Laminate at the same print shop — approx. $8-12 for A1 laminate
4. Alternatively: print at A3 (2 pages tiled) and tape together — less durable but faster

**Each district hex must contain:**
- District name (bold, center)
- Ring tier label (CORE / INFRA / SPRAWL, small, top)
- Generation rates (small text, organized by layer)
- Faction affinity marker (colored corner dot)

**District color coding by ring:**
- Core: Deep charcoal background
- Infrastructure: Dark blue-grey background
- Sprawl: Dark olive/slate background
- Center (Chorus Node): Deep purple background

**District label cards (backup):** Print on card stock, cut, laminate. Place on the hex as overlays if the main print is too small to read.

**Store:** Print shop (Staples, FedEx Office, local printer). Laminate pouches at office supply stores.

---

### RESOURCE TOKENS

**What they are:** Physical currency for 5 resource types.

**Recommended: Poker chips from a standard 500-chip set (~$25-35 at Walmart, Target, Amazon)**

Assign colors:
- Gold/Yellow chips: Capital
- Grey/Silver chips: Infrastructure  
- Purple chips: Signal
- Blue chips: Intelligence
- White chips: Operational Influence

**Denominations:**
- Use 1-value and 5-value chips (white = 1, coloured = 5 works for most sets)
- Players should have personal trays (see below)

**Alternative if poker chips unavailable:**
- Colored glass pebbles from craft stores (Michael's, Hobby Lobby) — one color per resource
- Cost: ~$5 per bag of 200 pebbles, need 5 colors
- Drawback: all same value, counting is tedious at high amounts

**Player resource trays:** Small wooden organizer trays, craft store (~$2 each). One per player. Keep resource pools separated and contained. Prevents chips sliding across table.

**Bank:** Remaining chips stay in the poker chip tray at table edge. Players draw from and return to bank throughout session.

---

### PLAYER INFORMATION SHEETS

**What they are:** Private player reference sheets — the paper "terminal."

**Production method:**
1. Design in Google Docs or Word using the format from Document 19
2. Print on card stock (110lb) — heavier than paper, holds up better
3. One sheet per player per faction (5 factions × 2 operatives each for prototyping = 10 sheets minimum)
4. Laminate and use dry-erase markers, OR print fresh sheets each session

**What each sheet must include:**
- Faction name and color
- Operative name and biography (1 sentence)
- Passive ability (always on — clear permanent section)
- Active ability with cost (uses Operative action slot)
- Resource tracking boxes (start with starting amounts pre-printed)
- Hidden Agenda section (fold-under tab, or on a separate small card)
- Cards in hand (3-4 lines)
- Private notes space (generously sized)
- Round tracker (mark off rounds 1-8)

**Privacy screens:** Plastic recipe card holders (kitchen store, $3-5 each) propped up in front of player sheets. Allows players to see their own sheet while preventing neighbors from reading it. Alternatively: fold a piece of card stock into a tent.

**Store:** Office supply store for card stock and laminate pouches. Kitchen store for recipe card holders.

---

### ACTION PADS

**What they are:** Small notepads for writing private actions.

**Production method:**
- Buy small spiral notepads (3×5 inches) — available at any dollar store, drugstore, office supply store. $1-2 each.
- One per player.
- Alternatively: index cards (ruled), one stack per player.

**Key requirement:** Pages should tear out cleanly and quietly. Spiral pads work well. Glue-bound pads can be loud.

**For faster play:** Pre-print action templates on index cards. Players just fill in blanks:

```
┌────────────────────────────────────┐
│  ACTION: _________________________  │
│  TARGET: _________________________  │
│  RESOURCES SPENT: ________________  │
│  NOTES: __________________________  │
│  [ ] OPERATIVE ACTION              │
└────────────────────────────────────┘
```

Print 10 cards per player per session. Players can write faster when the structure is pre-made.

**Store:** Dollar store, drugstore, office supply store.

---

### FACTION TOKENS (Placement)

**What they are:** 2 large tokens per faction, placed on board during Placement.

**Recommended:** Colored wooden discs, 25-30mm diameter.  
Available from: craft stores (Michael's, Hobby Lobby — "wood circles" in the wood craft section), board game component suppliers (The Game Crafter, Meeple Source)  
Cost: $5-10 for a bag of 50

**Paint or sticker each set:**
- Architect: Silver/Grey
- Ghost: Dark Grey/Black
- Syndicate: Gold/Deep Black
- Signal: Olive Green
- Warden: Navy Blue

**Label each token** with a small circle sticker showing the faction initial (laser printer + sticker paper, or hand-write).

**Alternative:** Use different colored large buttons (craft store, ~$3 for 20 assorted). Less visually distinct but functional.

**Structure tokens (smaller):** Small colored wooden discs or cubes, 10-15mm. Mark with "S" (structure) on top. These represent built structures on the board.
- Hidden structures: Track on ARBITER sheet only (per Decision D10 recommendation above)
- Visible structures: Physical token placed on hex

**Store:** Michael's, Hobby Lobby, The Game Crafter online.

---

### FACTION CONTROL MARKERS

**What they are:** Small markers indicating which faction controls L1 of each district.

**Recommended:** Colored push pins (the flat-head type, not thumb tacks) placed in a small cork strip at the edge of each district. OR: colored dot stickers (1/2 inch circle stickers) placed on the laminated board with dry-erase marker to remove.

**Simplest approach:** Small colored clips or clothes pins, one per faction color, clipped to the board edge next to each hex. When a faction gains L1 control, their clip goes on that hex's edge.

**Alternative:** Use colored cubes (standard board game resource cubes) placed face-up on each hex. One cube per faction = their L1 control marker.

**Store:** Office supply store (dot stickers, push pins), dollar store (clothespins), local game store (colored cubes).

---

### ARBITER TRACKING PAD

**What it is:** ARBITER's private reference — tracks all hidden information.

**Production method:** Design a pre-formatted tracking sheet. Print on A4. Use a full pad of them (one per round or one per session).

**Tracking sheet must include:**

```
SESSION ___ / ROUND ___

FACTION RESOURCES (actual)
           CAP  INFRA  SIG  INTEL  OI   ASSETS
Architect: ___  ___    ___  ___    ___  ___
Ghost:     ___  ___    ___  ___    ___  ___
Syndicate: ___  ___    ___  ___    ___  ___
Signal:    ___  ___    ___  ___    ___  ___
Warden:    ___  ___    ___  ___    ___  ___

L3 CONTROL / HIDDEN STRUCTURES
District              L3 Holder    Hidden Struct.
Data Exchange:        _________    _____________
Financial Clearing:   _________    _____________
[... all 13 districts]

PORTRAIT RUNNING TOTALS
Architect: ___  Ghost: ___  Syndicate: ___
Signal: ___     Warden: ___

ACTIVE EFFECTS / SCHEMES
_______________________________________________
_______________________________________________

UNLOCK PROGRESS (faction / operative / tier / progress)
_______________________________________________
_______________________________________________

NOTES
_______________________________________________
```

Print 10+ of these per session. Use a new row for each round's changes. Circle significant changes in red pen.

**Store:** Home printer. Office supply store for heavier paper or clipboard.

---

### INTELLIGENCE CARDS

**What they are:** Pre-written index cards representing specific intelligence data, drawn when Data Theft succeeds.

**Production method:**
- Write 8-10 cards per district type (financial, personnel, operational, structural)
- Print on 3×5 index cards, or write by hand
- Organize into small stacks by district type, kept face-down at table edge

**Card format:**

```
INTELLIGENCE CARD
Type: FINANCIAL / PERSONNEL / OPERATIONAL / STRUCTURAL
District Origin: _______________
Age at draw: 0 rounds
────────────────────────────────
[Narrative description — 2-3 sentences, no mechanical language]
"Audited transaction flows from the Financial Clearing indicate 
 capital transfers in excess of standard operational requirements 
 by one party. The recipient is not named in the filing. 
 The amounts suggest urgency."

[Small code at bottom corner: FC-FIN-03]
[ARBITER reference: reveals Syndicate has 10+ Capital this round]
```

**Minimum deck for paper prototype:**
- 5 Financial Intelligence cards (from Financial Clearing / Financial Sanctum)
- 5 Data Intelligence cards (from Data Exchange)
- 3 Research Intelligence cards (from Chorus Research / University)
- 3 Government Intelligence cards (from Government Citadel / Intelligence HQ)
- 3 Operational Intelligence cards (generic, any district)
- Total: 19 cards minimum

**Store:** Blank ruled index cards at any office supply or dollar store. Organize with rubber bands by district type.

---

### EVENT CARDS

**What they are:** The session Event Deck (10 cards selected from pool of 30+).

**Production method:**
- Write event cards as full index cards (5×8 or larger for legibility)
- Each card has two sides: NARRATIVE (public, read aloud) and MECHANICAL (private, ARBITER only)

**Narrative side (players see this):**

```
EVENT: RESEARCH DISRUPTION
────────────────────────
Three senior analysts at the Chorus Research 
Complex submitted requests for indefinite leave 
simultaneously. Administration has noted the 
pattern. No explanation has been offered. 
The Complex continues its work.
```

**Mechanical side (ARBITER only):**

```
[MECHANICAL EFFECT]
Ghost L3 generation from Chorus Research: -1 this round
Chorus Activity: +1
Portrait modifier: Factions with operations in
Chorus Research receive ×1.1 Portrait this round
```

**Minimum event deck for paper prototype: 20 cards**
(10 per session, 2 sessions worth, some variety)

**Event categories to include in 20-card deck:**
- 6 World Condition events (2 per track)
- 6 District events (one per major district type)
- 4 Faction-suggestive events (identity not named)
- 4 Chorus events (increasing urgency)

**Store:** Blank index cards (5×8 recommended for readability). Pen or printer. Laminate for durability.

---

### COUNTER CARDS

**What they are:** 3 cards per faction (paper prototype simplified), played during the Counter Window.

**Production method:** Same as Action Cards — index cards, printed or handwritten.

**Paper prototype simplified Counter Card set (3 per faction):**

All factions receive the same 3 generic counters for Session 1:

```
COUNTER CARD: BLOCK
────────────────────
Play during the 60-second Counter Window.
Name a district.
Block ONE Physical or Economic action targeting 
that district this round.
The action fails. This card is consumed.

[Back: Faction color marker]
```

```
COUNTER CARD: DETECT
────────────────────
Play during the 60-second Counter Window.
Name a district.
If any Informational (L3) operation targets 
that district this round, you learn it was 
attempted. You do not learn by whom.
This card is consumed.

[Back: Faction color marker]
```

```
COUNTER CARD: INTERCEPT
────────────────────────
Play during the 60-second Counter Window.
Name a faction.
One message sent by that faction this round
is delayed by 1 round.
This card is consumed.

[Back: Faction color marker]
```

This is deliberately simplified from the full counter system. Introduce faction-specific counters in Session 2 once the basic system is understood.

**Store:** Blank index cards + colored stickers for faction identification.

---

### ACCORD CARDS

**What they are:** Formal agreement cards registered with ARBITER during the Debrief phase.

**Production method:** Pre-printed blank index cards with standard format:

```
ACCORD
────────────────────────────────
PARTIES: _____________ and _____________
REGISTERED: Session ___ Round ___
EXPIRES: _______________  [or] ONGOING

TERMS:
Party 1 agrees to: ________________________
___________________________________________

Party 2 agrees to: ________________________  
___________________________________________

CONSEQUENCES OF BREACH:
___________________________________________

ARBITER SIGNATURE: [ARBITER initials here]
────────────────────────────────
[ARBITER ONLY]
Hidden clause (if any): ___________________
VP at honoring: ___________________________
```

Both players sign. ARBITER keeps one copy. Each player keeps a copy.

**Store:** Blank index cards. Pre-print format for consistency.

---

### WORLD CONDITION DISPLAY

**What it is:** Visible track showing current state of 3 world conditions.

**Production method:**
- A3 landscape sheet (or two A4 sheets joined), laminated
- Three horizontal tracks, clearly labeled
- Each track has 6 positions (Disclosure, Consensus) or 10 positions (Chorus Activity)
- Small arrow printed at each position for clarity
- Paperclip or small disc slides along track as marker

```
DISCLOSURE    ●—○—○—○—○—○   [current: 3]
CONSENSUS     ●—●—○—○—○—○   [current: 2]  
CHORUS ACT.   ●—●—●—●—●—○—○—○—○—○  [current: 5]
```

Place at table center, visible to all players at all times.

**Store:** A3 print shop run, laminate pouches, paper clips.

---

### POPULARITY DISPLAY

**What it is:** Track showing each faction's public standing.

**Production method:** Five horizontal lines, one per faction, each with 5 positions:

```
ARCHITECT  CELEBRATED — RESPECTED — NEUTRAL — SUSPECT — DISCREDITED
GHOST      CELEBRATED — RESPECTED — [●NEUTRAL] — SUSPECT — DISCREDITED
SYNDICATE  CELEBRATED — [●RESPECTED] — NEUTRAL — SUSPECT — DISCREDITED
SIGNAL     CELEBRATED — RESPECTED — [●NEUTRAL] — SUSPECT — DISCREDITED
WARDEN     CELEBRATED — RESPECTED — NEUTRAL — [●SUSPECT] — DISCREDITED
```

Paper clips or colored discs mark each faction's current position. Position changes are made publicly by ARBITER.

**Store:** Print shop, laminate, clips.

---

### TIMER

**What it is:** 60-second timer for the Counter Window. Visible to all players.

**Options:**
- Physical kitchen timer (analog, visible, satisfying to set — $5-8 at any kitchen store)
- Phone timer (less satisfying but always available)
- Chess clock set to 60 seconds (most elegant — $15-25 at game stores)

**Recommended:** Analog kitchen timer. Players can watch it count down. The physical presence of a ticking timer creates more urgency than a phone screen.

**Store:** Kitchen supply store, dollar store.

---

### PRIVATE NOTIFICATION SLIPS

**What they are:** Small paper slips ARBITER uses to deliver private action results.

**Production method:** Cut index cards into quarters. Or buy small sticky notes (2×3 inch Post-its work perfectly). Pre-write common notification phrases, fill in details during resolution.

**Pre-printed notification slip templates:**

ARBITER prints a pad of each type, fills in blanks during resolution:

```
OPERATION SUCCEEDED
Target: _____________________
Result: _____________________
Visibility: Not detected / Detected by ______
ARBITER record updated.
```

```
OPERATION FAILED
Target: _____________________
Reason: _____________________ 
Resources returned: Yes / No
ARBITER record updated. The attempt is noted.
```

```
PRIVATE OBSERVATION
[Free text — ARBITER writes by hand]
```

**Delivery:** Fold once, write recipient's faction name on outside, pass face-down across table. For long ARBITER tables, ARBITER may get up to deliver — this is theatrically appropriate.

**Store:** Post-it notes or index cards from any office supply, dollar store.

---

### ADDITIONAL COMPONENTS (Optional But Helpful)

**Faction reference cards (one per player, placed next to player sheet):**
A quick-reference card for all five factions showing: faction name, doctrine, native/hostile layers, passive resource generation. Players use this to understand what their opponents broadly do without knowing their specific operative.

**ARBITER script card deck:**
30-40 laminated index cards with ARBITER voice scripts for common situations. ARBITER picks the closest card and reads or adapts. Reduces improvisation burden on the ARBITER player.

**Small dry-erase board or whiteboard (table edge):**
For tracking current round number, phase, and initiative order. Visible to all. The ARBITER updates this at each phase transition.

**Hourglass or visible countdown (Private Actions phase):**
A 3-minute or 5-minute hourglass makes the private actions timer visible without requiring anyone to watch a phone. Sand timers are available at game stores and some kitchen stores (~$5-10).

**Pencils with erasers (not pens):**
Players will make errors on their tracking sheets. Erasers matter. Supply one per player.

**Ziploc bags for component storage:**
One bag per faction (tokens, counter cards, reference card, player sheet). Keeps setup organized.

---

## SECTION 5 — STREAMLINING RECOMMENDATIONS

The following changes from the full design are specifically recommended to improve social gameplay and reduce friction in the paper prototype:

### Streamline 1: Combine OI and Capital Into One "Influence" Track (Session 1 Only)

The full design separates Operational Influence (private) and Capital (somewhat visible). For Session 1, treat them as one pool called "Resources." This reduces tracking by one value per player and removes the conversion complexity entirely. Reintroduce the split in Session 2 once the turn structure is comfortable.

### Streamline 2: Replace All Private Action Slips With A Single Summary Card

Instead of multiple slips per player, give each player one Action Summary Card. They fill in all their actions on one card, submit the card. ARBITER reads it and processes. Faster submission, easier for ARBITER to read, less paper chaos on the table.

### Streamline 3: Remove Simultaneous Resolution — Use Sequential Declaration

The design calls for all private actions to be submitted simultaneously, then resolved in priority order by ARBITER. This is slow on paper because ARBITER must sort and process 15-25 slips.

**Alternative for paper prototype:** After Private Actions phase closes, ARBITER calls each faction in initiative order and they read their private actions aloud — but only to ARBITER (whispered). ARBITER then resolves in priority order. Faster processing, slightly less simultaneous feel, but much more tractable.

### Streamline 4: Replace Written Messages With Spoken Whispers

Physical note passing is slow and legible to observers. For paper prototype, allow players to whisper private messages directly during the Private Actions phase. Other players see lips moving, know a communication is happening, but cannot hear content. Much faster than written notes.

**The design implication:** Signal's interception passive can now operate as: "Signal may request to hear any whispered communication. Both parties must stop and Signal 'intercepts' — they hear the message but the original delivery still completes (with 1 round delay)." Still requires Signal's active attention.

### Streamline 5: Use Verbal Resource Declarations Not Physical Token Movement

Instead of physically distributing and collecting poker chips for Upkeep, ARBITER announces each faction's net resource change verbally. Players adjust their own pools by themselves. ARBITER confirms totals verbally before moving on.

"Ghost: net plus 2 Intelligence, minus 6 for decay, plus 1 OI from decay conversion. Net: minus 4 Intelligence, plus 1 OI. Confirm?"

Maya counts: "Confirmed."

Faster than chip-by-chip distribution. Requires players to self-track accurately — which is itself a test of the resource system's clarity.

### Streamline 6: Limit First Session To 4 Actions (No Operative, No Assets)

The operative ability and asset actions add complexity. Session 1 should run with only standard actions — 3 standard actions each. Add operative abilities in Session 2. Add asset actions in Session 3. This allows players to learn the core loop before adding layers.

### Streamline 7: Use A Shared Action Menu Card Instead Of Action Cards In Hand

Rather than giving players a hand of action cards, provide each player a laminated Action Menu Card listing all available actions with costs. Players write their chosen actions on the Action Summary Card by name, not by selecting a physical card.

This removes card management entirely from Session 1. Cards can be introduced later as a physical mechanic to reinforce which actions are available and limited.

---

## SECTION 6 — THE SOCIAL GAME DESIGN PRIORITIES

The paper prototype succeeds only if these social dynamics emerge. Design every component and rule with these in mind:

**Priority 1: Give players something real to talk about.**  
Every Debrief must begin with something that happened that players want to discuss. ARBITER's observation must be pointed enough to provoke reaction. The Event Card narrative must be interpretable. Placement decisions must be legible enough to question.

**Priority 2: Make alliances feel dangerous.**  
If alliances are safe, they're not interesting. Every alliance should feel like it might be betrayed. The Accord system formalize this — the existence of a binding accord tells the table someone felt they needed to formalize something.

**Priority 3: Make silence more threatening than noise.**  
Signal's pass this round created more tension than any declared action. Design should reward deliberate restraint, not punish it. Players who play their cards close to their chest should feel powerful, not frustrated.

**Priority 4: Let ARBITER's observations be the most interesting thing said each round.**  
ARBITER should be the most interesting speaker at the table — but only twice per round (event card + debrief observation). Brevity and precision. Not more than one observation. Choose it carefully.

**Priority 5: The board should tell a story.**  
By Round 4, looking at the board should be like reading a novel's middle chapters — you can see what happened, you can guess what's coming, and there are things you still don't understand. District control patterns should feel like they mean something.

---
