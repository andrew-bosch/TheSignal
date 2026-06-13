# 00a — GOVERNING RULES & DESIGN POLICY
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.8 — Signed Off — S83 (§11 added — L108 Data Table Standard migrated from 00b §3)  
**Status:** Signed Off  
**Last Updated:** 2026-06-09  
**Companion to:** 00 — Factions, World & Narrative Context  
**Depends on:** 00, 01, 02, 03, 04, 04b

---

## 1. Overview

### Problem This Document Solves

Design questions arise that cannot be answered by reading the five pillars alone, and re-deriving answers from narrative descriptions across multiple artifacts is slow and inconsistent. This document captures explicit, testable, binding rules derived from all design decisions made across the signed-off artifact set. It is the first reference when a design question arises.

---

### How to Use This Document

When evaluating a proposed card, mechanic, or ruling: check the relevant section here before going to the source artifact. Rules are stated with a canonical rule statement, narrative grounding, and mechanical expression. If a proposed design would require violating a rule here, the design must change — not the rule — unless a formal locked decision revises the rule in PM02.

---

### What This Document Is Not

This document does not restate all rules. Its content falls into three categories:

**Design Principles (§3):** How to read and extend this document — conventions for rule structure, cross-referencing, and future additions. These are not game rules.

**Foundational Design Principles (§4):** Premises about the game world, ARBITER's role, and design intent. These are not mechanical constraints — they are the basis from which governing rules derive.

**Governing Rules (§5–§10):** Explicit, testable constraints that answer design questions spanning multiple artifacts and need a single canonical statement. Derived from narrative principles, expressed as mechanical constraints.

Purely mechanical rules that live cleanly in their source artifact (e.g., Findings decay brackets, initiative D10 table) are not repeated here.

---

## 2. Index

| Section | Content |
|---------|---------|
| §1 | Overview |
| §2 | Index |
| §3 | [Design Principles for This Document](#3-design-principles-for-this-document) |
| §4 | [Foundational Design Pillars](#4-foundational-design-pillars) |
| §5 | [Portrait & Evaluation Rules](#5-portrait--evaluation-rules) |
| §6 | [ARBITER Procedure Rules](#6-arbiter-procedure-rules) |
| §7 | [Board State & Commitment Rules](#7-board-state--commitment-rules) |
| §8 | [Footprint Rules](#8-footprint-rules) |
| §9 | [Economy & Resources Rules](#9-economy--resources-rules) |
| §10 | [Information & Privacy Rules](#10-information--privacy-rules) |
| §11 | [Data Table Standard (L108)](#11-data-table-standard-l108) |

---

## 3. Design Principles for This Document

*Scope: this document only. Principles here govern how 00a is written, structured, and extended. Cross-artifact premises — things that are true about the game and drive design decisions across all artifacts — belong in §4.*

*How the rules and foundational principles in this document were constructed. These are not governing rules — they do not constrain card or mechanic design. They explain how to read and extend this document.*

---

### What Qualifies as a Foundational Design Principle

Foundational Design Pillars (§4) are premises — things that are true about the game that drive all design decisions. They are not mechanical constraints. A principle belongs in §4 if:

1. It cannot be violated without changing the fundamental nature of the game
2. It spans the entire design — it cannot be derived from a single mechanical system
3. It answers "why does this game work this way?" rather than "what are the rules?"

Rules that flow directly from a foundational pillar belong in §5–§10 Rules sections as governing rules, not in §4. §4 entries are premises; §5–§10 entries are constraints derived from those premises.

---

### Rule Structure Principle — Generalized Statements, Organized by Corollary

Rules are stated at the most general level that captures the principle. Corollaries — rules that follow directly from a more general rule — are numbered and grouped under their parent rule (5.1a, 5.1b, etc.). A rule that can only be understood by reference to a specific card, component, or situation is not general enough; it belongs on the card or in the source artifact.

---

### Rule Structure Principle — No Exceptions in Rule Statements

Rules in this document are stated as complete, universally applicable constraints. A rule that requires an "exception" clause to function correctly is not fully stated — the exception is part of the rule's scope definition and belongs in the Rule and Mechanics fields as a positive statement, not as a carve-out.

When a rule appears to have an exception: reframe the rule to encompass all cases. If a specific behavior is governed separately, give it its own rule. Exceptions signal incomplete framing, not design complexity.

---

### Rule Structure Principle — Mechanics vs. Process

The **Mechanics:** field states the rule and any binding design constraints that cannot be overridden. It does not contain execution procedure — the sequence of who does what, when, and in what order. Procedure belongs in the source artifact (Artifact 03 for round structure, Artifact 07 for ARBITER scripting, Artifact 11 for component specs). If a Mechanics field describes how something is carried out rather than what is constrained, the procedural content is in the wrong place.

---

### Rule Data Structure — Governs vs. Pending

Each rule carries two cross-reference fields with different permanence:

**Governs:** — permanent. Lists the artifacts, rules, and card sets this rule constrains. Governs entries do not expire.

**Pending:** — temporary. Lists open design decisions, audits, or unresolved cross-references that require future action. When the referenced item resolves, the Pending entry is removed. If a rule has no open dependencies, the Pending field is absent entirely.

---

### Copy Design Principle — Do Not Hardcode Variable Values

Copy in this document must not hardcode specific values — rates, costs, counts, thresholds — that are variable, under active consideration, or subject to future decisions. Reference the concept and point to where the canonical value is defined. If the value changes, it changes in one place. This applies to all copy in this document — rules, Narrative fields, and Mechanics fields.

*Example: Income generation rules in this document reference Art 02 and Artifact 03 for rates — if a rate changes, it changes in one place.*

---

### Information Design — Terminology Sequencing

No term may appear in this document without its narrative grounding having been established in a prior artifact or earlier in this document. See PM03 §1 for the full cross-artifact principle and audit implications.

---

### Copy Design Principle — In-Game Terms in Narrative Fields

All Narrative fields in this document use the canonical in-game terms defined in §3.1. Where game-mechanical language would use a functional descriptor, the Narrative field uses the in-world term — "Quarter" not "round," "Public Standing" not "popularity track," "Presence chip" not "influence token." The canonical term list is the reference.

---

### 3.1 — Canonical Definitions

Authoritative definitions for all in-world terms, components, and game systems used across the artifact set. This section is the source of truth; all downstream artifacts reference here. Each entry identifies the artifact where the term receives its narrative grounding in reading order.

---

#### Temporal Conventions

| In-World Term | Mechanical Equivalent | Narrative Summary | Full Treatment |
|---------------|-----------------------|-------------------|----------------|
| Quarter | One round of play | Approximately three months of real-world time in New Meridian. The factions at The Table are operating on a human timeline. Session length: Art 03 §3. Chorus timeline duration: Art 00 §1. | Art 00 §1 |
| Month | One of three sequential phases within a Quarter | Outcomes from earlier Months are known before later Months dispatch, giving each successive Month more information than the last. | Art 03 §4 |

---

#### Component & System Terms

| In-World Term | Mechanical Equivalent | Narrative Summary | Full Treatment |
|---------------|-----------------------|-------------------|----------------|
| The Chorus | Extraterrestrial transmission | Non-repeating structured signal of non-human origin, transmitting continuously for thirty-one years. Best current interpretation: a question. What that question is cannot be agreed upon. | Art 00 §6 |
| New Meridian | Game board location | Boom city assembled around a listening station in thirty-one years. 800,000 people from everywhere. The city's entire history is a response to a transmission it still cannot fully interpret. | Art 00 §6 |
| District | Board space | A named geographic zone within New Meridian. | Art 01 §1 |
| The Chorus Node | Central game board district | The original detection installation, expanded over three decades into a permanent research complex. ARBITER's district. The reason New Meridian exists. | Art 00 §6 |
| The Table | Coalition of five factions + ARBITER | The deliberative body assembled to produce humanity's response to the Chorus. No formal authority, no enforcement mechanism. What it has is presence. | Art 00 §8 |
| ARBITER | Game facilitator | Part of the Chorus protocol. Has complete information — every operation, resource, and agreement at The Table. Does not advocate. Does not coerce. Reveals, withholds, and times. | Art 00 §9 |
| Faction Representative | Player role | Each faction's present face at The Table. The individual whose choices, at this deliberation, become the faction's record. | Art 00 §14 |
| The Chronicle | End-of-session narrative account | ARBITER's written record of the session, narrated in The Witness register. Where Resolution stands at session end shapes what kind of story it tells. | Art 00 §9 |
| Resolution | ARBITER's track | ARBITER's private measure of how clearly The Table's behavior is producing a coherent answer to the Chorus. Not visible to factions — felt through the quality of ARBITER's narration and the tone of the Chronicle. | Art 00 §9 |
| The Overview | Game mat / full shared display | The Table's shared situational interface. MIRROR's projection — real-time holographic rendering of the state of New Meridian. ARBITER administers accuracy, not content. | Art 00 §8 |
| Footprint | Physical board presence | Everything the faction has placed: influence markers, structure blocks, and deployment markers on The Overview. The collective term for §8 components. | Art 00 §14 |
| The Backlog | Shared Dispatch Token pool | The queue of authorized but uncommitted operational work. All Dispatch Tokens live here when not in faction possession. Tokens drawn at Upkeep represent a faction's operational capacity for the Quarter; spent tokens return at Quarter close. | Art 00 §14, Art 02 §9 |
| Dispatch case | Sealed envelope or small box | Protocol for covert submission. Each faction's covert operations pass through here each Quarter. | Art 00 §14 |
| Reservoir | Resource bank | The supply of available faction resources. *"The Reservoir does not judge what is drawn from it."* | Art 02 |
| Public Standing track | Popularity track | Bell curve enforced by natural drift. Scale and drift thresholds: Art 02 §11. | Art 02 §11 |
| Chorus Portrait | Portrait score | ARBITER's private assessment of faction alignment with the Chorus Question. Determines initiative and feeds the Chronicle. | Art 02 §10 |
| Intel Token | Proof token / intel note | Physical token representing confirmed intelligence one faction holds about another. Held privately; disclosed at faction's discretion. | Art 02 §12 |
| Presence chip | Influence token | The felt weight of faction power in a district. Ambient weight, deference in the air, unspoken rules. | Art 02 §6 |
| Operational marker | Claim marker | Temporary deployment presence; counts as a presence chip during the Quarter. | Art 01 §1 |
| Covert operation | Private action | Actions submitted face-down to the dispatch case. | Art 00 §14 |
| Public act | Public action | Actions declared openly at the table. | Art 00 §14 |
| Classified Directive | Hidden objective card | Per-faction sealed mission carried by operatives. Full arc objective — surfaces at session close. | Art 00 §14 |
| Situation Report | World event card | Two-card system: public narrative + ARBITER effect card. | Art 01 §1 |
| Countermeasure Card | Reaction card | Reactive card type. | Art 03 §17 |
| Field Operative Dossier | Agent card | The faction's single named operative — the one who can make the Apex play. | Art 00 §14 |
| Findings (Ghost) | Ghost faction resource | The power of knowing. | Art 02 |
| Exposure (Network) | Network faction resource | The power of being seen. | Art 02 |
| Capital (Syndicate) | Syndicate faction resource | The power of economic control. | Art 02 |
| Capacity (Guild) | Guild faction resource | The power of building and doing. | Art 02 |
| Mandate (Directorate) | Directorate faction resource | The power of institutional legitimacy. | Art 02 |
| Dominant | Majority control | A faction holds Dominant when their Holt magnitude is unambiguously higher than all others and has crossed the absolute floor. The condition of being the unambiguous leader — it subsides the moment that clarity is in question. Thresholds: Art 02 §6. | Art 00 §14, Art 02 §6 |
| Established | Qualified presence | The district begins to organize around this faction's weight. Thresholds: Art 02 §6. | Art 02 §6 |
| Present | Foothold | Atmospheric weight present but not yet defining. The district absorbs it. | Art 00 §14 |
| Contested | Tied control condition | When two factions are close at the top, neither holds Dominant: the atmosphere is contested, the weight unresolved, the district in flux. Trigger: count of factions at Dominant status > 1. | Art 00 §14, Art 02 §6 |

---

## 4. Foundational Design Pillars

*Scope: all V1 artifacts. These are the premises from which governing rules are derived and against which all downstream design is tested.*

*First-principles about The Signal — premises about the game world, the ARBITER role, and design intent. These are not mechanical rules. They are the basis from which governing rules are derived.*

---

### Core Design Pillars

#### 4.1 — The Overview is Truth

**No hidden state on The Overview. Everything shared is visible there.**

What factions conceal lives in their Terminals, their hands, and their dispatch cases — never on the shared display.

---

#### 4.2 — Information Has Timing

**Secrecy exists but only temporarily. The game moves toward disclosure.**

Covert operations may be discovered. Intelligence tokens age and expire. Hidden directives are revealed at session end.

---

#### 4.3 — Negotiation is Mandatory

**No faction can achieve its goals alone.**

The most significant actions require resources, relationships, and cooperation that no single faction can generate independently. Cooperation is incentivized even when it is politically uncomfortable.

---

#### 4.4 — Control of Systems Defines What Outcomes Are Possible

**Who controls the districts, the structures, and the resource flows determines which answers to the Chorus remain viable.**

Players don't pick an ending — they shape what endings remain possible.

---

#### 4.5 — The System Decides

**Players shape the system through their actions. The system produces the answer.**

No single player, and no single faction, decides what humanity says. What becomes inevitable emerges from what The Table does.

---

#### 4.6 — Narrative and World Consistency

**Every rule must carry a narrative grounding — the mechanical constraint follows from the world, not the other way around. If narrative reasoning and mechanical reasoning conflict, narrative takes precedence.**

If the narrative reason for a rule cannot be stated, the rule may be arbitrary. This is the operative meta-principle for all design in The Signal — it applies to every rule, card, decision, and policy.

**Art 00 is the origin of all canonical narrative.** Downstream artifacts may reference, summarize, or point to Art 00 narrative — they may not introduce canonical narrative of their own. If narrative content is needed anywhere in the design, Art 00 is amended first; downstream artifacts reference it. A narrative statement that does not have its origin in Art 00 is not canonical.

*Source: PM02 L195. Governs: all V1 artifacts.*

---

#### 4.6a — The Overview Zone Anchoring

**Every zone, track, and strip on The Overview must have a narrative anchor — a statement of what that element IS in the world of New Meridian — before visual design is finalized.**

They are not decorative. They are feeds.

> *"The Table doesn't print abstractions on the wall. Everything up there means something. You just have to know how to read it."*
> — Directorate protocol officer, orientation brief

Zones whose narrative anchor is pending are marked TBD in Artifact 01 and Artifact 11 until resolved.

*Source: Design Pillar 4.6, PM02 FD-02.*

---

#### 4.6b — The Missing Author Vacuum

**No faction at The Table is positioned to write the content of humanity's response to the Chorus. The structural gap in the doctrinal geometry is permanent and deliberate.**

The factions fight over medium, timing, ownership, and access. The moment any faction claims authorship of the message itself, the geometry collapses. No card flavor text, Chronicle entry, faction perspective, or any authored content in The Signal may assert or imply that any faction knows what the message to the Chorus should say.

*Source: PM02 L174, Art 00 §14.*

---

### ARBITER Design Principles

#### 4.7 — ARBITER vs. The ARBITER Player

**Two distinct identities must be kept terminologically separate across all project artifacts.**

**ARBITER** — the in-world entity. The Chorus's instrument. The presence at The Table with four registers, a hidden agenda, and an ongoing relationship with the factions. ARBITER does not learn from the dispatch cases — everything that happens in New Meridian is already known to ARBITER. In a technology-enhanced version of the game, ARBITER is the system.

**The ARBITER player** — the human performing ARBITER's role in the paper prototype. Operates in two modes: as ARBITER (embodying the entity, delivering notifications) and as game engine (rolling dice, applying difficulty, stating outcomes — functions automated in a technology-enhanced implementation).

**Conventions:**
- **Narrative fields and ARBITER scripts (Artifact 07):** Always use "ARBITER."
- **Mechanics fields:** "ARBITER" for entity-level acts. "The ARBITER player" for physical paper prototype execution.
- **Rule statements:** "ARBITER" — rules govern the entity's authority across all implementations.

These identities are the same person in the paper prototype. They will not be in all implementations.

*See also: PM02 L88, PM05 00a-10 (retroactive audit).*

---

#### 4.7a — ARBITER Player Is Human

**The ARBITER player is a human sitting at the table, not a system. All ARBITER-facing design must protect this operative reality.**

An ARBITER player who cannot keep up with the game — tracking per-card notes, consulting exception tables, processing parallel demands — is failing in a role the game created. The mechanism of protection is simplification: general procedures, faction monitoring, and immediate authority. The question is never "can ARBITER do this?" but "can ARBITER do this reliably, every time, under table pressure, without degrading the game?"

The paper prototype abstracts ARBITER's role into two operational modes: engine mode (mechanical processing) and entity mode (ARBITER as character). This abstraction is a design decision, not a model of ARBITER's actual nature.

*See also: 6.1 and corollaries. Full treatment: Artifact 07. PM02 07-04.*

---

#### 4.7b — ARBITER Cognitive Efficiency

**Every rule, card effect, and game procedure that involves ARBITER must be designed by asking: how can this narrative function be implemented while impacting the ARBITER player as lightly as possible?**

**Implementation preference order:**
1. Physical objects carry their own state — ARBITER moves components, does not track state
2. Faction players monitor and enforce — ARBITER adjudicates calls; does not watch
3. General procedures applied uniformly — no per-card special cases
4. ARBITER-specific per-instance procedures — only when the above are unavailable

If a narrative function cannot be implemented within this order without significant cognitive overhead, it is either deferred to L2+ or redesigned until it fits.

*See also: 6.1 and corollaries.*

---

### Guaranteed Effects

#### 4.8 — Guaranteed Effects

**Certain game properties are declared constant. No card, rule, mechanic, or player action may override them.**

These are not defaults or strong guidelines — they are invariants. They exist to guarantee that the world of The Signal remains consistent regardless of player choices, card combinations, or edge conditions.

---

#### 4.8a — District Character Is Intrinsic

**No card, effect, or mechanic may change what a district fundamentally produces. Conquest changes governance. It does not change geography.**

A district generates its particular resource because of what it is — its infrastructure, its history, its people — not because of who holds the flag.

*Source: Art 02 §8, PM02 L73.*

---

#### 4.8b — Irreducible Chance

**Preparation shapes outcomes. It does not eliminate uncertainty.**

The probability system has hard floors and ceilings that no modifier can override — a best-prepared operation can fail on a stroke of bad luck, and a desperate attempt can succeed against all odds. This is not a mechanical convenience. It is a design statement about how the world works.

*See also: Art 03 §9.4, Art 04 card design — crit ranges are hard constraints, not guidelines.*

---

#### 4.8c — The Game Guarantees a Playable Floor

**No faction may ever be without a valid action, regardless of resource state or hand composition.**

A faction reduced to its last unit of power can still walk into that room and make a move. The Table was not designed to produce observers.

---

#### 4.8d — Passive Generation Is Inviolable

**Each faction has reach beyond New Meridian. No game action may reduce, block, redirect, or affect a faction's passive resource generation.**

The city cannot starve a faction's entire existence. It can only constrain their presence within it.

*Source: Art 02 §8.*

---

## 5. Portrait & Evaluation Rules

Rules governing the Chorus Portrait track — what it is, how it is maintained, who can access it, and when it fires.

---

#### 5.1 — The Chorus Portrait

**Rule:** The Chorus Portrait is the Chorus's ongoing record of each faction's doctrinal alignment — not their success, but their nature. It is not a resource The Table controls, not a score factions can influence, and not a player-visible outcome. ARBITER maintains it as the Chorus's instrument.

**Narrative:** No faction can instruct the Chorus on how to evaluate them. The Portrait is not a resource — it is an observation. The separation between actor and evaluator is fundamental: if factions could move their own Portrait, the Chorus would be receiving a performance rather than observing behavior. ARBITER does not score factions. It transmits what the Chorus already sees.

> *"Watch ARBITER long enough and you start noticing the pauses. Something happens at the table and ARBITER goes very still. You never find out what it means."*
> — Network field observer, session log

**Mechanics:** ARBITER is the sole mover of the Portrait marker. No other participant moves it under any circumstance. Portrait movement is not a player-visible game outcome — no card Effect field may reference it as such.

*Source: PM02 L84. Derived from Artifact 00 §9.*

*Governs: All card design. See also: 5.1a, 5.1b, 5.1c. Retired: Cross-Category — Shift — Chorus Portrait as player-facing taxonomy function (04b).*

---

#### 5.1a — Portrait Accumulates Without Decay

**Rule:** The Chorus Portrait accumulates without drift or decay.

**Narrative:** The Chorus does not forget. Its record of what the factions have done is complete and permanent. There is no statute of limitations on behavior observed by something that has been watching for thirty-one years. A faction that acts against its doctrine has acted against its doctrine — that does not fade because quarters have passed.

> *"It doesn't matter what we do differently from here. The record is the record."*
> — Directorate counsel, private memo, Quarter 5

**Mechanics:** Portrait scores are permanent and cumulative. There is no passive drift, recovery, or forgetting. A faction cannot passively recover Portrait — new behavior adds on top of what is already recorded.

*Source: Art 02 §10.*

*Governs: Artifacts 02, 07. Corollary of 5.1.*

---

#### 5.1b — Portrait Track is Always Private

**Rule:** The Chorus Portrait track is always private.

**Narrative:** If factions could see what the Chorus has recorded about them, they would perform for it. The Chorus is not interested in performances. It is interested in behavior under conditions where the evaluation is not visible. The Portrait must remain invisible to remain meaningful.

> *"We spent three months trying to figure out what ARBITER thought of us. Completely wasted. You can't read it."*
> — Ghost analyst, debrief notes

**Mechanics:** Factions cannot see their own Portrait position or any other faction's position. ARBITER communicates Portrait state only through Debrief observations and the Chronicle — never through direct numerical disclosure. No card or mechanic may grant a faction read access to the Portrait track. Setup procedure: Artifact 03.

*Source: Art 02 §10.*

*Governs: Artifacts 02, 07, 09. Corollary of 5.1.*

---

#### 5.1c — Portrait Scoring Fires at Resolution

**Rule:** Portrait scoring fires at Resolution — when behavior is demonstrated, regardless of outcome.

**Narrative:** The Chorus evaluates what a faction is. Not whether they succeeded. A faction that attempts a doctrinally aligned action and fails has still demonstrated something about their values. Intent is observable. The Chorus has been watching long enough to know the difference between who a faction is and what they managed to accomplish this quarter.

> *"Ghost ran the same surveillance op three times and failed each time. After the first failure, something moved on ARBITER's side of the table. We still don't know what."*
> — Network field observer, mid-session report

**Mechanics:** Portrait scoring fires at Resolution via two parallel mechanisms. A card where doctrine is demonstrated by the act applies its Portrait value regardless of roll outcome. A card where the outcome itself is the doctrine demonstration applies its Portrait value when the stated condition is met. A card may carry both. ARBITER applies all Portrait values present on the card at Resolution.

*Source: PM02 L82, Artifact 04 Principle 10. Corollary of 5.1.*

*Governs: All card design; Portrait fields in card data structure.*

*Pending: Art 04 card design principles migration (PM05 XA-xx) — card implementation detail (Portrait values printed on card) migrates with §7 content.*

---

## 6. ARBITER Procedure Rules

Rules governing how the ARBITER player executes procedures and makes rulings. All rules in this section flow from Foundational Design Pillars 4.7–4.7b.

---

#### 6.1 — General Procedures Only

**Rule:** ARBITER executes general procedures, not card-specific instructions. All ARBITER-facing content in the game must map to defined, generalizable procedures that apply uniformly across all game states in their category — derivable from a reference document, without per-card notes or per-beat tracking tables. Physical tools (card UI, reference mats, threshold calculators, splaying conventions) carry the complexity; ARBITER carries the judgment.

**Narrative:** ARBITER is a human player, not a computer. The game must protect that experience. An ARBITER maintaining per-card notes, per-beat tracking tables, and card-specific exception procedures is not playing — they are administering.

*Source: PM02 L187. Implementation of: Design Pillar 4.7a.*

*Governs: All artifacts defining ARBITER-facing procedure or content.*

---

#### 6.1a — Factions Police Their Own Permanent Effects

**Rule:** A faction that plays a permanent effect is responsible for monitoring and enforcing that effect for its duration. When a violation occurs, the owning faction calls it; ARBITER adjudicates and applies the consequence. ARBITER does not proactively track faction-played permanent effects between calls.

**Narrative:** The faction that issued the regulation enforces it. ARBITER does not maintain a running watch on every card in play — that is the owning faction's obligation. Faction law, faction enforcement.

**Mechanics:** At resolution of a permanent card, the playing faction assumes monitoring responsibility. When a violation is called, ARBITER adjudicates and reverses the violating board change. If the owning faction does not call a violation at the time it occurs, the board state stands (7.2b). Other players may call clearing conditions on any active permanent effect; ARBITER adjudicates all calls.

*Source: Corollary of 6.1. See also: 7.2b.*

*Governs: All faction-played permanent effects.*

---

#### 6.1b — ARBITER Unavailable During Resolution

**Rule:** ARBITER is unavailable for service requests during Resolution. Conversion requests and other non-resolution demands are deferred until ARBITER is no longer in engine mode.

**Narrative:** At the start of each quarter, the factions draw from New Meridian the form of power their doctrine is built to gather. The Translation is different — a faction admitting their doctrine was insufficient, asking ARBITER to transmute one form of human power into another. ARBITER accommodates it. But not while the city is in motion.

> *"The conversion is granted. The request was noted."*
> — ARBITER, The Record register

**Mechanics:** Resource conversion (The Translation) is available during Debrief and between phases only. It is not available during Resolution Beats 1–5. Rate defined in Artifact 03, subject to D02a-01. Procedure: Art 03 §9, §11.

*Source: Art 03 §9, §11. Corollary of 6.1.*

*Governs: Artifact 07 scripting.*

---

#### 6.1c — ARBITER's Ruling is Final

**Rule:** The ARBITER player's ruling on any ambiguous situation or edge case is final and immediate. The game does not pause for debate or rule research.

**Narrative:** ARBITER is not a rules database. Its authority comes from the Chorus, not from procedural expertise. An ARBITER player who stops play to research precedent has broken engine mode — the same cognitive load the system is designed to prevent. The ruling stands because it was made. Corrections are design decisions for the next session.

**Mechanics:** When an unexpected situation requires a judgment call, the ARBITER player rules and play continues. No justification is owed to other players. How to deliver rulings in character: Artifact 07.

*Source: Derived from Artifact 00 §9. Corollary of 6.1.*

*Governs: Artifact 07.*

---

## 7. Board State & Commitment Rules

Rules governing the board's relationship to physical reality, and the irreversibility of all game commitments. Implements Design Pillars 4.1 and 4.2.

---

#### 7.1 — Public Zone Accessibility

**Rule:** All information in public zones is accessible to all players at all times.

**Narrative:** A faction's standing in New Meridian is not recorded on a form. It accumulates in a thousand simultaneous interactions — the doorman who hesitates, the journalist who calls back, the neighborhood that goes quiet. These are the city's ongoing assessment, visible to anyone paying attention.

**Mechanics:** All components, values, and states in any zone not designated private are visible to and readable by all players at all times. No mechanic may obscure or restrict access to information in a public zone. "Public zone" is defined in Artifact 01.

*Source: Art 02 §11.*

*Governs: Artifacts 02, 09. See also: 7.2a.*

---

#### 7.2 — Board Reflects True Current State

**Rule:** The board reflects true current state at every moment in the Quarter.

**Narrative:** What appears on The Overview cannot be negotiated away. A structure placed is placed. Presence lost is lost. The city does not hold events in suspension while the factions decide how to characterize them.

> *"New Meridian is not a map. It is a clock. What it shows is not where things were. It is where things are. Right now. While you're looking."*
> — Senior signal analyst, orientation briefing (unofficial)

**Mechanics:** The board is never permitted to show a stale or deferred state. When a game action causes a board change, that change is made immediately upon resolution — not at the end of the beat or Quarter.

*Source: Artifact 03 §5.*

*Governs: Artifact 03 Resolution beats; Artifacts 02, 09.*

---

#### 7.2a — Board State is Always Publicly Visible

**Rule:** All board state is always publicly visible.

**Narrative:** Physical presence in a city cannot be hidden. A structure exists. Deployed operatives are in the streets. No one can have an invisible building.

**Mechanics:** Presence tokens, deployment markers, structure blocks, control flags, established markers, and tension markers are visible to all players at all times. Nothing on the board surface is ever hidden. Cards and ARBITER scripts may not create mechanics that place hidden state on the board surface.

*Source: Design Pillar 4.1 (00a §4.1), Artifact 01 §5, Art 02 §5, Artifact 03 §5.*

*Governs: All artifacts. Corollary of 7.2. See also: 7.1.*

---

#### 7.2b — Committed Board States Cannot Be Nullified

**Rule:** Board states are committed on resolution. Once an effect resolves and alters the board, that change is fixed — no subsequent card, effect, or procedure may retroactively nullify it. Countering an established board state requires a forward action.

**Narrative:** The building was built. Demolish it to counter it. The signal was transmitted. You respond to what was sent.

**Mechanics:** Effects resolve against the board state as it exists at time of resolution. There is no mechanism for undoing a committed board state — only for acting on it going forward.

*Source: Corollary of 7.2. See also: 6.1a, 7.3.*

*Governs: All card effects, all phases.*

---

#### 7.3 — Commitment is Irreversible

**Rule:** Commitment is irreversible. A closed dispatch case, a declared public act, a submitted resource — once committed, these are facts in the world. They cannot be recalled, modified, or undone.

**Narrative:** A Dispatch Case, a declared act, a spent resource — these are facts that exist in the world now. The world does not allow uncausing. There is no taking it back, no reconsidering, no polite withdrawal. The Table moves. What was done was done.

> *"The moment you close that case, you've done it. There is no 'I changed my mind.'"*
> — Syndicate operations lead, training brief

**Mechanics:** A closed dispatch case cannot be opened or modified. A declared public act cannot be withdrawn or changed. Submitted resources cannot be reclaimed.

*Source: Artifact 03 Principle 2.*

*Governs: Artifacts 03, 04, 07.*

---

#### 7.3a — Phases Do Not Overlap

**Rule:** Phases do not overlap. Once a phase ends, it cannot be revisited.

**Narrative:** The Table has structure because structure is how civilized parties conduct business. Breaking phase order does not just violate a rule. It breaks the pretense of civilization that The Table depends on.

**Mechanics:** No action valid in a later phase may be taken in an earlier phase. No action from a prior phase may be revisited once the next phase begins. Phase announcement procedure: Artifact 07.

*Source: Artifact 03 §6. Corollary of 7.3.*

*Governs: Artifact 03; Artifact 07.*

---

#### 7.3b — Submission Order is Tiebreaker

**Rule:** Submission order is the tiebreaker within resolution priority tiers.

**Narrative:** Decisiveness is a form of power. A faction that commits first shapes what comes after. A faction that hesitates has ceded something to the one that did not.

**Mechanics:** When multiple operations in the same beat are otherwise equal in priority, they resolve in the order their dispatch cases were submitted. This applies within Beat 3 and within Beat 4.

*Source: PM02 L16, Artifact 03 §9. Corollary of 7.3.*

*Governs: Artifact 03; Artifact 07.*

---

#### 7.3c — Dispatch Token Required

**Rule:** Each action — covert operation or public act — requires exactly one Dispatch Token. The token is the instrument of commitment. Submission without a Dispatch Token is invalid: the action does not resolve and the cost is not spent.

**Narrative:** Internal capacity is not the same as organizational readiness. The token is the accounting of synchronization — approvals completed, commitments made. Without it, the operation exists as a plan. It does not exist as an action.

**Mechanics:** Each action requires one Dispatch Token. A covert operation submitted without a token is rejected at Beat 0 — cost not spent. A public act requires a token placed on the declared card. Full procedure: Artifact 03 §9. Component definition: Art 02 §9.

*Source: Artifact 03 §9; PM02 L180. Corollary of 7.3.*

*Governs: Artifacts 02, 03.*

---

## 8. Footprint Rules

Rules governing a faction's physical Footprint — the board presence components (influence markers, structure blocks, and deployment markers) that represent their active presence in New Meridian. Organized by component type. Canonical definitions: 00a §3.1.

---

### Influence Markers

#### 8.1 — Maximum Presence Per District

**Rule:** No faction may hold more than 6 presence tokens in a single district at any time.

**Narrative:** There is a saturation point to any faction's presence. A district can only absorb so much of one faction's atmosphere before the weight becomes something else. The number comes from the Holt Index — adopted by The Table as the boundary The Overview could track.

> *"You can fill a room so full of your people it collapses. Doesn't make it yours. Makes it something else."*
> — Directorate district coordinator, field notes

**Mechanics:** No faction may hold more than 6 presence tokens in a single district at any time. Deployment markers count toward this limit during the Quarter they are placed. No card effect or operative ability may place a token that would exceed this limit — the attempt fails regardless of other conditions.

*Source: PM02 L26, Art 02 §6.*

*Governs: All cards placing presence; Artifact 05.*

---

#### 8.1a — ARBITER's Permanent Presence at Chorus Node

**Rule:** ARBITER holds permanent, structurally dominant presence at the Chorus Node. This presence exceeds the human maximum, making Dominant structurally unreachable there and precluding all faction structure placement.

**Narrative:** The Chorus Node exists outside human jurisdiction. ARBITER's infrastructure fills the space — there is nothing left to build on or in. A faction can be present at the Node. They cannot build there, not because the law forbids it, but because something else is already using the space.

> *"Thirty-seven site visits. I've checked every room in that facility. Except one. I keep marking it inspected in my log. I haven't been inside."*
> — Guild structural engineer, personnel debrief (unprompted disclosure)

> *"We filed a construction permit for the Node perimeter six times. Sixth time, the permit office said the space was already occupied. There's nothing there. Just ARBITER's piece, and whatever is underneath it."*
> — Guild administrative record, permit log

**Mechanics:** The Chorus Node holds ARBITER's single fused piece — always present, never removed. The piece comprises eight ARBITER-keyed presence tokens topped by ARBITER's dominance marker, fused as one inseparable component. Because ARBITER's presence count permanently exceeds the human maximum of six, Dominant is structurally unreachable at the Chorus Node. No faction structure blocks may be placed at the Chorus Node under any game state or card effect. Component design and visual specification: Artifact 11. Placement at setup: Artifact 03.

*Source: PM02 L28, Artifact 01 §8, Art 02 §14. Corollary of 8.1.*

*Governs: Any card targeting the Chorus Node; Artifacts 01, 02, 11. See also FD-01 (PM02 §5).*

---

### Structure Blocks

#### 8.2 — Presence Required for Structure Placement

**Rule:** A faction must hold at least 1 presence token in a district to place or retain a structure block there.

**Narrative:** Commitment requires someone to sustain it. A structure block records that a faction is invested in this district. When the last of their people leave, the commitment does not persist — because the commitment itself does not persist. The building may remain. The Overview records something else.

**Mechanics:** A faction may not place a structure block in a district where they have no presence. Execution procedure: Artifact 03.

*Source: PM02 L25, Art 02 §7.*

*Governs: All cards placing structures; Artifact 03.*

---

#### 8.2a — Maximum One Structure Block Per District

**Rule:** No faction may hold more than 1 structure block in a single district at any time.

**Narrative:** A faction's investment in a district is binary: the structure block is present or it is not. A second block cannot deepen a commitment already declared. The fact of commitment cannot be stated twice in the same district.

**Mechanics:** No card effect may place a second structure block for a faction in a district where they already have one.

*Source: Art 02 §7. Corollary of 8.2.*

*Governs: C01, C14, P03, P09, and any future structure-placement cards.*

---

#### 8.2b — Structure Blocks Lost on Absence

**Rule:** Structure blocks are lost immediately when a faction goes Absent.

**Narrative:**

> *"The moment Ghost left the Data Exchange, the building was just a building."*
> — Guild infrastructure report, Quarter 4

**Mechanics:** The moment a faction reaches 0 presence tokens and 0 deployment markers in a district — by any means — all their structure blocks in that district are immediately removed. No card effect can prevent this.

*Source: PM02 L25, Art 02 §7. Corollary of 8.2.*

*Governs: All cards removing presence; Artifacts 03, 09.*

---

### Deployment Markers

#### 8.3 — Deployment Markers Count as Presence

**Rule:** Deployment markers count as temporary presence tokens.

**Narrative:** A faction in motion is still a faction present. Where presence tokens represent ambient weight that fills a district over time, a deployment marker is the faction actively engaging there. The distinction between a token and a marker is administrative; the presence is the same.

**Mechanics:** Any rule, card text, or restriction that states "at least 1 presence token" or equivalent applies equally to presence tokens and deployment markers. Deployment markers count as temporary presence tokens for all purposes during the Quarter they are placed.

*Source: PM02 L14, PM02 L58, Art 02 §6.*

*Governs: All artifacts. Global convention.*

---

#### 8.3a — Displaced Markers Must Be Immediately Repositioned

**Rule:** A deployment marker displaced from a district must be immediately repositioned to another valid district. A faction always retains operational presence on the board.

**Narrative:** A faction is an idea. The Overview does not show a faction without deployments. It shows a faction whose deployments have moved.

> *"Nothing on the board for two quarters. Audience response: irrelevant, finished, gone. Actual status: still seated, still speaking."*
> — The Network, Signal Coverage broadcast, Quarter 6

**Mechanics:** When an effect displaces a deployment marker, it is removed from its current district and immediately placed in another valid district in accordance with the effect.

*Source: Design decision B — session 6. Corollary of 8.3.*

*Governs: All cards and effects that interact with deployment markers; Artifacts 02, 03, 04.*

---

#### 8.3b — No Faction Elimination

**Rule:** No faction is eliminated from The Table.

**Narrative:** The factions are not organizations — they are ideas. A faction that loses all physical presence in New Meridian has lost the argument for now. They have not lost the right to keep making it.

**Mechanics:** A faction that loses all accumulated presence is not eliminated. Deployment markers remain in play per 8.3a. Their voice, doctrine, and participation in The Table continue. They lose all resource generation derived from board presence; base generation continues. All strategic effects tied to board presence are suspended. The Chronicle records their decline.

*Source: Artifact 00 §13. Corollary of 8.3a.*

*Governs: Artifacts 03, 07, 10.*

---

## 9. Economy & Resources Rules

Rules governing resource generation and the modifiers that affect it.

---

#### 9.1 — Three Sources of Income Only

**Rule:** A faction's upkeep income derives from three sources only: passive generation, district presence, and structure block output. No other game state modifies upkeep income generation.

**Narrative:** Each faction has reach beyond New Meridian — contracts in other cities, broadcasts that continue regardless of what happens at The Table, operations no one knows about. Public Standing, Portrait, Accord status, and all other game outcomes do not reach those sources.

**Mechanics:** Upkeep income is determined by passive generation rate, board presence, and structure block output only. No card, World Condition, Accord, or game state other than presence and structure output may modify upkeep income generation.

*Source: Art 02 §8, §11, §12.*

*Governs: Artifacts 02, 03, 04, 09.*

---

#### 9.1a — Public Standing Modifies Difficulty, Not Income

**Rule:** Public Standing modifies action difficulty, not resource income.

**Narrative:** New Meridian's opinion of a faction changes how easily they can operate there — closed doors, reluctant cooperation, hostile witnesses. But the city's opinion does not determine how much power the faction can draw. Only how smoothly they can exercise it.

**Mechanics:** The Public Standing modifier shifts the difficulty target threshold on all 2d10 rolls by the stated amount. It does not affect income generation in any way.

*Source: Art 02 §11, §12. Corollary of 9.1.*

*Governs: Artifacts 02, 03, 04, 09.*

---

#### 9.1b — Card and Action Resource Generation Is Not Income

**Rule:** Resources generated by card effects and player actions are not upkeep income. The three-source restriction of 9.1 does not apply to them.

**Narrative:** A faction's income is what flows to them whether or not they act — the baseline the city owes them for existing in it. What they extract through operations, leverage, and tactical pressure is something else: earned in the moment, contingent on the action.

**Mechanics:** Resources produced by card effects or operative actions are not subject to the upkeep income restrictions of 9.1. They do not modify income calculation and are governed by individual card Effect fields and Art 02.

*Source: Art 02 §11, §12. Corollary of 9.1.*

*Governs: Artifacts 02, 03, 04, 09.*

---

## 10. Information & Privacy Rules

Rules governing privately held information: what constitutes private information, who controls disclosure, and the lifecycle of intelligence tokens.

---

#### 10.1 — Private Information Disclosure is Discretional

**Rule:** Players have agency over their privately held information. Disclosure is discretional.

**Narrative:** Information held is information owned. The Table does not compel confession. A faction's intelligence, directives, and hand are their own to share, weaponize, withhold, or lie about. No rule forces a faction to reveal what they know. That would not be a negotiation. It would be an interrogation.

> *"What I know and what I tell you are two different things. That's not a threat. That's The Table."*
> — Ghost Table representative, open session

**Mechanics:** Any private information a player holds — Intel Tokens, hand cards, modifier cards, classified directives, or any other private component — is disclosed only when the holder chooses. No card may compel disclosure. A Reveal effect creates a stake around the disclosure choice: the card defines the consequence for revealing or withholding, but the decision remains the player's.

*Source: Art 02 §10, §12.*

*Governs: Artifacts 02, 04, 05, 08.*

*Pending: Consequences for voluntary strategic non-disclosure — open design question.*

---

#### 10.1a — Verbal Claims Cannot Be Verified by ARBITER

**Rule:** Verbal claims about undisclosed private information cannot be verified by ARBITER.

**Narrative:**

> *"ARBITER knows what is actually held — every note, every directive. ARBITER will not be used as a prop in a deception. If a faction wants to prove what they hold, they must reveal it. ARBITER watches. ARBITER does not narrate."*
> — ARBITER, The Record

**Mechanics:** A faction claiming to hold a specific private component cannot ask ARBITER to confirm or deny the claim without a Reveal effect. ARBITER does not validate bluffs or threats referencing undisclosed information.

*Source: Art 02 §12. Corollary of 10.1.*

*Governs: Artifacts 02, 04, 07.*

*See also: 4.7a, 4.7b.*

---

#### 10.2 — Intel Tokens Leave Play When Spent

**Rule:** Spent or discarded intel tokens leave active play.

**Narrative:**

> *"Twelve days of source contact in that note. Three locations, two operational windows, one name we'd been building toward for months. Thirty seconds in the shredder. You tell yourself you had to — and maybe you did. But there's no 'had to' that gives it back."*
> — Ghost field operative, after-action debrief

**Mechanics:** An intel token that has been used or discarded by its holder is removed from active play. It cannot be retrieved or referenced in any subsequent game action. The physical mechanism — disposable or erasable — is a component design decision (Artifact 11, Art 02).

*Source: Art 02 §12.*

*Governs: Artifacts 02, 04, 09.*

---

#### 10.3 — Intel Token Holdings Have Limits and Expiry

**Rule:** Intel token holdings are subject to per-faction limits. Held tokens expire — expired tokens are invalid or less effective when spent.

**Narrative:**

> *"The Directorate carried three notes into Quarter 5. Their doctrine calls for two. The third was a source contact they hadn't acted on. The Chorus noted the hesitation. Not the note. The hesitation."*
> — ARBITER, The Observation

**Mechanics:** Intel token holdings are subject to per-faction limits and expiry. Specific limit values and expiry definitions are balance decisions in Art 02, subject to playtesting. Neither holding limits nor expiry are mechanically enforced — ARBITER handles called violations per Artifact 07.

*Source: Art 02 §12.*

*Governs: Artifacts 02, 07.*

---

## 11. Data Table Standard (L108)

All data tables in THE SIGNAL artifact suite must satisfy the following five requirements (L108 — Database Translatable Data Design). Requirements 1 and 3 are standard 1NF; Requirement 4 (ID-based foreign references, no prose) enforces 3NF referential discipline; Requirements 2 and 5 are project-specific extensions.

| # | Requirement | Test |
|---|-------------|------|
| 1 | Each column carries a single typed value — no compound cells | No cell contains "A / B" or mixed types |
| 2 | Values from controlled vocabulary (enum) where possible | Column values are drawn from a defined set, not freeform prose |
| 3 | Every table has an explicit primary key (ID column) | First column is always a unique ID |
| 4 | Cross-references use ID-based keys, not prose descriptions | Foreign references name an ID (e.g., F-01), not a label (e.g., "Ghost") |
| 5 | Null / N/A is explicit, never absent | Empty cells use N/A; omission is not a valid null |

*These requirements apply to all data tables in all V1 artifacts, retroactively.*

**Column type vocabulary (L123):** All schema documents in the artifact suite must declare column types using the canonical type vocabulary: **String** (short text), **Semver** (version identifier), **Integer** (non-negative count), **Enum** (controlled vocabulary), **Prose** (long-form text), **±Integer** (signed integer), **ID Reference** (foreign key to an entity ID namespace — governed by Req 4). New types require a locked decision to extend the vocabulary. Source: L121 (Art 04 §6 first application), L123 (promoted to suite-wide standard).

*Governs: all V1 artifacts. Migration status tracked in 00b §5.*

---

## Appendix A — Rule Summary

| ID | Rule | Section |
|----|------|---------|
| 5.1 | Portrait is the Chorus's record of doctrinal alignment — not player-visible; ARBITER sole mover | §5 |
| 5.1a | Portrait accumulates without drift or decay | §5 |
| 5.1b | Portrait track is always private | §5 |
| 5.1c | Portrait scoring fires at Resolution — on act, outcome, or both | §5 |
| 6.1 | ARBITER executes general procedures, not card-specific instructions | §6 |
| 6.1a | Factions police their own permanent effects; ARBITER adjudicates calls | §6 |
| 6.1b | ARBITER unavailable for service requests during Resolution | §6 |
| 6.1c | ARBITER's ruling is final and immediate; game does not pause | §6 |
| 7.1 | All information in public zones is accessible to all players at all times | §7 |
| 7.2 | Board reflects true current state at every moment | §7 |
| 7.2a | All board state is always publicly visible | §7 |
| 7.2b | Committed board states cannot be retroactively nullified | §7 |
| 7.3 | Commitment is irreversible — cases, acts, resources | §7 |
| 7.3a | Phases do not overlap; phase changes are permanent | §7 |
| 7.3b | Submission order is tiebreaker within resolution priority tiers | §7 |
| 7.3c | Each action requires one Dispatch Token — the instrument of commitment | §7 |
| 8.1 | Max 6 presence tokens per faction per district | §8 |
| 8.1a | ARBITER holds permanent dominant presence at Chorus Node; no faction structures there | §8 |
| 8.2 | Faction must have presence to place or retain a structure block | §8 |
| 8.2a | Max 1 structure block per faction per district | §8 |
| 8.2b | Structure blocks lost immediately when faction goes Absent | §8 |
| 8.3 | Deployment markers count as temporary presence tokens | §8 |
| 8.3a | Displaced deployment markers must be immediately repositioned to another valid district | §8 |
| 8.3b | No faction is eliminated from The Table | §8 |
| 9.1 | Upkeep income derives from three sources only: passive, district presence, structure output | §9 |
| 9.1a | Public Standing modifies action difficulty, not upkeep income | §9 |
| 9.1b | Card and action resource generation is not upkeep income; three-source restriction does not apply | §9 |
| 10.1 | Disclosure is discretional; no card may compel it; Reveal effects create stakes, not compulsion | §10 |
| 10.1a | Verbal claims about undisclosed information cannot be verified by ARBITER | §10 |
| 10.2 | Spent or discarded intel tokens leave active play | §10 |
| 10.3 | Intel token holdings are subject to per-faction limits and expiry | §10 |

---

## Appendix B — Rule ID Migration Map

### v0.5 → v0.6 (this version)

*Rule IDs changed from `00-Rnn` format to section-prefixed `n.n` format. Required sweep: all V1 artifacts (PM05 XA-xx).*

| v0.5 ID | v0.6 ID |
|---------|---------|
| 00-R01 | 5.1 |
| 00-R01a | 5.1a |
| 00-R01b | 5.1b |
| 00-R01c | 5.1c |
| 00-R08 | 7.1 |
| 00-R09 | 7.2 |
| 00-R09a | 7.2a |
| 00-R09b | 7.2b |
| 00-R10 | 8.1 |
| 00-R10a | 8.1a |
| 00-R11 | 8.2 |
| 00-R11a | 8.2a |
| 00-R11b | 8.2b |
| 00-R13 | 8.3 |
| 00-R13a | 8.3a |
| 00-R13b | 8.3b |
| 00-R20 | 9.1 |
| 00-R20a | 9.1a |
| 00-R30 | 10.1 |
| 00-R30a | 10.1a |
| 00-R32 | 10.2 |
| 00-R33 | 10.3 |
| 00-R35 | 7.3 |
| 00-R35a | 7.3a |
| 00-R35b | 7.3b |
| 00-R35c | 7.3c |
| 00-R40 | 6.1 |
| 00-R40a | 6.1a |
| 00-R40b | 6.1b |
| 00-R40c | 6.1c |

---

### v0.4 → v0.5

*Cross-reference update guide. Old IDs (v0.4) → New IDs (v0.5).*

| Old ID | New ID | Note |
|--------|--------|------|
| 00-R01 | 00-R01 | Rule statement revised |
| 00-R01a | 00-R01a | Unchanged |
| 00-R02 | — | Moved to Art 07 stub (ARBITER registers) |
| 00-R03 | 00-R40c | Mechanics content; narrative content → Art 07 |
| 00-R04 | 00-R10a | Merged with former R14 |
| 00-R05 | 00-R40b | Reframed as ARBITER procedure corollary |
| 00-R06 | 00-R09a | Corollary of R09 |
| 00-R06a | 00-R09b | Corollary of R09 |
| 00-R07 | 00-R01b | Corollary of R01 |
| 00-R08 | 00-R08 | Generalized to all public zones |
| 00-R09 | 00-R09 | Unchanged; now parent of R09a/R09b |
| 00-R10 | 00-R10 | Unchanged |
| 00-R11 | 00-R11a | Old content; R11 is now new parent rule |
| 00-R12 | 00-R11b | Corollary of new R11 |
| 00-R13 | 00-R13 | Unchanged |
| 00-R13a | 00-R13a | Unchanged |
| 00-R13b | 00-R13b | Unchanged |
| 00-R14 | 00-R10a | Merged with former R04 |
| 00-R15 | — | Moved to §4 Foundational Design |
| 00-R16 | — | Moved to §4 Foundational Design |
| 00-R17 | — | Moved to §4 Foundational Design |
| 00-R18 | — | Moved to Art 03 (upkeep procedure) |
| 00-R19 | 00-R01a | Previously moved S72 |
| 00-R20 | 00-R20 | Rule statement revised (income sources) |
| 00-R20a | — | Formerly R20 difficulty content; now 00-R20a |
| 00-R21–R28 | — | Moved to Art 04 card design principles (PM05) |
| 00-R24 | 00-R01c | Principle level only; card impl → Art 04 |
| 00-R24a | — | Moved to Art 04 |
| 00-R29 | — | Moved to §4 Foundational Design |
| 00-R30 | 00-R30 | Rule statement revised |
| 00-R30a | 00-R30a | Formerly R31 |
| 00-R32 | 00-R32 | Rule statement revised |
| 00-R33 | 00-R33 | Rule statement revised |
| 00-R34 | 00-R35a | Corollary of R35 |
| 00-R35 | 00-R35 | Unchanged; now parent of R35a/R35b/R35c |
| 00-R36 | — | Moved to §4 Foundational Design |
| 00-R37 | 00-R35b | Corollary of R35 |
| 00-R38 | — | Moved to Art 03 (already there) |
| 00-R39 | 00-R35c | Corollary of R35 |
| 00-R40 | 00-R40 | Unchanged; source updated |
| 00-R40a | 00-R40a | Unchanged |

*Pending sweep: PM05 XA-xx (cross-reference update across all V1 artifacts).*
*Pending: Art 07 stub for ARBITER registers (formerly R02/R03 narrative content).*
*Pending: Art 04 Card Design Principles section (formerly §7 content — R21–R28, R24a).*
*Pending: Art 03 — confirm R18 content (structure block declaration) already coded in upkeep procedure.*

---

*End of Artifact 00a — Governing Rules & Design Policy v0.5*
*Populated from review of all V1 artifacts: 00, 01, 02, 03, 04, 04b, PM01, PM02, PM03*
*31 rules across 6 sections (§5–§10). Pending re-sign-off S73 (material restructure — §4 pillar reorganization, §5 design principles moved from Art 00, section-prefixed rule numbering, §9/§10 revisions).*
