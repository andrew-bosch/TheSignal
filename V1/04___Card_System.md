# 04 — CARD SYSTEM
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.9.52 Draft  
**Status:** 🔄 Draft — Pending Sign-Off  
**Last Updated:** 2026-06-28  
**Supersedes:** v0.9.5, action_redesign (retired artifact)  
**Companion document:** 04b — Action Taxonomy & Design Analysis

---

## 1. Overview

Artifact 04 is the complete design specification for The Signal's action card system. It defines the data schema all cards share, full card content, and the mechanical rules governing card use at the table.

---

## 2. Index

| Section | Content |
|---------|---------|
| §3 | [Game Purpose](#3-game-purpose) |
| §4 | [Narrative Function](#4-narrative-function) |
| §5 | [Design Principles](#5-design-principles) |
| §5a | [Faction Playstyle Reference](#5a-faction-playstyle-reference) |
| §6 | [Card Data Schema](#6-card-data-schema) |
| §7 | [Card Specifications](#7-card-specifications) |
| §8 | [Card Taxonomy Index](#8-card-taxonomy-index) |
| §9 | [Faction Coverage Matrix](#9-faction-coverage-matrix) |
| §10 | [Deck Construction & Pool Selection](#10-deck-construction--pool-selection) |
| §11 | [Rules & Constraints — Modifier Cards](#11-rules-constraints-modifier-cards) |
| §12 | [Rules & Constraints — Pass Cards](#12-rules-constraints-pass-cards) |
| §13 | [Card Information Design Requirements](#13-card-information-design-requirements) |
| §14 | [Special Conditions & Gameplay Impacts](#14-special-conditions-gameplay-impacts) |
| §15 | [Examples & Exceptions](#15-examples-exceptions) |
| §16 | [Appendix — Outstanding Decisions & Assumptions](#16-appendix-outstanding-decisions-assumptions) |

---

## 3. Game Purpose

Cards are not menus — they are physical commitments.

Card systems serve many design purposes. The Signal uses all seven below — the first three are general properties of the card medium; the last four are the properties that specifically motivated the card format over simpler action-declaration mechanisms.

| Property | In The Signal |
|---|---|
| **Deck construction** — Pre-game strategic layer through selection from a larger pool. | Factions select their deck before each session. Preparation expresses doctrine. You cannot play a card you didn't prepare with. |
| **Draw variance** — Shuffle creates uncertainty about card availability each round. | Shuffled decks mean your intended action may not be available — forcing adaptation and planning for uncertainty. |
| **Resource economy** — Cards as tradeable assets with diplomatic value. | Modifier cards can be traded between factions — giving up a real advantage to build a relationship. |
| **Simultaneous commitment** — All players commit before any outcomes are known. | A covert operation card placed in the dispatch case is irreversible. A public act laid face-up cannot be retracted. |
| **Hidden information** — Decisions made under incomplete knowledge of opponent intentions. | Covert operations remain secret until ARBITER opens the case. Public acts are public — known, but not yet resolved. |
| **Asymmetric options** — Different players have access to different choices. | Faction-specific cards give each faction a decision space that reflects its doctrine. No two factions face exactly the same choices. |
| **Self-contained resolution** — Each card resolves without external reference. | Each card carries everything needed — no rules lookup required. |

---

## 4. Narrative Function

Every card is a decision made under incomplete information by people who believe the stakes are existential.

A covert operation in the dispatch case represents operatives committed, resources allocated, and a plan set in motion before anyone knows what anyone else has planned. A public act is a public stance taken in front of The Table: a claim that can be supported, refuted, or turned against the faction that made it.

The fiction is not window dressing. A Denounce costs the target faction's native resource because accusations in New Meridian are drawn from the domain where a faction is most powerful. A Broadcast operation raises difficulty because people under observation behave differently. The mechanics are the story.

All card names, action text, and effect descriptions are written in the language of New Meridian and the factions that operate within it. The word on the card is the in-world term for what is happening. Players are not managing tokens — they are making decisions on behalf of people in a city who believe the future of human contact with the unknown depends on what happens at this table.

---

## 5. Design Principles

**Principle 1 — Every card has exactly one primary layer.**

Cards may produce secondary effects in other layers, but their primary layer and function must be unambiguous. A card that appears to span layers belongs to the layer of its primary target. When the primary target is unclear, the card is a design problem.

**Principle 2 — Faction-specific cards fill gaps, not duplicate standard cards.**

Where standard cards already cover a Layer — Function — Subject combination, faction-specific cards should either fill a gap or provide a meaningfully differentiated version (different restriction, scope, or scale).

**Principle 3 — Layer assignment reflects the game system being affected, not the physical verb.**

The same physical verb (`Add`, `Move`) can serve different layers depending on what it is acting on. Economy and Territory both use `Add` — the layer is determined by the target, not the action.

**Principle 4 — Protect belongs to the target's layer.**

Protect is not cross-layer. A card that protects a Territory element is a Territory card. A card that protects an Information element is an Information card. This keeps Protect assessable within faction coverage analysis for each layer independently.

**Principle 5 — React conditions must be publicly observable.**

React fires on publicly countable or observable conditions. Hidden conditions are not valid React triggers. This maintains information integrity — you cannot react to information you shouldn't have. *Authoritative constraint; non-negotiable. A trigger requiring hidden information invalidates the card design. Formerly 00a R26.*

**Principle 6 — Effect duration is permanent or within-Quarter. Multi-Quarter temporaries are prohibited.**

Effects either resolve permanently (persisting for the remainder of the session) or expire at end of the current Quarter. An effect that lasts a stated number of Quarters is not a valid design — it creates tracking overhead with no corresponding design payoff. When both durations could work, prefer permanent. *See also: Principle 19 — the four valid duration types named explicitly.*

**Principle 7 — Faction-specific cards are doctrinally exclusive.**

Every faction-specific card must pass two tests: mechanical (only this faction would do this — the effect cannot be justified by another faction's doctrine) and narrative (only this faction would say it this way — the card text sounds like no other faction). If either test fails, the card belongs to no one. Traceable to Artifact 00 §7.

**Principle 8 — Every card carries multiple voices in tension.**

The same action means different things depending on who is watching — this is the narrative texture of The Signal, and it runs through every card. Standard cards carry one perspective from each of the five factions. Faction-specific cards carry three: the owning faction's voice, one perspective from a doctrinally aligned faction, and one perspective from a doctrinally opposed faction.

*Faction alignment map: Art 00 §7 — Doctrinal Alignment Pentagram. L174.*

**Principle 9 — Difficulty is a card property.**

Base difficulty is designed and printed on the card. It is not derived from board state or influence level. Board state may modify the threshold through ring modifiers and affinity bonuses — it does not set the base. *L91, L97.*

**Principle 10 — Narrative consistency with Artifact 00.**

All card text is consistent with the world, factions, and doctrines in Artifact 00. Standard cards are grounded in actions any capable organization in New Meridian might plausibly take. The mechanics and the fiction are the same thing written differently.

**Principle 11 — Portrait fires on action, not outcome.**

Portrait is impacted when an action strongly aligns with or against faction doctrine. Grey areas produce no Portrait effect. Unconditional Portrait fires on action taken regardless of roll outcome. Portrait Bonus fires only on a specified condition. *L82.*

**Principle 12 — ARBITER is the sole mover of the Portrait track.**

No card Effect field may state a direct Portrait track shift. Faction influence on Portrait is mediated entirely through ARBITER's application of Portrait scoring. *L84.*

**Principle 13 — Flat portrait modifiers are prohibited on standard cards.**

Flat modifiers fire on every resolution regardless of submitter — on standard cards this creates unbounded accumulation risk. Flat is reserved for faction-specific cards where a board-state change is doctrinally significant in a bounded, deliberate way. *L131.*

**Principle 14 — Card entries contain only card-specific information.**

If a rule or convention is already established in a signed-off artifact, do not restate it. Card entries contain only information unique to that card: restrictions that override a general rule, ARBITER timing specific to this card, edge cases not covered by universal rules. *L127.*

**Principle 15 — Cost is equitable to the success effect.**

The resource cost of a card is calibrated to the expected value of its success outcome. A high-cost card must deliver a commensurately significant success. Connects to 00c §8 Derived Cost Analysis.

**Principle 16 — Portrait entries are submitter-bounded.**

A portrait entry may only affect the portrait of the faction that submitted the card. No entry may fire for a non-submitting faction. ARBITER evaluates the doctrinal alignment of the faction taking the action — not the reactions of factions that did not act.

**Principle 17 — Faction-native capabilities have accessible standard equivalents.**

Where a faction-specific card represents a native, in-house capability (Ghost's intelligence pipeline, Guild's construction expertise, Directorate's regulatory authority), a corresponding standard card should exist that any faction can access — at higher cost or lower threshold — representing outsourced execution through hired data specialists, contractors, or counsel. Faction-specific cards embody the competency; standard cards are the contract. Standard equivalents are designed as separate cards alongside their faction-specific counterparts and are tracked as PM05 items when the faction-specific card is written.

**Principle 18 — ARBITER instructions reference procedures; they do not define them.**

Every card requiring ARBITER action maps to a named general procedure defined in a governing artifact. `arbiter_note` fields reference existing procedures — they do not define new ones. When a card design requires new ARBITER behavior, that behavior must be defined as a generalizable procedure in a governing artifact (Art 03, Art 07, or equivalent) before the card is finalized. *Governing Rule 6.1.*

**Principle 19 — Card effects use exactly one of four valid duration types.**

- **Immediate** — resolves and is removed at the Beat in which the card resolves; no lingering game state
- **Transient** — persists until Close Month (end of the current month); removed automatically
- **Seasonal** — persists until End of Quarter (Debrief); removed automatically
- **Permanent** — persists for the remainder of the session until a named action or condition removes it

No other duration is valid. *See also: Art 00a §3.1 — canonical duration definitions; Principle 6 — prohibition on multi-Quarter temporaries. Formerly 00a R21.*

**Principle 20 — Actions proceed with whatever resources are committed. Shortfalls carry consequences.**

- **Full payment:** action proceeds at stated difficulty
- **Partial payment:** action proceeds with a threshold penalty (procedure in Art 03)
- **Zero payment:** action is voided; returned to faction, cost not applied

The Table does not extend credit. *Formerly 00a R22.*

**Principle 21 — Critical success never adds cost.**

Critical success may modify, amplify, or expand the success effect. It may never impose a cost or obligation not present on standard success. Cost reductions on critical success are permitted (e.g., "return primary cost to dispatch case"). *Formerly 00a R23.*

**Principle 22 — Portrait values are a card property.**

Portrait scoring values are printed on the card at design time. ARBITER reads and applies the printed portrait field — it does not calculate Portrait at resolution. A card with no Portrait impact carries `portrait = None`. *See also: Art 00a Governing Rule 5.1c — Portrait fires at resolution. Formerly 00a R24a.*

**Principle 23 — Ring Modifier cards target only their assigned ring.**

A Ring Modifier card effect targets only districts in the ring the card is assigned to. The ring restriction applies regardless of which faction holds or plays the card. *See also: Art 04 §11. Formerly 00a R25.*

**Principle 24 — Corrupt applies only to physically written or recorded values.**

Valid Corrupt targets: Intel Token content, Accord agreement terms. Invalid targets: marker positions, printed card text, verbal agreements, any board state tracked by physical placement rather than inscription. *Formerly 00a R27.*

**Principle 25 — Standard language conventions apply globally and are not restated on individual cards.**

The following phrases are defined once and used as written across all card entries:

- **"At least 1 presence token"** — includes deployment markers *(Art 00a Governing Rule 8.3)*
- **"Delivered in case"** — standard phrase for privately delivered effects *(L59)*
- **"Return primary cost to dispatch case"** — standard phrase for crit success resource refunds *(L60)*
- **"Any other faction"** — standard target phrase when self-targeting is not permitted *(L61)*

Cards do not define or qualify these phrases. *Formerly 00a R28.*

**Principle 26 — Every card must be expressible as a narrative story.**

Each card represents something that happens in New Meridian — a decision, a gambit, an act of power or desperation. A card passes the Narrative Story test if a player can answer *"What is actually happening in the world when this card is played?"* in one or two plain sentences. If no coherent narrative can be constructed — if the card's effect reads only as a mechanical rule with no discernible real-world analog — the card is a design problem. Narrative is not decoration applied after mechanics are settled; it is the first test of whether the mechanics are right. The story drives the card, not the reverse. *See Art 04 §5a — Narrative Anchor; Art 00 §5 P1/P5; Design Pillar 4.6b.*

**Principle 27 — Every card resolves to exactly one determinate outcome per resolution tier.**

Each of the four resolution fields — `success`, `successcrit`, `fail`, `failcrit` — must specify exactly one outcome. Branching within any tier — `game.choose_one()` constructs, conditional player choice, or any either/or resolution — is prohibited. Each tier represents one specific event that occurred in New Meridian; unambiguous outcomes are required for ARBITER execution, narrative coherence, and compliance with the ARBITER Cognitive Efficiency principle. *Successcrit and failcrit are additive to their base outcome — they are not alternative paths.*

---

**P28 — Resource Cost Positioning**

A card's resource cost must match its power level per the floor/ceiling model in 00a §9.2. Mono-resource costs (acting faction's own native resource only) belong on floor-power cards — limited in effect, available from game-open. Cross-faction-resource costs (two or more distinct native resources) belong on ceiling-power cards — proportionally stronger, executable only through prior trade or territorial expansion. A card may not be simultaneously mono-resource and high-power. If a card's effect is strong, its cost must cross faction lines.

Non-native resource generation through card effects must be exceptional. The canonical paths to non-native resources are trade and territory expansion — a card that generates them directly shortcuts those paths and requires explicit doctrine justification.

---

### Design Rationale

Each card entry opens with a Design Rationale block. The Design Rationale documents the design intent and mechanical reasoning for the card — the "why" behind the spec. A reviewer reading the Design Rationale alone should understand what role the card plays, why it is built the way it is, and what narrative logic the design serves.

**Design Rationale covers:**
- The card's role in the system — what gap it fills, what mechanism it embodies, or what player behavior it enables
- Cost vs. reward calibration — why the cost and success effect are set at these values relative to comparable cards
- Resolution rationale — why Automatic or probabilistic; why this base threshold
- Restriction and affinity rationale — why the play conditions are designed this way; what doctrine they reflect
- Relationship to paired or mirror cards where meaningful

**Outstanding Issues** is a subsection of Design Rationale when open design questions exist. Each issue states the question clearly and, where possible, enumerates the options. An empty Outstanding Issues section means no blocking questions remain. The presence of Outstanding Issues sets the card's status to Pending sign-off.

---

### Card Story

The Card Story block immediately follows the Design Rationale and precedes the Design Checklist. It contains 1–3 sentences of plain-language narrative answering: *"What is actually happening in the world when this card is played?"* The story should read as an event in New Meridian — not as a description of the card's mechanical effect.

Design Rationale explains *why* the card is designed a particular way. Card Story tells *what happens*. The two are separate: Design Rationale addresses mechanical intent, design objectives, and callouts. Card Story is the human event. A card with a strong Design Rationale can still fail P26 — and a compelling Card Story that doesn't survive mechanical scrutiny is still a design problem. Both must hold independently.

---

### Design Checklist

Every card entry includes a design checklist table immediately before the Python spec, followed by a Status table. The checklist and status table together gate a card's progression through review and sign-off.

The **Artifact ref** column in each card's checklist should cite the specific section or procedure in the supporting artifact that validates that row for that card — not just the artifact number. Where no specific section exists yet, that absence is itself a gap to flag in Status. The general guidance column below shows where to look; card entries must be more specific.

**Status table format:**

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

- **Design Pass** ✓ — checklist evaluation complete; all 17 rows assessed
- **Issues Resolved** ✓ — all flagged issues addressed; blank if open issues remain
- **Signed off** ✓ — Andy's explicit approval; record session number (e.g., ✓ S49); blank until signed

A card with no issues from the design pass gets ✓ in both Design Pass and Issues Resolved. Signed off stays blank until Andy reviews and approves.

| Category | What it checks | General guidance |
|----------|----------------|-----------------|
| Action fit | Does this card's action type belong in New Meridian? Is the mechanical premise grounded in the world? *(GUI.PA.2, P7 test 1)* | Art 00 §7 |
| Voice fit | Do the faction perspective fields read in the correct register? Could each faction's line have been written by someone who knows that doctrine? *(P7 test 2, P8)* | Art 00 §7, §9 |
| Doctrine alignment | Does the card's effect serve or oppose the doctrine of specific faction(s)? If so, is that doctrinal relevance captured — through portrait entries, affinity, or `doctrine_mod`? Where `target_faction` is set: is `doctrine_mod` applied and justified, or is the decision not to apply it documented? | Art 00 §7; Art 04 §6.5 |
| Card type fit | Is the Card Type/Subtype classification correct (Standard vs. faction-specific; Covert vs. Political)? For faction-specific cards: does it fill a gap or provide meaningful differentiation from existing standard cards? *(P1, P2)* | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | Does the Layer/Function/Subject assignment correctly represent the action per the Art 04b taxonomy? *(P3, P4)* | Art 04b §4 |
| Balance | Is cost equitable to success effect? Is difficulty calibrated to restriction and ring context? Best-effort until Art 00c economics is built — note any assumptions made. *(P9, SYN.PA.1)* | Art 02 §6–§7; Art 04 §6.5 |
| Effect duration | Are all effects permanent or within-Quarter? No multi-Quarter temporaries. Which of the four named types applies? N/A for immediate-resolution cards. *(P6, P19)* | Art 04 §5 P19; Art 03 §15 |
| Persistence | Is the `persistence` value set correctly in the card spec? Does this card leave a game-state marker on the table requiring Transient or Seasonal? Default = Immediate for cards fully resolved at beat. | Art 04 §6 |
| Trigger validity | If `trigger` is set: is the trigger condition publicly observable? N/A when no trigger. *(P5)* | Art 02; Art 03 |
| Portrait validity | Does portrait timing fire on action taken, not outcome? Are Effect fields free of direct Portrait track shifts? For Standard cards: is each faction's portrait entry (or justified absence) documented? Is entry magnitude doctrinally grounded? Do all portrait entries fire only for the submitting faction — no entry affects a faction that did not act? Are portrait values printed on the card (not computed at resolution)? *(DIR.PA.1, DIR.PA.2, NET.PA.1, SYN.PA.2, P22)* | Art 04 §6.2 |
| Supported by zones | Does `target_district` reference a valid zone? Is ring context consistent? | Art 01 §6–§7 |
| Supported by components | Do all referenced components and cost resources exist? | Art 02 §6–§8 |
| Supported by game procedure | Are all ARBITER and player actions implied by this card covered by Art 03 procedure? Flag any implied action not yet procedurally defined as a gap. | Art 03 |
| Data schema validation | Are all required fields from §6.1 present in the card spec? Do field values match §6.2 data dictionary types — e.g., `affinity` is `ConditionalExpr \| None` (not a tag); `doctrine_mod` is present and correctly typed; `persistence_condition`/`persistence_effect` are None unless `persistence=Permanent`; all enum values are valid per §6.3? | Art 04 §6.1–§6.3 |
| Card narrative | Is a Card Story block present and populated? Does it answer "What is actually happening in the world when this card is played?" in plain language — as an event in the world, not a restatement of the mechanic? Does the mechanic follow naturally from that story, or does the narrative feel retrofitted? If the story cannot be told plainly, the card should be revisited. *(P26)* | Art 04 §5 Card Story; Art 00 §5 P1/P5 |
| Outcome determinacy | Do all four resolution tiers (`success`, `successcrit`, `fail`, `failcrit`) each resolve to exactly one outcome? Is `game.choose_one()` absent from every tier? Does the card avoid conditional player choice in any resolution tier? *(P27)* | Art 04 §5 P27 |
| Resource cost positioning | Is this card's cost mono-resource (acting faction's own native resource only) or cross-faction-resource (two or more distinct native resources)? Confirm power level matches: mono-resource = floor-power; cross-faction-resource = ceiling-power. Flag if mono-resource and high-power, or cross-resource and underpowered. If cost generates non-native resources as an effect, flag — requires doctrine justification. *(P28)* | Art 00a §9.2 |

---

## 5a. Faction Playstyle Reference

This section defines each faction's intended operation economy, win path, and deck identity. It is the design reference for card assignments and gap analysis — read before designing or evaluating any faction-specific card.

---

### Narrative Anchor

Each faction's playstyle is the mechanical expression of its doctrinal position in Art 00 §7. Operation economy, win path, and deck identity are not design choices independent of the fiction — they are the fiction made playable. A card that feels wrong for a faction is wrong narratively before it is wrong mechanically.

| Faction | Core doctrine | Mechanical expression |
|---------|--------------|----------------------|
| Ghost | Understanding must precede action | Intelligence pipeline; delay; suppress premature consensus |
| Network | No one gets to decide this in the dark | Broadcast-derived presence; modifier deck growth; reactive exposure |
| Guild | What you build reveals what you are | Structures as win condition; permanence over adaptation; everything leaves a physical artifact |
| Directorate | Survival requires control, restraint, and continuity | Suppression over construction; legislative mode; managed stability |
| Syndicate | Whatever this is, it has value. Control comes from positioning early | Capital accumulation; infrastructure ownership; Ring 1/2 Dominant |

**Inter-faction doctrinal alignment:** Ghost → Directorate → Guild → Network → Syndicate → Ghost  
Adjacent factions share philosophical proximity; non-adjacent are opposed. Neighbor targeting: positive `doctrine_mod`. Opposed targeting: negative `doctrine_mod`. Full pair descriptions: Art 00 §7.

---

### Faction Goals

| Faction | Win via | Territory | Preferred Ring | Strategy |
|---------|---------|-----------|----------------|----------|
| Ghost | Delay — no premature answer to the Chorus | None required | N/A | Information control; intelligence pipeline; suppress premature consensus |
| Guild | Structures on board | Core / Mid priority | 0–1 | Build deep; compound via GUI.CA.5 |
| Network | Wide Presence tokens | Baryo outward | 3 → 2 → 1 | Broadcast-derived presence; grow modifier deck |
| Directorate | Established in more districts than any other faction | Wide, Core outward | 0 → all | Suppress Dominant; Directorate-moderated hegemony |
| Syndicate | Dominant in Ring 1/2 | Economic spine | 1–2 | Patient Capital; acquire, outmaneuver, hold |

---

### Path to Victory

Five scoring axes are active simultaneously throughout all eight Quarters. There is no single winner — ARBITER's Q8 account records which doctrines held, which fractured, and what humanity chose to do.

| Axis | What it measures | Portrait cost | Faction best positioned |
|------|-----------------|---------------|------------------------|
| Faction Goal | Components on board per faction's primary objective | None | Faction-specific |
| Public Standing | Alignment of your actions with New Meridian's public interest | Varies by action | Network |
| Portrait | Adherence to your faction's doctrine across all 8 Quarters | None — earned by playing true | Directorate, Guild |
| Classified Directive | Achievement of your hidden objective, revealed at Q8 debrief | Depends on objective | Unknown until revealed |
| Cooperative Apex | Joint achievement of the Operative Apex path with one or more factions | Yes — doctrine betrayal for all participants | Any faction; see Art 05 |

*Cooperative Apex is the human win condition: factions stop responding to the Chorus and act on their own terms. ARBITER and the Chorus continue watching. The response window is what it is.*

---

### Faction Playstyle Summaries

**Ghost**

Ghost believes understanding must precede action — that an incorrect answer to the Chorus may be worse than no answer at all. The pressure to respond at The Table, driven by politics, capital, and institutional anxiety, is, in Ghost's view, the greatest danger. Their presence in New Meridian is embedded, invisible, and thirty-one years deep — long enough to know that certainty about the Chorus is indistinguishable from hubris. Ghost wins not by answering the question, but by ensuring no one else answers it prematurely. Intelligence is the mechanism; doctrinal deviation in others is the outcome. Every faction that fractures its own doctrine — chasing a Cooperative Apex, acting on incomplete intelligence, overcommitting to a position it cannot sustain — has done Ghost's work for it.

- **Economy:** Intel (Findings) → faction-keyed Intel tokens via Gather operations
- **SCIF:** consume token → place SCIF Record card in Dispatch Case; at debrief, draw modifier cards equal to target's building count at time of play — Ghost is always funding next Quarter's hand
- **Flip:** consume token → ARBITER loads target faction's native resources into Ghost's Dispatch Case
- **Higher-tier cards:** carry a secondary cost drawn from Flip acquisitions — the target faction's own assets turned against them
- **Passive generation:** Intel tokens from game events occurring near Ghost presence
- **Signals Analysis:** high-cost; deduce a target faction's Classified Directive — knowledge used to suppress premature consensus
- **No permanent territory** — presence is operational, not positional
- **Win path:** build intelligence pipeline early; pre-fund multiple Quarters via Full Take (burst card — Findings×N for proportional token yield); arrive at Q8 with a hand assembled from other factions' capabilities via Flip → Deep Cover and future Flip-fed cards
- **Deck feel:** precise, patient, deliberately small

**Guild**

Guild believes the Chorus is an evaluation: humanity's response will be judged not by intent, but by what it builds. Improvisation reveals weakness. Shortcuts reveal urgency. What Guild places on the board is not a tactical position — it is an argument about what humanity is capable of at its best, made permanent in physical form. Guild is also the only faction at The Table that cannot operate covertly in principle: planetary-scale infrastructure cannot be classified. Operations are submitted through the shared dispatch procedure (sealed, timed), but the results are never hidden — everything lands immediately on the board as a presence token or structure. The procedure is shared; the doctrine is not. The deck does not feel covert. It feels like construction.

- **Economy:** Capacity, compounded via GUI.CA.5 Infrastructure Yield — zero-cost Automatic; draws Capacity from each Established or Dominant district each Quarter
- **Passive income:** +1 Capacity when any opponent completes STD.CA.1 in a district where Guild has presence (Guild employees did the work)
- **GUI.CA.2 Materials Acquisition:** converts correctly anticipated demolition into paid recovery
- **Win condition:** structures on board, not just presence tokens — Guild is building the response, not positioning for it
- **Win path:** Foundation Rights (GUI.CA.3, near-automatic in Ring 0) → high tier in Core and Mid → GUI.CA.5 compounds → Fortify Structure (GUI.CA.1) defends → GUI.CA.2 collects salvage from the table's demolition activity
- **Deck feel:** heavy, deliberate, permanent

**Network**

Network believes no one gets to decide this in the dark. They arrived after The Chorus Papers, and loudly. Their presence in New Meridian is not territorial occupation — it is broadcast reach, community relationships, and the infrastructure of public knowledge. A district with Network presence is a district that knows what is happening there. Presence tokens represent how far the Network's voice carries; the win condition is not about holding ground — it is about ensuring that when the answer to the Chorus is spoken, the public of New Meridian has already heard everything The Table tried to keep quiet. Network and Syndicate share a structural relationship neither faction announces publicly: proxy funding flows through channels that route around Directorate visibility, a lateral bypass that both factions find useful for different reasons.

- **Economy:** Exposure via Public Acts and tripwire fires
- **True engine:** modifier deck — React and instant modifier cards pulled from action deck into modifier deck on discard; deck grows each Quarter through play, making Network louder without individual cards becoming stronger
- **Tripwire:** public global condition on the Overview; declares Network is monitoring a named operation type from a named faction; fires when condition met → Exposure income + Standing damage to target + presence token gains; paranoia effect of a pending broadcast is free
- **Structures:** accelerate modifier deck growth; not the win condition
- **Win path:** wide Presence coverage, Baryo outward, broadcast-derived; Q6–8 modifier deck self-sustaining with multiple React options per Upkeep
- **Attack vectors:** vs. Directorate = territorial; vs. Ghost = informational (exposing covert operations and SCIF pipelines)
- **Deck feel:** distributed, reactive, increasingly loud as the game progresses

**Directorate**

The Directorate's doctrine is not domination — it is managed stability. Survival requires control, restraint, and continuity; the win state is Established in more districts than any other faction because that configuration is not hegemony — it is the only board state the Directorate can guarantee remains reversible. No faction Dominant anywhere means no escalation has outrun institutional capacity to model and correct. Suppression is the instrument of restraint, not aggression: pushing another faction's tier down prevents a condition from becoming irreversible. The Directorate makes no distinction between rogue capital and rogue information — the Syndicate's gray-market acquisitions and the Network's broadcast operations are the same threat expressed through different channels. The procedural commitment does not change based on the mechanism of the disruption.

- **Economy:** Mandate via institutional acts and Core structures; Core structures draw an adjacency bonus: +1 modifier card per adjacent district at Established presence
- **Modifier deck — military assets:** enforcement personnel and equipment for conflict resolution and presence removal; available but costs Portrait
- **Modifier deck — legislative assets:** regulatory teams that reduce Public Act costs and extend world event duration; the doctrinal mode
- **Suppression toolkit:** push other factions' control tiers down rather than building own tiers up — best suppression capability in the game
- **Entry/Exit Controls (P-D1):** persistent world event; lowers opposing presence placement thresholds district-wide until another faction removes it
- **Win path:** Established in more districts than any other faction; no faction Dominant anywhere
- **Deck feel:** institutional, methodical, capable of making the whole table play defensively

**Syndicate**

The Syndicate does not debate whether the Chorus matters. They ask who will control the conditions under which a response is made. A reply requires infrastructure: transmission systems, energy, materials, coordination at scale. Whoever owns that infrastructure owns who speaks, how they speak, and what survives the process. Capital in The Signal is not just a resource — it is the Syndicate's argument that control over the physical basis of communication outlasts any political arrangement at The Table. The Syndicate was acquiring ground underneath the planned response facilities as early as year seven. They were inside before anyone else found the door.

- **Economy:** Capital exclusively; generated at upkeep at a higher rate than any other faction's native resource — the Capital pool is visibly larger from Quarter 1
- **No native secondary resource** — other types require direct trade, a formal Accord, or ARBITER's 4:1 conversion rate
- **Capital application lanes:** direct card costs; deferred investment returns; bypass payments (negate enforcement actions without a dice roll); hostile takeover costs (replace a faction's presence tokens at equivalent control tier); proxy funding via Network shadow relationship
- **Ghost structural link:** high-cost plays (accord transfer, hostile takeover, battle winner) additionally require faction-keyed Intel tokens — a link that operates beneath the table's visible alliances
- **Accord Transfer:** Syndicate alone can transfer accords between factions — every bilateral agreement is a potential Syndicate asset
- **Battle winner modifier cards:** rare and costly; serve primarily as deterrent — Directorate's awareness shapes Ring 1/2 calculus without deployment
- **Win path:** early positioning via foresight cards and Land Title → compound Capital through Q4 → push Dominant in Ring 1/2 economic spine Q5–8
- **Deck feel:** wealthy, patient, capable of restructuring the table's deals from underneath

---

## 6. Card Data Schema

*Art 04 §6 schema informed by a card game data structure gap analysis conducted sessions 23–24. Research notes (non-artifact): `Projects/TheSignal/Whiteboard/researchNotes_CardDesign.md`.*

---

### 6.1 Card Class Definition

Each card is an instance of `Card`. Fields are grouped by class. Narrative fields are prose; all other fields are typed expressions or static values.

```python
class Card:
    # ── Identity ──────────────────────────────────── static
    card_id:      CardID                      # canonical ID — [FAC].[TYPE].n per L219; registry: card_ref
    id:           str
    version:      Semver
    name:         str
    tagline:      str
    type:         CardType
    subtype:      Subtype
    faction:      Faction

    # ── Pool ──────────────────────────────────────── static
    is_unique:    bool                     # True = at most 1 copy in active deck (Operative, Apex); False for all others
    deck_limit:   int | None               # max copies in active deck; None = no per-card limit (pool-size governed)

    # ── Taxonomy ──────────────────────────────────── static, dimension-backed (Art 04b §4)
    layer:        Layer
    function:     Function
    subject:      Subject

    # ── Metadata ──────────────────────────────────── static
    beat:         int                       # 1–5
    resolution:   Resolution                # d100 | Automatic
    threshold:    int | None                # None when Automatic
    ring_mod:     dict[Ring, int] | None              # None when no ring variation
    doctrine_mod: dict[PentagramRelation, int] | None # None when no faction target or no doctrinal variation
    trigger:      TriggerExpr | None        # None = default beat timing
    resolution_type: str | None            # evolving vocabulary — feeds 00c §8
    outcome_type: OutcomeType | None        # public acts only
    persistence:           Persistence              # card table presence — Immediate/Transient/Seasonal/Permanent; default Immediate for covert ops
    persistence_condition: BoolExpr | None           # None unless persistence=Permanent; card discarded immediately when this evaluates False
    persistence_effect:    MutationExpr | None        # None unless persistence=Permanent; ongoing board condition active while card is in play

    # ── Targeting ─────────────────────────────────── expressions
    target_district:  DistrictExpr
    target_faction:   FactionExpr  | None
    target_object:    ObjectExpr   | None
    target_taxonomy:  TaxonomyExpr | None   # action taxonomy category this card targets; None = no taxonomy target

    # ── Logic ─────────────────────────────────────── predicates + expressions
    affinity:     ConditionalExpr | None    # evaluated before cost
    restriction:  BoolExpr       | None    # card unplayable if False
    cost:         CostExpr
    boost:        BoostExpr | None          # optional scaling — condition: per-unit CostExpr; may differ from base cost type

    # ── Effects ───────────────────────────────────── mutations  [VS-06]
    success:      MutationExpr | None
    successcrit:  MutationExpr | None       # additive delta — fires with success
    fail:         MutationExpr | None
    failcrit:     MutationExpr | None       # additive delta — fires with fail
    on_accept:    MutationExpr | None       # ElectPlayer only — effect when target accepts; None otherwise
    on_decline:   MutationExpr | None       # ElectPlayer only — effect when target declines; None otherwise

    # ── Portrait ──────────────────────────────────── dimension table  [VS-06]
    portrait:     dict[Faction, PortraitEntry]

    # ── Public Standing ───────────────────────────── structured PS model
    ps_framing:   PSFraming | None     # None = no PS shift from this card

    # ── Narrative ─────────────────────────────────── prose
    narrative:    str
    perspectives: dict[Faction, str]
    design_note:  str | None                # [VS-04 — ARBITER-only]
    arbiter_note: str | None                # [VS-04 — ARBITER-only]


class PortraitEntry:
    flat:      int | None         # fires on resolution regardless of submitter — faction-specific cards only (L131)
    submitter: int | None         # fires when this faction submits the card
    where:     BoolExpr | None    # entry fires only when this evaluates True
    modifier:  int | None         # adjustment to submitter under additional condition
    mod_where: BoolExpr | None    # modifier fires only when this evaluates True (AND entry active)

class PSShift:
    faction:  str   # "acting" | "target" | named faction
    delta:    int   # positive = gain, negative = loss

class PSFraming:
    type:       str                  # "probabilistic" | "fixed"
    trigger:    str                  # "resolution" | "discovery" | "placement"
    ps_target:  str                  # "acting" | "target" | "both"
    threshold:  int | None           # D100 roll target; probabilistic only; None when fixed
    on_success: list[PSShift]
    on_fail:    list[PSShift] | None # None = no PS on fail; probabilistic PA default = acting −1


class ModActionCard(Card):
    # Modifier bundled with an op at Covert Dispatch; fires with host action. Field constraints: §6.2.
    effect:           ModActionExpr        # tagged union: threshold_delta | success_multiplier | ps_shift | cost_reduction (PA only)
    value_rating:     int | None            # 1–3; printed on card face; None = TBD (stub only)
    ring_constraint:  Ring | None          # None = no deployment restriction; Ring = usable only targeting that ring's districts
    ring_origin:      Ring | None          # None = faction modifier deck; 1/2/3 = drawn from that ring's modifier deck


class ModBattleCard(Card):
    # Modifier for Battlefield Strength resolution (§10 Contested District Resolution). Field constraints: §6.2.
    effect:           ModBattleExpr        # threshold delta; direction (Self | Opponent) + magnitude
    value_rating:     int | None            # 1–3; None = TBD (stub only)
    ring_constraint:  Ring | None          # if set, usable only in Battlefield Strength for a district in that ring
    ring_origin:      Ring | None          # None = faction modifier deck; 1/2/3 = drawn from that ring's modifier deck


class ModReactCard(Card):
    # Modifier firing on a publicly observable board state delta. Played in Faction Resolution Grid.
    # trigger: required (never None) — defines what activates the card; overrides Card.trigger default
    # beat:    always None — React fires on trigger condition, not at a named beat
    # Field constraints: §6.2.
    value_rating:     int | None            # 1–3; None = TBD (stub only)
    ring_constraint:  Ring | None          # None = no deployment restriction; Ring = fires only when trigger fires in that ring
    ring_origin:      Ring | None          # None = faction modifier deck; 1/2/3 = drawn from that ring's modifier deck
```

---

### 6.2 Data Dictionary

| Field | Class | Type | Purpose | Displayed |
|-------|-------|------|---------|-----------|
| is_unique | Pool | bool | True = at most 1 copy in active deck; applies to Operative and Apex cards; False for all others | No |
| deck_limit | Pool | int \| None | Max copies of this card in the faction's active deck; None = no per-card limit (pool size governed by §10 rules only) | No |
| card_id | Identity | CardID | Canonical card identifier — `[FAC].[TYPE].n` per L219; registry: `card_ref` | TBD |
| id | Identity | str | Legacy sequence integer (e.g., `id=42`); preserved in specs for traceability | TBD |
| version | Identity | Semver | Per-card revision — v[major].[minor]; independent of Art 04 version | TBD |
| name | Identity | str | In-world card name — not a mechanical label | Face |
| tagline | Identity | str | One-line in-world description | Face |
| type | Identity | CardType | Top-level card category — governs deck assignment and resolution handling | TBD |
| subtype | Identity | Subtype | Distribution scope | TBD |
| faction | Identity | Faction | Owning faction — All = standard card; named faction = faction-specific | TBD |
| layer | Taxonomy | Layer | Action taxonomy layer — see Art 04b §4 | TBD |
| function | Taxonomy | Function | Action taxonomy function — see Art 04b §4 | TBD |
| subject | Taxonomy | Subject | Action taxonomy subject — see Art 04b §4 | TBD |
| beat | Metadata | int | Phase 6 beat this card resolves in; order within beat = dispatch case submission order (Art 03 §7) | TBD |
| resolution | Metadata | Resolution | d100 = probability roll; Automatic = guaranteed, fires on submission | Face |
| threshold | Metadata | int | Base difficulty as numeric threshold; None when Automatic | Face |
| ring_mod | Metadata | dict[Ring, int] | Per-ring threshold adjustment; positive = easier, negative = harder; None when no variation | Face |
| doctrine_mod | Metadata | dict[PentagramRelation, int] | Per-doctrinal-relationship threshold adjustment based on acting/target faction pentagram proximity; positive = easier, negative = harder; None when no faction target or no doctrinal variation | Face |
| trigger | Metadata | TriggerExpr | Activation condition when card does not fire at default beat timing; None = default | TBD |
| resolution_type | Metadata | str | Strategic classification of how uncertainty resolves — evolving vocabulary; feeds 00c §8 | No |
| outcome_type | Metadata | OutcomeType | Public act resolution process type; None for covert operations | Face |
| persistence | Metadata | Persistence | How long the card remains on the table as a game state marker — Immediate: removed at Beat 4 cleanup; Transient: removed at Close Month of current Month; Seasonal: removed at Phase 21 (End of Quarter); Permanent: removed only by explicit game action. Default for covert operations: Immediate. PA cards with active board-condition effects must use Transient or Seasonal. | Face |
| persistence_condition | Metadata | BoolExpr | Condition that must remain True for a Permanent card to stay in play; card is discarded immediately when it evaluates False. None for all non-Permanent cards. | Face |
| persistence_effect | Metadata | MutationExpr | Ongoing board condition active while a Permanent card is in play; evaluated continuously until persistence_condition is met. Use `game.board_condition(...)` to express scoped persistent effects. None for all non-Permanent cards. | Face |
| target_district | Targeting | DistrictExpr | District scope for the card's effect | Face |
| target_faction | Targeting | FactionExpr | Faction this card targets; None = no faction target | Face |
| target_object | Targeting | ObjectExpr | Game component this card acts on; None = no object target | Face |
| target_taxonomy | Targeting | TaxonomyExpr | Action taxonomy category this card targets (Layer/Function or Layer/Function/Subject); used when the effect targets a class of actions rather than a specific object; declared at Phase B alongside target_faction; None = no taxonomy target | Face |
| affinity | Logic | ConditionalExpr | Faction-based cost modifier — evaluated before cost expression | Face |
| restriction | Logic | BoolExpr | Submission preconditions — card unplayable if evaluates False | Face |
| cost | Logic | CostExpr | Physical, fungible resources consumed at submission — valid cost resources are those that can be traded or transferred (Mandate, Capital, Influence, district native resource). Non-fungible markers (Public Standing, presence tiers) are not valid cost values; marker changes that function as a cost belong in `success`/`fail` effect fields. | Face |
| boost | Logic | BoostExpr | Optional variable-multiplier mechanic — player submits additional resources beyond base cost; no declaration required. ARBITER detects at Beat 0: n = (total submitted − base cost) / boost unit cost; places n BoostMarker tokens (BM-xx) on the card's grid slot alongside the card. At Beat 2/3 resolution: effect fires (1 + BM-xx count) times; BM-xx returned to ARBITER supply at beat cleanup. For threshold-scaling cards, threshold is locked at Beat 0 using total count (1 + BM-xx). Boost unit cost may differ from base cost resource type. None = no boost mechanic. | Face |
| success | Effects | MutationExpr | Primary effect on resolution success | Face |
| successcrit | Effects | MutationExpr | Additive delta on critical success (roll ≤ 5, i.e. 01–05); None when Automatic | Face |
| fail | Effects | MutationExpr | Effect on failure; None = cost spent, no additional effect | Face |
| failcrit | Effects | MutationExpr | Additive delta on critical failure (roll ≥ 96, i.e. 96–00); None when Automatic | Face |
| on_accept | Effects | MutationExpr | ElectPlayer outcome type only — effect applied when target accepts the offer at resolution; None when outcome_type ≠ ElectPlayer | Face |
| on_decline | Effects | MutationExpr | ElectPlayer outcome type only — effect applied when target declines the offer at resolution; None when outcome_type ≠ ElectPlayer | Face |
| portrait | Portrait | dict[Faction, PortraitEntry] | Per-faction portrait scoring — evaluated by ARBITER; analyzed in DB | TBD |
| ps_framing | Public Standing | PSFraming \| None | Structured public-reception PS model. `type`: probabilistic (D100 roll at trigger) or fixed (unconditional). `trigger`: resolution (Beat 4 PA), discovery (covert failcrit only), or placement (on card placement). `threshold`: D100 roll target; probabilistic only. `on_success`/`on_fail`: lists of PSShift (faction + delta). Probabilistic PA default on_fail: acting −1. None = card produces no PS shift. | Face |
| narrative | Narrative | str | In-world narrative grounding — one sentence; neutral observer (standard) or owning faction voice (faction-specific) | TBD |
| perspectives | Narrative | dict[Faction, str] | Per-faction in-world perspective — one sentence per faction | TBD |
| design_note | Narrative | str | Design intent — doctrine rationale, Art 11 layout context | No |
| arbiter_note | Narrative | str | ARBITER resolution guidance — timing, edge cases, table validation | No |

---

#### Modifier Subclass Fields

Fields added by ModActionCard, ModBattleCard, and ModReactCard. All three subclasses also inherit the full Card field set; always-None fields per subclass are listed in the table below.

| Field | Subclass | Type | Purpose | Displayed |
|-------|----------|------|---------|-----------|
| effect | ModActionCard | ModActionExpr | Tagged union — exactly one: threshold_delta(n) \| success_multiplier(n) \| ps_shift(faction, delta) \| cost_reduction(n); cost_reduction is PA ops only (CA cost committed at dispatch before Beat 0) | Face |
| effect | ModBattleCard | ModBattleExpr | Threshold delta applied to submitting faction (Self) or opponent (Opponent) during Battlefield Strength resolution | Face |
| value_rating | All modifier subclasses | int \| None | 1–3; modifier strength signal printed on card face; used in Splay calculation; None = TBD (stub only — must be set before design pass) | Face |
| ring_constraint | All modifier subclasses | Ring \| None | Deployment restriction set at card design time by narrative — location-anchored assets get the ring value; portable assets get None. ModActionCard: usable only with ops targeting that ring's districts. ModBattleCard: usable only in Battlefield Strength for a district in that ring. ModReactCard: fires only when trigger condition occurs in that ring's districts. | Face |
| ring_origin | All modifier subclasses | Ring \| None | Which modifier deck this card belongs to — None = faction modifier deck; 1/2/3 = Ring 1/2/3 modifier deck. Determines draw eligibility (§11.2) and card back color. Separate from ring_constraint: a Ring 1 card (ring_origin=1) may have ring_constraint=None (portable, no deployment restriction). | No |

#### Modifier Subclass Field Constraints

Which inherited Card fields are always None vs. per-card design vs. required. `None` = always None for that subclass; `—` = inherits from Card class, value set per individual card design; `Required` = must be non-None.

| Field | ModActionCard | ModBattleCard | ModReactCard |
|-------|--------------|--------------|--------------|
| layer / function / subject | None | None | — |
| beat | None — fires with host action | None | None — fires on trigger |
| resolution / threshold | None | None | — |
| ring_mod / doctrine_mod | None | None | — |
| trigger | None — fires when bundled | None | **Required** — never None |
| resolution_type | None | None | — |
| outcome_type | None | None | — |
| persistence / persistence_condition / persistence_effect | None | None | — |
| target_district / target_faction / target_object / target_taxonomy | None | None | — |
| affinity / restriction | — | None | — |
| boost | None | None | — |
| success / successcrit / fail / failcrit | None | None | — |
| on_accept / on_decline | None | None | — |
| ps_framing | None | None | — |
| perspectives / design_note | — | None | — |

*ModReactCard: only `beat` is always None. All other `—` fields are live — set per individual card design.*

---

### 6.3 Enum Vocabularies

```
CardType:     CovertOperation | PublicAct | Pass | Countermeasure | Modifier | EmergencyResponse
Subtype:      Standard | FactionSpecific
Faction:      All | Ghost | Network | Syndicate | Guild | Directorate
Layer:        Territory | Economy | Information | Submission | Resolution | Standing
Function:     → Art 04b §4
Subject:      → Art 04b §4
Resolution:   d100 | Automatic
Ring:                0 (Chorus Node) | 1 (Core) | 2 (The Mid) | 3 (Baryo)
PentagramRelation:   Neighbor | Opposed
OutcomeType:         Binary | ElectPlayer | ElectDistrict | ElectFaction | BilateralAgreement | Unilateral
Persistence:         Immediate | Transient | Seasonal | Permanent

PSFramingType:       probabilistic | fixed
PSFramingTrigger:    resolution | discovery | placement
PSTarget:            acting | target | both

BoostExpr:           condition: CostExpr
# condition: BoolExpr — when the boost mechanic is available to the acting player
# CostExpr: per-unit cost for each additional success instance beyond the first
# No Phase B declaration — player submits resources implying n; ARBITER counts at Beat 0
# Submitted resources must be an exact multiple of boost unit cost (no partial units)
# Boost condition False + excess resources submitted: Beat 0 rejects as invalid cost
# Physical: ARBITER places n BM-xx (BoostMarker) tokens on card's grid slot at Beat 0
# Resolution (Beat 2/3): effect fires (1 + BM-xx count) times; BM-xx returned to ARBITER supply at beat cleanup
# Threshold-scaling cards: threshold locked at Beat 0 using (1 + BM-xx count) as total n

TriggerExpr:         Any
                     | component[.scope][.attribute].change(faction)
# component:   presence_chip | structure_block | deployment_marker | dominant_marker |
#              established_marker | tension_marker | standing_marker | world_event |
#              accord | resolution_grid
# scope:       ring1 | ring2 | ring3 | district.{id} | global  (optional filter)
# attribute:   optional sub-state filter on component (e.g., influence level, chip count)
# change:      placed | removed | converted | blocked | increased | decreased |
#              played | expired | corrupted | updated
# faction:     Any | Ghost | Network | Syndicate | Guild | Directorate
#
# Confirmed React trigger set (sourced from Art 03b + Art 02; public-only):
#   presence_chip.placed / removed
#   structure_block.placed / removed
#   deployment_marker.placed / converted / blocked     (blocked = Blocked-face flip)
#   dominant_marker.placed / removed                   (Dominant status change)
#   established_marker.placed / removed
#   tension_marker.placed / removed                    (Contested condition)
#   standing_marker.increased / decreased              (PS track shift at Beat resolution)
#   world_event.played / expired
#   accord.placed / corrupted / removed              (accord.removed: Accord breach or expiry — S128)
#   resolution_grid.updated                            (after Beat 0 public reveal)
#   broadcast_card.placed                              (db25 — public SitRep card placed in Situation Report Zone; fires at Upkeep phase 1 and Beat 5 phase 18; added S128)
#
# Excluded (static — never change): district tiles, board geography, ARBITER Dominance Marker
# Excluded (procedural — not player-driven): Initiative Strip, Session Timeline, Quarter/Month markers

ModActionExpr:       threshold_delta(n: int)
                     | success_multiplier(n: int)
                     | ps_shift(faction: str, delta: int)
                     | cost_reduction(n: int)
# threshold_delta:    +n or −n applied to host action threshold; valid for CA and PA
# success_multiplier: effect fires additional n times; valid for CA and PA
# ps_shift:           faction = "acting" | "target" | named faction; valid for CA and PA
# cost_reduction:     reduce PA cost by n resources; PA ops only
#                     (CA cost committed at dispatch before Beat 0; cannot be reduced post-submission)
# Tagged union — exactly one effect expression per card

ModBattleExpr:       direction: Self | Opponent
                     magnitude: int
# Self:    +magnitude applied to submitting faction's Battlefield Strength threshold
# Opponent: −magnitude applied to opponent's threshold
```

---

### 6.4 Visibility Rules

Three rules replace per-field VS-xx notation:

- **VS-01 (Public):** All fields not listed below
- **VS-04 (ARBITER-only):** `design_note`, `arbiter_note`
- **VS-06 (Hidden until resolution):** `success`, `successcrit`, `fail`, `failcrit`, `portrait`

---

### 6.5 Modifier Baselines

Design guidance for `ring_mod` and `doctrine_mod`. Not locked — adjust based on narrative justification per card. Deviations should be noted in the card's Design Rationale.

**ring_mod baseline:**

| Ring | Modifier | Design rationale |
|------|----------|-----------------|
| 0 (Chorus Node) | −15 | Densest institutional presence; hardest operational environment |
| 1 (Core) | −10 | Established authority; significant friction |
| 2 (The Mid) | 0 | Baseline — standard operational environment |
| 3 (Baryo) | +10 | Looser structures; easier to operate |

**doctrine_mod baseline:**

| PentagramRelation | Modifier | Design rationale |
|-------------------|----------|-----------------|
| Neighbor | +15 | Capital flows more easily between doctrinally aligned factions |
| Opposed | −15 | Capital faces resistance crossing doctrinal distance |

*Applies only when `target_faction` is set. `doctrine_mod = None` when card has no faction target. Pentagram arrangement: Art 00 §7. L174.*

---

---

---

## 7. Card Specifications

[Standard](#standard) · [Guild](#guild) · [Ghost](#ghost) · [Directorate](#directorate) · [Network](#network) · [Syndicate](#syndicate)

---

## Standard
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#standard-covert-operations) · [Public Acts](#standard-public-acts)

---

### Standard — Covert Operations
[↑ Standard](#standard)

| Card | Name |
|------|------|
| [STD.CA.1](#c01-build-structure) | Build Structure |
| [STD.CA.2](#c02-demolish) | Demolish |
| [STD.CA.3](#c03-campaign) | Campaign |
| [STD.CA.4](#c04-undermine) | Undermine |
| [STD.CA.5](#c05-gather) | Gather |
| [STD.CA.6](#c06-broadcast-interference) | Broadcast Interference |
| [STD.CA.7](#c07-amplify) | Amplify |
| [STD.CA.8](#c08-buy-influence) | Buy Influence |
| [STD.CA.9](#c09-fund) | Fund |
| [STD.CA.10](#c10-protect) | Protect |
| [STD.CA.12](#c39-absolute-compromise) | Absolute Compromise |
| [—](#standard-disinformation-campaign) | Disinformation Campaign |
| [—](#standard-disprove) | Disprove |
| [—](#standard-intel-extraction) | Intel Extraction |
| [—](#standard-modifier-raid) | Modifier Raid |

### STD.CA.1 — BUILD STRUCTURE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Territory-control foundation card. Construction is publicly visible — the covert element is intent, not the act. Every faction must establish structured positions to hold territory; this is the universal mechanism. Cost vs reward: dual cost (1 faction native + 1 district native) models that building requires both faction resources and local knowledge; Automatic resolution is appropriate if prerequisites are met. Guild affinity waives the district-native cost: the Guild *is* the city's builder and does not purchase access to their own infrastructure ecosystem.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Physical construction as territorial assertion is core to New Meridian. The covert element is unannounced intent — the visible act is public. All five factions acknowledge building as a valid form of presence. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | All five perspectives are doctrinally distinct. Guild's "permanence is possible here" is the foundational argument; Syndicate's "the question is who captures it" reframes construction as economic extraction; Ghost's "commitments are data points" is cold and analytical. No faction sounds like another. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | Building directly serves Guild doctrine (permanence, structural investment). Captured via portrait submitter=+1 and cost affinity. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: every faction must establish structure; no faction-specific exclusivity warranted. CovertOperation: unannounced intent is the covert element, not the visible act. Fills the universal territorial foundation role — no standard card duplicates it. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Add / StructureBlock — unambiguous. Layer is Territory because the target is a StructureBlock, not because of the Add verb. | Art 04b §4 |
| Balance | ✓ | Automatic resolution gated by dual cost + presence prerequisite + no-existing-structure restriction. Not independently playable without prior presence. Guild affinity waives district native only — cost-scoped, not difficulty. | Art 02 §6–§7 |
| Effect duration | ✓ | No duration — structure placement is permanent; persists until removed. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`: permanence doctrine — core alignment (DIR.PA.1, SYN.PA.2). Ghost `submitter=−1`: structure is a permanent visible commitment; Ghost doctrine is concealment, not construction (DIR.PA.1, SYN.PA.2). Directorate: no entry — builds pragmatically ("if it serves the mandate"); instrumental, not doctrinal. Network: no entry — presence-building via community relationships (STD.CA.3), not structures; observational stance confirms absence. Syndicate: no entry — doctrine is acquisition and capital flow; "who captures it" is observer framing, not builder framing. No direct Portrait track shift in effect fields (DIR.PA.2). All entries submitter-bounded (SYN.PA.2). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any` — valid. Ring entry implicit via presence requirement in restriction. | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock (Art 02 §6); presence token / deployment marker in restriction (Art 02 §6); faction native + district native cost (Art 02 §7). | Art 02 §6–§7 |
| Supported by game procedure | ✓ | Submitted in Dispatch (Art 03 §9.1); Beat 3 Resolution Grid (Art 03 §9.4). ARBITER places Structure Block at Beat 3 outcome. Guild affinity evaluated at dispatch. | Art 03 §9, §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | ✓ S63 |

```python
STD.CA.1 = Card(
    id      = "STD.CA.1",  version = "v1.1",
    name    = "Build Structure",
    tagline = "Construct a physical installation in a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Add,  subject = StructureBlock,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Guild: cost.resource.district(native) = 0,
    restriction = (
        district(target).faction(acting).presence > 0 and
        district(target).faction(acting).structure == 0
    ),
    cost = resource.faction(acting) * 1 + resource.district(native) * 1,

    success     = district(target).faction(acting).structure += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Guild: PortraitEntry(submitter=+1),
        Ghost: PortraitEntry(submitter=-1),
    },

    narrative    = "Every faction that wants to matter in New Meridian eventually has to build something.",
    perspectives = {
        Guild:       "This is what we do. Every structure we build is an argument that permanence is possible here.",
        Directorate: "Infrastructure serves order. We will use it if it serves the mandate.",
        Network:     "Building is a statement of intent. We watch carefully to understand what kind.",
        Ghost:       "A structure is a commitment. Commitments are data points.",
        Syndicate:   "Every structure generates value. The question is who captures it.",
    },
)
```

---

### STD.CA.2 — DEMOLISH
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Territory disruption card — the destructive mirror of STD.CA.1. Structure removal is publicly visible; source of removal is not announced. Cost vs reward: dual cost (1 faction native + 1 district native) reflects that demolition requires both capability and local knowledge; probabilistic resolution models genuine resistance — you do not control what you are destroying. Crit success yields salvage (1 native recovered); crit fail costs Public Standing, representing the reputational risk of publicly-failed covert demolition.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Demolition as covert territorial disruption is grounded — the act is visible, the source is not. The asymmetry with STD.CA.1 (probabilistic vs. Automatic) correctly reflects operating against someone else's infrastructure rather than your own. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Guild's "something has gone badly wrong" and Network's "infrastructure of control needs to come down" are the sharpest contrast in the set. Ghost's absence-as-data read is clean. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` is set; `doctrine_mod = None` is an explicit design choice — demolition difficulty reflects physical opportunity (ring, restriction), not doctrinal relationship. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions engage in demolition as territorial disruption. CovertOperation: source undisclosed. Distinct from STD.CA.1 — Remove vs. Add, probabilistic vs. Automatic. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Remove / StructureBlock. Layer is Territory because the target is a StructureBlock. | Art 04b §4 |
| Balance | ✓ | Same dual cost as STD.CA.1, probabilistic at threshold 50. Ring_mod {0:−15, 1:−10, 2:0, 3:+10} — harder near Chorus Node. Crit success salvage rewards execution; crit fail PS loss is a meaningful downside. | Art 02 §6–§7 |
| Effect duration | ✓ | No duration — structure removal is permanent; persists until rebuilt. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: demolition against permanence doctrine — "we do not unmake" (DIR.PA.1, SYN.PA.2). Network `submitter=+1`: counter-entrenchment doctrine — removing infrastructure of control is on-doctrine (DIR.PA.1, SYN.PA.2). Directorate `submitter=−1`: structures represent institutional investment; doctrinal reluctance parallels STD.CA.4 (DIR.PA.1, SYN.PA.2). Ghost: no entry — analytical observer, not demolition-as-doctrine; absence justified. Syndicate: no entry — pragmatic asset-management framing, no doctrinal signal; absence justified. `failcrit standing -= 1` is Public Standing (Art 02), not Portrait — DIR.PA.2 clear. | Art 04 §6.2; Art 02 §11 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction uses self-or-adjacent presence — adjacency model required; district_adjacency confirmed (DB-09 ✅ S50). | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock target (Art 02 §6); presence in restriction (Art 02 §6); dual cost (§8); failcrit `standing -= 1` (Art 02 §11). | Art 02 §6–§8; Art 02 §11 |
| Supported by game procedure | ✓ | Dispatch (Art 03 §9.1); Beat 3 Resolution Grid (Art 03 §9.4.2); d100 threshold 50 with ring_mod. ARBITER removes Structure Block on success; standing loss on crit fail — Beat 3 outcome steps. | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | ✓ S63 |

```python
STD.CA.2 = Card(
    id      = "STD.CA.2",  version = "v1.1",
    name    = "Demolish",
    tagline = "Remove an opponent's structure from a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Remove,  subject = StructureBlock,

    beat            = 3,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = StructureBlock,

    target_taxonomy=None,
    affinity    = None,
    restriction = (
        district(self|adjacent).faction(acting).presence > 0 and
        district(target).faction(target).structure > 0
    ),
    cost = resource.faction(acting) * 1 + resource.district(native) * 1,

    success     = district(target).faction(target).structure -= 1,
    successcrit = resource.faction(acting).native += 1,
    fail        = None,
    failcrit    = faction(acting).standing -= 1,

    portrait = {
        Guild:       PortraitEntry(submitter=-1),
        Network:     PortraitEntry(submitter=+1),
        Directorate: PortraitEntry(submitter=-1),
    },

    narrative    = "Not everything built in New Meridian was meant to last.",
    perspectives = {
        Guild:       "We build. We do not unmake. Every time we perform this action something has gone badly wrong.",
        Directorate: "Demolition is a last resort. Structures represent investment in the city we are here to protect.",
        Network:     "Sometimes the infrastructure of control needs to come down before something better can be built.",
        Ghost:       "A demolished structure tells us as much as a standing one. We note the absence.",
        Syndicate:   "Assets change hands. Sometimes the most efficient transfer is removal.",
    },
)
```

---

### STD.CA.3 — CAMPAIGN
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Presence-deepening card — a deliberate structural parallel to STD.CA.1. To Campaign, you must already be present; this is not an entry card. Cost vs reward: dual cost mirrors STD.CA.1 (same principle, same gate). Automatic resolution because you're operating within your own established footprint, not against opposition. Network affinity waives the district-native cost because Network growth is relational, not material — it does not purchase access to local infrastructure.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Presence-deepening in a district you already occupy is grounded. Campaign is relational/operational deepening of an existing footprint — distinct from entry. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Ghost's "presence creates exposure" explains why Ghost doesn't over-extend; Network's "relationships are how things actually change" directly justifies the affinity. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | Presence-deepening through community relationships directly serves Network doctrine (relational growth). Captured via portrait submitter=+1 and cost affinity. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions build presence. CovertOperation: presence-building is done quietly. Structurally mirrors STD.CA.1 (presence vs. structure) — distinct role, not duplicative. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken. Layer is Territory because the target is a PresenceToken. | Art 04b §4 |
| Balance | ✓ | Automatic gated by presence prerequisite — same structure as STD.CA.1. Network affinity waives district native (relational, not material). Intentional cost symmetry with STD.CA.1. | Art 02 §6–§7 |
| Effect duration | ✓ | No duration — presence placement is permanent until removed. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Network `submitter=+1`: relational growth is doctrinally core (DIR.PA.1, SYN.PA.2). Guild: no entry — STD.CA.1/structural investment is Guild's primary presence signal; Campaign is available but not doctrinally distinct; absence justified. Directorate: no entry — presence-building is instrumental ("where the mandate requires it"), not doctrinal; absence justified. Ghost: no entry — "presence creates exposure" frames expansion as calculated exception, not doctrinal endorsement; absence justified. Syndicate: no entry — community presence-building is not Syndicate's mode; capital and acquisition is; absence justified. No direct Portrait track shift in effect fields (DIR.PA.2). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Ring entry implicit via presence restriction. | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); faction native + district native cost (Art 02 §7). | Art 02 §6, §7 |
| Supported by game procedure | ✓ | Dispatch (Art 03 §9.1); Beat 3 Resolution Grid (Art 03 §9.4). ARBITER places PresenceToken on success. Network affinity evaluated at dispatch. | Art 03 §9, §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | ✓ S63 |

```python
STD.CA.3 = Card(
    id      = "STD.CA.3",  version = "v1.1",
    name    = "Campaign",
    tagline = "Build local support and deepen presence in a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Add,  subject = PresenceToken,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Network: cost.resource.district(native) = 0,
    restriction = district(target).faction(acting).presence > 0,
    cost        = resource.faction(acting) * 1 + resource.district(native) * 1,

    success     = district(target).faction(acting).presence += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Network: PortraitEntry(submitter=+1)},

    narrative    = "Presence without roots is just occupation.",
    perspectives = {
        Guild:       "Presence is the foundation everything else is built on. We are methodical about this.",
        Directorate: "Authority requires visibility. We establish presence where the mandate requires it.",
        Network:     "Every person we reach in a district is a relationship. Relationships are how things actually change.",
        Ghost:       "Presence creates exposure. We expand only when the intelligence justifies the risk.",
        Syndicate:   "Market position requires footprint. We place ourselves where the returns justify it.",
    },
)
```

---

### STD.CA.4 — UNDERMINE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Presence-disruption card — the destructive mirror of STD.CA.3, following the same build/demolish asymmetry as STD.CA.1/STD.CA.2. Probabilistic because you're operating against someone else's established footing. Cost vs reward: same dual cost as STD.CA.3; crit success doubles effect (−2 presence), crit fail costs PS. Portrait is selective: Guild and Directorate are negatively disposed to undercutting presence (institutional stability preference); Network is affirmative (disruption aligns with its counter-entrenchment doctrine). Ghost and Syndicate are absent — neither is doctrinally committed to presence disruption as a default.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert erosion of opponent presence is grounded — source undisclosed, structural parallel to STD.CA.2. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Directorate's conditional ("unless the target is The Network — then it is public safety") maps directly to the `where=faction(target) != Network` portrait exception. Ghost's "we prefer signal" explains their absence from affinity. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` set; `doctrine_mod = None` — explicit design choice. Doctrinal relationship does not affect disruption difficulty; ring_mod handles variation. Same rationale as STD.CA.2. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions engage in presence disruption. CovertOperation: source undisclosed. Distinct from STD.CA.2 (presence vs. structure). | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Remove / PresenceToken. Layer is Territory because the target is a PresenceToken. | Art 04b §4 |
| Balance | ✓ | Same dual cost as STD.CA.3. Crit success = −2 total (success + successcrit additive) — intentionally stronger than STD.CA.2 salvage; presence erosion compounds. Crit fail PS loss mirrors STD.CA.2. | Art 02 §6–§7 |
| Effect duration | ✓ | No duration — presence removal is permanent until replenished. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: undermining presence is doctrinally incongruent — "we do not erase what others have built" (DIR.PA.1, SYN.PA.2). Directorate `submitter=−1, where=faction(target) != Network`: covert erosion conflicts with governance doctrine; exception when targeting Network — framed as "public safety," no doctrinal conflict; `where=` constrains by target identity, not outcome (DIR.PA.1, SYN.PA.2). Network `submitter=+1`: counter-entrenchment doctrine — eroding entrenched presence is on-doctrine (DIR.PA.1, SYN.PA.2). Ghost: no entry — "disruption without intelligence purpose is noise"; presence disruption is not Ghost's primary mode; absence justified. Syndicate: no entry — pragmatic observer framing, no doctrinal stake in presence disruption; absence justified. `failcrit standing -= 1` is Public Standing (Art 02), not Portrait — DIR.PA.2 clear. | Art 04 §6.2; Art 02 §11 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction requires self-or-adjacent presence AND target has presence > 0. Adjacency model required. | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken in restriction and as target (Art 02 §6); dual cost (Art 02 §7); failcrit `standing -= 1` (Art 02 §11). | Art 02 §6, §7; Art 02 §11 |
| Supported by game procedure | ✓ | Dispatch (Art 03 §9.1); Beat 3 Resolution Grid (Art 03 §9.4.2); d100 threshold 50 with ring_mod. ARBITER removes PresenceToken on success; double on crit success; standing loss on crit fail — Beat 3 outcome steps. | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | ✓ S63 |

```python
STD.CA.4 = Card(
    id      = "STD.CA.4",  version = "v1.1",
    name    = "Undermine",
    tagline = "Erode an opponent's presence in a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Remove,  subject = PresenceToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = PresenceToken,

    target_taxonomy=None,
    affinity    = None,
    restriction = (
        district(self|adjacent).faction(acting).presence > 0 and
        district(target).faction(target).presence > 0
    ),
    cost        = resource.faction(acting) * 1 + resource.district(native) * 1,

    success     = district(target).faction(target).presence -= 1,
    successcrit = district(target).faction(target).presence -= 1,
    fail        = None,
    failcrit    = faction(acting).standing -= 1,

    portrait = {
        Guild:       PortraitEntry(submitter=-1),
        Directorate: PortraitEntry(submitter=-1, where=faction(target) != Network),
        Network:     PortraitEntry(submitter=+1),
    },

    narrative    = "The most effective opposition leaves no visible wound.",
    perspectives = {
        Guild:       "We do not erase what others have built. Even our enemies.",
        Directorate: "Covert erosion is not governance. Unless the target is The Network — then it is public safety.",
        Network:     "Entrenched presence does not become legitimate just because it has been there long enough.",
        Ghost:       "Disruption without intelligence purpose is noise. We prefer signal.",
        Syndicate:   "If their presence can be eroded, it was never well-positioned to begin with.",
    },
)
```

---

### STD.CA.5 — GATHER
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Universal intelligence card — the baseline for the Information layer. Observation does not consume local infrastructure, hence faction-native-only cost. Ghost adjacency exemption is doctrinal: remote analysis does not require physical proximity. Crit success is additive (both `success` and `successcrit` dispatch the same token type — 2 Intel Tokens total on crit). Crit fail reveals the attempt to the target, creating genuine operational risk for careless intelligence-gathering.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence-gathering as a covert baseline is grounded. Ghost's adjacency exemption (remote analysis, L69) is doctrinally accurate. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Ghost's "this is what we are here for" makes the affinity mechanically legible. Network's "gaps between what is said and what is true" is the sharpest perspective. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` set; `doctrine_mod = None` — explicit choice. Intelligence-gathering effectiveness doesn't vary by doctrinal relationship. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions gather intelligence. CovertOperation: observation is covert. Ghost adjacency exemption is a doctrinal exception to the restriction, not a subtype change. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Information` — intelligence-gathering generates IntelToken; dominant design intent is information acquisition, consistent with Art 04b §4.4. `doctrine_mod = None` — correct, doctrinal proximity does not affect intel-gathering effectiveness. | Art 04b §4 |
| Balance | ✓ | Single faction-native cost — cheapest intel card. Ghost effective threshold 75 (50+25 affinity). Crit success = 2 tokens total (additive). Crit fail NotificationSlip creates real operational risk. | Art 02 §7, §8, §9 |
| Effect duration | ✓ | No duration — Intel Token is a durable resource that persists until spent. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Ghost `submitter=+1`: intelligence-gathering is core doctrine — "this is what we are here for" (DIR.PA.1, SYN.PA.2). Network: no entry — intel is a tool for Network, not their primary mode; relational growth and communication are doctrinal (absence justified). Guild: no entry — pragmatic use only; "we gather when we need to build smarter" (absence justified). Directorate: no entry — prefers formal collection; covert gathering is a tool, not a belief (absence justified). Syndicate: no entry — transactional framing, no doctrinal signal (absence justified). `failcrit` dispatches NotificationSlip — game effect, not Portrait shift (DIR.PA.2 clear). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: presence in self-or-adjacent OR Ghost exemption. | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Art 02 §9); faction native cost (Art 02 §7); failcrit NotificationSlip (Art 02 §8 — subtype definition pending). | Art 02 §7, §8, §9 |
| Supported by game procedure | ✓ | Dispatch (Art 03 §9.1); Beat 3 Resolution Grid (Art 03 §9.4.2); d100 threshold 50 with Ghost affinity. ARBITER delivers IntelToken on success, NotificationSlip to target on crit fail — Art 03 Beat 3 outcome steps (per L170; Art 07 ref is stale). | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
STD.CA.5 = Card(
    id      = "STD.CA.5",  version = "v1.1",
    name    = "Gather",
    tagline = "Extract actionable intelligence about a specific faction's operations.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Information,  function = Add,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Ghost: threshold += 25,
    restriction = (
        district(self|adjacent).faction(acting).presence > 0 or
        faction(acting) == Ghost
    ),
    cost        = resource.faction(acting) * 1,

    success     = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)),
    successcrit = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)),
    fail        = None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "In New Meridian, knowing is the first form of power.",
    perspectives = {
        Guild:       "Intelligence informs construction. We gather when we need to build smarter.",
        Directorate: "Information is the foundation of legitimate authority. We collect it formally.",
        Network:     "The city speaks constantly. We listen for the gaps between what is said and what is true.",
        Ghost:       "This is what we are here for. Everything else follows from understanding.",
        Syndicate:   "Information has market value. We acquire it when the return justifies the cost.",
    },
)
```

---

### STD.CA.6 — BROADCAST INTERFERENCE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Submission-layer Beat 2 card — places a cost modifier on Public Acts targeting a district this round. Broadcast interference is ambient, hence no presence requirement. Cost is Exposure-denominated: non-Network factions must acquire Exposure through incursion or trade, making this card natively affordable only to the Network. Network affinity reduces cost by 1 (net: 1 Exposure), making it a low-friction tactical tool for Network while remaining expensive for others.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Broadcast disruption as covert intelligence operation: ambient signal interference requires no physical presence in the district. No faction presence requirement is correct — you don't need to be there to jam a signal. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Tagline clear and grounded. Five perspectives doctrinally distinct: Guild (operational delays), Directorate (jurisdictional note), Network (strategic noise), Ghost (analytical cover), Syndicate (market inefficiency). | Art 00 §7 |
| Doctrine alignment | ✓ | Network is the primary aligned faction — signal disruption as tactical information control. Ghost benefits doctrinally (analytical cover). Directorate opposed — covert disruption conflicts with their institutional-authority doctrine. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: disruption mechanism is hidden even if cost increase is observable at Beat 4. Standard: all factions can disrupt broadcast infrastructure. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Submission` — modifies cost of a PA (submission-phase property). `function = Modify`, `subject = PublicAct` — correctly scoped and narrow. | Art 04b §4, §5 |
| Balance | ✓ | Beat 2 positional wager. Cost 2 Exposure (1 for Network via affinity). Raises PA cost +1 native — meaningful deterrence, not a hard block. No fail state. | Art 03 §9.4 |
| Effect duration | ✓ | Single-round: arms at Beat 2, applies at Beat 4, does not persist. Appropriate for a tactical cost modifier. | Art 03 §10 |
| Persistence | ✓ | Immediate — Beat 2 carry; applied at Beat 4 via Resolution Grid; no game-state marker persists beyond round | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Network `submitter=+1`: tactical information control — primary aligned faction (DIR.PA.1, SYN.PA.2). Ghost `submitter=+1`: interference creates analytical cover, consistent with Ghost's low-profile doctrine (DIR.PA.1, SYN.PA.2). Directorate `submitter=−1`: covert disruption undermines institutional legitimacy; Directorate's tool is regulatory authority, not anonymous interference (DIR.PA.1, SYN.PA.2). Guild: no entry — operational delays are a cost, not a doctrinal signal; absence justified. Syndicate: no entry — market inefficiency is an opportunity, not a doctrinal stake; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. No presence restriction — broadcast effect is ambient to the district. | Art 01 §6 |
| Supported by components | ✓ | PublicAct as target type; Exposure resource as cost. Both defined. | Art 02 §8; Art 04b §5 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); placed in Beat 2 row at Resolution Grid setup (Art 03 §9.4.0); moved to Beat 4 carry row during Beat 2 processing (Art 03 §9.4.2); arming and effect applied at Beat 4 (Art 03 §9.4.3). | Art 03 §9, §9.4, §10 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | ✓ S63 |

```python
STD.CA.6 = Card(
    id      = "STD.CA.6",  version = "v1.1",
    name    = "Broadcast Interference",
    tagline = "Disrupt public communications in a district, dampening public activity.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Submission,  function = Modify,  subject = PublicAct,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Positional wager",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = PublicAct,

    target_taxonomy=None,
    affinity    = faction(acting) == Network: cost.resource.exposure -= 1,
    restriction = None,
    cost        = resource.faction(acting).exposure * 2,

    success     = game.ops(beat=4, type=PublicAct, at=district(target)).cost.native += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Network:     PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=+1),
        Directorate: PortraitEntry(submitter=-1),
    },

    narrative    = "People don't act naturally when they know they're being watched.",
    perspectives = {
        Guild:       "Disrupting communications delays approvals, permits, agreements. We feel this more than most.",
        Directorate: "Interference with public communications is a jurisdictional matter. We note who is responsible.",
        Network:     "Noise is a tool. Sometimes silence is louder than anything we could broadcast.",
        Ghost:       "Interference creates analytical cover. We appreciate the quiet.",
        Syndicate:   "Disrupted communications create market inefficiencies. Those can be profitable.",
    },
)
```

---

### STD.CA.7 — AMPLIFY
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Beat 2 modifier for the acting faction's own Public Act — the offensive counterpart to STD.CA.6. Amplification cuts both ways: a PA that wins +1 PS resolves as +2; a PA that loses −1 PS resolves as −2. Cost is Exposure-denominated (same as STD.CA.6), slightly favoring the Network. Restriction is None — ARBITER holds awareness through Beat 4; if no Public Act is submitted, Amplify fizzles and Exposure is spent.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covertly amplifying your own political messaging fits the covert operations frame. Ghost's categorical opposition ("volume attracts attention") is the clearest doctrinal test for the card. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Ghost's perspective is the sharpest. All five are doctrinally distinct — opposition, authority-sufficiency, tactical use, suppression logic, leverage framing. | Art 00 §7 |
| Doctrine alignment | ✓ | Amplifying public messaging strongly serves Network doctrine; strongly opposes Ghost (volume = exposure risk). Both captured via portrait entries. Self-targeted → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: amplification mechanism is hidden. Standard: all factions can amplify their messaging covertly. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Resolution` — scales the outcome (standing_impact) of a PA; Art 04b §4.2 "outcome scale" is a Resolution property. `function = Modify`, `subject = PublicAct`. Note: `resolution_type = "Transactional"` may be a misnomer — card fizzles if no PA is submitted (same positional-wager behavior as STD.CA.6). Minor schema inconsistency, not blocking. | Art 04b §4, §5 |
| Balance | ✓ | Symmetric multiplier: both success (+×2) and failure (−×2) scale. Prevents risk-free use. Fizzle (Exposure spent, no PA) ensures Beat 2 commitment is real. | Art 02 §11 |
| Effect duration | ✓ | Single-round: arms at Beat 2, applies at Beat 4, does not persist. | Art 03 §10 |
| Persistence | ✓ | Immediate — Beat 2 carry; applied at Beat 4 via Resolution Grid; no game-state marker persists beyond round | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Network `submitter=+1`: amplifying public messaging is core Network doctrine (DIR.PA.1, SYN.PA.2). Ghost `submitter=−1`: amplification = attention = exposure risk — "volume attracts attention, attention ends operations" (DIR.PA.1, SYN.PA.2). Guild: no entry — "let our structures speak"; amplification is a substitute for physical evidence, not a doctrinal tool; absence justified. Directorate: no entry — institutional authority doesn't require amplification; tactical use only; absence justified. Syndicate: no entry — leverage framing is opportunistic, not doctrinal; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | N/A — `target_district = None`; card operates on acting faction's own PA submission, not a district. | — |
| Supported by components | ✓ | PublicAct as target; Exposure as cost; `standing_impact` for outcome (Art 02 §11). | Art 02 §8; Art 02 §11; Art 04b §5 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); placed in Beat 2 row at Resolution Grid setup (Art 03 §9.4.0 Beat 0); moved to Beat 4 carry row during Beat 2 processing (Art 03 §9.4.2 Beat 2); `standing_impact` multiplier applied at Beat 4 (Art 03 §17). | Art 03 §9, §11, §17 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | ✓ S63 |

```python
STD.CA.7 = Card(
    id      = "STD.CA.7",  version = "v1.1",
    name    = "Amplify",
    tagline = "Boost the Public Standing impact of your own public act this round.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Resolution,  function = Modify,  subject = PublicAct,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.acting,
    target_object   = PublicAct,

    target_taxonomy=None,
    affinity    = faction(acting) == Network: cost.resource.exposure -= 1,
    restriction = None,
    cost        = resource.faction(acting).exposure * 2,

    success     = faction(acting).op(beat=4, type=PublicAct).standing_impact *= 2,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Network: PortraitEntry(submitter=+1),
        Ghost:   PortraitEntry(submitter=-1),
    },

    narrative    = "A message worth sending is worth sending loudly.",
    perspectives = {
        Guild:       "We let our structures speak. Amplification is for those who lack physical evidence.",
        Directorate: "Institutional authority does not require amplification. Though we note its effectiveness.",
        Network:     "Every message we send should land as hard as possible. This ensures it does.",
        Ghost:       "Amplification is the opposite of what we do. Volume attracts attention. Attention ends operations.",
        Syndicate:   "Leverage applied at the right moment can move markets. This is that tool.",
    },
)
```

---

### STD.CA.8 — BUY INFLUENCE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Economy-bypasses-Territory card — the only Standard CovertOperation with no restriction and no presence requirement. Capital buys presence directly, reflecting that money can substitute for community groundwork. Cost vs reward: 3 Capital is high but buys 2 presence on success (more than STD.CA.3's 1), and crit success adds a third. Syndicate affinity is difficulty reduction, not cost reduction — the Syndicate does not spend less; it converts capital to presence more reliably. Three portrait penalties represent strong doctrinal opposition: bought influence is an institutional threat to Guild's earned-presence model, Directorate's legitimate-process model, and Network's relational model.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Deploying capital to buy presence covertly fits the game's economic warfare frame. No presence requirement is a deliberate design feature — capital substitutes for community groundwork. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Syndicate's perspective ("capital determines which doors exist") is the sharpest statement of the card's design logic. All five perspectives doctrinally distinct. | Art 00 §7 |
| Doctrine alignment | ✓ | Card effect strongly opposes Guild (earned-presence model), Directorate (legitimate-process model), and Network (relational model); supports Syndicate doctrine. Captured via portrait entries (Guild/Directorate/Network submitter=−1, Syndicate submitter=+1). No target_faction → doctrine_mod not applicable; doctrinal signal is portrait-only by design. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: purchase mechanism is covert; resulting presence tokens are visible board state. Standard: all factions can deploy capital to buy presence. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Territory` — placing PresenceTokens is a territorial operation. `function = Add`, `subject = PresenceToken` — correctly scoped. | Art 04b §4, §5 |
| Balance | ✓ | 3 Capital is the highest Standard cost. No presence restriction is the tradeoff. Success = +2 presence (superior to STD.CA.3's +1); crit = +3 total. Syndicate affinity: effective threshold 75%. Crit fail −2 PS is severe — publicly-failed capital deployment. | Art 02 §6, §8; Art 02 §11 |
| Effect duration | ✓ | Permanent: presence tokens persist until removed. Appropriate for a territorial placement card. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: bought presence undermines earned-presence model (DIR.PA.1, SYN.PA.2). Directorate `submitter=−1`: purchasing influence bypasses legitimate institutional process (DIR.PA.1, SYN.PA.2). Network `submitter=−1`: capital-as-power is exactly what Network opposes (DIR.PA.1, SYN.PA.2). Ghost `submitter=−1`: bought presence is noisy — "draws the wrong kind of attention"; against low-profile doctrine (DIR.PA.1, SYN.PA.2). Syndicate `submitter=+1`: capital doctrine — "determines which doors exist" (DIR.PA.1, SYN.PA.2). All five entries present; four opposing, one aligned — STD.CA.8 is Syndicate's card by design. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. No presence restriction — capital bypasses standard entry requirement. | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); Capital cost (Art 02 §8); failcrit PS −2 (Art 02 §11). | Art 02 §6, §8; Art 02 §11 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); placed in Beat 3 row of Resolution Grid (Art 03 §9.4.0 Beat 0); d100 threshold 50 with ring_mod and affinity; resolved at Beat 3 (Art 03 §9.4.2 Beat 3). | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | ✓ S63 |

```python
STD.CA.8 = Card(
    id      = "STD.CA.8",  version = "v1.1",
    name    = "Buy Influence",
    tagline = "Deploy capital to place presence tokens directly, without groundwork.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Add,  subject = PresenceToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Syndicate: threshold += 25,
    restriction = None,
    cost        = resource.faction(acting).capital * 3,

    success     = district(target).faction(acting).presence += 2,
    successcrit = district(target).faction(acting).presence += 1,
    fail        = None,
    failcrit    = faction(acting).standing -= 2,

    portrait = {
        Guild:       PortraitEntry(submitter=-1),
        Directorate: PortraitEntry(submitter=-1),
        Network:     PortraitEntry(submitter=-1),
        Ghost:       PortraitEntry(submitter=-1),
        Syndicate:   PortraitEntry(submitter=+1),
    },

    narrative    = "In New Meridian, capital is a language everyone understands.",
    perspectives = {
        Guild:       "Presence earned through investment rather than community is fragile. We have seen it collapse.",
        Directorate: "Purchasing influence undermines the legitimate institutional processes we exist to maintain.",
        Network:     "This is exactly the kind of power we are here to expose and resist.",
        Ghost:       "Bought presence is noisier than earned presence. It draws the wrong kind of attention.",
        Syndicate:   "Capital does not just open doors. It determines which doors exist in the first place.",
    },
)
```

---

### STD.CA.9 — FUND
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Alliance-seeding card — the only card in the Standard set that transfers resources between factions. Source is anonymous by default; on success the acting faction receives an Overture modifier card (delivered from ARBITER tableau) that may be assigned to any of their PAs to initiate an Accord proposal per Art 06 §9.4. Cost vs reward: 2 Capital spent to transfer 2 Capital to the target — net zero to the actor at success, but crit success awards +1 PS and Overture opens alliance mechanics. Syndicate affinity is difficulty reduction — the Syndicate is the faction most practiced at informal financial transfers.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Anonymous resource transfer as covert act — the act of funding is covert; Overture is what potentially reveals it. Faction-to-faction relationship seeding fits the game's alliance layer. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Directorate's "we monitor these carefully" is the subtlest threat at the table. All five perspectives doctrinally distinct — relationship investment, institutional scrutiny, financial exposure, operational awareness, capital relationships. | Art 00 §7 |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` — `doctrine_mod = {Neighbor: +15, Opposed: -15}` applies. Syndicate affinity (+25) stacks — funding a Neighbor as Syndicate reaches effective threshold 90. Capital flows where doctrine is aligned; crosses resistance where it is not. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: anonymous transfer is covert; Overture preserves optionality on disclosure. Standard: all factions can fund others. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Economy` — capital transfer is NativeResource flow, correctly Economy under Art 04b §4.4. `function = Redirect`, `subject = NativeResource` — correctly scoped. | Art 04b §4, §5 |
| Balance | ✓ | Net capital zero at success (2 Capital spent = 2 Capital delivered). Overture path to AccordForm costs 2 of 4 available action slots per Quarter (STD.CA.9 covert op slot + PA with Overture attached) — the slot cost is the real gate on this route, not the resource cost. Cost unchanged at 2 Capital (standard covert op cost). L201. | Art 02 §8; Art 04 §11.8 |
| Effect duration | ✓ | Capital transfer is instantaneous. Overture modifier card lifecycle governed by Art 04 §11.8 and Art 06 §9.4. | Art 04 §11.8; Art 06 §9.4 |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Syndicate `submitter=+1`: capital-in-motion doctrine — "relationships create opportunities" (DIR.PA.1, SYN.PA.2). Directorate `submitter=−1`: using anonymous financial transfer conflicts with legitimate-process doctrine; Directorate scrutinises these transfers in others — performing one is in-doctrine hypocrisy (DIR.PA.1, SYN.PA.2). Guild: no entry — relationship investment is pragmatic, not doctrinal; absence justified. Network: no entry — analytical framing only; no doctrinal stake as actor; absence justified. Ghost: no entry — observational framing; Ghost tracks capital flows for intelligence, not as participant; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | N/A — `target_district = None`; faction-level operation, no district target. | — |
| Supported by components | ✓ | Capital (Art 02 §8) ✓. Overture modifier card full spec written — Art 04 §11.8. | Art 02 §8; Art 04 §11.8 |
| Supported by game procedure | ⚠ | Dispatch and Beat 3 resolution ✓. Overture delivery procedure (ARBITER tableau → faction hand at Beat 3 resolution) pending Art 07 ARBITER subroutine pass. | Art 03 §9; Art 04 §11.8 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Overture delivery procedure:** Overture delivered from ARBITER tableau to acting faction's hand at Beat 3 resolution of STD.CA.9. Exact procedure (ARBITER hands card; notation) pending Art 07 ARBITER subroutine pass.
- **Anonymous transfer case-return:** Resources delivered to target faction at Beat 3. Covert attribution preserved — acting faction not announced. Procedure pending Art 03/Art 07 pass.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
STD.CA.9 = Card(
    id      = "STD.CA.9",  version = "v1.1",
    name    = "Fund",
    tagline = "Transfer resources to another faction as a gesture of support.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Redirect,  subject = NativeResource,

    beat            = 3,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = None,
    doctrine_mod    = {Neighbor: +15, Opposed: -15},
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = NativeResource,

    target_taxonomy=None,
    affinity    = faction(acting) == Syndicate: threshold += 25,
    restriction = None,
    cost        = resource.faction(acting).capital * 2,

    success     = (
        faction(target).resource.capital += 2,
        arbiter.deliver(faction(acting), Overture),  # from ARBITER tableau supply
    ),
    successcrit = faction(acting).standing += 1,
    fail        = None,
    failcrit    = faction(acting).standing -= 1,

    portrait = {
        Directorate: PortraitEntry(submitter=-1),
        Syndicate:   PortraitEntry(submitter=+1),
    },

    narrative    = "Every alliance in New Meridian begins with someone extending a hand.",
    perspectives = {
        Guild:       "Investment in relationships is as important as investment in structures.",
        Directorate: "Financial transfers between factions warrant scrutiny. We monitor these carefully.",
        Network:     "Follow the money. It always leads somewhere interesting.",
        Ghost:       "Resources flowing between factions change the operational landscape. We note the direction.",
        Syndicate:   "Capital in motion creates relationships. Relationships create opportunities.",
    },
)
```

---

### STD.CA.10 — PROTECT
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Defensive Beat 2 positional wager — the only Standard card that explicitly protects existing assets. Applies only to the acting faction's assets in the named district, not the district broadly. Cost vs reward: 1 district-native paid regardless of whether an attack materializes; if it does, −25 threshold reduction (−45 for Guild/Directorate) meaningfully degrades opponents' attack probability. Guild and Directorate affinity reflects institutional defense as core competency, not exceptional response.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Defensive preparations as covert act — protection is installed silently; effect is felt at Beat 3. Positional wager structure makes the action genuinely risky (wrong read wastes the slot). | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Ghost's "best protection is not being found" is the anti-use doctrine. All five perspectives distinct — obligation to defend, institutional resource, people-first, non-presence, value retention. | Art 00 §7 |
| Doctrine alignment | ✓ | Active asset defense serves Guild (protect what we build) and Directorate (institutional assets require defense) — both captured via portrait. Ghost is doctrinally opposed (concealment over fortification) — captured via portrait. Self-targeted → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: defensive preparations are covert. Standard: all factions can protect their assets; Guild/Directorate affinity rewards institutional-defense doctrine. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Resolution` — per Art 04b §4.6, Protect distributes to the target's layer. Target is CovertOperation (Resolution layer). `function = Protect`, `subject = CovertOperation` — correctly scoped. | Art 04b §4.6, §5 |
| Balance | ✓ | Beat 2 positional wager; 1 native cost. Guild/Directorate affinity −45 locked (L179): near-nullification narratively justified — Guild knows every access point and structural vulnerability in their own infrastructure; Directorate's institutional security apparatus (personnel, protocols, access control) can effectively stop a covert demolition attempt. The 5% floor acknowledges no protection is absolute. Attacker does not know protection is installed (STD.CA.10 is covert) — near-nullification is a consequence of capability, not a visible deterrent. Base −25 (other factions) leaves 25% — acceptable risk. | Art 02 §8; Art 02 §11 |
| Effect duration | ✓ | Single-round: arms at Beat 2, applies at Beat 3, does not persist past round. | — |
| Persistence | ✓ | Immediate — Beat 2 carry; applied at Beat 3 via Resolution Grid; no game-state marker persists beyond round | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Guild `submitter=+1`: protecting built assets is non-optional doctrine — "we protect what we build" (DIR.PA.1, SYN.PA.2). Directorate `submitter=+1`: institutional assets require active defense — resourced accordingly (DIR.PA.1, SYN.PA.2). Ghost `submitter=−1`: active fortification conflicts with concealment doctrine — "best protection is not being found" (DIR.PA.1, SYN.PA.2). Network: no entry — "we protect our people first; infrastructure is secondary"; situational use, not doctrinal; absence justified. Syndicate: no entry — rational asset-value framing, no doctrinal stake in fortification; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: acting presence in target district. | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken (restriction); district native cost (Art 02 §8); threshold reduction applied to Beat 3 ops targeting acting assets. | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); placed in Beat 2 row at Resolution Grid setup (Art 03 §9.4.0); threshold reduction applied at Beat 3 resolution (Art 03 §9.4.3). Note: Art 03 §20 M-09 refs in prior version are stale (pre-S52 reorg). | Art 03 §9, §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Art 03 dependency:** Threshold reduction marker placement (ARBITER places −25/−45 marker on Beat 3 ops targeting acting faction's assets at Beat 2 resolution) to be defined in Art 03 §9.4 Beat 2 processing steps.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | ✓ S63 |

```python
STD.CA.10 = Card(
    id      = "STD.CA.10",  version = "v1.1",
    name    = "Protect",
    tagline = "Defend a district's assets from covert disruption this round.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Resolution,  function = Protect,  subject = CovertOperation,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Positional wager",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = CovertOperation,

    target_taxonomy=None,
    affinity    = faction(acting) IN [Guild, Directorate]: threshold_protection = 45,
    restriction = district(target).faction(acting).presence > 0,
    cost        = resource.district(native) * 1,

    success     = game.ops(beat=3, at=district(target), targeting=faction(acting).assets).threshold -= (threshold_protection if affinity else 25),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Guild:       PortraitEntry(submitter=+1),
        Directorate: PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },

    narrative    = "What you build is only worth as much as your willingness to defend it.",
    perspectives = {
        Guild:       "We protect what we build. This is not optional.",
        Directorate: "Institutional assets require active defense. We resource this accordingly.",
        Network:     "We protect our people first. Infrastructure is secondary.",
        Ghost:       "The best protection is not being found in the first place.",
        Syndicate:   "Protected assets retain value. Unprotected assets invite acquisition.",
    },
)
```

---

### STD.CA.11 — TORT INTERFERENCE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Standard card available to all factions — any faction with a stake in an active Accord can lock it against voluntary dissolution through back-channel means. Reflects the legal concept of tortious interference: a third party prevents two contracting parties from exiting an agreement the third party benefits from. Directorate invokes this with institutional standing; Ghost files paperwork no one can trace; Syndicate retains counsel; Network embeds the agreement in public record; Collective organizes pressure around it. Cost is 1 Mandate + 1 of the acting faction's native resource — the Mandate requirement means any faction must spend a unit of institutional authority to invoke this regardless of doctrine. Lock persists until game end or direct breach by the Accord parties; breach is not blocked, but consequences apply normally. Voluntary dissolution suspended; unilateral breach is not.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Accord lock — prevents voluntary dissolution of a named executed Accord; distinct from GHO.CA.4 (evidence destruction) and DIR.CA.3 (surveillance); any faction with a stake can invoke | Art 00 §7 |
| Voice fit | ✓ | Standard card; five faction perspectives by design — each faction arrives at the same outcome through different means | Art 00 §7 |
| Doctrine alignment | ✓ | Standard; 1 Mandate + 1 native resource; Mandate requirement gates casual play regardless of faction; lock/breach distinction is mechanically clean | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / Standard — lock filed covertly; acting faction not announced at resolution; effect (marked Accord) is publicly visible | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/Accord — corrupts the dissolution process; target is a defined physical component (executed Accord on table) | Art 04b §4, §5 |
| Balance | ✓ | 1 Mandate + 1 native — dual resource cost reflects invoking legal/institutional authority outside normal doctrine; balance deferred until lock enforcement defined | Art 02 §6–§7 |
| Effect duration | ✓ | Until game end or breach — not permanent in the absolute sense; releases on direct breach by parties | — |
| Persistence | ✓ | Until(game.end OR Accord(named).breach_by_party) — card leaves a physical lock marker on the Accord; lingering per design | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | No portrait entry — PS implications deferred to 04-n34 sweep | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — Accord is on table/overview, not district-anchored | Art 01 §6–§7 |
| Supported by components | ✓ | Accord (executed, on table) — physically verifiable by all players; no ARBITER ledger required | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; lock enforcement and breach detection outstanding (Outstanding Issues) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

None — all resolved S68. District-keyed resource model makes Mandate acquirable by any faction (S68). `faction(acting).native` is existing notation precedent. Enforcement and breach detection are player-visible via the annotated public document per Governing Rule 6.1a — ARBITER does not track.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Redesigned S68: Directorate FactionSpecific CovertOperation (Evidence Preservation) → Standard CovertOperation. Name: Evidence Preservation → Tort Interference.*

```python
STD.CA.11 = Card(
    id      = "STD.CA.11",  version="v2.0",
    name    = "Tort Interference",
    tagline = "Lock an executed Accord against voluntary dissolution until game end or breach.",
    type    = CovertOperation,  subtype = Standard,  faction = All,
    layer   = Information,  function = Corrupt,  subject = Accord,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Permanent,
    persistence_condition = not (game.end OR Accord(named).breach_by_party),
    persistence_effect    = None,
    target_district=None, target_faction=None, target_object=Accord(executed, on_table),
    target_taxonomy=None,
    affinity=None,
    restriction = Accord(named).is_executed == True AND Accord(named).on_table == True,
    cost        = resource.faction(acting).mandate * 1 + resource.faction(acting).native * 1,
    success     = game.lock(Accord(named), until=game.end OR Accord(named).breach_by_party),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "The agreement stands. Whatever your reasons for wanting out, the record disagrees.",
    perspectives = {
        Directorate: "The agreement is now a matter of institutional record. Dissolution would require a filing no one is prepared to make.",
        Ghost:       "The paperwork has been submitted. Quietly. Neither party knows who filed it.",
        Syndicate:   "We have an interest in this arrangement continuing. Our lawyers agree.",
        Network:     "We have made this agreement part of the public record. Dissolving it now would be a story.",
        Collective:  "We hold both parties to what they agreed to. The community remembers.",
    },
    design_note  = "Redesigned S68: Directorate FactionSpecific CovertOperation (Evidence Preservation) → Standard CovertOperation. Any faction with a stake in an active Accord can lock it against voluntary dissolution. Cost: 1 Mandate + 1 faction native resource. Lock persists until game end or direct breach by Accord parties — breach not blocked, consequences apply normally.",
    arbiter_note = "ARBITER annotates the named Accord document at Beat 3 — writes 'cannot voluntarily dissolve' or marks equivalent field on the Accord blank (TBD Art 06). No new component. Annotation is public; faction players enforce. Annotation is voided if either party directly breaches the Accord terms — breach consequences apply normally. Acting faction identity is not announced at resolution.",
)
```

---

### STD.CA.12 — ABSOLUTE COMPROMISE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Standard counter-counter card — the only card available to all factions that removes active Block or Protect plays before they can apply. Addresses the problem that committed defensive plays (Invoke Jurisdiction, Regulatory Capture, Fortify Structure, Protect) otherwise have no counter in the same round.

**Scope (confirmed S119/S120):** Absolute Compromise targets all cards with `function=Block` or `function=Protect` in the Beat 2 row — CA cards in ARBITER's covert grid and Protect/Fortify modifier plays in the Faction Resolution Grid. ARBITER has full visibility of the covert grid and executes the removal sweep from that position; the acting faction commits a blanket sweep without disclosing what was removed. Countermeasure Cards (CM-A, CM-B) are not valid targets: they are processed at Beat 1 and discarded before Beat 2 begins (Art 03 §9.4.1.2). CM-B modifier tokens left on operations are also not targetable — they are not Block/Protect cards.

Intel token cost makes this a premium play — factions must hold Intel specifically to access this capability, reinforcing Intel as a cross-faction strategic resource. Positioned here from Art 04 §8 (retired) where it was misplaced: STD.CA.12 is subtype=Standard (all factions), not FactionSpecific.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Counter-counter card — removes a committed Beat 2 Block or Protect before it applies; fills gap where defensive positional wagers have no standard counter | Art 00 §7 |
| Voice fit | ✓ | Standard card; all-faction access; no faction-specific voice required; perspectives block expected for full Standard spec — confirm complete in code block | Art 00 §7 |
| Doctrine alignment | ✓ | N/A — Standard card; no faction doctrine alignment required; no affinity; portrait = {} | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / Standard / faction=All — all-faction counter-counter capability; no faction restriction | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Submission/Block/CovertOperation — removes a submitted covert op's effect before it applies; Block function correct | Art 04b §4, §5 |
| Balance | ✓ | Intel token for one Beat 2 card removal — premium cost justified by cross-faction utility; resources on discarded card not refunded (confirmed S120 — GR 7.2b consistent) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: target card discarded at Beat 2 resolution; no lingering effect | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces target Beat 2 card exists | — |
| Portrait validity | ✓ | portrait = {} — Standard card; no portrait entry confirmed intentional | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — Beat 2 cards are district-anchored | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; Beat 2 Block or Protect card as target (function=Block or function=Protect per Art 04b taxonomy) — scope resolved S119, CA-inclusive | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; target card must exist in Beat 2 row at resolution; discard occurs at Beat 2. CM cards are not valid targets — processed and discarded at Beat 1 (Art 03 §9.4.1.2) before CA.12 fires. Valid targets: CA cards (function=Block or function=Protect) and Protect/Fortify modifier plays. | Art 03 §9.4.1.2, §9.4.2 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

None — all design questions resolved S119/S120:
- Scope: CA-inclusive (covert grid + public Protect/Fortify). ARBITER sweeps both domains at Beat 2. S119.
- CM interaction: Countermeasure Cards (both types) are Beat 1 — processed and discarded at §9.4.1.2 before Beat 2 begins. CA.12 never encounters a live CM card. S120 (Art 03 §9.4.1.2 read).
- Scope boundary: SYN.CA.4 Golden Parachute and SYN.CA.6 Parasitic are Beat 2 Automatic but not function=Block/Protect — not valid targets. S119.
- Resource refund: no refund (GR 7.2b consistent — committed resources are sunk). S120.
- Remaining: 04-n70 (schema) + 04-n79 (narrative) — infrastructure sweeps only.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Migrated from Art 04 §8 (retired) Intel Economy block to Standard Covert section S59. Pre-convention flat format — full schema pass pending (04-47).*

```python
STD.CA.12 = Card(
    id      = "STD.CA.12",  version="v1.0",
    name    = "Absolute Compromise",
    tagline = "Some barriers are not barriers at all — just the illusion of one.",
    type    = CovertOperation,  subtype = Standard,  faction = All,
    layer   = Submission,  function = Block,  subject = CovertOperation,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.named, target_faction=None, target_object=Beat2BlockOrProtectCard,
    target_taxonomy=None,
    affinity=None,
    restriction = district(target).beat2_row.has_block_or_protect_card == True,
    cost        = IntelToken(any) * 1,
    success     = game.discard(target_card, district(target).beat2_row),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "There are no walls. There are only varying degrees of access.",
    perspectives = {},
    design_note  = "Scope (S119): CA-inclusive — targets Block/Protect plays in both the Faction Resolution Grid (Type A CMs, Protect/Fortify modifier plays) and ARBITER's covert resolution grid (Beat 2 CA cards with function=Block or function=Protect). Cannot target Type B Countermeasures (faction defense — reduces difficulty, not a Block/Protect play). Intel token consumed is any held token.",
    arbiter_note = "At Beat 2 resolution: sweep both grid domains. (1) Faction Resolution Grid: discard any Type A Countermeasure or Protect/Fortify modifier play targeting the named district. (2) Covert grid: discard any Beat 2 CA with function=Block or function=Protect from the named district row. Resources committed to discarded cards are not refunded. Operations those cards would have affected proceed without the modifier.",
)
```

---

### STANDARD — DISINFORMATION CAMPAIGN
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
First Standard card with Public Standing shift as its primary covert effect — fills the Standing/Shift coverage gap flagged in Art 04b §8. Distinct from Public Act PS cards (STD.PA.4, STD.PA.7): this is a covert operation, so the acting faction is unknown to the target. Presence restriction grounds it in operational reality: you need a footprint in a district to run a local narrative operation. The failcrit NotificationSlip follows DIR.CA.2 precedent — a badly botched campaign leaves traces, and ARBITER notifies the target that a campaign ran in that district (not who ran it). Network affinity (threshold +10) reflects broadcast infrastructure amplifying covert narrative reach. Ghost affinity (cost −1) reflects datastream manipulation as native capability.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert narrative manipulation as a standard capability: all factions can conduct local perception operations against each other | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild notices effects rather than participating; Directorate opposes covert image manipulation on principle; Network values the tool but distinguishes signal from noise; Ghost flags the attention risk; Syndicate tracks market implications | Art 00 §7 |
| Doctrine alignment | ✓ | Network affinity (threshold +10): broadcast infrastructure amplifies narrative reach. Ghost affinity (cost −1): datastream manipulation is native capability. Directorate portrait −1: covert manipulation conflicts with institutional legitimacy doctrine. No doctrine_mod (no faction target for modifier) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: the source of the campaign is hidden. Standard: all factions can contest standing via covert narrative operations | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding — first Standard covert card in this taxonomy slot | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 40, ring_mod standard. Success swing: target −2 PS, acting +1 PS (net 3). Fail: acting −1 PS. Presence restriction limits targeting. Failcrit exposure risk makes reckless use costly | Art 02 §6–§7 |
| Effect duration | ✓ | PS shifts are Immediate; no lasting marker | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Network +1: broadcasting narrative to shift perception is core doctrine (DIR.PA.1, SYN.PA.2). Ghost −1: public narrative campaigns attract attention, conflicting with low-profile doctrine (DIR.PA.1, SYN.PA.2). Directorate −1: covert image manipulation undermines institutional legitimacy (DIR.PA.1, SYN.PA.2). Guild, Syndicate: no entry — neither has a doctrinal stake in covert narrative authorship | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any; restriction checks acting faction's presence in that district | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. PS tracked on Public Standing track (Art 02 §7); NotificationSlip (failcrit, same as DIR.CA.2) | Art 02 §7; Art 03 §9.4 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; NotificationSlip failcrit follows DIR.CA.2 established procedure | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
C_DisinformationCampaign = Card(
    id      = "STD.CA.13",  version = "v1.0",
    name    = "Disinformation Campaign",
    tagline = "Run a covert narrative operation degrading a faction's public standing in a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Standing,  function = Shift,  subject = StandingMarker,

    beat            = 3,
    resolution      = d100,
    threshold       = 40,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = (
        faction(acting) == Network: threshold += 10,
        faction(acting) == Ghost:   cost.resource.native -= 1,
    ),
    restriction = faction(acting).presence(target_district) > 0,
    cost        = resource.faction(acting).native * 2,

    success     = (faction(target).standing -= 2, faction(acting).standing += 1),
    successcrit = None,
    fail        = faction(acting).standing -= 1,
    failcrit    = (
        faction(acting).standing -= 2,
        arbiter.dispatch(NotificationSlip(type="Disinformation Campaign", district=target_district), target_faction),
    ),

    portrait = {
        Network:     PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
        Directorate: PortraitEntry(submitter=-1),
    },

    narrative    = "The city's opinion is infrastructure. It can be built. It can be demolished.",
    perspectives = {
        Guild:       "Narrative operations are not our toolset. We notice the shift after the quarter closes.",
        Directorate: "Covert image manipulation conflicts with the institutional legitimacy we exist to uphold. We note who deploys it.",
        Network:     "We have channels built for exactly this. Using them properly is what separates signal from noise.",
        Ghost:       "A successful operation leaves no signature. Campaigns draw attention. This is the compromise.",
        Syndicate:   "Standing shifts move markets and tables. We note who runs this and in which districts.",
    },
    design_note  = "First Standard covert card with PS shift as primary effect — fills Standing/Shift coverage gap. Presence restriction: must have operational footprint to run local narrative operation. Success swing: target −2 PS, acting +1 PS (net 3). Fail: acting −1 PS. Failcrit: acting −2 PS + NotificationSlip to target (campaign ran against you in [district] this Month; not who ran it). Ring modifier: harder in Core (denser institutional oversight). Standard equivalents under Principle 17: Network and Ghost have superior faction-specific versions.",
    arbiter_note = "Beat 0: confirm acting faction has presence (token or deployment marker) in target district; if not — op voided, resources returned. Beat 3: roll d100. Success: target −2 PS, acting +1 PS. Fail: acting −1 PS. Fail crit (01–05): acting −2 PS; dispatch NotificationSlip to target faction ('A disinformation campaign was run against you in [district] this Month'). Target does not learn who ran it.",
)
```

---

### STANDARD — DISPROVE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Fills the Economy/Remove/IntelToken coverage gap in the Standard card set. All factions have operational reason to destroy intelligence records held against them or a rival — no faction has a doctrine-native advantage for the act of destruction itself, so no affinity is warranted. Blind random removal: the acting faction names a target faction; ARBITER draws one Intel token at random from that faction's supply and removes it from play. Silent on success — the target receives no notification and discovers the loss only on a count. Cost 2 native reflects the offensive nature of a pure denial operation with no material return. Fails automatically if target holds no tokens at Beat 3.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert destruction of opponent's intelligence records is a standard operational capability — all factions have grounds for denial operations against intel supply | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild reads operational records as accountability; Directorate holds institutional record preservation as principle; Network frames destruction as information erasure; Ghost frames it as operational security; Syndicate reads it as supply-side intelligence management | Art 00 §7 |
| Doctrine alignment | ✓ | No affinity — no faction has doctrine-native advantage for destroying a third party's intelligence tokens. Ghost portrait +1: operational security doctrine aligns with removing incriminating records. Network portrait −1: information destruction conflicts with transparency doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: source of removal is hidden. Standard: available to all factions | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Remove/IntelToken — fills coverage gap per Art 04b §6 | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 45, ring_mod None (no district target). Fail = no effect, cost sunk. Automatic fail if target holds no tokens at Beat 3. Pure denial — no material gain | Art 02 §5 |
| Effect duration | ✓ | Immediate — token destroyed at Beat 3, no lingering marker | Art 04 §5 P19 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Ghost +1: destroying records aligns with low-profile and operational security doctrine. Network −1: information erasure conflicts with transparency and broadcast doctrine. Guild, Directorate, Syndicate: no entry | Art 04 §6.2 |
| Supported by zones | ✓ | No district target; operation targets faction's supply directly | Art 01 §6–§7 |
| Supported by components | ✓ | Intel tokens (Art 02 §5); no new components required | Art 02 §5 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; ARBITER blind draw from supply is consistent with ARBITER draw authority | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
C_Disprove = Card(
    id      = "STD.CA.14",  version = "v1.0",
    name    = "Disprove",
    tagline = "Covertly destroy one Intel token held in an opponent's supply.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Remove,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 45,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = IntelToken.any,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).native * 2,

    success     = arbiter.draw_random(IntelToken, source=faction(target).supply,
                      count=1, action=destroy),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Ghost:   PortraitEntry(submitter=+1),
        Network: PortraitEntry(submitter=-1),
    },

    narrative    = "What the record does not contain cannot be verified.",
    perspectives = {
        Guild:       "Operational evidence is a fact of the city. We account for what we do. Who removes the accounting is who fears it.",
        Directorate: "The record exists for a reason. Selectively removing it undermines the institutional process we exist to uphold.",
        Network:     "Every destroyed token is a story that will never be told. That is not intelligence. That is erasure.",
        Ghost:       "Evidence that does not exist cannot follow you. This is the most important lesson we teach.",
        Syndicate:   "Market intelligence has a half-life. The fastest way to extend it is to reduce the competition's supply.",
    },
    design_note  = "Standard covert op targeting an opponent's Intel token supply via blind random removal — ARBITER draws one token from target's supply without acting faction specifying which. No district restriction; no affinity (destroying evidence has no faction-native doctrine edge). Silent on success: target receives no notification. Automatic fail if target holds no tokens at Beat 3 (cost sunk).",
    arbiter_note = "Covert Dispatch: acting faction names target faction. Beat 3: if target faction holds zero Intel tokens, op fails (cost sunk; do not announce reason). Otherwise, draw one Intel token at random from target faction's supply and remove from play (return to box). Acting faction receives no information about the removed token. Target faction receives no notification.",
)
```

---

### STANDARD — INTEL EXTRACTION
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Economy/Redirect/IntelToken — splits Asset Extraction (S62) into two focused cards. Blind random draw: ARBITER transfers one Intel token from the target faction's supply to the acting faction's dispatch case, face-down. Acting faction discovers the token's content privately at Beat 3 resolution when the case opens; ARBITER does not announce content. Target faction's token count decreases visibly. Cost 2 native: extracting and getting away clean with a resource is operationally harder than destroying it. Ghost affinity (threshold +10): covert acquisition is Ghost doctrine. Syndicate portrait +1: capital intelligence infrastructure aligns Syndicate with resource acquisition by any means, but physical covert acquisition is not Syndicate's mechanical specialty — no threshold bonus warranted. Fails automatically if target holds no tokens at Beat 3.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert acquisition of an opponent's Intel tokens is a standard economic-denial operation — acting faction gains an intelligence asset while the target loses one | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild refuses to take others' gathered work; Directorate opposes covert acquisition as bypassing sanctioned process; Network notes the token continues to exist; Ghost treats it as native operational methodology; Syndicate reads it as capital intelligence arbitrage | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost affinity (threshold +10): covert acquisition is Ghost doctrine. Syndicate portrait +1: capital intelligence motivation aligns Syndicate with resource acquisition — no mechanical threshold bonus, physical acquisition is not Syndicate-native. Directorate portrait −1: covert acquisition bypasses legitimate process. Guild portrait −1: taking what others gathered | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: acting faction unknown; target's count decreases visibly. Standard: available to all factions | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Redirect/IntelToken — fills coverage gap per Art 04b §6; splits Asset Extraction (S62) | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 45 (Ghost: 55), ring_mod None. Fail = no effect, cost sunk. Automatic fail if target holds no tokens at Beat 3. Double effect (acting gains, target loses) justifies same cost as pure-denial Disprove | Art 02 §5 |
| Effect duration | ✓ | Immediate — token transferred at Beat 3, no lingering marker | Art 04 §5 P19 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Syndicate +1: covert resource acquisition aligns with capital intelligence doctrine. Guild −1: taking what others gathered conflicts with earned-value principle. Directorate −1: bypasses sanctioned intelligence handling. Ghost, Network: no entry | Art 04 §6.2 |
| Supported by zones | ✓ | No district target; operates directly on faction's supply | Art 01 §6–§7 |
| Supported by components | ✓ | Intel tokens (Art 02 §5); dispatch case procedure established (Art 03 §9.4); no new components | Art 02 §5; Art 03 §9.4 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; face-down transfer to dispatch case follows established case-handling procedure | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
C_IntelExtraction = Card(
    id      = "STD.CA.15",  version = "v1.0",
    name    = "Intel Extraction",
    tagline = "Covertly transfer one Intel token from an opponent's supply into your dispatch case.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Redirect,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 45,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = IntelToken.any,

    target_taxonomy=None,
    affinity    = (
        faction(acting) == Ghost: threshold += 10,
    ),
    restriction = None,
    cost        = resource.faction(acting).native * 2,

    success     = arbiter.draw_random(IntelToken, source=faction(target).supply,
                      count=1, action=transfer(faction(acting).case, face_down=True)),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Syndicate:   PortraitEntry(submitter=+1),
        Guild:       PortraitEntry(submitter=-1),
        Directorate: PortraitEntry(submitter=-1),
    },

    narrative    = "Information doesn't belong to anyone. It belongs to whoever holds it.",
    perspectives = {
        Guild:       "We do not take what others have built. The intelligence they gathered represents real work.",
        Directorate: "Covert acquisition bypasses every sanctioned process for handling intelligence. We treat the result accordingly.",
        Network:     "A token in a different hand does not cease to be information. The question is what it becomes.",
        Ghost:       "Their intelligence is now a liability. Ours is now an asset. The operation is the same.",
        Syndicate:   "Capital intelligence infrastructure exists precisely for this — locating value before the market prices it in.",
    },
    design_note  = "Economy/Redirect/IntelToken — splits Asset Extraction (S62) into two cards. Blind random draw from target's supply; acting faction receives token face-down in case, inspects privately at Beat 3 resolution. Target's token count decreases visibly (visible resource denial). Ghost affinity (threshold +10): covert acquisition doctrine. Syndicate portrait +1: capital intelligence motivation, no threshold bonus (physical acquisition is not Syndicate-native). Automatic fail if target holds no tokens at Beat 3.",
    arbiter_note = "Covert Dispatch: acting faction names target faction. Beat 3: if target faction holds zero Intel tokens, op fails (cost sunk; do not announce reason). Otherwise, draw one Intel token at random from target faction's supply. Transfer face-down to acting faction's dispatch case — acting faction may inspect privately. Target faction's token count decreases by 1 (visible).",
)
```

---

### STANDARD — MODIFIER RAID
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Economy/Redirect/ModifierCard — splits Asset Extraction (S62) alongside Intel Extraction, with modifier cards as the target resource. Same blind draw mechanic: ARBITER transfers one modifier card at random from the target faction's hand to the acting faction's dispatch case, face-down. Acting faction discovers the card privately at Beat 3 resolution. Target faction's card count decreases visibly. Modifier cards represent prepared tactical advantages — stealing one simultaneously strips the opponent's preparation and delivers that advantage to the acting faction. Same affinity structure as Intel Extraction (Ghost threshold +10; Syndicate portrait +1). Cost 2 native. Fails automatically if target holds no modifier cards at Beat 3.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert acquisition of an opponent's modifier cards simultaneously denies their tactical preparation and transfers that advantage to the acting faction | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild refuses to take tools others made; Directorate opposes covert seizure of operational resources; Network notes the card's function shifts by context; Ghost targets the tactical disruption aspect; Syndicate reads it as operational arbitrage | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost affinity (threshold +10): covert acquisition doctrine, same as Intel Extraction. Syndicate portrait +1: resource acquisition by covert means aligns with capital intelligence doctrine. Same affinity structure as Intel Extraction | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: source hidden; target's card count decreases visibly. Standard: available to all factions | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Redirect/ModifierCard — fills coverage gap per Art 04b §6; splits Asset Extraction (S62) | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 45 (Ghost: 55), ring_mod None. Parallel structure to Intel Extraction — same cost and threshold for same operational profile. Automatic fail if target holds no modifier cards at Beat 3 | Art 02 §5 |
| Effect duration | ✓ | Immediate — card transferred at Beat 3, no lingering marker | Art 04 §5 P19 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Syndicate +1: covert resource acquisition aligns with capital intelligence doctrine. Guild −1: taking tools others built conflicts with earned-value principle. Directorate −1: seizure of operational resources bypasses legitimate process. Ghost, Network: no entry | Art 04 §6.2 |
| Supported by zones | ✓ | No district target; operates directly on faction's modifier card hand | Art 01 §6–§7 |
| Supported by components | ✓ | Modifier cards (Art 02); dispatch case procedure established (Art 03 §9.4); no new components | Art 02; Art 03 §9.4 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; face-down transfer to dispatch case follows established case-handling procedure | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
C_ModifierRaid = Card(
    id      = "STD.CA.16",  version = "v1.0",
    name    = "Modifier Raid",
    tagline = "Covertly transfer one modifier card from an opponent's hand into your dispatch case.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Redirect,  subject = ModifierCard,

    beat            = 3,
    resolution      = d100,
    threshold       = 45,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = ModifierCard.any,

    target_taxonomy=None,
    affinity    = (
        faction(acting) == Ghost: threshold += 10,
    ),
    restriction = None,
    cost        = resource.faction(acting).native * 2,

    success     = arbiter.draw_random(ModifierCard, source=faction(target).hand,
                      count=1, action=transfer(faction(acting).case, face_down=True)),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Syndicate:   PortraitEntry(submitter=+1),
        Guild:       PortraitEntry(submitter=-1),
        Directorate: PortraitEntry(submitter=-1),
    },

    narrative    = "They packed for an operation they will never run.",
    perspectives = {
        Guild:       "Tools are built for a purpose. Taking them from someone who made them is not the same as earning them.",
        Directorate: "Seizing operational resources outside any sanctioned process is the definition of what we are here to prevent.",
        Network:     "A modifier card in the wrong hand is a signal on the wrong frequency. It still transmits.",
        Ghost:       "Strip their tactical advantage before they deploy it. The modifier they held is now the one we use.",
        Syndicate:   "Their preparation becomes our edge. That is the nature of capital intelligence — arbitrage at the operational level.",
    },
    design_note  = "Economy/Redirect/ModifierCard — splits Asset Extraction (S62) into two cards alongside Intel Extraction. Blind random draw from target's modifier hand; acting faction receives card face-down in case, inspects privately at Beat 3 resolution. Target's card count decreases visibly. Ghost affinity (threshold +10); Syndicate portrait +1. Automatic fail if target holds no modifier cards at Beat 3.",
    arbiter_note = "Covert Dispatch: acting faction names target faction. Beat 3: if target faction holds zero modifier cards, op fails (cost sunk; do not announce reason). Otherwise, draw one modifier card at random from target faction's hand. Transfer face-down to acting faction's dispatch case — acting faction may inspect privately. Target faction's modifier card count decreases by 1 (visible).",
)
```

---


---

### Standard — Public Acts
[↑ Standard](#standard)

Public acts use the same data schema as covert operations (§6) with two additional fields:

| Additional Field | Description |
|-----------------|-------------|
| **Popularity effect** | Popularity movement on success and failure. |
| **Declaration requirement** | Any verbal or physical declaration required at time of play. |

Public acts are Beat 4 cards unless otherwise specified.

| Card | Name |
|------|------|
| [STD.PA.1](#p01-open-operations) | Open Operations |
| [STD.PA.2](#p02-disputed-claim) | Disputed Claim |
| [STD.PA.3](#p03-public-commission) | Public Commission |
| [STD.PA.4](#p04-public-censure) | Public Censure |
| [STD.PA.5](#p05-on-the-record) | On the Record |
| [STD.PA.6](#p06-economic-sanction) | Economic Sanction |
| [STD.PA.7](#p07-public-address) | Public Address |
| [STD.PA.8](#p08-table-an-accord) | Table an Accord |

### STD.PA.1 — OPEN OPERATIONS
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Public counterpart to STD.CA.3 (Campaign). Same cost (2 native), guaranteed outcome (Automatic), PS +1 on success. The trade: covert presence-building is hidden but risky (d100/50, fail wastes cost); Open Operations is visible from Phase B declaration but certain. Directorate's cost waiver reflects that formal institutional presence declaration is a zero-friction doctrinal act — the mandate is the permission. Ghost's portrait −1 captures the cost of committing to visibility against concealment doctrine.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public territorial declaration is a core political act in New Meridian — every faction makes formal presence claims | Art 00 §7 |
| Voice fit | ✓ | Five distinct perspectives: Guild grounds it in the build, Directorate in the record, Network in confirmation, Ghost in commitment-cost, Syndicate in sequencing | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate affinity (cost = 0) + portrait +1. Ghost portrait −1. Others no entry — justified | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard — all factions make public presence claims; universally useful | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken — unambiguous | Art 04b §4 |
| Balance | ✓ | Same cost as STD.CA.3; Automatic vs. d100/50; +PS. Trade is visibility, not resources | Art 02 §6–§7 |
| Effect duration | ✓ | Presence tokens are Permanent board state; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1: submitter-bounded (SYN.PA.2). Ghost −1: submitter-bounded. No direct PS shift in portrait (DIR.PA.2) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone reference; ring entry enforced at Beat 0 by ARBITER | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); faction native × 2 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 4 resolution; ring entry rules enforced at Beat 0 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
STD.PA.1 = Card(
    id      = "STD.PA.1",  version="v1.0",
    name    = "Open Operations",
    tagline = "Formally declare your operational presence in a district.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Add,  subject = PresenceToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Directorate: cost.faction(native) = 0,
    restriction = None,  # ring entry enforced universally at Beat 0
    cost        = resource.faction(acting) * 2,

    success     = (district(target).faction(acting).presence += 2, faction(acting).standing += 1),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Directorate: PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },

    narrative    = "A formal declaration carries weight in New Meridian. Presence on the record is presence that cannot be denied.",
    perspectives = {
        Guild:       "We are here. What we build will say the rest.",
        Directorate: "Formal establishment of operations in this district. The record reflects it.",
        Network:     "Our presence here was always going to be known. This makes it official.",
        Ghost:       "Every formal declaration is a commitment we would rather not have made.",
        Syndicate:   "The first step is always claiming the position. Everything else follows.",
    },
    design_note  = "Public version of STD.CA.3 Campaign. Same cost (2 native), guaranteed outcome (Automatic), PS +1 on success. Trade: covert = hidden + risky vs. public = visible + certain. Directorate affinity: formal institutional presence declaration has no resource cost against mandate doctrine. Ghost −1: visibility conflicts with concealment doctrine. Ring entry rules still enforced by ARBITER at Beat 0.",
    arbiter_note = "Place 2 presence tokens for acting faction in declared district at Beat 4. Apply PS +1 to acting faction. Confirm ring entry requirements at Beat 0 — if not satisfied, PA voided; resources returned; acting faction takes Public Pass.",
)
```

---

### STD.PA.2 — DISPUTED CLAIM
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Public counterpart to STD.CA.4 (Undermine). Same cost (2 native), slightly better base threshold (45 vs 40), PS effects added. Going public here means accepting accountability: a failed challenge hurts the challenger's standing. Network and Directorate gain threshold bonuses reflecting doctrinal alignment with formal territorial dispute mechanisms. The fail/failcrit PS penalties make this meaningfully riskier than it looks — public challenges are public commitments.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal territorial challenges are institutionally grounded in New Meridian | Art 00 §7 |
| Voice fit | ✓ | All five perspectives credible and distinct: Guild's reluctance-but-will-defend, Directorate's formal-mechanism preference, Network's public-accountability, Ghost's attention-cost framing, Syndicate's leverage reading | Art 00 §7 |
| Doctrine alignment | ✓ | Network +10 threshold + portrait +1; Directorate +10 threshold + portrait +1 — formal dispute mechanisms align with both doctrines. Ghost portrait −1: public confrontation conflicts with concealment. doctrine_mod captures target relationship | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard — all factions contest territory | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Remove / PresenceToken — target is a PresenceToken being removed | Art 04b §4 |
| Balance | ✓ | Same cost as STD.CA.4; slightly better threshold; PS effects add risk on fail. Contested marker fires on tie — procedural | Art 02 §6–§7 |
| Effect duration | ✓ | Presence token removal is a permanent state change; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1, Directorate +1, Ghost −1: all submitter-bounded (SYN.PA.2). PS effects are game effects, not Portrait shifts (DIR.PA.2) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone reference; ring_mod calibrated to ring context | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken — target removal (Art 02 §6); ContestedMarker — procedural (Art 03 §9.4); faction native × 2 cost (Art 02 §8) | Art 02 §6, §8; Art 03 §9.4 |
| Supported by game procedure | ✓ | Beat 4; Contested marker placement governed by Art 03 §9.4; ring_mod applies | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
STD.PA.2 = Card(
    id      = "STD.PA.2",  version="v1.0",
    name    = "Disputed Claim",
    tagline = "Formally challenge another faction's presence in a district.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Remove,  subject = PresenceToken,

    beat            = 4,
    resolution      = d100,
    threshold       = 45,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = {Neighbor: +10, Opposed: -10},
    trigger         = None,
    resolution_type = "Contested",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = (
        faction(acting) == Network:    threshold += 10,
        faction(acting) == Directorate: threshold += 10,
    ),
    restriction = faction(target).influence_tier(target_district) >= Established,
    cost        = resource.faction(acting) * 2,

    success     = (
        district(target_district).faction(target).presence -= 1,
        if tie_condition(target_district): arbiter.place(ContestedMarker, target_district),
        faction(acting).standing += 1,
        faction(target).standing  -= 1,
    ),
    successcrit = None,
    fail        = faction(acting).standing -= 1,
    failcrit    = faction(acting).standing -= 2,

    portrait = {
        Network:     PortraitEntry(submitter=+1),
        Directorate: PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },

    narrative    = "A contested district is not a resolved one. Filing a formal challenge makes the dispute legible.",
    perspectives = {
        Guild:       "We would rather build than challenge. But we will not cede ground claimed without cause.",
        Directorate: "A formal challenge is the legitimate mechanism for resolving territorial disputes. We prefer it to ambiguity.",
        Network:     "Presence built on hollow ground should not stand. We will say so publicly.",
        Ghost:       "Public challenges create public attention. Attention is expensive.",
        Syndicate:   "Challenges are leverage. The willingness to file one changes the calculus of every faction at the table.",
    },
    design_note  = "Public version of STD.CA.4 Undermine. Same cost (2 native); threshold 45 vs STD.CA.4's 40; PS consequences added. Fail/failcrit penalise the challenger — public challenges are public commitments. Network/Directorate +10 threshold: doctrinal alignment with formal dispute mechanisms. Ghost −1: public confrontation conflicts with concealment doctrine. doctrine_mod: Neighbor +10, Opposed −10 on target faction relationship.",
    arbiter_note = "Beat 4. Remove 1 presence token from target faction. Check for tie at highest chip count — if tie at 3+ chips, place Contested marker. PS: acting +1, target −1 on success. Acting −1 on fail. Acting −2 on failcrit (no token removed on fail/failcrit).",
)
```

---

### STD.PA.3 — PUBLIC COMMISSION
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Public counterpart to STD.CA.1 (Build Structure). Same cost; unlike STD.CA.1, the construction is publicly announced at Phase B and ARBITER records it. The covert element is absent — there is no hidden intent here. Going public provides certainty (Automatic) and PS +1 versus STD.CA.1's concealed attempt with failure risk. Guild's affinity (district native = 0) is maximally on-doctrine here: Guild building in public is the purest expression of permanence doctrine. Ghost's portrait −1 reflects that public structures are commitments Ghost would not voluntarily create.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public construction is a core territorial act — all factions build where the strategy demands it | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct and credible: Guild's open permanence, Directorate's mandate/record framing, Network's observation of public statements, Ghost's accountability-cost, Syndicate's visible-portion-of-investment framing | Art 00 §7 |
| Doctrine alignment | ✓ | Guild affinity (district native = 0) + portrait +1 — maximally on-doctrine (permanence through building). Ghost −1: permanent public structure conflicts with concealment. Others: no doctrinal stake in public construction | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard — structure building is universally available; Guild affinity appropriate but not exclusive | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / StructureBlock | Art 04b §4 |
| Balance | ✓ | Same cost as STD.CA.1; Automatic vs d100; PS +1. Trade: visibility for certainty. Guild effectively pays 1 native (affinity waives district native) | Art 02 §6–§7 |
| Effect duration | ✓ | StructureBlock = Permanent board state; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Guild +1, Ghost −1: submitter-bounded. Same doctrine logic as STD.CA.1 | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid; restriction checks district presence and structure state (valid zone conditions) | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock (Art 02 §7); PresenceToken — restriction (Art 02 §6); faction native + district native costs (Art 02 §8) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 4; restriction checked at Beat 0 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
STD.PA.3 = Card(
    id      = "STD.PA.3",  version="v1.0",
    name    = "Public Commission",
    tagline = "Publicly announce and fund construction of a structure in a district.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Add,  subject = StructureBlock,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Guild: cost.resource.district(native) = 0,
    restriction = (
        district(target).faction(acting).presence > 0 and
        district(target).faction(acting).structure == 0
    ),
    cost = resource.faction(acting) * 1 + resource.district(native) * 1,

    success     = (district(target).faction(acting).structure += 1, faction(acting).standing += 1),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Guild: PortraitEntry(submitter=+1),
        Ghost: PortraitEntry(submitter=-1),
    },

    narrative    = "Every faction that wants to be taken seriously in New Meridian eventually has to build something where everyone can see it.",
    perspectives = {
        Guild:       "We build in the open because the work is not something we need to hide.",
        Directorate: "Infrastructure serves the mandate. We build when the district requires it and the record supports it.",
        Network:     "Building is a public statement. We attend to what the statement claims.",
        Ghost:       "A structure in public view is a structure we have to account for.",
        Syndicate:   "The public commission is the visible portion of the investment. The value is in what follows.",
    },
    design_note  = "Public counterpart to STD.CA.1. Same cost; Automatic (no fail risk); PS +1. Guild affinity (district native = 0) on-doctrine. Ghost −1: public structure = permanent commitment against concealment doctrine. Counter to Guild's build pace: Directorate DIR.PA.1 (Regulatory Override) raises cost of presence-placement in district (prerequisite for this card); GUI.PA.1 (Civic Works Mandate) can be blocked by DIR.PA.1.",
    arbiter_note = "Place 1 structure block for acting faction in declared district at Beat 4. PS +1. Restriction at Beat 0: acting faction must have presence and no existing structure. If restriction fails, PA voided.",
)
```

---

### STD.PA.4 — PUBLIC CENSURE
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
The PS attack card of the standard set. A formal public accusation carries both potential and risk — a failed censure reflects worse on the accuser than the target. Network and Directorate get cost reductions (accusation is their institutional/broadcast mode). An optional Fresh Intel token submitted at Phase B provides a +15 threshold bonus, rewarding prior intelligence work. The fail and failcrit costs ensure reckless censure is punished. Ghost's portrait −1 reflects that self-exposure is the cost of public accusation.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal accusations are a core political act — all factions can and do make them | Art 00 §7 |
| Voice fit | ✓ | All five perspectives credible: Guild's evidence-based restraint, Directorate's formal mechanism framing, Network's public-fact stance, Ghost's attention-trace surveillance read, Syndicate's public-leverage calculation | Art 00 §7 |
| Doctrine alignment | ✓ | Network −1 cost + portrait +1; Directorate −1 cost + portrait +1 — formal accusation aligns with institutional/broadcast doctrines. Ghost −1 portrait: public accusation = self-exposure. Intel token affinity is doctrinally neutral. No target_faction → doctrine_mod not applicable | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard | Art 04 §6.2 |
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding | Art 04b §4 |
| Balance | ✓ | Base threshold 35 is demanding; Intel token affinity rewards preparation. Fail/failcrit PS penalties create real downside | Art 02 §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1, Directorate +1, Ghost −1: submitter-bounded. PS shifts are game effects not Portrait (DIR.PA.2) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted action; no zone reference. ring_mod = None. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (optional, Fresh — spent on resolution regardless; Art 02 §6); faction native × 2 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 4; Intel token submitted with case at Phase B; token spent regardless | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
STD.PA.4 = Card(
    id      = "STD.PA.4",  version="v1.0",
    name    = "Public Censure",
    tagline = "Formally accuse another faction of conduct contrary to the city's interest.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Standing,  function = Shift,  subject = StandingMarker,

    beat            = 4,
    resolution      = d100,
    threshold       = 35,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Contested",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = (
        faction(acting).holds_intel_token(faction=target, age=Fresh): threshold += 15,  # token optional; spent on resolution
        faction(acting) == Network:     cost.faction(native) -= 1,
        faction(acting) == Directorate: cost.faction(native) -= 1,
    ),
    restriction = target_faction != faction(acting),
    cost        = resource.faction(acting) * 2,

    success     = (faction(target).standing -= 2, faction(acting).standing += 1),
    successcrit = None,
    fail        = faction(acting).standing -= 1,
    failcrit    = faction(acting).standing -= 2,

    portrait = {
        Network:     PortraitEntry(submitter=+1),
        Directorate: PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },

    narrative    = "A formal accusation in New Meridian is not a rumor. It is a claim that goes into the record and demands a response.",
    perspectives = {
        Guild:       "We do not make accusations we cannot support. But we do not stay silent when the conduct is clear.",
        Directorate: "Formal censure is the legitimate response to misconduct. The mechanism exists for a reason.",
        Network:     "The city deserves to know. We are not making an allegation — we are making a fact public.",
        Ghost:       "Public censure creates public attention. We note that the accusation traces back to whoever filed it.",
        Syndicate:   "Censure is leverage applied publicly. The question is always: what does the target do next?",
    },
    design_note  = "PS attack card of the standard set. Base threshold 35 — demanding. Fresh Intel token (optional, placed on PA at Art 03 §9.2.0, spent regardless of outcome) provides +15 threshold. Network/Directorate −1 cost each. Fail/failcrit PS penalties punish reckless censure. Ghost −1 portrait: public accusation = self-exposure. PS shifts in success/fail are game effects, not Portrait (DIR.PA.2).",
    arbiter_note = "At Art 03 §9.2.0: acting faction places PA with Target Profile face-down; Intel token (if submitted) placed on card. At Art 03 §9.4.3.1.1: flip Target Profile face-up; note target faction. Beat 4: threshold = 35 + 15 if Fresh Intel token on card. On success: target −2 PS, acting +1 PS; Intel token spent. On fail: acting −1 PS; Intel token still spent. On failcrit: acting −2 PS.",
)
```

---

### STD.PA.5 — ON THE RECORD
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Formal public attribution of a covert action. Requires an Intel token naming the target faction (spent regardless of outcome) — you cannot make the accusation without evidence. Token age determines confidence: Fresh = threshold 50, Stale = 35. Network gains +10 threshold bonus (broadcasting attribution is their mode). Ghost's portrait at −2 (the highest negative in the set) reflects that Ghost's doctrine protects operational anonymity across the entire table — attributing any faction's covert operation is a violation of Ghost's belief that understanding accumulates privately.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public attribution of covert operations is a core political act — creates accountability where covert ops sought deniability | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's evidence-responsibility framing, Directorate's institutional/conditional support, Network's right-to-know, Ghost's doctrine of operational privacy (principle not preference), Syndicate's leverage-timing calculation | Art 00 §7 |
| Doctrine alignment | ✓ | Network portrait +1: broadcasting attribution is doctrinal. Ghost portrait −2 (highest negative in set): attributing any faction's op violates Ghost's belief that operational anonymity protects the whole table's intelligence discipline. Others: no doctrinal stake in the attribution mechanism itself | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard — any faction can attribute | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Reveal / ActionAttribution | Art 04b §4 |
| Balance | ✓ | Token cost + resource cost; token age tiers threshold (Fresh 50, Stale 35); Expired excluded. Fail: self-PS loss (false or botched attribution). High success PS reward reflects the significance of public attribution | Art 02 §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1 (doctrine), Ghost −2 (doctrine): both submitter-bounded. No Portrait shifts in effect fields | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted attribution; no zone reference. ring_mod = None. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (faction=target, age=Fresh or Stale — Expired excluded per restriction; Art 02 §6); faction native × 1 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 4; Intel token submitted with case; token age determined at Beat 4 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
STD.PA.5 = Card(
    id      = "STD.PA.5",  version="v1.0",
    name    = "On the Record",
    tagline = "Formally attribute a recent covert action to a named faction before the city.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Information,  function = Reveal,  subject = ActionAttribution,

    beat            = 4,
    resolution      = d100,
    threshold       = 35,  # base = Stale token; Fresh → +15 via affinity; Network → +10 via affinity
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Contested",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = (
        faction(acting).holds_intel_token(faction=target, age=Fresh):  threshold += 15,
        faction(acting) == Network: threshold += 10,
    ),
    restriction = faction(acting).holds_intel_token(faction=target, age__in=[Fresh, Stale]),  # Expired excluded — too degraded to constitute usable attribution evidence
    cost        = resource.faction(acting) * 1 + intel_token(target=faction(target)) * 1,

    success     = (
        arbiter.announce(attribution=target_faction, context=intel_token.quarter),
        faction(target).standing  -= 2,
        faction(acting).standing  += 2,
    ),
    successcrit = None,
    fail        = faction(acting).standing -= 1,
    failcrit    = None,

    portrait = {
        Network: PortraitEntry(submitter=+1),
        Ghost:   PortraitEntry(submitter=-2),
    },

    narrative    = "In New Meridian, there are very few true secrets. There are only secrets that haven't been made public yet.",
    perspectives = {
        Guild:       "If we can prove it, we will say it. What someone did with their dispatch case is their own responsibility.",
        Directorate: "Public attribution is the mechanism for accountability. We support it when the evidence supports us.",
        Network:     "The city has a right to know who is operating in its districts. We are providing that record.",
        Ghost:       "We do not publish what we know about other factions' operations. That is a principle, not a preference.",
        Syndicate:   "Attribution is leverage. The question is always: what is the information worth on the table versus in hand?",
    },
    design_note  = "Standard information-attribution PA. Restriction requires Fresh or Stale token — Expired excluded (too degraded to constitute usable attribution evidence). Token spent regardless of outcome. Threshold from token age (Fresh = 50, Stale = 35) + Network +10. Ghost portrait −2: attributing any faction's covert op violates Ghost's belief that operational anonymity protects the intelligence discipline of the whole table — the highest negative portrait value in the set.",
    arbiter_note = "At Art 03 §9.2.0: Intel token placed on PA card with Target Profile face-down. At Art 03 §9.4.3.1.1: flip Target Profile face-up; verify token age — Fresh or Stale satisfies restriction; Expired does not. Beat 4: threshold = age-based (50 Fresh / 35 Stale) + 10 if Network. On success: announce '[Acting faction] attributes [op type, quarter] to [target faction].' Target −2 PS, acting +2 PS. Token spent. On fail: acting −1 PS. Token spent regardless.",
)
```

---

### STD.PA.6 — ECONOMIC SANCTION
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
The economic attack card of the standard PA set. PS is intentionally reversed from intuitive expectation: the faction applying sanctions takes a public standing penalty (aggressor optic), while the target gains sympathy. The card's value is purely the resource damage (target loses 2 native) — players trade PS for economic impact. This creates meaningful faction differentiation: Ghost plays it readily (low PS concern), Network is reluctant (PS-dependent), Syndicate is the natural primary user (Capital leverage, threshold bonus). Fail/failcrit penalise the acting faction — a failed public sanction looks worse than not attempting one.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Economic sanctions are a legitimate public instrument — all factions can apply financial pressure | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's last-resort restraint, Directorate's formal instrument framing, Network's neutral observation, Ghost's collateral-attention awareness, Syndicate's capital-discipline framing | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate +15 threshold + portrait +1: Capital leverage doctrine aligns with economic pressure. Guild portrait −1: economic weapons conflict with permanence-through-building doctrine. doctrine_mod accounts for target relationship | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Remove / NativeResource | Art 04b §4 |
| Balance | ✓ | Acting faction absorbs −1 PS on success as the cost of the aggressor position. Threshold 40 + Syndicate +15. Value = resource denial (up to 2 native, floor = 0), not PS gain | Art 02 §6–§7 |
| Effect duration | ✓ | Resource removal and PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Syndicate +1, Guild −1: submitter-bounded. PS shifts are game effects, not Portrait | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted action; no zone reference. ring_mod = None. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource (target's supply, Art 02 §8); faction native × 1 cost (Art 02 §8). Floor clause is procedural | Art 02 §8 |
| Supported by game procedure | ✓ | Beat 4; ARBITER removes up to 2 native resources from target (floor = 0 — all available if fewer than 2) | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
STD.PA.6 = Card(
    id      = "STD.PA.6",  version="v1.0",
    name    = "Economic Sanction",
    tagline = "Publicly impose economic pressure on a faction, forcing resource loss.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Remove,  subject = NativeResource,

    beat            = 4,
    resolution      = d100,
    threshold       = 40,
    ring_mod        = None,
    doctrine_mod    = {Neighbor: +10, Opposed: -10},
    trigger         = None,
    resolution_type = "Contested",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(acting) == Syndicate: threshold += 15,
    restriction = None,
    cost        = resource.faction(acting) * 1,

    success     = (
        faction(target).resource(native) -= min(2, faction(target).resource(native)),  # floor = 0
        faction(acting).standing -= 1,  # aggressor optic
        faction(target).standing += 1,  # sympathy
    ),
    successcrit = None,
    fail        = faction(acting).standing -= 1,
    failcrit    = faction(acting).standing -= 2,

    portrait = {
        Syndicate: PortraitEntry(submitter=+1),
        Guild:     PortraitEntry(submitter=-1),
    },

    narrative    = "Economic pressure in New Meridian is always visible. The faction applying it accepts that visibility as part of the cost.",
    perspectives = {
        Guild:       "Economic weapons undermine the table's capacity to build. We use them only when other options are exhausted.",
        Directorate: "Sanctions are a formal instrument of institutional pressure. Applied correctly, they do not require apology.",
        Network:     "We note who imposes economic sanctions on whom. The city will form its own judgment.",
        Ghost:       "Public economic aggression makes enemies. We observe the transaction and its aftermath.",
        Syndicate:   "Capital discipline is a legitimate instrument. The target chose to be in a position where this was possible.",
    },
    design_note  = "PS reversed by design: acting −1 (aggressor optic), target +1 (sympathy) on success. Value is purely resource denial (target loses up to 2 native; floor = 0 — remove all available if fewer than 2). Faction differentiation: Ghost plays freely (PS-agnostic), Network avoids (PS-dependent), Syndicate primary user (+15 threshold). Guild −1 portrait: economic weapons conflict with permanence-through-building doctrine.",
    arbiter_note = "Beat 4. d100 vs threshold 40 (+15 Syndicate; doctrine_mod Neighbor +10 / Opposed −10). On success: remove 2 native resources from target, or all available if fewer than 2 (floor = 0); acting −1 PS; target +1 PS. On fail: acting −1 PS only. On failcrit: acting −2 PS.",
)
```

---

### STD.PA.7 — PUBLIC ADDRESS
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Self-directed PS building — fills the gap in the standard set (STD.PA.4 attacks opponent's PS; STD.PA.7 builds own). Cheap (1 native), certain (Automatic), grants +2 PS in exchange for having presence in the target district. No faction monopolises public communication — all factions make public statements — but the portrait reflects who finds it doctrinally meaningful (Directorate, Network) versus costly (Ghost). The requirement to already have presence prevents factions from claiming standing in districts where they have no legitimacy.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public statements and rallies are universal political acts | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's building-primary-but-does-speak, Directorate's institutional communication expectation, Network's terse "this is what we do", Ghost's analytical surveillance framing of own public acts, Syndicate's investment/return calculation | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate +1, Network +1: institutional communication and broadcasting are both core doctrinal expressions. Ghost −1: public address = attention = exposure risk. Others: no strong doctrinal alignment with the act itself | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard | Art 04 §6.2 |
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding — +2 PS is a relative position change, not an unconditional grant | Art 04b §4 |
| Balance | ✓ | 1 native for +2 PS with presence restriction. Cheap but not free; presence requirement prevents abuse | Art 02 §6–§7 |
| Effect duration | ✓ | PS shift is immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1, Network +1, Ghost −1: submitter-bounded. No direct PS shift in portrait fields | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone; restriction checks presence in target district ✓ | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken — restriction check (Art 02 §6); faction native × 1 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 4; restriction at Beat 0 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
STD.PA.7 = Card(
    id      = "STD.PA.7",  version="v1.0",
    name    = "Public Address",
    tagline = "Rally public support in a district where you operate.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Standing,  function = Shift,  subject = StandingMarker,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = district(target).faction(acting).presence > 0,
    cost        = resource.faction(acting) * 1,

    success     = faction(acting).standing += 2,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Directorate: PortraitEntry(submitter=+1),
        Network:     PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },

    narrative    = "Presence without voice is presence waiting to become something else.",
    perspectives = {
        Guild:       "We speak through what we build. But occasionally, we also speak.",
        Directorate: "A formal address in a district we operate in is institutional communication. It is expected.",
        Network:     "This is what we do. The address is the point.",
        Ghost:       "Public addresses are signals. We note the frequency, the district, and the audience.",
        Syndicate:   "Standing is a resource. We invest in it when the return is clear.",
    },
    design_note  = "Self-directed PS building — the missing card type in the standard set. STD.PA.4 attacks opponent PS; STD.PA.7 builds own. Automatic, 1 native, +2 PS. Presence requirement: cannot claim standing in districts where you have no legitimacy. Directorate +1 and Network +1: institutional communication and broadcasting are doctrinal for both. Ghost −1: public address = attention = exposure risk.",
    arbiter_note = "Beat 4. Restriction at Beat 0: acting faction must have at least 1 presence token in declared district. If restriction fails, PA voided. On success: acting faction +2 PS.",
)
```

---

### STD.PA.8 — TABLE AN ACCORD
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
The formal bilateral agreement mechanism of the standard set. Playing STD.PA.8 at Phase B publicly declares an intent to propose an Accord with a named target faction. ARBITER delivers a blank AccordForm to the submitting faction at Beat 4. The faction drafts the terms and places the completed form in the Accord Placement Area at their discretion; formation and execution procedure per Art 06 §9.4. PS consequences apply at Debrief on acceptance or decline. Cost is 1 native flat — the PA submission slot (3 per Quarter; draw-dependent) is the primary gate on Accord access; the resource cost signals accessible diplomacy rather than gating potential. Ghost portrait −1: Accords create commitments, which Ghost avoids structurally.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal accord proposals are a core political act — every faction can and does make bilateral agreements | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's pragmatic/permanence framing, Directorate's institutional mechanism preference, Network's record-and-observe stance, Ghost's obligation-aversion (not value-aversion), Syndicate's asset/exit-cost calculus | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate portrait +1: bilateral stability is Directorate institutional doctrine. Ghost −1: Accords create commitments. Syndicate affinity removed — Syndicate manipulates Accords through faction-specific cards, not standard proposals. doctrine_mod not applicable | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / Standard — BilateralAgreement outcome type | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Add / AccordAgreement | Art 04b §4 |
| Balance | ✓ | Cost 1 native flat (all factions). PA slot is the primary gate — 3 PA slots per Quarter, card is draw-dependent. PS vote mechanic gates proposal quality. At 1 native the form price signals accessible diplomacy; the slot cost and PS mechanics provide volume and quality control. L200. | Art 02 §6–§7 |
| Effect duration | ✓ | AccordForm delivery is Immediate. Form lifecycle and cross-Quarter persistence governed by Art 06 §9.4. | Art 04 §5 P19; Art 06 §9.4 |
| Persistence | ✓ | Immediate — PA delivers blank AccordForm at Beat 4; form lifecycle governed by Art 06 §9.4. | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1, Ghost −1: submitter-bounded. No PS shifts in portrait fields | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no zone reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | AccordForm (Art 06 §9.2). No new components. | Art 06 §9.2 |
| Supported by game procedure | ✓ | Phase B: target faction named publicly. Beat 4: blank AccordForm delivered to submitting faction. Faction drafts and places per Art 06 §9.4. Execution at Debrief. | Art 03 Phase B; Art 06 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Upkeep income tracking:** n/a — no ongoing income on STD.PA.8 itself (Accord income terms are player-drafted per Art 06 §9.3).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
STD.PA.8 = Card(
    id      = "STD.PA.8",  version="v1.0",
    name    = "Table an Accord",
    tagline = "Formally propose a binding agreement with another faction, placed on the public record.",
    type    = PublicAct,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Add,  subject = AccordAgreement,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = BilateralAgreement,
    persistence     = Immediate,  # AccordForm delivery resolves at Beat 4; form lifecycle governed by Art 06 §9.4
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,  # named publicly at Phase B declaration
    target_object   = AccordForm,

    target_taxonomy=None,
    affinity    = None,
    restriction = (
        target_faction != faction(acting) and
        accord(faction(acting), faction(target)).active == False
    ),
    cost = resource.faction(acting) * 1,

    success = arbiter.deliver(faction(acting), AccordForm(blank)),
    # Faction drafts terms per Art 06 §9.3; places in Accord Placement Area at their discretion.

    # BilateralAgreement resolution at Debrief: PS consequences per Art 06 §9.4

    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {
        Directorate: PortraitEntry(submitter=+1),
        Ghost:       PortraitEntry(submitter=-1),
    },

    narrative    = "The Table exists to make agreements. This is one of the few acts that uses it as intended.",
    perspectives = {
        Guild:       "We make agreements when they serve what we are building. We honor them for the same reason.",
        Directorate: "A formal accord is the institutional mechanism for bilateral stability. We prefer it to informal arrangements.",
        Network:     "Every formal agreement is a piece of the city's record. We observe the terms and what follows.",
        Ghost:       "Accords create obligations. We are not opposed to what they achieve — only to what they commit us to.",
        Syndicate:   "Every accord is an asset. The question is who controls the terms and what the exit costs.",
    },
    design_note  = "Accord initiation PA. Cost = 1 native flat (all factions). PA slot is the primary gate: 3 PA slots per Quarter, card is draw-dependent. PS vote at decline gates proposal quality (unreasonable proposal = proposer −1 PS). Blank form is a proposal, not a contract; 1 native signals that diplomacy is accessible. L200. Ghost −1: Accords are commitments.",
    arbiter_note = "Phase B: target faction named publicly. Beat 4: deliver blank AccordForm from ARBITER tableau supply to submitting faction. No timing constraint on drafting or placement — form queued for next Debrief when placed in Accord Placement Area. At Debrief: target reviews, accepts or declines per Art 06 §9.4. PS consequences per Art 06 §9.4.",
)
```

---


---

## Guild
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#guild-covert-operations) · [Public Acts](#guild-public-acts)

---

### Guild — Covert Operations
[↑ Guild](#guild)

| Card | Name |
|------|------|
| [GUI.CA.1](#c11-fortify-structure) | Fortify Structure |
| [GUI.CA.2](#c12-materials-acquisition) | Materials Acquisition |
| [GUI.CA.3](#c13-foundation-rights) | Foundation Rights |
| [GUI.CA.4](#c14-construction-crew) | Construction Crew |
| [GUI.CA.5](#c15-infrastructure-yield) | Infrastructure Yield |
| [—](#guild-labor-contract) | Labor Contract |

### GUI.CA.1 — FORTIFY STRUCTURE
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive structural defense card. The hardest counter to STD.CA.2 Demolish in the set — not a threshold reduction (STD.CA.10 Protect) but total immunity. Cost vs reward: 1 Capacity is relatively cheap for full immunity; the Beat 2 commitment is the real cost, since you're betting a slot that your structure will be targeted this round. Guild's structural investment is its primary territorial asset; this card formalizes that the Guild defends what it has built.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Structural reinforcement as covert preparation — fortification work is done quietly before Beat 3 resolution window. Guild-exclusive competency; no other faction has the structural standing to claim total demolition immunity. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | "The Guild does not abandon what it has built" is the doctrine statement. Network's "what's inside them" is the sharpest counter-perspective. Three perspectives only (Guild, Network, Directorate) — FactionSpecific card; Ghost and Syndicate absence acceptable. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild-exclusive card; structural defense is core Guild doctrine. Portrait submitter=+1 captures this. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: fortification is covert prep. FactionSpecific (Guild): total immunity is Guild's unique structural competency, not available to others. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Territory` — per Art 04b §4.6, Protect distributes to target's layer; target is StructureBlock (Territory). `function = Protect`, `subject = StructureBlock` — correctly scoped. | Art 04b §4.6, §5 |
| Balance | ✓ | Beat 2 positional wager; wrong-read wastes slot. 1 Capacity cost. Immunity is total but Quarter-limited; one play protects one structure only. | Art 02 §7, §8 |
| Effect duration | ✓ | Quarter-limited: immune flag persists until end of Quarter. Appropriate for a structural defense card. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). Guild's structural-investment doctrine grounds the affinity. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: Guild structure in target district. | Art 01 §6, §7 |
| Supported by components | ✓ | StructureBlock (restriction + immunity target); Capacity cost. | Art 02 §7, §8 |
| Supported by game procedure | ⚠ | Submitted at Dispatch (Art 03 §9.1); Beat 2 row (Art 03 §9.4.0 Beat 0); immunity flag applied at Beat 3 when STD.CA.2 Demolish resolves (Art 03 §9.4.2 Beat 3). **Open:** Art 03 §9.4.2 Beat 2 covers Countermeasures and Protect only — no procedure defined for Fortify Structure immunity flag. Gap in Art 03. | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Art 03 §9.4 procedure gap:** §11 Beat 2 section does not include a procedure for applying the Fortify Structure immunity flag. Extension required before GUI.CA.1 can be fully procedurally supported.
- **Arbiter note:** ARBITER retains awareness after Beat 2 opens. Immunity applied when STD.CA.2 Demolish resolves in Beat 3. Verify Art 03 §9.4.2 Beat 2 extension covers this step.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
GUI.CA.1 = Card(
    id      = "GUI.CA.1",  version = "v1.1",
    name    = "Fortify Structure",
    tagline = "Reinforce a structure against demolition this Quarter.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Protect,  subject = StructureBlock,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Positional wager",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = StructureBlock,

    target_taxonomy=None,
    affinity    = None,
    restriction = district(target).faction(acting).structure > 0,
    cost        = resource.faction(acting).capacity * 1,

    success     = district(target).faction(acting).structure.set_flag(immune_to_demolish=True),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "The Guild does not abandon what it has built.",
    perspectives = {
        Guild:       "Reinforcement is not fear. It is preparation.",
        Network:     "Hardened walls are preparation. What's inside them decides whether the cost was worth it.",
        Directorate: "A structure immune to demolition is a structure immune to code review. We notice these arrangements.",
    },
)
```

---

### GUI.CA.2 — MATERIALS ACQUISITION
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive economic counter to demolition — not a defense card but a revenue card. The Guild names a target faction at submission, betting a Beat 2 slot that this faction will execute STD.CA.2 this Quarter. Cost vs reward: zero resource cost; the action slot itself is the bet. Success mirrors STD.CA.2's cost exactly (1 native + 1 district native) — intentionally self-calibrating; if STD.CA.2's cost changes in playtesting, GUI.CA.2's reward scales automatically. A wrong read wastes the slot with no other loss.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Positioning to recover demolition costs before demolition happens — uniquely Guild, fits the game's economic-intelligence frame. Beat 2 commitment watching for opponent's Beat 3 action is a clean trigger structure. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Three perspectives (Guild, Syndicate, Ghost) — FactionSpecific card; acceptable. Syndicate's "we simply call it by a different name" and Ghost's "already told us what it knows" both provide doctrinal depth. | Art 00 §7 |
| Doctrine alignment | ✓ | `target_faction = faction.opponent`, `doctrine_mod = None` — explicit design choice. Recovery amount mirrors STD.CA.2's cost regardless of doctrinal distance; the Guild gets paid the same whoever demolished. Correct. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: observation and positioning is covert; payment materializes via case mechanism. FactionSpecific (Guild): treating demolition as a Guild service is uniquely Guild doctrine. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Economy` — returning NativeResource is capital flow, correctly Economy under Art 04b §4.4. `function = Add`, `subject = NativeResource` — Recover retired S106 (04b-20); trigger-context Add is the correct primitive. | Art 04b §4, §5 |
| Balance | ✓ | Zero resource cost; action slot is the only cost. Trigger-contingent — wrong read wastes slot with no other penalty. First qualifying Demolish from named faction only. | Art 02 §8 |
| Effect duration | ✓ | Instantaneous: resources delivered once when trigger fires. No persistent state. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = faction(target).completes(CovertOp, id=STD.CA.2)` — well-defined; ARBITER confirms at Beat 3. Note: `id=STD.CA.2` uses variable name, not integer — update to `id=2` when DB integers assigned (non-material; carry). | Art 04 (STD.CA.2) |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). | Art 04 §6.2 |
| Supported by zones | N/A | `target_district = None` — trigger monitors named opponent globally, not district-specific. | — |
| Supported by components | ✓ | NativeResource (Art 02 §8); STD.CA.2 Demolish as trigger source. | Art 02 §8; Art 04 (STD.CA.2) |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); placed in Beat 2 row (Art 03 §9.4.0 Beat 0); trigger fires when named faction completes STD.CA.2 at Beat 3 (Art 03 §9.4.2 Beat 3); delivery via ARBITER case (Art 07). | Art 03 §9, §11; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Arbiter note:** ARBITER confirms trigger at Beat 3. Only the first qualifying Demolish from the named faction this Quarter triggers. Effect delivered in case.
- **Trigger notation (non-material):** `id=STD.CA.2` is a variable name reference. Update to `id=2` when DB integers are assigned.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
GUI.CA.2 = Card(
    id      = "GUI.CA.2",  version = "v1.1",
    name    = "Materials Acquisition",
    tagline = "Recover the costs of demolition as subcontract payment.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Economy,  function = Add,  subject = NativeResource,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = faction(target).completes(CovertOp, id=STD.CA.2),
    resolution_type = "Positional wager",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = NativeResource,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = None,

    success     = (
        faction(acting).resource.native += 1,
        faction(acting).resource.native += 1   # mirrors STD.CA.2.cost: 1 faction native + 1 district native
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "In New Meridian, even demolition is a Guild service.",
    perspectives = {
        Guild:     "We do not need to swing the hammer ourselves. We simply ensure we are paid when someone else does.",
        Syndicate: "Positioning to profit from someone else's action before they take it. The instinct is sound. We simply call it by a different name.",
        Ghost:     "A faction that announces it expects demolition before demolition happens has already told us what it knows.",
    },
)
```

---

### GUI.CA.3 — FOUNDATION RIGHTS
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive first-entry card for unclaimed districts. Unclaimed territory has no established resource infrastructure, hence Capacity-only cost. Threshold 25 reflects genuine first-mover difficulty — unclaimed territory resists entry even for the faction with the deepest historical claim. Crit success upgrades presence to presence+structure (immediate foothold). Crit fail is politically the most sensitive outcome: a failed foundation claim is a regulatory event, and the Directorate receives an Intel Token silently. Guild never knows the paper trail was created.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | First-entry territorial claim as covert operation — unannounced land assertion fits Guild's historical-precedence doctrine. The Directorate's jurisdictional counter makes the doctrinal tension mechanical rather than just narrative. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | "The Guild was here before the city had a name" is the doctrine statement. Three perspectives (Guild, Network, Directorate) — FactionSpecific card; acceptable. Directorate's "legal process, not archive" is the sharpest counter. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild territorial-precedence doctrine (first-mover claim). Crit fail delivers Intel Token to Directorate — Directorate's regulatory oversight role is doctrinal, not incidental. Guild portrait submitter=+1 captures alignment. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Guild) — unannounced territorial claim. Covert until established. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Territory` — placing first presence is a territorial operation. `function = Add`, `subject = PresenceToken` — correctly scoped. Crit success adds StructureBlock (stacks with success; same layer). | Art 04b §4, §5 |
| Balance | ⚠ | Threshold 25 + ring_mod {0: −15} = effective threshold 10 in Ring 0. **Open:** Near-automatic for unclaimed Ring 0 districts — should first-entry be that easy? Consider raising base to 35–40. Crit success (presence + structure simultaneously) is a significant leap; confirm intent. | Art 01 §7; Art 02 §6, §7 |
| Effect duration | ✓ | Permanent: presence and structure persist until removed. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). `failcrit` dispatches IntelToken to Directorate — game effect, not Portrait shift (DIR.PA.2 clear). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: total presence == 0 (unclaimed only). | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken (success); StructureBlock (crit success); Capacity cost; IntelToken to Directorate on crit fail. | Art 02 §6, §7, §8; Art 02 §12 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); Beat 3 row (Art 03 §9.4.0 Beat 0); d100 threshold 25 with ring_mod; ARBITER silent IntelToken delivery to Directorate on crit fail (Art 03 §9.4.2 Beat 3; Art 07). | Art 03 §9, §11; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Balance — Ring 0 threshold:** Effective threshold 10 in Ring 0 (25 − 15). Near-automatic for unclaimed city-center districts. Consider raising base threshold to 35–40. Confirm before v1.2.
- **Crit success design:** Success = presence only; crit success stacks +structure. Verify this is the intended "presence + structure" foothold, not just structure replacing presence.
- **Arbiter note:** On crit fail: deliver 1 Intel Token naming Guild to Directorate via case. Do not notify Guild.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
GUI.CA.3 = Card(
    id      = "GUI.CA.3",  version = "v1.1",
    name    = "Foundation Rights",
    tagline = "Claim a foothold in territory no other faction has entered.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Add,  subject = PresenceToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 25,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = district(target).presence.total == 0,
    cost        = resource.faction(acting).capacity * 1,

    success     = district(target).faction(acting).presence += 1,
    successcrit = district(target).faction(acting).structure += 1,
    fail        = None,
    failcrit    = game.dispatch(Directorate, IntelToken(faction=acting, quarter=game.quarter)),

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "The Guild was here before the city had a name.",
    perspectives = {
        Guild:       "Unclaimed territory is not unknown to us. We have records going back further than anyone else at this table.",
        Network:     "The Guild's records go back further than ours. What they do with that history is what we watch.",
        Directorate: "Precedence is established through legal process, not through whoever kept the longer archive.",
    },
)
```

---

### GUI.CA.4 — CONSTRUCTION CREW
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive rush-construction card — bypasses STD.CA.1's presence prerequisite at premium cost and elevated difficulty. Threshold 65 models that unauthorized construction (without prior presence) is significantly harder than licensed work. Cost: 3 Capacity vs STD.CA.1's 1 faction native + 1 district native — a premium for skipping the prerequisite. Crit fail is deliberately multi-faction: failed unauthorized construction triggers both Ghost surveillance and Syndicate resource extraction — the city's two most opportunistic actors benefit from the Guild's overreach.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Rush construction without prior presence — unauthorized build is covert, high-risk, and distinctly Guild. Ghost and Syndicate as crit-fail beneficiaries is doctrinally perfect (the two most opportunistic actors). | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Three perspectives (Guild, Network, Ghost) — FactionSpecific card; acceptable. Ghost's "better at covert operations than they admit" is the sharpest outside read. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild construction doctrine (rush, without permission). Crit fail rewards Ghost (Intel Token) and Syndicate (district native) — explicitly doctrinal: the two most opportunistic actors benefit from Guild overreach. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: unauthorized construction is covert until established. FactionSpecific (Guild): rush-build without prerequisites is exclusively Guild. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Submission` — primary design intent is removing the STD.CA.1 presence prerequisite (a restriction on a CovertOperation). Territorial outcomes (presence + structure) are the consequence, not the driver. `function = RemoveRestriction`, `subject = CovertOperation` — correctly scoped per design intent. | Art 04b §4, §5 |
| Balance | ✓ | High cost (3 Capacity), high threshold (65). Crit fail rewards both Ghost (Intel Token) and Syndicate (district native) — asymmetric penalty for overreach. Net: saves STD.CA.3+STD.CA.1 sequential plays at the cost of one high-risk probabilistic slot. | Art 02 §6, §7, §8; Art 02 §12 |
| Effect duration | ✓ | Permanent: presence and structure placed on success persist. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). `failcrit` delivers IntelToken/native to opponents — game effects, not Portrait shifts (DIR.PA.2 clear). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: no existing Guild structure in target district. Ring mods apply normally. | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken + StructureBlock on success; Capacity cost; IntelToken to Ghost + district native to Syndicate on crit fail. | Art 02 §6, §7, §8; Art 02 §12 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); Beat 3 row (Art 03 §9.4.0 Beat 0); d100 threshold 65 with ring_mod; ARBITER delivers crit fail rewards to Ghost and Syndicate (Art 03 §9.4.2 Beat 3; Art 07). | Art 03 §9, §11; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Arbiter note:** Crit fail: deliver 1 Guild Intel Token → Ghost and 1 district native → Syndicate via case. Do not notify Guild.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
GUI.CA.4 = Card(
    id      = "GUI.CA.4",  version = "v1.1",
    name    = "Construction Crew",
    tagline = "Build a structure before your presence is fully established.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Submission,  function = RemoveRestriction,  subject = CovertOperation,

    beat            = 3,
    resolution      = d100,
    threshold       = 65,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = district(target).faction(acting).structure == 0,
    cost        = resource.faction(acting).capacity * 2 + resource.faction(acting).findings * 1,

    success     = (
        district(target).faction(acting).presence += 1,
        district(target).faction(acting).structure += 1
    ),
    successcrit = district(target).faction(acting).presence += 1,
    fail        = None,
    failcrit    = (
        game.dispatch(Ghost, IntelToken(faction=acting, quarter=game.quarter)),
        game.transfer(district(target).resource.native, 1, faction(Syndicate))
    ),

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "The Guild does not always wait for permission.",
    perspectives = {
        Guild:    "Sometimes the crews arrive before the paperwork. This is not an accident.",
        Network:  "We know this method. Presence before permission is how this city was actually built.",
        Ghost:    "Establishing presence before authorization is requested — the Guild is better at covert operations than they admit.",
    },
    design_note  = "Cost reasoning: 2 Capacity + 1 Findings (Mid-tier). Findings identify the un-zoned loopholes necessary to bypass prerequisites and break ground immediately.",
)
```

---

### GUI.CA.5 — INFRASTRUCTURE YIELD
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive passive income card — the economic expression of territorial control. Zero cost reflects that drawing from established infrastructure is not a new expenditure; it is the return on prior investment. The sole gate (Established or Dominant control tier) makes this card valuable precisely because it rewards maintained territorial control. Counter-lever is territorial: the card becomes unplayable if the Guild loses control tier, creating natural interdependence with STD.CA.1/STD.CA.3.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Passive income from controlled infrastructure is the natural economic expression of Guild territorial control. Covert framing (yield not publicly attributed) fits the operations register. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Three perspectives (Guild, Syndicate, Directorate) — FactionSpecific card; acceptable. Syndicate's "billing us for the water" is the sharpest outside read. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild infrastructure-ownership doctrine — return on prior investment. Guild↔Syndicate are Opposed: Syndicate believes it should capture this yield, not the Guild ("billing us for the water"). No opponent target → doctrine_mod N/A; Syndicate portrait entry warrants consideration (see Portrait validity). | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: yield is not publicly attributed. FactionSpecific (Guild): infrastructure-ownership income is exclusively Guild. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Economy` — adding NativeResource is capital flow, correctly Economy under Art 04b §4.4. `function = Add`, `subject = NativeResource` — correctly scoped. | Art 04b §4, §5 |
| Balance | ⚠ | Zero cost + Automatic + no fail state + repeatable each Quarter. **Open:** Multiple Established/Dominant districts → multiple free native resources per Quarter, uncapped. Consider per-Quarter activation cap (e.g., max 2). Flag for playtesting. | Art 02 §6, §8 |
| Effect duration | ✓ | Instantaneous: +1 native delivered per play. No persistent state; card is re-playable each Quarter if restriction still met. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: Guild must hold Established or Dominant control tier in target district. | Art 01 §6, §7 |
| Supported by components | ✓ | NativeResource (Art 02 §8); control_tier states Established/Dominant (Art 02 §6). | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); Beat 3 row (Art 03 §9.4.0 Beat 0); Automatic resolution at Beat 3 (Art 03 §9.4.2 Beat 3). | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Balance — per-Quarter cap:** Zero cost + Automatic means uncapped income at scale. Guild controlling 3+ Established/Dominant districts earns 3+ free native resources per Quarter. Consider cap of 2 activations per Quarter; flag for playtesting.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
GUI.CA.5 = Card(
    id      = "GUI.CA.5",  version = "v1.1",
    name    = "Infrastructure Yield",
    tagline = "Draw resources from infrastructure you have already built.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Economy,  function = Add,  subject = NativeResource,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = district(target).faction(acting).control_tier IN [Established, Dominant],
    cost        = None,

    success     = faction(acting).resource.native += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "The Guild built New Meridian's infrastructure. Drawing from it is not theft. It is dividend.",
    perspectives = {
        Guild:       "We built this. Every unit we draw from it was always ours.",
        Syndicate:   "The Guild built the pipes. They are billing us for the water. We respect the position even if we resent the rate.",
        Directorate: "Infrastructure built under city contract belongs to New Meridian, not to the builder. We have the original agreements.",
    },
)
```

---

### Guild — LABOR CONTRACT
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Construction analogue to GUI.CA.2 Materials Acquisition — GUI.CA.2 covers demolition revenue, Labor Contract covers construction revenue. Together they implement the Guild doctrine that no structural change to New Meridian happens without Guild being paid. Beat 2 positional wager: Guild names a faction and bets an action slot on that faction building this Quarter. Zero resource cost means a wrong read loses only the slot. Payout mirrors STD.CA.1's cost (2 Capacity), making the card self-calibrating if STD.CA.1's cost changes in playtesting.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Construction fee mechanic — Guild monetises any faction's STD.CA.1 play; analogue to GUI.CA.2 Materials Acquisition (demolition revenue) completing the Guild doctrine that no structural change to New Meridian happens without Guild payment | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; limited perspectives in current spec — full voice set expected (confirm complete in code block) | Art 00 §7 |
| Doctrine alignment | ✓ | Guild only; zero resource cost (slot IS the bet); payout 2 Capacity mirrors STD.CA.1.cost — self-calibrating on balance pass; Beat 2 positional wager fits the "bet on opponent building" play style | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Guild) — Guild's passive revenue model | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — Recover retired S106 (04b-20); trigger-context Add is the correct primitive; STD.CA.3 exclusion confirmed locked S59 | Art 04b §4, §5 |
| Balance | ✓ | Payout 2 Capacity mirrors STD.CA.1.cost — self-calibrating | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: Capacity delivered at Beat 3 when trigger fires | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | Trigger = STD.CA.1 completion by named faction; first qualifying play only; Beat 2 positional wager monitors trigger across the round | Art 04 (STD.CA.1) |
| Portrait validity | ✓ | Confirm portrait entries present in code block — Guild faction-specific expected | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None; trigger monitors named faction globally | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource (Capacity); STD.CA.1 as trigger source; no new components | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 submission; trigger confirmed at Beat 3; ARBITER case delivery | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **STD.CA.3 scope confirmed excluded:** Labor Contract is a financial claim on physical construction (STD.CA.1) only. Campaign (STD.CA.3) does not trigger — no labor fee on presence/influence activity. Locked S59.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Draft S59 — design pass pending*

```python
GUI.CA.6 = Card(
    id      = "GUI.CA.6",  version="v1.0",  # ID pending PM05 04-n1
    name    = "Labor Contract",
    tagline = "Collect subcontract payment when a faction develops district infrastructure.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Economy,  function = Add,  subject = NativeResource,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = faction(target).completes(CovertOp, id=STD.CA.1),
    resolution_type = "Positional wager",
    outcome_type    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = NativeResource,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = None,

    success     = (
        faction(acting).resource.native += 1,
        faction(acting).resource.native += 1,  # mirrors STD.CA.1.cost: 1 faction native + 1 district native
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "In New Meridian, every foundation poured is a Guild invoice.",
    perspectives = {
        Guild:       "We do not ask to be compensated. We ensure that we are.",
        Directorate: "The Guild has found a way to treat infrastructure development as a private revenue stream. This requires a regulatory response.",
        Network:     "Every build is a Guild fee. Every fee is a constraint. The city grows on Guild's terms.",
    },
    design_note  = "Construction analogue to GUI.CA.2 Materials Acquisition. Together with GUI.CA.2 and 04-n2 passive rule: no faction demolishes or builds in New Meridian without Guild being paid. Trigger is STD.CA.1 only — Labor Contract is a financial claim on physical construction, not influence or presence activity. Payout mirrors STD.CA.1.cost (2 Capacity). First qualifying STD.CA.1 from named faction only.",
    arbiter_note = "At Beat 3: confirm whether named faction completed STD.CA.1 this Quarter. First qualifying play only. If triggered: deliver 2 Capacity to Guild's Dispatch Case.",
)
```

---


---

### Guild — Public Acts
[↑ Guild](#guild)

| Card | Name |
|------|------|
| [GUI.PA.1](#p09-civic-works-mandate) | Civic Works Mandate |
| [GUI.PA.2](#p10-infrastructure-bond) | Infrastructure Bond |

---

### GUI.CA.7 — BUYOUT CLAUSE *(stub)*
[↑ Covert Operations](#guild-covert-operations)

```python
GUI.CA.7 = Card(
    id      = "GUI.CA.7",  version = "v1.0",
    name    = "Buyout Clause",
    tagline = "Liquidate an opponent's real estate through an unblockable coercive eviction.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Remove,  subject = PresenceToken,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    trigger         = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    cost        = resource.faction(Guild).capacity * 2 + resource.faction(Guild).capital * 1,

    success     = "Guild pays 2 target.native resources to target_faction; arbiter.remove(presence_chip, district=target_district, faction=target_faction, count=1)",
    
    design_note = "Guild's territorial response gap filled. Coercive eviction via buyout. Cost reasoning: 2 Capacity + 1 Capital (Mid-tier). Liquidating real estate out from under an opponent."
)
```

---

---

### GUI.CA.8 — BUILDING INSPECTION *(stub)*
[↑ Covert Operations](#guild-covert-operations)

```python
GUI.CA.8 = Card(
    id      = "GUI.CA.8",  version = "v1.1",
    name    = "Building Inspection",
    tagline = "Condemn an opponent's building via weaponized zoning code.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,
    layer   = Territory,  function = Remove,  subject = StructureBlock,
    beat    = 3,  resolution = d100,  threshold = 60,
    cost    = resource.faction(Guild).capacity * 1 + resource.faction(Guild).mandate * 1,
    success = "Remove 1 target Structure Block. Guild gains +1 PS.",
    design_note = "A thematic variant of STD.CA.2 (Demolish). Bribe removed to keep resolution strictly blind via Arbiter."
)
```

### GUI.PA.1 — CIVIC WORKS MANDATE
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
Guild's prestige structure PA — a simultaneous double build in two named districts. One PA slot for two structures is the core value; the cost premium (4 Capacity vs two sequential P03s at 2 Capacity each using two PA slots across two Months) reflects the single-slot efficiency gain. Guild's faction affinity waives both district native costs. The PS reward (+3) is the highest of any standard or faction-specific single build card, reflecting the scale of the public commitment. Primary counter: Directorate's DIR.PA.1 (Regulatory Override) raises the cost of presence prerequisites; DIR.PA.1 (Issue Directive in prior design, now Regulatory Override) can be deployed against the district beforehand.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Simultaneous dual construction is Guild's maximum public commitment | Art 00 §7 |
| Voice fit | ✓ | Guild on-doctrine; Network (aligned): public commitment scale; Ghost (opposed): acting before the question is answered | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Guild-exclusive: 4 Capacity cost, district native waived for both districts, portrait +2 (double structure = doctrinal maximum). Directly serves permanence doctrine. No target_faction → doctrine_mod not applicable | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / StructureBlock — two targets | Art 04b §4 |
| Balance | ⚠ | Cost 4 Capacity; both district natives waived (Guild). PS +3. Single slot for two structures is efficient — balance review after playtesting | Art 02 §6–§7 |
| Effect duration | ✓ | StructureBlocks = Permanent board state; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Guild +2: submitter-bounded; double structure = maximum doctrinal expression | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.two — both named districts valid; restriction checks each independently | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock (Art 02 §7); PresenceToken — restriction (Art 02 §6); 4 Capacity — Guild faction native (Art 02 §8) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Both districts declared at Phase B; restriction checked at Beat 0; both-or-nothing rule | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
GUI.PA.1 = Card(
    id      = "GUI.PA.1",  version="v1.0",
    name    = "Civic Works Mandate",
    tagline = "Declare a public infrastructure program across two districts simultaneously.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Add,  subject = StructureBlock,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.two,  # both named at Phase B
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = faction(Guild): cost.resource.district(native) = 0,  # waived for both districts
    restriction = (
        district(target1).faction(Guild).presence > 0 and
        district(target2).faction(Guild).presence > 0 and
        district(target1).faction(Guild).structure == 0 and
        district(target2).faction(Guild).structure == 0
    ),
    cost = resource.faction(Guild).capacity * 2 + resource.faction(Guild).capital * 1 + resource.faction(Guild).mandate * 1,

    success     = (
        district(target1).faction(Guild).structure += 1,
        district(target2).faction(Guild).structure += 1,
        faction(Guild).standing += 3,
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+2)},

    narrative    = "The Civic Works Mandate is Guild's strongest public statement: we are not here to compete. We are here to build what New Meridian requires.",
    perspectives = {
        Guild:   "This is the declaration. Two districts, simultaneous, public. This is what we came here to do.",
        Network: "Two districts at once. When Guild commits at this scale, the announcement becomes the infrastructure. The public knows before the cement sets.",  # aligned
        Ghost:   "Guild builds when we have not yet established whether what is being built belongs in the answer. The structures will outlast the certainty they were built on.",  # opposed
    },
    design_note  = "Guild's prestige build PA. Cost reasoning: 2 Capacity + 1 Capital + 1 Mandate (Ceiling-tier). Capital secures the massive land footprint, while Mandate bypasses zoning laws to fast-track construction. Both-or-nothing: if either district fails restriction at Beat 0, full PA is voided. PS +3: highest single-card build reward. Portrait +2: double structure = doctrinal maximum. Counter: Directorate DIR.PA.1 Regulatory Override applied to either district beforehand raises presence-placement costs, potentially blocking prerequisite presence for this card.",
    arbiter_note = "Phase B: two distinct districts named. Beat 0: both restrictions checked simultaneously. If either fails (no Guild presence, or existing structure), entire PA voided; 4 Capacity returned; Guild takes Public Pass. Beat 4: place 1 structure in each declared district; Guild +3 PS.",
)
```

---

### GUI.PA.2 — INFRASTRUCTURE BOND
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
Guild's economic relationship PA. Distinct from STD.CA.9 (Fund) in cost currency (Capacity vs Capital) and mechanism (ongoing income Accord vs one-time payment). Guild pays 1 Capacity (form price, equitable with STD.PA.8 per L200/L201) and delivers 2 native resources to the target as a sweetener — the upfront investment that makes the Accord terms credible and acceptance worthwhile. ARBITER then delivers a blank AccordForm to Guild. Guild drafts the Infrastructure Bond terms (target pays 1 Capacity per Upkeep while Accord active) and places the completed form in the Accord Placement Area at their discretion per Art 06 §9.4. On acceptance, Guild recovers the sweetener over 2 Quarters and profits thereafter. Addresses 04-n11 (Guild↔Network neighbor cooperation): Network is the natural target given pentagram proximity.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Guild public investment in another faction's territory is narratively grounded — infrastructure serves both | Art 00 §7 |
| Voice fit | ✓ | Guild on-doctrine; Directorate (aligned): structural partnership recognition; Syndicate (opposed): extraction reframed as partnership | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Guild investment economy: 2 Capacity upfront, 1 Capacity/Upkeep return. Restriction (Guild Established adjacent) keeps it doctrinally grounded. Portrait +1. Addresses 04-n11 (Guild↔Network neighbor cooperation) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Add / AccordAgreement — the Accord is the primary artifact; resource delivery is the trigger | Art 04b §4 |
| Balance | ✓ | Cost 1 Capacity (form price, per L200/L201) + 2 native delivered to target (sweetener). Income 1 Capacity/Upkeep from target on Accord execution — net positive over 2+ Quarters. PA slot is the primary gate. L201. | Art 02 §6–§7 |
| Effect duration | ✓ | Resource delivery Immediate. AccordForm delivery Immediate; form lifecycle and cross-Quarter persistence governed by Art 06 §9.4. | Art 04 §5 P19; Art 06 §9.4 |
| Persistence | ✓ | Immediate — resource delivery and AccordForm delivery both resolve at Beat 4; form lifecycle governed by Art 06 §9.4. | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Guild +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; restriction uses Guild Established adjacency to target's presence (valid zone-based check) | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource (target delivery, Art 02 §8); AccordForm (Art 06 §9.2); Capacity × 2 cost (Art 02 §8). | Art 02 §8; Art 06 §9.2 |
| Supported by game procedure | ⚠ | Phase B: target faction named publicly. Beat 4: 2 native delivered; blank AccordForm delivered to Guild. Guild drafts bond terms; places per Art 06 §9.4. Upkeep income tracking requires Accord execution confirmation. | Art 03 Phase B; Art 06 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Upkeep income tracking:** Confirm Accord income procedure (target pays 1 Capacity/Upkeep to Guild at Upkeep Step 6 while Accord active) against Art 06 §9.4 execution model.
- **Upkeep income tracking:** Confirm Accord income procedure (target pays 1 Capacity/Upkeep to Guild at Upkeep Step 6 while Accord active) against Art 06 §9.4 execution model.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
GUI.PA.2 = Card(
    id      = "GUI.PA.2",  version="v1.0",
    name    = "Infrastructure Bond",
    tagline = "Publicly extend Guild infrastructure investment to another faction, establishing a formal economic relationship.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Economy,  function = Add,  subject = AccordAgreement,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,  # Neighbor relationship noted for narrative — no threshold variance (Automatic)
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = BilateralAgreement,
    persistence     = Immediate,  # resource delivery and AccordForm delivery resolve at Beat 4; form lifecycle governed by Art 06 §9.4
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Guild).influence_tier(district.any_adjacent_to(faction(target).presence)) >= Established,
    cost        = resource.faction(Guild).capacity * 1  # form price → Reservoir
              + resource.faction(Guild).native * 2,   # sweetener → delivered to target at success

    success = (
        faction(target).resource(native) += 2,  # immediate delivery
        arbiter.deliver(Guild, AccordForm(blank)),  # Guild drafts Infrastructure Bond terms per Art 06 §9.3
    ),

    # BilateralAgreement resolution at Debrief: PS consequences per Art 06 §9.4
    # on_accept: track Accord income — target pays Guild 1 Capacity at each Upkeep Step 6 while Accord active

    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "Guild does not give resources away. The Infrastructure Bond is an investment — the terms make that clear.",
    perspectives = {
        Guild:       "We extend this partnership because the infrastructure serves both of us. The terms reflect that.",
        Directorate: "Guild formalizes the relationship before the need becomes urgent. The Accord terms are what the investment was always going to require. This is how structural partners communicate.",  # aligned
        Syndicate:   "Guild packages the extraction as partnership. The initial delivery is cover. The recurring return is the structure. We recognize this.",  # opposed
    },
    design_note  = "Guild economic relationship PA. Cost: 1 Capacity (form price, per L200/L201) + 2 native delivered to target (sweetener — makes Accord terms credible). Accord on acceptance includes 1 Capacity/Upkeep income from target; net positive for Guild in 2+ Quarters. Restriction: Guild must have Established adjacent to target's operations. Distinct from STD.CA.9 Fund (Capital, covert, two-action route). Distinct from STD.PA.8 (bare form, no sweetener). Addresses 04-n11 (Guild↔Network neighbor cooperation).",
    arbiter_note = "Phase B: target faction named publicly. Beat 4: deliver 2 native resources to target immediately; deliver blank AccordForm from ARBITER tableau supply to Guild. No timing constraint on drafting or placement — form queued for next Debrief when placed in Accord Placement Area. At Debrief: target reviews, accepts or declines per Art 06 §9.4. PS consequences per Art 06 §9.4. On accept: track Accord income (target pays Guild 1 Capacity at each Upkeep Step 6 while Accord active).",
)
```

---


---


---

---

### GUI.PA.3 — HERITAGE REGISTRY *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.3 = Card(
    id      = "GUI.PA.3",  version = "v1.0",
    name    = "Heritage Registry",
    tagline = "Declare a district's structures historically protected.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Protect,  subject = StructureBlock,

    beat            = 4,
    resolution      = Automatic,
    persistence     = Permanent,
    
    target_district = district.any,
    target_faction  = None,

    cost = resource.faction(Guild).capacity * 2 + resource.faction(Guild).mandate * 1,

    success = "Places standing condition on target_district: If a structure block is removed for any reason (unless due to influence token reaching 0), add the structure block back to the district. Remove this standing effect after it triggers once.",
    
    design_note = "Defense scaling gap addressed. Cost reasoning: 2 Capacity + 1 Mandate (Mid-tier). Mandate provides the legal shield to protect the concrete."
)
```

---

### GUI.PA.4 — CIVIC UNVEILING *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.4 = Card(
    id      = "GUI.PA.4",  version = "v1.0",
    name    = "Civic Unveiling",
    tagline = "A highly publicized ribbon-cutting ceremony that compounds structural density into public adoration.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Standing,  function = Shift,  subject = StandingMarker,

    beat            = 4,
    resolution      = Automatic,
    
    target_district = district.any,

    cost = resource.faction(Guild).capacity * 1 + resource.faction(Guild).exposure * 1,

    success = "faction(Guild).standing += district(target_district).faction(Guild).structure * 1",
    
    design_note = "Standing / PS Compounding gap filled. Cost reasoning: 1 Capacity + 1 Exposure (Mid-tier). Broadcasting the massive ribbon-cutting to the city."
)
```

---

### GUI.PA.5 — ZONING EXEMPTION *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.5 = Card(
    id      = "GUI.PA.5",  version = "v1.0",
    name    = "Zoning Exemption",
    tagline = "Secure a blanket override of Ring expansion limitations.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Submission,  function = RemoveRestriction,  subject = District,

    beat            = 4,
    resolution      = Automatic,
    
    target_district = district.any,

    cost = resource.faction(Guild).capacity * 2 + resource.faction(Guild).findings * 1 + resource.faction(Guild).capital * 1,

    success = "For the next Quarter, Guild may place structures in the target district regardless of Ring limitations or connectivity rules.",
    
    design_note = "Ceiling-tier expansion enabler. Cost reasoning: 2 Capacity + 1 Findings + 1 Capital. Finding the bureaucratic loop-hole and buying the necessary judges to skip the physical expansion limits."
)
```

---

---

### GUI.PA.6 — ASSET TRANSFER *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.6 = Card(
    id      = "GUI.PA.6",  version = "v1.1",
    name    = "Asset Transfer",
    tagline = "Liquidate Guild property into another faction's hands for massive resource injection.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Territory,  function = Modify,  subject = StructureBlock,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Guild).capacity * 1,
    restriction = "district(target).faction(Guild).structure > 0 AND district(target).faction(target_faction).presence > 0",
    success = "Guild removes 1 of their Structure Blocks in target_district and replaces it with 1 Structure Block of the target_faction. Guild gains 3 of the target_faction's native resource from the supply.",
    design_note = "A powerful, legal asset flip. Leverages existing footprint to extract deep foreign resource pockets."
)
```

---

### GUI.PA.7 — EMINENT DOMAIN PETITION *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.7 = Card(
    id      = "GUI.PA.7",  version = "v1.1",
    name    = "Eminent Domain Petition",
    tagline = "Force massive influence into a district to pave the way for expansion.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Territory,  function = Add,  subject = PresenceToken,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Guild).capacity * 2 + resource.faction(Guild).mandate * 1,
    restriction = "district(target).faction(Guild).presence > 0",
    success = "Place 2 Guild Presence Tokens in target_district.",
    design_note = "Requires existing foothold. A blunt-force legal maneuver to crack an opponent's Established status."
)
```

---

### GUI.PA.8 — STRUCTURAL SUBSIDY *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.8 = Card(
    id      = "GUI.PA.8",  version = "v1.1",
    name    = "Structural Subsidy",
    tagline = "Turn a district's development into a PR engine.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Standing,  function = Shift,  subject = StandingMarker,
    beat    = 4,  resolution = Automatic,  persistence = Permanent,
    cost    = resource.faction(Guild).capacity * 2,
    success = "Places standing condition on target_district: 'Whenever an opponent places a Structure Block here, Guild gains +1 PS.'",
    design_note = "A standing effect. Guild weaponizes other factions' construction efforts to build their own prestige."
)
```

### GUI.MOD.1 — NIGHT SHIFT CREW *(stub)*

*S106. Guild React Modifier — stub. Originally conceived as Territory|Recover|PresenceToken CovertAction (GUI.CA.6), redesigned as React Modifier after two blocking findings: (1) structure block removal is simultaneous with chips hitting 0 — no React window can catch it; (2) "Recover" may not be a valid primitive per 00a §7.2 (see 00a-77). Taxonomy reclassified as Territory|Add|PresenceToken pending 00a-77 resolution.*

**Design Rationale:** Guild's React presence card — when a Guild chip is removed from a district, Guild may immediately respond by placing a chip back. "Established communities don't abandon positions — they return." The return is reflexive, not planned. Trigger is the chip removal itself (publicly observable resolved action). No structure dependency — structure may be simultaneously removed when chips hit 0, so the trigger window must not require it.

**Outstanding Issues:**
- **00a-77:** Taxonomy validity — if "Recover" is reclassified as Add+React context, this card's Layer|Function|Subject = Territory|Add|PresenceToken. Pending 00a Art 02 §7.2 review.
- **09-06:** Full ModReactCard spec (trigger, value_rating, ring_constraint, ring_origin) pending design pass.
- **Trigger scope:** Confirm whether trigger fires on any chip removal (STD.CA.4, DIR.CA.5, any chip-removing effect) or only on specific action types.
- **card_id:** GUI.MOD.1 (first Guild Modifier card).

**Status:** Stub — all passes pending.

```python
# GUI.MOD.1 — RETURN TO SITE (stub; full ModReactCard spec pending 09-06 design pass)
GUI.MOD.1 = Card(
    id      = "GUI.MOD.1",  card_id="GUI.MOD.1",  version="v0.1",
    name    = "Night Shift Crew",
    type    = ModReactCard,  faction = Guild,
    layer   = Territory,  function = Add,  subject = PresenceToken,
    # function = Add pending 00a-77 (Recover taxonomy validity)
    trigger = chip_removed.where(faction=Guild, district=district(trigger.target)),
    target_district = district(trigger.target),
    cost    = TBD,
    success = faction(acting).presence_chips(district(target)).add(1),
    successcrit = TBD,  fail = None,  failcrit = TBD,
    portrait = {Guild: PortraitEntry(submitter=+1)},
)
```

---

### GUI.MOD.2 — UNION REPRESENTATIVE *(stub)*

*S128. React on opponent structure placement. Guild labor built it — Guild gets paid. Generic opponent variant. Faction-targeted variant: GUI.MOD.3 (Directorate). Ring-constrained variant: GUI.MOD.4 (Ring 1 premium rate). Connects to §5a passive income / 04-n2.*

```python
GUI.MOD.2 = Card(
    id      = "GUI.MOD.2",  card_id="GUI.MOD.2",  version="v0.1",
    name    = "Union Representative",
    tagline = "Other factions build with Guild labor. Guild gets paid.",
    type    = ModReactCard,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    trigger         = structure_block.placed(faction=opponent),  # any non-Guild faction places structure
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,  # no presence requirement — Guild workforce is citywide
    cost            = None,

    success     = faction(Guild).resources.add(1, Capacity),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Guild: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Passive income React. Any opponent structure placement triggers 1 Capacity yield to Guild. Guild's doctrine: construction is Guild's domain regardless of who commissions it. Companion to 04-n2 (unimplemented passive income governing rule) — this delivers the same income as a ModReactCard rather than an Art 03 procedural rule. No presence restriction: Guild labor operates citywide.",
    arbiter_note = None,
)
```

---

### GUI.MOD.3 — INSTITUTIONAL CONTRACT *(stub)*

*S128. Faction-targeted variant of GUI.MOD.2. Trigger narrowed to Directorate structure placement. Directorate builds institutional-scale structures — Guild is the primary contractor for government facilities.*

```python
GUI.MOD.3 = Card(
    id      = "GUI.MOD.3",  card_id="GUI.MOD.3",  version="v0.1",
    name    = "Institutional Contract",
    tagline = "Directorate builds. Guild crews and invoices.",
    type    = ModReactCard,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    trigger         = structure_block.placed(faction=Directorate),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(Guild).resources.add(1, Capacity),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Guild: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Directorate-targeted variant of GUI.MOD.2 (Union Representative). Same trigger/effect, faction-narrowed to Directorate. Guild–Directorate tension: Directorate controls Guild's operating environment (PA.1 Regulatory Override raises construction costs); Guild charges Directorate for every structure it commissions. Narrower trigger window than generic variant; reliable in DIR-heavy games.",
    arbiter_note = None,
)
```

---

### GUI.MOD.4 — CORE PREMIUM *(stub)*

*S128. Ring-constrained variant of GUI.MOD.2. Ring 1 (Core) structure placement by any opponent triggers 2 Capacity yield. Core ring commands premium construction rates — the infrastructure is more complex, the labor is scarcer.*

```python
GUI.MOD.4 = Card(
    id      = "GUI.MOD.4",  card_id="GUI.MOD.4",  version="v0.1",
    name    = "Core Premium",
    tagline = "Core construction pays Guild at institutional rates.",
    type    = ModReactCard,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    trigger         = structure_block.placed(faction=opponent, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(Guild).resources.add(2, Capacity),  # double rate for Core ring
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Guild: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Ring 1–constrained variant of GUI.MOD.2. Core construction yields 2 Capacity (vs. 1 for generic). Scarcity and complexity of Core construction means Guild commands premium rates. Strongest Guild passive income trigger — incentivizes Guild to maintain Core presence to capture premium construction income from all factions.",
    arbiter_note = None,
)
```

---

### GUI.MOD.5 — COMPANY TOWN *(stub)*

*React on opponent presence placement near Guild structures. Passive modifier draw engine.*

```python
GUI.MOD.5 = Card(
    id      = "GUI.MOD.5",  card_id="GUI.MOD.5",  version="v0.1",
    name    = "Company Town",
    tagline = "Our people built the walls. We hear who whispers behind them.",
    type    = ModReactCard,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    trigger         = presence_chip.placed(faction=opponent, district=where(faction(Guild).structure > 0)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.draw_modifier(faction=Guild, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Passive intelligence engine. Guild's massive labor footprint acts as an informant network. When an opponent expands into a district where Guild has a structure, Guild draws 1 Faction Modifier card. Turns their win-condition (structures) into a territorial tax on opponent expansion.",
    arbiter_note = None,
)
```

---

### GUI.MOD.6 — EMERGENCY RECONSTRUCTION *(stub)*

*React on Guild structure removal. Fast-tracked structural replacement.*

```python
GUI.MOD.6 = Card(
    id      = "GUI.MOD.6",  card_id="GUI.MOD.6",  version="v0.1",
    name    = "Emergency Reconstruction",
    tagline = "You can knock down the building, but you can't erase the blueprint.",
    type    = ModReactCard,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    trigger         = structure_block.removed(faction=Guild),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = faction(Guild).district.adjacent_to(trigger.district).acting_choice,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Guild).presence_in(target_district),
    cost            = list([Resource(Capacity, 1), Resource(Capital, 1)]),

    success     = arbiter.place(structure_block, district=target_district, faction=Guild, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Scaling structural defense. Reacts to the physical removal of a Guild structure (whether by covert Demolish or public act). Guild spends heavy resources to instantly place a replacement structure in an adjacent district. Ensures their structure count remains constant even under heavy attack.",
    arbiter_note = None,
)
```

---

### GUI.MOD.7 — WORKER RETALIATION *(stub)*

*React on Guild structure removal. Territorial fallback swarm.*

```python
GUI.MOD.7 = Card(
    id      = "GUI.MOD.7",  card_id="GUI.MOD.7",  version="v0.1",
    name    = "Worker Retaliation",
    tagline = "The site is clear, but the workers are still here.",
    type    = ModReactCard,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    trigger         = structure_block.removed(faction=Guild),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = Resource(Capacity, 1),

    success     = arbiter.place(presence_chip, district=target_district, faction=Guild, count=2),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Scaling structural defense. If an opponent manages to remove a Guild structure, Guild burns Capacity to flood the district with 2 presence chips. The territory becomes completely infested with Guild influence, preventing the attacker from claiming the space they just cleared.",
    arbiter_note = None,
)
```

---

### GUI.MOD.8 — SITE CLEARANCE *(stub)*

*React on any structure removal. The demolition and cleanup contract.*

```python
GUI.MOD.8 = Card(
    id      = "GUI.MOD.8",  card_id="GUI.MOD.8",  version="v0.1",
    name    = "Site Clearance",
    tagline = "We built it, we get paid. You blew it up, we get paid to clean it up.",
    type    = ModReactCard,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    trigger         = structure_block.removed(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(Guild).resources.add(1, district(trigger.district).native_resource),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Passive demolition income. Whenever ANY structure is removed, Guild takes the cleanup contract and receives 1 of the district's native resource type from the Reservoir. Pairs with GUI.MOD.2 to ensure Guild profits on both ends of a structure's lifecycle.",
    arbiter_note = None,
)
```

---

## Ghost
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#ghost-covert-operations) · [Public Acts](#ghost-public-acts)

---

### Ghost — Covert Operations
[↑ Ghost](#ghost)

| Card | Name |
|------|------|
| [GHO.CA.1](#c16-pattern-match) | Pattern Match |
| [GHO.CA.2](#c17-intercept) | Intercept |
| [GHO.CA.3](#c18-dossier-breach) | Dossier Breach |
| [GHO.CA.4](#c19-deep-cover) | Deep Cover |
| [GHO.CA.5](#c20-misdirection) | Misdirection |
| [GHO.CA.7](#ghost-station) | Station |
| [GHO.CA.8](#ghost-full-take) | Full Take |
| [GHO.CA.9](#ghost-scif) | SCIF |
| [GHO.CA.10](#ghost-flip) | Flip |
| [—](#ghost-signals-analysis) | Signals Analysis |
| [—](#ghost-synthesize) | Synthesize |
| [GHO.CA.12](#ghost-source-substitution) | Source Substitution |
| [—](#ghost-backdate) | Backdate |
| [—](#ghost-field-verification) | Field Verification |

### GHO.CA.1 — PATTERN MATCH
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost-exclusive intelligence-into-action card — the only card with Predictive resolution in the set. Ghost submits a prediction at §9.1: target faction, target district, and the operation they believe that faction has dispatched. At Beat 2, ARBITER checks all three against the covert grid. A correct match causes ARBITER to move the matched operation from the target faction's Beat 3 lane into Ghost's lane. The target faction loses the operation entirely: their case returns empty, resources spent, Dispatch Token consumed.

This is not a copy. The operation executes once, for Ghost.

Ghost resolves the stolen operation at Beat 3 as `faction(acting)`. Same target district, same Target Profile as originally submitted — but Ghost is the actor and Ghost receives the benefit. Any op, any faction — if Ghost can identify and execute it, Ghost keeps it. Effects that reference `faction(acting)` now reference Ghost; Ghost receives whatever the op produces, including off-faction resources.

Executability check precedes the move: if Ghost cannot execute the stolen op (restriction failure, resource type mismatch), Pattern Match fizzles. The op stays in the target's lane. Ghost gains nothing; 2 Findings spent. The risk of a wrong prediction — or an unexecutable steal — is real.

Prediction bar is high: all three elements (faction + district + operation name) must match. Intelligence depth is the enabler — Intel Tokens, prior observations, pattern analysis. At that depth, the interception is earned.

Fills `Submission | Redirect | CovertOperation` — a function unique to Ghost in the card set. No standard equivalent (Art 04 §5 P17). The Redirect taxonomy needs Art 04b §5.1 validity matrix confirmation (PM05 flagged).

#### Card Story
A faction submits their operation. Ghost, watching, named all three things in advance. At Beat 2, ARBITER finds Ghost's prediction in the grid, finds the matching operation, and moves it. The faction's case comes back lighter than they expected. The operation resolves — but not for them.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence-into-action via operational interception — Ghost's prediction accuracy converts to execution, not just information. Fits Ghost doctrine: understanding precedes action, and in this case enables theft. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Ghost only; single perspective — interception as doctrine. Extended in v2.0 to include the "theft" framing. | Art 00 §7 |
| Doctrine alignment | ✓ | target_faction = faction.named; doctrine_mod = None — prediction accuracy is about intelligence depth, not doctrinal proximity. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — operation interception is Ghost-exclusive; no Standard equivalent. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ⚠ | Submission/Redirect/CovertOperation — Redirect communicates the mechanism (op moves from target lane to Ghost lane; no duplication). Needs Art 04b §5.1 validity matrix check (PM05 queued). | Art 04b §4, §5 |
| Balance | ✓ | 2 Findings for a triple-prediction. High prediction bar (faction + district + operation name) is the gate. Stolen op is free to Ghost — original faction bore the cost. Fizzle risk (wrong prediction OR can't execute) is the downside. | Art 02 §8 |
| Effect duration | ✓ | Immediate: stolen op resolves at Beat 3, no persistent state from Pattern Match itself. | — |
| Persistence | ✓ | Immediate — fully resolved at Beat 3; no lingering game-state marker from Pattern Match. | Art 04 §6 |
| Trigger validity | N/A | trigger = None — Predictive resolution: ARBITER checks prediction against grid at Beat 2. | — |
| Portrait validity | ⚠ | Ghost submitter=+1, modifier=+1, mod_where=game.outcome == Success. Portrait AND/OR semantics still open (see Outstanding Issues). Additional open: does Portrait also fire when the stolen op resolves at Beat 3 under Ghost's lane? | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — Ghost names a specific district in the prediction. No adjacency restriction (analytical op). | Art 01 §6 |
| Supported by components | ✓ | Findings cost; CovertOperation as redirect target; stolen op's components governed by that op's spec. Ghost may receive off-faction resources (Mandate, Capacity, etc.) — tradeable at Debrief. | Art 02 §8 |
| Supported by game procedure | ⚠ | Beat 2 resolution; ARBITER checks prediction against covert grid; if match + executable: lane redirect. Art 03 gap: Pattern Match redirect procedure not yet written in Art 03 §9.4 — simpler than the prior copy-injection model but still unwritten. | Art 03 §9 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S119 | Art 04 §5 P26 |

#### Outstanding Issues

- **Portrait AND/OR semantics:** `modifier=+1, mod_where=game.outcome == Success` — confirm AND semantics: `submitter` always fires on play; `modifier` fires additionally on Success. Confirm OR is not intended.
- **Portrait from stolen op:** The moved op has its own portrait block (keyed to original faction). When it resolves in Ghost's lane, does ARBITER fire those portrait entries for the original faction (who didn't submit it) or not at all? Rule needed.
- **Art 03 procedure gap:** Pattern Match redirect (Beat 2 lane move) not yet written in Art 03. Simpler than copy-injection — just a grid lane transfer — but still requires a new sub-step in §9.4.2. Blocked on Art 03 edit.
- **Submission|Redirect L×F validity:** Art 04b §5.1 matrix check required. PM05 queued.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*S119 v2.0 redesign — mechanism changed from Copy (Beat 3) to Redirect/steal (Beat 2 intercept → Beat 3 execution). Original faction loses op, cost, and Dispatch Token. Ghost is actor on stolen op; effects reference Ghost as faction(acting). Prediction now requires all three: faction + district + operation name.*

```python
GHO.CA.1 = Card(
    id      = "GHO.CA.1",  card_id = "GHO.CA.1",  version = "v2.0",
    name    = "Pattern Match",
    tagline = "Identify a faction's operation and location — then take it.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Submission,  function = Redirect,  subject = CovertOperation,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Predictive",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.named,
    target_faction  = faction.named,
    target_object   = CovertOperation,
    declared_params = operation.named,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).findings * 2,
    boost       = None,

    success     = game.redirect(
        op        = faction(target).beat3_row.op(district=target_district, name=declared_params.operation),
        to        = faction(acting).beat3_lane,
        condition = game.can_execute(faction(acting), op),
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1, modifier=+1, mod_where=game.outcome == Success)},
    ps_framing = None,

    narrative    = "Ghost does not guess. Ghost identifies what is already in motion — and takes it.",
    perspectives = {
        Ghost: "We are not predicting. We are recognising a pattern we have already seen. And then we are keeping it.",
    },
    design_note  = "Steal not copy: matched op moves from target faction's Beat 3 lane to Ghost's. Original faction loses the op, the cost, and the Dispatch Token — no compensation. Ghost resolves the stolen op as faction(acting) at Beat 3; same target as originally submitted; Ghost receives all effects including off-faction resources. Executability check precedes the move: if Ghost cannot execute (restriction failure, wrong resource type), Pattern Match fizzles and the op stays in target's lane. Taxonomy: Submission|Redirect — Art 04b §5.1 L×F validity check pending (PM05 queued).",
    arbiter_note = "At Beat 2: (1) Check Ghost's declared_params (target faction + target district + operation name) against the Beat 3 grid. (2) If all three match: check whether Ghost can execute the matched op — if restriction or resource type blocks execution, Pattern Match fizzles (2 Findings spent; op stays in target lane; no notification). (3) If match AND executable: move the op and its Target Profile from target faction's Beat 3 lane to Ghost's Beat 3 lane. Target faction's committed cost resources and Dispatch Token are consumed — not returned. (4) At Beat 3: the moved op resolves in Ghost's lane with Ghost as faction(acting). The original Target Profile governs targeting (same district, same target faction as originally submitted). All effects referencing faction(acting) now reference Ghost.",
)
```

---

### GHO.CA.2 — INTERCEPT
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost-exclusive active-surveillance card — distinguishes from GHO.CA.3 Dossier Breach by targeting submitted operations, not hand contents. Intel Token cost consumed at submission regardless of outcome: you spend what you know to learn what they're doing. Cost structure (Intel Token + 2 Findings) reflects active operational depth — harder to execute than Gather, rewarded with real-time intelligence rather than historical data. Failure notifies the target; crit fail triggers a PS loss.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Active surveillance of submitted operations — direct expression of Ghost's real-time intelligence doctrine. Distinct from STD.CA.5 Gather (historical intel) and GHO.CA.3 Dossier Breach (hand contents). | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | One perspective (Ghost only) — FactionSpecific; acceptable. "We do not wait for the after-action report." Ghost's active-vs-passive intelligence distinction is clear. | Art 00 §7 |
| Doctrine alignment | ✓ | `target_faction = faction(named_opponent)`, `doctrine_mod = None` — explicit design choice: surveillance effectiveness is about intelligence quality, not doctrinal proximity. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: active surveillance is covert. FactionSpecific (Ghost): real-time operational intel is Ghost's exclusive capability. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Information` — revealing the content of a submitted operation is Information layer. `function = Reveal`, `subject = CovertOperation` — correctly scoped. | Art 04b §4, §5 |
| Balance | ✓ | Intel Token consumed at submission regardless of outcome — meaningful downside for failed surveillance. Double-resource cost (IntelToken + 2 Findings). Crit success stacks additional IntelToken on top of IntelDeliverySlip. | Art 02 §8; Art 02 §12 |
| Effect duration | ✓ | Instantaneous: IntelDeliverySlip delivered once at Beat 2 resolution; reads target faction's Beat 3 grid column. IntelToken on crit. No persistent state beyond the delivered token. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Ghost `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). `failcrit = standing -= 2` is a PS shift (not Portrait — DIR.PA.2 clear). | Art 04 §6.2; Art 02 §11 |
| Supported by zones | N/A | `target_district = None` — Intercept operates on submitted ops in the Resolution Grid, not a specific district. | — |
| Supported by components | ✓ | IntelToken cost; Findings cost; IntelDeliverySlip (success); IntelToken (crit success); NotificationSlip (fail); PS −2 (failcrit). | Art 02 §8; Art 02 §11, §8 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); resolves Beat 2; reads Beat 3 grid column; d100 threshold 50; ARBITER delivers IS-xx via case (Art 07). Art 03 §9.4 Beat 2 Step 7a covers IS-xx delivery; Step 7b covers NotificationSlip; Step 7b.i covers failcrit. | Art 03 §9, §11; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Arbiter note:** Crit success: deliver IntelToken (faction=target) to acting faction's case. Success: write target faction's first submitted op type and district on Intel Delivery Slip; deliver to acting faction's case. Fail: deliver Notification Slip to target faction's case. Crit fail: apply PS −2.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | ⚠ pending re-sign-off (v1.1 — beat timing correction) |

```python
GHO.CA.2 = Card(
    id      = "GHO.CA.2",  version="v1.1",
    name    = "Intercept",
    tagline = "Surveil a faction's covert operations in real time.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Reveal,  subject = CovertOperation,
    beat=2, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10}, doctrine_mod=None,
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction(named_opponent), target_object=CovertOperation,
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = IntelToken(faction=faction(target)) * 1 + resource.faction(acting).findings * 2,
    success     = game.dispatch(faction(acting), IntelDeliverySlip(faction=faction(target), op_type=faction(target).op(beat=3).type, district=faction(target).op(beat=3).district)),
    successcrit = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)),
    fail        = game.dispatch(faction(target), NotificationSlip),
    failcrit    = faction(acting).standing -= 2,
    portrait    = {Ghost: PortraitEntry(submitter=+1)},
    narrative   = "To know what they are doing while they are doing it — that is the only intelligence that matters.",
    perspectives = {Ghost: "We do not wait for the after-action report. We read the operation as it happens."},
)
```

---

### GHO.CA.3 — DOSSIER BREACH
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
SIGINT tap on a named faction's dispatch channel. Ghost submits at Beat 2 — establishing the tap before Beat 3 fires. At Beat 2 resolution, ARBITER reads the target faction's Beat 3 grid column (all submitted ops for that faction: name and declared target only; modifier cards excluded — splayed edge not readable) and delivers an IntelDeliverySlip to Ghost privately. No interaction with the target player. Covert attribution preserved throughout.

GHO.CA.3 reads a faction column from the Beat 3 grid; DIR.CA.3 reads a district row. Both use IntelDeliverySlip — the content varies by card procedure.

Redesigned S68: original target was the unplayed hand (CardHandContents) — requires physical access to the target player's cards during Beat 3, which breaks covert attribution at the paper table. The SIGINT model removes that constraint: Ghost's tap is in ARBITER's domain (dispatch cases), not the target player's private domain. Information target shifts from planning pool to committed operations — what the faction decided to do, not what they could do. Beat 2 commitment is the risk: 2 Findings spent before Ghost knows what the target will submit.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | SIGINT tap on dispatch channel — faction column read from Beat 3 grid; distinct from GHO.CA.2 (disrupts one submitted op), DIR.CA.3 (district row read), and STD.CA.5 (generates intel tokens); Ghost reads committed operations, not planning pool | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — covert channel interception is Ghost-exclusive doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; Beat 2 commitment is the risk (spends before knowing target's submission); Automatic resolution fits signals intelligence work | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — covert channel access is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/IntelDeliverySlip — subject updated S68 (DR-xx collapsed into IS-xx) | Art 04b §4, §5 |
| Balance | ✓ | 2 Findings, Automatic, Beat 2 — information advantage without dice risk; Beat 2 blind commitment is the cost; empty case = resources spent | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: IntelDeliverySlip delivered at Beat 2 resolution; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at Beat 2; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — intelligence operation confirms Ghost operational activity | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — operates on Beat 3 grid faction column; no district context required | Art 01 §6–§7 |
| Supported by components | ✓ | IntelDeliverySlip (IS-xx) — Art 02 component entry pending (04-n45); 00b definition update pending (04-n46) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; ARBITER reads existing Beat 3 grid faction column — no new tracking required; Art 03 Beat 2 procedure addition pending (04-n44) | Art 03 §9, §9.4; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Art 03 Beat 2 procedure:** Beat 2 section does not yet cover IntelDeliverySlip delivery for intelligence cards. Procedure addition required before Issues Resolved (04-n44).
- **Art 02 component entry:** IntelDeliverySlip has no design entry in Art 02. Addition required before Issues Resolved (04-n45).
- **00b IS-xx definition:** IS-xx definition needs updating to cover Beat 2 delivery and faction column reads (04-n46).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*S68 redesign — SIGINT tap model*

\`\`\`python
GHO.CA.3 = Card(
    id      = "GHO.CA.3", version="v1.2",
    name    = "Dossier Breach",
    tagline = "Tap a rival's dispatch channel — read their submitted operations at Beat 2 resolution.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Ghost,
    layer   = Information, function = Reveal, subject = IntelDeliverySlip,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction(named_opponent), target_object=DispatchCase(faction=faction(target)),
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).findings * 2,
    success     = game.deliver(IntelDeliverySlip(faction=faction(target), content=resolution_grid(month=current, beat=3, faction=faction(target)).operations(fields=[name, target])), to=faction(acting), private=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Ghost: PortraitEntry(submitter=+1)},
    narrative   = "Understanding the operation before it begins. That is the only tactical advantage worth having.",
    perspectives = {Ghost: "We did not take their cards. We simply read their intentions. They will act on plans we already know."},
    design_note  = "Redesigned S68: original target was unplayed hand (CardHandContents) — requires physical access to target player's cards, not executable covertly at paper table. Redesigned to SIGINT tap model: Ghost taps faction X's dispatch channel at Beat 2. ARBITER reads faction X's Beat 3 grid column at Beat 2 resolution (name + declared target only; modifier cards excluded). IntelDeliverySlip delivered to Ghost at Beat 2 resolution. Beat 2 commitment is the risk. Empty case = empty slip — resources spent. DR-xx (DispatchReport) collapsed into IS-xx S68 — column read is IntelDeliverySlip with list content.",
    arbiter_note = "During Beat 2 resolution of this card: read faction X's Beat 3 resolution grid column. Write an IntelDeliverySlip listing each operation by name and declared target (district, faction, or object). Modifier cards not included. Deliver privately to Ghost at Beat 2 resolution. Do not notify faction X. If faction X has no Beat 3 operations, deliver an empty slip — Ghost's resources are spent. Procedure pending Art 03 Beat 2 addition (04-n44).",
)
\`\`\`

---

### GHO.CA.4 — DEEP COVER
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's intelligence interdiction card — operational disruption rather than evidence destruction. At Art 03 §9.1 Covert Dispatch, Ghost names a target faction and pays 1 unit of that faction's native resource (the operational prerequisite — Ghost must already be embedded in the target's systems). At Beat 3, ARBITER checks the first PA in the target faction's Faction Resolution Grid queue: if an IntelToken is submitted on it, Ghost removes it before Beat 4 processes the PA. Two disruption outcomes depending on how the token was used: if it was the PA's cost payment, the PA is voided; if it was a modifier, the PA loses that modifier and resolves blind. Threshold 25 (Challenging) reflects the difficulty of locating and intercepting live intelligence before a public act proceeds. Redesigned S113: prior design (S68) targeted rival-held private IntelTokens — violated 00a Art 02 §10.1 (ARBITER reaching into a faction's private domain). Faction Resolution Grid is the only valid targeting location for another faction's IntelToken.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence interdiction — Ghost removes a rival's submitted IntelToken from the Faction Resolution Grid before Beat 4; voids PA or strips modifier depending on how token was used; distinct from GHO.CA.3 (reads plans) and STD.CA.5 (gathers intel) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective — interdiction as doctrine, not tactic | Art 00 §7 |
| Doctrine alignment | ✓ | Cost = 1 native resource of target faction — Ghost must be embedded in the target's operational systems; threshold 25 reflects difficulty of live intelligence interdiction; targets the intelligence that was meant to precede the rival's action | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence interdiction is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information / Remove / IntelToken — IntelToken submitted on PA in Faction Resolution Grid is the only valid cross-faction IntelToken target (00a Art 02 §10.1); confirmed S113 | Art 04b §4, §5 |
| Balance | ✓ | 1 native resource (target faction), threshold 25 — cost requires prior economic embedding; Challenging roll is the difficulty gate; disruption ceiling (PA void) is high-stakes but gated behind both cost and roll | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: token removed at Beat 3; PA outcome resolved at Beat 4 | — |
| Persistence | ✓ | Immediate — card fully resolved at Beat 3; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 3 timing is default for covert ops | — |
| Portrait validity | ✓ | No portrait entry — Ghost interdicting live intelligence is tradecraft, not doctrine; absence intentional (confirmed S113) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — operates on Faction Resolution Grid, not a district | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken as target_object — component registered; Faction Resolution Grid is ARBITER-maintained procedure | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Art 03 §9.1 names target at Covert Dispatch; Beat 3 ARBITER checks first PA in target's Faction Resolution Grid queue; Beat 4 PA resolves without token (or is voided) | Art 03 §9.1, §9.4.2, §9.4.3; Art 07 |
| Data schema validation | ✓ | Validated S113: card_id, doctrine_mod, boost, ps_framing added; resolution=d100, resolution_type=Probabilistic, fail=None corrected | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*S113 redesign — Issues Resolved pending sign-off review*

```python
GHO.CA.4 = Card(
    card_id      = "GHO.CA.4",
    id="GHO.CA.4",  version="v1.2",
    name    = "Deep Cover",
    tagline = "Intercept and destroy the intelligence behind a rival's public act.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Remove,  subject = IntelToken,
    beat=3, resolution=d100, threshold=25, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence           = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None,
    target_faction=faction(named_opponent),  # declared at Art 03 §9.1 Covert Dispatch
    target_object=IntelToken(submitted_on=faction(target).resolution_grid.pa_queue[0]),
    target_taxonomy=None,
    affinity=None,
    restriction=None,  # target condition evaluated at Beat 3 — see arbiter_note
    cost=resource.faction(target).native * 1,
    boost=None,
    success  = game.remove(target_object),
    # If token was PA cost payment: PA is voided (auto-fail at Beat 4, Dispatch Token returned)
    # If token was PA modifier: PA loses modifier, resolves at Beat 4 without it
    successcrit=None,  fail=None,  failcrit=None,
    portrait    = {},
    ps_framing  = None,
    narrative   = "The act has no foundation once the intelligence beneath it is removed.",
    perspectives = {Ghost: "They submitted their evidence expecting it to do what evidence does. We made sure it did not arrive."},
    design_note  = "Cost is 1 native resource of the target faction — Ghost must already hold it, meaning prior economic embedding in the target's operations. This is the operational prerequisite, not a doctrinal gate (doctrine_mod=None). The Faction Resolution Grid is the only location where another faction's IntelToken is a valid card target (00a Art 02 §10.1); privately held tokens are untouchable. Two disruption tiers: token as cost voids the PA; token as modifier strips it. Both are significant; the ceiling (PA void) is the rare case where the target committed their token as payment.",
    arbiter_note = "At Art 03 §9.1: Ghost names target faction. At Beat 3: (1) confirm Ghost holds 1 unit of target faction's native resource — if not, case is invalid, return to Ghost, no effect. (2) Check first PA in target faction's Faction Resolution Grid queue for a submitted IntelToken. If none present: announce 'no valid target,' operation has no effect, cost spent, no roll. (3) If IntelToken present: collect cost, roll d100 vs. 25 (+/− PS modifier). On success: remove IntelToken (recycle or dispose per component physical design). If token was cost payment, mark PA as voided — at Beat 4 it auto-fails; Dispatch Token returned to target faction. If token was a modifier, PA continues at Beat 4 without it. On fail: no effect.",
)
```

---

### GHO.CA.5 — MISDIRECTION
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Evidence corruption — Ghost alters the faction attribution on an Intel Token a target faction has submitted on an active Public Act. The token remains in place; its `faction_name` field now identifies a different source. Any resolution depending on that attribution — Flip eligibility, Debrief gate access, attribution-based inference work — proceeds from a corrupted record.

Unlike GHO.CA.12 Source Substitution (which re-keys Ghost's own held tokens as an internal analytical step), Misdirection is offensive: Ghost corrupts the record while it is in active play. The target faction submitted this token believing they know what it says. Ghost has changed what it says.

1 Findings cost, Automatic — the corruption is technically simple once Ghost is in position; the difficulty is timing the operation against the target's PA submission. Fills Information|Corrupt|IntelToken at the offensive targeting scope that Source Substitution does not cover. L222 compliant — targets publicly placed tokens in the Faction Resolution Grid only (Beat 0–4 window). `declared_params` carries the replacement faction name declared at §9.1.

#### Card Story
A faction submits intelligence alongside their public declaration — an Intel Token they believe says exactly what they think it says. By the time their declaration resolves, the attribution on that token has been quietly changed. The intelligence is genuine. The source is not.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Offensive evidence corruption — Ghost alters attribution on a token publicly submitted by a target faction; fills Information|Corrupt|IntelToken at offensive scope (distinct from Source Substitution's self-directed re-keying) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — record alteration as operational doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; 1 Finding cost reflects precision operation; Automatic resolution reflects Ghost's technical competence in field correction | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence record manipulation is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/IntelToken — alters faction_name field on publicly placed token; L222 compliant (FRG submission, Beat 0–4 window) | Art 04b §4, §5 |
| Balance | ✓ | 1 Finding — low cost reflects precision play; power is timing-dependent (target must have PA with Intel Token) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: token field altered at Beat 3; no card-level lingering effect | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — evidence corruption aligns with Ghost intelligence manipulation doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — token is in Faction Resolution Grid, not district-anchored | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (publicly placed on PA in FRG); Findings cost; no new components; declared_params carries replacement faction name | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 resolution; ARBITER checks FRG for qualifying token; alters faction_name; if no qualifying token: fizzle | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S119 | Art 04 §5 P26 |

#### Outstanding Issues

None. (Taxonomy resolved S119 — Corrupt function confirmed; content=false retired; self-token restriction removed.)

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*S119 redesign — taxonomy changed from Information|Add to Information|Corrupt; targeting model changed from fabrication/plant to FRG attribution corruption. L222 compliant.*

```python
GHO.CA.5 = Card(
    id      = "GHO.CA.5",  card_id="GHO.CA.5",  version="v2.0",
    name    = "Misdirection",
    tagline = "Ghost has been thinking about what they think they know.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Corrupt,  subject = IntelToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction.named, target_object=IntelToken,
    target_taxonomy=None,
    declared_params = FactionName,
    affinity=None,
    restriction = faction(target).FRG.active_PA.intel_token.count >= 1,
    cost        = resource.faction(acting).findings * 1,
    boost       = None,
    success     = game.corrupt(field=faction_name, target=faction(target).FRG.active_PA.intel_token, new_value=declared_params.faction),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Ghost: PortraitEntry(submitter=+1)},
    ps_framing  = None,
    narrative   = "Ghost has been considering what the record says. It is never quite right.",
    perspectives = {Ghost: "The attribution is wrong. Systematically, deliberately wrong. By the time anyone checks, it will have been wrong for a while."},
    design_note  = "Fills Information|Corrupt|IntelToken at the offensive targeting scope: alters faction attribution on a token publicly placed on an active PA. Distinct from GHO.CA.12 Source Substitution (which re-keys Ghost's own held tokens). L222 compliant — targets publicly placed tokens in FRG only (Beat 0–4 window). declared_params carries the replacement faction name declared at §9.1.",
    arbiter_note = "At Beat 3: check whether target faction has any Intel Token submitted on an active PA in the Faction Resolution Grid. If yes: alter the faction_name field on that token to the faction named in declared_params. Token remains face-down on the PA; target faction is not notified. If no qualifying token: card fizzles, 1 Findings spent, no effect.",
)
```

---

### Ghost — STATION
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's dedicated faction-specific gather platform. Distinct from STD.CA.5 Gather (standard, adjacency-exempt, 1 token yield) by higher yield (2 tokens on success) at higher cost (2 Findings). STD.CA.5 is Ghost's remote general-purpose sweep; Station is a deployed collection platform sustaining coverage against a named faction over a Quarter. Two deck copies make Station Ghost's primary Intel generation card. Threshold 55 — above STD.CA.5 base (50), reflecting Station's reliability as a sustained platform. Adjacency restriction applies per 04-n6 direction: a deployed node requires physical proximity, unlike Ghost's analytical ops (GHO.CA.1–5).

#### Card Story
Ghost installs a passive collection node in the target faction's operational district. A sweep goes looking; Station waits. By Quarter's end, the target has brought everything past it at least once.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Dedicated gather platform — Ghost's high-yield intelligence collection card; distinct from STD.CA.5 (standard, 1 token) by sustained multi-token output | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — Station as deployed platform, not remote sweep | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; 2 Findings cost for 2-token yield reflects sustained collection investment; threshold 55 — above STD.CA.5 base (50), Station is a reliable sustained platform | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — Ghost's primary Intel generation card beyond standard STD.CA.5 | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Add/IntelToken — same taxonomy as STD.CA.5; faction-specific variant with higher yield | Art 04b §4, §5 |
| Balance | ✓ | Threshold 55, cost 2 Findings, yield 2 tokens — calibrated above STD.CA.5 base; deferred full balance validation to playtest | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: Intel tokens dispatched at Beat 3; durable resource, no card-level duration | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — collection operations align with Ghost intelligence doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | Adjacency restriction applied per 04-n6 direction — deployed collection node requires Ghost presence in target district or adjacent; no exemption (unlike analytical ops) | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Art 02 §12); Findings cost; no new components | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 d100 resolution; tokens dispatched to Ghost case on success; failcrit NotificationSlip per standard | Art 03 §9, §11 |
| Data schema validation | ✓ | 04-n70 ✅ S95 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S112 | Art 04 §5 P26 |

#### Outstanding Issues

None.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Issues Resolved S112*

```python
GHO.CA.7 = Card(
    card_id      = "GHO.CA.7",  version = "v1.1",
    name    = "Station",
    tagline = "Deploy a sustained intelligence collection platform against a named faction.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Add,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 55,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy = None,
    affinity        = None,
    restriction     = district(self|adjacent).faction(acting).presence > 0,
    cost            = resource.faction(acting).findings * 2,

    success     = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)) * 2,
    successcrit = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)),  # +1 = 3 total
    fail        = None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Every asset leaves a signal. Ghost listens until the signal becomes a pattern.",
    perspectives = {Ghost: "A station does not move. It waits until the target walks past it again."},
    design_note  = "Ghost's dedicated gather platform. Higher yield than STD.CA.5 (2 tokens vs 1 on success) at double Findings cost. Threshold 55 calibrated above STD.CA.5 base (50) — Station is a reliable sustained platform. Adjacency restriction per 04-n6: deployed node requires Ghost presence in target district or adjacent. Cards stack: STD.CA.5 and Station may both target same faction in same Quarter.",
)
```

---

### Ghost — FULL TAKE
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Burst gather for pre-loading multi-Quarter intelligence sequences. Single copy representing a total-collection operation: Ghost declares n Findings at submission, receives 2n Intel tokens on success (3n on crit). The slot commitment plus n Findings is the bet — fail returns nothing. Variable cost makes the card self-scaling: a small Full Take (n=1) is conservative; a large Full Take (n=3+) pre-loads an entire SCIF/Flip sequence. Reserved for mid-to-late game plays when Ghost has Findings reserves to invest. Singleton enforces scarcity. Threshold 40 is intentional: variable cost and fail=nothing are the risk floor; low threshold is the compensating upside. Adjacency restriction applies per 04-n6 direction — field collection op requires Ghost presence in target district or adjacent.

#### Card Story
Ghost counts the Findings and commits: all of it against one target, declared before the case is sealed. The return is proportional. The loss, if it comes, is total — investment gone, target notified.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Burst intelligence collection — pre-loads multi-Quarter sequences (SCIF, Flip, Signals Analysis); singleton scarcity enforces mid-to-late game use | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — maximum-yield operation as Ghost doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; variable cost scales with investment; singleton forces strategic commitment; adjacency restriction applied per 04-n6 | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — burst intelligence platform; no Standard equivalent | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Add/IntelToken — higher-yield variant of Station/STD.CA.5 pattern | Art 04b §4, §5 |
| Balance | ✓ | Variable cost n × 2 yield (3n crit) — singleton scarcity limits use; Intel holding guideline (4, not HARD) tolerates high-n plays; fail=nothing is the correct floor; threshold 40 confirmed | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: Intel tokens dispatched at Beat 3; durable resource, no card-level duration | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — maximum-yield collection aligns with Ghost intelligence doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | Adjacency restriction applied per 04-n6 — field collection op requires Ghost presence in target district or adjacent | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Art 02 §12); Findings cost; n validated at Beat 0 via arbiter_note (Art 04 §5 P20) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 0: arbiter_note specifies ARBITER records declared n and validates Findings present; Beat 3 resolution per Art 03 §9, §11 | Art 03 §9, §11 |
| Data schema validation | ✓ | 04-n70 ✅ S95 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S112 | Art 04 §5 P26 |

#### Outstanding Issues

None.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Issues Resolved S112*

```python
GHO.CA.8 = Card(
    card_id      = "GHO.CA.8",  version = "v1.1",
    name    = "Full Take",
    tagline = "Saturate collection against a single target — maximum yield from a single operation.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Add,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 40,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy = None,
    affinity        = None,
    restriction     = district(self|adjacent).faction(acting).presence > 0,
    cost            = resource.faction(acting).findings * n,  # n declared at submission; n >= 1; all n Findings physically present (Art 04 §5 P20)

    success     = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)) * (n * 2),
    successcrit = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)) * n,   # +n = 3n total
    fail        = None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Some intelligence is gathered patiently. Some is taken all at once.",
    perspectives = {Ghost: "The take was complete. Everything they transmitted this Quarter. We have it."},
    design_note  = "Singleton. Variable cost: Ghost declares n at submission; cost = n Findings; success = 2n Intel tokens; crit success = 3n. Fail = nothing. Threshold 40 confirmed — variable cost and fail=nothing are sufficient risk; low threshold is the compensating upside. Adjacency restriction per 04-n6. Intel holding guideline is 4 (not HARD); high-n plays may exceed guideline.",
    arbiter_note = "At Beat 0: record declared n; validate n Findings present in case. At Beat 3: success = dispatch 2n IntelToken(faction=target) to Ghost's case; crit success = dispatch 3n; fail = nothing; crit fail = NotificationSlip to target.",
)
```

---

### GHO.CA.15 — ROUTING OVERRIDE *(stub)*
[↑ Covert Operations](#ghost-covert-operations)

```python
GHO.CA.15 = Card(
    id      = "GHO.CA.15",  version = "v1.0",
    name    = "Routing Override",
    tagline = "Blindly intercept and redirect an opponent's covert operation.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Corrupt,  subject = TargetProfile,
    beat    = 2,  resolution = Automatic,
    cost    = resource.faction(Ghost).findings * 1 + intel_token * 1,
    success = "Ghost corrupts the first CA in target faction's Beat 3 resolution queue if it matches Ghost's specified parameters.",
    arbiter_note = "At Covert Dispatch, Ghost writes a target field (e.g., 'target_district') and expected value (e.g., 'Core'), plus a replacement value (e.g., 'Baryo'), in their Target Profile freeform space. At Beat 2: ARBITER checks target faction's first CA in the ARG. If that CA's Target Profile contains the exact field and value Ghost named, ARBITER silently crosses it out and writes Ghost's new value. If it does not match, Ghost's operation fizzles. The target faction executes their CA at Beat 3 against the new corrupted target.",
    design_note = "Beat 2 positional wager against a Beat 3 CA. Ghost must correctly predict a parameter of the opponent's first queued operation. The corruption is entirely silent until the operation resolves at Beat 3."
)
```


---

### Ghost — SCIF
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Converts existing faction-keyed Intel into future modifier capability. Spends one Intel token; ARBITER records the target faction's current structure block count in a SCIF Record card placed in Ghost's Dispatch Case. At Debrief, Ghost draws modifier cards equal to that count. Ghost is always building next Quarter's hand rather than spending this one. Yield scales with target development: SCIF against a lightly-built faction early game is modest; against a heavily-built Directorate or Guild late game it fills Ghost's modifier hand. The deferred payoff creates a planning horizon that no other faction can directly interrupt.

#### Card Story
Ghost cashes one piece of intelligence for something more durable. ARBITER records how deeply the target has built — and next Quarter, that depth becomes Ghost's tactical hand.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Converts Intel into future modifier capability — Ghost builds next Quarter's tactical hand rather than spending this one; deferred payoff no other faction can directly interrupt | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — intelligence as infrastructure for future action | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; IntelToken cost gates use on prior collection; yield scales with target development — balance concern flagged (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — deferred modifier economy is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Add/DebriefActionCard — SCIFRecord is a subtype; DA-01; registered in 00b §4 (agy S88, DB-34 ✅) | Art 04b §4, §5 |
| Balance | ✓ | Yield scales with target's structure count per ring; balance assessment deferred until Art 03 procedure locked | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: SCIFRecord instantiated at Beat 3; Debrief draw is Art 03 procedure, not a card-level lingering effect — compliant with Art 04 §5 P19 | — |
| Persistence | ✓ | Immediate — card fully resolved at Beat 3; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — Automatic resolution; restriction enforces Intel token presence | — |
| Portrait validity | ✓ | Ghost +1 submitter — intelligence-to-modifier conversion aligns with Ghost doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted operation; no district required | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; DebriefActionCard (type, DB:100) / SCIFRecord (DA-01) — registered in 00b §4 and Art 02 §13 | Art 02 §6–§8 |
| Supported by game procedure | ✓ | SCIFRecord instantiated at Beat 3 (Art 03 §9.4); Debrief draw procedure in Art 03 §11; DA-01 fields and procedure in Art 04 §12a | Art 03 §9, §11; Art 04 §12a |
| Data schema validation | ✓ | 04-n70 ✅ S95 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S112 | Art 04 §5 P26 |

#### Outstanding Issues

- **Balance — yield scaling:** SCIF yield grows as Guild and Directorate build. Playtest flag — non-blocking.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ S94 | |

```python
GHO.CA.9 = Card(
    card_id      = "GHO.CA.9",  version = "v1.1",
    name    = "SCIF",
    tagline = "Turn intelligence into operational assets.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Add,  subject = DebriefActionCard,  # subtype = SCIFRecord

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(acting).intel_tokens(faction=faction(target)) >= 1,
    cost        = IntelToken(faction=faction(target)) * 1,

    success     = DebriefActionCard(subtype=SCIFRecord, target=faction(target)),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "The structure count is the number of ways they have committed themselves. Ghost counts carefully.",
    perspectives = {Ghost: "We do not need to be inside their operation. We need to know how large it is."},
    design_note  = "Converts held intelligence into future modifier capability — Ghost builds next Quarter's hand from this Quarter's intelligence. Pairs with Station, Full Take, and Synthesize: the SCIF pipeline is the destination for accumulated faction-keyed Intel. Yield scales with target development, creating an intelligence premium on heavily-built opponents.",
    arbiter_note = "SCIFRecord procedure: Beat 3 instantiation (Art 03 §9.4); Debrief draw in Art 03 §11; DA-01 fields and procedure in Art 04 §12a.",
)
```

---

### Ghost — FLIP
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Economic arm of Ghost's intelligence pipeline. One faction-keyed Intel token consumed; ARBITER places 2 of the target faction's native resource in Ghost's Dispatch Case at Beat 3. Resources return at month-end with normal case contents — no deferred procedure required. Flip is the unlock for Ghost's higher-tier cards, which carry a secondary cost of Flip-acquired faction resources (the "target faction's assets turned against them" design direction, per GHO.CA.2 model). Layer is Economy per L175: primary effect is resource acquisition despite the Intel gating. Copy model confirmed: target's resource pool is not reduced. Quantity 2 confirmed as working value; final calibration deferred to playtest. Adjacency restriction applies per 04-n6 — field collection op requires Ghost presence in target district or adjacent.

#### Card Story
One Intel token, two of their resources. The target's reserves are untouched — Ghost didn't take from them. Ghost learned where the tap was.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Economic arm of Ghost's intelligence pipeline — converts faction-keyed Intel into target faction's native resource; unlock for higher-tier Ghost cards | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — resource redirection as intelligence exploitation | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; IntelToken cost enforces intelligence pipeline dependency; quantity 2 confirmed (playtest calibration) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence-gated resource acquisition is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/FactionNativeResource — Layer = Economy per L175 confirmed; copy model, not transfer | Art 04b §4, §5 |
| Balance | ✓ | Quantity 2 confirmed as working value; playtest calibration item. Copy model confirmed — target pool unchanged | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: resources dispatched at Beat 3; available at month-end via normal case return (Art 04 §5 P19 compliant) | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — Automatic resolution | — |
| Portrait validity | ✓ | Ghost +1 submitter — resource acquisition via intelligence pipeline aligns with Ghost doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | Adjacency restriction applied per 04-n6 — field collection op requires Ghost presence in target district or adjacent | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; target faction native resource type delivered to case; no new components | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Resources in Dispatch Case returned at month-end per normal procedure — no new Art 03 step required | Art 03 §9, §11 |
| Data schema validation | ✓ | 04-n70 ✅ S95 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S112 | Art 04 §5 P26 |

#### Outstanding Issues

None.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Issues Resolved S112*

```python
GHO.CA.10 = Card(
    card_id      = "GHO.CA.10",  version = "v1.1",
    name    = "Flip",
    tagline = "Redirect a target faction's operational resources through Ghost supply channels.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Economy,  function = Add,  subject = FactionNativeResource,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy = None,
    affinity        = None,
    restriction     = (
        faction(acting).intel_tokens(faction=faction(target)) >= 1 and
        district(self|adjacent).faction(acting).presence > 0
    ),
    cost            = IntelToken(faction=faction(target)) * 1,

    success     = game.dispatch(faction(acting), resource.faction(target).native * 2),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Ghost does not steal. Ghost redirects what was already in motion.",
    perspectives = {Ghost: "Their resource. Our pipeline. They built something worth taking."},
    design_note  = "Layer=Economy per L175 — primary effect is resource acquisition despite intelligence gating. Copy model confirmed: target faction does NOT lose resources. Quantity 2 confirmed working value; final calibration deferred to playtest. Adjacency restriction per 04-n6 (combined with Intel token restriction). Resources dispatched to Ghost's Dispatch Case at Beat 3; returned at month-end. Higher-tier Ghost cards carry secondary cost = faction(target).native consumed on play (GHO.CA.2 model).",
    arbiter_note = "At Beat 3: consume IntelToken(faction=target) from Ghost's case. Dispatch 2 units of target faction's native resource type to Ghost's Dispatch Case. Target faction's resource pool is not reduced. Resources available to Ghost at month-end with normal case return.",
)
```

---

### Ghost — SIGNALS ANALYSIS
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's strategically decisive card. Reveals the target faction's Classified Directive privately to Ghost, enabling Ghost to engineer situations where pursuing a hidden objective requires betraying visible doctrine — Ghost's core win vector. Highest cost in the Ghost set (2 faction-keyed Intel tokens + 3 Findings) with the lowest threshold (30%), reflecting that this is a rare, high-investment play not available until Ghost has accumulated significant Intel reserves. Analytical work — no adjacency required, consistent with the GHO.CA.1-GHO.CA.5 pattern. Portrait modifier on success (+2 total) captures Ghost's doctrine that intelligence is only vindicated by operational use.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost's strategically decisive card — reveals Classified Directive enabling Ghost to engineer doctrine-betrayal situations; Ghost's core win vector | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — intelligence as strategic leverage | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; highest cost in Ghost set (2 Intel + 3 Findings); threshold 30 — reserved for Ghost players with Intel reserves; portrait AND semantics outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — Directive reveal is Ghost-exclusive win-condition card | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/ClassifiedDirective — component registration outstanding (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | Threshold 30 + cost 2 Intel + 3 Findings — rarity level appropriate for Directive reveal; singleton | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: private information revealed once at Beat 3; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces Intel token floor (≥2) | — |
| Portrait validity | ✓ | submitter=+1 unconditional + modifier=+1 on success — AND semantics outstanding (Outstanding Issue) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — no district target; operates on abstract ClassifiedDirective object | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost (×2); ClassifiedDirective as target_object — component registration outstanding (Outstanding Issue) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Private reveal via ARBITER screen; private faction-to-faction reveal procedure outstanding (Outstanding Issue) | Art 03 §9, §11; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **BLOCKED — Classified Directive record-keeping procedure required.** The success mechanism requires ARBITER to hold a setup record of each faction's Classified Directive. This infrastructure does not exist. A Classified Directive management procedure (Art 06.x or equivalent) must be designed independently before this execution model can be finalized — do not build this procedure to support a single card. All other outstanding issues are secondary to this blocker.
- **ClassifiedDirective component:** `target_object = ClassifiedDirective` — confirm this is a registered component type in Art 02 series. May need to be added.
- **Private reveal procedure:** ARBITER reveals Directive across screen to Ghost player. Confirm Art 07 has or will have a procedure for private faction reveals (same mechanism as GHO.CA.2 IntelDeliverySlip?).
- **Portrait AND semantics:** `submitter=+1, modifier=+1, mod_where=game.outcome==Success` — confirm same model as GHO.CA.1 Pattern Match (submitter always fires; modifier fires additionally on success).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Draft S59 — design pass pending*

```python
Card(
    id=TBD,  version="v1.0",  # ID pending PM05 04-n1
    name    = "Signals Analysis",
    tagline = "Deduce a target faction's Classified Directive from accumulated intelligence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Reveal,  subject = ClassifiedDirective,

    beat            = 3,
    resolution      = d100,
    threshold       = 30,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = ClassifiedDirective,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(acting).intel_tokens(faction=faction(target)) >= 2,
    cost        = IntelToken(faction=faction(target)) * 2 + resource.faction(acting).findings * 3,

    success     = game.reveal_private(
                    faction(target).classified_directive,
                    to  = faction(acting),
                    via = arbiter
                  ),
    successcrit = None,
    fail        = None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),

    portrait = {Ghost: PortraitEntry(submitter=+1, modifier=+1, mod_where=game.outcome==Success)},

    narrative    = "The Directive is not a secret. It is a pattern. Ghost reads patterns.",
    perspectives = {Ghost: "We are not guessing. We have read enough of their decisions to know what they are trying to protect."},
    design_note  = "Ghost's highest-cost card. Cost: 2 faction-keyed Intel tokens + 3 Findings, all physically present (Art 04 §5 P20). Threshold 30 — reserved for Ghost players who have built Intel reserves. No adjacency restriction (analytical work — consistent with GHO.CA.1-GHO.CA.5 pattern). Portrait: submitter=+1 unconditional + modifier=+1 on success. ClassifiedDirective component type pending verification in Art 02 series.",
    arbiter_note = "Privately reveal target faction's Classified Directive to Ghost player across screen. Do not announce to table. Ghost may not publicly prove knowledge. Crit fail: NotificationSlip to target only — do not reveal what Ghost was attempting.",
)
```

---

### Ghost — SYNTHESIZE
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's intelligence amplification card — converts one held Intel token into three, netting +2. Designed for the GATHER→SYNTHESIZE Double Case Pass combo (L145): play STD.CA.5 Gather in Month 1 to acquire an Intel token, then play Synthesize in Month 2 or 3 to multiply it before a high-cost operation (SCIF, Flip, Signals Analysis). The consumed token can be any faction-keyed token — Synthesize is processing, not targeting. Findings×1 is the analytical cost of converting raw surveillance into operational signal. The result is Ghost building Intel reserves without needing to place additional Gather operations.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence amplification — converts 1 token into 3 (net +2); enables GATHER→SYNTHESIZE combo that pre-loads high-cost operations (SCIF, Flip, Signals Analysis) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — processing as doctrine, not just collection | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; Findings×1 cost reflects analytical work; consumed token is any held token; generated token faction-keying outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence processing is Ghost-exclusive pipeline capability | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/IntelToken — net amplification of Intel supply; Economy layer correct for resource generation effect | Art 04b §4, §5 |
| Balance | ✓ | Findings×1 + 1 IntelToken → 3 IntelTokens (net +2) — amplification rate reasonable; token faction-keying affects SCIF/Flip gate eligibility (Outstanding Issue) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: tokens delivered at Beat 3; durable resource | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter only; submitter-bounded per SYN.PA.2 | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — internal intel processing; no district context | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken as both cost and subject; Findings cost; no new components | Art 02 §6–§8; Art 02 §12 |
| Supported by game procedure | ✓ | Beat 3 Automatic; tokens delivered at Beat 3; SCIF/Flip gate eligibility of generated tokens outstanding (Outstanding Issue) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **GATHER→SYNTHESIZE combo L145:** Confirm L145 is still the canonical reference for this combo — if L145 has been superseded or renumbered, update reference.

*Token faction-keying resolved S119: generated tokens carry the consumed token's faction key. Ghost consumes an X-keyed token and receives three X-keyed tokens. Enables the Gather→Synthesize→Flip pipeline (collect X-keyed token; amplify; use Flip to access Faction X's resources).*

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Migrated from Art 04 §8 (retired) Intel Economy block to Ghost extended section S59. Pre-convention flat format — full schema pass pending (04-47). Token keying resolved S119.*

```python
GHO.CA.6 = Card(
    id      = "GHO.CA.6",  card_id="GHO.CA.6",  version="v1.1",
    name    = "Synthesize",
    tagline = "Convert raw intelligence into operational clarity.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Economy,  function = Add,  subject = IntelToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=None, target_object=IntelToken,
    target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).intel_tokens.count >= 1,
    cost        = resource.faction(acting).findings * 1 + IntelToken(any) * 1,
    boost       = None,
    success     = game.dispatch(faction(acting), IntelToken(faction=consumed_token.faction) * 3),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Ghost: PortraitEntry(submitter=+1)},
    ps_framing  = None,
    narrative   = "Raw surveillance is noise. What Ghost does to it — that is signal.",
    perspectives = {Ghost: "We don't just gather. We process. The difference is what we are."},
    design_note  = "GATHER→SYNTHESIZE Double Case Pass combo (L145): Gather in Month 1, Synthesize in Month 2/3. Consumed token is any held token — not required to be faction-keyed. Generated tokens carry the consumed token's faction key (S119 decision) — enables Gather→Synthesize→Flip pipeline for any target faction.",
    arbiter_note = "Consume 1 held Intel token (any faction key) and 1 Findings from Ghost's supply. Deliver 3 Intel tokens keyed to the consumed token's faction to Ghost's Dispatch Case.",
)
```

---

### Ghost — SOURCE SUBSTITUTION
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Pure utility card — re-keys a held Intel token from its current faction attribution to a different faction. Ghost submits a token in their dispatch case; ARBITER alters the faction field and returns it. Quarter field unchanged; freshness carries over. Cost is the CA slot — no Findings spent. The tradeoff is opportunity cost: spending a covert action on re-keying rather than direct collection. Primary use: Ghost accumulates tokens on accessible targets but needs tokens keyed to specific factions to unlock higher-tier plays (SCIF, Flip, Intercept all require faction-matched tokens). Automatic — no dice, no risk.

Standard equivalent: PM05 04-n15.

#### Card Story
Ghost submits a token from their case. ARBITER alters the name on it. The token returns — it now says what Ghost needs it to say.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Token re-keying enables Ghost's intelligence pipeline — converts available tokens into faction-matched currency for higher-tier plays | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective — record alteration as operational routine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; no Findings cost — CA slot is the gate; Automatic reflects Ghost's precision (no chance of failure on a technical alteration) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence record manipulation is Ghost-exclusive; standard equivalent flagged PM05 04-n15 | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/IntelToken — alters the faction field on an existing token; Corrupt is correct (field modification of an existing component) | Art 04b §4 |
| Balance | ✓ | Cost = CA slot only; Automatic resolution; restriction = must hold a token. Opportunity cost is the constraint | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: token altered and returned at Beat 3; no lingering game-state marker | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat | Art 04 §6 |
| Trigger validity | ✓ | N/A — Automatic; trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — intelligence manipulation is core Ghost doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — no district involvement; token is held asset, faction-targeted re-key only | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken as target_object; no new physical components; quarter field preserved | Art 02 §12 |
| Supported by game procedure | ✓ | Token submitted in case; ARBITER alters faction field at Beat 3; returns to Ghost case — covered by standard Beat 3 cleanup | Art 03 §9.4 |
| Data schema validation | ✓ | 04-n70 ✅ S95 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S112 | Art 04 §5 P26 |

#### Outstanding Issues

None.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Redesigned S112 — plant mode retired; Automatic resolution; cost = CA slot*

```python
GHO.CA.12 = Card(
    card_id      = "GHO.CA.12",  version = "v1.0",
    name    = "Source Substitution",
    tagline = "Alter the faction attribution on a held Intel token.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Corrupt,  subject = IntelToken,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = IntelToken(held, faction(acting)),

    target_taxonomy = None,
    affinity        = None,
    restriction     = faction(acting).intel_tokens() >= 1,
    cost            = None,

    success     = arbiter.corrupt(target_object, field=faction_name, value=faction(target)),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    on_accept  = None,
    on_decline = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "The record says what Ghost needs it to say.",
    perspectives = {Ghost: "The attribution is wrong. It will stay wrong. What matters is what Ghost does with it next."},
    design_note  = "Re-keys an Intel token's faction field to faction(target). Quarter field unchanged — freshness carries over. Cost = CA slot (no Findings). Automatic — no dice, no risk. Token is target_object: submitted in case alongside card, returned after alteration. Standard equivalent: PM05 04-n15.",
    arbiter_note = "Token submitted in Ghost's case alongside card. At Beat 3: alter faction_name field on token to faction(target); return altered token to Ghost's case. No announcement.",
)
```

---

### Ghost — BACKDATE 🚫 BLOCKED
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Intelligence poisoning — alter the quarter field on a held Intel token to make it appear older. A Fresh token can be degraded to Stale or Expired. The primary use is the poisoned gift (plant mode): deliver a degraded token to a target faction who will discover — when they attempt to use it — that their intelligence is stale or worthless. The acting faction sacrifices a functional token to waste a future opposing action. Keep mode has narrower use: Ghost may want to make an operation appear to have occurred earlier (strategic alibi). Threshold 30 is harder than Source Substitution (45) because temporal records are more verifiable — altering when something happened is more conspicuous than altering who. Fail destroys the token; failcrit notifies the originally-named faction. Ghost adjacency applies in plant mode.

Standard equivalent: PM05 04-n15.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Temporal falsification of intelligence records — primary use is poisoned gift (plant Expired token on target to waste their attribution play) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — temporal record manipulation as operational doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; threshold 30 (harder than Source Substitution 45) reflects temporal records are more verifiable; same keep/plant dual mode as Source Substitution | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/IntelToken (quarter field) — distinct from Source Substitution (faction field) | Art 04b §4 |
| Balance | ✓ | Threshold 30 — harder than Source Substitution; temporal records more verifiable; fail destroys token — real cost | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: token altered and returned/planted at Beat 3; fail destroys token at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces Intel token presence | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no adjacency restriction. Plant mode retired S112. Card 🚫 BLOCKED (L222). | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken as both cost and target; requires two writable fields (faction + quarter) outstanding (Outstanding Issue); instructions slip in case | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Plant mode delivery protocol same as Source Substitution — outstanding (Outstanding Issue) | Art 02 §6–§8; Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Token writable fields:** Intel token component must support two writable fields (faction name + quarter). Confirm component design in Art 02.
- **Plant mode delivery protocol:** Same as Source Substitution — discreet delivery to target terminal during Beat 3 cleanup; procedure not yet defined in Art 03/07.
- **🚫 BLOCKED (S107, L222):** Two permanent constraints. (1) Location: Intel token in private terminal zone is not reachable by opposing card. (2) GR 7.2b: the quarter field records when the token was committed — a committed fact; retroactive alteration violates the finality principle. The provenance-field approach is permanently closed. Fundamental redesign required; design path must be additive. Cross-ref: Art 04b §8.1 item 3, PM05 04-n103.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | 🚫 BLOCKED | — | — |

```python
Backdate = Card(
    id      = "Ghost-ext-TBD",  version = "v1.0",
    name    = "Backdate",
    tagline = "Corrupt the quarter field on a held Intel token — make it appear older than it is.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Corrupt,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 30,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Deceptive",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.any_or_none,  # None = keep; named = plant
    target_object   = intel_token.held,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Ghost).holds_intel_token(count=1),
    cost        = resource.faction(Ghost).findings * 2 + intel_token.held * 1,

    # Instructions slip in case: [new quarter — must be earlier than current] | [return: self / named faction]
    success = (
        arbiter.corrupt(intel_token.held, field=quarter, value=declared_earlier_quarter),
        if target_faction == None:
            arbiter.return_to_case(intel_token),
        else:
            arbiter.deliver_discreet(intel_token, target_faction),
    ),
    successcrit = None,
    fail        = arbiter.destroy(intel_token),
    failcrit    = (
        arbiter.destroy(intel_token),
        arbiter.dispatch(NotificationSlip, recipient=intel_token.faction_named),
    ),

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "The question is not what the token says. The question is when it says it happened.",
    perspectives = {
        Ghost: "An old record is a useless record. We are making it old.",
    },
    design_note  = "Temporal falsification — quarter field only. Distinct from Source Substitution (faction field). Threshold 30 vs 45: altering when is harder than altering who. Primary use: plant mode to deliver degraded/Expired token as poisoned gift — target wastes a future attribution play. Keep mode: make own operations appear to have occurred earlier. Intel token component must support two writable fields (faction + quarter). Standard equivalent PM05 04-n15.",
    arbiter_note = "Instructions slip in case: new quarter number (must pre-date current Quarter) + keep or plant destination. Beat 3: d100 vs 30. On success: alter quarter field; token age reclassified accordingly (may shift Fresh → Stale, Stale → Expired, or Fresh → Expired depending on magnitude). Keep: return in case. Plant: discreet delivery to target terminal (same protocol as Source Substitution). On fail: destroy token. On failcrit: destroy + NotificationSlip to faction named on token.",
)
```

---

### Ghost — FIELD VERIFICATION 🚫 BLOCKED
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost re-validates expired intelligence. An Expired Intel token is submitted in the dispatch case with no instructions — the question posed to ARBITER is simply: is this still current? On success, the token's quarter is updated to the present Quarter and its classification becomes Fresh. On fail, the token is returned Expired and Ghost has lost only the dispatch slot. No Findings cost — the slot IS the investment. Threshold 35 reflects genuine uncertainty: intelligence gathered 4+ quarters ago may or may not still describe reality; there is no guarantee the world has not changed. This is not falsification — Ghost is genuinely re-checking a cold lead. Self-operation only; no adjacency required. Distinct from Source Substitution and Backdate (which falsify; this verifies).

Standard equivalent: PM05 04-n15 (hired investigator reopening cold case — same mechanic, costs Findings, lower threshold).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost re-validating aged intelligence — "understanding must precede action" includes verifying that old understanding is still current; Expired → Fresh recovery | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — verification as discipline, not just collection | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; no Findings cost — slot IS the investment; self-operation only; distinct from Source Substitution/Backdate (falsification vs. verification) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence pipeline methodology; standard equivalent flagged PM05 04-n15 | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Recover/IntelToken — Recover returns a degraded element to active play; Expired → Fresh is a recovery | Art 04b §4 |
| Balance | ✓ | No Findings cost; dispatch slot only; fail = slot wasted, token returned (no token loss); threshold 35 creates meaningful failure rate | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: token updated or returned at Beat 3; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces Expired token in case | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded; re-validation before acting is Ghost's core doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — self-operation on held token; no district context | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Expired) as cost and target; requires writable quarter field (same as Backdate — see Backdate Outstanding Issue) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Self-operation; no adjacency required; ARBITER updates quarter field on success, returns token on fail | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

- **🚫 BLOCKED (S107, L222):** GR 7.2b — the quarter field records when the token was committed; updating it to the current Quarter alters a committed provenance field. The field-update approach is permanently closed. Fundamental redesign required. Cross-ref: Art 04b §8.1 item 3, PM05 04-n103.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | 🚫 BLOCKED | — | — |

```python
FieldVerification = Card(
    id      = "Ghost-ext-TBD",  version = "v1.0",
    name    = "Field Verification",
    tagline = "Re-validate an Expired Intel token — confirm the intelligence is still current.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Recover,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 35,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Verification",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,  # self-operation; no adjacency required
    target_faction  = None,
    target_object   = intel_token.held,  # must be Expired; submitted in case

    target_taxonomy=None,
    affinity    = None,
    restriction = intel_token.held.age == Expired,
    cost        = None,  # no resource cost; dispatch slot is the investment (Governing Rule 7.3c)

    success = (
        arbiter.update(intel_token.held, field=quarter, value=game.current_quarter),
        arbiter.return_to_case(intel_token),
        # token reclassified Fresh (0–1 quarters old = current Quarter)
    ),
    successcrit = None,
    fail        = arbiter.return_to_case(intel_token),  # token returned Expired; no loss
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "The intelligence is old. The question is whether it is still true.",
    perspectives = {
        Ghost: "We go back to check. The answer determines whether we can use this at all.",
    },
    design_note  = "Self-operation to re-validate cold intelligence. No Findings cost — dispatch slot only. Fail returns the token Expired (no loss beyond the slot). Success advances token to Fresh (current Quarter). d100 threshold 35 reflects genuine uncertainty about whether aged intelligence still describes reality. Not falsification — Ghost is actually checking. Distinct from Source Substitution and Backdate. Standard equivalent (hired PI, higher cost) flagged PM05 04-n15.",
    arbiter_note = "Token submitted in case. Restriction: token must be Expired. No instructions slip needed. Beat 3: d100 vs 35. On success: update token's quarter field to current Quarter; token is now Fresh; return in case. On fail: return token in case unchanged (still Expired). No resource consumed either outcome.",
)
```

---


---

---

### GHO.CA.13 — PHANTOM ACCOUNTS *(stub)*
[↑ Covert Operations](#ghost-covert-operations)

```python
GHO.CA.13 = Card(
    id      = "GHO.CA.13",  version = "v1.1",
    name    = "Phantom Accounts",
    tagline = "Siphon a shadow copy of an opponent's influence-based resource generation.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Economy,  function = Add,  subject = DebriefActionCard,
    beat    = 3,  resolution = d100,  threshold = 50,
    cost    = resource.faction(Ghost).findings * 2,
    success = "Arbiter places 1 DA-02 (PhantomRecord) in Ghost's Dispatch Case. At debrief, Ghost gains district native resources equal to target_faction's influence-based generation.",
    design_note = "A financial twin to SCIF. Instead of generating Modifier cards off of structural density, this converts Findings into a mirrored payout of the target's passive district income."
)
```

---

### GHO.CA.14 — GHOST PROTOCOL *(stub)*
[↑ Covert Operations](#ghost-covert-operations)

```python
GHO.CA.14 = Card(
    id      = "GHO.CA.14",  version = "v1.1",
    name    = "Ghost Protocol",
    tagline = "Completely erase an opponent's operation from existence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Submission,  function = Block,  subject = CovertOperation,
    beat    = 2,  resolution = Automatic,
    cost    = resource.faction(Ghost).findings * 2 + resource.faction(Ghost).exposure * 1 + resource.faction(Ghost).capital * 1 + intel_token * 1,
    success = "The Arbiter invalidates and removes the first Covert Operation submitted by target_faction in Beat 3.",
    design_note = "Massive multi-resource cost to justify an unblockable, blind veto of an opponent's action."
)
```

### Ghost — Public Acts
[↑ Ghost](#ghost)

| Card | Name |
|------|------|
| [GHO.PA.1](#p17-publish-analysis) | Publish Analysis |
| [GHO.PA.2](#p18-signal-review-request) | Signal Review Request |
| [GHO.PA.3](#ghopa3--declassified-records) | Declassified Records |
| [GHO.PA.4](#ghopa4--public-threat-assessment) | Public Threat Assessment |
| [GHO.PA.5](#ghopa5--agency-recruitment-fair) | Agency Recruitment Fair |

### GHO.PA.1 — PUBLISH ANALYSIS
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Ghost's highest-cost PA — a simultaneous public attribution of two factions using two Intel tokens as evidence. The token requirement is the certainty check: Ghost does not publish speculation. Two tokens naming different factions are spent; both attributions are announced at Beat 4. Each named faction loses −2 PS; Ghost gains +2 PS flat. Ghost pays 3 Findings (their core intelligence currency) plus two Intel tokens for a decisive multi-target public strike — the cost reflects that going public is doctrinally expensive for Ghost even when the intelligence justifies it. Portrait +1: Ghost acts on doctrine when understanding precedes the disclosure decision.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost publishing curated analysis is a calculated, rare public act — the cost enforces rarity | Art 00 §7 |
| Voice fit | ✓ | Ghost on-doctrine; Directorate (aligned): verified, sequenced disclosure; Network (opposed): held both when one was enough | Art 00 §7, §9 |
| Doctrine alignment | ✓ | "Understanding must precede action" — Ghost publishes only when two tokens confirm both attributions. Portrait +1: calculated disclosure from position of knowledge. 3 Findings cost reflects that public disclosure is doctrinally expensive for Ghost | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Reveal / ActionAttribution (multi-target) | Art 04b §4 |
| Balance | ✓ | 3 Findings + 2 Intel tokens; Automatic; two targets −2 PS each; Ghost +2 PS. High cost, high yield. Token acquisition is the natural limiter | Art 02 §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded. Published from position of knowledge — doctrine affirmed | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — two faction targets; no district reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (two, faction-keyed to different targets; Art 02 §6); Findings × 3 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Two targets named at Phase B; both tokens submitted; Automatic Beat 4 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
GHO.PA.1 = Card(
    id      = "GHO.PA.1",  version="v1.0",
    name    = "Publish Analysis",
    tagline = "Release curated intelligence simultaneously attributing operations to two factions — a calculated, costly disclosure.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Reveal,  subject = ActionAttribution,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.two_opponents,  # two different factions named at Phase B
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = (
        faction(Ghost).holds_intel_token(faction=target1) and
        faction(Ghost).holds_intel_token(faction=target2) and
        target1 != target2
    ),
    cost = (
        resource.faction(Ghost).findings * 3
        + intel_token(target=faction(target1)) * 1
        + intel_token(target=faction(target2)) * 1
    ),

    success = (
        arbiter.announce(attribution=target1, context=intel_token_1.quarter),
        arbiter.announce(attribution=target2, context=intel_token_2.quarter),
        faction(target1).standing -= 2,
        faction(target2).standing -= 2,
        faction(Ghost).standing   += 2,
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Ghost does not publish because it wants credit. Ghost publishes because the analysis is complete and the disclosure serves more than the concealment.",
    perspectives = {
        Ghost:       "We have done the work. Both attributions are supported. The timing is correct. We publish.",
        Directorate: "Ghost discloses both attributions from verified position. The timing was chosen. The evidence was held until both targets were confirmed. This is how intelligence should enter the record.",  # aligned
        Network:     "Ghost waited for both confirmations. We published after the first. The second attribution was true by the time Ghost released it — and so was all the damage that came between.",  # opposed
    },
    design_note  = "Ghost's highest-cost PA. 3 Findings + 2 Intel tokens (different factions). Automatic — token requirement is the certainty check (Ghost does not publish speculation). Simultaneous dual attribution: each target −2 PS, Ghost +2 PS flat. Portrait +1: calculated disclosure affirms 'understanding must precede action' doctrine. Option 3 (operational blackout mechanic) flagged as PM05 item for potential Network PA extension.",
    arbiter_note = "Phase B: Ghost names two target factions. Both Intel tokens submitted with case. Beat 4: announce '[Ghost] attributes [op type, quarter] to [target1]' and '[Ghost] attributes [op type, quarter] to [target2].' Each target −2 PS. Ghost +2 PS. Both tokens spent.",
)
```

---

### GHO.PA.2 — SIGNAL REVIEW REQUEST
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Ghost uses institutional channels to apply operational pressure on a named faction. The effect is a −15 threshold penalty on that faction's covert operations in the named district next Month (Transient). Ghost gains no PS — this is a tool, not a stage. Ghost adjacency applies — Ghost must have presence in a district adjacent to the target. Persistence = Transient: the GHO.PA.2 card stays face-up on the table with a marker on the target district until Close Month of next Month, serving as the active condition indicator. ARBITER removes the card and returns it to Ghost at Close Month.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost using institutional accountability to enforce operational scrutiny is on-doctrine and narratively grounded | Art 00 §7 |
| Voice fit | ✓ | Ghost on-doctrine; Syndicate (aligned): institutional tool with no exposure cost; Guild (opposed): bureaucratic delay vs. direct action | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Ghost uses the institutional channel as a tool, not a stage — no PS gain. Adjacency requirement grounds the card in Ghost's operational footprint. Portrait +1: submitter-bounded | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Resolution / Modify / CovertOperation (difficulty) | Art 04b §4 |
| Balance | ✓ | 2 Findings; −15 threshold (meaningful but not absolute block); Transient. Ghost adjacency limits targeting range | Art 02 §6–§7 |
| Effect duration | ✓ | Threshold modifier is Transient (until Close Month of next Month — within-Quarter). No multi-Quarter duration | Art 04 §5 P19 |
| Persistence | ✓ | Transient — card stays face-up on table with district marker until Close Month next Month | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone; restriction: Ghost presence in district adjacent to target | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — threshold modifier is a world condition tracked by ARBITER; Findings × 2 cost (Art 02 §8) | Art 02 §8 |
| Supported by game procedure | ✓ | Physical tracking: GHO.PA.2 card face-up + district marker; ARBITER removes at Close Month next Month | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
GHO.PA.2 = Card(
    id      = "GHO.PA.2",  version="v1.0",
    name    = "Signal Review Request",
    tagline = "Formally request institutional scrutiny on a faction's next covert operation in a named district.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Resolution,  function = Modify,  subject = CovertOperation,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Transient,  # card stays on table with district marker until Close Month next Month
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Ghost).presence(district.adjacent_to(target_district)) > 0,
    cost        = resource.faction(Ghost).findings * 2,

    success = game.world_condition(
        scope    = district(target),
        target   = covert_op(faction=target_faction),
        effect   = threshold -= 15,
        duration = Transient,  # Close Month of next Month
    ),
    # Ghost does not gain PS — uses the channel as a tool, not a stage

    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Ghost does not need credit for this. The scrutiny is the point.",
    perspectives = {
        Ghost:     "We are not making an accusation. We are requesting that the process do what the process is designed to do.",
        Syndicate: "Ghost asks ARBITER to enforce the review. No exposure, no escalation, no record beyond the request itself. We recognize the structure. The target carries the friction. Ghost carries nothing.",  # aligned
        Guild:     "Ghost routes the pressure through ARBITER rather than holding the position itself. The district gets harder to operate in. Nothing is built. Ghost calls this strategy. Guild calls it avoidance.",  # opposed
    },
    design_note  = "Ghost operational pressure PA. Uses institutional scrutiny (ARBITER) to apply −15 threshold to target faction's covert ops in named district next Month. No PS gain for Ghost — the channel is a tool. Ghost adjacency: must have presence in district adjacent to target. Persistence = Transient: GHO.PA.2 card face-up on table + district marker until Close Month of next Month. Multiple P18s from different Months can stack. Distinct from GHO.PA.1 (attribution) — GHO.PA.2 creates ongoing pressure without disclosure.",
    arbiter_note = "Beat 4: place GHO.PA.2 card face-up on table with marker on target district. Apply −15 threshold penalty to all covert operations submitted by target faction in target district next Month (Beat 3). Card expires Close Month that Month — announce removal, return card to Ghost. Multiple GHO.PA.2 cards on same district from different Months stack (each tracked independently). Ghost adjacency enforced at Beat 0.",
)
```

---

### GHO.PA.3 — DECLASSIFIED RECORDS
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Declassified Records converts accumulated expired Intel tokens into Public Standing through formal public disclosure. The base card (+1 PS, threshold 50, cost 1 Findings) is playable on its own; the boost mechanic is the amplifier. Each expired token submitted adds one BM-xx marker — the standard BM-xx mechanism then multiplies all effects by (1+n). Three expired tokens turns a +1 PS play into +4 PS, and the failcrit into −4 PS. The design rewards multi-Quarter Intel discipline: Ghost factions that run intelligence operations over time without spending their tokens covertly build a deferred credibility reserve. The restriction (at least 1 expired token) keeps the card grounded narratively — Ghost releases *something*; a blank disclosure is not this card. The Faction Player may optionally give a brief in-character account of what records are being released; this is not a procedure step.

#### Card Story
Ghost submits the case files in order — sequential, dated, attributed. The records are expired. The intelligence is cold. The point is that Ghost kept them, and kept them clean, and is releasing them now because the moment is right. Each file laid on the table is a demonstration that the agency did the work while others were reacting.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal release of archived intelligence as institutional credibility play — information is power, including cold information released on Ghost's terms | Art 00 §7 |
| Voice fit | ✓ | Ghost on-doctrine; Directorate (aligned): sequenced formal disclosure is the proper channel; Network (opposed): "publish when you have it" conflicts with Ghost's timing discipline | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Patience and sequenced disclosure are Ghost doctrine. Portrait +1 submitter. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Remove / IntelToken — expired qualifier handled via restriction + boost field | Art 04b §4 |
| Balance | ✓ | Base: 1 Findings, +1 PS at threshold 50. Boost: each expired token ×(1+n). Risk scales with depth — failcrit = −(1+n) PS | Art 02 §6–§7 |
| Effect duration | ✓ | PS shift immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — tokens are held, not placed | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken expired (Art 02 §9); BM-xx (Art 02 §12); Findings × 1 (Art 02 §8) | Art 02 §8–§9, §12 |
| Supported by game procedure | ✓ | BM-xx at Beat 4: boost detection added Art 03 §9.4.3.1.0.0 (S109); threshold at Art 03 §9.4.3.2.0; effect multiplication at Art 03 §9.4.3.3 | Art 03 §9.4.3 |
| Data schema validation | ✓ | All §6.1 fields present | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Story block above | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
GHO.PA.3 = Card(
    id      = "GHO.PA.3",  version="v1.0",
    name    = "Declassified Records",
    tagline = "Release expired intelligence as institutional record — each file compounds the disclosure.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Remove,  subject = IntelToken,

    beat            = 4,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    target_taxonomy = None,

    affinity    = None,
    restriction = count(intel_token(holder=Ghost, status=Expired)) >= 1,
    cost        = resource.faction(Ghost).findings * 1,
    boost       = intel_token(holder=Ghost, status=Expired),  # 1 expired token = 1 BM-xx; BM-xx ×(1+n) all effects at Art 03 §9.4.3.3

    success     = faction(Ghost).standing.add(1),
    successcrit = faction(Ghost).standing.add(1),  # +1 PS additional delta; also ×(1+n) via BM-xx
    fail        = None,
    failcrit    = faction(Ghost).standing.remove(1),  # delta from fail; also ×(1+n) via BM-xx

    on_accept  = None,
    on_decline = None,

    portrait   = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Ghost does not release because it ran out of options. Ghost releases because it chose this moment, these records, and this account. The archive is not empty — this is a selection.",
    perspectives = {
        Ghost:       "The tokens are expired. The operations they document are closed. We are not losing intelligence by releasing this — we are spending it correctly.",
        Directorate: "Ghost held these until the moment suited them. The records are verified. The disclosure is formal. This is how intelligence should enter the public domain.",
        Network:     "Ghost sat on this for three Quarters and then picked their moment. We published when we had it. Ghost published when it helped Ghost.",
    },
    design_note  = "Base success = +1 PS; successcrit = +1 PS additional. Boost = expired Intel tokens (status=Expired, holder=Ghost); each submitted token = 1 BM-xx at Art 02 §9.4.3.1.0.0. BM-xx ×(1+n) multiplies all effects: n tokens → +(1+n) PS on success; +(1+n)+1 PS on successcrit (success + crit both multiplied); −(1+n) PS on failcrit. Restriction ensures at least 1 expired token present (narrative grounding). Faction Player may optionally narrate what records are being declassified — this is not a procedure step.",
    arbiter_note = "Phase B: Ghost declares expired tokens (status=Expired) being submitted as boost — record count as n. Beat 4 Art 03 §9.4.3.1.0.0: place n BM-xx on card; expired tokens deposited to Dossier at Art 02 §9.4.3.1.0.1. Art 03 §9.4.3.3: effects ×(1+n). Success: Ghost +(1+n) PS. Successcrit: Ghost +(1+n) PS success + +(1+n) PS crit delta = +(2+2n) PS total. Fail: no effect. Failcrit: Ghost −(1+n) PS.",
)
```

---

### GHO.PA.4 — PUBLIC THREAT ASSESSMENT
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Ghost forces ARBITER to publicly reveal a Broadcast Effect Card. The Broadcast Card (public face) is already visible in the Situation Report Zone — Ghost is naming the thing the table can already see. The BEC (mechanical face, ARBITER Tableau) is what Ghost is extracting. GR 10.1b obligates ARBITER to disclose from its own domain when a valid trigger is submitted, so resolution is Automatic. The +1 PS reflects that forcing institutional transparency is itself a credibility act. BC/BEC linking is already established at Art 02 §7.2.1 — no new mechanism required. The named BC is recorded on the Target Profile at Phase B (target object field, S109).

#### Card Story
Ghost files the request before Beat 4. The Broadcast Card has been face-up all Quarter — its name, its narrative, its presence. What Ghost is asking for is the other half. ARBITER opens the file. The table reads the effect for the first time. Ghost already knew what to ask.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Forcing disclosure of hidden mechanical effects — Ghost doctrine: information asymmetry is a threat to be corrected | Art 00 §7 |
| Voice fit | ✓ | Ghost on-doctrine; Directorate (aligned): formal disclosure through proper channel; Network (opposed): "we'd have published it sooner" | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Disclosure from institutional authority is on-doctrine. Portrait +1 submitter. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Reveal / BroadcastEffectCard — GR 10.1b governs; ARBITER performs the reveal | Art 04b §4 |
| Balance | ✓ | Automatic. Cost: 1 Findings + PA slot. Reward: table-wide BEC information + +1 PS. Limiter: requires active BC. | Art 02 §6–§7 |
| Effect duration | ✓ | Reveal immediate; PS immediate; BEC stays in Tableau | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — BEC returned to Tableau; mechanical effects continue per Art 03 §9.4.1.1 / Art 03 §9.4.3.0.1 | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None; target_object = BroadcastCard (Situation Report Zone) | Art 01 §6–§7 |
| Supported by components | ✓ | BroadcastCard (DB:25, Art 02 §10); BroadcastEffectCard (DB:98, Art 02 §10); Target Profile target-object field (DB:48, Art 02 §8 — S109); Findings × 1 (Art 02 §8) | Art 02 §8, §10 |
| Supported by game procedure | ✓ | §7.2.1 establishes BC/BEC link at setup. Art 03 §9.4.3.3.0 VM-xx placement clause; Art 03 §9.4.3.1.3 BEC public resolution step (S110). | Art 03 §7.2.1, §9.4.3.1.3, §9.4.3.3 |
| Data schema validation | ✓ | All §6.1 fields present | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Story block above | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
GHO.PA.4 = Card(
    id      = "GHO.PA.4",  version="v1.0",
    name    = "Public Threat Assessment",
    tagline = "Name a Situation Report. ARBITER opens the file.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Reveal,  subject = BroadcastEffectCard,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = None,
    target_object   = BroadcastCard.named,  # declared at Phase B on Target Profile; must be active in Situation Report Zone
    target_taxonomy = None,

    affinity    = None,
    restriction = count(broadcast_card(zone=SituationReportZone, status=Active)) >= 1,
    cost        = resource.faction(Ghost).findings * 1 + resource.faction(Ghost).exposure * 1,
    boost       = None,

    success = (
        arbiter.place_vm(broadcast_effect_card(linked_to=target_object)),
        faction(Ghost).standing.add(1),
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    on_accept  = None,
    on_decline = None,

    portrait   = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Ghost does not wait to find out what the Situation Report means. Ghost asks ARBITER, on the record, in front of everyone.",
    perspectives = {
        Ghost:       "The broadcast is public. The effect is not. That asymmetry is not information — it's concealment. We are correcting the record.",
        Directorate: "Ghost has formalized the disclosure request. ARBITER complied. The effect was known to us already, but now it is known to everyone. We note this.",
        Network:     "We would have published that two weeks ago if we had it. Ghost had the institutional standing to ask. That's the difference.",
    },
    design_note  = "Automatic — GR 10.1b obligates ARBITER to disclose from own domain when a valid trigger is submitted. Ghost names a Broadcast Card at Phase B (recorded on Target Profile target-object field); ARBITER places VM-xx on the linked BEC at Art 03 §9.4.3.3.0. BEC resolves publicly at Art 03 §9.4.3.1.3 when the next PA in initiative order is reached, or at Art 03 §9.4.1.1 next Quarter if Ghost plays last. BC/BEC link established at Art 02 §7.2.1; no new mechanism required. +1 PS: forcing institutional transparency is a credibility act. Portrait +1: disclosure from institutional authority is on-doctrine Cost reasoning: Exposure represents the deliberate unmasking of the threat to the public, amplifying the raw intelligence.",
    arbiter_note = None,
)
```

---

### GHO.PA.5 — AGENCY RECRUITMENT FAIR
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Ghost's only territory PA — operates entirely in the open, targeting districts where the analytical workforce already lives. Career fairs, public outreach, visible institutional presence. Distinct from STD.CA.3 Campaign (covert, +1 chip, any district): this is public (+2 chips, declared at Phase B, React-able), costs Ghost's own resource, and is restricted to the 4 Findings-generating districts where Ghost's doctrine is most legible. PA slot + 1 Findings justifies the +2 chip output. Ring modifier: easier in Baryo (University Perimeter — Ghost's natural Baryo anchor), harder in Core (Chorus Research — high-prestige, contested institutional space). Successcrit +1 PS: a well-attended fair is a public credibility event. Failcrit −1 PS: low turnout in public is an embarrassment. Ghost adjacency applies — must have presence in a district adjacent to the target Findings district.

#### Card Story
Ghost files the act at Phase B. A table. A banner. Printed materials no other faction would bother preparing. The researchers in this district have been watching Ghost operate for two Quarters — they know what the work is. By Beat 4 the conversations have happened. Ghost has presence now, not just access. The district noted the distinction.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost operating in public in knowledge districts — recruitment = institutional legitimacy, not covert expansion | Art 00 §7 |
| Voice fit | ✓ | Ghost-specific; Directorate (aligned) watches but doesn't interfere — this is procedure, not threat; Network (opposed) notes Ghost is building in the open what they normally build in the shadows | Art 00 §7, §9 |
| Doctrine alignment | ✓ | "Understanding must precede action" — public presence in research districts is Ghost anchoring where understanding is produced; Portrait +1 submitter | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory \| Add \| PresenceToken — places Ghost presence chips in target district | Art 04b §4 |
| Balance | ✓ | 1 Findings + PA slot → +2 chips; restricted to 4 districts, public/React-able, adjacency required | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — chips placed on board are permanent board state (not a Permanent card) | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; chips remain per normal board rules | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | Findings districts (University Perimeter, Data Exchange, Research Institute, Chorus Research) — all valid board zones | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); Findings × 1 (Art 02 §8); max 6 chips/faction/district enforced at game.add() (GR 8.1) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 4 PA resolution; game.add() for presence chips; GR 8.1 chip cap | Art 03 §9.4 |
| Data schema validation | ✓ | All §6.1 fields present | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Story block above | Art 04 §5 P26 |
| Outcome determinacy | ✓ | success = exactly one outcome; successcrit = additive delta; fail = None; failcrit = additive delta | Art 04 §5 P27 |
| Resource cost positioning | Is this card's cost mono-resource (acting faction's own native resource only) or cross-faction-resource (two or more distinct native resources)? Confirm power level matches: mono-resource = floor-power; cross-faction-resource = ceiling-power. Flag if mono-resource and high-power, or cross-resource and underpowered. If cost generates non-native resources as an effect, flag — requires doctrine justification. *(P28)* | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
GHO.PA.5 = Card(
    id      = "GHO.PA.5",  version="v1.0",
    name    = "Agency Recruitment Fair",
    tagline = "The agency operates in the open. The interested are watching.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Ghost,

    layer   = Territory,  function = Add,  subject = PresenceToken,

    beat            = 4,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = {Ring3: +10, Ring1: -15},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any(resource_type=Findings),
    target_faction  = None,
    target_object   = None,
    target_taxonomy = None,

    affinity    = None,
    restriction = district.resource_type == Findings and faction(Ghost).presence(district.adjacent_to(target_district)) > 0,
    cost        = resource.faction(Ghost).findings * 1,
    boost       = None,

    success     = game.add(PresenceToken, to=target_district, count=2),
    successcrit = faction(Ghost).standing.add(1),
    fail        = None,
    failcrit    = faction(Ghost).standing.sub(1),

    on_accept  = None,
    on_decline = None,

    portrait   = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = None,  # pending D-04-08
    perspectives = None,  # pending D-04-08
    design_note  = "Ghost's only territory PA. Adds 2 presence chips in a Findings-generating district (University Perimeter, Data Exchange, Research Institute, Chorus Research — 4 districts). PA slot + 1 Findings cost justifies +2 output over STD.CA.3 Campaign's covert +1; public declaration means opponents see the target at Phase B and can React. Ring modifier: easier in Baryo (University Perimeter, familiar academic ground), harder in Core (Chorus Research, contested institutional space). Successcrit +1 PS: a well-attended fair is a public credibility event. Failcrit −1 PS: low turnout is a public embarrassment. Ghost adjacency applies at Beat 0. card_id = GHO.PA.5.",
    arbiter_note = "Restriction check at Beat 0: confirm target district resource_type = Findings AND Ghost has presence in a district adjacent to target. On success: place 2 Ghost presence chips in target district (enforce GR 8.1 max 6). On successcrit: additionally move Ghost's PS marker +1. On failcrit: move Ghost's PS marker −1. Cost (1 Findings) submitted to Reservoir regardless of outcome.",
)
```

---


---


---

### GHO.MOD.1 — SLEEPER ANALYST *(stub)*

*S110. Ghost Modifier/React — fires at Art 03 §9.2.0 on any PA placed with an Intel token. Ghost must name the faction on the token; ARBITER validates. Note: Art 02 §9 excludes Modifier cards from the taxonomy matrix; Layer/Function/Subject fields below describe the card's effect category for spec clarity only.*

**Design Rationale:** Ghost's counter-attribution React. When any faction places a PA with an Intel token in the Faction Resolution Grid at Art 03 §9.2.0, Ghost may announce React and declare the faction they believe is named on that token. ARBITER checks the token's faction field. If Ghost's declaration matches: the Intel token is removed, the PA is cancelled, all resource tokens on the PA drain to the Reservoir (no refund), and Ghost gains +1 PS. If Ghost is wrong: card consumed, no effect, PA proceeds.

The intelligence test is genuine: because Target Profiles are placed face-down at Art 03 §9.2.0 (revealing at Art 03 §9.4.3.1.1), and Intel token content is always ARBITER-private, Ghost cannot guess from publicly visible information. Prior intelligence work is required — SIGINT taps, Source Substitution plant mode, or other intelligence that revealed the token's faction field. The chain play is: plant or observe the token → hold React → fire when the attribution PA is declared.

Ghost's portrait −2 on STD.PA.5 documents that public attribution violates Ghost's doctrine across all factions. Sleeper Analyst makes that doctrine actionable: Ghost can mechanically suppress any attribution they have intelligence on. Works against corrupted tokens (planted by Ghost via Source Substitution) and legitimate ones alike — Ghost believes no covert attribution belongs on the public record.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Counter-attribution at PA placement — Ghost doctrine: operational anonymity across the full table | Art 00 §7 |
| Voice fit | ⚠ | Perspectives TBD — deferred to modifier card voice pass (D-04-08) | Art 00 §9 |
| Doctrine alignment | ✓ | Ghost +1 portrait: publicly demonstrating intelligence superiority while suppressing attribution is Ghost doctrine at peak visibility. FactionSpecific — no other portraits | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard / FactionSpecific (Ghost) — trigger is publicly visible board state change (PA placement at Art 03 §9.2.0) per Art 03 §18.0 | Art 04 §6.1, §6.2; Art 03 §18 |
| Taxonomy fit | ✓ | Modifier cards excluded from matrix per §11.1 — Layer/Function/Subject = None. Spec clarity: Information / Remove / IntelToken | Art 04b §9; Art 04 §11.1 |
| Balance | ✓ | No activation cost — card consumed on fire. Requires prior intelligence to use reliably. Misfire wastes the card. Strongly rewards GHO Source Substitution plant chain | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — PA cancellation and PS shift at Art 03 §9.2.0 trigger | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — no lingering board state marker | Art 04 §6 |
| Trigger validity | ✓ | Any PA with Intel token placed at Art 03 §9.2.0 — publicly visible board state change (Art 02 §18.0). React window closes when Art 03 §9.2.0 advances to next faction's declaration | Art 03 §18.0; Art 03 §9.2.0 |
| Portrait validity | ✓ | Ghost submitter=+1 — submitter-bounded. Suppressing attribution from position of intelligence knowledge is Ghost on-doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | No district reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (on placed PA card in Resolution Grid; Art 02 §6); PS shift (Art 02 §11) | Art 02 §6, §11 |
| Supported by game procedure | ✓ | React per Art 03 §18. Trigger at Art 03 §9.2.0. Target Profile face-down at Art 03 §9.2.0 (per Art 03 §9.2.0 procedure — intelligence test is genuine). Ghost Source Substitution provides corruption mechanism. | Art 03 §18; Art 03 §9.2.0; Art 04 GHO — Source Substitution |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

**Outstanding Issues:**
- **Card name:** "Sleeper Analyst" — pending voice pass (D-04-08). Card suppresses attribution whether true or false; name reflects Ghost's doctrine that any public attribution distorts understanding.
- **Card ID:** GHO.MOD.1 — pending 04-n1 numbering pass.
- **Modifier card schema:** Full spec pending modifier card design pass (04-n4). Fields below use established conventions.

**Status:** Design pass complete — S110. Issues Resolved and sign-off pending 04-n4 schema pass.

```python
GHO.MOD.1 = Card(
    id      = "GHO.MOD.1",  card_id="GHO.MOD.1",  version="v1.0",
    name    = "Sleeper Analyst",
    tagline = "Name the faction on the Intel token. If correct: the attribution ends here.",
    type    = ModReactCard,  faction = Ghost,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1
    # Spec clarity: Information / Remove / IntelToken

    trigger = faction(opponent).places(PA, with=IntelToken(any), at=Art 03 §9.2.0),
    beat    = None,  # React — fires at Art 03 §9.2.0, not in initiative
    resolution = Prediction,  # Ghost declares faction named on token; ARBITER validates
    threshold  = None,
    ring_mod   = None,  doctrine_mod = None,  resolution_type = "Conditional",

    target_district = None,
    target_faction  = None,
    target_object   = IntelToken(on=target_PA),
    target_taxonomy = None,
    affinity    = None,
    restriction = None,
    cost        = None,  # card consumed on fire (success or misfire)

    success = (
        arbiter.remove(IntelToken, from=target_PA),
        arbiter.cancel(target_PA),   # flip face-down; drain all resource tokens to Reservoir
        faction(Ghost).standing.add(1),
    ),
    successcrit = None,
    fail        = None,   # card consumed; no board effect; PA proceeds normally
    failcrit    = None,
    on_accept   = None,  on_decline = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = None,  # pending 04-n79
    perspectives = None,  # pending D-04-08

    design_note  = "Counter-attribution React payoff for Ghost's intelligence chain. Fires when any faction places a PA with Intel token at Art 02 §9.2.0. Ghost announces React and declares the faction they believe is on the token. ARBITER checks (Prediction resolution). Match → token removed, PA cancelled (resources drained to Reservoir, no refund), Ghost +1 PS. No match → card consumed, PA proceeds. Intelligence-gated: Target Profile face-down at Art 03 §9.2.0 means Ghost cannot derive the target from visible information — requires prior SIGINT or Source Substitution plant mode. Works against corrupted and legitimate tokens alike — Ghost doctrine: no attribution belongs on the public record. card_id = GHO.MOD.1.",
    arbiter_note = "React at Art 03 §9.2.0 when opponent places any PA with an Intel token. Ghost announces React; states the faction they believe is named on the token's faction field. Pause Art 03 §9.2.0 declaration sequence. Check token faction field (do not reveal to table). If Ghost's declared faction matches token: React succeeds — remove token; flip PA face-down (cancelled); drain all resource tokens from PA card to Reservoir; Ghost +1 PS; resume Art 03 §9.2.0. If no match: React misfires — consume Sleeper Analyst card; no board effect; resume Art 03 §9.2.0; placed PA proceeds normally.",
)
```

---

### GHO.MOD.2 — PERIMETER SENSORS *(stub)*

*S128. Delivers §5a "passive generation: Intel tokens from game events near Ghost presence" as a ModReactCard. Output of 04-n143. Generic variant (faction=Any). Faction-targeted variants: GHO.MOD.3 (Directorate), GHO.MOD.4 (Network).*

```python
GHO.MOD.2 = Card(
    id      = "GHO.MOD.2",  card_id="GHO.MOD.2",  version="v0.1",
    name    = "Perimeter Sensors",
    tagline = "Faction activity near Ghost presence generates automatic intelligence.",
    type    = ModReactCard,  faction = Ghost,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    trigger         = presence_chip.placed(faction=Any, district=where(faction(Ghost).presence > 0)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    value_rating    = None,   # TBD

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Ghost).presence > 0,  # Ghost must be present in triggered district
    cost            = None,  # card consumed on fire

    success     = arbiter.deliver(faction(Ghost), IntelToken(faction=trigger.faction)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Ghost: PortraitEntry(submitter=+1)},
    narrative    = None,  # pending
    perspectives = None,  # pending
    design_note  = "Passive Intel generation from nearby faction activity. Trigger: any faction places presence in a Ghost-present district (publicly observable). Ghost receives 1 Intel token keyed to the placing faction. Intelligence-minimal design: Ghost learns who is expanding near its positions without taking any action. Output of 04-n143.",
    arbiter_note = None,  # TBD
)
```

---

### GHO.MOD.3 — INSTITUTIONAL TRACE *(stub)*

*S128. Faction-targeted variant of GHO.MOD.2. Trigger narrowed to Directorate presence placement. Directorate expansion near Ghost positions is the highest-value intelligence signal — institutional authority is Ghost's primary constraint.*

```python
GHO.MOD.3 = Card(
    id      = "GHO.MOD.3",  card_id="GHO.MOD.3",  version="v0.1",
    name    = "Institutional Trace",
    tagline = "Directorate expansion near Ghost presence generates targeted intelligence.",
    type    = ModReactCard,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    trigger         = presence_chip.placed(faction=Directorate, district=where(faction(Ghost).presence > 0)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = Directorate,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Ghost).presence > 0,
    cost            = None,

    success     = arbiter.deliver(faction(Ghost), IntelToken(faction=Directorate)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Ghost: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Directorate-targeted variant of GHO.MOD.2 (Perimeter Sensors). Same trigger/effect, faction-narrowed. Directorate expansion near Ghost positions is a high-priority intelligence signal — Directorate is Ghost's doctrinal suppressor. Narrower window than generic variant; more reliable in Directorate-heavy games.",
    arbiter_note = None,
)
```

---

### GHO.MOD.4 — SIGNAL BLEED *(stub)*

*S128. Faction-targeted variant of GHO.MOD.2. Trigger narrowed to Network presence placement. Network broadcast reach expanding into Ghost-present districts is an operational exposure risk.*

```python
GHO.MOD.4 = Card(
    id      = "GHO.MOD.4",  card_id="GHO.MOD.4",  version="v0.1",
    name    = "Signal Bleed",
    tagline = "Network expansion near Ghost presence generates exposure intelligence.",
    type    = ModReactCard,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    trigger         = presence_chip.placed(faction=Network, district=where(faction(Ghost).presence > 0)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = Network,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Ghost).presence > 0,
    cost            = None,

    success     = arbiter.deliver(faction(Ghost), IntelToken(faction=Network)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Ghost: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Network-targeted variant of GHO.MOD.2 (Perimeter Sensors). Network presence placement near Ghost positions generates Network-keyed Intel — Ghost tracks the broadcast infrastructure expanding into shared territory. Network expansion = exposure risk for Ghost covert ops in those districts.",
    arbiter_note = None,
)
```

---

### GHO.MOD.5 — FALSE FLAG *(stub)*

*React on positive PS shift. The "Flip" point-disruption payoff. Reverse the opponent's public narrative.*

```python
GHO.MOD.5 = Card(
    id      = "GHO.MOD.5",  card_id="GHO.MOD.5",  version="v0.1",
    name    = "False Flag",
    tagline = "Let them claim the victory, then rewrite the headline.",
    type    = ModReactCard,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    trigger         = public_standing.shifted(faction=Any, direction=Positive),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Ghost).findings * 1 + resource.faction(Ghost).exposure * 1,

    success     = arbiter.shift(public_standing, faction=trigger.faction, amount=-(trigger.amount * 2)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Late-game Flipped intel sink. Ghost spends the target's native resource to invert their public victory into a disaster. Since Reacts occur after the state change (the positive shift), this effectively applies a negative shift equal to double the trigger amount to achieve the inversion Cost reasoning: Exposure is expended to actively seed the manufactured narrative into the public consciousness.",
    arbiter_note = None,
)
```

---

### GHO.MOD.6 — SUPPLY CHAIN TAP *(stub)*

*React on resource generation. Precision economic disruption via mirrored draw.*

```python
GHO.MOD.6 = Card(
    id      = "GHO.MOD.6",  card_id="GHO.MOD.6",  version="v0.1",
    name    = "Supply Chain Tap",
    tagline = "Their infrastructure is our logistics.",
    type    = ModReactCard,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    trigger         = resource.drawn_from_reservoir(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = Resource(faction(trigger.faction).native, 1),

    success     = arbiter.deliver(faction(Ghost), trigger.resources),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Ghost pays 1 cross-faction resource to copy the entire resource draw of an opponent's Upkeep phase. Pure mirrored parasitic economy.",
    arbiter_note = None,
)
```

---

### GHO.MOD.7 — SLEEPER CELL *(stub)*

*React on Dominant marker placement. Point-disruption targeting end-game power spikes.*

```python
GHO.MOD.7 = Card(
    id      = "GHO.MOD.7",  card_id="GHO.MOD.7",  version="v0.1",
    name    = "Sleeper Cell",
    tagline = "Total control is just a convenient illusion.",
    type    = ModReactCard,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    trigger         = dominant_marker.placed(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Ghost).findings * 1 + resource.faction(Ghost).capacity * 1 + resource.faction(Ghost).capital * 1,

    success     = list([arbiter.remove(presence_chip, district=target_district, faction=target_faction, count=1), arbiter.place(presence_chip, district=target_district, faction=Ghost, count=1)]),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Reacts to a massive late-game state change. By physically swapping 1 of the target's chips for 1 Ghost chip, Ghost instantly drops the opponent's chip count, stripping the Dominant marker the moment it is placed and forcing them back to Established. Delays the endgame condition Cost reasoning: Requires Capacity to house the cell and Capital to fund their sudden activation, backed by precise intelligence.",
    arbiter_note = None,
)
```

---

### GHO.MOD.8 — LOCAL SYMPATHIZERS *(stub)*

*React on Established marker placement. Point-disruption targeting mid-game expansion.*

```python
GHO.MOD.8 = Card(
    id      = "GHO.MOD.8",  card_id="GHO.MOD.8",  version="v0.1",
    name    = "Local Sympathizers",
    tagline = "They thought this neighborhood belonged to them.",
    type    = ModReactCard,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    trigger         = established_marker.placed(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = Resource(faction(trigger.faction).native, 1),

    success     = arbiter.remove(presence_chip, district=target_district, faction=target_faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Reacts to a faction reaching IL-02 (Established). Ghost burns 1 cross-faction resource to immediately remove one of their chips, instantly downgrading them back to IL-01. Slows the table's structural expansion.",
    arbiter_note = None,
)
```

---

---

### GHO.MOD.9 — BURN NOTICE *(stub)*
[↑ Modifier & React Cards](#ghost-modifier-and-react-cards)

```python
GHO.MOD.9 = Card(
    id      = "GHO.MOD.9",  version = "v1.1",
    name    = "Burn Notice",
    tagline = "Incinerate an opponent's intelligence assets as they try to use them.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Submission,  function = Remove,  subject = ModifierCard,
    trigger = "public_act.submitted(uses_intel_token=True)",
    cost    = resource.faction(Ghost).findings * 1,
    success = "Remove all Modifier cards submitted with the target PA.",
    design_note = "Punishes factions trying to aggressively brute-force a PA using Intel Tokens."
)
```

---

### GHO.MOD.10 — DATA WIPE *(stub)*
[↑ Modifier & React Cards](#ghost-modifier-and-react-cards)

```python
GHO.MOD.10 = Card(
    id      = "GHO.MOD.10",  version = "v1.1",
    name    = "Data Wipe",
    tagline = "A devastating cyber-attack that cripples a faction's operational hand.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Remove,  subject = FactionHand,
    trigger = "public_act.submitted",
    cost    = resource.faction(Ghost).findings * 2 + intel_token * 1,
    success = "Target faction must discard their entire hand of unplayed CA and PA cards. (They will redraw normally at Debrief).",
    design_note = "Hugely disruptive. Clears their operational runway for the rest of the quarter."
)
```

---

### GHO.MOD.11 — MANUFACTURED EVIDENCE *(stub)*
[↑ Modifier & React Cards](#ghost-modifier-and-react-cards)

```python
GHO.MOD.11 = Card(
    id      = "GHO.MOD.11",  version = "v1.0",
    name    = "Manufactured Evidence",
    tagline = "Hijack a public act before the ink dries.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Corrupt,  subject = TargetProfile,
    trigger = "public_act.placed_with_target_profile",
    cost    = resource.faction(Ghost).findings * 1 + resource.faction(Ghost).exposure * 1,
    success = "Replaces the PA's original Target Profile with a new Target Profile provided by Ghost.",
    arbiter_note = "Reacts at Art 03 §9.2.0 when an opponent places a PA with a face-down Target Profile. Ghost announces the React, discards the opponent's original face-down Target Profile, and places their own face-down Target Profile on the PA. At Beat 4 Apex Check, the PA resolves against Ghost's corrupted targets.",
    design_note = "A public hijacking. The table sees Ghost swap the paperwork, but because Target Profiles are placed face-down, no one (not even the table) knows what Ghost changed the target to until Beat 4."
)
```


## Directorate
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#directorate-covert-operations) · [Public Acts](#directorate-public-acts)

---

### Directorate — Covert Operations
[↑ Directorate](#directorate)

| Card | Name |
|------|------|
| [DIR.CA.1](#c21-invoke-jurisdiction) | Invoke Jurisdiction |
| [DIR.CA.2](#c22-detain) | Detain |
| [STD.CA.11](#c23-tort-interference) | Tort Interference |
| [DIR.CA.3](#c24-surveillance-placement) | Surveillance Placement |
| [DIR.CA.4](#c25-tactical-redirection) | Tactical Redirection |
| [DIR.CA.5](#directorate-sanctioned-raid) | Sanctioned Raid |
| [DIR.CA.6](#dirca6--institutional-audit) | Institutional Audit |
| [DIR.CA.7](#dirca7--institutional-brief) | Institutional Brief |
| [DIR.CA.8](#dirca8--enhanced-scrutiny) | Enhanced Scrutiny |

### DIR.CA.1 — INVOKE JURISDICTION
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's positional authority card — asserts institutional control over a named district for a full round by blocking the two primary expansion actions (STD.CA.1 Build Structure, STD.CA.3 Campaign). Beat 2 Automatic positional wager: no dice, but the card slot is committed at Dispatch. No restriction means Invoke Jurisdiction can target any district, including ones where Directorate has no presence — the Directorate's authority is institutional, not territorial. Cost Mandate×2 reflects this as a mid-tier operational spend. The block is public (per game.block parameters), signaling to the table exactly which district is under oversight.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional authority assertion over a district — blocks primary expansion actions for one round; distinct from DIR.CA.4 (repositions own presence) and SYN.CA.5 (blocks named action type for a faction) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; no presence requirement — institutional authority is not territorial; Mandate×2 calibrated as mid-tier spend; block scope outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — jurisdictional authority is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Submission/Block/CovertOperation — beats Beat 2 Automatic; block applies to STD.CA.1 and STD.CA.3 in target district for one round | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic, blocks STD.CA.1+STD.CA.3 for one round — block scope calibration outstanding (Outstanding Issue) | Art 02 §6–§7 |
| Effect duration | ✓ | One round: block applies for round=game.round only | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 positional wager fires on STD.CA.1/STD.CA.3 submissions in target district | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; jurisdictional assertion aligns with institutional doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | No new components; game.block() is an existing Beat 2 mechanism | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 positional wager; game.block() applies at Beat 2 resolution; game.block resolution (resources on blocked card) outstanding (Outstanding Issue) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Block scope — STD.CA.1/STD.CA.3 only:** DIR.CA.1 blocks STD.CA.1 and STD.CA.3 explicitly. Confirm whether this should extend to STD.CA.4 (Demolition) or STD.CA.8 (Buy Influence) to reflect true jurisdictional authority, or remain limited to the two build/presence cards by design.
- **game.block resolution:** Confirm Beat 2 block mechanic — does a blocked STD.CA.1/STD.CA.3 cost the submitter their action slot and resources, or is it returned? Needs Art 03 §9.4 Beat 2 procedure to confirm.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
DIR.CA.1 = Card(
    id      = "DIR.CA.1",  version="v1.0",
    name    = "Invoke Jurisdiction",
    tagline = "Assert institutional authority over a target district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Submission,  function = Block,  subject = CovertOperation,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any, target_faction=None, target_object=CovertOperation,
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).mandate * 2,
    success     = game.block(district(target), cards=[STD.CA.1, STD.CA.3], round=game.round, public=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate was here before the other factions arrived. Their jurisdictional authority is not theoretical.",
    perspectives = {Directorate: "This district is under institutional oversight. Expansion requires authorisation. Authorisation has not been granted."},
    design_note  = None,
    arbiter_note = None,
)
```

---

### DIR.CA.2 — DETAIN
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's permanent removal card — eliminates a faction's deployment marker from a district, permanently. The strongest single-target suppression in the Directorate set. Distinct from STD.CA.4 Demolition (removes structure blocks) and DIR.CA.4 Tactical Redirection (moves own presence): Detain removes an opponent's operational anchor. Intel restriction (fresh token required) forces Directorate to have gathered intelligence before arresting — doctrine-consistent and a resource cost beyond the Mandate spend. Successcrit returns +3 Mandate, rewarding efficient institutional execution. Failcrit −1 PS reflects the institutional embarrassment of a failed detention. ChorusNode exclusion reflects ARBITER's deployment marker's special status.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Permanent deployment marker removal — Directorate's strongest single-target suppression; distinct from STD.CA.4 (removes structures) and DIR.CA.4 (repositions own presence); Intel restriction enforces doctrine | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design — detention as institutional process | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Intel token restriction forces prior intelligence collection; ChorusNode exclusion respects ARBITER marker's special status; L183 Detention zone on Directorate public tableau | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — permanent removal is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Move/DeploymentMarker — marker moved to Detention zone (Governing Rule 8.3a compliant); function corrected S107 L226 (Remove → Move; success block uses game.move(), not game.remove()) | Art 04b §4, §5 |
| Balance | ✓ | Mandate×3, threshold 50, permanent removal — highest Directorate covert cost; successcrit Mandate recovery outstanding (Outstanding Issue) | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent: marker remains in Detention for remainder of session | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; failcrit −1 PS is game effect (not portrait), confirmed per DIR.PA.2 | Art 04 §6.2; Art 02 §11 |
| Supported by zones | ✓ | target_district = district.any; ChorusNode.deployment_marker excluded; Detention zone on Directorate public tableau (L183) | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken restriction; DeploymentMarker target; Detention zone is faction Terminal zone per L183; Intel age definition outstanding (Outstanding Issue) | Art 02 §6–§8; Art 02 §11 |
| Supported by game procedure | ✓ | Beat 3 d100 resolution; Intel check at Dispatch; ARBITER moves marker to Detention; visible to all players; no NotificationSlip needed | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Intel token age interpretation:** `intel(faction=faction(target), age_rounds<=1)` — confirm "age_rounds<=1" means Fresh token (gathered this or last round) per Art 02 §12 aging definitions.
- **Successcrit Mandate recovery:** +3 Mandate on crit success is the highest reward in the Directorate set — confirm this is intentional given Mandate×3 base cost (net zero, but only on crit).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
DIR.CA.2 = Card(
    id      = "DIR.CA.2",  version="v1.0",
    name    = "Detain",
    tagline = "Permanently remove a faction's deployment marker from a district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Move,  subject = DeploymentMarker,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10},
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any, target_faction=faction(named_opponent), target_object=DeploymentMarker,
    target_taxonomy=None,
    affinity=None,
    restriction = (
        district(target).faction(target).deployment_marker >= 1
        AND intel(faction=faction(target), age_rounds<=1) >= 1
        AND district(target) != ChorusNode.deployment_marker
    ),
    cost        = resource.faction(acting).mandate * 2 + resource.faction(acting).findings * 1,
    success     = game.move(faction(target).deployment_marker, from_=district(target), to=Directorate.tableau.detention, public=True),
    successcrit = resource.faction(acting).mandate += 3,
    fail=None,
    failcrit    = faction(acting).standing -= 1,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate does not destroy — it detains. The distinction matters to them.",
    perspectives = {Directorate: "The marker has been detained. Its conversion will not occur."},
    design_note  = "L183. Marker moved to Directorate public tableau Detention zone — Governing Rule 8.3a compliant (moved, not removed from play). Permanent: marker remains in Detention for remainder of session. No NotificationSlip — detention is publicly visible on Directorate tableau. Faction Terminals may be unique per faction (L183) Cost reasoning: Requires Capital to grease the bureaucratic wheels while Mandate provides the authority.",
    arbiter_note = "Consume Intel token. Move named faction's deployment marker from target district to Directorate public tableau Detention zone. Physically place on Detention area — visible to all players. No separate notification. Crit success: return 3 Mandate to Directorate. Crit fail: no marker move; −1 PS to Directorate only.",
)
```

---


### DIR.CA.3 — SURVEILLANCE PLACEMENT
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's active surveillance card — dedicates operational resources to watch a named district this month. Resolves at Beat 2: ARBITER checks the Beat 3 resolution grid for submitted ops targeting that district and delivers an IntelDeliverySlip (op type only, no faction) to Directorate before Beat 3 fires. If no ops target the district, nothing is delivered and resources are spent. Distinct from STD.CA.5 Gather (generates an Intel token about a named faction) and GHO.CA.2 Intercept (targets a named faction's op and disrupts it): DIR.CA.3 watches territory, not actors. Op type only — no faction identity delivered; Directorate learns what is happening in the district, not who is doing it.

Episodic by design: no board marker exists (any covert placement would be public per Governing Rule 7.2a); surveillance cannot persist. Directorate must play the card to surveil. Multiple deck copies flagged for deck design pass (04-n42, 04-n43).

Redesigned S68: original model was permanent passive feed with beat3_pre_resolution delivery — invalidated (Governing Rule 7.2a prohibits covert board markers; ARBITER holds no log in L1 paper game).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Active district surveillance — watches territory this month; distinct from STD.CA.5 (faction-targeted token) and GHO.CA.2 (faction-targeted disruption) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — institutional monitoring doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; no presence requirement; Mandate×2 for intelligence without dice risk; Beat 2 blind commitment (resources spent before knowing if ops are in flight) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information / Reveal / CovertOperation — district-scoped; subject = submitted op type(s) in target district | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic, Beat 2 — no dice risk; blind commitment is the cost; empty district = nothing delivered | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — IntelDeliverySlip delivered once at Beat 2 resolution; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at Beat 2; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — institutional monitoring doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | IntelDeliverySlip (IS-xx) — Art 02 component entry pending (04-n45); 00b definition update pending (04-n46) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; ARBITER reads existing Beat 3 grid row — no new tracking required; Art 03 Beat 2 procedure addition pending (04-n44) | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Art 03 Beat 2 procedure:** Beat 2 section does not yet include district-surveillance IntelDeliverySlip delivery. Procedure addition required before Issues Resolved (04-n44). Gates Art 03 re-sign-off.
- **Art 02 component entry:** IntelDeliverySlip has no design entry in Art 02. Addition required before Issues Resolved (04-n45). Gates Art 02 re-sign-off.
- **00b IS-xx definition:** IS-xx definition covers Beat 3 delivery only. Update required to include Beat 2 delivery pattern (04-n46). Gates 00b re-sign-off.
- **Card name:** "Placement" implies permanent installation — consider rename (e.g., "Surveillance Order," "District Watch") during naming pass.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Redesigned S68 v2.0 — episodic Beat 2 model. Blocking open issues: 04-n44 (Art 03), 04-n45 (Art 02), 04-n46 (00b).*

```python
DIR.CA.3 = Card(
    id      = "DIR.CA.3", version="v2.0",
    name    = "Surveillance Placement",
    tagline = "Watch a named district — learn what has been submitted before it resolves.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Directorate,
    layer   = Information, function = Reveal, subject = CovertOperation,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any, target_faction=None, target_object=None,
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).mandate * 2,
    success     = game.deliver(IntelDeliverySlip(district=district(target), content="op_type_only", source="beat3_grid"), to=faction(acting), private=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate monitors because monitoring is their primary tool for managing what they cannot directly control.",
    perspectives = {Directorate: "We know what moves through that district before it moves. We will respond accordingly."},
    design_note  = "Redesigned S68 v2.0: original permanent passive feed with beat3_pre_resolution delivery invalidated — Governing Rule 7.2a prohibits covert board markers; ARBITER holds no log in L1. Episodic model: Directorate watches one district one month. ARBITER reads existing Beat 3 grid row at Beat 2 resolution — no new tracking. Op type only, no faction. Multiple copies in Directorate deck flagged for deck design pass (04-n42).",
    arbiter_note = "During Beat 2 resolution of this card: check the Beat 3 resolution grid for covert operations targeting district(target). For each operation present, write the operation type on an IntelDeliverySlip and deliver privately to Directorate. Do not include faction identity. If no Beat 3 operations target the district, deliver nothing — Directorate's resources are spent. Procedure pending Art 03 Beat 2 addition (04-n44).",
)
```

---

### DIR.CA.4 — TACTICAL REDIRECTION
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's repositioning card — the only card in the full set using Territory — Move — PresenceToken (Beat 2, Automatic). Designed to fill the gap identified in S51 when DIR.CA.4 Sealed Border was retired. Where most Directorate cards act on opponents, Tactical Redirection acts on Directorate's own presence, moving up to 2 tokens between adjacent districts before Beat 3 outcomes are applied. Beat 2 Automatic makes it a proactive positional adjustment — Directorate anticipates the round's contested districts and pre-positions before dice are rolled. ChorusNode exclusion (both source and destination) prevents repositioning through the central Chorus district. Mandate×2 is a mid-tier cost.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Proactive repositioning — moves up to 2 presence tokens between adjacent districts before Beat 3; fills Territory/Move/PresenceToken gap; only card in full set with this verb+subject at Beat 2 | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design — tactical pre-positioning as institutional doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Beat 2 Automatic — proactive, not reactive; ChorusNode exclusion; entry qualification outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — institutional pre-positioning is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Move/PresenceToken — unique taxonomy slot in full card set; Move function correct for same-faction repositioning | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic, moves count=2 — move count vs. restriction outstanding (Outstanding Issue) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: tokens moved at Beat 2 resolution; control flags recalculated post-move | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 positional wager fires on submission | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; repositioning aligns with tactical doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | source and target both district.named; adjacency enforced in restriction; ChorusNode excluded from both | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken in restriction and as target; Mandate cost; adjacency per district_adjacency table | Art 02 §6; Art 02 §8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; tokens moved before Beat 3 resolution; entry qualification and move count resolution outstanding (Outstanding Issues) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Entry qualification check:** `arbiter_note` states that if Directorate does not qualify for entry at the destination, the card is discarded without effect (resources not refunded). Confirm "qualify for entry" criteria — is there a district-entry restriction in Art 01 or Art 03?
- **Move count vs. restriction:** Restriction requires source.presence >= 1 but the card moves count=2. Can the card be played if source has only 1 token (moving fewer than 2)? Confirm whether count=2 is a maximum or exact.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*S51 redesign — design rationale scaffold added S59. Design pass pending.*

```python
DIR.CA.4 = Card(
    id      = "DIR.CA.4",  version="v1.0",
    name    = "Tactical Redirection",
    tagline = "Reposition institutional presence ahead of a contested exchange.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Move,  subject = PresenceToken,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.adjacent(source), target_faction=faction(acting), target_object=PresenceToken,
    target_taxonomy=None,
    affinity=None,
    restriction = (
        district(source).faction(acting).presence >= 1
        AND district(source).is_adjacent(district(target))
        AND district(source) != ChorusNode
        AND district(target) != ChorusNode
    ),
    cost        = resource.faction(acting).mandate * 2,
    success     = game.move(faction(acting).presence, count=2, from_=district(source), to=district(target)),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "Institutional authority is not static. The Directorate repositions before others recognize the shift.",
    perspectives = {Directorate: "Our presence is where it needs to be. This was always the plan. The redistribution was anticipated."},
    design_note  = "Replaces DIR.CA.4 Sealed Border (retired S51). Fills Territory — Move — Presence token gap; no other card in the full set uses this verb + subject combination. Most impactful before Battlefield Strength when district control margins are tight.",
    arbiter_note = "Move named Directorate presence tokens from source to destination. Adjacency confirmed against district adjacency table. Entry requirements rechecked at destination — if Directorate does not qualify for entry, card is discarded without effect (resources not refunded). Control flags and Established markers recalculated after move.",
)
```

---

### Directorate — REGULATORY DOWNGRADE 🚫 BLOCKED
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's active tier suppression play — declared publicly at Phase B, resolved at Beat 4. The card stays on the Overview as the persistent condition: no separate marker component needed. Target faction collects resources in the named district as one tier lower (resource generation only; actual presence count still governs control tier for win-condition calculations). Cleared when target pays 2 native to Reservoir — available any time after Beat 4 resolution, including immediately. Economics: clearing same Quarter costs the target 2 native (net 3 from a full Core+structure district). Each Upkeep with the card active costs −1 resource generation plus the eventual 2 to clear. Directorate spent 3 Mandate for a guaranteed minimum 2-resource drain; compounding if target delays. Paired with Regulatory Freeze: Downgrade is the active suppression play once a faction is entrenched; Freeze is the cheaper preventive play to gate lower-tier factions out of advancement.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public institutional reclassification — declared openly, contested in Countermeasure window, persistent economic suppression | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — reclassification as institutional act | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; target must be Established+; public act fits regulatory authority doctrine — the Directorate does not act in secret when it reclassifies | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) — institutional reclassification is public, permanent, and Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Modify/InfluenceTier — card on board IS the condition; no separate component needed | Art 04b §4, §5 |
| Balance | ✓ | Mandate×3, Automatic; guaranteed economic suppression; minimum 2-native drain on target; compounding cost per Upkeep delayed | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent — card stays on Overview until persistence_condition met | — |
| Persistence | ✓ | Permanent public act; `persistence_condition` = target pays 2 native to Reservoir; card removed on payment | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — reclassification aligns with regulatory authority doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — card on Overview is the persistent condition | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Phase B declaration → Countermeasure window → Beat 4 Automatic resolution; standard Permanent Public Act lifecycle | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Win-condition scope:** Resource generation tier penalty only — actual presence count governs control tier for Dominance/Established win-condition calculations. Needs explicit statement in Art 03 Upkeep Step 5 procedure or Art 07 reference. Tracks under 04-n27.
- **Freeze interaction:** If Downgrade and Freeze are both active on the same faction/district simultaneously, combined effect is: one tier down for resource gen + blocked from tier advancement. Needs explicit procedure note confirming coexistence is valid and no additional interaction applies.
- **🚫 BLOCKED (S107, L223):** Two permanent constraints. (1) InfluenceTier is derived state (calculated from token counts), not a placed component — it cannot be directly targeted by a card. (2) GR 9.1 prohibits direct income modification by card. Both are permanent. Fundamental redesign required: income suppression must work through board state — Territory|Remove|PresenceToken is the valid path (token removal reduces tier, which reduces income naturally). Cross-ref: Art 04b §8.2 item 4, PM05 04-n104.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | 🚫 BLOCKED | — | — |

*Redesigned S67 — v2.0. CovertOperation → PublicAct. TierPenaltyMarker removed; card-as-condition pattern.*

```python
RegulatoryDowngrade = Card(
    id      = "DIR.PA.4",  version="v2.0",
    name    = "Regulatory Downgrade",
    tagline = "Reclassify a faction's standing in a district. They generate resources as if one tier lower until they pay to clear it.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer   = Territory,  function = Modify,  subject = InfluenceTier,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Permanent public act",
    outcome_type    = None,
    persistence     = Permanent,
    persistence_condition = faction(target).pays(2, resource.native, to=Reservoir),
    persistence_effect    = game.board_condition(
                                scope  = district(target) + faction(target),
                                effect = resource_gen.tier_effective -= 1,
                            ),

    target_district = district.named,
    target_faction  = faction(named_opponent),
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(target).influence_tier(district(target)) >= Established,
    cost        = resource.faction(acting).mandate * 1 + resource.faction(acting).exposure * 1 + resource.faction(acting).capital * 1,

    success     = None,
    successcrit = None,

    portrait    = {Directorate: PortraitEntry(submitter=+1)},

    narrative    = "The Directorate does not need to remove them. It need only redefine what they are.",
    perspectives = {Directorate: "The reclassification stands. Their tier in this district now reflects our assessment, not their aspirations."},

    design_note  = "Card placed in Directorate play area (public, face-up) — no TierPenaltyMarker. Card IS the persistent condition. Resource generation only; presence count unchanged. Clearing: target pays 2 native to Reservoir, any time after Beat 4 resolution. Economics: clear same Quarter = net 3; each Upkeep active = −1 gen then pay 2. Paired with Regulatory Freeze for full suppression toolkit.",
    arbiter_note = "Per Permanent Public Act procedure: card placed in Directorate play area at Beat 4 (public, face-up; target district and faction declared). At each Upkeep Step 5: apply one-tier reduction to resource generation for faction(target) in district(target). Win-condition tier (Dominance/Established) uses actual presence count — do not apply penalty to control calculations. Clearing: when faction(target) pays 2 native to Reservoir (any time after Beat 4), remove card and announce.",
)
```

---

### Directorate — REGULATORY FREEZE 🚫 BLOCKED
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Preventive tier suppression — lighter than Regulatory Downgrade but cheaper. Where Downgrade reduces an existing tier, Freeze prevents advancement from the current tier. Cost Mandate×2 and Automatic resolution reflect that issuing a regulatory ceiling is a procedural act, not a contested operation. No ring_mod — administrative acts carry the same institutional weight anywhere in New Meridian. Clearing is deliberately cheaper than Downgrade (1 native vs 2) because a ceiling is a future constraint, not a reclassification of existing status. Card-as-condition pattern: the card placed in the Directorate play area is the persistent condition; no separate marker component needed. Enforcement per Governing Rule 6.1a: Directorate monitors, calls violations, ARBITER adjudicates and reverses. Paired with Regulatory Downgrade for full suppression toolkit.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Preventive tier suppression — cheaper alternative to Regulatory Downgrade; blocks advancement from current tier; card-as-condition pattern | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design — administrative tier ceiling as institutional act | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Mandate×2, Automatic; no ring_mod consistent with administrative nature; no restriction on target tier | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) — institutional act must be on record to be binding; consistent with Regulatory Downgrade | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Block/InfluenceTier — blocks tier advancement; card IS the persistent condition | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic — 1-Mandate cheaper than Downgrade; clearing 1 native vs Downgrade 2 native is intentional (ceiling vs reclassification) | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent — card stays on Overview until persistence_condition met | — |
| Persistence | ✓ | Permanent public act; card on board IS the condition; self-policing per Governing Rule 6.1a | Art 04 §6; Governing Rule 6.1a |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; tier ceiling aligns with regulatory authority doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — standard zone targeting | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — card on Overview is the persistent condition | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Phase B declaration → Countermeasure window → Beat 4 Automatic; standard Permanent Public Act lifecycle; Downgrade/Freeze coexistence = one tier down for gen + blocked advancement, no additional interaction | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **🚫 BLOCKED (S107, L223):** Two permanent constraints. (1) InfluenceTier is derived state (not a placed component) — Block function targets actions, not derived states; Block|InfluenceTier is a subject mismatch. (2) Same subject violation as Regulatory Downgrade: InfluenceTier is not a targetable component. Fundamental redesign required. Redesign pair with Regulatory Downgrade — both address income suppression intent through board state manipulation. Cross-ref: Art 04b §8.2 item 4, PM05 04-n104.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | 🚫 BLOCKED | — | — |

*Redesigned S67 — v2.0. CovertOperation → PublicAct. TierFreezeMarker removed; card-as-condition pattern. Self-policing per Governing Rule 6.1a.*

```python
RegulatoryFreeze = Card(
    id      = "DIR.PA.5",  version="v2.0",
    name    = "Regulatory Freeze",
    tagline = "Establish a tier ceiling in a target district. Target cannot advance beyond their current standing until they pay to lift it.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer   = Territory,  function = Block,  subject = InfluenceTier,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Permanent public act",
    outcome_type    = None,
    persistence     = Permanent,
    persistence_condition = (
        faction(target).pays(1, resource.native, to=Reservoir) OR
        faction(target).influence_tier(district(target)) == Absent
    ),
    persistence_effect = tier_advancement.blocked(
        above = faction(target).influence_tier(district(target)).at_resolution
    ),

    target_district = district.named,
    target_faction  = faction(named_opponent),
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).mandate * 2,

    success     = None,
    successcrit = None,

    portrait    = {Directorate: PortraitEntry(submitter=+1)},

    narrative    = "Forward progress in this district has been administratively paused. The Directorate is still reviewing.",
    perspectives = {Directorate: "They can build all they want. The tier ceiling is established. They will not pass through it."},

    design_note  = "Card placed in Directorate play area (public, face-up) — card IS the persistent condition. Tier cap = target's tier at Beat 4 resolution. Enforcement per Governing Rule 6.1a: Directorate monitors tier advancement attempts; on called violation, ARBITER reverses the placement and returns tokens to supply. Clearing: target pays 1 native to Reservoir (any time after Beat 4) OR target reaches Absent in district — remove card and announce. No restriction on target tier — playing against a Dominant faction is a legal but wasted play. Paired with Regulatory Downgrade for full suppression toolkit.",
)
```

---

### Directorate — SANCTIONED RAID
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's maximum-force territorial removal card. The Intel token is the authorization document; faction + native resource is the operational cost. Cannot bypass countermeasures — clears target faction's modifier cards at the district before removing presence tokens. Scales via boost: each additional unit of faction + native submitted at Phase B removes one more presence token and deepens the threshold (harder to relocate more people in a single op). PS scales symmetrically with n — forced relocation creates resentment proportional to scale; a clean large-scale op generates proportional public support. Distinct from DIR.CA.2 Detain (deployment marker, permanent) and STD.CA.4 Undermine (one token, standard, no Intel gate).

#### Card Story
The Directorate dispatches a team to the district — no announcement, no negotiation. The intel token is the authorization document; the operation runs exactly as filed. When the team leaves, the target faction has fewer people there than it did this morning. Whether the public calls it a cleanup or a crackdown depends entirely on how cleanly it was done.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Scaled-force removal via boost; target faction modifier card clear; PS scales with n in both directions | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — sanctioned institutional action | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Intel gate enforces intelligence-first doctrine; threshold = 65−10n; PS risk/reward scales with ambition | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Remove/PresenceToken — (1 + BM-xx) tokens removed at Beat 3 | Art 04b §4, §5 |
| Card narrative | ✓ | Intel-authorized team clears district; public verdict (PS) scales with scope and execution quality | Art 04 §5 P26 |
| Balance | ⚠ | Boost scaling adds new cost/PS curve — playtesting required | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent: (1 + BM-xx) presence tokens removed; target faction modifier cards cleared | — |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter; PS effects are game effects (not portrait) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named | Art 01 §6–§7 |
| Supported by components | ⚠ | BM-xx not yet registered — gate: 04-n81 | Art 02 §6; Art 02 §11–§12 |
| Supported by game procedure | ⚠ | Beat 0 boost detection (04-n82); Beat 2/3 BM-xx resolution (04-n83); Discovery definition (04-n84) — all gate sign-off | Art 03 §9, §11 |
| Data schema validation | ✓ | boost field present; threshold-scaling noted in §6.3; affinity corrected to None (04-n70) | Art 04 §6.1–§6.3 |

#### Outstanding Issues

- **IntelToken as restriction:** Should IntelToken(faction=faction(target)) also appear as `restriction =` (card unplayable without it in hand) in addition to appearing in cost? Or is cost placement sufficient? Carry.
- **Intel token faction-keying:** Confirm faction-keyed to target is correct (vs. any held token of the type).
- **Sign-off gates:** 04-n81 (BM-xx registration), 04-n82 (Beat 0 boost procedure), 04-n83 (Beat 2/3 BM-xx resolution), 04-n84 (Discovery mechanic definition).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*v2.2 — S79: boost model replaces Phase B n-declaration; base cost = faction×1 + native×1 + IntelToken (Mandate×2 removed); boost = same unit; threshold = 65−10×n_boost; PS scales with (1+n) in both directions; successcrit = PS+(1+n_boost) (public endorsement of clean large-scale op); fail = NotificationSlip; failcrit = Discovery + PS−(1+n_boost); modifier scope = target faction only; 04-n81/82/83/84 gate sign-off.*

```python
DIR.CA.5 = Card(
    id      = "DIR.CA.5",  version="v2.2",
    name    = "Sanctioned Raid",
    tagline = "Not every operation leaves a paper trail.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Remove,  subject = PresenceToken,
    beat=3, resolution=d100,
    threshold = 65 - (10 * n_boost),  # n_boost = BM-xx count; locked at Beat 0
    ring_mod  = {0:-15, 1:-10, 2:0, 3:+10},
    doctrine_mod = None,
    trigger   = None,
    resolution_type = "Probabilistic", outcome_type = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district = district.named, target_faction = faction(named_opponent), target_object = PresenceToken,
    target_taxonomy=None,
    affinity  = None,
    restriction = None,
    cost      = resource.faction(acting) * 1
              + resource.district(native) * 1
              + IntelToken(faction=faction(target)) * 1,
    boost     = True: resource.faction(acting) * 1 + resource.district(native) * 1,
    success   = [game.remove_modifier_cards(district(target_district), faction=faction(target)),
                 game.remove(faction(target).presence_tokens, district(target_district), count=(1 + n_boost)),
                 faction(acting).standing -= (1 + n_boost)],
    successcrit = faction(acting).standing += (1 + n_boost),
    fail      = game.dispatch(faction(target), NotificationSlip),
    failcrit  = [Discovery, faction(acting).standing -= (1 + n_boost)],
    portrait  = {Directorate: PortraitEntry(submitter=+1)},
    narrative = "The Directorate does not ask permission. It records the action and moves on.",
    perspectives = {Directorate: "The intelligence warranted the action. The action was authorised. There is nothing further to say."},
    design_note  = "Boost model: base cost (faction×1 + native×1 + IntelToken) covers removal of 1 token (threshold 65). Each boost unit = 1 BM-xx = 1 additional token removed, threshold −10. PS scales symmetrically with (1+n): success = −(1+n), successcrit = +(1+n), failcrit = Discovery + −(1+n). Modifier clear = target faction's cards only. See 04-n13: Network modifier card auto-triggers off Directorate sweep.",
    arbiter_note = "Beat 0: (1) validate base cost paid; (2) n_boost = excess payment ÷ (faction×1+native×1); (3) place n_boost BM-xx on grid slot; (4) lock threshold = 65−10×n_boost; (5) confirm faction(target) has ≥ (1+n_boost) presence tokens at district — reject if not. Beat 3 success: remove target faction's modifier cards from district; remove (1+n_boost) presence tokens from faction(target); Directorate PS −(1+n_boost); remove BM-xx to supply. Crit success: PS +(1+n_boost) instead of −(1+n_boost). Fail: dispatch NotificationSlip to target. Crit fail: Discovery (Art 03 §9.4 Step 7b.i — 04-n84 pending definition); Directorate PS −(1+n_boost).",
)
```

---

### DIR.CA.6 — INSTITUTIONAL AUDIT
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's institutional resource-generation card — fills the Economy gap left when DIR.CA.4 Tactical Redirection replaced the prior Economy vehicle. The audit targets a district where Directorate has meaningful operational footprint (chip count > 1), and counts active Directorate Permanent cards whose target district is in the same ring. Each unchallenged standing directive in the ring represents continued compliance with institutional authority; the audit converts that compliance record into Mandate. No floor: 0 active Permanents in the target ring yields 0 Mandate on success — the card is only worth submitting when Permanents are in play. Pairs with DIR.CA.7 Institutional Brief (same counting mechanism, PS yield).

#### Card Story
An internal team works through the standing record. Active directives in this ring are in force. Active restrictions are being observed. The documentation is clean. The budget allocation goes through.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional resource generation — fills Economy gap in Directorate set; yield scales with maintained standing authority in ring | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — institutional allocation as procedural validation | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; chip count > 1 restriction requires operational footprint; no floor enforces genuine Permanent investment before yield is meaningful | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — internal budget allocation is not a public declaration | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy / Add / NativeResource — Mandate generation through institutional validation | Art 04b §4 |
| Balance | ⚠ | Yield scales 0–N with active Permanents; Mandate×1 cost is low — may be generous if Permanents accumulate; playtesting required | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — Mandate added once at Beat 3 resolution | — |
| Persistence | ✓ | Immediate — no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — institutional allocation aligns with authority doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; restriction = chip count > 1 | Art 01 §6–§7 |
| Supported by components | ✓ | Counts face-up Directorate Permanent cards in Directorate play area — no new component | Art 02 §6–§8 |
| Supported by game procedure | ✓ | ARBITER reads board state (face-up Permanents in play area, target ring match) — existing permanent card procedure | Art 03 §9 |
| Data schema validation | ✓ | Fields consistent with §6.1–§6.3 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Internal audit — standing record clean, allocation approved | Art 04 §5 P26 |

#### Outstanding Issues

- **DB registration:** New card — requires id assignment in card_ref and component_metadata.
- **game.active_permanents() scope:** Confirm counting mechanism is unambiguous in paper play — ARBITER reads face-up Directorate Permanent cards from Directorate play area where card's target_district.ring == district(target).ring.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*New card — S106. Fills Economy|Add|NativeResource gap (04b §8.2 HP).*

```python
DIR.CA.6 = Card(
    id      = "DIR.CA.6", version="v1.0",
    name    = "Institutional Audit",
    tagline = "Review the standing record. Active directives in this ring generate institutional capital.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Directorate,
    layer   = Economy, function = Add, subject = NativeResource,
    beat=3, resolution=d100, threshold=50,
    ring_mod=None, doctrine_mod=None, trigger=None,
    outcome_type=None,
    persistence=Immediate, persistence_condition=None, persistence_effect=None,
    target_district = district.named,
    target_faction=None, target_object=None, target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).presence_count(district(target)) > 1,
    cost    = resource.faction(acting).mandate * 1,
    success = resource.faction(acting).mandate.add(
                count(game.active_permanents(faction=acting,
                      ring=district(target).ring))),
    successcrit = resource.faction(acting).mandate.add(1),
    fail        = None,
    failcrit    = resource.faction(acting).mandate.remove(1),
    on_accept=None, on_decline=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate does not improvise. The allocation exists because the framework exists. The framework is intact. The allocation is approved.",
    perspectives = {Directorate: "The standing record in this ring is clean. What was ordered is being carried out. Resources are allocated accordingly."},
    design_note  = "No floor — 0 active Permanents in target ring yields 0 Mandate on success. Count: face-up Directorate Permanent cards in Directorate play area where card.target_district.ring == district(target).ring. Pairs with DIR.CA.7 (same mechanism, PS yield).",
    arbiter_note = "Beat 3: count face-up Directorate Permanent cards in Directorate play area whose target district is in the same ring as district(target). Add that count in Mandate to Directorate supply. Successcrit: +1 Mandate additional. Failcrit: remove 1 Mandate from Directorate supply.",
)
```

---

### DIR.CA.7 — INSTITUTIONAL BRIEF
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's covert Standing card — fills the Standing|Shift gap identified in Art 04b §8.2. The mechanism is grounded in the same architecture as DIR.CA.6: target a district with operational footprint, count active Permanents in that ring, yield scales accordingly. The covert operation circulates the institutional record from the target ring through closed channels — demonstrated compliance with active directives creates a public confidence signal without disclosing authorship. The public receives the signal (stability, competence, maintained order) without knowing the Directorate arranged it. This resolves the PS legitimacy question: the mechanism is covert; the outcome enters public perception through the channels the Permanents already occupy. PS yield = 0 if no Permanents active in ring — players should verify ring Permanent count before submitting.

#### Card Story
Before any version of events could circulate, the Directorate's closed channels had already carried a different one. Active directives in this ring, maintained restrictions, a clean procedural record. The population receives signals they cannot source. The public confidence reading improves.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert PS generation — mechanism is hidden authorship of a public signal; distinct from Network PS cards (mass broadcast vs. closed-channel institutional record) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — institutional credibility through demonstrated record, not claimed reputation | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; chip count > 1 restriction; covert type consistent with undisclosed authorship | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — mechanism is covert; effect is public | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding — upward PS shift; target = acting faction | Art 04b §4 |
| Balance | ⚠ | PS yield scales with Permanents — same risk as DIR.CA.6 if Permanents accumulate; Mandate×2 cost higher than CA.6 to reflect PS vs. resource asymmetry | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — PS marker moved once at Beat 3 resolution | — |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; restriction = chip count > 1 | Art 01 §6–§7 |
| Supported by components | ✓ | PS marker (existing); no new component | Art 02 §11–§12 |
| Supported by game procedure | ✓ | PS movement by ARBITER at Beat 3 resolution — existing procedure | Art 03 §9 |
| Data schema validation | ✓ | Fields consistent with §6.1–§6.3 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Closed-channel record circulation; public confidence signal without disclosed authorship | Art 04 §5 P26 |

#### Outstanding Issues

- **DB registration:** New card — requires id assignment.
- **Failcrit narrative:** PS−1 represents the brief being traced back to Directorate — confirm this holds as an institutional embarrassment consequence (vs. a larger penalty).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*New card — S106. Fills Standing|Shift|PublicStanding gap (04b §8.2 HP). Narrative grounding: covert mechanism, public outcome via closed-channel circulation of institutional record.*

```python
DIR.CA.7 = Card(
    id      = "DIR.CA.7", version="v1.0",
    name    = "Institutional Brief",
    tagline = "Circulate the standing record through closed channels. Demonstrated authority in this ring builds public confidence.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Directorate,
    layer   = Standing, function = Shift, subject = StandingMarker,
    beat=3, resolution=d100, threshold=50,
    ring_mod=None, doctrine_mod=None, trigger=None,
    outcome_type=None,
    persistence=Immediate, persistence_condition=None, persistence_effect=None,
    target_district = district.named,
    target_faction=None, target_object=None, target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).presence_count(district(target)) > 1,
    cost    = resource.faction(acting).mandate * 2,
    success = faction(acting).standing.add(
                count(game.active_permanents(faction=acting,
                      ring=district(target).ring))),
    successcrit = faction(acting).standing.add(1),
    fail        = None,
    failcrit    = faction(acting).standing.remove(1),
    on_accept=None, on_decline=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate does not announce competence. It demonstrates it — quietly, through the record, through the channels that matter. The public receives the signal without knowing its source.",
    perspectives = {Directorate: "The active directives in this ring speak for themselves. We are not making a claim. We are presenting a record."},
    design_note  = "PS yield = count of active Directorate Permanents in same ring as target district. 0 Permanents → +0 PS on success. Same counting mechanism as DIR.CA.6 (Mandate yield). Failcrit PS−1: brief traced to Directorate — institutional embarrassment.",
    arbiter_note = "Beat 3: count face-up Directorate Permanent cards in Directorate play area whose target district is in the same ring as district(target). Move Directorate PS marker up by that count. Successcrit: +1 PS additional. Failcrit: move PS marker down 1.",
)
```

---

### DIR.CA.8 — ENHANCED SCRUTINY
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's difficulty-suppression card — a district-wide threshold penalty applied before Beat 3 resolves. Distinct from DIR.CA.1 Invoke Jurisdiction (blocks specific card types at Beat 2) and STD.CA.10 Protect (shields acting faction's assets only): Enhanced Scrutiny raises the operational cost for everyone in the district, including Directorate. That inclusion is doctrine-consistent — the Directorate accepts its own operational friction in exchange for universal suppression; scrutiny that has exceptions means nothing. Mechanism uses existing Modifier tokens placed by ARBITER on each Beat 3 row targeting the district at Beat 2 resolution. No new component needed. Beat 2 Directorate ops in the district (DIR.CA.1, DIR.CA.3, DIR.CA.4) are unaffected — only Beat 3 ops take the −15.

#### Card Story
The district is under enhanced institutional review. Documentation requirements are elevated. Checkpoint procedures are doubled. The Directorate's own teams work under the same conditions — scrutiny means something only when it applies uniformly.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | District-wide difficulty suppression — all Beat 3 covert ops in named district take −15; distinct from DIR.CA.1 (type-specific block) and STD.CA.10 (faction-specific protect) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — uniform scrutiny as institutional doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; applies to own Beat 3 ops — restraint doctrine; Mandate×2 mid-tier cost | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — scrutiny order is institutional, not public | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Resolution / Modify / Difficulty — threshold adjustment before Beat 3 resolution | Art 04b §4 |
| Balance | ⚠ | −15 to all Beat 3 ops in district is significant suppression at Mandate×2; self-inclusion is the cost; playtesting required | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate (within-month) — tokens placed at Beat 2, consumed at Beat 3 | — |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 Automatic | — |
| Portrait validity | ✓ | Directorate +1 submitter | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | Uses existing Modifier tokens — no new component | Art 02 §11 |
| Supported by game procedure | ✓ | ARBITER places existing Modifier tokens (−15) on each Beat 3 row targeting district at Beat 2 resolution — within existing modifier placement procedure | Art 03 §9 |
| Data schema validation | ✓ | Automatic, no threshold/ring_mod; Beat 2 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Enhanced institutional review; uniform scrutiny including own ops | Art 04 §5 P26 |

#### Outstanding Issues

- **DB registration:** New card — requires id assignment.
- **Beat 2 Automatic + Beat 3 scope:** Confirm ARBITER can identify all Beat 3 rows for the target district at Beat 2 resolution before Beat 3 ops are revealed. Resolution grid rows are placed at Beat 0 — ARBITER has grid visibility. No new tracking required.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*New card — S106. Fills Resolution|Modify|Difficulty gap (04b §8.2 MP). No new component — uses existing Modifier tokens placed per-row.*

```python
DIR.CA.8 = Card(
    id      = "DIR.CA.8", version="v1.0",
    name    = "Enhanced Scrutiny",
    tagline = "Place a district under institutional review. All Beat 3 covert operations in this district find conditions harder.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Directorate,
    layer   = Resolution, function = Modify, subject = Difficulty,
    beat=2, resolution=Automatic, threshold=None,
    ring_mod=None, doctrine_mod=None, trigger=None,
    outcome_type=None,
    persistence=Immediate, persistence_condition=None, persistence_effect=None,
    target_district = district.named,
    target_faction=None, target_object=None, target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost    = resource.faction(acting).mandate * 2,
    success = game.apply_modifier(
                ops=game.resolution_grid.beat3(district=district(target)),
                threshold_mod=-15),
    successcrit=None, fail=None, failcrit=None,
    on_accept=None, on_decline=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "Enhanced scrutiny has been authorised for this district. All activity here is subject to review. All activity. Including ours.",
    perspectives = {Directorate: "The district is under review. Scrutiny means something only when it applies uniformly."},
    design_note  = "Applies to all factions including Directorate. Beat 2 ops in district (DIR.CA.1/CA.3/CA.4) unaffected — only Beat 3 rows. Uses existing Modifier tokens (−15) placed by ARBITER per row, not a district-column flag.",
    arbiter_note = "Beat 2 Automatic resolution: identify all rows in the resolution grid targeting district(target) at Beat 3. Place a standard Modifier token (−15 threshold) on each row. All factions, no exceptions. Tokens are in place when Beat 3 opens — apply −15 to each op's threshold before rolling.",
)
```

---


---

### Directorate — Public Acts
[↑ Directorate](#directorate)

| Card | Name |
|------|------|
| [DIR.PA.1](#p11-regulatory-override) | Regulatory Override |
| [DIR.PA.2](#p12-convene-an-inquiry) | Convene an Inquiry |
| [—](#directorate-entryexit-controls) | Entry/Exit Controls |
| [—](#directorate-standing-injunction) | Standing Injunction |
| [—](#directorate-regulatory-downgrade) | Regulatory Downgrade |
| [—](#directorate-regulatory-freeze) | Regulatory Freeze |

### DIR.PA.1 — REGULATORY OVERRIDE
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's district-level regulatory control PA. All non-Directorate presence-placement actions (cards that Add PresenceTokens) in the named district cost +1 native for the remainder of the Quarter. Persistence = Seasonal: the PA card (or RegulatoryOverrideMarker) stays on the table as an active condition marker until Phase 21 or Directorate goes Absent from the district. This is the structural counter to Guild's build pace — raising the cost of the presence prerequisite that enables STD.PA.3/GUI.PA.1. Restriction: Directorate must have Established in the district to invoke jurisdictional authority.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Directorate regulatory authority over district operations is core to their institutional doctrine | Art 00 §7 |
| Voice fit | ✓ | Directorate on-doctrine; Ghost (aligned): observe who stops crossing; Network (opposed): regulation as toll | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Directorate institutional regulatory authority: Mandate × 2 cost, Established restriction (jurisdictional legitimacy), PS +1. Shapes all other factions' territorial economics in the district. Directly serves Directorate control doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Modify / PresenceToken — modifies the cost of PresenceToken placement actions | Art 04b §4 |
| Balance | ⚠ | Seasonal scope at 2 Mandate is strong — affects all remaining Months of Quarter. Single district only. Balance subject to playtesting | Art 02 §6–§7 |
| Effect duration | ✓ | World condition is Seasonal (within-Quarter, cleared at Phase 21 or Directorate Absent). No multi-Quarter duration. Consistent with Art 04 §5 P19 | Art 04 §5 P19 |
| Persistence | ✓ | Seasonal — DIR.PA.1 card / RegulatoryOverrideMarker stays on district until Phase 21 or Directorate Absent | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid; restriction checks Directorate's influence tier in the district (valid zone condition) | Art 01 §6–§7 |
| Supported by components | ⚠ | RegulatoryOverrideMarker is a new component — register in Art 02 before production | Art 02; Art 03 §9.4 |
| Supported by game procedure | ⚠ | World condition application to PresenceToken.Add actions needs ARBITER tracking protocol. RegulatoryOverrideMarker component registration required | Art 03 §9.4; Art 02 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
DIR.PA.1 = Card(
    id      = "DIR.PA.1",  version="v1.0",
    name    = "Regulatory Override",
    tagline = "Declare a district under Directorate oversight, raising the cost of all non-Directorate presence operations.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer    = Territory,  function = Modify,  subject = PresenceToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Seasonal,  # DIR.PA.1 card / RegulatoryOverrideMarker stays on district until Phase 21
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.all_except(Directorate),
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Directorate).influence_tier(target_district) >= Established,
    cost        = resource.faction(Directorate).mandate * 2,

    success = (
        arbiter.place(RegulatoryOverrideMarker, district(target)),
        game.world_condition(
            scope    = district(target),
            effect   = presence_placement_action(faction=faction.all_except(Directorate)).cost += 1,
            duration = Seasonal,
            clear_on = (
                faction(Directorate).influence_tier(target_district) == Absent
                or game.phase == EndOfQuarter
            ),
        ),
        faction(Directorate).standing += 1,
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Directorate: PortraitEntry(submitter=+1)},

    narrative    = "The Directorate does not need to block what it can simply make more expensive.",
    perspectives = {
        Directorate: "Regulatory oversight is the institutional mechanism for managed stability. The cost increase is the signal, not the sanction.",
        Ghost:       "The Directorate taxes the district. We do not need to control the threshold. We only need to observe who stops trying to cross it.",  # aligned
        Network:     "One Mandate and the Directorate makes every other faction pay to exist in the district. They call it regulation. We call it a toll.",  # opposed
    },
    design_note  = "District-level regulatory PA. +1 native cost on all non-Directorate PresenceToken.Add actions in district for remainder of Quarter (Seasonal). Physical marker on district; card stays on table as marker. Counter to Guild STD.PA.3/GUI.PA.1 build chain — raises cost of presence prerequisite. Restriction: Directorate Established+ in district. Multiple P11s may target different districts. Balance review pending playtesting Cost reasoning: Exposure is necessary to enforce the controls publicly, making the restrictions visible across the district.",
    arbiter_note = "Beat 4: place RegulatoryOverrideMarker on declared district. DIR.PA.1 card stays on table as marker. Apply +1 native cost to all non-Directorate presence-placement actions (STD.CA.3 Campaign, STD.PA.1 Open Operations, STD.CA.8 Buy Influence, GUI.PA.1 Civic Works Mandate) targeting this district for remaining Months of Quarter. Directorate PS +1. Clear: Directorate Absent in district (remove immediately) OR Phase 21 cleanup. Multiple markers on different districts tracked independently.",
)
```

---

### DIR.PA.2 — CONVENE AN INQUIRY
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's institutional intelligence-gathering PA. No formal restriction — Directorate can always commission an inquiry. The yield (Intel tokens) is determined by ARBITER's count of publicly attributed covert actions against the target faction in the last 2 months (from resolved STD.PA.4/STD.PA.5 outcomes this Quarter). Zero yield if no prior attribution groundwork was laid — 3 Mandate wasted. This creates a two-step sequence incentive: STD.PA.4/STD.PA.5 → DIR.PA.2. Distinct from Ghost's STD.CA.5 (Gather): Directorate uses ARBITER as the collection mechanism rather than operational fieldwork.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional investigation via ARBITER is Directorate's mode of intelligence — not covert fieldwork | Art 00 §7 |
| Voice fit | ✓ | Directorate on-doctrine; Guild (aligned): institutional process produces verifiable record; Syndicate (opposed): operating margin is what the record cannot reach | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Directorate commissions ARBITER investigation (not covert fieldwork): 3 Mandate, yield contingent on prior STD.PA.4/STD.PA.5 groundwork. Creates two-step sequence incentive (STD.PA.4/STD.PA.5 → DIR.PA.2). Portrait +1: submitter-bounded | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Add / IntelToken | Art 04b §4 |
| Balance | ✓ | 3 Mandate cost is high. Yield 0–2 tokens depending on prior STD.PA.4/STD.PA.5 outcomes. Expensive gamble without groundwork; reliable payoff when chain is set up | Art 02 §6–§7 |
| Effect duration | ✓ | IntelToken delivery and PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no zone reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (yielded by ARBITER from supply, Art 02 §6); Mandate × 3 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | ARBITER tracks STD.PA.4/STD.PA.5 resolution outcomes; yields based on that record | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
DIR.PA.2 = Card(
    id      = "DIR.PA.2",  version="v1.0",
    name    = "Convene an Inquiry",
    tagline = "Commission an ARBITER-mediated institutional investigation into a faction's recent operations.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer    = Information,  function = Add,  subject = IntelToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,  # no public restriction; yield is variable (0–2) based on ARBITER's record
    cost        = resource.faction(Directorate).mandate * 3,

    success = (
        arbiter.provide_intel_tokens(
            target    = target_faction,
            count     = arbiter.count_attributed_actions(target_faction, months=2),  # 0–2; 0 if no prior STD.PA.4/STD.PA.5
            recipient = Directorate,
        ),
        faction(target).standing    -= 1,
        faction(Directorate).standing += 1,
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Directorate: PortraitEntry(submitter=+1)},

    narrative    = "The Directorate does not gather intelligence in the traditional sense. It commissions review.",
    perspectives = {
        Directorate: "We invoke the institutional mechanism for accountability. Whether it yields anything depends on what the target has done publicly.",
        Guild:       "Directorate uses ARBITER to formalize what was publicly attributed. The investigation costs Mandate but produces something the record can verify. Guild respects the process.",  # aligned
        Syndicate:   "Directorate asks ARBITER to count what was already on the record. What was not on the record, ARBITER cannot count. That distinction is our operating margin.",  # opposed
    },
    design_note  = "Directorate intelligence PA via institutional channel. No restriction — always available. Yield: 1 Intel token per publicly attributed covert action against target faction in last 2 months (from successful STD.PA.4 or STD.PA.5 this Quarter). 0 tokens = 3 Mandate wasted (costly gamble without prior groundwork). Distinct from Ghost STD.CA.5 Gather (covert fieldwork). Creates two-step sequence incentive: STD.PA.4/STD.PA.5 → DIR.PA.2 Cost reasoning: Findings provide the legal precedent and evidence required to sustain the injunction long-term.",
    arbiter_note = "Beat 4. Count: how many successful STD.PA.4 or STD.PA.5 resolutions named this target faction this Quarter? Provide Directorate with that many Fresh Intel tokens (max 2). Apply PS: target −1, Directorate +1. If count = 0: no tokens delivered. 3 Mandate spent regardless.",
)
```

---

### Directorate — ENTRY/EXIT CONTROLS
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's persistent territorial control tool — a district-level board condition that displaces non-Directorate deployment markers immediately and blocks future placement in the named district. Distinct from Invoke Jurisdiction (DIR.CA.1), which blocks specific card types in a single district for one Beat: Entry/Exit Controls operates on deployment marker movement, persists across rounds and Quarters, and is self-policing via persistence_condition (auto-discards if Directorate loses Established status). PS −1 at resolution reflects the public backlash of establishing hard movement restrictions. Removal requires a counter-action — new card type TBD (PM05).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | District-level movement control — displaces markers immediately; blocks future placement; distinct from DIR.CA.1 (card-type block) and DIR.CA.4 (repositioning) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — regulatory authority as territorial infrastructure | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Mandate×3 for permanent district lock; Established restriction (jurisdictional legitimacy requires institutional presence) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) — district-level movement authority is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Block/DeploymentMarker — hard block on placement is the function | Art 04b §4, §5 |
| Balance | ✓ | Mandate×3, permanent district lock, PS −1 — cost TBD playtesting | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent — persists until counter-acted or persistence_condition fails | — |
| Persistence | ✓ | Permanent; persistence_condition auto-discards on Directorate falling below Established in named district | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction requires Directorate Established in named district | — |
| Portrait validity | ✓ | Directorate submitter=+1; PS −1 in success field is a game effect, not portrait | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — standard targeting | Art 01 §6–§7 |
| Supported by components | ✓ | Operates on deployment markers (existing component); no new component required | Art 02 §6–§8 |
| Supported by game procedure | ⚠ | Beat 4 PA resolution defined; persistence_condition monitoring trigger not yet in Art 03 (PM05 04-n29 — blocks Issues Resolved) | Art 03 §9 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Counter-card removal:** Card sits in Directorate's PA area as a permanent board condition. Removal by counter-action requires new card type(s) — design TBD. See PM05 04-n29.
- **Art 03 persistence monitoring:** ARBITER needs a defined trigger point to check persistence_condition of all permanent PA cards (e.g., after any influence tier change). See PM05 04-n29. Blocks Issues Resolved.
- **Displaced faction with no presence elsewhere:** `move_to=district.where(faction.has_presence)` has no valid destination if the displaced faction holds no presence outside the named district. Fallback rule needed — e.g., marker is returned to hand (faction skips next placement) or moved to Baryo as unconditional fallback (Governing Rule 8.3b: no elimination).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Redesigned S66 — v1.0 (ring-scope) retired*

```python
EntryExitControls = Card(
    id      = "DIR.PA.3",  version="v2.0",
    name    = "Entry/Exit Controls",
    tagline = "Designate a district as a controlled zone — displacing non-Directorate deployment markers and blocking future placement.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Block,  subject = DeploymentMarker,
    beat=4,  resolution=Automatic,  threshold=None,  ring_mod=None,
    trigger=None,
    resolution_type="Transactional",  outcome_type=Unilateral,
    persistence           = Permanent,
    persistence_condition = faction(acting).influence_tier(district.named) >= Established,
    persistence_effect    = placement(faction.all_except(Directorate), district=district.named, type=DeploymentMarker).blocked,
    target_district = district.named,
    target_faction  = faction.all_except(Directorate),
    target_object   = None,
    target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).influence_tier(district.named) >= Established,
    cost = resource.faction(acting).mandate * 2 + resource.faction(acting).capacity * 1,
    success = (
        for_each(
            deployment_marker(faction=faction.all_except(Directorate), district=district.named),
            arbiter.instruct(marker.owner, move_to=district.where(faction.has_presence), flip_to=Blocked),
        ),
        faction(acting).standing -= 1,
    ),
    successcrit=None,  fail=None,  failcrit=None,
    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    narrative    = "Movement within the designated zone is now subject to Directorate authorization. Non-compliant presence has been relocated.",
    perspectives = {
        Directorate: "The district is designated. Who enters does so with our permission — or not at all.",
    },
    design_note  = "Persistent PA. Card sits in Directorate's active PA area on the Overview (not on district tile). Immediate: non-Directorate deployment markers in named district displaced to any district where owning faction has presence, flipped to Blocked. Persistent: non-Directorate deployment marker placement blocked in named district. persistence_condition auto-discards card if Directorate falls below Established. PS −1 at resolution (public backlash). Counter-card removal TBD — see PM05 04-n29.",
    arbiter_note = "Name the district. Each non-Directorate deployment marker there: owning faction moves it to any district where they have presence, flip to Blocked.",
)
```

---

### DIRECTORATE — STANDING INJUNCTION
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's pre-emptive PA block — distinct from DIR.PA.1 Regulatory Override (which raises presence-placement cost) and DIR.CA.1 Invoke Jurisdiction (which blocks a specific card type for one Beat in one district). Standing Injunction blocks any PA of a named taxonomy (Layer/Function) from a named faction until triggered or until the quarter ends. Permanent persistence with a dual clearing condition: trigger (target submits blocked PA at Phase B) or quarter end (Phase 21). The partial Mandate refund on Phase 21 expiry provides a safety valve against pure deterrent plays that are never triggered. PS +1 at placement reflects the public legitimacy signal of filing the injunction. No operational footprint restriction — 3 Mandate is the gate. Accords excluded: bilateral acts cannot be unilaterally blocked. Card-as-condition: the card placed in the Directorate play area IS the condition; no marker component needed. Enforcement per Governing Rule 6.1a: Directorate monitors Phase B declarations, calls the trigger, ARBITER adjudicates.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pre-emptive institutional block on a named PA taxonomy is Directorate doctrine — controlling the space of permissible action rather than reacting after the fact | Art 00 §7 |
| Voice fit | ✓ | Directorate on-doctrine; Ghost (aligned) recognizes structural pre-emption as correct; Network (opposed) names it as information control | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Directorate exclusive: Mandate×3, PS +1. Pre-emptive control over PA space is core Directorate doctrine. No operational footprint restriction — cost is the gate | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) — institutional act is public; consistent with Regulatory Downgrade/Freeze pattern | Art 04 §6.2 |
| Taxonomy fit | ✓ | Submission/Block/PublicAct — blocks a PA taxonomy from entering the resolution queue | Art 04b §4 |
| Balance | ⚠ | 3 Mandate for a Seasonal taxonomy block. Partial refund (1 Mandate) on Phase 21 expiry reduces deadweight loss. Balance review pending playtesting | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent — dual clearing condition: trigger (target submits blocked PA) or quarter end (Phase 21) | Art 04 §5 P19 |
| Persistence | ✓ | Permanent public act; card on board IS the condition; self-policing per Governing Rule 6.1a | Art 04 §6; Governing Rule 6.1a |
| Trigger validity | ✓ | No beat-timing trigger; reactive condition (target declares blocked taxonomy at Phase B) documented in design_note | — |
| Portrait validity | ✓ | Directorate +1 submitter-bounded; placing a public institutional block is maximum doctrinal expression | Art 04 §6.2 |
| Supported by zones | ✓ | No district target — faction-targeted; no operational footprint restriction | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — card on Overview is the persistent condition | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Phase B void: Dispatch Token returned, target −1 PS, card removed. No resources committed at Phase B (payment is Beat 4 Step 1) — nothing to refund. PAs declared before Injunction resolved (Beat 4) are committed board states; Governing Rule 7.2b governs, no retroactive block applies | Art 03 §9; Governing Rule 7.2b; Governing Rule 7.3 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

None.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Redesigned S67 — v2.0. PublicAct → PublicAct. InjunctionMarker removed; card-as-condition pattern. Seasonal → Permanent with dual clearing condition (trigger OR Phase 21). Dispatch Token consumed on trigger per Governing Rule 7.3. target_taxonomy field introduced (§6.1/§6.2). Self-policing per Governing Rule 6.1a.*

```python
P_StandingInjunction = Card(
    id      = "DIR.PA.6",  version = "v2.0",
    name    = "Standing Injunction",
    tagline = "Declare a public restriction on a named faction's next act of a specified type. If triggered, the act is voided.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer    = Submission,  function = Block,  subject = PublicAct,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Permanent public act",
    outcome_type    = Unilateral,
    persistence     = Permanent,
    persistence_condition = (
        faction(target).submits(PA(taxonomy=target_taxonomy)) OR
        quarter.phase == 21
    ),
    persistence_effect = PA(taxonomy=target_taxonomy, submitter=faction(target)).blocked_at(phase_b),

    target_district  = None,
    target_faction   = faction.named_opponent,
    target_object    = None,
    target_taxonomy  = taxonomy.declared,  # Layer/Function declared at Phase B; BilateralAgreement excluded

    affinity    = None,
    restriction = None,
    cost        = resource.faction(Directorate).mandate * 1 + resource.faction(Directorate).capital * 1 + resource.faction(Directorate).findings * 1,

    success     = faction(Directorate).standing += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Directorate: PortraitEntry(submitter=+1)},

    narrative    = "The Injunction does not prevent the act. It establishes that the act will carry costs the target has not yet calculated.",
    perspectives = {
        Directorate: "The Injunction does not prevent the act. It relocates its costs.",
        Ghost:       "Directorate pre-empts the declaration rather than reacting to it. We recognize this as the structurally correct approach.",
        Network:     "A pre-emptive block on a public act is the Directorate deciding which information enters the record. We have a word for that.",
    },

    design_note = "Card placed in Directorate play area (public, face-up; target faction and target_taxonomy declared at Phase B). Card IS the persistent condition. Enforcement per Governing Rule 6.1a: Directorate monitors Phase B — when target submits a PA matching target_taxonomy, Directorate calls it; ARBITER voids the PA (target −1 PS, Dispatch Token consumed per Governing Rule 7.3, card removed). PA resources not yet committed at Phase B (payment is Beat 4 Step 1) — nothing to refund. PAs declared before Injunction resolved at Beat 4 are unaffected — committed board state per Governing Rule 7.2b. Quarter-end expiry: if untriggered at Phase 21, Directorate removes card and recovers 1 Mandate. target_taxonomy may not be BilateralAgreement — Accords are bilateral and cannot be unilaterally blocked. Distinct from DIR.PA.1 (cost increase on presence placement) and DIR.CA.1 (single-Beat block in one district).",
)
```

---


---


---

---

### DIR.PA.7 — CURFEW *(stub)*
[↑ Public Acts](#directorate-public-acts)

```python
DIR.PA.7 = Card(
    id      = "DIR.PA.7",  version = "v1.1",
    name    = "Curfew",
    tagline = "Lock down a district to freeze physical movement.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Block,  subject = DeploymentMarker,
    beat    = 4,  resolution = Automatic,  persistence = Transient,
    cost    = resource.faction(Directorate).mandate * 2,
    success = "Places a Standing Condition on target_district until the end of Quarter+1: Deployment Markers cannot be moved into this district.",
    design_note = "A massive territorial denial tool. Blocks physical movement (which is public and enforceable) rather than targeting blind covert space."
)
```

---

### DIR.PA.8 — SUBPOENA *(stub)*
[↑ Public Acts](#directorate-public-acts)

```python
DIR.PA.8 = Card(
    id      = "DIR.PA.8",  version = "v1.2",
    name    = "Subpoena",
    tagline = "Weaponize target-keyed intelligence into a public audit that bleeds an opponent's finances or reputation.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Economy,  function = Remove,  subject = Capital,
    beat    = 4,  resolution = d100,  threshold = 40,
    cost    = resource.faction(Directorate).mandate * 1 + intel_token(faction=target_faction) * 1,
    success = "Target faction must pay 2 Capital or 2 of their Native Resource to the supply. If they do not, they lose 2 Public Standing.",
    design_note = "Cost uses a faction-keyed Intel Token: Directorate 'found out something' that justifies the legal action. The target has the choice to pay the fine or take the PR hit."
)
```

### DIR.MOD.1 — RIOT SQUAD *(stub)*

*S128. First Directorate React. Military-mode enforcement — institutional authority to reverse unauthorized presence placement. Generic variant (faction=Any). Faction-targeted variant: DIR.MOD.2 (Syndicate). Ring-constrained variant: DIR.MOD.3 (Ring 1 Core).*

```python
DIR.MOD.1 = Card(
    id      = "DIR.MOD.1",  card_id="DIR.MOD.1",  version="v0.1",
    name    = "Riot Squad",
    tagline = "Presence placed without Directorate approval can be removed with Directorate authority.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = presence_chip.placed(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Directorate).influence >= Established,  # jurisdictional authority requires Established presence
    cost            = None,  # card consumed; cost TBD (possibly 1 Mandate)

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=trigger.faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Military-mode enforcement React. Fires when any faction places presence in a district where Directorate has Established presence. Directorate may remove 1 chip immediately. Restriction: Directorate must be Established — jurisdictional authority is earned by presence, not proclaimed. This is the suppression toolkit delivered at React speed: Directorate responds to expansion before Beat 3 resolves. Cost TBD — possibly 1 Mandate (enforcement has institutional overhead).",
    arbiter_note = None,
)
```

---

### DIR.MOD.2 — CAPITAL SUPPRESSION *(stub)*

*S128. Faction-targeted variant of DIR.MOD.1. Trigger narrowed to Syndicate presence placement. Syndicate's capital-driven territorial expansion is Directorate's primary doctrinal adversary in Ring 1/2.*

```python
DIR.MOD.2 = Card(
    id      = "DIR.MOD.2",  card_id="DIR.MOD.2",  version="v0.1",
    name    = "Capital Suppression",
    tagline = "Syndicate presence in regulated territory draws immediate institutional response.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = presence_chip.placed(faction=Syndicate),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = Syndicate,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Directorate).influence >= Established,
    cost            = None,

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=Syndicate, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1), Syndicate: PortraitEntry(flat=-1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Syndicate-targeted variant of DIR.MOD.1. Directorate's doctrine makes no distinction between rogue capital and rogue information — Syndicate's gray-market acquisitions are the same institutional threat as Network's broadcasts. Syndicate portrait flat=-1 on fire: the Syndicate's response to having presence removed is public and traceable. Narrower trigger window than generic; reliable in SYN-heavy games.",
    arbiter_note = None,
)
```

---

### DIR.MOD.3 — CITY COUNCIL LOYALIST *(stub)*

*S128. Ring-constrained variant of DIR.MOD.1. Ring 1 (Core) only. No Established restriction — Directorate has blanket institutional authority in Core ring regardless of presence level.*

```python
DIR.MOD.3 = Card(
    id      = "DIR.MOD.3",  card_id="DIR.MOD.3",  version="v0.1",
    name    = "City Council Loyalist",
    tagline = "In the Core, the Directorate's authority does not require a justification.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = presence_chip.placed(faction=Any, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,  # Core ring: no Established requirement — blanket institutional authority
    cost            = None,

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=trigger.faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Ring 1–constrained variant of DIR.MOD.1. Core ring is institutional home territory — Directorate removes presence without needing Established status. Reflects doctrine: Directorate's authority in the Core is structural, not earned faction by faction. Strongest DIR enforcement React — no restriction to work around.",
    arbiter_note = None,
)
```

---

### DIR.MOD.4 — ADMINISTRATIVE OVERHEAD *(stub)*

*S128. Legislative-mode React. Directorate documents all new Accords — procedural overhead yields Mandate income.*

```python
DIR.MOD.4 = Card(
    id      = "DIR.MOD.4",  card_id="DIR.MOD.4",  version="v0.1",
    name    = "Administrative Overhead",
    tagline = "Every Accord formed is a Directorate administrative event.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = accord.placed,
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(Directorate).resources.add(1, Mandate),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Legislative-mode React on accord.placed. Directorate charges institutional overhead for registering diplomatic agreements — Mandate income regardless of which factions are party to the Accord.",
    arbiter_note = None,
)
```

---

### DIR.MOD.5 — EMERGENCY APPROPRIATION *(stub)*

*React to subsidize the heavy Mandate cost of Permanent PAs.*

```python
DIR.MOD.5 = Card(
    id      = "DIR.MOD.5",  card_id="DIR.MOD.5",  version="v0.1",
    name    = "Emergency Appropriation",
    tagline = "Institutional scale requires institutional funding.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = public_act.placed_on_frg(faction=Directorate, persistence=Permanent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(Directorate).resources.add(2, Mandate),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Economy fixer. Triggers when Directorate places a Permanent Public Act on their Faction Resolution Grid at Phase 9.2 (before resolution). Instantly yields 2 Mandate, subsidizing the crippling Q1/Q2 cost of laying down their win-condition standing condition PAs.",
    arbiter_note = None,
)
```

---

### DIR.MOD.6 — STATE OF EMERGENCY *(stub)*

*Creates a standing global difficulty constraint triggered by a World Event.*

```python
DIR.MOD.6 = Card(
    id      = "DIR.MOD.6",  card_id="DIR.MOD.6",  version="v0.1",
    name    = "State of Emergency",
    tagline = "The world changes. The Directorate dictates how.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = world_event.revealed,
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Directorate).mandate * 1 + resource.faction(Directorate).exposure * 1,

    success     = "Card remains in play (persistence=Quarter) on Directorate FRG. While in play, any opponent Public Act targeting a district where Directorate influence is >= Established suffers boost=-10.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Environmental shaping. Triggers when the Arbiter reveals a World Event. The ModReactCard itself is placed face-up on the Directorate's Faction Resolution Grid as a standing condition for the rest of the Quarter. It imposes a -10 difficulty penalty on any opponent PA that targets a district where Directorate is Established or higher. Solves the 'world event extension' gap by letting Directorate piggyback on the World Event phase to declare their own global environmental constraint. Legally escapes Art 00a §9.1 because it modifies action difficulty (9.1a), not resource income Cost reasoning: Exposure represents the widespread public broadcast necessary to enforce an emergency lockdown.",
    arbiter_note = None,
)
```

---

### DIR.MOD.7 — EMINENT DOMAIN *(stub)*

*Jurisdictional claim over private development.*

```python
DIR.MOD.7 = Card(
    id      = "DIR.MOD.7",  card_id="DIR.MOD.7",  version="v0.1",
    name    = "Eminent Domain",
    tagline = "Private development is subject to institutional oversight.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = structure_block.placed(faction=opponent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.place(presence_chip, district=target_district, faction=Directorate, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Win-condition engine. Whenever an opponent builds a structure, Directorate immediately claims jurisdictional oversight, placing a presence chip in that district for free. Helps Directorate passively achieve 'Established in more districts'.",
    arbiter_note = None,
)
```

---

### DIR.MOD.8 — ASSET SEIZURE *(stub)*

*Impounds public operational funds in Established territory.*

```python
DIR.MOD.8 = Card(
    id      = "DIR.MOD.8",  card_id="DIR.MOD.8",  version="v0.1",
    name    = "Asset Seizure",
    tagline = "Unlicensed public operations are subject to immediate fines.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = public_act.placed_on_frg(target_district=where(faction(Directorate).influence >= Established)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Directorate).mandate * 1 + resource.faction(Directorate).capital * 1,

    success     = arbiter.remove(resource_token, target=trigger.card, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Bureaucratic taxation. Triggers when a PA is placed on the FRG targeting a Directorate-Established district. Directorate instantly removes (impounds) 1 resource token off the card. The acting faction must either add a replacement resource before Beat 4, or suffer partial-payment failure Cost reasoning: Requires Capital to mobilize the physical impoundment teams while Mandate authorizes the seizure.",
    arbiter_note = None,
)
```

---

## Network
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#network-covert-operations) · [Public Acts](#network-public-acts)

---

### Network — Covert Operations
[↑ Network](#network)

| Card | Name |
|------|------|
| [NET.CA.1](#c26-leak) | Leak |
| [NET.CA.2](#c27-disclosure-loop) | Disclosure Loop |
| [NET.CA.3](#c28-breaking-news) | Breaking News |
| [NET.CA.4](#c29-network-cascade) | Network Cascade |
| [NET.CA.5](#c30-community-anchor) | Community Anchor |
| [NET.CA.6](#network-sacrifice) | Sacrifice |
| [—](#network-weaponized-transparency) | Weaponized Transparency (Retired S70) |
| [NET.CA.7](#netca7--ground-signal) | Ground Signal |

### NET.CA.1 — LEAK
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's pre-execution discovery card — spends 1 Exposure + 1 Findings to expose a target faction's most resource-costly unresolved covert operation before it fires, cancelling it in the process. Full discovery mechanic applies: ARBITER publicly announces operation type, acting faction, and targets; target faction suffers PS reduction; the operation does not resolve. Resources the target submitted are lost. Beat 3 timing is intentional — Network has a strategic incentive to go first in initiative order so Leak fires before the target's operation resolves; going late risks a fizzle if all valid targets have already been processed. The Findings cost requires Network to have a trade relationship with Ghost or hold Findings-generating territory — cross-resource by design. Pairs with NET.CA.2 Disclosure Loop (successful Reveal → +1 Exposure) to make revelation self-sustaining.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pre-execution discovery + cancellation — distinct from NET.CA.3 (faction communications) and all post-resolution reveal cards; Network burns the plan before it fires | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective — selective, precision disclosure as doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; 1 Exposure + 1 Findings cross-resource; Automatic; fizzle risk on low initiative creates meaningful cost beyond resources | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — broadcast-based pre-execution discovery is Network-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/District — what is made public is geographic (district + operation type); subject corrected from ActionAttribution S68 | Art 04b §4, §5 |
| Balance | ✓ | 1 Exposure + 1 Findings; can cancel a costly op — cross-resource cost is the primary gate; fizzle risk and initiative dependency add further constraint; flag for 04-n34c sweep | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — discovery announced and cancellation applied at resolution; no lingering state | — |
| Persistence | ✓ | Immediate — card resolves fully at Beat 3; cancelled op leaves no residual game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Network +1 submitter — discovery operation aligns with transparency doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — operation district is revealed as part of discovery, not targeted as a zone | Art 01 §6–§7 |
| Supported by components | ✓ | CovertOperation (unresolved, in Beat 3 grid) as target — physically verifiable by ARBITER at resolution | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; initiative order determines valid targets; ps_framing on target pending 04-n33/04-n34b | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **ps_framing on target:** Target faction PS reduction on discovery is the standard failcrit consequence — pending 04-n33 schema addition and 04-n34b sweep to formalise in spec.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Redesigned S68: subject ActionAttribution → District; pre-execution discovery + cancellation model; cross-resource cost; beat=3 initiative incentive confirmed.*

```python
NET.CA.1 = Card(
    id      = "NET.CA.1",  version="v1.1",
    name    = "Leak",
    tagline = "Expose and cancel a rival's most costly unresolved operation before it fires.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Information,  function = Reveal,  subject = CovertOperation,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction(named_opponent), target_object=CovertOperation(faction=faction(target), beat=3, unresolved=True),
    target_taxonomy=None,
    affinity=None,
    restriction = faction(target).op(beat=3, unresolved=True).count >= 1,
    cost        = resource.faction(acting).exposure * 1 + resource.faction(acting).findings * 1,
    success     = [
        game.announce(faction(target).op(beat=3, unresolved=True, selection=highest_cost), discovery=True, public=True),
        game.cancel(faction(target).op(beat=3, unresolved=True, selection=highest_cost)),
    ],
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The Network does not need to know everything — only enough to make the right question public.",
    perspectives = {Network: "We do not reveal everything. We reveal the piece that makes everything else visible."},
    design_note  = "Redesigned S68: subject corrected to District (was ActionAttribution — taxonomy mismatch); pre-execution discovery + cancellation model confirmed (target op cancelled, resources lost, PS reduction applies); cross-resource cost 1 Exposure + 1 Findings by design to force trade dependency. Beat 3 initiative incentive: Network benefits from going first; fizzle risk if target ops resolve before Leak fires. ps_framing for target PS reduction pending 04-n33/04-n34b. S126 agy audit: subject corrected to CovertOperation (District was also a mismatch — DistrictTile has no Reveal in comp_verb_phase; the card reveals and cancels a CovertOperation, not the district itself).",
    arbiter_note = "Among target faction's unresolved covert operations in the Beat 3 grid, identify the operation with the highest total resource cost submitted. Publicly announce: operation name, acting faction, target district. Cancel the operation — it does not resolve; resources submitted are lost. Target faction PS reduction applies (discovery consequence — ps_framing pending 04-n33). If no unresolved operations remain for target faction at time of Leak's resolution, operation has no effect — Network's resources spent. Network's acting faction identity is not announced at resolution.",
)
```

---

### NET.CA.2 — DISCLOSURE LOOP
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's Exposure generation card — converts the act of revealing into additional broadcast capacity. Spends 1 Finding; if Network successfully resolved any Reveal card this round, delivers +1 Exposure. The loop is the mechanic: reveal with NET.CA.1 or NET.CA.3, then play NET.CA.2 to convert that act into more Exposure for future reveals. Replaced NET.CA.2 Source Protection (S51) which was doctrinally misaligned — protecting attribution is Ghost's register. The conditional success (`if reveal_resolved_this_round >= 1`) means NET.CA.2 only pays out when Network is actively broadcasting; a NET.CA.2 played in isolation does nothing, burning only the Finding cost.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Exposure generation from reveal activity — self-sustaining broadcast loop; dead-weight if used in isolation, which is the intended design | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — loop as resource doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Findings×1 low cost; conditional payoff requires active reveal this round; replaces retired Source Protection (doctrinally misaligned) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — Exposure amplification is Network infrastructure | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/Exposure — converts reveal activity to resource; Economy layer correct | Art 04b §4, §5 |
| Balance | ✓ | Findings×1 for conditional Exposure — low cost; isolation dead-weight is intentional cost gate; conditional cost resolution outstanding (Outstanding Issue) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: Exposure delivered at Beat 3 cleanup | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | Conditional success — `reveal_resolved_this_round >= 1` is inline trigger; trigger vs. success field distinction outstanding (Outstanding Issue) | — |
| Portrait validity | ✓ | portrait = {} — Disclosure Loop is internal resource infrastructure, not a visible doctrinal act; absence confirmed intentional (Outstanding Issue) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — self-targeting; no district context | Art 01 §6–§7 |
| Supported by components | ✓ | Exposure as subject; Findings cost; no new components | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 cleanup; ARBITER tracks Reveal card resolutions this round; conditional resolution outstanding (Outstanding Issue) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Conditional success modelling:** `success = exposure += 1 if reveal_resolved_this_round >= 1 else None` — confirm whether the "else None" path consumes the Finding cost (card slot and Findings are spent, no outcome) or refunds it. Current design note says "the slot cost was the investment" — confirm.
- **portrait = {} justification:** Empty portrait for a Network FactionSpecific card is uncommon. Confirm intentional — Disclosure Loop is an internal resource mechanism, not a visible doctrinal act.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*S51 redesign — design rationale scaffold added S59. Design pass pending.*

```python
NET.CA.2 = Card(
    id      = "NET.CA.2",  version="v1.0",
    name    = "Disclosure Loop",
    tagline = "Transparency is self-sustaining. Revealing information generates the capacity to reveal more.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Economy,  function = Add,  subject = Exposure,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction(acting), target_object=None,
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).findings * 1,
    success     = resource.faction(acting).exposure += 1 if faction(acting).reveal_resolved_this_round >= 1 else None,
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "The act of disclosure is not only a tactic. It is a resource. The Network learned this before anyone else at this table.",
    perspectives = {Network: "We revealed something. Now we can reveal something more. The loop is already running."},
    design_note  = "Replaces NET.CA.2 Source Protection (retired S51). Source Protection was doctrinally misaligned — protecting attribution is Ghost's register, not Network's. Pairs with NET.CA.1 Leak and NET.CA.3 Breaking News.",
    arbiter_note = "At Beat 3 cleanup, check whether any Network Reveal card resolved successfully this round. If yes, deliver 1 Exposure to Network's resource pool. If no Reveal resolved, card takes effect but produces nothing — the slot cost was the investment.",
)
```

---

### NET.CA.3 — BREAKING NEWS
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's forced-transparency Beat 2 card — submits into the Beat 2 row to force public revelation of the target faction's first committed Beat 3 operation before the round fires. The operation still resolves; it simply does so with the table informed. Exposure×2 is the price of intelligence at this scale; threshold 50 introduces a risk the table can observe and react to.

Distinct from NET.CA.1 Leak: Leak cancels before firing (Beat 3), with the revelation as a side effect of destruction. Breaking News reveals before firing (Beat 2), with no cancellation — the operation proceeds in public. Two different Network postures: *stop it* vs. *ensure everyone watches it happen*.

Distinct from GHO.CA.2 Intercept: GHO.CA.2 delivers a private IntelDeliverySlip to Ghost — intelligence for one faction's use. Breaking News announces publicly — the whole table knows.

Crit success reveals the full queue, a significant information advantage that resets all players' tactical picture before Beat 3.

*Replaces NET.CA.3 Open Channel (retired S68). Open Channel required ARBITER to maintain a notification redirect state from Beat 2 through Beat 3 — proactive cross-beat tracking, Governing Rule 6.1 violation. Breaking News is point-in-time: ARBITER announces at Beat 2 and places a Visibility Marker (VM-xx); no state to carry forward.*

#### Card Story

A Network operative submits intelligence on a target faction's committed operation — and instead of keeping it, broadcasts it. Before Beat 3 fires, the table knows what's coming. The operation proceeds; it just does so in public.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Beat 2 forced public reveal before Beat 3 fires — distinct from NET.CA.1 (pre-execution cancel, Beat 3, no public announcement) and GHO.CA.2 (private IS-xx to Ghost, Beat 2) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective — forced transparency at the moment of commitment | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Exposure×2; threshold 50; fizzle risk if target has no committed ops; crit reveals full queue | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — forced public reveal of committed ops is Network-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ⚠ | Information/Reveal/CovertOperation — subject = CovertOperation needs 04b validation; no registered grid-card subject type currently | Art 04b §4, §5 |
| Balance | ✓ | Exposure×2 at threshold 50; fizzle risk on empty queue; crit is high-value (full queue exposure) — appropriate variance for Network initiative card | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — announcement fires at Beat 2; VM-xx handles Beat 3 public resolution flag; VM-xx is transient game-state on the grid card, not a card-level persistence field | — |
| Persistence | ✓ | Immediate — card fully resolved at Beat 2; VM-xx is physical game state managed per Art 03 procedure | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Network +1 submitter — forced transparency is core doctrine; FactionSpecific card, no other portrait entries | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no zone restriction | Art 01 §6–§7 |
| Supported by components | ✓ | VM-xx registered in 00b §4 (S82, 04-n76 ✅) | Art 02 §6–§8; Art 07 |
| Supported by game procedure | ✓ | Beat 2 d100 procedure added Art 03 §9.4 (S81, 04-n75 ✅); VM-xx Beat 3 public resolution clause added (S81, 04-n76 ✅) | Art 03 §9, §11 |
| Data schema validation | ✓ | All §6.1 fields present; subject = CovertOperation flagged for 04b taxonomy validation | Art 04 §6.1 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Taxonomy subject:** subject = CovertOperation — no registered grid-card subject type exists. Needs 04b validation pass. (Non-gate — tracked in taxonomy checklist row.)

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ S89 | |

```python
NET.CA.3 = Card(
    id      = "NET.CA.3", version="v2.0",
    name    = "Breaking News",
    tagline = "Force ARBITER to publicly reveal the target faction's first committed operation before Beat 3 resolves.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Network,
    layer   = Information, function = Reveal, subject = CovertOperation,  # 04b validation needed
    beat=2, resolution=d100, threshold=50, ring_mod=None, trigger=None,
    resolution_type = "Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district = None,
    target_faction  = faction(named_opponent),
    target_object   = None,
    target_taxonomy=None,
    affinity        = None,
    restriction     = "target_faction != acting_faction",
    cost        = resource.faction(acting).exposure * 2,
    success     = [
        game.announce(faction(target).beat3_queue[0], fields=[name, type, targets], destination=public),
        game.place(VM_xx, on=faction(target).beat3_queue[0]),
    ],
    successcrit = [
        game.announce(faction(target).beat3_queue[:], fields=[name, type, targets], destination=public),
        game.place(VM_xx, on=faction(target).beat3_queue[:]),
    ],
    fail        = None,
    failcrit    = game.dispatch(NotificationSlip(recipient=faction(target))),
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The story was going to come out. We simply chose the timing.",
    perspectives = {
        Network: "We don't ask permission to broadcast. We decide when.",
    },
    design_note  = "Replaces NET.CA.3 Open Channel (retired S68 — Governing Rule 6.1 cross-beat state violation). Fills Network's forced-transparency FactionSpecific slot at L1. Beat 2: ARBITER announces target's first Beat 3 queue entry to all players; VM-xx placed to flag public Beat 3 resolution. Distinct from NET.CA.1 Leak (Beat 3 cancel + reveal) and GHO.CA.2 Intercept (private IS-xx to Ghost). Fizzle: if target has no committed Beat 3 ops at Beat 2, announce fizzle; cost spent. Second Beat 2 d100 card alongside GHO.CA.2 — procedure gap in Art 03 tracked in 04-n75.",
    arbiter_note = "Network has played Breaking News targeting faction X. Roll d100 (threshold 50 + PS modifier). Success: check faction X's Beat 3 queue. If empty: announce 'No operations queued for faction X — Breaking News fizzles'; cost spent, no further effect. Otherwise: identify faction X's first entry in Beat 3 resolution order; announce to all players: card name, type, declared targets; place VM-xx on that card in the grid. VM-xx procedure at Beat 3: when this card is reached, announce it publicly, roll d100 visibly, announce outcome to table, then remove VM-xx. Do not announce Network as acting faction. Crit success: reveal and place VM-xx on ALL of faction X's Beat 3 queue entries. Fail: cost spent, no announcement. Crit fail: dispatch NotificationSlip to faction X only. Do not announce Network.",
)
```

---

### NET.CA.4 — NETWORK CASCADE
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's signal propagation card — extends STD.CA.6 Broadcast Interference's Public Act cost increase to an adjacent district on the same round. Mechanically ties the two cards together: STD.CA.6 must be submitted in the same round for NET.CA.4 to fire. This creates a planned two-card combo: pay the STD.CA.6 Exposure cost to disrupt PA activity in one district, then pay NET.CA.4's Exposure×2 to extend that disruption to an adjacent district. The "signal propagation" framing is doctrinally exact — The Network understands that broadcast interference is not bounded by administrative district lines. Beat 2 Automatic means both disruption effects land before Beat 4 PA resolution.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Signal propagation — extends STD.CA.6 Broadcast Interference to adjacent district; mechanically implements "broadcast doesn't stop at district borders" doctrine | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — signal propagation as operational reality | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; requires STD.CA.6 same round (restriction); Exposure×2; Beat 2 Automatic — both disruption effects land before Beat 4 PA resolution | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — signal propagation is Network-exclusive two-card mechanic | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Submission/Modify/PublicAct — extends STD.CA.6's PA cost increase to adjacent district | Art 04b §4, §5 |
| Balance | ✓ | Exposure×2 for adjacency extension; total combo cost outstanding calibration noted; STD.CA.6 dependency limits use | Art 02 §6–§7 |
| Effect duration | ✓ | One round: PA cost increase applies this round's Beat 4 PA phase only | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | STD.CA.6 submission as restriction prerequisite; submission ordering and void-on-STD.CA.6-cancel outstanding (Outstanding Issues) | — |
| Portrait validity | ✓ | Network +1 submitter; signal extension aligns with broadcast doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = adjacent to STD.CA.6.target_district; dependency resolution outstanding (Outstanding Issue) | Art 01 §6–§7 |
| Supported by components | ✓ | PublicAct as target_object; Exposure cost; no new components | Art 02 §6–§8; Art 04b §5 |
| Supported by game procedure | ✓ | Beat 2 Automatic; PA cost increase at Beat 4; STD.CA.6 submission ordering outstanding (Outstanding Issue) | Art 03 §9, §9.4, §10 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **STD.CA.6 dependency at Dispatch:** Restriction requires `submitted(STD.CA.6, round=game.round) == True`. Confirm: can NET.CA.4 be submitted before STD.CA.6 in the same round (with STD.CA.6 submission validated later), or must STD.CA.6 already be submitted when NET.CA.4 is checked?
- **target_district dependency:** NET.CA.4's target is derived from STD.CA.6's target district. If STD.CA.6 is cancelled or discarded after NET.CA.4 is submitted, what happens to NET.CA.4? Confirm void or independent resolution.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
NET.CA.4 = Card(
    id      = "NET.CA.4",  version="v1.0",
    name    = "Network Cascade",
    tagline = "Extend Broadcast Interference to an adjacent district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Submission,  function = Modify,  subject = PublicAct,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.adjacent(C06.target_district), target_faction=None, target_object=PublicAct,
    target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).submitted(STD.CA.6, round=game.round) == True,
    cost        = resource.faction(acting).exposure * 1 + resource.faction(acting).findings * 1,
    success     = district(target).political_act_cost += 1,
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The Network understands signal propagation better than anyone at this table.",
    perspectives = {Network: "The signal does not stop at district borders. Neither do we."},
    design_note  = None,
    arbiter_note = None,
)
```

---

### NET.CA.5 — COMMUNITY ANCHOR
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's Baryo-targeted presence card — specialized version of STD.CA.3 Campaign, restricted to Baryo ring districts where Network has zero presence. The restriction enforces the narrative: Community Anchor is how Network establishes a beachhead through existing relationships, not how it expands from existing territory. Cheaper than STD.CA.3 (Exposure×1 vs dual-cost) because the card is zone-restricted and fires only on initial entry — once Network has any presence in the district, the card cannot target it again. Baryo focus aligns with Network's win path (wide Presence coverage from New Meridian, Baryo outward).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Network's Baryo entry mechanic — initial beachhead via existing relationships; distinct from STD.CA.3 Campaign (general presence) by Baryo restriction and zero-presence gate | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — community-based entry as doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Exposure×1 (cheaper than STD.CA.3 dual-cost); Baryo+zero-presence restriction enforces narrative; aligns with Network's wide-presence win path | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — Baryo-targeted entry is Network-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Add/PresenceToken — Baryo-restricted variant of STD.CA.3 Campaign pattern | Art 04b §4, §5 |
| Balance | ✓ | Exposure×1, Automatic, Baryo+zero-presence restriction — narrower and cheaper than STD.CA.3; Baryo entry advantage calibration noted | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: +1 presence token at Beat 3; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces zero-presence condition | — |
| Portrait validity | ✓ | Network +1 submitter; community-based entry aligns with broadcast doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any(zone=Baryo) — Baryo zone definition outstanding (Outstanding Issue) | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken; Exposure cost; no new components | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; ARBITER places presence token; zone check at Dispatch | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Baryo zone definition:** `district.any(zone=Baryo)` — confirm Baryo as a defined zone in Art 01. If Baryo includes multiple rings' districts, the zone boundary needs to be explicit.
- **Expansion beyond initial entry:** Once Network has 1 presence in a Baryo district (via Community Anchor), the restriction blocks reuse in that district. Confirm this is the intended scarcity design — Community Anchor establishes but does not reinforce.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
NET.CA.5 = Card(
    id      = "NET.CA.5",  version="v1.0",
    name    = "Community Anchor",
    tagline = "Establish presence in a Baryo district through existing relationships.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Territory,  function = Add,  subject = PresenceToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any(zone=Baryo), target_faction=None, target_object=None,
    target_taxonomy=None,
    affinity=None,
    restriction = district(target).faction(acting).presence == 0 AND district(target).zone == Baryo,
    cost        = resource.faction(acting).exposure * 1,
    success     = district(target).faction(acting).presence += 1,
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The Network did not arrive in New Meridian through official channels. They arrived through people.",
    perspectives = {Network: "We already have contacts there. This is formalising what already exists."},
    design_note  = None,
    arbiter_note = None,
)
```

---

### Network — SACRIFICE
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's credibility-to-Intel conversion card. Reflects the Network doctrine that institutional standing is a means, not an end: when The Network needs intelligence on a specific faction and has no other path to it, it trades credibility for operational capability. The PS loss is a success effect — not a submission cost — because Public Standing is a non-fungible marker, not a tradeable resource (Art 04 §6.2). Single use per play, 2 PS per token. Faction target is required: tokens must be keyed to a faction at Dispatch ("no blank checks").

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | PS-to-Intel conversion — Network doctrine: standing is a means, not an end; deliberate sacrifice for targeted intelligence | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; free submission; PS loss as success effect; target_faction required for token keying; 2 PS per token calibrated as real doctrine commitment | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/IntelToken — PS effect generates faction-keyed Intel; Economy layer correct | Art 04b §4, §5 |
| Balance | ✓ | Free cost; 2 PS for 1 IntelToken; single use per play — PS track scarcity is the gate; 2:1 ratio prevents cheap arbitrage vs. Weaponized Transparency | Art 02 §6–§7; Art 02 §11 |
| Effect duration | ✓ | Immediate: PS reduced and token delivered at Beat 3 resolution | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | portrait = {} — PS loss is a success effect, not a portrait track shift; absence confirmed intentional | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — no district context | Art 01 §6–§7 |
| Supported by components | ✓ | target_faction required; IntelToken keyed to target_faction at Dispatch | Art 02 §6–§8; Art 02 §11 |
| Supported by game procedure | ✓ | Beat 3 Automatic; PS loss and IntelToken delivery handled by Art 03 apply effect | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

*None.*

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Migrated from Art 04 §8 (retired) Intel Economy block to Network extended section S59. Pre-convention flat format — full schema pass pending (04-47).*

```python
NET.CA.6 = Card(
    id      = "NET.CA.6",  version="v1.1",
    name    = "Sacrifice",
    tagline = "Spend two steps of credibility. Receive one piece of intelligence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Economy,  function = Add,  subject = IntelToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction.any, target_object=None,
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = None,
    success     = faction(acting).standing -= 2, IntelToken(target_faction) += 1,
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "The Network knows: sometimes you spend credibility like currency. This is one of those times.",
    perspectives = {Network: "What we have built is not a goal. It is a tool. And sometimes a tool must be spent."},
    design_note  = "PS −2 is a success effect, not a cost — PS is non-fungible and cannot appear in the cost field (Art 04 §6.2). target_faction required: tokens must be keyed at Dispatch. Single use per play; 2:1 ratio prevents cheap IntelToken arbitrage Cost reasoning: Findings are needed to identify the exact weak points in adjacent district firewalls for the signal to jump.",
    arbiter_note = None,
)
```

---

### Network — WEAPONIZED TRANSPARENCY
[↑ Covert Operations](#network-covert-operations)

*Retired S70 — split into two successor cards per PM05 04-n47 (choose_one on success violation) and 04-n48. Successor A: React modifier stub below. Successor B: PA stub in Network PA section.*

---

### NET.CA.7 — GROUND SIGNAL
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's public standing card — fills the Standing|Shift gap identified in Art 04b §8.3. Available only when Network IL is ≤ Established in the target district: at Dominant, the street already knows who Network is; outreach adds nothing. The card activates Network's existing chip presence to generate a legible public signal — the people carrying the message are already part of the district's daily traffic. No new infrastructure, no announcement. On a successcrit the signal lands hard enough to convert: +1 chip placed in target district alongside additional +1 PS.

#### Card Story
The message doesn't travel because Network announced it. It travels because Network is already there.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | PS generation when not Dominant — fills Standing|Shift gap in Network set; successcrit converts signal to physical presence | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective — presence made legible, not announced | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; IL ≤ Established restriction is doctrinal (no outreach needed at Dominant); Exposure×1 cost calibrated to PS yield | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — street-level signal is unannounced, deniable | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding — PS generation via distributed presence signal | Art 04b §4 |
| Balance | ⚠ | Successcrit +1 chip placement strong at Established threshold — validate against chip economy in playtesting | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — PS and chip effects resolve at Beat 3 | — |
| Persistence | ✓ | Immediate — no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Network +1 submitter — visible-but-deniable public signal aligns with Broadcaster doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; IL restriction checked at resolution | Art 01 §6–§7 |
| Supported by components | ✓ | Successcrit places 1 chip — standard chip placement, no new component | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 d100; IL check and chip placement handled by Art 03 apply effect | Art 03 §9, §11 |
| Data schema validation | ✓ | Fields consistent with §6.1–§6.3 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Street-level signal; presence made legible without announcement | Art 04 §5 P26 |

#### Outstanding Issues

- **DB registration:** New card — requires id assignment in card_ref and component_metadata.
- **IL enum value:** Confirm `InfluenceLevel.Established` is the correct enum identifier in schema.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*New card — S106. Fills Standing|Shift|PublicStanding gap (04b §8.3 HP).*

```python
NET.CA.7 = Card(
    id      = "NET.CA.7", version="v1.0",
    name    = "Ground Signal",
    tagline = "Put the message on the street. Presence here is readable. Let it be read.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Network,
    layer   = Standing, function = Shift, subject = StandingMarker,
    beat=3, resolution=d100, threshold=50,
    ring_mod=None, doctrine_mod=None, trigger=None,
    outcome_type=None,
    persistence=Immediate, persistence_condition=None, persistence_effect=None,
    target_district = district.named,
    target_faction=None, target_object=None, target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).influence_level(district(target)) <= InfluenceLevel.Established,
    cost    = resource.faction(acting).exposure * 1,
    success = faction(acting).standing.add(1),
    successcrit = (faction(acting).presence_chips(district(target)).add(1),
                   faction(acting).standing.add(1)),
    fail=None,
    failcrit    = faction(acting).standing.remove(1),
    on_accept=None, on_decline=None,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "No one announces this. The message moves because the people carrying it are already there, already part of the district's daily traffic. The signal is readable only to those who know how to read it.",
    perspectives = {Network: "We're not running outreach. We're making our existing presence legible to people who've been ignoring it."},
    design_note  = "Restriction: Network IL in target district ≤ Established (Dominant excluded — at Dominant, the street already knows). Successcrit delta: +1 chip in target district + +1 PS additional on top of success's +1 PS (total on successcrit: +2 PS, +1 chip placed).",
    arbiter_note = "Beat 3: Network IL in target district must be ≤ Established (Dominant: card invalid, do not resolve). On success: +1 PS to Network. On successcrit: additionally place 1 Network chip in target district AND +1 PS (total: +2 PS, +1 chip placed). Failcrit: −1 PS.",
)
```

---

### Network — Public Acts
[↑ Network](#network)

| Card | Name |
|------|------|
| [NET.PA.1](#p13-public-disclosure) | Public Disclosure |
| [NET.PA.2](#p14-community-rally) | Community Rally |
| [—](#network-live-coverage) | Live Coverage |

### NET.PA.1 — PUBLIC DISCLOSURE
[↑ Public Acts](#network-public-acts)

#### Design Rationale
Network's signature information-attack PA — a coordinated release of all substantiated intelligence against a target faction. Scaling mechanic: each Intel token spent contributes both to the threshold calculation (more tokens = more credible = easier to land) and to the damage on both success and fail (more tokens = more damage, even when the full release fails). The partial damage on fail ("the dirt still gets out") reflects that even a botched broadcast releases something. High investment ceiling makes this Network's most powerful single card when fully loaded.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Coordinated multi-attribution broadcast is Network's highest-expression public act | Art 00 §7 |
| Voice fit | ✓ | Network on-doctrine; Guild (aligned): disclosure makes attribution permanent; Ghost (opposed): sequenced release vs. full dump | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Maximum-expression Network broadcast: all held Intel tokens spent; Exposure × 2 (Network's resource). Network +2 PS on success. Intel token scarcity (Ghost pipeline or covert gathering) is the natural ceiling on doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Network) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Reveal / ActionAttribution | Art 04b §4 |
| Balance | ⚠ | Threshold scales with token count (30 + 10n). Damage scales per token (−2 PS each on success, −1 on fail). High cost (2 Exposure + all tokens). Intel tokens are scarce (require Ghost cooperation or covert gathering) — natural limiter | Art 02 §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted broadcast; no zone reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (all held, faction-keyed to target; Art 02 §6); Exposure × 2 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Token count calculated at Beat 4; all tokens spent regardless of outcome | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
NET.PA.1 = Card(
    id      = "NET.PA.1",  version="v1.0",
    name    = "Public Disclosure",
    tagline = "Network broadcasts all substantiated intelligence about a faction's operations in a single coordinated release.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,

    layer    = Information,  function = Reveal,  subject = ActionAttribution,

    beat            = 4,
    resolution      = d100,
    threshold       = 30 + (10 * count(intel_token(target=faction(target)).held)),  # +10 per token held naming target
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Contested",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Network).holds_intel_token(faction=target, count=1),
    cost        = resource.faction(Network).exposure * 2 + intel_token(target=faction(target)).all_held,

    success = (
        faction(target).standing  -= (2 * count(intel_token(target=faction(target)).spent)),
        faction(Network).standing += 2,
    ),
    successcrit = None,
    fail = (
        faction(target).standing  -= (1 * count(intel_token(target=faction(target)).spent)),  # partial — dirt still gets out
        faction(Network).standing -= 1,
    ),
    failcrit = None,

    portrait = {Network: PortraitEntry(submitter=+1)},

    narrative    = "Network does not sit on what it knows. When the moment is right, everything comes out at once.",
    perspectives = {
        Network: "We have been patient. This is the release.",
        Guild:   "Network makes the attribution permanent. Everyone knew some of this. After the disclosure, no one can pretend otherwise. That is the kind of outcome Guild recognizes.",  # aligned
        Ghost:   "Network releases everything it has. We would have sequenced it. You do not exhaust an intelligence reserve in a single action — you do not know what the next month requires.",  # opposed
    },
    design_note  = "Network's highest-damage information PA. Threshold: 30 base + 10 per token held (1 token=40, 2=50, 3=60). All held tokens spent regardless. Success: −2 PS per token, Network +2 flat. Fail: −1 PS per token (partial release), Network −1. Token scarcity (Ghost pipeline or covert gathering) is natural limiter. Beat 4 timing: benefits from covert ops having resolved at Beat 3.",
    arbiter_note = "Count Network's held Intel tokens naming target. Threshold = 30 + (10 × count). All tokens spent at resolution. On success: target loses (2 × count) PS; Network +2 PS. On fail: target loses (1 × count) PS (partial release announced); Network −1 PS. Token count cannot be zero (restriction enforces minimum 1).",
)
```

---

### NET.PA.2 — COMMUNITY RALLY
[↑ Public Acts](#network-public-acts)

#### Design Rationale
Network's broadcast-derived presence PA — scaling territorial expansion built on established foothold. Network names up to 3 districts where they are already Established or Dominant; 1 presence token is placed in each. Cost scales with district count (2 Exposure + 1 per additional district). This is not expansion into new territory — it is deepening existing presence through community mobilisation, the most on-doctrine territorial act for Network. Replaces Open Record Request, which had unworkable mechanical premises.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Broadcast-derived community presence growth is Network's primary win-condition mechanism | Art 00 §7 |
| Voice fit | ✓ | Network on-doctrine; Syndicate (aligned): acquisition-free consolidation; Directorate (opposed): unregulated expansion | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Network deepens existing foothold (Established+) — consolidation, not expansion. Scaling Exposure cost (Network's resource). Portrait +1. Directly serves Network's community-relationship territorial doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Network) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken | Art 04b §4 |
| Balance | ✓ | Scales: 2 Exposure (1 district), 3 Exposure (2), 4 Exposure (3 max). Restricted to Established+ (not expansion). Partial resolution if some districts fail restriction | Art 02 §6–§7 |
| Effect duration | ✓ | PresenceToken placement = Permanent board state; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.up_to_three — valid zone references; restriction checks Established+ per district (valid zone conditions) | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); Exposure × 2+ cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Districts named at Phase B; restriction per district at Beat 0 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
NET.PA.2 = Card(
    id      = "NET.PA.2",  version="v1.0",
    name    = "Community Rally",
    tagline = "Mobilize communities across Network's established presence network.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,

    layer    = Territory,  function = Add,  subject = PresenceToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.up_to_three,  # 1–3 districts named at Phase B; each must be Established+
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Network).influence_tier(district.each_target) >= Established,
    cost        = resource.faction(Network).exposure * 2 + resource.district(each_target).native * 1,
    # cost = 2 Exposure + 1 district native per targeted district

    success     = (
        district.each(target).faction(Network).presence += 1,
        faction(Network).standing += 1,
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Network: PortraitEntry(submitter=+1)},

    narrative    = "Network presence does not require a march. It requires a broadcast and the communities that were already listening.",
    perspectives = {
        Network:     "We are already there. This makes it visible.",
        Syndicate:   "Network deepens without purchasing. No Accord, no offer fee, no formal mechanism. The community already listening becomes the position. Efficient.",  # aligned
        Directorate: "Network consolidates three Established positions simultaneously without a single permit or notification. The Directorate marks this as unregulated expansion and files accordingly.",  # opposed
    },
    design_note  = "Broadcast-derived presence PA. Deepens existing foothold (Established+) rather than expanding into new territory. Scaling cost: 2 Exposure (1 district), 3 (2 districts), 4 (3 districts). Partial resolution: if a named district fails Established+ restriction at Beat 0, that district is dropped from resolution; remaining valid districts proceed; cost already committed. Replaces Open Record Request (unworkable) Cost reasoning: District native resources represent the local on-the-ground support required to organize a massive rally.",
    arbiter_note = "Phase B: Network names 1–3 districts. Cost calculated (2 + extras) and committed. Beat 0: check each named district for Established+ restriction. Drop invalid districts from resolution. Beat 4: place 1 presence token in each valid district. Network +1 PS.",
)
```

---

### Network — LIVE COVERAGE
[↑ Public Acts](#network-public-acts)

#### Design Rationale
Network's forced-transparency PA — the broadcaster turns its full institutional reach on a named faction and makes them The Story. The declaration is public and immediate: from the next Covert Dispatch, the named faction is under live coverage. They must choose each Covert Dispatch whether to cooperate (hand face-up on the table, covert ops proceed) or go dark (dispatch case disabled this Month, hand stays hidden). The scrutiny doesn't end by fighting it; it ends when the faction gives the interview.

Comply for one full Covert Dispatch → card clears. The faction has been transparent enough; Network moves on. The strategic question is *when* to give the interview — a faction holding strong ops for Month 3 may choose to absorb the disability in Month 2 to protect the play, then comply in Month 3 when there's less to expose.

*Note: cards laid face-up during compliance are still "in hand" for all game purposes — card counts, submittability, and eligibility are unchanged. The open hand is a visibility state, not a mechanical restriction.*

*Successor to C40 Option B (Weaponized Transparency, retired S70). Replaces dispatch-case forced-reveal mechanism — hand visibility is the simpler, more narratively grounded L1 mechanism.*

#### Card Story

Network turns its full broadcast infrastructure on a named faction, making them The Story. Under live coverage, that faction faces a choice each Covert Dispatch: open their hand to the table and operate in full view, or go dark and forfeit covert submissions entirely. The scrutiny doesn't end by fighting it — it ends when the faction gives the interview.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Unique PA effect — Seasonal hand-visibility obligation on named faction; comply/resist model with genuine decision friction per Month | Art 00 §7 |
| Voice fit | ✓ | Network perspective (accountability as doctrine) + Directorate counter (institutional authority contested); FactionSpecific PA — two perspectives sufficient | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Exposure×2; threshold 50; Seasonal persistence; comply-once clearing models natural media-cycle end | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Network) — public declaration of broadcast accountability; Network-exclusive institutional leverage | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ⚠ | Information / Reveal / FactionHand — FactionHand not a registered subject type; needs 04b validation | Art 04b §4, §5 |
| Balance | ✓ | Exposure×2 at threshold 50; comply-to-clear limits maximum duration; resist penalty (covert ops disabled) is real cost; crit adds immediate PS pressure | Art 02 §6–§7 |
| Effect duration | ✓ | Seasonal — clears at Quarter end OR when target complies once (whichever is first) | — |
| Persistence | ✓ | Seasonal; `persistence_condition` = target complied for one Covert Dispatch; `persistence_effect` = Covert Dispatch comply/resist obligation | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Network +1 submitter; FailCrit Network −1 (failed broadcast backfires — reckless accusation without traction); FactionSpecific, no other entries | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no zone restriction | Art 01 §6–§7 |
| Supported by components | ✓ | No new component required — open hand is a physical visibility state, not a board marker; comply/resist is self-policing per Governing Rule 6.1a | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Art 03 §9.0 (Start of Month) provides generalizable Covert Dispatch obligation procedure — Steps 0–2 cover comply/resist for any active PA with this obligation type (04-n77 ✅) | Art 03 §9.0 |
| Data schema validation | ✓ | All §6.1 fields present; FactionHand subject flagged for 04b validation | Art 04 §6.1 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Taxonomy subject:** subject = FactionHand — not a registered subject type. Needs 04b validation pass. (Non-gate — tracked in taxonomy checklist row.)
- **Card ID:** TBD — pending PM05 04-n1 numbering pass. (Non-gate.)

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ S89 | |

```python
NET.PA.3 = Card(
    id      = "NET.PA.3", version="v1.0",
    name    = "Live Coverage",
    tagline = "Force a named faction to play with their hand visible or forfeit covert submissions, each Covert Dispatch for the remaining Months of the Quarter.",
    type    = PublicAct, subtype = FactionSpecific, faction = Network,
    layer   = Information, function = Reveal, subject = FactionHand,  # 04b validation needed
    beat=4, resolution=d100, threshold=50, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type = "Probabilistic", outcome_type=None,
    persistence     = Seasonal,
    persistence_condition = "target_faction complied (open hand) for one full Covert Dispatch this Quarter → card clears at end of that Covert Dispatch; or Quarter end",
    persistence_effect    = "Each Covert Dispatch of remaining Months: target faction elects comply (lay all held cards face-up on table; covert ops proceed normally this Covert Dispatch) or resist (dispatch case disabled this Month — no covert submissions). Comply once → card clears.",
    target_district = None,
    target_faction  = faction(named_opponent),
    target_object   = None,
    target_taxonomy=None,
    affinity        = None,
    restriction     = "target_faction != Network",
    cost        = resource.faction(acting).exposure * 2,
    success     = game.activate(LiveCoverage_obligation, target=faction(target)),
    successcrit = (
        game.activate(LiveCoverage_obligation, target=faction(target)),
        faction(target).standing -= 1,
    ),
    fail        = None,
    failcrit    = faction(acting).standing -= 1,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The story is already written. The only question is whether the subject chooses the cameras or the consequences.",
    perspectives = {
        Network:     "We are not exposing secrets. We are establishing accountability. The distinction matters to us.",
        Directorate: "Network has appointed itself an oversight authority. The Directorate notes this. It will not be forgotten.",
    },
    design_note  = "Successor to C40 Option B (Weaponized Transparency, retired S70). Hand-visibility model replaces dispatch-case forced-reveal — simpler L1 execution, genuine comply/resist decision friction. Comply once → card clears (the faction gave the interview; Network moves on). Resist → covert submissions disabled that Month; card persists. Natural expiry: Quarter end. SuccessCrit: obligation activates + target −1 PS (story breaks big). FailCrit: Network −1 PS (reckless broadcast, story didn't land). Art 03 Covert Dispatch procedure required (04-n77). Subject = FactionHand — 04b validation needed.",
    arbiter_note = "Network has declared Live Coverage against faction X. Place card in Network's active PA area, face-up; faction X announced. Effect begins next Covert Dispatch. Each Covert Dispatch while Live Coverage is active: at start of Covert Dispatch announce — 'Live Coverage is active against [Faction X]. Faction X: comply (lay all held cards face-up on your table area for Covert Dispatch — cards remain in hand; covert ops proceed) or resist (forfeit covert submissions this Month).' If faction X complies: covert submissions proceed normally; at end of Covert Dispatch, remove Live Coverage from Network's active PA area. If faction X resists: faction X does not open their dispatch case this Covert Dispatch; Live Coverage remains in play. Cards laid face-up during compliance are still counted as in hand. Network identity as declaring faction is already public (Phase B declaration).",
)
```

---


---


---

### NET.MOD.2 — TROLL FARM *(stub)*

*Moved to §11.8 — S71. Successor to C40 Option A (Weaponized Transparency). React modifier card — Network faction.*

**Design Rationale:** Network deploys gathered intelligence to damage a faction's reputation at the moment a visible trigger fires. The PS reduction is unblockable — once Network activates the information, the reputational damage cannot be countered or retracted. Operates as a React modifier card per Art 03 §18: Network announces and presents the card on the trigger condition; ARBITER confirms and pauses play. Trigger condition TBD.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | — | Intelligence-to-reputation conversion; unblockable PS −1 on visible trigger | Art 00 §7 |
| Voice fit | — | TBD — single Network perspective minimum | Art 00 §7 |
| Doctrine alignment | — | TBD | Art 00 §7; Art 04 §6.5 |
| Card type fit | — | ModReactCard — not a CovertOperation; full spec pending 09-06 design pass | Art 04 §6.1, §6.2 |
| Taxonomy fit | — | TBD — modifier card taxonomy differs from action card taxonomy | Art 04b §4, §5 |
| Balance | — | IntelToken cost; Automatic; PS −1; unblockable — TBD relative to countermeasure rarity | Art 02 §6–§7 |
| Effect duration | — | Immediate at trigger point | — |
| Persistence | — | Immediate | Art 04 §6 |
| Trigger validity | — | **TBD.** Must be publicly observable (Art 04 §5 P5). Candidates: target faction plays a PA at Beat 4; target faction achieves Established+ in any district; target faction places a deployment marker. | Art 03 §18; Art 04 §5 P5 |
| Portrait validity | — | TBD — modifier card portrait model | Art 04 §6.2 |
| Supported by zones | — | TBD | Art 01 §6–§7 |
| Supported by components | — | IntelToken cost; PublicStanding target | Art 02 §6–§8 |
| Supported by game procedure | — | Art 03 §18 React rules apply; unblockability governing rule outstanding | Art 03 §18 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

**Outstanding Issues:**
- **Trigger condition:** Set S128 — `standing_marker.increased(faction=Any, except=Network)`. Publicly observable (§5 P5 compliant).
- **Unblockability formalization:** Art 03 governing rule deferred until a second bypass-capable card establishes the generalizable pattern. Issues Resolved cannot be set until the rule is written.
- **Card name:** Placeholder — confirm before sign-off.
- **Ring variants:** Consider faction-targeted variants (e.g., trigger narrowed to specific faction) as 09-06 design pass progresses.

**Status:** Stub — trigger set S128. Issues Resolved and sign-off pending unblockability governing rule.

```python
NET.MOD.2 = Card(
    id      = "NET.MOD.2",  card_id="NET.MOD.2",  version="v0.1",
    name    = "Troll Farm",  # placeholder name — confirm before sign-off
    tagline = "The narrative was already moving. We just changed where it was going.",
    type    = ModReactCard,  faction = Network,
    trigger = standing_marker.increased(faction=Any, except=Network),
              # fires when any other faction's standing marker increases (publicly observable)
    ring_constraint = None,  ring_origin = None,  value_rating = None,
    beat    = None,  resolution = Automatic,
    cost    = resource.faction(Network).exposure * 1 + resource.faction(Network).capital * 1,
    success = faction(trigger.faction).standing -= 1,  # unblockable — governing rule TBD; see Outstanding Issues
    fail    = None,
    restriction = None,
    portrait = {Network: PortraitEntry(submitter=+1)},
    narrative = None,  perspectives = None,  arbiter_note = None,
    design_note = "Network activates an Intel dossier the moment a faction's standing increases — converting gathered intelligence into immediate reputational damage at the opponent's highest-visibility moment. PS −1 is unblockable: once the information releases, retraction is impossible. Governing rule for unblockability outstanding — address alongside any second bypass-capable card. Trigger is standing_marker.increased (publicly observable, §5 P5 compliant). Does not fire on Network's own standing increases. card_id = NET.MOD.2 Cost reasoning: Capital funds the server farms and botnets needed to rapidly manufacture the public narrative.",
)
```

---

---

### NET.PA.4 — GRASSROOTS PROTEST *(stub)*
[↑ Public Acts](#network-public-acts)

```python
NET.PA.4 = Card(
    id      = "NET.PA.4",  version = "v1.1",
    name    = "Grassroots Protest",
    tagline = "Mobilize the masses to physically drown out an opponent's influence.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Territory,  function = Remove,  subject = PresenceToken,
    beat    = 4,  resolution = d100,  threshold = 60,
    cost    = resource.faction(Network).exposure * 1 + district_native(target_district) * 1,
    success = "Remove 1 target_faction's Presence Token from target_district. Target faction loses 1 PS. Network gains +1 PS.",
    design_note = "A loud territorial disruption. Burns Exposure and local resources to physically remove an opponent's token while shifting the PR balance."
)
```

---

### NET.PA.5 — VIRAL OUTRAGE *(stub)*
[↑ Public Acts](#network-public-acts)

```python
NET.PA.5 = Card(
    id      = "NET.PA.5",  version = "v1.1",
    name    = "Viral Outrage",
    tagline = "Weaponize an opponent's own assets against them to tank their standing.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Standing,  function = Shift,  subject = StandingMarker,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Network).exposure * 2 + resource.faction(target_faction).native * 1,
    success = "Target faction loses 3 Public Standing. Network gains +1 PS.",
    design_note = "Pure PR assassination. Network burns the opponent's own native resource to fuel the smear campaign."
)
```

---

### NET.PA.6 — CROWDFUNDING CAMPAIGN *(stub)*
[↑ Public Acts](#network-public-acts)

```python
NET.PA.6 = Card(
    id      = "NET.PA.6",  version = "v1.1",
    name    = "Crowdfunding Campaign",
    tagline = "Convert public goodwill into hard resources.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Economy,  function = Add,  subject = AnyResource,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Network).exposure * 1,
    success = "Network names a resource type. Network gains 1 of that resource type for every 4 points of positive Public Standing they currently have.",
    design_note = "Network's economy is driven by their audience. This rewards them for maintaining a high, positive PS track by converting it into any resource they need."
)
```

### NET.MOD.1 — PIRATE TRANSMITTER *(stub)*

*S106. Network React Modifier — Territory|Add|PresenceToken. Successor B to Weaponized Transparency (retired S70, 04-n47/04-n48). Note: Art 04b §9 excludes Modifier cards from the taxonomy matrix; Layer/Function/Subject fields below describe the card's effect category for spec clarity only.*

**Design Rationale:** Network's opportunistic presence card. Fires when any PA success causes a board state change (influence chip or structure block placed or removed) in a district. The act of change is publicly observable — qualifying trigger. Network announces Pirate Transmitter and rolls d100. On success: 1 Network chip placed in the changed district. The card does not require Network to have existing presence; the PA's visibility is the only entry condition. On successcrit: additional +1 PS — the signal lands publicly as well as physically. Failcrit: −1 PS — the insertion attempt is noticed and goes badly.

#### Card Story
The district was already moving. Network didn't start the change — it arrived at the same time the change did.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Opportunistic chip placement on publicly-observable PA trigger — fills Territory|Add|PresenceToken gap in Network Modifier set | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective — presence inserted through public disruption | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; trigger is publicly observable (any PA board state change); no prior presence required — doctrinal reach-first | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard — trigger is PA success causing board state change; not a CovertOperation | Art 04 §6.1, §6.2; Art 04b §9 |
| Taxonomy fit | — | Modifier cards excluded from matrix (Art 04b §9); effect is Territory|Add|PresenceToken for spec reference only | Art 04b §9 |
| Balance | ⚠ | Exposure×1 cost; broad trigger (any PA board state change); chip placement with no prior foothold requirement is strong — validate against board state frequency in playtesting | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — chip placed at Beat 4 trigger point | — |
| Persistence | ✓ | Immediate — no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | PA success causing board state change (influence or structure, + or −) — publicly observable | Art 03 §18; Art 04 §5 P5 |
| Portrait validity | ✓ | Network +1 submitter — opportunistic broadcast insertion aligns with Broadcaster doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district(trigger.target) — fixed by trigger, not a free choice | Art 01 §6–§7 |
| Supported by components | ✓ | Chip placement — standard; Exposure×1 cost — standard Network resource | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 4 React; Art 03 §18 React rules apply; trigger window opens on PA success announcement | Art 03 §18 |
| Data schema validation | ⚠ | ModReactCard schema defined (04-n102 ✅); full spec (trigger, value_rating, ring_constraint, ring_origin) pending 09-06 design pass | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Board disruption as entry window — Network presence arrives with the change | Art 04 §5 P26 |

**Outstanding Issues:**
- **Modifier card schema:** Full spec pending modifier card design pass (04-n4). Fields below use CA conventions for clarity.
- **DB registration:** card_id = NET.MOD.1 — requires integer id assignment and card_ref entry. First Network Modifier card.
- **Board state change definition:** Confirm "board state change" scope — influence chip count change OR structure block placed/removed; excludes PS shift, resource transfer, Intel token delivery.

**Status:** Design pass complete — S106. Issues Resolved and sign-off pending 04-n4 schema pass.

```python
NET.MOD.1 = Card(
    id      = "NET.MOD.1",  card_id="NET.MOD.1",  version="v1.0",
    name    = "Pirate Transmitter",
    tagline = "A public action changes the district. The signal finds the opening.",
    type    = ModReactCard,  faction = Network,
    trigger = PA_success.where(effect.causes_board_state_change(district)),
              # fires on any PA success that places or removes an influence chip
              # or structure block in any district; target = that district
    target_district = district(trigger.target),
    beat    = 4,  resolution = d100,  threshold = 50,
    ring_mod=None,  doctrine_mod=None,  outcome_type=None,
    persistence=Immediate,  persistence_condition=None,  persistence_effect=None,
    target_faction=None,  target_object=None,  target_taxonomy=None,
    affinity=None,  restriction=None,
    cost    = resource.faction(acting).exposure * 1,
    success = faction(acting).presence_chips(district(target)).add(1),
    successcrit = faction(acting).standing.add(1),
    fail    = None,
    failcrit = faction(acting).standing.remove(1),
    on_accept=None,  on_decline=None,
    portrait = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The district was already moving. Network didn't start the change — it arrived at the same time the change did. Two signals crossing in the open.",
    perspectives = {Network: "We don't need to create the disruption. We need to be in position when it happens."},
    design_note  = "Trigger: any PA success that causes a board state change (influence chip or structure block placed or removed in district). Target district fixed by trigger — not a free choice. No restriction on Network existing presence. Modifier card schema fields are CA-convention placeholders pending 04-n4.",
    arbiter_note = "Beat 4: when a PA success produces a board state change in district X (influence chip count changes, or structure block placed/removed), Network may announce Pirate Transmitter. Confirm trigger validity. Network spends 1 Exposure and rolls d100 (threshold 50, usual modifiers). Success: place 1 Network chip in district X. Successcrit: +1 PS additional. Fail: no effect. Failcrit: −1 PS.",
)
```

---

### NET.MOD.3 — BACKUP SERVER RACKS *(stub)*

*S128. React on Network PS loss. Enables Sacrifice (NET.CA.2 Disclosure Loop) + recovery arc. Network manages its own signal — what the public hears is what Network decides they hear.*

```python
NET.MOD.3 = Card(
    id      = "NET.MOD.3",  card_id="NET.MOD.3",  version="v0.1",
    name    = "Backup Server Racks",
    tagline = "When Network loses standing, redirect the narrative before it lands.",
    type    = ModReactCard,  faction = Network,
    layer   = None,  function = None,  subject = None,

    trigger         = standing_marker.decreased(faction=Network),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = Network,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,  # card consumed; cost TBD (possibly 1 Exposure)

    success     = faction(Network).standing.add(TBD),  # negate some or all of triggering decrease; magnitude TBD
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "PS recovery React. Fires when Network's own PS decreases by any cause. Partially or fully negates the loss — magnitude TBD at design pass. Enables Disclosure Loop (NET.CA.2) sacrifice + immediate recovery as a designed arc rather than a liability. Pairs with NET.CA.6 Sacrifice (PS→Intel) — the spend-and-recover cycle makes Network's PS expenditure feel controlled rather than punitive.",
    arbiter_note = None,
)
```

---

### NET.MOD.4 — AMPLIFICATION ARRAY *(stub)*

*S128. React on broadcast_card.placed (db25 — public SitRep card in Situation Report Zone). Fires at Upkeep SitRep and Beat 5. Generic variant — any district where Network already has presence. Ring-constrained variant: NET.MOD.5 (Mid ring).*

```python
NET.MOD.4 = Card(
    id      = "NET.MOD.4",  card_id="NET.MOD.4",  version="v0.1",
    name    = "Amplification Array",
    tagline = "When news breaks publicly, the Network's signal extends.",
    type    = ModReactCard,  faction = Network,
    layer   = None,  function = None,  subject = None,

    trigger         = broadcast_card.placed,  # db25 — SitRep card placed in Situation Report Zone
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = faction(Network).district.any,  # any district where Network has presence
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Network).any_presence,  # must have at least 1 district with presence
    cost            = None,

    success     = arbiter.place(presence_chip, district=faction(Network).district.acting_choice, faction=Network, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Presence expansion React on broadcast_card.placed (db25, public SitRep card). Every public information event is a Network signal event — the story expanding means the Network's reach expands. Network selects which existing-presence district receives the chip. Fires 1–2 times per Quarter (Upkeep SitRep + possible Beat 5). Delivers §5a 'broadcast-derived presence' at the modifier card level.",
    arbiter_note = None,
)
```

---

### NET.MOD.5 — INFRASTRUCTURE SIGNAL *(stub)*

*S128. Ring-constrained variant of NET.MOD.4. Fires only when SitRep fires and Network has presence in a Mid ring (Ring 2) district. Mid ring is the consolidation zone — this card deepens Network's reach in established infrastructure.*

```python
NET.MOD.5 = Card(
    id      = "NET.MOD.5",  card_id="NET.MOD.5",  version="v0.1",
    name    = "Infrastructure Signal",
    tagline = "Public broadcasts amplify Network reach in established infrastructure districts.",
    type    = ModReactCard,  faction = Network,
    layer   = None,  function = None,  subject = None,

    trigger         = broadcast_card.placed,  # db25
    beat            = None,
    ring_constraint = 2,  # fires only in context of Ring 2 (Mid ring) districts
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = faction(Network).district.ring(2).any,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Network).presence_in_ring(2),
    cost            = None,

    success     = arbiter.place(presence_chip, district=faction(Network).district.ring(2).acting_choice, faction=Network, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Ring 2–constrained variant of NET.MOD.4 (Amplification Array). Same trigger (broadcast_card.placed, db25) but fires only if Network has Mid ring presence; places chip in a Mid ring district. Deepens Network's Mid ring footprint each time public information spreads — Infrastructure districts amplify the signal.",
    arbiter_note = None,
)
```

---

### NET.MOD.6 — STREET-LEVEL AGITATOR *(stub)*

*S128. React on any presence placement in Baryo (Ring 3). When any faction moves in Baryo, Network's community reach follows — opportunistic Baryo expansion is Network's territorial signature.*

```python
NET.MOD.6 = Card(
    id      = "NET.MOD.6",  card_id="NET.MOD.6",  version="v0.1",
    name    = "Street-level Agitator",
    tagline = "When anyone moves in the Baryo, Network's voice follows.",
    type    = ModReactCard,  faction = Network,
    layer   = None,  function = None,  subject = None,

    trigger         = presence_chip.placed(faction=Any, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = faction(Network).district.ring(3).adjacent_to(trigger.district),
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Network).any_presence,
    cost            = None,

    success     = arbiter.place(presence_chip, district=faction(Network).district.ring(3).acting_choice, faction=Network, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Opportunistic Baryo expansion React. When any faction places presence in Ring 3 (Baryo), Network may place 1 chip in any Ring 3 district where it has presence (or adjacent — TBD at design pass). Network's community-relationship model means others' activity in Baryo draws Network in. Delivers §5a 'wide Presence coverage, Baryo outward' at the modifier deck level.",
    arbiter_note = None,
)
```

---

### NET.MOD.7 — COMMUNITY AMPLIFIERS *(stub)*

*React on any Public Act resolution. Feeds the Network's hand when the board gets loud.*

```python
NET.MOD.7 = Card(
    id      = "NET.MOD.7",  card_id="NET.MOD.7",  version="v0.1",
    name    = "Community Amplifiers",
    tagline = "The louder the city gets, the more they listen.",
    type    = ModReactCard,  faction = Network,
    layer   = None,  function = None,  subject = None,

    trigger         = public_act.resolved(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.draw_modifier(faction=Network, count=2, if_acting_faction=Network, then_count=3),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Net growth engine. Draws 2 cards on any PA, or 3 if Network resolved it. Transforms public state changes into hand advantage.",
    arbiter_note = None,
)
```

---

### NET.MOD.8 — FREQUENCY SPLITTER *(stub)*

*React on Network Modifier card placed. Links Reacts together sequentially.*

```python
NET.MOD.8 = Card(
    id      = "NET.MOD.8",  card_id="NET.MOD.8",  version="v0.1",
    name    = "Frequency Splitter",
    tagline = "A single broadcast splinters into a dozen channels.",
    type    = ModReactCard,  faction = Network,
    layer   = None,  function = None,  subject = None,

    trigger         = modifier_card.placed(faction=Network),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = faction(Network).district.ring(3).acting_choice,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Network).any_presence,
    cost            = None,

    success     = list([arbiter.draw_modifier(faction=Network, count=1), arbiter.place(presence_chip, district=target_district, faction=Network, count=1)]),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Chain enabler. Triggers off Network placing a ModReact card. Replaces itself and drops Baryo presence, letting them stack noise sequentially.",
    arbiter_note = None,
)
```

---

### NET.MOD.9 — BANDWIDTH OVERRIDE *(stub)*

*React on district becoming Contested. High-yield payload when the board gets messy.*

```python
NET.MOD.9 = Card(
    id      = "NET.MOD.9",  card_id="NET.MOD.9",  version="v0.1",
    name    = "Bandwidth Override",
    tagline = "Conflict creates the ultimate engagement metric.",
    type    = ModReactCard,  faction = Network,
    layer   = None,  function = None,  subject = None,

    trigger         = status_marker.contested.placed(),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Network).exposure * 1 + resource.faction(Network).findings * 1,

    success     = arbiter.draw_modifier(faction=Network, count=4),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "The massive hand-flooder. Triggered by a high-tension public state change. Since there is no hand limit, Network holds these cards indefinitely to fund their cascading react chain Cost reasoning: Findings pinpoint the opponent's exact communication frequencies to successfully jam them.",
    arbiter_note = None,
)
```

---

### NET.MOD.10 — LOCAL ORGANIZERS *(stub)*

*React on any presence placement in Baryo (Ring 3). Grassroots co-option of opponent territorial momentum.*

```python
NET.MOD.10 = Card(
    id      = "NET.MOD.10",  card_id="NET.MOD.10",  version="v0.1",
    name    = "Local Organizers",
    tagline = "They sent operatives. We sent neighbors.",
    type    = ModReactCard,  faction = Network,
    layer   = None,  function = None,  subject = None,

    trigger         = presence_chip.placed(faction=Any, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = Resource(Exposure, 1),

    success     = list([arbiter.remove(presence_chip, district=target_district, faction=target_faction, count=1), arbiter.place(presence_chip, district=target_district, faction=Network, count=1)]),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Opportunistic Baryo swap. When any faction places a presence chip in Ring 3 (Baryo), Network pays 1 Exposure to immediately swap it for a Network chip. Represents grassroots community organizing co-opting the opponent's momentum. Creates brutal point-disruption in the slums without requiring a Dispatch Token.",
    arbiter_note = None,
)
```

---

---

### NET.MOD.11 — CANCEL CAMPAIGN *(stub)*
[↑ Modifier & React Cards](#network-modifier-and-react-cards)

```python
NET.MOD.11 = Card(
    id      = "NET.MOD.11",  version = "v1.1",
    name    = "Cancel Campaign",
    tagline = "Hijack the narrative of an opponent's public action.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Network,
    layer   = Standing,  function = Shift,  subject = StandingMarker,
    trigger = "public_act.submitted",
    cost    = resource.faction(Network).exposure * 1,
    success = "The target faction's PA resolves normally, but their PS is reduced by 2 due to extreme public backlash. Network gains 1 Exposure.",
    design_note = "Network doesn't block the legal act (Directorate's job). Instead, Network weaponizes the public's reaction to the act, ensuring the target pays a heavy PR price for whatever they just did."
)
```

---

### NET.MOD.12 — FORCED TRANSPARENCY *(stub)*
[↑ Modifier & React Cards](#network-modifier-and-react-cards)

```python
NET.MOD.12 = Card(
    id      = "NET.MOD.12",  version = "v1.0",
    name    = "Forced Transparency",
    tagline = "Broadcast their intended target before they are ready.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Network,
    layer   = Information,  function = Reveal,  subject = TargetProfile,
    trigger = "public_act.placed_with_target_profile",
    cost    = resource.faction(Network).exposure * 1,
    success = "The Target Profile is immediately flipped face-up for the table to see.",
    arbiter_note = "Reacts at Art 03 §9.2.0 when an opponent places a PA with a face-down Target Profile. Network announces the React and spends 1 Exposure. The Target Profile is flipped face-up immediately. The PA is locked in and will resolve normally at Beat 4, but the target is now public knowledge for the rest of the round.",
    design_note = "A direct counter to hidden targets. By spending 1 Exposure, Network strips the opponent's tactical ambiguity for the entire round. This allows other factions to prepare defenses or negotiate before Beat 4."
)
```


## Syndicate
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#syndicate-covert-operations) · [Public Acts](#syndicate-public-acts)

---

### Syndicate — Covert Operations
[↑ Syndicate](#syndicate)

| Card | Name |
|------|------|
| [SYN.CA.1](#c31-leveraged-acquisition) | Leveraged Acquisition |
| [SYN.CA.2](#c32-short-the-market) | Short the Market |
| [SYN.CA.3](#c33-hostile-acquisition) | Hostile Acquisition |
| [SYN.CA.4](#c34-golden-parachute) | Golden Parachute |
| [SYN.CA.5](#c35-regulatory-capture) | Regulatory Capture |
| [—](#syndicate-land-title) | Land Title |
| [—](#syndicate-hostile-takeover) | Hostile Takeover |
| [SYN.CA.10](#syn-ca-10--accord-transfer) | Accord Transfer |
| [—](#syndicate-parasitic) | Parasitic |
| [—](#syndicate-corporate-blackmail) | Corporate Blackmail |
| [SYN.CA.11](#syn-ca-11--redline) | Redline |

### SYN.CA.1 — LEVERAGED ACQUISITION
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's non-presence resource extraction card — Capital buys immediate resource extraction from any district without Syndicate being physically present. Establishes the doctrine that ownership and presence are separate things. Distinguished from Land Title (extended set) by duration: SYN.CA.1 is a per-round transactional play; Land Title creates a permanent revenue claim. Core cost is the action slot itself; the 2:1 Capital:native conversion is a secondary trade rate, not the primary barrier.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Non-presence resource extraction — Capital buys revenue stream from any district; implements "ownership ≠ presence" doctrine; distinct from Land Title (permanent) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×2; no per-round limit; core cost = action slot; affinity boost directed (condition TBD — see Outstanding Issues) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — non-presence extraction is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — deferred upkeep delivery accepted | Art 04b §4, §5 |
| Balance | ✓ | Capital×2 for 1 district native resource at Beat 3 resolution; core cost = action slot. No per-round limit. Boost on affinity TBD. | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: native resource of target district delivered at Beat 3 resolution. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; non-presence extraction aligns with capital intelligence doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource cost + delivery; Immediate at Beat 3; no new component required. | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; Immediate delivery at resolution; no deferred procedure required. | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Schema violations in SYN.CA.7/DIR.CA.5:** `affinity=Syndicate` / `affinity=Directorate` corrected to `affinity=None` — 04-n70 fix pass.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*v1.4 — S71: boost field added (True: capital×2); affinity=None confirmed; Issues Resolved ✓.*

```python
SYN.CA.1 = Card(
    id      = "SYN.CA.1",  version = "v1.4",
    name    = "Leveraged Acquisition",
    tagline = "Extract resource income from a district without physical presence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,

    layer   = Economy,  function = Add,  subject = NativeResource,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).capital * 2,
    boost       = True: resource.faction(acting).capital * 2,
    # submit 2 Capital → 1 native; submit 4 Capital → 2 native; submit 6 Capital → 3 native
    # ARBITER counts n = (submitted − 2) / 2 at Beat 0; success fires (1 + n) times

    success     = game.grant(faction(acting), district(target).resource.native * 1),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Syndicate: PortraitEntry(submitter=+1)},

    narrative    = "The Syndicate does not need to be somewhere to profit from it. Ownership and presence are different things.",
    perspectives = {Syndicate: "We own the revenue stream. Whether we are physically present is irrelevant."},
    design_note  = "Immediate delivery at Beat 3 resolution. Core cost = action slot; 2:1 Capital:native is the unit rate. Boost: player submits multiples of 2 Capital; each unit yields 1 additional native. No declaration required.",
    arbiter_note = "Beat 0: if extra Capital submitted beyond 2, calculate n = (total − 2) / 2; must be whole number or reject. Beat 3: grant Syndicate (1 + n) units of target district's native resource.",
)
```

---

### SYN.CA.2 — SHORT THE MARKET
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's economic disruption card — directly reduces a target faction's native resource supply, impeding their ability to fund actions next round. The "short" framing reflects a deliberate market interference: Syndicate bets against a competitor's economic health and profits from their reduced capacity. Intel restriction (fresh token) requires prior intelligence, creating a two-step play: gather first, short second. Applied silently (no public announcement) reflects the covert nature of market manipulation. Crit success doubles the reduction (−2 native). Failcrit PS −1 represents the institutional embarrassment of a failed financial maneuver.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Economic disruption — direct native resource reduction; "short" framing aligns with Syndicate market interference doctrine; Intel restriction enforces prior intelligence requirement | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×2; Intel restriction creates STD.CA.5→SYN.CA.2 two-step; "applied silently" protocol outstanding (Outstanding Issue); 04-n14 redesign flag | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — covert market interference is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Remove/NativeResource — direct supply reduction | Art 04b §4, §5 |
| Balance | ✓ | Capital×2, threshold 50; Intel prereq adds secondary cost; "applied silently" and floor confirmation outstanding (Outstanding Issues) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: native resource reduced at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; failcrit PS −1 is game effect (not portrait), per DIR.PA.2 | Art 04 §6.2; Art 02 §11 |
| Supported by zones | ✓ | target_district = None — faction-targeted, not district-targeted | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken restriction; NativeResource target; "applied silently" protocol outstanding (Outstanding Issue) | Art 02 §6–§8; Art 02 §11 |
| Supported by game procedure | ✓ | Beat 3 d100; Intel check at Dispatch; silent application and floor outstanding (Outstanding Issues) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **"Applied silently" protocol:** SYN.CA.2 reduces native resource "silently" — the table does not see the effect. Confirm: does ARBITER privately notify the target, or is the loss simply applied to their resource pool with no notification? Distinction matters for game integrity.
- **Floor at minimum 0:** `success = faction(target).resource.native -= 1 # minimum 0` — confirm ARBITER applies a floor of 0 and any excess is simply absorbed without penalty.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
SYN.CA.2 = Card(
    id      = "SYN.CA.2",  version="v1.0",
    name    = "Short the Market",
    tagline = "Reduce a faction's native resource generation for one round.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Remove,  subject = NativeResource,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10},
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction(named_opponent), target_object=NativeResource,
    target_taxonomy=None,
    affinity=None,
    restriction = intel(faction=faction(target), age_rounds<=1) >= 1,
    cost        = resource.faction(acting).capital * 2,
    success     = faction(target).resource.native -= 1,  # minimum 0; applied silently
    successcrit = faction(target).resource.native -= 2,  # minimum 0
    fail=None,
    failcrit    = faction(acting).standing -= 1,
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},
    narrative   = "Capital can suppress as easily as it can produce.",
    perspectives = {Syndicate: "We are not destroying their capacity. We are adjusting market conditions temporarily."},
    design_note  = None,
    arbiter_note = None,
)
```

---

### SYN.CA.3 — HOSTILE ACQUISITION
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's structure takeover card — Capital purchases ownership of an opponent's structure block, transferring it to Syndicate along with the district's native resource compensation to the dispossessed faction. The most expensive Syndicate base card at Capital×5, reflecting that acquiring built infrastructure is a major transaction. The "fair offer" framing in the narrative — Syndicate pays, target receives a resource — positions this as market-legal rather than theft. Guild Protection (GUI.CA.1 active in district) creates a doctrinal carve-out: when Guild has actively asserted its structural permanence in the district, Syndicate cannot override it this round. Successcrit returns Capital×1 (financial efficiency on the acquisition). Failcrit PS −1: a publicly failed acquisition damages Syndicate's financial reputation.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Structure takeover — Capital purchases ownership with compensation; "fair offer" framing positions this as market-legal; Guild Protection carve-out for doctrinal symmetry | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×5 highest base cost; compensation to target; GUI.CA.1 Guild Protection interaction outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — structure ownership purchase is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Redirect/StructureBlock — ownership transfer | Art 04b §4, §5 |
| Balance | ✓ | Capital×5, threshold 50, permanent transfer; compensation mechanics and GUI.CA.1 interaction outstanding (Outstanding Issues) | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent: structure ownership transferred; compensation delivered once at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; failcrit PS −1 is game effect (not portrait), per DIR.PA.2 | Art 04 §6.2; Art 02 §11 |
| Supported by zones | ✓ | target_district = district.any — presence-free acquisition | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock transfer; NativeResource compensation; GUI.CA.1 interaction outstanding (Outstanding Issue) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 d100; ARBITER re-assigns structure ownership; GUI.CA.1 active-state visibility outstanding (Outstanding Issue) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **C11 Guild Protection interaction:** Restriction excludes acquisition when `C11.active(district(target), round=game.round)` — confirm C11's "active" state is visible to ARBITER at Beat 3 and that this interaction is symmetrical (C11 blocks C33, but C33 does not block C11 playback in same round).
- **Compensation mechanics:** `game.dispatch(faction(target), resource.faction(target).native * 1)` delivers 1 native to the dispossessed faction. Confirm this is the target faction's native resource type (not Syndicate's), and that the delivery is immediate.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
SYN.CA.3 = Card(
    id      = "SYN.CA.3",  version="v1.0",
    name    = "Hostile Acquisition",
    tagline = "Purchase ownership of an opponent's structure.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Redirect,  subject = StructureBlock,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10},
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any, target_faction=faction(named_opponent), target_object=StructureBlock,
    target_taxonomy=None,
    affinity=None,
    restriction = (
        district(target).faction(target).structure >= 1
        AND NOT (faction(target) == Guild AND C11.active(district(target), round=game.round))
    ),
    cost        = resource.faction(acting).capital * 3 + resource.faction(acting).findings * 1 + resource.faction(acting).exposure * 1,
    success     = (
        game.transfer(district(target).faction(target).structure(1), faction(acting)),
        game.dispatch(faction(target), resource.faction(target).native * 1),
    ),
    successcrit = resource.faction(acting).capital += 1,
    fail=None,
    failcrit    = faction(acting).standing -= 1,
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},
    narrative   = "Everything in New Meridian has a price. The Syndicate is the only faction honest about this.",
    perspectives = {Syndicate: "We made a fair offer. The market determined the value. We accepted the market's judgment."},
    design_note  = None,
    arbiter_note = None,
)
```

---

### SYN.CA.4 — GOLDEN PARACHUTE
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's bribe card — pays a named faction to nullify their Beat 3 operations against Syndicate. Capital is declared at Dispatch, validated at Beat 0 (retained with card, not drained to Reservoir), and distributed at Beat 2 across the target faction's Beat 3 ops that target Syndicate in submission order until exhausted. At Beat 3: any operation with full Capital coverage is voided and the Capital returns to that faction's case; partial coverage attaches a −50 threshold marker. If the target faction submitted no operations against Syndicate, the Capital arrives in their return case as an unexplained windfall — the bribe worked, or was unnecessary. Either way, the Capital is gone from Syndicate's pool.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Bribe mechanic — Capital always reaches target faction; nullification is conditional on their submitted ops | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective — positional wager is doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Beat 2 Automatic; Capital retained with card (not drained); target_faction = bribe recipient; wager structure (positional vs. faction) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Protect/NativeResource — Capital expenditure protects Syndicate assets from named faction's ops | Art 04b §4, §5 |
| Balance | ✓ | Variable cost 1–N declared at Dispatch; cost is the effect vehicle — goes to target regardless of outcome; over-payment is wasted Capital | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: Capital distributed at Beat 2, void/partial resolved at Beat 3 | — |
| Persistence | ✓ | Immediate — fully resolved by end of Beat 3 | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; player judgment on whether to submit | — |
| Portrait validity | ✓ | Syndicate +1 submitter — positional wager aligns with capital doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted | Art 01 §6–§7 |
| Supported by components | ✓ | Capital retained with card at Beat 0; distributed Beat 2; returned to target_faction at Beat 3 | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 0 Retained validation; Beat 2 distribution procedure; Beat 3 capital-on-card void/partial — all defined in Art 03 | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

*None.*

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Pre-convention card — design rationale scaffold added S59. Full redesign S65.*

```python
SYN.CA.4 = Card(
    id      = "SYN.CA.4",  version="v2.0",
    name    = "Golden Parachute",
    tagline = "Declare a bribe. Their operations against you are covered. Windfall or nullification — the Capital leaves either way.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Protect,  subject = NativeResource,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district = None, target_faction = faction(named), target_object = None,
    target_taxonomy=None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(acting).capital * declared(N, min=1),  # retained with card at Beat 0 — does not drain to Reservoir
    success         = game.bribe(capital=declared(N), target=faction(target), against=faction(acting), beat3_ops_first_to_last=True),
    successcrit     = None, fail=None, failcrit=None,
    portrait        = {Syndicate: PortraitEntry(submitter=+1)},
    narrative       = "The Syndicate does not wait to find out. They price the outcome in advance.",
    perspectives    = {Syndicate: "We did not lose those resources. We placed them where the problem would be. There is a difference."},
    design_note     = "Capital declared at Dispatch on target profile. Beat 0: retained (not drained). Beat 2: distributed across target_faction Beat 3 ops targeting Syndicate, first-to-last, until exhausted. Beat 3: full coverage = void + Capital to submitter case; partial = −50 marker + Capital to submitter case. No ops from target_faction = windfall to return case. Wager structure: Syndicate bets positionally — wrong bet wastes Capital, correct bet nullifies threat Cost reasoning: Exposure and Findings identify the target's vulnerabilities and legitimize the aggressive posture.",
    arbiter_note    = "See Art 03 Beat 0 (Retained validation), Beat 2 (Golden Parachute procedure), Beat 3 Step 1.4 (capital-on-card resolution).",
)
```

---

### SYN.CA.5 — REGULATORY CAPTURE
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's submission-layer blocking card — analogous to DIR.CA.1 Invoke Jurisdiction (Directorate) but broader in scope and more expensive. Where DIR.CA.1 is limited to STD.CA.1/STD.CA.3, Regulatory Capture blocks any named action type in a district for one round. This flexibility reflects Syndicate's financial reach into regulatory structures. Capital×3 at Beat 2 Automatic with public announcement makes it a visible table signal — everyone knows Syndicate has blocked this action type. The portrait entry with modifier=-2 when targeting a Guild-primary action type captures the doctrinal tension: buying regulatory outcomes is precisely what Guild's permanence doctrine opposes.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Broad submission-layer block — Capital buys regulatory control over any named action type; broader than DIR.CA.1 (Directorate, STD.CA.1/STD.CA.3 only); public announcement makes it a visible table signal | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design — regulatory capture as market governance | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×3; public announcement; Guild-primary portrait modifier outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — regulatory purchase is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Submission/Block/NamedActionType — NamedActionType definition outstanding (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | Capital×3 vs DIR.CA.1's Mandate×2; breadth calibration and NamedActionType scope outstanding (Outstanding Issues) | Art 02 §6–§7 |
| Effect duration | ✓ | One round: block applies for round=game.round only | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 positional wager fires on submission | — |
| Portrait validity | ✓ | Syndicate +1 submitter with modifier=−2 for Guild-primary action type; firing conditions outstanding (Outstanding Issue) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any; ChorusNode excluded | Art 01 §6–§7 |
| Supported by components | ✓ | NamedActionType definition outstanding (Outstanding Issue); no new physical components | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; named action type blocked for round; public announcement by ARBITER | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **`NamedActionType` definition:** What constitutes a "named action type" — is this a card name (e.g., "STD.CA.1"), a taxonomy function (e.g., "Add — StructureBlock"), or a broader category (e.g., "Build")? The breadth of the block changes significantly based on this definition.
- **portrait modifier=-2 for Guild-primary action:** `mod_where=action_type(named).primary_faction == Guild` — confirm "primary_faction" is a defined property of action types, or if this needs to be a player declaration at submission.
- **Comparison to DIR.CA.1:** SYN.CA.5 is explicitly broader than DIR.CA.1 at a 1-Mandate premium. Ensure the gap is documented in design notes for balance review.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
SYN.CA.5 = Card(
    id      = "SYN.CA.5",  version="v1.0",
    name    = "Regulatory Capture",
    tagline = "Block a specific action type in a named district for one round.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Submission,  function = Block,  subject = NamedActionType,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any, target_faction=None, target_object=NamedActionType,
    target_taxonomy=None,
    affinity=None,
    restriction = district(target) != ChorusNode,
    cost        = resource.faction(acting).capital * 2 + resource.faction(acting).exposure * 1,
    success     = game.block(district(target), action_type=named, round=game.round, public=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Syndicate: PortraitEntry(submitter=+1, modifier=-2, mod_where=action_type(named).primary_faction == Guild)},
    narrative   = "If you own enough of the regulatory structure, you define what is permitted. The Syndicate does not see this as corruption. They see it as governance.",
    perspectives = {Syndicate: "The regulatory framework exists. We simply ensure it reflects current market conditions."},
    design_note  = None,
    arbiter_note = None,
)
```

#### Syndicate Gap Concepts — Design Notes

Three capability gaps identified in Artifact 04b §8.4: zero information/intelligence capability; Cross-Category — Corrupt — Accord unused; Resource — Redirect — Accord unused. Concepts below are placeholders for slot assignment and detail design. No full data structure — see D-04-05.

**ALTER THE RECORD** — Cross-Category — Corrupt — Accord agreement.
Design note: Syndicate modifies one numeric value in a registered Accord (Capital, presence, or term). ARBITER records the alteration. Both parties notified by case. Value of this card is that alterations are ARBITER-logged — deniable to the table, visible to the record. Addresses Corrupt — Accord gap. Requires Accord mechanic (Artifact 06) to be finalized before detail design.

**SECONDARY OBLIGATIONS** — Resource — Redirect — Accord agreement.
Design note: Transfer an Accord's obligations from the original party to a named faction. The named faction inherits all terms; original party released. Source faction gains 1 Capital at transfer. Neither party's consent is required — Syndicate controls the paper, not the relationship. Addresses Resource — Redirect — Accord gap. Requires Accord mechanic finalized before detail design.

**PORTFOLIO REVIEW** — Cross-Category — Reveal — Intel tokens held.
Design note: Name a faction; ARBITER announces that faction's current Intel token count to acting faction only (private). Syndicate may immediately offer to purchase one token from that faction at 3 Capital — target faction may decline. Provides Syndicate an information entry point without requiring field presence. Addresses zero information/intelligence gap.

### Syndicate — LAND TITLE
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Land Title files a capital claim on undeveloped land — no faction holds a structure block there yet. The card delivers a Grant Deed (ARBITER-issued card, placed in Syndicate's Dispatch Case, moves to hand at Debrief). Grant Deed is a tripwire React card Syndicate holds until another faction builds in the named district, at which point the deed fires. No board marker from this card; no ongoing ARBITER monitoring. Distinct from SYN.CA.1 Leveraged Acquisition (transactional per-round income): Land Title is a positional play — Syndicate reads the board, registers claims on districts likely to develop, then reacts when the trigger fires. Multiple Grant Deeds on the same district are permitted; cost-governed.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Capital claim on undeveloped district; delivers Grant Deed to hand | Art 00 §7 |
| Voice fit | ✓ | Syndicate-only; paper before patrols | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; undeveloped districts only; ChorusNode excluded; multiple deeds permitted (cost-governed) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Add/StructureBlock — ultimate effect is Syndicate structure placed via Grant Deed | Art 04b §4, §5 |
| Balance | ✓ | Capital×5 per deed; payback contingent on opponent building in target district | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent — Grant Deed held until played or game end | — |
| Trigger validity | ✓ | N/A — trigger = None on this card | — |
| Portrait validity | ✓ | Syndicate +1 submitter | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; ChorusNode excluded | Art 01 §6–§7 |
| Supported by components | ✓ | Grant Deed = new component (SCIF-pattern); stored blank in ARBITER tableau; no marker placed by this card | Art 02 §6–§8 |
| Supported by game procedure | ⚠ | Grant Deed tripwire react window needs Art 03 procedure addition (04-n27 territory) | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Grant Deed tripwire react window:** "immediately after structure block placed, before any other board state change" — this react class is not yet in Art 03. Tracks under 04-n27.
- **Grant Deed component registration:** New component; needs Art 02 entry (SCIF-pattern: blank card stored in ARBITER tableau, fields: `district | owner`). Tracks under 04-n26.
- **Governing Rule 8.2 interaction on Grant Deed fire:** If Syndicate already holds a structure block in the named district when the deed fires, step 3 (place Syndicate structure) is blocked by Governing Rule 8.2. Steps 1–2 still execute. No card-level restriction needed — Governing Rule 8.2 governs.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Redesigned S67 — v2.0*

```python
LandTitle = Card(
    id      = "SYN.CA.8",  version="v2.0",
    name    = "Land Title",
    tagline = "File a capital claim on undeveloped land. Let someone else build. Then collect.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Add,  subject = StructureBlock,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None,
    trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.named, target_faction=None, target_object=None,
    target_taxonomy=None,
    affinity=None,
    restriction = (
        district(target).structure_count == 0
        AND district(target) != ChorusNode
    ),
    cost        = resource.faction(acting).capital * 5,
    success     = arbiter.dispatch(GrantDeed(district=district(target)), faction(acting).case),
    successcrit = None,  fail=None,  failcrit=None,
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},
    narrative   = "The deed was filed before the foundation was poured. That is how the Syndicate prefers it.",
    perspectives = {Syndicate: "We don't need to be there. We just need to be on the paperwork."},
    design_note  = "Delivers Grant Deed component (ARBITER tableau → Syndicate case → hand at Debrief). Grant Deed is a tripwire React played from hand when any faction places a structure block in the named district. No board marker from this card. Automatic resolution — no crit or fail. Multiple deeds permitted; cost-governed. Governing Rule 8.2 governs step 3 of Grant Deed effect Cost reasoning: Exposure forces the targeted individuals out of the shadows, making the extraction inevitable.",
    arbiter_note = "Take 1 blank Grant Deed from ARBITER tableau. Write target district name. Place in submitting faction's Dispatch Case. Grant Deed moves to Syndicate hand at Debrief.",
)
```

---

### Syndicate — HOSTILE TAKEOVER
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's presence absorption card — distinct from SYN.CA.3 Hostile Acquisition (which targets structure blocks). Hostile Takeover purchases an opponent's community presence and replaces it with Syndicate presence at the same tier, instantly swinging district control without demolition. The Intel token requirement establishes a Ghost-Syndicate structural link: Syndicate cannot execute a takeover without prior intelligence on the target. Capital×4 + Intel reflects the combined financial and intelligence investment required. The net effect on the district's control tier is neutral — same count of tokens, different faction — making this a covert displacement rather than a destructive act. Successcrit returns 1 Capital (efficient acquisition). Failcrit NotificationSlip to target: a failed takeover attempt alerts the target.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Presence absorption — control swing without demolition; displaces target presence and replaces with Syndicate at equivalent tier; distinct from SYN.CA.3 (StructureBlock) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design — acquisition of relationships, not displacement | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×4 + IntelToken; Ghost-Syndicate structural link; token supply and void-on-Absent outstanding (Outstanding Issues) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — presence absorption is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Add/PresenceToken — replaces target presence at same count | Art 04b §4, §5 |
| Balance | ✓ | Capital×4 + IntelToken, threshold 50; dual cost vs SYN.CA.3 (Capital×5 only); token replacement count outstanding (Outstanding Issue) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: presence tokens replaced at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; failcrit NotificationSlip is game effect (not portrait), per DIR.PA.2 | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken transfer; IntelToken cost; token supply source and void-on-Absent outstanding (Outstanding Issues) | Art 02 §6, §8; Art 02 §11–§12 |
| Supported by game procedure | ✓ | Beat 3 d100; ARBITER replaces tokens; void-on-Absent resolution outstanding (Outstanding Issue) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Token replacement count:** At resolution, ARBITER replaces ALL of target's presence tokens in the district with Syndicate tokens at the same count. Confirm: if target is Dominant (3 tokens), Syndicate places 3 tokens and target drops to Absent. Does Syndicate need those tokens in reserve, or does ARBITER provide them from supply?
- **Self-takeover of Absent district:** If target reaches Absent between Dispatch and Beat 3 resolution (e.g., from a prior Beat 3 action this round), the restriction `presence >= 1` fails at resolution — confirm card is void (slot + resources lost) or triggered on Dispatch state.
- **Ghost-Syndicate link:** This card creates the structural link between Ghost's Intel collection and Syndicate's high-end plays. Confirm with Ghost players that faction-keyed Intel token mechanics are compatible (Ghost generates Syndicate-keyed Intel; Syndicate can purchase or trade for it).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Draft S59 — design pass pending*

```python
HostileTakeover = Card(
    id      = "SYN.MOD.8",  version="v1.0",
    name    = "Hostile Takeover",
    tagline = "Purchase control of a faction's community presence in a district, replacing their tokens with Syndicate's at equivalent tier.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Add,  subject = PresenceToken,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10}, doctrine_mod=None,
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.named, target_faction=faction(named_opponent), target_object=PresenceToken,
    target_taxonomy=None,
    affinity=None,
    restriction = (
        faction(target).presence(district(target)) >= 1
        AND faction(acting).intel_tokens(faction=faction(target)) >= 1
    ),
    cost        = resource.faction(acting).capital * 3 + resource.faction(acting).mandate * 2,
    success     = game.replace_presence(
        faction(target), district(target),
        with_faction=faction(acting),
        count=faction(target).presence_count(district(target)),
    ),
    successcrit = resource.faction(acting).capital += 1,
    fail=None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},
    narrative   = "The Syndicate does not displace people. It acquires their positions. There is a difference, legally speaking.",
    perspectives = {Syndicate: "We purchased the relationship. The people can stay. Their affiliation is now ours."},
    design_note  = "Distinct from SYN.CA.3 Hostile Acquisition (StructureBlock). Replaces ALL target presence in district with Syndicate presence at same count (same control tier — neutral effect on tier, swing in ownership). Requires Ghost-sourced faction-keyed Intel token. Intel token creates structural link between Ghost and Syndicate — neither faction announces it publicly.",
    arbiter_note = "At resolution: count target's presence tokens in district. Remove all of them. Place equal count of Syndicate presence tokens in same district. Net tier unchanged; ownership transferred. Deliver NotificationSlip to target on crit fail. Crit success: +1 Capital to Syndicate.",
)
```

---

### SYN.CA.10 — ACCORD TRANSFER
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's party-substitution card — the mechanism by which every bilateral agreement becomes a potential Syndicate asset. Replaces one named party in an active Accord with any faction (including Syndicate itself), without either party's consent. ARBITER makes the physical alteration on the Accord form and announces the change publicly at Beat 3. On crit success, the incoming party gains a renegotiation right: one numeric term of their choosing is altered at the table. This gives the involuntarily inserted party a single concession — the transfer comes with a term adjustment. Completes the Accord manipulation suite with SYN.CA.11 Redline (Terms). Supersedes gap concept SECONDARY OBLIGATIONS.

#### Card Story
A form that has been in the Accord Placement Area since Debrief is quietly updated between beats. ARBITER announces the change at Beat 3 resolution. The parties to the original agreement have already moved on.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Accord party replacement without consent; fills Economy\|Corrupt\|AccordCard Syndicate gap; distinct from SYN.CA.11 (Terms) and SYN.CA.3 (StructureBlock redirect); supersedes SECONDARY OBLIGATIONS gap | Art 00 §7 |
| Voice fit | ✓ | FactionSpecific Syndicate; full perspectives block; "restructured who holds it" is on-voice | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital(3); no consent required (confirmed — Art 06 §9.10 signed off L205); Syndicate may be outgoing or incoming party | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy\|Corrupt\|AccordCard — party names on Accord form are written records; replacement is a Corrupt operation on the document (taxonomy corrected S107 L227 from Redirect) | Art 04b §4, §5 |
| Balance | ⚠ | d100 threshold 50 with high-impact consent-free effect; crit renegotiation right for incoming party adds table interaction; flag for doctrine review | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent board state change (Accord form altered, stays active); card itself is Immediate | — |
| Persistence | ✓ | Immediate — no lingering card-as-condition | Art 04 §6 |
| Portrait validity | ✓ | flat entries only; submitter-bounded; no direct Portrait track shift in effect fields | Art 04 §6.2 |
| Supported by zones | ✓ | Accord Placement Area (Art 01); Target Profile in Dispatch Case (covert path) | Art 01 §6–§7 |
| Supported by components | ✓ | AccordCard/AccordForm (Art 06 §9); Target Profile DB:48 with declared_params (Art 02 v2.4 — L233); Dispatch Case (Art 02) | Art 02; Art 06 §9 |
| Supported by game procedure | ✓ | Beat 3 covert d100; Art 06 §9.10 Alter/Named Party governs physical alteration; Art 06 §9.10 Alter/Terms governs crit term change (incoming party elects at table); ARBITER announces success publicly | Art 03 §9, §11; Art 06 §9.10 |
| Data schema validation | ✓ | All fields per §6.1/§6.2 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story present | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Four paths (success / crit success / fail / failcrit) each has exactly one outcome | Art 04 §5 P27 |
| Resource cost positioning | Is this card's cost mono-resource (acting faction's own native resource only) or cross-faction-resource (two or more distinct native resources)? Confirm power level matches: mono-resource = floor-power; cross-faction-resource = ceiling-power. Flag if mono-resource and high-power, or cross-resource and underpowered. If cost generates non-native resources as an effect, flag — requires doctrine justification. *(P28)* | Art 00a §9.2 |

#### Outstanding Issues

- **Balance:** Threshold 50 with consent-free, permanent Accord restructuring is high-impact. Crit renegotiation right for incoming party is untested — could create unexpected table dynamics. Flag for doctrine review.
- **Incoming party renegotiation constraint:** On crit success, incoming party may alter "any" numeric term — no restriction stated on which clause or by how much. Consider whether to bound the new value (e.g., within clause-type vocabulary per Art 06 §9.3) or leave fully free. Non-blocking — Art 06 §9.3 clause vocabulary applies implicitly.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ⚠ | |

*v0.1 — S111: full design pass replacing S59 stub. Art 06 §9.10 signed off (L205); taxonomy corrected (L227). Issues Resolved pending balance doctrine review.*

```python
SYN.CA.10 = Card(
    card_id      = "SYN.CA.10",  version = "v0.1",
    name     = "Accord Transfer",
    tagline  = "All terms remain binding. The signatories have been updated.",
    type     = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,

    layer    = Economy,  function = Corrupt,  subject = AccordCard,

    beat         = 3,
    resolution   = d100,
    threshold    = 50,
    ring_mod     = None,
    doctrine_mod = None,

    target_district = None,
    target_faction  = faction(outgoing_party),
    target_object   = AccordCard(state=active, party=target_faction),
    declared_params = (
        incoming_party = faction(any),
        # written on TP declared-parameters line at Covert Dispatch
        # may be Syndicate (self-insertion or self-exit) or any other faction not
        # already a named party on the target Accord
    ),

    affinity    = None,
    restriction = (
        target_object.state == active
        AND target_faction in target_object.parties
        AND declared_params.incoming_party not in target_object.parties
    ),
    cost     = Capital(3),
    boost    = None,

    success = target_object.alter(
        type     = NamedParty,
        outgoing = target_faction,
        incoming = declared_params.incoming_party,
    ),
    # ARBITER strikes outgoing_party on Accord form; writes incoming_party.
    # All obligations and benefits transfer. Accord remains active.
    # ARBITER announces to table: "[Outgoing] replaced by [Incoming] on [Accord]."
    # Art 06 §9.10 Alter/Named Party. No consent required from either party.

    successcrit = faction(declared_params.incoming_party).player.elect(
        target_object.alter(type=Terms, clause=any_numeric, new_value=player_chosen_int),
    ),
    # delta only: named party change (from success) + incoming party elects one
    # numeric term alteration at the table immediately after ARBITER announcement.
    # Incoming party names the clause row and states the new integer value;
    # ARBITER makes the physical alteration per Art 06 §9.10 Alter/Terms.

    fail        = None,
    failcrit    = faction(acting).standing -= 2,
    # no Accord change; cost spent; acting faction announced publicly (Discovery)

    on_accept  = None,
    on_decline = None,

    persistence           = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    portrait = {
        Syndicate:   PortraitEntry(flat=+1),
        Network:     PortraitEntry(flat=-1),
        Directorate: PortraitEntry(flat=-1),
    },

    narrative = "The form in the Accord Placement Area is updated. The parties to the original agreement learn about it at the same time as everyone else.",

    perspectives = {
        Syndicate:   "The agreement was always an asset. We've restructured who holds it.",
        Ghost:       "The Accord changed hands without a handshake. The power to do that is worth understanding.",
        Network:     "A binding agreement — restructured by someone who wasn't party to it, without notice. This is what unaccountable capital does.",
        Directorate: "A covert restructuring of a binding agreement. The incoming party is now bound. Noted.",
        Guild:       "Agreements don't restructure themselves. Someone just demonstrated they can override the process.",
    },

    design_note  = "Completes the Accord manipulation suite with SYN.CA.11 Redline: CA.10 controls who is bound; CA.11 controls what the terms say. Economy|Corrupt|AccordCard — party names on the Accord form are written records; replacement is a Corrupt operation. ARBITER makes the physical alteration at Beat 3 per Art 06 §9.10 and announces publicly (the change is public; the acting faction remains covert). No consent required from either party (Art 06 §9.10, L205). Outgoing_party may be Syndicate (self-exit, forcing obligations onto incoming party). Incoming_party may be Syndicate (self-insertion to acquire another faction's Accord position). Restriction: incoming_party not already a named party on the same Accord. Crit success: incoming party — the involuntarily inserted faction — elects one numeric term change at the table; gives them a single renegotiation concession. Supersedes SECONDARY OBLIGATIONS gap concept.",
    arbiter_note = "Covert Dispatch: acting faction writes on TP declared-parameters line: incoming party. Beat 0: verify restriction — outgoing party is named on target Accord; incoming party is not. Beat 3: roll d100. On success (≤50): locate Accord form in Accord Placement Area; strike outgoing party name; write incoming party name; announce to table: '[Outgoing] replaced by [Incoming] on [Accord]. All terms now bind [Incoming].' On crit success (01–05): apply named party change as above; then address incoming party player: 'You may alter one numeric term in this Accord — name the clause and state the new value.' Apply declared change per Art 06 §9.10 Alter/Terms. On fail: no effect; cost spent. On failcrit (96–00): no Accord change; announce acting faction publicly; apply Syndicate −2 PS.",
)
```

---

### Syndicate — PARASITIC
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's economic intelligence tap — a positional wager on district activity. At Beat 2, Syndicate bets that someone is already operating in the target district this round. ARBITER checks the Beat 3 dispatch queue; if a Beat 3 card targeting the district exists, Syndicate receives an Intel token keyed to that card's submitting faction (first in resolution order). If no one is operating there, the card fails and Capital is spent. The wager rewards Syndicate for reading the board correctly before operations fire — not for monitoring what happens, but for knowing what's coming. Covert — other factions cannot observe the tap.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intel from reading opponent dispatch queue — positional wager on district activity before Beat 3 fires | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective — infrastructure that reads commerce before it happens | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×2; positional wager; payoff requires correct district read; covert | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/IntelToken — Intel from district activity read | Art 04b §4, §5 |
| Balance | ✓ | Capital×2; fail = cost spent; payoff contingent on opponent operating in district this round | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — resolved fully at Beat 2; no carry, no deferred effects | — |
| Persistence | ✓ | Immediate — no game-state marker persists beyond Beat 2 resolution | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 3 queue check is resolution condition, not a trigger | — |
| Portrait validity | ✓ | Fires on success (Intel delivered); unconditional on success — no mod_where needed | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — Intel token from standard stock | Art 02 §6–§8 |
| Supported by game procedure | ⚠ | ARBITER Beat 3 queue check at Beat 2 resolution — procedure not yet in Art 03 §9.4. Tracks under 04-n27. | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Art 03 Beat 2 procedure:** ARBITER checking the Beat 3 dispatch queue at Beat 2 resolution is not yet proceduralized in Art 03 §9.4. Tracks under 04-n27.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Redesigned S67 — v2.0. Positional wager replacing deferred conditional. No component needed.*

```python
SYN.CA.6 = Card(
    id      = "SYN.CA.6",  version="v2.0",
    name    = "Parasitic",
    tagline = "Wire a district's commerce. Let others do the work.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,

    layer   = Economy,  function = Add,  subject = IntelToken,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Positional wager",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.named,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).capital * 2,

    success     = arbiter.dispatch(
                    IntelToken(faction=game.ops(beat=3, at=district(target)).first(resolution_order).submitter),
                    faction(acting).case
                  ),
    successcrit = None,

    portrait    = {Syndicate: PortraitEntry(submitter=+1)},

    narrative    = "The Syndicate does not steal from the river. They build a weir.",
    perspectives = {Syndicate: "We invested in the district's infrastructure. Why shouldn't we see what moves through it?"},

    design_note  = "Positional wager — resolved fully at Beat 2. ARBITER checks Beat 3 dispatch queue for any card targeting district(target). If found: Intel token keyed to the submitting faction of the first card in resolution order delivered to Syndicate's case. If no Beat 3 card targets the district: cost spent, no effect. Covert — other factions cannot observe.",
    arbiter_note = "At Beat 2 resolution: check Beat 3 dispatch queue for any card targeting district(target). If found: deliver IntelToken keyed to that card's submitting faction (first in resolution order) to Syndicate's case; portrait fires. If none found: cost spent, no effect, portrait does not fire. Covert — do not announce.",
)
```

---

### Syndicate — CORPORATE BLACKMAIL
[↑ Covert Operations](#syndicate-covert-operations)

*Split S70 per PM05 04-n47 (choose_one violation) and 04-n48. Card A (Capital coercion) below. Card B (forced Accord vote) stub follows — mechanics deferred to future session.*

---

### SYN.CA.7 — CORPORATE BLACKMAIL
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate uses covertly gathered intelligence to threaten a faction operating in a named district. ARBITER delivers the blackmail notice privately to the target at Beat 3 — notification is covert, not public. The target faces a binary choice: comply (pay resources and keep their position) or resist (accept consequences). Either way, Syndicate pays a PS cost — operating this way corrodes institutional relationships regardless of outcome. Distinct from SYN.CA.1 Leveraged Acquisition: SYN.CA.1 is transactional extraction (pays Capital, receives native output without interaction); SYN.CA.7 is coercive leverage (threatens loss to extract compliance from a specific target at a specific position).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intel-to-compliance coercion; target choice (pay or suffer) replaces forced transfer; presence restriction grounds the threat in a real position | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; IntelToken cost; flat portrait −1 self-cost; target_district added (S71) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Redirect/NativeResource — compliance payment or presence loss at target district | Art 04b §4, §5 |
| Balance | — | Comply cost (resource amount) TBD; resist consequence (presence tier loss + PS −1) outstanding | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate at Beat 3 resolution | — |
| Persistence | ✓ | Immediate — no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Syndicate flat=−1 regardless of outcome — schema validation outstanding | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — presence restriction is district-specific | Art 01 §6–§7 |
| Supported by components | — | Comply path: resource transfer (amount TBD). Resist path: presence tier reduction + PS — components confirmed; amount outstanding | Art 02 §6–§8 |
| Supported by game procedure | — | Beat 3 covert ElectPlayer: ARBITER whispers to target; target elects comply/resist. No existing Art 03 procedure for covert notification + choice at Beat 3. New procedure required before Issues Resolved. | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Comply resource amount:** What does the target pay on compliance? Suggest 2 native of target district (parallel to SYN.CA.1 output rate). Confirm type and amount.
- **Resist consequence — presence loss:** "Lose influence" interpreted as lose 1 presence tier at target_district. Confirm: tier loss vs. token count loss.
- **Covert ElectPlayer procedure:** No Art 03 procedure exists for covert notification + player choice at Beat 3. Must be written as generalizable procedure. Issues Resolved blocked until written.
- **Flat portrait modifier:** `portrait = {Syndicate: PortraitEntry(flat=-1)}` — confirm "flat" is valid schema field. Flag for schema pass if not.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*v2.0 — S71: full redesign. Forced transfer replaced with coercive choice (ElectPlayer). target_district added. Restriction: target presence > 0 at district. Comply/resist model. Covert notification procedure outstanding.*

```python
SYN.CA.7 = Card(
    id      = "SYN.CA.7",  version="v2.0",
    name    = "Corporate Blackmail",
    tagline = "Submit covertly. The target decides what compliance costs less.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Redirect,  subject = NativeResource,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=ElectPlayer,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district = district.named,
    target_faction  = faction(named_opponent),
    target_object   = None,
    target_taxonomy=None,
    affinity        = None,
    restriction     = faction(target).presence(district(target_district)) > 0,
    cost            = IntelToken(any) * 1,

    success     = None,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    # ElectPlayer — ARBITER notifies target privately at Beat 3 resolution
    on_accept  = faction(target).resource(native) -= 2,  # amount TBD; placeholder 2 native
    on_decline = (
        faction(target).presence_tier(district(target_district)) -= 1,
        faction(target).standing -= 1,
    ),
    # always: faction(acting).standing -= 1 regardless of outcome (encoded in portrait flat=-1)

    portrait    = {Syndicate: PortraitEntry(flat=-1)},
    narrative   = "The information was gathered properly. What is done with it is simply business.",
    perspectives = {Syndicate: "We don't call it blackmail. We call it an incentive structure with consequences attached."},
    design_note  = "Covert submission; private notification at Beat 3 (ARBITER whispers to target — not public). Target elects comply or resist. Comply: pay resources (amount TBD). Resist: presence tier −1 at target district + PS −1. Syndicate PS −1 always. Covert ElectPlayer procedure required in Art 03 before Issues Resolved.",
    arbiter_note = "Beat 3: whisper privately to target faction — inform them of blackmail attempt. Target elects comply or resist (not announced publicly). On comply: transfer [X native TBD] from target to Syndicate. On resist: reduce target's presence tier at named district by 1; reduce target PS by 1. Regardless of outcome: reduce Syndicate PS by 1.",
)
```

---

### Syndicate — ACCORD LEVERAGE *(placeholder name)*
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate converts gathered intelligence into a forced Accord commitment. The Intel token is the leverage; the effect fires during the Beat 4 Accord formation window. The target cannot negotiate amendments, decline, or counter-propose — they accept the draft as written. Uses Art 06 §9 Lock manipulation type. Distinct from SYN.CA.7 Corporate Blackmail (presence-based coercion in a district): The Fixer operates entirely in the Accord formation layer, with no district dependency. The target must be a named party to the Accord draft being locked.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence leverage applied to Accord formation — forces yes-vote on existing draft terms | Art 00 §7 |
| Voice fit | — | TBD — single Syndicate perspective minimum | Art 00 §7 |
| Doctrine alignment | — | Syndicate only; IntelToken cost; Art 06 §9 Lock interaction outstanding | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | ModActionCard — modifier applied to Accord formation window, not a CovertOperation | Art 04 §6.1, §6.2 |
| Taxonomy fit | — | Modifier card taxonomy — excluded from Layer/Function/Subject taxonomy | Art 04b §5.1, §9 |
| Balance | — | IntelToken × 1; effect = forced acceptance of existing Accord draft; scope and party requirements outstanding | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate at Beat 4 Accord formation | — |
| Persistence | ✓ | Immediate — Accord execution follows standard Art 06 §9 procedure once locked | Art 04 §6 |
| Trigger validity | — | Trigger = named Accord draft exists + not yet executed. Trigger confirmation outstanding. | Art 06 §9 |
| Portrait validity | — | TBD — modifier card portrait model | Art 04 §6.2 |
| Supported by zones | ✓ | No district dependency — Accord-layer effect only | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; AccordDraft as target object (registered Art 06 §9) | Art 02 §6–§8 |
| Supported by game procedure | — | Art 06 §9 Lock manipulation type covers forced acceptance in principle. Interaction between modifier card timing and Beat 4 Accord window not yet written. Procedure required before Issues Resolved. | Art 06 §9; Art 03 §9 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Art 03 procedure — modifier card in Accord window:** No procedure written for ModActionCard played during Beat 4 Accord formation. Must be written as generalizable rule before Issues Resolved.
- **Party requirement:** Must Syndicate be a named party to the target Accord? Expected yes — this is leverage, not arbitration. Confirm.
- **Scope after forced acceptance:** Can the target exercise any standard Accord rights after forced acceptance (dissolution, breach action), or are they fully bound as written? Clarify.
- **Lock type interaction:** Art 06 §9 Lock applies to a single manipulation within an existing Accord. Confirm whether "forcing acceptance of a draft Accord" is a Lock (modifying the target's vote) or a new manipulation category.
- **Card name:** Placeholder — confirm before sign-off.
- **Card ID:** TBD — pending PM05 04-n1 numbering pass.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*v1.0 — S71: redesigned as modifier card (Instant). Forced acceptance of Accord draft as written. Replaces deferred "forced Accord vote" stub from S70.*

```python
# STUB — full ModActionCard spec (effect, value_rating, ring_constraint, ring_origin) pending 09-06; Art 06 §9 Lock interaction outstanding
Card(
    id=TBD,  version="v1.0",
    name        = "The Fixer",  # placeholder
    type        = ModActionCard,  faction = Syndicate,
    beat        = 4,  # Accord formation window
    trigger     = AccordDraft(named).status == Draft,  # draft exists, not yet executed
    restriction = AccordDraft(named).party(faction(target)) == True,  # target is named party
    cost        = IntelToken(any) * 1,
    effect      = AccordDraft(named).lock(faction(target), accept_as_written=True),
    # Art 06 §9 Lock manipulation type — target cannot negotiate, decline, or counter-propose
    target_taxonomy=None,
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},  # TBD — modifier card portrait model
)
```

---

### SYN.CA.11 — REDLINE
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate quietly alters a numeric or ordinal fill-in value in an active Accord — a resource quantity, an influence tier, a Quarter deadline — while the form sits face-up in the Accord Placement Area. The effect is public (the altered form is visible to all players) but the actor is covert (ARBITER makes the physical change without identifying the submitting faction). Completes the Syndicate Accord manipulation suite: SYN.CA.10 Accord Transfer changes a named party; SYN.CA.11 Redline changes what the terms say. Fills the Information|Corrupt|AccordAgreement gap identified in Art 04b §8.3. Distinct from The Fixer modifier card (which forces acceptance of a draft, not alteration of an active one).

#### Card Story
A Syndicate operative approaches the Accord Placement Area during a recess. They adjust a number in one clause — a quantity, a tier, a deadline. The revision goes unquestioned. By the time anyone re-reads the terms carefully, the original number is simply what everyone thought they agreed to.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Information-layer Accord alteration; Syndicate "small print" doctrine; fills Information\|Corrupt\|AccordAgreement gap (Art 04b §8.3); distinct from SYN.CA.10 (named-party alteration) and The Fixer modifier (forced acceptance of draft) | Art 00 §7 |
| Voice fit | ✓ | FactionSpecific Syndicate; single Syndicate perspective; full perspectives block documented | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×2; covert; altering written agreements for positional advantage = Capital doctrine ("control comes from positioning early") | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/AccordAgreement — Accord clause fill-in values are physically written records; valid Corrupt target per §4.10/P24 | Art 04b §4, §5 |
| Balance | ✓ | Capital×2; threshold 50 (Average); restriction = active Accord present only; failcrit = Discovery; prospective clause alteration scales with Accord significance | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — one-time physical alteration; no persistent game-state marker; Accord persists with altered terms under its own lifecycle | — |
| Persistence | ✓ | Immediate — alteration committed at Beat 3; no persistence tracking required | Art 04 §6 |
| Trigger validity | ✓ | trigger = None; restriction gates on active Accord count checked at Beat 0 | — |
| Portrait validity | ✓ | flat entries only; submitter-bounded (Syndicate, Network, Directorate); no direct Portrait track shift in effect fields (DIR.PA.2); failcrit = Discovery (not a portrait entry) | Art 04 §6.2 |
| Supported by zones | ✓ | Accord Placement Area registered zone (Art 06 §9.5) | Art 01 §6–§7 |
| Supported by components | ✓ | AccordAgreement face-up in Accord Placement Area (Art 06 §9); Target Profile declared-parameters blank line added Art 02 §8 (S111) | Art 02 §6–§8; Art 06 §9 |
| Supported by game procedure | ✓ | Alter/Terms covert procedure: Art 06 §9.10 (covert op → ARBITER makes physical alteration); no new Art 03 step required | Art 06 §9.10 |
| Data schema validation | ✓ | All fields populated per §6.1/§6.2 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story present | Art 04 §5 P26 |
| Outcome determinacy | ✓ | One outcome per tier; no branching; successcrit additive on success; failcrit additive on fail | Art 04 §5 P27 |
| Resource cost positioning | Is this card's cost mono-resource (acting faction's own native resource only) or cross-faction-resource (two or more distinct native resources)? Confirm power level matches: mono-resource = floor-power; cross-faction-resource = ceiling-power. Flag if mono-resource and high-power, or cross-resource and underpowered. If cost generates non-native resources as an effect, flag — requires doctrine justification. *(P28)* | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*v0.1 — S111: new card, fills Information\|Corrupt\|AccordAgreement gap. Art 02 §8 Target Profile declared-parameters field added (S111).*

```python
SYN.CA.11 = Card(
    card_id      = "SYN.CA.11",
    version  = "v0.1",
    name     = "Redline",
    tagline  = "The numbers that matter are the ones no one double-checked.",
    type     = CovertOperation,
    subtype  = FactionSpecific,
    faction  = Syndicate,

    layer    = Information,
    function = Corrupt,
    subject  = AccordAgreement,

    beat         = 3,
    resolution   = d100,
    threshold    = 50,
    ring_mod     = None,
    doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = AccordAgreement(state=active, clause_contains=numeric_fill_in),

    affinity    = None,
    restriction = AccordAgreement.count(state=active) >= 1,
    cost        = Capital(2),
    boost       = None,

    success     = target_object.alter(type=Terms, clause=declared_clause,
                                      new_value=declared_value),
    successcrit = standing += 1,
    fail        = None,
    failcrit    = Discovery,

    on_accept  = None,
    on_decline = None,

    persistence           = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    portrait = {
        Syndicate:   PortraitEntry(flat=+1),
        Network:     PortraitEntry(flat=-1),
        Directorate: PortraitEntry(flat=-1),
    },

    narrative = "The document in the placement area is a public record. It has always been a public record. The number in the third clause has always been that number. If it seems different from what you remember — you're probably misremembering.",

    perspectives = {
        Syndicate:   "Leverage doesn't expire. It just changes shape.",
        Ghost:       "We noticed the discrepancy. We are still determining whether it was us, them, or the original terms.",
        Network:     "Someone revised the Accord. No one is claiming it. That's the story.",
        Directorate: "The written record is the law. We will find out who changed this.",
        Guild:       "We build to the spec we signed. If the spec changed, we need to know now.",
    },

    design_note  = "Syndicate's only Information-layer covert op. Effect is public (form changes) but actor is covert — unique table dynamic. Valid clause targets: fill-in values that are numeric or ordinal (resource quantity, influence tier, Quarter number). Prohibited: clause rows with only named entries (district name, PA type) — not numeric alterations. declared_clause and declared_value sourced from Target Profile declared-parameters line.",
    arbiter_note = "Acting faction declares at Covert Dispatch: (a) target Accord by named parties, (b) clause row to alter, (c) replacement value — all written on Target Profile declared-parameters line. On success at Beat 3: locate declared Accord form in Accord Placement Area; apply Alter/Terms per Art 06 §9.10 — write new value; acting faction identity not disclosed. If declared Accord has been removed before Beat 3 resolution, treat as fail. Alteration resolves in submission order; subsequent Beat 3 ops see altered terms.",
)
```

---


---

### Syndicate — Public Acts
[↑ Syndicate](#syndicate)

| Card | Name |
|------|------|
| [SYN.PA.1](#p15-acquisition-offer) | Acquisition Offer |
| [SYN.PA.2](#p16-public-dividend) | Public Dividend |
| [SYN.PA.3](#syn-pa-3--data-acquisition) | Data Acquisition |

### SYN.PA.1 — ACQUISITION OFFER
[↑ Public Acts](#syndicate-public-acts)

#### Design Rationale
Syndicate's public territorial acquisition PA — the counterpart to SYN.CA.3 Hostile Acquisition (which is covert and forcible). This card asks first. Scaling: 2 Capital per presence token acquired (n declared at Phase B). Cost scales with the position being purchased: 2 tokens at Established = 4 Capital; 6 tokens at full Dominant = 12 Capital. The offer fee (1 Capital at Phase B) is non-refundable regardless of outcome — the cost of making a public offer. The balance payment (2n Capital) is conditional on acceptance and paid at Beat 4 cleanup. On refusal, Syndicate gains the PS advantage of having made a good-faith offer publicly.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public buyout offers are core Syndicate doctrine — acquire, not take | Art 00 §7 |
| Voice fit | ✓ | Syndicate on-doctrine; Network (aligned): public offer creates public record; Guild (opposed): presence is built, not bought | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Syndicate acquire-not-take doctrine: public offer before forced action. Scaling cost (n × 2 Capital) rewards the target. PS on decline (+1 Syndicate, −1 target) incentivizes acceptance. Portrait +1. Legitimizes acquisition mode vs SYN.CA.3 Hostile's coercive mode | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Syndicate) / ElectPlayer | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Redirect / PresenceToken | Art 04b §4 |
| Balance | ✓ | 1 Capital offer fee (non-refundable) + 2n conditional. Scaling cost makes Dominant buyout expensive (12 Capital). Beat 4 resolution (not Debrief) | Art 02 §6–§7 |
| Effect duration | ✓ | PresenceToken transfer is immediate at Beat 4 acceptance; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card resolved at Beat 4; no game-state marker persists | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Syndicate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid; restriction checks target's Established+ in district (valid zone condition) | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); Capital cost + conditional payment (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Target decides at Beat 4 (not Debrief); token/Capital transfer at Beat 4 cleanup | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
SYN.PA.1 = Card(
    id      = "SYN.PA.1",  version="v1.0",
    name    = "Acquisition Offer",
    tagline = "Publicly offer to purchase another faction's presence position in a district.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,

    layer    = Territory,  function = Redirect,  subject = PresenceToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = ElectPlayer,  # target accepts or declines at Beat 4
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(target).influence_tier(target_district) >= Established,
    # declared at Phase B: target faction, district, token count (n)
    cost = resource.faction(Syndicate).capital * 1,  # offer fee; non-refundable regardless of outcome

    success     = None,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    # ElectPlayer — target faction publicly accepts or declines at Beat 4
    on_accept  = (
        district(target_district).faction(target).presence -= n,
        district(target_district).faction(Syndicate).presence += n,
        faction(target).resource(capital) += (2 * n),  # balance payment from Syndicate
        faction(Syndicate).standing += 1,
        faction(target).standing += 1,
    ),
    on_decline = (
        faction(Syndicate).standing += 1,
        faction(target).standing -= 1,
    ),

    portrait = {Syndicate: PortraitEntry(submitter=+1)},

    narrative    = "Syndicate does not take what it can buy. The offer is always made first. What the other faction does with it is their business.",
    perspectives = {
        Syndicate: "This is the formal mechanism. We are not here to take — we are here to acquire. The distinction matters.",
        Network:   "Syndicate makes the offer at The Table where everyone watches. Whatever the target decides, their answer is on the record. That is also useful to us.",  # aligned
        Guild:     "Syndicate offers Capital for positions Guild built through construction and sustained through presence. We did not build it to sell. That is not a position the offer changes.",  # opposed
    },
    design_note  = "Public counterpart to SYN.CA.3 Hostile Acquisition. 1 Capital offer fee non-refundable. Balance payment (2n Capital) conditional on acceptance, paid at Beat 4. Scaling: n=2 (Established min) = 4 Capital; n=6 (Dominant max) = 12 Capital. On accept: both PS +1. On decline: Syndicate +1, target −1. Beat 4 resolution — not Debrief.",
    arbiter_note = "Phase B: Syndicate names target faction, district, token count (n). 1 Capital offer fee committed. Beat 0: restriction check (target Established+). Beat 4: target faction publicly accepts or declines. On accept: transfer n presence tokens from target to Syndicate; Syndicate pays 2n Capital to target from supply; both +1 PS. On decline: Syndicate +1 PS, target −1 PS. Offer fee (1 Capital) is not returned in either case.",
)
```

---

### SYN.PA.2 — PUBLIC DIVIDEND
[↑ Public Acts](#syndicate-public-acts)

#### Design Rationale
Syndicate's political leverage PA. Places a Capital-valued marker on a named district. At next Upkeep Step 5, whoever holds Dominant in that district receives the Capital. Syndicate pre-commits 2 Capital (physically placed under the marker as escrow) and gains PS +1 at Beat 4. The card creates a persistent incentive structure that shapes table behavior without Syndicate taking direct action: factions will fight over Dominant in that district because there's Capital to claim. Syndicate may voluntarily withdraw the marker by paying 1 Mandate (removing the incentive, a diplomatic instrument). Persistence = Seasonal (marker stays until claimed or Quarter end).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Capital-as-political-leverage is core Syndicate doctrine | Art 00 §7 |
| Voice fit | ✓ | Syndicate on-doctrine; Ghost (aligned): deferred mechanism patience; Directorate (opposed): unregulated shadow investment | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Capital-as-leverage: 2 Capital escrow shapes table behavior without direct action. PS +1 at Beat 4. Voluntary withdrawal (1 Mandate) as diplomatic instrument. Portfolio +1: submitter-bounded | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Syndicate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Add / NativeResource (deferred, conditional on Dominant at Upkeep) — note: payout resource is Capital; subject label may need schema pass clarification | Art 04b §4 |
| Balance | ✓ | 2 Capital cost + PS +1; 2 Capital at risk if another faction claims Dominant. Maximum loss: 2 Capital + 1 Mandate (withdrawal) | Art 02 §6–§7 |
| Effect duration | ✓ | DividendMarker payout at Upkeep Step 5 — within-Quarter. Seasonal persistence. Phase 21 escrow return if unclaimed. No multi-Quarter effect | Art 04 §5 P19 |
| Persistence | ✓ | Seasonal — DividendMarker stays on district until claimed at Upkeep, withdrawn, or Phase 21 | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Syndicate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone; DividendMarker placed on district (valid zone-based component placement) | Art 01 §6–§7 |
| Supported by components | ⚠ | DividendMarker is a new component — register in Art 02 before production | Art 02 |
| Supported by game procedure | ⚠ | DividendMarker is a new component — register in Art 02. Upkeep Step 5 procedure needs amendment to handle marker resolution | Art 03 §11; Art 02 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
SYN.PA.2 = Card(
    id      = "SYN.PA.2",  version="v1.0",
    name    = "Public Dividend",
    tagline = "Declare a public capital investment in a district — rewarding whoever holds Dominance at next Upkeep.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,

    layer    = Economy,  function = Add,  subject = NativeResource,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Seasonal,  # DividendMarker stays on district until claimed, withdrawn, or Phase 21
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,  # dynamic — whoever holds Dominant at next Upkeep
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = resource.faction(Syndicate).capital * 2,  # placed as escrow under DividendMarker

    success = (
        arbiter.place(DividendMarker(value=2, resource=Capital, district=target_district)),
        faction(Syndicate).standing += 1,
        game.world_condition(
            scope    = district(target_district),
            effect   = faction(district(target_district).dominant).resource(Capital) += 2,
            duration = Seasonal,
            trigger  = game.phase == Upkeep,
            clear_on = DividendMarker(district=target_district).claimed == True OR game.phase == EndOfQuarter,
        ),
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Syndicate: PortraitEntry(submitter=+1)},

    narrative    = "Syndicate backs positions, not factions. The investment is in the district. The winner claims it.",
    perspectives = {
        Syndicate:   "We do not choose who collects. We choose where the capital sits. That is sufficient leverage.",
        Ghost:       "Syndicate places the incentive and removes themselves from the contest. The district will spend three months fighting over two Capital. We understand the patience required to let mechanisms run.",  # aligned
        Directorate: "Syndicate places two Capital in a district and calls it public investment. The Directorate notes there is no permit, no declared ownership, and no regulatory oversight on what the marker represents.",  # opposed
    },
    design_note  = "Persistent economic leverage PA. 2 Capital placed as physical escrow under DividendMarker on district. At next Upkeep Step 5: Dominant faction claims it. If no Dominant (Contested or all Absent): marker stays, recheck next Upkeep. Quarter end: Syndicate recovers unclaimed escrow. Voluntary withdrawal: 1 Mandate public declaration. DividendMarker is a new component — Art 02 registration required.",
    arbiter_note = "Beat 4: place DividendMarker on district with 2 Capital tokens as physical escrow. Syndicate +1 PS. At each Upkeep Step 5 while marker present: check for Dominant in district. If Dominant: transfer 2 Capital to that faction; remove marker. If Contested or Absent: marker remains for next Upkeep. Phase 21: return unclaimed escrow to Syndicate. Voluntary withdrawal: Syndicate declares to ARBITER, pays 1 Mandate; escrow returned.",
)
```

---

### SYN.PA.3 — DATA ACQUISITION
[↑ Public Acts](#syndicate-public-acts)

#### Design Rationale
Syndicate publicly demands a target faction's Intel Token count and offers to purchase them. The demand is a guess — N is committed at Art 03 §9.2 Public Declaration. ElectPlayer resolves publicly at Beat 4 — target faction responds at the table. Three resolution paths: (1) trade — N tokens transfer to Syndicate, card discards; (2) show — target reveals all held tokens face-down (count public, content private), no transfer, card discards; (3) decline — no reveal, no trade, Syndicate −2 PS, card becomes Permanent. As Permanent, the card acts as a standing React: the first time target faction places a PA with a non-blank Target Profile at Art 03 §9.2, Syndicate replaces that Target Profile with one they fill in, then card discards. If target avoids targeted PAs for the rest of the Quarter, the card expires — the threat IS the constraint. Verbal offer is unenforceable; the coercive frame is intentional: this is extortion with a commercial label.

Narrative logic for the decline effect: declining a Syndicate offer in public does not end the relationship — it shifts the leverage. The Syndicate has already demonstrated they know approximately what the target is holding. Refusing to deal signals that the intel position is worth protecting. Syndicate's response: *fine — then we determine how you use it publicly.* The next targeted public act belongs to them. "Control comes from positioning early" — the decline transfers that positioning from the information layer to the target's submission layer.

#### Card Story
A Syndicate representative rises at Beat 4 and addresses the table: "We believe you hold [N] intelligence assets. We are prepared to acquire them at our stated consideration. You may accept our terms, demonstrate you cannot meet them, or decline." The table waits for the answer.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public coercion for intel count disclosure; fills Information\|Reveal\|IntelTokensHeld Syndicate gap; distinct from covert intel gathering (GHO.CA.x); PA-layer — act is the declaration, not the knowledge | Art 00 §7 |
| Voice fit | ✓ | FactionSpecific Syndicate; full perspectives block; verbal offer framing is on-voice | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital(1) cost; intel count as transactional commodity; "control comes from positioning early" — Permanent React transfers positional leverage on decline | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/IntelTokensHeld — surfacing private count via public ElectPlayer; count is information content (not token board position = Economy) | Art 04b §4, §5 |
| Balance | ⚠ | Permanent React potency (PA Target Profile corruption) untested — flag for doctrine review | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent on decline path; accept/cannot-meet paths discard at Beat 4; React fires once then card discards; Quarter-end expiry if React never fires | — |
| Persistence | ✓ | Permanent model applied correctly; persistence_condition clear; card-as-condition sits in Syndicate PA area face-up | Art 04 §6 |
| Trigger validity | ✓ | React trigger: PA with non-blank Target Profile placed at Art 03 §9.2 Public Declaration — publicly observable (P5) | Art 04 §5 P5 |
| Portrait validity | ✓ | flat entries only; submitter-bounded (Syndicate, Network, Directorate); no direct Portrait track shift in effect fields; Automatic resolution — no failcrit | Art 04 §6.2 |
| Supported by zones | ✓ | Faction Resolution Grid (Art 01/02); faction terminal (Intel Tokens held behind screen — faction-private) | Art 01 §6–§7 |
| Supported by components | ✓ | Intel Token (Art 02 §9); Target Profile with declared-parameters line (Art 02 v2.4 — S111); Faction Resolution Grid (Art 02 §5) | Art 02 §5, §8, §9 |
| Supported by game procedure | ✓ | Beat 4 ElectPlayer: publicly resolved at table — target declares trade, show, or decline openly; standard PA resolution (Art 03 §9.4). React framework (Art 03 §18) covers Permanent persistence_effect; table enforces React timing; no new procedure needed | Art 03 §9.4; §18 |
| Data schema validation | ✓ | All fields populated per §6.1/§6.2 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story present | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Three paths (accept / cannot-meet / decline) — each has exactly one outcome; no branching within paths; Permanent React fires once then discards | Art 04 §5 P27 |
| Resource cost positioning | Is this card's cost mono-resource (acting faction's own native resource only) or cross-faction-resource (two or more distinct native resources)? Confirm power level matches: mono-resource = floor-power; cross-faction-resource = ceiling-power. Flag if mono-resource and high-power, or cross-resource and underpowered. If cost generates non-native resources as an effect, flag — requires doctrine justification. *(P28)* | Art 00a §9.2 |

#### Outstanding Issues

- **Balance:** Permanent React effect (Target Profile replacement on next targeted PA) has no playtesting baseline. Monitor in doctrine review (04-n88).
- **Consideration non-fulfillment (design note — non-blocking):** Consideration is a verbal offer written on the TP declared-parameters line; it is not held in escrow. If Syndicate cannot deliver at sub-case A, the exchange fails and the card stays Permanent. Bluff mechanic is intentional — Syndicate bears public failure risk. Ruling: sub-case A fails → card stays Permanent (L234).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ⚠ | |

*v0.1 — S111: new card, fills Information\|Reveal\|IntelTokensHeld gap. Permanent React model. Issues Resolved pending doctrine review (04-n88).*

```python
SYN.PA.3 = Card(
    card_id      = "SYN.PA.3",
    version  = "v0.1",
    name     = "Data Acquisition",
    tagline  = "We know approximately what you're holding. We're giving you the chance to make this a transaction.",
    type     = PublicAct,
    subtype  = FactionSpecific,
    faction  = Syndicate,

    layer    = Information,
    function = Reveal,
    subject  = IntelTokensHeld,

    beat         = 4,
    resolution   = Automatic,
    threshold    = None,
    ring_mod     = None,
    doctrine_mod = None,
    outcome_type = ElectPlayer,

    target_district = None,
    target_faction  = faction(any, not=Syndicate),
    target_object   = IntelTokensHeld(count=N_declared),
    declared_params = (
        N             = int,                         # tokens requested
        consideration = verbaloffer(faction(acting)), # free-text: Capital | ModifierCard(named) | any combination
        # both written on TP declared-parameters line at Art 03 §9.2 Public Declaration
    ),

    affinity    = None,
    restriction = None,
    cost        = Capital(1),
    boost       = None,

    on_accept  = (
        # sub-case A — trade: bilateral exchange
        consideration.move(faction(acting), faction(target)),          # Syndicate pays
        IntelToken(N_declared).move(faction(target).terminal,
                                    faction(acting).terminal),         # target pays
        # if Syndicate cannot fulfill consideration: exchange fails; card stays Permanent
        # card → PA discard only if both transfers complete

        # sub-case B — show: target voluntarily reveals all held Intel Tokens face-down;
        # count visible, content private; no transfer; tokens returned to terminal
        # card → PA discard (information goal met)
    ),

    on_decline = faction(acting).standing -= 2,
    # full refusal — no reveal, no trade; card → Permanent; stays in Syndicate PA area

    persistence           = Permanent,
    persistence_condition = NOT (Quarter.ended OR react_fired OR terms_accepted),
    # applies on decline path only; sub-case A (completed) and sub-case B both discard at Beat 4
    # terms_accepted: target completes trade OR reveals all tokens face-down (count public)
    # at any point while card is active — either clears card

    persistence_effect    = React(
        trigger = faction(target).PA(target_profile != None).placed_at("Art 03 §9.2.0"),
        effect  = target_profile.replace(Syndicate.written),
        on_fire = SYN_PA_3 → faction_PA_discard,
    ),
    # While Permanent: when target faction places any PA with non-blank Target Profile
    # at Art 03 §9.2 Public Declaration (Art 03 §9.2.0), card fires as React — Syndicate immediately
    # replaces that Target Profile with one they fill in. SYN.PA.3 → PA discard.
    # Table enforces; no ARBITER tracking required.
    # If target submits no PA with Target Profile this Quarter: card expires Quarter end.
    # PAs without Target Profile (e.g., Floor Act) do not trigger — React does not fire.

    portrait = {
        Syndicate:   PortraitEntry(flat=+1),
        Network:     PortraitEntry(flat=-1),
        Directorate: PortraitEntry(flat=-1),
    },

    narrative = "The offer is made in public, which is unusual for the Syndicate. They prefer quiet transactions. This one is designed to be loud.",

    perspectives = {
        Syndicate:   "Intelligence is a commodity. We're establishing the market price and giving them the chance to sell at it.",
        Ghost:       "The offer is a probe. The response — whatever form it takes — is the data.",
        Network:     "This is how private information becomes public leverage. This is exactly what we exist to counter.",
        Directorate: "A public extortion offer dressed as commerce. We note the terms and the response.",
        Guild:       "Whatever they're buying, they think they need it. That tells us something about their position.",
    },

    design_note  = "Three resolution paths at Beat 4 ElectPlayer: (1) trade — bilateral exchange: consideration moves Syndicate→target, N tokens move target→Syndicate; card discards only if both transfers complete; (2) show — target reveals all held tokens face-down (count public, content private), no transfer, card discards — information goal met; (3) decline — no reveal, no trade, Syndicate −2 PS, card becomes Permanent. Sub-cases 1 (completed) and 2 both satisfy the card; only 3 triggers the stake. Non-fulfillment edge case (sub-case A, Syndicate cannot deliver consideration): exchange fails; card stays Permanent — Syndicate set the terms and failed to meet them. Bluff mechanic is intentional: consideration is a verbal offer written on TP declared-parameters line, not held in escrow; Syndicate bears public failure risk. Show path: target voluntarily reveals count — not compelled, consistent with GR 10.1 (ElectPlayer creates stake; choice is player's). PERMANENT PHASE is fully table-enforced: card is face-up in Syndicate PA area; table observes when target places a PA with Target Profile at Art 03 §9.2.0 and allows Syndicate to replace it (React); table observes if target accepts at any point (trade or show) and card is cleared. No ARBITER involvement required at any stage — Beat 4 ElectPlayer is public; Permanent card is table-enforced. Target may accept at any time to clear the card. Threat is the constraint: target must deal with Syndicate or avoid targeted PAs for the rest of the Quarter. N and consideration declared at Art 03 §9.2 on TP declared-parameters line (Art 02 v2.4).",
)
```

---


---


---

---

### SYN.PA.4 — CHARITY GALA *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.4 = Card(
    id      = "SYN.PA.4",  version = "v1.0",
    name    = "Charity Gala",
    tagline = "A massive display of wealth that forces rivals to pay up or lose face.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Standing,  function = Shift,  subject = StandingMarker,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Syndicate).capital * 2,
    success = "Syndicate gains +2 PS. Every opponent must either pay 1 Capital to the supply or immediately lose 1 PS.",
    design_note = "A public flex of pure capital. Weaponizes Syndicate's wealth to farm PR while forcing opponents to bleed money or take a PR hit just to keep up appearances."
)
```

---

### SYN.PA.5 — PROTECTION RACKET *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.5 = Card(
    id      = "SYN.PA.5",  version = "v1.1",
    name    = "Protection Racket",
    tagline = "Publicly leverage capital to extort physical expansion.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Remove,  subject = StructureBlock,
    beat    = 4,  resolution = Automatic,  persistence = Transient,
    cost    = resource.faction(Syndicate).capital * 2 + resource.faction(Syndicate).mandate * 1,
    success = "Places a Standing Condition on target_district until Quarter+1: Whenever a Structure Block or Presence Token is placed here, the faction that owns it must pay 1 Capital to Syndicate. If they do not, the structure or token is immediately removed.",
    design_note = "Fixes the covert targeting issue. Physical placement of chips and blocks is public knowledge. Syndicate sets up a toll booth on the district: the owner of the structure pays, or their asset is destroyed."
)
```

### SYN.MOD.2 — SHELL CORPORATION *(stub)*

*S128. React on Accord formation. Every formal deal creates economic opportunity — Syndicate positions inside it immediately. Pairs with SYN.MOD.3 (Offshore Slush Fund on accord.corrupted).*

```python
SYN.MOD.2 = Card(
    id      = "SYN.MOD.2",  card_id="SYN.MOD.2",  version="v0.1",
    name    = "Shell Corporation",
    tagline = "Every Accord is a market event. Syndicate responds accordingly.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    trigger         = accord.placed,
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(Syndicate).resources.add(1, Capital),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Syndicate: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Accord formation React. Every new Accord at The Table generates 1 Capital for Syndicate — the economic positioning happens before Syndicate is even a party. Delivers §5a 'accord manipulation' at the modifier level: Syndicate doesn't need to be invited to benefit from diplomatic activity. Compare DIR.MOD.4: DIR earns Mandate from the same trigger; SYN earns Capital. Competing institutional reactions to the same event.",
    arbiter_note = None,
)
```

---

### SYN.MOD.3 — OFFSHORE SLUSH FUND *(stub)*

*S128. React on Accord breach. Syndicate extracts Capital from diplomatic breakdown. Higher yield than formation — breach creates leverage. Pairs with SYN.MOD.2.*

```python
SYN.MOD.3 = Card(
    id      = "SYN.MOD.3",  card_id="SYN.MOD.3",  version="v0.1",
    name    = "Offshore Slush Fund",
    tagline = "When an Accord fails, Syndicate had a clause for that.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    trigger         = accord.removed,
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(Syndicate).resources.add(2, Capital),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Syndicate: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Accord removal React. 2 Capital yield. Trigger corrected from 'corrupted' to 'removed' to align with Art 06 physical game state. Open question for detail design: Should accord.removed be the sole condition (meaning Syndicate profits off ANY Accord ending, completed or breached), or is a separate mod card needed to distinguish breach vs completion?",
    arbiter_note = None,
)
```

---

### SYN.MOD.4 — INSIDER TRADING *(stub)*

*Market speculation on positive faction momentum.*

```python
SYN.MOD.4 = Card(
    id      = "SYN.MOD.4",  card_id="SYN.MOD.4",  version="v0.1",
    name    = "Insider Trading",
    tagline = "Public success always creates private wealth.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    trigger         = public_standing.shifted(direction=positive, faction=opponent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(Syndicate).resources.add(1, Capital),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Market speculation React. Syndicate bets on the political market. When someone else scores a massive PR victory, Syndicate quietly makes a fortune off the back of it.",
    arbiter_note = None,
)
```

---

### SYN.MOD.5 — SHORT SQUEEZE *(stub)*

*Market speculation on negative faction momentum.*

```python
SYN.MOD.5 = Card(
    id      = "SYN.MOD.5",  card_id="SYN.MOD.5",  version="v0.1",
    name    = "Short Squeeze",
    tagline = "A reputation in freefall is just an undervalued asset.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    trigger         = public_standing.shifted(direction=negative, faction=opponent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Syndicate).capital * 2 + resource.faction(Syndicate).findings * 1,

    success     = faction(Syndicate).resources.add(1, Capital),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Companion to SYN.MOD.4. Syndicate profits off the downfall of other factions. By holding both MOD.4 and MOD.5, Syndicate guarantees income from any major political volatility at the table Cost reasoning: Findings identify the target's financial vulnerabilities before Capital is deployed to crush them.",
    arbiter_note = None,
)
```

---

### SYN.MOD.6 — BOUNTY CONTRACT *(stub)*

*Syndicate weaponizes other factions by crowdsourcing their own defense or offense.*

```python
SYN.MOD.6 = Card(
    id      = "SYN.MOD.6",  card_id="SYN.MOD.6",  version="v0.1",
    name    = "Bounty Contract",
    tagline = "If someone wants them gone, I am willing to subsidize the effort.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    trigger         = public_act.placed_on_frg(faction=opponent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = "Syndicate places this card on their FRG as a standing condition and places 2 Capital on it. The target opponent's PA gains boost=+20. When target PA resolves: if success, the 2 Capital is transferred to the acting faction; if failure, the Capital is returned to Syndicate.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Transactional warfare. Played onto Syndicate's own FRG with 2 Capital 'escrowed' on the card, preventing any Beat 4 resource-cleanup conflicts with the target PA itself. The submitting faction effectively becomes Syndicate's mercenary, receiving the Capital only if the op succeeds.",
    arbiter_note = None,
)
```

---

### SYN.MOD.7 — RENEGOTIATION FEE *(stub)*

*Reacts to the corruption (textual alteration) of an Accord's terms.*

```python
SYN.MOD.7 = Card(
    id      = "SYN.MOD.7",  card_id="SYN.MOD.7",  version="v0.1",
    name    = "Renegotiation Fee",
    tagline = "When the fine print changes, the lawyers get paid.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    trigger         = covert_operation.resolved(layer=Information, function=Corrupt, subject=AccordAgreement),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(Syndicate).resources.add(2, Capital),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Leveraging Accord manipulation. Triggers when ANY faction successfully corrupts an Accord (e.g., via SYN.CA.11 Redline). Syndicate earns 2 Capital from the procedural friction of rewriting the agreement.",
    arbiter_note = None,
)
```

---

### SYN.MOD.8 — HOSTILE TAKEOVER *(stub)*

*Syndicate buys up the territory left behind by destroyed infrastructure.*

```python
SYN.MOD.8 = Card(
    id      = "SYN.MOD.8",  card_id="SYN.MOD.8",  version="v0.1",
    name    = "Hostile Takeover",
    tagline = "Buy when there's blood in the streets.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    trigger         = structure_block.removed(faction=opponent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Syndicate).resources.has(2, Capital),
    cost            = resource.faction(Syndicate).capital * 2 + resource.faction(Syndicate).exposure * 1,

    success     = "arbiter.place(presence_chip, district=target_district, faction=Syndicate, count=1); arbiter.place(structure_block, district=target_district, faction=Syndicate, count=1)",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Opportunistic expansion. When a structure falls, Syndicate swoops in, paying 2 Capital to immediately place both a presence chip and a structure in the newly cleared real estate. Extremely powerful territorial swing funded entirely by Capital Cost reasoning: Exposure ensures the takeover is recognized publicly, legitimizing the new ownership immediately.",
    arbiter_note = None,
)
```

---

## 8. Card Taxonomy Index

*Column definitions and Layer × Function validity matrix in Art 04b §5.1. Status key: ✅ Signed off — canonical, use for gap analysis. 📝 Draft — designed but not signed off. ⬜ Not yet designed. 🚫 Retired.*

| Card ID | Name | Status | Layer | Visibility | Function | Subject | Primitive Verb(s) |
|---------|------|--------|-------|------|----------|---------|-------------------|
| DIR.CA.1 | Invoke Jurisdiction | 📝 | Submission | Split | Block | Covert Operation (STD.CA.1, STD.CA.3) | — |
| DIR.CA.2 | Detain | 📝 | Territory | Public | Move | Deployment Marker | Move | *(taxonomy corrected S107 L226: success operation is game.move() to Detention zone; Remove was incorrect — Remove = return to supply; Detention zone is an active play area on Directorate's tableau. Art 04 spec function field correction tracked under 04-n105)* |
| DIR.CA.3 | Surveillance Placement | 📝 | Information | Private → Public | Reveal | Covert Operation | Reveal |
| DIR.CA.4 | Tactical Redirection | 📝 | Territory | Public | Move | Presence Token | Move |
| DIR.CA.5 | Sanctioned Raid | 📝 | Territory | Public | Remove | Presence Token | Remove |
| DIR.PA.1 | Regulatory Override | 📝 | Territory | Public | Modify | Presence Token (placement cost) | — |
| DIR.PA.2 | Convene an Inquiry | 📝 | Information | Private → Public | Add | Intel Token | Add |
| DIR.PA.3 | Entry/Exit Controls | 📝 | Territory | Public | Block | Deployment Marker | — |
| DIR.PA.4 | Regulatory Downgrade | 🚫 BLOCKED | Territory | Public | Modify | InfluenceTier (derived — not targetable) | — | *L223: InfluenceTier is not a targetable component — tier is derived from influence token counts, not a placed or written value. Only board state changes (token add/remove) can affect tier. 9.1 prohibits direct income modification by card. Fundamental redesign required (04-n104).* |
| DIR.PA.5 | Regulatory Freeze | 🚫 BLOCKED | Territory | Public | Block | InfluenceTier (derived — not targetable) | — | *L223: Same subject violation — InfluenceTier not a targetable component. Additionally, Block targets actions (not derived states); Block\|InfluenceTier is a subject mismatch. Fundamental redesign required (04-n104).* |
| DIR.PA.6 | Standing Injunction | 📝 | Submission | Split | Block | Public Act | — |
| DIR.MOD.1 | Riot Squad | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.2 | Capital Suppression | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.3 | City Council Loyalist | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.4 | Administrative Overhead | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.5 | Emergency Appropriation | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.6 | State of Emergency | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.7 | Eminent Domain | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.8 | Asset Seizure | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.CA.1 | Pattern Match | 📝 | Submission | Private | Redirect | Covert Operation (lane steal — Beat 2 intercept) | Redirect |
| GHO.CA.2 | Intercept | 📝 | Information | Private → Public | Reveal | Covert Operation | Reveal |
| GHO.CA.3 | Dossier Breach | 📝 | Information | Private → Public | Reveal | Intel Delivery Slip | Reveal |
| GHO.CA.4 | Deep Cover | 📝 | Information | Private → Public | Remove | Intel Token | Remove |
| GHO.CA.5 | Misdirection | 📝 | Information | Private | Corrupt | Intel Token (faction_name field — FRG placed only) | Corrupt |
| GHO.CA.6 | Synthesize | 📝 | Economy | Public | Add | Intel Token | Add |
| GHO.CA.7 | Station | 📝 | Information | Private → Public | Add | Intel Token | Add |
| GHO.CA.8 | Full Take | 📝 | Information | Private → Public | Add | Intel Token | Add |
| GHO.CA.9 | SCIF | 📝 | Information | Private → Public | Add | Debrief Action Card | Add |
| GHO.CA.10 | Flip | 📝 | Economy | Public | Add | Native Resource | Add |
| GHO.CA.11 | Signals Analysis | 📝 | Information | Private → Public | Reveal | Classified Directives | Reveal |
| GHO.CA.12 | Source Substitution | 📝 | Information | Private → Public | Corrupt | Intel Token | Corrupt |
| GHO.CA.13 | Backdate | 🚫 BLOCKED | Information | Private → Public | Corrupt | Intel Token (round-number field) | Corrupt | *L222: (1) Location constraint — Intel token in private terminal zone unreachable by opposing card; only publicly placed tokens (PA payment window) are valid Corrupt targets. (2) 7.2b — round-number records committed validity state; altering it is retroactive modification. §4.10 revised. Art 04 spec: BLOCKED pending redesign (04-n103).* |
| GHO.CA.14 | Field Verification | 🚫 BLOCKED | Information | Private → Public | Corrupt | Intel Token (age field) | Corrupt | *7.2b violation: mechanic alters committed token age field retroactively. Fundamental redesign required. G-ext id retired. Art 04 spec: BLOCKED pending redesign (04-n103).* |
| GHO.PA.1 | Publish Analysis | 📝 | Information | Private → Public | Reveal | Action Attribution | Reveal |
| GHO.PA.2 | Signal Review Request | 📝 | Resolution | Split by phase | Modify | Covert Operation (difficulty) | — |
| GHO.PA.3 | Declassified Records | 📝 | Information | Public | Remove | Intel Token (expired) | Remove |
| GHO.PA.4 | Public Threat Assessment | 📝 | Information | Private → Public | Reveal | Broadcast Effect Card | Reveal |
| GHO.PA.5 | Agency Recruitment Fair | 📝 | Territory | Public | Add | Presence Token | Add |
| GHO.MOD.1 | Sleeper Analyst | 📝 | Information | Public | Remove | Intel Token | Remove | *ModReactCard — taxonomy excluded from §11.1; effect description for spec clarity only* |
| GHO.MOD.2 | Perimeter Sensors | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.3 | Institutional Trace | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.4 | Signal Bleed | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.5 | False Flag | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.6 | Supply Chain Tap | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.7 | Sleeper Cell | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.8 | Local Sympathizers | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.CA.1 | Fortify Structure | ✅ | Territory | Public | Protect | Structure Block | — |
| GUI.CA.2 | Materials Acquisition | ✅ | Economy | Public | Add | Native Resource | Add | *(function: Recover → Add, S106 — 04b-20; Art 04 spec fix pending 04-n103)*
| GUI.CA.3 | Foundation Rights | ✅ | Territory | Public | Add | Presence Token | Add |
| GUI.CA.4 | Construction Crew | ✅ | Submission | Split | Remove Restriction | Covert Operation (presence requirement) | — |
| GUI.CA.5 | Infrastructure Yield | ✅ | Economy | Public | Add | Native Resource | Add |
| GUI.CA.6 | Labor Contract | 📝 | Economy | Public | Add | Native Resource | Add | *(function: Recover → Add, S106 — 04b-20; card_id GUI.CA.6 assigned; Art 04 spec fix pending 04-n103)*
| GUI.PA.1 | Civic Works Mandate | 📝 | Territory | Public | Add | Structure Block | Add |
| GUI.PA.2 | Infrastructure Bond | 📝 | Economy | Public | Add | Accord Agreement | Add |
| GUI.MOD.1 | Night Shift Crew | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.2 | Union Representative | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.3 | Institutional Contract | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.4 | Core Premium | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.5 | Company Town | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.6 | Emergency Reconstruction | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.7 | Worker Retaliation | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.8 | Site Clearance | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.CA.1 | Leak | 📝 | Information | Private → Public | Reveal | District | Reveal |
| NET.CA.2 | Disclosure Loop | 📝 | Economy | Public | Add | Exposure | Add |
| NET.CA.3 | Breaking News | 📝 | Information | Private → Public | Reveal | Covert Operation | Reveal |
| NET.CA.4 | Network Cascade | 📝 | Submission | Split | Modify | Public Act | — |
| NET.CA.5 | Community Anchor | 📝 | Territory | Public | Add | Presence Token | Add |
| NET.CA.6 | Sacrifice | 📝 | Economy | Public | Add | Intel Token | Add |
| NET.MOD.1 | Pirate Transmitter | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.2 | Troll Farm | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.3 | Backup Server Racks | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.4 | Amplification Array | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.5 | Infrastructure Signal | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.6 | Street-level Agitator | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.7 | Community Amplifiers | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.8 | Frequency Splitter | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.9 | Bandwidth Override | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.10 | Local Organizers | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.PA.1 | Public Disclosure | 📝 | Information | Private → Public | Reveal | Action Attribution | Reveal |
| NET.PA.2 | Community Rally | 📝 | Territory | Public | Add | Presence Token | Add |
| NET.PA.3 | Live Coverage | 📝 | Information | Private → Public | Reveal | Faction Hand | Reveal |
| STD.CA.1 | Build Structure | ✅ | Territory | Public | Add | Structure Block | Add |
| STD.CA.2 | Demolish | ✅ | Territory | Public | Remove | Structure Block | Remove |
| STD.CA.3 | Campaign | ✅ | Territory | Public | Add | Presence Token | Add |
| STD.CA.4 | Undermine | ✅ | Territory | Public | Remove | Presence Token | Remove |
| STD.CA.5 | Gather | ✅ | Information | Private → Public | Add | Intel Token | Add |
| STD.CA.6 | Broadcast Interference | ✅ | Submission | Split | Modify | Public Act (cost) | — |
| STD.CA.7 | Amplify | ✅ | Resolution | Split by phase | Modify | Public Act (outcome scale) | — |
| STD.CA.8 | Buy Influence | ✅ | Territory | Public | Add | Presence Token | Add |
| STD.CA.9 | Fund | ✅ | Economy | Public | Redirect | Native Resource | Move |
| STD.CA.10 | Protect | ✅ | Resolution | Split by phase | Protect | Covert Operation (difficulty) | — |
| STD.CA.11 | Tort Interference | 📝 | Information | Private → Public | Corrupt | Accord Agreement | Corrupt |
| STD.CA.12 | Absolute Compromise | 📝 | Submission | Split | Block | Covert Operation | — |
| STD.CA.13 | Disinformation Campaign | 📝 | Standing | Split | Shift | Public Standing | Move |
| STD.CA.14 | Disprove | 📝 | Economy | Public | Remove | Intel Token | Remove |
| STD.CA.15 | Intel Extraction | 📝 | Economy | Public | Redirect | Intel Token | Move |
| STD.CA.16 | Modifier Raid | 📝 | Economy | Public | Redirect | Modifier Card | Move |
| STD.MOD.1 | Overture | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.PA.1 | Open Operations | 📝 | Territory | Public | Add | Presence Token | Add |
| STD.PA.2 | Disputed Claim | 📝 | Territory | Public | Remove | Presence Token | Remove |
| STD.PA.3 | Public Commission | 📝 | Territory | Public | Add | Structure Block | Add |
| STD.PA.4 | Public Censure | 📝 | Standing | Split | Shift | Public Standing (−) | Move |
| STD.PA.5 | On the Record | 📝 | Information | Private → Public | Reveal | Action Attribution | Reveal |
| STD.PA.6 | Economic Sanction | 📝 | Economy | Public | Remove | Native Resource | Remove |
| STD.PA.7 | Public Address | 📝 | Standing | Split | Shift | Public Standing (+) | Move |
| STD.PA.8 | Table an Accord | 📝 | Economy | Public | Add | Accord Agreement | Add |
| SYN.CA.1 | Leveraged Acquisition | 📝 | Economy | Public | Add | Native Resource | Add |
| SYN.CA.2 | Short the Market | 📝 | Economy | Public | Remove | Native Resource | Remove |
| SYN.CA.3 | Hostile Acquisition | 📝 | Territory | Public | Redirect | Structure Block | Move |
| SYN.CA.4 | Golden Parachute | 📝 | Economy | Public | Protect | Native Resource | — |
| SYN.CA.5 | Regulatory Capture | 📝 | Submission | Split | Block | Named Action Type | — |
| SYN.CA.6 | Parasitic | 📝 | Economy | Public | Add | Intel Token | Add |
| SYN.CA.7 | Corporate Blackmail | 📝 | Economy | Public | Redirect | Native Resource | Move |
| SYN.CA.8 | Land Title | 📝 | Territory | Public | Add | Structure Block | Add |
| SYN.CA.9 | Hostile Takeover | 📝 | Territory | Public | Add | Presence Token | Add |
| SYN.CA.10 | Accord Transfer | 📝 | Economy | Covert | Corrupt | Accord Agreement | Corrupt | S111: full design pass; Art 06 §9.10 confirmed (L205); d100 threshold 50; crit = incoming party elects numeric term change |
| SYN.CA.11 | Redline | 📝 | Information | Covert | Corrupt | Accord Agreement | Corrupt | S111: new card; fills Information\|Corrupt\|AccordAgreement gap; d100 threshold 50; alters numeric fill-in on active Accord form |
| SYN.MOD.1 | The Fixer | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.2 | Shell Corporation | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.3 | Offshore Slush Fund | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.4 | Insider Trading | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.5 | Short Squeeze | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.6 | Bounty Contract | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.7 | Renegotiation Fee | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.8 | Hostile Takeover | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.PA.1 | Acquisition Offer | 📝 | Territory | Public | Redirect | Presence Token | Move |
| SYN.PA.2 | Public Dividend | 📝 | Economy | Public | Add | Native Resource (conditional) | Add |
| SYN.PA.3 | Data Acquisition | 📝 | Information | Public | Reveal | Intel Token | Reveal | S111: new card; fills Information\|Reveal\|IntelTokensHeld gap; ElectPlayer; Permanent React on decline |

---

## 9. Faction Coverage Matrix

*Standard column = faction=All cards and Political Acts (P-prefix). Faction columns = faction-specific cards only.*

| Layer | Function | Subject | Standard | Guild | Ghost | Directorate | Network | Syndicate |
|-------|----------|---------|----------|-------|-------|-------------|---------|-----------|
| **Territory** | | | | | | | | |
| | Add | Presence Token | STD.CA.3, STD.CA.8, STD.PA.1 | GUI.CA.3 | GHO.PA.5 | — | NET.CA.5, NET.PA.2 | SYN.CA.9 |
| | Add | Structure Block | STD.CA.1, STD.PA.3 | GUI.PA.1 | — | — | — | SYN.CA.8 |
| | Block | Deployment Marker | — | — | — | DIR.PA.3 | — | — |
| | Remove | Presence Token | STD.CA.4, STD.PA.2 | — | — | DIR.CA.5 | — | — |
| | Move | Deployment Marker | — | — | — | DIR.CA.2 | — | — |
| | Remove | Structure Block | STD.CA.2 | — | — | — | — | — |
| | Move | Presence Token | — | — | — | DIR.CA.4 | — | — |
| | Redirect | Presence Token | — | — | — | — | — | SYN.PA.1 |
| | Redirect | Structure Block | — | — | — | — | — | SYN.CA.3 |
| | Protect | Structure Block | — | GUI.CA.1 | — | — | — | — |
| | Modify | Presence Token | — | — | — | DIR.PA.1 | — | — |
| **Economy** | | | | | | | | |
| | Add | Native Resource | — | GUI.CA.2, GUI.CA.5, GUI.CA.6 | — | DIR.CA.6 | — | SYN.CA.1, SYN.PA.2 |
| | Add | Intel Token | — | — | GHO.CA.6 | — | NET.CA.6 | SYN.CA.6 |
| | Add | Accord Agreement | STD.PA.8, GUI.PA.2 | — | — | — | — | — |
| | Add | Exposure | — | — | — | — | NET.CA.2 | — |
| | Add | Native Resource | — | — | GHO.CA.10 | — | — | — |
| | Remove | Native Resource | STD.PA.6 | — | — | — | — | SYN.CA.2 |
| | Remove | Intel Token | STD.CA.14 | — | — | — | — | — |
| | Remove | Accord Agreement | — | — | — | — | — | — |
| | Redirect | Native Resource | STD.CA.9 | — | — | — | — | SYN.CA.7 |
| | Redirect | Intel Token | STD.CA.15 | — | — | — | — | — |
| | Redirect | Modifier Card | STD.CA.16 | — | — | — | — | — |
| | Redirect | Accord Agreement | — | — | — | — | — | — |
| | Corrupt | Accord Agreement | — | — | — | — | — | SYN.CA.10 |
| | Protect | Native Resource | — | — | — | — | — | SYN.CA.4 |
| **Information** | | | | | | | | |
| | Add | Intel Token | STD.CA.5 | — | GHO.CA.5, GHO.CA.7, GHO.CA.8 | DIR.PA.2 | — | — |
| | Add | Debrief Action Card | — | — | GHO.CA.9 | — | — | — |
| | Reveal | Covert Operation | — | — | GHO.CA.2 | DIR.CA.3 | NET.CA.3 | — |
| | Reveal | Intel Delivery Slip | — | — | GHO.CA.3 | — | — | — |
| | Reveal | District | — | — | — | — | NET.CA.1 | — |
| | Reveal | Faction Hand | — | — | — | — | NET.PA.3 | — |
| | Reveal | Action Attribution | STD.PA.5 | — | GHO.PA.1 | — | NET.PA.1 | — |
| | Reveal | Classified Directives | — | — | GHO.CA.11 | — | — | — |
| | Reveal | Broadcast Effect Card | — | — | GHO.PA.4 | — | — | — |
| | Reveal | Intel Token | — | — | — | — | — | SYN.PA.3 |
| | Remove | Intel Token | — | — | GHO.CA.4, GHO.PA.3, GHO.MOD.1 | — | — | — |
| | Corrupt | Accord Agreement | STD.CA.11 | — | — | — | — | SYN.CA.11 |
| | Corrupt | Intel Token | — | — | GHO.CA.12 | — | — | — |
| **Submission** | | | | | | | | |
| | Block | Covert Operation | STD.CA.12 | — | — | DIR.CA.1 | — | — |
| | Block | Named Action Type | — | — | — | — | — | SYN.CA.5 |
| | Block | Public Act | — | — | — | DIR.PA.6 | — | — |
| | Modify | Public Act | STD.CA.6 | — | — | — | NET.CA.4 | — |
| | Copy | Covert Operation | — | — | GHO.CA.1 | — | — | — |
| | Remove Restriction | Covert Operation | — | GUI.CA.4 | — | — | — | — |
| **Resolution** | | | | | | | | |
| | Modify | Public Act (outcome scale) | STD.CA.7 | — | — | — | — | — |
| | Modify | Covert Operation | — | — | GHO.PA.2 | — | — | — |
| | Modify | Difficulty | — | — | — | DIR.CA.8 | — | — |
| | Protect | Covert Operation | STD.CA.10 | — | — | — | — | — |
| **Standing** | | | | | | | | |
| | Shift | Public Standing | STD.CA.13, STD.PA.4, STD.PA.7 | — | — | DIR.CA.7 | NET.CA.7 | — |

---

## 10. Deck Construction & Pool Selection

Before the session begins, each faction player constructs their active decks from a larger initial card pool (Art 02, components DB:114/115). The pool is not played with in its entirety — players select a working subset for Q1–Q8. Cards not selected are returned to the box and remain out of play for the duration of the session.

This is the first strategic decision of the game. Preparation expresses doctrine: you cannot play a card you didn't bring.

### 10.1 Per-Faction Selection

| Card Type | Selection Rule |
|-----------|---------------|
| Covert Operations (CA) | Select a subset from the CA pool (Standard CAs + Faction CAs combined). Shuffle into the Covert Operation Deck. |
| Public Acts (PA) | Select a subset from the PA pool (Standard PAs + Faction PAs combined). Shuffle into the Public Act Deck. |
| Modifier Cards | Select a working subset from the Modifier pool. Form the Faction Modifier Deck. |
| Operative | Select **1** from the Operative pool. |
| Apex | Select **1** from the Apex pool. |

Standard cards are distributed as part of each faction's CA and PA pools — each faction holds its own physical set of Standard cards, not a shared deck.

> **Design note:** Deck sizes (total card counts, per-card copy counts, and pool sizes) are pending balance analysis and playtesting. Legacy `pool_copies` field references are retired. Counts will be established during the balance pass. *(PM05 04-n136)*

**Procedure:** Art 03-init §3.9.

---

## 11. Rules & Constraints — Modifier Cards

### 11.1 What They Are

Modifier cards alter the parameters of an action rather than targeting a game layer directly. They produce no game-state primitives on their own; their effect is mediated by the host action or condition they modify. Modifier cards carry no Layer — Function — Subject assignment and are excluded from the card taxonomy. *(Art 04b §5.1, §9)*

Three subclass types govern how a modifier card fires (§6.1):

- **ModActionCard** — bundled with a submitted operation (CA, PA, Operative, Emergency, Apex) at Covert Dispatch; fires with the host action; effect expressed as a `ModActionExpr` tagged union.
- **ModBattleCard** — played during Battlefield Strength resolution (§10 Contested District Resolution); effect is a `ModBattleExpr` threshold delta.
- **ModReactCard** — fires when a publicly observable board state change matches its `trigger` condition; played in the Faction Resolution Grid, not bundled with a dispatch case.

*"Instant" was a working designation in earlier design. The canonical term is ModActionCard (operation modifier) or ModReactCard (react/trigger modifier) per §6.1.*

Two sets:

Faction modifier cards represent faction-specific individuals, assets, tactical approaches, doctrine, and equipment. Ring modifier cards represent key ring individuals, assets, equipment, and synergies within the ring.

**Faction modifier cards** — drawn from faction modifier deck in player tableau. Shuffled and placed face-down at session setup. *Card back: faction color, no border. Card face: effect, Portrait alignment (if applicable), value rating (1–3).*

**Ring modifier cards** — drawn from shared ring decks on game board (Sprawl, Infrastructure, Core). Chorus Node has no modifier deck. *Card back: ring color. Card face: ring constraint prominently stated ("Usable on [Ring] district targets only"), effect, Portrait alignment (if applicable), value rating (1–3).*

Ring constraint applies to all users regardless of holder.

*Naming note: "Modifier cards" is a working designation — pending decision D-04-07.*

### 11.2 Draw Conditions (Upkeep Step 6)

Factions that have triggered Burst Play skip modifier draws for the remainder of the session.

**Faction modifier draw:**

| Structure blocks owned | Cards drawn |
|------------------------|-------------|
| 0–1 | 0 |
| 2–3 | 1 |
| 4–5 | 2 |
| 6+ | 3 (maximum) |

**Ring modifier draw:** 1 card from a ring deck if the faction has both:
1. At least 1 structure block in that ring, AND
2. Established or Dominant in at least 1 district in that ring.

One draw per qualifying ring per round.

### 11.3 Hand Accumulation

No hand limit. Count publicly visible; content private. Modifier decks not reshuffled — one-pass per session.

### 11.4 Submit Rules

Maximum 1 modifier card per action submitted. No total per-round limit. Burst Play supersedes (§11.6).

### 11.5 Trading

Freely tradeable between factions at any time outside Resolution. Ring constraint travels with the card. ARBITER notes trades. End-of-session cleanup: sort by card back color.

### 11.6 Burst Play

**Trigger:** After Upkeep Step 6 draws complete, before Dispatch phase opens.

**Effect:** Trade ALL held modifier cards for Reservoir resources at 1:1 — any resource type, each card independently.

**Consequence:** Faction modifier deck removed from tableau for the remainder of the session. Modifier draw skipped at all future Upkeeps. Post-Burst factions may still receive and use modifier cards through trade — Burst removes draw access only.

**ARBITER announces publicly:** *"[Faction] has liquidated their operational reserve."* Resource gain private.

*Modifier card individual design is a full design pass — pending decision D-04-08.*

### 11.7 Effect Types

**ModActionCard** effects (§6.3 `ModActionExpr` — one per card):

| ModActionExpr | Effect | Valid for |
|---------------|--------|-----------|
| `threshold_delta(n)` | +n or −n applied to host action threshold | CA and PA |
| `success_multiplier(n)` | Effect fires additional n times on success | CA and PA |
| `ps_shift(faction, delta)` | Applies a PS shift to "acting", "target", or a named faction | CA and PA |
| `cost_reduction(n)` | Reduces PA cost by n resources | PA only |

**ModBattleCard** effects (§6.3 `ModBattleExpr`):

| Direction | Effect |
|-----------|--------|
| `Self` | +magnitude applied to submitting faction's Battlefield Strength threshold |
| `Opponent` | −magnitude applied to opponent's threshold |

**ModReactCard** effects: Full CA/PA effect field set (`success`, `successcrit`, `fail`, `failcrit`) — see §6.1.

*Legacy effect categories from earlier design (Effect extension, Detection immunity, Reach extension, Outcome addition) are superseded by the §6.1 modifier subclass schema. Outcome addition remains valid for ModActionCard via `success` on Automatic host action.*

### 11.8 Named Modifier Cards — Stubs

*Individual modifier card design is a full design pass pending decision D-04-08 and §11 redesign. Named cards below are direction-locked stubs.*


---

#### OVERTURE

*S77.*

#### Design Rationale

Overture is the bridge between STD.CA.9's anonymous funding gesture and formal alliance. When STD.CA.9 Fund succeeds, ARBITER delivers Overture (as a modifier card) to the acting faction. In a subsequent Month or Quarter, the faction assigns Overture to any of their Public Acts at Phase B. When that PA resolves at Beat 4 — regardless of outcome — ARBITER delivers a blank AccordForm to the acting faction. The faction drafts the terms and places the completed form in the Accord Placement Area during Beat 4 resolution or Debrief. The target faction then accepts, negotiates, or declines at Debrief. Mechanically: a free ModActionCard that attaches one Accord initiation to any PA slot.

**Timing constraint:** Overture cannot be used in the Month it is received. STD.CA.9 resolves at Beat 3; the host PA must be declared at Phase B (before Beat 3). Overture is held to Month 2, Month 3, or a subsequent Quarter. Tradeable per Art 03 §11.5.

**Host PA restriction:** Cannot be assigned to STD.PA.8 Table an Accord or GUI.PA.2 Infrastructure Bond — both already deliver a blank AccordForm at Beat 4; stacking Overture would duplicate the Accord initiation on the same PA.

**Outcome addition mechanic:** Fires as an additional Automatic outcome when the host PA resolves at Beat 4, regardless of the host PA's success or failure. See §11.7.

#### Design Checklist

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Modifier card attaching Accord initiation as PA outcome addition. Alliance-opening mechanic — earned through STD.CA.9; formalized through PA attachment. | Art 04 §11.1; Art 06 §9.4 |
| Voice fit | ✓ | Narrative in diplomatic register. Perspectives: TBD — deferred to modifier card voice pass (D-04-08). | Art 00 §9 |
| Doctrine alignment | ✓ | `faction = All` — no alignment penalty for using Overture; doctrine weight carried by STD.CA.9. | Art 04 §6.5 |
| Card type fit | ✓ | `ModActionCard` — assigned at Phase B; fires when host PA resolves. Does not enter Resolution Grid as independent action. | Art 04 §6.1, §11.1, §11.4 |
| Taxonomy fit | ✓ | No Layer / Function / Subject — modifier cards excluded per §11.1. | Art 04b §5.1, §9 |
| Balance | ✓ | `cost = None` — reward from STD.CA.9 success (2 Capital + roll risk already paid). Assignment free. Accord Portrait implications governed by Art 06 §9.9. Reassess STD.CA.9 threshold after §11 redesign. | Art 02 §8; Art 06 §9.9 |
| Effect duration | ✓ | Immediate — AccordForm delivery is instantaneous. Resulting Accord's duration governed by Art 06 §9.3–§9.7 independently. | Art 04 §5 P19 |
| Trigger validity | ✓ | ModActionCard — fires at Beat 4 when host PA resolves. Art 03 §5 P5 does not apply (ModActionCard bundled with host op at Covert Dispatch, not an independent play). | Art 04 §5 P5; §11.1 |
| Portrait validity | ✓ | No portrait entry for Overture assignment. Portrait from resulting Accord governed by Art 06 §9.9. | Art 04 §6.2; Art 06 §9.9 |
| Supported by components | ✓ | AccordForm (Art 06 §9.2). No new components. | Art 06 §9.2 |
| Supported by game procedure | ✓ | Assignment at Phase B; blank form delivered at Beat 4; faction drafts and places in Accord Placement Area at their discretion (no timing constraint; queued for next Debrief if placed outside Debrief window). Execution at Debrief per Art 06 §9.4. Delivery from ARBITER tableau: procedure in STD.CA.9 `arbiter_note`; Art 07 subroutine pass to formalize. | Art 03 Phase B; Art 06 §9.4; STD.CA.9 |
| New ARBITER behavior | ✓ | Deliver-from-tableau consistent with IS-xx and existing delivery subroutines. No novel ARBITER behavior — Art 07 pass formalizes. | Design Pillar 4.7b; Governing Rule 6.1 |
| Data schema validation | ✓ | All fields conform to §6.1/§6.2 modifier card schema. | Art 04 §6 |

#### Outstanding Issues

- **Perspectives:** TBD — deferred to modifier card voice pass (D-04-08)
- **Card ID:** TBD — pending 04-n1 numbering pass
- **Value rating (1–3):** TBD — deferred (D-04-08)
- **STD.CA.9 balance reassessment:** Flag for after §11 redesign confirms Overture's modifier value
- **ARBITER delivery formalization:** Overture delivery (STD.CA.9 → Beat 3 → acting faction hand) pending Art 07 ARBITER subroutine pass; STD.CA.9 `arbiter_note` covers interim reference

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ⚠ (Perspectives, ID, value rating) | |

```python
Overture = Card(
    id      = "STD.MOD.1",  version = "v1.0",
    name    = "Overture",
    tagline = "Extend a formal invitation to negotiate — attached to any public act you declare.",
    type    = ModActionCard,  faction = All,

    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = None,  # named on AccordForm when drafted — not declared at card assignment
    target_object   = AccordForm,

    target_taxonomy=None,
    affinity    = None,
    restriction = host_action.type not in [STD.PA.8, GUI.PA.2],  # avoids duplicate AccordForm on same PA
    cost        = None,  # earned as STD.CA.9 success reward; free to assign

    # Outcome addition — fires at Beat 4 on host PA resolution (any outcome: success or fail)
    success = arbiter.deliver(faction(acting), AccordForm(blank)),
    # Faction fills form per Art 06 §9.3; places in Accord Placement Area during Beat 4 or Debrief.
    # Art 06 §9.4 formation procedure applies from placement forward.

    portrait = {},  # no entry; Art 06 §9.9 governs Portrait for resulting Accord

    narrative    = "The terms don't matter yet. What matters is that the door is open.",
    perspectives = {},  # modifier card voice pass deferred to D-04-08
    design_note  = "Outcome addition modifier: attaches Accord initiation as additional Beat 4 outcome on any PA. "
                   "Fires on any host PA outcome — success or fail. Earned from STD.CA.9 success; free to assign. "
                   "Cannot assign to STD.PA.8 or GUI.PA.2 (duplicate AccordForm). "
                   "Must be held to a subsequent Month: Overture delivered at Beat 3 via STD.CA.9; host PA declared at Phase B before Beat 3. "
                   "Target faction not declared at Phase B — named on AccordForm when drafted.",
    arbiter_note = "On host PA resolution at Beat 4: deliver one blank AccordForm from ARBITER tableau supply to acting faction. "
                   "Faction drafts and places in Accord Placement Area at their discretion — no timing constraint. "
                   "Proceed per Art 06 §9.4.",
)
```

---

## 12. Rules & Constraints

## 12a. Debrief Action Cards

ARBITER-issued cards placed in a faction's Dispatch Case during operation resolution. Not player-submitted; not drawn from a deck. Carry a single instruction that fires at the start of Art 03 §11 Debrief. Physical form: disposable slip or reusable erasable card — design direction pending Art 11. Component: DB:100 (DebriefActionCard).

Debrief Action Cards are distinguished from all other card types by source and timing: created by ARBITER as a consequence of resolved operation; no faction player submits or draws them.

---

### 12a.1 Card Identifier: DA-xx

Debrief Action Cards use the **DA-xx** identifier prefix, assigned sequentially as subtypes are defined.

---

### 12a.2 DA-01 — SCIFRecord

Produced by Ghost SCIF card on successful Beat 3 resolution (see Art 03 §7.2 Ghost — SCIF). ARBITER places one completed SCIFRecord in Ghost's Dispatch Case at Beat 3 instantiation.

**Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `quarter` | Integer | Quarter in which the card was produced |
| `draw_ring1` | Integer | Target faction's Ring 1 structure block count at Beat 3 (snapshot) |
| `draw_ring2` | Integer | Target faction's Ring 2 structure block count at Beat 3 (snapshot) |
| `draw_ring3` | Integer | Target faction's Ring 3 structure block count at Beat 3 (snapshot) |

**Debrief procedure (Art 03 §11):** At the start of Debrief, process all DA-01 slips in Ghost's Dispatch Case:

1. For each recorded ring count (draw_ring1, draw_ring2, draw_ring3): draw that many cards from the corresponding Ring modifier deck.
2. Sum the three ring counts. Draw from the Ghost faction deck: 0–1 total → 0 draws; 2–3 → 1; 4–5 → 2; 6+ → 3.
3. No ring-eligibility check applies to these draws.
4. Discard the DA-01 slip after use.
5. DA-01 slips remaining in the Dispatch Case at Phase 21 are discarded without effect.

---

## 13. Card Information Design Requirements

*Full visual design in Artifact 11. Card content tables in Artifact 09. These requirements are design-level constraints both must satisfy.*

### 13.1 All Action Cards

Card face must carry in clear information hierarchy:
1. Card ID (primary key)
2. Card name
3. Tagline
4. Card type indicator
5. Beat (numeric)
6. Target
7. Restriction
8. Primary cost / Secondary cost (separate fields)
9. Faction affinity / Affinity bonus (if applicable)
10. Difficulty
11. Effect fields (grouped under single "Effect" header — crit success, success, failure, crit failure listed beneath)
12. Portrait (positive/negative values only)
13. Narrative anchor
14. Taxonomy (Layer — Function — Subject)

Faction perspectives are in the card data structure. Visual design (Artifact 11) decides whether they appear on the card face.

### 13.2 Modifier Cards — Faction

Face: name, type indicator, effect, attachment rule (if restricted), Portrait (if applicable), value rating (1–3). Back: faction color, faction symbol.

### 13.3 Modifier Cards — Ring

Face: ring constraint statement as visually distinct element, name, type indicator, effect, Portrait (if applicable), value rating (1–3). Back: ring color, ring name.

### 13.4 Pass Cards

Four named variants (PS-01–PS-04). Face: variant name, tagline, and secondary effect (if any). Ghost rule note small on all variants. Back: neutral grey. Full card face design pending Artifact 11 visual pass.

### 13.5 Emergency Response Cards

Face: name, faction indicator, trigger condition, complete effect text, Board Strength interaction note. Pre-sealed in faction envelopes at setup. Full card data structure review pending (D-04-10).

---

## 14. Special Conditions & Gameplay Impacts

### 14.1 Emergency Response Cards

*Card data structure review pending D-04-10. Effects carried forward.*

| Faction | Emergency Response | Effect |
|---------|-------------------|--------|
| The Guild | Emergency Fortification | Place 2 presence tokens in any district. Remove 1 structure block from Apex faction's total. |
| The Directorate | Emergency Injunction | Apex faction loses 2 presence tokens from their highest-token district. Board Strength recalculated. |
| Ghost | Counter-Analysis | Reveal one Intel token publicly. If accurate and damaging to Apex faction: Apex faction Public Standing −2 before threshold check. |
| The Network | Emergency Broadcast | Apex faction Public Standing −3 immediately. VP calculation affected. |
| The Syndicate | Hostile Takeover Bid | Offer Apex faction 4 Capital for 2 structure blocks (converted to Syndicate). If accepted: Board Strength −2. If declined: no effect. |

### 14.2 Countermeasure Interaction

Countermeasure cards interact with covert operations only — not public acts. Type A (district block) blocks covert operations targeting the named district. Type B (faction defense) reduces covert operation difficulty against that faction's assets. Full Countermeasure card design pending D-04-12.

### 14.3 Resource Availability Constraint

Covert operation resources must be physically present in the dispatch case at Beat 3. Public act resources must be physically paid at Declaration. If absent:
- **Covert:** Action fails. Resources spent. ARBITER notes privately.
- **Political:** Declaration void. Faction takes Political Pass. Public Standing −1 as "failed commitment." Resources already paid returned.

### 14.4 Self-Directed Undermine

A faction may submit Undermine targeting themselves (cost: 1 native resource + 1 district native resource — no Intel token required). Creates a false Public Standing drop recorded as unattributed. ARBITER does not note self-targeting.

### 14.5 Deck Exhaustion

Covert and political draw decks: when exhausted, shuffle discard pile immediately to form new deck and continue. Modifier decks are not reshuffled.

### 14.6 Resource Acquisition — Non-Native Resources

Non-native resources acquired through:
1. District incursion — presence in districts controlled by the resource's native faction
2. Direct faction-to-faction trade at any agreed rate
3. ARBITER conversion — 4:1 universal rate

---

## 15. Examples & Exceptions

### Example A — Ghost 4-Operation Round

*Round 4. Ghost uses Political Pass. Dispatch case: Pattern Match (targeting Directorate — Invoke Jurisdiction), Archive Recovery, Deep Cover, Gather (Government Citadel).*

ARBITER opens case at Beat 3. Pattern Match resolves first — Directorate submitted Invoke Jurisdiction this round. Pattern Match succeeds; resolves as Invoke Jurisdiction targeting Financial Clearing. Archive Recovery: Ghost recovers Round 2 Intel token. Deep Cover: Round 3 Gather attribution permanently removed. Gather at Government Citadel: Average −20 Core = Challenging. Roll → 19. Target 01–25. Succeeds.

### Example B — Denounce Mechanics

*Round 5. Network holds Round 3 Intel token naming Ghost (age 2 — stale). Network declares Denounce.*

Cost: 1 Findings + 2 additional Findings (stale) = 3 Findings total. Verbal accusation delivered. Average difficulty. Roll → 22. Target 01–45. Success. Ghost Public Standing −2. Network Public Standing +1. Token spent.

### Example C — Commission With Guild Affinity

*Round 3. Guild operational markers at Power Grid (Present) and Industrial Fringe (Present). Guild declares Commission.*

Guild affinity: secondary cost waived per district. Cost: 1 Capacity + 1 Capacity (Power Grid native) + 1 Capacity (Industrial Fringe native) = 3 Capacity. Both structures placed immediately.

### Example D — Ring Modifier Constraint in Trade

*Round 5. Syndicate holds 2 Infrastructure modifier cards. Guild offers 2 Capital for them. Guild attaches one to Commission targeting Power Grid (Infrastructure) — constraint satisfied. Guild later attempts to attach the second to Gather targeting University Perimeter (Sprawl) — ARBITER rejects. Card face: "Usable on Infrastructure district targets only."*

### Example E — Burst Play and Post-Burst Trade

*Round 6. Directorate triggers Burst Play. 7 modifier cards → 4 Mandate + 3 Capital. Faction modifier deck removed. ARBITER: "The Directorate has liquidated their operational reserve."*

*Round 7. Guild offers Directorate 2 modifier cards as part of Accord. Directorate accepts and uses them normally — Burst removed draw access, not ability to hold or play cards.*

---

## 16. Appendix — Outstanding Decisions & Assumptions

### Decisions Blocking Sign-Off

| ID | Description | Blocking what |
|----|-------------|---------------|
| D-04-01 | Card set completeness — taxonomy gaps may warrant additional cards before production. Setup pool sizes (30/24 covert, 20/12 political) are assumptions pending final card set. | Production, Artifact 09 |
| D-04-02 | Ghost GHO.CA.1–GHO.CA.5 redesign — GHO.CA.3 replaced with Dossier Breach (S51); GHO.CA.4 now unique. Portrait Shift, targeted Reveal, Copy subset gaps remain open. | Artifact 09 |
| D-04-03 | Directorate DIR.CA.1–DIR.CA.4 redesign — DIR.CA.4 replaced with Tactical Redirection (S51). Block duplication resolved. Mandate generation and Public Standing Shift cards still needed. | Artifact 09 |
| D-04-04 | Network NET.CA.1–NET.CA.5 redesign — NET.CA.2 replaced with Disclosure Loop (S51). Exposure generation addressed. NET.CA.1/NET.CA.3 Reveal overlap and Public Standing Shift card remain open. | Artifact 09 |
| D-04-05 | Syndicate SYN.CA.1–SYN.CA.5 redesign — zero information capability; Corrupt Accord and Redirect Accord unused. Approve current set or redesign? | Artifact 09 |
| D-04-06 | Public acts STD.PA.1–GHO.PA.2 full card data structure review — all fields (Beat, Taxonomy, Faction perspectives, Restriction, crit effects, Portrait) need card-by-card application. | Artifact 09 |
| D-04-07 | Modifier card in-world naming — "Modifier cards" is a working designation. | Artifact 09 |
| D-04-08 | Modifier card individual content — faction modifier decks and ring modifier decks have no individual card designs. | Artifact 09, physical production |
| D-04-09 | Adjacency definition — formal district adjacency table needed in Artifact 01. Required by STD.CA.2, STD.CA.4, STD.CA.5, GUI.CA.4, NET.CA.4, NET.CA.5. | Artifact 01, physical play |
| D-04-10 | Emergency Response card data structure review — full card data structure not yet applied. | Artifact 09 |
| D-04-11 | Intel token mechanics cross-reference — Art 02 §12 audit against current card designs needed. Potential inconsistency with Denounce cost structure, token age rules, STD.CA.5 crit failure. | Art 02 |
| D-04-12 | Countermeasure card design — referenced in §14.2 and Artifact 03 Phase 5 but no card data structure definition exists. | Artifact 09 |

### Assumptions Requiring Explicit Confirmation

| ID | Assumption | Impact if wrong |
|----|------------|----------------|
| A-04-01 | Setup pool sizes (30/24 covert, 20/12 political) are correct for the final card set | Deck construction rules change |
| A-04-02 | Deck exhaustion occurs at approximately Round 4 | Pacing and strategy may differ — playtesting required |
| A-04-03 | Maximum 1 structure per faction per district is the right balance cap | Guild doctrine and late-game economy affected |
| A-04-04 | Ghost 4-operation slot available only when Ghost passes politically — confirmed design intent | Ghost balance and doctrine affected |
| A-04-05 | Pre-written ARBITER notification slips are feasible as paper prototype components | ✅ Resolved S50 — Notification Slip (NS-xx, id=95) and Intel Delivery Slip (IS-xx, id=96) registered in 00b §4 and `component` table. Text/format: Art 07 (F-ART07-01). |

### Cross-Artifact Flags

| Flag | Description | Target artifact |
|------|-------------|----------------|
| F-ART01-01 | Formal district adjacency table needed | Artifact 01 |
| F-ART02A-01 | Global convention: "at least 1 presence token" includes claim markers. Defined once here, not restated on cards | Art 02, Artifact 09 |
| F-ART02B-01 | Intel token mechanics cross-reference audit | Art 02 |
| F-ART03-01 | Beat 2 renamed "The Ground Shifts" — applied in Artifact 03 v1.5 | ✅ Done |
| F-ART03-02 | Step 6 Card Draw rewritten — applied in Artifact 03 v1.5 | ✅ Done |
| F-ART03-03 | Free Accord card (STD.CA.9) not from political deck — noted in Artifact 03 Declaration phase | ✅ Done |
| F-ART07-01 | Pre-written notification slip component category and text | Artifact 07 |
| F-ART09-01 | "Delivered in case" — standard phrase for privately delivered effects | Artifact 09 |
| F-ART09-02 | "Return primary cost to dispatch case" — standard resolution phrase | Artifact 09 |
| F-ART09-03 | Modifier card value rating field (1–3) on every modifier card | Artifact 09 |
| F-ART09-04 | Free Accord card is not drawn from political deck — ARBITER-delivered | Artifact 09 |

---

*End of Artifact 04 — Card System v0.9.52*
