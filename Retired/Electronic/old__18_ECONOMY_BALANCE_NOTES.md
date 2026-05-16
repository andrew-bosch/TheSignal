# THE SIGNAL — Economy Balance Notes

**Document:** 18  
**Status:** Complete (pre-playtest estimates — require calibration)

---

## Purpose

This document captures the starting economic numbers, faction economic arcs, and balance rationale in one place. These numbers are designed rationally but will require significant playtest calibration. The goal is to have internally consistent starting values that create the intended experience — tight early game, capable mid game, consequential late game — and then tune from there.

---

## Starting Resource Values — Session 1

All factions begin with approximately 11-13 resource units. This funds roughly 2 Round 1 actions plus the Operative ability. Players must choose carefully.

```
FACTION STARTING RESOURCES

ARCHITECT
  Capital:              3
  Infrastructure:       5  ← native resource
  Signal:               0
  Intelligence:         1
  Operational Influence: 3
  Assets:               0
  TOTAL:               12

GHOST
  Capital:              1
  Infrastructure:       1
  Signal:               2
  Intelligence:         5  ← native resource
  Operational Influence: 2
  Assets:               0
  TOTAL:               11

SYNDICATE
  Capital:              6  ← native resource
  Infrastructure:       2
  Signal:               0
  Intelligence:         2
  Operational Influence: 3
  Assets:               0
  TOTAL:               13

SIGNAL
  Capital:              1
  Infrastructure:       1
  Signal:               3  ← native resource
  Intelligence:         3
  Operational Influence: 3  ← secondary resource
  Assets:               0
  TOTAL:               11

WARDEN
  Capital:              2
  Infrastructure:       2
  Signal:               0
  Intelligence:         3
  Operational Influence: 5  ← native resource
  Assets:               0
  TOTAL:               12
```

### Design Rationale

Each faction starts with their native resource at 5-6 units — enough for 2-3 actions of their preferred type in Round 1. Non-native resources are at 0-3 units — enough for 1 cross-type action or conversion if urgently needed.

Signal starts at 0 for all factions except Signal faction and Ghost (who has 2 due to research access). Signal is the rarest resource and should feel rare from the first moment.

Assets start at 0 for all factions. Recruitment is a Round 1 priority for all players — the asset network must be built, not inherited.

---

## Faction Passive Generation

```
PASSIVE GENERATION PER ROUND
[Before district control — faction baseline]

ARCHITECT
  Primary:    2 Infrastructure/round
  Secondary:  1 Capital/round
  Note:       Architect's passive reflects ongoing
              contract revenue and maintenance work.

GHOST
  Primary:    2 Intelligence/round
  Secondary:  0
  Note:       Ghost's network is always listening.
              They generate through district control,
              not passive income of secondary types.

SYNDICATE
  Primary:    2 Capital/round
  Secondary:  +1 Capital if 5+ Capital unspent
              [Banker interest mechanic]
  Note:       Money makes money. Syndicate's passive
              reflects financial engine that runs
              regardless of board position.

SIGNAL
  Primary:    2 Operational Influence/round
  Secondary:  1 Signal/round
  Note:       Signal's community organizing and
              broadcast presence generates influence
              continuously. Digital infrastructure
              generates a trickle of Signal.

WARDEN
  Primary:    2 Operational Influence/round
  Secondary:  1 Intelligence/round
  Note:       Institutional authority generates
              political capital automatically.
              Surveillance infrastructure provides
              baseline intelligence.
```

---

## District Generation — Summary Tables

### Per Layer, Per Round

Districts generate resources for the faction controlling each layer. Generation is per layer controlled — a faction controlling all four layers of a district earns all four rows.

```
SPRAWL DISTRICTS

District            L1        L2          L3       L4
─────────────────────────────────────────────────────
Transit Hub         1 Infra   1 OI        2 Intel  0
Commercial Strip    2 Cap     1 Cap+1 OI  1 Intel  1 Cap
Residential Zone    0         2 OI        1 Intel  0
Media District      1 OI      2 OI        2 Intel  1 Sig
Harbor/Freight      2 Cap     1 Cap+1 Inf 1 Intel  0
University Perim.   1 Intel   1 Int+1 OI  2 Intel  2 Sig
Industrial Fringe   2 Infra   1 Inf+1 Cap 1 Intel  0

INFRASTRUCTURE DISTRICTS

District            L1        L2          L3       L4
─────────────────────────────────────────────────────
Data Exchange       1 Intel   1 Intel     3 Intel  1 Sig
Financial Clear.    2 Cap     2 Cap       2 Intel  0
Power Grid          2 Infra   1 Inf+1 OI  1 Intel  0(+4*)
Communications      1 Infra   1 OI        2 Intel  2 Sig
Civic Admin         2 OI      2 OI        1 Intel  0
Medical Complex     0         1 OI+1 Int  2 Intel  1 Sig
Transit Control     2 Infra   1 Inf+1 OI  1 Intel  1 Infra
Corporate Campus    2 Cap     2 Cap+1 OI  1 Intel  0
Research Facility   1 Intel   1 Int+1 OI  2 Intel  2 Sig

*Power Grid L4: grants special board-wide ability, not resource

CORE DISTRICTS

District            L1        L2          L3            L4
──────────────────────────────────────────────────────────
Government Cit.     3 OI      2 OI        2 Intel       1 Sig
Military Install.   2 Infra   1 OI+1 Inf  2 Intel       0
Intelligence HQ     1 OI      2 Intel     3 Intel       1 Sig
Financial Sanctum   2 Cap     3 Cap       2 Intel       0
Corporate Tower     3 Cap     3 Cap+1 OI  2 Intel       1 Cap
Chorus Research     1 Int+1OI 2 Intel     3 Int+1 Sig   3 Sig(*)

(*) Chorus Research L4 unclaimed at start — highest value position

CENTER

District            L1       L2      L3       L4
─────────────────────────────────────────────────
Chorus Node         1 Sig    1 Intel 2 Sig    ARBITER ONLY
```

---

## Faction Affinity Bonuses

When a faction controls a district in their affinity type, they receive an additional bonus beyond base generation. **Affinity bonus applies to maximum 2 districts per round** — this cap prevents exponential scaling.

```
ARCHITECT AFFINITY BONUSES
  Infrastructure zones:    +1 Infrastructure/round
  Civic zones:             +1 Infrastructure/round
  Transit zones:           +1 Infrastructure/round
  Maximum bonus:           +2 Infrastructure/round (cap)

GHOST AFFINITY BONUSES
  Data zones:              +2 Intelligence/round
  Research zones:          +1 Intelligence/round
  Communications zones:    +1 Intelligence/round
  Maximum bonus:           +2 Intelligence/round (cap)
  Note: Data Exchange gives +2 (unique double bonus)

SYNDICATE AFFINITY BONUSES
  Financial zones:         +1 Capital/round
  Commercial zones:        +1 Capital/round
  Corporate zones:         +1 Capital/round
  Maximum bonus:           +2 Capital/round (cap)

SIGNAL AFFINITY BONUSES
  Communications zones:    +1 Signal/round
  Media zones:             +1 Influence/round
  Dark zones:              +1 of any resource
  Maximum bonus:           +2 units/round (cap)

WARDEN AFFINITY BONUSES
  Government zones:        +2 OI/round (Citadel only)
  Civic zones:             +1 OI/round
  Military zones:          +1 Infrastructure/round
  Maximum bonus:           +2 OI/round (cap)
  Note: Government Citadel gives +2 (unique double bonus)
```

---

## Action Cost Reference — Complete

### Physical Layer 1

```
Physical Intrusion
  Base:           2 Infrastructure
  Sprawl ring:    +0
  Infrastructure: +1 Infrastructure
  Core ring:      +2 Infrastructure
  Chorus Node:    +4 Infrastructure
  Per security:   +1 Infrastructure per level above 2

Physical Theft
  Base:           1 Infrastructure + 1 OI
  Defended:       +1 Infrastructure
  Heavy security: +2 Infrastructure + detection risk

Build Structure — Basic
  Cost:           2 Infrastructure

Build Structure — Fortified
  Cost:           3 Infrastructure + 1 Capital

Build Structure — Hidden
  Cost:           2 Infrastructure
  [Removed Intelligence cost — concealment is
   technique, not intelligence gathering]

Contest District
  Declaration:    1 OI (public action, included in action)
  Commitment:     2 OI + 1 Capital minimum
  Can commit more to improve contest odds
```

### Social Layer 2

```
Recruit — Professional
  Cost:           2 OI + 1 Capital

Recruit — Cultivated
  Round 1:        2 OI
  Round 2:        1 OI
  [2-round process]

Recruit — Coerced
  Cost:           1 OI + 1 Intelligence

Confidence Scheme — Initiation
  Cost:           2 OI + 1 Intelligence

Confidence Scheme — Maintenance
  Cost:           1 OI per round
  Maximum:        4 rounds total

Social Engineering
  Base:           3 OI + 1 Intelligence
  Loyal target:   +2 OI
  Reliable:       +1 OI
  Wavering:       +0 (base cost)
  Critical:       -1 OI (they're nearly turned already)

Propaganda — Positive Campaign
  Base:           3 OI + 1 Political Asset action
  Without asset:  5 OI
  Duration:       2 rounds to manifest

Propaganda — Opposition Research
  Cost:           2 Intelligence + 2 OI
  Duration:       1 round

Propaganda — Disinformation
  Basic:          3 Intelligence + 2 OI
  Sophisticated:  4 Intelligence + 2 OI
  Deep (Signal):  3 Intelligence + 1 Signal

Propaganda — Controlled Leak
  Cost:           1 Intelligence Card (consumed)

Propaganda — Ideological Capture
  Cost:           2 OI per round × 3 consecutive rounds
  Total:          6 OI over 3 rounds

Crisis Management (Counter Card)
  Cost:           2 OI + 1 Political Asset action
  Without asset:  3 OI
```

### Informational Layer 3

```
Data Theft
  Base:           2 Intelligence
  Infrastructure: +1 Intelligence
  Core ring:      +2 Intelligence

Intercept (passive setup)
  Setup cost:     1 Intelligence
  Duration:       3 rounds
  [Automatic thereafter while in
   Communications-type hex at Established+]

Surveillance Install (Equipment Card)
  Cost:           1 Intelligence + Equipment Card

Plant False Data — Basic
  Cost:           3 Intelligence + 2 OI

Plant False Data — Sophisticated
  Cost:           4 Intelligence + 2 OI

Plant False Data — Deep
  Cost:           3 Intelligence + 1 Signal

Counter-Surveillance — Active
  Cost:           2 Intelligence
  Duration:       1 round

Counter-Surveillance — Passive
  Cost:           1 Intelligence per round
  [Lower detection threshold than active]
```

### Digital Layer 4

```
Hack — Basic system
  Cost:           1 Signal + 1 Intelligence

Hack — Secured system
  Cost:           2 Signal + 1 Intelligence

Hack — Core/Military (hardened)
  Cost:           3 Signal + 2 Intelligence

Deploy Autonomous Asset
  Cost:           2 Signal + Equipment Card

Deep Intercept
  Cost:           2 Signal + 1 Intelligence

Purge — Standard
  Cost:           1 Signal + 1 Intelligence

Purge — Enhanced (reveals source)
  Cost:           2 Signal + 2 Intelligence
```

### Communication and Trade

```
Send Message
  Cost:           FREE

Send Message — Encrypted
  Cost:           1 Intelligence

Propose Accord
  Cost:           1 OI

ARBITER Conversion
  Rate:           4:1 (any → any)
  Signal IN:      5:1 (Signal costs more to acquire)
  Asset Liquidation: 1 asset → 4 of capability resource type
  No action point required
  No phase restriction (except Resolution)
  No per-round limit

Player-to-Player Trade
  Cost:           FREE (no action point)
  Available:      Any phase except Resolution
```

---

## Economic Trajectory — Faction Arcs

### ARCHITECT Economic Arc

```
ROUND 1-2 [Early — Physical Foundation]
  Income:         8-10 Infrastructure/round
                  2-3 Capital/round
  Actions funded: 2 Builds + 1 Contest
  Constraint:     Cannot spy, cannot hack, limited Influence
  Strategy:       Lock down Infrastructure zones early,
                  establish physical presence before
                  opposition can displace

ROUND 3-4 [Mid — Infrastructure Established]
  Income:         10-14 Infrastructure/round
                  3-4 Capital/round
                  2-3 OI/round (civic zone control)
  Actions funded: 3-4 actions, mostly physical
  Constraint:     Signal still 0, Intelligence still thin
  Strategy:       Begin converting Infrastructure surplus
                  to other types via ARBITER (painful but
                  necessary for cross-layer operations)

ROUND 5-6 [Late Mid — Defensive]
  Income:         Full Infrastructure economy
  Awakening:      Eminent Domain typically achieved
  Actions funded: Full 4 standard actions
  Constraint:     Other factions attacking physical structures
  Strategy:       Defend what's built, pursue Ascendant unlock,
                  trade Infrastructure for Intelligence/Signal
                  to understand threats to structures

ROUND 7-8 [Final — Apex Window]
  Income:         Peak physical economy
  Apex cost:      4 Infra + 3 Influence + 2 Intel
  Challenge:      Intelligence requirement (2) requires
                  either stockpiling or 8 Intelligence
                  from other sources (8 Intel via ARBITER
                  → 2 Intel costs 10-12 OI total — very painful)
  Strategy:       Pre-position 2 Intelligence over rounds 6-7,
                  save Influence from civic zones
```

### GHOST Economic Arc

```
ROUND 1-2 [Early — Information Flood]
  Income:         8-12 Intelligence/round (quickly)
  Constraint:     Decay kicks in above 6 — MUST spend
  Strategy:       Data Theft and Pattern Match immediately,
                  trade excess Intelligence to other factions
                  for resources Ghost can't generate

ROUND 3-4 [Mid — Information Economy]
  Income:         15-20 Intelligence/round (potential)
  Decay impact:   Above 6: 25% decay → 4-5 OI from decay
                  Above 12: 50% decay → significant waste
  Constraint:     Ghost must spend 8-10 Intelligence/round
                  or waste it to decay
  Strategy:       Run 3-4 intelligence operations per round,
                  trade Intelligence aggressively,
                  build asset network for secondary income

ROUND 5-6 [Late Mid — Information Dominance]
  Income:         20+ Intelligence potential
  Awakening:      Behavioral Profile typically achieved
  Challenge:      Ghost's actions become readable — pattern
                  of intelligence operations is visible
  Strategy:       Vary operation targets to obscure patterns,
                  begin building toward Ascendant unlock,
                  leverage intelligence advantage for alliance trades

ROUND 7-8 [Final — Omniscience Window]
  Apex cost:      6 Intelligence + 2 Capital
  Capital problem: Ghost generates 0-1 Capital natively
                   Requires 8 Intelligence → 2 Capital via ARBITER
                   OR trade with Syndicate
  Strategy:       Trade Intelligence to Syndicate for Capital
                  over rounds 5-7, build toward Omniscience
```

### SYNDICATE Economic Arc

```
ROUND 1-2 [Early — Capital Dominance]
  Income:         10-14 Capital/round immediately
  Constraint:     Visible above 20 — Auditor notices
  Strategy:       Establish financial district control fast,
                  deploy Capital for early Leveraged Buyouts
                  before others are established

ROUND 3-4 [Mid — Financial Empire]
  Income:         16-22 Capital/round
  Affinity cap:   +2 Capital max from affinity bonuses
  Shadow pool:    Launderer can hide 30 Capital max
  Constraint:     Capital-rich but Signal-poor, digital blind
  Strategy:       Trade Capital for Signal (via Signal faction
                  or ARBITER), maintain shadow pool to
                  avoid Auditor detection

ROUND 5-6 [Late Mid — Leverage]
  Income:         Peak Capital economy
  Everyone owes:  Enforcer passive, Accord terms,
                  resource dependencies created
  Awakening:      Compound Interest typically achieved
  Challenge:      Other factions know Syndicate is winning
                  financially — become primary target
  Strategy:       Use financial leverage to buy protection,
                  fund allied operations, set up Monopoly Apex

ROUND 7-8 [Final — Monopoly Window]
  Apex cost:      8 Capital + 3 OI + 1 Intel
  Requirement:    "Be wealthiest player for 4 consecutive rounds"
  Challenge:      Other factions specifically try to drain
                  Syndicate resources in rounds 4-7
  Strategy:       Shadow pool is key — hidden wealth means
                  others can't track whether Syndicate is
                  actually wealthiest
```

### SIGNAL Economic Arc

```
ROUND 1-2 [Early — Digital Reach]
  Income:         5-7 Signal/round
                  4-5 OI/round
                  0 Capital, 0 Infrastructure
  Constraint:     Cannot build, cannot buy
  Strategy:       Establish hidden digital presence in
                  key infrastructure hexes immediately,
                  exploit existing hidden L4 positions
                  (Commercial Strip, Data Exchange, etc.)

ROUND 3-4 [Mid — Disruption]
  Income:         6-8 Signal/round, 5-7 OI/round
  Soft cap:       Signal decays 10%/round above 10 → must spend
  Constraint:     Physical poverty — no structures to contest with
  Strategy:       Convert Signal surplus to Influence via ARBITER
                  (4:1 painful but necessary),
                  run Blackout/Jammer operations to create
                  value through disruption

ROUND 5-6 [Late Mid — Chaos Dividend]
  Income:         Bleed effects from prior disruptions
                  generating secondary benefits
  Awakening:      Frequency Lock typically achieved
  Challenge:      Bleed effects are unpredictable —
                  Signal's own disruptions may hurt their
                  assets in affected districts
  Strategy:       Careful targeting to direct bleed toward
                  enemies, away from own assets

ROUND 7-8 [Final — Total Blackout Window]
  Apex cost:      6 Signal + 2 Infrastructure
  Infrastructure problem: Signal generates 0 Infrastructure
                   Requires 8 Signal → 2 Infrastructure via ARBITER
                   This costs 8 Signal — nearly a full round's
                   Signal income at peak
  Strategy:       Accumulate 8 Signal over rounds 6-7,
                  execute Total Blackout in Round 7 or 8
                  when it disrupts final vote preparation
```

### WARDEN Economic Arc

```
ROUND 1-2 [Early — Institutional Presence]
  Income:         8-10 OI/round immediately
                  2-3 Intelligence/round
  Constraint:     0 Signal — digital blind from start
  Strategy:       Establish jurisdiction in key districts,
                  begin Accord network early (cheap for Warden),
                  use Marshal passive to gather information
                  without spending Intelligence

ROUND 3-4 [Mid — Surveillance State]
  Income:         11-15 OI/round (affinity cap limiting)
  OI surplus:     Above 16 publicly implied — must spend
  Constraint:     Signal deficit acute — Ghost/Signal
                  operating digitally without Warden knowledge
  Strategy:       Convert OI to Signal via ARBITER (5:1 — very
                  painful: 5 OI → 1 Signal; 3 Signal costs 15 OI)
                  OR trade OI to Signal faction for Signal
                  (Signal faction will trade — they need
                  physical resources they don't have)

ROUND 5-6 [Late Mid — Control]
  Income:         Peak OI economy
  Awakening:      Jurisdiction typically achieved
  Challenge:      OI surplus creates Popularity pressure —
                  "extensive operational network" noted publicly
  Strategy:       Purge operations to expose digital intrusions,
                  use Warrant to surface hidden resource states,
                  negotiate position as enforcement authority

ROUND 7-8 [Final — Martial Law Window]
  Apex cost:      5 OI + 3 Infrastructure + 1 Signal
  The irony:      Martial Law requires Signal — the resource
                  the Warden most distrusts
  ARBITER note:   When Warden uses Martial Law, ARBITER delivers
                  an Observation noting the irony of institutional
                  control requiring digital infrastructure
  Strategy:       Accumulate 1 Signal over multiple rounds
                  (painful at 5:1) OR trade for Signal specifically
                  for this moment
```

---

## Balance Concerns — Pre-Playtest Watchlist

The following potential issues should be monitored during playtesting:

### Watch 1: Ghost Intelligence Dominance

**Concern:** Ghost generates 15-20 Intelligence/round at full control, far exceeding any other faction's primary resource generation. Decay rule prevents stockpiling but may not prevent overwhelming intelligence operations.

**Indicator of problem:** Ghost player can afford every Intelligence action every round without resource decisions.

**Tuning lever:** Reduce L3 district generation rates by 25%, OR increase Intelligence action costs, OR reduce Ghost faction passive from 2 to 1.

### Watch 2: Syndicate Capital Purchasing Everything

**Concern:** Syndicate with 20+ Capital/round can run 4 Leveraged Buyouts per round, potentially taking any non-Architect structure every round.

**Indicator of problem:** Syndicate player acquires 3+ structures via Buyout in a single round.

**Tuning lever:** Affinity cap already limits bonus. If still too powerful: add a cooldown (Leveraged Buyout once per 2 rounds per target faction) or increase the cost to 7 Capital.

### Watch 3: Warden OI Surplus Without Recourse

**Concern:** Warden generates 11-15 OI/round but OI's use cases may not absorb all of it, creating frustrating surplus.

**Indicator of problem:** Warden player consistently ends rounds with 15+ OI unspent.

**Tuning lever:** Add OI costs to Warden's investigation/detain passive capabilities (currently free), or reduce Government Citadel generation.

### Watch 4: Signal's Physical Poverty

**Concern:** Signal has 0 Capital and 0 Infrastructure. Every build action and recruitment requires ARBITER conversion from their OI/Signal at painful rates.

**Indicator of problem:** Signal player cannot participate in physical layer at all — stuck in digital operations exclusively.

**Tuning lever:** Give Signal 2 starting Capital (adjust total to 13), or add a Signal faction ability that generates 1 Infrastructure per Blackout/Jammer operation (chaos creates opportunity).

### Watch 5: Four Action Economy Overwhelm

**Concern:** 4 standard actions + 1 operative + all assets may be too many choices per round, creating decision paralysis especially for new players.

**Indicator of problem:** Private Actions phase consistently runs to timer expiry even in Round 5+.

**Tuning lever:** Reduce to 3 standard actions for competitive play, keep 4 as optional "experienced" setting. Or keep 4 but restrict asset actions to 2 per round regardless of available assets.

### Watch 6: ARBITER Conversion Frequency

**Concern:** If ARBITER conversion is used routinely (more than once per faction per round), the 4:1 rate isn't painful enough and resource specialization becomes irrelevant.

**Indicator of problem:** Players use ARBITER conversion in 50%+ of rounds.

**Tuning lever:** Add a 1 OI "access fee" for ARBITER conversion that stacks (1 OI first conversion, 2 OI second, 3 OI third). This keeps conversion available but makes it increasingly costly.

---

## Trade Economy Notes

### What Actually Gets Traded

Based on faction resource profiles, the most natural trades are:

```
NATURAL TRADE PAIRS

Architect ↔ Ghost:
  Architect gives: Infrastructure (surplus)
  Ghost gives:     Intelligence (surplus)
  Rationale:       Architect needs intel to protect structures;
                   Ghost needs physical capability for cover

Syndicate ↔ Signal:
  Syndicate gives: Capital (surplus)
  Signal gives:    Signal (surplus)
  Rationale:       Syndicate needs digital capability;
                   Signal needs physical resources to recruit

Warden ↔ Signal:
  Warden gives:    OI (surplus)
  Signal gives:    Signal (small amount)
  Rationale:       Warden needs Signal desperately;
                   Signal needs political capital for community ops

Ghost ↔ Syndicate:
  Ghost gives:     Intelligence (surplus)
  Syndicate gives: Capital (surplus)
  Rationale:       Syndicate wants financial intelligence;
                   Ghost wants to buy physical cover
```

These natural trade pairs create the game's political economy. Factions that need each other's resources have incentive to ally. Factions whose primary resources don't pair (Architect and Warden both generate non-tradeable surpluses with each other) have less economic incentive to work together.

### ARBITER Conversion as Information

The public notification on conversion:
*"Resource reallocation processed through Table infrastructure. A faction has converted at significant cost. The reason is their own."*

This tells the table:
1. Someone needed something urgently
2. They couldn't get it through normal channels (trade or generation)
3. They paid 4:1 for it — they were desperate

Sophisticated players track conversion events across rounds. A faction that converts twice in three rounds is resource-constrained and may be vulnerable.

The Ghost faction's Analyst may pattern-match these conversion events to build a picture of which faction is operating in which domain despite their nominal resource profile.

---

## Cooperative Economy Adjustments

When multiple players share a faction, the economy adjusts as follows:

```
RESOURCE GENERATION: Unchanged
  [Two players in Syndicate generate the same
   Capital as one player. The faction's economic
   engine is the same size.]

ACTION ECONOMY: Expanded
  [Two players = 6 standard actions + 2 operative
   vs one player's 4 + 1]

EFFECTIVE HOURLY ECONOMY:
  One player, 4 actions, 20 units/round:
    5 units per action available
    
  Two players, 6 actions, 20 units/round:
    3.3 units per action available
    [Each action costs more relative to generation]
    
  This creates interesting tension in co-op play:
  More actions are possible but each is more
  resource-constrained. Coordination matters more
  because both players are drawing from the same pool.
```

---

## Session Economy Summary

A complete session economic summary, tracking a typical Syndicate faction across all 8 rounds:

```
ROUND 1:
  Income:    10 Capital (starting 6 + passive 2 + 2 from control)
  Spent:     5 Capital (Leveraged Buyout) + 1 Capital (Recruit)
  End:       10 Capital remaining
  
ROUND 2:
  Income:    12 Capital (growing control) + 1 interest
  Spent:     6 Capital (two operations)
  End:       17 Capital — nearing visible threshold

ROUND 3:
  Income:    14 Capital + interest
  Spent:     5 Capital (Buyout) + 4 Capital (shadow pool)
  End:       22 Capital total (14 public, 8 shadow)
  [Launderer splits to avoid Auditor]

ROUNDS 4-6:
  Income:    16-18 Capital/round
  Spending:  10-12 Capital/round (aggressive operations)
  Shadow pool: grows to 20+ units
  
ROUND 7:
  Income:    18 Capital
  Apex prep: Saving for Monopoly — need 8 + 3 OI + 1 Intel
  End:       30+ Capital across all accounts
  
ROUND 8:
  Income:    18 Capital
  Monopoly:  8 Capital + 3 OI (traded for) + 1 Intel (ARBITER converted)
  Total spent on Apex: 8 Capital + 3 OI + 5 Capital (ARBITER: 5C→1Int)
  VERDICT: Achievable with careful planning from Round 4
```

This arc demonstrates the intended experience: tight in Round 1, capable by Round 3, consequential decisions in Rounds 6-8, Apex achievable but requiring multi-round preparation.

---
