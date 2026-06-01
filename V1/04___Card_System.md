# 04 — CARD SYSTEM
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.9.21 Draft  
**Status:** 🔄 Draft — Pending Sign-Off  
**Last Updated:** 2026-05-29  
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
| §6 | [Card Data Schema](#6-card-data-schema) |
| §7 | [Standard Covert Operations C01–C10](#7-standard-covert-operations--c01c10) |
| §8 | [Faction-Specific Covert Operations C11–C35](#8-faction-specific-covert-operations--c11c35) |
| §9 | [Standard Political Acts P01–P08](#9-standard-political-acts--p01p08) |
| §10 | [Faction-Specific Political Acts P09–P18](#10-faction-specific-political-acts--p09p18) |
| §11 | [Rules & Constraints — Modifier Cards](#11-rules--constraints--modifier-cards) |
| §12 | [Rules & Constraints — Pass Cards](#12-rules--constraints--pass-cards) |
| §13 | [Card Information Design Requirements](#13-card-information-design-requirements) |
| §14 | [Special Conditions & Gameplay Impacts](#14-special-conditions--gameplay-impacts) |
| §15 | [Examples & Exceptions](#15-examples--exceptions) |
| §16 | [Appendix — Outstanding Decisions & Assumptions](#16-appendix--outstanding-decisions--assumptions) |

---

## 3. Game Purpose

Cards are not menus — they are physical commitments.

Card systems serve many design purposes. The Signal uses all seven below — the first three are general properties of the card medium; the last four are the properties that specifically motivated the card format over simpler action-declaration mechanisms.

| Property | In The Signal |
|---|---|
| **Deck construction** — Pre-game strategic layer through selection from a larger pool. | Factions select their deck before each session. Preparation expresses doctrine. You cannot play a card you didn't prepare with. |
| **Draw variance** — Shuffle creates uncertainty about card availability each round. | Shuffled decks mean your intended action may not be available — forcing adaptation and planning for uncertainty. |
| **Resource economy** — Cards as tradeable assets with diplomatic value. | Modifier cards can be traded between factions — giving up a real advantage to build a relationship. |
| **Simultaneous commitment** — All players commit before any outcomes are known. | A covert operation card placed in the dispatch case is irreversible. A political act laid face-up cannot be retracted. |
| **Hidden information** — Decisions made under incomplete knowledge of opponent intentions. | Covert operations remain secret until ARBITER opens the case. Political acts are public — known, but not yet resolved. |
| **Asymmetric options** — Different players have access to different choices. | Faction-specific cards give each faction a decision space that reflects its doctrine. No two factions face exactly the same choices. |
| **Self-contained resolution** — Each card resolves without external reference. | Each card carries everything needed — no rules lookup required. |

---

## 4. Narrative Function

Every card is a decision made under incomplete information by people who believe the stakes are existential.

A covert operation in the dispatch case represents operatives committed, resources allocated, and a plan set in motion before anyone knows what anyone else has planned. A political act is a public stance taken in front of The Table: a claim that can be supported, refuted, or turned against the faction that made it.

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

- **Design Pass** ✓ — checklist evaluation complete; all 12 rows assessed
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
| Trigger validity | If `trigger` is set: is the trigger condition publicly observable? N/A when no trigger. *(P5)* | Art 02a; Art 03 |
| Portrait validity | Does portrait timing fire on action taken, not outcome? Are Effect fields free of direct Portrait track shifts? For Standard cards: is each faction's portrait entry (or justified absence) documented? Is entry magnitude doctrinally grounded? Do all portrait entries fire only for the submitting faction — no entry affects a faction that did not act? *(P11, P12, P13, P16)* | Art 04 §6.2 |
| Supported by zones | Does `target_district` reference a valid zone? Is ring context consistent? | Art 01 §6–§7 |
| Supported by components | Do all referenced components and cost resources exist? | Art 02a §6–§8 |
| Supported by game procedure | Are all ARBITER and player actions implied by this card covered by Art 03 procedure? Flag any implied action not yet procedurally defined as a gap. | Art 03 |

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
    outcome_type: OutcomeType | None        # political acts only

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
| outcome_type | Metadata | OutcomeType | Political act resolution process type; None for covert operations | Face |
| target_district | Targeting | DistrictExpr | District scope for the card's effect | Face |
| target_faction | Targeting | FactionExpr | Faction this card targets; None = no faction target | Face |
| target_object | Targeting | ObjectExpr | Game component this card acts on; None = no object target | Face |
| affinity | Logic | ConditionalExpr | Faction-based cost modifier — evaluated before cost expression | Face |
| restriction | Logic | BoolExpr | Submission preconditions — card unplayable if evaluates False | Face |
| cost | Logic | CostExpr | Resources consumed at submission | Face |
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

## Card Specifications

Navigation index. Card IDs link directly to the full card entry. Section headers link to the subsection.

---

### Covert Operations Deck

**Standard — C01–C10** · [→ §7](#user-content-7-standard-covert-operations--c01c10) · Available to all factions

| [C01](#user-content-c01--build-structure) | [C02](#user-content-c02--demolish) | [C03](#user-content-c03--campaign) | [C04](#user-content-c04--undermine) | [C05](#user-content-c05--gather) |
|---|---|---|---|---|
| Build Structure | Demolish | Campaign | Undermine | Gather |

| [C06](#user-content-c06--broadcast-interference) | [C07](#user-content-c07--amplify) | [C08](#user-content-c08--buy-influence) | [C09](#user-content-c09--fund) | [C10](#user-content-c10--protect) |
|---|---|---|---|---|
| Broadcast Interference | Amplify | Buy Influence | Fund | Protect |

**Faction-Specific — C11–C35** · [→ §8](#user-content-8-faction-specific-covert-operations--c11c35)

Guild — C11–C15

| [C11](#user-content-c11--fortify-structure) | [C12](#user-content-c12--materials-acquisition) | [C13](#user-content-c13--foundation-rights) | [C14](#user-content-c14--construction-crew) | [C15](#user-content-c15--infrastructure-yield) |
|---|---|---|---|---|
| Fortify Structure | Materials Acquisition | Foundation Rights | Construction Crew | Infrastructure Yield |

Ghost — C16–C20
| [C16](#user-content-c16--pattern-match) | [C17](#user-content-c17--intercept) | [C18](#user-content-c18--dossier-breach) | [C19](#user-content-c19--deep-cover) | [C20](#user-content-c20--misdirection) |
|---|---|---|---|---|
| Pattern Match | Intercept | Dossier Breach | Deep Cover | Misdirection |

Directorate — C21–C25
| [C21](#user-content-c21--invoke-jurisdiction) | [C22](#user-content-c22--detain) | [C23](#user-content-c23--evidence-preservation) | [C24](#user-content-c24--surveillance-placement) | [C25](#user-content-c25--tactical-redirection) |
|---|---|---|---|---|
| Invoke Jurisdiction | Detain | Evidence Preservation | Surveillance Placement | Tactical Redirection |

Network — C26–C30
| [C26](#user-content-c26--leak) | [C27](#user-content-c27--disclosure-loop) | [C28](#user-content-c28--open-channel) | [C29](#user-content-c29--network-cascade) | [C30](#user-content-c30--community-anchor) |
|---|---|---|---|---|
| Leak | Disclosure Loop | Open Channel | Network Cascade | Community Anchor |

Syndicate — C31–C35
| [C31](#user-content-c31--leveraged-acquisition) | [C32](#user-content-c32--short-the-market) | [C33](#user-content-c33--hostile-acquisition) | [C34](#user-content-c34--golden-parachute) | [C35](#user-content-c35--regulatory-capture) |
|---|---|---|---|---|
| Leveraged Acquisition | Short the Market | Hostile Acquisition | Golden Parachute | Regulatory Capture |

---

### Political Acts Deck

**Standard — P01–P08** · [→ §9](#user-content-9-standard-political-acts--p01p08) · Available to all factions

| P01 | P02 | P03 | P04 |
|---|---|---|---|
| Establish Presence | Contest | Commission | Denounce |

| P05 | P06 | P07 | P08 |
|---|---|---|---|
| Broadcast | Leverage | Invoke the Table | Propose Accord |

**Faction-Specific — P09–P18** · [→ §10](#user-content-10-faction-specific-political-acts--p09p18)

Guild — P09–P10

| P09 | P10 |
|---|---|
| Public Works Declaration | Infrastructure Bond |

Directorate — P11–P12

| P11 | P12 |
|---|---|
| Issue Directive | Convene an Inquiry |

Network — P13–P14

| P13 | P14 |
|---|---|
| Public Disclosure | Open Record Request |

Syndicate — P15–P16

| P15 | P16 |
|---|---|
| Acquisition Offer | Market Pressure |

Ghost — P17–P18

| P17 | P18 |
|---|---|
| Publish Analysis | Signal Review Request |

---

## 7. Standard Covert Operations — C01–C10


### C01 — BUILD STRUCTURE
[↑ Card Specifications](#user-content-card-specifications)

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
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`: permanence doctrine — core alignment (P11, P16). Ghost `submitter=−1`: structure is a permanent visible commitment; Ghost doctrine is concealment, not construction (P11, P16). Directorate: no entry — builds pragmatically ("if it serves the mandate"); instrumental, not doctrinal. Network: no entry — presence-building via community relationships (C03), not structures; observational stance confirms absence. Syndicate: no entry — doctrine is acquisition and capital flow; "who captures it" is observer framing, not builder framing. No direct Portrait track shift in effect fields (P12). All entries submitter-bounded (P16). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any` — valid. Ring entry implicit via presence requirement in restriction. | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock (§7); presence token / deployment marker in restriction (§6); faction native + district native cost (§8). | Art 02a §6–§8 |
| Supported by game procedure | ✓ | Submitted in Dispatch (§9); Beat 3 Resolution Grid (§11); Automatic resolution (§20). ARBITER places Structure Block at Beat 3 outcome. Guild affinity evaluated at dispatch. | Art 03 §9, §11, §20 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S57 |

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
[↑ Card Specifications](#user-content-card-specifications)

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
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: demolition against permanence doctrine — "we do not unmake" (P11, P16). Network `submitter=+1`: counter-entrenchment doctrine — removing infrastructure of control is on-doctrine (P11, P16). Directorate `submitter=−1`: structures represent institutional investment; doctrinal reluctance parallels C04 (P11, P16). Ghost: no entry — analytical observer, not demolition-as-doctrine; absence justified. Syndicate: no entry — pragmatic asset-management framing, no doctrinal signal; absence justified. `failcrit standing -= 1` is Public Standing (Art 02b), not Portrait — P12 clear. | Art 04 §6.2; Art 02b §7 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction uses self-or-adjacent presence — adjacency model required; district_adjacency confirmed (DB-09 ✅ S50). | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock target (§7); presence in restriction (§6); dual cost (§8); failcrit `standing -= 1` (Art 02b §7). | Art 02a §6–§8; Art 02b §7 |
| Supported by game procedure | ✓ | Dispatch (§9); Beat 3 Resolution Grid (§11); d100 threshold 50 with ring_mod. ARBITER removes Structure Block on success; standing loss on crit fail — Beat 3 outcome steps. | Art 03 §9, §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S57 |

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
[↑ Card Specifications](#user-content-card-specifications)

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
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Network `submitter=+1`: relational growth is doctrinally core (P11, P16). Guild: no entry — C01/structural investment is Guild's primary presence signal; Campaign is available but not doctrinally distinct; absence justified. Directorate: no entry — presence-building is instrumental ("where the mandate requires it"), not doctrinal; absence justified. Ghost: no entry — "presence creates exposure" frames expansion as calculated exception, not doctrinal endorsement; absence justified. Syndicate: no entry — community presence-building is not Syndicate's mode; capital and acquisition is; absence justified. No direct Portrait track shift in effect fields (P12). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Ring entry implicit via presence restriction. | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (§6); faction native + district native cost (§8). | Art 02a §6, §8 |
| Supported by game procedure | ✓ | Dispatch (§9); Beat 3 Resolution Grid (§11); Automatic resolution (§20). ARBITER places PresenceToken on success. Network affinity evaluated at dispatch. | Art 03 §9, §11, §20 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S57 |

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
[↑ Card Specifications](#user-content-card-specifications)

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
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: undermining presence is doctrinally incongruent — "we do not erase what others have built" (P11, P16). Directorate `submitter=−1, where=faction(target) != Network`: covert erosion conflicts with governance doctrine; exception when targeting Network — framed as "public safety," no doctrinal conflict; `where=` constrains by target identity, not outcome (P11, P16). Network `submitter=+1`: counter-entrenchment doctrine — eroding entrenched presence is on-doctrine (P11, P16). Ghost: no entry — "disruption without intelligence purpose is noise"; presence disruption is not Ghost's primary mode; absence justified. Syndicate: no entry — pragmatic observer framing, no doctrinal stake in presence disruption; absence justified. `failcrit standing -= 1` is Public Standing (Art 02b), not Portrait — P12 clear. | Art 04 §6.2; Art 02b §7 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction requires self-or-adjacent presence AND target has presence > 0. Adjacency model required. | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken in restriction and as target (§6); dual cost (§8); failcrit `standing -= 1` (Art 02b §7). | Art 02a §6, §8; Art 02b §7 |
| Supported by game procedure | ✓ | Dispatch (§9); Beat 3 Resolution Grid (§11); d100 threshold 50 with ring_mod. ARBITER removes PresenceToken on success; double on crit success; standing loss on crit fail — Beat 3 outcome steps. | Art 03 §9, §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S57 |

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
[↑ Card Specifications](#user-content-card-specifications)

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
[↑ Card Specifications](#user-content-card-specifications)

#### Design Rationale
Submission-layer Beat 2 card — places a cost modifier on Political Acts targeting a district this round. Broadcast interference is ambient, hence no presence requirement. Cost is Exposure-denominated: non-Network factions must acquire Exposure through incursion or trade, making this card natively affordable only to the Network. Network affinity reduces cost by 1 (net: 1 Exposure), making it a low-friction tactical tool for Network while remaining expensive for others.

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
| Trigger validity | ✓ | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Network `submitter=+1`: tactical information control — primary aligned faction (P11, P16). Ghost `submitter=+1`: interference creates analytical cover, consistent with Ghost's low-profile doctrine (P11, P16). Directorate `submitter=−1`: covert disruption undermines institutional legitimacy; Directorate's tool is regulatory authority, not anonymous interference (P11, P16). Guild: no entry — operational delays are a cost, not a doctrinal signal; absence justified. Syndicate: no entry — market inefficiency is an opportunity, not a doctrinal stake; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. No presence restriction — broadcast effect is ambient to the district. | Art 01 §6 |
| Supported by components | ✓ | PoliticalAct as target type; Exposure resource as cost. Both defined. | Art 02a §8; Art 04b §5 |
| Supported by game procedure | ✓ | Submitted at Dispatch (§9); placed in Beat 2 row at Resolution Grid setup (§11 Beat 0); moved to Beat 4 carry row during Beat 2 processing (§11 Beat 2); arming and effect applied at Beat 4 (§17). | Art 03 §9, §11, §17 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S57 |

```python
C06 = Card(
    id      = 6,  version = "v1.1",
    name    = "Broadcast Interference",
    tagline = "Disrupt public communications in a district, dampening political activity.",
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
[↑ Card Specifications](#user-content-card-specifications)

#### Design Rationale
Beat 2 modifier for the acting faction's own Political Act — the offensive counterpart to C06. Amplification cuts both ways: a PA that wins +1 PS resolves as +2; a PA that loses −1 PS resolves as −2. Cost is Exposure-denominated (same as C06), slightly favoring the Network. Restriction is None — ARBITER holds awareness through Beat 4; if no Political Act is submitted, Amplify fizzles and Exposure is spent.

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
| Trigger validity | ✓ | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Network `submitter=+1`: amplifying public messaging is core Network doctrine (P11, P16). Ghost `submitter=−1`: amplification = attention = exposure risk — "volume attracts attention, attention ends operations" (P11, P16). Guild: no entry — "let our structures speak"; amplification is a substitute for physical evidence, not a doctrinal tool; absence justified. Directorate: no entry — institutional authority doesn't require amplification; tactical use only; absence justified. Syndicate: no entry — leverage framing is opportunistic, not doctrinal; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | N/A — `target_district = None`; card operates on acting faction's own PA submission, not a district. | — |
| Supported by components | ✓ | PoliticalAct as target; Exposure as cost; `standing_impact` for outcome (Art 02b §7). | Art 02a §8; Art 02b §7; Art 04b §5 |
| Supported by game procedure | ✓ | Submitted at Dispatch (§9); placed in Beat 2 row at Resolution Grid setup (§11 Beat 0); moved to Beat 4 carry row during Beat 2 processing (§11 Beat 2); `standing_impact` multiplier applied at Beat 4 (§17). | Art 03 §9, §11, §17 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S57 |

```python
C07 = Card(
    id      = 7,  version = "v1.1",
    name    = "Amplify",
    tagline = "Boost the Public Standing impact of your own political act this round.",
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
[↑ Card Specifications](#user-content-card-specifications)

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
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=−1`: bought presence undermines earned-presence model (P11, P16). Directorate `submitter=−1`: purchasing influence bypasses legitimate institutional process (P11, P16). Network `submitter=−1`: capital-as-power is exactly what Network opposes (P11, P16). Ghost `submitter=−1`: bought presence is noisy — "draws the wrong kind of attention"; against low-profile doctrine (P11, P16). Syndicate `submitter=+1`: capital doctrine — "determines which doors exist" (P11, P16). All five entries present; four opposing, one aligned — C08 is Syndicate's card by design. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. No presence restriction — capital bypasses standard entry requirement. | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken (Art 02a §6); Capital cost (Art 02a §8); failcrit PS −2 (Art 02b §7). | Art 02a §6, §8; Art 02b §7 |
| Supported by game procedure | ✓ | Submitted at Dispatch (§9); placed in Beat 3 row of Resolution Grid (§11 Beat 0); d100 threshold 50 with ring_mod and affinity; resolved at Beat 3 (§11 Beat 3). | Art 03 §9, §11 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | ✓ S57 |

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
[↑ Card Specifications](#user-content-card-specifications)

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
| Balance | ⚠ | Net capital zero at success (2 Capital spent = 2 Capital delivered). Syndicate effective threshold 75%. Crit success = +1 PS bonus. **Open:** AccordCard = free Political Act (cost 0); its value is determined by P-series PA card costs. Reassess C09 balance once P-series is designed — if a free PA is worth more than 2 Capital spent, cost or threshold may need adjustment. | Art 02a §8; Art 04 P-series (pending) |
| Effect duration | ✓ | Capital transfer is instantaneous. AccordCard duration governed by Art 06 (pending). | Art 06 (pending) |
| Trigger validity | ✓ | `trigger = None` | — |
| Portrait validity | ✓ | Syndicate `submitter=+1`: capital-in-motion doctrine — "relationships create opportunities" (P11, P16). Directorate `submitter=−1`: using anonymous financial transfer conflicts with legitimate-process doctrine; Directorate scrutinises these transfers in others — performing one is in-doctrine hypocrisy (P11, P16). Guild: no entry — relationship investment is pragmatic, not doctrinal; absence justified. Network: no entry — analytical framing only; no doctrinal stake as actor; absence justified. Ghost: no entry — observational framing; Ghost tracks capital flows for intelligence, not as participant; absence justified. | Art 04 §6.2 |
| Supported by zones | ✓ | N/A — `target_district = None`; faction-level operation, no district target. | — |
| Supported by components | ⚠ | Capital (Art 02a §8) ✓. AccordCard undefined — pending Art 02 component definition. | Art 02a §8; Art 02 (pending) |
| Supported by game procedure | ⚠ | Dispatch and Beat 3 resolution ✓. Anonymous transfer case-return procedure and AccordCard delivery undefined — pending Art 03 definition. | Art 03 §9, §11; Art 03 (pending) |

#### Outstanding Issues

- **P-series dependency:** AccordCard = free Political Act; its balance value is determined by P-series PA card costs. Reassess after P-series is designed.
- **AccordCard PA slot conflict:** AccordCard grants a free, additional Political Act beyond normal dispatch. This likely violates Art 03 Quarter structure — PA slot limits, dispatch sequencing, or Beat 2/4 submission rules. Needs Art 03 review; AccordCard mechanic may need to be reframed (e.g., as a modifier to an existing PA rather than an extra one, or as a deferred PA in a later Quarter).
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
[↑ Card Specifications](#user-content-card-specifications)

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
| Status | ✓ | ✓ | ✓ S57 |

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

## 8. Faction-Specific Covert Operations — C11–C35



---

### THE GUILD — C11–C15

### C11 — FORTIFY STRUCTURE
[↑ Card Specifications](#user-content-card-specifications)

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
[↑ Card Specifications](#user-content-card-specifications)

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
[↑ Card Specifications](#user-content-card-specifications)

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
[↑ Card Specifications](#user-content-card-specifications)

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
[↑ Card Specifications](#user-content-card-specifications)

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

### THE GHOST — C16–C20

### C16 — PATTERN MATCH
[↑ Card Specifications](#user-content-card-specifications)

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
[↑ Card Specifications](#user-content-card-specifications)

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
| Status | ✓ | | ✓ S49 |

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
[↑ Card Specifications](#user-content-card-specifications)

```python
C18 = Card(
    id=18,  version="v1.0",
    name    = "Dossier Breach",
    tagline = "Penetrate a faction's operational planning before the round begins.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Reveal,  subject = CardHandContents,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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
    arbiter_note = "Privately show target faction's current hand of Covert and Political Act cards to Ghost player. Modifier cards excluded. Do not confirm or announce to the table. Information is solely between Ghost and ARBITER — Ghost may not publicly announce or prove the contents.",
)
```

---

### C19 — DEEP COVER
[↑ Card Specifications](#user-content-card-specifications)

```python
C19 = Card(
    id=19,  version="v1.0",
    name    = "Deep Cover",
    tagline = "Permanently remove a prior operation from the accessible record.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Protect,  subject = ActionAttribution,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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
[↑ Card Specifications](#user-content-card-specifications)

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

### THE DIRECTORATE — C21–C25

*S51: C25 Sealed Border replaced with Tactical Redirection (Territory — Move — Presence token). Block duplication resolved. Mandate generation gap and Public Standing Shift candidate remain open — see D-04-03 PM05.*

### C21 — INVOKE JURISDICTION
[↑ Card Specifications](#user-content-card-specifications)

```python
C21 = Card(
    id=21,  version="v1.0",
    name    = "Invoke Jurisdiction",
    tagline = "Assert institutional authority over a target district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Submission,  function = Block,  subject = CovertOperation,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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
[↑ Card Specifications](#user-content-card-specifications)

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
    target_district=district.any, target_faction=faction(named_opponent), target_object=DeploymentMarker,
    affinity=None,
    restriction = (
        district(target).faction(target).deployment_marker >= 1
        AND intel(faction=faction(target), age_rounds<=1) >= 1
        AND district(target) != ChorusNode.deployment_marker
    ),
    cost        = resource.faction(acting).mandate * 3,
    success     = (
        game.remove(faction(target).deployment_marker, district(target), permanent=True),
        game.dispatch(faction(target), NotificationSlip),
    ),
    successcrit = resource.faction(acting).mandate += 3,
    fail=None,
    failcrit    = faction(acting).standing -= 1,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate does not destroy — it removes from play. Sometimes that is enough.",
    perspectives = {Directorate: "The marker has been detained. Its conversion will not occur."},
    design_note  = "Permanent per Principle 11. Prior version returned marker at end of next round — revised.",
    arbiter_note = "Intel token requirement means Directorate must have gathered intelligence on target faction this or last round.",
)
```

---

### C23 — EVIDENCE PRESERVATION
[↑ Card Specifications](#user-content-card-specifications)

```python
C23 = Card(
    id=23,  version="v1.0",
    name    = "Evidence Preservation",
    tagline = "Lock a written record against modification for the remainder of the session.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Information,  function = Protect,  subject = WrittenRecord,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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
[↑ Card Specifications](#user-content-card-specifications)

```python
C24 = Card(
    id=24,  version="v1.0",
    name    = "Surveillance Placement",
    tagline = "Install permanent monitoring in a target district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Information,  function = Add,  subject = IntelToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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
[↑ Card Specifications](#user-content-card-specifications)

```python
C25 = Card(
    id=25,  version="v1.0",
    name    = "Tactical Redirection",
    tagline = "Reposition institutional presence ahead of a contested exchange.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Move,  subject = PresenceToken,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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

### THE NETWORK — C26–C30

*S51: C27 Source Protection replaced with Disclosure Loop (Economy — Add — Exposure). Doctrinal misalignment resolved; Exposure generation gap addressed. C26/C28 Reveal overlap remains under review. Public Standing Shift covert card still needed — see D-04-04 PM05.*

### C26 — LEAK
[↑ Card Specifications](#user-content-card-specifications)

```python
C26 = Card(
    id=26,  version="v1.0",
    name    = "Leak",
    tagline = "Make one resolved operation's target district public after resolution.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Information,  function = Reveal,  subject = ActionAttribution,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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
[↑ Card Specifications](#user-content-card-specifications)

```python
C27 = Card(
    id=27,  version="v1.0",
    name    = "Disclosure Loop",
    tagline = "Transparency is self-sustaining. Revealing information generates the capacity to reveal more.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Economy,  function = Add,  subject = Exposure,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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
[↑ Card Specifications](#user-content-card-specifications)

```python
C28 = Card(
    id=28,  version="v1.0",
    name    = "Open Channel",
    tagline = "Force private ARBITER notifications to a faction to be delivered publicly.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Information,  function = Reveal,  subject = PrivateCommunications,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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
[↑ Card Specifications](#user-content-card-specifications)

```python
C29 = Card(
    id=29,  version="v1.0",
    name    = "Network Cascade",
    tagline = "Extend Broadcast Interference to an adjacent district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Submission,  function = Modify,  subject = PoliticalAct,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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
[↑ Card Specifications](#user-content-card-specifications)

```python
C30 = Card(
    id=30,  version="v1.0",
    name    = "Community Anchor",
    tagline = "Establish presence in a Baryo district through existing relationships.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Territory,  function = Add,  subject = PresenceToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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

### THE SYNDICATE — C31–C35

*Current cards carried forward. Taxonomy gap analysis in Artifact 04b §8.4 identifies redesign targets: zero information/intelligence capability; Cross-Category — Corrupt Accord unused; Resource — Redirect Accord ("small print") unused.*

### C31 — LEVERAGED ACQUISITION
[↑ Card Specifications](#user-content-card-specifications)

```python
C31 = Card(
    id=31,  version="v1.0",
    name    = "Leveraged Acquisition",
    tagline = "Gain resource generation from a district without presence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Add,  subject = NativeResource,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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
[↑ Card Specifications](#user-content-card-specifications)

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
[↑ Card Specifications](#user-content-card-specifications)

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
[↑ Card Specifications](#user-content-card-specifications)

```python
C34 = Card(
    id=34,  version="v1.0",
    name    = "Golden Parachute",
    tagline = "Transfer resources before a forced resource-loss event.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Protect,  subject = NativeResource,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    target_district=None, target_faction=faction(named), target_object=NativeResource,
    affinity=None,
    restriction=None,  # player judgment — submitted when resource-loss event is anticipated this round
    cost=None,
    success     = game.transfer(faction(acting).capital, count=3, to=faction(target), pre_loss_calc=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},
    narrative   = "The Syndicate plans for outcomes not yet confirmed. They move assets before the decision is made.",
    perspectives = {Syndicate: "We did not lose those resources. We repositioned them. There is a difference."},
    design_note  = "Transfer cannot be reclaimed after execution. Transferred Capital exits Syndicate's pool before any resource-loss calculation applies this round.",
    arbiter_note = "Record transfer privately. Do not announce to table. Transferred Capital exits Syndicate's pool before resource-loss calculations this round.",
)
```

---

### C35 — REGULATORY CAPTURE
[↑ Card Specifications](#user-content-card-specifications)

```python
C35 = Card(
    id=35,  version="v1.0",
    name    = "Regulatory Capture",
    tagline = "Block a specific action type in a named district for one round.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Submission,  function = Block,  subject = NamedActionType,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
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

---

### Intel Economy Cards — C36–C42

*Draft specifications. Locked by L145–L148 (S37). Full §6 schema pass required (04-47). These cards establish the universal Intel token economy that closes PM05 04-41.*

---

### C36 — SYNTHESIZE

- **Card ID:** C36
- **Card name:** Synthesize
- **Tagline:** *Convert raw intelligence into operational clarity.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Ghost only.
- **Beat:** 3
- **Target district:** N/A
- **Target faction:** N/A
- **Target object:** Intel token
- **Restriction:** Requires at least 1 Intel token held by Ghost at time of submission.
- **Primary cost qty:** 1
- **Primary cost type:** Faction native (Findings)
- **Secondary cost qty:** 1
- **Secondary cost type:** Intel token
- **Faction affinity:** Ghost only.
- **Difficulty:** N/A
- **Crit success:** N/A — Automatic.
- **Success:** Spend 1 Intel token; gain 3 Intel tokens. Net: +2 Intel.
- **Failure:** N/A — Automatic.
- **Crit failure:** N/A — Automatic.
- **Portrait:** +1 Ghost Submitter.
- **Narrative anchor:** *Raw surveillance is noise. What Ghost does to it — that is signal.*
- **Faction perspectives:**
  - Ghost: *We don't just gather. We process. The difference is what we are.*
- **Design note:** Designed for the GATHER→SYNTHESIZE Double Case Pass combo (L145). Play GATHER (C05) in Month 1 to acquire Intel; play SYNTHESIZE in Month 2 using the acquired token. Affords Ghost a compounding intelligence advantage within a single Quarter. Intel token consumed is any held token — not required to be faction-indexed.
- **Taxonomy:** Resource — Add — Intel token.

---

### C37 — SACRIFICE

- **Card ID:** C37
- **Card name:** Sacrifice
- **Tagline:** *Burn The Network's institutional credibility for an intelligence edge.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Network only.
- **Beat:** 3
- **Target district:** N/A
- **Target faction:** N/A
- **Target object:** N/A
- **Restriction:** None.
- **Primary cost qty:** 1
- **Primary cost type:** Public Standing (direct track step — Network Submitter moves down 1 on the PS track; not a resource spend)
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Network only.
- **Difficulty:** N/A
- **Crit success:** N/A — Automatic.
- **Success:** Gain 1 Intel token.
- **Failure:** N/A — Automatic.
- **Crit failure:** N/A — Automatic.
- **Portrait:** N/A (the PS track loss is the cost, not a Portrait adjustment).
- **Narrative anchor:** *The Network knows: sometimes you spend credibility like currency. This is one of those times.*
- **Faction perspectives:**
  - Network: *Standing is not an end. It is a means. And sometimes a means must be spent.*
- **Design note:** Converts Public Standing directly into Intel. Network Submitter loses 1 step on the PS track — this is the payment, not a portrait effect. Generates Intel without a specific target district or faction. Cost representation pending full schema review in 04-47.
- **Taxonomy:** Resource — Convert — Public Standing (to Intel token).

---

### C38 — PARASITIC

- **Card ID:** C38
- **Card name:** Parasitic
- **Tagline:** *Wire a district's commerce. Let others do the work.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Syndicate only.
- **Beat:** 2
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** District (Capital flows)
- **Restriction:** None.
- **Primary cost qty:** 2
- **Primary cost type:** Capital
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Syndicate only.
- **Difficulty:** N/A
- **Crit success:** N/A — Automatic.
- **Success:** Place a PARASITIC marker on the named district. If any faction successfully extracts Capital (native or district resource) from that district this Month, Syndicate gains 1 Intel token. ARBITER delivers at end of Beat 3.
- **Failure:** N/A — Automatic.
- **Crit failure:** N/A — Automatic.
- **Portrait:** +1 Syndicate Submitter (if Intel is collected this Month). N/A if no Capital extraction occurs.
- **Narrative anchor:** *The Syndicate does not steal from the river. They build a weir.*
- **Faction perspectives:**
  - Syndicate: *We invested in the district's infrastructure. Why shouldn't we see what moves through it?*
- **Design note:** Conditional Intel generation. Syndicate profits from other factions' economic activity. Requires ARBITER to track Capital extraction in the marked district through Beat 3. Physical PARASITIC marker component needed — flag for Art 07 / component spec. Portrait trigger is conditional on activation.
- **Taxonomy:** Resource — Add — Intel token (conditional trigger).

---

### C39 — ABSOLUTE COMPROMISE

- **Card ID:** C39
- **Card name:** Absolute Compromise
- **Tagline:** *Some barriers are not barriers at all — just the illusion of one.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Faction:** All.
- **Beat:** 2
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** Block or Protect card in Beat 2 row
- **Restriction:** Must target a face-up Beat 2 Block (Type A Countermeasure) or Protect operation in the named district.
- **Primary cost qty:** 1
- **Primary cost type:** Intel token
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** N/A.
- **Difficulty:** N/A
- **Crit success:** N/A — Automatic.
- **Success:** The named Beat 2 Block or Protect card is discarded. Its effect does not apply this Month. Resources committed to the blocked card are not refunded. The operations it would have blocked or protected against proceed without that modifier.
- **Failure:** N/A — Automatic.
- **Crit failure:** N/A — Automatic.
- **Portrait:** N/A.
- **Narrative anchor:** *There are no walls. There are only varying degrees of access.*
- **Design note:** Intel cost makes this a premium counter. Intel token consumed is any held token. Cannot target Type B Countermeasures (faction defense) — only Type A (District Block) and Protect/Fortify operations. Extends Beat 2 interactions; processes in Beat 2 row alongside Countermeasures and Protect.
- **Taxonomy:** Action — Block — Positional wager (Block + Protect).

---

### C40 — WEAPONIZED TRANSPARENCY

- **Card ID:** C40
- **Card name:** Weaponized Transparency
- **Tagline:** *Exposure is not a threat. It is a delivery mechanism.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Network only.
- **Beat:** 3
- **Target district:** N/A
- **Target faction:** Named opponent faction
- **Target object:** Public Standing / Covert operation
- **Restriction:** None.
- **Primary cost qty:** 1
- **Primary cost type:** Intel token
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Network only.
- **Difficulty:** N/A
- **Crit success:** N/A — Automatic.
- **Success:** Choose one: (A) Target faction loses 1 Public Standing step — unblockable, no Countermeasure may prevent this; or (B) Target faction must submit their Month 2 covert action cards face-up (revealed play). If this is Month 2, the revealed play applies to Month 3 political acts instead.
- **Failure:** N/A — Automatic.
- **Crit failure:** N/A — Automatic.
- **Portrait:** +1 Network Submitter.
- **Narrative anchor:** *The Network does not publish what it knows. It delivers it — privately, precisely, to exactly one person.*
- **Faction perspectives:**
  - Network: *Transparency is a tool. We decide when and where to deploy it.*
- **Design note:** Intel cost is the authorization. The card represents The Network leveraging gathered intelligence as a coercive instrument rather than a public broadcast. Option A (PS drop) is unblockable by design — this is The Network's doctrine differentiator. Option B (revealed play) introduces information asymmetry. ARBITER enforces revealed play rule at next Month's Dispatch.
- **Taxonomy:** Action — Shift (PS) / Reveal — Public Standing / Covert operation.

---

### C41 — CORPORATE BLACKMAIL

- **Card ID:** C41
- **Card name:** Corporate Blackmail
- **Tagline:** *Leverage converts intelligence into compliance.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Syndicate only.
- **Beat:** 3
- **Target district:** N/A
- **Target faction:** Named opponent faction
- **Target object:** Capital / Accord agreement
- **Restriction:** Option B (force Yes vote) only valid if an Accord is proposed during Debrief this Quarter.
- **Primary cost qty:** 1
- **Primary cost type:** Intel token
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Syndicate only.
- **Difficulty:** N/A
- **Crit success:** N/A — Automatic.
- **Success:** Choose one: (A) Target faction transfers 2 Capital to Syndicate immediately. No negotiation. ARBITER enforces. Or (B) Target faction must vote 'Yes' on the next Accord proposal directed at them during Debrief this Quarter.
- **Failure:** N/A — Automatic.
- **Crit failure:** N/A — Automatic.
- **Portrait:** −1 Syndicate Flat (blackmail corrodes everyone's trust in the system, regardless of who submits it).
- **Narrative anchor:** *The information was gathered properly. What is done with it is simply business.*
- **Faction perspectives:**
  - Syndicate: *We don't call it blackmail. We call it accelerated negotiation.*
- **Design note:** Option A (Capital theft) is unconditional — no block. Option B (forced Yes vote) requires an Accord context; if no Accord is proposed, Option B cannot be chosen. ARBITER tracks the forced vote through Debrief. Flat portrait modifier (−1 Syndicate regardless of who submits) reflects systemic corruption effect; subject to review during full Portrait economy analysis (PM05 04-21).
- **Taxonomy:** Resource — Steal (Capital) / Action — Force (Accord vote).

---

### C42 — SANCTIONED RAID

- **Card ID:** C42
- **Card name:** Sanctioned Raid
- **Tagline:** *Not every operation leaves a paper trail.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Directorate only.
- **Beat:** 3
- **Target district:** Any district
- **Target faction:** Named opponent faction
- **Target object:** Presence token
- **Restriction:** None.
- **Primary cost qty:** 1
- **Primary cost type:** Mandate
- **Secondary cost qty:** 1
- **Secondary cost type:** Intel token
- **Faction affinity:** Directorate only.
- **Difficulty:** Challenging (25) + ring modifier
- **Resolution:** d100
- **Resolution type:** Probabilistic
- **Crit success:** Remove all named faction's presence chips from the named district. Directorate gains 1 Mandate from Reservoir.
- **Success:** Remove all named faction's presence chips from the named district. Ignores Block cards, Type A and Type B Countermeasures, and Protect operations. No Public Standing penalty to acting faction.
- **Failure:** No effect. Intel token and Mandate spent.
- **Crit failure:** No effect. Intel token and Mandate spent. Notification slip delivered to target.
- **Portrait:** +1 Directorate Submitter.
- **Narrative anchor:** *The Directorate does not ask permission. It records the action and moves on.*
- **Faction perspectives:**
  - Directorate: *The intelligence warranted the action. The action was authorised. There is nothing further to say.*
- **Design note:** The Intel cost represents the intelligence that justifies the raid — without prior surveillance, the Directorate cannot sanction the action. The "ignores blocks" property makes this a premium Directorate capability. Difficulty Challenging (rather than Automatic) reflects that even sanctioned operations can fail. ARBITER removes presence chips; acting Faction Player updates Control flags and Established markers.
- **Taxonomy:** Action — Remove — Presence token.

---

## 9. Standard Political Acts — P01–P08


Political acts use the same data schema as covert operations (§6) with two additional fields:

| Additional Field | Description |
|-----------------|-------------|
| **Popularity effect** | Popularity movement on success and failure. |
| **Declaration requirement** | Any verbal or physical declaration required at time of play. |

Political acts are Beat 4 cards unless otherwise specified.

| Card ID | Name | Primary taxonomy | Faction affinity | Status |
|---------|------|-----------------|-----------------|--------|
| P01 | Establish Presence | Territory — Add — Presence token | Directorate | Pending full data structure |
| P02 | Contest | Territory — Remove — Presence token (contested) | Directorate, Network | Pending |
| P03 | Commission | Territory — Add — Structure block (both districts) | Guild | Pending |
| P04 | Denounce | Standing — Shift — Public Standing (−) | Network, Directorate | Pending |
| P05 | Broadcast | Information — Reveal — Action attribution | Network | Pending |
| P06 | Leverage | Economy — Remove — Native resource | Syndicate | Pending |
| P07 | Invoke the Table | Submission — Block — Any (procedural) | Directorate | Pending |
| P08 | Propose Accord | Economy — Add — Accord agreement | Directorate | Pending |

---

## 10. Faction-Specific Political Acts — P09–P18

*Status: Same as §9 — pending full card data structure revision.*

| Card ID | Name | Faction | Primary taxonomy | Status |
|---------|------|---------|-----------------|--------|
| P09 | Public Works Declaration | Guild | Territory — Add — Structure block (both districts) | Pending |
| P10 | Infrastructure Bond | Guild | Economy — Add — Native resource (target faction) | Pending |
| P11 | Issue Directive | Directorate | Submission — Block — Political act | Pending |
| P12 | Convene an Inquiry | Directorate | Economy — Add — Intel token | Pending |
| P13 | Public Disclosure | Network | Information — Reveal — Action attribution | Pending |
| P14 | Open Record Request | Network | Information — Reveal — Written record | Pending |
| P15 | Acquisition Offer | Syndicate | Territory — Redirect — Presence token | Pending |
| P16 | Market Pressure | Syndicate | Submission — Modify — Covert + Political act (cost) | Pending |
| P17 | Publish Analysis | Ghost | Cross-Category — Shift — Chorus Portrait | Pending |
| P18 | Signal Review Request | Ghost | Resolution — Modify — Covert operation (difficulty) | Pending |

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
| Reach extension | Apply a political act to a non-operational-marker district |

---

## 12. Rules & Constraints — Pass Cards

**Four variants per faction.** Kept beside the tableau — not drawn from any deck. Reusable every round. Neutral grey back. Each faction holds one of each variant.

**Generalized — Beat 3 or Beat 4.** The same Pass card is valid in either context. No specialized covert-only or political-only Pass cards.

**In dispatch case (Beat 3):** Signals that covert operation slot is intentionally empty. Three Pass cards with no operations = Full Covert Pass — legal, noted.

**At Declaration (Beat 4):** Place face-up instead of declaring a political act.

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

Countermeasure cards interact with covert operations only — not political acts. Type A (district block) blocks covert operations targeting the named district. Type B (faction defense) reduces covert operation difficulty against that faction's assets. Full Countermeasure card design pending D-04-12.

### 14.3 Resource Availability Constraint

Covert operation resources must be physically present in the dispatch case at Beat 3. Political act resources must be physically paid at Declaration. If absent:
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
| D-04-06 | Political acts P01–P18 full card data structure review — all fields (Beat, Taxonomy, Faction perspectives, Restriction, crit effects, Portrait) need card-by-card application. | Artifact 09 |
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
