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
- ~~Ring modifier geography principle~~ — **Closed S134 (PM05 04-29).** Resolved via Art 00 §6.7 "Ring Character": Core = institutional access/proximity, Mid = operational throughput, Baryo = gray economy/community. Applied to the 24-card Ring Modifier ModBattleCard set (STD.MOD.2–25).
- Multiplier Effect needs review against current Art 03 Portrait resolution rules
- Modifier token Beat 4 disposition undefined (PM05 04-52)

---

*See PM05 items: 04-n4 (S58 architecture), 04-56 (deck types), 04-49 (battlefield modifier), XA-35 (assets rename), 04-29 (geography principle — closed S134), 04-52 (token disposition)*

---

## Ring ModAction Card Seeds (S134) — Raw Pool, NOT Locked Design

**Status: seed material only.** Gated on 04-n157 (ModActionCard action-space analysis — not yet done). Unlike the ModBattleCard pass, ModActionCard has no locked count/format yet — no confirmed per-ring card count, no confirmed host-type distribution, no confirmed Boost/Hinder-style effect shape. These 48 entries (name + one-line narrative hook, 16 per ring) exist so that once 04-n157 defines the actual action-space, there's a rich pool to draw from instead of starting cold — captured now while the Art 00 §6.7 ring-voice context was live in-session. **None of these are card IDs, none have schema fields, none are committed to a specific host action type.** Bucketed by the four categories `ModActionExpr` actually defines in schema (§6.3) — `threshold_delta` / `success_multiplier` / `ps_shift` / `cost_reduction` — matching the Faction ModAction pool below (Andy, S134: the two pools should share the same shape). Revised from an earlier draft that used looser taxonomy-family buckets (Territory/Information/Economy/Standing-Submission); several entries were reframed here, not just relabeled, since a few of the originals described effects (moving resources, revealing information outright) outside what `ModActionExpr` actually supports.

Voice per Art 00 §6.7, same doctrine as the ModBattleCard set: Ring 1/Core leans on institutional access and procedural weight; Ring 2/Mid leans on operational throughput and infrastructure chokepoints; Ring 3/Baryo leans on the gray economy and community network. Kept distinct from the already-shipped faction ModActionCard/ModBattleCard voices for the same reason as the Battle set — these represent what's available to *any* faction operating in that ring, not a doctrine.

### Ring 1 — Core

**threshold_delta:** *Zoning Variance* (a quiet exception makes a Core placement or build action easier to clear) · *Cordoned Block* (a rival's target district is sealed "for maintenance," raising the difficulty of their operation there) · *Sealed Minutes* (key context is classified before a rival can plan around it, raising their operation's difficulty) · *Redacted File* (a report reaches its audience with the inconvenient part blacked out, smoothing the acting faction's own submission)

**success_multiplier:** *Ceremonial Groundbreaking* (official recognition of a successful placement makes its result carry further than usual) · *Institutional Backing* (an unseen endorsement from within the Core amplifies a successful action's effect) · *Closed-Door Outcome* (a decision made without public record lands at full force, undiluted by compromise) · *On the Record, Off the Books* (an action's official version is more favorable than what actually happened, and that's the version that counts)

**ps_shift:** *Public Citation* (a formal citation boosts standing through institutional channels rather than the public eye) · *Quietly Buried* (an action's less flattering details never surface, protecting the acting faction's standing) · *Named in the Review* (an audit's findings reach exactly the audience that costs a rival the most standing) · *Off the Record* (an exchange is agreed to never have happened, insulating the acting faction from the standing cost it would otherwise carry)

**cost_reduction:** *Emergency Allocation* (funds normally locked behind approval move immediately, discounting an urgent action's cost) · *Fee Waived* (a routine institutional charge is quietly set aside for the acting faction only) · *Reassigned on Paper* (an administrative reshuffle absorbs part of an action's overhead) · *Jumped the Queue* (a submission that skips the full review process skips the overhead that comes with it)

### Ring 2 — Mid

**threshold_delta:** *Rezoned Corridor* (an infrastructure corridor is reclassified, making a placement there easier to clear) · *Manifest Discrepancy* (a shipping manifest doesn't match its cargo, raising the difficulty of a rival's logistics-dependent action) · *Relay Intercept* (a tapped communications relay lets the acting faction anticipate and ease their own move) · *Union Grievance* (a formal labor complaint raises the bar a rival's submission has to clear)

**success_multiplier:** *Overtime Crew* (an extra shift pushes a build further than scheduled, amplifying its result) · *Cross-Docked Efficiently* (resources moved without ever formally stopping compound the action's benefit) · *Full Utilization* (a facility running at capacity turns a routine action into an exceptional one) · *Chain Reaction* (one system's output feeding directly into the next multiplies the outcome)

**ps_shift:** *Safety Citation* (a public safety violation becomes standing damage for whoever's named) · *Compliance Certificate* (a stamp of approval becomes a small, visible standing win) · *Filed Under Routine* (a genuinely significant action is buried among routine paperwork, muting its standing consequence either way) · *Overdrawn Account Exposed* (a rival's resource draw becomes public knowledge, at a cost to their standing)

**cost_reduction:** *Bulk Rate* (a resource purchase clears at an institutional discount not normally available) · *Consignment Hold Released* (a shipment already in the system is released without the fee a fresh order would carry) · *Standing Utility Contract* (an existing service agreement lowers what this action costs to mount) · *Priority Routing* (the acting faction's submission is rerouted to the front of a queue, skipping delay-related overhead)

### Ring 3 — Baryo

**threshold_delta:** *Squatter's Claim* (an informally occupied space becomes easier to formalize into a real presence claim) · *Landlord's Blessing* (backing from one of Baryo's unofficial housing authorities smooths a placement nobody easily challenges) · *Word on the Docks* (advance knowledge of a rival's shipment raises the difficulty of their operation) · *Petition Drive* (visible grassroots opposition raises the bar a rival's submission has to clear)

**success_multiplier:** *Festival Grounds* (a temporary permit becomes cover for something that lands bigger than expected) · *Community Pool* (several small contributions combine into an outcome larger than any single source could produce) · *Packed House* (an unusually large crowd amplifies whatever the action was counting on being seen) · *Word Spreads Fast* (informal networks carry an outcome further than any official channel would)

**ps_shift:** *Street Reputation* (word of mouth shifts standing faster than any official channel) · *Overheard at the Strip* (a casual conversation becomes something a rival has to publicly answer for) · *Busker's Tip* (a street performer's aside becomes the detail that costs someone standing) · *Quiet Word to the Crowd* (a rumor seeded in a gathering changes how an outcome is publicly read, protecting or costing standing depending on who seeded it)

**cost_reduction:** *Barter Chain* (a resource moves through several informal trades before landing where it was always headed, cheaper than a direct purchase) · *Credit with the Vendor* (informal credit lets an action proceed before payment technically clears) · *Scrap Value* (discarded materials from the Mid get reused at a fraction of fresh cost) · *Favor Owed* (a debt called in from the informal economy waives part of what an action would otherwise cost)

---

## Faction ModAction Card Seeds (S134) — Raw Pool, NOT Locked Design

**Status: seed material only, same caveats as the Ring ModAction pool above.** Gated on 04-n157. 60 entries (12 per faction), grouped by the four categories `ModActionExpr` actually defines in schema (§6.3) — `threshold_delta`, `success_multiplier`, `ps_shift`, `cost_reduction` — rather than the taxonomy-family buckets used for the Ring pool, since ModActionCard's real mechanical shape is already fixed even though no content exercises it yet. This grouping is closer to load-bearing than the Ring pool's, but is still not a design decision — 04-n157 may find the actual per-faction distribution across these four should be uneven, or that some don't suit a given faction's doctrine at all. Voice per Art 00 §7 faction doctrine and the doctrine framing already locked for each faction's ModBattleCard set (S132) — same faction personality, different mechanical lever (modifies a host action's odds/scale/standing/cost rather than throwing weight into a live contest).

### Directorate — literal force, institutional control, suppression-first doctrine

**threshold_delta:** *Regulatory Inspection* (a surprise inspection raises the bar a rival's operation must clear) · *Standing Order* (a pre-cleared directive eases the acting faction's own submission) · *Show of Force* (a visible deployment nearby raises the difficulty of anyone else's operation in the area)

**success_multiplier:** *Full Compliance Sweep* (an enforcement action that succeeds, succeeds harder than planned) · *Overwhelming Response* (a routine action escalates into a much larger institutional response) · *By the Book* (procedural correctness amplifies an action's formal outcome)

**ps_shift:** *Public Reprimand* (an official rebuke costs the named faction standing, on the record) · *Model Citizen* (the acting faction's compliance is publicly praised) · *Internal Affairs Referral* (a rival's conduct is quietly referred for review, and word gets out)

**cost_reduction:** *Requisitioned Resources* (institutional supply lines discount a deployment) · *Jurisdiction Waiver* (a procedural waiver removes part of an action's overhead) · *Standing Task Force* (a unit already in position reduces what the action costs to mount)

### Syndicate — capital and leverage, patient accumulation, deterrent-first doctrine

**threshold_delta:** *Insider Terms* (favorable terms negotiated in advance ease a financial move) · *Market Pressure* (applied leverage makes a rival's economic action harder to complete cleanly) · *Golden Handshake* (a well-placed incentive smooths the acting faction's own play)

**success_multiplier:** *Leveraged Position* (capital already in place multiplies a successful move's payout) · *Compound Interest* (a resource action's outcome grows the longer it's been set up) · *Controlling Stake* (enough capital already committed turns a modest success into a decisive one)

**ps_shift:** *Philanthropic Gesture* (a visible donation buys a standing boost) · *Predatory Terms Exposed* (a rival's finance practices become public knowledge, at cost to them) · *Quiet Settlement* (a dispute resolved out of public view protects standing)

**cost_reduction:** *Line of Credit* (pre-arranged financing discounts what an action costs to mount) · *Bulk Contract* (a standing agreement lowers the price of doing this again) · *Written Off* (a cost is quietly absorbed elsewhere on the books)

### Guild — construction and material, visible-by-doctrine, cannot operate covertly in principle

**threshold_delta:** *Structural Survey* (an engineering assessment eases a build action) · *Permit Delay Imposed* (a procedural obstruction raises the bar for a rival's construction action) · *Load-Bearing Confidence* (verified material integrity smooths a successful build)

**success_multiplier:** *Overbuilt* (a structure goes up stronger than the minimum required, amplifying its effect) · *Union Crew* (an experienced crew turns a routine build into an exceptional one) · *Ahead of Schedule* (early completion compounds the action's benefit)

**ps_shift:** *Ribbon Cutting* (a completed project is publicly celebrated) · *Code Violation Cited* (a rival's construction is publicly flagged for cutting corners) · *Community Groundbreaking* (visible investment in a neighborhood buys goodwill)

**cost_reduction:** *Material Surplus* (leftover stock from a prior job discounts the next one) · *Standing Contract* (an existing supplier relationship lowers costs) · *In-House Fabrication* (doing the work internally cuts out a markup)

### Ghost — intelligence and leverage, epistemic doctrine, incomplete truth over false clarity

**threshold_delta:** *Pre-Analysis* (advance modeling eases an operation's execution) · *Compromised Model* (planted bad data makes a rival's operation harder to complete accurately) · *Known Variable* (removing an unknown smooths the acting faction's own play)

**success_multiplier:** *Confirmed Hypothesis* (a correct prediction lands harder than planned) · *Layered Analysis* (multiple independent confirmations amplify an outcome) · *Clean Data* (an operation run on verified information performs better than expected)

**ps_shift:** *Findings Published* (a selective disclosure earns credibility and standing) · *Model Failure Exposed* (a rival's flawed analysis becomes public, at cost to them) · *Quiet Correction* (an error is fixed before anyone notices, protecting standing)

**cost_reduction:** *Existing Dataset* (prior research lowers the cost of new analysis) · *Shared Infrastructure* (borrowed analytical tools cut overhead) · *Known Contact* (an established source reduces the cost of getting information)

### Network — broadcast and exposure, transparency doctrine, decentralized information

**threshold_delta:** *Advance Coverage* (pre-positioned attention eases a public action) · *Signal Jammed* (disrupted messaging makes a rival's broadcast-dependent action harder) · *Groundswell* (organic public interest smooths the acting faction's own play)

**success_multiplier:** *Viral Moment* (an action catches unexpected attention and lands much harder than planned) · *Cross-Posted* (coverage across multiple channels amplifies an outcome) · *Trusted Source* (built-up credibility makes this disclosure land harder)

**ps_shift:** *Exclusive Access* (being first to a story earns standing) · *Retraction Demanded* (a rival's claim is publicly discredited, at cost to them) · *Off-Air* (a story is deliberately not run, protecting someone's standing quietly)

**cost_reduction:** *Existing Airtime* (a standing broadcast slot lowers the cost of getting a message out) · *Volunteer Stringers* (community contributors cut the cost of coverage) · *Borrowed Platform* (using someone else's channel avoids the cost of building one)

---

## Ring ModReact Card Seeds (S134) — Raw Pool, NOT Locked Design

**Status: seed material only.** Distinct gate from the two pools above: ModReactCard is the one subclass that routinely carries genuine Layer/Function/Subject taxonomy (§11.1, per the S133 rewrite), so Ring ModReactCard content is gated on **04-53** (Ring Modifier asset taxonomy, itself gated on 04b-03) rather than 04-n157 (which is ModActionCard-specific). 09-06 still tracks "Ring modifier content... pending" generally — this closes none of it, it's a pool. 36 entries (12 per ring), bucketed by the actual taxonomy **Layer** values already in use everywhere else in the schema (Territory / Information / Economy / Standing) — meaningful here in a way the ModAction pool's original taxonomy-family bucketing wasn't, because ModReactCard genuinely carries that taxonomy rather than excluding it. Each entry names a rough trigger concept (a board-state change in that ring) and what the reaction does — no `TriggerExpr` syntax, no card IDs, no confirmed Function/Subject assignment. Count is approximate (Andy: "8–12 per ring") — rounded up to 12 for parity with the other two pools.

Voice consistent with the other two Ring pools and Art 00 §6.7: Core reacts through institutional/procedural channels, Mid reacts through infrastructure and throughput disruption, Baryo reacts through the crowd and the informal economy.

### Ring 1 — Core

**Territory:** *Notified of Encroachment* (fires when a rival places presence in a Core district — the acting faction reacts to being boxed out) · *Structural Objection* (fires when a rival's structure goes up nearby — a formal objection carries real consequence) · *Escort Withdrawn* (fires when a rival's last presence in a Core district is removed — the acting faction claims what's vacated)

**Information:** *Overheard in the Commissary* (fires when a rival's covert operation targeting the Core resolves — the acting faction reacts to what leaked) · *Flagged for Review* (fires when a rival submits an operation touching the Core — the acting faction reacts before it resolves) · *Access Log Pulled* (fires when a rival's operation in the Core is discovered — the acting faction benefits from having already known)

**Economy:** *Budget Reallocated* (fires when a rival moves a resource through the Core — the acting faction redirects part of it) · *Audit Trail* (fires when a rival's Core-based transfer is publicly revealed — an institutional consequence follows) · *Emergency Reserve* (fires when the acting faction's own resource falls short inside the Core — a reserve kicks in automatically)

**Standing:** *On the Docket* (fires when a Public Act targeting the Core resolves — the acting faction formally responds) · *Precedent Cited* (fires when an Accord involving a Core-based faction forms — the acting faction invokes it elsewhere) · *Quiet Reprimand* (fires when a rival's standing drops inside the Core — the acting faction capitalizes on the moment)

### Ring 2 — Mid

**Territory:** *Line Rerouted* (fires when a rival places presence adjacent to the acting faction's Mid structure — a reroute automatically follows) · *Capacity Exceeded* (fires when a Mid district reaches structure capacity — the acting faction reacts to the overflow) · *Salvage Rights* (fires when a rival's Mid structure is demolished — the acting faction claims part of what's left)

**Information:** *Flagged Shipment* (fires when a rival's covert operation moves through the Mid — the acting faction intercepts word of it) · *Routine Inspection* (fires when a rival submits an operation touching Mid infrastructure — the acting faction reacts before resolution) · *Grid Anomaly Logged* (fires when a rival's Mid operation is discovered — the acting faction already flagged the anomaly)

**Economy:** *Toll Collected* (fires when a resource passes through Mid infrastructure the acting faction has a stake in — a cut is automatically taken) · *Overtime Billed* (fires when a rival's Mid action exceeds a resource threshold — the acting faction reacts with a cost) · *Backup Generator* (fires when the acting faction's own Mid-based generation is disrupted — a reserve kicks in)

**Standing:** *Union Statement* (fires when a Public Act affecting Mid labor resolves — the acting faction issues a formal reaction) · *Service Level Breach* (fires when an Accord involving Mid infrastructure is broken — a standing consequence follows) · *Quiet Fix* (fires when the acting faction's own standing would drop from a Mid-based failure — the damage is quietly mitigated)

### Ring 3 — Baryo

**Territory:** *Crowd Gathers* (fires when a rival places presence in a contested Baryo district — the crowd's reaction shifts the situation) · *Eviction Notice* (fires when a rival's Baryo presence drops to its last token — the acting faction moves in on what's vacated) · *Block Party* (fires when the acting faction successfully places presence in Baryo — a community celebration reinforces it)

**Information:** *Word Travels* (fires when a rival's covert operation in Baryo resolves — the street already knew) · *Someone's Watching* (fires when a rival submits an operation in Baryo — the acting faction reacts before it resolves) · *Caught on the Strip* (fires when a rival's Baryo operation is discovered — the acting faction benefits from the timing)

**Economy:** *Informal Toll* (fires when a resource moves through Baryo's gray economy — a cut is taken without anyone filing paperwork) · *Vendor Credit Called* (fires when the acting faction's resource falls short in Baryo — informal credit covers the gap) · *Community Chips In* (fires when the acting faction's Public Act in Baryo would otherwise fail for lack of resources — the community closes the gap)

**Standing:** *The Crowd Remembers* (fires when a rival's standing drops in Baryo — the shift sticks longer than usual) · *Handshake Deal* (fires when an Accord involving a Baryo-based faction forms — the acting faction reacts with an informal side-benefit) · *Reputation Precedes* (fires when the acting faction's own standing in Baryo would rise — it rises further on reputation alone)
