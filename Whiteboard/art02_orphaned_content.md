# Art 02 Orphaned Content — S90

Stripped from Art 02 v2.0 rewrite. Content below was the canonical home in v1.1
but has no confirmed home in the current artifact set. Needs to land in Art 03,
00a, Art 07, or 10a before Art 02 v2.0 can be signed off.

**Dead pointers to fix once content is migrated:**
- Art 03 §20: "Full income tables and base generation values: Art 02a §8" → update to new home
- Art 03 §1145: "Rate table: Art 02a §8 (D02a-01)" → update to new home

---

## 1. Influence Level Thresholds → Art 03

Art 03 references IL-01 (Dominant) and IL-02 (Established) but never defines the chip minimums.

| Level | Chip Minimum | Rank Condition |
|-------|-------------|----------------|
| Dominant | 3+ | Strictly more chips than all others in district |
| Established | 2+ | In second place by chip count |
| Present | 1+ | Third place or lower by chip count |
| Absent | 0 | No chips or deployment markers |

Additional rules:
- Maximum 6 presence chips per faction per district at any time
- Deployment markers count toward chip count and toward the 6-chip limit during the Quarter placed
- Multiple factions may hold Established simultaneously (each places their own marker); up to 4–5 may coexist per district
- A faction at Absent immediately loses all structure blocks in that district (removed publicly by the player who caused the last chip removal)

**Resource generation by influence level:**

| Level | Generation |
|-------|-----------|
| Dominant | Full (×1) |
| Established | Full (×1) |
| Present | Half, round down (minimum 0) |
| Absent | Zero |
| Contested (3+ chips, tied) | 1 unit flat regardless of base value |

---

## 2. Ring Base Values → Art 03 (§20 stub needs these values)

| Ring | Base Resource Value per Quarter |
|------|--------------------------------|
| Baryo | 1 unit |
| The Mid | 2 units |
| Core | 3 units |
| Chorus Node | 0 — no resource generation |

**Affinity bonus:** When a faction holds Dominant influence in a district whose native resource matches their faction's native resource: +1 additional unit of that resource. Applies at Dominant level only. Applies in every qualifying district simultaneously (no cap on qualifying districts per Quarter).

**Structure block generation:** Each structure block generates +1 resource per Quarter. Owning player declares which resource at Upkeep, per structure block, before income is collected. Options: +1 of district's native resource OR +1 of owning faction's native resource. Choice may differ Quarter to Quarter and structure to structure. Requires at least 1 presence chip or deployment marker in district — removed immediately if faction is Absent.

**Passive generation:** Each faction generates 1 unit of their native resource per Quarter unconditionally.

| Faction | Passive | Source |
|---------|---------|--------|
| Ghost | 1 Findings | Distributed analyst network |
| The Network | 1 Exposure | Continuous broadcast operations |
| The Syndicate | 1 Capital | Background financial instrument returns |
| The Guild | 1 Capacity | Active construction and infrastructure contracts |
| The Directorate | 1 Mandate | Federal and interagency budget allocations |

---

## 3. Translation (Bank Exchange) Rate Table → Art 03

*(Was canonical at Art 02a §8 — D02a-01. Art 03 §1145 references this dead pointer.)*

Any faction may request The Translation — resource conversion via ARBITER — at any time ARBITER is not actively processing Resolution or delivering narrative. Debrief is the primary window.

| Requesting faction's presence at Chorus Node | Conversion rate |
|----------------------------------------------|----------------|
| Contested (Tension marker placed) | 5:1 |
| No presence | 4:1 |
| Present | 3:1 |
| Established | 2:1 |

- Any resource → any other resource at the applicable rate
- No action slot required
- No limit per Quarter
- Announce to ARBITER; ARBITER states the rate in The Record register; take tokens from the Reservoir directly
- Timing rule: Governing Rule 6.1b

The Contested rate is not a balancing mechanism — it is ARBITER's response to factions bringing conflict into the Chorus Node.

---

## 4. Chorus Node Benefits Table → Art 03

*(Art 03 only references Chorus Question access condition — full table not there.)*

| Presence level at Chorus Node | Benefits |
|-------------------------------|---------|
| ARBITER (constitutive — 8 tokens, Dominance Marker) | Controls Node narrative |
| Established (one faction, no tie) | Chorus Activity suppression + Portrait amplifier + Chorus Question access + 2:1 Translation rate |
| Present | Chorus Question access + 3:1 Translation rate |
| Tied at Established / Contested (Tension marker placed) | 5:1 Translation rate — no other Node benefits available |
| No presence | 4:1 Translation rate (standard) |

**Portrait amplifier:** Each Quarter a faction holds Established at the Chorus Node, their Chorus Portrait score moves further in its current direction — +1 if currently positive, −1 if currently negative. If at exactly 0 (Ambiguous), no movement. The ARBITER player moves the Portrait marker at close of Quarter per Governing Rule 5.1.

**Dominant is structurally unreachable at the Chorus Node.** ARBITER's permanent presence count is 8; human faction maximum is 6. The Dominant marker is not placed at the Chorus Node. Only one faction may hold Established at the Chorus Node at any time — if two or more factions reach 2+ chips and tie, the Tension marker is placed and all tied factions drop to Present-equivalent benefits.

**No structure blocks at the Chorus Node.** The Node's space is entirely occupied by receiving infrastructure that predates every faction's presence.

---

## 5. Portrait Scale → Art 07

*(Art 07 has TBD stubs. Full 11-band scale is here.)*

Portrait runs from −20 to +20. All factions start at 0. Eleven named states in a bell-curve distribution:

| State | Range | Width | Chorus Stance |
|-------|-------|-------|---------------|
| Resonant | +18 to +20 | 3 | This faction has become something the Chorus recognizes |
| Aligned | +13 to +17 | 5 | Behavior and doctrine have converged |
| Coherent | +8 to +12 | 5 | A consistent pattern is emerging |
| Legible | +4 to +7 | 4 | The Chorus can begin to read this faction |
| Observed | +2 to +3 | 2 | Initial signals noted. Trajectory forming |
| Ambiguous | −1 to 0 | 2 | No determination. Observation continues |
| Uncertain | −2 to −3 | 2 | Early contradictions detected |
| Dissonant | −4 to −7 | 4 | Stated doctrine and observed behavior diverge |
| Fractured | −8 to −12 | 5 | The pattern of contradiction is consistent |
| Collapsed | −13 to −17 | 5 | This faction no longer produces readable signal |
| Void | −18 to −20 | 3 | Silence. The Chorus has nothing to interpret here |

Starting position: 0, upper boundary of Ambiguous. Any scored action immediately moves a faction out of Ambiguous — positive actions into Observed (+2), negative actions into Uncertain (−2). The Ambiguous band is narrow by design.

---

## 6. Public Standing Scale → Art 03 (or 00a)

*(Art 03 has modifier values in card metadata table M-01–M-05 but not the full band definition and difficulty grid.)*

Public Standing runs from 0 to 20. All factions start at 10 (Neutral).

| State | Range | Target Modifier |
|-------|-------|----------------|
| Celebrated | 18–20 | +20 to target |
| Respected | 14–17 | +10 to target |
| Neutral | 7–13 | 0 |
| Suspect | 3–6 | −10 to target |
| Discredited | 0–2 | −20 to target |

The modifier shifts the difficulty target before the roll. Applied to all d100 rolls the faction makes across all contexts.

| Difficulty | Base Target | Celebrated (+20) | Respected (+10) | Neutral | Suspect (−10) | Discredited (−20) |
|-----------|------------|-----------------|----------------|---------|--------------|------------------|
| Automatic | No roll | No roll | No roll | No roll | No roll | No roll |
| Easy | 01–75 | 01–95 | 01–85 | 01–75 | 01–65 | 01–55 |
| Average | 01–50 | 01–70 | 01–60 | 01–50 | 01–40 | 01–30 |
| Challenging | 01–25 | 01–45 | 01–35 | 01–25 | 01–15 | 01–05 |
| Impossible | No roll | No roll | No roll | No roll | No roll | No roll |

Modifiers cannot change Automatic into a required roll or Impossible into a possible success.

**Natural drift:**

| Position | Drift per Quarter |
|----------|-----------------|
| Above 13 | −1 |
| 7 to 13 | No drift |
| Below 7 | +1 |

Applied at Quarter end after all other standing changes.

---

## 7. Residential Quarter — Public Standing Amplifier → Art 03

*(Not in Art 03 or 00a.)*

The Residential Quarter amplifies all Public Standing effects for factions with presence there, applied to every Public Standing change that faction experiences anywhere on the board.

| Influence Level in Residential Quarter | Public Standing Multiplier |
|----------------------------------------|---------------------------|
| Dominant | ×2 |
| Established | ×1.5, round toward stronger effect |
| Present | ×1.25, round toward stronger effect |
| Contested condition active | ×1 |
| Absent | ×1 |

Positive multipliers round up. Negative multipliers round up in magnitude.

---

## 8. University Perimeter — The Network's Virtual Structure → Art 03

*(Art 03 has procedure references at §7.4 but not the definitional rule.)*

The Network has a virtual structure block at University Perimeter from session start. This is not a physical structure block on the board. It:
- Cannot be demolished
- Does not count toward the 1-structure-per-faction-per-district limit
- Functions exactly like a structure block for all game purposes — income, faction modifier draw threshold, ring modifier eligibility, and any future mechanic referencing structure blocks owned

At Upkeep, The Network declares whether University Perimeter's virtual structure produces +1 Findings (district resource) or +1 Exposure (faction native resource).

Active as long as The Network has any presence (chip or deployment marker) at University Perimeter. If The Network is Absent, produces nothing that Quarter.

---

## 9. Dispatch Token Allocation ✓ Resolved S90

**Correct value:** 4 per faction player per Quarter (20 total). Art 03 §21 is authoritative.
Art 02 v1.1 had the old "Ghost=4, others=3" value — corrected in Art 02 v2.0.

---

## 10. Findings Decay → already in Art 03 ✓

Confirmed at Art 03 §12.1. No action needed.

---

## 11. Resolution Outcome (RO-xx) → Art 03 §13

*(Was in 00b §4.2 — moved here S96. Implicit in Art 03 §9.4 procedures but never enumerated as a formal reference table. Add to Art 03 §13 alongside §13.3 Base Difficulty.)*

| ID | Name | Trigger |
|----|------|---------|
| RO-01 | Succeeded | Roll ≤ threshold; success conditions apply |
| RO-02 | Failed | Roll > threshold; failure conditions apply |
| RO-03 | Voided | Operation removed in Beat 1 or Beat 2 before resolution — targeting restriction or Type A Countermeasure |
| RO-04 | Discovered | Roll outcome triggers discovery condition on card |
| RO-05 | Auto-failed | Face-down card — no roll made; zero or shortfall payment |

**Crit Flag:** Critical rolls set a `crit: true` modifier alongside the base RO-xx outcome — crit is not a standalone outcome type. Critical Success (01–05): RO-01 + crit flag. Critical Fail (96–00): RO-02 + crit flag. (L202)

---

*Created S90. Delete once content migrated to destination artifacts and dead pointers in Art 03 updated.*
