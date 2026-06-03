# 04b — ACTION TAXONOMY & DESIGN ANALYSIS
## THE SIGNAL P1 — Paper Prototype

**Version:** 1.6  
**Status:** ✅ Signed Off — S48  
**Last Updated:** 2026-05-29  
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
| §3.3 | [Primitive Action Model — Database-Backed Analysis](#33-primitive-action-model--database-backed-analysis-s47) |
| §4 | [Card Design Layer — Key Decisions](#4-card-design-layer--key-decisions) — rationale for Layer/Function framework; six game layers |
| §5 | [Card Taxonomy Index](#5-card-taxonomy-index) — Layer, Function, Subject, Primitive Verb per card |
| §6 | [Coverage Analysis — Gaps and Concentrations](#6-coverage-analysis--gaps-and-concentrations) |
| §7 | [Faction Coverage Matrix](#7-faction-coverage-matrix) |
| §8 | [Design Recommendations by Faction](#8-design-recommendations-by-faction) |
| §9 | [Standalone Card Types — Taxonomy Exclusions](#9-standalone-card-types--taxonomy-exclusions) |

---

## 3. Physical Action Taxonomy

Every game action in The Signal resolves as a sequence of one or more physical primitives — discrete operations a human hand can perform on a game component. This section defines those primitives and their valid subjects: the seven physical verbs and the components each one can act on.

### 3.1 Physical Action Verbs

| Verb | Primitive | Definition |
|------|-----------|------------|
| **Add** | Place | A component enters active play from supply or off-board |
| **Remove** | Remove | A component exits active play to supply or off-board |
| **Move** | Remove + Place | A component relocates from one on-board location to another |
| **Reveal** | Transform | A component's face or contents become visible to named recipients |
| **Conceal** | Transform | A component is placed or returned face-down or closed |
| **Flip** | Transform | A component's physical orientation is changed — not an information state change |
| **Corrupt** | Transform | A physically written or recorded value on a component is altered |

*Every game action is a sequence of one or more of these primitives: Remove → Transform? → Place. The human hand is the implicit intermediary — not modeled.*

---

### 3.2 Component × Verb Matrix

| Component | Add | Remove | Move | Reveal | Conceal | Flip | Corrupt |
|-----------|-----|--------|------|--------|---------|------|---------|
| Accord agreement | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Activity marker | ✓ | ✓ | ✓ | — | — | — | — |
| ARBITER Dominance Marker | ✓ | ✓ | ✓ | — | — | — | — |
| Classified directives | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Control flag | ✓ | ✓ | ✓ | — | — | — | — |
| Covert operation | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Deployment marker | ✓ | ✓ | ✓ | — | — | ✓ | — |
| Dispatch case | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Dispatch token | ✓ | ✓ | ✓ | — | — | — | — |
| Established marker | ✓ | ✓ | ✓ | — | — | — | — |
| Faction order marker | ✓ | ✓ | ✓ | — | — | — | — |
| Intel token | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Modifier card | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Modifier token | ✓ | ✓ | ✓ | — | — | — | — |
| Native resource | ✓ | ✓ | ✓ | — | — | — | — |
| Operative ability | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Pointer marker | ✓ | ✓ | ✓ | — | — | — | — |
| Political act | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Presence token | ✓ | ✓ | ✓ | — | — | — | — |
| Situation Report card | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Standing marker | ✓ | ✓ | ✓ | — | — | — | — |
| Structure block | ✓ | ✓ | ✓ | — | — | — | — |
| Target Profile | ✓ | ✓ | ✓ | — | — | — | ✓ |
| Tension marker | ✓ | ✓ | ✓ | — | — | — | — |
| Threshold marker | ✓ | ✓ | ✓ | — | — | — | — |

*Source: `the_signal_db.v_comp_verb_matrix`. Art 07 and Art 08 components extend this table — update DB first, regenerate from view. Game Layers (Territory / Economy / Information / Submission / Resolution / Standing) are a card design context layer — see §4 and §5.*

---

### 3.3 Primitive Action Model — Database-Backed Analysis (S47)

#### Methodology

Session 47 formalized the physical action taxonomy into a relational model in `the_signal_db`. The model answers three questions simultaneously: **what** can be acted on, **when** it can be acted on, and **who** can act on it. Each axis is a separate dimension table; legal actions are the intersection.

**Dimension tables:**

| Table | Axis | Content |
|-------|------|---------|
| `tmp_component` | What | 51 registered physical components |
| `tmp_verb` | How | 7 physical verbs (+ Invoke meta-verb) |
| `tmp_beat` | When | 20 beats across the full Quarter structure |
| `tmp_player_role` | Who | Faction / ARBITER |
| `tmp_role_phase` | Role phase | Initiator / Executor / Fulfiller |
| `tmp_trigger_type` | Why | 10 trigger classifications |

**Junction tables** (`tmp_comp_verb_beat`, `tmp_comp_verb_role`) define valid combinations. A valid *primitive* is any row in both junction tables for the same component × verb pair — the intersection of what is possible by timing AND what is possible by role.

**Primitives are derived** as: `tmp_comp_verb_beat × tmp_comp_verb_role (phase_id=1)`. Phase_id=1 (initiator) captures who calls for the action; the executor (phase_id=2) is tracked separately in `tmp_comp_verb_role` and is not collapsed into the primitive row. Result: **213 primitives** in `tmp_action` as of S47.

#### Trigger Taxonomy

Every primitive in `tmp_action` carries a `trigger_type_id` classifying what causes the action to fire:

| Type | Subtype | Definition |
|------|---------|------------|
| phase | open | Action fires at beat entry |
| phase | during | Action is valid throughout a beat window |
| phase | closed | Action fires at beat transition |
| rule | card | Card text mandates the action |
| rule | resolution | Quarter resolution procedure mandates the action |
| player | introduce_card | Player submits or declares a card |
| player | agreement | Bilateral consent (trade, Accord) |
| player | verbal_statement | Player declaration with game effect |
| state_condition | — | Compound board/game state check |
| cascade | — | Prior action must have occurred (prereq_id) |

**S47 trigger distribution (primitives only):**

| Trigger | ARBITER | Faction |
|---------|---------|---------|
| phase.during | 56 | 15 |
| rule.card | 117 | 3 |
| rule.resolution | 1 | 4 |
| player.introduce_card | — | 14 |
| player.agreement | — | 3 |

#### Governing Principle (L166)

The taxonomy defines **possibility space** — every valid combination of component × verb × beat × role that the physical game system can support. Art 03 defines **legal space** — the subset of those combinations that the rules actually permit and describe a procedure for.

A primitive present in `tmp_action` with no corresponding Art 03 procedure is not a modeling error — it is an open design question. Every gap discovered through this analysis is routed to Art 03 for resolution: **permit** (write the procedure), **prohibit** (annotate as explicitly illegal), or **defer**. The two artifacts co-evolve iteratively.

#### Gap Analysis Views

Two views provide the ongoing procedure coverage audit:

**`v_unlegislated_primitives`** — All (beat, subject, verb, component) combinations valid in the taxonomy but absent from `tmp_action`. 60 rows as of S47; organized by beat. Primary use: beat-by-beat procedure review.

**`v_unlegislated_by_trigger`** — All (subject, verb, component) tuples with zero coverage in `tmp_action` under any trigger type or beat. 14 rows as of S47 (all Faction-initiated). Primary use: legalization decision queue — for each row: permit / prohibit / defer.

S47 identified 14 unlegislated Faction-initiated combinations:

| Subject | Verb | Component | Beats | Decision |
|---------|------|-----------|-------|----------|
| Faction | Add | Intel token | 2 | 🔄 |
| Faction | Add | Political act | 2 | 🔄 |
| Faction | Add | Presence token | 3 | 🔄 |
| Faction | Add | Structure block | 3 | 🔄 |
| Faction | Conceal | Intel token | 2 | 🔄 |
| Faction | Corrupt | Accord agreement | 2 | 🔄 |
| Faction | Corrupt | Intel token | 2 | 🔄 |
| Faction | Corrupt | Target Profile | 2 | 🔄 |
| Faction | Remove | Accord agreement | 2 | 🔄 |
| Faction | Remove | Deployment marker | 2 | 🔄 |
| Faction | Remove | Intel token | 2 | 🔄 |
| Faction | Remove | Structure block | 2 | 🔄 |
| Faction | Reveal | Accord agreement | 1 | 🔄 |
| Faction | Reveal | Intel token | 2 | 🔄 |

*Decision column: ✅ Permit (Art 03 procedure exists or written) / ❌ Prohibit (explicitly excluded) / 🔄 Deferred*

All planned views completed S47: `v_gap_executor_check`, `v_unassigned_triggers`, `v_duplicate_primitives`, `v_component_coverage`, `v_beat_subject_coverage`, `v_trigger_beat_coverage`. View `v_card_primitive_map` remains blocked — requires `tmp_card_ref` seed table.

#### Known Seeding Gaps (S48)

The following are pending DB population tasks — not design gaps in the taxonomy.

| Component / Beat | Gap | Note |
|-----------------|-----|------|
| Countermeasures beats (4, 10, 16) | 0 primitives seeded | Art 03 §10/§13/§16 defines the procedure. Pending component registration for Countermeasure card. |
| ARBITER Dominance Marker (`tmp_component` id=42) | No `tmp_comp_verb_role` or `tmp_comp_verb_beat` entries | Present in §3.2 matrix. DB seeding queued. |
| Classified directives (`tmp_component` id=17) | No `tmp_comp_verb_role` or `tmp_comp_verb_beat` entries | Present in §3.2 matrix. DB seeding queued. |
| Standing marker — resolution beats | ARBITER Move absent from `tmp_action` for Beat 3 / Beat 4 | Card-triggered primitive. Beat 3: failure/discovery only (covert success produces no Standing marker move — unobserved). Beat 4: all outcomes. Seeding queued. |
| 37 duplicate rows | Exact duplicates in resolution beats (Month 1/2 Beat 3, Month 3 Beat 4) | Seeding artifact. Deletion queued. |

---

## 4. Card Design Layer — Key Decisions

The physical action taxonomy (§3) defines what can happen to components. The card design layer defines *which game system a card affects* — independent of which physical verbs execute the effect. These are the decisions that produced the Layer — Function — Subject framework used in §5.

*Naming note: the six divisions in this section are called **Layers**. The existing L2-L5 expansion implementation terminology also uses "layer" — that terminology requires renaming to avoid collision. See PM05 04b-10.*

### 4.1 Layers define game systems, not action types

A **Layer** answers: which game system does this card affect?
A **Function** answers: what does the card do to it?

The distinction matters because the same physical verb can serve different design purposes. `Add` as a Territory action (placing presence) and `Add` as an Economy action (gaining Intel) are the same physical primitive but different design intents. Layer assignment ensures the portfolio is balanced across game systems, not just across verbs.

Layers are game-design partitions — not narrative concepts, not phase concepts. They describe what the game is tracking and what cards can affect.

### 4.2 The six game layers

| Layer | Visibility | Governs |
|-------|-----------|---------|
| **Territory** | Public | The influence landscape: presence tokens, structures, control flags, spatial markers |
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

A card that adds an Intel token to the pool (C05 Gather) is an Information card — the dominant design intent is intelligence acquisition, not resource accumulation. Token count is an Economy property of a held asset; card layer is classified by what the card's primary effect serves. A card that reveals the content of a token is an Information card. A card that introduces a token with falsified content (C20 Misdirection) is an Information card — the qualitative deception is the primary design intent, even though the Add primitive is also executed.

### 4.5 Accord is a known-narrow Economy subset

Whether an Accord exists between two factions is a public, countable fact → Economy. The recorded terms of an Accord are Information. Accord as a category is mechanically narrow in the current design; the Economy classification holds, but Accord-specific design space may warrant dedicated attention in future passes.

### 4.6 Protect distributes to the target's layer

A Protect card belongs to the layer of its protected target — it is not a cross-layer function. The principle is established; individual card assignments below are pending full card development except where noted.

| Card | Protected target | Layer | Status |
|------|----------------|-------|--------|
| C10 Protect | Covert operation difficulty | Resolution | ✅ Signed off |
| C11 Fortify Structure | Structure block | Territory | ✅ Signed off |
| C18 Identity Blind | Action attribution | Information | 📝 Pending development |
| C19 Deep Cover | Action attribution (permanent) | Information | 📝 Pending development |
| C23 Evidence Preservation | Written record | Information | 📝 Pending development |
| C34 Golden Parachute | Native resource | Economy | 📝 Pending development |

### 4.7 Submission and Resolution are distinct layers

The original Action category covered blocking submissions, modifying costs, adjusting difficulty, and changing scope — two separate systems:

- **Submission** governs what enters the queue: costs, eligibility restrictions, blocks, operational scope
- **Resolution** governs how the queue resolves: the d100 threshold, difficulty, modifier application, outcome scale

A card that blocks an operation from being submitted (C21 Invoke Jurisdiction, C25 Sealed Border) is a Submission card. A card that changes the difficulty of an operation in the queue (P18 Signal Review Request) is a Resolution card.

### 4.8 Standing is an affectable consequence register

Public Standing and Portrait tracks record resolution outcomes across the session — they function as consequence registers. However, they are also independently affectable: cards can shift track values directly, independent of any underlying action resolving. This dual role (output register + independently affectable surface) warrants a dedicated layer.

Portrait is ARBITER-controlled (L84, 00a R01). Player-facing Standing cards affect Public Standing only.

### 4.9 React, Instant, and interrupt effects

React, Instant, and interrupt effects are an intentional play mechanic — trigger-based cards that fire automatically on publicly observable conditions. These mechanics are valid and in full scope for the game.

In the taxonomy, React/Instant/interrupt is a *timing classification*, not a Layer or Function. A card using this mechanic carries its own Layer — Function — Subject for its primary effect; the timing mechanism describes *when* the effect fires, not *what* it affects. These mechanics can appear across all layers:

- A React card that recovers resources on a condition → Economy — Recover — Native resource (C12)
- An Instant card that blocks a submission in-flight → Submission — Block — [target]
- An interrupt that reveals attribution when triggered → Information — Reveal — Action attribution

Because timing is a separate axis, React / Instant / interrupt cards are classified by their effect, not their trigger. The full mechanic treatment — trigger conditions, stack behavior, observability requirements — is in §10.

### 4.10 Corrupt applies only to physically written or recorded values

Corrupt is classified in the Information layer. Scope is strict: applies only to values physically written or tracked in the paper prototype. Valid targets: Intel tokens (faction name and round number written on token), Accord agreements (terms written on document), Target Profile (content within an operation bundle inside the dispatch case). Invalid: printed card text, marker positions (tracked by physical position, not written value), Chronicle (ARBITER narrative — not a mechanical game element).

### 4.11 Redirect unifies Convert and Transfer

Convert (changing ownership of a board element) and Transfer (moving resources between factions) are both instances of Redirect. Convert is Territory — Redirect. Transfer is Economy — Redirect.

### 4.12 No persistent temporary cross-round effects

All card effects are either immediate (this Quarter only) or permanent (rest of session). No card creates a state that expires after a defined number of Quarters.

### 4.13 Design note — Paper vs Electronic ARBITER knowledge gap

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
| Recover | Returns a spent, removed, or degraded element to active play | Add |
| Modify | Alters a cost, value, or attribute without changing the element's fundamental state | — (abstract constraint) |
| Protect | Preserves the current state of a target against a named change | — (meta-constraint) |
| Block | Prevents another action from being initiated or resolving | — (meta-constraint) |
| Copy | Duplicates another action's effect chain with a new initiating subject | Invoke |
| Reveal | Makes hidden information visible to a named audience | Reveal |
| Conceal | Places information or attribution into a hidden state | Conceal |
| Shift | Moves a track value (Portrait, Public Standing) up or down | Move |
| Corrupt | Alters a physically written or recorded value on a component | Corrupt |

**Primitive Verb(s)** — the physical verb(s) from §3.1 that execute this card's effect on a component. `—` indicates the card operates as a constraint or modifier on another action rather than directly executing a physical primitive. This is the bridge between the card design layer and the physical action model.

**Modifier Card Scope** — Modifier cards are excluded from Layer — Function — Subject taxonomy (§9). They do not produce game-state primitives; they alter the parameters of primitives initiated by taxonomy cards. Their design space spans all six layers — any valid action from any layer can be the host action for a Modifier. The design question is not "which layer?" but "what host action does this require, and what parameter does it change?" Parameters a Modifier can alter include difficulty, cost, threshold, scope, outcome, timing, or validity of the host action.

React and Instant are timing sub-functions within the Modifier card type — they describe when a Modifier fires, not what it does. React fires automatically when a named publicly-observable condition is met (Art 04 §5 Principle 5); Instant is played actively during a defined window. Both are specified in Artifact 04 card specs. A Timing column may be added to §5.2 when the full modifier timing model is locked.

### 5.2 Card Index

*Status key: ✅ Signed off — canonical, use for gap analysis. 📝 Draft — designed but not signed off. ⬜ Not yet designed. 🚫 Retired.*

| Card ID | Name | Status | Layer | Function | Subject | Primitive Verb(s) |
|---------|------|--------|-------|----------|---------|-------------------|
| C01 | Build Structure | ✅ | Territory | Add | Structure block | Add |
| C02 | Demolish | ✅ | Territory | Remove | Structure block | Remove |
| C03 | Campaign | ✅ | Territory | Add | Presence token | Add |
| C04 | Undermine | ✅ | Territory | Remove | Presence token | Remove |
| C05 | Gather | ✅ | Information | Add | Intel token | Add |
| C06 | Broadcast Interference | ✅ | Submission | Modify | Political act (cost) | — |
| C07 | Amplify | ✅ | Resolution | Modify | Political act (outcome scale) | — |
| C08 | Buy Influence | ✅ | Territory | Add | Presence token | Add |
| C09 | Fund | ✅ | Economy | Redirect | Native resource | Move |
| C10 | Protect | ✅ | Resolution | Protect | Covert operation (difficulty) | — |
| C11 | Fortify Structure | ✅ | Territory | Protect | Structure block | — |
| C12 | Materials Acquisition | ✅ | Economy | Recover | Native resource | Add |
| C13 | Foundation Rights | ✅ | Territory | Add | Presence token | Add |
| C14 | Construction Crew | ✅ | Submission | Remove Restriction | Covert operation (presence requirement) | — |
| C15 | Infrastructure Yield | ✅ | Economy | Add | Native resource | Add |
| C16 | Pattern Match | ✅ | Submission | Copy | Covert operation (full) | Invoke |
| C17 | Intercept | 📝 | Information | Reveal | Covert operation — named faction | Reveal |
| C18 | Identity Blind | 📝 | Information | Protect | Action attribution | Conceal |
| C19 | Deep Cover | 📝 | Information | Protect (permanent) | Action attribution | Conceal |
| C20 | Misdirection | 📝 | Information | Add | Intel token (corrupt content) | Add + Corrupt |
| C21 | Invoke Jurisdiction | 📝 | Submission | Block | Covert operation (C01, C03) | — |
| C22 | Detain | 📝 | Territory | Remove (permanent) | Deployment marker | Remove |
| C23 | Evidence Preservation | 📝 | Information | Protect (permanent) | Written record | — |
| C24 | Surveillance Placement | 📝 | Information | Add (permanent) | Intel token | Add |
| C25 | Sealed Border | 📝 | Submission | Block | Covert operation (presence placement) | — |
| C26 | Leak | 📝 | Information | Reveal | Action attribution | Reveal |
| C27 | Source Protection | 📝 | Information | Protect | Action attribution | — |
| C28 | Open Channel | 📝 | Information | Reveal | Private communications | Reveal |
| C29 | Network Cascade | 📝 | Submission | Modify | Covert operation (scope) | — |
| C30 | Community Anchor | 📝 | Territory | Add | Presence token | Add |
| C31 | Leveraged Acquisition | 📝 | Economy | Add | Native resource | Add |
| C32 | Short the Market | 📝 | Economy | Remove | Native resource | Remove |
| C33 | Hostile Acquisition | 📝 | Territory | Redirect | Structure block | Move |
| C34 | Golden Parachute | 📝 | Economy | Protect | Native resource | — |
| C35 | Regulatory Capture | 📝 | Submission | Block | Named action type | — |
| — | Source Substitution | 📝 | Information | Corrupt | Intel token | Corrupt |
| — | Backdate | 📝 | Information | Corrupt | Intel token | Corrupt |
| — | Field Verification | 📝 | Information | Recover | Intel token | — |
| — | Disinformation Campaign | 📝 | Standing | Shift | Public Standing | Move |
| — | Standing Injunction | 📝 | Submission | Block | Political act | — |
| — | Disprove | 📝 | Economy | Remove | Intel token | Remove |
| — | Intel Extraction | 📝 | Economy | Redirect | Intel token | Move |
| — | Modifier Raid | 📝 | Economy | Redirect | Modifier card | Move |
| P01 | Open Operations | 📝 | Territory | Add | Presence token | Add |
| P02 | Disputed Claim | 📝 | Territory | Remove | Presence token | Remove |
| P03 | Public Commission | 📝 | Territory | Add | Structure block | Add |
| P04 | Public Censure | 📝 | Standing | Shift | Public Standing (−) | Move |
| P05 | On the Record | 📝 | Information | Reveal | Action attribution | Reveal |
| P06 | Economic Sanction | 📝 | Economy | Remove | Native resource | Remove |
| P07 | Public Address | 📝 | Standing | Shift | Public Standing (+) | Move |
| P08 | Table an Accord | 📝 | Economy | Add | Accord agreement | Add |
| P09 | Civic Works Mandate | 📝 | Territory | Add | Structure block | Add |
| P10 | Infrastructure Bond | 📝 | Economy | Add | Accord agreement | Add |
| P11 | Regulatory Override | 📝 | Submission | Modify | Presence token (placement cost) | — |
| P12 | Convene an Inquiry | 📝 | Information | Add | Intel token | Add |
| P13 | Public Disclosure | 📝 | Information | Reveal | Action attribution | Reveal |
| P14 | Community Rally | 📝 | Territory | Add | Presence token | Add |
| P15 | Acquisition Offer | 📝 | Territory | Redirect | Presence token | Move |
| P16 | Public Dividend | 📝 | Economy | Add | Native resource (conditional) | Add |
| P17 | Publish Analysis | 📝 | Information | Reveal | Action attribution | Reveal |
| P18 | Signal Review Request | 📝 | Resolution | Modify | Covert operation (difficulty) | — |

---

## 6. Coverage Analysis — Gaps and Concentrations

### 6.1 Unused taxonomy combinations

The following combinations exist in the taxonomy but have no current card. Layer and Function definitions are included to prompt the core design question: *is there a narrative reason to perform this action in this game system?* If yes, it is a candidate for card development.

---

**Layer: Territory** — *The influence landscape: presence tokens, structures, control flags, spatial markers*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Redirect | Changes ownership, destination, or allegiance of an element | Structure | Low | Transfer structure faction — C33 partially covers |
| Recover | Returns a spent, removed, or degraded element to active play | Presence token | Medium | Return removed tokens — Guild candidate |
| Recover | Returns a spent, removed, or degraded element to active play | Structure | High | Reconstruct demolished structure — strong Guild card |

**Layer: Economy** — *Quantitative holdings: native resources, token counts, card counts, Accord existence*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Remove | Takes an element out of active play | Intel token | Low | Strip opponent Intel tokens |
| Remove | Takes an element out of active play | Modifier card | Medium | Strip opponent modifier cards |
| Remove | Takes an element out of active play | Accord agreement | High | Break Accord covertly — important missing mechanic |
| Recover | Returns a spent, removed, or degraded element to active play | Modifier card | Low | Return spent modifier card |
| Redirect | Changes ownership, destination, or allegiance of an element | Accord agreement | High | "Small print" mechanic — Syndicate doctrine |
| Redirect | Changes ownership, destination, or allegiance of an element | Modifier card | Low | Partially covered by trade rules |

**Layer: Submission** — *What enters the resolution queue: costs, eligibility, blocks, scope*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Copy | Duplicates another action's effect chain with a new initiating subject | Political act | Low | Copy opponent political act |
| Copy | Duplicates another action's effect chain with a new initiating subject | Subset only | Medium | Copy target or effect only — Ghost doctrine. ⚠️ Partial-copy mechanism needed in action model |

**Layer: Information** — *Qualitative content: token content, written records, attribution, reconnaissance*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Reveal | Makes hidden information visible to a named audience | Faction hand | High | `Faction hand` (id=94) registered S48. Covered: Modifier card ✅, Countermeasure card ✅. Pre-submission cards (Political act, Covert operation) not in play at intelligence beats — hand-targeting mechanic applies uniformly to all held types. See ⚠️ below |
| Reveal | Makes hidden information visible to a named audience | Classified directives | Low | Very high impact — use carefully |
| Reveal | Makes hidden information visible to a named audience | Modifier cards held | Medium | Disclose individual modifier card contents |
| Reveal | Makes hidden information visible to a named audience | Named faction only | High | Targeted disclosure — Ghost intelligence delivery. ⚠️ Target-scope/filter system needed |
| Corrupt | Alters a physically written or recorded value on a component | Intel token | High | Falsify Intel token content |
| Corrupt | Alters a physically written or recorded value on a component | Accord agreement | High | Alter Accord terms — Syndicate doctrine |

**Layer: Standing** — *Reputation tracks: Public Standing and Portrait*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Shift | Moves a track value up or down | ~~Chorus Portrait (primary covert)~~ | — | **Retired (L84, 00a R01).** ARBITER sole mover of Portrait. Ghost doctrine gap: new primary covert effect needed — see PM05 04-11 |
| Shift | Moves a track value up or down | Public Standing (primary covert) | High | Standing as primary covert effect — Network doctrine |

---

*React / Instant / interrupt timing is a separate design dimension not captured in this table — cards with these triggers carry their own Layer/Function/Subject for the primary effect. React-triggered card design space to be tracked once the timing mechanic is fully specified. See §4.9 and §10.*

*⚠️ Two subjects require schema extension before primitives can be modeled: **Named faction only** (target-scope/filter system) and **Subset only** (partial-copy mechanism).*

*🔬 **Research flag (S48 — agy):** Established card games (Netrunner, espionage genre) use a distinct **Inspect** function — private read of a face-down card without making it public. Currently merged into `Reveal` (which implies public disclosure). If Inspect is added to §5.1, candidate gaps: Information | Inspect | Intel token; Information | Inspect | Covert operation. Flag for §5.1 review before actioning.*

### 6.2 Overrepresented combinations

| Layer | Function | Subject | Cards | Issue |
|-------|----------|--------|-------|-------|
| Territory | Add | Presence token | C03, C08, C13, C30, P01 | 5 cards — differentiation critical |
| Submission | Block | Various | C21, C25, P07, P11 | 4 Block cards — C21/C25 target covert operations, P07 any procedural, P11 political act; Function concentration across all four |
| Information | Protect | Action attribution | C18, C19, C27 | 3 cards, 2 same faction, same function |
| Information | Reveal | Various | C26, P05, P13 (action attribution); C28 (private communications) | 4 Reveal cards — 3 share the same subject (action attribution); consolidation candidates |

### 6.3 DB-Backed Gap Analysis (S47)

*Supersedes §6.1 as the authoritative gap source. §6.1 retains historical value as a card design ideation list using the Layer/Function framework. §6.3 is derived directly from the primitive model and is the operative reference for legalization decisions.*

The DB primitive model generates two gap views. See §3.3 for methodology.

**`v_unlegislated_by_trigger`** — 14 unlegislated Faction-initiated (subject, verb, component) tuples. Reproduced in §3.3 with decision tracking. Each row requires a permit / prohibit / defer ruling before the corresponding Art 03 procedure can be written or explicitly closed.

**`v_unlegislated_primitives`** — 60 beat-specific gaps. 46 are expected (Faction-at-Beat-3, ARBITER-executed beat); 2 are ARBITER-Move-Standing-marker-at-Beat-3 (inverse of the public-exception primitive); 12 are Faction-at-M3-Beat-4, the most interesting design space for new card effects.

All planned gap views completed S47 — see §3.3 for view list and status. `v_card_primitive_map` remains blocked pending `tmp_card_ref`.

---

## 7. Faction Coverage Matrix

| Layer | Function | Subject | Standard | Guild | Ghost | Directorate | Network | Syndicate |
|-------|----------|--------|----------|-------|-------|-------------|---------|-----------|
| **Territory** | | | | | | | | |
| | Add | Presence token | C03, C08 | C13 | — | — | C30 | — |
| | Add | Structure | C01 | — | — | — | — | — |
| | Remove | Presence token | C04 | — | — | — | — | — |
| | Remove | Deployment marker | — | — | — | C22 | — | — |
| | Remove | Structure | C02 | — | — | — | — | — |
| | Redirect | Presence token | P15 | — | — | — | — | — |
| | Redirect | Structure | — | — | — | — | — | C33 |
| | Protect | Structure block | — | C11 | — | — | — | — |
| | Recover | Presence token | — | — | — | — | — | — |
| | Recover | Structure | — | — | — | — | — | — |
| **Economy** | | | | | | | | |
| | Add | Native resource | — | C15 | — | — | — | C31 |
| | Add | Intel token | C05 | — | — | C24 | P12 | — |
| | Add | Accord agreement | P08 | — | — | — | — | — |
| | Remove | Native resource | P06 | — | — | — | — | C32 |
| | Remove | Accord agreement | — | — | — | — | — | — |
| | Recover | Native resource | — | C12 | — | — | — | — |
| | Recover | Intel token | — | — | C17 | — | — | — |
| | Redirect | Native resource | C09 | — | — | — | — | — |
| | Redirect | Accord agreement | — | — | — | — | — | — |
| | Protect | Native resource | — | — | — | — | — | C34 |
| **Information** | | | | | | | | |
| | Reveal | Action attribution | P05, P13 | — | — | — | C26, C28 | — |
| | Reveal | Written record | P14 | — | — | — | — | — |
| | Reveal | Named faction | — | — | — | — | — | — |
| | Protect | Action attribution | — | — | C18, C19 | — | C27 | — |
| | Protect | Written record | — | — | C23 | — | — | — |
| | Add | Intel token (corrupt content) | — | — | C20 | — | — | — |
| | Corrupt | Intel token | — | — | — | — | — | — |
| | Corrupt | Accord agreement | — | — | — | — | — | — |
| **Submission** | | | | | | | | |
| | Block | Covert operation | — | — | — | C21, C25 | — | — |
| | Block | Named action type | — | — | — | — | — | C35 |
| | Block | Political act | P07 | — | — | P11 | — | — |
| | Modify | Cost | C06 | — | — | — | — | P16 |
| | Modify | Scope | — | — | — | — | C29 | — |
| | Copy | Full action | — | — | C16 | — | — | — |
| | Copy | Subset | — | — | — | — | — | — |
| | Remove Restriction | Presence | — | C14 | — | — | — | — |
| **Resolution** | | | | | | | | |
| | Modify | Outcome scale | C07 | — | — | — | — | — |
| | Modify | Difficulty | — | — | — | — | — | P18 |
| | Protect | Covert operation (difficulty) | C10 | — | — | — | — | — |
| **Standing** | | | | | | | | |
| | Shift | Public Standing | P04, P07 | — | — | — | — | — |

---

## 8. Design Recommendations by Faction

These recommendations inform the redesign decisions D-04-02 through D-04-05 in Artifact 04 §16.

### 8.1 Ghost — Priority redesign targets

Current Ghost set (C16–C20) is doctrinally coherent but mechanically narrow. Two cards duplicate the same function (Information — Protect — Action attribution). Ghost lacks a primary covert effect that isn't attribution-protection — the Portrait avenue is closed (L84, 00a R01); see PM05 04-11.

**High priority:**
1. **Information — Reveal — Named faction:** Ghost delivers targeted intelligence to a specific faction privately rather than the whole table. *Targeted intelligence disclosure that strengthens relationships without public exposure.*
2. **Submission — Copy — Subset:** Ghost should have a partial copy card — copy only the target (apply your own operation to the same district as named faction) without replicating the full cost and effect.
3. **Replace C18 Identity Blind:** Both C18 and C19 are Information — Protect — Action attribution. C19's permanent effect is stronger and more interesting. C18 could be replaced with Economy — Add — Intel token (generate intelligence through analysis without physical presence — Findings spent, Intel token received, no adjacency restriction).

### 8.2 Directorate — Priority redesign targets

Directorate is over-indexed on Submission — Block: C21, C25 (covert), P07, P11 (political) — four Block cards.

**High priority:**
1. **Replace C25 Sealed Border with Resource — Add — Native resource (Mandate):** Institutional authority generates Mandate when exercised and respected. *"When The Directorate issues an instruction that is complied with this round — no faction contests a Directive, no faction enters a sealed district — Mandate is generated as institutional validation."*
2. **Standing — Shift — Public Standing (primary covert):** The Directorate managing public perception through institutional channels. A covert card that shifts Public Standing positively when an institutional action succeeds.

**Medium priority:**
3. **Resolution — Modify — Difficulty (increasing, against all factions):** Institutional scrutiny raises difficulty of all covert operations in a named district this round. Distinct from C10 Protect (which only protects the protecting faction's assets).

### 8.3 Network — Priority redesign targets

Network has duplicate Reveal cards and a doctrinal contradiction in C27.

**High priority:**
1. **Replace C27 Source Protection with Economy — Add — Exposure:** The Network generating Exposure through information activity. *"When The Network successfully Reveals information this round, gain 1 Exposure — the act of disclosure generates the resource that enables further disclosure."* Creates positive feedback loop consistent with Network doctrine.
2. **Standing — Shift — Public Standing (primary covert):** Network managing city-wide public perception through covert information operations. *"Targeted community outreach in a named district shifts Public Standing based on the district's current control state."*
3. **Territory — Add — Presence token (React trigger: political act success):** Network responding to opponent public actions. *"When any faction's political act succeeds this round, The Network may trigger — placing 1 presence token in the district where the political act resolved."* Timing trigger handled in card spec; primary effect is Territory — Add.

**Medium priority:**
4. **Consolidate C26 and C28:** Both are Information — Reveal with different scopes (Action attribution vs Private communications). Consider whether both are needed or one broader Reveal card covers the design space.

### 8.4 Syndicate — Priority redesign targets

Syndicate has excellent Economy coverage but zero information capability despite being an economic intelligence operation.

**High priority:**
1. **Information — Corrupt — Accord agreement:** Alter the recorded terms of an existing Accord. *"The Syndicate may alter one numeric value in any registered Accord — changing a resource amount, duration, or threshold. The alteration is physically made to the Accord document. Both parties notified in case."* Requires ARBITER to manage Accord document integrity.
2. **Economy — Redirect — Accord agreement:** The "small print" mechanic. *"The Syndicate transfers an existing Accord's obligations from one faction to another. The receiving faction is privately notified — they may accept or contest at the start of the next round."*
3. **Information — Reveal — Intel tokens held:** Economic intelligence. *"The Syndicate names a faction. ARBITER announces the count (not content) of Intel tokens that faction holds. The Syndicate may offer to purchase one token from the named faction at 3 Capital — the named faction may accept or decline."*

---

## 9. Standalone Card Types — Taxonomy Exclusions

The following card types are excluded from the Layer — Function — Subject taxonomy. They are not game-state actions targeting a specific game layer — they are meta-actions or structural components that operate on the play procedure rather than the game state.

**Pass cards** — Excluded. Pass is a procedural declaration (this slot is intentionally empty / no political act declared). Any secondary effect on a Pass card (e.g., Findings gain, modifier draw) is incidental and does not constitute a taxonomy action. Pass cards carry no Layer — Function — Subject fields.

**Modifier cards** — Excluded. Modifier cards modify the parameters of an action rather than targeting a game layer directly. They may be played as interrupts during battle, triggered as React (firing automatically when a named publicly-observable condition is met — not submitted in the standard action sequence), or used to fund a burst play. Their effect — whether against a card, a board state, a resource, or any valid react/instant target — is mediated by the action or condition they modify. React is a timing sub-function within the Modifier card type, not a standalone card type. Modifier cards carry no Layer — Function — Subject fields.

**Emergency Response cards** — Excluded. Trigger-based, pre-staged cards with fixed effects. Not submitted in dispatch cases or declared in the standard action sequence. The penultimate action available to a faction before Apex fires.

*Source: Session 28 design note. Consistent with L115 (Art 04 owns all card design; card type determines scope, not taxonomy category).*

---

*End of Artifact 04b — Action Taxonomy & Design Analysis v1.5*
