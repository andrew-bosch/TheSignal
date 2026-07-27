# 04 — CARD SYSTEM
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.9.90 Draft  
**Status:** 🔄 Draft — Pending Sign-Off  
**Last Updated:** 2026-07-17  
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
| §7 | [Card Specifications](#7-card-specifications) — see File Map below; content lives in Parts 2–4e |
| §8 | [Card Taxonomy Index](#8-card-taxonomy-index) |
| §9 | [Faction Coverage Matrix](#9-faction-coverage-matrix) |
| §10 | [Deck Construction & Pool Selection](#10-deck-construction--pool-selection) |
| §11 | [Rules & Constraints — Modifier Cards](#11-rules-constraints-modifier-cards) |
| §12 | [Rules & Constraints](#12-rules-constraints) |
| §13 | [Card Information Design Requirements](#13-card-information-design-requirements) |
| §14 | [Special Conditions & Gameplay Impacts](#14-special-conditions-gameplay-impacts) |

**File Map:** Artifact 04 is physically split across 8 files — one version, one sign-off, single artifact. Card specs are addressed by Card ID, not section number.

| File | Content |
|------|---------|
| `04___Card_System___Part1_Core.md` (this file) | §1–6, §8–15 |
| [`04___Card_System___Part2_Standard.md`](04___Card_System___Part2_Standard.md) | Standard — Covert Operations, Public Acts (STD.CA, STD.PA) |
| [`04___Card_System___Part3_Ring_Modifiers.md`](04___Card_System___Part3_Ring_Modifiers.md) | Ring-sourced Modifier Cards (STD.MOD.1–133) |
| [`04___Card_System___Part4a_Guild.md`](04___Card_System___Part4a_Guild.md) | Guild |
| [`04___Card_System___Part4b_Ghost.md`](04___Card_System___Part4b_Ghost.md) | Ghost |
| [`04___Card_System___Part4c_Directorate.md`](04___Card_System___Part4c_Directorate.md) | Directorate |
| [`04___Card_System___Part4d_Network.md`](04___Card_System___Part4d_Network.md) | Network |
| [`04___Card_System___Part4e_Syndicate.md`](04___Card_System___Part4e_Syndicate.md) | Syndicate |

`04___Card_System.md` (the original monolith) is regenerated from these 8 parts by `tools/assemble_card_system.py` — it is a build artifact, not source of truth, and stays around for legacy analysis scripts that expect a single file.

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
- **Zero payment:** action is voided; the card is returned to the faction

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

**P29 — Discard-Immune Cards**

A card with `on_discard` set is immune to every discard event that would otherwise apply to it — normal post-resolution discard and any effect that discards cards from a faction's hand (e.g. `arbiter.discard_hand`) alike. Instead of being removed, the card returns to the acting faction's hand. This is not an ARBITER-tracked step: the acting faction self-polices the return as part of their own end-of-Beat cleanup, the same way Permanent card-as-condition cards are self-policed (Pillar 4.7b; ARBITER adjudicates disputes only, GR 6.1a). `on_discard = None` on every card by default; set only where a card is explicitly designed as reusable/evergreen rather than consumed (currently: STD.PA.9 Town Hall, the Floor Act — PM02 D04-13/L216).

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

### ModReactCard Design Checklist

ModReactCards introduce design dimensions the checklist above doesn't cover — all specific to trigger-based firing. Use this addendum during any design review pass on ModReactCard stubs, including Issued ModReactCards (GD-01, Overture, The Fixer — §11.1). Rows here don't repeat what the main checklist already asks: trigger observability is covered by that table's Trigger validity row, persistence timing by its Persistence row, and PS signal legibility by its Portrait validity row.

| Criterion | Design question | Guidance |
|-----------|----------------|---------|
| **Trigger frequency** | How often does this trigger fire in a typical Quarter? | Underfire (condition rarely met) = dead weight. Overfire (every round) = oppressive or trivial. Document expected frequency in `design_note`. |
| **Firing window** | Does this card's trigger fire at the same time as other React cards? Is priority order needed? | Multiple React cards with identical or simultaneous triggers compete. If racing is possible, confirm resolution order or note as a design gap. |
| **Automatic vs. d100** | Is `resolution = Automatic` justified? | Automatic is appropriate when the trigger is precisely defined and the effect is bounded. d100 is appropriate when outcome should depend on execution quality or add tension. |
| **Stack behavior** | Can multiple copies fire on the same trigger event in the same Quarter? | If a faction holds two copies and the trigger fires once, do both fire? Document the answer in `design_note`; add a restriction clause if stacking is undesirable. |
| **Ring constraint** | Is `ring_constraint` set correctly relative to trigger frequency and effect power? | Ring-constrained React cards fire only when the trigger occurs in the specified ring. If trigger frequency is already low, a ring constraint may make the card unplayable. |

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
    value_rating: int | None                # 1–4; power/strength tier, printed on card face. Base Card() field — all card types inherit it. CA/PA meaning not yet defined; None = TBD/unscaffolded pending whole-set cost-derivation analysis (04-n178).
    trigger:      TriggerExpr | None        # None = default beat timing
    resolution_type: ResolutionType | None  # confirmed enum (§6.3) — feeds 00c §8; formalized from a free-form str, schema_cleanup_log #41
    outcome_type: OutcomeType | None        # public acts only
    persistence:           Persistence              # card table presence — Immediate/Transient/Seasonal/Permanent; default Immediate for covert ops
    persistence_condition: BoolExpr | None           # Seasonal/Permanent only; a genuine continuously-evaluated state predicate — Standing Condition discarded immediately when this evaluates False. NOT for one-time clearing events — use persistence_clearing_trigger for those (schema_cleanup_log #2)
    persistence_clearing_trigger: TriggerExpr | None # Seasonal/Permanent only; the one-time board event that ends this Standing Condition (e.g. a payment, a submission) — same TriggerExpr vocabulary as `trigger` (§6.3). Distinct from persistence_condition: an event, not a continuous predicate. None = no discrete clearing event (either the Standing Condition never clears, or it clears on a phase boundary already implied by Seasonal/persistence_condition)
    persistence_effect:    MutationExpr | None        # Seasonal/Permanent only; the ongoing effect of the Standing Condition while it remains active

    # ── Targeting ─────────────────────────────────── expressions
    target_district:  DistrictExpr
    target_faction:   FactionExpr  | None
    target_object:    ObjectExpr   | None
    target_taxonomy:  TaxonomyExpr | None   # action taxonomy category this card targets; None = no taxonomy target

    # ── Logic ─────────────────────────────────────── predicates + expressions
    affinity:     ConditionalExpr | None    # evaluated before cost; None on every FactionSpecific card
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
    on_discard:   MutationExpr | None       # None = normal discard applies; else fires instead of discard — including targeted hand-discard effects — card returns to hand (P29)

    # ── Portrait ──────────────────────────────────── dimension table  [VS-06]
    portrait:     dict[Faction, PortraitEntry] | None   # None = no portrait effect

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
    # value_rating inherited from Card()
    ring_constraint:  Ring | None          # None = no deployment restriction; Ring = usable only targeting that ring's districts
    ring_origin:      Ring | None          # None = faction modifier deck; 1/2/3 = drawn from that ring's modifier deck
    acquisition:      AcquisitionSource    # Deck (default — drawn at Upkeep) | Issued (ARBITER-delivered as a consequence)
    generating_card:  CardID | list[CardID] | None   # required when acquisition=Issued; None when Deck


class ModBattleCard(Card):
    # Modifier for Battlefield Strength resolution (§10 Contested District Resolution). Field constraints: §6.2.
    effect:           ModBattleExpr        # delta on a named contesting faction's total; direction (Boost | Hinder) + target + magnitude — see §6.3
    # value_rating inherited from Card()
    ring_constraint:  Ring | None          # if set, usable only in Battlefield Strength for a district in that ring
    ring_origin:      Ring | None          # None = faction modifier deck; 1/2/3 = drawn from that ring's modifier deck
    acquisition:      AcquisitionSource    # Deck (default — drawn at Upkeep) | Issued (ARBITER-delivered as a consequence)
    generating_card:  CardID | list[CardID] | None   # required when acquisition=Issued; None when Deck


class ModReactCard(Card):
    # Modifier firing on a publicly observable board state delta. Played in Faction Resolution Grid.
    # trigger:     required (never None) — defines what activates the card; overrides Card.trigger default
    # beat:        always None — React fires on trigger condition, not at a named beat
    # persistence: Immediate = consumed on fire (default); Seasonal = remains on FRG as a Standing Condition until Quarter end;
    #              Permanent = remains until persistence_condition goes False or persistence_clearing_trigger fires
    #              (e.g. DIR.MOD.9 Fiscal Sanction — clears via persistence_clearing_trigger, schema_cleanup_log #2)
    # Field constraints: §6.2.
    # value_rating inherited from Card()
    ring_constraint:  Ring | None          # None = no deployment restriction; Ring = fires only when trigger fires in that ring
    ring_origin:      Ring | None          # None = faction modifier deck; 1/2/3 = drawn from that ring's modifier deck
    acquisition:      AcquisitionSource    # Deck (default — drawn at Upkeep) | Issued (ARBITER-delivered as a consequence)
    generating_card:  CardID | list[CardID] | None   # required when acquisition=Issued; None when Deck
```

**Acquisition axis:** `acquisition` is orthogonal to which of the three subclasses above a card is. A card fires according to its subclass (bundled-with-host / Battlefield-commit / trigger-based) regardless of where it came from. Most cards are `acquisition=Deck` — drawn from a Faction or Ring Modifier deck at Upkeep (§11.2), gated by `ring_origin`. A card is `acquisition=Issued` when ARBITER hands it directly to a faction as a specific, named consequence of another card's resolution (`generating_card`) — no Upkeep draw, no deck, no `ring_origin`. Current Issued cards: GD-01 Grant Deed, STD.MOD.1 Overture, SYN.MOD.1 The Fixer — all three are structurally ModReactCard (fire on a trigger condition) under this model; nothing yet exercises an Issued ModActionCard or ModBattleCard, but the schema doesn't rule it out.

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
| threshold | Metadata | int | Base difficulty as numeric threshold; None when Automatic. **Must be a multiple of 5 (L280).** Reason: threshold-slider physical design and mental math both favor round-5 increments — lower cognitive overhead reading a d100 roll against a multiple of 5 than an arbitrary number. | Face |
| ring_mod | Metadata | dict[Ring, int] | Per-ring threshold adjustment; positive = easier, negative = harder; None when no variation | Face |
| doctrine_mod | Metadata | dict[PentagramRelation, int] | Per-doctrinal-relationship threshold adjustment based on acting/target faction pentagram proximity; positive = easier, negative = harder; None when no faction target or no doctrinal variation | Face |
| value_rating | Metadata | int \| None | 1–4. Power/strength tier printed on card face; used in Splay calculation for Modifier cards. Base Card() field — all card types inherit it. Feeds the whole-set cost-derivation model (04-n178). CA/PA definition not yet set; `None` = TBD/unscaffolded until the whole-set analysis assigns real values. | Face |
| trigger | Metadata | TriggerExpr | Activation condition when card does not fire at default beat timing; None = default | TBD |
| resolution_type | Metadata | ResolutionType | Strategic classification of how uncertainty resolves — confirmed 3-value enum (§6.3, schema_cleanup_log #41); feeds 00c §8 | No |
| outcome_type | Metadata | OutcomeType | Public act resolution process type; None for covert operations | Face |
| persistence | Metadata | Persistence | How long the card remains on the table as a game state marker — Immediate: removed at Beat 4 cleanup; Transient: removed at Close Month of current Month; Seasonal: removed at Phase 21 (End of Quarter); Permanent: removed only by explicit game action. Default for covert operations: Immediate. A Seasonal/Permanent card in play is a **Standing Condition** (locked term, schema_cleanup_log #2) — Card-as-condition PAs with standing board-condition effects commonly use Permanent (e.g., DIR.PA.1/PA.3/PA.5/PA.6/PA.11). | Face |
| persistence_condition | Metadata | BoolExpr | Continuously-evaluated state predicate for a Seasonal/Permanent Standing Condition — discarded immediately when it evaluates False. For a one-time clearing event, use `persistence_clearing_trigger` instead (schema_cleanup_log #2). None for Immediate/Transient cards, and for Seasonal/Permanent cards with no continuous-predicate clearing condition. | Face |
| persistence_clearing_trigger | Metadata | TriggerExpr | The one-time board event that ends a Seasonal/Permanent Standing Condition (e.g. a payment, a submission) — same TriggerExpr vocabulary as `trigger` (§6.3). Distinct from `persistence_condition`: an event, not a continuous predicate. None = no discrete clearing event. | Face |
| persistence_effect | Metadata | MutationExpr | The Standing Condition's ongoing effect while a Seasonal/Permanent card remains in play; evaluated continuously until cleared by `persistence_condition` going False or `persistence_clearing_trigger` firing. Use `game.board_condition(...)` to express scoped persistent effects. None for Immediate/Transient cards. | Face |
| target_district | Targeting | DistrictExpr | District scope for the card's effect | Face |
| target_faction | Targeting | FactionExpr | Faction this card targets; None = no faction target | Face |
| target_object | Targeting | ObjectExpr | Game component this card acts on; None = no object target | Face |
| target_taxonomy | Targeting | TaxonomyExpr | Action taxonomy category this card targets (Layer/Function or Layer/Function/Subject); used when the effect targets a class of actions rather than a specific object; declared at Phase B alongside target_faction; None = no taxonomy target | Face |
| affinity | Logic | ConditionalExpr | Faction-based cost/threshold modifier, evaluated before cost — differentiates how the *same* card plays out depending on which faction submits it. Meaningful only on a Standard card (`subtype = Standard`, `faction = All`), where more than one faction genuinely could submit it. `None` on every FactionSpecific card — the card is already locked to one faction, so there's no other faction's terms to differentiate from. | Face |
| restriction | Logic | BoolExpr | Submission preconditions — card unplayable if evaluates False | Face |
| cost | Logic | CostExpr | Physical, fungible resources consumed at submission — valid resource types are native, capital, mandate, exposure, findings, capacity (§6.3), plus Intel Token as a confirmed discrete-object cost category (§6.3). Non-fungible markers (Public Standing, presence tiers) are not valid cost values; marker changes that function as a cost belong in `success`/`fail` effect fields. | Face |
| boost | Logic | BoostExpr | Optional variable-multiplier mechanic — player submits additional resources beyond base cost; no declaration required. ARBITER detects at Beat 0: n = (total submitted − base cost) / boost unit cost; places n BoostMarker tokens (BM-xx) on the card's grid slot alongside the card. At Beat 2/3 resolution: effect fires (1 + BM-xx count) times; BM-xx returned to ARBITER supply at beat cleanup. For threshold-scaling cards, threshold is locked at Beat 0 using total count (1 + BM-xx). Boost unit cost may differ from base cost resource type. None = no boost mechanic. | Face |
| success | Effects | MutationExpr | Primary effect on resolution success | Face |
| successcrit | Effects | MutationExpr | Additive delta on critical success (roll ≤ 5, i.e. 01–05); None when Automatic | Face |
| fail | Effects | MutationExpr | Effect on failure; None = cost spent, no additional effect | Face |
| failcrit | Effects | MutationExpr | Additive delta on critical failure (roll ≥ 96, i.e. 96–00); None when Automatic | Face |
| on_accept | Effects | MutationExpr | ElectPlayer outcome type only — effect applied when target accepts the offer at resolution; None when outcome_type ≠ ElectPlayer | Face |
| on_decline | Effects | MutationExpr | ElectPlayer outcome type only — effect applied when target declines the offer at resolution; None when outcome_type ≠ ElectPlayer | Face |
| on_discard | Effects | MutationExpr | None = normal discard applies. When set, fires instead of any discard event — including targeted hand-discard effects (e.g. `arbiter.discard_hand`) — in place of removing the card. Self-policed by the acting faction as part of their own end-of-Beat cleanup; not an ARBITER-tracked step (P29, Pillar 4.7b, GR 6.1a). | Face |
| portrait | Portrait | dict[Faction, PortraitEntry] \| None | Per-faction portrait scoring — evaluated by ARBITER; analyzed in DB; None = no portrait effect | TBD |
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
| effect | ModBattleCard | ModBattleExpr | Delta (Boost or Hinder) applied to a named contesting faction's Battlefield Strength total (Art 03 §10.1.2); target faction is chosen by the playing faction at commit and need not be themselves, nor a contestant — Art 03 §10.1.2 Step 2 | Face |
| ring_constraint | All modifier subclasses | Ring \| None | Deployment restriction set at card design time by narrative — location-anchored assets get the ring value; portable assets get None. ModActionCard: usable only with ops targeting that ring's districts. ModBattleCard: usable only in Battlefield Strength for a district in that ring. ModReactCard: fires only when trigger condition occurs in that ring's districts. Semantics under review for Ring-sourced cards specifically — PM05 04-n161. | Face |
| ring_origin | All modifier subclasses | Ring \| None | Which modifier deck this card belongs to — None = faction modifier deck; 1/2/3 = Ring 1/2/3 modifier deck. Determines draw eligibility (§11.2) and card back color. Separate from ring_constraint: a Ring 1 card (ring_origin=1) may have ring_constraint=None (portable, no deployment restriction). None (not applicable) when acquisition=Issued. | No |
| acquisition | All modifier subclasses | AcquisitionSource | Deck (default) = drawn from a Faction or Ring Modifier deck at Upkeep, gated by ring_origin. Issued = ARBITER delivers the card directly as a named consequence of another card's resolution — no Upkeep draw, no deck, ring_origin forced None. Orthogonal to subclass — any of the three subclasses may in principle be Issued; all current Issued cards happen to be ModReactCard. | Face |
| generating_card | All modifier subclasses | CardID \| list[CardID] \| None | Which card's resolution delivers this card — required when acquisition=Issued (e.g. GD-01: [SYN.CA.8, GUI.CA.10]; Overture: STD.CA.9); None when acquisition=Deck. | No |

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
| persistence / persistence_condition / persistence_clearing_trigger / persistence_effect | None | None | — |
| target_district / target_faction / target_object / target_taxonomy | None | None | — |
| affinity / restriction | — | None | — |
| boost | None | None | — |
| cost | None | None | — |
| success / successcrit / fail / failcrit | None | None | — |
| on_accept / on_decline | None | None | — |
| on_discard | None | None | — |
| ps_framing | None | None | — |
| perspectives / design_note | — | None | — |
| acquisition | Deck by default — omit unless Issued | Deck by default — omit unless Issued | Deck by default — omit unless Issued |
| generating_card | None unless acquisition=Issued | None unless acquisition=Issued | None unless acquisition=Issued |

*ModReactCard: only `beat` is always None. All other `—` fields are live — set per individual card design. `acquisition` defaults to Deck for every existing stub that doesn't state it — only state it explicitly on the 3 current Issued cards.*

*`cost` is locked `None` for `ModActionCard` and `ModBattleCard`, but for two independently-arrived-at reasons (PM02 L256, L302), not one shared rationale — `ModActionCard`'s cost could technically be enforced (Beat 0 payment validation exists), but the splay-display convention (Art 03 §9.4.0.1 Step 4: modifier value printed at top and bottom edge, splayed beneath the host operation card) folds it into the host packet's total drain rather than tracking it as a distinct line item; `ModBattleCard`'s cost is genuinely unenforceable — Art 03 §10.1.2's commit sequence has no cost validation/payment step at all. `ModReactCard`'s `cost` is live and per-card design — it resolves through its own trigger rather than a host's commit, so a real payment step exists.*

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
ResolutionType:      Probabilistic | Transactional | PositionalWager
# Formalized from a free-form str (schema_cleanup_log #41) — was 9 values in active use, only
# 2 documented. Full-corpus discriminating test applied to every candidate: does deleting this value lose
# information no other field already carries? Result: 6 of 9 either mapped directly onto Resolution
# (Probabilistic = d100, Transactional = Automatic) or were pure restatements of another field; only one
# genuinely distinct third category survived.
#   Probabilistic:    resolution = d100 always.
#   Transactional:    resolution = Automatic always — immediate, deterministic, no cross-beat dependency.
#   PositionalWager:  resolution = Automatic, but the effect targets a not-yet-revealed future beat's
#                      submission slate (e.g. a Beat 2 card modifying a Beat 4 op that hasn't been declared
#                      yet) — deterministic once resolved, but committed against genuinely unknown
#                      information, unlike a plain Transactional card. 8 confirmed instances: STD.CA.6,
#                      STD.CA.7, STD.CA.10, GUI.CA.1/2/6/9, SYN.CA.6.
# Collapsed into the above, not separately confirmed:
#   "Contested"            → Probabilistic. 5 instances (STD.PA.2/4/5/6, NET.PA.1); only STD.PA.2 actually
#                            placed a ContestedMarker (a `success`-field effect) — the label didn't
#                            correlate with a real distinct mechanism across its own cluster.
#   "Permanent public act" → Transactional. 3 instances (DIR.PA.5/6/11); fully redundant with the
#                            existing `persistence = Permanent` field.
#   "Predictive"            → Transactional. 1 instance (GHO.CA.1); resolution = Automatic, deterministic
#                            declare-then-verify check — not a distinct resolution mechanism.
# Not formalized — tied to broken/blocked cards, left as non-conforming pending their own separate fix:
#   "Conditional"  — GHO.MOD.1, a pre-S127 fossil already carrying an invalid `resolution = Prediction`
#                    value (schema_cleanup_log #12). Fix belongs to that item's own reconciliation.
#   "Deceptive"    — Backdate, 🚫 BLOCKED (GR 7.2b, PM05 04-n103), fundamental redesign required.
#   "Verification" — Field Verification, 🚫 BLOCKED (same GR 7.2b reason, same PM05 gate).
#   "PlayerChoice(target)" — pre-registered (PM05 04-n36) for a not-yet-built Directorate card family;
#                    never actually appears as a real field value anywhere in the corpus.
Ring:                0 (Chorus Node) | 1 (Core) | 2 (The Mid) | 3 (Baryo)
PentagramRelation:   Neighbor | Opposed
OutcomeType:         Binary | ElectPlayer | ElectDistrict | ElectFaction | BilateralAgreement | Unilateral
Persistence:         Immediate | Transient | Seasonal | Permanent
AcquisitionSource:   Deck | Issued   # modifier subclasses only (§6.1/§6.2) — Deck = drawn at Upkeep; Issued = ARBITER-delivered

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
                     | component[.scope][.attribute].change(faction[, except])
# component:   presence_chip | structure_block | deployment_marker | dominant_marker |
#              established_marker | tension_marker | standing_marker | world_event |
#              accord | resolution_grid
# scope:       ring1 | ring2 | ring3 | district.{id} | global  (optional filter)
# attribute:   optional sub-state filter on component (e.g., influence level, chip count)
# change:      placed | removed | converted | blocked | increased | decreased |
#              played | expired | corrupted | updated
# faction:     Any | Ghost | Network | Syndicate | Guild | Directorate
# except:      optional Faction — subtracted from faction=Any's match set (see semantics below)
#
# faction=Any semantics: inclusive of the reacting card's own faction by default — Any means every
# faction, no implicit self-exclusion. A card that needs to exclude self (e.g. because self-fire
# would be actively harmful, not just a no-op) states it explicitly with except=X.
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
#   accord.placed / corrupted / removed              (accord.removed: breach or expiry; accord.corrupted: requires Art 06 breach procedure ARBITER corrupt step on Accord form — 06-n pending)
#   resolution_grid.updated                            (after Beat 0 public reveal)
#   broadcast_card.placed                              (db25 — public SitRep card placed in Situation Report Zone; fires at Upkeep phase 1 and Beat 5 phase 18)
#   public_act.placed_on_frg(faction, ...)             (any faction places a PA face-up on their FRG at §9.2 Public Declaration)
#
# ring= confirmed valid on all .removed() forms, symmetric with .placed() (schema_cleanup_log #3,
# PM05 04-n195 item 1) — e.g. presence_chip.removed(faction=X, ring=Z) is confirmed vocabulary,
# not just presence_chip.placed(faction=X, ring=Z).
#
# public_act.placed_on_frg() additionally accepts uses_intel_token=True as a confirmed filter
# parameter (schema_cleanup_log #12/#13, PM05 04-n195 item 10) — matches only when the placed PA
# carries an Intel Token as part of its declared cost/payment. Default (omitted) = no filter, any
# PA placement matches regardless of Intel Token presence.
#
# board_state.changed(component=, change=, cause=, faction=, district=, ring=) — general-purpose
# TriggerExpr primitive (PM05 04-n195 items 11/12) for cards that need to react to more than one
# component type and/or any direction of change at once, which the itemized single-event forms above
# can't express (they have no OR-composition). Coexists with the itemized forms — those remain the
# precise/preferred choice for a card that only cares about one specific event and direction;
# board_state.changed() is for the genuinely broader case.
#   component: presence_chip | structure_block | standing_marker | deployment_marker | accord |
#              public_act | modifier_card | native_resource | intel_token | target_profile | Any
#              — component=Any is an open/extensible category meaning "any publicly visible,
#              non-procedural board object" (same public/player-driven scope as the Excluded notes
#              below already establish) — a new component type added to the game later qualifies
#              automatically, no re-confirmation of this primitive needed. May also be a list of
#              specific component values to match more than one type but not all.
#   change:    placed | removed | increased | decreased | moved | corrupted | Any
#              — change=Any matches any direction. Not every component supports every change value
#              (e.g. standing_marker only ever increased/decreased); use whichever applies.
#   cause:     public_act | covert_operation | modifier_card | upkeep | Any
#              — filters by what produced the change, distinct from component (what changed). No
#              separate "arbiter" value — ARBITER executes the change but is never itself the cause;
#              the cause is always the CA, PA, or Modifier Card that made ARBITER act (upkeep is a
#              4th, procedural cause, kept for completeness even though no confirmed instance uses it
#              yet). Default Any = no filter, matching every card written before this parameter existed.
#              A card that means "specifically as a consequence of a PA resolving," not any board
#              change regardless of source, must state cause=public_act explicitly — a card's beat=
#              field is not a substitute for this filter.
#   faction/district/ring: same semantics as the itemized forms above.
#
# Excluded (static — never change): district tiles, board geography, ARBITER Dominance Marker
# Excluded (procedural — not player-driven): Initiative Strip, Session Timeline, Quarter/Month markers

MutationExpr:        confirmed helper symbols only (full grammar not yet enumerated — schema_cleanup_log
                      #20/#22); documents individually-reconciled forms as they're confirmed by use.

#   holder                        — bare symbol: the faction currently holding/reacting with this card
#                                   (Deck-acquired, faction=All context). Bare-argument form, e.g.
#                                   NativeResource(holder). Mirrors the existing bare-keyword pattern
#                                   (trigger.faction, acting, opponent).
#   faction(holder)               — wrapped form of the same symbol, used when a Faction-object receiver
#                                   is needed for a method call (e.g. faction(holder).standing.add(n),
#                                   faction(holder).resources.add(...)). Mirrors Overture's established
#                                   faction(acting) (STD.MOD.1).
#   NativeResource(faction)       — parameterized form of the bare NativeResource subject symbol (§6.1);
#                                   resolves to the resource type native to the given faction argument at
#                                   runtime. faction may be trigger.faction (the faction whose action fired
#                                   the trigger) or holder (the reacting faction itself). Needed for
#                                   faction=All Deck content with no single fixed faction context (contrast
#                                   faction-specific precedent, e.g. GUI.MOD.2/3/4's hardcoded Capacity).
#   arbiter.modify(target, field, delta)
#                                 — signed delta on an already-submitted card's named field (e.g.
#                                   threshold). Not new ARBITER behavior — feeds the existing threshold-
#                                   modifier-accumulation pipeline already used by BM-xx tokens and M-11
#                                   Type B Countermeasure (Art 03 §9.4.1.1/§9.4.3.1.3).
#   arbiter.remove(presence_chip, ...)
#                                 — confirmed (schema_cleanup_log #6, PM05 04-n195 item 2): can never
#                                   target a Deployment Marker. Presence Token (DB:1) and Deployment
#                                   Marker (DB:2) are separate physical components, not a marker-plus-
#                                   linked-chip pair — a Deployment Marker "counts as 1 Presence Token
#                                   for all purposes" (Art 02 §6) only for counting/influence-level
#                                   purposes, not as a valid removal target. If a faction's only presence
#                                   in scope is a Deployment Marker (no separate literal chip), this call
#                                   simply has nothing valid to remove there. GR 8.3a (displaced markers
#                                   are repositioned, never removed) is not in tension with this call.
#
# Confirmed via: STD.MOD.98–133 (Ring 1/2/3 ModReactCard stub passes, S135–S138). Reconciles 04-n171.

CostExpr:            ResourceType * n
                     | ResourceType * n [+ ResourceType * n ...]
                     | faction.X.native * n
                     | district.Y.native * n
                     | IntelToken(about: FactionExpr | None, status: TokenStatus | list[TokenStatus] | None) * n
                     | IntelToken(about: FactionExpr | None, status: TokenStatus | list[TokenStatus] | None).all_held
#
# Cost is paid from the acting (submitting) faction's own resource pool.
#
# ResourceType: capital | mandate | exposure | findings | capacity — names one specific resource type
#   outright, used bare whenever the cost is the same resource type no matter who plays the card or what
#   it targets (e.g. Capital * 3 + Findings * 1 + Mandate * 1 — three fixed types in one cost).
#
# faction.X.native / district.Y.native — resolves at play time to whichever resource type X (a faction)
#   or Y (a district) itself generates. faction.X.native depends on which faction X is (each faction has
#   its own native resource, Art 02); district.Y.native depends on which district Y is (each of the 21
#   districts has its own Resource Type — Mandate, Capital, Findings, Capacity, or Exposure, Art 01 §6.4 —
#   the same resource it generates for its occupying faction every Upkeep). native isn't a resource
#   category of its own; it's "whatever this particular X/Y generates," not a sixth type alongside the
#   five ResourceType names. A single X (or Y) always resolves to one type, but a cost can combine several
#   different native terms to build a cross-resource cost whose specific types track the scenario rather
#   than staying fixed — e.g. faction.acting.native * 1 + faction.target.native * 1 +
#   district.target.native * 1 prices out to different concrete resources depending on which faction is
#   acting, which is targeted, and which district is targeted, without the card needing to name any of
#   them outright.
#
# X: acting | target | target1 | target2 | target_faction | a named Faction
# Y: target | target_district | target1 | target2 | each_target
#
# target/target_district/target_faction/target1/target2/each_target all resolve through the physical
# Target Profile component (Art 02 §8, DB:48) — the sole mechanism by which a CA/PA declares/enumerates
# its target(s). Bare `target` is safe shorthand only when a card populates exactly one target field
# (target_district XOR target_faction XOR target_object); once a card populates more than one, expression
# bodies must use the qualified field name (target_district, target_faction, ...) to disambiguate — the
# wrapper (district(...) vs faction(...)) narrows by type, but not by which field, once two coexist.
# target1/target2/each_target (a card targeting more than one district or faction of the same type) are
# recorded on the Target Profile's free-form declared-parameters line — there's no second printed field
# per type. This entire mechanism is CA/PA-only. ModReactCards never reference target/target_district/
# target_faction — they fire off board events, not a declared target, so any targeting context they need
# comes from the firing TriggerExpr's own faction=/district=/ring= parameters instead.
#
# faction.acting.native simplifies to the bare ResourceType on a FactionSpecific card — Card().faction is
# fixed, so the resolved type is already known and doesn't need a relative lookup (e.g. a Network card
# writes Exposure, not faction.acting.native). A Standard card (faction = All) can use either form,
# depending on design intent: the bare ResourceType if the cost should be one specific resource no matter
# who plays it, or faction.acting.native if the cost should track whichever resource is native to whoever
# plays it. faction.target.native / district.Y.native stay relative on any card, any subtype — the
# resolved type genuinely depends on runtime targeting, which nothing on the card fixes in advance.
#
# Terms combine additively (+); * n sets the per-term unit count.
#
# IntelToken(...) — a discrete, individually-tracked object, not a fungible resource pool, but valid
# `cost`/`boost` content.
#   about:    which faction the spent token(s) concern/track (the token's subject, not its holder); None =
#             any faction. A faction can only ever spend tokens it currently holds — holder is always
#             implicit (the faction paying the cost), never a separate parameter.
#   status:   TokenStatus filter — single value or list; None = any status.
#   * n:      spend exactly n matching tokens.
#   .all_held: spend every currently-held token matching the filter (variable count, not a fixed n).
# TokenStatus: Fresh | Stale | Expired

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

ModBattleExpr:       direction: Boost | Hinder
                     target:    Faction   # a contesting faction identified at Art 03 §10.1.1; chosen by the playing faction, need not be themselves
                     magnitude: int
# Boost:  +magnitude applied to target faction's Battlefield Strength total
# Hinder: −magnitude applied to target faction's Battlefield Strength total
# Playing faction need not be the target, and need not itself be a contesting faction — Art 03 §10.1.2 Step 2
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

Card specifications (all Card IDs, full schema instances) are physically split into Parts 2–4e — see File Map in §2 above. This section is a pointer only; do not add card content here.

[Part 2 — Standard](04___Card_System___Part2_Standard.md) · [Part 3 — Ring Modifiers](04___Card_System___Part3_Ring_Modifiers.md) · [Part 4a — Guild](04___Card_System___Part4a_Guild.md) · [Part 4b — Ghost](04___Card_System___Part4b_Ghost.md) · [Part 4c — Directorate](04___Card_System___Part4c_Directorate.md) · [Part 4d — Network](04___Card_System___Part4d_Network.md) · [Part 4e — Syndicate](04___Card_System___Part4e_Syndicate.md)

---
## 8. Card Taxonomy Index

*Column definitions and Layer × Function validity matrix in Art 04b §5.1. Status key: ✅ Signed off — canonical, use for gap analysis. 📝 Draft — designed but not signed off. ⬜ Not yet designed. 🚫 Retired.*

| Card ID | Name | Status | Layer | Visibility | Function | Subject | Primitive Verb(s) |
|---------|------|--------|-------|------|----------|---------|-------------------|
| DIR.CA.1 | Invoke Jurisdiction | 📝 | Submission | Split | Block | Covert Operation (STD.CA.1, STD.CA.3) | — |
| DIR.CA.2 | Detain | 📝 | Territory | Public | Move | Deployment Marker | Move | *(Success operation is game.move() to Detention zone — Detention zone is an active play area on Directorate's tableau, not a return to supply, so the function is Move, not Remove. Art 04 spec function field correction tracked under 04-n105.)* |
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
| DIR.MOD.9 | Fiscal Sanction | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.10 | Riot Control Unit | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.11 | Emergency Curfew | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.12 | Requisitioned Equipment | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.13 | Martial Lockdown | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.14 | Standing Order | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.15 | Regulatory Clearance | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.16 | Show of Force | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.17 | By the Book | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.18 | Overwhelming Response | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.19 | Model Citizen | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.20 | Public Reprimand | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.21 | Jurisdiction Waiver | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.22 | Requisitioned Resources | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.23 | Commendation | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.24 | Internal Affairs Referral | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| DIR.MOD.25 | Executive Mandate | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
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
| GHO.MOD.12 | Embedded Contact | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.13 | Signals Package | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.14 | Planted Doubt | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.15 | Blown Cover | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.16 | Pre-Analysis | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.17 | Known Variable | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.18 | Clean Channel | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.19 | Total Picture | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.20 | Clean Data | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.21 | Layered Analysis | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.22 | Quiet Correction | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.23 | Findings Published | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.24 | Discreet Leak | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.25 | Model Failure Exposed | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.26 | Existing Dataset | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GHO.MOD.27 | Shared Infrastructure | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.CA.1 | Fortify Structure | ✅ | Territory | Public | Protect | Structure Block | — |
| GUI.CA.2 | Materials Acquisition | ✅ | Economy | Public | Add | Native Resource | Add | *(Art 04 spec fix pending 04-n103)*
| GUI.CA.3 | Foundation Rights | ✅ | Territory | Public | Add | Presence Token | Add |
| GUI.CA.4 | Construction Crew | ✅ | Submission | Split | Remove Restriction | Covert Operation (presence requirement) | — |
| GUI.CA.5 | Infrastructure Yield | ✅ | Economy | Public | Add | Native Resource | Add |
| GUI.CA.6 | Labor Contract | 📝 | Economy | Public | Add | Native Resource | Add | *(Art 04 spec fix pending 04-n103)*
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
| GUI.MOD.9 | Field Supervisor | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.10 | Contractor's Favor | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.11 | Site Foreman | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.12 | Material Stockpile | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.13 | Permit Delay | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.14 | Structural Condemnation | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.15 | Structural Survey | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.16 | Load-Bearing Confidence | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.17 | Permit Fast-Track | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.18 | Certified to Code | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.19 | Union Crew | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.20 | Overbuilt | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.21 | Community Groundbreaking | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.22 | Ribbon Cutting | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.23 | Inspection Noted | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.24 | Code Violation Cited | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.25 | Material Surplus | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| GUI.MOD.26 | In-House Fabrication | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
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
| NET.MOD.15 | Community Turnout | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.16 | Live Broadcast | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.17 | Street Pressure | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.18 | Public Outcry | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.19 | Groundswell | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.20 | Advance Coverage | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.21 | Clear Signal | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.22 | Full Saturation | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.23 | Cross-Posted | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.24 | Viral Moment | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.25 | Off-Air | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.26 | Exclusive Access | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.27 | Follow-Up Question | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.28 | Retraction Demanded | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.29 | Volunteer Stringers | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| NET.MOD.30 | Existing Airtime | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
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
| STD.MOD.1 | Overture | 📝 | Issued ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.2 | Senior Liaison | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.3 | Signed-Out Instrumentation | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.4 | Clearance Review | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.5 | Access Frozen | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.6 | Citadel Contact | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.7 | Sanctum Ledger Access | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.8 | Checkpoint Delay | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.9 | Perimeter Lockout | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.10 | Line Supervisor | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.11 | Relay Priority | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.12 | Regulatory Hold | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.13 | Supply Line Frozen | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.14 | Power Grid Chief | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.15 | Communications Hub Override | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.16 | Permit Office Freeze | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.17 | Clearinghouse Lockout | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.18 | Familiar Face | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.19 | Scavenged Rig | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.20 | Vendors Close Ranks | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.21 | Baryo Turns Its Back | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.22 | Strip Regular | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.23 | Market Stall Cache | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.24 | Housing Arrangement Called In | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.25 | Transit Hub Shutout | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.26 | Zoning Variance | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.27 | Redacted File | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.28 | Maintenance Window | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.29 | Classified Briefing | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.30 | Institutional Backing | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.31 | Ceremonial Groundbreaking | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.32 | Off the Record | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.33 | Public Citation | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.34 | Word to the Wise | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.35 | Named in the Review | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.36 | Fee Waived | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.37 | Emergency Allocation | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.38 | Recognized on Sight | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.39 | Standing Request | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.40 | Back-Channel Word | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.41 | Full Clearance | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.42 | Shift Change Timing | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.43 | Full Institutional Weight | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.44 | Noted Favorably | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.45 | Formal Recognition | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.46 | Quietly Flagged | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.47 | Denied Access | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.48 | Reassigned on Paper | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.49 | Jumped the Queue | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.50 | Rezoned Corridor | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.51 | Relay Intercept | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.52 | Manifest Correction | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.53 | Grievance Withdrawn | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.54 | Cross-Docked Efficiently | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.55 | Chain Reaction | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.56 | Compliance Certificate | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.57 | Model Facility | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.58 | Delay Logged | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.59 | Safety Citation | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.60 | Priority Routing | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.61 | Bulk Rate | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.62 | Dock Familiarity | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.63 | Grid Rapport | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.64 | Line Access | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.65 | Full Processing Rights | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.66 | Overtime Crew | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.67 | Full Utilization | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.68 | Filed Under Routine | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.69 | Reliability Commendation | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.70 | Overdrawn Account Exposed | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.71 | Public Sanction | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.72 | Consignment Hold Released | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.73 | Standing Utility Contract | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.74 | Squatter's Claim | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.75 | Landlord's Blessing | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.76 | Dock Contacts | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.77 | Neighborhood Backing | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.78 | Community Pool | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.79 | Packed House | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.80 | Street Reputation | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.81 | Neighborhood Vouching | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.82 | Busker's Tip | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.83 | Overheard at the Strip | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.84 | Credit with the Vendor | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.85 | Barter Chain | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.86 | Regular Customer | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.87 | Route Knowledge | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.88 | Neighborhood Standing | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.89 | Local Fixture | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.90 | Festival Grounds | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.91 | Word Spreads Fast | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.92 | Quiet Word to the Crowd | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.93 | Block Party | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.94 | Quiet Word Against Them | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.95 | Turned Away | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.96 | Scrap Value | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.97 | Favor Owed | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| STD.MOD.98 | Notified of Encroachment | 📝 | Territory | Public | Add | Presence Token | — |
| STD.MOD.99 | Structural Objection | 📝 | Territory | Public | Remove | Presence Token | — |
| STD.MOD.100 | Escort Withdrawn | 📝 | Territory | Public | Add | Presence Token | — |
| STD.MOD.101 | Overheard in the Commissary | 📝 | Information | Public | Add | Intel Token | — |
| STD.MOD.102 | Access Log Pulled | 📝 | Information | Public | Add | Public Standing | — |
| STD.MOD.103 | Flagged for Review | 📝 | Submission | Public | Modify | Public Act | — |
| STD.MOD.104 | Budget Reallocated | 📝 | Economy | Public | Add | Native Resource | — |
| STD.MOD.105 | Audit Trail | 📝 | Economy | Public | Add | Native Resource | — |
| STD.MOD.106 | Emergency Reserve | 📝 | Economy | Public | Add | Native Resource | — |
| STD.MOD.107 | On the Docket | 📝 | Standing | Public | Add | Public Standing | — |
| STD.MOD.108 | Precedent Cited | 📝 | Standing | Public | Add | Public Standing | — |
| STD.MOD.109 | Quiet Reprimand | 📝 | Standing | Public | Add | Public Standing | — |
| STD.MOD.110 | Line Rerouted | 📝 | Territory | Public | Add | Presence Token | — |
| STD.MOD.111 | Capacity Exceeded | 📝 | Territory | Public | Remove | Presence Token | — |
| STD.MOD.112 | Salvage Rights | 📝 | Territory | Public | Add | Presence Token | — |
| STD.MOD.113 | Grid Anomaly Logged | 📝 | Information | Public | Add | Intel Token | — |
| STD.MOD.114 | Service Level Breach | 📝 | Information | Public | Add | Public Standing | — |
| STD.MOD.115 | Routine Inspection | 📝 | Submission | Public | Modify | Public Act | — |
| STD.MOD.116 | Toll Collected | 📝 | Economy | Public | Add | Native Resource | — |
| STD.MOD.117 | Overtime Billed | 📝 | Economy | Public | Add | Native Resource | — |
| STD.MOD.118 | Backup Generator | 📝 | Economy | Public | Add | Native Resource | — |
| STD.MOD.119 | Union Statement | 📝 | Standing | Public | Add | Public Standing | — |
| STD.MOD.120 | On Record | 📝 | Standing | Public | Add | Public Standing | — |
| STD.MOD.121 | Formal Notice | 📝 | Standing | Public | Add | Public Standing | — |
| STD.MOD.122 | Crowd Gathers | 📝 | Territory | Public | Add | Presence Token | — |
| STD.MOD.123 | Priced Out | 📝 | Territory | Public | Remove | Presence Token | — |
| STD.MOD.124 | Eviction Notice | 📝 | Territory | Public | Add | Presence Token | — |
| STD.MOD.125 | Word Travels | 📝 | Information | Public | Add | Intel Token | — |
| STD.MOD.126 | Quietly Rewritten | 📝 | Information | Public | Add | Public Standing | — |
| STD.MOD.127 | Someone's Watching | 📝 | Submission | Public | Modify | Public Act | — |
| STD.MOD.128 | Informal Toll | 📝 | Economy | Public | Add | Native Resource | — |
| STD.MOD.129 | Cut of the Action | 📝 | Economy | Public | Add | Native Resource | — |
| STD.MOD.130 | Vendor Credit Called | 📝 | Economy | Public | Add | Native Resource | — |
| STD.MOD.131 | Neighborhood Notices | 📝 | Standing | Public | Add | Public Standing | — |
| STD.MOD.132 | Sides Are Taken | 📝 | Standing | Public | Add | Public Standing | — |
| STD.MOD.133 | The Crowd Remembers | 📝 | Standing | Public | Add | Public Standing | — |
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
| SYN.CA.10 | Accord Transfer | 📝 | Economy | Covert | Corrupt | Accord Agreement | Corrupt | Art 06 §9.10 confirmed (L205); d100 threshold 50; crit = incoming party elects numeric term change |
| SYN.CA.11 | Redline | 📝 | Information | Covert | Corrupt | Accord Agreement | Corrupt | Fills Information\|Corrupt\|AccordAgreement gap; d100 threshold 50; alters numeric fill-in on active Accord form |
| SYN.CA.12 | Boilerplate | 📝 | Economy | Covert | Add | Accord Form | Add |
| SYN.MOD.1 | The Fixer | 📝 | Issued ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.2 | Shell Corporation | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.3 | Offshore Slush Fund | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.4 | Insider Trading | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.5 | Short Squeeze | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.6 | Bounty Contract | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.7 | Renegotiation Fee | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.8 | Vulture Fund | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.9 | Goodwill | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.10 | Lobby | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.11 | Signature on File | 📝 | ModReactCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.12 | Contracted Muscle | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.13 | Armored Transport | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.14 | Called-In Debt | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.15 | Bought Off | 📝 | ModBattleCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.16 | Golden Handshake | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.17 | Insider Terms | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.18 | Cleared Position | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.19 | Total Leverage | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.20 | Compound Interest | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.21 | Controlling Stake | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.22 | Quiet Settlement | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.23 | Philanthropic Gesture | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.24 | Word Gets Around | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.25 | Predatory Terms Exposed | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.26 | Bulk Contract | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.MOD.27 | Line of Credit | 📝 | ModActionCard — taxonomy excluded §11.1 | — | — | — | — |
| SYN.PA.1 | Acquisition Offer | 📝 | Territory | Public | Redirect | Presence Token | Move |
| SYN.PA.2 | Public Dividend | 📝 | Economy | Public | Add | Native Resource (conditional) | Add |
| SYN.PA.3 | Data Acquisition | 📝 | Information | Public | Reveal | Intel Token | Reveal | Fills Information\|Reveal\|IntelTokensHeld gap; ElectPlayer; Permanent React on decline |

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

**Minimum unique pool floor (L240):** Distinct from 04-n136's per-card copy-count question above — this governs the size of the pool a faction drafts *from*, not how many of it a player selects. Every faction's drafting pool (Standard set + faction-specific set, excluding blocked and Ring Modifier cards) must total **≥ 54 unique cards**: Standard set = 26 (fixed — every faction draws from the same STD pool) + faction set ≥ 28. Live count: DB view `v_card_faction_deck_floor`. Directorate is currently 6 cards short of the floor — tracked at PM05 04-n149.

**Procedure:** Art 03-init §3.9.

---

## 11. Rules & Constraints — Modifier Cards

### 11.1 What They Are

Modifier cards are the game's secondary layer of play — cards that don't act alone, but attach to, alter, or react to something else already in motion at the table. Two independent questions define any modifier card: **which of three subclasses governs how it fires** (below), and **which of three sets governs where it came from** (§11.1 second half). The two are orthogonal — a card's firing mechanism doesn't determine its acquisition source, and vice versa.

**Three subclasses govern how a modifier card fires (§6.1):**

- **ModActionCard** — attached to a CA/PA/Operative/Emergency/Apex at the moment it's submitted (Covert Dispatch); rides along and resolves when its host does. Its effect is always parasitic on the host action, so it carries no independent Layer/Function/Subject — the taxonomy belongs to the host, not the modifier. Effect expressed as a `ModActionExpr` tagged union (§6.3).
- **ModBattleCard** — thrown into a live district contest at Battlefield Strength resolution (Art 03 §10.1.2); its only job is to shift a named contesting faction's total up or down before the d10 roll. Like ModActionCard, it has no independent taxonomy — the contest itself is the taxonomy-bearing act, not the modifier thrown into it. Effect is a `ModBattleExpr` (Boost/Hinder + target + magnitude).
- **ModReactCard** — the odd one out: it doesn't attach to anything. It sits in a faction's hand until a publicly observable board-state change matches its `trigger`, then fires on its own — structurally closer to a self-triggering CA/PA than to the other two subclasses. This is why ModReactCard is the one subclass that routinely carries genuine Layer/Function/Subject taxonomy (per-card, not universal — see §6.2): it *is* an action, just one that declares itself instead of being submitted at Phase B.

**Three sets govern where a modifier card comes from — independent of subclass:**

Faction and Ring modifier cards are drawn from a shuffled deck; ARBITER-issued cards are not.

- **Faction modifier cards** — drawn from faction modifier deck in player tableau. Shuffled and placed face-down at session setup. Represent faction-specific individuals, assets, tactical approaches, doctrine, and equipment. *Card back: faction color, no border. Card face: effect, Portrait alignment (if applicable), value rating (1–4).*
- **Ring modifier cards** — drawn from shared ring decks on game board (Baryo, The Mid, Core). Chorus Node has no modifier deck. Represent key ring individuals, assets, equipment, and synergies within the ring. *Card back: ring color. Card face: ring constraint prominently stated ("Usable on [Ring] district targets only") when set, effect, Portrait alignment (if applicable), value rating (1–4).* Rather than a single blanket default, the shipped Ring Modifier content (STD.MOD.2–25, §7) fields two complete 4-card sets per ring — Portable (`ring_constraint=None`) and Ring-Locked (`ring_constraint=`ring) — so both models exist in play simultaneously; per-card narrative judgment (location-anchored vs. portable) determines which set a given concept belongs to, not a schema-wide rule.
- **ARBITER-issued cards** — not drawn from any deck. ARBITER hands the card directly to a faction as a specific, named consequence of another card's resolution (`generating_card`, §6.2) — no shuffle, no card back convention, no Upkeep draw eligibility. Current examples: GD-01 Grant Deed (§12b.2), STD.MOD.1 Overture, SYN.MOD.1 The Fixer — all three happen to be ModReactCard underneath (fire on a trigger, once delivered), but acquisition source doesn't constrain which of the three subclasses a card is; an Issued ModActionCard or ModBattleCard is schema-valid, just unbuilt so far.

Ring constraint, when set, applies to all users regardless of holder.

*Naming note: "Modifier cards" is a working designation — pending decision D-04-07.*

### 11.2 Draw Conditions (Art 03 §7.5.3 Modifier Card Draw)

Factions that have triggered Burst Play skip modifier draws for the remainder of the session.

**Faction modifier draw (§7.5.3.0):**

| Structure blocks owned | Cards drawn |
|------------------------|-------------|
| 0–1 | 0 |
| 2–3 | 1 |
| 4–5 | 2 |
| 6+ | 3 (maximum) |

*Table values sourced from Art 03 §21 Card Economy Reference (temporary home — migrates to Art 04 §12 when deck construction is finalized). Confirm this copy stays in sync if §21 changes.*

**Ring modifier draw (§7.5.3.1):** 1 card from a ring deck if the faction has both:
1. At least 1 structure block in that ring, AND
2. Established or Dominant in at least 1 district in that ring.

One draw per qualifying ring per round.

### 11.3 Hand Accumulation

No hand limit. Modifier decks not reshuffled — one-pass per session.

### 11.4 Submit Rules

No cap. A faction may attach as many modifier cards to as many submitted actions as it holds in hand — limited only by hand size (§11.3), not by an artificial per-action or per-round count.

### 11.5 Trading

Freely tradeable faction-to-faction — any resource, Intel Token, or modifier card — whenever both parties agree; not restricted to a specific window, though play shouldn't stall to negotiate one.

### 11.6 Burst Play

**Trigger:** After Art 03 §7.5.3 draws complete (§7.5.3.2 Burst Play Window), before Dispatch phase opens.

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
| `Boost` | +magnitude applied to the named target faction's Battlefield Strength total |
| `Hinder` | −magnitude applied to the named target faction's Battlefield Strength total |

Target is any contesting faction identified at Art 03 §10.1.1 — chosen by the playing faction, not necessarily themselves. Any faction may play a Battlefield Modifier Card into an active contest, whether or not they are contesting it themselves (Art 03 §10.1.2 Step 2).

**ModReactCard** effects: Full CA/PA effect field set (`success`, `successcrit`, `fail`, `failcrit`) — see §6.1. Applies identically to Issued ModReactCards (GD-01, Overture, The Fixer — §11.1); `acquisition` and `generating_card` govern where the card came from, not what its effect field looks like.

*Legacy effect categories from earlier design (Effect extension, Detection immunity, Reach extension, Outcome addition) are superseded by the §6.1 modifier subclass schema.*


## 12. Rules & Constraints

## 12a. Debrief Action Cards

ARBITER-issued cards placed in a faction's Dispatch Case during operation resolution. Not player-submitted; not drawn from a deck. Carry a single instruction that fires at the start of Art 03 §11 Debrief. Physical form: disposable slip or reusable erasable card — design direction pending Art 11. Component: DB:100 (DebriefActionCard).

Debrief Action Cards are distinguished from all other card types by source and timing: created by ARBITER as a consequence of resolved operation; no faction player submits or draws them.

**Acquisition:** same acquisition source as GD-01/Overture/The Fixer (§11.1, §12b) — ARBITER-delivered as a named consequence of a resolved operation (its generating CA), not drawn from a deck. But DA-xx cards are **not** Modifier cards and not `Card()` instances — they carry no `type` from the CardType enum, no Layer/Function/Subject, and critically, no `trigger`. Considered and rejected: typing them Issued `ModReactCard` — ModReactCard requires a non-None `trigger` (§6.2 field constraint), and "fires at the start of Debrief" isn't a `TriggerExpr` event a card reacts to; it's a **scheduled procedural checkpoint** it executes at unconditionally, the same category as `persistence=Seasonal` clearing at Phase 21 (End of Quarter) — phase-anchored, not board-state-reactive. This also matches Art 04 §6.3's explicit exclusion of Session Timeline/Quarter-Month markers from the TriggerExpr vocabulary (a physical Debrief-position marker wouldn't change this — it would still be exactly the excluded category). DA-xx therefore stays its own lightweight category: fields table + Art 03 §11 procedure, not folded into the modifier subclass hierarchy.

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

### 12a.3 DA-02 — PhantomRecord

*GHO.CA.13 Phantom Accounts, the generating card, is itself an undesigned stub (id/version/beat/resolution/threshold only — no Design Rationale, checklist, or Status). DA-02's fields and procedure below match GHO.CA.13's one-line success text as written; exact mechanics are pending GHO.CA.13's own full design pass, not settled by this entry.*

Produced by Ghost's GHO.CA.13 Phantom Accounts on successful Beat 3 resolution. ARBITER places one completed PhantomRecord in Ghost's Dispatch Case at Beat 3 instantiation.

**Fields (ARBITER completes at generation):**

| Field | Type | Description |
|-------|------|-------------|
| `quarter` | Integer | Quarter in which the card was produced |
| `target_faction` | Faction | Faction whose district-native resource generation is being mirrored |
| `generation_snapshot` | TBD | Target faction's influence-based district-native resource generation at Beat 3 (snapshot) — exact calculation method pending GHO.CA.13 full design pass |

**Debrief procedure (Art 03 §11):** At the start of Debrief, process all DA-02 slips in Ghost's Dispatch Case:

1. Ghost gains district-native resources equal to `generation_snapshot`.
2. Discard the DA-02 slip after use.
3. DA-02 slips remaining in the Dispatch Case at Phase 21 are discarded without effect.

⚠ **Outstanding:** `generation_snapshot`'s exact source (which formula/table defines "influence-based generation") is undefined — GHO.CA.13 needs its own design pass before this is more than a placeholder field.

---

## 12b. Grant Deeds

ARBITER-issued cards placed in a faction's Dispatch Case during covert operation resolution. Not player-submitted; not drawn from a deck. Held in faction hand after Debrief delivery. Fire as an Issued ModReactCard (`acquisition=Issued`) — trigger is a fill-in-the-blank district field written by ARBITER on the physical card at generation time. Fire effect applies to the holding faction regardless of which CA generated the deed. Multiple Grant Deeds may be held simultaneously; one fires per trigger event.

Physical form: blank card with printed trigger text and effect text; two fill-in fields completed by ARBITER at generation. Stored blank in ARBITER tableau; ARBITER completes and routes at Beat 3 or Beat 4 of the generating CA's resolution.

---

### 12b.1 Card Identifier: GD-xx

Grant Deeds use the **GD-xx** identifier prefix, assigned sequentially as subtypes are defined.

---

### 12b.2 GD-01 — Grant Deed

Produced by any CA that delivers a Grant Deed (currently SYN.CA.8 Land Title and GUI.CA.10 Development Order). ARBITER completes and places in the acting faction's Dispatch Case at resolution; moves to holding faction's hand at Debrief.

**Fill-in fields (ARBITER completes at generation):**

| Field | Description |
|-------|-------------|
| `district` | Named district from the generating CA's target declaration |
| `holder` | Acting faction from the generating CA |

**Trigger:** `structure_block.placed(district=deed.district)` — fires when any faction places a structure block in the named district. Trigger is evaluated against the district name written on the card; no ARBITER monitoring required — deed holder self-polices and announces React.

⚠ **Outstanding issue (04-n27 / trigger vocab):** `structure_block.placed(district=X)` is a district-scoped trigger form not yet in the confirmed TriggerExpr vocabulary (current vocabulary is ring-scoped: `structure_block.placed(faction=X, ring=Z)`). District-scoped extension needed in Art 04 §6.3 and design_reference_card_system.md.

**Effect on fire:**
1. Deed holder announces React; presents Grant Deed card; names district.
2. Place 1 Presence Token for deed holder in `deed.district`.
3. Place 1 Structure Block for deed holder in `deed.district` (Governing Rule 8.2 governs — if holder already has a structure block there, step 3 is skipped; step 2 still executes).
4. Remove 1 Structure Block belonging to the triggering faction from `deed.district` — the registered deed takes precedence over the unauthorized build that just fired it.
5. Discard Grant Deed.

**Component registration:** New component — Art 02 entry pending 04-n26.

```python
GD01 = Card(
    id      = "GD-01",  version = "v0.4",
    name    = "Grant Deed",
    tagline = "A registered claim. When someone else breaks ground, the deed fires.",
    type    = ModReactCard,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Add,  subject = StructureBlock,

    beat            = None,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = structure_block.placed(district=deed.district),
    resolution_type = Transactional,
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = deed.district,
    target_faction  = None,
    target_object   = None,
    declared_params = None,

    affinity    = None,
    restriction = None,
    cost        = None,
    boost       = None,

    acquisition      = Issued,
    generating_card  = ["SYN.CA.8", "GUI.CA.10"],

    success = [faction(holding).presence_token.add(deed.district, 1),
               faction(holding).structure_block.add(deed.district, 1),
               faction(trigger.faction).structure_block.remove(deed.district, 1)],
    successcrit = None,  fail = None,  failcrit = None,

    portrait    = None,
    ps_framing  = None,

    narrative    = None,
    perspectives = None,
    design_note  = "ARBITER-issued (acquisition=Issued); not drawn from a deck. Fill-in fields: district (from generating CA target) and holder (acting faction of generating CA). GR 8.2 governs step 3 — structure block placement blocked if holder already holds one in deed.district; step 2 (Presence Token) always executes on fire. Multiple deeds on the same district are permitted; each fires independently. Produced by SYN.CA.8 Land Title and GUI.CA.10 Development Order. Step 3 (removing the triggering faction's structure block) reflects that a registered claim doesn't just let the holder catch up when someone else builds — it displaces that build outright: a Land Title/Development Order registered earlier legally supersedes an unauthorized structure raised later on the same ground. This interacts with SYN.CA.8/GUI.CA.10's own cost calibration (04-n178).",
    arbiter_note = "At generating CA resolution: take 1 blank Grant Deed from ARBITER tableau; write target district name in 'district' field and acting faction in 'holder' field; place in acting faction's Dispatch Case. Card moves to holder's hand at Debrief. No ongoing ARBITER monitoring required — holder self-polices and announces React when trigger fires.",
)
```

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

Face: name, type indicator, effect, attachment rule (if restricted), Portrait (if applicable), value rating (1–4). Back: faction color, faction symbol.

### 13.3 Modifier Cards — Ring

Face: ring constraint statement as visually distinct element, name, type indicator, effect, Portrait (if applicable), value rating (1–4). Back: ring color, ring name.

---

## 14. Special Conditions & Gameplay Impacts

### 14.4 Self-Directed Targeting

`target_faction` on Covert Operations is free-form text on the physical Target Profile component, not a rigid schema enum — any faction, including the acting faction itself, can be named. All cards support this; it is not a per-card exception. An "unattributed" Public Standing shift needs no new schema concept: the existing `PSFraming` "target" value already resolves correctly when the named target is the acting faction itself.

### 14.5 Deck Exhaustion

Covert and political draw decks: when exhausted, shuffle discard pile immediately to form new deck and continue. Modifier decks are not reshuffled.

### 14.6 Resource Acquisition — Non-Native Resources

Non-native resources acquired through:
1. District incursion — presence in districts controlled by the resource's native faction
2. Direct faction-to-faction trade at any agreed rate
3. Where no direct trade is arranged: conversion follows **The Translation** (Art 03 §19.1), a Chorus-Node-presence-tiered rate table (Established 2:1, Present 3:1, None 4:1, Tied/Contested 5:1) — not a flat universal rate.

---

---

*End of Artifact 04 — Card System v0.9.75*
