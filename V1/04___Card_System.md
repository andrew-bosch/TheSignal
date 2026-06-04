# 04 — CARD SYSTEM
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.9.26 Draft  
**Status:** 🔄 Draft — Pending Sign-Off  
**Last Updated:** 2026-06-02  
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

React fires on publicly countable or observable conditions. Hidden conditions are not valid React triggers. This maintains information integrity — you cannot react to information you shouldn't have.

**Principle 6 — Effect duration is permanent or within-Quarter. Multi-Quarter temporaries are prohibited.**

Effects either resolve permanently (persisting for the remainder of the session) or expire at end of the current Quarter. An effect that lasts a stated number of Quarters is not a valid design — it creates tracking overhead with no corresponding design payoff. When both durations could work, prefer permanent.

**Principle 7 — Faction-specific cards are doctrinally exclusive.**

Every faction-specific card must pass two tests: mechanical (only this faction would do this — the effect cannot be justified by another faction's doctrine) and narrative (only this faction would say it this way — the card text sounds like no other faction). If either test fails, the card belongs to no one. Traceable to Artifact 00 §7. *00a R29.*

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

Every card requiring ARBITER action maps to a named general procedure defined in a governing artifact. `arbiter_note` fields reference existing procedures — they do not define new ones. When a card design requires new ARBITER behavior, that behavior must be defined as a generalizable procedure in a governing artifact (Art 03, Art 07, or equivalent) before the card is finalized. *00-R40.*

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

### Design Checklist

Every card entry includes a design checklist table immediately before the Python spec, followed by a Status table. The checklist and status table together gate a card's progression through review and sign-off.

The **Artifact ref** column in each card's checklist should cite the specific section or procedure in the supporting artifact that validates that row for that card — not just the artifact number. Where no specific section exists yet, that absence is itself a gap to flag in Status. The general guidance column below shows where to look; card entries must be more specific.

**Status table format:**

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

- **Design Pass** ✓ — checklist evaluation complete; all 13 rows assessed
- **Issues Resolved** ✓ — all flagged issues addressed; blank if open issues remain
- **Signed off** ✓ — Andy's explicit approval; record session number (e.g., ✓ S49); blank until signed

A card with no issues from the design pass gets ✓ in both Design Pass and Issues Resolved. Signed off stays blank until Andy reviews and approves.

| Category | What it checks | General guidance |
|----------|----------------|-----------------|
| Action fit | Does this card's action type belong in New Meridian? Is the mechanical premise grounded in the world? *(P10, P7 test 1)* | Art 00 §7 |
| Voice fit | Do the faction perspective fields read in the correct register? Could each faction's line have been written by someone who knows that doctrine? *(P7 test 2, P8)* | Art 00 §7, §9 |
| Doctrine alignment | Does the card's effect serve or oppose the doctrine of specific faction(s)? If so, is that doctrinal relevance captured — through portrait entries, affinity, or `doctrine_mod`? Where `target_faction` is set: is `doctrine_mod` applied and justified, or is the decision not to apply it documented? | Art 00 §7; Art 04 §6.5 |
| Card type fit | Is the Card Type/Subtype classification correct (Standard vs. faction-specific; Covert vs. Political)? For faction-specific cards: does it fill a gap or provide meaningful differentiation from existing standard cards? *(P1, P2)* | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | Does the Layer/Function/Subject assignment correctly represent the action per the Art 04b taxonomy? *(P3, P4)* | Art 04b §4 |
| Balance | Is cost equitable to success effect? Is difficulty calibrated to restriction and ring context? Best-effort until Art 00c economics is built — note any assumptions made. *(P9, P15)* | Art 02a §6–§7; Art 04 §6.5 |
| Effect duration | Are all effects permanent or within-Quarter? No multi-Quarter temporaries. N/A for immediate-resolution cards. *(P6)* | Art 03 §1 |
| Persistence | Is the `persistence` value set correctly in the card spec? Does this card leave a game-state marker on the table requiring Transient or Seasonal? Default = Immediate for cards fully resolved at beat. | Art 04 §6 |
| Trigger validity | If `trigger` is set: is the trigger condition publicly observable? N/A when no trigger. *(P5)* | Art 02a; Art 03 |
| Portrait validity | Does portrait timing fire on action taken, not outcome? Are Effect fields free of direct Portrait track shifts? For Standard cards: is each faction's portrait entry (or justified absence) documented? Is entry magnitude doctrinally grounded? Do all portrait entries fire only for the submitting faction — no entry affects a faction that did not act? *(P11, P12, P13, P16)* | Art 04 §6.2 |
| Supported by zones | Does `target_district` reference a valid zone? Is ring context consistent? | Art 01 §6–§7 |
| Supported by components | Do all referenced components and cost resources exist? | Art 02a §6–§8 |
| Supported by game procedure | Are all ARBITER and player actions implied by this card covered by Art 03 procedure? Flag any implied action not yet procedurally defined as a gap. | Art 03 |

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
| Guild | Structures on board | Core / Mid priority | 0–1 | Build deep; compound via C15 |
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
- **Win path:** build intelligence pipeline early; pre-fund multiple Quarters via Deep Cover (burst card); arrive at Q8 with a hand assembled from other factions' capabilities
- **Deck feel:** precise, patient, deliberately small

**Guild**

Guild believes the Chorus is an evaluation: humanity's response will be judged not by intent, but by what it builds. Improvisation reveals weakness. Shortcuts reveal urgency. What Guild places on the board is not a tactical position — it is an argument about what humanity is capable of at its best, made permanent in physical form. Guild is also the only faction at The Table that cannot operate covertly in principle: planetary-scale infrastructure cannot be classified. Operations are submitted through the shared dispatch procedure (sealed, timed), but the results are never hidden — everything lands immediately on the board as a presence token or structure. The procedure is shared; the doctrine is not. The deck does not feel covert. It feels like construction.

- **Economy:** Capacity, compounded via C15 Infrastructure Yield — zero-cost Automatic; draws Capacity from each Established or Dominant district each Quarter
- **Passive income:** +1 Capacity when any opponent completes C01 in a district where Guild has presence (Guild employees did the work)
- **C12 Materials Acquisition:** converts correctly anticipated demolition into paid recovery
- **Win condition:** structures on board, not just presence tokens — Guild is building the response, not positioning for it
- **Win path:** Foundation Rights (C13, near-automatic in Ring 0) → high tier in Core and Mid → C15 compounds → Fortify Structure (C11) defends → C12 collects salvage from the table's demolition activity
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

*§6 schema informed by a card game data structure gap analysis conducted sessions 23–24. Research notes (non-artifact): `Projects/Whiteboard/researchNotes_CardDesign.md`.*

---

### 6.1 Card Class Definition

Each card is an instance of `Card`. Fields are grouped by class. Narrative fields are prose; all other fields are typed expressions or static values.

```python
class Card:
    # ── Identity ──────────────────────────────────── static
    id:           str
    version:      Semver
    name:         str
    tagline:      str
    type:         CardType
    subtype:      Subtype
    faction:      Faction

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
    target_district: DistrictExpr
    target_faction:  FactionExpr | None
    target_object:   ObjectExpr  | None

    # ── Logic ─────────────────────────────────────── predicates + expressions
    affinity:     ConditionalExpr | None    # evaluated before cost
    restriction:  BoolExpr       | None    # card unplayable if False
    cost:         CostExpr

    # ── Effects ───────────────────────────────────── mutations  [VS-06]
    success:      MutationExpr | None
    successcrit:  MutationExpr | None       # additive delta — fires with success
    fail:         MutationExpr | None
    failcrit:     MutationExpr | None       # additive delta — fires with fail

    # ── Portrait ──────────────────────────────────── dimension table  [VS-06]
    portrait:     dict[Faction, PortraitEntry]

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
```

---

### 6.2 Data Dictionary

| Field | Class | Type | Purpose | Displayed |
|-------|-------|------|---------|-----------|
| id | Identity | str | Primary key — format: [type prefix][sequence number] | TBD |
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
| persistence | Metadata | Persistence | How long the card remains on the table as a game state marker — Immediate: removed at Beat 4 cleanup; Transient: removed at Beat 5 of current Month; Seasonal: removed at Phase 21 (End of Quarter); Permanent: removed only by explicit game action. Default for covert operations: Immediate. PA cards with active board-condition effects must use Transient or Seasonal. | Face |
| persistence_condition | Metadata | BoolExpr | Condition that must remain True for a Permanent card to stay in play; card is discarded immediately when it evaluates False. None for all non-Permanent cards. | Face |
| persistence_effect | Metadata | MutationExpr | Ongoing board condition active while a Permanent card is in play; evaluated continuously until persistence_condition is met. Use `game.board_condition(...)` to express scoped persistent effects. None for all non-Permanent cards. | Face |
| target_district | Targeting | DistrictExpr | District scope for the card's effect | Face |
| target_faction | Targeting | FactionExpr | Faction this card targets; None = no faction target | Face |
| target_object | Targeting | ObjectExpr | Game component this card acts on; None = no object target | Face |
| affinity | Logic | ConditionalExpr | Faction-based cost modifier — evaluated before cost expression | Face |
| restriction | Logic | BoolExpr | Submission preconditions — card unplayable if evaluates False | Face |
| cost | Logic | CostExpr | Physical, fungible resources consumed at submission — valid cost resources are those that can be traded or transferred (Mandate, Capital, Influence, district native resource). Non-fungible markers (Public Standing, presence tiers) are not valid cost values; marker changes that function as a cost belong in `success`/`fail` effect fields. | Face |
| success | Effects | MutationExpr | Primary effect on resolution success | Face |
| successcrit | Effects | MutationExpr | Additive delta on critical success (roll < 5); None when Automatic | Face |
| fail | Effects | MutationExpr | Effect on failure; None = cost spent, no additional effect | Face |
| failcrit | Effects | MutationExpr | Additive delta on critical failure (roll ≥ 95); None when Automatic | Face |
| portrait | Portrait | dict[Faction, PortraitEntry] | Per-faction portrait scoring — evaluated by ARBITER; analyzed in DB | TBD |
| narrative | Narrative | str | In-world narrative grounding — one sentence; neutral observer (standard) or owning faction voice (faction-specific) | TBD |
| perspectives | Narrative | dict[Faction, str] | Per-faction in-world perspective — one sentence per faction | TBD |
| design_note | Narrative | str | Design intent — doctrine rationale, Art 11 layout context | No |
| arbiter_note | Narrative | str | ARBITER resolution guidance — timing, edge cases, table validation | No |

---

### 6.3 Enum Vocabularies

```
CardType:     CovertOperation | PoliticalAct | Pass | Countermeasure | Modifier | EmergencyResponse
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
| [C01](#c01-build-structure) | Build Structure |
| [C02](#c02-demolish) | Demolish |
| [C03](#c03-campaign) | Campaign |
| [C04](#c04-undermine) | Undermine |
| [C05](#c05-gather) | Gather |
| [C06](#c06-broadcast-interference) | Broadcast Interference |
| [C07](#c07-amplify) | Amplify |
| [C08](#c08-buy-influence) | Buy Influence |
| [C09](#c09-fund) | Fund |
| [C10](#c10-protect) | Protect |
| [C39](#c39-absolute-compromise) | Absolute Compromise |
| [—](#standard-disinformation-campaign) | Disinformation Campaign |
| [—](#standard-disprove) | Disprove |
| [—](#standard-intel-extraction) | Intel Extraction |
| [—](#standard-modifier-raid) | Modifier Raid |

### C01 — BUILD STRUCTURE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Territory-control foundation card. Construction is publicly visible — the covert element is intent, not the act. Every faction must establish structured positions to hold territory; this is the universal mechanism. Cost vs reward: dual cost (1 faction native + 1 district native) models that building requires both faction resources and local knowledge; Automatic resolution is appropriate if prerequisites are met. Guild affinity waives the district-native cost: the Guild *is* the city's builder and does not purchase access to their own infrastructure ecosystem.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Physical construction as territorial assertion is core to New Meridian. The covert element is unannounced intent — the visible act is public. All five factions acknowledge building as a valid form of presence. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | All five perspectives are doctrinally distinct. Guild's "permanence is possible here" is the foundational argument; Syndicate's "the question is who captures it" reframes construction as economic extraction; Ghost's "commitments are data points" is cold and analytical. No faction sounds like another. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | Building directly serves Guild doctrine (permanence, structural investment). Captured via portrait submitter=+1 and cost affinity. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: every faction must establish structure; no faction-specific exclusivity warranted. CovertOperation: unannounced intent is the covert element, not the visible act. Fills the universal territorial foundation role — no standard card duplicates it. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Add / StructureBlock — unambiguous. Layer is Territory because the target is a StructureBlock, not because of the Add verb. | Art 04b §4 |
| Balance | ✓ | Automatic resolution gated by dual cost + presence prerequisite + no-existing-structure restriction. Not independently playable without prior presence. Guild affinity waives district native only — cost-scoped, not difficulty. | Art 02a §6–§7 |
| Effect duration | ✓ | No duration — structure placement is permanent; persists until removed. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`: permanence doctrine — core alignment (P11, P16). Ghost `submitter=−1`: structure is a permanent visible commitment; Ghost doctrine is concealment, not construction (P11, P16). Directorate: no entry — builds pragmatically ("if it serves the mandate"); instrumental, not doctrinal. Network: no entry — presence-building via community relationships (C03), not structures; observational stance confirms absence. Syndicate: no entry — doctrine is acquisition and capital flow; "who captures it" is observer framing, not builder framing. No direct Portrait track shift in effect fields (P12). All entries submitter-bounded (P16). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any` — valid. Ring entry implicit via presence requirement in restriction. | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock (§7); presence token / deployment marker in restriction (§6); faction native + district native cost (§8). | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Submitted in Dispatch (§9); Beat 3 Resolution Grid (§11); Automatic resolution (§20). ARBITER places Structure Block at Beat 3 outcome. Guild affinity evaluated at dispatch. | Art 03 §9, §11, §20 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
C01 = Card(
    id      = 1,  version = "v1.1",
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

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

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

### C02 — DEMOLISH
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Territory disruption card — the destructive mirror of C01. Structure removal is publicly visible; source of removal is not announced. Cost vs reward: dual cost (1 faction native + 1 district native) reflects that demolition requires both capability and local knowledge; probabilistic resolution models genuine resistance — you do not control what you are destroying. Crit success yields salvage (1 native recovered); crit fail costs Public Standing, representing the reputational risk of publicly-failed covert demolition.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Demolition as covert territorial disruption is grounded — the act is visible, the source is not. The asymmetry with C01 (probabilistic vs. Automatic) correctly reflects operating against someone else's infrastructure rather than your own. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Guild's "something has gone badly wrong" and Network's "infrastructure of control needs to come down" are the sharpest contrast in the set. Ghost's absence-as-data read is clean. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` is set; `doctrine_mod = None` is an explicit design choice — demolition difficulty reflects physical opportunity (ring, restriction), not doctrinal relationship. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions engage in demolition as territorial disruption. CovertOperation: source undisclosed. Distinct from C01 — Remove vs. Add, probabilistic vs. Automatic. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Remove / StructureBlock. Layer is Territory because the target is a StructureBlock. | Art 04b §4 |
| Balance | ✓ | Same dual cost as C01, probabilistic at threshold 50. Ring_mod {0:−15, 1:−10, 2:0, 3:+10} — harder near Chorus Node. Crit success salvage rewards execution; crit fail PS loss is a meaningful downside. | Art 02a §6–§7 |
| Effect duration | ✓ | No duration — structure removal is permanent; persists until rebuilt. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: demolition against permanence doctrine — "we do not unmake" (P11, P16). Network `submitter=+1`: counter-entrenchment doctrine — removing infrastructure of control is on-doctrine (P11, P16). Directorate `submitter=−1`: structures represent institutional investment; doctrinal reluctance parallels C04 (P11, P16). Ghost: no entry — analytical observer, not demolition-as-doctrine; absence justified. Syndicate: no entry — pragmatic asset-management framing, no doctrinal signal; absence justified. `failcrit standing -= 1` is Public Standing (Art 02b), not Portrait — P12 clear. | Art 04 §6.2; Art 02b §7 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction uses self-or-adjacent presence — adjacency model required; district_adjacency confirmed (DB-09 ✅ S50). | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock target (§7); presence in restriction (§6); dual cost (§8); failcrit `standing -= 1` (Art 02b §7). | Art 02a §6–§8; Art 02b §7 |
| Supported by game procedure | ✓ | Dispatch (§9); Beat 3 Resolution Grid (§11); d100 threshold 50 with ring_mod. ARBITER removes Structure Block on success; standing loss on crit fail — Beat 3 outcome steps. | Art 03 §9, §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
C02 = Card(
    id      = 2,  version = "v1.1",
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

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = StructureBlock,

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

### C03 — CAMPAIGN
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Presence-deepening card — a deliberate structural parallel to C01. To Campaign, you must already be present; this is not an entry card. Cost vs reward: dual cost mirrors C01 (same principle, same gate). Automatic resolution because you're operating within your own established footprint, not against opposition. Network affinity waives the district-native cost because Network growth is relational, not material — it does not purchase access to local infrastructure.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Presence-deepening in a district you already occupy is grounded. Campaign is relational/operational deepening of an existing footprint — distinct from entry. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Ghost's "presence creates exposure" explains why Ghost doesn't over-extend; Network's "relationships are how things actually change" directly justifies the affinity. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | Presence-deepening through community relationships directly serves Network doctrine (relational growth). Captured via portrait submitter=+1 and cost affinity. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions build presence. CovertOperation: presence-building is done quietly. Structurally mirrors C01 (presence vs. structure) — distinct role, not duplicative. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken. Layer is Territory because the target is a PresenceToken. | Art 04b §4 |
| Balance | ✓ | Automatic gated by presence prerequisite — same structure as C01. Network affinity waives district native (relational, not material). Intentional cost symmetry with C01. | Art 02a §6–§7 |
| Effect duration | ✓ | No duration — presence placement is permanent until removed. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Network `submitter=+1`: relational growth is doctrinally core (P11, P16). Guild: no entry — C01/structural investment is Guild's primary presence signal; Campaign is available but not doctrinally distinct; absence justified. Directorate: no entry — presence-building is instrumental ("where the mandate requires it"), not doctrinal; absence justified. Ghost: no entry — "presence creates exposure" frames expansion as calculated exception, not doctrinal endorsement; absence justified. Syndicate: no entry — community presence-building is not Syndicate's mode; capital and acquisition is; absence justified. No direct Portrait track shift in effect fields (P12). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Ring entry implicit via presence restriction. | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (§6); faction native + district native cost (§8). | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Dispatch (§9); Beat 3 Resolution Grid (§11); Automatic resolution (§20). ARBITER places PresenceToken on success. Network affinity evaluated at dispatch. | Art 03 §9, §11, §20 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
C03 = Card(
    id      = 3,  version = "v1.1",
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

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

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

### C04 — UNDERMINE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Presence-disruption card — the destructive mirror of C03, following the same build/demolish asymmetry as C01/C02. Probabilistic because you're operating against someone else's established footing. Cost vs reward: same dual cost as C03; crit success doubles effect (−2 presence), crit fail costs PS. Portrait is selective: Guild and Directorate are negatively disposed to undercutting presence (institutional stability preference); Network is affirmative (disruption aligns with its counter-entrenchment doctrine). Ghost and Syndicate are absent — neither is doctrinally committed to presence disruption as a default.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert erosion of opponent presence is grounded — source undisclosed, structural parallel to C02. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Directorate's conditional ("unless the target is The Network — then it is public safety") maps directly to the `where=faction(target) != Network` portrait exception. Ghost's "we prefer signal" explains their absence from affinity. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` set; `doctrine_mod = None` — explicit design choice. Doctrinal relationship does not affect disruption difficulty; ring_mod handles variation. Same rationale as C02. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions engage in presence disruption. CovertOperation: source undisclosed. Distinct from C02 (presence vs. structure). | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory / Remove / PresenceToken. Layer is Territory because the target is a PresenceToken. | Art 04b §4 |
| Balance | ✓ | Same dual cost as C03. Crit success = −2 total (success + successcrit additive) — intentionally stronger than C02 salvage; presence erosion compounds. Crit fail PS loss mirrors C02. | Art 02a §6–§7 |
| Effect duration | ✓ | No duration — presence removal is permanent until replenished. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: undermining presence is doctrinally incongruent — "we do not erase what others have built" (P11, P16). Directorate `submitter=−1, where=faction(target) != Network`: covert erosion conflicts with governance doctrine; exception when targeting Network — framed as "public safety," no doctrinal conflict; `where=` constrains by target identity, not outcome (P11, P16). Network `submitter=+1`: counter-entrenchment doctrine — eroding entrenched presence is on-doctrine (P11, P16). Ghost: no entry — "disruption without intelligence purpose is noise"; presence disruption is not Ghost's primary mode; absence justified. Syndicate: no entry — pragmatic observer framing, no doctrinal stake in presence disruption; absence justified. `failcrit standing -= 1` is Public Standing (Art 02b), not Portrait — P12 clear. | Art 04 §6.2; Art 02b §7 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction requires self-or-adjacent presence AND target has presence > 0. Adjacency model required. | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken in restriction and as target (§6); dual cost (§8); failcrit `standing -= 1` (Art 02b §7). | Art 02a §6, §8; Art 02b §7 |
| Supported by game procedure | ✓ | Dispatch (§9); Beat 3 Resolution Grid (§11); d100 threshold 50 with ring_mod. ARBITER removes PresenceToken on success; double on crit success; standing loss on crit fail — Beat 3 outcome steps. | Art 03 §9, §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
C04 = Card(
    id      = 4,  version = "v1.1",
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

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = PresenceToken,

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

### C05 — GATHER
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Universal intelligence card — the baseline for the Information layer. Observation does not consume local infrastructure, hence faction-native-only cost. Ghost adjacency exemption is doctrinal: remote analysis does not require physical proximity. Crit success is additive (both `success` and `successcrit` dispatch the same token type — 2 Intel Tokens total on crit). Crit fail reveals the attempt to the target, creating genuine operational risk for careless intelligence-gathering.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence-gathering as a covert baseline is grounded. Ghost's adjacency exemption (remote analysis, L69) is doctrinally accurate. | Art 00 §7 — faction doctrines |
| Voice fit | ✓ | Ghost's "this is what we are here for" makes the affinity mechanically legible. Network's "gaps between what is said and what is true" is the sharpest perspective. All five doctrinally distinct. | Art 00 §7 — faction profiles |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` set; `doctrine_mod = None` — explicit choice. Intelligence-gathering effectiveness doesn't vary by doctrinal relationship. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Standard: all factions gather intelligence. CovertOperation: observation is covert. Ghost adjacency exemption is a doctrinal exception to the restriction, not a subtype change. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Information` — intelligence-gathering generates IntelToken; dominant design intent is information acquisition, consistent with Art 04b §4.4. `doctrine_mod = None` — correct, doctrinal proximity does not affect intel-gathering effectiveness. | Art 04b §4 |
| Balance | ✓ | Single faction-native cost — cheapest intel card. Ghost effective threshold 75 (50+25 affinity). Crit success = 2 tokens total (additive). Crit fail NotificationSlip creates real operational risk. | Art 02a §8; Art 02b §8 |
| Effect duration | ✓ | No duration — Intel Token is a durable resource that persists until spent. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Ghost `submitter=+1`: intelligence-gathering is core doctrine — "this is what we are here for" (P11, P16). Network: no entry — intel is a tool for Network, not their primary mode; relational growth and communication are doctrinal (absence justified). Guild: no entry — pragmatic use only; "we gather when we need to build smarter" (absence justified). Directorate: no entry — prefers formal collection; covert gathering is a tool, not a belief (absence justified). Syndicate: no entry — transactional framing, no doctrinal signal (absence justified). `failcrit` dispatches NotificationSlip — game effect, not Portrait shift (P12 clear). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: presence in self-or-adjacent OR Ghost exemption. | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Art 02b §8); faction native cost (Art 02a §8); failcrit NotificationSlip (Art 02a — subtype definition pending 02a-11). | Art 02a §8; Art 02b §8 |
| Supported by game procedure | ✓ | Dispatch (§9); Beat 3 Resolution Grid (§11); d100 threshold 50 with Ghost affinity. ARBITER delivers IntelToken on success, NotificationSlip to target on crit fail — Art 03 Beat 3 outcome steps (per L170; Art 07 ref is stale). | Art 03 §9, §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
C05 = Card(
    id      = 5,  version = "v1.1",
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

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

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

### C06 — BROADCAST INTERFERENCE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Submission-layer Beat 2 card — places a cost modifier on Public Acts targeting a district this round. Broadcast interference is ambient, hence no presence requirement. Cost is Exposure-denominated: non-Network factions must acquire Exposure through incursion or trade, making this card natively affordable only to the Network. Network affinity reduces cost by 1 (net: 1 Exposure), making it a low-friction tactical tool for Network while remaining expensive for others.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Broadcast disruption as covert intelligence operation: ambient signal interference requires no physical presence in the district. No faction presence requirement is correct — you don't need to be there to jam a signal. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Tagline clear and grounded. Five perspectives doctrinally distinct: Guild (operational delays), Directorate (jurisdictional note), Network (strategic noise), Ghost (analytical cover), Syndicate (market inefficiency). | Art 00 §7 |
| Doctrine alignment | ✓ | Network is the primary aligned faction — signal disruption as tactical information control. Ghost benefits doctrinally (analytical cover). Directorate opposed — covert disruption conflicts with their institutional-authority doctrine. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: disruption mechanism is hidden even if cost increase is observable at Beat 4. Standard: all factions can disrupt broadcast infrastructure. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Submission` — modifies cost of a PA (submission-phase property). `function = Modify`, `subject = PoliticalAct` — correctly scoped and narrow. | Art 04b §4, §5 |
| Balance | ✓ | Beat 2 positional wager. Cost 2 Exposure (1 for Network via affinity). Raises PA cost +1 native — meaningful deterrence, not a hard block. No fail state. | Art 03 §11 |
| Effect duration | ✓ | Single-round: arms at Beat 2, applies at Beat 4, does not persist. Appropriate for a tactical cost modifier. | Art 03 §17 |
| Persistence | ✓ | Immediate — Beat 2 carry; applied at Beat 4 via Resolution Grid; no game-state marker persists beyond round | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Network `submitter=+1`: tactical information control — primary aligned faction (P11, P16). Ghost `submitter=+1`: interference creates analytical cover, consistent with Ghost's low-profile doctrine (P11, P16). Directorate `submitter=−1`: covert disruption undermines institutional legitimacy; Directorate's tool is regulatory authority, not anonymous interference (P11, P16). Guild: no entry — operational delays are a cost, not a doctrinal signal; absence justified. Syndicate: no entry — market inefficiency is an opportunity, not a doctrinal stake; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. No presence restriction — broadcast effect is ambient to the district. | Art 01 §6 |
| Supported by components | ✓ | PoliticalAct as target type; Exposure resource as cost. Both defined. | Art 02a §8; Art 04b §5 |
| Supported by game procedure | ✓ | Submitted at Dispatch (§9); placed in Beat 2 row at Resolution Grid setup (§11 Beat 0); moved to Beat 4 carry row during Beat 2 processing (§11 Beat 2); arming and effect applied at Beat 4 (§17). | Art 03 §9, §11, §17 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
C06 = Card(
    id      = 6,  version = "v1.1",
    name    = "Broadcast Interference",
    tagline = "Disrupt public communications in a district, dampening public activity.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Submission,  function = Modify,  subject = PoliticalAct,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Positional wager",
    outcome_type    = None,
    persistence     = Immediate,

    target_district = district.any,
    target_faction  = None,
    target_object   = PoliticalAct,

    affinity    = faction(acting) == Network: cost.resource.exposure -= 1,
    restriction = None,
    cost        = resource.faction(acting).exposure * 2,

    success     = game.ops(beat=4, type=PoliticalAct, at=district(target)).cost.native += 1,
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

### C07 — AMPLIFY
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Beat 2 modifier for the acting faction's own Public Act — the offensive counterpart to C06. Amplification cuts both ways: a PA that wins +1 PS resolves as +2; a PA that loses −1 PS resolves as −2. Cost is Exposure-denominated (same as C06), slightly favoring the Network. Restriction is None — ARBITER holds awareness through Beat 4; if no Public Act is submitted, Amplify fizzles and Exposure is spent.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covertly amplifying your own political messaging fits the covert operations frame. Ghost's categorical opposition ("volume attracts attention") is the clearest doctrinal test for the card. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Ghost's perspective is the sharpest. All five are doctrinally distinct — opposition, authority-sufficiency, tactical use, suppression logic, leverage framing. | Art 00 §7 |
| Doctrine alignment | ✓ | Amplifying public messaging strongly serves Network doctrine; strongly opposes Ghost (volume = exposure risk). Both captured via portrait entries. Self-targeted → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: amplification mechanism is hidden. Standard: all factions can amplify their messaging covertly. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Resolution` — scales the outcome (standing_impact) of a PA; Art 04b §4.2 "outcome scale" is a Resolution property. `function = Modify`, `subject = PoliticalAct`. Note: `resolution_type = "Transactional"` may be a misnomer — card fizzles if no PA is submitted (same positional-wager behavior as C06). Minor schema inconsistency, not blocking. | Art 04b §4, §5 |
| Balance | ✓ | Symmetric multiplier: both success (+×2) and failure (−×2) scale. Prevents risk-free use. Fizzle (Exposure spent, no PA) ensures Beat 2 commitment is real. | Art 02b §7 |
| Effect duration | ✓ | Single-round: arms at Beat 2, applies at Beat 4, does not persist. | Art 03 §17 |
| Persistence | ✓ | Immediate — Beat 2 carry; applied at Beat 4 via Resolution Grid; no game-state marker persists beyond round | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Network `submitter=+1`: amplifying public messaging is core Network doctrine (P11, P16). Ghost `submitter=−1`: amplification = attention = exposure risk — "volume attracts attention, attention ends operations" (P11, P16). Guild: no entry — "let our structures speak"; amplification is a substitute for physical evidence, not a doctrinal tool; absence justified. Directorate: no entry — institutional authority doesn't require amplification; tactical use only; absence justified. Syndicate: no entry — leverage framing is opportunistic, not doctrinal; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | N/A — `target_district = None`; card operates on acting faction's own PA submission, not a district. | — |
| Supported by components | ✓ | PoliticalAct as target; Exposure as cost; `standing_impact` for outcome (Art 02b §7). | Art 02a §8; Art 02b §7; Art 04b §5 |
| Supported by game procedure | ✓ | Submitted at Dispatch (§9); placed in Beat 2 row at Resolution Grid setup (§11 Beat 0); moved to Beat 4 carry row during Beat 2 processing (§11 Beat 2); `standing_impact` multiplier applied at Beat 4 (§17). | Art 03 §9, §11, §17 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
C07 = Card(
    id      = 7,  version = "v1.1",
    name    = "Amplify",
    tagline = "Boost the Public Standing impact of your own public act this round.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Resolution,  function = Modify,  subject = PoliticalAct,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,

    target_district = None,
    target_faction  = faction.acting,
    target_object   = PoliticalAct,

    affinity    = faction(acting) == Network: cost.resource.exposure -= 1,
    restriction = None,
    cost        = resource.faction(acting).exposure * 2,

    success     = faction(acting).op(beat=4, type=PoliticalAct).standing_impact *= 2,
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

### C08 — BUY INFLUENCE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Economy-bypasses-Territory card — the only Standard CovertOperation with no restriction and no presence requirement. Capital buys presence directly, reflecting that money can substitute for community groundwork. Cost vs reward: 3 Capital is high but buys 2 presence on success (more than C03's 1), and crit success adds a third. Syndicate affinity is difficulty reduction, not cost reduction — the Syndicate does not spend less; it converts capital to presence more reliably. Three portrait penalties represent strong doctrinal opposition: bought influence is an institutional threat to Guild's earned-presence model, Directorate's legitimate-process model, and Network's relational model.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Deploying capital to buy presence covertly fits the game's economic warfare frame. No presence requirement is a deliberate design feature — capital substitutes for community groundwork. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Syndicate's perspective ("capital determines which doors exist") is the sharpest statement of the card's design logic. All five perspectives doctrinally distinct. | Art 00 §7 |
| Doctrine alignment | ✓ | Card effect strongly opposes Guild (earned-presence model), Directorate (legitimate-process model), and Network (relational model); supports Syndicate doctrine. Captured via portrait entries (Guild/Directorate/Network submitter=−1, Syndicate submitter=+1). No target_faction → doctrine_mod not applicable; doctrinal signal is portrait-only by design. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: purchase mechanism is covert; resulting presence tokens are visible board state. Standard: all factions can deploy capital to buy presence. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Territory` — placing PresenceTokens is a territorial operation. `function = Add`, `subject = PresenceToken` — correctly scoped. | Art 04b §4, §5 |
| Balance | ✓ | 3 Capital is the highest Standard cost. No presence restriction is the tradeoff. Success = +2 presence (superior to C03's +1); crit = +3 total. Syndicate affinity: effective threshold 75%. Crit fail −2 PS is severe — publicly-failed capital deployment. | Art 02a §6, §8; Art 02b §7 |
| Effect duration | ✓ | Permanent: presence tokens persist until removed. Appropriate for a territorial placement card. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: bought presence undermines earned-presence model (P11, P16). Directorate `submitter=−1`: purchasing influence bypasses legitimate institutional process (P11, P16). Network `submitter=−1`: capital-as-power is exactly what Network opposes (P11, P16). Ghost `submitter=−1`: bought presence is noisy — "draws the wrong kind of attention"; against low-profile doctrine (P11, P16). Syndicate `submitter=+1`: capital doctrine — "determines which doors exist" (P11, P16). All five entries present; four opposing, one aligned — C08 is Syndicate's card by design. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. No presence restriction — capital bypasses standard entry requirement. | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken (Art 02a §6); Capital cost (Art 02a §8); failcrit PS −2 (Art 02b §7). | Art 02a §6, §8; Art 02b §7 |
| Supported by game procedure | ✓ | Submitted at Dispatch (§9); placed in Beat 3 row of Resolution Grid (§11 Beat 0); d100 threshold 50 with ring_mod and affinity; resolved at Beat 3 (§11 Beat 3). | Art 03 §9, §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
C08 = Card(
    id      = 8,  version = "v1.1",
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

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

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

### C09 — FUND
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Alliance-seeding card — the only card in the Standard set that transfers resources between factions. Source is anonymous by default; the acting faction receives an Accord Card (cost 0) that it may play to announce the transfer publicly. Cost vs reward: 2 Capital spent to transfer 2 Capital to the target — net zero to the actor at success, but crit success awards +1 PS and the Accord Card opens alliance mechanics. Syndicate affinity is difficulty reduction — the Syndicate is the faction most practiced at informal financial transfers. Full balance assessment deferred until Art 06 (Accord mechanics) is developed.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Anonymous resource transfer as covert act — the act of funding is covert; the Accord Card is what potentially reveals it. Faction-to-faction relationship seeding fits the game's alliance layer. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Directorate's "we monitor these carefully" is the subtlest threat at the table. All five perspectives doctrinally distinct — relationship investment, institutional scrutiny, financial exposure, operational awareness, capital relationships. | Art 00 §7 |
| Doctrine alignment | ✓ | `target_faction = faction.opponent` — `doctrine_mod = {Neighbor: +15, Opposed: -15}` applies. Syndicate affinity (+25) stacks — funding a Neighbor as Syndicate reaches effective threshold 90. Capital flows where doctrine is aligned; crosses resistance where it is not. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: anonymous transfer is covert; Accord Card preserves optionality on disclosure. Standard: all factions can fund others. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Economy` — capital transfer is NativeResource flow, correctly Economy under Art 04b §4.4. `function = Redirect`, `subject = NativeResource` — correctly scoped. | Art 04b §4, §5 |
| Balance | ⚠ | Net capital zero at success (2 Capital spent = 2 Capital delivered). Syndicate effective threshold 75%. Crit success = +1 PS bonus. **Open:** AccordCard = free Public Act (cost 0); its value is determined by P-series PA card costs. Reassess C09 balance once P-series is designed — if a free PA is worth more than 2 Capital spent, cost or threshold may need adjustment. | Art 02a §8; Art 04 P-series (pending) |
| Effect duration | ✓ | Capital transfer is instantaneous. AccordCard duration governed by Art 06 (pending). | Art 06 (pending) |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Syndicate `submitter=+1`: capital-in-motion doctrine — "relationships create opportunities" (P11, P16). Directorate `submitter=−1`: using anonymous financial transfer conflicts with legitimate-process doctrine; Directorate scrutinises these transfers in others — performing one is in-doctrine hypocrisy (P11, P16). Guild: no entry — relationship investment is pragmatic, not doctrinal; absence justified. Network: no entry — analytical framing only; no doctrinal stake as actor; absence justified. Ghost: no entry — observational framing; Ghost tracks capital flows for intelligence, not as participant; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | N/A — `target_district = None`; faction-level operation, no district target. | — |
| Supported by components | ⚠ | Capital (Art 02a §8) ✓. AccordCard undefined — pending Art 02 component definition. | Art 02a §8; Art 02 (pending) |
| Supported by game procedure | ⚠ | Dispatch and Beat 3 resolution ✓. Anonymous transfer case-return procedure and AccordCard delivery undefined — pending Art 03 definition. | Art 03 §9, §11; Art 03 (pending) |

#### Outstanding Issues

- **P-series dependency:** AccordCard = free Public Act; its balance value is determined by P-series PA card costs. Reassess after P-series is designed.
- **AccordCard PA slot conflict:** AccordCard grants a free, additional Public Act beyond normal dispatch. This likely violates Art 03 Quarter structure — PA slot limits, dispatch sequencing, or Beat 2/4 submission rules. Needs Art 03 review; AccordCard mechanic may need to be reframed (e.g., as a modifier to an existing PA rather than an extra one, or as a deferred PA in a later Quarter).
- **Art 02 dependency:** AccordCard requires component definition in Art 02 series before C09 spec is complete.
- **Art 03 dependency:** Anonymous transfer case-return procedure (resources delivered at debrief, covert until AccordCard played) and AccordCard delivery procedure to be defined in Art 03; migrates to Art 07 when ARBITER subroutines are identified.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
C09 = Card(
    id      = 9,  version = "v1.1",
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

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = NativeResource,

    affinity    = faction(acting) == Syndicate: threshold += 25,
    restriction = None,
    cost        = resource.faction(acting).capital * 2,

    success     = (
        faction(target).resource.capital += 2,
        game.dispatch(faction(acting), AccordCard)
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

### C10 — PROTECT
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Defensive Beat 2 positional wager — the only Standard card that explicitly protects existing assets. Applies only to the acting faction's assets in the named district, not the district broadly. Cost vs reward: 1 district-native paid regardless of whether an attack materializes; if it does, −25 threshold reduction (−45 for Guild/Directorate) meaningfully degrades opponents' attack probability. Guild and Directorate affinity reflects institutional defense as core competency, not exceptional response.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Defensive preparations as covert act — protection is installed silently; effect is felt at Beat 3. Positional wager structure makes the action genuinely risky (wrong read wastes the slot). | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Ghost's "best protection is not being found" is the anti-use doctrine. All five perspectives distinct — obligation to defend, institutional resource, people-first, non-presence, value retention. | Art 00 §7 |
| Doctrine alignment | ✓ | Active asset defense serves Guild (protect what we build) and Directorate (institutional assets require defense) — both captured via portrait. Ghost is doctrinally opposed (concealment over fortification) — captured via portrait. Self-targeted → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: defensive preparations are covert. Standard: all factions can protect their assets; Guild/Directorate affinity rewards institutional-defense doctrine. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Resolution` — per Art 04b §4.6, Protect distributes to the target's layer. Target is CovertOperation (Resolution layer). `function = Protect`, `subject = CovertOperation` — correctly scoped. | Art 04b §4.6, §5 |
| Balance | ✓ | Beat 2 positional wager; 1 native cost. Guild/Directorate affinity −45 locked (L179): near-nullification narratively justified — Guild knows every access point and structural vulnerability in their own infrastructure; Directorate's institutional security apparatus (personnel, protocols, access control) can effectively stop a covert demolition attempt. The 5% floor acknowledges no protection is absolute. Attacker does not know protection is installed (C10 is covert) — near-nullification is a consequence of capability, not a visible deterrent. Base −25 (other factions) leaves 25% — acceptable risk. | Art 02a §8; Art 02b §7 |
| Effect duration | ✓ | Single-round: arms at Beat 2, applies at Beat 3, does not persist past round. | — |
| Persistence | ✓ | Immediate — Beat 2 carry; applied at Beat 3 via Resolution Grid; no game-state marker persists beyond round | Art 04 §6 |
| Trigger validity | ✓ | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Guild `submitter=+1`: protecting built assets is non-optional doctrine — "we protect what we build" (P11, P16). Directorate `submitter=+1`: institutional assets require active defense — resourced accordingly (P11, P16). Ghost `submitter=−1`: active fortification conflicts with concealment doctrine — "best protection is not being found" (P11, P16). Network: no entry — "we protect our people first; infrastructure is secondary"; situational use, not doctrinal; absence justified. Syndicate: no entry — rational asset-value framing, no doctrinal stake in fortification; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: acting presence in target district. | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken (restriction); district native cost (Art 02a §8); threshold reduction applied to Beat 3 ops targeting acting assets. | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Submitted at Dispatch (§9); placed in Beat 2 row at Resolution Grid setup (§11 Beat 0); threshold reduction applied at Beat 3 resolution (§11 Beat 3). Note: Art 03 §20 M-09 refs in prior version are stale (pre-S52 reorg). | Art 03 §9, §11 |

#### Outstanding Issues

- **Art 03 dependency:** Threshold reduction marker placement (ARBITER places −25/−45 marker on Beat 3 ops targeting acting faction's assets at Beat 2 resolution) to be defined in Art 03 §11 Beat 2 processing steps.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
C10 = Card(
    id      = 10,  version = "v1.1",
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

    target_district = district.any,
    target_faction  = None,
    target_object   = CovertOperation,

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

### C39 — ABSOLUTE COMPROMISE
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Standard counter-counter card — the only card available to all factions that removes a Beat 2 Block or Protect operation before it can apply. Addresses the problem that committed defensive plays (Invoke Jurisdiction, Regulatory Capture, Fortify Structure, Protect) otherwise have no counter in the same round. Intel token cost makes this a premium play — factions must hold Intel specifically to access this capability, reinforcing Intel as a cross-faction strategic resource. Cannot target Type B Countermeasures (faction defense layers) or Hidden Objectives — only active Beat 2 Board Conditions. Positioned here from §8 where it was misplaced: C39 is subtype=Standard (all factions), not FactionSpecific.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Counter-counter card — removes a committed Beat 2 Block or Protect before it applies; fills gap where defensive positional wagers have no standard counter | Art 00 §7 |
| Voice fit | ✓ | Standard card; all-faction access; no faction-specific voice required; perspectives block expected for full Standard spec — confirm complete in code block | Art 00 §7 |
| Doctrine alignment | ✓ | N/A — Standard card; no faction doctrine alignment required; no affinity; portrait = {} | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / Standard / faction=None — all-faction counter-counter capability; no faction restriction | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Submission/Block/CovertOperation — removes a submitted covert op's effect before it applies; Block function correct | Art 04b §4, §5 |
| Balance | ✓ | Intel token for one Beat 2 card removal — premium cost justified by cross-faction utility; resources on discarded card not refunded (Outstanding Issue) | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: target card discarded at Beat 2 resolution; no lingering effect | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces target Beat 2 card exists | — |
| Portrait validity | ✓ | portrait = {} — Standard card; no portrait entry confirmed intentional | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — Beat 2 cards are district-anchored | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; Beat 2 Block or Protect card as target — scope definition outstanding (Outstanding Issue) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; target card must exist in Beat 2 row at resolution; discard occurs at Beat 2; Type A/B distinction outstanding (Outstanding Issue) | Art 03 §9, §11 |

#### Outstanding Issues

- **Type A vs Type B Countermeasure distinction:** Design note says "cannot target Type B Countermeasures (faction defense)." Confirm Type A / Type B taxonomy is defined somewhere in Art 03 or Art 04 — if not, this card cannot be adjudicated correctly.
- **Scope of "Block or Protect card":** Does this include all Beat 2 Automatic cards that create restrictions (e.g., C34 Golden Parachute, C38 Parasitic) or only cards that explicitly Block/Protect? Definition needed for ARBITER adjudication.
- **Resource refund on discard:** Resources committed to the discarded card are explicitly not refunded. Confirm this is the intent — the faction who played the blocked card loses both the slot and resources.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Migrated from §8 Intel Economy block to Standard Covert section S59. Pre-convention flat format — full schema pass pending (04-47).*

```python
C39 = Card(
    id=39,  version="v1.0",
    name    = "Absolute Compromise",
    tagline = "Some barriers are not barriers at all — just the illusion of one.",
    type    = CovertOperation,  subtype = Standard,  faction = None,
    layer   = Submission,  function = Block,  subject = CovertOperation,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=district.named, target_faction=None, target_object=Beat2BlockOrProtectCard,
    affinity=None,
    restriction = district(target).beat2_row.has_block_or_protect_card == True,
    cost        = IntelToken(any) * 1,
    success     = game.discard(target_card, district(target).beat2_row),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "There are no walls. There are only varying degrees of access.",
    perspectives = {},
    design_note  = "Cannot target Type B Countermeasures (faction defense) — only Type A (District Block) and Protect/Fortify ops. Intel token consumed is any held token. Migrated from §8 Intel Economy block — Standard subtype confirmed.",
    arbiter_note = "At Beat 2 resolution: discard named Beat 2 Block or Protect card from target district. Resources committed to that card by its submitting faction are not refunded. Operations the card would have blocked or protected proceed without that modifier.",
)
```

---

### STANDARD — DISINFORMATION CAMPAIGN
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
First Standard card with Public Standing shift as its primary covert effect — fills the Standing/Shift coverage gap flagged in Art 04b §8. Distinct from Public Act PS cards (P04, P07): this is a covert operation, so the acting faction is unknown to the target. Presence restriction grounds it in operational reality: you need a footprint in a district to run a local narrative operation. The failcrit NotificationSlip follows C22 precedent — a badly botched campaign leaves traces, and ARBITER notifies the target that a campaign ran in that district (not who ran it). Network affinity (threshold +10) reflects broadcast infrastructure amplifying covert narrative reach. Ghost affinity (cost −1) reflects datastream manipulation as native capability.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert narrative manipulation as a standard capability: all factions can conduct local perception operations against each other | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild notices effects rather than participating; Directorate opposes covert image manipulation on principle; Network values the tool but distinguishes signal from noise; Ghost flags the attention risk; Syndicate tracks market implications | Art 00 §7 |
| Doctrine alignment | ✓ | Network affinity (threshold +10): broadcast infrastructure amplifies narrative reach. Ghost affinity (cost −1): datastream manipulation is native capability. Directorate portrait −1: covert manipulation conflicts with institutional legitimacy doctrine. No doctrine_mod (no faction target for modifier) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: the source of the campaign is hidden. Standard: all factions can contest standing via covert narrative operations | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding — first Standard covert card in this taxonomy slot | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 40, ring_mod standard. Success swing: target −2 PS, acting +1 PS (net 3). Fail: acting −1 PS. Presence restriction limits targeting. Failcrit exposure risk makes reckless use costly | Art 02a §6–§7 |
| Effect duration | ✓ | PS shifts are Immediate; no lasting marker | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Network +1: broadcasting narrative to shift perception is core doctrine (P11, P16). Ghost −1: public narrative campaigns attract attention, conflicting with low-profile doctrine (P11, P16). Directorate −1: covert image manipulation undermines institutional legitimacy (P11, P16). Guild, Syndicate: no entry — neither has a doctrinal stake in covert narrative authorship | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any; restriction checks acting faction's presence in that district | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. PS tracked on Public Standing track (Art 02a §7); NotificationSlip (failcrit, same as C22) | Art 02a §7; Art 03 §11 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; NotificationSlip failcrit follows C22 established procedure | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
C_DisinformationCampaign = Card(
    id      = "—",  version = "v1.0",
    name    = "Disinformation Campaign",
    tagline = "Run a covert narrative operation degrading a faction's public standing in a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Standing,  function = Shift,  subject = PublicStanding,

    beat            = 3,
    resolution      = d100,
    threshold       = 40,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

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

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert destruction of opponent's intelligence records is a standard operational capability — all factions have grounds for denial operations against intel supply | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild reads operational records as accountability; Directorate holds institutional record preservation as principle; Network frames destruction as information erasure; Ghost frames it as operational security; Syndicate reads it as supply-side intelligence management | Art 00 §7 |
| Doctrine alignment | ✓ | No affinity — no faction has doctrine-native advantage for destroying a third party's intelligence tokens. Ghost portrait +1: operational security doctrine aligns with removing incriminating records. Network portrait −1: information destruction conflicts with transparency doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: source of removal is hidden. Standard: available to all factions | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Remove/IntelToken — fills coverage gap per Art 04b §6 | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 45, ring_mod None (no district target). Fail = no effect, cost sunk. Automatic fail if target holds no tokens at Beat 3. Pure denial — no material gain | Art 02a §5 |
| Effect duration | ✓ | Immediate — token destroyed at Beat 3, no lingering marker | 00-R21 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Ghost +1: destroying records aligns with low-profile and operational security doctrine. Network −1: information erasure conflicts with transparency and broadcast doctrine. Guild, Directorate, Syndicate: no entry | Art 04 §6.2 |
| Supported by zones | ✓ | No district target; operation targets faction's supply directly | Art 01 §6–§7 |
| Supported by components | ✓ | Intel tokens (Art 02a §5); no new components required | Art 02a §5 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; ARBITER blind draw from supply is consistent with ARBITER draw authority | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
C_Disprove = Card(
    id      = "—",  version = "v1.0",
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

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = IntelToken.any,

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
    arbiter_note = "Phase A: acting faction names target faction. Beat 3: if target faction holds zero Intel tokens, op fails (cost sunk; do not announce reason). Otherwise, draw one Intel token at random from target faction's supply and remove from play (return to box). Acting faction receives no information about the removed token. Target faction receives no notification.",
)
```

---

### STANDARD — INTEL EXTRACTION
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Economy/Redirect/IntelToken — splits Asset Extraction (S62) into two focused cards. Blind random draw: ARBITER transfers one Intel token from the target faction's supply to the acting faction's dispatch case, face-down. Acting faction discovers the token's content privately at Beat 3 resolution when the case opens; ARBITER does not announce content. Target faction's token count decreases visibly. Cost 2 native: extracting and getting away clean with a resource is operationally harder than destroying it. Ghost affinity (threshold +10): covert acquisition is Ghost doctrine. Syndicate portrait +1: capital intelligence infrastructure aligns Syndicate with resource acquisition by any means, but physical covert acquisition is not Syndicate's mechanical specialty — no threshold bonus warranted. Fails automatically if target holds no tokens at Beat 3.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert acquisition of an opponent's Intel tokens is a standard economic-denial operation — acting faction gains an intelligence asset while the target loses one | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild refuses to take others' gathered work; Directorate opposes covert acquisition as bypassing sanctioned process; Network notes the token continues to exist; Ghost treats it as native operational methodology; Syndicate reads it as capital intelligence arbitrage | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost affinity (threshold +10): covert acquisition is Ghost doctrine. Syndicate portrait +1: capital intelligence motivation aligns Syndicate with resource acquisition — no mechanical threshold bonus, physical acquisition is not Syndicate-native. Directorate portrait −1: covert acquisition bypasses legitimate process. Guild portrait −1: taking what others gathered | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: acting faction unknown; target's count decreases visibly. Standard: available to all factions | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Redirect/IntelToken — fills coverage gap per Art 04b §6; splits Asset Extraction (S62) | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 45 (Ghost: 55), ring_mod None. Fail = no effect, cost sunk. Automatic fail if target holds no tokens at Beat 3. Double effect (acting gains, target loses) justifies same cost as pure-denial Disprove | Art 02a §5 |
| Effect duration | ✓ | Immediate — token transferred at Beat 3, no lingering marker | 00-R21 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Syndicate +1: covert resource acquisition aligns with capital intelligence doctrine. Guild −1: taking what others gathered conflicts with earned-value principle. Directorate −1: bypasses sanctioned intelligence handling. Ghost, Network: no entry | Art 04 §6.2 |
| Supported by zones | ✓ | No district target; operates directly on faction's supply | Art 01 §6–§7 |
| Supported by components | ✓ | Intel tokens (Art 02a §5); dispatch case procedure established (Art 03 §11); no new components | Art 02a §5; Art 03 §11 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; face-down transfer to dispatch case follows established case-handling procedure | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
C_IntelExtraction = Card(
    id      = "—",  version = "v1.0",
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

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = IntelToken.any,

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
    arbiter_note = "Phase A: acting faction names target faction. Beat 3: if target faction holds zero Intel tokens, op fails (cost sunk; do not announce reason). Otherwise, draw one Intel token at random from target faction's supply. Transfer face-down to acting faction's dispatch case — acting faction may inspect privately. Target faction's token count decreases by 1 (visible).",
)
```

---

### STANDARD — MODIFIER RAID
[↑ Covert Operations](#standard-covert-operations)

#### Design Rationale
Economy/Redirect/ModifierCard — splits Asset Extraction (S62) alongside Intel Extraction, with modifier cards as the target resource. Same blind draw mechanic: ARBITER transfers one modifier card at random from the target faction's hand to the acting faction's dispatch case, face-down. Acting faction discovers the card privately at Beat 3 resolution. Target faction's card count decreases visibly. Modifier cards represent prepared tactical advantages — stealing one simultaneously strips the opponent's preparation and delivers that advantage to the acting faction. Same affinity structure as Intel Extraction (Ghost threshold +10; Syndicate portrait +1). Cost 2 native. Fails automatically if target holds no modifier cards at Beat 3.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert acquisition of an opponent's modifier cards simultaneously denies their tactical preparation and transfers that advantage to the acting faction | Art 00 §7 |
| Voice fit | ✓ | Five perspectives doctrinally distinct — Guild refuses to take tools others made; Directorate opposes covert seizure of operational resources; Network notes the card's function shifts by context; Ghost targets the tactical disruption aspect; Syndicate reads it as operational arbitrage | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost affinity (threshold +10): covert acquisition doctrine, same as Intel Extraction. Syndicate portrait +1: resource acquisition by covert means aligns with capital intelligence doctrine. Same affinity structure as Intel Extraction | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: source hidden; target's card count decreases visibly. Standard: available to all factions | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Redirect/ModifierCard — fills coverage gap per Art 04b §6; splits Asset Extraction (S62) | Art 04b §4 |
| Balance | ✓ | 2 native, threshold 45 (Ghost: 55), ring_mod None. Parallel structure to Intel Extraction — same cost and threshold for same operational profile. Automatic fail if target holds no modifier cards at Beat 3 | Art 02a §5 |
| Effect duration | ✓ | Immediate — card transferred at Beat 3, no lingering marker | 00-R21 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Syndicate +1: covert resource acquisition aligns with capital intelligence doctrine. Guild −1: taking tools others built conflicts with earned-value principle. Directorate −1: seizure of operational resources bypasses legitimate process. Ghost, Network: no entry | Art 04 §6.2 |
| Supported by zones | ✓ | No district target; operates directly on faction's modifier card hand | Art 01 §6–§7 |
| Supported by components | ✓ | Modifier cards (Art 02b); dispatch case procedure established (Art 03 §11); no new components | Art 02b; Art 03 §11 |
| Supported by game procedure | ✓ | Beat 3 covert resolution; face-down transfer to dispatch case follows established case-handling procedure | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
C_ModifierRaid = Card(
    id      = "—",  version = "v1.0",
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

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = ModifierCard.any,

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
    arbiter_note = "Phase A: acting faction names target faction. Beat 3: if target faction holds zero modifier cards, op fails (cost sunk; do not announce reason). Otherwise, draw one modifier card at random from target faction's hand. Transfer face-down to acting faction's dispatch case — acting faction may inspect privately. Target faction's modifier card count decreases by 1 (visible).",
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
| [P01](#p01-open-operations) | Open Operations |
| [P02](#p02-disputed-claim) | Disputed Claim |
| [P03](#p03-public-commission) | Public Commission |
| [P04](#p04-public-censure) | Public Censure |
| [P05](#p05-on-the-record) | On the Record |
| [P06](#p06-economic-sanction) | Economic Sanction |
| [P07](#p07-public-address) | Public Address |
| [P08](#p08-table-an-accord) | Table an Accord |

### P01 — OPEN OPERATIONS
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Public counterpart to C03 (Campaign). Same cost (2 native), guaranteed outcome (Automatic), PS +1 on success. The trade: covert presence-building is hidden but risky (d100/50, fail wastes cost); Open Operations is visible from Phase B declaration but certain. Directorate's cost waiver reflects that formal institutional presence declaration is a zero-friction doctrinal act — the mandate is the permission. Ghost's portrait −1 captures the cost of committing to visibility against concealment doctrine.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public territorial declaration is a core political act in New Meridian — every faction makes formal presence claims | Art 00 §7 |
| Voice fit | ✓ | Five distinct perspectives: Guild grounds it in the build, Directorate in the record, Network in confirmation, Ghost in commitment-cost, Syndicate in sequencing | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate affinity (cost = 0) + portrait +1. Ghost portrait −1. Others no entry — justified | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / Standard — all factions make public presence claims; universally useful | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken — unambiguous | Art 04b §4 |
| Balance | ✓ | Same cost as C03; Automatic vs. d100/50; +PS. Trade is visibility, not resources | Art 02a §6–§7 |
| Effect duration | ✓ | Presence tokens are Permanent board state; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1: submitter-bounded (P16). Ghost −1: submitter-bounded. No direct PS shift in portrait (P12) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone reference; ring entry enforced at Beat 0 by ARBITER | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02a §6); faction native × 2 cost (Art 02a §8) | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Beat 4 resolution; ring entry rules enforced at Beat 0 | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P01 = Card(
    id="P01",  version="v1.0",
    name    = "Open Operations",
    tagline = "Formally declare your operational presence in a district.",
    type    = PoliticalAct,  subtype = Standard,  faction = All,

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

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

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
    design_note  = "Public version of C03 Campaign. Same cost (2 native), guaranteed outcome (Automatic), PS +1 on success. Trade: covert = hidden + risky vs. public = visible + certain. Directorate affinity: formal institutional presence declaration has no resource cost against mandate doctrine. Ghost −1: visibility conflicts with concealment doctrine. Ring entry rules still enforced by ARBITER at Beat 0.",
    arbiter_note = "Place 2 presence tokens for acting faction in declared district at Beat 4. Apply PS +1 to acting faction. Confirm ring entry requirements at Beat 0 — if not satisfied, PA voided; resources returned; acting faction takes Public Pass.",
)
```

---

### P02 — DISPUTED CLAIM
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Public counterpart to C04 (Undermine). Same cost (2 native), slightly better base threshold (45 vs 40), PS effects added. Going public here means accepting accountability: a failed challenge hurts the challenger's standing. Network and Directorate gain threshold bonuses reflecting doctrinal alignment with formal territorial dispute mechanisms. The fail/failcrit PS penalties make this meaningfully riskier than it looks — public challenges are public commitments.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal territorial challenges are institutionally grounded in New Meridian | Art 00 §7 |
| Voice fit | ✓ | All five perspectives credible and distinct: Guild's reluctance-but-will-defend, Directorate's formal-mechanism preference, Network's public-accountability, Ghost's attention-cost framing, Syndicate's leverage reading | Art 00 §7 |
| Doctrine alignment | ✓ | Network +10 threshold + portrait +1; Directorate +10 threshold + portrait +1 — formal dispute mechanisms align with both doctrines. Ghost portrait −1: public confrontation conflicts with concealment. doctrine_mod captures target relationship | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / Standard — all factions contest territory | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Remove / PresenceToken — target is a PresenceToken being removed | Art 04b §4 |
| Balance | ✓ | Same cost as C04; slightly better threshold; PS effects add risk on fail. Contested marker fires on tie — procedural | Art 02a §6–§7 |
| Effect duration | ✓ | Presence token removal is a permanent state change; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1, Directorate +1, Ghost −1: all submitter-bounded (P16). PS effects are game effects, not Portrait shifts (P12) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone reference; ring_mod calibrated to ring context | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken — target removal (Art 02a §6); ContestedMarker — procedural (Art 03 §11); faction native × 2 cost (Art 02a §8) | Art 02a §6, §8; Art 03 §11 |
| Supported by game procedure | ✓ | Beat 4; Contested marker placement governed by Art 03 §11; ring_mod applies | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P02 = Card(
    id="P02",  version="v1.0",
    name    = "Disputed Claim",
    tagline = "Formally challenge another faction's presence in a district.",
    type    = PoliticalAct,  subtype = Standard,  faction = All,

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

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

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
    design_note  = "Public version of C04 Undermine. Same cost (2 native); threshold 45 vs C04's 40; PS consequences added. Fail/failcrit penalise the challenger — public challenges are public commitments. Network/Directorate +10 threshold: doctrinal alignment with formal dispute mechanisms. Ghost −1: public confrontation conflicts with concealment doctrine. doctrine_mod: Neighbor +10, Opposed −10 on target faction relationship.",
    arbiter_note = "Beat 4. Remove 1 presence token from target faction. Check for tie at highest chip count — if tie at 3+ chips, place Contested marker. PS: acting +1, target −1 on success. Acting −1 on fail. Acting −2 on failcrit (no token removed on fail/failcrit).",
)
```

---

### P03 — PUBLIC COMMISSION
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Public counterpart to C01 (Build Structure). Same cost; unlike C01, the construction is publicly announced at Phase B and ARBITER records it. The covert element is absent — there is no hidden intent here. Going public provides certainty (Automatic) and PS +1 versus C01's concealed attempt with failure risk. Guild's affinity (district native = 0) is maximally on-doctrine here: Guild building in public is the purest expression of permanence doctrine. Ghost's portrait −1 reflects that public structures are commitments Ghost would not voluntarily create.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public construction is a core territorial act — all factions build where the strategy demands it | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct and credible: Guild's open permanence, Directorate's mandate/record framing, Network's observation of public statements, Ghost's accountability-cost, Syndicate's visible-portion-of-investment framing | Art 00 §7 |
| Doctrine alignment | ✓ | Guild affinity (district native = 0) + portrait +1 — maximally on-doctrine (permanence through building). Ghost −1: permanent public structure conflicts with concealment. Others: no doctrinal stake in public construction | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / Standard — structure building is universally available; Guild affinity appropriate but not exclusive | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / StructureBlock | Art 04b §4 |
| Balance | ✓ | Same cost as C01; Automatic vs d100; PS +1. Trade: visibility for certainty. Guild effectively pays 1 native (affinity waives district native) | Art 02a §6–§7 |
| Effect duration | ✓ | StructureBlock = Permanent board state; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Guild +1, Ghost −1: submitter-bounded. Same doctrine logic as C01 | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid; restriction checks district presence and structure state (valid zone conditions) | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock (Art 02a §7); PresenceToken — restriction (Art 02a §6); faction native + district native costs (Art 02a §8) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 4; restriction checked at Beat 0 | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P03 = Card(
    id="P03",  version="v1.0",
    name    = "Public Commission",
    tagline = "Publicly announce and fund construction of a structure in a district.",
    type    = PoliticalAct,  subtype = Standard,  faction = All,

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

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

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
    design_note  = "Public counterpart to C01. Same cost; Automatic (no fail risk); PS +1. Guild affinity (district native = 0) on-doctrine. Ghost −1: public structure = permanent commitment against concealment doctrine. Counter to Guild's build pace: Directorate P11 (Regulatory Override) raises cost of presence-placement in district (prerequisite for this card); P09 (Civic Works Mandate) can be blocked by P11.",
    arbiter_note = "Place 1 structure block for acting faction in declared district at Beat 4. PS +1. Restriction at Beat 0: acting faction must have presence and no existing structure. If restriction fails, PA voided.",
)
```

---

### P04 — PUBLIC CENSURE
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
The PS attack card of the standard set. A formal public accusation carries both potential and risk — a failed censure reflects worse on the accuser than the target. Network and Directorate get cost reductions (accusation is their institutional/broadcast mode). An optional Fresh Intel token submitted at Phase B provides a +15 threshold bonus, rewarding prior intelligence work. The fail and failcrit costs ensure reckless censure is punished. Ghost's portrait −1 reflects that self-exposure is the cost of public accusation.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal accusations are a core political act — all factions can and do make them | Art 00 §7 |
| Voice fit | ✓ | All five perspectives credible: Guild's evidence-based restraint, Directorate's formal mechanism framing, Network's public-fact stance, Ghost's attention-trace surveillance read, Syndicate's public-leverage calculation | Art 00 §7 |
| Doctrine alignment | ✓ | Network −1 cost + portrait +1; Directorate −1 cost + portrait +1 — formal accusation aligns with institutional/broadcast doctrines. Ghost −1 portrait: public accusation = self-exposure. Intel token affinity is doctrinally neutral. No target_faction → doctrine_mod not applicable | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / Standard | Art 04 §6.2 |
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding | Art 04b §4 |
| Balance | ✓ | Base threshold 35 is demanding; Intel token affinity rewards preparation. Fail/failcrit PS penalties create real downside | Art 02a §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1, Directorate +1, Ghost −1: submitter-bounded. PS shifts are game effects not Portrait (P12) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted action; no zone reference. ring_mod = None. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (optional, Fresh — spent on resolution regardless; Art 02a §6); faction native × 2 cost (Art 02a §8) | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Beat 4; Intel token submitted with case at Phase B; token spent regardless | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P04 = Card(
    id="P04",  version="v1.0",
    name    = "Public Censure",
    tagline = "Formally accuse another faction of conduct contrary to the city's interest.",
    type    = PoliticalAct,  subtype = Standard,  faction = All,

    layer    = Standing,  function = Shift,  subject = PublicStanding,

    beat            = 4,
    resolution      = d100,
    threshold       = 35,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Contested",
    outcome_type    = Unilateral,
    persistence     = Immediate,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

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
    design_note  = "PS attack card of the standard set. Base threshold 35 — demanding. Fresh Intel token (optional, submitted at Phase B, spent regardless of outcome) provides +15 threshold. Network/Directorate −1 cost each. Fail/failcrit PS penalties punish reckless censure. Ghost −1 portrait: public accusation = self-exposure. PS shifts in success/fail are game effects, not Portrait (P12).",
    arbiter_note = "At Phase B: acting faction names target faction. If Intel token submitted, ARBITER holds it. Beat 4: threshold = 35 + 15 if Fresh Intel submitted. On success: target −2 PS, acting +1 PS; Intel token spent. On fail: acting −1 PS; Intel token still spent. On failcrit: acting −2 PS.",
)
```

---

### P05 — ON THE RECORD
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Formal public attribution of a covert action. Requires an Intel token naming the target faction (spent regardless of outcome) — you cannot make the accusation without evidence. Token age determines confidence: Fresh = threshold 50, Stale = 35. Network gains +10 threshold bonus (broadcasting attribution is their mode). Ghost's portrait at −2 (the highest negative in the set) reflects that Ghost's doctrine protects operational anonymity across the entire table — attributing any faction's covert operation is a violation of Ghost's belief that understanding accumulates privately.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public attribution of covert operations is a core political act — creates accountability where covert ops sought deniability | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's evidence-responsibility framing, Directorate's institutional/conditional support, Network's right-to-know, Ghost's doctrine of operational privacy (principle not preference), Syndicate's leverage-timing calculation | Art 00 §7 |
| Doctrine alignment | ✓ | Network portrait +1: broadcasting attribution is doctrinal. Ghost portrait −2 (highest negative in set): attributing any faction's op violates Ghost's belief that operational anonymity protects the whole table's intelligence discipline. Others: no doctrinal stake in the attribution mechanism itself | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / Standard — any faction can attribute | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Reveal / ActionAttribution | Art 04b §4 |
| Balance | ✓ | Token cost + resource cost; token age tiers threshold (Fresh 50, Stale 35); Expired excluded. Fail: self-PS loss (false or botched attribution). High success PS reward reflects the significance of public attribution | Art 02a §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1 (doctrine), Ghost −2 (doctrine): both submitter-bounded. No Portrait shifts in effect fields | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted attribution; no zone reference. ring_mod = None. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (faction=target, age=Fresh or Stale — Expired excluded per restriction; Art 02a §6); faction native × 1 cost (Art 02a §8) | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Beat 4; Intel token submitted with case; token age determined at Beat 4 | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P05 = Card(
    id="P05",  version="v1.0",
    name    = "On the Record",
    tagline = "Formally attribute a recent covert action to a named faction before the city.",
    type    = PoliticalAct,  subtype = Standard,  faction = All,

    layer    = Information,  function = Reveal,  subject = ActionAttribution,

    beat            = 4,
    resolution      = d100,
    threshold       = None,  # derived from token age — Fresh: 50, Stale: 35; see affinity
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Contested",
    outcome_type    = Unilateral,
    persistence     = Immediate,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    affinity    = (
        faction(acting).holds_intel_token(faction=target, age=Fresh):  threshold = 50,
        faction(acting).holds_intel_token(faction=target, age=Stale):  threshold = 35,
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
    arbiter_note = "Intel token submitted at Phase B. Verify token age: Fresh or Stale satisfies restriction; Expired does not. Beat 4: threshold = age-based (50 Fresh / 35 Stale) + 10 if Network. On success: announce '[Acting faction] attributes [op type, quarter] to [target faction].' Target −2 PS, acting +2 PS. Token spent. On fail: acting −1 PS. Token spent regardless.",
)
```

---

### P06 — ECONOMIC SANCTION
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
The economic attack card of the standard PA set. PS is intentionally reversed from intuitive expectation: the faction applying sanctions takes a public standing penalty (aggressor optic), while the target gains sympathy. The card's value is purely the resource damage (target loses 2 native) — players trade PS for economic impact. This creates meaningful faction differentiation: Ghost plays it readily (low PS concern), Network is reluctant (PS-dependent), Syndicate is the natural primary user (Capital leverage, threshold bonus). Fail/failcrit penalise the acting faction — a failed public sanction looks worse than not attempting one.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Economic sanctions are a legitimate public instrument — all factions can apply financial pressure | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's last-resort restraint, Directorate's formal instrument framing, Network's neutral observation, Ghost's collateral-attention awareness, Syndicate's capital-discipline framing | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate +15 threshold + portrait +1: Capital leverage doctrine aligns with economic pressure. Guild portrait −1: economic weapons conflict with permanence-through-building doctrine. doctrine_mod accounts for target relationship | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / Standard | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Remove / NativeResource | Art 04b §4 |
| Balance | ✓ | Acting faction absorbs −1 PS on success as the cost of the aggressor position. Threshold 40 + Syndicate +15. Value = resource denial (up to 2 native, floor = 0), not PS gain | Art 02a §6–§7 |
| Effect duration | ✓ | Resource removal and PS shifts are immediate; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Syndicate +1, Guild −1: submitter-bounded. PS shifts are game effects, not Portrait | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted action; no zone reference. ring_mod = None. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource (target's supply, Art 02a §8); faction native × 1 cost (Art 02a §8). Floor clause is procedural | Art 02a §8 |
| Supported by game procedure | ✓ | Beat 4; ARBITER removes up to 2 native resources from target (floor = 0 — all available if fewer than 2) | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P06 = Card(
    id="P06",  version="v1.0",
    name    = "Economic Sanction",
    tagline = "Publicly impose economic pressure on a faction, forcing resource loss.",
    type    = PoliticalAct,  subtype = Standard,  faction = All,

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

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

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

### P07 — PUBLIC ADDRESS
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
Self-directed PS building — fills the gap in the standard set (P04 attacks opponent's PS; P07 builds own). Cheap (1 native), certain (Automatic), grants +2 PS in exchange for having presence in the target district. No faction monopolises public communication — all factions make public statements — but the portrait reflects who finds it doctrinally meaningful (Directorate, Network) versus costly (Ghost). The requirement to already have presence prevents factions from claiming standing in districts where they have no legitimacy.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public statements and rallies are universal political acts | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's building-primary-but-does-speak, Directorate's institutional communication expectation, Network's terse "this is what we do", Ghost's analytical surveillance framing of own public acts, Syndicate's investment/return calculation | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate +1, Network +1: institutional communication and broadcasting are both core doctrinal expressions. Ghost −1: public address = attention = exposure risk. Others: no strong doctrinal alignment with the act itself | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / Standard | Art 04 §6.2 |
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding — +2 PS is a relative position change, not an unconditional grant | Art 04b §4 |
| Balance | ✓ | 1 native for +2 PS with presence restriction. Cheap but not free; presence requirement prevents abuse | Art 02a §6–§7 |
| Effect duration | ✓ | PS shift is immediate; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1, Network +1, Ghost −1: submitter-bounded. No direct PS shift in portrait fields | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone; restriction checks presence in target district ✓ | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken — restriction check (Art 02a §6); faction native × 1 cost (Art 02a §8) | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Beat 4; restriction at Beat 0 | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P07 = Card(
    id="P07",  version="v1.0",
    name    = "Public Address",
    tagline = "Rally public support in a district where you operate.",
    type    = PoliticalAct,  subtype = Standard,  faction = All,

    layer    = Standing,  function = Shift,  subject = PublicStanding,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

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
    design_note  = "Self-directed PS building — the missing card type in the standard set. P04 attacks opponent PS; P07 builds own. Automatic, 1 native, +2 PS. Presence requirement: cannot claim standing in districts where you have no legitimacy. Directorate +1 and Network +1: institutional communication and broadcasting are doctrinal for both. Ghost −1: public address = attention = exposure risk.",
    arbiter_note = "Beat 4. Restriction at Beat 0: acting faction must have at least 1 presence token in declared district. If restriction fails, PA voided. On success: acting faction +2 PS.",
)
```

---

### P08 — TABLE AN ACCORD
[↑ Public Acts](#standard-public-acts)

#### Design Rationale
The formal bilateral agreement mechanism of the standard set. Persistence = Seasonal: the card (or an AccordOffer marker) stays on the table from Beat 4 through Debrief, visible to all players. The offer cannot be taken back. Target accepts or declines at Debrief — a public decision with PS consequences either way. Directorate affinity only (Syndicate affinity removed: Syndicate manipulates Accords through C-S3 and faction-specific cards, not by proposing them publicly as a general instrument). Ghost portrait −1: Accords are commitments, which Ghost avoids structurally.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal accord proposals are a core political act — every faction can and does make bilateral agreements | Art 00 §7 |
| Voice fit | ✓ | All five perspectives distinct: Guild's pragmatic/permanence framing, Directorate's institutional mechanism preference, Network's record-and-observe stance, Ghost's obligation-aversion (not value-aversion), Syndicate's asset/exit-cost calculus | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate affinity (−1 cost) + portrait +1: bilateral stability is Directorate institutional doctrine. Ghost −1: Accords create commitments. Syndicate affinity removed — Syndicate manipulates Accords through faction-specific cards, not standard proposals. doctrine_mod not applicable | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / Standard — BilateralAgreement outcome type | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Add / AccordAgreement | Art 04b §4 |
| Balance | ✓ | Cost 2 native (Directorate −1). PS consequences for both accept and refusal outcomes. AccordCard created only on acceptance — open question: what are AccordCard terms? Art 06 pending | Art 02a §6–§7 |
| Effect duration | ✓ | AccordOffer marker persists as Seasonal (through Debrief — within-Quarter per 00-R21). AccordCard lifecycle governed by Art 06 (pending). No multi-Quarter temporary for the offer marker itself | 00-R21; Art 06 |
| Persistence | ✓ | Seasonal — AccordOffer marker stays through Debrief; removed after accept/decline. Correct for BilateralAgreement resolution at Debrief | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1, Ghost −1: submitter-bounded. No PS shifts in portrait fields | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no zone reference. N/A | Art 01 §6–§7 |
| Supported by components | ⚠ | AccordOffer marker placed on table — component not yet defined in Art 02a. AccordCard on acceptance governed by Art 06 (pending) | Art 02a §6–§8; Art 06 |
| Supported by game procedure | ⚠ | Beat 4 placement; Debrief acceptance/refusal. AccordCard terms and lifecycle governed by Art 06 (pending) | Art 03 §11, §19; Art 06 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
P08 = Card(
    id="P08",  version="v1.0",
    name    = "Table an Accord",
    tagline = "Formally propose a binding agreement with another faction, placed on the public record.",
    type    = PoliticalAct,  subtype = Standard,  faction = All,

    layer    = Economy,  function = Add,  subject = AccordAgreement,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = BilateralAgreement,
    persistence     = Seasonal,  # AccordOffer marker stays through Debrief; removed after accept/decline

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    affinity    = faction(acting) == Directorate: cost.faction(native) -= 1,
    restriction = (
        target_faction != faction(acting) and
        accord(faction(acting), faction(target)).active == False
    ),
    cost = resource.faction(acting) * 2,

    success = arbiter.place(AccordOffer(terms=declared, proposer=faction(acting), target=target_faction)),
    # P08 card persists on table as AccordOffer marker until Debrief (Seasonal)

    # BilateralAgreement resolution at Debrief:
    # on_accept: arbiter.create(AccordCard); faction(acting).standing += 1; faction(target).standing += 1
    # on_decline: faction(target).standing -= 1; faction(acting).standing += 1
    # AccordOffer marker removed after Debrief resolution

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
    design_note  = "Accord creation PA. Directorate affinity only (−1 cost). Persistence = Seasonal: P08 card or AccordOffer marker stays on table from Beat 4 through Debrief. Terms declared publicly at Phase B — cannot be retracted. AccordCard created on acceptance; both parties +1 PS. On decline: target −1 PS, proposer +1 PS. Ghost −1: Accords are commitments. Art 06 governs AccordCard terms and lifecycle.",
    arbiter_note = "Phase B: terms declared publicly. Beat 4: place AccordOffer marker (or leave P08 card) on table with terms visible. Card persists until Debrief. At Debrief: target faction publicly accepts or declines. On accept: create AccordCard (terms per Art 06); both +1 PS. On decline: target −1 PS, proposer +1 PS. Remove AccordOffer marker after resolution.",
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
| [C11](#c11-fortify-structure) | Fortify Structure |
| [C12](#c12-materials-acquisition) | Materials Acquisition |
| [C13](#c13-foundation-rights) | Foundation Rights |
| [C14](#c14-construction-crew) | Construction Crew |
| [C15](#c15-infrastructure-yield) | Infrastructure Yield |
| [—](#guild-labor-contract) | Labor Contract |

### C11 — FORTIFY STRUCTURE
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive structural defense card. The hardest counter to C02 Demolish in the set — not a threshold reduction (C10 Protect) but total immunity. Cost vs reward: 1 Capacity is relatively cheap for full immunity; the Beat 2 commitment is the real cost, since you're betting a slot that your structure will be targeted this round. Guild's structural investment is its primary territorial asset; this card formalizes that the Guild defends what it has built.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Structural reinforcement as covert preparation — fortification work is done quietly before Beat 3 resolution window. Guild-exclusive competency; no other faction has the structural standing to claim total demolition immunity. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | "The Guild does not abandon what it has built" is the doctrine statement. Network's "what's inside them" is the sharpest counter-perspective. Three perspectives only (Guild, Network, Directorate) — FactionSpecific card; Ghost and Syndicate absence acceptable. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild-exclusive card; structural defense is core Guild doctrine. Portrait submitter=+1 captures this. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: fortification is covert prep. FactionSpecific (Guild): total immunity is Guild's unique structural competency, not available to others. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Territory` — per Art 04b §4.6, Protect distributes to target's layer; target is StructureBlock (Territory). `function = Protect`, `subject = StructureBlock` — correctly scoped. | Art 04b §4.6, §5 |
| Balance | ✓ | Beat 2 positional wager; wrong-read wastes slot. 1 Capacity cost. Immunity is total but Quarter-limited; one play protects one structure only. | Art 02a §7, §8 |
| Effect duration | ✓ | Quarter-limited: immune flag persists until end of Quarter. Appropriate for a structural defense card. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (P11). Submitter-scoped (P12). Single entry (P13). Guild's structural-investment doctrine grounds the affinity. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: Guild structure in target district. | Art 01 §6, §7 |
| Supported by components | ✓ | StructureBlock (restriction + immunity target); Capacity cost. | Art 02a §7, §8 |
| Supported by game procedure | ⚠ | Submitted at Dispatch (§9); Beat 2 row (§11 Beat 0); immunity flag applied at Beat 3 when C02 Demolish resolves (§11 Beat 3). **Open:** §11 Beat 2 covers Countermeasures and Protect only — no procedure defined for Fortify Structure immunity flag. Gap in Art 03. | Art 03 §9, §11 |

#### Outstanding Issues

- **Art 03 §11 procedure gap:** §11 Beat 2 section does not include a procedure for applying the Fortify Structure immunity flag. Extension required before C11 can be fully procedurally supported.
- **Arbiter note:** ARBITER retains awareness after Beat 2 opens. Immunity applied when C02 Demolish resolves in Beat 3. Verify §11 Beat 2 extension covers this step.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
C11 = Card(
    id      = 11,  version = "v1.1",
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

    target_district = district.any,
    target_faction  = None,
    target_object   = StructureBlock,

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

### C12 — MATERIALS ACQUISITION
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive economic counter to demolition — not a defense card but a revenue card. The Guild names a target faction at submission, betting a Beat 2 slot that this faction will execute C02 this Quarter. Cost vs reward: zero resource cost; the action slot itself is the bet. Success mirrors C02's cost exactly (1 native + 1 district native) — intentionally self-calibrating; if C02's cost changes in playtesting, C12's reward scales automatically. A wrong read wastes the slot with no other loss.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Positioning to recover demolition costs before demolition happens — uniquely Guild, fits the game's economic-intelligence frame. Beat 2 commitment watching for opponent's Beat 3 action is a clean trigger structure. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Three perspectives (Guild, Syndicate, Ghost) — FactionSpecific card; acceptable. Syndicate's "we simply call it by a different name" and Ghost's "already told us what it knows" both provide doctrinal depth. | Art 00 §7 |
| Doctrine alignment | ✓ | `target_faction = faction.opponent`, `doctrine_mod = None` — explicit design choice. Recovery amount mirrors C02's cost regardless of doctrinal distance; the Guild gets paid the same whoever demolished. Correct. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: observation and positioning is covert; payment materializes via case mechanism. FactionSpecific (Guild): treating demolition as a Guild service is uniquely Guild doctrine. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Economy` — recovering NativeResource is capital flow, correctly Economy under Art 04b §4.4. `function = Recover`, `subject = NativeResource` — correctly scoped. | Art 04b §4, §5 |
| Balance | ✓ | Zero resource cost; action slot is the only cost. Trigger-contingent — wrong read wastes slot with no other penalty. First qualifying Demolish from named faction only. | Art 02a §8 |
| Effect duration | ✓ | Instantaneous: resources delivered once when trigger fires. No persistent state. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = faction(target).completes(CovertOp, id=C02)` — well-defined; ARBITER confirms at Beat 3. Note: `id=C02` uses variable name, not integer — update to `id=2` when DB integers assigned (non-material; carry). | Art 04 (C02) |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (P11). Submitter-scoped (P12). Single entry (P13). | Art 04 §6.2 |
| Supported by zones | N/A | `target_district = None` — trigger monitors named opponent globally, not district-specific. | — |
| Supported by components | ✓ | NativeResource (Art 02a §8); C02 Demolish as trigger source. | Art 02a §8; Art 04 (C02) |
| Supported by game procedure | ✓ | Submitted at Dispatch (§9); placed in Beat 2 row (§11 Beat 0); trigger fires when named faction completes C02 at Beat 3 (§11 Beat 3); delivery via ARBITER case (Art 07). | Art 03 §9, §11; Art 07 |

#### Outstanding Issues

- **Arbiter note:** ARBITER confirms trigger at Beat 3. Only the first qualifying Demolish from the named faction this Quarter triggers. Effect delivered in case.
- **Trigger notation (non-material):** `id=C02` is a variable name reference. Update to `id=2` when DB integers are assigned.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
C12 = Card(
    id      = 12,  version = "v1.1",
    name    = "Materials Acquisition",
    tagline = "Recover the costs of demolition as subcontract payment.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Economy,  function = Recover,  subject = NativeResource,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = faction(target).completes(CovertOp, id=C02),
    resolution_type = "Positional wager",
    outcome_type    = None,
    persistence     = Immediate,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = NativeResource,

    affinity    = None,
    restriction = None,
    cost        = None,

    success     = (
        faction(acting).resource.native += 1,
        faction(acting).resource.native += 1   # mirrors C02.cost: 1 faction native + 1 district native
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

### C13 — FOUNDATION RIGHTS
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive first-entry card for unclaimed districts. Unclaimed territory has no established resource infrastructure, hence Capacity-only cost. Threshold 25 reflects genuine first-mover difficulty — unclaimed territory resists entry even for the faction with the deepest historical claim. Crit success upgrades presence to presence+structure (immediate foothold). Crit fail is politically the most sensitive outcome: a failed foundation claim is a regulatory event, and the Directorate receives an Intel Token silently. Guild never knows the paper trail was created.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | First-entry territorial claim as covert operation — unannounced land assertion fits Guild's historical-precedence doctrine. The Directorate's jurisdictional counter makes the doctrinal tension mechanical rather than just narrative. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | "The Guild was here before the city had a name" is the doctrine statement. Three perspectives (Guild, Network, Directorate) — FactionSpecific card; acceptable. Directorate's "legal process, not archive" is the sharpest counter. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild territorial-precedence doctrine (first-mover claim). Crit fail delivers Intel Token to Directorate — Directorate's regulatory oversight role is doctrinal, not incidental. Guild portrait submitter=+1 captures alignment. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Guild) — unannounced territorial claim. Covert until established. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Territory` — placing first presence is a territorial operation. `function = Add`, `subject = PresenceToken` — correctly scoped. Crit success adds StructureBlock (stacks with success; same layer). | Art 04b §4, §5 |
| Balance | ⚠ | Threshold 25 + ring_mod {0: −15} = effective threshold 10 in Ring 0. **Open:** Near-automatic for unclaimed Ring 0 districts — should first-entry be that easy? Consider raising base to 35–40. Crit success (presence + structure simultaneously) is a significant leap; confirm intent. | Art 01 §7; Art 02a §6, §7 |
| Effect duration | ✓ | Permanent: presence and structure persist until removed. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (P11). Submitter-scoped (P12). Single entry (P13). `failcrit` dispatches IntelToken to Directorate — game effect, not Portrait shift (P12 clear). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: total presence == 0 (unclaimed only). | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken (success); StructureBlock (crit success); Capacity cost; IntelToken to Directorate on crit fail. | Art 02a §6, §7, §8; Art 02b §8 |
| Supported by game procedure | ✓ | Submitted at Dispatch (§9); Beat 3 row (§11 Beat 0); d100 threshold 25 with ring_mod; ARBITER silent IntelToken delivery to Directorate on crit fail (§11 Beat 3; Art 07). | Art 03 §9, §11; Art 07 |

#### Outstanding Issues

- **Balance — Ring 0 threshold:** Effective threshold 10 in Ring 0 (25 − 15). Near-automatic for unclaimed city-center districts. Consider raising base threshold to 35–40. Confirm before v1.2.
- **Crit success design:** Success = presence only; crit success stacks +structure. Verify this is the intended "presence + structure" foothold, not just structure replacing presence.
- **Arbiter note:** On crit fail: deliver 1 Intel Token naming Guild to Directorate via case. Do not notify Guild.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
C13 = Card(
    id      = 13,  version = "v1.1",
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

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

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

### C14 — CONSTRUCTION CREW
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive rush-construction card — bypasses C01's presence prerequisite at premium cost and elevated difficulty. Threshold 65 models that unauthorized construction (without prior presence) is significantly harder than licensed work. Cost: 3 Capacity vs C01's 1 faction native + 1 district native — a premium for skipping the prerequisite. Crit fail is deliberately multi-faction: failed unauthorized construction triggers both Ghost surveillance and Syndicate resource extraction — the city's two most opportunistic actors benefit from the Guild's overreach.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Rush construction without prior presence — unauthorized build is covert, high-risk, and distinctly Guild. Ghost and Syndicate as crit-fail beneficiaries is doctrinally perfect (the two most opportunistic actors). | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Three perspectives (Guild, Network, Ghost) — FactionSpecific card; acceptable. Ghost's "better at covert operations than they admit" is the sharpest outside read. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild construction doctrine (rush, without permission). Crit fail rewards Ghost (Intel Token) and Syndicate (district native) — explicitly doctrinal: the two most opportunistic actors benefit from Guild overreach. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: unauthorized construction is covert until established. FactionSpecific (Guild): rush-build without prerequisites is exclusively Guild. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Submission` — primary design intent is removing the C01 presence prerequisite (a restriction on a CovertOperation). Territorial outcomes (presence + structure) are the consequence, not the driver. `function = RemoveRestriction`, `subject = CovertOperation` — correctly scoped per design intent. | Art 04b §4, §5 |
| Balance | ✓ | High cost (3 Capacity), high threshold (65). Crit fail rewards both Ghost (Intel Token) and Syndicate (district native) — asymmetric penalty for overreach. Net: saves C03+C01 sequential plays at the cost of one high-risk probabilistic slot. | Art 02a §6, §7, §8; Art 02b §8 |
| Effect duration | ✓ | Permanent: presence and structure placed on success persist. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (P11). Submitter-scoped (P12). Single entry (P13). `failcrit` delivers IntelToken/native to opponents — game effects, not Portrait shifts (P12 clear). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: no existing Guild structure in target district. Ring mods apply normally. | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken + StructureBlock on success; Capacity cost; IntelToken to Ghost + district native to Syndicate on crit fail. | Art 02a §6, §7, §8; Art 02b §8 |
| Supported by game procedure | ✓ | Submitted at Dispatch (§9); Beat 3 row (§11 Beat 0); d100 threshold 65 with ring_mod; ARBITER delivers crit fail rewards to Ghost and Syndicate (§11 Beat 3; Art 07). | Art 03 §9, §11; Art 07 |

#### Outstanding Issues

- **Arbiter note:** Crit fail: deliver 1 Guild Intel Token → Ghost and 1 district native → Syndicate via case. Do not notify Guild.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
C14 = Card(
    id      = 14,  version = "v1.1",
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

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    affinity    = None,
    restriction = district(target).faction(acting).structure == 0,
    cost        = resource.faction(acting).capacity * 3,

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
)
```

---

### C15 — INFRASTRUCTURE YIELD
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive passive income card — the economic expression of territorial control. Zero cost reflects that drawing from established infrastructure is not a new expenditure; it is the return on prior investment. The sole gate (Established or Dominant control tier) makes this card valuable precisely because it rewards maintained territorial control. Counter-lever is territorial: the card becomes unplayable if the Guild loses control tier, creating natural interdependence with C01/C03.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Passive income from controlled infrastructure is the natural economic expression of Guild territorial control. Covert framing (yield not publicly attributed) fits the operations register. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Three perspectives (Guild, Syndicate, Directorate) — FactionSpecific card; acceptable. Syndicate's "billing us for the water" is the sharpest outside read. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild infrastructure-ownership doctrine — return on prior investment. Guild↔Syndicate are Opposed: Syndicate believes it should capture this yield, not the Guild ("billing us for the water"). No opponent target → doctrine_mod N/A; Syndicate portrait entry warrants consideration (see Portrait validity). | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: yield is not publicly attributed. FactionSpecific (Guild): infrastructure-ownership income is exclusively Guild. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Economy` — adding NativeResource is capital flow, correctly Economy under Art 04b §4.4. `function = Add`, `subject = NativeResource` — correctly scoped. | Art 04b §4, §5 |
| Balance | ⚠ | Zero cost + Automatic + no fail state + repeatable each Quarter. **Open:** Multiple Established/Dominant districts → multiple free native resources per Quarter, uncapped. Consider per-Quarter activation cap (e.g., max 2). Flag for playtesting. | Art 02a §6, §8 |
| Effect duration | ✓ | Instantaneous: +1 native delivered per play. No persistent state; card is re-playable each Quarter if restriction still met. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (P11). Submitter-scoped (P12). Single entry (P13). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: Guild must hold Established or Dominant control tier in target district. | Art 01 §6, §7 |
| Supported by components | ✓ | NativeResource (Art 02a §8); control_tier states Established/Dominant (Art 02a §6). | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Submitted at Dispatch (§9); Beat 3 row (§11 Beat 0); Automatic resolution at Beat 3 (§11 Beat 3). | Art 03 §9, §11 |

#### Outstanding Issues

- **Balance — per-Quarter cap:** Zero cost + Automatic means uncapped income at scale. Guild controlling 3+ Established/Dominant districts earns 3+ free native resources per Quarter. Consider cap of 2 activations per Quarter; flag for playtesting.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
C15 = Card(
    id      = 15,  version = "v1.1",
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

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

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
Construction analogue to C12 Materials Acquisition — C12 covers demolition revenue, Labor Contract covers construction revenue. Together they implement the Guild doctrine that no structural change to New Meridian happens without Guild being paid. Beat 2 positional wager: Guild names a faction and bets an action slot on that faction building this Quarter. Zero resource cost means a wrong read loses only the slot. Payout mirrors C01's cost (2 Capacity), making the card self-calibrating if C01's cost changes in playtesting.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Construction fee mechanic — Guild monetises any faction's C01 play; analogue to C12 Materials Acquisition (demolition revenue) completing the Guild doctrine that no structural change to New Meridian happens without Guild payment | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; limited perspectives in current spec — full voice set expected (confirm complete in code block) | Art 00 §7 |
| Doctrine alignment | ✓ | Guild only; zero resource cost (slot IS the bet); payout 2 Capacity mirrors C01.cost — self-calibrating on balance pass; Beat 2 positional wager fits the "bet on opponent building" play style | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Guild) — Guild's passive revenue model | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Recover/NativeResource — Recover returns resources based on triggered event; C03 exclusion confirmed locked S59 | Art 04b §4, §5 |
| Balance | ✓ | Payout 2 Capacity mirrors C01.cost — self-calibrating | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: Capacity delivered at Beat 3 when trigger fires | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | Trigger = C01 completion by named faction; first qualifying play only; Beat 2 positional wager monitors trigger across the round | Art 04 (C01) |
| Portrait validity | ✓ | Confirm portrait entries present in code block — Guild faction-specific expected | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None; trigger monitors named faction globally | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource (Capacity); C01 as trigger source; no new components | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 2 submission; trigger confirmed at Beat 3; ARBITER case delivery | Art 03 §9, §11 |

#### Outstanding Issues

- **C03 scope confirmed excluded:** Labor Contract is a financial claim on physical construction (C01) only. Campaign (C03) does not trigger — no labor fee on presence/influence activity. Locked S59.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Draft S59 — design pass pending*

```python
Card(
    id=TBD,  version="v1.0",  # ID pending PM05 04-n1
    name    = "Labor Contract",
    tagline = "Collect subcontract payment when a faction develops district infrastructure.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Economy,  function = Recover,  subject = NativeResource,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = faction(target).completes(CovertOp, id=C01),
    resolution_type = "Positional wager",
    outcome_type    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = NativeResource,

    affinity    = None,
    restriction = None,
    cost        = None,

    success     = (
        faction(acting).resource.native += 1,
        faction(acting).resource.native += 1,  # mirrors C01.cost: 1 faction native + 1 district native
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
    design_note  = "Construction analogue to C12 Materials Acquisition. Together with C12 and 04-n2 passive rule: no faction demolishes or builds in New Meridian without Guild being paid. Trigger is C01 only — Labor Contract is a financial claim on physical construction, not influence or presence activity. Payout mirrors C01.cost (2 Capacity). First qualifying C01 from named faction only.",
    arbiter_note = "At Beat 3: confirm whether named faction completed C01 this Quarter. First qualifying play only. If triggered: deliver 2 Capacity to Guild's Dispatch Case.",
)
```

---


---

### Guild — Public Acts
[↑ Guild](#guild)

| Card | Name |
|------|------|
| [P09](#p09-civic-works-mandate) | Civic Works Mandate |
| [P10](#p10-infrastructure-bond) | Infrastructure Bond |

### P09 — CIVIC WORKS MANDATE
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
Guild's prestige structure PA — a simultaneous double build in two named districts. One PA slot for two structures is the core value; the cost premium (4 Capacity vs two sequential P03s at 2 Capacity each using two PA slots across two Months) reflects the single-slot efficiency gain. Guild's faction affinity waives both district native costs. The PS reward (+3) is the highest of any standard or faction-specific single build card, reflecting the scale of the public commitment. Primary counter: Directorate's P11 (Regulatory Override) raises the cost of presence prerequisites; P11 (Issue Directive in prior design, now Regulatory Override) can be deployed against the district beforehand.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Simultaneous dual construction is Guild's maximum public commitment | Art 00 §7 |
| Voice fit | ✓ | Guild on-doctrine; Network (aligned): public commitment scale; Ghost (opposed): acting before the question is answered | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Guild-exclusive: 4 Capacity cost, district native waived for both districts, portrait +2 (double structure = doctrinal maximum). Directly serves permanence doctrine. No target_faction → doctrine_mod not applicable | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / StructureBlock — two targets | Art 04b §4 |
| Balance | ⚠ | Cost 4 Capacity; both district natives waived (Guild). PS +3. Single slot for two structures is efficient — balance review after playtesting | Art 02a §6–§7 |
| Effect duration | ✓ | StructureBlocks = Permanent board state; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Guild +2: submitter-bounded; double structure = maximum doctrinal expression | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.two — both named districts valid; restriction checks each independently | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock (Art 02a §7); PresenceToken — restriction (Art 02a §6); 4 Capacity — Guild faction native (Art 02a §8) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Both districts declared at Phase B; restriction checked at Beat 0; both-or-nothing rule | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
P09 = Card(
    id="P09",  version="v1.0",
    name    = "Civic Works Mandate",
    tagline = "Declare a public infrastructure program across two districts simultaneously.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Guild,

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

    target_district = district.two,  # both named at Phase B
    target_faction  = None,
    target_object   = None,

    affinity    = faction(Guild): cost.resource.district(native) = 0,  # waived for both districts
    restriction = (
        district(target1).faction(Guild).presence > 0 and
        district(target2).faction(Guild).presence > 0 and
        district(target1).faction(Guild).structure == 0 and
        district(target2).faction(Guild).structure == 0
    ),
    cost = resource.faction(Guild) * 4,

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
    design_note  = "Guild's prestige build PA. 4 Capacity (district native waived for both). Both-or-nothing: if either district fails restriction at Beat 0, full PA is voided. PS +3: highest single-card build reward. Portrait +2: double structure = doctrinal maximum. Counter: Directorate P11 Regulatory Override applied to either district beforehand raises presence-placement costs, potentially blocking prerequisite presence for this card.",
    arbiter_note = "Phase B: two distinct districts named. Beat 0: both restrictions checked simultaneously. If either fails (no Guild presence, or existing structure), entire PA voided; 4 Capacity returned; Guild takes Public Pass. Beat 4: place 1 structure in each declared district; Guild +3 PS.",
)
```

---

### P10 — INFRASTRUCTURE BOND
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
Guild's economic relationship PA. Distinct from C09 (Fund) in cost currency (Capacity vs Capital) and mechanism (AccordCard with ongoing income terms vs one-time payment). Guild invests 2 Capacity upfront and delivers 2 native resources to the target faction immediately. In return, an AccordCard is created with ongoing income terms (target pays Guild 1 Capacity per Upkeep while Accord active) — Guild recovers the initial cost over 2 rounds, then profits. This makes P10 a medium-horizon investment rather than a gift. Addresses 04-n11 (Guild↔Network neighbor cooperation): doctrine_mod noted for narrative tracking; Network is the natural partner given pentagram proximity.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Guild public investment in another faction's territory is narratively grounded — infrastructure serves both | Art 00 §7 |
| Voice fit | ✓ | Guild on-doctrine; Directorate (aligned): structural partnership recognition; Syndicate (opposed): extraction reframed as partnership | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Guild investment economy: 2 Capacity upfront, 1 Capacity/Upkeep return. Restriction (Guild Established adjacent) keeps it doctrinally grounded. Portrait +1. Addresses 04-n11 (Guild↔Network neighbor cooperation) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Add / AccordAgreement — the Accord is the primary artifact; resource delivery is the trigger | Art 04b §4 |
| Balance | ⚠ | Cost 2 Capacity + 2 native delivered; income 1 Capacity/Upkeep. Net positive over 2+ Quarters. Accord terms need Art 06 confirmation | Art 02a §6–§7 |
| Effect duration | ✓ | Resource delivery immediate; AccordCard income within-Quarter per Upkeep (00-R21). AccordOffer marker Seasonal through Debrief within same Quarter | 00-R21; Art 06 |
| Persistence | ✓ | Seasonal — AccordOffer marker stays through Debrief; removed after accept/decline | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Guild +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; restriction uses Guild Established adjacency to target's presence (valid zone-based check) | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource (target delivery, Art 02a §8); AccordOffer marker, AccordCard (Art 06 pending); Capacity × 2 cost (Art 02a §8) | Art 02a §8; Art 06 |
| Supported by game procedure | ⚠ | Upkeep income from Accord requires Art 06 Accord lifecycle definition and Upkeep procedure confirmation | Art 03 §19; Art 06 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
P10 = Card(
    id="P10",  version="v1.0",
    name    = "Infrastructure Bond",
    tagline = "Publicly extend Guild infrastructure investment to another faction, establishing a formal economic relationship.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Economy,  function = Add,  subject = AccordAgreement,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,  # Neighbor relationship noted for narrative — no threshold variance (Automatic)
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = BilateralAgreement,
    persistence     = Seasonal,  # AccordOffer marker stays through Debrief

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    affinity    = None,
    restriction = faction(Guild).influence_tier(district.any_adjacent_to(faction(target).presence)) >= Established,
    cost        = resource.faction(Guild) * 2,  # 2 Capacity

    success = (
        faction(target).resource(native) += 2,  # immediate delivery
        arbiter.place(AccordOffer(
            terms  = "Infrastructure Bond: target faction pays Guild 1 Capacity at each Upkeep while Accord active",
            proposer = Guild,  target = target_faction,
        )),
    ),

    # BilateralAgreement resolution at Debrief:
    # on_accept: arbiter.create(AccordCard(terms)); Guild.standing += 1; target.standing += 1
    # on_decline: Guild.standing += 1; target.standing -= 1

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
    design_note  = "Guild economic relationship PA. 2 Capacity cost; 2 native delivered to target immediately (good-faith investment). AccordCard on acceptance with ongoing income (1 Capacity/Upkeep from target). Net positive for Guild over 2+ rounds. Restriction: Guild must have Established adjacent to target's operations. Distinct from C09 Fund (Capital, one-time, no income return). Addresses 04-n11 (Guild↔Network neighbor cooperation); Network is natural target given pentagram proximity.",
    arbiter_note = "Phase B: target faction named. Beat 4: deliver 2 native resources to target immediately. Place AccordOffer on table (persistent through Debrief). On acceptance: create AccordCard; Guild +1 PS, target +1 PS. Track Accord income: at each Upkeep Step 6 while Accord active, target pays Guild 1 Capacity. On decline: Guild +1 PS, target −1 PS.",
)
```

---


---

## Ghost
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#ghost-covert-operations) · [Public Acts](#ghost-public-acts)

---

### Ghost — Covert Operations
[↑ Ghost](#ghost)

| Card | Name |
|------|------|
| [C16](#c16-pattern-match) | Pattern Match |
| [C17](#c17-intercept) | Intercept |
| [C18](#c18-dossier-breach) | Dossier Breach |
| [C19](#c19-deep-cover) | Deep Cover |
| [C20](#c20-misdirection) | Misdirection |
| [—](#ghost-station) | Station |
| [—](#ghost-full-take) | Full Take |
| [—](#ghost-scif) | SCIF |
| [—](#ghost-flip) | Flip |
| [—](#ghost-signals-analysis) | Signals Analysis |
| [—](#ghost-synthesize) | Synthesize |
| [—](#ghost-source-substitution) | Source Substitution |
| [—](#ghost-backdate) | Backdate |
| [—](#ghost-field-verification) | Field Verification |

### C16 — PATTERN MATCH
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost-exclusive intelligence-into-action card — the only card with Prediction resolution in the set. No roll; success is structural (correct prediction on faction OR district — either match is sufficient). Rewards moderate intelligence rather than perfect intelligence. Cost vs reward: 2 Findings to copy a covert operation worth whatever that operation costs — asymmetric upside if the copied op is expensive. Portrait modifier on success (+1 PS on crit) reflects the Ghost doctrine that intelligence is vindicated by successful prediction, not by gathering alone.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pattern-matching intelligence into executed action — Ghost's prediction mechanic makes intelligence operationally consequential rather than purely informational. Fits Ghost doctrine: understanding precedes action. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | "We are not predicting. We are recognising a pattern we have already seen." — Ghost's core intelligence-vs-prediction distinction. Only one perspective (Ghost only) — unusually minimal even for FactionSpecific; consider adding 1–2 outside readings in a future pass. | Art 00 §7 |
| Doctrine alignment | ✓ | `target_faction = faction.opponent`, `doctrine_mod = None` — explicit design choice: prediction accuracy is about intelligence quality, not doctrinal proximity to the target faction. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: prediction and operation-copying is covert intelligence work. FactionSpecific (Ghost): Prediction resolution is Ghost's unique mechanism. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Submission` — copying an opponent's operation modifies what enters Ghost's resolution queue. `function = Copy`, `subject = CovertOperation` — correctly scoped. | Art 04b §4, §5 |
| Balance | ⚠ | **Open:** Does Ghost pay the copied op's cost? Option C (fizzle if Ghost cannot supply) recommended. Without this constraint, Ghost can copy expensive ops at marginal 2-Findings cost. | Art 02a §8 |
| Effect duration | ✓ | One-time execution of the copied operation; no persistent state. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` — Prediction resolution verified by ARBITER at Beat 3. | — |
| Portrait validity | ✓ | Ghost `submitter=+1, modifier=+1, mod_where=game.outcome == Success`. `submitter=+1` fires on play (P11). Submitter-scoped (P12). Single entry (P13). **Open:** `modifier=+1` AND/OR semantics — confirm `submitter` always fires on play AND `modifier` additionally fires on Success (not independent of submitter activation). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. No presence restriction — Ghost intelligence operations unrestricted by zone. | Art 01 §6 |
| Supported by components | ✓ | Findings cost (Art 02a §8); CovertOperation as copy target; copied op's components governed by that op's spec. | Art 02a §8; Art 04b §5 |
| Supported by game procedure | ⚠ | Submitted at Dispatch (§9); Beat 3 row (§11 Beat 0). **Open:** Prediction resolution not defined in Art 03 — §11 covers Automatic and d100 only. Procedure gap: Art 03 extension required for Prediction resolution type. | Art 03 §9, §11 |

#### Outstanding Issues

- **Copied op cost (design decision):** Does Ghost pay the copied operation's cost? Options: (A) free, (B) pay equivalent, (C) fizzle if Ghost cannot supply. Option C recommended — confirm before v1.1.
- **Portrait `mod_where=` semantics:** `modifier=+1, mod_where=game.outcome == Success` — confirm AND semantics: `submitter` always fires on play; `modifier` fires additionally on Success. Confirm OR is not intended.
- **Art 03 Prediction procedure gap:** Art 03 §11 covers Automatic and d100 only. Prediction resolution requires a procedure extension before C16 can be fully procedurally supported.
- **Arbiter note:** If the copied operation cannot legally be executed by Ghost, Pattern Match fizzles — 2 Findings spent, no effect regardless of prediction accuracy.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
C16 = Card(
    id      = 16,  version = "v1.0",
    name    = "Pattern Match",
    tagline = "Identify a faction's operation and location before they move.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Submission,  function = Copy,  subject = CovertOperation,

    beat            = 3,
    resolution      = Prediction,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Predictive",
    outcome_type    = None,
    persistence     = Immediate,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = CovertOperation,

    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).findings * 2,

    success     = game.copy_op(faction(target).op(beat=3, type=CovertOperation)),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1, modifier=+1, mod_where=game.outcome == Success)},

    narrative    = "Ghost does not guess. Ghost identifies what is already in motion.",
    perspectives = {
        Ghost: "We are not predicting. We are recognising a pattern we have already seen.",
    },
)
```

---

### C17 — INTERCEPT
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost-exclusive active-surveillance card — distinguishes from C18 Dossier Breach by targeting submitted operations, not hand contents. Intel Token cost consumed at submission regardless of outcome: you spend what you know to learn what they're doing. Cost structure (Intel Token + 2 Findings) reflects active operational depth — harder to execute than Gather, rewarded with real-time intelligence rather than historical data. Failure notifies the target; crit fail triggers a silent PS loss (recorded internally by ARBITER only).

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Active surveillance of submitted operations — direct expression of Ghost's real-time intelligence doctrine. Distinct from C05 Gather (historical intel) and C18 Dossier Breach (hand contents). | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | One perspective (Ghost only) — FactionSpecific; acceptable. "We do not wait for the after-action report." Ghost's active-vs-passive intelligence distinction is clear. | Art 00 §7 |
| Doctrine alignment | ✓ | `target_faction = faction(named_opponent)`, `doctrine_mod = None` — explicit design choice: surveillance effectiveness is about intelligence quality, not doctrinal proximity. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: active surveillance is covert. FactionSpecific (Ghost): real-time operational intel is Ghost's exclusive capability. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Information` — revealing the content of a submitted operation is Information layer. `function = Reveal`, `subject = CovertOperation` — correctly scoped. | Art 04b §4, §5 |
| Balance | ✓ | Intel Token consumed at submission regardless of outcome — meaningful downside for failed surveillance. Double-resource cost (IntelToken + 2 Findings). Crit success stacks additional IntelToken on top of IntelDeliverySlip. | Art 02a §8; Art 02b §8 |
| Effect duration | ✓ | Instantaneous: IntelDeliverySlip delivered once at Beat 3 resolution; IntelToken on crit. No persistent state beyond the delivered token. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Ghost `submitter=+1`. Fires on submission (P11). Submitter-scoped (P12). Single entry (P13). `failcrit = standing -= 2` is a PS shift (not Portrait — P12 clear). Note: Design Rationale says "silent PS loss" — confirm with ARBITER procedure whether the −2 PS is announced at Beat 3 or recorded privately. | Art 04 §6.2; Art 02b §7 |
| Supported by zones | N/A | `target_district = None` — Intercept operates on submitted ops in the Resolution Grid, not a specific district. | — |
| Supported by components | ✓ | IntelToken cost; Findings cost; IntelDeliverySlip (success); IntelToken (crit success); NotificationSlip (fail); PS −2 (failcrit). | Art 02a §8; Art 02b §7, §8 |
| Supported by game procedure | ⚠ | Submitted at Dispatch (§9); Beat 3 row (§11 Beat 0); d100 threshold 50; ARBITER delivers via case (Art 07). **Open:** Art 03 procedure migration pending — §11 Beat 3 does not yet include the IntelDeliverySlip and silent-PS-loss steps. | Art 03 §9, §11; Art 07 |

#### Outstanding Issues

- **Art 03 procedure migration:** §11 Beat 3 does not yet include the Intercept delivery steps (IntelDeliverySlip, NotificationSlip, silent PS loss). Migration pending post-S52 Art 03 reorganization. Card design was signed off S49.
- **Failcrit PS "silent" question:** `failcrit = standing -= 2` is a PS shift — confirm whether ARBITER announces at Beat 3 or records internally only. PS is normally a public track.
- **Arbiter note:** Crit success: deliver IntelToken (faction=target) to acting faction's case. Success: write target faction's first submitted op type and district on Intel Delivery Slip; deliver to acting faction's case. Fail: deliver Notification Slip to target faction's case. Crit fail: PS −2 — record internally only (per Design Rationale).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S63 |

```python
C17 = Card(
    id=17,  version="v1.0",
    name    = "Intercept",
    tagline = "Surveil a faction's covert operations in real time.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Reveal,  subject = CovertOperation,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10}, doctrine_mod=None,
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    target_district=None, target_faction=faction(named_opponent), target_object=CovertOperation,
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

### C18 — DOSSIER BREACH
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Fills the Information — Reveal — CardHand gap: Ghost reads the opponent's planning pool before they play it. Distinct from C17 Intercept (targets submitted ops in the Resolution Grid) and C05 Gather (generates Intel tokens rather than revealing content). No Notification risk — card hand reveal is private to Ghost; ARBITER does not announce it. 2 Findings cost and Automatic resolution reflects that penetrating planning files is achievable but requires a meaningful resource commitment. Ghost Double-Case Pass creates natural synergy: Month 1 Breach informs Month 2 and 3 strategy.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Preemptive read of opponent's planning pool fills Information/Reveal/CardHandContents gap; distinct from C17 (submitted ops) and C05 (token yield) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — planning-pool penetration is Ghost-exclusive doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; no portrait entry (intelligence revelation carries no PS consequence — confirmed intentional per Ghost low-profile doctrine); Automatic resolution fits analytical intelligence work | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — deeper intelligence access than Standard C17 | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/CardHandContents — fills gap; component registration outstanding (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | 2 Findings, Automatic — information advantage without dice risk; Automatic justified for analytical work; different information class from C17 (planning vs. attribution) | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: private reveal once at Beat 3; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | No portrait entry — intelligence work carries no PS consequence by Ghost doctrine; absence confirmed intentional | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — operates on card hand; no district context required | Art 01 §6–§7 |
| Supported by components | ✓ | CardHandContents as target_object — component registration outstanding (Outstanding Issue); modifier cards excluded from reveal per arbiter_note | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Private reveal via ARBITER; private faction-to-faction reveal procedure outstanding (Outstanding Issue) | Art 03 §9, §11; Art 07 |

#### Outstanding Issues

- **CardHandContents as component type:** Confirm `target_object = CardHandContents` is registered or flagged for Art 02 registration.
- **Private reveal procedure:** Same mechanism as C17 IntelDeliverySlip? Confirm Art 07 covers faction-to-faction private reveals via ARBITER.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*S51 redesign — design pass pending*

```python
C18 = Card(
    id=18,  version="v1.0",
    name    = "Dossier Breach",
    tagline = "Penetrate a faction's operational planning before the round begins.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Reveal,  subject = CardHandContents,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=None, target_faction=faction(named_opponent), target_object=CardHand,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).findings * 2,
    success     = game.reveal(faction(target).hand(types=[CovertOperation, PoliticalAct]), to=faction(acting), private=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Ghost: PortraitEntry(submitter=+1)},
    narrative   = "Understanding the operation before it begins. That is the only tactical advantage worth having.",
    perspectives = {Ghost: "We did not take their cards. We simply read their intentions. They will act on plans we already know."},
    design_note  = "Replaces C18 Identity Blind (retired S51). Fills Information — Reveal — Card hand gap; distinct from C17 Intercept (submitted ops) — Dossier Breach targets the unplayed planning pool. Ghost Double Case Pass creates natural synergy: Month 1 Breach informs Month 2 and Month 3 Declaration strategy.",
    arbiter_note = "Privately show target faction's current hand of Covert and Public Act cards to Ghost player. Modifier cards excluded. Do not confirm or announce to the table. Information is solely between Ghost and ARBITER — Ghost may not publicly announce or prove the contents.",
)
```

---

### C19 — DEEP COVER
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's operational security card — intelligence denial rather than intelligence collection. Permanently removes attribution from a prior Ghost operation, making it untraceably covert. Low cost (1 Finding) reflects that Ghost is tidying the record, not breaking new ground; the hard work was the original operation. The `prior_op` restriction ensures Deep Cover cannot be used preemptively — attribution must exist (and be Ghost's) for removal to fire. Permanent per Principle 11.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Operational security card — permanent attribution removal is Ghost's signature intelligence denial capability; distinct from C18 (reads plans) and C05 (gathers intel) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — concealment as doctrine, not tactic | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; 1 Finding cost reflects tidying the record, not new groundwork; prior_op restriction prevents preemptive use — attribution must exist first | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — permanent protection is Ghost-exclusive per Principle 11 | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Protect/ActionAttribution — permanent protection per Principle 11; Protect function correct | Art 04b §4, §5 |
| Balance | ✓ | 1 Finding, Automatic, permanent — low cost appropriate; restriction (must have prior attributed op) is the real gate; permanent effect justified by Ghost doctrine | Art 02a §6–§7 |
| Effect duration | ✓ | Permanent: attribution removal is irreversible per Principle 11 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces prior-op existence | — |
| Portrait validity | ✓ | No portrait entry — Ghost concealment doctrine: even performing Deep Cover leaves no doctrinal signal; absence confirmed intentional (Outstanding Issue) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — operates on action attribution record; no district context | Art 01 §6–§7 |
| Supported by components | ✓ | ActionAttribution as target_object — component registration outstanding (Outstanding Issue) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | ARBITER removes attribution permanently from record; procedure outstanding (Outstanding Issue) | Art 03 §9, §11; Art 07 |

#### Outstanding Issues

- **Empty portrait:** No portrait entry. Confirm intentional — Ghost concealment doctrine means even performing Deep Cover leaves no doctrinal signal.
- **ActionAttribution component:** `target_object = ActionAttribution` — confirm this is a defined component/record entity in Art 00b or Art 02.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*S51 redesign — design pass pending*

```python
C19 = Card(
    id=19,  version="v1.0",
    name    = "Deep Cover",
    tagline = "Permanently remove a prior operation from the accessible record.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Protect,  subject = ActionAttribution,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=None, target_faction=faction(acting), target_object=ActionAttribution,
    affinity=None,
    restriction = faction(acting).prior_op(min_rounds_ago=1, attributed=False).count >= 1,
    cost        = resource.faction(acting).findings * 1,
    success     = game.remove_attribution(faction(acting).op(prior=True, unattributed=True, named=True), permanent=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "Good cover does not expire at the end of the week.",
    perspectives = {Ghost: "It did not happen. This is not a lie. It is a permanent correction to an incomplete record."},
    design_note  = "Permanent attribution protection. Redesign flag resolved S51 — C18 replaced with Dossier Breach, making C19 the unique permanent-protection card in Ghost's set.",
    arbiter_note = None,
)
```

---

### C20 — MISDIRECTION
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Active deception — Ghost fabricates a self-directed Intel token and places it in an opponent's case. The false token is physically indistinguishable from a genuine Gather result; any Denounce built on it fails at resolution. Requires Ghost to hold a self-faction Intel token as the source material, meaning Ghost has previously gathered intelligence about their own operations to craft a believable false trail. 1 Finding cost, Automatic — the fabrication is simple once the source material exists; the difficulty is in having done the groundwork.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Active deception — Ghost fabricates a self-directed token and plants it in an opponent's case; fills Information/Add+Corrupt/IntelToken gap in Ghost's counter-intelligence toolkit | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — fabrication as operational doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; self-Intel token restriction means Ghost must have done prior groundwork; 1 Finding cost reflects fabrication is the easy part — having the source material is the hard part | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — fabrication is Ghost-exclusive; no Standard equivalent | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Add/IntelToken with false-content attribute — Add+corrupt-content vs Corrupt function outstanding (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | 1 Finding + self-Intel token — restriction is real gate (Ghost must hold self-directed token); false token creates downstream risk for recipient (wasted attribution play) | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: false token placed in target's case at Beat 3; no card-level lingering effect | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — deception operation aligns with Ghost intelligence manipulation doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — token delivered to target's case, not district-anchored | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken with content=false — false-content flag registration outstanding (Outstanding Issue); Ghost self-token cap exemption outstanding (Outstanding Issue) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | ARBITER delivers false token via case at Beat 3; token indistinguishable from real on inspection per design | Art 03 §9, §11; Art 07 |

#### Outstanding Issues

- **False-content IntelToken:** `IntelToken(faction=Ghost, content=false)` — confirm `content` flag is a defined field on IntelToken in Art 02b.
- **Taxonomy: Add vs Corrupt:** design_note says "Add with corrupt content." Confirm whether this should use Corrupt function or Add with a false-content attribute.
- **Self-Intel token cap exemption:** Ghost may hold self-directed Intel tokens without cap (Art 02b §8) — confirm this is documented.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*S51 redesign — design pass pending*

```python
C20 = Card(
    id=20,  version="v1.0",
    name    = "Misdirection",
    tagline = "Plant false intelligence about Ghost in the accessible record.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Add,  subject = IntelToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    target_district=None, target_faction=faction(named_opponent), target_object=None,
    affinity=None,
    restriction = faction(acting).intel_tokens(faction=Ghost) >= 1,
    cost        = resource.faction(acting).findings * 1,
    success     = game.dispatch(faction(target), IntelToken(faction=Ghost, content=false, quarter=game.quarter)),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Ghost: PortraitEntry(submitter=+1)},
    narrative   = "Ghost has been considering what its opponents think Ghost is doing. It is never quite right.",
    perspectives = {Ghost: "We have thought carefully about what they expect. We have given them exactly that."},
    design_note  = "Add with corrupt content — falsification is an attribute of content, not a separate function. False token is indistinguishable from a genuine Gather result. Any Denounce using it will fail.",
    arbiter_note = "Deliver false Intel token to target faction via case. Token contains false Ghost operation type and false target district for this round. Ghost may hold self-directed Intel tokens without cap (Art 02b §8).",
)
```

---

### Ghost — STATION
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's dedicated faction-specific gather platform. Distinct from C05 Gather (standard, adjacency-exempt, 1 token yield) by higher yield (2 tokens on success) at higher cost (2 Findings). C05 is Ghost's remote general-purpose sweep; Station is a deployed collection platform sustaining coverage against a named faction over a Quarter. Two deck copies make Station Ghost's primary Intel generation card. No adjacency restriction — consistent with C16-C20 pattern; 00-R29 clarification is a separate item (PM05 04-n6).

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Dedicated gather platform — Ghost's high-yield intelligence collection card; distinct from C05 (standard, 1 token) by sustained multi-token output | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — Station as deployed platform, not remote sweep | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; 2 Findings cost for 2-token yield reflects sustained collection investment; threshold 45 vs C05 50 — offset for higher cost (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — Ghost's primary Intel generation card beyond standard C05 | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Add/IntelToken — same taxonomy as C05; faction-specific variant with higher yield | Art 04b §4, §5 |
| Balance | ✓ | Threshold 45, cost 2 Findings, yield 2 tokens — calibration vs C05 outstanding (Outstanding Issue) | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: Intel tokens dispatched at Beat 3; durable resource, no card-level duration | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — collection operations align with Ghost intelligence doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any; no adjacency restriction per 00-R29 outstanding (Outstanding Issue) | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Art 02b §8); Findings cost; no new components | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 3 d100 resolution; tokens dispatched to Ghost case on success; failcrit NotificationSlip per standard | Art 03 §9, §11 |

#### Outstanding Issues

- **Threshold calibration:** 45 vs C05's 50 — offset for higher cost and no adjacency exemption. Confirm during balance pass.
- **00-R29 clarification:** no adjacency restriction applied; pending PM05 04-n6 rule clarification.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Draft S59 — design pass pending*

```python
Card(
    id=TBD,  version="v1.0",  # ID pending PM05 04-n1
    name    = "Station",
    tagline = "Deploy a sustained intelligence collection platform against a named faction.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Add,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 45,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).findings * 2,

    success     = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)) * 2,
    successcrit = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)),  # +1 = 3 total
    fail        = None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Every asset leaves a signal. Ghost listens until the signal becomes a pattern.",
    perspectives = {Ghost: "A station does not move. It waits until the target walks past it again."},
    design_note  = "Ghost's dedicated gather platform. Higher yield than C05 (2 tokens vs 1 on success) at double Findings cost. No adjacency restriction — consistent with C16-C20 pattern; 00-R29 refinement pending. Cards stack: C05 and Station may both target same faction in same Quarter.",
)
```

---

### Ghost — FULL TAKE
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Burst gather for pre-loading multi-Quarter intelligence sequences. Single copy representing a total-collection operation: Ghost declares n Findings at submission, receives 2n Intel tokens on success (3n on crit). The slot commitment plus n Findings is the bet — fail returns nothing. Variable cost makes the card self-scaling: a small Full Take (n=1) is conservative; a large Full Take (n=3+) pre-loads an entire SCIF/Flip sequence. Reserved for mid-to-late game plays when Ghost has Findings reserves to invest. Singleton enforces scarcity.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Burst intelligence collection — pre-loads multi-Quarter sequences (SCIF, Flip, Signals Analysis); singleton scarcity enforces mid-to-late game use | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — maximum-yield operation as Ghost doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; variable cost scales with investment; singleton forces strategic commitment; no adjacency restriction consistent with C16-C20 pattern | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — burst intelligence platform; no Standard equivalent | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Add/IntelToken — higher-yield variant of Station/C05 pattern | Art 04b §4, §5 |
| Balance | ✓ | Variable cost n × 2 yield (3n crit) — singleton scarcity limits use; Intel holding guideline (4, not HARD) tolerates high-n plays per Outstanding Issue; fail = nothing is the correct floor | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: Intel tokens dispatched at Beat 3; durable resource, no card-level duration | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — maximum-yield collection aligns with Ghost intelligence doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any; no adjacency restriction per 00-R29 outstanding | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Art 02b §8); Findings cost; variable n Beat 0 validation outstanding (Outstanding Issue) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 0: ARBITER records declared n, validates n Findings present (00-R22) — procedure confirmation outstanding (Outstanding Issue) | Art 03 §9, §11 |

#### Outstanding Issues

- **Variable cost validation:** ARBITER must record declared n at Beat 0 and verify n Findings physically present. Confirm Art 03 Beat 0 procedure covers this or flag for addition.
- **Intel holding guideline:** high-n Full Take may produce tokens exceeding the 4-token guideline. Guideline is not HARD — excess noted, not blocked. Confirm intent.
- **00-R29 clarification:** no adjacency restriction applied; pending PM05 04-n6.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Draft S59 — design pass pending*

```python
Card(
    id=TBD,  version="v1.0",  # ID pending PM05 04-n1
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

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).findings * n,  # n declared at submission; n >= 1; all n Findings physically present (00-R22)

    success     = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)) * (n * 2),
    successcrit = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)) * n,   # +n = 3n total
    fail        = None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Some intelligence is gathered patiently. Some is taken all at once.",
    perspectives = {Ghost: "The take was complete. Everything they transmitted this Quarter. We have it."},
    design_note  = "Singleton. Variable cost: Ghost declares n at submission; cost = n Findings; success = 2n Intel tokens; crit success = 3n. Fail = nothing. ARBITER validates n Findings present at Beat 0. NOT Deep Cover — C19 is Deep Cover. Intel holding guideline is 4 (not HARD); high-n plays may exceed guideline.",
    arbiter_note = "At Beat 0: record declared n; validate n Findings present in case. At Beat 3: success = dispatch 2n IntelToken(faction=target) to Ghost's case; crit success = dispatch 3n; fail = nothing; crit fail = NotificationSlip to target.",
)
```

---

### Ghost — SCIF
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Converts existing faction-keyed Intel into future modifier capability. Spends one Intel token; ARBITER records the target faction's current structure block count in a SCIF Record card placed in Ghost's Dispatch Case. At Debrief, Ghost draws modifier cards equal to that count. Ghost is always building next Quarter's hand rather than spending this one. Yield scales with target development: SCIF against a lightly-built faction early game is modest; against a heavily-built Directorate or Guild late game it fills Ghost's modifier hand. The deferred payoff creates a planning horizon that no other faction can directly interrupt.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Converts Intel into future modifier capability — Ghost builds next Quarter's tactical hand rather than spending this one; deferred payoff no other faction can directly interrupt | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — intelligence as infrastructure for future action | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; IntelToken cost gates use on prior collection; yield scales with target development — balance concern flagged (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — deferred modifier economy is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Add/SCIFRecord — registered 00b §4 (SR-xx); agy task outstanding | Art 04b §4, §5 |
| Balance | ✓ | Yield scales with target's structure count per ring; balance assessment deferred until Art 03 procedure locked | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: SCIFRecord instantiated at Beat 3; Debrief draw is Art 03 procedure, not a card-level lingering effect — compliant with 00-R21 | — |
| Persistence | ✓ | Immediate — card fully resolved at Beat 3; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — Automatic resolution; restriction enforces Intel token presence | — |
| Portrait validity | ✓ | Ghost +1 submitter — intelligence-to-modifier conversion aligns with Ghost doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted operation; no district required | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; SCIFRecord registered 00b §4 (SR-xx) — agy task outstanding | Art 02a §6–§8 |
| Supported by game procedure | ⚠ | Art 03 Beat 3 instantiation + Debrief draw procedure outstanding — blocks Issues Resolved (04-n27) | Art 03 §9, §11, §19 |

#### Outstanding Issues

- **SCIFRecord component:** Register SR-xx in 00b §4 (agy). Fields: `quarter | draw_ring1 | draw_ring2 | draw_ring3 | draw_faction`. draw_ringN = target's structure block count per ring at Beat 3 (snapshot). draw_faction = upkeep step formula on target's total structure block count (0–1: 0, 2–3: 1, 4–5: 2, 6+: 3).
- **⚠ Art 03 procedure — blocks Issues Resolved:** Beat 3 instantiation sequence and Debrief draw procedure (process all SCIF Records in Ghost's case; draw from ring decks + Ghost faction deck per recorded counts; no ring-eligibility check; discard slip after use; discard unused at Phase 21) not yet in Art 03. Track under 04-n27.
- **Balance — yield scaling:** SCIF yield grows as Guild and Directorate build. Playtest flag — non-blocking.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
Card(
    id=TBD,  version="v1.0",  # ID pending PM05 04-n1
    name    = "SCIF",
    tagline = "Turn intelligence into operational assets.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Add,  subject = SCIFRecord,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    affinity    = None,
    restriction = faction(acting).intel_tokens(faction=faction(target)) >= 1,
    cost        = IntelToken(faction=faction(target)) * 1,

    success     = SCIFRecord(target=faction(target)),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "The structure count is the number of ways they have committed themselves. Ghost counts carefully.",
    perspectives = {Ghost: "We do not need to be inside their operation. We need to know how large it is."},
    design_note  = "Converts held intelligence into future modifier capability — Ghost builds next Quarter's hand from this Quarter's intelligence. Pairs with Station, Full Take, and Synthesize: the SCIF pipeline is the destination for accumulated faction-keyed Intel. Yield scales with target development, creating an intelligence premium on heavily-built opponents.",
    arbiter_note = "⚠ Procedure outstanding — Beat 3 instantiation and Debrief draw sequence not yet in Art 03. See PM05 04-n27. Blocks Issues Resolved.",
)
```

---

### Ghost — FLIP
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Economic arm of Ghost's intelligence pipeline. One faction-keyed Intel token consumed; ARBITER places 2 of the target faction's native resource in Ghost's Dispatch Case at Beat 3. Resources return at month-end with normal case contents — no deferred procedure required. Flip is the unlock for Ghost's higher-tier cards, which carry a secondary cost of Flip-acquired faction resources (the "target faction's assets turned against them" design direction, per C17 model). Layer is Economy per L175: primary effect is resource acquisition despite the Intel gating.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Economic arm of Ghost's intelligence pipeline — converts faction-keyed Intel into target faction's native resource; unlock for higher-tier Ghost cards | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — resource redirection as intelligence exploitation | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; IntelToken cost enforces intelligence pipeline dependency; resource quantity placeholder pending Art 00c calibration (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence-gated resource acquisition is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/FactionNativeResource — Layer = Economy per L175; primary effect is resource acquisition despite Intel gating (Outstanding Issue for taxonomy review) | Art 04b §4, §5 |
| Balance | ✓ | Quantity 2 is a placeholder — calibrate against Art 00c; target does NOT lose resources (copy, not transfer — Outstanding Issue for confirmation) | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: resources dispatched at Beat 3; available at month-end via normal case return (00-R21 compliant) | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — Automatic resolution | — |
| Portrait validity | ✓ | Ghost +1 submitter — resource acquisition via intelligence pipeline aligns with Ghost doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; target faction native resource type delivered to case; no new components | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Resources in Dispatch Case returned at month-end per normal procedure — no new Art 03 step required | Art 03 §9, §11 |

#### Outstanding Issues

- **Resource quantity:** 2 is a placeholder. Adjust after Art 00c economy calibration.
- **Target does not lose resources:** Flip is a copy/redirect, not a transfer. Target faction's resource pool is not reduced. Confirm this is the intended model.
- **Layer = Economy:** Primary effect is resource acquisition; gated by Intel token. Per L175 correct, but confirm during taxonomy review.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Draft S59 — design pass pending*

```python
Card(
    id=TBD,  version="v1.0",  # ID pending PM05 04-n1
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

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    affinity    = None,
    restriction = faction(acting).intel_tokens(faction=faction(target)) >= 1,
    cost        = IntelToken(faction=faction(target)) * 1,

    success     = game.dispatch(faction(acting), resource.faction(target).native * 2),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Ghost does not steal. Ghost redirects what was already in motion.",
    perspectives = {Ghost: "Their resource. Our pipeline. They built something worth taking."},
    design_note  = "Layer=Economy per L175 — primary effect is resource acquisition despite intelligence gating. Resources dispatched to Ghost's Dispatch Case at Beat 3; returned to Ghost at month-end with normal case contents. Target faction does NOT lose resources. Quantity 2 is a design placeholder — calibrate against Art 00c. Higher-tier Ghost cards carry secondary cost = faction(target).native consumed on play (C17 model).",
    arbiter_note = "At Beat 3: consume IntelToken(faction=target) from Ghost's case. Dispatch 2 units of target faction's native resource type to Ghost's Dispatch Case. Target faction's resource pool is not reduced. Resources available to Ghost at month-end with normal case return.",
)
```

---

### Ghost — SIGNALS ANALYSIS
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's strategically decisive card. Reveals the target faction's Classified Directive privately to Ghost, enabling Ghost to engineer situations where pursuing a hidden objective requires betraying visible doctrine — Ghost's core win vector. Highest cost in the Ghost set (2 faction-keyed Intel tokens + 3 Findings) with the lowest threshold (30%), reflecting that this is a rare, high-investment play not available until Ghost has accumulated significant Intel reserves. Analytical work — no adjacency required, consistent with the C16-C20 pattern. Portrait modifier on success (+2 total) captures Ghost's doctrine that intelligence is only vindicated by operational use.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost's strategically decisive card — reveals Classified Directive enabling Ghost to engineer doctrine-betrayal situations; Ghost's core win vector | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — intelligence as strategic leverage | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; highest cost in Ghost set (2 Intel + 3 Findings); threshold 30 — reserved for Ghost players with Intel reserves; portrait AND semantics outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — Directive reveal is Ghost-exclusive win-condition card | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/ClassifiedDirective — component registration outstanding (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | Threshold 30 + cost 2 Intel + 3 Findings — rarity level appropriate for Directive reveal; singleton | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: private information revealed once at Beat 3; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces Intel token floor (≥2) | — |
| Portrait validity | ✓ | submitter=+1 unconditional + modifier=+1 on success — AND semantics outstanding (Outstanding Issue) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — no district target; operates on abstract ClassifiedDirective object | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost (×2); ClassifiedDirective as target_object — component registration outstanding (Outstanding Issue) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Private reveal via ARBITER screen; private faction-to-faction reveal procedure outstanding (Outstanding Issue) | Art 03 §9, §11; Art 07 |

#### Outstanding Issues

- **ClassifiedDirective component:** `target_object = ClassifiedDirective` — confirm this is a registered component type in Art 02 series. May need to be added.
- **Private reveal procedure:** ARBITER reveals Directive across screen to Ghost player. Confirm Art 07 has or will have a procedure for private faction reveals (same mechanism as C17 IntelDeliverySlip?).
- **Portrait AND semantics:** `submitter=+1, modifier=+1, mod_where=game.outcome==Success` — confirm same model as C16 Pattern Match (submitter always fires; modifier fires additionally on success).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = ClassifiedDirective,

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
    design_note  = "Ghost's highest-cost card. Cost: 2 faction-keyed Intel tokens + 3 Findings, all physically present (00-R22). Threshold 30 — reserved for Ghost players who have built Intel reserves. No adjacency restriction (analytical work — consistent with C16-C20 pattern). Portrait: submitter=+1 unconditional + modifier=+1 on success. ClassifiedDirective component type pending verification in Art 02 series.",
    arbiter_note = "Privately reveal target faction's Classified Directive to Ghost player across screen. Do not announce to table. Ghost may not publicly prove knowledge. Crit fail: NotificationSlip to target only — do not reveal what Ghost was attempting.",
)
```

---

### Ghost — SYNTHESIZE
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's intelligence amplification card — converts one held Intel token into three, netting +2. Designed for the GATHER→SYNTHESIZE Double Case Pass combo (L145): play C05 Gather in Month 1 to acquire an Intel token, then play Synthesize in Month 2 or 3 to multiply it before a high-cost operation (SCIF, Flip, Signals Analysis). The consumed token can be any faction-keyed token — Synthesize is processing, not targeting. Findings×1 is the analytical cost of converting raw surveillance into operational signal. The result is Ghost building Intel reserves without needing to place additional Gather operations.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence amplification — converts 1 token into 3 (net +2); enables GATHER→SYNTHESIZE combo that pre-loads high-cost operations (SCIF, Flip, Signals Analysis) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — processing as doctrine, not just collection | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; Findings×1 cost reflects analytical work; consumed token is any held token; generated token faction-keying outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence processing is Ghost-exclusive pipeline capability | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/IntelToken — net amplification of Intel supply; Economy layer correct for resource generation effect | Art 04b §4, §5 |
| Balance | ✓ | Findings×1 + 1 IntelToken → 3 IntelTokens (net +2) — amplification rate reasonable; token faction-keying affects SCIF/Flip gate eligibility (Outstanding Issue) | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: tokens delivered at Beat 3; durable resource | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter only; submitter-bounded per P16 | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — internal intel processing; no district context | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken as both cost and subject; Findings cost; no new components | Art 02a §6–§8; Art 02b §8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; tokens delivered at Beat 3; SCIF/Flip gate eligibility of generated tokens outstanding (Outstanding Issue) | Art 03 §9, §11 |

#### Outstanding Issues

- **Token faction-keying:** The original design note says "Intel token consumed is any held token — not required to be faction-indexed." Confirm whether the 3 tokens delivered are also unkeyed (any) or if Synthesize generates tokens keyed to the consumed token's faction. The answer affects SCIF/Flip gate eligibility.
- **GATHER→SYNTHESIZE combo L145:** Confirm L145 is still the canonical reference for this combo — if L145 has been superseded or renumbered, update reference.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Migrated from §8 Intel Economy block to Ghost extended section S59. Pre-convention flat format — full schema pass pending (04-47).*

```python
C36 = Card(
    id=36,  version="v1.0",
    name    = "Synthesize",
    tagline = "Convert raw intelligence into operational clarity.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Economy,  function = Add,  subject = IntelToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    target_district=None, target_faction=None, target_object=IntelToken,
    affinity=Ghost,
    restriction = faction(acting).intel_tokens.count >= 1,
    cost        = resource.faction(acting).findings * 1 + IntelToken(any) * 1,
    success     = game.dispatch(faction(acting), IntelToken(any) * 3),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Ghost: PortraitEntry(submitter=+1)},
    narrative   = "Raw surveillance is noise. What Ghost does to it — that is signal.",
    perspectives = {Ghost: "We don't just gather. We process. The difference is what we are."},
    design_note  = "GATHER→SYNTHESIZE Double Case Pass combo (L145): Gather in Month 1, Synthesize in Month 2/3. Consumed token is any held token — not required to be faction-keyed. Generated tokens: confirm faction-keying at schema pass (outstanding issue).",
    arbiter_note = "Consume 1 held Intel token (any faction key) and 1 Findings from Ghost's supply. Deliver 3 Intel tokens to Ghost's Dispatch Case. Confirm faction-keying of delivered tokens per resolution of outstanding issue.",
)
```

---

### Ghost — SOURCE SUBSTITUTION
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Intelligence falsification — alter the faction field on a held Intel token. Ghost submits the token in their dispatch case with a written instructions slip naming the new faction and the return destination (self or a named target faction). On success ARBITER makes the physical alteration and either returns the token to Ghost's case (keep mode) or discreetly delivers it to the named faction's terminal (plant mode). The planted version is a trap: the receiving faction holds an Intel token they believe is valid, which may cause them to play P04, P05, or P13 against the wrong target. Fail destroys the token — botched falsification leaves unusable evidence. Fail crit leaves traces: ARBITER dispatches a NotificationSlip to the faction originally named on the token, signalling that someone attempted to manipulate a record referencing them. Ghost adjacency applies in plant mode (you must be near where the operation is being attributed). Keep mode is a self-operation on a held asset — no adjacency required.

Standard equivalent: PM05 04-n15 (hired data specialist version — higher cost, lower threshold).

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence record falsification is Ghost's deepest operational mode — the pipeline endpoint that converts gathered intel into active deception | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — falsification as operational doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; keep/plant dual mode reflects Ghost's operational flexibility; IntelToken restriction enforces prior collection dependency | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence manipulation is Ghost-exclusive by Principle 17; standard equivalent flagged PM05 04-n15 | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/IntelToken (faction field) | Art 04b §4 |
| Balance | ✓ | 2 Findings + token cost is substantial; token destroyed on fail — real risk; plant mode threat value exists even without direct use | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: token altered and returned/planted at Beat 3; fail destroys token at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces Intel token presence | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded; intelligence manipulation is core Ghost doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None; plant mode adjacency (00-R29) applies only in plant mode — no zone restriction for keep mode | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken as both cost and target; instructions slip in case (written); no new physical components | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Plant mode delivery protocol and instructions slip format outstanding (Outstanding Issues) | Art 03 §11 |

#### Outstanding Issues

- **Plant mode delivery protocol:** Discreet delivery to target terminal during Beat 3 cleanup — procedure not yet defined in Art 03/07.
- **Instructions slip format:** Confirm written slip vs. verbal declaration at Phase A for keep/plant mode and target faction name.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
SourceSubstitution = Card(
    id      = "Ghost-ext-TBD",  version = "v1.0",
    name    = "Source Substitution",
    tagline = "Falsify the faction record on a held Intel token — keep for future use or plant on a target.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Corrupt,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 45,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Deceptive",
    outcome_type    = None,
    persistence     = Immediate,

    target_district = None,  # plant mode: adjacency to target faction's operations (00-R29)
    target_faction  = faction.any_or_none,  # None = keep mode; named faction = plant mode; declared at Phase A
    target_object   = intel_token.held,     # token submitted in dispatch case

    affinity    = None,
    restriction = faction(Ghost).holds_intel_token(count=1),
    cost        = resource.faction(Ghost).findings * 2 + intel_token.held * 1,

    # Instructions slip in case: [new faction name] | [return: self / named faction]
    success = (
        arbiter.corrupt(intel_token.held, field=faction_name, value=declared_new_faction),
        if target_faction == None:
            arbiter.return_to_case(intel_token),         # keep mode
        else:
            arbiter.deliver_discreet(intel_token, target_faction),  # plant mode
    ),
    successcrit = None,
    fail        = arbiter.destroy(intel_token),
    failcrit    = (
        arbiter.destroy(intel_token),
        arbiter.dispatch(NotificationSlip, recipient=intel_token.original_faction),
    ),

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "The record says what Ghost needs it to say. The question is where the record ends up.",
    perspectives = {
        Ghost: "The attribution is wrong. It will stay wrong. What happens next depends on who reads it.",
    },
    design_note  = "Intelligence falsification — faction field only. Keep mode: Ghost retains the altered token for future attribution plays. Plant mode: token delivered discreetly to target faction's terminal at Beat 3 cleanup; target holds a token they believe is valid. Fail destroys token. Failcrit additionally alerts the originally-named faction via NotificationSlip. Ghost adjacency applies only in plant mode (00-R29). Standard equivalent flagged PM05 04-n15.",
    arbiter_note = "Phase A: Ghost declares keep or plant mode and named faction (if plant). Token submitted in case with written instructions slip. Beat 3: d100 vs 45. On success: alter faction name field on token per slip. Keep: return token in case. Plant: deliver token discreetly to target faction's terminal during Beat 3 cleanup — do not announce. On fail: destroy token. On failcrit: destroy token AND dispatch NotificationSlip to the faction originally named on the token.",
)
```

---

### Ghost — BACKDATE
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Intelligence poisoning — alter the quarter field on a held Intel token to make it appear older. A Fresh token can be degraded to Stale or Expired. The primary use is the poisoned gift (plant mode): deliver a degraded token to a target faction who will discover — when they attempt to use it — that their intelligence is stale or worthless. The acting faction sacrifices a functional token to waste a future opposing action. Keep mode has narrower use: Ghost may want to make an operation appear to have occurred earlier (strategic alibi). Threshold 30 is harder than Source Substitution (45) because temporal records are more verifiable — altering when something happened is more conspicuous than altering who. Fail destroys the token; failcrit notifies the originally-named faction. Ghost adjacency applies in plant mode.

Standard equivalent: PM05 04-n15.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Temporal falsification of intelligence records — primary use is poisoned gift (plant Expired token on target to waste their attribution play) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — temporal record manipulation as operational doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; threshold 30 (harder than Source Substitution 45) reflects temporal records are more verifiable; same keep/plant dual mode as Source Substitution | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/IntelToken (quarter field) — distinct from Source Substitution (faction field) | Art 04b §4 |
| Balance | ✓ | Threshold 30 — harder than Source Substitution; temporal records more verifiable; fail destroys token — real cost | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: token altered and returned/planted at Beat 3; fail destroys token at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces Intel token presence | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None; plant mode adjacency (00-R29) applies only in plant mode | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken as both cost and target; requires two writable fields (faction + quarter) outstanding (Outstanding Issue); instructions slip in case | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Plant mode delivery protocol same as Source Substitution — outstanding (Outstanding Issue) | Art 02a §6–§8; Art 03 §11 |

#### Outstanding Issues

- **Token writable fields:** Intel token component must support two writable fields (faction name + quarter). Confirm component design in Art 02b.
- **Plant mode delivery protocol:** Same as Source Substitution — discreet delivery to target terminal during Beat 3 cleanup; procedure not yet defined in Art 03/07.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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

    target_district = None,
    target_faction  = faction.any_or_none,  # None = keep; named = plant
    target_object   = intel_token.held,

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

### Ghost — FIELD VERIFICATION
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost re-validates expired intelligence. An Expired Intel token is submitted in the dispatch case with no instructions — the question posed to ARBITER is simply: is this still current? On success, the token's quarter is updated to the present Quarter and its classification becomes Fresh. On fail, the token is returned Expired and Ghost has lost only the dispatch slot. No Findings cost — the slot IS the investment. Threshold 35 reflects genuine uncertainty: intelligence gathered 4+ quarters ago may or may not still describe reality; there is no guarantee the world has not changed. This is not falsification — Ghost is genuinely re-checking a cold lead. Self-operation only; no adjacency required. Distinct from Source Substitution and Backdate (which falsify; this verifies).

Standard equivalent: PM05 04-n15 (hired investigator reopening cold case — same mechanic, costs Findings, lower threshold).

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost re-validating aged intelligence — "understanding must precede action" includes verifying that old understanding is still current; Expired → Fresh recovery | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — verification as discipline, not just collection | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; no Findings cost — slot IS the investment; self-operation only; distinct from Source Substitution/Backdate (falsification vs. verification) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence pipeline methodology; standard equivalent flagged PM05 04-n15 | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Recover/IntelToken — Recover returns a degraded element to active play; Expired → Fresh is a recovery | Art 04b §4 |
| Balance | ✓ | No Findings cost; dispatch slot only; fail = slot wasted, token returned (no token loss); threshold 35 creates meaningful failure rate | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: token updated or returned at Beat 3; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces Expired token in case | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded; re-validation before acting is Ghost's core doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — self-operation on held token; no district context | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Expired) as cost and target; requires writable quarter field (same as Backdate — see Backdate Outstanding Issue) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Self-operation; no adjacency required; ARBITER updates quarter field on success, returns token on fail | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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

    target_district = None,  # self-operation; no adjacency required
    target_faction  = None,
    target_object   = intel_token.held,  # must be Expired; submitted in case

    affinity    = None,
    restriction = intel_token.held.age == Expired,
    cost        = None,  # no resource cost; dispatch slot is the investment (00-R39)

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

### Ghost — Public Acts
[↑ Ghost](#ghost)

| Card | Name |
|------|------|
| [P17](#p17-publish-analysis) | Publish Analysis |
| [P18](#p18-signal-review-request) | Signal Review Request |

### P17 — PUBLISH ANALYSIS
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Ghost's highest-cost PA — a simultaneous public attribution of two factions using two Intel tokens as evidence. The token requirement is the certainty check: Ghost does not publish speculation. Two tokens naming different factions are spent; both attributions are announced at Beat 4. Each named faction loses −2 PS; Ghost gains +2 PS flat. Ghost pays 3 Findings (their core intelligence currency) plus two Intel tokens for a decisive multi-target public strike — the cost reflects that going public is doctrinally expensive for Ghost even when the intelligence justifies it. Portrait +1: Ghost acts on doctrine when understanding precedes the disclosure decision.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost publishing curated analysis is a calculated, rare public act — the cost enforces rarity | Art 00 §7 |
| Voice fit | ✓ | Ghost on-doctrine; Directorate (aligned): verified, sequenced disclosure; Network (opposed): held both when one was enough | Art 00 §7, §9 |
| Doctrine alignment | ✓ | "Understanding must precede action" — Ghost publishes only when two tokens confirm both attributions. Portrait +1: calculated disclosure from position of knowledge. 3 Findings cost reflects that public disclosure is doctrinally expensive for Ghost | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Reveal / ActionAttribution (multi-target) | Art 04b §4 |
| Balance | ✓ | 3 Findings + 2 Intel tokens; Automatic; two targets −2 PS each; Ghost +2 PS. High cost, high yield. Token acquisition is the natural limiter | Art 02a §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded. Published from position of knowledge — doctrine affirmed | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — two faction targets; no district reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (two, faction-keyed to different targets; Art 02a §6); Findings × 3 cost (Art 02a §8) | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Two targets named at Phase B; both tokens submitted; Automatic Beat 4 | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P17 = Card(
    id="P17",  version="v1.0",
    name    = "Publish Analysis",
    tagline = "Release curated intelligence simultaneously attributing operations to two factions — a calculated, costly disclosure.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Ghost,

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

    target_district = None,
    target_faction  = faction.two_opponents,  # two different factions named at Phase B
    target_object   = None,

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

### P18 — SIGNAL REVIEW REQUEST
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Ghost uses institutional channels to apply operational pressure on a named faction. The effect is a −15 threshold penalty on that faction's covert operations in the named district next Month (Transient). Ghost gains no PS — this is a tool, not a stage. Ghost adjacency requirement (00-R29) applies to all Ghost cards except C05. Persistence = Transient: the P18 card stays face-up on the table with a marker on the target district until Beat 5 of next Month, serving as the active condition indicator. ARBITER removes the card and returns it to Ghost at Beat 5.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost using institutional accountability to enforce operational scrutiny is on-doctrine and narratively grounded | Art 00 §7 |
| Voice fit | ✓ | Ghost on-doctrine; Syndicate (aligned): institutional tool with no exposure cost; Guild (opposed): bureaucratic delay vs. direct action | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Ghost uses the institutional channel as a tool, not a stage — no PS gain. Adjacency requirement (00-R29) grounds the card in Ghost's operational footprint. Portrait +1: submitter-bounded | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Resolution / Modify / CovertOperation (difficulty) | Art 04b §4 |
| Balance | ✓ | 2 Findings; −15 threshold (meaningful but not absolute block); Transient. Ghost adjacency limits targeting range | Art 02a §6–§7 |
| Effect duration | ✓ | Threshold modifier is Transient (until Beat 5 of next Month — within-Quarter). No multi-Quarter duration | 00-R21 |
| Persistence | ✓ | Transient — card stays face-up on table with district marker until Beat 5 next Month | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone; restriction uses Ghost presence in adjacent district (valid zone condition per 00-R29) | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — threshold modifier is a world condition tracked by ARBITER; Findings × 2 cost (Art 02a §8) | Art 02a §8 |
| Supported by game procedure | ✓ | Physical tracking: P18 card face-up + district marker; ARBITER removes at Beat 5 next Month | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P18 = Card(
    id="P18",  version="v1.0",
    name    = "Signal Review Request",
    tagline = "Formally request institutional scrutiny on a faction's next covert operation in a named district.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Resolution,  function = Modify,  subject = CovertOperation,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Transient,  # card stays on table with district marker until Beat 5 next Month

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    affinity    = None,
    restriction = faction(Ghost).presence(district.adjacent_to(target_district)) > 0,  # 00-R29
    cost        = resource.faction(Ghost).findings * 2,

    success = game.world_condition(
        scope    = district(target),
        target   = covert_op(faction=target_faction),
        effect   = threshold -= 15,
        duration = Transient,  # Beat 5 of next Month
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
    design_note  = "Ghost operational pressure PA. Uses institutional scrutiny (ARBITER) to apply −15 threshold to target faction's covert ops in named district next Month. No PS gain for Ghost — the channel is a tool. Ghost adjacency (00-R29): must have presence in adjacent district. Persistence = Transient: P18 card face-up on table + district marker until Beat 5 of next Month. Multiple P18s from different Months can stack. Distinct from P17 (attribution) — P18 creates ongoing pressure without disclosure.",
    arbiter_note = "Beat 4: place P18 card face-up on table with marker on target district. Apply −15 threshold penalty to all covert operations submitted by target faction in target district next Month (Beat 3). Card expires Beat 5 that Month — announce removal, return card to Ghost. Multiple P18 cards on same district from different Months stack (each tracked independently). Ghost adjacency enforced at Beat 0.",
)
```

---


---

## Directorate
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#directorate-covert-operations) · [Public Acts](#directorate-public-acts)

---

### Directorate — Covert Operations
[↑ Directorate](#directorate)

| Card | Name |
|------|------|
| [C21](#c21-invoke-jurisdiction) | Invoke Jurisdiction |
| [C22](#c22-detain) | Detain |
| [C23](#c23-evidence-preservation) | Evidence Preservation |
| [C24](#c24-surveillance-placement) | Surveillance Placement |
| [C25](#c25-tactical-redirection) | Tactical Redirection |
| [C42](#directorate-sanctioned-raid) | Sanctioned Raid |
| [—](#directorate-regulatory-downgrade) | Regulatory Downgrade |
| [—](#directorate-regulatory-freeze) | Regulatory Freeze |

### C21 — INVOKE JURISDICTION
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's positional authority card — asserts institutional control over a named district for a full round by blocking the two primary expansion actions (C01 Build Structure, C03 Campaign). Beat 2 Automatic positional wager: no dice, but the card slot is committed at Dispatch. No restriction means Invoke Jurisdiction can target any district, including ones where Directorate has no presence — the Directorate's authority is institutional, not territorial. Cost Mandate×2 reflects this as a mid-tier operational spend. The block is public (per game.block parameters), signaling to the table exactly which district is under oversight.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional authority assertion over a district — blocks primary expansion actions for one round; distinct from C25 (repositions own presence) and C35 (blocks named action type for a faction) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; no presence requirement — institutional authority is not territorial; Mandate×2 calibrated as mid-tier spend; block scope outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — jurisdictional authority is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Submission/Block/CovertOperation — beats Beat 2 Automatic; block applies to C01 and C03 in target district for one round | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic, blocks C01+C03 for one round — block scope calibration outstanding (Outstanding Issue) | Art 02a §6–§7 |
| Effect duration | ✓ | One round: block applies for round=game.round only | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 positional wager fires on C01/C03 submissions in target district | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; jurisdictional assertion aligns with institutional doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | No new components; game.block() is an existing Beat 2 mechanism | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 2 positional wager; game.block() applies at Beat 2 resolution; game.block resolution (resources on blocked card) outstanding (Outstanding Issue) | Art 03 §9, §11 |

#### Outstanding Issues

- **Block scope — C01/C03 only:** C21 blocks C01 and C03 explicitly. Confirm whether this should extend to C04 (Demolition) or C08 (Buy Influence) to reflect true jurisdictional authority, or remain limited to the two build/presence cards by design.
- **game.block resolution:** Confirm Beat 2 block mechanic — does a blocked C01/C03 cost the submitter their action slot and resources, or is it returned? Needs Art 03 §11 Beat 2 procedure to confirm.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C21 = Card(
    id=21,  version="v1.0",
    name    = "Invoke Jurisdiction",
    tagline = "Assert institutional authority over a target district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Submission,  function = Block,  subject = CovertOperation,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=district.any, target_faction=None, target_object=CovertOperation,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).mandate * 2,
    success     = game.block(district(target), cards=[C01, C03], round=game.round, public=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate was here before the other factions arrived. Their jurisdictional authority is not theoretical.",
    perspectives = {Directorate: "This district is under institutional oversight. Expansion requires authorisation. Authorisation has not been granted."},
    design_note  = None,
    arbiter_note = None,
)
```

---

### C22 — DETAIN
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's permanent removal card — eliminates a faction's deployment marker from a district, permanently. The strongest single-target suppression in the Directorate set. Distinct from C04 Demolition (removes structure blocks) and C25 Tactical Redirection (moves own presence): Detain removes an opponent's operational anchor. Intel restriction (fresh token required) forces Directorate to have gathered intelligence before arresting — doctrine-consistent and a resource cost beyond the Mandate spend. Successcrit returns +3 Mandate, rewarding efficient institutional execution. Failcrit −1 PS reflects the institutional embarrassment of a failed detention. ChorusNode exclusion reflects ARBITER's deployment marker's special status.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Permanent deployment marker removal — Directorate's strongest single-target suppression; distinct from C04 (removes structures) and C25 (repositions own presence); Intel restriction enforces doctrine | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design — detention as institutional process | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Intel token restriction forces prior intelligence collection; ChorusNode exclusion respects ARBITER marker's special status; L183 Detention zone on Directorate public tableau | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — permanent removal is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Remove/DeploymentMarker — permanent per Principle 11; marker moved to Detention zone (00-R13a compliant) | Art 04b §4, §5 |
| Balance | ✓ | Mandate×3, threshold 50, permanent removal — highest Directorate covert cost; successcrit Mandate recovery outstanding (Outstanding Issue) | Art 02a §6–§7 |
| Effect duration | ✓ | Permanent: marker remains in Detention for remainder of session | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; failcrit −1 PS is game effect (not portrait), confirmed per P12 | Art 04 §6.2; Art 02b §7 |
| Supported by zones | ✓ | target_district = district.any; ChorusNode.deployment_marker excluded; Detention zone on Directorate public tableau (L183) | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken restriction; DeploymentMarker target; Detention zone is faction Terminal zone per L183; Intel age definition outstanding (Outstanding Issue) | Art 02a §6–§8; Art 02b §7 |
| Supported by game procedure | ✓ | Beat 3 d100 resolution; Intel check at Dispatch; ARBITER moves marker to Detention; visible to all players; no NotificationSlip needed | Art 03 §9, §11 |

#### Outstanding Issues

- **Intel token age interpretation:** `intel(faction=faction(target), age_rounds<=1)` — confirm "age_rounds<=1" means Fresh token (gathered this or last round) per Art 02b §8 aging definitions.
- **Successcrit Mandate recovery:** +3 Mandate on crit success is the highest reward in the Directorate set — confirm this is intentional given Mandate×3 base cost (net zero, but only on crit).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C22 = Card(
    id=22,  version="v1.0",
    name    = "Detain",
    tagline = "Permanently remove a faction's deployment marker from a district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Remove,  subject = DeploymentMarker,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10},
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    target_district=district.any, target_faction=faction(named_opponent), target_object=DeploymentMarker,
    affinity=None,
    restriction = (
        district(target).faction(target).deployment_marker >= 1
        AND intel(faction=faction(target), age_rounds<=1) >= 1
        AND district(target) != ChorusNode.deployment_marker
    ),
    cost        = resource.faction(acting).mandate * 3,
    success     = game.move(faction(target).deployment_marker, from_=district(target), to=Directorate.tableau.detention, public=True),
    successcrit = resource.faction(acting).mandate += 3,
    fail=None,
    failcrit    = faction(acting).standing -= 1,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate does not destroy — it detains. The distinction matters to them.",
    perspectives = {Directorate: "The marker has been detained. Its conversion will not occur."},
    design_note  = "L183. Marker moved to Directorate public tableau Detention zone — 00-R13a compliant (moved, not removed from play). Permanent: marker remains in Detention for remainder of session. No NotificationSlip — detention is publicly visible on Directorate tableau. Faction Terminals may be unique per faction (L183).",
    arbiter_note = "Consume Intel token. Move named faction's deployment marker from target district to Directorate public tableau Detention zone. Physically place on Detention area — visible to all players. No separate notification. Crit success: return 3 Mandate to Directorate. Crit fail: no marker move; −1 PS to Directorate only.",
)
```

---

### C23 — EVIDENCE PRESERVATION
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's record integrity card — locks a named written record permanently, preventing its modification for the remainder of the session. Reflects the institutional doctrine that the record is the Directorate's primary long-term advantage: once an event is inscribed and locked, no faction can revise, retract, or expunge it. The restriction (written record that isn't printed card text) is deliberately narrow — Evidence Preservation cannot lock card text itself, only ARBITER-maintained or player-written game records. Mandate×2 and Automatic resolution make this a routine institutional act. Permanent per Principle 11.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Record integrity card — permanently locks a game record against modification; distinct from C24 (surveillance infrastructure) and C19 Deep Cover (attribution erasure); Directorate's long-term institutional advantage | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design — institutional record preservation as doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Mandate×2, Automatic — routine institutional act; restriction narrowly scoped (no printed card text); WrittenRecord and lock enforcement outstanding (Outstanding Issues) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — record locking is Directorate-exclusive institutional capability | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Protect/WrittenRecord — permanent protection per Principle 11; WrittenRecord component registration outstanding (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic — balance assessment deferred until WrittenRecord component and lock enforcement defined (Outstanding Issues); currently low-cost for potentially high-impact preservation | Art 02a §6–§7 |
| Effect duration | ✓ | Permanent: locked record cannot be modified for remainder of session | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; record preservation aligns with institutional doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — operates on game record, not a district | Art 01 §6–§7 |
| Supported by components | ✓ | WrittenRecord as target_object — component registration and scope outstanding (Outstanding Issue) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; lock enforcement mechanism and naming procedure outstanding (Outstanding Issues) | Art 03 §9, §11 |

#### Outstanding Issues

- **WrittenRecord component type:** Undefined. Needs Art 02 registration. What physical or tracked game elements qualify as written records — ARBITER's ledger? Accord cards? Notated Chorus results? Scope must be defined before card passes component check.
- **Lock enforcement:** How does ARBITER enforce that a locked record cannot be modified? No existing procedure covers this. Needs Art 03 or Art 07 definition.
- **Naming specific records:** `game.record.element(named)` requires the Directorate player to name the specific record at Dispatch. Confirm procedure for naming and whether ARBITER validates the named element exists.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C23 = Card(
    id=23,  version="v1.0",
    name    = "Evidence Preservation",
    tagline = "Lock a written record against modification for the remainder of the session.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Information,  function = Protect,  subject = WrittenRecord,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=None, target_faction=None, target_object=WrittenRecord,
    affinity=None,
    restriction = game.record.element(target).is_written == True AND game.record.element(target).is_printed_card_text == False,
    cost        = resource.faction(acting).mandate * 2,
    success     = game.lock(game.record.element(named), permanent=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate's institutional advantage is the record. They protect it.",
    perspectives = {Directorate: "The record is preserved. Its integrity is now institutional fact."},
    design_note  = None,
    arbiter_note = None,
)
```

---

### C24 — SURVEILLANCE PLACEMENT
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's permanent intelligence infrastructure card — installs monitoring in a district that delivers operation-type notifications to Directorate before Beat 3 resolution for the rest of the game. Distinct from C05 Gather (one-time Intel token) and C17 Intercept (disrupts a single op): Surveillance Placement creates a permanent passive feed from a specific district. Operation type only (not faction) is intentional — it creates an intelligence chain requiring a follow-up Gather to identify the acting faction, rather than delivering full intelligence in one card. Automatic resolution reflects that installation is a procedural infrastructure act.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Permanent intelligence infrastructure — installs passive district monitoring; distinct from C05 (one-time token) and C17 (disrupts single op); creates ongoing information chain | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design — monitoring as institutional infrastructure | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; no presence requirement; Mandate×2 for permanent passive feed; delivery timing outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — institutional surveillance infrastructure is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Add/SurveillanceDevice — current spec has subject=IntelToken (taxonomy mismatch outstanding, Outstanding Issue); correct subject is surveillance infrastructure component | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic, permanent — balance assessment deferred until SurveillanceDevice component and delivery timing resolved (Outstanding Issues) | Art 02a §6–§7 |
| Effect duration | ✓ | Permanent: surveillance infrastructure persists until end of game | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; surveillance installation aligns with institutional monitoring doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | SurveillanceDevice component registration outstanding (Outstanding Issue); game.surveillance() function pending Art 02 definition | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; beat3_pre_resolution delivery timing outstanding (Outstanding Issue) | Art 03 §9, §11 |

#### Outstanding Issues

- **Surveillance component:** `game.surveillance()` implies a physical or tracked component (a marker or flag on the district). Needs Art 02 registration as `SurveillanceDevice` or similar; `subject = IntelToken` in current spec is a taxonomy mismatch — the card adds surveillance infrastructure, not Intel tokens.
- **Taxonomy subject mismatch:** `subject = IntelToken` is incorrect — the card's primary effect is surveillance infrastructure. Subject should be a surveillance component type pending Art 02 registration.
- **`beat3_pre_resolution` delivery timing:** Confirm whether ARBITER reveals the operation type to Directorate before or after the submitting faction resolves. Before resolution changes the information's strategic value significantly.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C24 = Card(
    id=24,  version="v1.0",
    name    = "Surveillance Placement",
    tagline = "Install permanent monitoring in a target district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Information,  function = Add,  subject = IntelToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=district.any, target_faction=None, target_object=None,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).mandate * 2,
    success     = game.surveillance(district(target), notify=Directorate, content="op_type_only", delivery="beat3_pre_resolution", permanent=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate monitors because monitoring is their primary tool for managing what they cannot directly control.",
    perspectives = {Directorate: "The installation is in place. Everything that happens in that district now happens with our awareness."},
    design_note  = "Permanent per Principle 11. Prior version monitored for 2 rounds — revised. Operation type only, not faction — creates intelligence chain requiring follow-up Gather to identify actors.",
    arbiter_note = None,
)
```

---

### C25 — TACTICAL REDIRECTION
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's repositioning card — the only card in the full set using Territory — Move — PresenceToken (Beat 2, Automatic). Designed to fill the gap identified in S51 when C25 Sealed Border was retired. Where most Directorate cards act on opponents, Tactical Redirection acts on Directorate's own presence, moving up to 2 tokens between adjacent districts before Beat 3 outcomes are applied. Beat 2 Automatic makes it a proactive positional adjustment — Directorate anticipates the round's contested districts and pre-positions before dice are rolled. ChorusNode exclusion (both source and destination) prevents repositioning through the central Chorus district. Mandate×2 is a mid-tier cost.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Proactive repositioning — moves up to 2 presence tokens between adjacent districts before Beat 3; fills Territory/Move/PresenceToken gap; only card in full set with this verb+subject at Beat 2 | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design — tactical pre-positioning as institutional doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Beat 2 Automatic — proactive, not reactive; ChorusNode exclusion; entry qualification outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — institutional pre-positioning is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Move/PresenceToken — unique taxonomy slot in full card set; Move function correct for same-faction repositioning | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic, moves count=2 — move count vs. restriction outstanding (Outstanding Issue) | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: tokens moved at Beat 2 resolution; control flags recalculated post-move | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 positional wager fires on submission | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; repositioning aligns with tactical doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | source and target both district.named; adjacency enforced in restriction; ChorusNode excluded from both | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken in restriction and as target; Mandate cost; adjacency per district_adjacency table | Art 02a §6; Art 02a §8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; tokens moved before Beat 3 resolution; entry qualification and move count resolution outstanding (Outstanding Issues) | Art 03 §9, §11 |

#### Outstanding Issues

- **Entry qualification check:** `arbiter_note` states that if Directorate does not qualify for entry at the destination, the card is discarded without effect (resources not refunded). Confirm "qualify for entry" criteria — is there a district-entry restriction in Art 01 or Art 03?
- **Move count vs. restriction:** Restriction requires source.presence >= 1 but the card moves count=2. Can the card be played if source has only 1 token (moving fewer than 2)? Confirm whether count=2 is a maximum or exact.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*S51 redesign — design rationale scaffold added S59. Design pass pending.*

```python
C25 = Card(
    id=25,  version="v1.0",
    name    = "Tactical Redirection",
    tagline = "Reposition institutional presence ahead of a contested exchange.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Move,  subject = PresenceToken,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=district.adjacent(source), target_faction=faction(acting), target_object=PresenceToken,
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
    design_note  = "Replaces C25 Sealed Border (retired S51). Fills Territory — Move — Presence token gap; no other card in the full set uses this verb + subject combination. Most impactful before Battlefield Strength when district control margins are tight.",
    arbiter_note = "Move named Directorate presence tokens from source to destination. Adjacency confirmed against district adjacency table. Entry requirements rechecked at destination — if Directorate does not qualify for entry, card is discarded without effect (resources not refunded). Control flags and Established markers recalculated after move.",
)
```

---

### Directorate — REGULATORY DOWNGRADE
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's active tier suppression play — declared publicly at Phase B, resolved at Beat 4. The card stays on the Overview as the persistent condition: no separate marker component needed. Target faction collects resources in the named district as one tier lower (resource generation only; actual presence count still governs control tier for win-condition calculations). Cleared when target pays 2 native to Reservoir — available any time after Beat 4 resolution, including immediately. Economics: clearing same Quarter costs the target 2 native (net 3 from a full Core+structure district). Each Upkeep with the card active costs −1 resource generation plus the eventual 2 to clear. Directorate spent 3 Mandate for a guaranteed minimum 2-resource drain; compounding if target delays. Paired with Regulatory Freeze: Downgrade is the active suppression play once a faction is entrenched; Freeze is the cheaper preventive play to gate lower-tier factions out of advancement.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public institutional reclassification — declared openly, contested in Countermeasure window, persistent economic suppression | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — reclassification as institutional act | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; target must be Established+; public act fits regulatory authority doctrine — the Directorate does not act in secret when it reclassifies | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) — institutional reclassification is public, permanent, and Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Modify/InfluenceTier — card on board IS the condition; no separate component needed | Art 04b §4, §5 |
| Balance | ✓ | Mandate×3, Automatic; guaranteed economic suppression; minimum 2-native drain on target; compounding cost per Upkeep delayed | Art 02a §6–§7 |
| Effect duration | ✓ | Permanent — card stays on Overview until persistence_condition met | — |
| Persistence | ✓ | Permanent public act; `persistence_condition` = target pays 2 native to Reservoir; card removed on payment | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — reclassification aligns with regulatory authority doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — card on Overview is the persistent condition | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Phase B declaration → Countermeasure window → Beat 4 Automatic resolution; standard Permanent Public Act lifecycle | Art 03 §9, §11 |

#### Outstanding Issues

- **Win-condition scope:** Resource generation tier penalty only — actual presence count governs control tier for Dominance/Established win-condition calculations. Needs explicit statement in Art 03 Upkeep Step 5 procedure or Art 07 reference. Tracks under 04-n27.
- **Freeze interaction:** If Downgrade and Freeze are both active on the same faction/district simultaneously, combined effect is: one tier down for resource gen + blocked from tier advancement. Needs explicit procedure note confirming coexistence is valid and no additional interaction applies.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Redesigned S67 — v2.0. CovertOperation → PublicAct. TierPenaltyMarker removed; card-as-condition pattern.*

```python
RegulatoryDowngrade = Card(
    id=TBD,  version="v2.0",
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

    affinity    = None,
    restriction = faction(target).influence_tier(district(target)) >= Established,
    cost        = resource.faction(acting).mandate * 3,

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

### Directorate — REGULATORY FREEZE
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Preventive tier suppression — lighter than Regulatory Downgrade but cheaper and automatic. Where Downgrade reduces an existing tier, Freeze prevents advancement from the current tier. Applied against Present or Established factions to gate them out of higher-tier resource generation before they consolidate. Cost Mandate×2 and Automatic resolution reflect that issuing a regulatory ceiling is a procedural act, not a contested operation. No ring_mod — administrative acts carry the same institutional weight anywhere in New Meridian. Clearing is deliberately cheaper than Downgrade (1 native vs 2) because a ceiling is a future constraint, not a reclassification of existing status.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Preventive tier suppression — cheaper alternative to Regulatory Downgrade; blocks advancement from current tier; paired with Downgrade for full suppression toolkit | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design — administrative tier ceiling as institutional act | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Mandate×2, Automatic — procedural institutional act; Dominant restriction by design (Outstanding Issue for documentation); no ring_mod consistent with administrative nature | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — regulatory tier ceiling is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Block/InfluenceTier — blocks tier advancement; TierFreezeMarker registration outstanding (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic — 1-Mandate cheaper than Downgrade; Automatic vs Probabilistic calibration noted; clearing 1 native vs Downgrade 2 native is intentional (ceiling vs reclassification) | Art 02a §6–§7 |
| Effect duration | ✓ | Persistent: TierFreezeMarker until cleared (1 native spend or Absent) | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; tier ceiling aligns with regulatory authority doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — standard zone targeting | Art 01 §6–§7 |
| Supported by components | ✓ | TierFreezeMarker registration outstanding (Outstanding Issue); placement at Beat 3 | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; marker placed at Beat 3; simultaneous marker interaction with Downgrade outstanding (Outstanding Issue) | Art 03 §9, §11 |

#### Outstanding Issues

- **TierFreezeMarker component:** New component not yet registered in Art 02. Needs fields: `faction | district | tier_cap`. Confirm: excess presence placements that would advance tier — are they returned to supply or simply denied?
- **Dominant restriction by design:** Freeze restricted to Present or Established — cannot freeze a Dominant faction. This is intentional (a preventive tool cannot act on the top tier), but needs explicit documentation in 00a or Art 04 §6.5.
- **Simultaneous marker interaction:** See Regulatory Downgrade outstanding issue — both markers in same district on same faction needs combined-effect clarification.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Draft S59 — design pass pending*

```python
RegulatoryFreeze = Card(
    id=TBD,  version="v1.0",
    name    = "Regulatory Freeze",
    tagline = "Block a faction from advancing their institutional standing in a target district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Block,  subject = InfluenceTier,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None,
    trigger=None,
    resolution_type="Transactional", outcome_type=None,
    target_district=district.named, target_faction=faction(named_opponent), target_object=None,
    affinity=None,
    restriction = faction(target).influence_tier(district(target)) in [Present, Established],
    cost        = resource.faction(acting).mandate * 2,
    success     = arbiter.place(TierFreezeMarker(faction=faction(target)), district(target)),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "Forward progress in this district has been administratively paused. The Directorate is still reviewing.",
    perspectives = {Directorate: "They can build all they want. The tier ceiling is established. They will not pass through it."},
    design_note  = "TierFreezeMarker: target faction cannot advance above current tier in district while marker is in place. Permanent per Principle 11. Clearing: target spends 1 native resource OR target reaches Absent. Paired with Regulatory Downgrade for full suppression toolkit.",
    arbiter_note = "Place TierFreezeMarker on target faction in target district. While marker is present: deny any presence placement that would advance target above their current tier — return excess tokens to supply. Clear: target pays 1 native resource (at upkeep or voluntarily) OR target reaches Absent — remove marker and announce.",
)
```

---

### Directorate — SANCTIONED RAID
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's maximum-force removal card — removes all of a target faction's presence tokens from a district, ignoring all blocks, countermeasures, and protect operations. The "sanctioned" framing reflects that the Directorate is not acting covertly but institutionally: the Intel token is the authorization document, not a tradecraft requirement. Threshold 25 is the hardest in the Directorate set — making this a high-risk/high-reward play that requires both Intel investment and dice luck. Where C22 Detain removes a deployment marker (permanently, probabilistic), Sanctioned Raid removes all presence tokens (also permanent removal) at a much harder threshold but also bypasses all defenses. Migrated from §8 Intel Economy block.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Maximum-force removal — removes ALL target presence tokens from a district, bypassing all defenses; highest-impact Directorate territorial play | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design — sanctioned institutional action | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; threshold 25 (hardest in set) compensates for block-bypass; PS −1 on success distinguishes institutional weight from suppression; Intel token authorization outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — block-bypass authority is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Remove/PresenceToken — permanent all-token removal; block-bypass scope outstanding (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2 + IntelToken, threshold 25 — lowest threshold compensates for block-bypass; dominant play risk outstanding (Outstanding Issue) | Art 02a §6–§7 |
| Effect duration | ✓ | Permanent: all presence tokens removed; faction rebuilds from zero | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter; PS −1 on success is game effect (not portrait), confirmed per P12 | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — all target presence tokens in specific district | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken as target; Mandate + IntelToken costs; NotificationSlip on failcrit; no new components | Art 02a §6, §8; Art 02b §7–§8 |
| Supported by game procedure | ✓ | Beat 3 d100; block-bypass procedure outstanding (Outstanding Issue); ARBITER removes all tokens | Art 03 §9, §11 |

#### Outstanding Issues

- **Block-bypass scope:** Card "ignores Block cards, Type A and Type B Countermeasures, and Protect operations." Confirm this is exhaustive — does it also bypass C10 Protect (Standard), C11 Fortify Structure (Guild), C21 Invoke Jurisdiction (Directorate)? Art 03 §11 must explicitly authorize the bypass.
- **Intel token faction-keying:** Original spec requires IntelToken for target faction. Confirm: does the Intel token consumed need to be keyed to `faction(target)` (like SCIF/Flip) or is it any held token? The flat format says "Intel token" without faction-keying — clarify at schema pass.
- **No PS penalty on success:** The original design note explicitly states "no Public Standing penalty to acting faction." This differentiates Sanctioned Raid from similar violent actions. Confirm this is locked.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Migrated from §8 Intel Economy block to Directorate extended section S59. Pre-convention flat format — full schema pass pending (04-47).*

```python
C42 = Card(
    id=42,  version="v1.1",
    name    = "Sanctioned Raid",
    tagline = "Not every operation leaves a paper trail.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Remove,  subject = PresenceToken,
    beat=3, resolution=d100, threshold=25, ring_mod={0:-15,1:-10,2:0,3:+10},
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    target_district=district.named, target_faction=faction(named_opponent), target_object=PresenceToken,
    affinity=Directorate,
    restriction=None,
    cost        = resource.faction(acting).mandate * 2 + IntelToken(faction=faction(target)) * 1,
    success     = [game.remove(faction(target).presence_tokens, district(target), count=all, ignore_blocks=True),
                   faction(acting).standing -= 1],
    successcrit = resource.faction(acting).mandate += 1,
    fail=None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate does not ask permission. It records the action and moves on.",
    perspectives = {Directorate: "The intelligence warranted the action. The action was authorised. There is nothing further to say."},
    design_note  = "Ignores Block cards, Type A and Type B Countermeasures, and Protect operations. PS −1 on success: sanctioned but a sweep still carries institutional weight. Mandate×2 balances 'ignore all blocks' + 'remove ALL' scope. Threshold 25: hardest in Directorate set. Intel token faction-keying confirmation outstanding. Migrated from §8 Intel Economy block. See 04-n13: Network should have a modifier card that can auto-trigger off a Directorate sweep.",
    arbiter_note = "At resolution: bypass all countermeasure and protect checks. Remove ALL named faction's presence tokens from named district. Reduce Directorate PS by 1 (visible). Crit success: also return 1 Mandate to Directorate. Crit fail: deliver NotificationSlip to target — no other effect.",
)
```

---


---

### Directorate — Public Acts
[↑ Directorate](#directorate)

| Card | Name |
|------|------|
| [P11](#p11-regulatory-override) | Regulatory Override |
| [P12](#p12-convene-an-inquiry) | Convene an Inquiry |
| [—](#directorate-entryexit-controls) | Entry/Exit Controls |
| [—](#directorate-standing-injunction) | Standing Injunction |

### P11 — REGULATORY OVERRIDE
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's district-level regulatory control PA. All non-Directorate presence-placement actions (cards that Add PresenceTokens) in the named district cost +1 native for the remainder of the Quarter. Persistence = Seasonal: the PA card (or RegulatoryOverrideMarker) stays on the table as an active condition marker until Phase 21 or Directorate goes Absent from the district. This is the structural counter to Guild's build pace — raising the cost of the presence prerequisite that enables P03/P09. Restriction: Directorate must have Established in the district to invoke jurisdictional authority.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Directorate regulatory authority over district operations is core to their institutional doctrine | Art 00 §7 |
| Voice fit | ✓ | Directorate on-doctrine; Ghost (aligned): observe who stops crossing; Network (opposed): regulation as toll | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Directorate institutional regulatory authority: Mandate × 2 cost, Established restriction (jurisdictional legitimacy), PS +1. Shapes all other factions' territorial economics in the district. Directly serves Directorate control doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Modify / PresenceToken — modifies the cost of PresenceToken placement actions | Art 04b §4 |
| Balance | ⚠ | Seasonal scope at 2 Mandate is strong — affects all remaining Months of Quarter. Single district only. Balance subject to playtesting | Art 02a §6–§7 |
| Effect duration | ✓ | World condition is Seasonal (within-Quarter, cleared at Phase 21 or Directorate Absent). No multi-Quarter duration. Consistent with 00-R21 | 00-R21 |
| Persistence | ✓ | Seasonal — P11 card / RegulatoryOverrideMarker stays on district until Phase 21 or Directorate Absent | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid; restriction checks Directorate's influence tier in the district (valid zone condition) | Art 01 §6–§7 |
| Supported by components | ⚠ | RegulatoryOverrideMarker is a new component — register in Art 02a before production | Art 02a; Art 03 §11 |
| Supported by game procedure | ⚠ | World condition application to PresenceToken.Add actions needs ARBITER tracking protocol. RegulatoryOverrideMarker component registration required | Art 03 §11; Art 02a |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
P11 = Card(
    id="P11",  version="v1.0",
    name    = "Regulatory Override",
    tagline = "Declare a district under Directorate oversight, raising the cost of all non-Directorate presence operations.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Directorate,

    layer    = Territory,  function = Modify,  subject = PresenceToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Seasonal,  # P11 card / RegulatoryOverrideMarker stays on district until Phase 21

    target_district = district.any,
    target_faction  = faction.all_except(Directorate),
    target_object   = None,

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
    design_note  = "District-level regulatory PA. +1 native cost on all non-Directorate PresenceToken.Add actions in district for remainder of Quarter (Seasonal). Physical marker on district; card stays on table as marker. Counter to Guild P03/P09 build chain — raises cost of presence prerequisite. Restriction: Directorate Established+ in district. Multiple P11s may target different districts. Balance review pending playtesting.",
    arbiter_note = "Beat 4: place RegulatoryOverrideMarker on declared district. P11 card stays on table as marker. Apply +1 native cost to all non-Directorate presence-placement actions (C03 Campaign, P01 Open Operations, C08 Buy Influence, P09 Civic Works Mandate) targeting this district for remaining Months of Quarter. Directorate PS +1. Clear: Directorate Absent in district (remove immediately) OR Phase 21 cleanup. Multiple markers on different districts tracked independently.",
)
```

---

### P12 — CONVENE AN INQUIRY
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's institutional intelligence-gathering PA. No formal restriction — Directorate can always commission an inquiry. The yield (Intel tokens) is determined by ARBITER's count of publicly attributed covert actions against the target faction in the last 2 months (from resolved P04/P05 outcomes this Quarter). Zero yield if no prior attribution groundwork was laid — 3 Mandate wasted. This creates a two-step sequence incentive: P04/P05 → P12. Distinct from Ghost's C05 (Gather): Directorate uses ARBITER as the collection mechanism rather than operational fieldwork.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional investigation via ARBITER is Directorate's mode of intelligence — not covert fieldwork | Art 00 §7 |
| Voice fit | ✓ | Directorate on-doctrine; Guild (aligned): institutional process produces verifiable record; Syndicate (opposed): operating margin is what the record cannot reach | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Directorate commissions ARBITER investigation (not covert fieldwork): 3 Mandate, yield contingent on prior P04/P05 groundwork. Creates two-step sequence incentive (P04/P05 → P12). Portrait +1: submitter-bounded | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Add / IntelToken | Art 04b §4 |
| Balance | ✓ | 3 Mandate cost is high. Yield 0–2 tokens depending on prior P04/P05 outcomes. Expensive gamble without groundwork; reliable payoff when chain is set up | Art 02a §6–§7 |
| Effect duration | ✓ | IntelToken delivery and PS shifts are immediate; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no zone reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (yielded by ARBITER from supply, Art 02a §6); Mandate × 3 cost (Art 02a §8) | Art 02a §6, §8 |
| Supported by game procedure | ✓ | ARBITER tracks P04/P05 resolution outcomes; yields based on that record | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P12 = Card(
    id="P12",  version="v1.0",
    name    = "Convene an Inquiry",
    tagline = "Commission an ARBITER-mediated institutional investigation into a faction's recent operations.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Directorate,

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

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    affinity    = None,
    restriction = None,  # no public restriction; yield is variable (0–2) based on ARBITER's record
    cost        = resource.faction(Directorate).mandate * 3,

    success = (
        arbiter.provide_intel_tokens(
            target    = target_faction,
            count     = arbiter.count_attributed_actions(target_faction, months=2),  # 0–2; 0 if no prior P04/P05
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
    design_note  = "Directorate intelligence PA via institutional channel. No restriction — always available. Yield: 1 Intel token per publicly attributed covert action against target faction in last 2 months (from successful P04 or P05 this Quarter). 0 tokens = 3 Mandate wasted (costly gamble without prior groundwork). Distinct from Ghost C05 Gather (covert fieldwork). Creates two-step sequence incentive: P04/P05 → P12.",
    arbiter_note = "Beat 4. Count: how many successful P04 or P05 resolutions named this target faction this Quarter? Provide Directorate with that many Fresh Intel tokens (max 2). Apply PS: target −1, Directorate +1. If count = 0: no tokens delivered. 3 Mandate spent regardless.",
)
```

---

### Directorate — ENTRY/EXIT CONTROLS
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's persistent territorial control tool — a district-level board condition that displaces non-Directorate deployment markers immediately and blocks future placement in the named district. Distinct from Invoke Jurisdiction (C21), which blocks specific card types in a single district for one Beat: Entry/Exit Controls operates on deployment marker movement, persists across rounds and Quarters, and is self-policing via persistence_condition (auto-discards if Directorate loses Established status). PS −1 at resolution reflects the public backlash of establishing hard movement restrictions. Removal requires a counter-action — new card type TBD (PM05).

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | District-level movement control — displaces markers immediately; blocks future placement; distinct from C21 (card-type block) and C25 (repositioning) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — regulatory authority as territorial infrastructure | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Mandate×3 for permanent district lock; Established restriction (jurisdictional legitimacy requires institutional presence) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Directorate) — district-level movement authority is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Block/DeploymentMarker — hard block on placement is the function | Art 04b §4, §5 |
| Balance | ✓ | Mandate×3, permanent district lock, PS −1 — cost TBD playtesting | Art 02a §6–§7 |
| Effect duration | ✓ | Permanent — persists until counter-acted or persistence_condition fails | — |
| Persistence | ✓ | Permanent; persistence_condition auto-discards on Directorate falling below Established in named district | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction requires Directorate Established in named district | — |
| Portrait validity | ✓ | Directorate submitter=+1; PS −1 in success field is a game effect, not portrait | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — standard targeting | Art 01 §6–§7 |
| Supported by components | ✓ | Operates on deployment markers (existing component); no new component required | Art 02a §6–§8 |
| Supported by game procedure | ⚠ | Beat 4 PA resolution defined; persistence_condition monitoring trigger not yet in Art 03 (PM05 04-n29 — blocks Issues Resolved) | Art 03 §9 |

#### Outstanding Issues

- **Counter-card removal:** Card sits in Directorate's PA area as a permanent board condition. Removal by counter-action requires new card type(s) — design TBD. See PM05 04-n29.
- **Art 03 persistence monitoring:** ARBITER needs a defined trigger point to check persistence_condition of all permanent PA cards (e.g., after any influence tier change). See PM05 04-n29. Blocks Issues Resolved.
- **Displaced faction with no presence elsewhere:** `move_to=district.where(faction.has_presence)` has no valid destination if the displaced faction holds no presence outside the named district. Fallback rule needed — e.g., marker is returned to hand (faction skips next placement) or moved to Baryo as unconditional fallback (00-R13b: no elimination).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Redesigned S66 — v1.0 (ring-scope) retired*

```python
EntryExitControls = Card(
    id=TBD,  version="v2.0",
    name    = "Entry/Exit Controls",
    tagline = "Designate a district as a controlled zone — displacing non-Directorate deployment markers and blocking future placement.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Block,  subject = DeploymentMarker,
    beat=4,  resolution=Automatic,  threshold=None,  ring_mod=None,
    trigger=None,
    resolution_type="Transactional",  outcome_type=Unilateral,
    persistence           = Permanent,
    persistence_condition = faction(acting).influence_tier(district.named) >= Established,
    target_district = district.named,
    target_faction  = faction.all_except(Directorate),
    target_object   = None,
    affinity=None,
    restriction = faction(acting).influence_tier(district.named) >= Established,
    cost = resource.faction(acting).mandate * 3,
    success = (
        for_each(
            deployment_marker(faction=faction.all_except(Directorate), district=district.named),
            arbiter.instruct(marker.owner, move_to=district.where(faction.has_presence), flip_to=Blocked),
        ),
        game.board_condition(
            scope    = district.named,
            effect   = placement(faction.all_except(Directorate), type=DeploymentMarker).blocked,
            duration = Permanent,
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
Directorate's pre-emptive PA block — distinct from P11 Regulatory Override (which raises presence-placement cost) and C21 Invoke Jurisdiction (which blocks a specific card type for one Beat in one district). Standing Injunction blocks the next instance of a named PA type from a named faction for the entire Quarter or until triggered. The Seasonal persistence and 3 Mandate cost reflect the institutional weight of a formal injunction. The partial Mandate refund on Phase 21 expiry (untriggered) provides a safety valve against pure deterrent plays that are never triggered. PS +1 at placement reflects the public legitimacy signal of filing the injunction. Restriction: Directorate must share a ring with target's operations — institutional authority requires operational footprint overlap.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pre-emptive institutional block on a named PA type is Directorate doctrine — controlling the space of permissible action rather than reacting after the fact | Art 00 §7 |
| Voice fit | ✓ | Directorate on-doctrine; Ghost (aligned) recognizes structural pre-emption as correct; Network (opposed) names it as information control | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Directorate exclusive: Mandate × 3, Established restriction, PS +1. Pre-emptive control over PA space is core Directorate doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Directorate): only Directorate would use institutional mechanism to pre-emptively block a named PA type | Art 04 §6.2 |
| Taxonomy fit | ✓ | Submission / Block / PoliticalAct — blocks a PA from entering the resolution queue | Art 04b §4 |
| Balance | ⚠ | 3 Mandate for a Seasonal block on a specific PA type. Partial refund (1 Mandate) on Phase 21 expiry reduces deadweight loss. Balance review pending playtesting — single PA type block may be too narrow or too powerful depending on table state | Art 02a §6–§7 |
| Effect duration | ✓ | Seasonal — marker stays until triggered or Phase 21 | 00-R21 |
| Persistence | ✓ | Seasonal — InjunctionMarker stays on table face-up as active condition indicator | Art 04 §6 |
| Trigger validity | ✓ | trigger = None at placement; trigger condition is target declaring blocked PA type at Phase B | — |
| Portrait validity | ✓ | Directorate +1: submitter-bounded; placing a public institutional block is maximum doctrinal expression | Art 04 §6.2 |
| Supported by zones | ⚠ | Restriction: "Directorate Established+ in any district where target also has Established+" — "primary ring" wording from sketch replaced; confirm intent. No district-level target — faction-targeted | Art 01 §6–§7 |
| Supported by components | ⚠ | InjunctionMarker is a new component — Art 02a registration required. Queue for agy DB-S63-02 extension | Art 02a |
| Supported by game procedure | ⚠ | Trigger behavior requires ARBITER to track active injunctions across Phase B declarations for remaining Months of Quarter. Voiding a declared PA at Phase B is not yet covered in Art 03 §9 procedure. Phase 21 Mandate refund needs Upkeep/EoQ procedure note | Art 03 §9, §19 |

#### Outstanding Issues

- **⚠ Restriction wording:** "Directorate Established+ in any district where target also has Established+" — confirm this is the right gatekeeping intent vs. the original sketch's "same ring as primary operations."
- **⚠ InjunctionMarker:** New component — Art 02a registration required.
- **⚠ PA type declaration:** Blocked by card name (e.g., "Open Operations") or by taxonomy (Territory/Add). Current spec: by card name. Taxonomy block would be more powerful and harder to execute at the table.
- **⚠ Art 03 gap:** Phase B procedure for voiding a declared PA not yet specified. ARBITER needs a defined protocol for checking active injunctions when target declares a PA type.
- **⚠ Accord overlap:** Confirm PoliticalAct block applies to all PA types including BilateralAgreement (P08/P10) — or is Accord-targeting excluded?

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
P_StandingInjunction = Card(
    id      = "—",  version = "v1.0",
    name    = "Standing Injunction",
    tagline = "Place a conditional block on a named faction's next declared act of a specified type.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Directorate,

    layer    = Submission,  function = Block,  subject = PoliticalAct,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Seasonal,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = PoliticalAct(type=declared),  # declared card type at Phase B

    affinity    = None,
    restriction = faction(Directorate).influence_tier(district.any_where(faction(target).influence >= Established)) >= Established,
    cost        = resource.faction(Directorate).mandate * 3,

    success = (
        arbiter.place(InjunctionMarker(target=target_faction, blocked_pa=declared_pa_type)),
        faction(Directorate).standing += 1,
        # on trigger (target declares blocked PA type at Phase B any subsequent Month):
        #   PA voided; resources returned; target PS −1; InjunctionMarker removed
        # on Phase 21 expiry (untriggered):
        #   InjunctionMarker removed; Directorate recovers 1 Mandate
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Directorate: PortraitEntry(submitter=+1)},

    narrative    = "The Injunction does not prevent the act. It establishes that the act will carry costs the target has not yet calculated.",
    perspectives = {
        Directorate: "The Injunction does not prevent the act. It relocates its costs.",
        Ghost:       "Directorate pre-empts the declaration rather than reacting to it. We recognize this as the structurally correct approach.",  # aligned
        Network:     "A pre-emptive block on a public act is the Directorate deciding which information enters the record. We have a word for that.",  # opposed
    },
    design_note  = "⚠ Multiple open design questions — see Outstanding Issues. Seasonal PA block; InjunctionMarker face-up on table as active condition. Trigger: target declares blocked PA type at Phase B → void PA, return resources, target −1 PS, remove marker. Phase 21 untriggered: Directorate recovers 1 Mandate. Distinct from P11 (cost increase on presence placement) and C21 (single-Beat block in one district). Restriction: Directorate shares ring with target's operations — institutional authority requires footprint overlap.",
    arbiter_note = "Phase B: Directorate names target faction + PA card type (by card name). Beat 0: restriction check. Beat 4: place InjunctionMarker face-up on table. Directorate +1 PS. From next Month onward: at each Phase B, check if target faction declares the blocked PA type — if yes, void that PA (resources returned, target −1 PS, announce 'Standing Injunction applied', remove marker). Phase 21: if marker still present, return 1 Mandate to Directorate, remove marker.",
)
```

---


---

## Network
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#network-covert-operations) · [Public Acts](#network-public-acts)

---

### Network — Covert Operations
[↑ Network](#network)

| Card | Name |
|------|------|
| [C26](#c26-leak) | Leak |
| [C27](#c27-disclosure-loop) | Disclosure Loop |
| [C28](#c28-open-channel) | Open Channel |
| [C29](#c29-network-cascade) | Network Cascade |
| [C30](#c30-community-anchor) | Community Anchor |
| [—](#network-sacrifice) | Sacrifice |
| [—](#network-weaponized-transparency) | Weaponized Transparency |

### C26 — LEAK
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's attribution revelation card — spends 1 Exposure to force a target faction's highest-impact covert operation's target district into public record after Beat 3 resolution. Operation type is not revealed, only the district — enough information to trigger table reactions without fully exposing the target. Automatic resolution reflects that The Network's broadcast infrastructure makes district leaks routine; the cost is resources, not probability. No restriction means Leak can fire regardless of Network's own position. Pairs with C27 Disclosure Loop (Leak → free Exposure) to make revelation self-sustaining.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Attribution revelation via broadcast infrastructure — district-only post-resolution reveal; lighter than C28 (full round, pre-resolution) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — selective disclosure as doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Exposure×1 cost; Automatic — broadcast infrastructure makes district leaks routine; "highest-impact op" definition outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — broadcast-based attribution is Network-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/ActionAttribution — district-only reveal (not operation type); pairs with C27 Disclosure Loop | Art 04b §4, §5 |
| Balance | ✓ | Exposure×1, Automatic, district-only — relatively cheap for attribution intel; "highest-impact op" ranking outstanding (Outstanding Issue) | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: district announced after Beat 3 resolution; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Network +1 submitter; broadcast attribution aligns with transparency doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — reveals the district but targets a faction, not a zone | Art 01 §6–§7 |
| Supported by components | ✓ | ActionAttribution as target_object — component registration outstanding (Outstanding Issue) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; announcement post-Beat 3 resolution; ordering with other Beat 3 outcomes noted | Art 03 §9, §11 |

#### Outstanding Issues

- **"Highest-impact op" ranking:** `op(beat=3, rank=highest_impact)` — "highest impact" is undefined. Ranking criteria needed: by resource spent, by effect scope, by player declaration? Needs formal definition before checklist passes.
- **C26/C28 Reveal overlap:** Flagged in section header (D-04-04). C26 reveals district of one op post-resolution; C28 redirects all notifications of a faction to public pre-resolution. Different scopes and timings — confirm the distinction is sufficient to keep both cards or resolve one.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C26 = Card(
    id=26,  version="v1.0",
    name    = "Leak",
    tagline = "Make one resolved operation's target district public after resolution.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Information,  function = Reveal,  subject = ActionAttribution,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=None, target_faction=faction(named_opponent), target_object=ActionAttribution,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).exposure * 1,
    success     = game.announce(faction(target).op(beat=3, rank=highest_impact).district, public=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The Network does not need to know everything — only enough to make the right question public.",
    perspectives = {Network: "We do not reveal everything. We reveal the piece that makes everything else visible."},
    design_note  = None,
    arbiter_note = "Announce target district of highest-impact resolved covert operation from named faction this round — operation type not revealed, district only. Delivered after Beat 3 resolution.",
)
```

---

### C27 — DISCLOSURE LOOP
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's Exposure generation card — converts the act of revealing into additional broadcast capacity. Spends 1 Finding; if Network successfully resolved any Reveal card this round, delivers +1 Exposure. The loop is the mechanic: reveal with C26 or C28, then play C27 to convert that act into more Exposure for future reveals. Replaced C27 Source Protection (S51) which was doctrinally misaligned — protecting attribution is Ghost's register. The conditional success (`if reveal_resolved_this_round >= 1`) means C27 only pays out when Network is actively broadcasting; a C27 played in isolation does nothing, burning only the Finding cost.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Exposure generation from reveal activity — self-sustaining broadcast loop; dead-weight if used in isolation, which is the intended design | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — loop as resource doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Findings×1 low cost; conditional payoff requires active reveal this round; replaces retired Source Protection (doctrinally misaligned) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — Exposure amplification is Network infrastructure | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/Exposure — converts reveal activity to resource; Economy layer correct | Art 04b §4, §5 |
| Balance | ✓ | Findings×1 for conditional Exposure — low cost; isolation dead-weight is intentional cost gate; conditional cost resolution outstanding (Outstanding Issue) | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: Exposure delivered at Beat 3 cleanup | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | Conditional success — `reveal_resolved_this_round >= 1` is inline trigger; trigger vs. success field distinction outstanding (Outstanding Issue) | — |
| Portrait validity | ✓ | portrait = {} — Disclosure Loop is internal resource infrastructure, not a visible doctrinal act; absence confirmed intentional (Outstanding Issue) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — self-targeting; no district context | Art 01 §6–§7 |
| Supported by components | ✓ | Exposure as subject; Findings cost; no new components | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 3 cleanup; ARBITER tracks Reveal card resolutions this round; conditional resolution outstanding (Outstanding Issue) | Art 03 §9, §11 |

#### Outstanding Issues

- **Conditional success modelling:** `success = exposure += 1 if reveal_resolved_this_round >= 1 else None` — confirm whether the "else None" path consumes the Finding cost (card slot and Findings are spent, no outcome) or refunds it. Current design note says "the slot cost was the investment" — confirm.
- **portrait = {} justification:** Empty portrait for a Network FactionSpecific card is uncommon. Confirm intentional — Disclosure Loop is an internal resource mechanism, not a visible doctrinal act.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*S51 redesign — design rationale scaffold added S59. Design pass pending.*

```python
C27 = Card(
    id=27,  version="v1.0",
    name    = "Disclosure Loop",
    tagline = "Transparency is self-sustaining. Revealing information generates the capacity to reveal more.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Economy,  function = Add,  subject = Exposure,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=None, target_faction=faction(acting), target_object=None,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).findings * 1,
    success     = resource.faction(acting).exposure += 1 if faction(acting).reveal_resolved_this_round >= 1 else None,
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "The act of disclosure is not only a tactic. It is a resource. The Network learned this before anyone else at this table.",
    perspectives = {Network: "We revealed something. Now we can reveal something more. The loop is already running."},
    design_note  = "Replaces C27 Source Protection (retired S51). Source Protection was doctrinally misaligned — protecting attribution is Ghost's register, not Network's. Pairs with C26 Leak and C28 Open Channel.",
    arbiter_note = "At Beat 3 cleanup, check whether any Network Reveal card resolved successfully this round. If yes, deliver 1 Exposure to Network's resource pool. If no Reveal resolved, card takes effect but produces nothing — the slot cost was the investment.",
)
```

---

### C28 — OPEN CHANNEL
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's pre-emptive transparency card — placed at Beat 2, redirects all of a target faction's ARBITER case notifications for the round to public delivery. Where C26 Leak reveals one specific piece of attribution after the fact, Open Channel opens the pipeline before it runs. Any Intel Delivery Slips, Notification Slips, or other ARBITER-to-faction private communications generated for the target this round are delivered publicly instead. Higher cost (Exposure×2) reflects the broader scope. The Beat 2 timing is essential: must be placed before Beat 3 notifications are generated. Does not intercept Hidden Objective or Classified Directive communications — those are ARBITER-to-ARBITER constructs, not faction notifications.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pre-emptive transparency — opens pipeline before notifications are generated; distinct from C26 (post-resolution, one op, district-only) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — forced transparency as doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Exposure×2 for broader scope; Beat 2 timing essential — must precede Beat 3 notification generation; HO/CD exclusion confirmed | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — pipeline redirect is Network-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/PrivateCommunications — round-wide redirect vs C26 single-op; C26/C28 overlap outstanding (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | Exposure×2, Beat 2 Automatic, round-wide redirect — higher cost than C26 justified by broader scope | Art 02a §6–§7 |
| Effect duration | ✓ | One round: notifications generated this round delivered publicly; no carry-forward | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — Beat 2 placement fires on submission | — |
| Portrait validity | ✓ | Network +1 submitter; forced transparency aligns with broadcast doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no zone restriction | Art 01 §6–§7 |
| Supported by components | ✓ | PrivateCommunications as target_object — component scope outstanding (Outstanding Issue); Intel Delivery Slips and Notification Slips confirmed | Art 02a §6–§8; Art 07 |
| Supported by game procedure | ✓ | Beat 2 Automatic; redirect applied before Beat 3 generation; HO/CD exclusions confirmed in arbiter_note | Art 03 §9, §11 |

#### Outstanding Issues

- **C26/C28 Reveal overlap (D-04-04):** Both cards are Information — Reveal. C26: post-Beat 3, district-only, one op. C28: pre-Beat 3, all notifications, whole round. Scope and timing are genuinely different. Confirm both cards survive the D-04-04 review or whether one should be retired/merged.
- **PrivateCommunications component:** Undefined. Needs Art 02/Art 07 definition: which ARBITER-to-faction communications are "notifications" in scope of C28? Intel Delivery Slips, Notification Slips confirmed. Confirm scope edge cases.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C28 = Card(
    id=28,  version="v1.0",
    name    = "Open Channel",
    tagline = "Force private ARBITER notifications to a faction to be delivered publicly.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Information,  function = Reveal,  subject = PrivateCommunications,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=None, target_faction=faction(named_opponent), target_object=PrivateCommunications,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).exposure * 2,
    success     = game.redirect(faction(target).notifications(round=game.round), destination=public),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "Secret communications between powerful institutions are themselves a form of harm. Opening the channel is the argument.",
    perspectives = {Network: "If it happened, it should be known. We are simply making that principle operational."},
    design_note  = "Flagged for review — C26 and C28 both Reveal, same function different scope. See D-04-04.",
    arbiter_note = "Does not intercept Hidden Objective or Classified Directive communications. Beat 2 — must be active before Beat 3 notifications are generated.",
)
```

---

### C29 — NETWORK CASCADE
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's signal propagation card — extends C06 Broadcast Interference's Public Act cost increase to an adjacent district on the same round. Mechanically ties the two cards together: C06 must be submitted in the same round for C29 to fire. This creates a planned two-card combo: pay the C06 Exposure cost to disrupt PA activity in one district, then pay C29's Exposure×2 to extend that disruption to an adjacent district. The "signal propagation" framing is doctrinally exact — The Network understands that broadcast interference is not bounded by administrative district lines. Beat 2 Automatic means both disruption effects land before Beat 4 PA resolution.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Signal propagation — extends C06 Broadcast Interference to adjacent district; mechanically implements "broadcast doesn't stop at district borders" doctrine | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — signal propagation as operational reality | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; requires C06 same round (restriction); Exposure×2; Beat 2 Automatic — both disruption effects land before Beat 4 PA resolution | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — signal propagation is Network-exclusive two-card mechanic | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Submission/Modify/PoliticalAct — extends C06's PA cost increase to adjacent district | Art 04b §4, §5 |
| Balance | ✓ | Exposure×2 for adjacency extension; total combo cost outstanding calibration noted; C06 dependency limits use | Art 02a §6–§7 |
| Effect duration | ✓ | One round: PA cost increase applies this round's Beat 4 PA phase only | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | C06 submission as restriction prerequisite; submission ordering and void-on-C06-cancel outstanding (Outstanding Issues) | — |
| Portrait validity | ✓ | Network +1 submitter; signal extension aligns with broadcast doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = adjacent to C06.target_district; dependency resolution outstanding (Outstanding Issue) | Art 01 §6–§7 |
| Supported by components | ✓ | PoliticalAct as target_object; Exposure cost; no new components | Art 02a §6–§8; Art 04b §5 |
| Supported by game procedure | ✓ | Beat 2 Automatic; PA cost increase at Beat 4; C06 submission ordering outstanding (Outstanding Issue) | Art 03 §9, §11, §17 |

#### Outstanding Issues

- **C06 dependency at Dispatch:** Restriction requires `submitted(C06, round=game.round) == True`. Confirm: can C29 be submitted before C06 in the same round (with C06 submission validated later), or must C06 already be submitted when C29 is checked?
- **target_district dependency:** C29's target is derived from C06's target district. If C06 is cancelled or discarded after C29 is submitted, what happens to C29? Confirm void or independent resolution.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C29 = Card(
    id=29,  version="v1.0",
    name    = "Network Cascade",
    tagline = "Extend Broadcast Interference to an adjacent district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Submission,  function = Modify,  subject = PoliticalAct,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=district.adjacent(C06.target_district), target_faction=None, target_object=PoliticalAct,
    affinity=None,
    restriction = faction(acting).submitted(C06, round=game.round) == True,
    cost        = resource.faction(acting).exposure * 2,
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

### C30 — COMMUNITY ANCHOR
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's Baryo-targeted presence card — specialized version of C03 Campaign, restricted to Baryo ring districts where Network has zero presence. The restriction enforces the narrative: Community Anchor is how Network establishes a beachhead through existing relationships, not how it expands from existing territory. Cheaper than C03 (Exposure×1 vs dual-cost) because the card is zone-restricted and fires only on initial entry — once Network has any presence in the district, the card cannot target it again. Baryo focus aligns with Network's win path (wide Presence coverage from New Meridian, Baryo outward).

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Network's Baryo entry mechanic — initial beachhead via existing relationships; distinct from C03 Campaign (general presence) by Baryo restriction and zero-presence gate | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — community-based entry as doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Exposure×1 (cheaper than C03 dual-cost); Baryo+zero-presence restriction enforces narrative; aligns with Network's wide-presence win path | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — Baryo-targeted entry is Network-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Add/PresenceToken — Baryo-restricted variant of C03 Campaign pattern | Art 04b §4, §5 |
| Balance | ✓ | Exposure×1, Automatic, Baryo+zero-presence restriction — narrower and cheaper than C03; Baryo entry advantage calibration noted | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: +1 presence token at Beat 3; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces zero-presence condition | — |
| Portrait validity | ✓ | Network +1 submitter; community-based entry aligns with broadcast doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any(zone=Baryo) — Baryo zone definition outstanding (Outstanding Issue) | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken; Exposure cost; no new components | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; ARBITER places presence token; zone check at Dispatch | Art 03 §9, §11 |

#### Outstanding Issues

- **Baryo zone definition:** `district.any(zone=Baryo)` — confirm Baryo as a defined zone in Art 01. If Baryo includes multiple rings' districts, the zone boundary needs to be explicit.
- **Expansion beyond initial entry:** Once Network has 1 presence in a Baryo district (via Community Anchor), the restriction blocks reuse in that district. Confirm this is the intended scarcity design — Community Anchor establishes but does not reinforce.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C30 = Card(
    id=30,  version="v1.0",
    name    = "Community Anchor",
    tagline = "Establish presence in a Baryo district through existing relationships.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Territory,  function = Add,  subject = PresenceToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=district.any(zone=Baryo), target_faction=None, target_object=None,
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

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | PS-to-Intel conversion — Network doctrine: standing is a means, not an end; deliberate sacrifice for targeted intelligence | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; free submission; PS loss as success effect; target_faction required for token keying; 2 PS per token calibrated as real doctrine commitment | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/IntelToken — PS effect generates faction-keyed Intel; Economy layer correct | Art 04b §4, §5 |
| Balance | ✓ | Free cost; 2 PS for 1 IntelToken; single use per play — PS track scarcity is the gate; 2:1 ratio prevents cheap arbitrage vs. Weaponized Transparency | Art 02a §6–§7; Art 02b §7 |
| Effect duration | ✓ | Immediate: PS reduced and token delivered at Beat 3 resolution | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | portrait = {} — PS loss is a success effect, not a portrait track shift; absence confirmed intentional | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — no district context | Art 01 §6–§7 |
| Supported by components | ✓ | target_faction required; IntelToken keyed to target_faction at Dispatch | Art 02a §6–§8; Art 02b §7 |
| Supported by game procedure | ✓ | Beat 3 Automatic; PS loss and IntelToken delivery handled by Art 03 apply effect | Art 03 §9, §11 |

#### Outstanding Issues

*None.*

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

*Migrated from §8 Intel Economy block to Network extended section S59. Pre-convention flat format — full schema pass pending (04-47).*

```python
C37 = Card(
    id=37,  version="v1.1",
    name    = "Sacrifice",
    tagline = "Spend two steps of credibility. Receive one piece of intelligence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Economy,  function = Add,  subject = IntelToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    target_district=None, target_faction=faction.any, target_object=None,
    affinity=None,
    restriction=None,
    cost        = None,
    success     = faction(acting).public_standing -= 2, IntelToken(target_faction) += 1,
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "The Network knows: sometimes you spend credibility like currency. This is one of those times.",
    perspectives = {Network: "What we have built is not a goal. It is a tool. And sometimes a tool must be spent."},
    design_note  = "PS −2 is a success effect, not a cost — PS is non-fungible and cannot appear in the cost field (Art 04 §6.2). target_faction required: tokens must be keyed at Dispatch. Single use per play; 2:1 ratio prevents cheap IntelToken arbitrage.",
    arbiter_note = None,
)
```

---

### Network — WEAPONIZED TRANSPARENCY
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's coercive intelligence card — spends an Intel token to deliver one of two effects against a named faction: an unblockable PS reduction, or forced hand-reveal at next Dispatch. Option A (PS drop) is doctrine's sharpest edge — The Network's information advantage translates directly into reputational damage that no countermeasure can prevent. Option B (revealed play) is a strategic disruption: knowing a faction's next submission in advance shapes The Network's own planning. The Intel token is the authorization, not a targeting mechanism — Network is deploying gathered leverage, not performing surveillance.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Coercive intelligence — converts gathered Intel into targeted leverage (PS damage or forced hand-reveal); distinct from C26/C28 (broadcast/reveal) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — information as delivery mechanism | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; IntelToken cost; dual-mode choice; unblockable PS drop is Network doctrine differentiator; choose_one timing outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — intelligence leverage is Network-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/PublicStanding — Intel-gated leverage translates to PS impact; dual-mode accepted | Art 04b §4, §5 |
| Balance | ✓ | IntelToken, Automatic, dual-mode — Option A unblockable PS−1 vs Option B forced reveal; dominant option analysis outstanding (Outstanding Issue) | Art 02a §6–§7 |
| Effect duration | ✓ | Option A: immediate at Beat 3; Option B: persists until next Dispatch | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Network +1 submitter; intelligence leverage aligns with transparency doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; PublicStanding and card submission as targets; no new components | Art 02a §6–§8; Art 02b §7 |
| Supported by game procedure | ✓ | Beat 3 Automatic; unblockable exception scope outstanding; Option B Month 2 timing outstanding; choose_one timing outstanding (Outstanding Issues) | Art 03 §9, §11 |

#### Outstanding Issues

- **Unblockable PS drop:** Option A cannot be countered by any Countermeasure. Confirm this is an explicit exception to Art 03's countermeasure rules, and that it's documented in Art 03 or Art 04 §6 rather than only in this card's design note.
- **Option B "Month 2" timing:** Original design note: "If this is Month 2, the revealed play applies to Month 3 public acts instead." Confirm this clarification is accurate — why does Month 2 timing shift the scope?
- **choose_one mechanic:** `game.choose_one(A, B)` — confirm whether the choice is made at Dispatch or at resolution, and whether ARBITER must know the choice before the card resolves.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Migrated from §8 Intel Economy block to Network extended section S59. Pre-convention flat format — full schema pass pending (04-47).*

```python
C40 = Card(
    id=40,  version="v1.0",
    name    = "Weaponized Transparency",
    tagline = "Exposure is not a threat. It is a delivery mechanism.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Information,  function = Reveal,  subject = PublicStanding,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    target_district=None, target_faction=faction(named_opponent), target_object=None,
    affinity=Network,
    restriction=None,
    cost        = IntelToken(any) * 1,
    success     = game.choose_one(
        A=faction(target).standing -= 1,   # unblockable; no Countermeasure may prevent
        B=faction(target).next_dispatch.ops_revealed == True,
    ),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The Network does not publish what it knows. It delivers it — privately, precisely, to exactly one person.",
    perspectives = {Network: "Transparency is a tool. We decide when and where to deploy it."},
    design_note  = "Option A PS drop is unblockable by design — Network doctrine differentiator. Option B: ARBITER enforces revealed play at next Month's Dispatch. If Month 2, Option B applies to Month 3 PAs instead (outstanding issue). Intel token consumed is any held token.",
    arbiter_note = "Option A: reduce target PS by 1 — no countermeasure check, bypass all blocks. Announce at Beat 3 resolution. Option B: track forced-reveal commitment; at next Dispatch, require target to place their covert action cards face-up before other factions submit.",
)
```

---


---

### Network — Public Acts
[↑ Network](#network)

| Card | Name |
|------|------|
| [P13](#p13-public-disclosure) | Public Disclosure |
| [P14](#p14-community-rally) | Community Rally |

### P13 — PUBLIC DISCLOSURE
[↑ Public Acts](#network-public-acts)

#### Design Rationale
Network's signature information-attack PA — a coordinated release of all substantiated intelligence against a target faction. Scaling mechanic: each Intel token spent contributes both to the threshold calculation (more tokens = more credible = easier to land) and to the damage on both success and fail (more tokens = more damage, even when the full release fails). The partial damage on fail ("the dirt still gets out") reflects that even a botched broadcast releases something. High investment ceiling makes this Network's most powerful single card when fully loaded.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Coordinated multi-attribution broadcast is Network's highest-expression public act | Art 00 §7 |
| Voice fit | ✓ | Network on-doctrine; Guild (aligned): disclosure makes attribution permanent; Ghost (opposed): sequenced release vs. full dump | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Maximum-expression Network broadcast: all held Intel tokens spent; Exposure × 2 (Network's resource). Network +2 PS on success. Intel token scarcity (Ghost pipeline or covert gathering) is the natural ceiling on doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Network) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Reveal / ActionAttribution | Art 04b §4 |
| Balance | ⚠ | Threshold scales with token count (30 + 10n). Damage scales per token (−2 PS each on success, −1 on fail). High cost (2 Exposure + all tokens). Intel tokens are scarce (require Ghost cooperation or covert gathering) — natural limiter | Art 02a §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted broadcast; no zone reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (all held, faction-keyed to target; Art 02a §6); Exposure × 2 cost (Art 02a §8) | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Token count calculated at Beat 4; all tokens spent regardless of outcome | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
P13 = Card(
    id="P13",  version="v1.0",
    name    = "Public Disclosure",
    tagline = "Network broadcasts all substantiated intelligence about a faction's operations in a single coordinated release.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Network,

    layer    = Information,  function = Reveal,  subject = ActionAttribution,

    beat            = 4,
    resolution      = d100,
    threshold       = None,  # = 30 + (10 × tokens held naming target); calculated at Beat 4
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Contested",
    outcome_type    = Unilateral,
    persistence     = Immediate,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

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

### P14 — COMMUNITY RALLY
[↑ Public Acts](#network-public-acts)

#### Design Rationale
Network's broadcast-derived presence PA — scaling territorial expansion built on established foothold. Network names up to 3 districts where they are already Established or Dominant; 1 presence token is placed in each. Cost scales with district count (2 Exposure + 1 per additional district). This is not expansion into new territory — it is deepening existing presence through community mobilisation, the most on-doctrine territorial act for Network. Replaces Open Record Request, which had unworkable mechanical premises.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Broadcast-derived community presence growth is Network's primary win-condition mechanism | Art 00 §7 |
| Voice fit | ✓ | Network on-doctrine; Syndicate (aligned): acquisition-free consolidation; Directorate (opposed): unregulated expansion | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Network deepens existing foothold (Established+) — consolidation, not expansion. Scaling Exposure cost (Network's resource). Portrait +1. Directly serves Network's community-relationship territorial doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Network) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken | Art 04b §4 |
| Balance | ✓ | Scales: 2 Exposure (1 district), 3 Exposure (2), 4 Exposure (3 max). Restricted to Established+ (not expansion). Partial resolution if some districts fail restriction | Art 02a §6–§7 |
| Effect duration | ✓ | PresenceToken placement = Permanent board state; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.up_to_three — valid zone references; restriction checks Established+ per district (valid zone conditions) | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02a §6); Exposure × 2+ cost (Art 02a §8) | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Districts named at Phase B; restriction per district at Beat 0 | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P14 = Card(
    id="P14",  version="v1.0",
    name    = "Community Rally",
    tagline = "Mobilize communities across Network's established presence network.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Network,

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

    target_district = district.up_to_three,  # 1–3 districts named at Phase B; each must be Established+
    target_faction  = None,
    target_object   = None,

    affinity    = None,
    restriction = faction(Network).influence_tier(district.each_target) >= Established,
    cost        = resource.faction(Network).exposure * 2 + resource.faction(Network).exposure * (count(district.target) - 1),
    # cost = 2 Exposure + 1 per additional district above first

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
    design_note  = "Broadcast-derived presence PA. Deepens existing foothold (Established+) rather than expanding into new territory. Scaling cost: 2 Exposure (1 district), 3 (2 districts), 4 (3 districts). Partial resolution: if a named district fails Established+ restriction at Beat 0, that district is dropped from resolution; remaining valid districts proceed; cost already committed. Replaces Open Record Request (unworkable).",
    arbiter_note = "Phase B: Network names 1–3 districts. Cost calculated (2 + extras) and committed. Beat 0: check each named district for Established+ restriction. Drop invalid districts from resolution. Beat 4: place 1 presence token in each valid district. Network +1 PS.",
)
```

---


---

## Syndicate
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#syndicate-covert-operations) · [Public Acts](#syndicate-public-acts)

---

### Syndicate — Covert Operations
[↑ Syndicate](#syndicate)

| Card | Name |
|------|------|
| [C31](#c31-leveraged-acquisition) | Leveraged Acquisition |
| [C32](#c32-short-the-market) | Short the Market |
| [C33](#c33-hostile-acquisition) | Hostile Acquisition |
| [C34](#c34-golden-parachute) | Golden Parachute |
| [C35](#c35-regulatory-capture) | Regulatory Capture |
| [—](#syndicate-land-title) | Land Title |
| [—](#syndicate-hostile-takeover) | Hostile Takeover |
| [—](#syndicate-accord-transfer) | Accord Transfer |
| [—](#syndicate-parasitic) | Parasitic |
| [—](#syndicate-corporate-blackmail) | Corporate Blackmail |

### C31 — LEVERAGED ACQUISITION
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's non-presence resource extraction card — Capital buys a one-round upkeep grant from any district without Syndicate being physically present. Establishes the doctrine that ownership and presence are separate things. Distinguished from Land Title (extended set) by duration: C31 is a per-round transactional play; Land Title creates a permanent revenue claim. The `timing=Upkeep` delivery means the Capital is spent now but the resource arrives at the next upkeep cycle — a cash-flow timing risk. Per-round global limit (`game.ops_submitted(C31) <= 1`) prevents Syndicate from stacking multiple district extractions in one round.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Non-presence resource extraction — Capital buys revenue stream from any district; implements "ownership ≠ presence" doctrine; distinct from Land Title (permanent) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×4; per-round global limit prevents stacking; timing-lag risk is intentional (cash-flow mechanic) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — non-presence extraction is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — deferred upkeep delivery accepted | Art 04b §4, §5 |
| Balance | ✓ | Capital×4 for 1 district native at Upkeep; timing=Upkeep delivery and per-round limit scope outstanding (Outstanding Issues) | Art 02a §6–§7 |
| Effect duration | ✓ | One upkeep cycle: resource delivered at next Upkeep only | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; non-presence extraction aligns with capital intelligence doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource cost + delivery; timing=Upkeep parameter delivery procedure outstanding (Outstanding Issue) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; deferred Upkeep delivery procedure outstanding (Outstanding Issue) | Art 03 §9, §11, §19 |

#### Outstanding Issues

- **`timing=Upkeep` delivery:** Deferred upkeep delivery is not described in Art 03 upkeep procedure. Confirm where and how ARBITER tracks pending deferred grants until upkeep.
- **Per-round limit scope:** `game.ops_submitted(C31, round=game.round) <= 1` — confirm this is a table-wide limit (Syndicate cannot play C31 twice from multiple deck copies in one round) vs. a per-player-instance limit.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C31 = Card(
    id=31,  version="v1.0",
    name    = "Leveraged Acquisition",
    tagline = "Gain resource generation from a district without presence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Add,  subject = NativeResource,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=district.any, target_faction=None, target_object=None,
    affinity=None,
    restriction = game.ops_submitted(C31, round=game.round) <= 1,
    cost        = resource.faction(acting).capital * 4,
    success     = game.dispatch(faction(acting), district(target).resource.native * 1, timing=Upkeep),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},
    narrative   = "The Syndicate does not need to be somewhere to profit from it. Ownership and presence are different things.",
    perspectives = {Syndicate: "We own the revenue stream. Whether we are physically present is irrelevant."},
    design_note  = None,
    arbiter_note = None,
)
```

---

### C32 — SHORT THE MARKET
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's economic disruption card — directly reduces a target faction's native resource supply, impeding their ability to fund actions next round. The "short" framing reflects a deliberate market interference: Syndicate bets against a competitor's economic health and profits from their reduced capacity. Intel restriction (fresh token) requires prior intelligence, creating a two-step play: gather first, short second. Applied silently (no public announcement) reflects the covert nature of market manipulation. Crit success doubles the reduction (−2 native). Failcrit PS −1 represents the institutional embarrassment of a failed financial maneuver.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Economic disruption — direct native resource reduction; "short" framing aligns with Syndicate market interference doctrine; Intel restriction enforces prior intelligence requirement | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×2; Intel restriction creates C05→C32 two-step; "applied silently" protocol outstanding (Outstanding Issue); 04-n14 redesign flag | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — covert market interference is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Remove/NativeResource — direct supply reduction | Art 04b §4, §5 |
| Balance | ✓ | Capital×2, threshold 50; Intel prereq adds secondary cost; "applied silently" and floor confirmation outstanding (Outstanding Issues) | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: native resource reduced at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; failcrit PS −1 is game effect (not portrait), per P12 | Art 04 §6.2; Art 02b §7 |
| Supported by zones | ✓ | target_district = None — faction-targeted, not district-targeted | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken restriction; NativeResource target; "applied silently" protocol outstanding (Outstanding Issue) | Art 02a §6–§8; Art 02b §7 |
| Supported by game procedure | ✓ | Beat 3 d100; Intel check at Dispatch; silent application and floor outstanding (Outstanding Issues) | Art 03 §9, §11 |

#### Outstanding Issues

- **"Applied silently" protocol:** C32 reduces native resource "silently" — the table does not see the effect. Confirm: does ARBITER privately notify the target, or is the loss simply applied to their resource pool with no notification? Distinction matters for game integrity.
- **Floor at minimum 0:** `success = faction(target).resource.native -= 1 # minimum 0` — confirm ARBITER applies a floor of 0 and any excess is simply absorbed without penalty.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C32 = Card(
    id=32,  version="v1.0",
    name    = "Short the Market",
    tagline = "Reduce a faction's native resource generation for one round.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Remove,  subject = NativeResource,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10},
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    target_district=None, target_faction=faction(named_opponent), target_object=NativeResource,
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

### C33 — HOSTILE ACQUISITION
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's structure takeover card — Capital purchases ownership of an opponent's structure block, transferring it to Syndicate along with the district's native resource compensation to the dispossessed faction. The most expensive Syndicate base card at Capital×5, reflecting that acquiring built infrastructure is a major transaction. The "fair offer" framing in the narrative — Syndicate pays, target receives a resource — positions this as market-legal rather than theft. Guild Protection (C11 active in district) creates a doctrinal carve-out: when Guild has actively asserted its structural permanence in the district, Syndicate cannot override it this round. Successcrit returns Capital×1 (financial efficiency on the acquisition). Failcrit PS −1: a publicly failed acquisition damages Syndicate's financial reputation.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Structure takeover — Capital purchases ownership with compensation; "fair offer" framing positions this as market-legal; Guild Protection carve-out for doctrinal symmetry | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×5 highest base cost; compensation to target; C11 Guild Protection interaction outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — structure ownership purchase is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Redirect/StructureBlock — ownership transfer | Art 04b §4, §5 |
| Balance | ✓ | Capital×5, threshold 50, permanent transfer; compensation mechanics and C11 interaction outstanding (Outstanding Issues) | Art 02a §6–§7 |
| Effect duration | ✓ | Permanent: structure ownership transferred; compensation delivered once at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; failcrit PS −1 is game effect (not portrait), per P12 | Art 04 §6.2; Art 02b §7 |
| Supported by zones | ✓ | target_district = district.any — presence-free acquisition | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock transfer; NativeResource compensation; C11 interaction outstanding (Outstanding Issue) | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 3 d100; ARBITER re-assigns structure ownership; C11 active-state visibility outstanding (Outstanding Issue) | Art 03 §9, §11 |

#### Outstanding Issues

- **C11 Guild Protection interaction:** Restriction excludes acquisition when `C11.active(district(target), round=game.round)` — confirm C11's "active" state is visible to ARBITER at Beat 3 and that this interaction is symmetrical (C11 blocks C33, but C33 does not block C11 playback in same round).
- **Compensation mechanics:** `game.dispatch(faction(target), resource.faction(target).native * 1)` delivers 1 native to the dispossessed faction. Confirm this is the target faction's native resource type (not Syndicate's), and that the delivery is immediate.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C33 = Card(
    id=33,  version="v1.0",
    name    = "Hostile Acquisition",
    tagline = "Purchase ownership of an opponent's structure.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Redirect,  subject = StructureBlock,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10},
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    target_district=district.any, target_faction=faction(named_opponent), target_object=StructureBlock,
    affinity=None,
    restriction = (
        district(target).faction(target).structure >= 1
        AND NOT (faction(target) == Guild AND C11.active(district(target), round=game.round))
    ),
    cost        = resource.faction(acting).capital * 5,
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

### C34 — GOLDEN PARACHUTE
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's bribe card — pays a named faction to nullify their Beat 3 operations against Syndicate. Capital is declared at Dispatch, validated at Beat 0 (retained with card, not drained to Reservoir), and distributed at Beat 2 across the target faction's Beat 3 ops that target Syndicate in submission order until exhausted. At Beat 3: any operation with full Capital coverage is voided and the Capital returns to that faction's case; partial coverage attaches a −50 threshold marker. If the target faction submitted no operations against Syndicate, the Capital arrives in their return case as an unexplained windfall — the bribe worked, or was unnecessary. Either way, the Capital is gone from Syndicate's pool.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Bribe mechanic — Capital always reaches target faction; nullification is conditional on their submitted ops | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective — positional wager is doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Beat 2 Automatic; Capital retained with card (not drained); target_faction = bribe recipient; wager structure (positional vs. faction) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Protect/NativeResource — Capital expenditure protects Syndicate assets from named faction's ops | Art 04b §4, §5 |
| Balance | ✓ | Variable cost 1–N declared at Dispatch; cost is the effect vehicle — goes to target regardless of outcome; over-payment is wasted Capital | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: Capital distributed at Beat 2, void/partial resolved at Beat 3 | — |
| Persistence | ✓ | Immediate — fully resolved by end of Beat 3 | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; player judgment on whether to submit | — |
| Portrait validity | ✓ | Syndicate +1 submitter — positional wager aligns with capital doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted | Art 01 §6–§7 |
| Supported by components | ✓ | Capital retained with card at Beat 0; distributed Beat 2; returned to target_faction at Beat 3 | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 0 Retained validation; Beat 2 distribution procedure; Beat 3 capital-on-card void/partial — all defined in Art 03 | Art 03 §9, §11 |

#### Outstanding Issues

*None.*

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

*Pre-convention card — design rationale scaffold added S59. Full redesign S65.*

```python
C34 = Card(
    id=34,  version="v2.0",
    name    = "Golden Parachute",
    tagline = "Declare a bribe. Their operations against you are covered. Windfall or nullification — the Capital leaves either way.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Protect,  subject = NativeResource,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district = None, target_faction = faction(named), target_object = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(acting).capital * declared(N, min=1),  # retained with card at Beat 0 — does not drain to Reservoir
    success         = game.bribe(capital=declared(N), target=faction(target), against=faction(acting), beat3_ops_first_to_last=True),
    successcrit     = None, fail=None, failcrit=None,
    portrait        = {Syndicate: PortraitEntry(submitter=+1)},
    narrative       = "The Syndicate does not wait to find out. They price the outcome in advance.",
    perspectives    = {Syndicate: "We did not lose those resources. We placed them where the problem would be. There is a difference."},
    design_note     = "Capital declared at Dispatch on target profile. Beat 0: retained (not drained). Beat 2: distributed across target_faction Beat 3 ops targeting Syndicate, first-to-last, until exhausted. Beat 3: full coverage = void + Capital to submitter case; partial = −50 marker + Capital to submitter case. No ops from target_faction = windfall to return case. Wager structure: Syndicate bets positionally — wrong bet wastes Capital, correct bet nullifies threat.",
    arbiter_note    = "See Art 03 Beat 0 (Retained validation), Beat 2 (Golden Parachute procedure), Beat 3 Step 1.4 (capital-on-card resolution).",
)
```

---

### C35 — REGULATORY CAPTURE
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's submission-layer blocking card — analogous to C21 Invoke Jurisdiction (Directorate) but broader in scope and more expensive. Where C21 is limited to C01/C03, Regulatory Capture blocks any named action type in a district for one round. This flexibility reflects Syndicate's financial reach into regulatory structures. Capital×3 at Beat 2 Automatic with public announcement makes it a visible table signal — everyone knows Syndicate has blocked this action type. The portrait entry with modifier=-2 when targeting a Guild-primary action type captures the doctrinal tension: buying regulatory outcomes is precisely what Guild's permanence doctrine opposes.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Broad submission-layer block — Capital buys regulatory control over any named action type; broader than C21 (Directorate, C01/C03 only); public announcement makes it a visible table signal | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design — regulatory capture as market governance | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×3; public announcement; Guild-primary portrait modifier outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — regulatory purchase is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Submission/Block/NamedActionType — NamedActionType definition outstanding (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | Capital×3 vs C21's Mandate×2; breadth calibration and NamedActionType scope outstanding (Outstanding Issues) | Art 02a §6–§7 |
| Effect duration | ✓ | One round: block applies for round=game.round only | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 positional wager fires on submission | — |
| Portrait validity | ✓ | Syndicate +1 submitter with modifier=−2 for Guild-primary action type; firing conditions outstanding (Outstanding Issue) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any; ChorusNode excluded | Art 01 §6–§7 |
| Supported by components | ✓ | NamedActionType definition outstanding (Outstanding Issue); no new physical components | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; named action type blocked for round; public announcement by ARBITER | Art 03 §9, §11 |

#### Outstanding Issues

- **`NamedActionType` definition:** What constitutes a "named action type" — is this a card name (e.g., "C01"), a taxonomy function (e.g., "Add — StructureBlock"), or a broader category (e.g., "Build")? The breadth of the block changes significantly based on this definition.
- **portrait modifier=-2 for Guild-primary action:** `mod_where=action_type(named).primary_faction == Guild` — confirm "primary_faction" is a defined property of action types, or if this needs to be a player declaration at submission.
- **Comparison to C21:** C35 is explicitly broader than C21 at a 1-Mandate premium. Ensure the gap is documented in design notes for balance review.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
C35 = Card(
    id=35,  version="v1.0",
    name    = "Regulatory Capture",
    tagline = "Block a specific action type in a named district for one round.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Submission,  function = Block,  subject = NamedActionType,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    target_district=district.any, target_faction=None, target_object=NamedActionType,
    affinity=None,
    restriction = district(target) != ChorusNode,
    cost        = resource.faction(acting).capital * 3,
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
Land Title files a capital claim on undeveloped land — no faction holds a structure block there yet. The card delivers a Grant Deed (ARBITER-issued card, placed in Syndicate's Dispatch Case, moves to hand at Debrief). Grant Deed is a tripwire React card Syndicate holds until another faction builds in the named district, at which point the deed fires. No board marker from this card; no ongoing ARBITER monitoring. Distinct from C31 Leveraged Acquisition (transactional per-round income): Land Title is a positional play — Syndicate reads the board, registers claims on districts likely to develop, then reacts when the trigger fires. Multiple Grant Deeds on the same district are permitted; cost-governed.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Capital claim on undeveloped district; delivers Grant Deed to hand | Art 00 §7 |
| Voice fit | ✓ | Syndicate-only; paper before patrols | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; undeveloped districts only; ChorusNode excluded; multiple deeds permitted (cost-governed) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Add/StructureBlock — ultimate effect is Syndicate structure placed via Grant Deed | Art 04b §4, §5 |
| Balance | ✓ | Capital×5 per deed; payback contingent on opponent building in target district | Art 02a §6–§7 |
| Effect duration | ✓ | Permanent — Grant Deed held until played or game end | — |
| Trigger validity | ✓ | N/A — trigger = None on this card | — |
| Portrait validity | ✓ | Syndicate +1 submitter | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; ChorusNode excluded | Art 01 §6–§7 |
| Supported by components | ✓ | Grant Deed = new component (SCIF-pattern); stored blank in ARBITER tableau; no marker placed by this card | Art 02a §6–§8 |
| Supported by game procedure | ⚠ | Grant Deed tripwire react window needs Art 03 procedure addition (04-n27 territory) | Art 03 §11 |

#### Outstanding Issues

- **Grant Deed tripwire react window:** "immediately after structure block placed, before any other board state change" — this react class is not yet in Art 03. Tracks under 04-n27.
- **Grant Deed component registration:** New component; needs Art 02 entry (SCIF-pattern: blank card stored in ARBITER tableau, fields: `district | owner`). Tracks under 04-n26.
- **00-R11 interaction on Grant Deed fire:** If Syndicate already holds a structure block in the named district when the deed fires, step 3 (place Syndicate structure) is blocked by 00-R11. Steps 1–2 still execute. No card-level restriction needed — 00-R11 governs.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Redesigned S67 — v2.0*

```python
LandTitle = Card(
    id=TBD,  version="v2.0",
    name    = "Land Title",
    tagline = "File a capital claim on undeveloped land. Let someone else build. Then collect.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Add,  subject = StructureBlock,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None,
    trigger=None,
    resolution_type="Transactional", outcome_type=None,
    target_district=district.named, target_faction=None, target_object=None,
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
    design_note  = "Delivers Grant Deed component (ARBITER tableau → Syndicate case → hand at Debrief). Grant Deed is a tripwire React played from hand when any faction places a structure block in the named district. No board marker from this card. Automatic resolution — no crit or fail. Multiple deeds permitted; cost-governed. 00-R11 governs step 3 of Grant Deed effect.",
    arbiter_note = "Take 1 blank Grant Deed from ARBITER tableau. Write target district name. Place in submitting faction's Dispatch Case. Grant Deed moves to Syndicate hand at Debrief.",
)
```

---

### Syndicate — HOSTILE TAKEOVER
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's presence absorption card — distinct from C33 Hostile Acquisition (which targets structure blocks). Hostile Takeover purchases an opponent's community presence and replaces it with Syndicate presence at the same tier, instantly swinging district control without demolition. The Intel token requirement establishes a Ghost-Syndicate structural link: Syndicate cannot execute a takeover without prior intelligence on the target. Capital×4 + Intel reflects the combined financial and intelligence investment required. The net effect on the district's control tier is neutral — same count of tokens, different faction — making this a covert displacement rather than a destructive act. Successcrit returns 1 Capital (efficient acquisition). Failcrit NotificationSlip to target: a failed takeover attempt alerts the target.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Presence absorption — control swing without demolition; displaces target presence and replaces with Syndicate at equivalent tier; distinct from C33 (StructureBlock) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design — acquisition of relationships, not displacement | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×4 + IntelToken; Ghost-Syndicate structural link; token supply and void-on-Absent outstanding (Outstanding Issues) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — presence absorption is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Add/PresenceToken — replaces target presence at same count | Art 04b §4, §5 |
| Balance | ✓ | Capital×4 + IntelToken, threshold 50; dual cost vs C33 (Capital×5 only); token replacement count outstanding (Outstanding Issue) | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate: presence tokens replaced at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; failcrit NotificationSlip is game effect (not portrait), per P12 | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken transfer; IntelToken cost; token supply source and void-on-Absent outstanding (Outstanding Issues) | Art 02a §6, §8; Art 02b §7–§8 |
| Supported by game procedure | ✓ | Beat 3 d100; ARBITER replaces tokens; void-on-Absent resolution outstanding (Outstanding Issue) | Art 03 §9, §11 |

#### Outstanding Issues

- **Token replacement count:** At resolution, ARBITER replaces ALL of target's presence tokens in the district with Syndicate tokens at the same count. Confirm: if target is Dominant (3 tokens), Syndicate places 3 tokens and target drops to Absent. Does Syndicate need those tokens in reserve, or does ARBITER provide them from supply?
- **Self-takeover of Absent district:** If target reaches Absent between Dispatch and Beat 3 resolution (e.g., from a prior Beat 3 action this round), the restriction `presence >= 1` fails at resolution — confirm card is void (slot + resources lost) or triggered on Dispatch state.
- **Ghost-Syndicate link:** This card creates the structural link between Ghost's Intel collection and Syndicate's high-end plays. Confirm with Ghost players that faction-keyed Intel token mechanics are compatible (Ghost generates Syndicate-keyed Intel; Syndicate can purchase or trade for it).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Draft S59 — design pass pending*

```python
HostileTakeover = Card(
    id=TBD,  version="v1.0",
    name    = "Hostile Takeover",
    tagline = "Purchase control of a faction's community presence in a district, replacing their tokens with Syndicate's at equivalent tier.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Add,  subject = PresenceToken,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10},
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    target_district=district.named, target_faction=faction(named_opponent), target_object=PresenceToken,
    affinity=None,
    restriction = (
        faction(target).presence(district(target)) >= 1
        AND faction(acting).intel_tokens(faction=faction(target)) >= 1
    ),
    cost        = resource.faction(acting).capital * 4 + IntelToken(faction=faction(target)) * 1,
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
    design_note  = "Distinct from C33 Hostile Acquisition (StructureBlock). Replaces ALL target presence in district with Syndicate presence at same count (same control tier — neutral effect on tier, swing in ownership). Requires Ghost-sourced faction-keyed Intel token. Intel token creates structural link between Ghost and Syndicate — neither faction announces it publicly.",
    arbiter_note = "At resolution: count target's presence tokens in district. Remove all of them. Place equal count of Syndicate presence tokens in same district. Net tier unchanged; ownership transferred. Deliver NotificationSlip to target on crit fail. Crit success: +1 Capital to Syndicate.",
)
```

---

### Syndicate — ACCORD TRANSFER
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's accord manipulation card — the mechanism by which the Syndicate turns every bilateral agreement into a potential asset. Replaces one party in an active Accord with Syndicate itself or a named third faction, without either original party's consent. The "fine print" doctrine: Syndicate controls the paper, not the relationship. Cost is low (Capital×3, Automatic) relative to effect, reflecting that Syndicate's expertise is in legal-financial restructuring, not brute force. Pool copy = 1 singleton: accord manipulation is rare and high-stakes. The card is blocked on Art 06 (Accord mechanic) — the full spec cannot be finalized until Accord registration and transfer procedures are defined.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Accord party replacement without consent — "fine print" doctrine; Syndicate controls the paper; blocked on Art 06 but mechanic direction locked | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design — restructuring as legal-financial power | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×3; singleton; no consent required by design; incoming party scope outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — accord manipulation is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Redirect/AccordCard — blocked on Art 06 (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | Capital×3; balance assessment pending Art 06 Accord value understanding | Art 02a §6–§7 |
| Effect duration | ✓ | Permanent: accord party assignment changed in ARBITER record | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; accord restructuring aligns with capital control doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — operates on ARBITER record | Art 01 §6–§7 |
| Supported by components | ✓ | AccordCard as target — blocked on Art 06 (Outstanding Issue) | Art 02a §6–§8; Art 06 (pending) |
| Supported by game procedure | ✓ | Beat 3 Automatic; ARBITER updates record; both affected factions notified; blocked on Art 06 (Outstanding Issue) | Art 03 §9, §11; Art 06 (pending) |

#### Outstanding Issues

- **Blocked on Art 06:** Full spec cannot be finalized until Art 06 Accord mechanic defines AccordCard structure, party roles, obligations vs benefits, and what constitutes a transferable term. This card is a design placeholder — mechanic direction is locked but implementation details depend on Art 06.
- **Who can be named as incoming party:** Can Syndicate assign the accord to any faction, including ones not currently party to any accord? Or only factions already in the game's active accord network? Confirm restriction scope.
- **Consent mechanics:** "Neither party's consent required" — confirm this is intentional (Syndicate's doctrinal power) and that there is no counter-card available to block Accord Transfer in the same Beat.
- **SECONDARY OBLIGATIONS overlap:** The gap concept in the file describes a similar mechanic (obligations-only transfer). Confirm whether Accord Transfer supersedes SECONDARY OBLIGATIONS or if they are two distinct cards.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Draft S59 — design pass pending. Blocked on Art 06 Accord mechanic.*

```python
AccordTransfer = Card(
    id=TBD,  version="v1.0",
    name    = "Accord Transfer",
    tagline = "Replace one party in an active Accord — without their consent.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Redirect,  subject = AccordCard,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None,
    trigger=None,
    resolution_type="Transactional", outcome_type=None,
    target_district=None, target_faction=None, target_object=AccordCard,
    affinity=None,
    restriction = (
        game.accord.active(named_accord) == True
        AND faction(named_outgoing) != Syndicate
        AND faction(named_outgoing) in accord(named_accord).parties
    ),
    cost        = resource.faction(acting).capital * 3,
    success     = game.transfer_party(
        accord(named_accord),
        outgoing=faction(named_outgoing),
        incoming=faction(named_incoming),  # Syndicate or named third faction
    ),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},
    narrative   = "The Syndicate does not need to be at the table to own the agreement. They wrote the paper.",
    perspectives = {Syndicate: "The accord has been restructured. The original parties will be notified. Their feelings about it are noted."},
    design_note  = "Blocked on Art 06 Accord mechanic. Replaces one party in any active named Accord — neither original party's consent required. Syndicate may insert itself or name a third faction as the incoming party. Both original parties notified by ARBITER case dispatch. Supersedes gap concept SECONDARY OBLIGATIONS (which was obligations-only) — confirm at Art 06 design pass.",
    arbiter_note = "At resolution: update named Accord in ARBITER record, replacing named outgoing party with named incoming party. All terms (obligations and benefits) transfer to incoming party. Dispatch case notifications to both original parties: '[Accord name] party assignment has been amended.' New party takes effect immediately.",
)
```

---

### Syndicate — PARASITIC
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's economic intelligence tap — a positional wager on district activity. At Beat 2, Syndicate bets that someone is already operating in the target district this round. ARBITER checks the Beat 3 dispatch queue; if a Beat 3 card targeting the district exists, Syndicate receives an Intel token keyed to that card's submitting faction (first in resolution order). If no one is operating there, the card fails and Capital is spent. The wager rewards Syndicate for reading the board correctly before operations fire — not for monitoring what happens, but for knowing what's coming. Covert — other factions cannot observe the tap.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intel from reading opponent dispatch queue — positional wager on district activity before Beat 3 fires | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective — infrastructure that reads commerce before it happens | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×2; positional wager; payoff requires correct district read; covert | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/IntelToken — Intel from district activity read | Art 04b §4, §5 |
| Balance | ✓ | Capital×2; fail = cost spent; payoff contingent on opponent operating in district this round | Art 02a §6–§7 |
| Effect duration | ✓ | Immediate — resolved fully at Beat 2; no carry, no deferred effects | — |
| Persistence | ✓ | Immediate — no game-state marker persists beyond Beat 2 resolution | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 3 queue check is resolution condition, not a trigger | — |
| Portrait validity | ✓ | Fires on success (Intel delivered); unconditional on success — no mod_where needed | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — Intel token from standard stock | Art 02a §6–§8 |
| Supported by game procedure | ⚠ | ARBITER Beat 3 queue check at Beat 2 resolution — procedure not yet in Art 03 §11. Tracks under 04-n27. | Art 03 §11 |

#### Outstanding Issues

- **Art 03 Beat 2 procedure:** ARBITER checking the Beat 3 dispatch queue at Beat 2 resolution is not yet proceduralized in Art 03 §11. Tracks under 04-n27.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Redesigned S67 — v2.0. Positional wager replacing deferred conditional. No component needed.*

```python
C38 = Card(
    id=38,  version="v2.0",
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

    target_district = district.named,
    target_faction  = None,
    target_object   = None,

    affinity    = Syndicate,
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

#### Design Rationale
Syndicate's leverage card — converts Intel into immediate compliance. Two options: force a Capital transfer now (Option A) or force a Yes vote on an Accord later (Option B). Neither is blockable. The flat portrait modifier (−1 Syndicate regardless of who submits) reflects that blackmail is systemically corrosive — even Syndicate pays a small doctrinal cost for using it, because operating this way erodes the institutional trust that underlies all Capital relationships. Option B's Accord dependency creates strategic timing: play Corporate Blackmail when you know an Accord proposal is coming, or when you want to force one. Intel token is the authorization — this card requires prior intelligence to deploy.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intel-to-compliance conversion — dual-mode leverage; unblockable PS hit or forced Accord vote; systemic self-cost (Syndicate flat −1) reflects institutional corrosion | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design — leverage as doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; IntelToken cost; flat portrait −1 schema outstanding; Option B blocked on Art 06 (Outstanding Issues) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — intelligence-leverage is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Redirect/Capital — Option A is Capital transfer; Option B depends on Art 06 | Art 04b §4, §5 |
| Balance | ✓ | IntelToken, Automatic; both options unblockable; Option A unblockability documentation outstanding; Option B void condition outstanding (Outstanding Issues) | Art 02a §6–§7 |
| Effect duration | ✓ | Option A: immediate at Beat 3; Option B: persists until Accord proposed this Quarter | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Option B restriction enforced at Accord event | — |
| Portrait validity | ✓ | Syndicate flat=−1 regardless of submitter — schema validation outstanding (Outstanding Issue) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; Capital (Option A); AccordCard vote (Option B — blocked on Art 06); Intel faction-keying confirmation outstanding (Outstanding Issue) | Art 02a §6–§8; Art 06 (pending) |
| Supported by game procedure | ✓ | Beat 3 Automatic; Option B Accord procedure blocked on Art 06; Option A unblockability documentation outstanding (Outstanding Issues) | Art 03 §9, §11; Art 06 (pending) |

#### Outstanding Issues

- **Flat portrait modifier:** `portrait = {Syndicate: PortraitEntry(flat=-1)}` — confirm "flat" is a valid portrait field (vs "submitter", "modifier"). If not in schema, flag for schema pass.
- **Option B void condition:** If Option B is chosen and no Accord is proposed this Quarter, the forced-vote commitment expires unused. Confirm whether Syndicate can then retroactively apply Option A, or the card effect is simply void if no Accord comes.
- **Option A unblockability:** Same unblockable claim as C40 Weaponized Transparency Option A. Confirm both cards cite the same Art 03 exception rule, and that the rule is written rather than card-level only.
- **Intel token faction-keying:** Original spec says "Intel token" without faction-keying. Confirm any held token is sufficient (not faction-keyed). Consistent with C37 and C39.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Migrated from §8 Intel Economy block to Syndicate extended section S59. Pre-convention flat format — full schema pass pending (04-47).*

```python
C41 = Card(
    id=41,  version="v1.0",
    name    = "Corporate Blackmail",
    tagline = "Leverage converts intelligence into compliance.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Redirect,  subject = Capital,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    target_district=None, target_faction=faction(named_opponent), target_object=None,
    affinity=Syndicate,
    restriction=None,
    cost        = IntelToken(any) * 1,
    success     = game.choose_one(
        A=game.transfer(faction(target).capital, count=2, to=faction(acting)),
        B=faction(target).accord_vote_next_debrief == True,
    ),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Syndicate: PortraitEntry(flat=-1)},
    narrative   = "The information was gathered properly. What is done with it is simply business.",
    perspectives = {Syndicate: "We don't call it blackmail. We call it accelerated negotiation."},
    design_note  = "Option A (Capital theft) and Option B (forced Yes vote) are both unblockable. Option B requires Accord context at Debrief — if no Accord proposed, Option B expires unused. Flat portrait modifier reflects systemic trust cost; subject to PM05 04-21 review. Blocked on Art 06 for Option B.",
    arbiter_note = "Option A: immediately transfer 2 Capital from target to Syndicate — unblockable. Option B: record forced-vote commitment; at Debrief, next Accord proposal directed at target requires a Yes vote. If no Accord proposed this Quarter, commitment expires.",
)
```

---


---

### Syndicate — Public Acts
[↑ Syndicate](#syndicate)

| Card | Name |
|------|------|
| [P15](#p15-acquisition-offer) | Acquisition Offer |
| [P16](#p16-public-dividend) | Public Dividend |

### P15 — ACQUISITION OFFER
[↑ Public Acts](#syndicate-public-acts)

#### Design Rationale
Syndicate's public territorial acquisition PA — the counterpart to C33 Hostile Acquisition (which is covert and forcible). This card asks first. Scaling: 2 Capital per presence token acquired (n declared at Phase B). Cost scales with the position being purchased: 2 tokens at Established = 4 Capital; 6 tokens at full Dominant = 12 Capital. The offer fee (1 Capital at Phase B) is non-refundable regardless of outcome — the cost of making a public offer. The balance payment (2n Capital) is conditional on acceptance and paid at Beat 4 cleanup. On refusal, Syndicate gains the PS advantage of having made a good-faith offer publicly.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public buyout offers are core Syndicate doctrine — acquire, not take | Art 00 §7 |
| Voice fit | ✓ | Syndicate on-doctrine; Network (aligned): public offer creates public record; Guild (opposed): presence is built, not bought | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Syndicate acquire-not-take doctrine: public offer before forced action. Scaling cost (n × 2 Capital) rewards the target. PS on decline (+1 Syndicate, −1 target) incentivizes acceptance. Portrait +1. Legitimizes acquisition mode vs C33 Hostile's coercive mode | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Syndicate) / ElectPlayer | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Redirect / PresenceToken | Art 04b §4 |
| Balance | ✓ | 1 Capital offer fee (non-refundable) + 2n conditional. Scaling cost makes Dominant buyout expensive (12 Capital). Beat 4 resolution (not Debrief) | Art 02a §6–§7 |
| Effect duration | ✓ | PresenceToken transfer is immediate at Beat 4 acceptance; card persistence = Immediate | 00-R21 |
| Persistence | ✓ | Immediate — card resolved at Beat 4; no game-state marker persists | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Syndicate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid; restriction checks target's Established+ in district (valid zone condition) | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02a §6); Capital cost + conditional payment (Art 02a §8) | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Target decides at Beat 4 (not Debrief); token/Capital transfer at Beat 4 cleanup | Art 03 §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
P15 = Card(
    id="P15",  version="v1.0",
    name    = "Acquisition Offer",
    tagline = "Publicly offer to purchase another faction's presence position in a district.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Syndicate,

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

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    affinity    = None,
    restriction = faction(target).influence_tier(target_district) >= Established,
    # declared at Phase B: target faction, district, token count (n)
    cost = resource.faction(Syndicate).capital * 1,  # offer fee; non-refundable regardless of outcome

    # Beat 4 — ElectPlayer: target faction publicly accepts or declines
    # on_accept: district(target_district).faction(target).presence -= n
    #            district(target_district).faction(Syndicate).presence += n
    #            faction(target).resource(capital) += (2 * n)  # balance payment from Syndicate
    #            faction(Syndicate).standing += 1; faction(target).standing += 1
    # on_decline: faction(Syndicate).standing += 1; faction(target).standing -= 1

    success     = None,  # outcome governed by ElectPlayer accept/decline at Beat 4
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Syndicate: PortraitEntry(submitter=+1)},

    narrative    = "Syndicate does not take what it can buy. The offer is always made first. What the other faction does with it is their business.",
    perspectives = {
        Syndicate: "This is the formal mechanism. We are not here to take — we are here to acquire. The distinction matters.",
        Network:   "Syndicate makes the offer at The Table where everyone watches. Whatever the target decides, their answer is on the record. That is also useful to us.",  # aligned
        Guild:     "Syndicate offers Capital for positions Guild built through construction and sustained through presence. We did not build it to sell. That is not a position the offer changes.",  # opposed
    },
    design_note  = "Public counterpart to C33 Hostile Acquisition. 1 Capital offer fee non-refundable. Balance payment (2n Capital) conditional on acceptance, paid at Beat 4. Scaling: n=2 (Established min) = 4 Capital; n=6 (Dominant max) = 12 Capital. On accept: both PS +1. On decline: Syndicate +1, target −1. Beat 4 resolution — not Debrief.",
    arbiter_note = "Phase B: Syndicate names target faction, district, token count (n). 1 Capital offer fee committed. Beat 0: restriction check (target Established+). Beat 4: target faction publicly accepts or declines. On accept: transfer n presence tokens from target to Syndicate; Syndicate pays 2n Capital to target from supply; both +1 PS. On decline: Syndicate +1 PS, target −1 PS. Offer fee (1 Capital) is not returned in either case.",
)
```

---

### P16 — PUBLIC DIVIDEND
[↑ Public Acts](#syndicate-public-acts)

#### Design Rationale
Syndicate's political leverage PA. Places a Capital-valued marker on a named district. At next Upkeep Step 5, whoever holds Dominant in that district receives the Capital. Syndicate pre-commits 2 Capital (physically placed under the marker as escrow) and gains PS +1 at Beat 4. The card creates a persistent incentive structure that shapes table behavior without Syndicate taking direct action: factions will fight over Dominant in that district because there's Capital to claim. Syndicate may voluntarily withdraw the marker by paying 1 Mandate (removing the incentive, a diplomatic instrument). Persistence = Seasonal (marker stays until claimed or Quarter end).

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Capital-as-political-leverage is core Syndicate doctrine | Art 00 §7 |
| Voice fit | ✓ | Syndicate on-doctrine; Ghost (aligned): deferred mechanism patience; Directorate (opposed): unregulated shadow investment | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Capital-as-leverage: 2 Capital escrow shapes table behavior without direct action. PS +1 at Beat 4. Voluntary withdrawal (1 Mandate) as diplomatic instrument. Portfolio +1: submitter-bounded | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PoliticalAct / FactionSpecific (Syndicate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Add / NativeResource (deferred, conditional on Dominant at Upkeep) — note: payout resource is Capital; subject label may need schema pass clarification | Art 04b §4 |
| Balance | ✓ | 2 Capital cost + PS +1; 2 Capital at risk if another faction claims Dominant. Maximum loss: 2 Capital + 1 Mandate (withdrawal) | Art 02a §6–§7 |
| Effect duration | ✓ | DividendMarker payout at Upkeep Step 5 — within-Quarter. Seasonal persistence. Phase 21 escrow return if unclaimed. No multi-Quarter effect | 00-R21 |
| Persistence | ✓ | Seasonal — DividendMarker stays on district until claimed at Upkeep, withdrawn, or Phase 21 | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Syndicate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone; DividendMarker placed on district (valid zone-based component placement) | Art 01 §6–§7 |
| Supported by components | ⚠ | DividendMarker is a new component — register in Art 02a before production | Art 02a |
| Supported by game procedure | ⚠ | DividendMarker is a new component — register in Art 02a. Upkeep Step 5 procedure needs amendment to handle marker resolution | Art 03 §19; Art 02a |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
P16 = Card(
    id="P16",  version="v1.0",
    name    = "Public Dividend",
    tagline = "Declare a public capital investment in a district — rewarding whoever holds Dominance at next Upkeep.",
    type    = PoliticalAct,  subtype = FactionSpecific,  faction = Syndicate,

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

    target_district = district.any,
    target_faction  = None,  # dynamic — whoever holds Dominant at next Upkeep
    target_object   = None,

    affinity    = None,
    restriction = None,
    cost        = resource.faction(Syndicate).capital * 2,  # placed as escrow under DividendMarker

    success = (
        arbiter.place(DividendMarker(value=2, resource=Capital, district=target_district)),
        # 2 Capital tokens placed physically under DividendMarker on district as escrow
        faction(Syndicate).standing += 1,
        # at next Upkeep Step 5: dominant faction receives 2 Capital from escrow
        # Syndicate may withdraw marker by declaring to ARBITER and paying 1 Mandate
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
    design_note  = "Persistent economic leverage PA. 2 Capital placed as physical escrow under DividendMarker on district. At next Upkeep Step 5: Dominant faction claims it. If no Dominant (Contested or all Absent): marker stays, recheck next Upkeep. Quarter end: Syndicate recovers unclaimed escrow. Voluntary withdrawal: 1 Mandate public declaration. DividendMarker is a new component — Art 02a registration required.",
    arbiter_note = "Beat 4: place DividendMarker on district with 2 Capital tokens as physical escrow. Syndicate +1 PS. At each Upkeep Step 5 while marker present: check for Dominant in district. If Dominant: transfer 2 Capital to that faction; remove marker. If Contested or Absent: marker remains for next Upkeep. Phase 21: return unclaimed escrow to Syndicate. Voluntary withdrawal: Syndicate declares to ARBITER, pays 1 Mandate; escrow returned.",
)
```

---


---

## 11. Rules & Constraints — Modifier Cards

### 11.1 What They Are

Modifier cards alter the parameters of an action rather than targeting a game layer directly. They produce no game-state primitives on their own; their effect is mediated by the host action or condition they modify. Parameters a modifier card can alter include difficulty, cost, threshold, scope, outcome, timing, or validity of the host action. Modifier cards carry no Layer — Function — Subject assignment and are excluded from the card taxonomy. *(Art 04b §5.1, §9)*

Two timing sub-types govern when a modifier card fires:

- **React** — fires automatically when a named publicly-observable condition is met; not submitted in the standard action sequence.
- **Instant** — played actively during a defined window.

React and Instant describe *when* a modifier fires, not what it does.

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

| Category | Effect |
|----------|--------|
| Difficulty reduction | Reduce covert operation target threshold by stated amount |
| Cost reduction | Reduce resource cost of modified action by 1 unit |
| Effect extension | Extend a one-round effect — permanent where applicable per Principle 11 |
| Detection immunity | One failed detection roll does not surface the faction |
| Reach extension | Apply a public act to a non-operational-marker district |

---

## 12. Rules & Constraints — Pass Cards

**Four variants per faction.** Kept beside the tableau — not drawn from any deck. Reusable every round. Neutral grey back. Each faction holds one of each variant.

**Generalized — Beat 3 or Beat 4.** The same Pass card is valid in either context. No specialized covert-only or political-only Pass cards.

**In dispatch case (Beat 3):** Signals that covert operation slot is intentionally empty. Three Pass cards with no operations = Full Covert Pass — legal, noted.

**At Declaration (Beat 4):** Place face-up instead of declaring a public act.

**Ghost's Political Pass:** Confirms dispatch case contains 4 covert operations. Fourth operation slot available only when Ghost uses their Political Pass. Any Pass variant counts. Full rule in Artifact 03 §9.

A Pass is information. Consistent passes signal posture. ARBITER notes the pattern.

---

### Pass Card Variants — Design Notes

*Four named variants replace the single generic card. Full data structure pending detail design pass. All variants: Card type = Pass; Beat = Beat 3 or Beat 4; Subject = N/A; Portrait = N/A. See 04b §10 — Pass cards are excluded from Layer — Function — Subject taxonomy.*

**PS-01 — STAND DOWN**
*"Nothing moves. No one knows why."*
Design note: No secondary effect. The value is pure information asymmetry — opponents cannot distinguish this from a live operation until Beat 3 resolution or Declaration review. The most common pass; communicates nothing beyond the pass itself.

**PS-02 — RESERVE**
*"The operatives are recalled. The resources remain."*
Design note: Gain 1 Findings at cleanup. Converts the opportunity cost of passing into a small information gain — the faction used the time to gather intelligence rather than act.

**PS-03 — HOLD**
*"Preparation compounds."*
Design note: Draw 1 additional modifier card at next Upkeep, if modifier draw eligible. Rewards restraint with increased capacity next round. Most useful for factions building toward a heavy operations quarter.

**PS-04 — OBSERVATION**
*"ARBITER noted the silence."*
Design note: If this faction holds the highest Chorus Portrait at cleanup this round, gain 1 Findings. Connects inaction to Portrait attunement — the faction most aligned with the Chorus gains something for listening rather than acting. Available to all factions; Ghost doctrine makes it most natural.

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
| D-04-02 | Ghost C16–C20 redesign — C18 replaced with Dossier Breach (S51); C19 now unique. Portrait Shift, targeted Reveal, Copy subset gaps remain open. | Artifact 09 |
| D-04-03 | Directorate C21–C25 redesign — C25 replaced with Tactical Redirection (S51). Block duplication resolved. Mandate generation and Public Standing Shift cards still needed. | Artifact 09 |
| D-04-04 | Network C26–C30 redesign — C27 replaced with Disclosure Loop (S51). Exposure generation addressed. C26/C28 Reveal overlap and Public Standing Shift card remain open. | Artifact 09 |
| D-04-05 | Syndicate C31–C35 redesign — zero information capability; Corrupt Accord and Redirect Accord unused. Approve current set or redesign? | Artifact 09 |
| D-04-06 | Public acts P01–P18 full card data structure review — all fields (Beat, Taxonomy, Faction perspectives, Restriction, crit effects, Portrait) need card-by-card application. | Artifact 09 |
| D-04-07 | Modifier card in-world naming — "Modifier cards" is a working designation. | Artifact 09 |
| D-04-08 | Modifier card individual content — faction modifier decks and ring modifier decks have no individual card designs. | Artifact 09, physical production |
| D-04-09 | Adjacency definition — formal district adjacency table needed in Artifact 01. Required by C02, C04, C05, C14, C29, C30. | Artifact 01, physical play |
| D-04-10 | Emergency Response card data structure review — full card data structure not yet applied. | Artifact 09 |
| D-04-11 | Intel token mechanics cross-reference — Artifact 02b §8–9 audit against current card designs needed. Potential inconsistency with Denounce cost structure, token age rules, C05 crit failure. | Artifact 02b |
| D-04-12 | Countermeasure card design — referenced in §14.2 and Artifact 03 Phase 5 but no card data structure definition exists. | Artifact 09 |

### Assumptions Requiring Explicit Confirmation

| ID | Assumption | Impact if wrong |
|----|------------|----------------|
| A-04-01 | Setup pool sizes (30/24 covert, 20/12 political) are correct for the final card set | Deck construction rules change |
| A-04-02 | Deck exhaustion occurs at approximately Round 4 | Pacing and strategy may differ — playtesting required |
| A-04-03 | Maximum 1 structure per faction per district is the right balance cap | Guild doctrine and late-game economy affected |
| A-04-04 | Ghost 4-operation slot available only when Ghost passes politically — confirmed design intent | Ghost balance and doctrine affected |
| A-04-05 | Pre-written ARBITER notification slips are feasible as paper prototype components | ✅ Resolved S50 — Notification Slip (NS-xx, id=95) and Intel Delivery Slip (IS-xx, id=96) registered in 00b §4 and tmp_component. Text/format: Art 07 (F-ART07-01). |

### Cross-Artifact Flags

| Flag | Description | Target artifact |
|------|-------------|----------------|
| F-ART01-01 | Formal district adjacency table needed | Artifact 01 |
| F-ART02A-01 | Global convention: "at least 1 presence token" includes claim markers. Defined once here, not restated on cards | Artifact 02a, Artifact 09 |
| F-ART02B-01 | Intel token mechanics cross-reference audit | Artifact 02b |
| F-ART03-01 | Beat 2 renamed "The Ground Shifts" — applied in Artifact 03 v1.5 | ✅ Done |
| F-ART03-02 | Step 6 Card Draw rewritten — applied in Artifact 03 v1.5 | ✅ Done |
| F-ART03-03 | Free Accord card (C09) not from political deck — noted in Artifact 03 Declaration phase | ✅ Done |
| F-ART07-01 | Pre-written notification slip component category and text | Artifact 07 |
| F-ART09-01 | "Delivered in case" — standard phrase for privately delivered effects | Artifact 09 |
| F-ART09-02 | "Return primary cost to dispatch case" — standard resolution phrase | Artifact 09 |
| F-ART09-03 | Modifier card value rating field (1–3) on every modifier card | Artifact 09 |
| F-ART09-04 | Free Accord card is not drawn from political deck — ARBITER-delivered | Artifact 09 |

---

*End of Artifact 04 — Card System v0.9.18*
