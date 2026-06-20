# 04b — ACTION TAXONOMY & DESIGN ANALYSIS
## THE SIGNAL P1 — Paper Prototype

**Version:** 1.8  
**Status:** 📝 Draft — S107 audit (L222–L227); re-sign-off required  
**Last Updated:** 2026-06-20  
**Companion to:** 04 — Action Card System  
**Purpose:** Preserve the taxonomy framework, development decisions, coverage analysis, and faction design recommendations that govern Artifact 04 and all future card design passes.

---

## 1. Overview

This document is the authoritative source for the action system taxonomy — the framework for categorizing what every card in The Signal can affect and how. It also contains the design analysis that produced it: coverage gap analysis, faction coverage matrix, and design recommendations for the next card pass.

Card definitions live in Artifact 04. This document does not reproduce card content. The taxonomy fields on each card (Category — Function — Subject) reference this document for definitions.

---

## 2. Index

| Section | Content |
|---------|---------|
| §3 | [Physical Action Taxonomy](#3-physical-action-taxonomy) — verbs, component matrix, DB primitive model |
| §3.3 | [Primitive Action Model — Database-Backed Analysis](#33-primitive-action-model-database-backed-analysis-s47) |
| §4 | [Card Design Layer — Key Decisions](#4-card-design-layer-key-decisions) — rationale for Layer/Function framework; six game layers |
| §5 | [Card Taxonomy Index](#5-card-taxonomy-index) — Layer, Function, Subject, Primitive Verb per card |
| §6 | [Coverage Analysis — Gaps and Concentrations](#6-coverage-analysis-gaps-and-concentrations) |
| §7 | [Faction Coverage Matrix](#7-faction-coverage-matrix) |
| §8 | [Design Recommendations by Faction](#8-design-recommendations-by-faction) |
| §9 | [Standalone Card Types — Taxonomy Exclusions](#9-standalone-card-types-taxonomy-exclusions) |

---

## 3. Physical Action Taxonomy

*Relocated S97. Content now lives in its canonical home:*

- **§3.1 Physical Action Verbs + §3.2 Component × Verb Matrix** → Art 02 §13. Art 02 is the component source of truth; the DB view `v_comp_verb_matrix` is the analytical aggregate.
- **§3.3 Primitive Action Model & Legalization Analysis** → Art 03 §22. Art 03 is the legality source of truth; DB views `v_unlegislated_primitives` and `v_unlegislated_by_trigger` are the ongoing coverage audit.

---

## 4. Card Design Layer — Key Decisions

The physical action taxonomy (§3) defines what can happen to components. The card design layer defines *which game system a card affects* — independent of which physical verbs execute the effect. These are the decisions that produced the Layer — Function — Subject framework used in §5.

*Naming note: the six divisions in this section are called **Layers**. The expansion tier terminology was renamed from "Layer N" to "Tier N" across all artifacts (XA-37, S49). No collision risk remains.*

### 4.1 Layers define game systems, not action types

A **Layer** answers: which game system does this card affect?
A **Function** answers: what does the card do to it?

The distinction matters because the same physical verb can serve different design purposes. `Add` as a Territory action (placing presence) and `Add` as an Economy action (gaining Intel) are the same physical primitive but different design intents. Layer assignment ensures the portfolio is balanced across game systems, not just across verbs.

Layers are game-design partitions — not narrative concepts, not phase concepts. They describe what the game is tracking and what cards can affect.

### 4.2 The six game layers

| Layer | Visibility | Governs |
|-------|-----------|---------|
| **Territory** | Public | The influence landscape: Presence chips, structures, Dominant markers, spatial markers |
| **Economy** | Public | Quantitative holdings: native resources, card counts, Accord existence |
| **Information** | Private → Public | Qualitative content: token content, written records, attribution, reconnaissance |
| **Submission** | Split (covert = private, political = public) | What enters the resolution queue: costs, eligibility, blocks, scope |
| **Resolution** | Split by phase | The d100 system: threshold, modifier stack, difficulty, Battlefield Strength, outcome scale |
| **Standing** | Split (Public Standing = public, Portrait = private) | Reputation tracks as affectable consequence registers |

### 4.3 Cross-Category is retired

The original four categories (Board / Resource / Action / Cross-Category) used Cross-Category as a catch-all for information revelation, reputation shifts, and protection effects. When a catch-all grows to cover ~30% of the card set, it is a signal that the underlying partitioning is incomplete.

The six layers resolve this explicitly:
- Information effects (Reveal, Conceal, attribution Protect, Corrupt) → Information layer
- Reputation-track effects → Standing layer
- Protect effects → layer of the protected target (§4.6)

Cross-Category has no entry in the Layer field. All cards have a primary layer assignment.

### 4.4 Dual-aspect components

Some components have both quantitative and qualitative properties. The count of a component is an Economy property; the content or recorded state of a component is an Information property. These are separate, independently affectable properties:

| Component | Economy property | Information property |
|-----------|----------------|-------------------|
| Intel token | Count held by faction | Content written on token |
| Modifier card | Count held | What modifiers the card carries |
| Accord agreement | Whether an Accord exists | Recorded terms and obligations |

A card that adds an Intel token to the pool (STD.CA.5 Gather) is an Information card — the dominant design intent is intelligence acquisition, not resource accumulation. Token count is an Economy property of a held asset; card layer is classified by what the card's primary effect serves. A card that reveals the content of a token is an Information card. A card that introduces a token with falsified content (GHO.CA.5 Misdirection) is an Information card — the qualitative deception is the primary design intent, even though the Add primitive is also executed.

### 4.5 Accord is a known-narrow Economy subset

Whether an Accord exists between two factions is a public, countable fact → Economy. The recorded terms of an Accord are Information. Accord-specific design space has expanded materially since this decision was written: Art 06 §9 (signed off L191/L198/L205) defines a full clause vocabulary (six types including Lock, Alter, Transfer, Duration, Prohibition, Obligation) and a card-driven formation and manipulation model. The Economy classification for Accord existence still holds; the design space is no longer narrow.

### 4.6 Protect distributes to the target's layer

A Protect card belongs to the layer of its protected target — it is not a cross-layer function. The principle is established; individual card assignments below are pending full card development except where noted.

| Card | Protected target | Layer | Status |
|------|----------------|-------|--------|
| STD.CA.10 Protect | Covert operation difficulty | Resolution | ✅ Signed off |
| GUI.CA.1 Fortify Structure | Structure block | Territory | ✅ Signed off |
| ~~GHO.CA.3 Identity Blind~~ | ~~Action attribution~~ | ~~Information~~ | 🚫 Retired — redesigned S68. GHO.CA.3 is now **Dossier Breach** (Information — Reveal — IntelDeliverySlip). No longer a Protect card. |
| GHO.CA.4 Deep Cover | ~~Action attribution (permanent)~~ | Information | 📝 Design pass complete (v1.1) — redesigned S51. Taxonomy changed: now **Information — Remove — IntelToken** (permanently removes Ghost attribution record from rival's Intel token). See §5.2. Issues not yet resolved. |
| ~~STD.CA.11 Evidence Preservation~~ | ~~Written record~~ | ~~Information~~ | 🚫 Retired — redesigned S68. STD.CA.11 is now **Tort Interference** (Standard CovertOperation; locks a named Accord against voluntary dissolution). No longer a Protect card — taxonomy: Economy — Block — Accord agreement. |
| SYN.CA.4 Golden Parachute | Native resource | Economy | 📝 Design pass complete (v2.0, L185) — bribe mechanic; variable Capital declared at Dispatch; nullification is conditional on target's submitted ops. Issues resolved. Pending sign-off. |

### 4.7 Submission and Resolution are distinct layers

The original Action category covered blocking submissions, modifying costs, adjusting difficulty, and changing scope — two separate systems:

- **Submission** governs what enters the queue: costs, eligibility restrictions, blocks, operational scope
- **Resolution** governs how the queue resolves: the d100 threshold, difficulty, modifier application, outcome scale

A card that blocks an operation from being submitted (DIR.CA.1 Invoke Jurisdiction, DIR.CA.4 Sealed Border) is a Submission card. A card that changes the difficulty of an operation in the queue (GHO.PA.2 Signal Review Request) is a Resolution card.

### 4.8 Standing is an affectable consequence register

Public Standing and Portrait tracks record resolution outcomes across the session — they function as consequence registers. However, they are also independently affectable: cards can shift track values directly, independent of any underlying action resolving. This dual role (output register + independently affectable surface) warrants a dedicated layer.

Portrait is ARBITER-controlled (L84, 00a §5.1). Player-facing Standing cards affect Public Standing only.

### 4.9 React, Instant, and interrupt effects

React, Instant, and interrupt effects are an intentional play mechanic — trigger-based cards that fire automatically on publicly observable conditions. These mechanics are valid and in full scope for the game.

In the taxonomy, React/Instant/interrupt is a *timing classification*, not a Layer or Function. A card using this mechanic carries its own Layer — Function — Subject for its primary effect; the timing mechanism describes *when* the effect fires, not *what* it affects. These mechanics can appear across all layers:

- A card adds resources triggered by an opponent's resolved action → Economy — Add — Native resource (GUI.CA.2) [Recover retired S106 — reducible to Add + temporal context; see 04b-20]
- An Instant card that blocks a submission in-flight → Submission — Block — [target]
- An interrupt that reveals attribution when triggered → Information — Reveal — Action attribution

Because timing is a separate axis, React / Instant / interrupt cards are classified by their effect, not their trigger. The full mechanic treatment — trigger conditions, stack behavior, observability requirements — is in Art 03 §18 (React Card Rules).

### 4.10 Corrupt applies only to physically written or recorded values

Corrupt is classified in the Information layer. Scope is strict: applies only to values physically written or tracked in the paper prototype. Valid targets: Intel tokens (faction name only — see location constraint below), Accord agreements (terms written on document; named party on Accord form — L227), Target Profile (content within an operation bundle inside the dispatch case). Invalid: printed card text, marker positions (tracked by physical position, not written value), Chronicle (ARBITER narrative — not a mechanical game element), round-number field on Intel tokens (see below).

**Intel token location constraint (L222):** Intel tokens reside in the faction terminal (private zone — unreachable by an opposing card) or the ARBITER terminal (write-only by ARBITER). The only window where an opposing faction's Intel token is publicly accessible is when placed on a Public Act as payment (Beat 0 through Beat 4 PA resolution). Only tokens in that public-placement window are valid Corrupt targets. Own-faction modification of privately held tokens constitutes falsification of game state and is prohibited. Round-number field is additionally blocked by 7.2b: round number records the token's committed validity state (when it was created); altering it retroactively modifies that committed state.

### 4.11 Redirect unifies Convert and Transfer

Convert (changing ownership of a board element) and Transfer (moving resources between factions) are both instances of Redirect. Convert is Territory — Redirect. Transfer is Economy — Redirect.

### 4.12 No multi-Quarter temporary effects

Card effects use exactly one of four valid duration types: **Immediate** (resolved at beat; no lingering marker), **Transient** (removed at end of current Month), **Seasonal** (removed at end of current Quarter / Phase 21), or **Permanent** (persists for the remainder of the session until a named action or condition removes it). No card creates a state that expires after a defined number of Quarters. *Locked: Art 04 §5 P6 and P19 (formerly 00a R21). See Art 00a §3.1 — canonical duration definitions.*

### 4.13 ARBITER-reveal is outside 10.1 (L225)

ARBITER may reveal any content from its own domain — the covert resolution grid, target profiles, modifier cards in the Beat 3 queue, tableau contents — without triggering 10.1's stake model. ARBITER's disclosure is an exercise of its own knowledge as the game's information authority, not a compulsion of a faction player's disclosure choice. The target faction is not making a disclosure decision when ARBITER reads from its own domain.

Portrait track is the only prohibited ARBITER reveal target (00a §5.1 — Portrait is ARBITER-controlled and never disclosed as a product of any card or script).

10.1's stake model applies only to cards that compel or incentivize a faction player to reveal information they hold privately.

### 4.14 Design note — Paper vs Electronic ARBITER knowledge gap

In the paper prototype, ARBITER knows what happened (actions taken, board state, resolved effects) but does not know what is being considered (cards held, options available, choices not made). This is consistent with ARBITER's narrative character — ARBITER reads signals that have entered the causal chain; intent before action is not yet signal.

In the electronic version, ARBITER would have access to hand contents and could generate Chronicles that include patterns of restraint alongside patterns of action. The unchosen path is also story. Flag for PM04 — Future Phases.

---

## 5. Card Taxonomy Index

*Card definitions are in Artifact 04. This index provides Layer — Function — Subject — Primitive Verb(s) assignments for all cards as a design reference. Use this table to identify coverage gaps and duplications.*

### 5.1 Column Definitions

**Layer** — which game system does this card affect? See §4.2 for visibility and full scope definitions.

| Layer | Scope |
|-------|-------|
| Territory | The influence landscape: presence tokens, structures, control flags, spatial markers |
| Economy | Quantitative holdings: native resources, token counts, card counts, Accord existence |
| Information | Qualitative content: token content, written records, attribution, reconnaissance |
| Submission | What enters the resolution queue: costs, eligibility, blocks, scope |
| Resolution | The d100 system: threshold, modifier stack, difficulty, outcome scale |
| Standing | Reputation tracks: Public Standing and Portrait |

**Function** — what does the card do to its subject?

| Function | Definition | Maps to Primitive Verb(s) |
|----------|------------|--------------------------|
| Add | Brings a new element into active play from supply or off-board | Add |
| Remove | Takes an element out of active play | Remove |
| Redirect | Changes ownership, destination, or allegiance of an element | Move |
| Modify | Alters a cost, value, or attribute without changing the element's fundamental state | — (abstract constraint) |
| Protect | Preserves the current state of a target against a named change | — (meta-constraint) |
| Block | Prevents another action from being initiated or resolving | — (meta-constraint) |
| Copy | Duplicates another action's effect chain with a new initiating subject | Invoke |
| Reveal | Makes hidden information visible to a named audience | Reveal |
| ~~Conceal~~ | **Retired S107 (L224)** — Concealment is a structural system behavior implemented by physical game components (dispatch case, faction terminal, ARBITER screen). It is not a card-triggerable function. 7.2a prohibits hidden state on board surface. Attribution concealment for covert ops is structural by default (all covert ops are anonymous until Discovered). No card Conceal function will be designed. | — |
| Shift | Moves a track value (Portrait, Public Standing) up or down | Move |
| Corrupt | Alters a physically written or recorded value on a component | Corrupt |

**Primitive Verb(s)** — the physical verb(s) from §3.1 that execute this card's effect on a component. `—` indicates the card operates as a constraint or modifier on another action rather than directly executing a physical primitive. This is the bridge between the card design layer and the physical action model.

**Modifier Card Scope** — Modifier cards are excluded from Layer — Function — Subject taxonomy (§9). They do not produce game-state primitives; they alter the parameters of primitives initiated by taxonomy cards. Their design space spans all six layers — any valid action from any layer can be the host action for a Modifier. The design question is not "which layer?" but "what host action does this require, and what parameter does it change?" Parameters a Modifier can alter include difficulty, cost, threshold, scope, outcome, timing, or validity of the host action.

React and Instant are timing sub-functions within the Modifier card type — they describe when a Modifier fires, not what it does. React fires automatically when a named publicly-observable condition is met (Art 04 §5 Principle 5); Instant is played actively during a defined window. Both are specified in Artifact 04 card specs. A Timing column may be added to §5.2 when the full modifier timing model is locked.

### 5.2 Card Index

*Status key: ✅ Signed off — canonical, use for gap analysis. 📝 Draft — designed but not signed off. ⬜ Not yet designed. 🚫 Retired.*

| Card ID | Name | Status | Layer | Function | Subject | Primitive Verb(s) |
|---------|------|--------|-------|----------|---------|-------------------|
| STD.CA.1 | Build Structure | ✅ | Territory | Add | Structure block | Add |
| STD.CA.2 | Demolish | ✅ | Territory | Remove | Structure block | Remove |
| STD.CA.3 | Campaign | ✅ | Territory | Add | Presence token | Add |
| STD.CA.4 | Undermine | ✅ | Territory | Remove | Presence token | Remove |
| STD.CA.5 | Gather | ✅ | Information | Add | Intel token | Add |
| STD.CA.6 | Broadcast Interference | ✅ | Submission | Modify | Political act (cost) | — |
| STD.CA.7 | Amplify | ✅ | Resolution | Modify | Political act (outcome scale) | — |
| STD.CA.8 | Buy Influence | ✅ | Territory | Add | Presence token | Add |
| STD.CA.9 | Fund | ✅ | Economy | Redirect | Native resource | Move |
| STD.CA.10 | Protect | ✅ | Resolution | Protect | Covert operation (difficulty) | — |
| GUI.CA.1 | Fortify Structure | ✅ | Territory | Protect | Structure block | — |
| GUI.CA.2 | Materials Acquisition | ✅ | Economy | Add | Native resource | Add | *(function: Recover → Add, S106 — 04b-20; Art 04 spec fix pending 04-n103)*
| GUI.CA.3 | Foundation Rights | ✅ | Territory | Add | Presence token | Add |
| GUI.CA.4 | Construction Crew | ✅ | Submission | Remove Restriction | Covert operation (presence requirement) | — |
| GUI.CA.5 | Infrastructure Yield | ✅ | Economy | Add | Native resource | Add |
| GHO.CA.1 | Pattern Match | ✅ | Submission | Copy | Covert operation (full) | Invoke |
| GHO.CA.2 | Intercept | 📝 | Information | Reveal | CovertOperation | Reveal |
| GHO.CA.3 | Dossier Breach | 📝 | Information | Reveal | IntelDeliverySlip | Reveal |
| GHO.CA.4 | Deep Cover | 📝 | Information | Remove | IntelToken | Remove |
| GHO.CA.5 | Misdirection | 📝 | Information | Add | Intel token (corrupt content) | Add + Corrupt |
| DIR.CA.1 | Invoke Jurisdiction | 📝 | Submission | Block | Covert operation (STD.CA.1, STD.CA.3) | — |
| DIR.CA.2 | Detain | 📝 | Territory | Move | Deployment marker | Move | *(taxonomy corrected S107 L226: success operation is game.move() to Detention zone; Remove was incorrect — Remove = return to supply; Detention zone is an active play area on Directorate's tableau. Art 04 spec function field correction tracked under 04-n105)* |
| STD.CA.11 | Tort Interference | 📝 | Information | Corrupt | Accord | Corrupt |
| DIR.CA.3 | Surveillance Placement | 📝 | Information | Reveal | CovertOperation | Reveal |
| DIR.CA.4 | Tactical Redirection | 📝 | Territory | Move | PresenceToken | Move |
| NET.CA.1 | Leak | 📝 | Information | Reveal | District | Reveal |
| NET.CA.2 | Disclosure Loop | 📝 | Economy | Add | Exposure | Add |
| NET.CA.3 | Breaking News | 📝 | Information | Reveal | CovertOperation | Reveal |
| NET.CA.4 | Network Cascade | 📝 | Submission | Modify | PoliticalAct | — |
| NET.CA.5 | Community Anchor | 📝 | Territory | Add | Presence token | Add |
| SYN.CA.1 | Leveraged Acquisition | 📝 | Economy | Add | Native resource | Add |
| SYN.CA.2 | Short the Market | 📝 | Economy | Remove | Native resource | Remove |
| SYN.CA.3 | Hostile Acquisition | 📝 | Territory | Redirect | Structure block | Move |
| SYN.CA.4 | Golden Parachute | 📝 | Economy | Protect | Native resource | — |
| SYN.CA.5 | Regulatory Capture | 📝 | Submission | Block | Named action type | — |
| GHO.CA.6 | Synthesize | 📝 | Economy | Add | IntelToken | Add |
| NET.CA.6 | Sacrifice | 📝 | Economy | Add | IntelToken | Add |
| SYN.CA.6 | Parasitic | 📝 | Economy | Add | IntelToken | Add |
| STD.CA.12 | Absolute Compromise | 📝 | Submission | Block | CovertOperation | — |
| NET.PA.3 | Live Coverage | 📝 | Information | Reveal | FactionHand | Reveal |
| SYN.CA.7 | Corporate Blackmail | 📝 | Economy | Redirect | NativeResource | Move |
| DIR.CA.5 | Sanctioned Raid | 📝 | Territory | Remove | PresenceToken | Remove |
| — | Source Substitution | 📝 | Information | Corrupt | Intel token | Corrupt |
| — | Backdate | 🚫 BLOCKED | Information | — | — | — | *L222: (1) Location constraint — Intel token in private terminal zone unreachable by opposing card; only publicly placed tokens (PA payment window) are valid Corrupt targets. (2) 7.2b — round-number records committed validity state; altering it is retroactive modification. §4.10 revised. Art 04 spec: BLOCKED pending redesign (04-n103).* |
| — | Field Verification | 🚫 BLOCKED | Information | — | Intel token | — | *7.2b violation: mechanic alters committed token age field retroactively. Fundamental redesign required. G-ext id retired. Art 04 spec: BLOCKED pending redesign (04-n103).* |
| GUI.CA.6 | Labor Contract | 📝 | Economy | Add | NativeResource | Add | *(function: Recover → Add, S106 — 04b-20; card_id GUI.CA.6 assigned; Art 04 spec fix pending 04-n103)*
| — | Station | 📝 | Information | Add | IntelToken | Add |
| — | Full Take | 📝 | Information | Add | IntelToken | Add |
| — | SCIF | 📝 | Information | Add | DebriefActionCard | Add |
| — | Flip | 📝 | Economy | Add | FactionNativeResource | Add |
| — | Signals Analysis | 📝 | Information | Reveal | ClassifiedDirective | Reveal |
| — | Entry/Exit Controls | 📝 | Territory | Block | DeploymentMarker | — |
| — | Regulatory Downgrade | 🚫 BLOCKED | Territory | — | — | — | *L223: InfluenceTier is not a targetable component — tier is derived from influence token counts, not a placed or written value. Only board state changes (token add/remove) can affect tier. 9.1 prohibits direct income modification by card. Fundamental redesign required (04-n104).* |
| — | Regulatory Freeze | 🚫 BLOCKED | Territory | — | — | — | *L223: Same subject violation — InfluenceTier not a targetable component. Additionally, Block targets actions (not derived states); Block\|InfluenceTier is a subject mismatch. Fundamental redesign required (04-n104).* |
| — | Land Title | 📝 | Territory | Add | StructureBlock | Add |
| — | Hostile Takeover | 📝 | Territory | Add | PresenceToken | Add |
| — | Accord Transfer | 📝 | Economy | Corrupt | AccordCard | Corrupt | *(taxonomy corrected S107 L227: party-name replacement is physical alteration of written record on Accord form — Corrupt, not Redirect. Blocked on Art 06 for implementation details.)* |
| — | Disinformation Campaign | 📝 | Standing | Shift | Public Standing | Move |
| — | Standing Injunction | 📝 | Submission | Block | Political act | — |
| — | Disprove | 📝 | Economy | Remove | Intel token | Remove |
| — | Intel Extraction | 📝 | Economy | Redirect | Intel token | Move |
| — | Modifier Raid | 📝 | Economy | Redirect | Modifier card | Move |
| C40A | Reputational Strike | 📝 | ModifierCard — taxonomy excluded §5.1 | — | — | — |
| — | Accord Leverage | 📝 | ModifierCard — taxonomy excluded §5.1 | — | — | — |
| — | Overture | 📝 | ModifierCard — taxonomy excluded §5.1 | — | — | — |
| STD.PA.1 | Open Operations | 📝 | Territory | Add | Presence token | Add |
| STD.PA.2 | Disputed Claim | 📝 | Territory | Remove | Presence token | Remove |
| STD.PA.3 | Public Commission | 📝 | Territory | Add | Structure block | Add |
| STD.PA.4 | Public Censure | 📝 | Standing | Shift | Public Standing (−) | Move |
| STD.PA.5 | On the Record | 📝 | Information | Reveal | Action attribution | Reveal |
| STD.PA.6 | Economic Sanction | 📝 | Economy | Remove | Native resource | Remove |
| STD.PA.7 | Public Address | 📝 | Standing | Shift | Public Standing (+) | Move |
| STD.PA.8 | Table an Accord | 📝 | Economy | Add | Accord agreement | Add |
| GUI.PA.1 | Civic Works Mandate | 📝 | Territory | Add | Structure block | Add |
| GUI.PA.2 | Infrastructure Bond | 📝 | Economy | Add | Accord agreement | Add |
| DIR.PA.1 | Regulatory Override | ⛔ BLOCKED | — | — | Cost modification is not a physical verb; "cost" is not a component attribute. Card targets action cost for all Add·PresenceChip operations — requires new component + ARBITER overhead. Needs redesign. See PM05 04-n99. | — |
| DIR.PA.2 | Convene an Inquiry | 📝 | Information | Add | Intel token | Add |
| NET.PA.1 | Public Disclosure | 📝 | Information | Reveal | Action attribution | Reveal |
| NET.PA.2 | Community Rally | 📝 | Territory | Add | Presence token | Add |
| SYN.PA.1 | Acquisition Offer | 📝 | Territory | Redirect | Presence token | Move |
| SYN.PA.2 | Public Dividend | 📝 | Economy | Add | Native resource (conditional) | Add |
| GHO.PA.1 | Publish Analysis | 📝 | Information | Reveal | Action attribution | Reveal |
| GHO.PA.2 | Signal Review Request | 📝 | Resolution | Modify | Covert operation (difficulty) | — |

---

## 6. Coverage Analysis — Gaps and Concentrations

### 6.1 Unused taxonomy combinations

The following combinations exist in the taxonomy but have no current card. Layer and Function definitions are included to prompt the core design question: *is there a narrative reason to perform this action in this game system?* If yes, it is a candidate for card development.

---

**Layer: Territory** — *The influence landscape: presence tokens, structures, control flags, spatial markers*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Redirect | Changes ownership, destination, or allegiance of an element | Structure | Low | Transfer structure faction — SYN.CA.3 partially covers |
| ~~Recover~~ | **Retired S106** (04b-20) — reducible to Add + React context; 7.2b violation for removed-from-game elements | Presence token | — | Guild candidate redesigned as GUI.MOD.1 Territory\|Add\|PresenceToken React. |
| ~~Recover~~ | **Retired S106** | Structure | N/A | Consequence of 00a 7.2b — committed board states cannot be nullified. Demolished structures are gone; reconstruction = Territory — Add — Structure block (STD.CA.1). |

**Layer: Economy** — *Quantitative holdings: native resources, token counts, card counts, Accord existence*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Remove | Takes an element out of active play | Intel token | Low | Strip opponent Intel tokens. Addressed: Disprove (📝) |
| Remove | Takes an element out of active play | Modifier card | Medium | Strip opponent modifier cards |
| Remove | Takes an element out of active play | Accord agreement | High | Break Accord covertly — important missing mechanic |
| ~~Recover~~ | **Retired S106** — spent modifier card re-acquisition is Add from supply, not Recover; 7.2b applies | Modifier card | — | Not a valid design target. |
| Redirect | Changes ownership, destination, or allegiance of an element | Accord agreement | High | "Small print" mechanic — Syndicate doctrine. **Unaddressed (L227):** Accord Transfer reclassified as Economy\|Corrupt\|AccordCard — party-name replacement is written-value corruption, not ownership redirect. Economy\|Redirect\|AccordAgreement remains an open coverage gap. |
| Redirect | Changes ownership, destination, or allegiance of an element | Modifier card | Low | Partially covered by trade rules |

**Layer: Submission** — *What enters the resolution queue: costs, eligibility, blocks, scope*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Copy | Duplicates another action's effect chain with a new initiating subject | Political act | Low | Copy opponent political act |
| Copy | Duplicates another action's effect chain with a new initiating subject | Subset only | Medium | Copy target or effect only — Ghost doctrine. ⚠️ Partial-copy mechanism needed in action model |

**Layer: Information** — *Qualitative content: token content, written records, attribution, reconnaissance*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Reveal | Makes hidden information visible to a named audience | Faction hand | High | `Faction hand` (id=94) registered S48. Covered: Modifier card ✅, Countermeasure card ✅. Pre-submission cards (Political act, Covert operation) not in play at intelligence beats — hand-targeting mechanic applies uniformly to all held types. Addressed: NET.PA.3 Live Coverage (📝). See ⚠️ below |
| Reveal | Makes hidden information visible to a named audience | Classified directives | Low | Very high impact — use carefully. Addressed: Signals Analysis (📝) |
| Reveal | Makes hidden information visible to a named audience | Modifier cards held | Medium | Disclose individual modifier card contents |
| Reveal | Makes hidden information visible to a named audience | Named faction only | High | Targeted disclosure — Ghost intelligence delivery. ⚠️ Target-scope/filter system needed |
| Corrupt | Alters a physically written or recorded value on a component | Intel token | High | Falsify Intel token content. Location constraint (L222): token must be in public-placement window (on PA as payment) — private terminal tokens unreachable. Addressed: Source Substitution (📝, faction-name field only); Backdate (🚫 BLOCKED L222 — round-number additionally prohibited by 7.2b). |
| Corrupt | Alters a physically written or recorded value on a component | Accord agreement (terms) | High | Alter Accord terms — Syndicate doctrine. Addressed: STD.CA.11 Tort Interference (📝). |
| Corrupt | Alters a physically written or recorded value on a component | AccordCard (named party) | High | Replace named party on Accord form — Syndicate doctrine. Addressed: Accord Transfer (📝, pending Art 06 — L227). |

**Layer: Standing** — *Reputation tracks: Public Standing and Portrait*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Shift | Moves a track value up or down | ~~Chorus Portrait (primary covert)~~ | — | **Retired (L84, 00a R01).** ARBITER sole mover of Portrait. Ghost doctrine gap: new primary covert effect needed — see PM05 04-11 |
| Shift | Moves a track value up or down | Public Standing (primary covert) | High | Standing as primary covert effect — Network doctrine. Addressed: Disinformation Campaign (📝) |

---

*React / Instant / interrupt timing is a separate design dimension not captured in this table — cards with these triggers carry their own Layer/Function/Subject for the primary effect. React-triggered card design space to be tracked once the timing mechanic is fully specified. See §4.9 and §10.*

*⚠️ Two subjects require schema extension before primitives can be modeled: **Named faction only** (target-scope/filter system) and **Subset only** (partial-copy mechanism).*

*🔬 **Research flag (S48 — agy):** Established card games (Netrunner, espionage genre) use a distinct **Inspect** function — private read of a face-down card without making it public. Currently merged into `Reveal` (which implies public disclosure). If Inspect is added to §5.1, candidate gaps: Information | Inspect | Intel token; Information | Inspect | Covert operation. Flag for §5.1 review before actioning.*

### 6.2 Overrepresented combinations

| Layer | Function | Subject | Cards | Issue |
|-------|----------|--------|-------|-------|
| Territory | Add | Presence token | STD.CA.3, STD.CA.8, GUI.CA.3, NET.CA.5, STD.PA.1 | 5 cards — Standard (×2), Guild, Network, Political Act. All five must remain mechanically distinct; differentiation is by cost, restriction, and doctrine alignment. |
| Information | Reveal | CovertOperation | GHO.CA.2, DIR.CA.3, NET.CA.3 | 3 faction cards (Ghost, Directorate, Network). Subject is identical across all three; differentiation falls entirely to trigger conditions, target restrictions, and disclosure scope in card specs. |
| Information | Reveal | (all subjects) | GHO.CA.2, GHO.CA.3, DIR.CA.3, NET.CA.1, NET.CA.3, NET.PA.3 | 6 Reveal cards; Ghost holds 2, Network holds 3, Directorate holds 1. Reveal is the most concentrated function in the Information layer. Standard has no faction Reveal cards — only Political Acts (STD.PA.5, NET.PA.1, GHO.PA.1). |

### 6.3 DB-Backed Gap Analysis (S47)

The DB primitive model generates two gap views that serve as the operative legalization audit tools. Methodology and decision tracking live in Art 03 §22 (Physical Action Taxonomy appendix) — that is the canonical location for view definitions and legalization status.

**`v_unlegislated_by_trigger`** — Faction-initiated (subject, verb, component) tuples with no legalization ruling. Each row requires a permit / prohibit / defer decision before the corresponding Art 03 procedure can be written or explicitly closed.

**`v_unlegislated_primitives`** — Beat-specific gaps. The Faction-at-M3-Beat-4 subset is the most actionable design space for new card effects.

Live view results are in the DB — query directly for current state. Results captured here as of S47 are superseded and not maintained; do not use as a gap reference.

---

## 7. Faction Coverage Matrix

*Rebuilt S104 from Art 04 card data. Standard column = faction=All cards and Political Acts (P-prefix). Faction columns = faction-specific cards only.*

| Layer | Function | Subject | Standard | Guild | Ghost | Directorate | Network | Syndicate |
|-------|----------|---------|----------|-------|-------|-------------|---------|-----------|
| **Territory** | | | | | | | | |
| | Add | Presence token | STD.CA.3, STD.CA.8 | GUI.CA.3 | — | — | NET.CA.5 | — |
| | Add | Structure block | STD.CA.1 | — | — | — | — | — |
| | Remove | Presence token | STD.CA.4 | — | — | DIR.CA.5 | — | — |
| | Move | Deployment marker | — | — | — | DIR.CA.2 | — | — |
| | Remove | Structure block | STD.CA.2 | — | — | — | — | — |
| | Move | Presence token | — | — | — | DIR.CA.4 | — | — |
| | Redirect | Presence token | SYN.PA.1 | — | — | — | — | — |
| | Redirect | Structure block | — | — | — | — | — | SYN.CA.3 |
| | Protect | Structure block | — | GUI.CA.1 | — | — | — | — |
| **Economy** | | | | | | | | |
| | Add | Native resource | SYN.PA.2 | GUI.CA.2, GUI.CA.5, GUI.CA.6 | — | DIR.CA.6 | — | SYN.CA.1 |
| | Add | Intel token | — | — | GHO.CA.6 | — | NET.CA.6 | SYN.CA.6 |
| | Add | Accord agreement | STD.PA.8, GUI.PA.2 | — | — | — | — | — |
| | Add | Exposure | — | — | — | — | NET.CA.2 | — |
| | Remove | Native resource | STD.PA.6 | — | — | — | — | SYN.CA.2 |
| | Remove | Intel token | — | — | — | — | — | — |
| | Remove | Accord agreement | — | — | — | — | — | — |
| | Redirect | Native resource | STD.CA.9 | — | — | — | — | SYN.CA.7 |
| | Redirect | Accord agreement | — | — | — | — | — | — |
| | Corrupt | AccordCard (named party) | — | — | — | — | — | AccordTransfer (📝) |
| | Protect | Native resource | — | — | — | — | — | SYN.CA.4 |
| **Information** | | | | | | | | |
| | Add | Intel token | STD.CA.5, DIR.PA.2 | — | GHO.CA.5 | — | — | — |
| | Reveal | CovertOperation | — | — | GHO.CA.2 | DIR.CA.3 | NET.CA.3 | — |
| | Reveal | IntelDeliverySlip | — | — | GHO.CA.3 | — | — | — |
| | Reveal | District | — | — | — | — | NET.CA.1 | — |
| | Reveal | FactionHand | — | — | — | — | NET.PA.3 | — |
| | Reveal | Action attribution | STD.PA.5, NET.PA.1, GHO.PA.1 | — | — | — | — | — |
| | Remove | Intel token | — | — | GHO.CA.4 | — | — | — |
| | Corrupt | Accord | STD.CA.11 | — | — | — | — | — |
| | Corrupt | Intel token | — | — | — | — | — | — |
| **Submission** | | | | | | | | |
| | Block | CovertOperation | STD.CA.12 | — | — | DIR.CA.1 | — | — |
| | Block | Named action type | — | — | — | — | — | SYN.CA.5 |
| | Block | Political act | — | — | — | DIR.PA.1 ⛔ | — | — |
| | Modify | Political act | STD.CA.6 | — | — | — | NET.CA.4 | — |
| | Copy | CovertOperation | — | — | GHO.CA.1 | — | — | — |
| | Remove Restriction | CovertOperation | — | GUI.CA.4 | — | — | — | — |
| **Resolution** | | | | | | | | |
| | Modify | Outcome scale | STD.CA.7 | — | — | — | — | — |
| | Modify | Difficulty | GHO.PA.2 | — | — | DIR.CA.8 | — | — |
| | Protect | CovertOperation | STD.CA.10 | — | — | — | — | — |
| **Standing** | | | | | | | | |
| | Shift | Public Standing | STD.PA.4, STD.PA.7 | — | — | DIR.CA.7 | NET.CA.7 | — |

---

## 8. Design Recommendations by Faction

These recommendations inform the redesign decisions D-04-02 through D-04-05 in Artifact 04 §16.

### 8.1 Ghost — Priority redesign targets

Current Ghost set (S104): GHO.CA.1 (Submission|Copy|CovertOp), GHO.CA.2 (Information|Reveal|CovertOp), GHO.CA.3 (Information|Reveal|IntelDeliverySlip), GHO.CA.4 (Information|Remove|IntelToken), GHO.CA.5 (Information|Add|IntelToken), GHO.CA.6 (Economy|Add|IntelToken). Attribution-protection duplication resolved by redesign; Ghost's suite now spans generation (GHO.CA.5), interception (GHO.CA.2), delivery tracking (GHO.CA.3), and removal (GHO.CA.4) — doctrinally coherent. Portrait pathway remains closed (L84, 00a R01); see PM05 04-11.

**High priority:**
1. **Information — Reveal — Named faction:** Ghost delivers targeted intelligence to a specific faction privately rather than the whole table. *Targeted intelligence disclosure that strengthens relationships without public exposure.* ⚠️ Target-scope/filter system needed before this can be specified.
2. **Submission — Copy — Subset:** Ghost should have a partial copy card — copy only the target (apply your own operation to the same district as named faction) without replicating the full cost and effect. ⚠️ Partial-copy mechanism needed in action model.

### 8.2 Directorate — Priority redesign targets

Current Directorate set (S104): DIR.CA.1 (Submission|Block|CovertOp), DIR.CA.2 (Territory|Move|DeploymentMarker — taxonomy corrected S107 L226), DIR.CA.3 (Information|Reveal|CovertOp), DIR.CA.4 (Territory|Move|PresenceToken), DIR.CA.5 (Territory|Remove|PresenceToken). Submission|Block concentration resolved — DIR.CA.4's redesign removed the second Block card. Effective Block count: DIR.CA.1 only; DIR.PA.1 (⛔ BLOCKED, PM05 04-n99) unresolved.

**High priority:**
1. **Economy — Add — Native resource (Mandate):** ✅ DIR.CA.6 Institutional Audit (S106). Beat 3 d100 threshold 50; yield = count of active Directorate Permanents in target ring; restriction chip count > 1.
2. **Standing — Shift — Public Standing (primary covert):** ✅ DIR.CA.7 Institutional Brief (S106). Beat 3 d100 threshold 50; PS yield = count of active Directorate Permanents in target ring; same architecture as DIR.CA.6. Mechanism: closed-channel circulation of institutional record — covert authorship, public confidence signal.

**Medium priority:**
3. **Resolution — Modify — Difficulty (increasing, against all factions):** ✅ DIR.CA.8 Enhanced Scrutiny (S106). Beat 2 Automatic; ARBITER places −15 Modifier tokens on each Beat 3 row targeting district; all factions including Directorate.

### 8.3 Network — Priority redesign targets

Current Network set (S104): NET.CA.1 (Information|Reveal|District), NET.CA.2 (Economy|Add|Exposure), NET.CA.3 (Information|Reveal|CovertOp), NET.CA.4 (Submission|Modify|PoliticalAct), NET.CA.5 (Territory|Add|PresenceToken), NET.CA.6 (Economy|Add|IntelToken), NET.PA.3 (Information|Reveal|FactionHand). NET.CA.2's redesign to Economy|Add|Exposure resolved the prior doctrinal contradiction. Network now holds three Reveal cards (NET.CA.1, NET.CA.3, NET.PA.3) across distinct subjects — mechanical differentiation between them must be enforced in card specs.

**High priority:**
1. **Standing — Shift — Public Standing (primary covert):** ✅ NET.CA.7 Ground Signal (S106). Beat 3 d100 threshold 50; success +1 PS; restriction IL ≤ Established (Dominant excluded — no outreach needed); successcrit +1 chip in target district + +1 PS additional. Doctrinal grounding: existing street presence made legible without announcement.
2. **Territory — Add — Presence token (React trigger):** ✅ Signal Break (S106). ModifierCard / React; trigger = PA success causing board state change (influence or structure, + or −) in district; target district fixed by trigger; Exposure×1; d100 threshold 50; success +1 chip; successcrit +1 PS; fail no effect; failcrit −1 PS. Full spec written to Art 04 §11.8. Schema pass pending (04-n4).

**Medium priority:**
3. **Consolidate NET.CA.1 and NET.CA.3:** NET.CA.1 reveals District-level data; NET.CA.3 reveals CovertOperation. Subjects are distinct — if both are retained, card specs must enforce clear mechanical differentiation; if consolidated, the broader subject scope needs defining.

### 8.4 Syndicate — Priority redesign targets

Current Syndicate set (S104): SYN.CA.1 (Economy|Add|NativeResource), SYN.CA.2 (Economy|Remove|NativeResource), SYN.CA.3 (Territory|Redirect|StructureBlock), SYN.CA.4 (Economy|Protect|NativeResource), SYN.CA.5 (Submission|Block|NamedActionType), SYN.CA.6 (Economy|Add|IntelToken), SYN.CA.7 (Economy|Redirect|NativeResource). Economy depth is Syndicate's defining characteristic — 5 of 7 cards are Economy layer. SYN.CA.6 provides an intel foothold within the Economy layer; Syndicate still has no direct Information-layer capability.

**High priority:**
1. **Information — Corrupt — Accord agreement:** Alter the recorded terms of an existing Accord. *"The Syndicate may alter one numeric value in any registered Accord — changing a resource amount, duration, or threshold. The alteration is physically made to the Accord document. Both parties notified in case."* Requires ARBITER to manage Accord document integrity.
2. **Economy — Redirect — Accord agreement:** The "small print" mechanic. **Unaddressed (L227):** Accord Transfer reclassified as Economy|Corrupt|AccordCard — party-name replacement is alteration of a written record on the Accord form, not a redirect of ownership. Economy|Redirect|AccordAgreement remains an open coverage gap — no card addresses the mechanic of transferring Accord *obligations* between factions as a redirect operation.
3. **Economy — Corrupt — AccordCard (named party):** ✅ Addressed by Accord Transfer (📝, L227 — pending Art 06 implementation).
3. **Information — Reveal — Intel tokens held:** Economic intelligence. *"The Syndicate names a faction. ARBITER announces the count (not content) of Intel tokens that faction holds. The Syndicate may offer to purchase one token from the named faction at 3 Capital — the named faction may accept or decline."*

### 8.5 Guild — Priority design targets

Current Guild set (S106): GUI.CA.1 (Territory|Protect|StructureBlock), GUI.CA.2 (Economy|Add|NativeResource — reclassified from Recover, S106), GUI.CA.3 (Territory|Add|PresenceToken), GUI.CA.4 (Submission|RemoveRestriction|CovertOp), GUI.CA.5 (Economy|Add|NativeResource), GUI.CA.6 Labor Contract (Economy|Add|NativeResource — id assigned S106, function reclassified from Recover). Standard STD.CA.1 (Build Structure) carries a Guild affinity waiving the district-native cost. Territory and Economy coverage is strong — aligned with Guild doctrine of permanence and structural investment. Art 04 spec fixes for GUI.CA.2 and GUI.CA.6 pending 04-n103.

**High priority:**
1. **Territory — Add — PresenceToken (React):** GUI.MOD.1 Return to Site (S106 stub). Originally Territory|Recover|PresenceToken — Recover retired S106 (04b-20): reducible to Add + React context; 7.2b prohibits retroactive board state reversal. Card is Territory|Add|PresenceToken React; trigger = Guild chip removed from district. Full spec pending 04-n102 (Modifier schema).

**Low priority:**
2. **Information — Any:** Guild has zero information capability. Doctrinally consistent — Guild is visible and structural, not intelligence-oriented. Structural reconnaissance (knowing what's built where) could give Guild an intel-adjacent capability without contradicting doctrine. Not a priority until Territory|Recover|PresenceToken is designed.

---

## 9. Standalone Card Types — Taxonomy Exclusions

The following card types are excluded from the Layer — Function — Subject taxonomy. They are not game-state actions targeting a specific game layer — they are meta-actions or structural components that operate on the play procedure rather than the game state.

**Modifier cards** — Excluded. Modifier cards modify the parameters of an action rather than targeting a game layer directly. They may be played as interrupts during battle, triggered as React (firing automatically when a named publicly-observable condition is met — not submitted in the standard action sequence), or used to fund a burst play. Their effect — whether against a card, a board state, a resource, or any valid react/instant target — is mediated by the action or condition they modify. React is a timing sub-function within the Modifier card type, not a standalone card type. Modifier cards carry no Layer — Function — Subject fields.

**Emergency Response cards** — Excluded. Trigger-based, pre-staged cards with fixed effects. Not submitted in dispatch cases or declared in the standard action sequence. The penultimate action available to a faction before Apex fires.

*Source: Session 28 design note. Consistent with L115 (Art 04 owns all card design; card type determines scope, not taxonomy category).*

---

*End of Artifact 04b — Action Taxonomy & Design Analysis v1.7*
