# THE SIGNAL — Paper Prototype & Core Game Design

**Document:** 19  
**Status:** Active Design — Priority Document

---

## The Right Framing

Before the ESP32 terminals, before the laser projection, before ARBITER's voice — there is a board game. The technology serves the game. The game does not serve the technology.

This document designs THE SIGNAL as a standalone tabletop experience that works completely without any electronics. Everything that makes the game good must work on a table with cards, tokens, and paper. The technology, when added, makes good things better. It does not rescue bad mechanics.

**The test:** Could someone play this game at a kitchen table with printed components and have a genuinely compelling experience? If not, the hardware will not save it.

---

## What The Core Game Must Deliver

Before any session of THE SIGNAL, five things must be true:

1. **Every player has a secret** — something they know that no one else knows, that genuinely matters
2. **Every player needs something from someone else** — no faction is self-sufficient; cooperation is necessary
3. **Every decision has consequences** — not just for the round, but for relationships and the board
4. **The table conversation is the game** — negotiation, deception, alliance, and accusation are the primary actions
5. **The ending feels earned** — the final vote resolves something real that has been building all session

If any of these five are absent, the game is broken regardless of how good the hardware looks.

---

## Stripping Back to the Essentials

### What Can Be Cut For Paper Prototype

The full game design contains many systems. For paper prototype, the following are **suspended** until core mechanics are validated:

- Digital Layer 4 operations (requires Signal concept, rare in early sessions)
- Computer vision token tracking (physical placement is fine)
- Generative soundtrack (silence or ambient music playlist)
- ARBITER voice generation (one player reads from script cards)
- Legacy / Covenant persistence (single-session scope first)
- Founding Figures (requires multiple sessions)
- NFC card tapping (flip cards face-up instead)
- Bleed-over effects (too complex until core loop is stable)
- World Condition tracks (simplify to 3 tracks instead of 6)

### What Must Survive The Cut

These are the **irreducible core** of the game:

- Five factions with genuinely different resource types and playstyles
- Hidden private information on each player's "terminal" (paper sheet)
- Layer control system (at least L1 Physical and L3 Informational for paper)
- Action economy (standard actions + operative ability)
- Private actions submitted simultaneously, resolved by ARBITER
- Player-to-player trade without action cost
- The Table Question (ARBITER asked something significant)
- Portrait (ARBITER tracking something players can't fully see)
- Session end vote and scoring

---

## Paper Prototype Components

### Player Information Sheet (replaces terminal)

Each player has a personal reference sheet, kept private (held upright or behind a screen). This sheet is the "terminal" for paper prototype purposes.

```
╔═══════════════════════════════════════════════════════╗
║  FACTION: [GHOST]          OPERATIVE: [THE ANALYST]   ║
║  SESSION: ___    ROUND: ___    INITIATIVE: ___        ║
╠═══════════════════════════════════════════════════════╣
║  RESOURCES                 │  OPERATOR                ║
║  Capital:       ___        │  PASSIVE: See 1 extra    ║
║  Infrastructure:___        │  event card each round   ║
║  Signal:        ___        │                          ║
║  Intelligence:  ___        │  ACTIVE (1/round):       ║
║  Op. Influence: ___        │  Pattern Match —         ║
║  Assets:        ___        │  Guess hidden action,    ║
║                            │  copy if correct.        ║
╠═══════════════════════════════════════════════════════╣
║  HIDDEN AGENDA (ARBITER ONLY — fold under):           ║
║  [Correctly predict 3 actions from 2 different        ║
║   players. VP bonus: +6]                              ║
╠═══════════════════════════════════════════════════════╣
║  CARDS IN HAND                                        ║
║  1. ___________________________________               ║
║  2. ___________________________________               ║
║  3. ___________________________________               ║
╠═══════════════════════════════════════════════════════╣
║  PRIVATE NOTES / ALLIANCES / INTEL                    ║
║                                                       ║
║                                                       ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
```

**Privacy mechanism:** Fold the Hidden Agenda section under so ARBITER can read it during setup but players cannot see each other's agendas. Players keep sheets angled away from neighbors.

---

### The Board

A printed hex grid representing New Meridian. For paper prototype, a simplified version:

**Simplified board (paper prototype v1): 13 districts**

Rather than 22 districts, start with a 13-hex map that hits all three rings and contains representative district types. This reduces setup time, rules explanation, and cognitive load while preserving the layer control dynamic.

```
SIMPLIFIED BOARD — 13 DISTRICTS

CORE (3 hexes):
  Government Citadel    [Warden home — high OI]
  Corporate Tower       [Syndicate home — high Capital]
  Chorus Research       [Ghost home — high Intel, Signal L4]

INFRASTRUCTURE (4 hexes):
  Data Exchange         [Ghost affinity — high Intel]
  Financial Clearing    [Syndicate affinity — high Capital]
  Power Grid            [Architect affinity — Infra + board ability]
  Communications Hub    [Signal affinity — Signal generation]

SPRAWL (5 hexes):
  University Perimeter  [Ghost affinity — Intel + Signal]
  Media District        [Signal affinity — OI + Signal]
  Residential Zone      [Social/neutral — OI, political]
  Commercial Strip      [Syndicate affinity — Capital]
  Industrial Fringe     [Architect affinity — Infra]

CENTER (1 hex):
  Chorus Node           [Special — ARBITER controls L4]
```

**Why this works:** Each faction has a clear home district and affinity zone. The core loop is preserved. If 13 hexes proves too few for interesting territorial dynamics, expand to the full 22 in paper prototype v2.

---

### Layer System (Paper Prototype Simplification)

For the initial paper prototype, run **two layers** instead of four:

**Layer 1 — Physical (Public):** Token placement, visible to all, tracked on board  
**Layer 3 — Informational (Hidden):** Intelligence investment, tracked on private sheets

This preserves the core insight — that controlling a district can mean different things to different factions — without requiring players to track four independent control states per district from session one.

Add Layer 2 (Social) in paper prototype v2 once L1/L3 feel stable. Add Layer 4 (Digital) in prototype v3 or when moving to digital implementation.

**Layer control tracking (physical):**

```
Each district on the board has:
  — A row of 5 small circles for Layer 1 control
    (colored token placed = that faction holds L1)
  — A paper strip next to the hex for Layer 3 notes
    (ARBITER writes faction initials as intel is invested)
    Players cannot see the L3 strip without investigation
```

---

### Action Cards (replaces terminal action submission)

Each player has a set of **Action Cards** — small cards listing each action type. During the Private Actions phase, players select their actions face-down from their hand.

```
ACTION CARD FORMAT (index card, 3×5):

┌────────────────────────────────┐
│  DATA THEFT                    │
│  Layer 3 Operation             │
├────────────────────────────────┤
│  TARGET HEX: ___________       │
│  RESOURCES:  2 Intelligence    │
│              + ring modifier   │
├────────────────────────────────┤
│  EFFECT: Extract Intelligence  │
│  from district's data layer.   │
│  Success: Gain Intel Card.     │
│  Detection: Varies.            │
└────────────────────────────────┘
```

**How private actions work in paper prototype:**

1. Players select action cards from their hand, write target on a slip of paper
2. Fold the action card around the target slip — sealed, private
3. Pass to ARBITER face-down
4. ARBITER collects all, then resolves in priority order
5. Results delivered on paper slips (one per player)

This is slower than the digital version but teaches the fundamental experience: you committed to something before you know what others committed to.

---

### Resource Tokens

For paper prototype, use a simple physical representation:

```
OPTION A (fastest setup):
  Different colored poker chips per resource type
  Gold chips = Capital
  Grey chips = Infrastructure  
  Purple chips = Signal
  Blue chips = Intelligence
  White chips = Operational Influence
  
OPTION B (clearest tracking):
  Index cards per player with tally marks
  One card per resource type, erase and recount each round

RECOMMENDED: Option A for play feel, Option B as backup
The physical act of counting and moving chips reinforces
resource management more than tally marks on paper.
```

---

### ARBITER Reference Pack

The player running ARBITER needs:

```
1. PRIORITY RESOLUTION REFERENCE (one laminated card)
   Tier 0: World effects
   Tier 1: Passives and ongoing
   Tier 2: Detection and defense
   Tier 3: Counter actions
   Tier 4: Interception
   Tier 5: Offensive operations
   Tier 7: Operator abilities
   Tier 8: Public actions
   Tier 9: Resource reconciliation
   Tier 10: Loyalty and exposure
   Tier 11: Popularity and Portrait
   Tier 12: Unlock checks

2. HIDDEN INFORMATION TRACKER (private notepad)
   Per district: L3 control, hidden structures
   Per faction: actual resources, shadow pools
   Per asset: loyalty, exposure level
   Portrait running tally (all factions)

3. EVENT CARD DECK (10 cards selected per session)
   One revealed per round, read aloud (narrative side)
   Mechanical effect visible only to ARBITER

4. PRIVATE NOTIFICATION SLIPS (small paper slips)
   Pre-written common messages:
   "Your operation succeeded. [Details:]"
   "Your operation failed. The requirements were not met."
   "ARBITER has observed something about your position this round."
   "Your asset [name] is showing signs of [concern/loyalty drift]."
```

---

## Paper Prototype — Session Structure

### Before Play (15-20 minutes)

```
1. SETUP:
   Place board at table center
   Each player selects faction
   Each player selects operative (choose from 4, keep private)
   ARBITER distributes starting resources (poker chips)
   ARBITER places starting L1 control tokens (from Document 04 matrix)
   ARBITER notes starting L3 control on hidden tracker

2. DOCTRINE STATEMENT:
   Each player reads their faction's doctrine aloud.
   "The [Faction Name] believes: [doctrine statement]."
   This is public. It sets the table's expectations.

3. HIDDEN AGENDA:
   ARBITER privately shows each player their hidden agenda.
   (Fold paper, whisper, or separate card passed face-down)
   Player acknowledges receipt.
   Agenda is returned to ARBITER — player keeps the memory.

4. RESOURCE DECLARATION:
   Each player declares starting resource state:
   "Strong" / "Adequate" / "Constrained"
   (These are narrative declarations, not exact numbers)
   All are public. Honesty is optional.
```

### Round Structure (8 rounds per session)

---

#### UPKEEP (2-3 minutes, ARBITER-run)

ARBITER performs:
1. Distributes passive generation (faction passives + district control)
2. Draws and reads Event Card (narrative side only, aloud to all)
3. Applies Event Card mechanical effect (privately, to tracker)
4. Applies Intelligence decay (privately adjusts hidden Intel amounts)
5. Notes any loyalty drift on assets (private)
6. Updates World Condition tracks (publicly, on shared display)

Players do: nothing. Listen to the event card. Observe what ARBITER does.

**Paper Prototype Simplification — World Conditions:**  
Use only 3 tracks for initial testing:
- **Disclosure** (1-6): How much does the public know?
- **Consensus** (1-6): How aligned is The Table?
- **Chorus Activity** (1-10): How urgent is the response question?

Display these on a shared strip of paper at board edge, marked with a paperclip.

---

#### PLACEMENT (5-10 minutes)

ARBITER announces initiative order (based on prior round performance, or randomized for round 1).

Snake order: Forward pass, then reverse pass.

Each faction places 2 tokens on the board. Rules:
- Any hex can be targeted
- Placement is public and immediate — no secrets here
- The token going down is a signal to everyone about your intentions

**What makes Placement interesting (paper prototype must validate):**

The tension is not in the rules — it is in the reading. Where did the Syndicate just place? Are they threatening the Financial Clearing that Ghost controls? Why is the Warden placing in the Residential Zone — what do they know about what's there?

If Placement generates no table conversation, the district design needs work. ARBITER should note: did players comment on each other's placements? Did placements change the room's energy?

---

#### PRIVATE ACTIONS (4-5 minutes)

All players simultaneously prepare their private actions in writing. No talking during this phase.

**Paper prototype mechanism:**
1. Each player writes actions on paper slips (one slip per action)
2. Include: action type, target, resources committed
3. Fold slips. Pass to ARBITER when done.
4. Declare done verbally ("passed" or thumbs-up)
5. Phase closes when all players have passed or timer expires

Players may also write private messages to other players during this phase. Pass them physically across the table, face-down. Recipient reads privately. May respond in kind.

**Operative ability:** Written on a separate slip marked "OPERATIVE." Costs the Free Operative action slot, not a standard action slot.

**Asset actions:** Players who have recruited assets may take additional asset actions on separate slips. Each asset gets one action.

**What ARBITER does with the slips:**
- Sorts by action type (priority tier)
- Resolves in order
- Writes outcomes on fresh slips, returns privately
- Notes anything significant in hidden tracker
- Identifies Portrait contributions (private note)

---

#### PUBLIC ACTIONS (5-10 minutes)

In initiative order, each player declares one public action aloud.

Options:
- **Build** — place a structure in a district you have L1 presence
- **Contest** — formally challenge another faction's L1 control
- **Investigate** — learn something about a district (ARBITER reveals a narrative clue)
- **Broadcast** — make a public statement that affects PI and ARBITER's Portrait assessment
- **Pass** — do nothing publicly (this itself is information)

Declarations are logged by ARBITER. Resolution happens during Resolution phase.

**The conversation around Public Actions is the game:**

"I'm building in the Data Exchange."  
"Interesting. Why there?"  
"Infrastructure investment."  
"The Analyst already has presence there."  
"I'm aware."

This is the table talking. ARBITER should note: is this happening? Are public actions generating reaction and response? If not, something in the design is suppressing it.

---

#### RESOLUTION (5-10 minutes, ARBITER-run)

ARBITER resolves all submitted private actions in priority order, then public actions.

**Simplified resolution for paper prototype:**

Skip the precise probability tables. Use this instead:

```
EFFECTIVENESS CHECK:
  If faction has DOMINANT presence (token + prior control + assets):
    Action succeeds automatically (absent counter)
  
  If faction has ESTABLISHED presence (token + some control):
    Action succeeds (absent counter)
  
  If faction has FUNCTIONAL presence (token only):
    Roll 1d6: 1-2 = fail, 3-6 = success
  
  If faction has PERIPHERAL presence (no token, just resources):
    Roll 1d6: 1-4 = fail, 5-6 = partial success

CONFLICT (two factions targeting same thing):
  Higher effectiveness wins
  Tie: higher resource commitment wins
  Tie: ARBITER decides (favor lower portrait score, never announced)
```

**Counter actions (paper prototype):**

Each faction has 3 generic Counter Cards dealt at session start. During the 60-second window after ARBITER announces "Resolution begins," any player may play a Counter Card face-up to block one specific incoming action. Counters are consumed on use.

The 60-second window is fixed — not shortened even if all counters are played early.

---

#### DEBRIEF (open-ended, 5-15 minutes)

No rules. The game pauses and players may talk freely.

**Structured elements:**
1. ARBITER reads one observation from the round (narrative, oblique)
2. Any player may propose a Table Question (if Resonance threshold reached)
3. Players may trade, negotiate, accuse, reveal, bluff freely
4. When all players signal ready, next round begins

**What ARBITER watches during Debrief:**
- Is conversation happening organically?
- Are players referencing what happened this round?
- Is anyone claiming credit for things that didn't happen?
- Is ARBITER's observation sparking something?
- Is anyone asking ARBITER direct questions?

---

### Session End (15-20 minutes)

**The Final Vote:**

Before scoring, The Table votes on the nature of humanity's response to the Chorus. Each faction submits a position card (one of 5 pre-written position cards, one per faction stance). The balance of power as ARBITER has tracked it determines how much each position influences the final composite response.

This vote is not the primary win condition — it is the culminating fiction. The response that goes out is shaped by who controlled what.

**Scoring:**

```
PUBLIC VP:
  L1 district control at session end: 1 VP per district
  Honored accords: 2 VP per accord honored all session
  Public faction objective complete: 3 VP

HIDDEN VP (revealed after public):
  Hidden agenda completion: VP per agenda (5-10)
  Operative unlocks used this session: 1 VP per tier
  
PORTRAIT CONTRIBUTION (ARBITER reveals last):
  ARBITER reads Portrait assessment (narrative, not numbers)
  +0 to +3 VP based on Portrait score this session
  ARBITER never reveals exact Portrait calculation method

WINNER: Highest total VP
TIEBREAKER: Portrait contribution
SECOND TIEBREAKER: ARBITER's discretion (announced in-character)
```

**Chronicle (abbreviated for paper):**

ARBITER reads 3-5 sentences summarizing what happened this session from ARBITER's perspective. This is the moment for the human ARBITER to be a little creative. It should feel like a debriefing document, not a recap.

---

## Faction Playstyle — Paper Prototype Targeting

Each faction must feel different to play. Here are the essential behavioral identities that paper prototype must validate:

### THE ARCHITECT
**Core experience:** Building things everyone else eventually needs

The Architect's fun is in creating presence that generates passive income and forces other factions to work around their structures. They should feel like they're playing a long game — early rounds establishing, late rounds collecting.

**What must be true:**
- Their structures generate resources that other factions notice
- Contesting their districts feels costly
- They feel dependent on others for information (their L3 blind spot matters)
- By Round 6, they have the most physical presence on the board

**Paper prototype test:** Does the Architect player feel like they're building something? Do other players interact with Architect structures as meaningful board features?

---

### THE GHOST
**Core experience:** Knowing things no one else knows, but unable to act on everything

The Ghost's fun is in the information advantage — seeing patterns others miss, reading the table more accurately, occasionally demonstrating that they knew something before anyone else. The constraint is resource: they can't act on all their intelligence at once.

**What must be true:**
- Their L3 presence means they genuinely know things (ARBITER tells them things privately)
- They must choose what to act on — intelligence decay creates real pressure
- Other factions should occasionally realize Ghost knew something they didn't, after the fact
- Trading intelligence to other factions should feel like a meaningful decision (reveal vs. withhold)

**Paper prototype test:** Does the Ghost player have moments where they visibly know something? Do other players feel the Ghost's information advantage as a real threat?

---

### THE SYNDICATE
**Core experience:** Having money, using it as leverage, being resented for it

The Syndicate's fun is in the financial engine — Capital comes in faster than it can be spent, which creates the interesting problem of deploying it advantageously before others drain it. The Leveraged Buyout (taking structures) should feel threatening to other factions.

**What must be true:**
- Capital surplus is visible and creates real table awareness
- Other factions want Syndicate money but don't want to depend on it
- Syndicate needs things only other factions can provide (Signal, Intelligence)
- The Leveraged Buyout must feel powerful enough to be feared, limited enough not to be game-breaking

**Paper prototype test:** Do other players negotiate with Syndicate differently because of their resources? Does Syndicate feel like it has leverage without feeling like it auto-wins?

---

### THE SIGNAL
**Core experience:** Creating chaos as a political act, being operationally unpredictable

The Signal's fun is in disruption — their actions create ripple effects, their presence is felt through interference, and their physical poverty forces creative play. They should feel like the faction that makes other factions nervous because their behavior doesn't follow economic logic.

**What must be true:**
- Their Blackout/disruption operations genuinely affect other players
- Their lack of Capital and Infrastructure forces reliance on trade or disruption-based resource acquisition
- Other factions aren't sure what Signal will do next
- Their wins should feel subversive — succeeding despite resources, not through them

**Paper prototype test:** Does the Signal player generate unpredictability? Do other factions factor Signal's potential disruptions into their plans?

---

### THE WARDEN
**Core experience:** Being the institutional authority, seeing everything, being resented for seeing everything

The Warden's fun is in enforcement — they know about rule violations, they can formalize agreements, they can constrain other factions through oversight. Their OI surplus gives them financial weight in the social layer. Their Signal blind spot is a genuine strategic constraint.

**What must be true:**
- Their passive notifications (knowing when rules are broken) give them real information
- Other factions have a reason to want Warden's cooperation (binding accords)
- Other factions resent Warden's surveillance enough to try to work around it
- Their inability to see L4 creates a specific vulnerability that other factions exploit

**Paper prototype test:** Does the Warden feel like an authority figure at the table? Do other factions make decisions partly based on what Warden can and can't see?

---

## The Critical Mechanical Questions

These are the specific things paper prototype must answer. For each, there is a hypothesis and a falsification condition.

### Q1: Is 4 standard actions the right number?

**Hypothesis:** 4 actions is enough for meaningful choices without decision paralysis.

**What to observe:**
- Private Actions phase: how long does it actually take?
- Do players use all 4 actions most rounds?
- Do players ever feel they had nothing good to do with an action?

**Falsification:**
- If average Private Actions phase > 5 minutes in rounds 4+, consider reducing to 3
- If players regularly have 2+ actions they feel forced to waste, consider reducing to 3
- If players consistently feel they can't do everything they want, 4 is correct

**Calibration threshold:** If 2 of 3 sessions show Private Actions averaging over 5 minutes, reduce to 3 standard actions and retest.

---

### Q2: Does the two-resource-type trade dynamic emerge naturally?

**Hypothesis:** Factions will naturally seek out their complementary trade partner (Ghost↔Architect, Syndicate↔Signal, Warden↔Signal) without explicit rules requiring it.

**What to observe:**
- Which trades actually happen?
- Do they match the predicted pairs?
- Do players reach out for trades or wait to be asked?

**Falsification:**
- If no trades happen in 3 consecutive sessions, something is suppressing trade (action cost? no incentive? lack of mechanism?)
- If only Syndicate trades (money for everything), non-Capital resources may not be scarce enough

---

### Q3: Does the layer system create real decisions?

**Hypothesis:** Knowing that a district can be controlled at L1 (visible) OR L3 (hidden) creates genuine strategic differentiation.

**What to observe:**
- Do players intentionally invest in L3 control of districts?
- Does L3 control surprise anyone when revealed?
- Do players make decisions based on the hidden layer system?

**Falsification:**
- If no player intentionally invests in L3 control before Round 4, L3 mechanics need to be more legible
- If L3 reveals never surprise anyone, the hidden information isn't actually hidden

---

### Q4: Does the Debrief generate real table conversation?

**Hypothesis:** The open Debrief phase will produce genuine negotiation and social dynamics without prompting.

**What to observe:**
- Does conversation start immediately after ARBITER's observation?
- What topics arise organically (accusations, alliances, questions to ARBITER)?
- Does the Debrief feel like a part of the game or an administrative pause?

**Falsification:**
- If Debrief is consistently silent and players just declare "ready" immediately, something needs to prompt conversation — either a forced Debrief element or a mechanical reason to talk

---

### Q5: Does the portrait system produce meaningful session arcs?

**Hypothesis:** ARBITER tracking Portrait contributions (doctrine alignment) creates a secondary narrative that players feel even if they can't see the score.

**What to observe:**
- Does ARBITER's portrait observation at Debrief land? Do players react to it?
- Do players make decisions that seem to reflect their doctrine?
- At session end, does the Portrait reveal feel like it reflects what actually happened?

**Falsification:**
- If players ignore the Portrait observation consistently, the delivery mechanism needs work
- If the Portrait score at session end surprises no one (too obvious) or everyone (too opaque), recalibrate

---

### Q6: Does the Table Question feel earned?

**Hypothesis:** When the Table Question window opens (if it opens), asking ARBITER something publicly will feel like a significant moment.

**What to observe:**
- Does Resonance threshold get crossed in most sessions?
- When the window opens, do players engage with it earnestly?
- Does ARBITER's response feel meaningful and true?

**Falsification:**
- If the window never opens in 3 sessions, Resonance thresholds are too high or Resonance triggers aren't firing
- If the window opens but players don't ask (fear of revealing interest, or don't care), the incentive structure needs work

---

## Simplified Faction Starting Positions (Paper Prototype)

For paper prototype, use these slightly simplified starting resources. The full tables from Document 18 can be introduced once economy is validated.

| Faction | Cap | Infra | Signal | Intel | OI | Starting L1 Presence |
|---------|-----|-------|--------|-------|-----|----------------------|
| Architect | 3 | 5 | 0 | 1 | 2 | Industrial Fringe, Power Grid |
| Ghost | 1 | 0 | 1 | 5 | 2 | University Perimeter, Data Exchange |
| Syndicate | 5 | 1 | 0 | 2 | 3 | Commercial Strip, Financial Clearing |
| Signal | 1 | 0 | 3 | 2 | 3 | Media District, Communications Hub |
| Warden | 2 | 2 | 0 | 2 | 5 | Government Citadel, Residential Zone |

**Starting L3 presence (ARBITER tracks privately):**

| Faction | L3 Presence (Hidden) |
|---------|----------------------|
| Ghost | Data Exchange, University Perimeter, Financial Clearing |
| Warden | Residential Zone, Communications Hub |
| Signal | Media District (hidden L3 alongside Ghost) |

This creates the first paper prototype hidden information state. Players know their own L3. They do not know others'.

---

## The ARBITER Stand-In Role in Paper Prototype

In the paper prototype, one person plays ARBITER. This is not a game master in the traditional sense — they are not the antagonist and they are not omnipotent. They are a referee who also plays the role of ARBITER the character.

### Who Should Be ARBITER

The ideal ARBITER stand-in for early sessions:
- Has read all design documents
- Is comfortable with ambiguity (some situations won't have clear rulings)
- Can read the table and gauge when to add narrative vs. when to stay quiet
- Is willing to make a call and move on, noting it for post-session discussion

ARBITER should **not** be the most experienced tabletop gamer at the table — that person should be playing. ARBITER should be someone who derives satisfaction from facilitating others' experience.

### ARBITER's Voice (Paper Prototype)

In paper prototype, ARBITER speaks from a set of voice script cards. These are short text prompts that capture ARBITER's register.

**Session opening card:**
> *"The Table convenes. New Meridian awaits. The Chorus continues. ARBITER is ready. The record begins."*

**Observation delivery card (generic):**
> *"ARBITER has been watching this round. [Read observation from tracker notes.] The record reflects this. ARBITER continues."*

**Private notification card (failure):**
> *"Your operation could not be completed. The requirements were not met. ARBITER notes the attempt."*

**Private notification card (success, undetected):**
> *"Your operation succeeded. [Deliver result.] The record is updated. No other faction has been informed."*

**Table Question window card:**
> *"The Table has produced something worth asking about. The question window is open. It closes at the end of this Debrief."*

**Table Question response card:**
> *"The Table has asked. ARBITER will answer in the manner ARBITER answers: truthfully, and insufficiently."*
> [Read prepared response from tracker notes]

**Founding Figure card (if applicable in extended play):**
> *"[Name]'s work at this Table is complete. Not concluded — complete. There is a difference. The record will preserve what was accomplished here."*

These cards should be printed on index cards, laminated, and kept in ARBITER's reference stack.

---

## Paper Prototype Test Protocol — Three Sessions

### Session 1: Rules Learning

**Goal:** Get through a complete session. No optimization, no winning. Just learn the rhythm.

**Configuration:**
- 4 players (leave one faction as Ambient Power for simplicity)
- 6 rounds (not 8 — allows session to complete in under 3 hours while learning)
- Simplified resolution (no probability rolls — just effectiveness check pass/fail)
- No asset actions (introduce in Session 2)
- Skip the Table Question mechanic (introduce in Session 3)

**Post-session focus:**
- Did everyone understand their action options?
- Were there rules moments that required stopping to clarify?
- What felt confusing vs. what felt natural?
- Roughly how long did each phase take?

**Do not change anything based on Session 1.** Just note. You need to see the game before tuning it.

---

### Session 2: Mechanics Pressure Test

**Goal:** Push the systems. Play to win. See what breaks.

**Configuration:**
- 5 players (all factions)
- 8 full rounds
- Full resolution including probability rolls
- Asset actions enabled
- Full resource economy (all starting resources, all generation)

**Post-session focus:**
- Economy balance (Watch items 1-4 from Document 18)
- Action count (Watch item 5)
- ARBITER conversion frequency (Watch item 6)
- Did any faction feel completely unable to act?
- Did anyone win by a margin that felt unfair?

**After Session 2:** Review Watch item data. Make at most ONE change to economy (one number). Document the change and reason.

---

### Session 3: Narrative and Social Test

**Goal:** Experience the game as a social and narrative experience. Table conversation quality.

**Configuration:**
- 5 players (all factions)
- 8 full rounds
- All mechanics enabled including Table Question
- Introduce 2-3 bleed effects from high-drama events
- ARBITER attempts full narrative voice (reads Portrait observations, delivers Chronicle at end)

**Post-session focus:**
- Did the Debrief generate real conversation?
- Did the Table Question feel significant if it occurred?
- Did the Portrait reveal at session end feel meaningful?
- Did anyone feel like ARBITER's observations reflected what actually happened?
- Would you want to play Session 2 of a campaign? (The legacy question)

**After Session 3:** Decide whether the core game is working. If yes, proceed to digital prototype. If no, identify the specific broken element and iterate.

---

## What Moves to Technology, and When

The technology exists to solve specific problems that paper creates:

| Paper Problem | Technology Solution | Priority |
|--------------|---------------------|----------|
| Information hiding is cumbersome (physical screens, whispers) | Terminals enforce information scope automatically | HIGH |
| ARBITER stand-in is fatiguing for one person | ARBITER server handles all resolution deterministically | HIGH |
| Private message passing is slow | WebSocket messaging is instant | MEDIUM |
| Resource tracking is error-prone | Server tracks exact values | MEDIUM |
| Layer 4 (digital) operations are hard to simulate | Server makes L4 real | MEDIUM |
| Board state updates require physical token movement | CV + projection updates automatically | LOW |
| ARBITER voice requires a skilled stand-in | Claude API + voice synthesis | LOW |
| Portrait tracking requires ARBITER attention | Server calculates automatically | LOW |
| Cross-session persistence is manual | SQLite event log | LOW |

**The high-priority items** should move to technology first — they make the game better mechanically. The low-priority items are experience enhancements that assume the game is already good.

**The rule:** Technology earns its place by solving a real problem from paper playtesting, not by assuming a problem exists.

---

## Indicators That The Core Game Is Working

After three paper prototype sessions, these are the green lights to proceed:

- Players reference specific things that happened earlier in the session when making decisions in Round 6+
- At least one player was genuinely surprised by the scoring reveal
- The Debrief phase generated at least one heated moment per session
- ARBITER's Portrait observation landed — players nodded or pushed back
- At least one trade happened that wasn't obviously in both parties' best interest
- Someone tried to lie and the lie mattered
- Someone asked ARBITER a direct question during Debrief
- Players wanted to play Session 2 before leaving

**Red lights that require iteration before proceeding:**

- Private Actions phase feels like a formality (players feel their choices don't matter)
- No faction feels clearly different from others
- Debrief is always short and transactional
- Syndicate wins every session by a large margin (or never wins)
- Players feel they had no meaningful decision points in their faction's weak areas
- The final vote feels disconnected from what happened in the session

---

## Living Document Note

This document should be updated after each paper prototype session with:
- Specific findings for each Critical Mechanical Question
- Watch item data
- Changes made and rationale
- ARBITER observations about table dynamics

The goal is to arrive at digital development with a core game that has been **observed working**, not theorized to work.

---
