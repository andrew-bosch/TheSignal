# 04b — ACTION TAXONOMY & DESIGN ANALYSIS
## THE SIGNAL P1 — Paper Prototype

**Version:** 1.9  
**Status:** ✅ Locked — v1.8 signed off S108 (04b-21). §4/§5 material changes require re-sign-off. §6–9 are working sections; updates do not require re-sign-off. v1.9: §5.2 card index and §7 faction coverage matrix relocated to Art 04 §8/§9 (S116); §8 completed items removed.  
**Last Updated:** 2026-06-24  
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
| §5 | [Card Taxonomy Index](#5-card-taxonomy-index) — Column definitions and Layer × Function validity matrix; card index → Art 04 §8 |
| §6 | [Coverage Analysis — Gaps and Concentrations](#6-coverage-analysis-gaps-and-concentrations) |
| §7 | [Faction Coverage Matrix](#7-faction-coverage-matrix) — Relocated to Art 04 §9 |
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
- *Territory | Corrupt: component positions are tracked by physical placement, not written values (§4.6)*
- *Resolution | Corrupt: no physically written or recorded values in the resolution system (§4.6)*
- *Standing | Add / Remove: subsumed by Shift — the Standing modification primitive*
- *Standing | Reveal: PS is public; Portrait is the sole prohibited reveal target — never surfaced by card effect (GR 10.1b)*
- *Standing | Corrupt: track positions are physical markers, not written values (§4.6)*
- *All non-Standing | Shift: Shift applies only to Standing track values*

### 5.2 Card Index

*Relocated to Art 04 §8. See Art 04 §8 — Card Taxonomy Index.*

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

*Relocated to Art 04 §9. See Art 04 §9 — Faction Coverage Matrix.*

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

### 8.2 Directorate — Priority redesign targets

Current Directorate set (S108): DIR.CA.1 (Submission|Block|CovertOp), DIR.CA.2 (Territory|Move|DeploymentMarker — taxonomy corrected S107 L226), DIR.CA.3 (Information|Reveal|CovertOp), DIR.CA.4 (Territory|Move|PresenceToken), DIR.CA.5 (Territory|Remove|PresenceToken), DIR.CA.6 (Economy|Add|NativeResource ✅ S106), DIR.CA.7 (Standing|Shift|PublicStanding ✅ S106), DIR.CA.8 (Resolution|Modify|Difficulty ✅ S106), DIR.PA.3 Entry/Exit Controls (Territory|Block|DeploymentMarker), DIR.PA.4 Regulatory Downgrade (🚫 BLOCKED L223), DIR.PA.5 Regulatory Freeze (🚫 BLOCKED L223), DIR.PA.6 Standing Injunction (Submission|Block|PublicAct). Effective Block count: DIR.CA.1 (CovertOp), DIR.PA.6 (PublicAct). DIR.PA.1 (⛔ BLOCKED, PM05 04-n99) unresolved.

**Blocked — redesign required:**
1. **DIR.PA.4 Regulatory Downgrade / DIR.PA.5 Regulatory Freeze** — both target InfluenceTier (Territory|Modify and Territory|Block respectively). Blocked: InfluenceTier is a derived state (calculated from token counts), not a placed component; GR 9.1 prohibits direct income modification by card. Design intent: economic suppression — reduce or freeze a rival's territorial income. Valid redesign path: income suppression must work through board state. Territory|Remove|PresenceToken is the permitted approach — token removal reduces tier, which reduces income naturally. A PA version (public, political character) would be distinct from DIR.CA.5 Sanctioned Raid (covert). Design the pair together; specs blocked at Art 04 (04-n104).
2. **DIR.PA.1 Regulatory Override** — attempted Submission|Modify|PublicAct (add·PresenceChip cost) — a district-wide cost increase on presence operations for all factions. Blocked: "cost" is not a physical component attribute; no board object represents operation cost. Valid redesign path: requires a physical regulatory burden component placed on districts that ARBITER reads when processing operations — a new component design question touching Art 02 (registration), Art 03 (procedure for applying modifier), and Art 07 (ARBITER overhead). Prerequisite to redesign: define the component and Art 03 procedure. PM05 04-n99.

### 8.3 Network — Priority redesign targets

Current Network set (S104): NET.CA.1 (Information|Reveal|District), NET.CA.2 (Economy|Add|Exposure), NET.CA.3 (Information|Reveal|CovertOp), NET.CA.4 (Submission|Modify|PublicAct), NET.CA.5 (Territory|Add|PresenceToken), NET.CA.6 (Economy|Add|IntelToken), NET.PA.3 (Information|Reveal|FactionHand). NET.CA.2's redesign to Economy|Add|Exposure resolved the prior doctrinal contradiction. Network now holds three Reveal cards (NET.CA.1, NET.CA.3, NET.PA.3) across distinct subjects — mechanical differentiation between them must be enforced in card specs.

**Medium priority:**
1. **Consolidate NET.CA.1 and NET.CA.3:** NET.CA.1 reveals District-level data; NET.CA.3 reveals CovertOperation. Subjects are distinct — if both are retained, card specs must enforce clear mechanical differentiation; if consolidated, the broader subject scope needs defining.

### 8.4 Syndicate — Priority redesign targets

Current Syndicate set (S111): SYN.CA.1 (Economy|Add|NativeResource), SYN.CA.2 (Economy|Remove|NativeResource), SYN.CA.3 (Territory|Redirect|StructureBlock), SYN.CA.4 (Economy|Protect|NativeResource), SYN.CA.5 (Submission|Block|NamedActionType), SYN.CA.6 (Economy|Add|IntelToken), SYN.CA.7 (Economy|Redirect|NativeResource), SYN.CA.8 Land Title (Territory|Add|StructureBlock), SYN.CA.9 Hostile Takeover (Territory|Add|PresenceToken), SYN.CA.10 Accord Transfer (Economy|Corrupt|AccordCard), SYN.CA.11 Redline (Information|Corrupt|AccordAgreement), SYN.PA.3 Data Acquisition (Information|Reveal|IntelTokensHeld). Economy depth remains Syndicate's defining characteristic; SYN.CA.8/9 add a meaningful Territory foothold. SYN.CA.10/11 complete the Accord manipulation suite (who is bound; what the terms say). SYN.CA.11 and SYN.PA.3 give Syndicate its first direct Information-layer capability.

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
