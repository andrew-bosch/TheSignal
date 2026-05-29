# 04b — ACTION TAXONOMY & DESIGN ANALYSIS
## THE SIGNAL P1 — Paper Prototype

**Version:** 1.4  
**Status:** 📝 Pending Re-Sign-Off — material additions S47  
**Last Updated:** 2026-05-28  
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
| §4 | [Card Design Layer — Key Decisions](#4-card-design-layer--key-decisions) — rationale for Category/Function framework |
| §5 | [Card Taxonomy Index](#5-card-taxonomy-index) — Category, Function, Subject, Primitive Verb per card |
| §6 | [Coverage Analysis — Gaps and Concentrations](#6-coverage-analysis--gaps-and-concentrations) |
| §7 | [Faction Coverage Matrix](#7-faction-coverage-matrix) |
| §8 | [Design Recommendations by Faction](#8-design-recommendations-by-faction) |
| §9 | [Design Principles Derived from Taxonomy](#9-design-principles-derived-from-taxonomy) |
| §10 | [Standalone Card Types — Taxonomy Exclusions](#10-standalone-card-types--taxonomy-exclusions) |

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

*Source: `the_signal_db.v_comp_verb_matrix`. Art 07 and Art 08 components extend this table — update DB first, regenerate from view. Categories (Board / Resource / Action / Cross-Category) are a card design context layer — see §5.*

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

Additional views planned (agy, next session): component coverage, beat/subject coverage, trigger×beat coverage, card reverse map, executor check, unassigned triggers, duplicate primitive detection.

---

## 4. Card Design Layer — Key Decisions

The physical action taxonomy (§3) defines what can happen to components. The card design layer defines *why* a card exists and *what system it affects* — independent of which physical verbs execute the effect. These are the decisions that produced the Category — Function — Subject framework used in §5.

### 4.1 Categories reflect what is being affected, not what is being done

A **Category** answers: what part of the game system does this card affect?
A **Function** answers: what does the card do to it?

The distinction matters because the same physical verb can serve different design purposes. `Add` as a Board action (placing presence) and `Add` as a Resource action (gaining Intel) are the same physical primitive but different design intents. Category ensures the portfolio is balanced across game systems, not just across verbs.

### 4.2 Knowledge and Reputation collapse into Cross-Category

Knowledge (hidden information control) and Reputation (assessment track management) do not belong to a single category — they cut across Board, Resource, and Action states. Both were initially separate categories and were merged into Cross-Category:
- Knowledge targets (card hand, dispatch case, Intel tokens) contain elements from multiple categories
- Reputation tracks reflect behavior across all categories

Cross-Category functions (Reveal, Shift, Protect, Corrupt) apply to targets that don't belong cleanly to any single category.

### 4.3 Protect is cross-category and not constrained to adverse effects

Protect was initially defined as shielding against adverse effects only. Revised to: *preserve the current state of a named target against a specified effect — any named change, whether adverse or beneficial.* A faction could protect an Accord from being modified by anyone including themselves.

### 4.4 Corrupt applies only to physically written or recorded values

Corrupt was initially considered as a Knowledge function. Revised to Cross-Category with strict physical scope: applies only to values physically written or tracked in the paper prototype. Valid targets: Intel tokens (faction name and round number written on token), Accord agreements (terms written on document). Invalid: printed card text, marker positions (tracked by physical position not written value), Chronicle (ARBITER narrative — not a mechanical game element).

### 4.5 React is a timing/interrupt mechanism, not a Function

React cards fire automatically when a named publicly-observable condition is met. Reclassified as modifier card mechanic: React is not a Category — Function — Subject action but a timing/interrupt layer applied to another card's resolution. Excluded from the card taxonomy (see §10).

The triggering condition must be publicly observable — hidden conditions are not valid React triggers. The card's primary effect resolves in its own Category and Function independent of the trigger. C12 Materials Acquisition: React is the trigger; primary Function is Resource — Recover — Native resource.

### 4.6 Redirect unifies Convert and Transfer

Convert (changing ownership of a board element) and Transfer (moving resources between factions) are both instances of Redirect. Convert is Board — Redirect. Transfer is Resource — Redirect.

### 4.7 No persistent temporary cross-round effects

All card effects are either immediate (this Quarter only) or permanent (rest of session). No card creates a state that expires after a defined number of Quarters.

### 4.8 Design note — Paper vs Electronic ARBITER knowledge gap

In the paper prototype, ARBITER knows what happened (actions taken, board state, resolved effects) but does not know what is being considered (cards held, options available, choices not made). This is consistent with ARBITER's narrative character — ARBITER reads signals that have entered the causal chain; intent before action is not yet signal.

In the electronic version, ARBITER would have access to hand contents and could generate Chronicles that include patterns of restraint alongside patterns of action. The unchosen path is also story. Flag for PM04 — Future Phases.

---

## 5. Card Taxonomy Index

*Card definitions are in Artifact 04. This index provides Category — Function — Subject — Primitive Verb(s) assignments for all cards as a design reference. Use this table to identify coverage gaps and duplications.*

### 5.1 Column Definitions

**Category** — what part of the game system does this card affect?

| Category | Scope |
|----------|-------|
| Board | The influence landscape: presence tokens, structures, control flags, territory state |
| Resource | Faction holdings and information assets: native resources, Intel tokens, Accord agreements, modifier cards |
| Action | The submission and resolution process itself: modifying, blocking, or copying other actions in flight |
| Cross-Category | Effects that cut across multiple categories simultaneously: information revelation, attribution concealment, standing/reputation shifts |

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
| React | *Timing mechanism only — not a Function.* See §4.5 and §10. | — |

**Primitive Verb(s)** — the physical verb(s) from §3.1 that execute this card's effect on a component. `—` indicates the card operates as a constraint or modifier on another action rather than directly executing a physical primitive. This is the bridge between the card design layer and the physical action model.

### 5.2 Card Index

*Status key: ✅ Signed off — canonical, use for gap analysis. 📝 Draft — designed but not signed off. ⬜ Not yet designed. 🚫 Retired.*

| Card ID | Name | Status | Category | Function | Subject | Primitive Verb(s) |
|---------|------|--------|----------|----------|---------|-------------------|
| C01 | Build Structure | ✅ | Board | Add | Structure block | Add |
| C02 | Demolish | ✅ | Board | Remove | Structure block | Remove |
| C03 | Campaign | ✅ | Board | Add | Presence token | Add |
| C04 | Undermine | ✅ | Board | Remove | Presence token | Remove |
| C05 | Gather | ✅ | Resource | Add | Intel token | Add |
| C06 | Broadcast Interference | ✅ | Action | Modify | Political act (cost) | — |
| C07 | Amplify | ✅ | Action | Modify | Political act (effect magnitude) | — |
| C08 | Buy Influence | ✅ | Board | Add | Presence token | Add |
| C09 | Fund | ✅ | Resource | Redirect | Native resource | Move |
| C10 | Protect | ✅ | Cross-Category | Protect | Covert operation (difficulty) | — |
| C11 | Fortify Structure | ✅ | Cross-Category | Protect | Structure block | — |
| C12 | Materials Acquisition | ✅ | Resource + Action | Recover + React | Native resource | Add |
| C13 | Foundation Rights | ✅ | Board | Add | Presence token | Add |
| C14 | Construction Crew | ✅ | Action | Remove Restriction | Covert operation (presence requirement) | — |
| C15 | Infrastructure Yield | ✅ | Resource | Add | Native resource | Add |
| C16 | Pattern Match | ✅ | Action | Copy | Covert operation (full) | Invoke |
| C17 | Archive Recovery | 📝 | Resource | Recover | Intel token | Add |
| C18 | Identity Blind | 📝 | Cross-Category | Protect | Action attribution | Conceal |
| C19 | Deep Cover | 📝 | Cross-Category | Protect (permanent) | Action attribution | Conceal |
| C20 | Misdirection | 📝 | Resource | Add | Intel token (corrupt content) | Add + Corrupt |
| C21 | Invoke Jurisdiction | 📝 | Action | Block | Covert operation (C01, C03) | — |
| C22 | Detain | 📝 | Board | Remove (permanent) | Operational marker | Remove |
| C23 | Evidence Preservation | 📝 | Cross-Category | Protect (permanent) | Written record | — |
| C24 | Surveillance Placement | 📝 | Resource | Add (permanent) | Intel token | Add |
| C25 | Sealed Border | 📝 | Action | Block | Covert operation (presence placement) | — |
| C26 | Leak | 📝 | Cross-Category | Reveal | Action attribution | Reveal |
| C27 | Source Protection | 📝 | Cross-Category | Protect | Action attribution | — |
| C28 | Open Channel | 📝 | Cross-Category | Reveal | Private communications | Reveal |
| C29 | Network Cascade | 📝 | Action | Modify | Covert operation (scope) | — |
| C30 | Community Anchor | 📝 | Board | Add | Presence token | Add |
| C31 | Leveraged Acquisition | 📝 | Resource | Add | Native resource | Add |
| C32 | Short the Market | 📝 | Resource | Remove | Native resource | Remove |
| C33 | Hostile Acquisition | 📝 | Board | Redirect | Structure block | Move |
| C34 | Golden Parachute | 📝 | Cross-Category | Protect | Native resource | — |
| C35 | Regulatory Capture | 📝 | Action | Block | Named action type | — |
| P01 | Establish Presence | 📝 | Board | Add | Presence token | Add |
| P02 | Contest | 📝 | Board | Remove | Presence token (contested) | Remove |
| P03 | Commission | 📝 | Board | Add | Structure block (both districts) | Add |
| P04 | Denounce | 📝 | Cross-Category | Shift | Public Standing (−) | Move |
| P05 | Broadcast | 📝 | Cross-Category | Reveal | Action attribution | Reveal |
| P06 | Leverage | 📝 | Resource | Remove | Native resource | Remove |
| P07 | Invoke the Table | 📝 | Action | Block | Any (procedural) | — |
| P08 | Propose Accord | 📝 | Resource | Add | Accord agreement | Add |
| P09 | Public Works Declaration | 📝 | Board | Add | Structure block | Add |
| P10 | Infrastructure Bond | 📝 | Resource | Add | Native resource (target faction) | Add |
| P11 | Issue Directive | 📝 | Action | Block | Political act | — |
| P12 | Convene an Inquiry | 📝 | Resource | Add | Intel token | Add |
| P13 | Public Disclosure | 📝 | Cross-Category | Reveal | Action attribution | Reveal |
| P14 | Open Record Request | 📝 | Cross-Category | Reveal | Written record | Reveal |
| P15 | Acquisition Offer | 📝 | Board | Redirect | Presence token | Move |
| P16 | Market Pressure | 📝 | Action | Modify | Covert + Political act (cost) | — |
| P17 | Publish Analysis | 🚫 | Cross-Category | Shift | ~~Chorus Portrait~~ — retired (L84). Redesign required; see PM05 04-11. | — |
| P18 | Signal Review Request | 📝 | Action | Modify | Covert operation (difficulty) | — |

---

## 6. Coverage Analysis — Gaps and Concentrations

### 6.1 Unused taxonomy combinations

The following combinations exist in the taxonomy but have no current card. These represent available design space for future card development.

| Category | Function | Subject | Priority | Notes |
|----------|----------|--------|----------|-------|
| Board | Redirect | Presence token | Medium | Move tokens between districts |
| Board | Redirect | Structure | Low | Transfer structure faction — C33 partially covers |
| Board | Recover | Presence token | Medium | Return removed tokens — Guild candidate |
| Board | Recover | Structure | High | Reconstruct demolished structure — strong Guild card |
| Resource | Remove | Intel token | Low | Strip opponent Intel tokens |
| Resource | Remove | Modifier card | Medium | Strip opponent modifier cards |
| Resource | Remove | Accord agreement | High | Break Accord covertly — important missing mechanic |
| Resource | Recover | Modifier card | Low | Return spent modifier card |
| Resource | Redirect | Accord agreement | High | "Small print" mechanic — Syndicate doctrine |
| Resource | Redirect | Modifier card | Low | Partially covered by trade rules |
| Action | Copy | Political act | Low | Copy opponent political act |
| Action | Copy | Subset only | Medium | Copy target or effect only — Ghost doctrine |
| Action | React | Resource condition | Low | Fire on resource state change |
| Action | React | Accord existence | Medium | Fire on Accord creation or breach |
| Cross-Category | Reveal | Card hand contents | High | Disclose opponent's held cards |
| Cross-Category | Reveal | Classified directives | Low | Very high impact — use carefully |
| Cross-Category | Reveal | Modifier cards held | Medium | Disclose modifier card contents |
| Cross-Category | Reveal | Named faction only | High | Targeted disclosure — Ghost intelligence delivery |
| Cross-Category | Shift | ~~Chorus Portrait (primary covert)~~ | — | **Retired (L84, 00a R01).** ARBITER is sole mover of Portrait — not valid player-facing taxonomy. P17 Publish Analysis requires redesign (see 04-11, PM05). Ghost doctrine gap: new primary covert effect needed. |
| Cross-Category | Shift | Public Standing (primary covert) | High | Standing as primary covert effect — Network doctrine |
| Cross-Category | Corrupt | Intel token | High | Falsify Intel token content |
| Cross-Category | Corrupt | Accord agreement | High | Alter Accord terms — Syndicate doctrine |

### 6.2 Overrepresented combinations

| Category | Function | Subject | Cards | Issue |
|----------|----------|--------|-------|-------|
| Board | Add | Presence token | C03, C08, C13, C30, P01 | 5 cards — differentiation critical |
| Action | Block | Covert operation | C21, C25, P07, P11 | 4 Block cards across standard and faction |
| Cross-Category | Protect | Action attribution | C18, C19, C27 | 3 cards, 2 same faction, same function |
| Cross-Category | Reveal | Action attribution | C26, C28, P05, P13 | 4 Reveal cards, two pairs with same scope |

### 6.3 DB-Backed Gap Analysis (S47)

*Supersedes §6.1 as the authoritative gap source. §6.1 retains historical value as a card design ideation list using the Category/Function framework. §6.3 is derived directly from the primitive model and is the operative reference for legalization decisions.*

The DB primitive model generates two gap views. See §4.3 for methodology.

**`v_unlegislated_by_trigger`** — 14 unlegislated Faction-initiated (subject, verb, component) tuples. Reproduced in §4.3 with decision tracking. Each row requires a permit / prohibit / defer ruling before the corresponding Art 03 procedure can be written or explicitly closed.

**`v_unlegislated_primitives`** — 60 beat-specific gaps. 46 are expected (Faction-at-Beat-3, ARBITER-executed beat); 2 are ARBITER-Move-Standing-marker-at-Beat-3 (inverse of the public-exception primitive); 12 are Faction-at-M3-Beat-4, the most interesting design space for new card effects.

**Additional gap views queued for next agy session:**
- `v_gap_executor_check` — for each row in `v_unlegislated_by_trigger`, shows the executor role (phase_id=2); clarifies which gaps are expected (Faction initiates, ARBITER executes) vs. true design gaps
- `v_unassigned_triggers` — primitives in `tmp_action` with NULL `trigger_type_id`
- `v_duplicate_primitives` — duplicate (beat_id, subject_id, verb_id, component_id) rows
- `v_component_coverage` — components in `tmp_component` with no `tmp_action` rows
- `v_beat_subject_coverage` — verb and component count per subject per beat
- `v_trigger_beat_coverage` — trigger type presence by beat
- `v_card_primitive_map` — card ID → primitive reverse map (requires card reference table)

---

## 7. Faction Coverage Matrix

| Category | Function | Subject | Standard | Guild | Ghost | Directorate | Network | Syndicate |
|----------|----------|--------|----------|-------|-------|-------------|---------|-----------|
| **Board** | | | | | | | | |
| | Add | Presence token | C03, C08 | C13 | — | — | C30 | — |
| | Add | Structure | C01 | C14 | — | — | — | — |
| | Remove | Presence token | C04 | — | — | — | — | — |
| | Remove | Operational marker | — | — | — | C22 | — | — |
| | Remove | Structure | C02 | — | — | — | — | — |
| | Redirect | Presence token | — | — | — | — | — | — |
| | Redirect | Structure | — | — | — | — | — | C33 |
| | Recover | Presence token | — | — | — | — | — | — |
| | Recover | Structure | — | — | — | — | — | — |
| **Resource** | | | | | | | | |
| | Add | Native resource | — | C15 | — | — | — | C31 |
| | Add | Intel token | C05 | — | — | C24 | — | — |
| | Add | Accord agreement | P08 | — | — | — | — | — |
| | Remove | Native resource | — | — | — | — | — | C32 |
| | Remove | Accord agreement | — | — | — | — | — | — |
| | Recover | Native resource | — | C12 | — | — | — | — |
| | Recover | Intel token | — | — | C17 | — | — | — |
| | Redirect | Native resource | C09 | — | — | — | — | — |
| | Redirect | Accord agreement | — | — | — | — | — | — |
| **Action** | | | | | | | | |
| | Block | Covert operation | — | — | — | C21, C25 | — | — |
| | Block | Named action type | — | — | — | — | — | C35 |
| | Block | Political act | P07 | — | — | P11 | — | — |
| | Modify | Cost | C06 | — | — | — | — | P16 |
| | Modify | Effect magnitude | C07 | — | — | — | — | — |
| | Modify | Scope | — | — | — | — | C29 | — |
| | Modify | Difficulty | C10 | — | — | — | — | P18 |
| | Copy | Full action | — | — | C16 | — | — | — |
| | Copy | Subset | — | — | — | — | — | — |
| | Remove Restriction | Presence | — | C14 | — | — | — | — |
| | React | Action outcome | — | C12 | — | — | — | — |
| **Cross-Category** | | | | | | | | |
| | Reveal | Action attribution | — | — | — | — | C26, C28 | — |
| | Reveal | Named faction | — | — | — | — | — | — |
| | Shift | Public Standing | P04 | — | — | — | — | — |
| | Shift | ~~Chorus Portrait~~ | — | — | P17 | — | — | — |
| | Protect | Structure block | — | C11 | — | — | — | — |
| | Protect | Native resource | — | — | — | — | — | C34 |
| | Protect | Action attribution | — | — | C18, C19 | — | C27 | — |
| | Protect | Covert operation | C10 | — | — | — | — | — |
| | Corrupt | Intel token | — | — | C20 | — | — | — |
| | Corrupt | Accord agreement | — | — | — | — | — | — |

---

## 8. Design Recommendations by Faction

These recommendations inform the redesign decisions D-04-02 through D-04-05 in Artifact 04 §16.

### 8.1 Ghost — Priority redesign targets

Current Ghost set (C16–C20) is doctrinally coherent but mechanically narrow. Two cards duplicate the same function (Cross-Category — Protect — Action attribution).

**High priority:**
1. **Cross-Category — Reveal — Named faction:** Ghost delivers targeted intelligence to a specific faction privately rather than the whole table. *Targeted intelligence disclosure that strengthens relationships without public exposure.*
2. **Cross-Category — Shift — Chorus Portrait (primary covert):** Ghost's doctrine is understanding the Chorus. A card whose primary effect is Portrait improvement through demonstrated understanding is the most doctrinally correct gap. Candidate: *Calibrated Analysis — submit a specific interpretation of current board state; ARBITER evaluates accuracy; Portrait shift based on correctness.*
3. **Action — Copy — Subset:** Ghost should have a partial copy card — copy only the target (apply your own operation to the same district as named faction) without replicating the full cost and effect.
4. **Replace C18 Identity Blind:** Both C18 and C19 are Cross-Category — Protect — Action attribution. C19's permanent effect is stronger and more interesting. C18 could be replaced with Resource — Add — Intel token (generate intelligence through analysis without physical presence — Findings spent, Intel token received, no adjacency restriction).

### 8.2 Directorate — Priority redesign targets

Directorate is over-indexed on Action — Block: C21, C25 (covert), P07, P11 (political) — four Block cards.

**High priority:**
1. **Replace C25 Sealed Border with Resource — Add — Native resource (Mandate):** Institutional authority generates Mandate when exercised and respected. *"When The Directorate issues an instruction that is complied with this round — no faction contests a Directive, no faction enters a sealed district — Mandate is generated as institutional validation."*
2. **Cross-Category — Shift — Public Standing (primary covert):** The Directorate managing public perception through institutional channels. A covert card that shifts Public Standing positively when an institutional action succeeds.

**Medium priority:**
3. **Action — Modify — Difficulty (increasing, against all factions):** Institutional scrutiny raises difficulty of all covert operations in a named district this round. Distinct from C10 Protect (which only protects the protecting faction's assets).

### 8.3 Network — Priority redesign targets

Network has duplicate Reveal cards and a doctrinal contradiction in C27.

**High priority:**
1. **Replace C27 Source Protection with Resource — Add — Exposure:** The Network generating Exposure through information activity. *"When The Network successfully Reveals information this round, gain 1 Exposure — the act of disclosure generates the resource that enables further disclosure."* Creates positive feedback loop consistent with Network doctrine.
2. **Cross-Category — Shift — Public Standing (primary covert):** Network managing city-wide public perception through covert information operations. *"Targeted community outreach in a named district shifts Public Standing based on the district's current control state."*
3. **Action — React — Action resolution outcome:** Network responding to opponent public actions. *"When any faction's political act succeeds this round, The Network may trigger — placing 1 presence token in the district where the political act resolved."*

**Medium priority:**
4. **Consolidate C26 and C28:** Both are Cross-Category — Reveal with different scopes (Action attribution vs Private communications). Consider whether both are needed or one broader Reveal card covers the design space.

### 8.4 Syndicate — Priority redesign targets

Syndicate has excellent Resource coverage but zero information capability despite being an economic intelligence operation.

**High priority:**
1. **Cross-Category — Corrupt — Accord agreement:** Alter the recorded terms of an existing Accord. *"The Syndicate may alter one numeric value in any registered Accord — changing a resource amount, duration, or threshold. The alteration is physically made to the Accord document. Both parties notified in case."* Requires ARBITER to manage Accord document integrity.
2. **Resource — Redirect — Accord agreement:** The "small print" mechanic. *"The Syndicate transfers an existing Accord's obligations from one faction to another. The receiving faction is privately notified — they may accept or contest at the start of the next round."*
3. **Cross-Category — Reveal — Intel tokens held:** Economic intelligence. *"The Syndicate names a faction. ARBITER announces the count (not content) of Intel tokens that faction holds. The Syndicate may offer to purchase one token from the named faction at 3 Capital — the named faction may accept or decline."*

---

## 9. Design Principles Derived from Taxonomy

The following principles were established or confirmed during taxonomy development. They supplement the principles in Artifact 04 §5.

**Taxonomy principle 1 — Every card has a primary function.**
Cards may have secondary effects across multiple categories but their primary category and function must be clear. A card that does too many things across categories is a design problem.

**Taxonomy principle 2 — Faction-specific cards should fill gaps, not duplicate standard cards.**
Where standard cards already cover a function/target combination, faction-specific cards should either fill a gap or provide a meaningfully differentiated version (different restriction, scope, or scale).

**Taxonomy principle 3 — Symmetric categories enable symmetric learning.**
Board and Resource have the same four functions (Add, Remove, Recover, Redirect). A player who understands one category understands the other by analogy. New categories should maintain this symmetry where possible.

**Taxonomy principle 4 — Cross-Category functions need a clear reason for cross-category status.**
A function belongs in Cross-Category when its targets genuinely span multiple categories (Reveal, Shift) or when it modifies any target regardless of category (Protect, Corrupt).

**Taxonomy principle 5 — React conditions must be publicly observable.**
React fires on publicly countable or observable conditions. Hidden conditions are not valid React triggers. This maintains information integrity — you cannot react to information you shouldn't have.

**Taxonomy principle 6 — Permanent effects are more interesting than temporary ones.**
Principle 11 (Artifact 04) eliminated cross-round temporary effects. When designing new cards, prefer permanent effects over temporary ones.

---

## 10. Standalone Card Types — Taxonomy Exclusions

The following card types are excluded from the Category — Function — Subject taxonomy. They are not game-state actions targeting a Board, Resource, or Action element — they are meta-actions or structural components that operate on the play procedure rather than the game state.

**Pass cards (PS-01–PS-04)** — Excluded. Pass is a procedural declaration (this slot is intentionally empty / no political act declared). Any secondary effect on a Pass card (e.g., Findings gain, modifier draw) is incidental and does not constitute a taxonomy action. Pass cards carry no Category — Function — Subject fields.

**Modifier cards** — Excluded. Modifier cards alter the parameters of another card's resolution. They are resolved in Beat 2 against other cards, not against board or resource targets. Their effect is mediated by the operation they modify.

**Emergency Response cards** — Excluded. Trigger-based, pre-staged cards with fixed effects. Not submitted in dispatch cases or declared in the standard action sequence.

**React cards** — Excluded. React is a timing/interrupt mechanism that fires when a named publicly-observable condition is met. The trigger condition determines when the card activates; the card's primary effect carries its own Category — Function — Subject classification. React cards are not submitted in the standard action sequence — they fire automatically on condition.

*Source: Session 28 design note. Consistent with L115 (Art 04 owns all card design; card type determines scope, not taxonomy category).*

---

*End of Artifact 04b — Action Taxonomy & Design Analysis v1.3*
