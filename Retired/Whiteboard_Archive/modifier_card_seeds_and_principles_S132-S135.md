# Modifier Card Seeds & Design Principles — Archived S135

*Moved from `Whiteboard/modifier_card_ideas.md` at session close (S135) once all seed pools and design principles below were fully consumed — every card described here has shipped into Art 04 §7. Kept as historical record of the design reasoning and reframing decisions behind the shipped content; not a live reference. Canonical content lives in Art 04; canonical decision history lives in PM02 (L242, L256–L265) and PM05 (09-06, 04-n157, 04-n170, 04-n171, 04-53).*

---

## ModBattleCard Design Principle (S132)

**Status: faction-set stub pass complete (S132) — 20 cards shipped, all 5 factions (Art 04 §7, DIR.MOD.10–13/GHO.MOD.12–15/NET.MOD.15–18/GUI.MOD.11–14/SYN.MOD.12–15). Ring-set stub pass complete (S134) — 24 cards, all 3 rings (STD.MOD.2–25).**

**Locked (Andy, S132):** All 5 factions get ModBattleCard content — not just the factions with obvious combat doctrine. Framing: **"battle" in this game is tension resolution — the struggle over a shift in a district's dominant influence, not necessarily violence.** Battlefield Strength (§10.1.2) fires whenever a district goes Contested; every faction has a stake in that outcome and a doctrinal way of contesting it.

**Per-faction voice — confirmed via the shipped stub sets:**
- **Directorate** — literal force: enforcement personnel, equipment, military assets (§5a explicit). Shipped: Riot Control Unit (Boost +1), Requisitioned Equipment (Boost +2), Emergency Curfew (Hinder −1), Martial Lockdown (Hinder −2).
- **Syndicate** — rare, costly "battle winner" assets; deterrent more than deployed (§5a explicit) — "costly" stayed a deck-level/rarity property, not a per-play resource cost. Shipped: Contracted Muscle (+1), Armored Transport (+2), Called-In Debt (−1), Bought Off (−2).
- **Guild** — construction crews, material stockpiles, structural expertise; Hinder cards kept procedural/visible (permits, inspections), consistent with Guild's "cannot operate covertly in principle" doctrine. Shipped: Site Foreman (+1), Material Stockpile (+2), Permit Delay (−1), Structural Condemnation (−2).
- **Ghost** — leverage/intelligence-based: what they know about the contest, not what they bring to it. Shipped: Embedded Contact (+1), Signals Package (+2), Planted Doubt (−1), Blown Cover (−2).
- **Network** — broadcast/exposure-based: public attention and narrative pressure as a form of contest weight. Shipped: Community Turnout (+1), Live Broadcast (+2), Street Pressure (−1), Public Outcry (−2).

**Mechanics — locked and shipped (S132, PM02 L242; full procedure: Art 03 §10.1.2):**
- `effect = ModBattleExpr(direction: Boost|Hinder, target: Faction, magnitude: int)`. Every card names a **target** — a contesting faction identified at §10.1.1 — chosen freely by the playing faction.
- **Any faction may play a card, contesting or not.**
- Placed face-down in front of the named target at commit; all commitments reveal simultaneously, before the d10 roll. No Target Profile — target is spoken, not written.
- **No quantity cap.**
- **`cost = None` for every shipped card, all 5 factions — including Syndicate.** An initial attempt to give Syndicate's set a Capital cost was corrected — Art 03 §10.1.2 has no cost-payment step in the commit sequence.
- **Magnitude scale (04-n94):** shipped as ±1/±2, mirrored by `value_rating` — flagged for playtest validation.
- Discarded on use regardless of outcome — may not be replayed in the same contest or any subsequent district contest that Quarter.
- Naming convention (S130): Asset (human/business), Equipment, or Tactic.

**Ring set (S134):** 24 cards, 8/ring (4 Portable, `ring_constraint=None` + 4 Ring-Locked, `ring_constraint=ring`), voiced from Art 00 §6.7 Ring Character.

---

## ModActionCard Design Principle (S135)

**Status: complete — 132 cards (60 faction, 12/faction + 72 ring, 24/ring).**

**Host-binding — resolved, no schema change.** A ModActionCard's host is whichever CA/PA/Operative/Emergency/Apex it's packeted with at Dispatch assembly (Art 03 §9.1.1). No card-level restriction field — a faction may splay any held ModActionCard under any of its own submitted operations. A ModActionCard can only ever ride with its own faction's own operation — packeted privately at case assembly, never dropped into a rival's sealed case.

**Cost — resolved, `cost = None` uniformly.** Beat 0 Dispatch resolution does validate payment per card in the packet (Art 03 §9.4.0.1 Step 2), so a live modifier cost was mechanically possible — but Modifier Cards are splayed beneath the operation card at Beat 0 to display value (§9.4.0.1 Step 4); a distinct per-modifier cost wouldn't read as its own legible line item in that display convention.

**Self-only constraint (PM05 04-n170).** Of the four `ModActionExpr` types, only `ps_shift` carries a faction parameter (`acting | target | named faction`). `threshold_delta`, `success_multiplier`, and `cost_reduction` have no faction field in schema — they can only ever apply to the card's own host action, matching the procedural fact that a ModActionCard can't reach a rival's sealed Dispatch Case. Hostile-flavored seed entries (Cordoned Block, Manifest Discrepancy, Show of Force, Signal Jammed, etc.) needed reframing to a self-only read wherever the stub pass drew from them — not a gap needing a fix, since the Faction Coverage Matrix already has a dedicated slot for hostile threshold interference (DIR.CA.8).

**Count/format per faction — locked (Andy, S135):**

| Effect | Anchor | Tiers |
|---|---|---|
| `threshold_delta` | Real thresholds run 25–65; `ring_mod`/`doctrine_mod` already establish ±10/±15 as "meaningful" | **4 — revised same session (caught reading back the transcript): +5 / +10 / +15 / +20, not 3.** `value_rating` widened 1–3 → 1–4 schema-wide (PM02 L259) so every tier gets its own distinct value. |
| `success_multiplier` | n=1 already doubles the host effect | 2 — n=1 common, n=2 rare/capstone |
| `ps_shift` | Only variant with a faction parameter | **4 — revised same session: a full 2×2 matrix (self +1/+2, target −1/−2), not 2 same-direction magnitude tiers.** Mirrors ModBattleCard's Boost/Hinder structure exactly. |
| `cost_reduction` | PA costs sample at 1–4 total units | 2 — reduce by 1, reduce by 2 |

**4 + 2 + 4 + 2 = 12 cards/faction** (revised twice same session — first 9→11 once the `ps_shift` matrix was recognized, then 11→12 once the `threshold_delta` tier count was corrected). Ring set: same 12-card structure ×2 (Portable + Ring-Locked) = 24/ring, 72 total.

**Shipped content:**

- **Directorate (DIR.MOD.14–25):** Standing Order (+5), Regulatory Clearance (+10), Show of Force (+15), Executive Mandate (+20); By the Book (n=1), Overwhelming Response (n=2); Model Citizen (acting +1), Commendation (acting +2), Public Reprimand (target −2), Internal Affairs Referral (target −1); Jurisdiction Waiver (n=1), Requisitioned Resources (n=2). Institutional-authority doctrine.
- **Guild (GUI.MOD.15–26):** Structural Survey (+5), Load-Bearing Confidence (+10), Permit Fast-Track (+15), Certified to Code (+20); Union Crew (n=1), Overbuilt (n=2); Community Groundbreaking (+1), Ribbon Cutting (+2), Inspection Noted (−1), Code Violation Cited (−2); Material Surplus (n=1), In-House Fabrication (n=2).
- **Ghost (GHO.MOD.16–27):** Pre-Analysis (+5), Known Variable (+10), Clean Channel (+15), Total Picture (+20); Clean Data (n=1), Layered Analysis (n=2); Quiet Correction (+1), Findings Published (+2), Discreet Leak (−1), Model Failure Exposed (−2); Existing Dataset (n=1), Shared Infrastructure (n=2).
- **Network (NET.MOD.19–30):** Groundswell (+5), Advance Coverage (+10), Clear Signal (+15), Full Saturation (+20); Cross-Posted (n=1), Viral Moment (n=2); Off-Air (+1), Exclusive Access (+2), Follow-Up Question (−1), Retraction Demanded (−2); Volunteer Stringers (n=1), Existing Airtime (n=2).
- **Syndicate (SYN.MOD.16–27):** Golden Handshake (+5), Insider Terms (+10), Cleared Position (+15), Total Leverage (+20); Compound Interest (n=1), Controlling Stake (n=2); Quiet Settlement (+1), Philanthropic Gesture (+2), Word Gets Around (−1), Predatory Terms Exposed (−2); Bulk Contract (n=1), Line of Credit (n=2).
- **Ring 1/Core (STD.MOD.26–49):** Portable — Zoning Variance (+5), Redacted File (+10), Maintenance Window (+15), Classified Briefing (+20); Institutional Backing (n=1), Ceremonial Groundbreaking (n=2); Off the Record/Public Citation (+1/+2), Word to the Wise/Named in the Review (−1/−2); Fee Waived (n=1), Emergency Allocation (n=2). Ring-Locked — Recognized on Sight (+5), Standing Request (+10), Back-Channel Word (+15), Full Clearance (+20); Shift Change Timing (n=1), Full Institutional Weight (n=2); Noted Favorably/Formal Recognition (+1/+2), Quietly Flagged/Denied Access (−1/−2); Reassigned on Paper (n=1), Jumped the Queue (n=2).
- **Ring 2/Mid (STD.MOD.50–73):** Portable — Rezoned Corridor (+5), Relay Intercept (+10), Manifest Correction (+15), Grievance Withdrawn (+20); Cross-Docked Efficiently (n=1), Chain Reaction (n=2); Compliance Certificate/Model Facility (+1/+2), Delay Logged/Safety Citation (−1/−2); Priority Routing (n=1), Bulk Rate (n=2). Ring-Locked — Dock Familiarity (+5), Grid Rapport (+10), Line Access (+15), Full Processing Rights (+20); Overtime Crew (n=1), Full Utilization (n=2); Filed Under Routine/Reliability Commendation (+1/+2), Overdrawn Account Exposed/Public Sanction (−1/−2); Consignment Hold Released (n=1), Standing Utility Contract (n=2).
- **Ring 3/Baryo (STD.MOD.74–97):** Portable — Squatter's Claim (+5), Landlord's Blessing (+10), Dock Contacts (+15), Neighborhood Backing (+20); Community Pool (n=1), Packed House (n=2); Street Reputation/Neighborhood Vouching (+1/+2), Busker's Tip/Overheard at the Strip (−1/−2); Credit with the Vendor (n=1), Barter Chain (n=2). Ring-Locked — Regular Customer (+5), Route Knowledge (+10), Neighborhood Standing (+15), Local Fixture (+20); Festival Grounds (n=1), Word Spreads Fast (n=2); Quiet Word to the Crowd/Block Party (+1/+2), Quiet Word Against Them/Turned Away (−1/−2); Scrap Value (n=1), Favor Owed (n=2).

Every card: `cost=None` uniformly, `value_rating` 1–4 mirroring tier/magnitude, `faction=All`/`subtype=Standard` for ring content.

---

## Ring ModAction Card Seeds (S134) — Raw Pool, Fully Consumed S135

Bucketed by the four `ModActionExpr` categories (§6.3): `threshold_delta` / `success_multiplier` / `ps_shift` / `cost_reduction`. Voice per Art 00 §6.7: Core = institutional access/procedural weight, Mid = operational throughput/infrastructure chokepoints, Baryo = gray economy/community network.

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

## Faction ModAction Card Seeds (S134) — Raw Pool, Fully Consumed S135

Voice per Art 00 §7 faction doctrine, same personality as each faction's shipped ModBattleCard set (S132), different mechanical lever.

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

## Ring ModReact Card Seeds (S134) — Raw Pool, Fully Consumed S135

**Full history:** 04-53 closed S135 as design-direction (PM02 L262). Reclassified S135: *Flagged for Review* (Core), *Routine Inspection* (Mid), *Someone's Watching* (Baryo) moved Information→Submission. Ring 1 (Core) shipped STD.MOD.98–109 (PM02 L263) — 6 of 12 seed concepts needed real redesign (no confirmed public trigger existed for several); *Overheard in the Commissary* rejected 3 candidate mechanics before landing on `dominant_marker.placed`. Ring 2 (Mid) shipped STD.MOD.110–121 (PM02 L264) — 11 direct ring=2 duplicates + one redesign (`accord.removed`). Ring 3 (Baryo) shipped STD.MOD.122–133 (PM02 L265) — same pattern, `accord.corrupted`. New syntax introduced (`holder`, `NativeResource(faction)`, `arbiter.modify`) flagged pending reconciliation at PM05 04-n171.

Voice per Art 00 §6.7: Core reacts through institutional/procedural channels, Mid reacts through infrastructure and throughput disruption, Baryo reacts through the crowd and the informal economy.

### Ring 1 — Core

**Territory:** *Notified of Encroachment* (fires when a rival places presence in a Core district — the acting faction reacts to being boxed out) · *Structural Objection* (fires when a rival's structure goes up nearby — a formal objection carries real consequence) · *Escort Withdrawn* (fires when a rival's last presence in a Core district is removed — the acting faction claims what's vacated)

**Information:** *Overheard in the Commissary* (fires when a rival's covert operation targeting the Core resolves — the acting faction reacts to what leaked) · *Access Log Pulled* (fires when a rival's operation in the Core is discovered — the acting faction benefits from having already known)

**Submission:** *Flagged for Review* (fires when a rival submits an operation touching the Core — the acting faction reacts before it resolves)

**Economy:** *Budget Reallocated* (fires when a rival moves a resource through the Core — the acting faction redirects part of it) · *Audit Trail* (fires when a rival's Core-based transfer is publicly revealed — an institutional consequence follows) · *Emergency Reserve* (fires when the acting faction's own resource falls short inside the Core — a reserve kicks in automatically)

**Standing:** *On the Docket* (fires when a Public Act targeting the Core resolves — the acting faction formally responds) · *Precedent Cited* (fires when an Accord involving a Core-based faction forms — the acting faction invokes it elsewhere) · *Quiet Reprimand* (fires when a rival's standing drops inside the Core — the acting faction capitalizes on the moment)

### Ring 2 — Mid

**Territory:** *Line Rerouted* (fires when a rival places presence adjacent to the acting faction's Mid structure — a reroute automatically follows) · *Capacity Exceeded* (fires when a Mid district reaches structure capacity — the acting faction reacts to the overflow) · *Salvage Rights* (fires when a rival's Mid structure is demolished — the acting faction claims part of what's left)

**Information:** *Flagged Shipment* (fires when a rival's covert operation moves through the Mid — the acting faction intercepts word of it) · *Grid Anomaly Logged* (fires when a rival's Mid operation is discovered — the acting faction already flagged the anomaly)

**Submission:** *Routine Inspection* (fires when a rival submits an operation touching Mid infrastructure — the acting faction reacts before resolution)

**Economy:** *Toll Collected* (fires when a resource passes through Mid infrastructure the acting faction has a stake in — a cut is automatically taken) · *Overtime Billed* (fires when a rival's Mid action exceeds a resource threshold — the acting faction reacts with a cost) · *Backup Generator* (fires when the acting faction's own Mid-based generation is disrupted — a reserve kicks in)

**Standing:** *Union Statement* (fires when a Public Act affecting Mid labor resolves — the acting faction issues a formal reaction) · *Service Level Breach* (fires when an Accord involving Mid infrastructure is broken — a standing consequence follows) · *Quiet Fix* (fires when the acting faction's own standing would drop from a Mid-based failure — the damage is quietly mitigated)

### Ring 3 — Baryo

**Territory:** *Crowd Gathers* (fires when a rival places presence in a contested Baryo district — the crowd's reaction shifts the situation) · *Eviction Notice* (fires when a rival's Baryo presence drops to its last token — the acting faction moves in on what's vacated) · *Block Party* (fires when the acting faction successfully places presence in Baryo — a community celebration reinforces it)

**Information:** *Word Travels* (fires when a rival's covert operation in Baryo resolves — the street already knew) · *Caught on the Strip* (fires when a rival's Baryo operation is discovered — the acting faction benefits from the timing)

**Submission:** *Someone's Watching* (fires when a rival submits an operation in Baryo — the acting faction reacts before it resolves)

**Economy:** *Informal Toll* (fires when a resource moves through Baryo's gray economy — a cut is taken without anyone filing paperwork) · *Vendor Credit Called* (fires when the acting faction's resource falls short in Baryo — informal credit covers the gap) · *Community Chips In* (fires when the acting faction's Public Act in Baryo would otherwise fail for lack of resources — the community closes the gap)

**Standing:** *The Crowd Remembers* (fires when a rival's standing drops in Baryo — the shift sticks longer than usual) · *Handshake Deal* (fires when an Accord involving a Baryo-based faction forms — the acting faction reacts with an informal side-benefit) · *Reputation Precedes* (fires when the acting faction's own standing in Baryo would rise — it rises further on reputation alone)
