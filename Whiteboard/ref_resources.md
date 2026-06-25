# Reference — Resource System (Art 02 §6–§9)
*Load when: resource mechanics, generation, conversion, structure blocks, Contested districts, starting positions.*

---

## Generation Formula

```
Generation = District Base Value × Level Modifier
           + Affinity Bonus (if applicable)
           + Structure Block Bonus (per structure block owned)
```

District base values: Baryo = 1 · The Mid = 2 · Core = 3 · Chorus Node = 0.

Level modifiers: Dominant = full + affinity · Established = full · Present = half (round down) · Absent = 0 · Contested = flat 1 (regardless of chip count).

---

## Affinity Bonus

+1 additional unit when: (a) faction holds Dominant AND (b) district's native resource matches faction's native resource. Applies in every qualifying district simultaneously. Dominant only. (Playtest variable PT-02-02.)

---

## Structure Block Mechanics

Each structure block generates +1/Quarter. Owner declares publicly at Upkeep (before income collected), per block:
- **Option A:** +1 district's native resource
- **Option B:** +1 faction's native resource

Choice may differ Quarter to Quarter and block to block. Key lever: a Directorate structure block in a Findings district can produce Mandate instead — in-place cross-resource conversion without The Translation. Structure generation is **not** affected by the Contested condition. Structures survive any influence level except Absent. Structure blocks also gate modifier card draws (draw thresholds in design_reference.md).

---

## Contested District — Full Mechanics

Contested = two or more factions tie at 3+ chips. **Second place wins** — any faction at 2+ chips not in the tie holds Established and generates full base value, more than tied factions generating flat 1. Tied factions also lose Dominant-level structure defense (drops to Average). Structure block generation unaffected by Contested.

---

## The Translation (Resource Conversion)

Available during Debrief and between phases. No action slot; no per-Quarter limit. Rate scales with Chorus Node presence:

| Faction's Node influence | Rate |
|--------------------------|------|
| None | 4:1 |
| Present | 3:1 |
| Established | 2:1 |
| Contested (Tension marker placed) | 5:1 |

The 2:1 rate at Established is a major strategic lever — rewards holding the Node beyond its Portrait/suppression benefits.

---

## Findings Decay

Applied at Quarter end after all other changes:

| Findings held | Decay |
|---------------|-------|
| 1–6 | None |
| 7–12 | Lose 2 |
| 13+ | Lose 4 |

Ghost starts Q1 with 12 Findings (5 reserves + 7 income) and loses 2 immediately (ends at 10). Unspent Findings carry forward and combine with next Quarter's income — risk of hitting higher bracket compounds.

---

## Dispatch Tokens — Capacity, Not Resource

Not resources. Per-Quarter operational capacity drawn from The Backlog (shared public pool). Ghost: 4 · All others: 3. Covert operations and public acts each cost 1 token. Pass requires none. Tokens return to The Backlog at Quarter close — they do not accumulate. A faction that burns all tokens in Month 1 can only Pass in Month 2.

---

## Chorus Node — Special Economics

Factions cannot reach Dominant (ARBITER holds 8 tokens; faction max is 6). Maximum = Established; only one faction may hold it (tie at 2+ = both drop to Present-equivalent). Benefits for Established holder: Chorus Activity suppression + Portrait amplifier (+1/−1/Quarter in trending direction) + Chorus Question access + 2:1 Translation rate.

---

## Residential Quarter — PS Amplifier

All Public Standing changes are amplified for factions with presence in Residential Quarter (district 3), applied to every PS change anywhere on the board:

| Level | Multiplier |
|-------|-----------|
| Dominant | ×2 |
| Established | ×1.5 (round toward stronger effect) |
| Present | ×1.25 |
| Contested / Absent | ×1 |

Positive effects round up; negative effects round up in magnitude.

---

## Starting Resources (Q1)

Asymmetric reserves — faction resource theory shapes opening Quarter priorities:
- Ghost: 5 Findings (decay pressure immediate)
- Syndicate: 6 Capital (no decay)
- Others: TBD per artifact (playtest variable)
