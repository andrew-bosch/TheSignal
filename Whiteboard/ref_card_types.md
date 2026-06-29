# Reference — Card Types & Resolution Mechanics (Art 04 §5, §6, §11)
*Load when: card type questions, resolution mechanics, Modifier Card rules, §5 principle arguments.*

---

## Card Types

**CovertOperation** — Committed secretly face-down in Dispatch Case. Content hidden until ARBITER opens case at Beat 3. Irreversible once submitted. Resolves on the Beat 3 Resolution Grid. May be Automatic or d100. Default persistence = Immediate.

**PublicAct** — Declared openly face-up at Phase B. Public and visible from moment of declaration. Carries `outcome_type` field (Binary · ElectPlayer · ElectDistrict · ElectFaction · BilateralAgreement · Unilateral). Resolves at Beat 4.

**Pass** — Not drawn from a deck; four faction-specific variants (PS-01 through PS-04) kept beside tableau, reusable every round. Signals a covert or political slot is intentionally empty. Works for Beat 3 or Beat 4. Ghost's Political Pass special rule: using it confirms Ghost's case contains four Covert Operations rather than the standard three. Named variants carry small secondary effects (PS-02: +1 Findings at cleanup; PS-03: +1 modifier draw next Upkeep; PS-04: +1 Findings if faction holds highest Chorus Portrait). Excluded from Layer/Function/Subject taxonomy.

**Countermeasure** — Interact with Covert Operations only; not Public Acts. Submitted at Beat 2. Two types:
- **Type A (district block):** blocks Covert Operations targeting the named district
- **Type B (faction defense):** reduces Covert Operation difficulty against that faction's assets
STD.CA.12 (Absolute Compromise) can remove active Type A and Protect/Fortify plays; cannot target Type B. ⚠ Type A/B distinction is an open outstanding issue — the taxonomy must be defined in Art 03 or Art 04 before STD.CA.12 can be fully adjudicated (Art 04 STD.CA.12 checklist). Full Countermeasure design pending D-04-12.

**Modifier** — Alters parameters of a host action or fires on publicly observable board state changes. No independent game-state primitives. Three subclasses (Art 04 §6.1, 04-n102 ✅ S127):

- **ModReactCard** — fires automatically when trigger condition (publicly observable board state change) is met. `beat=None` always. `trigger` field Required (TriggerExpr — confirmed vocabulary in Art 04 §6.3; full list: design_reference_card_system.md). `ring_constraint` / `ring_origin` fields apply. Default: consumed on fire. FRG standing condition variant: DIR.MOD.6, SYN.MOD.6 place themselves face-up on the faction's FRG as a Quarter standing condition — no custom marker needed (schema model pending 04-n145). Accord trigger semantics: `accord.corrupted` = textual alteration via Covert Op (Accord stays active); `accord.removed` = breach or expiry (Accord card leaves board). Procedural authority: Art 03 §18.
- **ModActionCard** — submitted at Covert Dispatch bundled with a host Covert Operation; fires as an outcome addition when the host action resolves. `beat` inherited from host. Example: STD.MOD.1 Overture.
- **ModBattleCard** — submitted during §10 Contested District Resolution (Battlefield Strength resolution) only. Entirely separate from React cards; not playable outside that window.

**Outcome addition (ModActionCard behavior)** — attaches an additional Automatic outcome to the host PA at Beat 4 regardless of host success or failure. No Dispatch Token required. Example: STD.MOD.1 Overture.

Maximum 1 Modifier Card per action submitted. Excluded from taxonomy.

**EmergencyResponse** — Pre-sealed in faction envelopes at setup. Faction-specific; one per faction. Reactive threshold interventions that fire when a faction's board position is threatened. Not drawn from a deck. Effect descriptions are in Art 04 §14.1 — stub/draft territory; treat as working content only. Full card data structure not yet applied — pending D-04-10.

**Debrief Action Card** — Component type (not a CardType); a card that resolves at Debrief. SCIFRecord is the first defined subtype: placed in Ghost's Dispatch Case during play; at Debrief, Ghost draws Modifier Cards equal to target faction's Structure Block count at time of play.

---

## Modifier Cards in Depth

**Faction Modifier Cards** — drawn from faction's own deck in player tableau. Draw gated by Structure Block count (0–1: 0; 2–3: 1; 4–5: 2; 6+: 3 max). Back: faction color. One-pass per session; not reshuffled. Freely tradeable between factions outside Resolution — ring constraint on ring cards travels with the card.

**Ring Modifier Cards** — drawn from shared ring decks on the game board (Ring 3/2/1; no Chorus Node deck). Draw requires: 1+ Structure Block AND Established+ in at least 1 district in that ring. Back: ring color. Ring constraint applies to all users regardless of holder (Principle 23).

**Burst Play:** After Upkeep Step 6, before Dispatch — faction may trade all held Modifier Cards to Reservoir at 1:1 (any resource type per card). Removes the faction's Modifier Deck from tableau for rest of session. Post-Burst factions may still receive and use Modifier Cards through trade — Burst removes draw access only. *(Art 04 §11.6 — draft section)*

---

## Resolution Mechanics

**Threshold baselines by ring** (ring_mod applied to base threshold):
| Ring | Default ring_mod |
|------|-----------------|
| Ring 0 — Chorus Node | −15 |
| Ring 1 — Core | −10 |
| Ring 2 — The Mid | 0 |
| Ring 3 — Baryo | +10 |

*Direction convention: positive = easier (raises effective threshold); negative = harder (lowers it). *(Art 04 §6.2)**

**Doctrine_mod** (based on pentagram proximity of acting and target faction):
- Neighbor (adjacent on doctrinal ring): +15
- Opposed (non-adjacent): −15
- None when no `target_faction`

**Critical ranges:** 01–05 = Critical Success (`roll ≤ 5`) · 96–00 = Critical Fail (`roll ≥ 96`). 5% chance each. Always apply regardless of threshold or modifier stack — hard floors and ceilings.

---

## §5 Design Principles — Thematic Overview

§5 establishes 25 binding principles across five concerns:

**Structural integrity (P1–P4):** Every card has exactly one primary layer. Faction-specific cards fill gaps or provide meaningful differentiation — they don't duplicate standard cards.

**Information and trigger discipline (P5, P24, P25):** React triggers must be publicly observable. Corrupt applies only to physically written/recorded values. Standard language phrases are defined once and used as written.

**Effect duration and cost discipline (P6, P15, P19–P21):** Exactly four valid duration types. Effects are permanent or within-Quarter — multi-Quarter temporaries prohibited. Cost is equitable to success effect. Crit success never adds cost.

**Faction doctrine and narrative integrity (P7–P10, P17):** Every faction-specific card must pass both mechanical test (only this faction would do this) and narrative test (only this faction would say it this way). Where a faction-specific card represents a native capability, a standard equivalent must exist at higher cost or lower threshold.

**Portrait and ARBITER governance (P11–P13, P16, P18, P22, P23):** Portrait fires on action taken, not outcome. ARBITER is the sole mover of Portrait — no Effect field may state a direct Portrait shift. Portrait entries are submitter-bounded. ARBITER instructions reference existing procedures; they do not define new ones.

**Card narrative integrity (P26):** Every card must be expressible as a 1–2 sentence plain-language narrative — what is actually happening in the world when this card is played? If the story cannot be told plainly, the card has a design problem. P26 is satisfied by the Card Story block (see below).

**Outcome determinacy (P27):** All four resolution tiers (`success`, `successcrit`, `fail`, `failcrit`) must each resolve to exactly one determinate outcome. `game.choose_one()` constructs, conditional player choice, and any either/or resolution within a tier are prohibited. Successcrit and failcrit are additive to their base outcome — not alternative paths.

---

## Required Card Entry Blocks

Every card entry in Art 04 §7+ must contain these two blocks in order, between the construction logic and the Design Checklist:

**Design Rationale** — documents design intent and mechanical reasoning: what role the card plays, why it is built the way it is, what narrative logic it serves. Includes an **Outstanding Issues** subsection when open design questions exist; an empty Outstanding Issues means no blockers. The presence of Outstanding Issues sets status to Pending sign-off.

**Card Story** — 1–3 sentences of plain-language narrative answering: *"What is actually happening in the world when this card is played?"* Reads as an event in New Meridian, not a restatement of the mechanic. Design Rationale explains *why*; Card Story tells *what happens*. Both must hold independently. *(P26)*
