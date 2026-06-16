# Faction Playstyle Development — S58
*Working notes — not locked. Migrate to Art 04 playstyle summary when complete.*

---

## Ghost — COMPLETE

### Economy
- **Intel** — native resource; primary cost on all Ghost cards
- **Gather** (multiple deck copies) — spend Intel → earn faction-keyed Intel token for a named target
- **Deep Cover** (single copy, burst) — spend n Intel → earn 2n Intel tokens for a named target; pre-funds multiple Quarters against same target
- **Faction-keyed Intel tokens** — gating resource for SCIF and Flip; must hold a faction's token to attempt that operation; difficulty is encoded in how hard/expensive that faction's tokens are to gather
- **SCIF** (action card) — spend faction Intel token → place SCIF Record card in Dispatch Case (records target's building count at time of play); at debrief, draw modifier cards equal to tally; cards enter hand for next Quarter
- **Flip** (action card) — spend faction Intel token → ARBITER loads target faction's native resources directly into Ghost's Dispatch Case at debrief
- **Own buildings** — if Ghost holds any structures, draws modifier cards normally at upkeep
- **Higher-tier Ghost cards** — primary cost Intel + secondary cost of Flip-acquired faction resource (consumed on play, C17 model); target faction's own resources used as instruments against them

### New Component
- **SCIF Record card** — placed in Dispatch Case when SCIF resolves; fields: `Q_ | Draw _ modifier cards`; minimal, no target name recorded on card; target identity stays with Ghost permanently

### Win Path
Build intelligence pipeline against primary target early → pre-fund via Deep Cover → run sustained SCIF/Flip in mid-to-late Quarters → arrive at Q8 with a hand built from other factions' capabilities. No permanent territory required; own building footprint is secondary.

### Design Notes
- Ghost presence is small; constraints are operational risk (Intel token scarcity) not territorial
- Snapshot timing is skill expression: SCIF target at their peak building count before disruption
- Modifier card draw count at debrief is visible (everyone sees Ghost gathering) but target is hidden — feature, not problem; conspicuous targets are Ghost's risk to manage
- Cross-Quarter stockpiling of Intel tokens is intentional; Deep Cover enables burst acquisition

---

## Guild — COMPLETE

### Economy
- **Capacity** — native resource; primary cost on all Guild cards
- **C15 Infrastructure Yield** — zero cost, Automatic; +1 Capacity per play from districts at Established/Dominant control tier; repeatable once per eligible district per Quarter; flywheel: more controlled districts = more activations = more Capacity
- **C01 passive labor income** (standing rule, not a card) — when any opponent completes C01 in a district where Guild has presence, Guild earns 1 Capacity automatically; Guild's own C01 plays are exempt ("built it for themselves"); presence gate creates broad early-spread incentive
- **C12 Materials Acquisition** — Beat 2 positional wager, zero cost; trigger: named faction completes C02 (Demolish) this Quarter; payment mirrors demolition cost; earns whether or not Guild is the target
- **Labor Contract** (placeholder name, new card) — C12 analogue for construction; Beat 2 wager, zero cost; trigger: named faction completes C01 or C03 this Quarter; payment mirrors build cost
- Together these three (C12 + Labor Contract + C01 passive rule): Guild gets paid when anyone builds or demolishes — no faction touches New Meridian infrastructure for free

### Territorial Engine
- **C13 Foundation Rights** — first-entry claim on unclaimed districts; near-automatic in Ring 0 (effective threshold 10); crit success = presence + structure simultaneously; crit fail = silent Intel Token to Directorate
- **C14 Construction Crew** — rush-build without presence prerequisite; 3 Capacity, threshold 65; crit fail rewards Ghost (Intel Token) and Syndicate (district native) — overreach feeds the opportunists
- **C11 Fortify Structure** — total immunity to C02 Demolish for one structure one Quarter; 1 Capacity; Beat 2 positional wager; strategic tension with C12 (can't protect and bet on demolition simultaneously)

### Win Path
Establish presence broadly and early (C13/C14) → control tier compounds into C15 income → passive C01 labor rule feeds Capacity from opponents' own building activity → mid-to-late Quarters, C15 flywheel + C12/Labor Contract counter-economics become self-sustaining → arrive at Q8 with the deepest physical footprint and a Capacity pool that scaled with the whole table's construction activity.

### Design Notes
- All five existing cards are CovertOperation type: "covert" = not pre-announced; results are immediately visible on the board (presence tokens, structures placed). Not a contradiction with Art 00 "Guild cannot operate covertly" — that's narrative doctrine, not card type
- C11 + C12 mutual exclusion is the key positional decision each Quarter: protect this structure, or bet someone demolishes it
- C15 balance concern (uncapped at scale) — outstanding issue; per-Quarter cap (max 2) flagged for playtesting
- C13 Ring 0 threshold concern — effective 10 after ring_mod; near-automatic; consider raising base to 35–40 (PM05 04-58)
- Card numbering schema rework flagged PM05 04-n1 — placeholder names acceptable for new cards now

---

## Syndicate — PENDING
*(Card concept flagged mid-session: "Land Title" card — Syndicate plays covert claim on a district 
asserting prior title (30 years ago, year 7 acquisitions per Art 00). When Guild subsequently builds 
a structure in that district, Syndicate becomes defacto owner — structure yields to Syndicate control 
or Syndicate earns income from it. Counters Guild C01/C14. Fits Art 00 doctrine: "Syndicate was 
acquiring ground underneath planned response facilities as early as year seven.")*

## Network — COMPLETE

### Economy
- **Exposure** — native resource; generated through Political Acts and successful tripwire fires
- **Modifier deck is the engine** — self-feeding; react/instant modifier cards on discard pull from action deck into modifier deck; deck grows each Quarter through play
- **Structures** — accelerate modifier deck growth (more structures = faster upkeep draws) but are not the win condition and not the primary focus; modest structural footprint, concentrated in Baryo
- **Tripwire (global condition card)** — Political Act, public; places a visible condition on the Overview declaring Network is monitoring a specific operation type from a named faction; expires end of Quarter or fires when tripped; fires deliver Exposure income + Standing damage to target + presence token gain for Network; starting assumption: 1 active tripwire per Quarter (not canonical — open to change)
- **Broadcast setup mechanic** — Political Act with two-phase resolution: Dispatch declares "setting up broadcast, target TBD"; on Network's initiative turn, name the faction; broadcast resolves (forced reveal + Exposure gain); creates table paranoia in the gap between setup and naming
- **React/instant modifier cards** — played in response to other factions' actions resolving; Network earns modifier draws from table activity (covert ops resolved, Standing shifts, structures built/demolished) — louder Quarter = richer Quarter

### Win Path
Generate **Presence tokens widely** across New Meridian, especially Baryo (Ring 3) outward. Network wins by breadth of presence, not control tier depth. Presence is earned through broadcasts and tripwire fires, not construction. Modifier deck grows each Quarter through self-feed mechanic; by Q6–8 Network has a large modifier hand per upkeep and multiple tripwires covering the table simultaneously.

### Two Attack Vectors
- **Against Directorate → influence.** Tripwires set on Directorate operation types; when fired, broadcast frames their action as corruption; Network earns presence in contested districts. Directorate's containment doctrine is Network's primary narrative target.
- **Against Ghost → information.** Ghost's economy runs on opacity; Network's information attack exposes SCIF cards, reveals Intel tokens, makes hidden activity public. Degrades Ghost's operational capability; generates Exposure for Network. No territorial contest — Ghost holds no territory anyway.

### Design Notes
- Structures are catalyst, not win condition — contrast with Guild (structures = output); demolishing a Network structure slows deck growth but doesn't collapse the economy
- "Louder but not stronger" — larger modifier deck = more reactions per Quarter, not bigger effects per card
- Network's presence is the only presence in the game not backed by structures — uniquely vulnerable to "discredit/suppress" type counter-cards rather than demolition
- Syndicate is protected (shadow investor relationship, not a mechanical rule — expressed through low affinity on Network targeting cards); Guild is irrelevant to Network's primary play
- Network home ring is Baryo; natural expansion is Ring 3 → Ring 2 → contesting Ring 1 against Directorate
- Quiet games hurt Network; they need table activity to fuel tripwire fires and modifier deck growth

---

## Syndicate — COMPLETE

### Economy
- **Capital only at upkeep** — Syndicate generates no native resource; all upkeep income converts to Capital at a higher rate than other factions' native resource generation; visibly wealthier pool at the table from Q1
- **Capital has multiple application lanes**: direct card costs, deferred investment returns, bypass payments, acquisition/takeover costs, proxy funding of Network, deterrent (held wealth implies battle winners available)
- **Resource conversion**: to acquire non-Capital resources: (1) direct trade with another faction, (2) formal Accord, (3) ARBITER 4:1 conversion (expensive floor — encourages negotiation over conversion)
- **Capital generation vectors**: structures (base modifier cards), foresight card returns, Land Title activations, C14 crit fall income, compound investment cards — more vectors than any other faction
- **Intel tokens as premium currency** — high-cost/high-reward plays (accord transfer, hostile takeover, battle winner deployment) require Capital + faction-keyed Intel token(s) for the target faction(s); Intel tokens not generated by Syndicate natively — must trade for them

### Ghost-Syndicate Structural Link
- Ghost generates Intel tokens; Syndicate needs them for high-value plays
- Natural trade: Ghost sells surplus Intel tokens to Syndicate for Capital; Ghost stays funded without territory; Syndicate accesses plays other factions can't execute
- Neither faction announces the relationship; other factions notice the pattern but can't prove an arrangement
- Ghost's Deep Cover burst card gains secondary value — generates surplus tokens for sale, not just own pipeline
- Cost template for Syndicate high-cost plays: `Capital (high) + faction-keyed Intel token(s) for each target party`

### Win Path
Position in Ring 1/2 early through foresight cards and Land Title → compound Capital through Q4 → push Dominant in 2–3 key economic spine districts Q5–8 → buy out any Directorate enforcement problems (bypass payment or shell complexity) → own the infrastructure the response runs on by Q8

### Key Mechanics
- **Land Title** — covert prior ownership claim on a district; when any faction builds there, Syndicate captures yield or becomes defacto owner
- **Hostile Takeover** — pay Capital + faction Intel token → replace target faction's presence tokens with Syndicate's at equivalent control tier; infrastructure stays, ownership transfers; "Acquisition" variant (Land Title pre-played) vs. "Hostile" variant (without prior claim, more expensive)
- **Buy your way out** — react modifier: spend Capital → enforcement action against Syndicate fails or threshold penalty negated; instant play, no dice roll
- **Accord Transfer** — unique to Syndicate; pay Capital + Intel tokens for each accord party → transfer accord from one faction to another; Syndicate can inject into any deal or liquidate any commitment; AccordCard needs "holder" field (updateable) — design note for Art 02
- **Battle winners** — rare, costly modifier cards; powerful enough to match Directorate military action in Ring 1/2; held as deterrent more than deployed; Directorate's awareness of their existence changes Ring 1/2 calculus

### Design Notes
- "Organized capital and organized crime — but are those really the same thing?" — Syndicate's core identity question; card perspectives never answer it
- Visible wealth attracts Directorate (white collar crime enforcement) and Network (privatizing public goods) — shell company mechanics are protective, not just thematic
- Shadow investor in Network: Syndicate funds Network's broadcasts; Network gets Capital; Syndicate gets political cover for Ring 1/2 operations; neither admits it
- Preferred mode: outwit/outmaneuver (bypass, legal complexity, accord transfer); military (battle winners) is available but doctrinally costly

---

## Directorate — COMPLETE

### Goals
- **Win via**: Established control tier in more districts than any other faction
- **Territory**: Wide — Core outward; 2nd place everywhere
- **Strategy**: Suppress Dominant (prevent any faction reaching Dominant); maintain broad Established presence; a balanced board with no Dominant factions and Directorate Established everywhere IS their win state — not neutral balance, Directorate-moderated hegemony
- **Two-front conflict**: Ring 3 (Baryo) vs. Network framed as "terrorism/destabilization"; Ring 1/2 vs. Syndicate framed as "white collar crime/financial regulation"

### Economy
- **Mandate** — native resource; generated through institutional acts (Political Acts, legislative filings) and from Core structures; the more institutional activity, the more Mandate generated
- **Structures in key areas only** — Core (command centers, HQ) and enforcement outposts (one per ring); generate base modifier cards + adjacency bonus: +1 modifier card per adjacent district where Directorate presence = Established; rewards wide Established strategy spatially
- **Modifier card modes**:
  - Military modifiers: boost conflict resolution, force presence removal thresholds, deploy enforcement assets
  - Legislative modifiers: reduce Political Act costs, extend world event duration, make legislation harder to remove

### Key Mechanics
- **Military Action vs. Legislation** — dual mode; legislation (Political Act) is slow, doctrinal, creates lasting restrictions, no Portrait cost; military action (CovertOp) is fast and direct but costs Portrait; Mandate funds both
- **Suppression** — push other factions' control tiers DOWN: Dominant → Established, Established → Present; regulatory freeze (no control tier advancement this Quarter in target district); best suppression toolkit in the game
- **Entry/Exit Controls** — persistent world event card placed on Overview; lowers success threshold for any faction placing presence in affected district; lasts one Quarter OR until removed by another faction; district-level by default; district + adjacent Established districts as extended variant; ring-level only via rare high-cost "state of emergency" card; Network has best tools to remove; Syndicate pays Capital to bypass
- **Modifier cards as assets** — human and equipment; patrol units, regulatory teams, intercept units, checkpoint equipment; deployable as instant/react plays

### Design Notes
- Cannot maintain Dominant anywhere without contradicting doctrine — Directorate holds Established as a deliberate strategic choice, not a ceiling
- Directorate avoids military confrontation with Syndicate not from weakness but from expected value calculation — Syndicate's battle winner modifier cards make the math unfavorable
- Network relationship: Directorate containment = Network's primary narrative target; Directorate frames Network as terrorism in Ring 3; Network frames Directorate as corruption everywhere
- C13 Foundation Rights crit fail delivers silent Intel Token to Directorate (Guild doesn't know); Directorate is passive Intel collector from other factions' mistakes

---

## Victory Architecture — COMPLETE

### Five Scoring Axes (all active simultaneously)

| Axis | What it measures | Notes |
|------|-----------------|-------|
| Faction goal | Components on board per faction's primary objective | Distinct per faction |
| Public Standing | Doing what New Meridian's public wants | Network best positioned |
| Portrait | Adherence to own doctrine throughout | Directorate, Guild strongest |
| Classified Directive | Hidden objective, revealed at Q8 | Unique per faction |
| Apex Activation | Operative apex path (Art 05) | Any faction; see below |

### Faction Goals

| Faction | Win via | Territory | Strategy |
|---------|---------|-----------|----------|
| Guild | Structures on board | Core/Mid priority | Build deep, compound via C15 |
| Network | Wide Presence tokens | Baryo outward | Broadcast in, grow modifier deck |
| Directorate | Established everywhere | Wide, Core outward | Suppress Dominant, moderate all |
| Syndicate | Dominant in Ring 1/2 | Economic spine | Buy position, wait for value |
| Ghost | Others betray doctrine | None required | Information control, manipulation |

### Cooperative Apex — The Human Win
- Multiple factions can pool toward a shared Apex activation
- Cost: doctrine-violating actions required → Portrait score damage for all participants
- **Apex = the human win condition**: factions stop responding to the Chorus and act on their own terms
- ARBITER and the Chorus are still watching; the signal keeps transmitting regardless
- Ghost's read: Apex is the worst outcome — not a wrong answer to the Chorus, but humanity ignoring it entirely with confidence
- No clear winner at Q8 — ARBITER's account of what happened IS the game's conclusion
