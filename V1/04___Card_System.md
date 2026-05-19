# 04 — CARD SYSTEM
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.9.8 Draft  
**Status:** 🔄 Draft — Pending Sign-Off  
**Last Updated:** 2026-05-19  
**Supersedes:** v0.9.5, action_redesign (retired artifact)  
**Companion document:** 04b — Action Taxonomy & Design Analysis

---

## 1. Overview

Artifact 04 defines the design of every card type faction players hold or play during the paper prototype session. It covers:

- Standard covert operations available to all factions
- Faction-specific covert operations per faction
- Standard political acts available to all factions
- Faction-specific political acts per faction
- The Pass card — one card type, four cards per faction, usable in both covert and political contexts
- Countermeasure cards — faction-held defensive declarations, played in Phase 5 (Type A: District Block; Type B: Faction Defense)
- Modifier cards: faction-specific deck (player tableau) and ring-specific decks (game board)
- Modifier card draw rules, hand accumulation, submit limits, burst play, and trading
- Intel token use in Denounce and covert operations
- Emergency Response cards (one per faction, used during Apex trigger)
- Card information design requirements

**Pending decision (D-04-01):** The current card set (10 standard covert, 5 faction-specific covert per faction, 8 standard political, 2 faction-specific political per faction) is a working baseline. Taxonomy gap analysis (Artifact 04b §6) has identified meaningful unused design space. Whether additional cards are needed before production is an open decision. The setup pool sizes (30 covert pool / select 24; 20 political pool / select 12) are assumptions pending validation against the final card set.

This artifact does not define operative abilities (Artifact 05), the dispatch case protocol (Artifact 06), ARBITER resolution beats (Artifact 07), card production specifications (Artifact 09 — Card Production Spec), or session setup procedures (Artifact 08 — Player Toolkit).

**Action taxonomy** — the full taxonomy table, card category/function/target assignments, coverage gap analysis, and faction design recommendations — is in Artifact 04b. This artifact references 04b for taxonomy context but does not reproduce it. Each card carries a Taxonomy field (Category — Function — Target) as a data element.

**Scope note:** L1 Paper Prototype only. Layer references (L2–L4) do not apply. Future layer mechanics tracked in PM03.

---

## 2. Index

| Section | Content |
|---------|---------|
| §3 | Game Purpose |
| §4 | Narrative Function |
| §5 | Design Principles |
| §6 | Card Data Structure |
| §7 | Standard Covert Operations C01–C10 |
| §8 | Faction-Specific Covert Operations C11–C35 |
| §9 | Standard Political Acts P01–P08 |
| §10 | Faction-Specific Political Acts P09–P18 |
| §11 | Rules & Constraints — Modifier Cards |
| §12 | Rules & Constraints — Pass Cards |
| §13 | Card Information Design Requirements |
| §14 | Special Conditions & Gameplay Impacts |
| §15 | Examples & Exceptions |
| §16 | Appendix — Outstanding Decisions & Assumptions |

---

## 3. Game Purpose

The action card system provides the mechanism by which factions commit to decisions simultaneously and in secret. Cards are not menus — they are physical commitments. Placing a covert operation card into a dispatch case is an irreversible act. Laying a political act card face-up on the table is a declaration that cannot be retracted.

The physical card format serves four design functions:

1. **Simultaneous commitment:** All players decide before outcomes are known.
2. **Hidden information:** Covert operation cards are secret until ARBITER opens the dispatch case.
3. **Asymmetric options:** Faction-specific cards give each faction a decision space that reflects its doctrine.
4. **Self-contained resolution:** Each card carries the information needed for ARBITER or the acting player to resolve its effect without a rules lookup.

---

## 4. Narrative Function

Every card is a decision made under incomplete information by people who believe the stakes are existential.

A covert operation in the dispatch case represents operatives committed, resources allocated, and a plan set in motion before anyone knows what anyone else has planned. A political act is a public stance taken in front of The Table: a claim that can be supported, refuted, or turned against the faction that made it.

The fiction is not window dressing. A Denounce costs the target faction's native resource because accusations in New Meridian are drawn from the domain where a faction is most powerful. A Broadcast operation raises difficulty because people under observation behave differently. The mechanics are the story.

All card names, action text, and effect descriptions are written in the language of New Meridian and the factions that operate within it. The word on the card is the in-world term for what is happening. Players are not managing tokens — they are making decisions on behalf of people in a city who believe the future of human contact with the unknown depends on what happens at this table.

---

## 5. Design Principles

**Principle 1 — Cards are not equivalent.**

Each faction-specific card is designed around what that faction uniquely can do in New Meridian.

**Principle 2 — Public and covert actions create different risks.**

Covert operations are secret until resolved. Political acts are locked the moment they are declared but visible to all.

**Principle 3 — Ghost is different.**

Ghost's set is larger (10 standard + 5 Ghost-specific). Intelligence operations are not a path to the same goal as everyone else — they are the goal.

**Principle 4 — All resource costs must be physically present.**

No deferred payments. Resources in the dispatch case before sealing; resources paid to the Reservoir at political act declaration.

**Principle 5 — Narrative consistency with Artifact 00.**

All card text must be consistent with the world, factions, and doctrines in Artifact 00. The mechanics and the fiction are the same thing written differently.

**Principle 6 — Cards are self-contained.**

Every card carries sufficient information to resolve its effect without consulting the rulebook.

**Principle 7 — Doctrinal Traceability.**

Every faction-specific card must pass two tests: **mechanical** (only this faction would do this — the effect is impossible for another faction's doctrine to justify) and **narrative** (only this faction would say it this way — the card text sounds like no other faction). If either test fails, the card belongs to no one. The doctrinal anchor must be traceable to Artifact 00 §7 (faction profiles and doctrine). A card is wrong if it could plausibly belong to a different faction. *Source: 00a R29.*

**Principle 8 — Standard cards have an in-world narrative anchor.**

Standard cards are grounded in actions that any capable organization in New Meridian might plausibly take.

**Principle 9 — Ring-specific modifier cards reflect geography.**

A ring modifier is wrong if its narrative could apply equally to any ring.

**Principle 10 — Portrait reflects doctrinal alignment.**

Portrait is impacted when an action strongly aligns with or against faction doctrine. Grey areas produce no Portrait effect. Faction perspectives explain Portrait values.

**Principle 11 — No persistent temporary effects across rounds.**

All card effects are either immediate (this round only) or permanent (rest of session). Only World Condition effects carry over round to round.

**Principle 12 — Standard actions cost less on average than standard political actions.**

Covert operations are operational work. Political acts are public commitments with broader consequences.

**Principle 13 — Faction-specific actions emphasize faction strengths.**

Faction-specific cards may have a secondary non-faction resource cost but their primary effect reflects what that faction uniquely can do.

---

## 6. Card Data Structure

Every card uses this data structure. All fields are required. N/A is a valid value.

*For the action taxonomy definitions (Category, Function, Target values) see Artifact 04b §4.*

*VS-xx Visibility Scope — values used in this table (full definitions: Artifact 00b §5.9):*
- *VS-01 — Public: visible to all players at all times.*
- *VS-04 — ARBITER-Only: visible to the ARBITER player only. Not revealed at resolution.*
- *VS-06 — Conditional: hidden until the card resolves; revealed to all players at resolution.*

*§6 schema informed by a card game data structure gap analysis conducted sessions 23–24. Research notes (non-artifact): `Projects/Whiteboard/researchNotes_CardDesign.md`. Sources: MTG/Scryfall API, Netrunner DB (NRDB), Arkham Horror LCG (Fantasy Flight), Marvel Champions (Fantasy Flight). Fields added as a result: Card version (§1.1), Trigger condition (§1.2), Pool copies (§1.3), Outcome type (§1.5). Fields reviewed and not added: §8.*

| Category | Field | Purpose | Constraints | VS-xx | Notes / Description |
|----------|-------|---------|-------------|-------|---------------------|
| Identity | **Card ID** | Primary key | Format: [type prefix][sequence number] | VS-01 | — |
| Identity | **Card version** | Per-card revision identifier | Format: v[major].[minor] (e.g., v1.0) | VS-01 | Printed on card face. Enables playtest copy identification. Independent of Artifact 04 version. |
| Identity | **Card name** | In-world card name | Not a mechanical label | VS-01 | — |
| Identity | **Tagline** | One-line in-world description | One sentence | VS-01 | Printed on card face |
| Identity | **Card type** | Top-level card category | Controlled vocabulary: Covert Operation, Political Act, Pass, Countermeasure, Modifier, Emergency Response | VS-01 | — |
| Identity | **Card subtype** | Distribution scope | Controlled vocabulary: Standard, Faction-specific | VS-01 | — |
| Identity | **Card faction** | Owning faction | All if available to all factions | VS-01 | — |
| Identity | **Pool copies** | Copies in faction's setup pool | Integer | VS-01 | Standard cards: 2 per faction. Emergency Response: 1 (Singleton). Governs print quantities. |
| Mechanics | **Beat** | Resolution beat | Numeric | VS-01 | The beat in Phase 6 in which this card is processed. Resolution order within a Beat: governed by dispatch case submission order per Art 03 §7. |
| Mechanics | **Trigger condition** | Activation condition for non-default timing | Controlled vocabulary: N/A, Submission-time, Beat-N, Phase-N, Condition-based | VS-01 | N/A for cards resolving at their default Beat. Required for React-function cards and Countermeasures. |
| Mechanics | **Target** | Valid submission targets | Broadest valid statement | VS-01 | Stated on card face |
| Mechanics | **Restriction** | Submission preconditions | All stated on card. No external references | VS-01 | — |
| Mechanics | **Primary cost** | Main cost to submit the card | — | VS-01 | — |
| Mechanics | **Secondary cost** | Additional cost beyond primary | N/A if not applicable | VS-01 | Often a district native resource; often waivable by affinity |
| Mechanics | **Faction affinity** | Faction receiving affinity discount | N/A if not applicable | VS-01 | — |
| Mechanics | **Affinity bonus** | What the affinity discount provides | N/A if Faction affinity is N/A | VS-01 | — |
| Mechanics | **Difficulty** | Base difficulty threshold | Controlled vocabulary: Easy, Average, Challenging, or N/A. Include ring modifier where applicable | VS-01 | N/A if no roll required. Thresholds defined in Artifact 03 §13 |
| Mechanics | **Resolution** | How this card resolves | Non-roll cards must state mechanism explicitly | VS-01 | Standard: d100 roll vs. Difficulty Threshold per Artifact 03 §13 |
| Mechanics | **Outcome type** | Political act resolution process type | Controlled vocabulary: Binary (For/Against), Elect player, Elect district, Elect faction, Bilateral agreement, Unilateral, N/A | VS-01 | N/A for all non-Political Act card types. Determines ARBITER's outcome-collection process at resolution. Required for L2+ enforcement. |
| Effects | **Effect on crit success** | Critical success outcome | N/A if no roll | VS-06 | Additional effects beyond success |
| Effects | **Effect on success** | Primary card effect | Full effect stated on card | VS-06 | — |
| Effects | **Effect on failure** | Failure outcome | N/A if no roll | VS-06 | — |
| Effects | **Effect on crit failure** | Critical failure outcome | N/A if no roll | VS-06 | Additional effects beyond failure |
| Portrait | **Portrait — Guild** | Guild base Portrait effect | N/A if no effect | VS-04 | +/− numeric value. Coded symbol on card face — physically visible to all players, interpreted by ARBITER only. |
| Portrait | **Portrait — Guild Condition** | Restriction on Guild base | N/A if unconditional | VS-01 | — |
| Portrait | **Portrait — Guild Modifier** | Adjustment to Guild Portrait under specific circumstances | N/A if none | VS-04 | +/− numeric value. Coded symbol on card face — physically visible to all players, interpreted by ARBITER only. |
| Portrait | **Portrait — Guild Modifier Condition** | When Guild Modifier applies | N/A if Modifier is N/A | VS-01 | — |
| Portrait | **Portrait — Directorate** | Directorate base Portrait effect | N/A if no effect | VS-04 | +/− numeric value. Coded symbol on card face — physically visible to all players, interpreted by ARBITER only. |
| Portrait | **Portrait — Directorate Condition** | Restriction on Directorate base | N/A if unconditional | VS-01 | — |
| Portrait | **Portrait — Directorate Modifier** | Adjustment to Directorate Portrait under specific circumstances | N/A if none | VS-04 | +/− numeric value. Coded symbol on card face — physically visible to all players, interpreted by ARBITER only. |
| Portrait | **Portrait — Directorate Modifier Condition** | When Directorate Modifier applies | N/A if Modifier is N/A | VS-01 | — |
| Portrait | **Portrait — Network** | Network base Portrait effect | N/A if no effect | VS-04 | +/− numeric value. Coded symbol on card face — physically visible to all players, interpreted by ARBITER only. |
| Portrait | **Portrait — Network Condition** | Restriction on Network base | N/A if unconditional | VS-01 | — |
| Portrait | **Portrait — Network Modifier** | Adjustment to Network Portrait under specific circumstances | N/A if none | VS-04 | +/− numeric value. Coded symbol on card face — physically visible to all players, interpreted by ARBITER only. |
| Portrait | **Portrait — Network Modifier Condition** | When Network Modifier applies | N/A if Modifier is N/A | VS-01 | — |
| Portrait | **Portrait — Ghost** | Ghost base Portrait effect | N/A if no effect | VS-04 | +/− numeric value. Coded symbol on card face — physically visible to all players, interpreted by ARBITER only. |
| Portrait | **Portrait — Ghost Condition** | Restriction on Ghost base | N/A if unconditional | VS-01 | — |
| Portrait | **Portrait — Ghost Modifier** | Adjustment to Ghost Portrait under specific circumstances | N/A if none | VS-04 | +/− numeric value. Coded symbol on card face — physically visible to all players, interpreted by ARBITER only. |
| Portrait | **Portrait — Ghost Modifier Condition** | When Ghost Modifier applies | N/A if Modifier is N/A | VS-01 | — |
| Portrait | **Portrait — Syndicate** | Syndicate base Portrait effect | N/A if no effect | VS-04 | +/− numeric value. Coded symbol on card face — physically visible to all players, interpreted by ARBITER only. |
| Portrait | **Portrait — Syndicate Condition** | Restriction on Syndicate base | N/A if unconditional | VS-01 | — |
| Portrait | **Portrait — Syndicate Modifier** | Adjustment to Syndicate Portrait under specific circumstances | N/A if none | VS-04 | +/− numeric value. Coded symbol on card face — physically visible to all players, interpreted by ARBITER only. |
| Portrait | **Portrait — Syndicate Modifier Condition** | When Syndicate Modifier applies | N/A if Modifier is N/A | VS-01 | — |
| Narrative | **Narrative anchor** | In-world narrative grounding | One sentence | VS-01 | Standard cards: neutral observer. Faction-specific: owning faction's voice |
| Narrative | **Faction perspectives** | Per-faction in-world perspective | Required for factions with Portrait values. One sentence per faction | VS-01 | Optional for others |
| Taxonomy | **Taxonomy — Category** | Action taxonomy — category | Controlled vocabulary: Board, Resource, Action, Cross-Category | VS-01 | See Artifact 04b §4 |
| Taxonomy | **Taxonomy — Function** | Action taxonomy — function | See Artifact 04b §4 | VS-01 | What the card does within its category |
| Taxonomy | **Taxonomy — Target** | Action taxonomy — target | See Artifact 04b §4 | VS-01 | What the card acts on |

> **Design note field:** Prose below the card data block. Not part of the card face. VS-04 (ARBITER-Only). Informs Artifact 11 layout decisions and Artifact 07 ARBITER resolution notes.

---

## 7. Standard Covert Operations — C01–C10

All factions have access to all ten standard covert operations. Each faction's setup pool contains 2 copies of each standard type (20 standard covert cards in pool). Player selects their covert deck of 24 from a combined pool of standard and faction-specific cards.

### C01 — BUILD STRUCTURE

**Identity**

- **Card ID:** C01
- **Card version:** v1.0
- **Card name:** Build Structure
- **Tagline:** *Construct a physical installation in a district.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** Acting faction must have at least 1 presence in the target district. No existing structure owned by the acting faction in the target district.
- **Primary cost:** 1 native resource.
- **Secondary cost:** 1 district native resource.
- **Faction affinity:** Guild.
- **Affinity bonus:** Secondary cost waived.
- **Difficulty:** N/A
- **Resolution:** No roll required. Effect resolves on submission.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** N/A
- **Effect on success:** Place 1 structure block (faction color) in the target district. Generates +1 of the district's native resource during each Upkeep while standing.
- **Effect on failure:** N/A
- **Effect on crit failure:** N/A

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | +1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *Every faction that wants to matter in New Meridian eventually has to build something.*
- **Faction perspectives:**
  - Guild: *This is what we do. Every structure we build is an argument that permanence is possible here.*
  - Directorate: *Infrastructure serves order. We will use it if it serves the mandate.*
  - Network: *Building is a statement of intent. We watch carefully to understand what kind.*
  - Ghost: *A structure is a commitment. Commitments are data points.*
  - Syndicate: *Every structure generates value. The question is who captures it.*

**Taxonomy**

- **Taxonomy — Category:** Board
- **Taxonomy — Function:** Add
- **Taxonomy — Target:** Structure block

> **Design note:** Construction is publicly visible — result announced at resolution. The covert element is the intent. Maximum 1 structure per faction per district — ARBITER rejects submission if acting faction already has a structure in the target district. "At least 1 presence" includes claim markers per Artifact 02a global convention.

---

### C02 — DEMOLISH

**Identity**

- **Card ID:** C02
- **Card version:** v1.0
- **Card name:** Demolish
- **Tagline:** *Remove an opponent's structure from a district.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** Acting faction must have at least 1 presence in the target district or in a district adjacent to the target district. Target faction must have a structure in the target district.
- **Primary cost:** 1 native resource.
- **Secondary cost:** 1 district native resource.
- **Faction affinity:** None.
- **Difficulty:** Average (50%) + ring modifier
- **Resolution:** d100 roll vs. Difficulty Threshold per Artifact 03 §13.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** Return primary cost to dispatch case.
- **Effect on success:** Remove 1 target faction structure from the target district.
- **Effect on failure:** Cost spent. No effect.
- **Effect on crit failure:** −1 Popularity.

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | −1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *Not everything built in New Meridian was meant to last.*
- **Faction perspectives:**
  - Guild: *We build. We do not unmake. Every time we perform this action something has gone badly wrong.*
  - Directorate: *Demolition is a last resort. Structures represent investment in the city we are here to protect.*
  - Network: *Sometimes the infrastructure of control needs to come down before something better can be built.*
  - Ghost: *A demolished structure tells us as much as a standing one. We note the absence.*
  - Syndicate: *Assets change hands. Sometimes the most efficient transfer is removal.*

**Taxonomy**

- **Taxonomy — Category:** Board
- **Taxonomy — Function:** Remove
- **Taxonomy — Target:** Structure block

> **Design note:** Structure removal is publicly visible. Source of removal is not announced. Crit failure detection condition defined in Artifact 03 §6.2. Ring modifier applies to difficulty threshold. Adjacency formal table flagged for Artifact 01 (D-ART01-01).

---

### C03 — CAMPAIGN

**Identity**

- **Card ID:** C03
- **Card version:** v1.0
- **Card name:** Campaign
- **Tagline:** *Build local support and deepen presence in a district.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** Acting faction must have at least 1 presence in the target district.
- **Primary cost:** 1 native resource.
- **Secondary cost:** 1 district native resource.
- **Faction affinity:** Network.
- **Affinity bonus:** Secondary cost waived.
- **Difficulty:** N/A
- **Resolution:** No roll required. Effect resolves on submission.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** N/A
- **Effect on success:** Place 1 additional presence token in the target district.
- **Effect on failure:** N/A
- **Effect on crit failure:** N/A

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | +1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *Presence without roots is just occupation.*
- **Faction perspectives:**
  - Guild: *Presence is the foundation everything else is built on. We are methodical about this.*
  - Directorate: *Authority requires visibility. We establish presence where the mandate requires it.*
  - Network: *Every person we reach in a district is a relationship. Relationships are how things actually change.*
  - Ghost: *Presence creates exposure. We expand only when the intelligence justifies the risk.*
  - Syndicate: *Market position requires footprint. We place ourselves where the returns justify it.*

**Taxonomy**

- **Taxonomy — Category:** Board
- **Taxonomy — Function:** Add
- **Taxonomy — Target:** Presence

> **Design note:** Token placement is publicly visible. C03 mirrors C01 structurally — Build Structure is the Guild's native action, Campaign is the Network's. Maximum 6 presence tokens per faction per district enforced at submission.

---

### C04 — UNDERMINE

**Identity**

- **Card ID:** C04
- **Card version:** v1.0
- **Card name:** Undermine
- **Tagline:** *Erode an opponent's presence in a district.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** Acting faction must have at least 1 presence in the target district or in a district adjacent to the target district. Target faction must have at least 1 presence token in the target district.
- **Primary cost:** 1 native resource.
- **Secondary cost:** 1 district native resource.
- **Faction affinity:** None.
- **Difficulty:** Average (50%) + ring modifier
- **Resolution:** d100 roll vs. Difficulty Threshold per Artifact 03 §13.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** Remove 2 presence tokens from target faction in target district.
- **Effect on success:** Remove 1 presence token from target faction in target district.
- **Effect on failure:** Cost spent. No effect.
- **Effect on crit failure:** −1 Popularity.

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | −1 | N/A | N/A | N/A |
| Directorate | −1 | Except when targeting Network | N/A | N/A |
| Network | +1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *The most effective opposition leaves no visible wound.*
- **Faction perspectives:**
  - Guild: *We do not erase what others have built. Even our enemies.*
  - Directorate: *Covert erosion is not governance. Unless the target is The Network — then it is public safety.*
  - Network: *Entrenched presence does not become legitimate just because it has been there long enough.*
  - Ghost: *Disruption without intelligence purpose is noise. We prefer signal.*
  - Syndicate: *If their presence can be eroded, it was never well-positioned to begin with.*

**Taxonomy**

- **Taxonomy — Category:** Board
- **Taxonomy — Function:** Remove
- **Taxonomy — Target:** Presence

> **Design note:** Source not announced. Target faction sees tokens removed but not by whom. Crit failure detection condition defined in Artifact 03 §6.2. Ring modifier applies. Portrait values reflect doctrinal alignment — Ghost and Syndicate omitted, neither strongly aligned nor opposed.

---

### C05 — GATHER

**Identity**

- **Card ID:** C05
- **Card version:** v1.0
- **Card name:** Gather
- **Tagline:** *Extract actionable intelligence about a specific faction's operations.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** Acting faction must have at least 1 presence in the target district or in a district adjacent to the target district. Ghost is exempt from this restriction.
- **Primary cost:** 1 native resource.
- **Secondary cost:** None.
- **Faction affinity:** Ghost.
- **Affinity bonus:** Difficulty is Easy (75%) + ring modifier.
- **Difficulty:** Average (50%) + ring modifier
- **Resolution:** d100 roll vs. Difficulty Threshold per Artifact 03 §13.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** ARBITER delivers 2 Intel tokens for the named faction in case.
- **Effect on success:** ARBITER delivers 1 Intel token for the named faction in case. Token marked: faction name + round number.
- **Effect on failure:** Cost spent. No effect.
- **Effect on crit failure:** ARBITER delivers pre-written notification slip to target faction in case.

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A |
| Ghost | +1 | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *In New Meridian, knowing is the first form of power.*
- **Faction perspectives:**
  - Guild: *Intelligence informs construction. We gather when we need to build smarter.*
  - Directorate: *Information is the foundation of legitimate authority. We collect it formally.*
  - Network: *The city speaks constantly. We listen for the gaps between what is said and what is true.*
  - Ghost: *This is what we are here for. Everything else follows from understanding.*
  - Syndicate: *Information has market value. We acquire it when the return justifies the cost.*

**Taxonomy**

- **Taxonomy — Category:** Resource
- **Taxonomy — Function:** Add
- **Taxonomy — Target:** Intel token

> **Design note:** No secondary cost — observation does not consume local resources. Ghost exemption from adjacency reflects doctrine: remote analysis does not require physical proximity. Ghost affinity is Easy + ring modifier — ring penalties still apply. Crit failure notification slip is a pre-written ARBITER component (A-04-05 — feasibility pending Artifact 07 confirmation). Slip text draft: *"An unknown party attempted to access sensitive information about your operations in [district]. The attempt was identified and neutralised. Exercise appropriate caution."* Intel token mechanics in Artifact 02b §8–9 (cross-reference audit pending — D-04-11). "Delivered in case" is standard language for all privately delivered effects.

---

### C06 — BROADCAST INTERFERENCE

**Identity**

- **Card ID:** C06
- **Card version:** v1.0
- **Card name:** Broadcast Interference
- **Tagline:** *Disrupt public communications in a district, dampening political activity.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** None.
- **Primary cost:** 2 Exposure.
- **Secondary cost:** None.
- **Faction affinity:** Network.
- **Affinity bonus:** Primary cost reduced to 1 Exposure.
- **Difficulty:** N/A
- **Resolution:** No roll required. Effect resolves on submission.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** N/A
- **Effect on success:** Political acts declared against the target district this round cost +1 additional native resource.
- **Effect on failure:** N/A
- **Effect on crit failure:** N/A

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | +1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *People don't act naturally when they know they're being watched.*
- **Faction perspectives:**
  - Guild: *Disrupting communications delays approvals, permits, agreements. We feel this more than most.*
  - Directorate: *Interference with public communications is a jurisdictional matter. We note who is responsible.*
  - Network: *Noise is a tool. Sometimes silence is louder than anything we could broadcast.*
  - Ghost: *Interference creates analytical cover. We appreciate the quiet.*
  - Syndicate: *Disrupted communications create market inefficiencies. Those can be profitable.*

**Taxonomy**

- **Taxonomy — Category:** Action
- **Taxonomy — Function:** Modify
- **Taxonomy — Target:** Political act (cost)

> **Design note:** Exposure is The Network's native resource. Non-Network factions acquire Exposure through district incursion or trade at 4:1. No presence requirement — signal disruption is broadcast. Source not announced. Beat 2 — ARBITER retains awareness after case opening. At Beat 4 declaration, ARBITER intercepts political acts targeting the affected district and states the additional cost before declaration is confirmed. Faction may proceed or withdraw.

---

### C07 — AMPLIFY

**Identity**

- **Card ID:** C07
- **Card version:** v1.0
- **Card name:** Amplify
- **Tagline:** *Boost the Popularity impact of your own political act this round.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target:** Self.
- **Restriction:** Acting faction must declare a political act this round. Cannot target a Pass.
- **Primary cost:** 2 Exposure.
- **Secondary cost:** None.
- **Faction affinity:** Network.
- **Affinity bonus:** Primary cost reduced to 1 Exposure.
- **Difficulty:** N/A
- **Resolution:** No roll required. Effect resolves on submission.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** N/A
- **Effect on success:** Popularity impact of the declared political act is doubled — positive or negative.
- **Effect on failure:** N/A
- **Effect on crit failure:** N/A

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A |
| Ghost | −1 | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *A message worth sending is worth sending loudly.*
- **Faction perspectives:**
  - Guild: *We let our structures speak. Amplification is for those who lack physical evidence.*
  - Directorate: *Institutional authority does not require amplification. Though we note its effectiveness.*
  - Network: *Every message we send should land as hard as possible. This ensures it does.*
  - Ghost: *Amplification is the opposite of what we do. Volume attracts attention. Attention ends operations.*
  - Syndicate: *Leverage applied at the right moment can move markets. This is that tool.*

**Taxonomy**

- **Taxonomy — Category:** Action
- **Taxonomy — Function:** Modify
- **Taxonomy — Target:** Political act (effect magnitude)

> **Design note:** Amplification cuts both ways — a failed political act that loses −1 Popularity loses −2 instead. ARBITER resolution mirrors C06: awareness retained after Beat 3 case opening, effect applied after political act resolves in Beat 4. "Self" is standard target value for self-targeting cards.

---

### C08 — BUY INFLUENCE

**Identity**

- **Card ID:** C08
- **Card version:** v1.0
- **Card name:** Buy Influence
- **Tagline:** *Deploy capital to place presence tokens directly, without groundwork.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** None.
- **Primary cost:** 3 Capital.
- **Secondary cost:** None.
- **Faction affinity:** Syndicate.
- **Affinity bonus:** Difficulty is Easy (75%) + ring modifier.
- **Difficulty:** Average (50%) + ring modifier
- **Resolution:** d100 roll vs. Difficulty Threshold per Artifact 03 §13.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** Place 3 presence tokens in the target district.
- **Effect on success:** Place 2 presence tokens in the target district.
- **Effect on failure:** Cost spent. No effect.
- **Effect on crit failure:** −2 Popularity.

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | −1 | N/A | N/A | N/A |
| Directorate | −1 | N/A | N/A | N/A |
| Network | −1 | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | +1 | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *In New Meridian, capital is a language everyone understands.*
- **Faction perspectives:**
  - Guild: *Presence earned through investment rather than community is fragile. We have seen it collapse.*
  - Directorate: *Purchasing influence undermines the legitimate institutional processes we exist to maintain.*
  - Network: *This is exactly the kind of power we are here to expose and resist.*
  - Ghost: *Bought presence is noisier than earned presence. It draws the wrong kind of attention.*
  - Syndicate: *Capital does not just open doors. It determines which doors exist in the first place.*

**Taxonomy**

- **Taxonomy — Category:** Board
- **Taxonomy — Function:** Add
- **Taxonomy — Target:** Presence

> **Design note:** No secondary cost — Capital bypasses local knowledge requirements. No presence requirement — primary entry mechanism for new districts. Syndicate affinity is difficulty reduction not cost reduction — better outcomes from spending, not discounts. Three Portrait penalties reflect strong doctrinal opposition.

---

### C09 — FUND

**Identity**

- **Card ID:** C09
- **Card version:** v1.0
- **Card name:** Fund
- **Tagline:** *Transfer resources to another faction as a gesture of support.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target:** Any other faction.
- **Restriction:** None.
- **Primary cost:** 2 Capital (transferred to target faction).
- **Secondary cost:** None.
- **Faction affinity:** Syndicate.
- **Affinity bonus:** Difficulty is Easy (75%).
- **Difficulty:** Average (50%)
- **Resolution:** d100 roll vs. Difficulty Threshold per Artifact 03 §13.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** Transfer occurs. +1 Popularity. ARBITER delivers free Accord card to acting faction.
- **Effect on success:** Transfer occurs. ARBITER delivers free Accord card to acting faction.
- **Effect on failure:** Cost spent. No effect.
- **Effect on crit failure:** −1 Popularity.

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | N/A | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | +1 | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *Every alliance in New Meridian begins with someone extending a hand.*
- **Faction perspectives:**
  - Guild: *Investment in relationships is as important as investment in structures.*
  - Directorate: *Financial transfers between factions warrant scrutiny. We monitor these carefully.*
  - Network: *Follow the money. It always leads somewhere interesting.*
  - Ghost: *Resources flowing between factions change the operational landscape. We note the direction.*
  - Syndicate: *Capital in motion creates relationships. Relationships create opportunities.*

**Taxonomy**

- **Taxonomy — Category:** Resource
- **Taxonomy — Function:** Redirect
- **Taxonomy — Target:** Native resource

> **Design note:** No ring modifier — targets a faction not a district. Transfer handled covertly at case return — resources appear in recipient's case at debrief. Source anonymous by default. Acting faction may announce after receiving free Accord card from ARBITER. Recipient may convert received Capital to native resource at 1:1. Free Accord card is a Political Act card (cost 0; return to ARBITER on play — not discarded) delivered to acting faction's hand at case resolution. Played in a subsequent Quarter — card returns in the dispatch case after Resolution, by which point Declaration for the current Quarter has already closed. Full card design: 04-12. "Any other faction" is standard target value when self-targeting is not permitted.

---

### C10 — PROTECT

**Identity**

- **Card ID:** C10
- **Card version:** v1.0
- **Card name:** Protect
- **Tagline:** *Defend a district's assets from covert disruption this round.*
- **Card type:** Covert Operation
- **Card subtype:** Standard
- **Card faction:** All
- **Pool copies:** 2

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** Acting faction must have at least 1 presence token in the target district.
- **Primary cost:** 1 district native resource.
- **Secondary cost:** None.
- **Faction affinity:** Guild. Directorate.
- **Affinity bonus:** Difficulty of all covert operations targeting acting faction's assets in district increased by 2 steps instead of 1.
- **Difficulty:** N/A
- **Resolution:** No roll required. Effect resolves on submission.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** N/A
- **Effect on success:** All covert operations targeting the acting faction's assets in the target district this round have their difficulty increased by 1 step.
- **Effect on failure:** N/A
- **Effect on crit failure:** N/A

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | +1 | N/A | N/A | N/A |
| Directorate | +1 | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *What you build is only worth as much as your willingness to defend it.*
- **Faction perspectives:**
  - Guild: *We protect what we build. This is not optional.*
  - Directorate: *Institutional assets require active defense. We resource this accordingly.*
  - Network: *We protect our people first. Infrastructure is secondary.*
  - Ghost: *The best protection is not being found in the first place.*
  - Syndicate: *Protected assets retain value. Unprotected assets invite acquisition.*

**Taxonomy**

- **Taxonomy — Category:** Cross-Category
- **Taxonomy — Function:** Protect
- **Taxonomy — Target:** Covert operation (difficulty)

> **Design note:** Applies only to acting faction's assets — not all factions' assets. ARBITER resolution mirrors C06. Source not announced. "At least 1 presence token" includes claim markers per Artifact 02a.

**Difficulty reference — affinity bonus:**

| Attacker's base difficulty | Standard Protect | Guild/Directorate Protect |
|---------------------------|-----------------|--------------------------|
| Automatic | Easy | Average |
| Easy | Average | Challenging |
| Average | Challenging | Impossible |
| Challenging | Impossible | Impossible |

---

## 8. Faction-Specific Covert Operations — C11–C35

Each faction holds 2 copies of each of their 5 faction-specific covert operation cards in their setup pool (10 faction-specific covert cards in pool). Faction-specific cards carry a faction-colored border on a charcoal back.

**Design status note:** C11–C15 (Guild) are signed off. C16–C35 are carried forward from prior drafts with full data structure applied. Taxonomy gap analysis in Artifact 04b §7 has identified redesign targets for Ghost (C16–C20), Directorate (C21–C25), Network (C26–C30), and Syndicate (C31–C35). These are flagged as pending decisions D-04-02 through D-04-05 in §16.

---

### THE GUILD — C11–C15 ✅ Signed Off

### C11 — FORTIFY STRUCTURE

**Identity**

- **Card ID:** C11
- **Card version:** v1.0
- **Card name:** Fortify Structure
- **Tagline:** *Reinforce a structure against demolition this round.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Guild
- **Pool copies:** 2

**Mechanics**

- **Beat:** 2
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** Acting faction must have a structure in the target district.
- **Primary cost:** 1 Capacity.
- **Secondary cost:** None.
- **Faction affinity:** Guild only.
- **Difficulty:** N/A
- **Resolution:** No roll required. Effect resolves on submission.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** N/A
- **Effect on success:** Guild structure in target district is immune to Demolish this round.
- **Effect on failure:** N/A
- **Effect on crit failure:** N/A

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | +1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *The Guild does not abandon what it has built.*
- **Faction perspectives:**
  - Guild: *Reinforcement is not fear. It is preparation.*

**Taxonomy**

- **Taxonomy — Category:** Cross-Category
- **Taxonomy — Function:** Protect
- **Taxonomy — Target:** Structure block

> **Design note:** Guild only. ARBITER retains awareness after Beat 2 opens. Immunity applied when C02 Demolish resolves in Beat 3.

---

### C12 — MATERIALS ACQUISITION

**Identity**

- **Card ID:** C12
- **Card version:** v1.0
- **Card name:** Materials Acquisition
- **Tagline:** *Recover the costs of demolition as subcontract payment.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Guild
- **Pool copies:** 2

**Mechanics**

- **Beat:** 2
- **Trigger condition:** Condition-based: target faction completes C02 Demolish this round, confirmed at Beat 3
- **Target:** Any other faction.
- **Restriction:** Target faction must successfully complete a C02 Demolish action this round. Only the first qualifying Demolish this round triggers this effect.
- **Primary cost:** None.
- **Secondary cost:** None.
- **Faction affinity:** Guild only.
- **Difficulty:** N/A
- **Resolution:** No roll required. Effect resolves when trigger condition is confirmed at Beat 3.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** N/A
- **Effect on success:** Guild receives all resources paid by the target faction to execute C02 this round — delivered in case.
- **Effect on failure:** N/A
- **Effect on crit failure:** N/A

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | +1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *In New Meridian, even demolition is a Guild service.*
- **Faction perspectives:**
  - Guild: *We do not need to swing the hammer ourselves. We simply ensure we are paid when someone else does.*

**Taxonomy**

- **Taxonomy — Category:** Resource
- **Taxonomy — Function:** Recover
- **Taxonomy — Target:** Native resource

> **Design note:** Guild names target faction at submission — betting that faction will execute C02 this round. Zero cost means no loss if prediction is wrong. Only the first qualifying Demolish triggers. ARBITER confirms trigger at Beat 3.

---

### C13 — FOUNDATION RIGHTS

**Identity**

- **Card ID:** C13
- **Card version:** v1.0
- **Card name:** Foundation Rights
- **Tagline:** *Claim a foothold in territory no other faction has entered.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Guild
- **Pool copies:** 2

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** Target district must have zero presence from any faction.
- **Primary cost:** 1 Capacity.
- **Secondary cost:** None.
- **Faction affinity:** Guild only.
- **Difficulty:** N/A
- **Resolution:** No roll required. Effect resolves on submission.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** N/A
- **Effect on success:** Place 1 presence token in the target district.
- **Effect on failure:** N/A
- **Effect on crit failure:** N/A

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | +1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *The Guild was here before the city had a name.*
- **Faction perspectives:**
  - Guild: *Unclaimed territory is not unknown to us. We have records going back further than anyone else at this table.*

**Taxonomy**

- **Taxonomy — Category:** Board
- **Taxonomy — Function:** Add
- **Taxonomy — Target:** Presence

> **Design note:** "Zero presence" includes deployment markers per Artifact 02a. Guild's own deployment marker disqualifies the district — Foundation Rights requires complete absence. No secondary cost — unclaimed districts have no established resource infrastructure.

---

### C14 — CONSTRUCTION CREW

**Identity**

- **Card ID:** C14
- **Card version:** v1.0
- **Card name:** Construction Crew
- **Tagline:** *Build a structure before your presence is fully established.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Guild
- **Pool copies:** 2

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** Acting faction must have at least 1 presence in the target district.
- **Primary cost:** 3 Capacity.
- **Secondary cost:** None.
- **Faction affinity:** Guild only.
- **Difficulty:** N/A if no other faction has presence in target district. Average (50%) + ring modifier if any other faction has presence in target district.
- **Resolution:** If no other faction has presence in target district, effect resolves without a roll. Otherwise, d100 roll vs. Average (50%) Difficulty Threshold + ring modifier per Artifact 03 §13.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** Return 1 Capacity to dispatch case.
- **Effect on success:** Place 1 structure block in target district.
- **Effect on failure:** Cost spent. No effect.
- **Effect on crit failure:** −1 Popularity.

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | +1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *The Guild does not always wait for permission.*
- **Faction perspectives:**
  - Guild: *Sometimes the crews arrive before the paperwork. This is not an accident.*

**Taxonomy**

- **Taxonomy — Category:** Action
- **Taxonomy — Function:** Remove Restriction
- **Taxonomy — Target:** Covert operation (presence requirement)

> **Design note:** Waives Established requirement from C01. Difficulty scales with contested presence. Failure effects apply only when contested difficulty condition is active. Crit success refunds 1 Capacity — net cost 2 Capacity matches C01 primary cost efficiency. Intended chain: C13 establishes presence, C14 builds structure same round. ARBITER confirms presence conditions at Beat 3. Submission order within Beat 3 matters for C13→C14 chain.

---

### C15 — INFRASTRUCTURE YIELD

**Identity**

- **Card ID:** C15
- **Card version:** v1.0
- **Card name:** Infrastructure Yield
- **Tagline:** *Draw resources from infrastructure you have already built.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Guild
- **Pool copies:** 2

**Mechanics**

- **Beat:** 3
- **Trigger condition:** N/A
- **Target:** Any district.
- **Restriction:** Acting faction must be Established or Dominant in target district.
- **Primary cost:** None.
- **Secondary cost:** None.
- **Faction affinity:** Guild only.
- **Difficulty:** N/A
- **Resolution:** No roll required. Effect resolves on submission.
- **Outcome type:** N/A

**Effects**

- **Effect on crit success:** N/A
- **Effect on success:** Gain 1 unit of the target district's native resource — delivered in case.
- **Effect on failure:** N/A
- **Effect on crit failure:** N/A

**Portrait**

| Faction | Base | Condition | Modifier | Mod Condition |
|---------|------|-----------|----------|---------------|
| Guild | +1 | N/A | N/A | N/A |
| Directorate | N/A | N/A | N/A | N/A |
| Network | N/A | N/A | N/A | N/A |
| Ghost | N/A | N/A | N/A | N/A |
| Syndicate | N/A | N/A | N/A | N/A |

**Narrative**

- **Narrative anchor:** *The Guild built New Meridian's infrastructure. Drawing from it is not theft. It is dividend.*
- **Faction perspectives:**
  - Guild: *We built this. Every unit we draw from it was always ours.*

**Taxonomy**

- **Taxonomy — Category:** Resource
- **Taxonomy — Function:** Add
- **Taxonomy — Target:** Native resource

> **Design note:** Zero cost — Established presence is the only gate. Grid Tap (sacrifice presence for 2 native resource) tabled as political act or operative ability — flag for §10 and Artifact 05.

---

### GHOST — C16–C20 🔄 Pending Redesign Review (D-04-02)

*Current cards carried forward. Taxonomy gap analysis in Artifact 04b §8.1 identifies redesign targets: C18/C19 duplicate function; Cross-Category — Shift Portrait primary card needed; Cross-Category — Reveal to named faction needed; Action — Copy subset needed.*

### C16 — PATTERN MATCH

- **Card ID:** C16
- **Card name:** Pattern Match
- **Tagline:** *Identify a faction's operation and location before they move.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Ghost only.
- **Beat:** 3
- **Target:** Any other faction.
- **Restriction:** Operation type and district named.
- **Primary cost:** 2 Findings.
- **Secondary cost:** None.
- **Faction affinity:** Ghost only.
- **Difficulty:** N/A.
- **Resolution:** Prediction accuracy — named faction must have acted. Both operation type and district correct = success. Exactly one correct = failure. Neither correct = crit failure. No roll.
- **Effect on crit success:** N/A.
- **Effect on success:** Named faction submitted named operation type in named district. Pattern Match resolves as a full copy of that operation in that district.
- **Effect on failure:** Named faction submitted named operation type in a different district, OR named faction submitted any operation in named district. 2 Findings returned to Ghost.
- **Effect on crit failure:** All other conditions. 2 Findings spent. No effect.
- **Portrait:** +2 Ghost (success). +1 Ghost (failure/refund condition).
- **Narrative anchor:** *Ghost does not guess. Ghost identifies what is already in motion.*
- **Faction perspectives:**
  - Ghost: *We are not predicting. We are recognising a pattern we have already seen.*
- **Taxonomy:** Action — Copy — Covert operation (full).

> **Design note:** If the copied operation cannot legally be executed by Ghost, Pattern Match fizzles — 2 Findings spent, no effect regardless of prediction accuracy.

---

### C17 — INTERCEPT

- **Card ID:** C17
- **Card name:** Intercept
- **Tagline:** *Surveil a faction's covert operations in real time.*
- **Card type:** Covert Operation
- **Card subtype:** Faction-specific
- **Card faction:** Ghost
- **Beat:** 3
- **Target:** Any other faction
- **Restriction:** Must hold at least 1 Intel note naming target faction
- **Primary cost:** 1 Intel note naming target faction (consumed)
- **Secondary cost:** 2 Findings
- **Difficulty:** Average
- **Resolution:** 2d10 roll vs. difficulty target — see §X
- **Effect on crit success:** ARBITER delivers first 2 covert operations submitted by target faction this round to Ghost in case — operation type and district for each
- **Effect on success:** ARBITER delivers first covert operation submitted by target faction this round to Ghost in case — operation type and district
- **Effect on failure:** ARBITER delivers notification slip to target faction in case — see C05 failure slip text
- **Effect on crit failure:** Ghost Public Standing −2. Reason not disclosed. ARBITER moves marker without explanation
- **Portrait Unconditional:** +1 Ghost
- **Portrait Bonus:** N/A
- **Portrait Bonus Condition:** N/A
- **Narrative anchor:** *To know what they are doing while they are doing it — that is the only intelligence that matters.*
- **Faction perspectives:**
  - Ghost: *We do not wait for the after-action report. We read the operation as it happens.*
- **Taxonomy — Category:** Cross-Category
- **Taxonomy — Function:** Reveal
- **Taxonomy — Target:** Covert operation — named faction

> **Design note:** Intel note consumed at submission regardless of roll outcome. "Delivered in case" is standard language per L59. Crit failure Public Standing shift is silent — ARBITER records reason internally only. Replaces C17 Archive Recovery (retired — L78).

---

### C18 — IDENTITY BLIND

- **Card ID:** C18
- **Card name:** Identity Blind
- **Tagline:** *Submit a covert operation with no attribution this round.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Ghost only.
- **Beat:** 2
- **Target:** Self.
- **Restriction:** Must be submitted with one other covert operation in the same dispatch case.
- **Primary cost:** 2 Findings.
- **Secondary cost:** None.
- **Faction affinity:** Ghost only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** One attached covert operation resolves normally. ARBITER records no faction attribution for it. Ghost not surfaced even on failed detection roll.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Narrative anchor:** *The most dangerous thing an analyst can do is be noticed.*
- **Faction perspectives:**
  - Ghost: *We were not there. The record confirms this.*
- **Taxonomy:** Cross-Category — Protect — Action attribution.

> **Design note:** One use per round. Beat 2. Flagged for redesign — duplicates function with C19 (Cross-Category — Protect — Action attribution). See D-04-02.

---

### C19 — DEEP COVER

- **Card ID:** C19
- **Card name:** Deep Cover
- **Tagline:** *Permanently remove a prior operation from the accessible record.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Ghost only.
- **Beat:** 3
- **Target:** Self.
- **Restriction:** Ghost must have a prior operation from a previous round that resolved without attribution.
- **Primary cost:** 1 Findings.
- **Secondary cost:** None.
- **Faction affinity:** Ghost only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** Ghost names one prior-round operation. That operation is permanently removed from any investigable record for the remainder of the session.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Narrative anchor:** *Good cover does not expire at the end of the week.*
- **Faction perspectives:**
  - Ghost: *It did not happen. This is not a lie. It is a permanent correction to an incomplete record.*
- **Taxonomy:** Cross-Category — Protect (permanent) — Action attribution.

> **Design note:** Permanent per Principle 11. Flagged for redesign — duplicates function with C18. See D-04-02.

---

### C20 — MISDIRECTION

- **Card ID:** C20
- **Card name:** Misdirection
- **Tagline:** *Plant false intelligence about Ghost in the accessible record.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Ghost only.
- **Beat:** 3
- **Target:** Any other faction.
- **Restriction:** Ghost must hold at least 1 Intel token naming Ghost (self-directed).
- **Primary cost:** 1 Findings.
- **Secondary cost:** None.
- **Faction affinity:** Ghost only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** ARBITER delivers a false Intel token to the target faction in case. Token contains a false operation type and false target district for Ghost this round.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Narrative anchor:** *Ghost has been considering what its opponents think Ghost is doing. It is never quite right.*
- **Faction perspectives:**
  - Ghost: *We have thought carefully about what they expect. We have given them exactly that.*
- **Taxonomy:** Resource — Add — Intel token (corrupt content).

> **Design note:** Ghost may hold self-directed Intel tokens without cap (Artifact 02b §8). False token indistinguishable from genuine Gather result. Any Denounce using it will fail. Taxonomy note: Add with corrupt content — falsification is an attribute of content, not a separate function.

---

### THE DIRECTORATE — C21–C25 🔄 Pending Redesign Review (D-04-03)

*Current cards carried forward. Taxonomy gap analysis in Artifact 04b §8.2 identifies redesign targets: C21/C25 duplicate Block function; Resource — Add (Mandate generation) card needed; Cross-Category — Shift Public Standing candidate.*

### C21 — INVOKE JURISDICTION

- **Card ID:** C21
- **Card name:** Invoke Jurisdiction
- **Tagline:** *Assert institutional authority over a target district.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Directorate only.
- **Beat:** 2
- **Target:** Any district.
- **Restriction:** None.
- **Primary cost:** 2 Mandate.
- **Secondary cost:** None.
- **Faction affinity:** Directorate only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** No faction may submit Build Structure (C01) or Campaign (C03) targeting the named district this round. Source is public.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Portrait:** +1 Directorate.
- **Narrative anchor:** *The Directorate was here before the other factions arrived. Their jurisdictional authority is not theoretical.*
- **Faction perspectives:**
  - Directorate: *This district is under institutional oversight. Expansion requires authorisation. Authorisation has not been granted.*
- **Taxonomy:** Action — Block — Covert operation (C01, C03).

---

### C22 — DETAIN

- **Card ID:** C22
- **Card name:** Detain
- **Tagline:** *Permanently remove a faction's operational marker from a district.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Directorate only.
- **Beat:** 3
- **Target:** Any district.
- **Restriction:** Target faction must have a deployment marker in the target district. Fresh Intel token naming the target faction required (age 0–1 rounds). Cannot target the Chorus Node operational marker.
- **Primary cost:** 3 Mandate.
- **Secondary cost:** None.
- **Faction affinity:** Directorate only.
- **Difficulty:** Average + ring modifier.
- **Effect on crit success:** Return primary cost to dispatch case.
- **Effect on success:** Target faction's operational marker in the named district is permanently removed for the remainder of the session. Target notified in case.
- **Effect on failure:** Cost spent. No effect.
- **Effect on crit failure:** −1 Popularity.
- **Portrait:** +1 Directorate.
- **Narrative anchor:** *The Directorate does not destroy — it removes from play. Sometimes that is enough.*
- **Faction perspectives:**
  - Directorate: *The marker has been detained. Its conversion will not occur.*
- **Taxonomy:** Board — Remove (permanent) — Presence (claim marker).

> **Design note:** Permanent per Principle 11. Prior version returned marker at end of next round — revised. Intel token requirement means Directorate must have gathered intelligence on target faction this or last round. Notification slip feasibility pending Artifact 07 (A-04-05).

---

### C23 — EVIDENCE PRESERVATION

- **Card ID:** C23
- **Card name:** Evidence Preservation
- **Tagline:** *Lock a written record against modification for the remainder of the session.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Directorate only.
- **Beat:** 3
- **Target:** Any written record element.
- **Restriction:** Target must be a physically written or recorded game element. Cannot target printed card text.
- **Primary cost:** 2 Mandate.
- **Secondary cost:** None.
- **Faction affinity:** Directorate only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** Named record element is locked for the remainder of the session. Cannot be modified by any card effect.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Portrait:** +1 Directorate.
- **Narrative anchor:** *The Directorate's institutional advantage is the record. They protect it.*
- **Faction perspectives:**
  - Directorate: *The record is preserved. Its integrity is now institutional fact.*
- **Taxonomy:** Cross-Category — Protect (permanent) — Accord agreement / written record.

---

### C24 — SURVEILLANCE PLACEMENT

- **Card ID:** C24
- **Card name:** Surveillance Placement
- **Tagline:** *Install permanent monitoring in a target district.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Directorate only.
- **Beat:** 3
- **Target:** Any district.
- **Restriction:** None.
- **Primary cost:** 2 Mandate.
- **Secondary cost:** None.
- **Faction affinity:** Directorate only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** For the remainder of the session, ARBITER privately notifies The Directorate of any covert operation submitted targeting the named district — operation type only, not faction. Delivered in case at Beat 3 before operations resolve.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Portrait:** +1 Directorate.
- **Narrative anchor:** *The Directorate monitors because monitoring is their primary tool for managing what they cannot directly control.*
- **Faction perspectives:**
  - Directorate: *The installation is in place. Everything that happens in that district now happens with our awareness.*
- **Taxonomy:** Resource — Add (permanent) — Intel token.

> **Design note:** Permanent per Principle 11. Prior version monitored for 2 rounds — revised. Operation type only, not faction — creates intelligence chain requiring follow-up Gather to identify actors. ARBITER maintains awareness of surveilled districts.

---

### C25 — SEALED BORDER

- **Card ID:** C25
- **Card name:** Sealed Border
- **Tagline:** *Prevent new presence from entering a district this round.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Directorate only.
- **Beat:** 2
- **Target:** Any district.
- **Restriction:** None.
- **Primary cost:** 3 Mandate.
- **Secondary cost:** None.
- **Faction affinity:** Directorate only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** No faction may place presence tokens in the named district this round. Existing tokens unaffected. Does not prevent Demolish, Gather, or Undermine. Source is public.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Portrait:** +1 Directorate.
- **Narrative anchor:** *The Directorate can close a border. The question it always faces is whether closing makes the situation more or less manageable.*
- **Faction perspectives:**
  - Directorate: *The border is sealed. Expansion requires our authorisation. It will not be granted today.*
- **Taxonomy:** Action — Block — Covert operation (presence placement).

> **Design note:** Flagged for redesign — C21 and C25 both Block covert operations, same function different scope. See D-04-03.

---

### THE NETWORK — C26–C30 🔄 Pending Redesign Review (D-04-04)

*Current cards carried forward. Taxonomy gap analysis in Artifact 04b §8.3 identifies redesign targets: C26/C28 duplicate Reveal function; C27 doctrinally misaligned; Resource — Add (Exposure generation) needed; Cross-Category — Shift Public Standing (primary) needed.*

### C26 — LEAK

- **Card ID:** C26
- **Card name:** Leak
- **Tagline:** *Make one resolved operation's target district public after resolution.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Network only.
- **Beat:** 3
- **Target:** Any other faction.
- **Restriction:** None.
- **Primary cost:** 1 Exposure.
- **Secondary cost:** None.
- **Faction affinity:** Network only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** After Beat 3 resolution, ARBITER publicly announces the target district of the highest-impact resolved covert operation from the named faction this round. Operation type not revealed — district only.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Portrait:** +1 Network.
- **Narrative anchor:** *The Network does not need to know everything — only enough to make the right question public.*
- **Faction perspectives:**
  - Network: *We do not reveal everything. We reveal the piece that makes everything else visible.*
- **Taxonomy:** Cross-Category — Reveal — Action attribution.

---

### C27 — SOURCE PROTECTION

- **Card ID:** C27
- **Card name:** Source Protection
- **Tagline:** *Prevent attribution on one of your own operations this round.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Network only.
- **Beat:** 2
- **Target:** Self.
- **Restriction:** Network must submit at least one other covert operation this round.
- **Primary cost:** 1 Exposure.
- **Secondary cost:** None.
- **Faction affinity:** Network only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** One Network covert operation this round has no ARBITER attribution on failed detection — fails silently.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Narrative anchor:** *The Network protects its sources. This includes itself.*
- **Faction perspectives:**
  - Network: *We believe in transparency. Except when protecting a source requires otherwise.*
- **Taxonomy:** Cross-Category — Protect — Action attribution.

> **Design note:** Flagged for redesign — Cross-Category — Protect — Action attribution is more doctrinally Ghost than Network. Network's stated doctrine (transparency) is in tension with source concealment. The faction perspective acknowledges this tension. See D-04-04.

---

### C28 — OPEN CHANNEL

- **Card ID:** C28
- **Card name:** Open Channel
- **Tagline:** *Force private ARBITER notifications to a faction to be delivered publicly.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Network only.
- **Beat:** 2
- **Target:** Any other faction.
- **Restriction:** None.
- **Primary cost:** 2 Exposure.
- **Secondary cost:** None.
- **Faction affinity:** Network only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** Any private notification ARBITER would send to the named faction this round is instead delivered publicly to the whole table.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Portrait:** +1 Network.
- **Narrative anchor:** *Secret communications between powerful institutions are themselves a form of harm. Opening the channel is the argument.*
- **Faction perspectives:**
  - Network: *If it happened, it should be known. We are simply making that principle operational.*
- **Taxonomy:** Cross-Category — Reveal — Private communications.

> **Design note:** Does not intercept Hidden Objective or Classified Directive communications. Beat 2 — must be active before Beat 3 notifications are generated. Flagged for review — C26 and C28 both Reveal, same function different scope. See D-04-04.

---

### C29 — NETWORK CASCADE

- **Card ID:** C29
- **Card name:** Network Cascade
- **Tagline:** *Extend Broadcast Interference to an adjacent district.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Network only.
- **Beat:** 2
- **Target:** Any district adjacent to the Network's Broadcast Interference target this round.
- **Restriction:** Network must also submit C06 Broadcast Interference this round. Adjacent district named at submission.
- **Primary cost:** 2 Exposure.
- **Secondary cost:** None.
- **Faction affinity:** Network only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** Adjacent district also has political act costs +1 this round.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Portrait:** +1 Network.
- **Narrative anchor:** *The Network understands signal propagation better than anyone at this table.*
- **Faction perspectives:**
  - Network: *The signal does not stop at district borders. Neither do we.*
- **Taxonomy:** Action — Modify — Covert operation (scope).

---

### C30 — COMMUNITY ANCHOR

- **Card ID:** C30
- **Card name:** Community Anchor
- **Tagline:** *Establish presence in a Sprawl district through existing relationships.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Network only.
- **Beat:** 3
- **Target:** Any Sprawl district.
- **Restriction:** Network must have zero presence in the target district. Sprawl districts only.
- **Primary cost:** 1 Exposure.
- **Secondary cost:** None.
- **Faction affinity:** Network only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** Place 1 presence token in the target Sprawl district.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Portrait:** +1 Network.
- **Narrative anchor:** *The Network did not arrive in New Meridian through official channels. They arrived through people.*
- **Faction perspectives:**
  - Network: *We already have contacts there. This is formalising what already exists.*
- **Taxonomy:** Board — Add — Presence.

---

### THE SYNDICATE — C31–C35 🔄 Pending Redesign Review (D-04-05)

*Current cards carried forward. Taxonomy gap analysis in Artifact 04b §8.4 identifies redesign targets: zero information/intelligence capability; Cross-Category — Corrupt Accord unused; Resource — Redirect Accord ("small print") unused.*

### C31 — LEVERAGED ACQUISITION

- **Card ID:** C31
- **Card name:** Leveraged Acquisition
- **Tagline:** *Gain resource generation from a district without presence.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Syndicate only.
- **Beat:** 3
- **Target:** Any district.
- **Restriction:** Maximum one district per round.
- **Primary cost:** 4 Capital.
- **Secondary cost:** None.
- **Faction affinity:** Syndicate only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** Gain 1 unit of the target district's native resource this Upkeep as though Established — delivered in case.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Portrait:** +1 Syndicate.
- **Narrative anchor:** *The Syndicate does not need to be somewhere to profit from it. Ownership and presence are different things.*
- **Faction perspectives:**
  - Syndicate: *We own the revenue stream. Whether we are physically present is irrelevant.*
- **Taxonomy:** Resource — Add — Native resource.

---

### C32 — SHORT THE MARKET

- **Card ID:** C32
- **Card name:** Short the Market
- **Tagline:** *Reduce a faction's native resource generation for one round.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Syndicate only.
- **Beat:** 3
- **Target:** Any other faction.
- **Restriction:** Fresh Intel token naming the target faction required (age 0–1 rounds).
- **Primary cost:** 2 Capital.
- **Secondary cost:** None.
- **Faction affinity:** Syndicate only.
- **Difficulty:** Average.
- **Effect on crit success:** Target faction generates 2 fewer units this Upkeep (minimum 0).
- **Effect on success:** Target faction generates 1 fewer unit of their native resource during Upkeep this round (minimum 0). Applied silently.
- **Effect on failure:** Cost spent. No effect.
- **Effect on crit failure:** −1 Popularity.
- **Portrait:** +1 Syndicate.
- **Narrative anchor:** *Capital can suppress as easily as it can produce.*
- **Faction perspectives:**
  - Syndicate: *We are not destroying their capacity. We are adjusting market conditions temporarily.*
- **Taxonomy:** Resource — Remove — Native resource.

---

### C33 — HOSTILE ACQUISITION

- **Card ID:** C33
- **Card name:** Hostile Acquisition
- **Tagline:** *Purchase ownership of an opponent's structure.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Syndicate only.
- **Beat:** 3
- **Target:** Any district.
- **Restriction:** Target faction must have a structure in the target district. Cannot target a Guild structure protected by Fortify Structure (C11) this round.
- **Primary cost:** 5 Capital.
- **Secondary cost:** None.
- **Faction affinity:** Syndicate only.
- **Difficulty:** Average + ring modifier.
- **Effect on crit success:** Return 1 Capital to dispatch case.
- **Effect on success:** Claim one named opponent structure. Block flips to Syndicate color. Prior owner receives 1 unit of their native resource as consideration — delivered in case.
- **Effect on failure:** Cost spent. No effect.
- **Effect on crit failure:** −1 Popularity.
- **Portrait:** +1 Syndicate.
- **Narrative anchor:** *Everything in New Meridian has a price. The Syndicate is the only faction honest about this.*
- **Faction perspectives:**
  - Syndicate: *We made a fair offer. The market determined the value. We accepted the market's judgment.*
- **Taxonomy:** Board — Redirect — Structure block.

---

### C34 — GOLDEN PARACHUTE

- **Card ID:** C34
- **Card name:** Golden Parachute
- **Tagline:** *Transfer resources before a forced resource-loss event.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Syndicate only.
- **Beat:** 2
- **Target:** Any other faction.
- **Restriction:** Must be submitted in the same round as an anticipated resource-loss event. Must be submitted before Beat 3. Cannot be reclaimed after transfer.
- **Primary cost:** None (transfer amount is the cost — leaves Syndicate's pool).
- **Secondary cost:** None.
- **Faction affinity:** Syndicate only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** Transfer up to 3 Capital to named faction. Recorded by ARBITER but not announced. Transferred Capital exits Syndicate's pool before any resource-loss calculation applies this round.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Portrait:** +1 Syndicate.
- **Narrative anchor:** *The Syndicate plans for outcomes not yet confirmed. They move assets before the decision is made.*
- **Faction perspectives:**
  - Syndicate: *We did not lose those resources. We repositioned them. There is a difference.*
- **Taxonomy:** Cross-Category — Protect — Native resource.

---

### C35 — REGULATORY CAPTURE

- **Card ID:** C35
- **Card name:** Regulatory Capture
- **Tagline:** *Block a specific action type in a named district for one round.*
- **Card type:** Faction-Specific Covert Operation
- **Faction:** Syndicate only.
- **Beat:** 2
- **Target:** Any district.
- **Restriction:** Cannot apply to the Chorus Node.
- **Primary cost:** 3 Capital.
- **Secondary cost:** None.
- **Faction affinity:** Syndicate only.
- **Difficulty:** Automatic.
- **Effect on crit success:** N/A — Automatic.
- **Effect on success:** Named district and action type: no faction may submit that type targeting that district this round. Source is public.
- **Effect on failure:** N/A — Automatic.
- **Effect on crit failure:** N/A — Automatic.
- **Portrait:** −1 Syndicate (if used to block Guild construction operations). +1 Syndicate otherwise.
- **Narrative anchor:** *If you own enough of the regulatory structure, you define what is permitted. The Syndicate does not see this as corruption. They see it as governance.*
- **Faction perspectives:**
  - Syndicate: *The regulatory framework exists. We simply ensure it reflects current market conditions.*
- **Taxonomy:** Action — Block — Covert operation + Political act.

---

## 9. Standard Political Acts — P01–P08

*Status: Political acts are carried forward from v0.9.4 in summary form. Full card data structure (§6) has not yet been applied card-by-card. Political act card-by-card review is the next design pass after 04 sign-off (D-04-06). Taxonomy assignments are preliminary.*

Political acts use the same data structure as covert operations (§6) with two additional fields:

| Additional Field | Description |
|-----------------|-------------|
| **Popularity effect** | Popularity movement on success and failure. |
| **Declaration requirement** | Any verbal or physical declaration required at time of play. |

Political acts are Beat 4 cards unless otherwise specified.

| Card ID | Name | Primary taxonomy | Faction affinity | Status |
|---------|------|-----------------|-----------------|--------|
| P01 | Establish Presence | Board — Add — Presence | Directorate | Pending full data structure |
| P02 | Contest | Board — Remove — Presence (contested) | Directorate, Network | Pending |
| P03 | Commission | Board — Add — Structure (both deployment districts) | Guild | Pending |
| P04 | Denounce | Cross-Category — Shift — Public Standing (−) | Network, Directorate | Pending |
| P05 | Broadcast | Cross-Category — Reveal — Action attribution | Network | Pending |
| P06 | Leverage | Resource — Remove — Native resource | Syndicate | Pending |
| P07 | Invoke the Table | Action — Block — Any (procedural) | Directorate | Pending |
| P08 | Propose Accord | Resource — Add — Accord agreement | Directorate | Pending |

---

## 10. Faction-Specific Political Acts — P09–P18

*Status: Same as §9 — pending full card data structure revision.*

| Card ID | Name | Faction | Primary taxonomy | Status |
|---------|------|---------|-----------------|--------|
| P09 | Public Works Declaration | Guild | Board — Add — Structure (both districts) | Pending |
| P10 | Infrastructure Bond | Guild | Resource — Add — Native resource (target faction) | Pending |
| P11 | Issue Directive | Directorate | Action — Block — Political act | Pending |
| P12 | Convene an Inquiry | Directorate | Resource — Add — Intel token (all factions) | Pending |
| P13 | Public Disclosure | Network | Cross-Category — Reveal — Action attribution | Pending |
| P14 | Open Record Request | Network | Cross-Category — Reveal — Written record | Pending |
| P15 | Acquisition Offer | Syndicate | Board — Redirect — Presence | Pending |
| P16 | Market Pressure | Syndicate | Action — Modify — Covert + Political act (cost) | Pending |
| P17 | Publish Analysis | Ghost | Cross-Category — Shift — Chorus Portrait | Pending |
| P18 | Signal Review Request | Ghost | Action — Modify — Covert operation (difficulty) | Pending |

---

## 11. Rules & Constraints — Modifier Cards

### 11.1 What They Are

Two sets:

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

**One card type. Four cards per faction.** Kept beside the tableau — not drawn from any deck. Reusable every round. Neutral grey back.

**In dispatch case:** Signals that slot is intentionally empty. Three Pass cards with no operations = Full Covert Pass — legal, noted.

**At Declaration:** Place face-up instead of declaring a political act.

**Ghost's Political Pass:** Confirms dispatch case contains 4 covert operations. Fourth operation slot available only when Ghost uses their Political Pass. Full rule in Artifact 03 §9.

A Pass is information. Consistent passes signal posture. ARBITER notes the pattern.

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
14. Taxonomy (Category — Function — Target)

Faction perspectives are in the card data structure. Visual design (Artifact 11) decides whether they appear on the card face.

### 13.2 Modifier Cards — Faction

Face: name, type indicator, effect, attachment rule (if restricted), Portrait (if applicable), value rating (1–3). Back: faction color, faction symbol.

### 13.3 Modifier Cards — Ring

Face: ring constraint statement as visually distinct element, name, type indicator, effect, Portrait (if applicable), value rating (1–3). Back: ring color, ring name.

### 13.4 Pass Cards

Face: "Pass — This slot is intentionally empty." Ghost rule note small. Back: neutral grey.

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
| D-04-02 | Ghost C16–C20 redesign — C18/C19 duplicate function; Portrait Shift, targeted Reveal, Copy subset gaps unaddressed. Approve current set or redesign? | Artifact 09 |
| D-04-03 | Directorate C21–C25 redesign — C21/C25 duplicate Block function; Mandate generation card needed. Approve current set or redesign? | Artifact 09 |
| D-04-04 | Network C26–C30 redesign — C26/C28 duplicate Reveal; C27 doctrinally misaligned; Exposure generation and Public Standing Shift needed. Approve current set or redesign? | Artifact 09 |
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
| A-04-05 | Pre-written ARBITER notification slips are feasible as paper prototype components | Multiple cards (C05, C22, C24, C32) depend on this component |

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

*End of Artifact 04 — Card System v0.9.6*
