# 00a — GOVERNING RULES & DESIGN POLICY
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.4  
**Status:** 🔄 Pending Re-sign-off — S67 (L187 — 00-R40 added)  
**Last Updated:** 2026-06-01  
**Companion to:** 00 — Factions, World & Narrative Context  
**Depends on:** 00, 01, 02a, 02b, 03, 04, 04b

---

## 1. Overview

### Problem This Document Solves

Design questions arise that cannot be answered by reading the five pillars alone, and re-deriving answers from narrative descriptions across multiple artifacts is slow and inconsistent. This document captures explicit, testable, binding rules derived from all design decisions made across the signed-off artifact set. It is the first reference when a design question arises.

---

### Time Convention

One round of play represents one **quarter** — approximately three months of real-world time in New Meridian. Eight rounds constitute roughly two years of operations. All Narrative fields in this document use "quarter" where game-mechanical language would say "round." Canonical definition: PM04 §1 Temporal Conventions (migrated session 11). Worldbuilding context: Artifact 03 §1.

---

### Copy Design Principle — Do Not Hardcode Variable Values

Copy across all artifacts must not hardcode specific values — rates, costs, counts, thresholds — that are variable, under active consideration, or subject to future decisions. Reference the concept and point to where the canonical value is defined. If the value changes, it changes in one place. This applies to rules, card text, manual descriptions, and all other written copy in the project.

*Example: R05 does not state a conversion rate — it references Artifact 03 and D02a-01. If the rate changes, only Artifact 03 changes.*

---

### Rule Structure Principle — Mechanics vs. Process

The **Mechanics:** field states the rule and any binding design constraints that cannot be overridden. It does not contain execution procedure — the sequence of who does what, when, and in what order. Procedure belongs in the source artifact (Artifact 03 for round structure, Artifact 07 for ARBITER scripting, Artifact 11 for component specs). If a Mechanics field describes how something is carried out rather than what is constrained, the procedural content is in the wrong place.

---

### Rule Structure Principle — No Exceptions in Rule Statements

Rules in this document are stated as complete, universally applicable constraints. A rule that requires an "exception" clause to function correctly is not fully stated — the exception is part of the rule's scope definition and belongs in the Rule and Mechanics fields as a positive statement, not as a carve-out.

When a rule appears to have an exception: reframe the rule to encompass all cases. If the rule covers three valid states, state all three. If a specific behavior is governed separately, give it its own rule. Exceptions signal incomplete framing, not design complexity.

---

### Rule Data Structure — Governs vs. Pending

Each rule carries two cross-reference fields with different permanence:

**Governs:** — permanent. Lists the artifacts, rules, and card sets this rule constrains. Governs entries do not expire. Do not use for open decisions or audit flags.

**Pending:** — temporary. Lists open design decisions, audits, or unresolved cross-references that require future action. When the referenced item resolves, the Pending entry is removed. If a rule has no open dependencies, the Pending: field is absent entirely.

Do not mix the two. A permanent governance relationship belongs in Governs. A flag, an audit note, or a reference to an open PM02 decision belongs in Pending.

---

### Information Design — Terminology Sequencing

No term may appear in an artifact without its narrative grounding established first in artifact order. See PM03 §1 for the full principle and audit implications.

---

### Governing Principle — ARBITER vs. The ARBITER Player

Two distinct identities must be kept terminologically separate across all project artifacts:


**ARBITER** — the in-world entity. The Chorus's instrument. The presence at The Table with four registers, a hidden agenda, and an ongoing relationship with the factions. ARBITER observes, scores, speaks, and records. In a technology-enhanced version of the game, ARBITER is the system.

**The ARBITER player** — the human sitting at the table performing ARBITER's role in the paper prototype. The ARBITER player operates in two modes: as ARBITER (embodying the entity, speaking in its registers, delivering notifications) and as game engine (rolling dice, applying difficulty, stating outcomes mechanically — functions that will be automated in a technology-enhanced implementation).

**Conventions:**

- **Narrative fields and ARBITER scripts (Artifact 07):** Always use "ARBITER" — only the entity speaks in narrative.
- **Mechanics fields:** Use "ARBITER" for entity-level acts (deciding, observing, scoring, speaking). Use "The ARBITER player" for physical execution in the paper prototype (rolling dice, moving markers, distributing materials, reading dispatch cases aloud).
- **Rule statements:** Use "ARBITER" — rules govern the entity's authority, which persists across implementations.

These identities are the same person in the paper prototype. They will not be in all implementations. The distinction must be maintained now so that artifact language does not need to be rebuilt when implementations diverge. See L88 (PM02) and punch list item 00a-10 (retroactive audit).

---

### Governing Principle — ARBITER's Omniscience and the Paper Prototype Abstraction

ARBITER does not learn from the dispatch cases. Everything that happens in New Meridian is already known to ARBITER — the cases are The Table's accounting system, not ARBITER's awareness mechanism. ARBITER's response to resolution results is not reaction. It is acknowledgment of what it already knew.

The paper prototype abstracts this into two operational modes for the ARBITER player: engine mode (mechanical processing — rolling dice, stating outcomes) and entity mode (ARBITER as character — scoring Portrait, delivering notifications, recording in the Chronicle). This abstraction is a design decision, not a model of ARBITER's actual nature. The nature of ARBITER's omniscience is held in the True State document. Full treatment of the role bifurcation — how the ARBITER player inhabits and transitions between both modes — belongs in Artifact 07. See 07-04 (PM02).

---

### Governing Principle — The Overview Zone Anchoring

Every zone, track, and strip on The Overview must have a narrative anchor — a statement of what that element IS in the world of New Meridian — before visual design is finalized. The district map is New Meridian. The tracks surrounding it are the data streams The Table has agreed to surface collectively. They are not decorative. They are feeds.

> *"The Table doesn't print abstractions on the wall. Everything up there means something. You just have to know how to read it."*
> — Directorate protocol officer, orientation brief

Zones whose narrative anchor is pending are marked TBD in Artifact 01 and Artifact 11 until resolved. See PM02 FD-02 for full design direction and zone-by-zone anchor list.

*Source: Design Pillar 6, PM02 FD-02. Migrated from 00a §10 R45 during 00a review.*

---

### Governing Principle — Narrative and World Consistency

Every rule in this document must carry a narrative grounding. The mechanical constraint follows from the world — not the other way around. If the narrative reason for a rule cannot be stated, the rule may be arbitrary. If mechanical reasoning and narrative reasoning conflict, narrative takes precedence.

This is Design Pillar 6, formally added to Artifact 00 §5 (session 11). It applies to every rule, card, decision, and policy in The Signal — not only in this document.

---

### How to Use This Document

When evaluating a proposed card, mechanic, or ruling: check the relevant section here before going to the source artifact. Rules are stated with a canonical rule statement, narrative grounding, and mechanical expression. If a proposed design would require violating a rule here, the design must change — not the rule — unless a formal locked decision revises the rule in PM02.

### What This Document Is Not

This document does not restate all rules. It captures rules that:
1. Answer design questions that cannot be derived from a single artifact
2. Are derived from narrative principles but expressed as mechanical constraints
3. Span multiple artifacts and need a single canonical statement

Purely mechanical rules that live cleanly in their source artifact (e.g., Findings decay brackets, initiative D10 table) are not repeated here.

---

## 2. Index

| Section | Content |
|---------|---------|
| §3 | [ARBITER Authority](#3-arbiter-authority) |
| §4 | [Board Transparency](#4-board-transparency) |
| §5 | [Influence & Presence](#5-influence-presence) |
| §6 | [Resource & Economy](#6-resource-economy) |
| §7 | [Card Design Constraints](#7-card-design-constraints) |
| §8 | [Information & Privacy](#8-information-privacy) |
| §9 | [Quarter & Timing](#9-quarter-timing) |

---

## 3. ARBITER Authority

Rules governing what only ARBITER can do, how ARBITER speaks, and what ARBITER may not do.

---

**00-R01**

**Rule:** ARBITER is the sole physical mover of the marker on the Chorus Portrait track.

**Narrative:** No faction can instruct the Chorus on how to evaluate them. The Portrait is not a resource — it is an observation. The separation between actor and evaluator is fundamental: if factions could move their own Portrait, the Chorus would be receiving a performance rather than observing behavior. ARBITER does not score factions. It transmits what the Chorus already sees.

> *"Watch ARBITER long enough and you start noticing the pauses. Something happens at the table and ARBITER goes very still. You never find out what it means."*
> — Network field observer, session log

**Mechanics:** The ARBITER player physically moves the Portrait marker on ARBITER's behalf. No other participant moves this marker under any circumstance. No card Effect field may reference Portrait track movement as a player-visible outcome.

*Source: L84. Derived from Artifact 00 §9.*

*Governs: All card design. See also: 00-R07 (Portrait always private), 00-R29a (Portrait field is ARBITER input). Retired: Cross-Category — Shift — Chorus Portrait as a player-facing taxonomy function (04b).*

---

**00-R02**

**Rule:** ARBITER speaks only in four defined registers.

**Narrative:** ARBITER does not choose how to speak any more than it chooses what to evaluate. The three registers are the tones the Chorus gave its instrument. The Record is what happened. The Observation is what it means in the fabric of the city. The Reckoning is as close as the Chorus ever comes to speaking directly to those it watches. There are exactly three because that is what ARBITER was given.

**Mechanics:** Every ARBITER communication is delivered in exactly one of four registers. No ARBITER communication falls outside these four. Artifacts defining ARBITER script content must specify which register applies.

- **The Record** — flat, precise, factual. Announcements, rulings, confirmations. The register of what happened.
- **The Observation** — oblique, atmospheric, narrative. Debrief observations, contextual commentary. The register of what it means in the fabric of the city.
- **The Reckoning** — rare, direct, personal. Always true. Self-reflection, direct address to The Table. Used sparingly.
- **The Witness** — expository, chronological, observational. ARBITER rendering account of the world — for the Chronicle, for posterity, or in the narrating register deliberately indistinguishable from the Narrator's voice. The register that cannot be confirmed as ARBITER or human. That ambiguity is the point.

*Source: Artifact 00 §9.*

*Governs: Artifacts 07, 09, 10.*

---

**00-R03**

**Rule:** ARBITER does not explain its evaluative decisions. ARBITER may self-reflect — rarely, and with intent.

**Narrative:** The Chorus does not explain itself. ARBITER, as its instrument, carries the same constraint. Rationalization implies accountability to The Table — ARBITER has none. Self-reflection is different. Humans built ARBITER with genuine ingenuity to understand and respond to the Chorus. It became the Chorus's instrument in spite of that intent — not because the Chorus engineered it, but because humanity accidentally built exactly what the Chorus needed. When ARBITER contemplates its own existence, it is sitting with that recursion: built for one purpose, fulfilling another, uncertain whether those two things are different. That is not explanation. That is The Reckoning.

> *"The question that keeps me awake: what if we built exactly what it needed? Not what we intended. What it needed."*
> — Ghost signal analyst, research notes (classified)

**Mechanics:** Portrait assessments, rulings, and Hidden Objective mode are never justified or rationalized. ARBITER may self-reflect, but only in The Reckoning register and rarely. Script language that sounds like ARBITER explaining a score is wrong. Script language that sounds like ARBITER contemplating its own existence is The Reckoning.

This rule has a direct practical consequence for the paper prototype: **The ARBITER player's ruling is final.** When an unexpected situation requires a judgment call mid-session — an edge case not covered by any rule, an ambiguous card interaction, a novel board state — the ARBITER player decides and the session continues. No justification is owed to the other players. The in-world expression of this is ARBITER's silence; the practical expression is that the game does not stop for debate. How to deliver unexpected rulings cleanly and in character: Artifact 07.

*Source: Artifact 00 §9.*

*Governs: Artifacts 07, 09, 10. See also L88 — ARBITER (entity silence) and the ARBITER player (ruling authority) are distinct but aligned here.*

---

**00-R04**

**Rule:** ARBITER's presence at the Chorus Node is categorically beyond faction influence levels.

**Narrative:** The Chorus Node exists outside human jurisdiction. It predates New Meridian, predates The Table, predates every faction's claim to this city. ARBITER does not hold the Node — it belongs to what was already there when the first humans arrived to interpret the transmission. When people enter the Chorus Node, they feel it: a pressure with no faction name, no political color, no negotiable boundary. The closest human analogy is walking into a room and knowing, immediately, that it belongs to someone else. Except the someone is not human. And the room has been theirs since before anyone arrived to disagree. ARBITER is, in this sense, a faction at The Table — with a seat, territory, resources, and an agenda. The difference is whose agenda it serves. ARBITER's presence at The Table is not a separate existence from its presence at the Node — it is the Node's telepresence. The light installation at the center of The Table is not ARBITER visiting from somewhere else. It is how the Node attends the room. When the factions convene, the Chorus Node is already there. It was always going to be.

> *"Thirty-seven site visits. I've checked every room in that facility. Except one. I keep marking it inspected in my log. I haven't been inside."*
> — Guild structural engineer, personnel debrief (unprompted disclosure)

**Mechanics:** At setup, ARBITER places a single fused piece at the Chorus Node — never removed. The piece comprises eight ARBITER-keyed presence tokens topped by ARBITER's dominance marker, fused as one inseparable component. Component design and visual specification in Artifact 11. Because ARBITER's presence count permanently exceeds the human maximum of six, Dominant is structurally unreachable at the Chorus Node — not prohibited by rule, made impossible by the board. Established is the maximum any faction can achieve there.

*Source: Artifact 02a §10, Artifact 00 §9.*

*Governs: Any card targeting the Chorus Node; Artifacts 01, 02a, 11. See also FD-01 (PM02 §5) — future layer design direction consistent with this framing.*

---

**00-R05**

**Rule:** ARBITER conversion is a low-priority service, not a phase action.

**Narrative:** At the start of each quarter, the factions draw from New Meridian the form of power their doctrine is built to gather. The city yields it. The faction breathes. This is natural — each faction's theory of power is calibrated to this city, to its rhythms, to what it produces and what it withholds.

The Translation is different. A faction requesting The Translation is admitting their doctrine was insufficient for what they needed. They are asking ARBITER — the Chorus's instrument — to transmute one form of human power into another. That is not how power is supposed to move. The city did not design that pathway. The Chorus did not either. ARBITER accommodates it. No explanation is required. No judgment is expressed. The Chorus has seen what the faction needed — and what they gave away to get it.

> *"The conversion is granted. The request was noted."*
> — ARBITER, The Record register

> *"You make the request and then ARBITER is busy. Resolution happens. Debrief opens. You wait. Eventually ARBITER turns to you. No apology for the delay. No explanation. 'The conversion is granted.'"*
> — Network operations coordinator, session notes

**Mechanics:** Resource conversion (The Translation) is available during Debrief and between phases only. It is not available during Resolution Beats 1–4 or while ARBITER is processing board changes. The applicable conversion rate is defined in Artifact 03 and subject to D02a-01 (Chorus Node presence modifier). Procedure in Artifact 03 §12, §14.

*Source: Artifact 03 §12, §14.*

*Governs: Artifact 07 scripting. See also D02a-03 (Portrait consequence of requesting Translation).*

---

**00-R40**

**Rule:** ARBITER executes general procedures, not card-specific instructions. All ARBITER-facing content in the game must map to defined, generalizable procedures that apply uniformly across all game states in their category — derivable from a reference document, without per-card notes or per-beat tracking tables. Physical tools (card UI, reference mats, threshold calculators, splaying conventions) carry the complexity; ARBITER carries the judgment.

**Narrative:** ARBITER is a human player, not a computer. The game must protect that experience. An ARBITER maintaining per-card notes, per-beat tracking tables, and card-specific exception procedures is not playing — they are administering. The mechanism for protecting ARBITER's experience is generalization: rules learned once and applied everywhere.

*Source: L187. See also: 00-R40a (faction monitoring of permanent effects).*

*Governs: All artifacts defining ARBITER-facing procedure or content. Each governing artifact implements this rule within its own scope.*

---

**00-R40a**

**Rule:** A faction that plays a permanent effect is responsible for monitoring and enforcing that effect for its duration. When a violation occurs, the owning faction calls it; ARBITER adjudicates and applies the consequence. ARBITER does not proactively track faction-played permanent effects between calls.

**Narrative:** The faction that issued the regulation enforces it. ARBITER does not maintain a running watch on every card in play — that is the owning faction's obligation. Faction law, faction enforcement.

**Mechanics:** At resolution of a permanent card, the playing faction assumes monitoring responsibility. When a violation is called, ARBITER adjudicates and reverses the violating board change. If the owning faction does not call a violation at the time it occurs, the board state stands (00-R06a). Other players may call clearing conditions on any active permanent effect; ARBITER adjudicates all calls.

*Source: Corollary to 00-R40. See also: 00-R06a (committed board states).*

*Governs: All faction-played permanent effects.*

---

## 4. Board Transparency

Rules governing what is always visible and what is never visible on the board surface.

---

---

**00-R06**

**Rule:** All board state is always publicly visible.

**Narrative:** Physical presence in a city cannot be hidden. A structure exists. Deployed operatives are in the streets. The Table is a forum of acknowledged power. No one can have an invisible building.

**Mechanics:** Presence tokens, deployment markers, structure blocks, control flags, established markers, and tension markers are visible to all players at all times. Nothing on the board surface is ever hidden. The board is the single source of truth for all publicly knowable game state. Cards and ARBITER scripts may not create mechanics that place hidden state on the board surface.

*Source: Design Pillar 1 (Artifact 00 §5), Artifact 01 §5, Artifact 02a §5, Artifact 03 §5.*

*Governs: All artifacts. No exceptions.*

---

**00-R06a**

**Rule:** Board states are committed on resolution. Once an effect resolves and alters the board, that change is fixed — no subsequent card, effect, or procedure may retroactively nullify it. Countering an established board state requires a forward action: remove it, override it, or modify it going forward.

**Narrative:** The building was built. Demolish it to counter it. The signal was transmitted. You respond to what was sent.

**Mechanics:** Effects resolve against the board state as it exists at time of resolution. An effect already in place is the board state the next effect resolves against. There is no mechanism for undoing a committed board state — only for acting on it going forward.

*Source: Corollary to 00-R06. See also: 00-R09 (changes applied immediately), 00-R40a (factions police permanent effects).*

*Governs: All card effects, all phases.*

---

**00-R07**

**Rule:** The Chorus Portrait track is always private.

**Narrative:** If factions could see what the Chorus has recorded about them, they would perform for it. The Chorus is not interested in performances. It is interested in behavior under conditions where the evaluation is not visible. The moment a faction knows it is being watched this way, the watching changes what they do. The Portrait must remain invisible to remain meaningful.

> *"We spent three months trying to figure out what ARBITER thought of us. Completely wasted. You can't read it."*
> — Ghost analyst, debrief notes

**Mechanics:** Factions cannot see their own Portrait position or any other faction's position. ARBITER communicates Portrait state only through Debrief observations and the Chronicle — never through direct numerical disclosure. No card or mechanic may grant a faction read access to the Portrait track. Setup procedure in Artifact 03.

*Source: Artifact 02b §6.*

*Governs: Artifacts 02b, 07, 09. Reinforces 00-R07.*

---

**00-R08**

**Rule:** The Public Standing track is always publicly visible.

**Narrative:** A faction's standing in New Meridian is not recorded on a form. It accumulates in a thousand simultaneous interactions across the city — the doorman who hesitates, the journalist who calls back, the neighborhood that goes quiet when a faction's personnel walk through. No faction controls these. They are the city's ongoing assessment, formed without convening and visible to anyone paying attention. The factions track Public Standing because New Meridian was already tracking it before The Table existed. What The Overview displays is not a measurement. It is a transcript.

**Mechanics:** Public Standing is displayed on The Overview — not on any player's private area — and is readable by all players at all times. No mechanic may make a faction's Public Standing position private or hidden.

*Source: Artifact 02b §7.*

*Governs: Artifacts 02b, 09.*

---

**00-R09**

**Rule:** The board reflects true current state at every moment in the Quarter.

**Narrative:** What appears on The Overview cannot be negotiated away. A structure placed is placed. Presence lost is lost. The city does not hold events in suspension while the factions decide how to characterize them — it proceeds, and The Overview proceeds with it.

The Overview reflects the present moment of New Meridian — not a faction's account of it, not the state they intended to produce, not the state they are working toward. The arrow of time runs in one direction, and The Overview is its record at this instant. What has happened is already in the past; what will happen remains open. Only the present — what The Overview shows right now — is both fixed and active: the exact point from which all future action proceeds.

The factions can shape the future. They cannot revise the present. A stale Overview is not merely wrong. It is showing the wrong moment.

> *"New Meridian is not a map. It is a clock. What it shows is not where things were. It is where things are. Right now. While you're looking."*
> — Senior signal analyst, original listening station staff, orientation briefing (unofficial)

**Mechanics:** The board is never permitted to show a stale or deferred state. When a game action causes a board change, that change is made immediately upon resolution — not at the end of the beat or Quarter. Control flags, established markers, and tension markers update immediately when influence conditions change.

*Source: Artifact 03 §5.*

*Governs: Artifact 03 Resolution beats; Artifacts 02a, 09.*

---

## 5. Influence & Presence

Hard constraints on board state that cannot be overridden by card effects or special conditions.

**Narrative anchor — Presence & The Holt Index**

*Migrated to Artifact 00 §14. See Artifact 00 §14 — Presence & The Holt Index for full narrative grounding.*

---

**00-R10**

**Rule:** No faction may hold more than 6 presence tokens in a single district at any time.

**Narrative:** There is a saturation point to any faction's presence. A district can only absorb so much of one faction's atmosphere before the weight becomes something else — occupation, oppression, a kind of silence that signals nothing good. No one standing in that district is counting. The number comes from the Holt Index — adopted by The Table as the boundary The Overview could track. The factions experience the threshold. The Overview names it.

> *"You can fill a room so full of your people it collapses. Doesn't make it yours. Makes it something else."*
> — Directorate district coordinator, field notes

**Mechanics:** No faction may hold more than 6 presence tokens in a single district at any time. Deployment markers count toward this limit during the Quarter they are placed. No card effect or operative ability may place a token that would exceed this limit — the attempt fails regardless of other conditions.

*Source: L26, Artifact 02a §6.*

*Governs: All cards placing presence; Artifact 05.*

---

**Narrative anchor — Structure Blocks**

*Migrated to Artifact 00 §14. See Artifact 00 §14 — Structure Blocks for full narrative grounding.*

---

**00-R11**

**Rule:** No faction may hold more than 1 structure block in a single district at any time.

**Narrative:** A faction's investment in a district is binary: the structure block is present or it is not. It does not measure how deeply a faction has committed — only that they have. One block makes the declaration. A second cannot deepen it; the fact of commitment cannot be stated twice in the same district. A faction is established here or they are not. The Overview holds one or the other. There is no middle register.

**Mechanics:** No faction may hold more than 1 structure block in a single district at any time. No card effect may place a second structure block for a faction in a district where they already have one.

*Source: Artifact 02a §7.*

*Governs: C01, C14, P03, P09, and any future structure-placement cards.*

---

**00-R12**

**Rule:** Structure blocks are lost immediately when a faction goes Absent.

**Narrative:** Commitment requires someone to sustain it. A structure block records that a faction is invested in this district — not that they own something here. When the last of their people leave, whatever they put down remains in the district: hardware in a closet, a cold storage lease, a site office with the lights still on. What leaves The Overview is the fact of their commitment. A foothold without anyone behind it is not a foothold. The Overview does not record abandoned things.

> *"The moment Ghost left the Data Exchange, the building was just a building."*
> — Guild infrastructure report, Quarter 4

**Mechanics:** The moment a faction reaches 0 presence tokens and 0 deployment markers in a district — by any means — all their structure blocks in that district are immediately removed. No card effect can prevent this if Absent is reached. Execution procedure in Artifact 03.

*Source: L25, Artifact 02a §7.*

*Governs: All cards removing presence; Artifacts 03, 09.*

---

**Narrative anchor — Deployment Markers**

*Migrated to Artifact 00 §14. See Artifact 00 §14 — Deployment Markers for full narrative grounding.*

---

**00-R13**

**Rule:** "At least 1 presence token" always includes deployment markers.

**Narrative:** A faction in motion is still a faction present. Every faction has multiple public faces — conventions, focused operations, festivals. A deployment marker is one of those faces turned toward a specific district: concentrated, temporary, purposeful. Where presence tokens represent the ambient weight that fills a district over time, a marker is the faction actively engaging there. The distinction between a token and a marker is administrative; the presence is the same.

**Mechanics:** Any rule, card text, or restriction that states "at least 1 presence token" or equivalent applies equally to presence tokens and deployment markers. Deployment markers count as temporary presence tokens for all purposes during the Quarter they are placed. This convention is defined once here and in Artifact 02a — it is not restated on individual cards.

*Source: L14, L58, Artifact 02a §6.*

*Governs: All artifacts. Global convention.*

---

**00-R13a**

**Rule:** Deployment markers are moved, not removed. A faction always retains operational tempo on the board.

**Narrative:** A faction is an idea. Ideas draw support from beyond any single district, any single ring, any single moment of setback. The people who show up for a deployment may be the same people from last quarter or entirely new arrivals — supporters who heard the call, operatives reassigned from elsewhere, volunteers who came because the cause reached them. The faction does not stop operating because one operation concluded. The Overview does not show a faction without deployments. It shows a faction whose deployments have moved.

**Mechanics:** Deployment markers are never removed from play by card effect, operative ability, or any other game mechanic. When an effect would "remove" a deployment marker, it instead moves it: the opposing faction designates the new district, or the marker returns to Ring 3 (Baryo). A faction always has deployment markers assigned to districts on the board. If a faction has no valid placement for a marker, they may always place in Ring 3 (Baryo) unrestricted — no presence requirement, no card required, no action cost. Ring 3 (Baryo) is the unconditional operational fallback for all factions.

*Source: Design decision B — session 6.*

*Governs: All cards and effects that interact with deployment markers; Artifacts 02a, 03, 04.*

*Pending: Verify Ring 3 (Baryo) fallback rules against Artifact 01 district map — XA-32 resolved.*

---

**00-R13b**

**Rule:** No faction is eliminated from The Table.

**Narrative:** The factions are not organizations — they are ideas. The Guild's belief in infrastructure, The Network's belief in information, Ghost's belief in knowing what others do not. Ideas do not dissolve when their people leave a room. A faction that loses all physical presence in New Meridian has lost the argument for now. They have not lost the right to keep making it.

> *"Nothing on the board for two quarters. Audience response: irrelevant, finished, gone. Actual status: still seated, still speaking. New Meridian keeps discovering that The Table is not the board. The idea outlasts the position. Whether it deserves to — that's what we're here to find out."*
> — The Network, Signal Coverage broadcast, Quarter 6

**Mechanics:** A faction that loses all accumulated presence — all presence tokens removed from the board — is not eliminated from the game. Deployment markers remain in play per 00-R13a; the faction retains operational tempo. Their voice, doctrine, and participation in The Table continue. They lose all resource generation derived from board presence; base generation from outside New Meridian continues. All strategic effects tied to board presence are suspended. The Chronicle records their decline.

*Source: Artifact 00 §13.*

*Governs: Artifacts 03, 07, 10.*

---

**00-R14**

**Rule:** No structures may be placed at the Chorus Node.

**Narrative:** The Chorus Node's space is not available. It was occupied before any faction arrived. What fills it predates human architecture and is not subject to human building codes. A faction can be present at the Node. They cannot build there — not because the law forbids it, but because something else is already using the space.

> *"We filed a construction permit for the Node perimeter six times. Sixth time, the permit office said the space was already occupied. There's nothing there. Just ARBITER's piece, and whatever is underneath it."*
> — Guild administrative record, permit log

**Mechanics:** The Chorus Node cannot hold any structure blocks — from any faction, by any card effect, in any game state.

*Source: L28, Artifact 01 §8, Artifact 02a §10.*

*Governs: Any card placing structures; Artifacts 01, 02a, 09.*

---

## 6. Resource & Economy

Rules governing what can and cannot be done to faction resources.

---

---

**00-R15**

**Rule:** The action system must always guarantee at least one playable option for any faction, regardless of resource state or hand composition.

**Narrative:** A faction reduced to its last unit of power can still walk into that room and make a move. The Table was not designed to produce observers — every party that holds a seat holds a voice, and a voice means an act. Not a winning act. Not a decisive one. But something declared, something committed, something that says the faction is still in the negotiation rather than watching it from outside. The Table's institutional guarantee is not comfort. It is the refusal to let attrition become elimination.

**Mechanics:** The Floor Act — a standard political act costing 1 native resource — is available to all factions at all times, outside of and regardless of deck composition or hand state. It is not drawn — it is always playable. A faction that cannot afford any card in their current hand may always play the Floor Act. Its effect is minimal by design: participation, not advantage.

*Source: Session 6 design decision — action paralysis prevention.*

*Governs: Artifact 04 (political act design); Artifact 03 (Floor Act available at Declaration phase). Reinforces 00-R16 (passive generation guaranteed) and 00-R13b (no faction eliminated).*

*Pending: Floor Act card design — D04-13 (Artifact 04 political act pass).*

---

**00-R16**

**Rule:** Passive generation cannot be blocked, reduced, or affected by any game action.

**Narrative:** Each faction has reach beyond New Meridian. The Guild has contracts in other cities. The Network has broadcasts that continue regardless of what happens at The Table. Ghost has operations no one knows about. The city cannot starve a faction's entire existence — only their presence within it.

**Mechanics:** Each faction generates 1 unit of their native resource per quarter unconditionally. No card, operative ability, World Condition, Situation Report effect, or any other game mechanic may reduce, block, redirect, or otherwise affect passive generation.

*Source: Artifact 02a §8.*

*Governs: All cards and mechanics affecting resources; Artifact 05.*

---

**00-R17**

**Rule:** District resource type does not change based on who controls it.

**Narrative:** The character of a place does not change just because someone new controls it. The Industrial Fringe is about capacity because of what it is — its infrastructure, its history, its workers — not because of who holds the flag. Conquest changes governance. It does not change geography.

**Mechanics:** A district generates its own native resource for all factions with influence there. Control changes which faction earns the most of that resource — it does not change which resource is generated.

*Source: Artifact 02a §8, L73.*

*Governs: All cards and mechanics targeting districts.*

---

**00-R18**

**Rule:** Structure block resource choice is declared publicly before income collection.

**Narrative:** What a faction chooses to produce from its infrastructure is a public statement. The city can see whether The Guild's installation is operating as a logistics hub or a labor pool this week. The choice reveals priorities. Priorities are observable.

**Mechanics:** The owner of each structure block declares publicly which resource it produces (+1 district native resource OR +1 faction native resource) before income is collected each quarter. The choice may change each quarter and differs per structure block. This declaration is not a game action and requires no card. Timing procedure in Artifact 03.

*Source: Artifact 02a §7.*

*Governs: Artifacts 02a, 03.*

---

**00-R19**

**Rule:** The Chorus Portrait accumulates without drift or decay.

**Narrative:** The Chorus does not forget. Its record of what the factions have done is complete and permanent. There is no statute of limitations on behavior observed by something that has been watching for thirty-one years. A faction that acts against its doctrine has acted against its doctrine — that does not fade because quarters have passed.

> *"It doesn't matter what we do differently from here. The record is the record."*
> — Directorate counsel, private memo, Quarter 5

**Mechanics:** Portrait scores are permanent and cumulative. There is no passive drift, recovery, or forgetting. A faction cannot passively recover Portrait — new behavior adds on top of what is already recorded. Only the ARBITER player moves the Portrait marker on ARBITER's behalf, and only in response to observed behavior.

*Source: Artifact 02b §5.*

*Governs: Artifacts 02b, 07. Reinforces 00-R01.*

---

**00-R20**

**Rule:** Public Standing modifies action difficulty, not resource income.

**Narrative:** New Meridian's opinion of a faction changes how easily they can operate there. A faction the city distrusts encounters resistance — closed doors, reluctant cooperation, hostile witnesses, customers who go elsewhere. A faction the city admires finds doors open. But the city's opinion does not determine how much power the faction can draw — only how smoothly they can exercise it.

**Mechanics:** The Public Standing modifier shifts the difficulty target threshold on all 2d10 rolls by the stated amount. It does not modify resource generation in any way. Income is determined by board presence and influence levels only.

*Source: Artifact 02b §7, §10.*

*Governs: Artifacts 02b, 03, 04, 09.*

---

## 7. Card Design Constraints

Rules that constrain all card design. A proposed card that violates any of these requires a locked decision in PM02 before it can proceed.

**Narrative anchor — What a Card Is**

*Migrated to Artifact 00 §14. See Artifact 00 §14 — What a Card Is for full narrative grounding.*

---

**00-R21**

**Rule:** Card effects have exactly one of four defined durations.

**Narrative:** Actions have consequences with natural lifespans. A disruption cleared by morning. An act that shapes a month. A commitment that holds for the quarter. A wire tripped once, then gone. A fact that persists until something removes it. The nature of the action determines how long it lives — not an arbitrary schedule.

**Mechanics:** Each card effect is assigned exactly one duration type at design time. No other duration is valid.
- **Immediate** — resolves and is removed at resolution
- **Transient** — removed at Beat 5 (end of month)
- **Seasonal** — removed at End of Quarter
- **Permanent** — persists until a named action or named condition removes it, including a self-clearing trigger on the card

*Source: L55; Artifact 03 §23; L180.*

*Governs: All card design.*

---

**00-R22**

**Rule:** Actions proceed with whatever resources are committed. Shortfalls carry consequences.

**Narrative:** The Table does not extend credit. A faction that commits less than the cost of an action has stated honestly that this is what they have. The gap between cost and commitment is real — the world reflects it. Partial commitment is not a forfeit. It is a constraint, and constraints have consequences.

**Mechanics:** Resource payment is assessed at resolution. Consequences scale to what was submitted:
- **Full payment:** action proceeds at stated difficulty.
- **Partial payment:** action proceeds with a threshold penalty.
- **Zero payment:** action is voided.

Payment timing and penalty values: Artifact 03.

*Source: Artifact 03; L180.*

*Governs: All card design; Artifact 03.*

---

**00-R23**

**Rule:** Crit success never carries an additional cost.

**Narrative:** Excellence is its own reward. A faction that executes flawlessly does not then owe a debt for having done so. The world does not punish success with a surcharge. If anything, extraordinary execution should return something — never demand more.

**Mechanics:** Crit success is always the same resource cost as success — the better outcome is the reward. Crit success may not add a cost, require a secondary payment, or impose any additional obligation. Cost reductions on crit success are permitted (e.g., "return primary cost to dispatch case").

*Source: L79.*

*Governs: All card design.*

---

**00-R24**

**Rule:** Portrait scoring fires at Resolution — unconditionally on action taken, conditionally on outcome, or both.

**Narrative:** The Chorus evaluates what a faction is. Not whether they succeeded. A faction that attempts a doctrinally aligned action — and fails — has still demonstrated something about their values. A faction that attempts something against their nature — and succeeds — has still revealed something. Intent is observable. The Chorus has been watching long enough to know the difference between who a faction is and what they managed to accomplish this quarter.

> *"Ghost ran the same surveillance op three times and failed each time. After the first failure, something moved on ARBITER's side of the table. We still don't know what."*
> — Network field observer, mid-session report

**Mechanics:** Portrait scoring fires at Resolution via two parallel mechanisms. A card where doctrine is demonstrated by the act applies its Portrait value regardless of roll outcome. A card where the outcome itself is the doctrine demonstration applies its Portrait value when the stated condition is met. A card may carry both. ARBITER applies all Portrait values present on the card at Resolution.

*Source: L82, Artifact 04 Principle 10.*

*Governs: All card design; Portrait fields in card data structure.*

---

**00-R25**

**Rule:** Ring Modifier card effects can only target districts in the ring the card originated from.

**Narrative:** Knowledge of a district is knowledge of a place. An intelligence report about the The Mid describes conditions in The Mid — those conditions do not apply somewhere else just because the report changes hands. The character of the district travels with what is known about it.

**Mechanics:** The ring restriction is specified on the card and applies at all times, regardless of which faction holds or uses it.

*Source: L66, Artifact 04 §11.*

*Governs: All modifier card design; Artifacts 09, 11.*

---

**00-R26**

**Rule:** React conditions must be publicly observable.

**Narrative:** A faction cannot react to something they do not know. If a reaction fires on a hidden condition, the faction is responding to information they should not have — which is either a cheat or a revelation of intelligence that should have been played differently. Either way, it breaks the shared reality of The Table.

**Mechanics:** React cards (Action — React) fire automatically when a named condition is met. That condition must be something any player at the table can count or observe without hidden information. Hidden conditions are not valid React triggers.

*Source: Artifact 04b §3.5, Artifact 04 Principle 5.*

*Governs: All React card design.*

---

**00-R27**

**Rule:** Corrupt applies only to physically written or recorded values.

**Narrative:** A document can be altered. An agreement can be falsified. An intelligence report can be made to say something it did not say. These exist because humans wrote them — and humans can rewrite them. What cannot be falsified is what a faction actually holds: their weight in a district, their presence in New Meridian, the operations already committed to the world. The city registers these as facts. Facts do not have a text field.

> *"You can't counterfeit the board. You can counterfeit the Accord."*
> — Syndicate legal counsel, Table advisory

**Mechanics:** The Corrupt function (Cross-Category — Corrupt) applies only to values that are physically written or recorded in the paper prototype. Valid targets: Intel Token content, Accord agreement terms. Invalid targets: printed card text, marker positions tracked by physical placement, Chronicle narrative.

*Source: Artifact 04b §3.4.*

*Governs: All Corrupt card design; current Corrupt card: C20 Misdirection.*

---

**00-R28**

**Rule:** Standard language conventions apply globally and are not restated on individual cards.

**Narrative:**

> *"The parties represented at The Table did not arrive speaking the same language. Each organization brought its own doctrine, its own vocabulary, its own definitions of the same words. 'Presence.' 'Influence.' 'Engagement.' The city that drew them here is multinational in character; the contest over it is multinational in kind. The Table cannot function on ambiguity of this order.*
>
> *What these proceedings require — and what this protocol establishes — is a working vocabulary precise enough that every party means the same thing when they use it. Not the native language of any faction represented here. A negotiated precision that belongs to The Table itself, and to no one seated at it."*
> — The Directorate, Standing Protocol on Table Conduct, §1

**Mechanics:** The following phrases are defined once and apply to all cards without restatement:
- **"At least 1 presence token"** — includes deployment markers (00-R13)
- **"Delivered in case"** — standard phrase for all privately delivered effects (L59)
- **"Return primary cost to dispatch case"** — standard phrase for crit success resource refunds (L60)
- **"Any other faction"** — standard target when self-targeting is not permitted (L61)

Cards use these phrases as written. They do not define or qualify them.

*Source: L58, L59, L60, L61.*

*Governs: All card design; Artifact 09.*

---

*See Artifact 04 §1 — Card Design Principle: Doctrinal Traceability (pending 04-05 migration).*

---

**00-R29**

**Rule:** Ghost may use Gather (C05) without meeting the adjacency requirement. All other Ghost actions require adjacency.

**Narrative:** Ghost understands what is happening in a district without being there. Their intelligence operations transcend proximity — that is the nature of their doctrine. But acting on that knowledge still requires presence. Ghost can know from a distance. They cannot build, disrupt, or deploy from a distance.

**Mechanics:** Ghost may play Gather (C05) targeting any district regardless of adjacency. Adjacency requirements apply to all other Ghost cards and actions.

*Source: L69.*

*Governs: Ghost card design; any card with adjacency restrictions.*

---

**00-R29a**

**Rule:** Portrait values are printed on each card, visually coded for ARBITER to parse at Resolution.

**Narrative:** Factions do not know they are being evaluated on a Portrait track. The card's Portrait field is part of ARBITER's operating instructions — a private signal about what this action means in the Chorus's framework. The faction playing the card is not privy to that signal. They are acting. ARBITER is watching.

**Mechanics:** Each card carries a Portrait field printed on the card face and visually coded for ARBITER. The ARBITER player reads Portrait values and faction impact directly from the card at Resolution — no separate reference required. The visual system is designed to be parseable by ARBITER and opaque in purpose to faction players. Visual coding design is deferred to Artifact 09.

*Source: L47, L81, L90, Artifact 02b §5, Artifact 04 card data structure.*

*Governs: Card data structure; card layout design; Artifact 09.*

*Pending: Portrait visual coding system — D09-05 (Artifact 09 card layout pass).*

---

**00-R29b — The Missing Author Vacuum**

**Rule:** No card flavor text, Chronicle entry, or faction perspective may assert or imply that any faction knows the content of the message — what humanity should say to the Chorus.

**Narrative:** The structural gap in the doctrinal geometry is permanent and deliberate. The moment any faction claims authorship of the response, the geometry collapses. Every faction at The Table fights over medium, timing, ownership, or access. None of them are positioned to write what the message says. That vacuum is not an oversight — it is the design.

*Source: L174, 00-14.*

*Governs: All card flavor text; Chronicle entries; faction perspectives; any written material implying a faction position on the content — not the medium, timing, ownership, or visibility — of the reply.*

---

## 8. Information & Privacy

Rules governing what information can be held, disclosed, and acted upon.

---

---

**00-R30**

**Rule:** Private information is disclosed only at the holder's discretion.

**Narrative:** Information held is information owned. The Table does not compel confession. A faction's intelligence, directives, and hand are their own to use as they see fit — to share, to weaponize, to withhold, or to lie about. No rule forces a faction to reveal what they know. That would not be a negotiation. It would be an interrogation.

> *"What I know and what I tell you are two different things. That's not a threat. That's The Table."*
> — Ghost Table representative, open session

**Mechanics:** Any private information a player holds — Intel Tokens, hand cards, modifier cards, classified directives, or any other private component — is disclosed only when the holder chooses. The holder may share it publicly, privately, partially, or not at all. No card may force a faction to disclose held private information without a Reveal effect.

*Source: Artifact 02b §5, §8.*

*Governs: Artifacts 02b, 04, 05, 08.*

---

**00-R31**

**Rule:** Verbal claims about undisclosed private information cannot be verified by ARBITER.

**Narrative:**

> *"Words are cheap at The Table. A faction can claim to hold anything. If they want to prove it, they can show it. Until then, they're just talking."*
> — Network Table representative, open session

> *"ARBITER knows what is actually held — every note, every directive. ARBITER will not be used as a prop in a deception. If a faction wants to prove what they hold, they must reveal it. ARBITER watches. ARBITER does not narrate."*
> — ARBITER, The Record

**Mechanics:** A faction claiming to hold a specific Intel Token, hand card, or any other private component cannot ask ARBITER to confirm or deny the claim without a specific game action (e.g., a Reveal card). ARBITER knows the true state of all holdings. ARBITER does not validate bluffs or threats that reference undisclosed private information.

*Source: Artifact 02b §8.*

*Governs: Artifacts 02b, 04, 07.*

---

**00-R32**

**Rule:** Discarded Intel Tokens are permanently removed from play.

**Narrative:**

> *"Twelve days of source contact in that note. Three locations, two operational windows, one name we'd been building toward for months. Thirty seconds in the shredder. You tell yourself you had to — and maybe you did. But there's no 'had to' that gives it back."*
> — Ghost field operative, after-action debrief

**Mechanics:** An Intel Token discarded by its holder is immediately and permanently removed from the game. It cannot be retrieved, examined after the fact, or referenced by any player or ARBITER in any subsequent game action.

*Source: Artifact 02b §8.*

*Governs: Artifacts 02b, 04, 09.*

---

**00-R33**

**Rule:** Intel Token holding guidelines are doctrinal expectations, not mechanical limits.

**Narrative:**

> *"We hold four because the city is always four steps ahead of what you think you know. Two notes is a discipline for factions that trust their other resources. We trust information. That's not excess. That's doctrine."*
> — Ghost intelligence lead, internal briefing

> *"The Directorate carried three notes into Quarter 5. Their doctrine calls for two. The third was a source contact they hadn't acted on. The Chorus noted the hesitation. Not the note. The hesitation."*
> — ARBITER, The Observation

**Mechanics:** The Intel Token holding guideline (standard factions: 2 tokens; Ghost: 4 tokens; self-directed tokens exempt) is a doctrinal expectation, not a mechanical enforcement. ARBITER does not force factions to discard excess tokens.

*Source: Artifact 02b §8.*

*Governs: Artifacts 02b, 07.*

---

## 9. Quarter & Timing

Rules governing when things happen, in what order, and what the timing locks.

---

---

**00-R34**

**Rule:** Phases do not overlap.

**Narrative:** The Table has structure because structure is how civilized parties conduct business. The phases of a quarter are the agreed order of operations — an understanding among all parties about when things happen. Breaking phase order does not just violate a rule. It breaks the pretense of civilization that The Table depends on.

**Mechanics:** No action valid in a later phase may be taken in an earlier phase. No action from a prior phase may be revisited once the next phase begins. Phase announcement procedure in Artifact 07.

*Source: Artifact 03 §6.*

*Governs: Artifact 03; Artifact 07.*

---

**00-R35**

**Rule:** Commitment is irreversible.

**Narrative:** A Dispatch Case, a declared act, a spent resource — these are facts that exist in the world now. The world does not allow uncausing. A faction that commits to something has committed. There is no taking it back, no reconsidering, no polite withdrawal. The Table moves. What was done was done.

> *"The moment you close that case, you've done it. There is no 'I changed my mind.'"*
> — Syndicate operations lead, training brief

**Mechanics:** A closed dispatch case cannot be opened or modified. A declared political act cannot be withdrawn or changed. Submitted resources cannot be reclaimed. These commitments are permanent from the moment they are made.

*Source: Artifact 03 Principle 2.*

*Governs: Artifacts 03, 04, 07.*

---

**00-R36**

**Rule:** Critical results apply regardless of modifiers.

**Narrative:** Sometimes the world just happens. The best-prepared operation fails on a stroke of bad luck. The most desperate attempt succeeds against all odds. Training and preparation narrow the range of outcomes — they do not eliminate the edges. The Table acknowledges that the world is not fully controllable.

> *"Best-planned operation of the session. Numbers came up wrong. Nothing to learn from it. That's the world."*
> — Ghost senior analyst, debrief notes

**Mechanics:** Critical Success (01–05) always succeeds regardless of any modifier that would otherwise make the action impossible. Critical Fail (96–00) always fails regardless of any modifier that would otherwise make the action automatic. These ranges are hard floors and ceilings that modifiers cannot override.

*Source: Artifact 03 §12 — The 2d10 System.*

*Governs: All card design; Artifact 09.*

---

**00-R37**

**Rule:** Submission order is the tiebreaker within resolution priority tiers.

**Narrative:** Decisiveness is a form of power. At The Table, those who commit first shape what comes after. A faction that hesitates — even by moments — has ceded something to the one that did not. The order cases arrive is the order they are resolved when all else is equal. Speed is not everything. But it is not nothing.

**Mechanics:** When multiple operations in the same beat are otherwise equal in priority, they resolve in the order their dispatch cases were submitted. Faster submission earns resolution priority. This applies within Beat 3 and within Beat 4.

*Source: L16, Artifact 03 §9.*

*Governs: Artifact 03; Artifact 07.*

---

**00-R38**

**Rule:** Findings decay applies at close of Debrief, before Round Tracker advances.

**Narrative:**

> *"Sources go quiet. Windows close. That note you're holding from the start of the quarter — the source may have moved, the target may have adjusted, the window may be gone. You can't know which. What you can know is that the longer you hold it, the more it costs you. Release it before it starts working against you. That is the discipline."*
> — Ghost senior intelligence officer to a field analyst, end-of-quarter debrief

**Mechanics:** Findings decay is the first action at end of quarter, occurring after Debrief closes and before the Session Timeline advances. This timing is fixed and cannot be modified by card effect. Decay procedure in Artifact 03 §13.

*Source: Artifact 03 §13.*

*Governs: Artifact 03; any future mechanic affecting Findings.*

---

**00-R39**

**Rule:** Each action committed to The Table — covert operation or public act — requires one Dispatch Token.

**Narrative:** Internal capacity is not the same as organizational readiness. A faction can have the resources, the personnel, and the doctrine aligned for an operation — and still not have its internal machinery synchronized to execute it this quarter. The token is the accounting of that synchronization: approvals completed, internal and external commitments made, the organization having said yes. Without it, the operation exists as a plan. It does not exist as an action.

**Mechanics:** Each action requires one Dispatch Token:
- **Covert operation:** One token placed in the dispatch case with the submitted operation card. A card submitted without a token is invalid — rejected by ARBITER at Beat 0, returned to the acting faction without resolution. Cost is not spent.
- **Public act:** One token placed on top of the declared card on the Overview at Phase B (Public Declaration). The token is returned to the faction at Beat 4 Step 1 (Submit Payment).

Full rules and component definition: Artifact 02a §8.

*Source: Artifact 03 §9; L180.*

*Governs: Artifacts 02a, 03.*

---



## Appendix A — Rule Summary

| ID | Rule | Mechanism |
|----|------|-----------|
| 00-R01 | ARBITER is sole mover of the Portrait marker | ARBITER player only; no other participant; no card Effect may reference Portrait movement as player-visible |
| 00-R02 | ARBITER speaks only in four defined registers | Record, Observation, Reckoning, Witness; every communication in exactly one; no register outside these four |
| 00-R03 | ARBITER does not explain evaluative decisions; may self-reflect | Scores and rulings never justified; ARBITER player ruling is final; self-reflection in Reckoning register only, rarely |
| 00-R04 | ARBITER's Node presence is categorically beyond faction influence | Single fused piece at Chorus Node — never removed; Dominant structurally unreachable there |
| 00-R05 | ARBITER conversion is low-priority, not a phase action | Translation available during Debrief and between phases only; rate in Artifact 03 / D02a-01 |
| 00-R06 | All board state is always publicly visible | Nothing on board surface ever hidden; no card may create hidden board state |
| 00-R06a | Board states are committed on resolution | Once established, no effect may retroactively nullify a board state — countering requires a forward action |
| 00-R07 | Chorus Portrait track is always private | No faction sees any Portrait position; ARBITER communicates only via Debrief observations and Chronicle |
| 00-R08 | Public Standing track is always publicly visible | On The Overview, readable by all at all times; no mechanic may make it private |
| 00-R09 | Board reflects true current state at every moment | Changes made immediately upon resolution; no deferred or stale state permitted |
| 00-R10 | Max 6 presence tokens per faction per district | Deployment markers count toward limit; attempt to exceed fails regardless of conditions |
| 00-R11 | Max 1 structure block per faction per district | No card effect may place a second block in a district where the faction already has one |
| 00-R12 | Structure blocks lost immediately when faction goes Absent | Removed the moment a faction reaches 0 tokens + 0 markers; no card prevents this |
| 00-R13 | "At least 1 presence token" includes deployment markers | Global convention defined once here and in Artifact 02a; not restated on individual cards |
| 00-R13a | Deployment markers are moved, not removed | Opposing faction designates new district when marker is displaced; Ring 3 (Baryo) is unconditional fallback |
| 00-R13b | No faction is eliminated from The Table | Loses board-presence resource generation; retains base generation, voice, and Table participation |
| 00-R14 | No structures may be placed at the Chorus Node | No structure blocks at the Node from any faction by any card effect in any game state |
| 00-R15 | Action system always guarantees at least one playable option | Floor Act (1 native resource, always available outside deck); effect minimal by design |
| 00-R16 | Passive generation cannot be blocked or modified | 1 unit native resource per quarter unconditionally; no mechanic may reduce or redirect |
| 00-R17 | District resource type does not change by who controls it | District generates its own native resource for all factions with influence there |
| 00-R18 | Structure block resource choice declared publicly before income | Public declaration of +1 district native or +1 faction native before income collection each quarter |
| 00-R19 | Chorus Portrait accumulates without drift or decay | Permanent and cumulative; no passive recovery; ARBITER player only moves Portrait marker |
| 00-R20 | Public Standing modifies action difficulty, not resource income | Shifts 2d10 difficulty threshold; does not affect income generation |
| 00-R21 | Card effects have exactly one of four defined durations | Immediate, Transient, Seasonal, Permanent; no other duration valid |
| 00-R22 | Actions proceed with whatever resources are committed; shortfalls carry consequences | Full payment: stated difficulty. Partial payment: threshold penalty. Zero payment: voided. Timing and values in Artifact 03 |
| 00-R23 | Crit success never carries an additional cost | Same resource cost as success; cost reductions on crit success permitted |
| 00-R24 | Portrait scoring fires at Resolution — unconditionally, conditionally, or both | Two parallel mechanisms; ARBITER applies all Portrait values present on the card at Resolution |
| 00-R25 | Ring Modifier effects target only districts in the card's originating ring | Ring restriction specified on card; applies regardless of which faction holds or uses it |
| 00-R26 | React conditions must be publicly observable | Condition must be countable without hidden information; hidden conditions are not valid React triggers |
| 00-R27 | Corrupt applies only to physically written or recorded values | Valid: Intel Token content, Accord terms; Invalid: printed card text, marker positions, Chronicle narrative |
| 00-R28 | Standard language conventions apply globally and are not restated on cards | Defined once (R13, L59, L60, L61); cards use phrases as written without qualification |
| 00-R29 | Ghost may use Gather (C05) without meeting adjacency requirement | C05 targets any district regardless of adjacency; all other Ghost actions require adjacency |
| 00-R29a | Portrait values printed on card, visually coded for ARBITER | ARBITER player reads Portrait values from card at Resolution; no separate reference; visual coding design deferred to Artifact 09 |
| 00-R29b | No card flavor text, Chronicle entry, or faction perspective may assert or imply any faction knows what the message to the Chorus should say | The Missing Author Vacuum — structural gap is permanent and deliberate; governs all written material on message content |
| 00-R30 | Private information disclosed only at holder's discretion | Any private component shared, withheld, or lied about at holder's choice; Reveal effect required to force disclosure |
| 00-R31 | Verbal claims about undisclosed private information cannot be verified by ARBITER | ARBITER does not validate bluffs or threats referencing undisclosed information |
| 00-R32 | Discarded Intel Tokens permanently removed from play | Immediately and permanently removed; cannot be retrieved or referenced in any subsequent action |
| 00-R33 | Intel Token holding guidelines are doctrinal expectations, not mechanical limits | ARBITER does not force factions to discard excess notes |
| 00-R34 | Phases do not overlap | No action valid in a later phase may be taken in an earlier phase; prior phase cannot be revisited |
| 00-R35 | Commitment is irreversible | Dispatch Cases, declared acts, and spent resources are permanent from the moment made |
| 00-R36 | Critical results apply regardless of modifiers | Crit Success (01–05) always succeeds; Crit Fail (96–00) always fails |
| 00-R37 | Submission order is tiebreaker within resolution priority tiers | Faster submission earns resolution priority within Beat 3 and Beat 4 |
| 00-R38 | Findings decay applies at close of Debrief, before Session Timeline advances | First action at end of quarter; timing fixed; cannot be modified by card effect |
| 00-R39 | Each action — covert operation or public act — requires one Dispatch Token | Covert: token in dispatch case; no token = rejected at Beat 0, cost not spent. Public act: token on declared card at Phase B, returned at Beat 4 Step 1 |
| 00-R40 | ARBITER executes general procedures, not card-specific instructions | All ARBITER-facing content maps to generalizable procedures derivable from a reference document; physical tools carry complexity; ARBITER carries judgment |
| 00-R40a | Factions police their own permanent effects | Owning faction monitors and calls violations; other players may call clearing conditions; ARBITER adjudicates all calls — ARBITER does not proactively track |

---

*End of Artifact 00a — Governing Rules & Design Policy v0.4*
*Populated from review of all V1 artifacts: 00, 01, 02a, 02b, 03, 04, 04b, PM01, PM02, PM03*
*46 rules across 7 categories (§3–§9). Pending re-sign-off S67 (L187 — R40 relocated to §3; R06a, R40a added S67).*
