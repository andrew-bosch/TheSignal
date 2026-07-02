# Modifier Card Ideas — Consolidated
*Working space. Not locked. Migrate to Art 04 modifier card design section when that phase begins.*
*Sources: Projects/Whiteboard/04_modifier_card_ideas.md · card_ideas_S51.md · faction_playstyle_S58.md (S58)*

---

## Architecture — S58 Taxonomy

### Three Types (+ one sub-category)

| Type | When played | Visibility | Payment timing |
|------|-------------|-----------|----------------|
| **React** | In response to a resolved action — instant | Public | At time of play |
| **Tripwire** | Placed on Overview as persistent condition; fires when condition met | Public | At time of play |
| **Battlefield modifier** | During contested resolution (Battlefield Strength) | Public | Within Beat structure |
| **Operation modifier** | Bundled with a submitted operation | Inherits operation visibility | Within Beat structure |

React and Tripwire fire outside the standard Art 03 Beat structure. Governing rule needed in Art 03 or Art 04 modifier card section: *"React and Tripwire modifier cards: cost is paid at time of play."*

**Cost:** Per-card — no blanket rule. Playtest/economy balancing question. React cards may be free (timing is the constraint). Tripwires probably cost 1 native resource. Battlefield assets (equipment, personnel) probably cost native resources. Operation modifiers probably free or very cheap.

---

## Tripwire Design Rules

- Placed openly on Overview as a declared condition: faction watching + operation type being watched
- Expires end of Quarter or when tripped (whichever first)
- **Decaying variant:** stops "the next X" actions, then disappears — forces opponents to burn low-value actions to clear
- **Physical interception variant:** targets the act of submitting a Dispatch Case (catches whatever is inside, indiscriminately)
- **Targeted interception variant:** fires when ARBITER publicly declares a specific operation type at resolution — more precise but requires knowing what to watch for
- **Counter-play:** the Execution Package Shield — pack an expensive shielding modifier inside Dispatch Case to bypass a known tripwire when it fires

Starting assumption for Network: 1 active Tripwire per Quarter. Not canonical — open to change.

---

## React (Interrupt) Design Rules

*(From Projects/Whiteboard/04_modifier_card_ideas.md — confirm against current Art 03)*

- **Observable triggers only:** a React cannot trigger off hidden information or contents of a Dispatch Case; trigger must be something any player at the table can openly observe
- **Immediate resolution:** no lingering or suspended states; when a card alters the board, that physical change resolves instantly
- **React to the result, not the order:** you cannot play a React to stop another React from being played; you must react to the new physical reality the first React creates

*Narrative example: Syndicate places a presence token. Directorate Reacts to remove it. Network cannot interrupt Directorate's order — must wait for the physical token to be removed, then Reacts to that board change (Directorate overreach as a story).*

---

## Visual / Physical Mechanics

*(From Projects/Whiteboard/04_modifier_card_ideas.md — confirm against Art 03/Art 09)*

- **The Splay:** all critical data (Portrait shifts, roll modifiers, resource costs) printed along a single edge; ARBITER splays cards to instantly calculate aggregate math and doctrinal impact
- **Covert Physical Commitment:** when submitted covertly, Action card + Modifier card + all resource tokens sealed inside Dispatch Case together; if operation fails or is intercepted, all committed resources permanently spent
- **Multiplier Effect (candidate — needs review):** base Portrait shift multiplied by total physical card count in Dispatch Case; massive operations amplify Chorus evaluation — *flag for review against current Art 03 portrait resolution*

---

## Faction Modifier Deck Design Notes

### Network
- Modifier deck is the primary economic engine — grows each Quarter via self-feed mechanic
- React/instant modifier cards on discard pull cards from action deck into modifier deck
- More structures = faster deck growth (structures as accelerant, not win condition)
- More modifier cards = more Reacts, more Tripwires active simultaneously — louder not stronger
- Network's tripwires pay out: Exposure + Public Standing damage to target + presence token gain

### Directorate
- Modifier cards represent deployable human and equipment assets: patrol units, regulatory teams, intercept units, checkpoint equipment
- Two modes: Military modifiers (boost conflict resolution, force presence removal thresholds) and Legislative modifiers (reduce PA costs, extend world events, make legislation harder to remove)
- Battlefield modifiers are the deterrent layer — visible deployment signals institutional strength
- Adjacency bonus: +1 modifier card at upkeep per adjacent district where Directorate presence = Established (structural rule, not a card)

### Syndicate
- Battle winners: rare, costly modifier cards; powerful enough to match Directorate military in Ring 1/2
- Held as deterrent more than deployed — Directorate's awareness of their existence changes Ring 1/2 calculus
- Their existence is the negotiating leverage, not the card effect

### Ghost
- Operation modifiers bundled with covert ops stay hidden until resolution — key information advantage
- Table never knows if Ghost's SCIF or Flip was enhanced; hidden modifier = hidden capability signal

### Guild
- Modifier cards tied to structure ownership: more structures = more modifier card draws at upkeep
- Battlefield modifiers likely: construction crews, material stockpiles, structural expertise

---

## Specific Card Candidates

*(From Projects/Whiteboard/card_ideas_S51.md — not yet assigned to card slots)*

### Cross-Faction / Standard

**TACTICAL WEIGHT**
During Battlefield Strength, burn any held modifier card face-up for +2 to d10 roll before resolution. Card discarded. One burn per faction per Battlefield Strength phase. *(Belongs in §11 Modifier Card mechanics, not the covert op set — flag for D-04-08)*

**INFORMATION WARFARE — STRIP**
Covert op: target faction loses 1 named modifier card from their hand (returned to deck). Requires Intel token naming the target faction. *(Targets modifier cards as an object class — new design territory; review interaction with Burst Play)*

**INFORMATION WARFARE — RECON**
Covert op: ARBITER privately reveals the count of modifier cards held by a named faction. Faction identities on those cards not revealed.

**ACCORD DISRUPTION**
Covert operation to break a binding Accord between two named factions. High cost; both parties notified. Requires Accord mechanic (Art 06) finalized before detail design.

**ACCORD REACT**
Fires automatically upon creation or public breach of an Accord. Acting faction may immediately take a named response action without submitting to standard queue. *(React timing and queue interaction need Art 03 review)*

### Guild

**RECONSTRUCTION PROTOCOL** — Territory — Add — Structure block (React)
Trigger: immediately when a Guild structure block is removed by Demolish or presence loss. Effect: return the structure block permanently and place 1 temporary operational marker. *(Uses "Recover" function — not in current verb set; needs verb decision before implementation — flag PM05)*

### Network

**NETWORK PS SHIFT** — Standing — Shift — Public Standing
Covert card: Network manages city-wide public perception through covert information operations. PS shift as a covert op rather than political act. Fills D-04-04 PS Shift gap.

**NETWORK PS RECOVERY / NEGATION** — Standing — Shift — Public Standing
Modifier card: negates some or all PS track changes for one beat, OR adds PS back after a deliberate sacrifice (e.g., post-Sacrifice recovery). Network-specific. Two possible forms: (1) React — when any effect would reduce Network PS, negate or reduce the loss; (2) Persistent — place at Dispatch, grants +1 or +2 PS at Beat 4 resolution. Pairs directly with Sacrifice (C37) — enables burst-and-recover pattern if Network builds around it. *(S65 — flagged during Sacrifice redesign)*

**REACT — PRESENCE PLACEMENT**
Trigger: when an opponent's political act succeeds this round, Network may immediately place 1 presence token in any district where they already have presence. *(Complex React timing — needs beat-sequencing review against Art 03)*

---

## ModBattleCard Design Principle (S132)

**Status: faction-set stub pass complete (S132) — 20 cards shipped, all 5 factions (Art 04 §7, DIR.MOD.10–13/GHO.MOD.12–15/NET.MOD.15–18/GUI.MOD.11–14/SYN.MOD.12–15).** Everything below is now confirmed design, not a hypothesis — see the per-faction breakdown at the end of this section. Ring-set content (Ring 1/2/3 versions) is the next pass, gated on 04-29 (ring-voice narrative gap — not yet resolved).

**Locked (Andy, S132):** All 5 factions get ModBattleCard content — not just the factions with obvious combat doctrine. Framing: **"battle" in this game is tension resolution — the struggle over a shift in a district's dominant influence, not necessarily violence.** Battlefield Strength (§10.1.2) fires whenever a district goes Contested; every faction has a stake in that outcome and a doctrinal way of contesting it.

**Per-faction voice — confirmed via the shipped stub sets, not provisional anymore:**
- **Directorate** — literal force: enforcement personnel, equipment, military assets (§5a explicit). Shipped: Riot Control Unit (Boost +1), Requisitioned Equipment (Boost +2), Emergency Curfew (Hinder −1), Martial Lockdown (Hinder −2).
- **Syndicate** — rare, costly "battle winner" assets; deterrent more than deployed (§5a explicit) — "costly" stayed a deck-level/rarity property, not a per-play resource cost (see Mechanics below). Shipped: Contracted Muscle (+1), Armored Transport (+2), Called-In Debt (−1), Bought Off (−2).
- **Guild** — construction crews, material stockpiles, structural expertise; Hinder cards kept procedural/visible (permits, inspections), consistent with Guild's "cannot operate covertly in principle" doctrine. Shipped: Site Foreman (+1), Material Stockpile (+2), Permit Delay (−1), Structural Condemnation (−2).
- **Ghost** — leverage/intelligence-based: what they know about the contest, not what they bring to it. Shipped: Embedded Contact (+1), Signals Package (+2), Planted Doubt (−1), Blown Cover (−2).
- **Network** — broadcast/exposure-based: public attention and narrative pressure as a form of contest weight. Shipped: Community Turnout (+1), Live Broadcast (+2), Street Pressure (−1), Public Outcry (−2).

Do not default to a uniform combat vocabulary across factions — each ModBattleCard's flavor reads as that faction's doctrine expressed through the tension-resolution mechanic, same narrative discipline as every other card type (Art 04 §5 P26). Use these 20 as the reference set when designing Ring-set or any future ModBattleCard content.

**Mechanics — locked and shipped (S132, PM02 L242; full procedure: Art 03 §10.1.2, condensed: `ref_procedures.md`):**
- `effect = ModBattleExpr(direction: Boost|Hinder, target: Faction, magnitude: int)`. Every card names a **target** — a contesting faction identified at §10.1.1 — chosen freely by the playing faction. `Boost (+magnitude)` adds to the target's total; `Hinder (−magnitude)` subtracts. A contesting faction's own Boost cards default to targeting themselves unless deliberately placed on a different contestant.
- **Any faction may play a card, contesting or not.** This is the mechanical hook for the "leverage/intelligence/broadcast" framing above — a Ghost or Network card doesn't need its own faction to be fighting over the district to have a doctrinal reason to weigh in on who wins it.
- Placed face-down in front of the named target at commit; all commitments (mod cards + Intel Tokens) reveal simultaneously, before the d10 roll. No Target Profile — target is spoken, not written.
- **No quantity cap** — Art 04 §11.4's "max 1 modifier card per action" does not apply here (§10.1.2 commit isn't an action submission; §11 itself is flagged non-canonical, 04-n153).
- **`cost = None` for every shipped card, all 5 factions — including Syndicate.** Art 03 §10.1.2 has no cost validation/payment step anywhere in the commit sequence, so a per-play resource cost is unenforceable content. Syndicate's "costly" (§5a) is expressed at the deck level (rarity/acquisition), not a mechanical cost field — an initial attempt to give Syndicate's set a Capital cost was corrected for this reason.
- **Magnitude scale (04-n94):** shipped as ±1/±2, mirrored 1:1 by `value_rating` — explicitly flagged for playtest validation, not treated as final balance numbers. Log actual play outcomes before locking.
- Discarded on use regardless of outcome — may not be replayed in the same contest or any subsequent district contest that Quarter. Press-the-Battle re-roll (§10.1.4.0.2) already supports playing fresh cards from hand on each loop.
- Naming convention (S130) still applies: Asset (human/business), Equipment, or Tactic.

---

## Open Design Questions

- Modifier card naming — "Assets" rename under consideration (PM05 XA-35); do not lock until Art 04 modifier section begins
- Modifier card deck types: Ring 1, Ring 2, Ring 3 modifier decks + 5 faction-specific modifier decks (PM05 04-56)
- Battlefield Modifier Card acquisition method — drawn at Upkeep with other Modifier Cards, or separate trigger? (PM05 04-49)
- Ring modifier geography principle — "a ring modifier is wrong if its narrative could apply equally to any ring" — revisit when modifier card design begins (PM05 04-29)
- Multiplier Effect needs review against current Art 03 Portrait resolution rules
- Modifier token Beat 4 disposition undefined (PM05 04-52)

---

*See PM05 items: 04-n4 (S58 architecture), 04-56 (deck types), 04-49 (battlefield modifier), XA-35 (assets rename), 04-29 (geography principle), 04-52 (token disposition)*
