# Reference — Design Pillars & Governing Rules (00a §4+)
*Load when: design principle arguments, canonical definition disputes, source-of-truth questions.*

**Art 00a content starts at §4.** §1–§3 are document structure (overview, index, meta-design for how 00a itself is written — not game content). §4 = Foundational Design Pillars. §5+ = governing rules by domain (Portrait, ARBITER procedure, board state, etc.). The title of the artifact — *Governing Rules — Design Policy* — describes §4 onward.

---

## §4 Foundational Design Pillars

These are premises — not constraints — from which all governing rules derive. Violating a pillar changes the fundamental nature of the game.

**4.1 — The Overview Is Truth.** No hidden state on The Overview. Everything shared is visible there. What factions conceal lives in Terminals, hands, and Dispatch Cases — never on the shared display.

**4.2 — Information Has Timing.** Secrecy is temporary. The game moves toward disclosure. Covert Operations may be discovered; Intel Tokens age and expire; hidden directives surface at session end.

**4.3 — Negotiation Is Mandatory.** No faction can achieve its goals alone. The most significant actions require resources, relationships, and cooperation no single faction can generate independently. Cooperation is incentivized even when it is politically uncomfortable.

**§9.2 — Cross-Faction Resource Economy** *(governing rule derived from 4.3; see 00a §9.2 for full Rule/Narrative/Mechanics)*: Every faction's native resource must be economically demanded by every other faction. Mono-resource plays are the floor (limited power); cross-faction-resource plays are the ceiling (more powerful, require prior trade). The action set must provide spending destinations for every native resource. The highest-power plays — including Apex — require at minimum one of each faction's native resource. *Source: Design Pillar 4.3. Governs: Art 04, Art 05.*

**4.4 — Control of Systems Defines What Outcomes Are Possible.** Who controls districts, structures, and resource flows determines which answers to the Chorus remain viable. Players don't pick an ending — they shape what endings remain possible.

**4.5 — The System Decides.** Players shape the system through their actions. The system produces the answer. No single player or faction decides what humanity says. What becomes inevitable emerges from what The Table does.

**4.6 — Narrative and World Consistency.** Every rule must carry a narrative grounding. If narrative reasoning and mechanical reasoning conflict, narrative takes precedence. If the narrative reason for a rule cannot be stated, the rule may be arbitrary. **Art 00 is the origin of all canonical narrative.** Downstream artifacts may reference, summarize, or point to Art 00 narrative — they may not introduce canonical narrative of their own. Art 00 is amended first; downstream artifacts reference it. A narrative statement that does not have its origin in Art 00 is not canonical. *(Source: PM02 L195. Governs: all V1 artifacts.)*

**4.6a — Overview Zone Anchoring.** Every zone, track, and strip on The Overview must have a narrative anchor before visual design is finalized.

**4.6b — The Missing Author Vacuum.** No faction at The Table is positioned to write the content of humanity's response to the Chorus. The structural gap in the doctrinal geometry is permanent and deliberate. The factions fight over medium, timing, ownership, and access. The moment any faction claims authorship of the message itself, the geometry collapses. No card flavor text, Chronicle entry, faction perspective, or any authored content in The Signal may assert or imply that any faction knows what the message to the Chorus should say. *(Source: PM02 L174, Art 00 §14.)*

---

## ARBITER Design Principles

*Sourced from Art 00a §4.7–§4.7b. Two distinct identities must be kept terminologically separate across all artifacts.*

**4.7 — ARBITER vs. The ARBITER Player.** **ARBITER** = the in-world entity. The Chorus's instrument. Complete information. Four registers. Does not advocate — reveals, withholds, times. In technology-enhanced implementations, ARBITER is the system. **The ARBITER player** = the human performing ARBITER's role in the paper prototype. Operates in two modes: as ARBITER (embodying the entity) and as game engine (rolling dice, applying difficulty, stating outcomes — functions automated in later implementations). *Conventions:* narrative fields and ARBITER scripts → always "ARBITER." Mechanics fields → "ARBITER" for entity-level acts; "The ARBITER player" for physical paper prototype execution. Rule statements → "ARBITER." These identities are the same person in the paper prototype; they will not be in all implementations.

**4.7a — ARBITER Player Is Human.** The ARBITER player is a human at the table. All ARBITER-facing design must protect this operative reality. The mechanism of protection is simplification: general procedures, faction monitoring, and immediate authority. The question is never "can ARBITER do this?" but "can ARBITER do this reliably, every time, under table pressure, without degrading the game?"

**4.7b — ARBITER Cognitive Efficiency.** Every rule, card effect, and procedure involving ARBITER must ask: how can this narrative function be implemented while impacting the ARBITER player as lightly as possible? Implementation preference order: (1) physical objects carry their own state; (2) faction players monitor and enforce; (3) general procedures applied uniformly; (4) per-card special cases — only when the above are unavailable. If a narrative function cannot fit this order without significant overhead, it is deferred to L2+ or redesigned.

---

## Guaranteed Effects

*Sourced from Art 00a §4.8–§4.8d. Invariants — not defaults or guidelines. No card, rule, mechanic, or player action may override them.*

**4.8 — Guaranteed Effects.** Certain game properties are declared constant. These are invariants. They exist to guarantee that the world of The Signal remains consistent regardless of player choices, card combinations, or edge conditions.

**4.8a — District Character Is Intrinsic.** No card, effect, or mechanic may change what a district fundamentally produces. Conquest changes governance — it does not change geography. A district generates its particular resource because of what it is, not because of who holds the flag. *(Source: Art 02 §8, PM02 L73.)*

**4.8b — Irreducible Chance.** The probability system has hard floors and ceilings that no modifier can override. A best-prepared operation can fail; a desperate attempt can succeed. This is a design statement about how the world works, not a mechanical convenience. *(See also: Art 03 §9.4; Art 04 crit ranges are hard constraints, not guidelines.)*

**4.8c — The Game Guarantees a Playable Floor.** No faction may ever be without a valid action, regardless of resource state or hand composition. A faction reduced to its last unit of power can still make a move. The Table was not designed to produce observers.

**4.8d — Passive Generation Is Inviolable.** Each faction has reach beyond New Meridian. No game action may reduce, block, redirect, or affect a faction's passive resource generation. The city can constrain a faction's presence within it — it cannot starve their entire existence. *(Source: Art 02 §8.)*

---

## §3 — Design Principles for 00a

*Governs how 00a itself is written — not the game.*

- **Pillars are premises, not constraints.** A §4 entry cannot be violated without changing the fundamental nature of the game — it spans the entire design and answers "why does this game work this way?" §4 entries carry no Governs field — they are global premises, not artifact-governing rules.
- **No exception clauses.** If a rule needs an exception, reframe it or give the exception its own numbered rule. Exceptions signal incomplete framing.
- **Mechanics field:** states binding constraints only, never execution procedure. Procedure belongs in source artifacts.
- **Governs field:** permanent cross-reference listing artifacts and rules this entry constrains. §5–§10 rules carry Governs; §4 pillars do not. No Pending field — open items belong in PM05.
- **No embedded action items.** Rule text states what is true and what it governs — period. Tracking notes, Pending items, session references, and audit flags belong in PM05.
- **Never hardcode variable values** — reference the concept and point to the canonical source.

---

## §3.1 Canonical Definitions

*Source of truth for in-world vs. mechanical term equivalences.*

### Temporal Terms
| In-World | Mechanical | Source |
|----------|-----------|--------|
| Quarter | Round | Art 03 §3 |
| Month | Phase within a Quarter | Art 03 §4 |

### Component & System Terms
| In-World | Mechanical | Notes |
|----------|-----------|-------|
| The Chorus | Extraterrestrial transmission | 31-year non-repeating signal. Best interpretation: a question. |
| New Meridian | Game board | City of 800K built around a listening station. |
| The Chorus Node | Central district | Original detection installation — ARBITER's district. |
| The Table | Five factions + ARBITER | Deliberative body. No formal authority or enforcement. |
| ARBITER | Game facilitator | Complete information. Does not advocate. Reveals, withholds, times. |
| The Chronicle | End-of-session narrative | ARBITER's written record in The Witness register. |
| Resolution | ARBITER's track | Private measure of The Table's coherence. Not visible to factions. |
| The Overview | Game mat / shared display | MIRROR's holographic rendering of New Meridian. |
| Footprint | Physical board presence | All placed influence markers, Structure Blocks, Deployment Markers. |
| The Backlog | Shared Dispatch Token pool | Queue of authorized but uncommitted operational work. |
| Dispatch Case | Sealed envelope/box | Protocol for covert submission. |
| Public Standing track | Popularity track | Bell curve with natural drift. |
| Chorus Portrait | Portrait score | ARBITER's private faction-alignment assessment. |
| Intel Token | Proof token | Confirmed intelligence held privately. |
| Presence Token | Influence token | Felt weight of faction power in a district. |
| Operational marker | Claim marker / Deployment Marker | Temporary deployment; counts as Presence Token during Quarter. |
| Classified Directive | Hidden objective card | Full-arc faction objective; surfaces at session close. |
| Situation Report | World event card | Two-card system: public narrative + ARBITER effect card. |
| Countermeasure Card | Reaction card | Reactive card type. Art 03 §10. |
| Field Operative Dossier | Agent card | Faction's single named operative; the one who can make the Apex play. |

### Faction Resources (Canonical)
| Term | Faction | Core Statement |
|------|---------|----------------|
| Findings | Ghost | The power of knowing. |
| Exposure | Network | The power of being seen. |
| Capital | Syndicate | The power of economic control. |
| Capacity | Guild | The power of building and doing. |
| Mandate | Directorate | The power of institutional legitimacy. |
