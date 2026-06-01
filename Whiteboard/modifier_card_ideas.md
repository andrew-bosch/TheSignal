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

**REACT — PRESENCE PLACEMENT**
Trigger: when an opponent's political act succeeds this round, Network may immediately place 1 presence token in any district where they already have presence. *(Complex React timing — needs beat-sequencing review against Art 03)*

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
