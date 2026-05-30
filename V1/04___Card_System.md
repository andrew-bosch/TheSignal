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

*Faction alignment map: Whiteboard/faction_pentagram_alignment.md — pending canonical home in Art 00 §7.*

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
    ring_mod:     dict[Ring, int] | None    # None when no ring variation
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
    flat:          int | None         # fires on resolution regardless of submitter — faction-specific cards only (L131)
    submitter:     int | None         # fires when this faction submits the card
    condition:     BoolExpr | None    # condition on submitter modifier
    modifier:      int | None         # adjustment to submitter under condition
    mod_condition: BoolExpr | None    # when modifier applies
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
Ring:         0 (Chorus Node) | 1 (Core) | 2 (The Mid) | 3 (Baryo)
OutcomeType:  Binary | ElectPlayer | ElectDistrict | ElectFaction | BilateralAgreement | Unilateral
```

---

### 6.4 Visibility Rules

Three rules replace per-field VS-xx notation:

- **VS-01 (Public):** All fields not listed below
- **VS-04 (ARBITER-only):** `design_note`, `arbiter_note`
- **VS-06 (Hidden until resolution):** `success`, `successcrit`, `fail`, `failcrit`, `portrait`

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

```python
C01 = Card(
    id      = "C01",  version = "v1.1",
    name    = "Build Structure",
    tagline = "Construct a physical installation in a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Add,  subject = StructureBlock,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    affinity    = faction(acting) == Guild: cost.resource.district(native) = 0,
    restriction = (
        district.faction(acting).presence > 0 and
        district.faction(acting).structure == 0
    ),
    cost = resource.faction(acting) * 1 + resource.district(native) * 1,

    success     = district(target).faction(acting).structure += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "Every faction that wants to matter in New Meridian eventually has to build something.",
    perspectives = {
        Guild:       "This is what we do. Every structure we build is an argument that permanence is possible here.",
        Directorate: "Infrastructure serves order. We will use it if it serves the mandate.",
        Network:     "Building is a statement of intent. We watch carefully to understand what kind.",
        Ghost:       "A structure is a commitment. Commitments are data points.",
        Syndicate:   "Every structure generates value. The question is who captures it.",
    },
    design_note  = "Construction is publicly visible — result announced at resolution. The covert element is the intent. The Guild-as-infrastructure-provider doctrine: every structure in New Meridian, regardless of who commissions it, is in some sense a Guild project.",
    arbiter_note = None,
)
```

---

### C02 — DEMOLISH
[↑ Card Specifications](#user-content-card-specifications)

```python
C02 = Card(
    id      = "C02",  version = "v1.1",
    name    = "Demolish",
    tagline = "Remove an opponent's structure from a district.",
    type    = CovertOperation,  subtype = Standard,  faction = All,

    layer    = Territory,  function = Remove,  subject = StructureBlock,

    beat            = 3,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = StructureBlock,

    affinity    = None,
    restriction = (
        district(self|adjacent).faction(acting).presence > 0 and
        district.faction(target).structure > 0
    ),
    cost = resource.faction(acting) * 1 + resource.district(native) * 1,

    success     = district(target).faction(target).structure -= 1,
    successcrit = resource.faction(acting).native += 1,
    fail        = None,
    failcrit    = faction(acting).standing -= 1,

    portrait = {Guild: PortraitEntry(submitter=-1)},

    narrative    = "Not everything built in New Meridian was meant to last.",
    perspectives = {
        Guild:       "We build. We do not unmake. Every time we perform this action something has gone badly wrong.",
        Directorate: "Demolition is a last resort. Structures represent investment in the city we are here to protect.",
        Network:     "Sometimes the infrastructure of control needs to come down before something better can be built.",
        Ghost:       "A demolished structure tells us as much as a standing one. We note the absence.",
        Syndicate:   "Assets change hands. Sometimes the most efficient transfer is removal.",
    },
    design_note  = "Structure removal is publicly visible. Source of removal is not announced.",
    arbiter_note = None,
)
```

---

### C03 — CAMPAIGN
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C03
- **Card version:** v1.1
- **Card name:** Campaign
- **Tagline:** *Build local support and deepen presence in a district.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Territory
- **Function:** Add
- **Subject:** Presence token

- **Design note:** C03 mirrors C01 structurally — Build Structure is the Guild's native action, Campaign is the Network's.
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *Presence without roots is just occupation.*
- **Faction perspectives:**
  - Guild: *Presence is the foundation everything else is built on. We are methodical about this.*
  - Directorate: *Authority requires visibility. We establish presence where the mandate requires it.*
  - Network: *Every person we reach in a district is a relationship. Relationships are how things actually change.*
  - Ghost: *Presence creates exposure. We expand only when the intelligence justifies the risk.*
  - Syndicate: *Market position requires footprint. We place ourselves where the returns justify it.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** N/A
- **Restriction:** Acting faction must have at least 1 presence in the target district.
- **Primary cost qty:** 1
- **Primary cost type:** Faction native
- **Secondary cost qty:** 1
- **Secondary cost type:** District native
- **Faction affinity:** Network.
- **Affinity bonus:** Secondary cost −1.
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Place 1 additional presence token in the target district.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | +1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C04 — UNDERMINE
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C04
- **Card version:** v1.1
- **Card name:** Undermine
- **Tagline:** *Erode an opponent's presence in a district.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Territory
- **Function:** Remove
- **Subject:** Presence token

- **Design note:** Portrait values reflect doctrinal alignment — Ghost and Syndicate omitted, neither strongly aligned nor opposed.
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *The most effective opposition leaves no visible wound.*
- **Faction perspectives:**
  - Guild: *We do not erase what others have built. Even our enemies.*
  - Directorate: *Covert erosion is not governance. Unless the target is The Network — then it is public safety.*
  - Network: *Entrenched presence does not become legitimate just because it has been there long enough.*
  - Ghost: *Disruption without intelligence purpose is noise. We prefer signal.*
  - Syndicate: *If their presence can be eroded, it was never well-positioned to begin with.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** Named opponent faction
- **Target object:** Presence token
- **Restriction:** Acting faction must have at least 1 presence in the target district or in a district adjacent to the target district. Target faction must have at least 1 presence token in the target district.
- **Primary cost qty:** 1
- **Primary cost type:** Faction native
- **Secondary cost qty:** 1
- **Secondary cost type:** District native
- **Faction affinity:** N/A
- **Affinity bonus:** N/A
- **Difficulty:** Average (50) + ring modifier
- **Ring 0 modifier:** −15
- **Ring 1 modifier:** −10
- **Ring 2 modifier:** 0
- **Ring 3 modifier:** +10
- **Resolution:** d100
- **Resolution type:** Probabilistic
- **Outcome type:** N/A

**Effects**

- **Crit success:** +1 presence token removed.
- **Success:** Remove 1 presence token from target faction in target district.
- **Failure:** No effect.
- **Crit failure:** −1 Public Standing.

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | −1 | N/A | N/A | N/A |
| Directorate | N/A | −1 | Except when targeting Network | N/A | N/A |
| Network | N/A | +1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C05 — GATHER
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C05
- **Card version:** v1.1
- **Card name:** Gather
- **Tagline:** *Extract actionable intelligence about a specific faction's operations.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Economy
- **Function:** Add
- **Subject:** Intel token

- **Design note:** No secondary cost — observation does not consume local resources. Ghost exemption from adjacency reflects doctrine: remote analysis does not require physical proximity.
- **Arbiter context:** Ghost affinity: ring penalties still apply. Intel token marked with faction name and round number. Crit failure notification slip delivered in case: *"An unknown party attempted to access sensitive information about your operations in [district]. The attempt was identified and neutralised. Exercise appropriate caution."*

**Narrative**

- **Narrative anchor:** *In New Meridian, knowing is the first form of power.*
- **Faction perspectives:**
  - Guild: *Intelligence informs construction. We gather when we need to build smarter.*
  - Directorate: *Information is the foundation of legitimate authority. We collect it formally.*
  - Network: *The city speaks constantly. We listen for the gaps between what is said and what is true.*
  - Ghost: *This is what we are here for. Everything else follows from understanding.*
  - Syndicate: *Information has market value. We acquire it when the return justifies the cost.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** Named opponent faction
- **Target object:** N/A
- **Restriction:** Acting faction must have at least 1 presence in the target district or in a district adjacent to the target district. Ghost is exempt from this restriction.
- **Primary cost qty:** 1
- **Primary cost type:** Faction native
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Ghost.
- **Affinity bonus:** +25 modifier.
- **Difficulty:** Average (50) + ring modifier
- **Ring 0 modifier:** −15
- **Ring 1 modifier:** −10
- **Ring 2 modifier:** 0
- **Ring 3 modifier:** +10
- **Resolution:** d100
- **Resolution type:** Probabilistic
- **Outcome type:** N/A

**Effects**

- **Crit success:** +1 Intel token.
- **Success:** 1 Intel token for the named faction delivered in case.
- **Failure:** No effect.
- **Crit failure:** Notification slip delivered to target faction.

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | +1 | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C06 — BROADCAST INTERFERENCE
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C06
- **Card version:** v1.1
- **Card name:** Broadcast Interference
- **Tagline:** *Disrupt public communications in a district, dampening political activity.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Submission
- **Function:** Modify
- **Subject:** Political act (cost)

- **Design note:** Exposure is The Network's native resource. Non-Network factions acquire Exposure through district incursion or trade at 4:1. No presence requirement — signal disruption is broadcast.
- **Arbiter context:** Beat 2 — ARBITER retains awareness after case opening. At Beat 4 declaration, ARBITER intercepts political acts targeting the affected district and states the additional cost before declaration is confirmed. Faction may proceed or withdraw.

**Narrative**

- **Narrative anchor:** *People don't act naturally when they know they're being watched.*
- **Faction perspectives:**
  - Guild: *Disrupting communications delays approvals, permits, agreements. We feel this more than most.*
  - Directorate: *Interference with public communications is a jurisdictional matter. We note who is responsible.*
  - Network: *Noise is a tool. Sometimes silence is louder than anything we could broadcast.*
  - Ghost: *Interference creates analytical cover. We appreciate the quiet.*
  - Syndicate: *Disrupted communications create market inefficiencies. Those can be profitable.*

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** Political act
- **Restriction:** None.
- **Primary cost qty:** 2
- **Primary cost type:** Exposure
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Network.
- **Affinity bonus:** Primary cost −1.
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Positional wager
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Political acts declared against the target district this round cost +1 additional native resource.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | +1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C07 — AMPLIFY
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C07
- **Card version:** v1.1
- **Card name:** Amplify
- **Tagline:** *Boost the Public Standing impact of your own political act this round.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Resolution
- **Function:** Modify
- **Subject:** Political act (outcome scale)

- **Design note:** Amplification cuts both ways — a failed political act that loses −1 Public Standing loses −2 instead.
- **Arbiter context:** Beat 2 — ARBITER retains awareness at resolution. Effect applied when political act resolves in Beat 4. [Beat 4 handling: TBD.] [TBD: how to flag submitting faction using Pass in Declaration step — restriction enforcement mechanism.]

**Narrative**

- **Narrative anchor:** *A message worth sending is worth sending loudly.*
- **Faction perspectives:**
  - Guild: *We let our structures speak. Amplification is for those who lack physical evidence.*
  - Directorate: *Institutional authority does not require amplification. Though we note its effectiveness.*
  - Network: *Every message we send should land as hard as possible. This ensures it does.*
  - Ghost: *Amplification is the opposite of what we do. Volume attracts attention. Attention ends operations.*
  - Syndicate: *Leverage applied at the right moment can move markets. This is that tool.*

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target district:** N/A
- **Target faction:** Self
- **Target object:** Political act
- **Restriction:** Acting faction must declare a political act this round. Cannot target a Pass.
- **Primary cost qty:** 2
- **Primary cost type:** Exposure
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Network.
- **Affinity bonus:** Primary cost −1.
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Public Standing impact of the declared political act is doubled — positive or negative.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | −1 | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C08 — BUY INFLUENCE
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C08
- **Card version:** v1.1
- **Card name:** Buy Influence
- **Tagline:** *Deploy capital to place presence tokens directly, without groundwork.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Territory
- **Function:** Add
- **Subject:** Presence token

- **Design note:** No secondary cost — Capital bypasses local knowledge requirements. No presence requirement — primary entry mechanism for new districts. Syndicate affinity is difficulty reduction not cost reduction — better outcomes from spending, not discounts. Three Portrait penalties reflect strong doctrinal opposition.
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *In New Meridian, capital is a language everyone understands.*
- **Faction perspectives:**
  - Guild: *Presence earned through investment rather than community is fragile. We have seen it collapse.*
  - Directorate: *Purchasing influence undermines the legitimate institutional processes we exist to maintain.*
  - Network: *This is exactly the kind of power we are here to expose and resist.*
  - Ghost: *Bought presence is noisier than earned presence. It draws the wrong kind of attention.*
  - Syndicate: *Capital does not just open doors. It determines which doors exist in the first place.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** N/A
- **Restriction:** None.
- **Primary cost qty:** 3
- **Primary cost type:** Capital
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Syndicate.
- **Affinity bonus:** +25 modifier.
- **Difficulty:** Average (50) + ring modifier
- **Ring 0 modifier:** −15
- **Ring 1 modifier:** −10
- **Ring 2 modifier:** 0
- **Ring 3 modifier:** +10
- **Resolution:** d100
- **Resolution type:** Probabilistic
- **Outcome type:** N/A

**Effects**

- **Crit success:** +1 presence token placed.
- **Success:** Place 2 presence tokens in the target district.
- **Failure:** No effect.
- **Crit failure:** −2 Public Standing.

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | −1 | N/A | N/A | N/A |
| Directorate | N/A | −1 | N/A | N/A | N/A |
| Network | N/A | −1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | +1 | N/A | N/A | N/A |

---

### C09 — FUND
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C09
- **Card version:** v1.1
- **Card name:** Fund
- **Tagline:** *Transfer resources to another faction as a gesture of support.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Economy
- **Function:** Redirect
- **Subject:** Native resource

- **Design note:** No ring modifier — targets a faction not a district. Source anonymous by default. Acting faction may announce after receiving free Accord card from ARBITER.
- **Arbiter context:** Transfer handled covertly at case return — resources appear in recipient's case at debrief. Recipient may convert received Capital to native resource at 1:1. Free Accord card is a Political Act card (cost 0; return to ARBITER on play — not discarded) delivered to acting faction's hand at case resolution. Played in a subsequent Quarter — card returns in the dispatch case after Resolution, by which point Declaration for the current Quarter has already closed.

**Narrative**

- **Narrative anchor:** *Every alliance in New Meridian begins with someone extending a hand.*
- **Faction perspectives:**
  - Guild: *Investment in relationships is as important as investment in structures.*
  - Directorate: *Financial transfers between factions warrant scrutiny. We monitor these carefully.*
  - Network: *Follow the money. It always leads somewhere interesting.*
  - Ghost: *Resources flowing between factions change the operational landscape. We note the direction.*
  - Syndicate: *Capital in motion creates relationships. Relationships create opportunities.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** N/A
- **Target faction:** Named opponent faction
- **Target object:** Native resource
- **Restriction:** None.
- **Primary cost qty:** 2
- **Primary cost type:** Capital
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Syndicate.
- **Affinity bonus:** +25 modifier.
- **Difficulty:** Average (50)
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** d100
- **Resolution type:** Probabilistic
- **Outcome type:** N/A

**Effects**

- **Crit success:** +1 Public Standing.
- **Success:** Transfer occurs. Free Accord card delivered.
- **Failure:** No effect.
- **Crit failure:** −1 Public Standing.

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | +1 | N/A | N/A | N/A |

---

### C10 — PROTECT
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C10
- **Card version:** v1.1
- **Card name:** Protect
- **Tagline:** *Defend a district's assets from covert disruption this round.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Resolution
- **Function:** Protect
- **Subject:** Covert operation (difficulty)

- **Design note:** Applies only to acting faction's assets — not all factions' assets.
- **Arbiter context:** Beat 2 — at resolution, ARBITER places −25 marker (−45 with Guild/Directorate affinity) directly on each Beat 3 covert operation in the grid targeting the acting faction's assets in the target district.

**Narrative**

- **Narrative anchor:** *What you build is only worth as much as your willingness to defend it.*
- **Faction perspectives:**
  - Guild: *We protect what we build. This is not optional.*
  - Directorate: *Institutional assets require active defense. We resource this accordingly.*
  - Network: *We protect our people first. Infrastructure is secondary.*
  - Ghost: *The best protection is not being found in the first place.*
  - Syndicate: *Protected assets retain value. Unprotected assets invite acquisition.*

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** Covert operation
- **Restriction:** Acting faction must have at least 1 presence token in the target district.
- **Primary cost qty:** 1
- **Primary cost type:** District native
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Guild, Directorate.
- **Affinity bonus:** Success −20.
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Positional wager
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** All covert operations targeting the acting faction's assets in the target district this round have their threshold reduced by −25.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | +1 | N/A | N/A | N/A |
| Directorate | N/A | +1 | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

## 8. Faction-Specific Covert Operations — C11–C35



---

### THE GUILD — C11–C15

### C11 — FORTIFY STRUCTURE
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C11
- **Card version:** v1.1
- **Card name:** Fortify Structure
- **Tagline:** *Reinforce a structure against demolition this Quarter.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Guild
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Territory
- **Function:** Protect
- **Subject:** Structure block

- **Design note:** N/A
- **Arbiter context:** ARBITER retains awareness after Beat 2 opens. Immunity applied when C02 Demolish resolves in Beat 3.

**Narrative**

- **Narrative anchor:** *The Guild does not abandon what it has built.*
- **Faction perspectives:**
  - Guild: *Reinforcement is not fear. It is preparation.*
  - Network: *Hardened walls are preparation. What's inside them decides whether the cost was worth it.*
  - Directorate: *A structure immune to demolition is a structure immune to code review. We notice these arrangements.*

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** Structure block
- **Restriction:** Acting faction must have a structure in the target district.
- **Primary cost qty:** 1
- **Primary cost type:** Capacity
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Guild only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Positional wager
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Guild structure in target district is immune to Demolish this Quarter.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | +1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C12 — MATERIALS ACQUISITION
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C12
- **Card version:** v1.1
- **Card name:** Materials Acquisition
- **Tagline:** *Recover the costs of demolition as subcontract payment.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Guild
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Economy
- **Function:** Recover
- **Subject:** Native resource

- **Design note:** Guild names target faction at submission — betting one of three Beat 2 action slots that the target will execute C02 this Quarter. The slot is the cost; a wrong read means a wasted action. Success mirrors C02's cost exactly — if C02's cost changes in playtesting, C12's reward scales automatically.
- **Arbiter context:** ARBITER confirms trigger at Beat 3. Only the first qualifying Demolish this Quarter triggers. Effect delivered in case.

**Narrative**

- **Narrative anchor:** *In New Meridian, even demolition is a Guild service.*
- **Faction perspectives:**
  - Guild: *We do not need to swing the hammer ourselves. We simply ensure we are paid when someone else does.*
  - Syndicate: *Positioning to profit from someone else's action before they take it. The instinct is sound. We simply call it by a different name.*
  - Ghost: *A faction that announces it expects demolition before demolition happens has already told us what it knows.*

**Mechanics**

- **Beat:** 2
- **Trigger condition:** Target faction completes C02 Demolish this Quarter.
- **Target district:** N/A
- **Target faction:** Named opponent faction
- **Target object:** Native resource
- **Restriction:** N/A
- **Primary cost qty:** N/A
- **Primary cost type:** N/A
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Guild only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Positional wager
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Target faction native resource + district native resource.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | +1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C13 — FOUNDATION RIGHTS
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C13
- **Card version:** v1.1
- **Card name:** Foundation Rights
- **Tagline:** *Claim a foothold in territory no other faction has entered.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Guild
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Territory
- **Function:** Add
- **Subject:** Presence token

- **Design note:** No secondary cost — unclaimed districts have no established resource infrastructure. Crit fail delivers an intel token to Directorate because a failed foundation claim is a regulatory event — a permit application that collapsed. Directorate holds that record; Guild never knows the paper trail exists.
- **Arbiter context:** On crit fail: deliver 1 intel token naming Guild to Directorate player via case. Do not notify Guild.

**Narrative**

- **Narrative anchor:** *The Guild was here before the city had a name.*
- **Faction perspectives:**
  - Guild: *Unclaimed territory is not unknown to us. We have records going back further than anyone else at this table.*
  - Network: *The Guild's records go back further than ours. What they do with that history is what we watch.*
  - Directorate: *Precedence is established through legal process, not through whoever kept the longer archive.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** N/A
- **Restriction:** Target district must have zero presence from any faction.
- **Primary cost qty:** 1
- **Primary cost type:** Capacity
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Guild only.
- **Affinity bonus:** N/A
- **Difficulty:** 25
- **Ring 0 modifier:** −15
- **Ring 1 modifier:** −10
- **Ring 2 modifier:** 0
- **Ring 3 modifier:** +10
- **Resolution:** d100
- **Resolution type:** Probabilistic
- **Outcome type:** N/A

**Effects**

- **Crit success:** Place 1 presence token and 1 structure block in target district.
- **Success:** Place 1 presence token in the target district.
- **Failure:** No effect.
- **Crit failure:** +1 Guild Intel Token → Directorate.

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | +1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C14 — CONSTRUCTION CREW
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C14
- **Card version:** v1.1
- **Card name:** Construction Crew
- **Tagline:** *Build a structure before your presence is fully established.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Guild
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Submission
- **Function:** Remove Restriction
- **Subject:** Covert operation (presence requirement)

- **Design note:** Premium play — 3 Capacity and d100 for simultaneous presence and structure anywhere.
- **Arbiter context:** Crit fail: deliver 1 Guild Intel Token → Ghost and 1 district native → Syndicate via case. Do not notify Guild.

**Narrative**

- **Narrative anchor:** *The Guild does not always wait for permission.*
- **Faction perspectives:**
  - Guild: *Sometimes the crews arrive before the paperwork. This is not an accident.*
  - Network: *We know this method. Presence before permission is how this city was actually built.*
  - Ghost: *Establishing presence before authorization is requested — the Guild is better at covert operations than they admit.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** N/A
- **Restriction:** No existing structure owned by the acting faction in the target district.
- **Primary cost qty:** 3
- **Primary cost type:** Capacity
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Guild only.
- **Affinity bonus:** Boost([1].[+15 Difficulty])
- **Difficulty:** 50
- **Ring 0 modifier:** −15
- **Ring 1 modifier:** −10
- **Ring 2 modifier:** 0
- **Ring 3 modifier:** +10
- **Resolution:** d100
- **Resolution type:** Probabilistic
- **Outcome type:** N/A

**Effects**

- **Crit success:** +1 presence token in target district.
- **Success:** +1 presence token and +1 structure block in target district.
- **Failure:** No effect.
- **Crit failure:** +1 Guild Intel Token → Ghost. +1 district native → Syndicate.

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | +1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C15 — INFRASTRUCTURE YIELD
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C15
- **Card version:** v1.1
- **Card name:** Infrastructure Yield
- **Tagline:** *Draw resources from infrastructure you have already built.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Guild
- **Pool copies:** 2

**Taxonomy**

- **Layer:** Economy
- **Function:** Add
- **Subject:** Native resource

- **Design note:** Zero cost — Established presence is the only gate. Grid Tap (sacrifice presence for 2 native resource) tabled as political act or operative ability — flag for §10 and Artifact 05.
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *The Guild built New Meridian's infrastructure. Drawing from it is not theft. It is dividend.*
- **Faction perspectives:**
  - Guild: *We built this. Every unit we draw from it was always ours.*
  - Syndicate: *The Guild built the pipes. They are billing us for the water. We respect the position even if we resent the rate.*
  - Directorate: *Infrastructure built under city contract belongs to New Meridian, not to the builder. We have the original agreements.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** N/A
- **Restriction:** Acting faction must be Established or Dominant in target district.
- **Primary cost qty:** N/A
- **Primary cost type:** N/A
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Guild only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** +1 target district native resource.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | +1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### THE GHOST — C16–C20

### C16 — PATTERN MATCH
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C16
- **Card version:** v1.0
- **Card name:** Pattern Match
- **Tagline:** *Identify a faction's operation and location before they move.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Ghost

**Taxonomy**

- **Layer:** Submission
- **Function:** Copy
- **Subject:** Covert operation (full)

- **Design note:** Prediction resolution — no roll. Success if the named faction's submitted covert operation targets the named faction or the named district — either match sufficient. No match: failure. Beat 3 timing dependency: Pattern Match must resolve before the targeted covert operation in the Resolution Grid. If the targeted operation has already resolved this beat, Pattern Match fails automatically regardless of match.
- **Arbiter context:** If the copied operation cannot legally be executed by Ghost, Pattern Match fizzles — 2 Findings spent, no effect regardless of prediction accuracy.

**Narrative**

- **Narrative anchor:** *Ghost does not guess. Ghost identifies what is already in motion.*
- **Faction perspectives:**
  - Ghost: *We are not predicting. We are recognising a pattern we have already seen.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** Named opponent faction
- **Target object:** Covert operation
- **Restriction:** N/A
- **Primary cost qty:** 2
- **Primary cost type:** Findings
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Ghost only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Prediction
- **Resolution type:** Predictive
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Pattern Match resolves as full copy of the matching covert operation.
- **Failure:** No effect.
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | +1 | Success | +1 | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C17 — INTERCEPT
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C17
- **Card version:** v1.0
- **Card name:** Intercept
- **Tagline:** *Surveil a faction's covert operations in real time.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Ghost

**Taxonomy**

- **Layer:** Information
- **Function:** Reveal
- **Subject:** Covert operation — named faction

- **Design note:** Replaces C17 Archive Recovery (retired — L78). Intel token cost consumed at submission regardless of roll outcome — not refunded on failure.
- **Arbiter context:** On crit success: place 1 Intel Token naming target faction in acting faction's dispatch case. On success: write target faction's first submitted covert operation type and district on an Intel Delivery Slip; place in acting faction's dispatch case. On failure: place pre-written Notification Slip in target faction's dispatch case (use C05 text). On crit failure: Public Standing shift is silent — record reason internally only.

**Narrative**

- **Narrative anchor:** *To know what they are doing while they are doing it — that is the only intelligence that matters.*
- **Faction perspectives:**
  - Ghost: *We do not wait for the after-action report. We read the operation as it happens.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** N/A
- **Target faction:** Named opponent faction
- **Target object:** Covert operation
- **Restriction:** N/A
- **Primary cost qty:** 1
- **Primary cost type:** Resource [inteltoken, target faction, active]
- **Secondary cost qty:** 2
- **Secondary cost type:** Findings
- **Faction affinity:** Ghost only.
- **Affinity bonus:** Boost([1].[+1 reveal on success])
- **Difficulty:** Average (50)
- **Ring 0 modifier:** −15
- **Ring 1 modifier:** −10
- **Ring 2 modifier:** 0
- **Ring 3 modifier:** +10
- **Resolution:** d100
- **Resolution type:** Probabilistic
- **Outcome type:** N/A

**Effects**

- **Crit success:** +1 target faction Intel Token.
- **Success:** Intel Delivery Slip — operation type and district of target faction's first submitted covert operation this round — placed in acting faction's dispatch case.
- **Failure:** Notification Slip placed in target faction's dispatch case.
- **Crit failure:** −2 Public Standing.

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | +1 | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C18 — DOSSIER BREACH
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C18
- **Card version:** v1.0
- **Card name:** Dossier Breach
- **Tagline:** *Penetrate a faction's operational planning before the round begins.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Ghost

**Taxonomy**

- **Layer:** Information
- **Function:** Reveal
- **Subject:** Card hand contents

- **Design note:** Replaces C18 Identity Blind (retired S51). Fills Information — Reveal — Card hand gap; no other card in the set targets unplayed cards as an object. Distinct from C17 Intercept (which targets a specific submitted operation) — Dossier Breach targets the unplayed planning pool. Ghost Double Case Pass creates natural synergy: Month 1 Breach informs Month 2 and Month 3 Declaration strategy.
- **Arbiter context:** ARBITER privately shows the target faction's current hand of Covert and Political Act cards to the Ghost player. Modifier cards excluded. ARBITER does not confirm or announce to the table whether this card was played. Information is solely between Ghost's player and ARBITER — Ghost may not publicly announce or prove the contents.

**Narrative**

- **Narrative anchor:** *Understanding the operation before it begins. That is the only tactical advantage worth having.*
- **Faction perspectives:**
  - Ghost: *We did not take their cards. We simply read their intentions. They will act on plans we already know.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** N/A
- **Target faction:** Named opponent faction
- **Target object:** Covert and Political Act cards (unplayed hand)
- **Restriction:** N/A
- **Primary cost qty:** 2
- **Primary cost type:** Findings
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Ghost only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Target faction privately reveals their full unplayed hand of Covert and Political Act cards to Ghost.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | +1 | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C19 — DEEP COVER
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C19
- **Card version:** v1.0
- **Card name:** Deep Cover
- **Tagline:** *Permanently remove a prior operation from the accessible record.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Ghost

**Taxonomy**

- **Layer:** Information
- **Function:** Protect (permanent)
- **Subject:** Action attribution

- **Design note:** Permanent attribution protection. Redesign flag resolved S51 — C18 replaced with Dossier Breach (Information — Reveal), making C19 the unique permanent-protection card in Ghost's set.
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *Good cover does not expire at the end of the week.*
- **Faction perspectives:**
  - Ghost: *It did not happen. This is not a lie. It is a permanent correction to an incomplete record.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** N/A
- **Target faction:** Self
- **Target object:** Action attribution
- **Restriction:** Ghost must have a prior operation from a previous round that resolved without attribution.
- **Primary cost qty:** 1
- **Primary cost type:** Findings
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Ghost only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** One named prior-round Ghost operation permanently removed from the accessible record for the remainder of the session.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C20 — MISDIRECTION
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C20
- **Card version:** v1.0
- **Card name:** Misdirection
- **Tagline:** *Plant false intelligence about Ghost in the accessible record.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Ghost

**Taxonomy**

- **Layer:** Information
- **Function:** Add
- **Subject:** Intel token (corrupt content)

- **Design note:** Taxonomy note: Add with corrupt content — falsification is an attribute of content, not a separate function.
- **Arbiter context:** Deliver false Intel token to target faction via case. Token contains false Ghost operation type and false target district for this round. False token is indistinguishable from a genuine Gather result. Any Denounce using it will fail. Ghost may hold self-directed Intel tokens without cap (Artifact 02b §8).

**Narrative**

- **Narrative anchor:** *Ghost has been considering what its opponents think Ghost is doing. It is never quite right.*
- **Faction perspectives:**
  - Ghost: *We have thought carefully about what they expect. We have given them exactly that.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** N/A
- **Target faction:** Named opponent faction
- **Target object:** N/A
- **Restriction:** Ghost must hold at least 1 Intel token naming Ghost (self-directed).
- **Primary cost qty:** 1
- **Primary cost type:** Findings
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Ghost only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Target faction receives false Intel token — false Ghost operation type and false target district for this round.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | +1 | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### THE DIRECTORATE — C21–C25

*S51: C25 Sealed Border replaced with Tactical Redirection (Territory — Move — Presence token). Block duplication resolved. Mandate generation gap and Public Standing Shift candidate remain open — see D-04-03 PM05.*

### C21 — INVOKE JURISDICTION
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C21
- **Card version:** v1.0
- **Card name:** Invoke Jurisdiction
- **Tagline:** *Assert institutional authority over a target district.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Directorate

**Taxonomy**

- **Layer:** Submission
- **Function:** Block
- **Subject:** Covert operation (C01, C03)

- **Design note:** N/A
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *The Directorate was here before the other factions arrived. Their jurisdictional authority is not theoretical.*
- **Faction perspectives:**
  - Directorate: *This district is under institutional oversight. Expansion requires authorisation. Authorisation has not been granted.*

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** Covert operation
- **Restriction:** None.
- **Primary cost qty:** 2
- **Primary cost type:** Mandate
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Directorate only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** No faction may submit Build Structure (C01) or Campaign (C03) targeting the named district this round. Source is public.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | +1 | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C22 — DETAIN
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C22
- **Card version:** v1.0
- **Card name:** Detain
- **Tagline:** *Permanently remove a faction's deployment marker from a district.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Directorate

**Taxonomy**

- **Layer:** Territory
- **Function:** Remove (permanent)
- **Subject:** Deployment marker

- **Design note:** Permanent per Principle 11. Prior version returned marker at end of next round — revised.
- **Arbiter context:** Intel token requirement means Directorate must have gathered intelligence on target faction this or last round.

**Narrative**

- **Narrative anchor:** *The Directorate does not destroy — it removes from play. Sometimes that is enough.*
- **Faction perspectives:**
  - Directorate: *The marker has been detained. Its conversion will not occur.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** Named opponent faction
- **Target object:** Deployment marker
- **Restriction:** Target faction must have a deployment marker in the target district. Fresh Intel token naming the target faction required (age 0–1 rounds). Cannot target the Chorus Node deployment marker.
- **Primary cost qty:** 3
- **Primary cost type:** Mandate
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Directorate only.
- **Affinity bonus:** N/A
- **Difficulty:** Average (50) + ring modifier
- **Ring 0 modifier:** −15
- **Ring 1 modifier:** −10
- **Ring 2 modifier:** 0
- **Ring 3 modifier:** +10
- **Resolution:** d100
- **Resolution type:** Probabilistic
- **Outcome type:** N/A

**Effects**

- **Crit success:** Return primary cost to dispatch case.
- **Success:** Target faction's deployment marker in the named district is permanently removed for the remainder of the session. Target notified in case.
- **Failure:** No effect.
- **Crit failure:** −1 Public Standing.

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | +1 | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C23 — EVIDENCE PRESERVATION
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C23
- **Card version:** v1.0
- **Card name:** Evidence Preservation
- **Tagline:** *Lock a written record against modification for the remainder of the session.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Directorate

**Taxonomy**

- **Layer:** Information
- **Function:** Protect (permanent)
- **Subject:** Written record

- **Design note:** N/A
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *The Directorate's institutional advantage is the record. They protect it.*
- **Faction perspectives:**
  - Directorate: *The record is preserved. Its integrity is now institutional fact.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** N/A
- **Target faction:** N/A
- **Target object:** Written record
- **Restriction:** Target must be a physically written or recorded game element. Cannot target printed card text.
- **Primary cost qty:** 2
- **Primary cost type:** Mandate
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Directorate only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Named record element is locked for the remainder of the session. Cannot be modified by any card effect.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | +1 | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C24 — SURVEILLANCE PLACEMENT
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C24
- **Card version:** v1.0
- **Card name:** Surveillance Placement
- **Tagline:** *Install permanent monitoring in a target district.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Directorate

**Taxonomy**

- **Layer:** Economy
- **Function:** Add (permanent)
- **Subject:** Intel token

- **Design note:** Permanent per Principle 11. Prior version monitored for 2 rounds — revised. Operation type only, not faction — creates intelligence chain requiring follow-up Gather to identify actors.
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *The Directorate monitors because monitoring is their primary tool for managing what they cannot directly control.*
- **Faction perspectives:**
  - Directorate: *The installation is in place. Everything that happens in that district now happens with our awareness.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** N/A
- **Restriction:** None.
- **Primary cost qty:** 2
- **Primary cost type:** Mandate
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Directorate only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** For the remainder of the session, ARBITER privately notifies The Directorate of any covert operation submitted targeting the named district — operation type only, not faction. Delivered in case at Beat 3 before operations resolve.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | +1 | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C25 — TACTICAL REDIRECTION
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C25
- **Card version:** v1.0
- **Card name:** Tactical Redirection
- **Tagline:** *Reposition institutional presence ahead of a contested exchange.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Directorate

**Taxonomy**

- **Layer:** Territory
- **Function:** Move
- **Subject:** Presence token

- **Design note:** Replaces C25 Sealed Border (retired S51). Fills Territory — Move — Presence token gap; no other card in the full set uses this verb + subject combination. Sealed Border blocked presence placement (Submission — Block); Tactical Redirection creates board-state positioning options instead. Most impactful before Battlefield Strength when district control margins are tight.
- **Arbiter context:** ARBITER moves the named Directorate presence tokens from source to destination. Adjacency confirmed against district adjacency table. Entry requirements rechecked at destination — if Directorate does not qualify for entry, card is discarded without effect (resources not refunded). Control flags and Established markers recalculated after move.

**Narrative**

- **Narrative anchor:** *Institutional authority is not static. The Directorate repositions before others recognize the shift.*
- **Faction perspectives:**
  - Directorate: *Our presence is where it needs to be. This was always the plan. The redistribution was anticipated.*

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target district:** Named adjacent destination district
- **Target faction:** Self
- **Target object:** Presence token (Directorate)
- **Restriction:** Source and destination must be adjacent. Directorate must have at least 1 presence token in source district. Cannot move from or to the Chorus Node.
- **Primary cost qty:** 2
- **Primary cost type:** Mandate
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Directorate only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Move up to 2 Directorate presence tokens from named source district to named adjacent destination district.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | +1 | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### THE NETWORK — C26–C30

*S51: C27 Source Protection replaced with Disclosure Loop (Economy — Add — Exposure). Doctrinal misalignment resolved; Exposure generation gap addressed. C26/C28 Reveal overlap remains under review. Public Standing Shift covert card still needed — see D-04-04 PM05.*

### C26 — LEAK
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C26
- **Card version:** v1.0
- **Card name:** Leak
- **Tagline:** *Make one resolved operation's target district public after resolution.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Network

**Taxonomy**

- **Layer:** Information
- **Function:** Reveal
- **Subject:** Action attribution

- **Design note:** N/A
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *The Network does not need to know everything — only enough to make the right question public.*
- **Faction perspectives:**
  - Network: *We do not reveal everything. We reveal the piece that makes everything else visible.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** N/A
- **Target faction:** Named opponent faction
- **Target object:** Action attribution
- **Restriction:** None.
- **Primary cost qty:** 1
- **Primary cost type:** Exposure
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Network only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** After Beat 3 resolution, ARBITER publicly announces the target district of the highest-impact resolved covert operation from the named faction this round. Operation type not revealed — district only.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | +1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C27 — DISCLOSURE LOOP
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C27
- **Card version:** v1.0
- **Card name:** Disclosure Loop
- **Tagline:** *Transparency is self-sustaining. Revealing information generates the capacity to reveal more.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Network

**Taxonomy**

- **Layer:** Economy
- **Function:** Add
- **Subject:** Exposure (conditional)

- **Design note:** Replaces C27 Source Protection (retired S51). Source Protection was doctrinally misaligned — protecting attribution is Ghost's register, not Network's. Disclosure Loop creates a positive resource feedback loop consistent with Network doctrine. Pairs with C26 Leak and C28 Open Channel — a Network round built around Reveal operations becomes self-sustaining on Exposure.
- **Arbiter context:** At Beat 3 cleanup, check whether any Network Reveal card resolved successfully this round. If yes, deliver 1 Exposure to Network's resource pool. If no Reveal resolved, card takes effect but produces nothing — the slot cost was the investment.

**Narrative**

- **Narrative anchor:** *The act of disclosure is not only a tactic. It is a resource. The Network learned this before anyone else at this table.*
- **Faction perspectives:**
  - Network: *We revealed something. Now we can reveal something more. The loop is already running.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** Network resolves at least 1 Reveal card this round
- **Target district:** N/A
- **Target faction:** Self
- **Target object:** N/A
- **Restriction:** N/A
- **Primary cost qty:** 1
- **Primary cost type:** Findings
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Network only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Gain 1 Exposure at cleanup if any Network Reveal card resolved successfully this round. No effect if no Reveal resolved.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C28 — OPEN CHANNEL
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C28
- **Card version:** v1.0
- **Card name:** Open Channel
- **Tagline:** *Force private ARBITER notifications to a faction to be delivered publicly.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Network

**Taxonomy**

- **Layer:** Information
- **Function:** Reveal
- **Subject:** Private communications

- **Design note:** Flagged for review — C26 and C28 both Reveal, same function different scope. See D-04-04.
- **Arbiter context:** Does not intercept Hidden Objective or Classified Directive communications. Beat 2 — must be active before Beat 3 notifications are generated.

**Narrative**

- **Narrative anchor:** *Secret communications between powerful institutions are themselves a form of harm. Opening the channel is the argument.*
- **Faction perspectives:**
  - Network: *If it happened, it should be known. We are simply making that principle operational.*

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target district:** N/A
- **Target faction:** Named opponent faction
- **Target object:** Private communications
- **Restriction:** None.
- **Primary cost qty:** 2
- **Primary cost type:** Exposure
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Network only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Any private notification ARBITER would send to the named faction this round is instead delivered publicly to the whole table.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | +1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C29 — NETWORK CASCADE
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C29
- **Card version:** v1.0
- **Card name:** Network Cascade
- **Tagline:** *Extend Broadcast Interference to an adjacent district.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Network

**Taxonomy**

- **Layer:** Submission
- **Function:** Modify
- **Subject:** Political act (scope)

- **Design note:** N/A
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *The Network understands signal propagation better than anyone at this table.*
- **Faction perspectives:**
  - Network: *The signal does not stop at district borders. Neither do we.*

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target district:** Any district adjacent to the Network's Broadcast Interference target this round
- **Target faction:** N/A
- **Target object:** Political act
- **Restriction:** Network must also submit C06 Broadcast Interference this round. Adjacent district named at submission.
- **Primary cost qty:** 2
- **Primary cost type:** Exposure
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Network only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Adjacent district also has political act costs +1 this round.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | +1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### C30 — COMMUNITY ANCHOR
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C30
- **Card version:** v1.0
- **Card name:** Community Anchor
- **Tagline:** *Establish presence in a Baryo district through existing relationships.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Network

**Taxonomy**

- **Layer:** Territory
- **Function:** Add
- **Subject:** Presence token

- **Design note:** N/A
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *The Network did not arrive in New Meridian through official channels. They arrived through people.*
- **Faction perspectives:**
  - Network: *We already have contacts there. This is formalising what already exists.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any Baryo district
- **Target faction:** N/A
- **Target object:** N/A
- **Restriction:** Network must have zero presence in the target district. Baryo districts only.
- **Primary cost qty:** 1
- **Primary cost type:** Exposure
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Network only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Place 1 presence token in the target Baryo district.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | +1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A | N/A |

---

### THE SYNDICATE — C31–C35

*Current cards carried forward. Taxonomy gap analysis in Artifact 04b §8.4 identifies redesign targets: zero information/intelligence capability; Cross-Category — Corrupt Accord unused; Resource — Redirect Accord ("small print") unused.*

### C31 — LEVERAGED ACQUISITION
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C31
- **Card version:** v1.0
- **Card name:** Leveraged Acquisition
- **Tagline:** *Gain resource generation from a district without presence.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Syndicate

**Taxonomy**

- **Layer:** Economy
- **Function:** Add
- **Subject:** Native resource

- **Design note:** N/A
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *The Syndicate does not need to be somewhere to profit from it. Ownership and presence are different things.*
- **Faction perspectives:**
  - Syndicate: *We own the revenue stream. Whether we are physically present is irrelevant.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** N/A
- **Restriction:** Maximum one district per round.
- **Primary cost qty:** 4
- **Primary cost type:** Capital
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Syndicate only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Gain 1 unit of the target district's native resource this Upkeep as though Established — delivered in case.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | +1 | N/A | N/A | N/A |

---

### C32 — SHORT THE MARKET
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C32
- **Card version:** v1.0
- **Card name:** Short the Market
- **Tagline:** *Reduce a faction's native resource generation for one round.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Syndicate

**Taxonomy**

- **Layer:** Economy
- **Function:** Remove
- **Subject:** Native resource

- **Design note:** N/A
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *Capital can suppress as easily as it can produce.*
- **Faction perspectives:**
  - Syndicate: *We are not destroying their capacity. We are adjusting market conditions temporarily.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** N/A
- **Target faction:** Named opponent faction
- **Target object:** Native resource
- **Restriction:** Fresh Intel token naming the target faction required (age 0–1 rounds).
- **Primary cost qty:** 2
- **Primary cost type:** Capital
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Syndicate only.
- **Affinity bonus:** N/A
- **Difficulty:** Average (50) + ring modifier
- **Ring 0 modifier:** −15
- **Ring 1 modifier:** −10
- **Ring 2 modifier:** 0
- **Ring 3 modifier:** +10
- **Resolution:** d100
- **Resolution type:** Probabilistic
- **Outcome type:** N/A

**Effects**

- **Crit success:** Target faction generates 2 fewer units this Upkeep (minimum 0).
- **Success:** Target faction generates 1 fewer unit of their native resource during Upkeep this round (minimum 0). Applied silently.
- **Failure:** No effect.
- **Crit failure:** −1 Public Standing.

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | +1 | N/A | N/A | N/A |

---

### C33 — HOSTILE ACQUISITION
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C33
- **Card version:** v1.0
- **Card name:** Hostile Acquisition
- **Tagline:** *Purchase ownership of an opponent's structure.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Syndicate

**Taxonomy**

- **Layer:** Territory
- **Function:** Redirect
- **Subject:** Structure block

- **Design note:** N/A
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *Everything in New Meridian has a price. The Syndicate is the only faction honest about this.*
- **Faction perspectives:**
  - Syndicate: *We made a fair offer. The market determined the value. We accepted the market's judgment.*

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** Named opponent faction
- **Target object:** Structure block
- **Restriction:** Target faction must have a structure in the target district. Cannot target a Guild structure protected by Fortify Structure (C11) this round.
- **Primary cost qty:** 5
- **Primary cost type:** Capital
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Syndicate only.
- **Affinity bonus:** N/A
- **Difficulty:** Average (50) + ring modifier
- **Ring 0 modifier:** −15
- **Ring 1 modifier:** −10
- **Ring 2 modifier:** 0
- **Ring 3 modifier:** +10
- **Resolution:** d100
- **Resolution type:** Probabilistic
- **Outcome type:** N/A

**Effects**

- **Crit success:** Return 1 Capital to dispatch case.
- **Success:** Claim one named opponent structure. Block flips to Syndicate color. Prior owner receives 1 unit of their native resource as consideration — delivered in case.
- **Failure:** No effect.
- **Crit failure:** −1 Public Standing.

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | +1 | N/A | N/A | N/A |

---

### C34 — GOLDEN PARACHUTE
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C34
- **Card version:** v1.0
- **Card name:** Golden Parachute
- **Tagline:** *Transfer resources before a forced resource-loss event.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Syndicate

**Taxonomy**

- **Layer:** Economy
- **Function:** Protect
- **Subject:** Native resource

- **Design note:** N/A
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *The Syndicate plans for outcomes not yet confirmed. They move assets before the decision is made.*
- **Faction perspectives:**
  - Syndicate: *We did not lose those resources. We repositioned them. There is a difference.*

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target district:** N/A
- **Target faction:** Named opponent faction
- **Target object:** Native resource
- **Restriction:** Must be submitted in the same round as an anticipated resource-loss event. Must be submitted before Beat 3. Cannot be reclaimed after transfer.
- **Primary cost qty:** N/A
- **Primary cost type:** N/A
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Syndicate only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Transfer up to 3 Capital to named faction. Recorded by ARBITER but not announced. Transferred Capital exits Syndicate's pool before any resource-loss calculation applies this round.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | +1 | N/A | N/A | N/A |

---

### C35 — REGULATORY CAPTURE
[↑ Card Specifications](#user-content-card-specifications)

**Identity**

- **Card ID:** C35
- **Card version:** v1.0
- **Card name:** Regulatory Capture
- **Tagline:** *Block a specific action type in a named district for one round.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Syndicate

**Taxonomy**

- **Layer:** Submission
- **Function:** Block
- **Subject:** Named action type

- **Design note:** N/A
- **Arbiter context:** N/A

**Narrative**

- **Narrative anchor:** *If you own enough of the regulatory structure, you define what is permitted. The Syndicate does not see this as corruption. They see it as governance.*
- **Faction perspectives:**
  - Syndicate: *The regulatory framework exists. We simply ensure it reflects current market conditions.*

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target district:** Any district
- **Target faction:** N/A
- **Target object:** Named action type
- **Restriction:** Cannot apply to the Chorus Node.
- **Primary cost qty:** 3
- **Primary cost type:** Capital
- **Secondary cost qty:** N/A
- **Secondary cost type:** N/A
- **Faction affinity:** Syndicate only.
- **Affinity bonus:** N/A
- **Difficulty:** N/A
- **Ring 0 modifier:** N/A
- **Ring 1 modifier:** N/A
- **Ring 2 modifier:** N/A
- **Ring 3 modifier:** N/A
- **Resolution:** Automatic
- **Resolution type:** Transactional
- **Outcome type:** N/A

**Effects**

- **Crit success:** N/A
- **Success:** Named district and action type: no faction may submit that type targeting that district this round. Source is public.
- **Failure:** N/A
- **Crit failure:** N/A

**Portrait**

| Faction | Flat | Submitter | Condition | Modifier | Mod Condition |
|---------|------|-----------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A | N/A |
| Syndicate | N/A | +1 | −2 | Blocking Guild construction | N/A |

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
