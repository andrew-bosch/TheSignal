# 04b — ACTION TAXONOMY & DESIGN ANALYSIS
## THE SIGNAL P1 — Paper Prototype

**Version:** 1.8  
**Status:** ✅ Locked — v1.8 signed off S108 (04b-21). §4/§5 material changes require re-sign-off. §6–9 are working sections; updates do not require re-sign-off.  
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

### 4.4 Dual-aspect components

Some components have both quantitative and qualitative properties. The count of a component is an Economy property; the content or recorded state of a component is an Information property. These are separate, independently affectable properties:

| Component | Economy property | Information property |
|-----------|----------------|-------------------|
| Intel token | Count held by faction | Content written on token |
| Modifier card | Count held | What modifiers the card carries |
| Accord agreement | Whether an Accord exists | Recorded terms and obligations |

A card that adds an Intel token to the pool (STD.CA.5 Gather) is an Information card — the dominant design intent is intelligence acquisition, not resource accumulation. Token count is an Economy property of a held asset; card layer is classified by what the card's primary effect serves. A card that reveals the content of a token is an Information card. A card that introduces a token with falsified content (GHO.CA.5 Misdirection) is an Information card — the qualitative deception is the primary design intent, even though the Add primitive is also executed.

### 4.5 Protect distributes to the target's layer

A Protect card belongs to the layer of its protected target — it is not a cross-layer function.

### 4.6 Corrupt applies only to physically written or recorded values

Corrupt is classified in the Information layer. Scope is strict: applies only to values physically written or tracked in the paper prototype. Valid targets: Intel tokens (faction name only — see location constraint below), Accord agreements (terms written on document; named party on Accord form — L227), Target Profile (content within an operation bundle inside the dispatch case). Invalid: printed card text, marker positions (tracked by physical position, not written value), Chronicle (ARBITER narrative — not a mechanical game element), round-number field on Intel tokens (see below).

**Intel token location constraint (L222):** Intel tokens reside in the faction terminal (private zone — unreachable by an opposing card) or the ARBITER terminal (write-only by ARBITER). The only window where an opposing faction's Intel token is publicly accessible is when placed on a Public Act as payment (Beat 0 through Beat 4 PA resolution). Only tokens in that public-placement window are valid Corrupt targets. Own-faction modification of privately held tokens constitutes falsification of game state and is prohibited. Round-number field is additionally blocked by 7.2b: round number records the token's committed validity state (when it was created); altering it retroactively modifies that committed state.

### 4.7 No multi-Quarter temporary effects

Card effects use exactly one of four valid duration types: **Immediate** (resolved at beat; no lingering marker), **Transient** (removed at end of current Month), **Seasonal** (removed at end of current Quarter / Phase 21), or **Permanent** (persists for the remainder of the session until a named action or condition removes it). No card creates a state that expires after a defined number of Quarters. (Art 04 §5 P19; Art 00a §3.1)

### 4.8 ARBITER is the information authority — corollary to GR 10.1

The game contains hidden information: Intel tokens in private terminals, covert operations in sealed dispatch cases, modifier assignments, the covert resolution grid. Faction players must receive controlled disclosures of hidden state during play — SitRep reads, IntelDeliverySlips, SCIF results, Beat 3 grid entries. ARBITER is the only entity that can surface hidden information while preserving the covert structure: it controls what gets revealed, to whom, and when. Without ARBITER disclosure, the hidden information model has no legal output channel.

This is why ARBITER-reveal is outside GR 10.1. GR 10.1 protects faction players from being forced to expose what they strategically hold. ARBITER holds nothing strategically — it is not a participant competing for informational advantage. Its disclosure is the game's information system functioning. Narratively: ARBITER is The Witness. Its disclosure is The Signal surfacing what it already sees. Compelling another player's disclosure is a faction act; ARBITER surfacing its own knowledge is a game function.

**Portrait is the sole carveout** (Art 00a §5.1): Portrait is ARBITER-controlled and is never disclosed as a product of any card, script, or ARBITER procedure. The Witness reads the track; it does not broadcast it.

*(Art 00a GR 10.1b)*

### 4.14 Committed board states are final (GR 7.2b)

No card, Accord, World Condition, or ARBITER script may retroactively nullify or modify a committed board state. "Committed" means the state existed at resolution — the dice rolled, the effect applied, the token placed. Whatever followed is downstream of that state, not a revision of it.

This constraint eliminates the Recover function in its original sense (restoring a prior board state) and blocks any mechanic whose primary effect is reaching backward in the causal chain. Recover was retired S106 on this basis. GHO.CA.13 Backdate and GHO.CA.14 Field Verification are BLOCKED because both alter values that record committed states (round-number field on Intel tokens).

### 4.15 Reveal creates a stake, not a compulsion (GR 10.1)

The Reveal function does not force a player to disclose. It creates a consequence for the holder's choice — reveal and gain the benefit (or avoid the penalty), withhold and accept the alternative. The decision belongs to the player; the card sets the stakes. Any card where the Reveal effect fires without the holder's choice is a 10.1 violation regardless of framing.

See §4.13 for the ARBITER-reveal carveout.

### 4.16 Income generation is untouchable (GR 9.1)

Upkeep income flows from presence and structure output only. No card may directly modify a faction's income generation — neither to suppress it nor to amplify it beyond the board state. InfluenceTier is not a targetable component; it is derived from token counts, not written or placed independently. A card can affect income only by changing the underlying board state (adding or removing tokens), which changes the tier, which changes income naturally.

This distinguishes Economy — Remove — Native resource (removing tokens from a faction's current holdings) from income suppression (preventing tokens from generating at Upkeep). The former is permissible; the latter is not. DIR.PA.4 Regulatory Downgrade and DIR.PA.5 Regulatory Freeze are BLOCKED on this basis.

---

## 5. Card Taxonomy Index

*Card definitions are in Artifact 04. This index provides Layer — Function — Subject — Primitive Verb(s) assignments for all cards as a design reference. Use this table to identify coverage gaps and duplications.*

### 5.1 Column Definitions

**Layer** — which game system does this card affect?

| Layer | Visibility | Scope |
|-------|-----------|-------|
| Territory | Public | The influence landscape: presence tokens, structures, Dominant markers, spatial markers |
| Economy | Public | Quantitative holdings: native resources, token counts, card counts, Accord existence |
| Information | Private → Public | Qualitative content: token content, written records, attribution, reconnaissance |
| Submission | Split (covert = private, political = public) | What enters the resolution queue: costs, eligibility restrictions, blocks, operational scope. Cards that affect whether and how an action reaches resolution — before the dice roll. |
| Resolution | Split by phase | The d100 system: threshold, difficulty, modifier stack, Battlefield Strength, outcome scale. Cards that alter how the queue resolves — at or during the dice roll, not the submission of the action. |
| Standing | Split (Public Standing = public, Portrait = private) | Reputation tracks as affectable consequence registers |

**Function** — what does the card do to its subject?

| Function | Definition | Maps to Primitive Verb(s) |
|----------|------------|--------------------------|
| Add | Brings a new element into active play from supply or off-board | Add |
| Remove | Takes an element out of active play | Remove |
| Redirect | Changes ownership, destination, or allegiance of an element. Subsumes prior vocabulary: ownership change of a board element = Convert (Territory — Redirect); cross-faction resource movement = Transfer (Economy — Redirect). | Move |
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

**React, Instant, and Interrupt** — timing sub-functions within the Modifier card type that describe *when* a Modifier fires, not *what* it affects. Timing is a separate classification axis from Layer and Function: a Modifier is classified by its primary effect, not its trigger. Because Modifiers can target host actions from any layer, React/Instant/interrupt effects can appear across all layers — for example, Economy — Add — Native resource triggered by an opponent's resolved action (GUI.CA.2); Submission — Block on an Instant played in-flight; Information — Reveal triggered on attribution. React triggers must be publicly observable (Art 04 §5 P5). Full mechanic treatment — trigger conditions, stack behavior, observability requirements — is in Art 03 §18. A Timing column may be added to §5.2 when the full modifier timing model is locked.

**Valid Layer × Function Combinations** — `—` indicates a combination prohibited by governing rule or physical constraint. All other cells represent valid design space regardless of whether a card currently exists.

| Layer | Visibility | Add | Remove | Redirect | Modify | Protect | Block | Copy | Reveal | Shift | Corrupt |
|-------|-----------|-----|--------|---------|--------|---------|-------|------|--------|-------|---------|
| Territory | Public | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — |
| Economy | Public | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ |
| Information | Private → Public | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Submission | Split | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Resolution | Split by phase | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Standing | Split | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — |

*Invalid cells (—):*
- *Territory and Economy | Reveal: layer is fully public — no hidden state for a card to surface*
- *Territory | Corrupt: component positions are tracked by physical placement, not written values (§4.9)*
- *Resolution | Corrupt: no physically written or recorded values in the resolution system (§4.9)*
- *Standing | Add / Remove: subsumed by Shift — the Standing modification primitive*
- *Standing | Reveal: PS is public; Portrait is the sole prohibited reveal target — never surfaced by card effect (GR 10.1b)*
- *Standing | Corrupt: track positions are physical markers, not written values (§4.9)*
- *All non-Standing | Shift: Shift applies only to Standing track values*

### 5.2 Card Index

*Status key: ✅ Signed off — canonical, use for gap analysis. 📝 Draft — designed but not signed off. ⬜ Not yet designed. 🚫 Retired.*

| Card ID | Name | Status | Layer | Visibility | Function | Subject | Primitive Verb(s) |
|---------|------|--------|-------|------|----------|---------|-------------------|
| DIR.CA.1 | Invoke Jurisdiction | 📝 | Submission | Split | Block | Covert operation (STD.CA.1, STD.CA.3) | — |
| DIR.CA.2 | Detain | 📝 | Territory | Public | Move | Deployment marker | Move | *(taxonomy corrected S107 L226: success operation is game.move() to Detention zone; Remove was incorrect — Remove = return to supply; Detention zone is an active play area on Directorate's tableau. Art 04 spec function field correction tracked under 04-n105)* |
| DIR.CA.3 | Surveillance Placement | 📝 | Information | Private → Public | Reveal | CovertOperation | Reveal |
| DIR.CA.4 | Tactical Redirection | 📝 | Territory | Public | Move | PresenceToken | Move |
| DIR.CA.5 | Sanctioned Raid | 📝 | Territory | Public | Remove | PresenceToken | Remove |
| DIR.PA.1 | Regulatory Override | ⛔ BLOCKED | Submission | Split | Modify | PoliticalAct (add·PresenceChip cost) | — | Cost modification is not a physical verb; "cost" is not a component attribute. Card targets action cost for all Add·PresenceChip operations — requires new component + ARBITER overhead. Needs redesign. See PM05 04-n99. |
| DIR.PA.2 | Convene an Inquiry | 📝 | Information | Private → Public | Add | Intel token | Add |
| DIR.PA.3 | Entry/Exit Controls | 📝 | Territory | Public | Block | DeploymentMarker | — |
| DIR.PA.4 | Regulatory Downgrade | 🚫 BLOCKED | Territory | Public | Modify | InfluenceTier (derived — not targetable) | — | *L223: InfluenceTier is not a targetable component — tier is derived from influence token counts, not a placed or written value. Only board state changes (token add/remove) can affect tier. 9.1 prohibits direct income modification by card. Fundamental redesign required (04-n104).* |
| DIR.PA.5 | Regulatory Freeze | 🚫 BLOCKED | Territory | Public | Block | InfluenceTier (derived — not targetable) | — | *L223: Same subject violation — InfluenceTier not a targetable component. Additionally, Block targets actions (not derived states); Block\|InfluenceTier is a subject mismatch. Fundamental redesign required (04-n104).* |
| DIR.PA.6 | Standing Injunction | 📝 | Submission | Split | Block | Political act | — |
| GHO.CA.1 | Pattern Match | ✅ | Submission | Split | Copy | Covert operation (full) | Invoke |
| GHO.CA.2 | Intercept | 📝 | Information | Private → Public | Reveal | CovertOperation | Reveal |
| GHO.CA.3 | Dossier Breach | 📝 | Information | Private → Public | Reveal | IntelDeliverySlip | Reveal |
| GHO.CA.4 | Deep Cover | 📝 | Information | Private → Public | Remove | IntelToken | Remove |
| GHO.CA.5 | Misdirection | 📝 | Information | Private → Public | Add | Intel token (corrupt content) | Add + Corrupt |
| GHO.CA.6 | Synthesize | 📝 | Economy | Public | Add | IntelToken | Add |
| GHO.CA.7 | Station | 📝 | Information | Private → Public | Add | IntelToken | Add |
| GHO.CA.8 | Full Take | 📝 | Information | Private → Public | Add | IntelToken | Add |
| GHO.CA.9 | SCIF | 📝 | Information | Private → Public | Add | DebriefActionCard | Add |
| GHO.CA.10 | Flip | 📝 | Economy | Public | Add | FactionNativeResource | Add |
| GHO.CA.11 | Signals Analysis | 📝 | Information | Private → Public | Reveal | ClassifiedDirective | Reveal |
| GHO.CA.12 | Source Substitution | 📝 | Information | Private → Public | Corrupt | Intel token | Corrupt |
| GHO.CA.13 | Backdate | 🚫 BLOCKED | Information | Private → Public | Corrupt | Intel token (round-number field) | Corrupt | *L222: (1) Location constraint — Intel token in private terminal zone unreachable by opposing card; only publicly placed tokens (PA payment window) are valid Corrupt targets. (2) 7.2b — round-number records committed validity state; altering it is retroactive modification. §4.10 revised. Art 04 spec: BLOCKED pending redesign (04-n103).* |
| GHO.CA.14 | Field Verification | 🚫 BLOCKED | Information | Private → Public | Corrupt | Intel token (age field) | Corrupt | *7.2b violation: mechanic alters committed token age field retroactively. Fundamental redesign required. G-ext id retired. Art 04 spec: BLOCKED pending redesign (04-n103).* |
| GHO.PA.1 | Publish Analysis | 📝 | Information | Private → Public | Reveal | Action attribution | Reveal |
| GHO.PA.2 | Signal Review Request | 📝 | Resolution | Split by phase | Modify | Covert operation (difficulty) | — |
| GHO.PA.3 | Declassified Records | 📝 | Information | Public | Remove | Intel token (expired) | Remove |
| GHO.PA.4 | Public Threat Assessment | 📝 | Information | Private → Public | Reveal | Broadcast Effect Card | Reveal |
| GHO.PA.5 | Agency Recruitment Fair | 📝 | Territory | Public | Add | PresenceToken | Add |
| GHO.MOD.1 | Clarify Misinformation | 📝 | Information | Public | Remove | IntelToken | Remove | *ModifierCard/React — taxonomy excluded from §11.1 per modifier card rules (S110)* |
| GUI.CA.1 | Fortify Structure | ✅ | Territory | Public | Protect | Structure block | — |
| GUI.CA.2 | Materials Acquisition | ✅ | Economy | Public | Add | Native resource | Add | *(function: Recover → Add, S106 — 04b-20; Art 04 spec fix pending 04-n103)*
| GUI.CA.3 | Foundation Rights | ✅ | Territory | Public | Add | Presence token | Add |
| GUI.CA.4 | Construction Crew | ✅ | Submission | Split | Remove Restriction | Covert operation (presence requirement) | — |
| GUI.CA.5 | Infrastructure Yield | ✅ | Economy | Public | Add | Native resource | Add |
| GUI.CA.6 | Labor Contract | 📝 | Economy | Public | Add | NativeResource | Add | *(function: Recover → Add, S106 — 04b-20; card_id GUI.CA.6 assigned; Art 04 spec fix pending 04-n103)*
| GUI.PA.1 | Civic Works Mandate | 📝 | Territory | Public | Add | Structure block | Add |
| GUI.PA.2 | Infrastructure Bond | 📝 | Economy | Public | Add | Accord agreement | Add |
| NET.CA.1 | Leak | 📝 | Information | Private → Public | Reveal | District | Reveal |
| NET.CA.2 | Disclosure Loop | 📝 | Economy | Public | Add | Exposure | Add |
| NET.CA.3 | Breaking News | 📝 | Information | Private → Public | Reveal | CovertOperation | Reveal |
| NET.CA.4 | Network Cascade | 📝 | Submission | Split | Modify | PoliticalAct | — |
| NET.CA.5 | Community Anchor | 📝 | Territory | Public | Add | Presence token | Add |
| NET.CA.6 | Sacrifice | 📝 | Economy | Public | Add | IntelToken | Add |
| NET.MOD.1 | Signal Break | 📝 | ModifierCard — taxonomy excluded §5.1 | — | — | — | — |
| NET.MOD.2 | Reputational Strike | 📝 | ModifierCard — taxonomy excluded §5.1 | — | — | — | — |
| NET.PA.1 | Public Disclosure | 📝 | Information | Private → Public | Reveal | Action attribution | Reveal |
| NET.PA.2 | Community Rally | 📝 | Territory | Public | Add | Presence token | Add |
| NET.PA.3 | Live Coverage | 📝 | Information | Private → Public | Reveal | FactionHand | Reveal |
| STD.CA.1 | Build Structure | ✅ | Territory | Public | Add | Structure block | Add |
| STD.CA.2 | Demolish | ✅ | Territory | Public | Remove | Structure block | Remove |
| STD.CA.3 | Campaign | ✅ | Territory | Public | Add | Presence token | Add |
| STD.CA.4 | Undermine | ✅ | Territory | Public | Remove | Presence token | Remove |
| STD.CA.5 | Gather | ✅ | Information | Private → Public | Add | Intel token | Add |
| STD.CA.6 | Broadcast Interference | ✅ | Submission | Split | Modify | Political act (cost) | — |
| STD.CA.7 | Amplify | ✅ | Resolution | Split by phase | Modify | Political act (outcome scale) | — |
| STD.CA.8 | Buy Influence | ✅ | Territory | Public | Add | Presence token | Add |
| STD.CA.9 | Fund | ✅ | Economy | Public | Redirect | Native resource | Move |
| STD.CA.10 | Protect | ✅ | Resolution | Split by phase | Protect | Covert operation (difficulty) | — |
| STD.CA.11 | Tort Interference | 📝 | Information | Private → Public | Corrupt | Accord | Corrupt |
| STD.CA.12 | Absolute Compromise | 📝 | Submission | Split | Block | CovertOperation | — |
| STD.CA.13 | Disinformation Campaign | 📝 | Standing | Split | Shift | Public Standing | Move |
| STD.CA.14 | Disprove | 📝 | Economy | Public | Remove | Intel token | Remove |
| STD.CA.15 | Intel Extraction | 📝 | Economy | Public | Redirect | Intel token | Move |
| STD.CA.16 | Modifier Raid | 📝 | Economy | Public | Redirect | Modifier card | Move |
| STD.MOD.1 | Overture | 📝 | ModifierCard — taxonomy excluded §5.1 | — | — | — | — |
| STD.PA.1 | Open Operations | 📝 | Territory | Public | Add | Presence token | Add |
| STD.PA.2 | Disputed Claim | 📝 | Territory | Public | Remove | Presence token | Remove |
| STD.PA.3 | Public Commission | 📝 | Territory | Public | Add | Structure block | Add |
| STD.PA.4 | Public Censure | 📝 | Standing | Split | Shift | Public Standing (−) | Move |
| STD.PA.5 | On the Record | 📝 | Information | Private → Public | Reveal | Action attribution | Reveal |
| STD.PA.6 | Economic Sanction | 📝 | Economy | Public | Remove | Native resource | Remove |
| STD.PA.7 | Public Address | 📝 | Standing | Split | Shift | Public Standing (+) | Move |
| STD.PA.8 | Table an Accord | 📝 | Economy | Public | Add | Accord agreement | Add |
| SYN.CA.1 | Leveraged Acquisition | 📝 | Economy | Public | Add | Native resource | Add |
| SYN.CA.2 | Short the Market | 📝 | Economy | Public | Remove | Native resource | Remove |
| SYN.CA.3 | Hostile Acquisition | 📝 | Territory | Public | Redirect | Structure block | Move |
| SYN.CA.4 | Golden Parachute | 📝 | Economy | Public | Protect | Native resource | — |
| SYN.CA.5 | Regulatory Capture | 📝 | Submission | Split | Block | Named action type | — |
| SYN.CA.6 | Parasitic | 📝 | Economy | Public | Add | IntelToken | Add |
| SYN.CA.7 | Corporate Blackmail | 📝 | Economy | Public | Redirect | NativeResource | Move |
| SYN.CA.8 | Land Title | 📝 | Territory | Public | Add | StructureBlock | Add |
| SYN.CA.9 | Hostile Takeover | 📝 | Territory | Public | Add | PresenceToken | Add |
| SYN.CA.10 | Accord Transfer | 📝 | Economy | Covert | Corrupt | AccordCard | Corrupt | S111: full design pass; Art 06 §9.10 confirmed (L205); d100 threshold 50; crit = incoming party elects numeric term change |
| SYN.CA.11 | Redline | 📝 | Information | Covert | Corrupt | AccordAgreement | Corrupt | S111: new card; fills Information\|Corrupt\|AccordAgreement gap; d100 threshold 50; alters numeric fill-in on active Accord form |
| SYN.MOD.1 | Accord Leverage | 📝 | ModifierCard — taxonomy excluded §5.1 | — | — | — | — |
| SYN.PA.1 | Acquisition Offer | 📝 | Territory | Public | Redirect | Presence token | Move |
| SYN.PA.2 | Public Dividend | 📝 | Economy | Public | Add | Native resource (conditional) | Add |
| SYN.PA.3 | Data Acquisition | 📝 | Information | Public | Reveal | IntelTokensHeld | Reveal | S111: new card; fills Information\|Reveal\|IntelTokensHeld gap; ElectPlayer; Permanent React on decline |

---

## 6. Coverage Analysis — Gaps and Concentrations

### 6.1 Unused taxonomy combinations

The following combinations exist in the taxonomy but have no current card. Layer and Function definitions are included to prompt the core design question: *is there a narrative reason to perform this action in this game system?* If yes, it is a candidate for card development.

---

**Layer: Territory** — *The influence landscape: presence tokens, structures, control flags, spatial markers*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Redirect | Changes ownership, destination, or allegiance of an element | Structure | Low | Transfer structure faction — SYN.CA.3 partially covers |

**Layer: Economy** — *Quantitative holdings: native resources, token counts, card counts, Accord existence*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Remove | Takes an element out of active play | Modifier card | Medium | Strip opponent modifier cards |
| Remove | Takes an element out of active play | Accord agreement | High | Break Accord covertly — important missing mechanic |
| Redirect | Changes ownership, destination, or allegiance of an element | Accord agreement | High | "Small print" mechanic — Syndicate doctrine. **Unaddressed (L227):** Accord Transfer reclassified as Economy\|Corrupt\|AccordCard — party-name replacement is written-value corruption, not ownership redirect. Economy\|Redirect\|AccordAgreement remains an open coverage gap. |

**Layer: Submission** — *What enters the resolution queue: costs, eligibility, blocks, scope*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Copy | Duplicates another action's effect chain with a new initiating subject | Political act | Low | Copy opponent political act |
| Copy | Duplicates another action's effect chain with a new initiating subject | Subset only | Medium | Copy target or effect only — Ghost doctrine. ⚠️ Partial-copy mechanism needed in action model |

**Layer: Information** — *Qualitative content: token content, written records, attribution, reconnaissance*

| Function | Definition | Subject | Priority | Notes |
|---|---|---|---|---|
| Reveal | Makes hidden information visible to a named audience | Modifier cards held | Medium | Disclose individual modifier card contents |
| Reveal | Makes hidden information visible to a named audience | Named faction only | High | Targeted disclosure — Ghost intelligence delivery. ⚠️ Target-scope/filter system needed |
| Corrupt | Alters a physically written or recorded value on a component | Intel token | High | Falsify Intel token content. Location constraint (L222): token must be in public-placement window (on PA as payment) — private terminal tokens unreachable. Partially addressed: Source Substitution (📝, faction-name field only); Backdate (🚫 BLOCKED L222 — round-number additionally prohibited by 7.2b). Full-field arbitrary corruption remains an open gap. |

**Layer: Standing** — *Reputation tracks: Public Standing and Portrait*

*All open gaps addressed or retired as of S108.*

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

*Rebuilt S104 from Art 04 card data; targeted update S108 for newly IDed cards. Standard column = faction=All cards and Political Acts (P-prefix). Faction columns = faction-specific cards only.*

| Layer | Function | Subject | Standard | Guild | Ghost | Directorate | Network | Syndicate |
|-------|----------|---------|----------|-------|-------|-------------|---------|-----------|
| **Territory** | | | | | | | | |
| | Add | Presence token | STD.CA.3, STD.CA.8 | GUI.CA.3 | GHO.PA.5 | — | NET.CA.5, NET.MOD.1 | SYN.CA.9 |
| | Add | Structure block | STD.CA.1 | — | — | — | — | SYN.CA.8 |
| | Block | Deployment marker | — | — | — | DIR.PA.3 | — | — |
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
| | Add | FactionNativeResource | — | — | GHO.CA.10 | — | — | — |
| | Remove | Native resource | STD.PA.6 | — | — | — | — | SYN.CA.2 |
| | Remove | Intel token | STD.CA.14 | — | — | — | — | — |
| | Remove | Accord agreement | — | — | — | — | — | — |
| | Redirect | Native resource | STD.CA.9 | — | — | — | — | SYN.CA.7 |
| | Redirect | Intel token | STD.CA.15 | — | — | — | — | — |
| | Redirect | Modifier card | STD.CA.16 | — | — | — | — | — |
| | Redirect | Accord agreement | — | — | — | — | — | — |
| | Corrupt | AccordCard (named party) | — | — | — | — | — | SYN.CA.10 |
| | Protect | Native resource | — | — | — | — | — | SYN.CA.4 |
| **Information** | | | | | | | | |
| | Add | Intel token | STD.CA.5, DIR.PA.2 | — | GHO.CA.5, GHO.CA.7, GHO.CA.8 | — | — | — |
| | Add | DebriefActionCard | — | — | GHO.CA.9 | — | — | — |
| | Reveal | CovertOperation | — | — | GHO.CA.2 | DIR.CA.3 | NET.CA.3 | — |
| | Reveal | IntelDeliverySlip | — | — | GHO.CA.3 | — | — | — |
| | Reveal | District | — | — | — | — | NET.CA.1 | — |
| | Reveal | FactionHand | — | — | — | — | NET.PA.3 | — |
| | Reveal | Action attribution | STD.PA.5, NET.PA.1, GHO.PA.1 | — | — | — | — | — |
| | Reveal | ClassifiedDirective | — | — | GHO.CA.11 | — | — | — |
| | Remove | Intel token | — | — | GHO.CA.4, GHO.PA.3, GHO.MOD.1 | — | — | — |
| | Corrupt | Accord | STD.CA.11 | — | — | — | — | — |
| | Corrupt | Intel token | — | — | GHO.CA.12 | — | — | — |
| **Submission** | | | | | | | | |
| | Block | CovertOperation | STD.CA.12 | — | — | DIR.CA.1 | — | — |
| | Block | Named action type | — | — | — | — | — | SYN.CA.5 |
| | Block | Political act | — | — | — | DIR.PA.1 ⛔, DIR.PA.6 | — | — |
| | Modify | Political act | STD.CA.6 | — | — | — | NET.CA.4 | — |
| | Copy | CovertOperation | — | — | GHO.CA.1 | — | — | — |
| | Remove Restriction | CovertOperation | — | GUI.CA.4 | — | — | — | — |
| **Resolution** | | | | | | | | |
| | Modify | Outcome scale | STD.CA.7 | — | — | — | — | — |
| | Modify | Difficulty | GHO.PA.2 | — | — | DIR.CA.8 | — | — |
| | Protect | CovertOperation | STD.CA.10 | — | — | — | — | — |
| **Standing** | | | | | | | | |
| | Shift | Public Standing | STD.CA.13, STD.PA.4, STD.PA.7 | — | — | DIR.CA.7 | NET.CA.7 | — |

---

## 8. Design Recommendations by Faction

These recommendations inform the redesign decisions D-04-02 through D-04-05 in Artifact 04 §16.

### 8.1 Ghost — Priority redesign targets

Current Ghost set (S108): GHO.CA.1 (Submission|Copy|CovertOp), GHO.CA.2 (Information|Reveal|CovertOp), GHO.CA.3 (Information|Reveal|IntelDeliverySlip), GHO.CA.4 (Information|Remove|IntelToken), GHO.CA.5 (Information|Add|IntelToken), GHO.CA.6 (Economy|Add|IntelToken), GHO.CA.7 Station (Information|Add|IntelToken), GHO.CA.8 Full Take (Information|Add|IntelToken), GHO.CA.9 SCIF (Information|Add|DebriefActionCard), GHO.CA.10 Flip (Economy|Add|FactionNativeResource), GHO.CA.11 Signals Analysis (Information|Reveal|ClassifiedDirective), GHO.CA.12 Source Substitution (Information|Corrupt|IntelToken), GHO.CA.13 Backdate (🚫 BLOCKED L222+7.2b), GHO.CA.14 Field Verification (🚫 BLOCKED 7.2b). Ghost now has the deepest Information suite of any faction — generation, interception, disclosure, delivery tracking, removal, and corruption all represented. Two design space entries remain blocked pending fundamental redesign (04-n103). Portrait pathway remains closed (L84, 00a R01); see PM05 04-11.

**High priority:**
1. **Information — Reveal — Named faction:** Ghost delivers targeted intelligence to a specific faction privately rather than the whole table. *Targeted intelligence disclosure that strengthens relationships without public exposure.* ⚠️ Target-scope/filter system needed before this can be specified.
2. **Submission — Copy — Subset:** Ghost should have a partial copy card — copy only the target (apply your own operation to the same district as named faction) without replicating the full cost and effect. ⚠️ Partial-copy mechanism needed in action model.

**Blocked — redesign required:**
3. **GHO.CA.13 Backdate / GHO.CA.14 Field Verification** — both target Intel token provenance fields (Information|Corrupt|Intel token): Backdate aimed at the round-number field (when the token was committed); Field Verification aimed at the age/validity field. Both blocked by 7.2b — those fields record committed facts and cannot be retroactively altered. Design intent: manipulation of token temporal provenance — making intelligence appear more or less current than it is. Valid redesign path: alteration of committed provenance fields is permanently closed. The mechanic must be additive — plant a new token that mimics a different temporal signature, or affect how token age is read (e.g., a modifier shifting the effective staleness threshold for a target faction) rather than altering the token itself. Both cards require fundamental redesign; specs blocked at Art 04 (04-n103).

**New PA/React design targets (S108):**
4. **GHO.PA.3 Declassified Records** — ✅ Design pass S109. Taxonomy: Information|Remove|IntelToken (expired). Cost: 1 Findings. Restriction: hold ≥1 expired Intel token. Boost: expired Intel tokens (each = 1 BM-xx at Beat 4 §9.4.3.1.0.0); BM-xx multiplies all effects ×(1+n). Success: +1 PS; successcrit: +1 PS additional; failcrit: −1 PS. Art 03 boost detection sub-step added §9.4.3.1.0.0 (S109). See Art 04 GHO.PA.3.
5. **GHO.PA.4 Public Threat Assessment** — ✅ Design pass S109. Taxonomy: Information|Reveal|BroadcastEffectCard. Automatic. Cost: 1 Findings. Restriction: ≥1 active BC in Situation Report Zone. Target object: named BC (recorded on Target Profile — target-object field added S109). Success: ARBITER reveals linked BEC to all players, returns to Tableau; Ghost +1 PS. BC/BEC link via §7.2.1 — no new mechanism required. Art 03 §9.4.3.3.0 clause added (S109). Art 02 DB:48 target-object field added (S109). See Art 04 GHO.PA.4.
6. **GHO.PA.5 → GHO.MOD.1 Clarify Misinformation** — ✅ Design pass S110. Redesigned as ModifierCard/React (Modifier deck, not PA deck). Taxonomy: Information|Remove|IntelToken. Trigger: any faction places PA with Intel token at §9.2.0. Ghost declares faction named on token (Prediction resolution); ARBITER checks privately. Match: token removed, PA cancelled, resources drained to Reservoir, Ghost +1 PS. No match: card consumed, PA proceeds. Intelligence-gated: Target Profile face-down at §9.2.0 (Art 03 v4.10). See Art 04 §11.8 GHO.MOD.1.
7. **GHO.PA.5 Agency Recruitment Fair** — ✅ Design pass S110. Taxonomy: Territory|Add|PresenceToken. Cost: 1 Findings. Restriction: district.resource_type == Findings (University Perimeter, Data Exchange, Research Institute, Chorus Research — 4 districts); adjacency per Design Pillar [04-n6 pending]. Beat 4, d100 threshold 50. Ring mod: Ring3 +10, Ring1 −15. Success: +2 PresenceTokens; successcrit: +1 PS; failcrit: −1 PS. Ghost's only territory PA — operates in the open in knowledge districts. See Art 04 GHO.PA.5.

### 8.2 Directorate — Priority redesign targets

Current Directorate set (S108): DIR.CA.1 (Submission|Block|CovertOp), DIR.CA.2 (Territory|Move|DeploymentMarker — taxonomy corrected S107 L226), DIR.CA.3 (Information|Reveal|CovertOp), DIR.CA.4 (Territory|Move|PresenceToken), DIR.CA.5 (Territory|Remove|PresenceToken), DIR.CA.6 (Economy|Add|NativeResource ✅ S106), DIR.CA.7 (Standing|Shift|PublicStanding ✅ S106), DIR.CA.8 (Resolution|Modify|Difficulty ✅ S106), DIR.PA.3 Entry/Exit Controls (Territory|Block|DeploymentMarker), DIR.PA.4 Regulatory Downgrade (🚫 BLOCKED L223), DIR.PA.5 Regulatory Freeze (🚫 BLOCKED L223), DIR.PA.6 Standing Injunction (Submission|Block|PoliticalAct). Effective Block count: DIR.CA.1 (CovertOp), DIR.PA.6 (PoliticalAct). DIR.PA.1 (⛔ BLOCKED, PM05 04-n99) unresolved.

**High priority:**
1. **Economy — Add — Native resource (Mandate):** ✅ DIR.CA.6 Institutional Audit (S106). Beat 3 d100 threshold 50; yield = count of active Directorate Permanents in target ring; restriction chip count > 1.
2. **Standing — Shift — Public Standing (primary covert):** ✅ DIR.CA.7 Institutional Brief (S106). Beat 3 d100 threshold 50; PS yield = count of active Directorate Permanents in target ring; same architecture as DIR.CA.6. Mechanism: closed-channel circulation of institutional record — covert authorship, public confidence signal.

**Medium priority:**
3. **Resolution — Modify — Difficulty (increasing, against all factions):** ✅ DIR.CA.8 Enhanced Scrutiny (S106). Beat 2 Automatic; ARBITER places −15 Modifier tokens on each Beat 3 row targeting district; all factions including Directorate.

**Blocked — redesign required:**
4. **DIR.PA.4 Regulatory Downgrade / DIR.PA.5 Regulatory Freeze** — both target InfluenceTier (Territory|Modify and Territory|Block respectively). Blocked: InfluenceTier is a derived state (calculated from token counts), not a placed component; GR 9.1 prohibits direct income modification by card. Design intent: economic suppression — reduce or freeze a rival's territorial income. Valid redesign path: income suppression must work through board state. Territory|Remove|PresenceToken is the permitted approach — token removal reduces tier, which reduces income naturally. A PA version (public, political character) would be distinct from DIR.CA.5 Sanctioned Raid (covert). Design the pair together; specs blocked at Art 04 (04-n104).
5. **DIR.PA.1 Regulatory Override** — attempted Submission|Modify|PoliticalAct (add·PresenceChip cost) — a district-wide cost increase on presence operations for all factions. Blocked: "cost" is not a physical component attribute; no board object represents operation cost. Valid redesign path: requires a physical regulatory burden component placed on districts that ARBITER reads when processing operations — a new component design question touching Art 02 (registration), Art 03 (procedure for applying modifier), and Art 07 (ARBITER overhead). Prerequisite to redesign: define the component and Art 03 procedure. PM05 04-n99.

### 8.3 Network — Priority redesign targets

Current Network set (S104): NET.CA.1 (Information|Reveal|District), NET.CA.2 (Economy|Add|Exposure), NET.CA.3 (Information|Reveal|CovertOp), NET.CA.4 (Submission|Modify|PoliticalAct), NET.CA.5 (Territory|Add|PresenceToken), NET.CA.6 (Economy|Add|IntelToken), NET.PA.3 (Information|Reveal|FactionHand). NET.CA.2's redesign to Economy|Add|Exposure resolved the prior doctrinal contradiction. Network now holds three Reveal cards (NET.CA.1, NET.CA.3, NET.PA.3) across distinct subjects — mechanical differentiation between them must be enforced in card specs.

**High priority:**
1. **Standing — Shift — Public Standing (primary covert):** ✅ NET.CA.7 Ground Signal (S106). Beat 3 d100 threshold 50; success +1 PS; restriction IL ≤ Established (Dominant excluded — no outreach needed); successcrit +1 chip in target district + +1 PS additional. Doctrinal grounding: existing street presence made legible without announcement.
2. **Territory — Add — Presence token (React trigger):** ✅ Signal Break (S106). ModifierCard / React; trigger = PA success causing board state change (influence or structure, + or −) in district; target district fixed by trigger; Exposure×1; d100 threshold 50; success +1 chip; successcrit +1 PS; fail no effect; failcrit −1 PS. Full spec written to Art 04 §11.8. Schema pass pending (04-n4).

**Medium priority:**
3. **Consolidate NET.CA.1 and NET.CA.3:** NET.CA.1 reveals District-level data; NET.CA.3 reveals CovertOperation. Subjects are distinct — if both are retained, card specs must enforce clear mechanical differentiation; if consolidated, the broader subject scope needs defining.

### 8.4 Syndicate — Priority redesign targets

Current Syndicate set (S111): SYN.CA.1 (Economy|Add|NativeResource), SYN.CA.2 (Economy|Remove|NativeResource), SYN.CA.3 (Territory|Redirect|StructureBlock), SYN.CA.4 (Economy|Protect|NativeResource), SYN.CA.5 (Submission|Block|NamedActionType), SYN.CA.6 (Economy|Add|IntelToken), SYN.CA.7 (Economy|Redirect|NativeResource), SYN.CA.8 Land Title (Territory|Add|StructureBlock), SYN.CA.9 Hostile Takeover (Territory|Add|PresenceToken), SYN.CA.10 Accord Transfer (Economy|Corrupt|AccordCard), SYN.CA.11 Redline (Information|Corrupt|AccordAgreement), SYN.PA.3 Data Acquisition (Information|Reveal|IntelTokensHeld). Economy depth remains Syndicate's defining characteristic; SYN.CA.8/9 add a meaningful Territory foothold. SYN.CA.10/11 complete the Accord manipulation suite (who is bound; what the terms say). SYN.CA.11 and SYN.PA.3 give Syndicate its first direct Information-layer capability.

**High priority:**
1. **Information — Corrupt — Accord agreement:** Alter the recorded terms of an existing Accord. *"The Syndicate may alter one numeric value in any registered Accord — changing a resource amount, duration, or threshold. The alteration is physically made to the Accord document. Both parties notified in case."* Requires ARBITER to manage Accord document integrity.
2. **Economy — Redirect — Accord agreement:** The "small print" mechanic. **Unaddressed (L227):** Accord Transfer reclassified as Economy|Corrupt|AccordCard — party-name replacement is alteration of a written record on the Accord form, not a redirect of ownership. Economy|Redirect|AccordAgreement remains an open coverage gap — no card addresses the mechanic of transferring Accord *obligations* between factions as a redirect operation.
3. **Economy — Corrupt — AccordCard (named party):** ✅ SYN.CA.10 Accord Transfer (L227 — pending Art 06 implementation).
4. **Information — Reveal — Intel tokens held:** Economic intelligence. *"The Syndicate names a faction. ARBITER announces the count (not content) of Intel tokens that faction holds. The Syndicate may offer to purchase one token from the named faction at 3 Capital — the named faction may accept or decline."*

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
