# Design Reference — Master Index
*Session-open read. Enough to discuss anything; load sub-references when going deep.*
*Updated: S76.*

---

## The Game in One Paragraph

**The Signal** is a 2–6 player negotiation/area-control tabletop game set in New Meridian, a 31-year-old city built around an alien transmission (The Chorus). Five factions compete for influence over the city and control of humanity's response to first contact. ARBITER — simultaneously game facilitator and possible element of the Chorus's design — observes everything, moves the Portrait track, and writes the Chronicle. Players act covertly and publicly, negotiate Accords, build presence across 21 districts in 4 rings, and at game end commit collectively to a response. The Chronicle's account of what they actually demonstrated, vs. what they claimed, is the second outcome. Both matter permanently.

---

## Faction Quick Reference

| Faction | Identity | Resource | Doctrine |
|---------|----------|----------|---------|
| Ghost | The Interpreters | Findings | Understanding must precede action |
| The Network | The Broadcasters | Exposure | No one gets to decide this in the dark |
| The Syndicate | The Investors | Capital | Control comes from positioning early |
| The Guild | The Builders | Capacity | Humanity's response must demonstrate what it's capable of at its best |
| The Directorate | The Authority | Mandate | Survival requires control, restraint, and continuity |

**Doctrinal ring:** Ghost — Directorate — Guild — Network — Syndicate — (back to Ghost). Adjacent = closer philosophically. `doctrine_mod`: neighbor +15, opposed −15.

---

## Sub-References — Load on Demand

| File | Contains | Load when... |
|------|----------|-------------|
| `ref_world_narrative.md` | The Signal/Chorus premise, New Meridian, faction profiles & voices, ARBITER identity & hidden objectives, Four Registers, victory/Chronicle, Art 00 design principles | Narrative design, faction discussion, ARBITER behavior, Chronicle framing |
| `ref_design_pillars.md` | Foundational Design Pillars 4.1–4.6, §3 principles for 00a, canonical definitions (in-world ↔ mechanical term table) | Design principle arguments, source-of-truth disputes, terminology questions |
| `ref_components.md` | Full component registry (NS-xx, CA-xx, O-xx, etc.), lifecycle rules, component_positions DB table | Component registration, 00b questions, DB schema |
| `ref_board_narrative.md` | The Overview/MIRROR narrative, Chorus Node identity, ring character, district faction geography, zone vs. component distinction, ARBITER physical position, starting configuration | District design, board layout, narrative anchoring, physical placement questions |
| `ref_resources.md` | Generation formula, affinity bonus, structure block mechanics, The Translation (conversion rates), Findings decay, Dispatch Token rules, Chorus Node economics, Residential Quarter PS amplifier, starting resources | Resource system mechanics, conversion, generation, Contested districts |
| `ref_tracking.md` | Portrait bands (all 11) + game effects, Public Standing bands + threshold formula + drift, Intel Token age/use/privacy/discard | Portrait design, PS design, scoring, Intel Token mechanics, initiative order |
| `ref_procedures.md` | Dice roll procedure + modifier stack, Phase B declaration rules, Beat 4 PA resolution steps, React card rules (§28), Debrief procedure, Battlefield Strength | Procedure gaps, timing questions, React card design, Debrief rules, dice mechanics |
| `ref_card_types.md` | All CardTypes (CovertOp, PublicAct, Pass, Countermeasure, Modifier, EmergencyResponse, DebriefActionCard), modifier card draw/assignment/Burst Play, resolution mechanics (ring_mod baselines, doctrine_mod), §5 thematic overview | Card type questions, resolution mechanics, modifier card rules, §5 principle arguments |
| `ref_taxonomy.md` | 7 verb primitives, Layer/Function/Subject vocabulary, construction logic, assignment rules | Taxonomy assignment for new cards, 04b audit work |

**For card spec work:** also read `design_reference_card_system.md` (schema, governing rules, design flags — always relevant for card design).

---

## Board at a Glance

4 rings: **Baryo** (Ring 3, 9 districts, base gen 1) → **The Mid** (Ring 2, 7 districts, base gen 2) → **Core** (Ring 1, 4 districts, base gen 3) → **Chorus Node** (Ring 0, ARBITER's district, gen 0, no structures). Entry: Mid requires no presence; Core requires Established+ in adjacent Mid; Chorus Node requires Established+ in adjacent Core.

21 districts total. Influence levels: Dominant (3+, strictly most) · Established (2+, second) · Present (1+) · Absent (0) · Contested (tie at 3+). Max 6 presence chips/faction/district (deployment markers count). Max 1 structure block/faction/district.

---

## Key System States

**Portrait:** −20 to +20. Private (ARBITER only). Accumulates, no drift. Drives initiative order, Chronicle tone, final scoring. Sole mover: ARBITER. Not directly affected by card Effect fields.

**Public Standing:** 0–20. Public. All factions start at 10 (Neutral). Modifies all roll thresholds (Celebrated +20 · Respected +10 · Neutral 0 · Suspect −10 · Discredited −20). Natural drift: above 13 → −1/Quarter; below 7 → +1/Quarter.

**Resolution:** d100. Roll ≤ threshold = success. Crits: 01–05 always success; 96–00 always fail. Base difficulties: Easy 75 · Average 50 · Challenging 25.

**Resources:** Passive generation +1 native/Quarter unconditional (cannot be blocked). Ghost Findings decay at 7–12 (−2) and 13+ (−4) at Quarter end.

---

## Quarter Structure (Summary)

Upkeep → Placement (2 markers, snake order) → Month 1/2/3 [Dispatch A (Covert) → B (PA declaration) → C (Countermeasures) → Resolution Beats 0–5] → Debrief → End of Quarter.

**Beats:** 0 = cases open/grid built · 1 = read board state/SitRep · 2 = conditions set (Beat 2 cards) · 3 = covert ops resolve · 4 = PAs resolve · 5 = cleanup/Battlefield Strength if Contested.

---

## Always-Relevant Design Rules (Quick Checks)

Before any card spec:
1. Duration: Immediate / Transient / Seasonal / Permanent only
2. Cost: fungible resources only; partial = threshold penalty; zero = voided
3. React trigger: publicly observable only
4. Portrait: ARBITER-only mover — card effects shift PS, not Portrait
5. Passive generation: cannot be blocked or reduced (Design Pillar 4.8d)
6. New ARBITER behavior: define as generalizable procedure in Art 03/07 first (Design Pillar 4.7b)
7. Narrative field: no flavor implies faction knows what the message to the Chorus should say (Design Pillar 4.6b)
8. Card-as-condition (Permanent PA): no board marker; card IS the condition; define `persistence_condition` + `persistence_effect`

*Full governing rules table, card schema (§6.1/§6.2), and design flags: `design_reference_card_system.md`*
