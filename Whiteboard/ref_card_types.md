# Reference — Card Types & Resolution Mechanics (Art 04 §1–§5)
*Load when: card type questions, resolution mechanics, modifier card rules, §5 principle arguments.*

---

## Card Types

**CovertOperation** — Committed secretly face-down in dispatch case. Content hidden until ARBITER opens case at Beat 3. Irreversible once submitted. Resolves on the Beat 3 Resolution Grid. May be Automatic or d100. Default persistence = Immediate.

**PublicAct** — Declared openly face-up at Phase B. Public and visible from moment of declaration. Carries `outcome_type` field (Binary · ElectPlayer · ElectDistrict · ElectFaction · BilateralAgreement · Unilateral). Resolves at Beat 4.

**Pass** — Not drawn from a deck; four faction-specific variants (PS-01 through PS-04) kept beside tableau, reusable every round. Signals a covert or political slot is intentionally empty. Works for Beat 3 or Beat 4. Ghost's Political Pass special rule: using it confirms Ghost's case contains four covert operations rather than the standard three. Named variants carry small secondary effects (PS-02: +1 Findings at cleanup; PS-03: +1 modifier draw next Upkeep; PS-04: +1 Findings if faction holds highest Chorus Portrait). Excluded from Layer/Function/Subject taxonomy.

**Countermeasure** — Interact with covert operations only; not public acts. Submitted at Beat 2. Two types:
- **Type A (district block):** blocks covert operations targeting the named district
- **Type B (faction defense):** reduces covert operation difficulty against that faction's assets
STD.CA.12 (Absolute Compromise) can remove active Type A and Protect/Fortify plays; cannot target Type B. Full Countermeasure design pending D-04-12.

**Modifier** — Alters parameters of a host action. No independent game-state primitives. Effect categories: difficulty reduction, cost reduction, effect extension, detection immunity, reach extension, outcome addition. Two timing sub-types:
- **React:** fires automatically when a named publicly-observable board state change occurs. Procedural authority: Art 03 §18. First registered example: Grant Deed (DB:113). Note: §6.3 CardType enum has no "React" value yet — schema question open in 04-n99.
- **Instant:** played actively during a defined window
Maximum 1 modifier card per action submitted. Excluded from taxonomy.

**EmergencyResponse** — Pre-sealed in faction envelopes at setup. Faction-specific; one per faction. Reactive threshold interventions that fire when a faction's board position is threatened. Not drawn from a deck. Full design pending D-04-10.

**DebriefActionCard** — Component type (not a CardType); a card that resolves at Debrief. SCIFRecord is the first defined subtype: placed in Ghost's Dispatch Case during play; at Debrief, Ghost draws modifier cards equal to target faction's structure block count at time of play.

---

## Modifier Cards in Depth

**Faction modifier cards** — drawn from faction's own deck in player tableau. Draw gated by structure block count (0–1: 0; 2–3: 1; 4–5: 2; 6+: 3 max). Back: faction color. One-pass per session; not reshuffled. Freely tradeable between factions outside Resolution — ring constraint on ring cards travels with the card.

**Ring modifier cards** — drawn from shared ring decks on the game board (Ring 3/2/1; no Chorus Node deck). Draw requires: 1+ structure block AND Established+ in at least 1 district in that ring. Back: ring color. Ring constraint applies to all users regardless of holder (Principle 23).

**Burst Play:** After Upkeep Step 6, before Dispatch — faction may trade all held modifier cards to Reservoir at 1:1 (any resource type per card). Removes the faction's modifier deck from tableau for rest of session.

---

## Resolution Mechanics

**Threshold baselines by ring** (ring_mod applied to base threshold):
| Ring | Default ring_mod |
|------|-----------------|
| Ring 0 — Chorus Node | −15 |
| Ring 1 — Core | −10 |
| Ring 2 — The Mid | 0 |
| Ring 3 — Baryo | +10 |

**Doctrine_mod** (based on pentagram proximity of acting and target faction):
- Neighbor (adjacent on doctrinal ring): +15
- Opposed (non-adjacent): −15
- None when no `target_faction`

**Critical ranges:** 01–05 = Critical Success · 96–00 = Critical Fail. Always apply regardless of threshold.

---

## §5 Design Principles — Thematic Overview

§5 establishes 25 binding principles across five concerns:

**Structural integrity (P1–P4):** Every card has exactly one primary layer. Faction-specific cards fill gaps or provide meaningful differentiation — they don't duplicate standard cards.

**Information and trigger discipline (P5, P24, P25):** React triggers must be publicly observable. Corrupt applies only to physically written/recorded values. Standard language phrases are defined once and used as written.

**Effect duration and cost discipline (P6, P15, P19–P21):** Exactly four valid duration types. Effects are permanent or within-Quarter — multi-Quarter temporaries prohibited. Cost is equitable to success effect. Crit success never adds cost.

**Faction doctrine and narrative integrity (P7–P10, P17):** Every faction-specific card must pass both mechanical test (only this faction would do this) and narrative test (only this faction would say it this way). Where a faction-specific card represents a native capability, a standard equivalent must exist at higher cost or lower threshold.

**Portrait and ARBITER governance (P11–P13, P16, P18, P22, P23):** Portrait fires on action taken, not outcome. ARBITER is the sole mover of Portrait — no Effect field may state a direct Portrait shift. Portrait entries are submitter-bounded. ARBITER instructions reference existing procedures; they do not define new ones.
