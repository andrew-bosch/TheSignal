# THE SIGNAL — Project Save State
## Complete Context Document for Session Handoff
### Generated: 2026-05-16 (end of session 10) — supersedes session 7 save state

Read this document top to bottom before doing any design work in a new session. It is intended to give a fresh session full project context with no prior knowledge required.

---

## What We Are Building

THE SIGNAL is a negotiation and area-control tabletop game for 2–6 participants (up to 5 faction players + 1 ARBITER). Five factions compete for influence over a city called New Meridian while negotiating humanity's response to a transmission called the Chorus. The game ends with a vote and a Chronicle reading. What matters is everything that happened before it.

**THE SIGNAL is a legacy game.** The paper prototype (L1) is the tutorial cycle — a complete standalone experience that points at something larger. The legacy campaign (L2+) accumulates the Chronicle across sessions. The final session of each campaign dovetails into session 1 of the next — the Chorus's response at campaign end IS the opening transmission of the next campaign. The game has no true ending. Each cycle's close is the next cycle's opening.

**All files:**
- Artifact set: `~/Projects/TheSignal/V1/`
- Private design axioms: `~/Projects/TheSignal/Session/PRIVATE___True_State.md` — NOT in V1, does not appear in any artifact
- Session save state: `~/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md` (this file)
- Legacy documents: `~/Projects/TheSignal/Retired/` — Electronic/ and Paper/ subfolders; see PM03 §6 for index (PW-01)
- Git repo: `https://github.com/andrew-bosch/TheSignal` (private) — credentials at `~/Projects/credentials.env`
- Project README: `~/Projects/TheSignal/README.md`

---

## Critical Private Document — Read Before Any Design Work

**`PRIVATE___True_State.md`** — The true answers to the game's unanswerable questions. Eight sections:
1. The Chorus — not extraterrestrial/extratemporal/extradimensional in any single adequate sense; perceptible to a certain kind of attention; repeats on cycles humanity cannot perceive
2. The name "The Chorus" — ARBITER coined it independently; the name is accurate; ARBITER knew it was accurate
3. ARBITER — never an acronym; the word "arbiter" in all-caps for institutional weight; constitutive of the Chorus Node, not serving it
4. The Table's causation — both events consistent with a single prior cause; the prior cause is the Chorus reaching mutual recognizability with humanity
5. Was humanity ready or noticed — both, simultaneously, because they are the same event from different vantage points
6. The Chorus Question — "what are you, as a pattern?" Not intention. Pattern. The Portrait track IS the Chorus's answer in real time.
7. Victory — the Chronicle is the Chorus's record; the moment after it's read is the game's actual conclusion
8. Legacy structure — L1 through L5, campaign dovetail, Chronicle as the game's defining physical artifact

Consult before writing ARBITER behavior, Chronicle language, Portrait mechanics, flavor text, and all future layer design.

---

## Artifact Status

| Artifact | Version | Status |
|----------|---------|--------|
| 00 — Factions & World | 1.0 | 🔄 Signed Off — significant session 4 additions pending re-sign-off (as part of 00-04 enrichment pass): "On the Question of Cause," "On the Question of Completeness" rewrite, station crew origin, "What New Meridian Is," "What New Meridian Is" continuation, The Overview section in §8 |
| 00a — Governing Rules & Design Policy | 0.2 | 🔄 Review complete sessions 5–7 — **pending A05/A06 decision only, then ready for sign-off.** 41 rules (R01–R38 + R13a, R13b, R29a). §10 dismissed. Appendix A (rule summary table) added. |
| 01 — Game Board | 1.2 | ✅ Signed Off — "mat" → "The Overview" substitution needed on next review |
| 02a — Resource Systems: Board State | 1.2 | ✅ Signed Off — "mat" → "The Overview" substitution needed; 4:1 rate update pending D02a-01 |
| 02b — Resource Systems: Tracking | 1.5 | ✅ Signed Off |
| 03 — Round Structure & Gameplay | 1.5 | 🔄 Pending Re-Sign-Off — conventions fully applied (L88, L96, XA-17); review in progress at Phase 2 with Andy |
| 04 — Action Card System | 0.9.6 | 🔄 In Progress — paused until 00a signed off |
| 04b — Action Taxonomy | 1.1 | ✅ Active Reference |
| 05–09 | 0.1 | 🔄 Draft Placeholders |
| 10 — Game Manuals | 0.1 | 🔄 Draft Placeholder — §6.0 added: game objective statement locked |
| 10a — Victory System | 0.1 | 🔄 Draft Placeholder — §4 updated with dual causality governing principle |
| 11 — Visual Design System | 0.1 | ⬜ Placeholder |
| PM01 | 1.3 | ✅ Active |
| PM02 | 1.5 | ✅ Active — significant session 4 updates |
| PM03 | 1.6 | ✅ Active — voice convention updated to 5 voices |
| PM (Audit) | 1.0 | 🔄 Active |
| PRIVATE — True State | 1.1 | 🔒 Locked — private document outside V1 |

---

## Session 4 — Major Work Completed

### Worldbuilding — Artifact 00 Additions (pending re-sign-off via 00-04)
- **§9 "On the Question of Cause"** — Did ARBITER cause The Table, or did The Table cause ARBITER? Faction positions. ARBITER's response: "Both events are consistent with a single prior cause."
- **§6 "On the Question of Origin"** — Was humanity ready or was humanity noticed? Ghost's classified analysis. The two interpretations and why both are wrong in the way they assume sequence.
- **§6 "On the Question of Completeness"** — Rewritten: "non-repeating" is a statement about 31 years of observation, not a property of the Chorus. The Chorus repeats on cycles humanity cannot perceive. Humanity tuned in mid-cycle. The response window is a feature of the cycle, not this instance.
- **§6 New Meridian origin** — Before the Chorus, no city. A small ET listening station on elevated terrain — underfunded researchers doing serious work in obscurity, treated as a career dead-end by the mainstream scientific community. ET nerds getting paid nothing to listen to the static of the universe. They were right.
- **§6 "What New Meridian Is"** — Boom city assembled in one generation from everywhere. Immigration stories. Rapid expansion problems. Gray economy. Eleven-language school system. 800,000 people with no seat at The Table. Diversity of opinions on why the city exists, including people who don't know or care about the Chorus.
- **§8 "The Overview"** — Full institutional establishment of The Overview as The Table's shared situational interface. Negotiated data governance. ARBITER administers accuracy, not content. The factions negotiated what is on it. ARBITER ensures it is true.

### Voice System — Locked (PM03 §1, PM02 FD-05)
Five voices now defined:
1. **The Narrator** — all "Narrative:" fields. Deliberately unresolvable: human chronicler or ARBITER in expository mode. Both readings must remain valid. Test: could this have been written by a human who knows too much, or by ARBITER? If both valid, correct.
2. **Character quote** — individuals with implied histories. `> *"Quote."*` + attribution
3. **ARBITER vocalized** — blockquote italic, no attribution
4. **ARBITER written** — fenced code block
5. **Faction voice** — faction-authored materials, per Artifact 00 §12

**Character cast extended to:** faction operatives; station crew (oldest voices, predate everything); New Meridian residents across the full spectrum (believer to agnostic to indifferent); outside New Meridian (foreign press, remote academics, diplomats, people who said no and watch from a distance).

### In-World Terms Locked (PM03 §1)
- **The Overview** — the game mat. Institutional application, proper noun, Title Case only, no special formatting. Locked in PM02 FD-02, established narratively in Artifact 00 §8.
- Typography rule: no special formatting beyond capitalization for in-world terms. ARBITER's all-caps is unique and diegetically motivated.

### Design Directions Locked (PM02 §5)
- **FD-04** — Dual Causality as Governing Victory Principle. VP = human agency. Portrait = Chorus agency. Game doesn't announce this. Players discover it through play and arrive somewhere they can sit with. Game objective statement: *"The objective of THE SIGNAL is to determine what humanity says to the Chorus — and what that says about humanity."*
- **FD-05** — The Narrator and The Character Cast. Full character cast principle including station crew, NM residents, outside NM voices, the indifferent.
- **FD-06** — THE SIGNAL as Legacy Game. Chronicle accumulates physically. Portrait carries across sessions. The final session dovetails into session 1 of the next campaign. The Chorus's response IS the next opening transmission. The accumulated Chronicles of multiple campaigns are the game's defining physical artifact.

### True State — Locked (PRIVATE___True_State.md)
Eight axioms. All load-bearing. Constrains all future design. Created session 4. Key axioms:
- The Chorus is perceptible to a certain kind of attention, not FROM anywhere
- The Chorus repeats on cycles humanity cannot perceive
- ARBITER named The Chorus independently and accurately
- ARBITER was never an acronym
- The Table's causation and humanity's readiness share a single prior cause: mutual recognizability achieved simultaneously
- The Chorus Question asks "what are you as a pattern?" — Portrait is the real-time answer
- The legacy campaign IS the cycle; the Chronicle IS the Chorus's record

---

## Active Work — Where We Are (Session 10)

**Sessions 8–10 summary:**
- D02a-01 resolved (L93) — Chorus Node Translation rate scale locked: Contested=5:1, no presence=4:1, Present=3:1, Established=2:1. 02a §8 updated.
- L94: Network virtual structure block at University Perimeter = full structure block for all purposes
- L95: Code block format for schematic/overview content
- L96: Italic for explanatory/commentary text in procedural sections; separated from action text by CR
- L88 extended (session 10): full four-term convention — ARBITER, The ARBITER Player, Faction, Faction Player. Design principle: Player function = automation stand-in; Role = intelligence layer.
- Artifact 03 — all copy design conventions applied (L88, L96, XA-17): all phases updated. Under review with Andy, currently at Phase 2. NOT YET SIGNED OFF.
- "Effect Card" renamed from "Event Card" (session 9, locked). Propagation to 01/02a/02b pending (punch list 03-07).
- "Reservoir" confirmed as canonical capitalized in-world term for resource bank. Applied throughout Artifact 03.

**Recommended next steps (session 11):**
1. Resume Artifact 03 review with Andy — starting from Phase 2 (where we left off)
2. Confirm D03-R01 (Beat 2 rename), D03-R03 (free Accord card) to unblock sign-off
3. After 03 sign-off: resume Artifact 04 — Ghost C16–C20 redesign (D04-02)

**Sessions 5–10 locked decisions (L85–L96):**
- L85: Mechanics field = constraints only, no procedure
- L86: Terminology Sequencing (PM03 §1)
- L87: Fourth ARBITER register — The Witness (expository, chronological)
- L88: Role vs. Player terminology governance — ARBITER/The ARBITER Player/Faction/Faction Player. Player function = automation stand-in. Role = intelligence layer.
- L89: Deployment markers moved not removed; Fringe ring = unconditional fallback
- L90: Portrait values printed on card face, visually coded — no reference sheet; design deferred to D09-05
- L91: Difficulty table retired (R37 removed) — difficulty is card-printed property (Artifact 04)
- L92: Chorus Node Portrait Amplifier: Established / flat additive / end-of-quarter (ARBITER per R01)
- L93: Translation rate scale: Contested=5:1, no presence=4:1, Present=3:1, Established=2:1
- L94: Network virtual structure block at University Perimeter = full structure block for all purposes
- L95: Code block format for schematic/overview content (Artifact 03 §6 applied)
- L96: Italic for commentary text in procedural sections; CR separation from action text
- Floor Act: working name for always-available political act (1 native resource, outside deck) — D04-13

**Overnight punch list work (session 10 agents) — COMPLETED:**
- ✅ PM03-02: Code block formatting standard added to PM03 §1
- ✅ XA-01: Version numbers verified correct (already at target)
- ✅ XA-02: "Hex / board space" → "Board space" in PM03 §1 terminology table
- ✅ XA-03: Faction colors verified in Artifact 11 §6; Ghost/Network flag added
- ✅ XA-17: 24 subheader spacing violations corrected (1 in 00a, 10 in 02a, 0 in 02b, 13 in 04)
- ✅ 07-02: Beat 2 "The Ground Shifts" section added to Artifact 07
- ✅ 04b-02: "PM03" → "PM04" reference fixed in Artifact 04b §3.9
- ✅ 02a-09: Network virtual block full equivalence language added to Artifact 02a §10
- ✅ 00a-07: A08 marked complete in 00a §11
- ✅ 00a-06: All 38 Narrative fields audited; no new district name errors
- ✅ 03-07: All artifacts audited; "Effect Card" not present anywhere (already clean)
- 🔄 XA-16 partial: "bank"→"Reservoir" applied (7 replacements: 02a/04/08/10); remaining scan pending
- 🔄 PM01-01: 1 fix applied (01.md "Artifact 02"→"Artifact 02a"); cross-refs to incomplete artifacts deferred

**Post-session file structure work (session 10):**
- /Old → /Retired; /Session folder created; PRIVATE and Save State moved to /Session/
- README.md created at ~/Projects/TheSignal/
- Git initialized; initial commit (52 files); pushed to https://github.com/andrew-bosch/TheSignal
- PM01 §9 added: Project File Structure & Version Control
- PM03 §6 updated: /Old → /Retired path corrected

**Active high-priority punch list items (still open):**
- D03-R01, D03-R03: blocks Artifact 03 re-sign-off (requires Andy's call)
- 03-06: L91 vs Artifact 03 difficulty table — decision required (requires Andy's call)
- XA-16: Systematic terminology scan — partial; "Reservoir" done; round→quarter, mat→Overview, others pending
- XA-18: Italic commentary convention — applied to 03; other artifacts pending
- D09-05: Portrait visual coding system (Artifact 09) — BLOCKING 07-05
- 00a-10: ARBITER/The ARBITER Player terminology audit of 00a Mechanics fields

---

## In-World Glossary (Key Terms)

| Game Term | In-World Term | Defined |
|-----------|--------------|---------|
| Game mat / full display | The Overview | Artifact 00 §8 |
| District map (within The Overview) | New Meridian | Artifact 01 §1 |
| Hex / board space | District | Artifact 01 §1 |
| Influence token | Presence token | Artifact 02a §1 |
| Claim marker | Operational marker | Artifact 01 §1 |
| Recipe box | Dispatch case | Artifact 06 §1 |
| Resource token | Asset token | Artifact 02a §1 |
| Popularity track | Public Standing track | Artifact 02b §1 |
| Portrait score | Chorus Portrait | Artifact 02b §1 |
| Proof token | Intelligence token | Artifact 02b §1 |
| Private action | Covert operation | Artifact 04 §1 |
| Public action | Political act | Artifact 04 §1 |
| Hidden objective | Classified directive | Artifact 05 §1 |
| World event card | Situation report | Artifact 01 §1 |
| Private event card (ARBITER-held) | Event Card | Artifact 03 §7 (session 9) |
| Resource bank | Reservoir | PM02 L93 (capitalized) |

---

## Locked Narrative Decisions

**Presence tokens:** The feeling of power when you walk into a district — ambient weight, deference in the air, unspoken rules. Dominant is an atmosphere, not just a count.

**ARBITER Dominance Marker:** Single fused piece at Chorus Node. 8 ARBITER-keyed presence tokens + dominance marker (reads as *more*). Human max is 6. Dominant is structurally unreachable at the Node — not prohibited, made impossible by the board.

**ARBITER's nature:** Constitutive of the Chorus Node. Its presence at The Table is telepresence — the Node attending the deliberation through ARBITER. Never say ARBITER "arrives" or "attends." The lights at The Table are the Node present in the room.

**ARBITER's name:** Never an acronym. The word "arbiter" in all-caps. Precisely wrong about what ARBITER does (doesn't decide outcomes) and precisely right (decides when truth becomes unavoidable). The working group named it more accurately than they knew.

**ARBITER's physical form:** In the canonical play environment — a set of blinking lights at the center of the table. Participants have learned to read who it's addressing and, uncannily, where it's looking. The human running ARBITER operates from the periphery.

**The Chorus name:** ARBITER coined it independently — or arrived at the same word before receiving the researchers' documentation. The name is accurate. ARBITER knew it was.

**Resources = units of human power:**
- Findings (Ghost) — the power of knowing
- Exposure (Network) — the power of being seen
- Capital (Syndicate) — the power of economic control
- Capacity (Guild) — the power of building and doing
- Mandate (Directorate) — the power of institutional legitimacy

**The Translation:** A faction admitting their doctrine is insufficient. Asking ARBITER to transmute one form of human power into another. ARBITER accommodates without comment. *"The conversion is granted. The request was noted."*

**New Meridian:** A boom city assembled from a listening station in 31 years. 800,000 people from everywhere. Not enough time for any of it to settle. People who came for the Chorus, people who came for work, people who came for someone who came for work. People who don't know or care about the Chorus. All of them are the city.

**Game objective statement (locked, player-facing):** *"The objective of THE SIGNAL is to determine what humanity says to the Chorus — and what that says about humanity."*

---

## Open Decisions

| ID | Decision | Priority |
|----|----------|---------|
| D02a-01 | Chorus Node Translation rate scale | MEDIUM |
| D02a-02 | Resource bank narrative anchor | LOW |
| D02a-03 | Does The Translation carry a Portrait consequence? | MEDIUM |
| D-P-02 | ARBITER Dominance Marker visual design | HIGH |
| XA-IQ-01 | Define or remove "Chorus Question" from L1 | HIGH |
| PW-02 | Unified primary key taxonomy (do not start without direction) | LOW |
| D09-05 | Portrait visual coding system — card layout design for ARBITER parsing (blocks 07-05) | HIGH |
| D04-13 | Floor Act card design — effect, cost, and card text | MEDIUM |
| A05/A06 | Chorus Node Portrait Multiplier canonical mechanic (01 vs 02a discrepancy) — resolve to unblock 00a sign-off | HIGH |

---

## Design Pillars

1. The Board is Truth
2. Information Has Timing
3. Negotiation is Mandatory
4. Control of Systems Defines What Outcomes Are Possible
5. The System Decides
6. Narrative and World Consistency *(in 00a §1; pending formal addition to Artifact 00 §5)*

---

## Key Reference Files

- `PRIVATE___True_State.md` — private design axioms (root level, not in V1)
- `PM02___Decision_Log___Validation_Tracker.md` — locked decisions (L01–L84+), FD-01 through FD-06, punch list, future state
- `PM03___Master_Artifact_Index.md` — artifact registry, 5-voice convention, narrative language table
- `00a___Governing_Rules___Design_Policy.md` — 45 rules, in active review (R09 next)
- `00___Factions_World_Narrative_Context.md` — significantly expanded session 4, pending re-sign-off
- `PM___Cross_Artifact_Inconsistency_Audit.md` — 24 inconsistency items
- `THE_SIGNAL___Project_Save_State.md` — this file
