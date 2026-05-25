# 00c — Economy Manifest
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.4
**Status:** 🔄 Partially Populated — Active Reference

**Purpose:** Single-source-of-truth for all economic quantities in THE SIGNAL. Aggregates coin values, resource generation rates, starting asset values, operation costs, and modifier thresholds from across the design artifacts into one calibration reference. Primary use: balance analysis and playtesting tuning.

**Relationship to source artifacts:** Source artifacts remain canonical. This document does not define economic values — it indexes them. When a source artifact defines a cost or rate, the value lives in the source artifact; 00c registers it here for cross-system visibility. Discrepancies resolve in favor of the source artifact; flag and correct here.

**Future state:** Becomes the primary playtesting tuning tool at L1 playtest. At L2+, feeds directly into the code engine's balance configuration layer.

**Depends on:** 02a — Resource Systems: Board State; 02b — Resource Systems: Tracking; 03 — Round Structure & Gameplay; 04 — Card System (§5 blocked pending completion)

**Source versions:** 02a v1.4; 02b v1.5; 03 v1.7; 04 pending (§5 not populated)

---

## 2. Index

1. Overview (§1 above)
2. Index
3. Starting Assets & Resource Quantities
4. Resource Generation Rates
5. Card Costs & Modifier Thresholds *(blocked — Art 04 incomplete)*
6. Operation System Values
7. Balance Notes & Playtest Observations
8. Derived Cost Analysis *(blocked — Art 04 §7, §8 required)*
9. Round Income Analysis — Quarters 2–8 *(blocked — probability model required; home TBD)*

---

## 3. Starting Assets & Resource Quantities

### Starting Resources per Faction

*Source: Art 02a §8*

| Faction | Findings | Exposure | Capital | Capacity | Mandate |
|---------|----------|----------|---------|----------|---------|
| Ghost | 5 | 0 | 0 | 0 | 1 |
| The Network | 0 | 3 | 0 | 0 | 2 |
| The Syndicate | 0 | 0 | 6 | 0 | 1 |
| The Guild | 0 | 0 | 1 | 4 | 0 |
| The Directorate | 1 | 0 | 0 | 1 | 4 |

### Round 1 Totals (Starting + Round 1 Income)

*Source: Art 02a §8*

| Faction | Resource | Starting | R1 Income | R1 Total | Decay Check |
|---------|----------|---------|-----------|---------|------------|
| Ghost | Findings | 5 | 7 | 12 | Loses 2 → ends R1 with **10** |
| The Network | Exposure | 3 | 4 | **7** | No decay |
| The Syndicate | Capital | 6 | 7 | **13** | No decay |
| The Guild | Capacity | 4 | 5 | **9** | No decay |
| The Directorate | Mandate | 4 | 6 | **10** | No decay |

### Component Quantities

*Source: Art 02a §9*

| Component | Quantity |
|-----------|----------|
| Presence chips | 15 per faction (75 total) |
| Deployment markers | 2 per faction (10 total) |
| Structure blocks | 6 per faction (30 total) |
| Control flags | 21 total (1 per district) |
| Established markers | TBD — up to 4–5 per district; pending Art 11 |
| Tension markers | 6 total |
| Findings tokens | 30 |
| Exposure tokens | 30 |
| Capital tokens | 30 |
| Capacity tokens | 30 |
| Mandate tokens | 30 |
| ARBITER Dominance Marker | 1 (Chorus Node only, never removed) |

### Tracking Scales

*Source: Art 02b §6–§7*

| Track | Scale | Starting Value | Notes |
|-------|-------|----------------|-------|
| Chorus Portrait | −20 to +20 | 0 (Ambiguous) | Private — ARBITER only |
| Public Standing | 0 to 20 | 10 (Neutral) | Public — all players |

---

## 4. Resource Generation Rates

### District Base Values by Ring

*Source: Art 02a §8*

| Ring | Base Value per Quarter |
|------|----------------------|
| Baryo | 1 |
| The Mid | 2 |
| Core | 3 |
| Chorus Node | 0 — no resource generation |

### Generation Formula

*Source: Art 02a §8*

```
Generation = District Base Value × Level Modifier
           + Affinity Bonus (if applicable)
           + Structure Block Bonus (per structure block owned)
           + Passive Generation
```

### Level Modifiers

*Source: Art 02a §6, §8*

| Influence Level | Modifier |
|----------------|---------|
| Dominant | Full (×1) |
| Established | Full (×1) |
| Present | Half, round down (minimum 0) |
| Absent | Zero |
| Contested (3+ chips, tied at top) | 1 unit flat regardless of base value |

### Affinity Bonus

*Source: Art 02a §8*

+1 unit of native resource when a faction holds **Dominant** in a district whose native resource matches the faction's native resource. Dominant only. No per-session cap — applies in every qualifying district simultaneously.

*Playtest variable PT-02-02: Monitor for economic dominance at Quarter 4. See PM02 §3.*

### Structure Block Bonus

*Source: Art 02a §7*

+1 per structure block owned, per quarter at Upkeep. Owner declares at Upkeep which resource the block produces:

- **Option A:** +1 of the district's native resource
- **Option B:** +1 of the owning faction's native resource

Choice is public, declared per block, may change each quarter. Requires at least 1 presence chip or deployment marker — zero generates nothing. Not affected by Contested condition.

### Passive Generation

*Source: Art 02a §8*

1 unit of native resource per faction per quarter. Cannot be blocked, reduced, or affected by any game action.

*Playtest note: Starting value 1; calibration range under consideration 1–3 per faction. See PM02.*

| Faction | Native Resource | Passive |
|---------|----------------|---------|
| Ghost | Findings | 1/quarter |
| The Network | Exposure | 1/quarter |
| The Syndicate | Capital | 1/quarter |
| The Guild | Capacity | 1/quarter |
| The Directorate | Mandate | 1/quarter |

### Findings Decay — Ghost Only

*Source: Art 02a §8*

Checked after all spending at quarter end.

| Findings Held at Quarter End | Decay |
|-----------------------------|-------|
| 1–6 | None |
| 7–12 | Lose 2 |
| 13+ | Lose 4 |

Cannot reduce below 0. No other faction's resources decay in L1.

### Public Standing — Natural Drift

*Source: Art 02b §7*

Applied at quarter end after all other standing changes.

| Position | Drift per Quarter |
|----------|------------------|
| Above 13 | −1 |
| 7 to 13 | No drift |
| Below 7 | +1 |

### Bank Exchange — The Translation

*Source: Art 02a §8*

Any resource → any resource. No action slot required. No quarterly limit. Rate scales with requesting faction's presence at the Chorus Node at time of request.

| Presence at Chorus Node | Conversion Rate |
|------------------------|----------------|
| Established | 2:1 |
| Present | 3:1 |
| No presence | 4:1 |
| Contested (Tension marker active) | 5:1 |

### Chorus Node Presence Benefits

*Source: Art 02a §10*

| Level | Economic Benefits |
|-------|------------------|
| Established (sole) | 2:1 Translation rate + Portrait amplifier (+1 in current direction per quarter) |
| Present | 3:1 Translation rate |
| Contested | 5:1 Translation rate only |
| No presence | 4:1 Translation rate |

### Guild Portrait Bonus — Total Structures on Board

*Source: Art 02a §7*

| Total Structure Blocks on Board at Session End | Guild Portrait Bonus |
|-----------------------------------------------|----------------------|
| 1–4 | +1 |
| 5–9 | +2 |
| 10–14 | +3 |
| 15–19 | +4 |
| 20+ | +5 |

*Subject to calibration — see PM02 validation target V09.*

### Residential Quarter — Public Standing Multiplier

*Source: Art 02a §10*

Amplifies all Public Standing changes for factions with presence in the Residential Quarter (Baryo, native: Mandate).

| Influence Level in Residential Quarter | Public Standing Multiplier |
|----------------------------------------|---------------------------|
| Dominant | ×2 |
| Established | ×1.5, round toward stronger effect |
| Present | ×1.25, round toward stronger effect |
| Contested | ×1 |
| Absent | ×1 |

---

## 5. Card Costs & Modifier Thresholds

— Pending. Blocked on Art 04 completion.

*(Card costs, hand size, deck construction economics, and Burst Play threshold to be populated when C01–C35 and P01–P18 are fully locked.)*

---

## 6. Operation System Values

*Source: Art 03 §14*

### Base Difficulty Thresholds

| Difficulty | Threshold (d100, roll ≤ to succeed) |
|------------|-------------------------------------|
| Easy | 75 |
| Average | 50 |
| Challenging | 25 |

### Critical Result Bands

| Roll | Result | Condition |
|------|--------|-----------|
| 01–05 | Critical Success | Always — overrides threshold |
| 96–00 | Critical Fail | Always — overrides threshold |

*5% floor and 5% ceiling apply regardless of modifier stack.*

### Difficulty Modifier Table (M-01–M-12)

*Source: Art 03 §14*

| ID | Category | Modifier | Scope | Applied | Instance Limit | Value Type | Threshold Adjustment |
|----|----------|----------|-------|---------|----------------|------------|----------------------|
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

*All modifiers cumulative. Maximum combined penalty scenario: M-07 (−50) + M-12 (−25) + M-05 (−20) + M-11 (−15) = −110. Only Critical Success (01–05) viable.*

### Public Standing — Roll Threshold Modifier Reference

*Source: Art 02b §7*

| State | Range | Threshold Modifier | Effect on Rolls |
|-------|-------|-------------------|----------------|
| Celebrated | 18–20 | +20 | Easy: 01–95; Average: 01–70; Challenging: 01–45 |
| Respected | 14–17 | +10 | Easy: 01–85; Average: 01–60; Challenging: 01–35 |
| Neutral | 7–13 | 0 | Easy: 01–75; Average: 01–50; Challenging: 01–25 |
| Suspect | 3–6 | −10 | Easy: 01–65; Average: 01–40; Challenging: 01–15 |
| Discredited | 0–2 | −20 | Easy: 01–55; Average: 01–30; Challenging: 01–05 |

---

## 7. Balance Notes & Playtest Observations

— Pending. Populated during L1 playtesting.

---

## 8. Derived Cost Analysis

*Blocked on Art 04 §7 (card costs) and §8 (critical effects) — full card set must be locked before this table can be populated.*

**Purpose:** For each card, express the resource cost in terms of expected outcome value — not just nominal cost. A card that costs 3 Capital at Average difficulty costs 6 Capital per successful outcome on expected value. That comparison, invisible from the card itself, is the core balance signal.

**Columns per card:**

| Column | Description |
|--------|-------------|
| Card ID | Source: Art 04 |
| Nominal Cost | Resources spent to play the card |
| Base Difficulty | Easy / Average / Challenging (base threshold) |
| Success Probability | At base difficulty, no modifiers |
| Cost per Success | Nominal Cost ÷ Success Probability |
| Cost per Crit Success | Nominal Cost at 5% floor — always possible |
| Cost per Crit Fail | Nominal Cost at 5% ceiling — always possible |
| Expected Cost | Weighted average across all four outcomes at base difficulty |

**Formula (no modifiers, base difficulty):**

```
Expected Cost = Nominal Cost × (1 / base threshold)

Cost per Success   = Nominal Cost / P(success)
Cost per Crit Suc  = Nominal Cost / 0.05
Cost per Crit Fail = Nominal Cost / 0.05
```

*Modifier effects (M-01–M-12) shift probability without changing nominal cost — apply modifier stack to base threshold before computing expected cost for specific scenarios.*

**Example (placeholder — values not yet locked):**

| Card ID | Nominal Cost | Difficulty | P(success) | Cost/Success | Expected Cost |
|---------|-------------|-----------|------------|-------------|--------------|
| C01 | TBD | TBD | TBD | TBD | TBD |
| P01 | TBD | TBD | TBD | TBD | TBD |

— To be populated from Art 04 §7 and §8 once C01–C35 and P01–P18 are fully locked.

---

## 9. Round Income Analysis — Quarters 2–8

*Blocked — requires a probability model of district control state distributions. Home TBD (see PM05 00c-02).*

**Purpose:** For each faction, express expected income per quarter across a full session with min/max bounds — accounting for realistic board state distributions rather than theoretical extremes. Quarter 1 income is deterministic (§3 R1 Totals table). Quarters 2–8 are stochastic: income depends on who controls which districts, which is a function of all prior actions.

**Planned outputs:**

| Output | Description |
|--------|-------------|
| Expected income Q2–Q8 | Per faction, per quarter — weighted average across probable board states |
| Minimum income Q2–Q8 | Floor per faction per quarter (passive generation only — no district presence) |
| Maximum income Q2–Q8 | Ceiling per faction per quarter (Dominant in all affinity districts + max structures) |
| Income trajectory | How each faction's expected income shifts across a session as board state evolves |

**Why this requires a probability model:**

Quarter N income depends on the probability distribution of district control states at Quarter N — which itself depends on card play, Incursion outcomes, and opponent actions across Quarters 1 through N−1. Simple arithmetic off the base generation table (§4) produces theoretical extremes only, not expected values. Modeling options: Monte Carlo simulation of board state evolution, or a Markov chain over influence level transitions per district per quarter.

**Minimum income (deterministic — no model required):**

Passive generation is the guaranteed floor regardless of board state.

| Faction | Min Income per Quarter | Source |
|---------|----------------------|--------|
| Ghost | 1 Findings | Passive only |
| The Network | 1 Exposure | Passive only |
| The Syndicate | 1 Capital | Passive only |
| The Guild | 1 Capacity | Passive only |
| The Directorate | 1 Mandate | Passive only |

**Maximum income (deterministic — no model required):**

Theoretical ceiling: Dominant in every district of the faction's native resource ring + structure block in each + affinity bonus in each. Not achievable in play — presence chip limit (15 chips, max 6 per district) constrains simultaneous district control. Serves as a balance ceiling check only.

**Expected values (Quarters 2–8):** — Pending probability model.

**Artifact home decision (PM05 00c-02):**

Two candidates:

- **03a Layer 5** — extends the formal balance analysis already in 03a (Layer 4 = modifier stack math; Layer 5 = income probability math). Keeps all balance analysis in one artifact. 03a is a technical companion document — consistent home.
- **00d — Probability Model** — standalone reference artifact in the 00-series. Keeps economic analysis separate from the code-engine specification. More accessible to a designer reading the economy manifest.

*Resolve before Art 04 completion — this work begins immediately after the card set is locked.*
