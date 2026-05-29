# PM01 — Project Charter & Work Breakdown
## THE SIGNAL P1 — Paper Prototype

**Version:** 1.6  
**Status:** 🔄 Updated — Active  
**Type:** Project Epic — all design artifacts are Features of this Epic

---

## 1. What We Are Building

THE SIGNAL is a negotiation and area-control tabletop game for 2–6 participants (up to 5 faction players plus 1 ARBITER). Five factions compete for influence over a city called New Meridian while negotiating humanity's response to an extraterrestrial transmission called the Chorus. The game ends with a vote. What matters is everything that happened before it.

The **Tier 1 Paper Prototype** is the first playable version of the game. It uses only the Physical Tier (Tier 1) of the game's intended five-tier design. All game information is public. No digital technology is required. It is played with printed cards, physical tokens, and a human ARBITER.

---

## 2. The Problem This Prototype Solves

Before any technology is developed — before hardware terminals, computer vision, projection, or AI narrative generation — we need to answer one question:

**Is the core game good?**

Specifically:
- Does the core loop (covert operations + political acts + contested territory) produce interesting decisions every quarter?
- Do the five factions feel meaningfully different in play?
- Does ARBITER's role feel rewarding rather than administrative?
- Does the session end with players wanting to play again?
- Does the narrative system (Chorus Portrait, Chronicle, Chorus Question) produce genuine emotional resonance?

These questions cannot be answered by design alone. They require observed play. The Tier 1 Paper Prototype exists to produce that observation data before any expensive development commitments are made.

### Core Assumption — Replayability

The game's replay value comes from meaningful player agency over the session's outcome and experience — not from randomized board state alone. Players return because the decisions available to them before and during a session allow them to pursue genuinely different objectives in genuinely different ways. The deckbuilding system (operative selection, hidden objective, and card pool composition) is the primary mechanical lever the design relies on to produce this.

**What the prototype must demonstrate:** players should leave a session able to articulate a different approach they would want to try. That articulation — not simply wanting to play again — is the signal the design is working. If players cannot name what they would do differently, the system is not producing meaningful strategic differentiation.

---

### Assumption to Validate — Player Count
The game is designed to accommodate **2–6 human participants**: up to 5 faction players plus 1 ARBITER. The following assumptions about player count must be validated in playtesting:

| Assumption | Risk if False | Test Method |
|-----------|--------------|-------------|
| The game is playable with 2 faction players + ARBITER | Low player count may make the board feel empty; Incursion and negotiation may not emerge organically | Run a 2-faction session; measure engagement and contested district count |
| The game is playable with a full table of 5 faction players + ARBITER | High player count may make Resolution too slow; ARBITER may be overwhelmed | Run a full-table session; measure Resolution time and ARBITER error rate |
| ARBITER can be run by any participant, rotating between sessions | Some players may find the ARBITER role unappealing or too complex | Survey post-session willingness to ARBITER again |
| The game is playable without a dedicated human ARBITER (automated fallback) | Some groups may not have a sixth willing participant | Design automated ARBITER fallback; test usability |
| Playtest sequence — 2-player vs 5-player configurations should be tested in a defined order | Testing full table first may produce noise that obscures 2-player issues; testing 2-player first may not surface full-table bottlenecks | Recommended sequence: Session 1 at 3-player (baseline); Session 2 at full table (5 + ARBITER); Session 3 at 2-player. Adjust based on availability. |

All five conditions are tracked in PM02 validation targets.

---

## 3. Approach & Strategy

### Why Paper First
Technology cannot rescue a game with broken mechanics. Building hardware, writing firmware, and training AI narrative before validating core gameplay would produce an expensive, unplayable product. The paper prototype isolates the game design variables from the technology variables — problems found at this stage cost hours to fix, not months.

### Why Tier 1 First
THE SIGNAL is designed with five information tiers per district. Attempting to validate all five simultaneously would make it impossible to isolate which tier is causing any observed problem. Tier 1 — the physical tier, fully public, no hidden information — is the foundation every other tier builds on. If it is not compelling on its own, adding tiers will not save it.

### Why This Documentation Structure
Each design document is a Feature of this Epic. Features must be independently useful (a reader can understand and act on them without reading every other document) but collectively complete (together they describe the entire game). The documentation is ordered so that each artifact builds only on concepts introduced in prior artifacts:

- **Artifact 00** introduces the world, factions, and narrative context — the "why" of everything
- **Artifact 01** introduces the board — the physical space where everything happens
- **Artifact 02** introduces resources — what is generated and tracked on that board
- **Artifacts 03–06** introduce what players and ARBITER do with those resources
- **Artifacts 07–08** introduce the tools each party uses
- **Artifacts 09–11** provide reference, specification, and production support

No artifact refers to a concept not yet introduced. Visual artifacts (V01–V19) can only be finalized after the text artifacts that define their content.

### Information Design Requirement
Every component — every card, token, track, marker, and printed surface — must have defined information requirements before visual design begins. Each artifact specifies: what information is presented, who can see it, why it exists (purpose), and how it is conveyed (format and constraints). This ensures visual design serves the game rather than decorating it.

### Document Change Governance

**Non-material changes** (corrections, clarifications, formatting, cross-reference updates, terminology alignment, adding design notes that do not alter mechanics) may be made to signed-off artifacts without requiring re-sign-off. The version number increments at the minor level (e.g., 1.0 → 1.0.1). The change is logged in PM02 Section 4.

**Material changes** (any change that alters a mechanical rule, adds or removes a phase or beat, changes a cost or effect, adds or removes a card or component, or changes a governing design principle) require the artifact status to be updated to 🔄 Pending Re-Sign-Off before the change is incorporated. The artifact must be reviewed and explicitly signed off before returning to ✅ status. Material changes are logged in PM02 Section 4 with a change description and rationale.

**What counts as material:** If a player or ARBITER reading the artifact before and after the change would make a different decision at the table, the change is material.

### Cross-Artifact Reference Convention

When one artifact references specific content in another artifact, the standard reference format is:

**[Artifact ID].[Section].[Subsection]**

Examples:
- `Artifact 04 §8` — refers to Section 8 of Artifact 04
- `Artifact 03 §12.3` — refers to Section 12, Subsection 3 of Artifact 03
- `Artifact 02b §8–9` — refers to Sections 8 through 9 of Artifact 02b
- `PM02 §2b` — refers to Section 2b of PM02

This convention applies to all in-document references, cross-artifact references in design notes, blocking decision descriptions in PM02, and punch list source citations. It provides a stable, unambiguous pointer to specific content without reproducing it. When an artifact is restructured and section numbers change, all references to that artifact should be audited and updated — this is a non-material change and does not require re-sign-off.

---

## 4. Deliverable

A self-contained tabletop game kit that can be:
- Assembled from printed and purchased components in under 2 hours
- Set up and played by a group encountering it for the first time under ARBITER guidance
- Used to run at least 3 structured playtest sessions with recorded feedback
- Evaluated against defined success criteria to determine readiness for digital development

---

## 5. Success Criteria

| # | Criterion | How Measured |
|---|-----------|-------------|
| S1 | A complete session (8 rounds) runs in 90–150 minutes | Clock |
| S2 | ARBITER can facilitate without consulting rules during resolution | Error count per session |
| S3 | All five factions feel meaningfully different in play — and players can identify a different faction or approach they would want to try next session | Players can describe opponent strategy unprompted; players can articulate an alternative strategy or faction they haven't tried |
| S4 | Players want to play Session 2 before leaving — and can name what they would do differently | Post-session question: not just "yes/no" but "what would you try next time?" |
| S5 | At least one Accord is proposed per session | Count |
| S6 | The Chronicle resonates at session end — players feel it reflects what they actually did, not just what happened | Player agreement with ARBITER's account; players recognize their own behavior in the record |
| S7 | No single faction dominates economically by Quarter 4 | Resource counts at Round 4 end |

---

## 6. Out of Scope

The following are explicitly excluded from the Tier 1 Paper Prototype:

- Digital terminals, ESP32 hardware, or any electronics
- Computer vision or board projection
- Tier 2–5 mechanics (social, wireless/communications, web/data, Chorus)
- AI-generated narrative
- Legacy or Covenant persistence between sessions
- Website or between-session content
- Full card library (366 cards) — prototype uses a minimum viable card set

---

## 7. Work Breakdown Structure

### WBS 1 — Design Artifacts

The following documents must exist and be signed off before physical production begins. They are ordered by dependency — each artifact may only reference concepts introduced in prior artifacts.

| ID | Artifact | Problem It Solves | Blocking Playtest? | Status |
|----|----------|------------------|--------------------|--------|
| 00 | Factions & World | Without narrative context, no other artifact is meaningful. Defines who the factions are, what New Meridian is, what the Chorus is, and why The Table exists. | Yes — must be first | ✅ |
| 01 | Game Board — New Meridian | Defines the physical space of play: district layout, rings, information displayed on each district, track positions, starting configuration, and board setup procedure. | Yes | ✅ |
| 02a | Resource Systems: Board State | Defines presence, influence, structures, and resource generation — the systems whose entire state is always visible on the board. | Yes | ✅ |
| 02b | Resource Systems: Tracking | Defines Chorus Portrait, Public Standing, and Intel Notes — the tracking systems that run alongside the board. | Yes | ✅ |
| 03 | Round Structure & Gameplay | Defines the seven-phase round, timing, initiative, the Apex trigger, and ARBITER conversion. Requires 00–02 to be meaningful. | Yes | ✅ Signed Off — Session 20 (v1.7) |
| 04 | Action Card System | Defines all covert operations, political acts, and faction-specific actions. Requires 00–03 for context. | Yes | 🔄 In progress — C01–C15 signed off; 12 blocking decisions open (see PM02 D04-01 through D04-12) |
| 04b | Action Taxonomy & Design Analysis | Companion to 04. Taxonomy framework, coverage gap analysis, faction design recommendations. Not a playtest-blocking artifact — reference document. | No | ✅ Active reference |
| 05 | Operative & Apex System | Defines all operatives, tier progression, Apex costs and effects, and the Founding Figure ceremony. Requires 00–04. | Yes | 🔄 |
| 06 | Messaging System | Defines the dispatch case protocol, ARBITER private communications, and Accord forms. Requires 00–05. | Yes | ⬜ |
| 07 | ARBITER Toolkit | Defines the Chorus Portrait board, Hidden Objective modes, Resolution track, Debrief reward system, resolution beats, narrative registers, Chronicle, and ARBITER script pack. Requires 00–06. | Yes | 🔄 |
| 08 | Player Toolkit | Defines player components, faction reference cards, starting resources, and classified directives. Requires 00–06. | No | 🔄 |
| 09 | Card Specifications | Defines all card content in table format for production. Requires 04–06 to be complete first. | Yes | ⬜ |
| 10 | Game Manuals | Player guide, ARBITER guide, setup guide, and components list with shopping list. Requires all prior artifacts. | Yes | 🔄 |
| 10a | Victory System | Defines all VP sources, Chorus Portrait conversion, scoring sequence, tiebreakers, and the vote mechanic. Integrated into Game Manuals but specified separately to ensure completeness. Requires 00–07. | Yes | ⬜ |
| 11 | Visual Design System | Color palette, faction identity system, component visual standards. Required before final production files. | No | ⬜ |

### WBS 2 — Physical Components

Production does not begin until relevant design artifacts are signed off. Items are listed with their design dependency.

| # | Component | In-World Name | Quantity | Source | Requires | Status | Est. Cost |
|---|-----------|---------------|----------|--------|---------|--------|-----------|
| 2.01 | Printed hex map | New Meridian | 1 (A1 or A0) | Print shop | 01, V01, V08 | ⬜ | $5–20 |
| 2.02 | Influence discs | Presence tokens | 15 per faction × 5 | Poker chips | 02a | ⬜ | $15–30 |
| 2.03 | Large distinct pieces — double-sided (normal / blocked face) | Operational markers | 2 per faction × 5 | Distinct shape; must support two faces — normal and blocked (for Event Card conversion-blocking effects) | 01, 03 | ⬜ | $5–10 |
| 2.04 | Small square chits | Structure tokens | 6 per faction × 5 | Card stock | 02a | ⬜ | $2–5 |
| 2.05 | Resource chips | Asset tokens | 30 per type × 5 | Poker chips | 02a | ⬜ | $20–35 |
| 2.06 | Faction chits + sticky notes | Intel notes | 4 per faction × 5 | Colored chits | 02b | ⬜ | $3–7 |
| 2.07 | Neutral chips | Tension markers | 6 | Neutral chips | 02a | ⬜ | $1–3 |
| 2.08 | Crown or star tokens | Control flags | 5 (1 per faction) | See D-P-01 | 02a | ⬜ | $3–7 |
| 2.08a | Fused single piece — ARBITER color | ARBITER Dominance Marker | 1 | Eight ARBITER-keyed presence tokens (white, TBD) stacked and fused, topped by ARBITER's dominance marker — same visual language as faction control flags but distinct: larger, differently keyed, or subtly off in a way that reads as *more*. All one inseparable piece. Placed at Chorus Node by ARBITER at setup. Never removed. | 00a R04, 01, 11, D-P-02 | ⬜ | $3–8 |
| 2.08b | Small silver markers | Established markers | TBD pending Art 11 component spec — 1 per Established faction per district; up to 4–5 may coexist in a single district simultaneously. Silver material distinguishes 2nd-place presence at a glance; placed on Established faction's presence chip stack. Placed and removed by the player whose action causes the influence change. Not placed at the Chorus Node. | 02a §6/§9, L111 | ⬜ | TBD |
| 2.09 | Ten-sided dice | — | 2 × d10 | Purchase | 03 | ⬜ | $2–5 |
| 2.10 | Covert operation cards | — | Per 09 spec | Print + cut | 09 | ⬜ | $8–20 |
| 2.11 | Political act cards | — | Per 09 spec | Print + cut | 09 | ⬜ | $5–15 |
| 2.12 | Operative dossier cards | Field operative dossiers | Per 09 spec | Print + cut | 09 | ⬜ | $5–15 |
| 2.13 | Modifier cards | Operational intelligence cards | Per 09 spec | Print + cut | 09 | ⬜ | $5–15 |
| 2.14 | Counter cards | Countermeasure cards | Per 09 spec | Print + cut | 09 | ⬜ | $3–8 |
| 2.15 | World event cards — two cards per Situation Report | Situation reports | Per 09 spec — each Situation Report is two cards: public narrative card (all players) + ARBITER effect card (ARBITER only). See L35. | Print + cut | 09 | ⬜ | $3–8 |
| 2.16 | Objective cards | Classified directives | Per 09 spec | Print + cut | 09 | ⬜ | $2–5 |
| 2.17 | Accord forms | Accord documents | 8 | Laminated dry-erase, 8cm × 8cm | 06 | ⬜ | $3–7 |
| 2.18 | Pass cards | — | Per 09 spec | Print + cut | 09 | ⬜ | $1–3 |
| 2.19 | Small boxes or envelopes | Dispatch cases | 1 per player | Purchase or make | 06 | ⬜ | $3–10 |
| 2.20 | Laminated strips | Public Standing tracks | 1 per faction | Print + laminate | 02b, V02 | ⬜ | $3–7 |
| 2.21 | Combined laminated strip | World Condition tracks | 1 | Print + laminate | 01, V04 | ⬜ | $1–3 |
| 2.22 | Simple strip | Quarter tracker | 1 | Print + laminate | 03 | ⬜ | $1–3 |
| 2.23 | Dry-erase grid behind screen | Chorus Portrait board | 1 | Print + laminate | 07 | ⬜ | $2–5 |
| 2.24 | Laminated A4 mat | ARBITER working mat | 1 — general ARBITER tableau surface for Portrait board, Chronicle area, and modifier token storage. Resolution Grid is a separate component (see 2.31). | Print + laminate | 07 | ⬜ | $1–3 |
| 2.25 | Sealed index cards | Apex envelopes | 10 (2 operatives × 5 factions) | Prepare at setup | 05 | ⬜ | $1–3 |
| 2.26 | Pre-printed forms | Chronicle forms | 30 sheets (8 per session — 1 per Quarter) | Print | 07 | ⬜ | $2–5 |
| 2.27 | Adhesive notes | Intel note age tracker | 1 pad | Purchase | 02b | ⬜ | $1–2 |
| 2.28 | Countdown device | Timer | 1 | Sand timer or phone | 03 | ⬜ | $3–10 |
| 2.29 | Writing tools | — | Set | Purchase | — | ⬜ | $5–10 |
| 2.30 | Laminated cards | Player quick reference cards | 1 per player | Print + laminate | V12–V18 | ⬜ | $3–7 |
| 2.31 | Laminated or printed grid mat | Resolution Grid | 1 — Beat 0 staging surface; 5 lanes (case receipt order) × rows for Beat 2 cards and paired Beat 3 card/target rows (up to 4 pairs for Ghost). Full spec: Artifact 07; visual design: Artifact 11. See PM05 XA-22. | Print + laminate | 07, 11 | ⬜ | $2–5 |
| 2.32 | Physically distinct tokens — by size, color, or numeral | Modifier tokens | Per session — known values: +50 (partial payment penalty, Beat 0); −15 (Type B Countermeasure, Beat 2). Full set TBD pending card system completion. Stored in ARBITER modifier area between use; must remain legible in card-stack cascade. See PM05 04-15. | Purchase or print | 07, 09 | ⬜ | $3–8 |
| 2.33 | Double-sided chips or printed cards | Status markers | 1 per faction × 5 — two sides: Discussing (yellow) / Ready. Faction Players flip at Phase 1 start and end. Full definition pending: PM05 XA-07. | Print + cut or purchase | 03, 07 | ⬜ | $3–7 |
| 2.34 | Small printed cards | Personal Tiebreaker cards | TBD set — ARBITER-held; drawn when initiative tiebreaker result 9 fires (Artifact 03 §7 Phase 1). Definition and quantity pending: PM05 XA-09. | Print + cut | 03, 07 | ⬜ | $1–3 |
| 2.35 | Blank card stock or pre-printed slips | Target slips | Per session — used in dispatch cases (covert operations) and on political act declarations. Suggest 10 per faction per session. | Print + cut or purchase | 03, 06 | ⬜ | $1–3 |
| 2.36 | Pre-printed cards | Operation Resolution cards | 4 types: Succeeded / Failed / Blocked / Discovered — quantity per 09 spec. ARBITER places one in each faction's dispatch case at Beat 3/4 resolution; Faction Players read privately at Beat 5. | Print + cut | 03, 07, 09 | ⬜ | $2–5 |
| 2.37 | Pre-printed slips — ARBITER-keyed format | ARBITER notification slips | Per session — ARBITER-to-faction private communications. Must be physically distinguishable from faction-authored messages to prevent forgery. See Artifact 06 §8. | Print | 06, 07 | ⬜ | $1–3 |
| 2.38 | Blank slips or index cards | Faction message slips | Per session — faction-to-faction written messages; used during Phase 2 (Placement) and Phase 4 (Declaration). See Artifact 06 §7. | Purchase (index cards) or print | 06 | ⬜ | $1–2 |
| 2.39 | Laminated strip with position markers | Initiative Strip | 1 — ARBITER updates at end of Phase 1 each Quarter; shows current faction initiative order on The Overview. Requires faction-colored position markers or pegs. | Print + laminate; faction markers from 2.08 | 03, 11 | ⬜ | $1–3 |
| 2.40 | Printed card | Floor Act card | 1 per faction × 5 (or 1 universal — TBD) — always available beside tableau, not part of deck. Full design pending: PM02 D04-13. | Print + cut | 04 D04-13 | ⬜ | $1–3 |
| **Total** | | | | | | | **$115–270** |

### WBS 3 — Playtest Infrastructure

| # | Deliverable | Requires | Status |
|---|-------------|---------|--------|
| 3.01 | Session feedback form | PM02 validation targets | ⬜ |
| 3.02 | Phase timing sheet | 03 | ⬜ |
| 3.03 | Post-session debrief script | 10 | ⬜ |
| 3.04 | Session 1 simplified configuration guide | 09, 10 | ⬜ |
| 3.05 | Getting Started walkthrough | All design artifacts | ⬜ |

---

## 8. Open Decisions Requiring Sign-Off

See PM02 for full decision detail and canonical decision IDs. Items currently blocking WBS 1 completion are listed below using PM02's per-artifact ID format. Decisions for signed-off artifacts (00–03) are locked — see PM02 Section 1 for the record.

| PM02 ID | Decision | Blocking Artifact |
|---------|---------|------------------|
| D04-01 | Faction-specific political acts — The Guild, The Syndicate, The Directorate, The Network | 04 |
| D04-02 | Faction-specific covert operations — The Guild, The Syndicate, The Directorate, The Network | 04 |
| D06-01 | Dispatch case physical format | 06 |
| D06-02 | Dispatch case submission protocol | 06 |
| D07-01 | ARBITER Resolution — track only vs. spendable resource | 07 |
| D05-01 | Board Strength thresholds by player count | 05 |
| D05-02 | Apex Emergency Response timing | 05 |

---

## 9. Project File Structure & Version Control

### File Structure

Root: `~/Projects/TheSignal/`

| Folder / File | Purpose |
|---------------|---------|
| `V1/` | Active design tier — Tier 1 Paper Prototype. All artifact editing happens here. "V1" is the tier designation (Tier 1 = physical tier); does not need renaming as the project evolves. |
| `Session/` | Session management files — save state and private design axioms. Not part of the artifact set; not referenced by any artifact. |
| `Creative/` | World-building creative content — characters, vignettes, stories, and quotes generated as potential source material for Artifact 00 and flavor copy. See `Creative/README.md` for submission index and evaluation status. Brief for writers/AI agents: `Creative/CREATIVE_BRIEF.md`. |
| `Retired/` | Read-only archive of superseded design generations. `Retired/Electronic/` — original electronic brainstorming suite (pre-code, old faction names). `Retired/Paper/` — 1st generation paper prototype artifacts. See PM03 §6 for file-level index. |
| `README.md` | Project overview and folder navigation guide for new sessions or collaborators. |
| `.gitignore` | Excludes zip archives, credentials files (`*.env`), and system files from version control. |

Files outside the git repo (at `~/Projects/` level):

| File | Purpose |
|------|---------|
| `credentials.env` | GitHub PAT and other project credentials. Never committed to any repository. |

### Version Control

The project uses git. Remote: `https://github.com/andrew-bosch/TheSignal` (private repository). Initialized session 10.

**Session commit convention:**

```
git add -A && git commit -m "session N — [primary decision or milestone]" && git push
```

Commit at the close of each design session. The commit message states the session's headline decision or milestone. Full decision rationale lives in PM02 — the commit is the pointer, not the record.

---

## 10. Playtest Readiness Checklist

Binary go/no-go. Before any playtest session is scheduled, every item in the relevant categories must be ✅. Items can be waived for a simplified Session 1 configuration — note the waiver explicitly.

### Category 1: Design Artifact Readiness

| # | Item | S1 Required | Status |
|---|------|-------------|--------|
| 1.01 | Artifact 00 — Factions & World — signed off | Yes | ✅ |
| 1.02 | Artifact 01 — Game Board — signed off | Yes | ✅ |
| 1.03 | Artifact 02a — Resource Systems: Board State — signed off | Yes | ✅ |
| 1.04 | Artifact 02b — Resource Systems: Tracking — signed off | Yes | ✅ |
| 1.05 | Artifact 03 — Round Structure — signed off | Yes | ✅ |
| 1.06 | Artifact 04 — Action Card System — sufficient card set complete (S1 waiver: Common set only acceptable) | Yes (waivable) | ⬜ |
| 1.07 | Artifact 05 — Operative & Apex System — Tier 1 operatives complete (Apex and higher tiers may be deferred) | S1 waivable | ⬜ |
| 1.08 | Artifact 07 — ARBITER Toolkit — Resolution procedure complete and ARBITER guide readable | Yes | ⬜ |
| 1.09 | Artifact 10 — Game Manuals — ARBITER guide and player guide sufficient for in-session reference | Yes | ⬜ |
| 1.10 | PM05 punch list READY NOW items — no unresolved high-priority blocking items open | Yes | ⬜ |

### Category 2: Physical Components

| # | Item | S1 Required | Status |
|---|------|-------------|--------|
| 2.01 | Printed board (New Meridian hex map, A1 or A0) | Yes | ⬜ |
| 2.02 | Presence tokens — at least 10 per faction × 5 factions (15 target) | Yes | ⬜ |
| 2.03 | Operational markers — 2 per faction × 5 factions | Yes | ⬜ |
| 2.04 | Structure tokens — at least 4 per faction × 5 factions (6 target) | Yes | ⬜ |
| 2.05 | Resource chips — faction-specific, at least 20 per type (30 target) | Yes | ⬜ |
| 2.06 | Dispatch cases — 1 per player × 6 (including ARBITER) | Yes | ⬜ |
| 2.07 | Public Standing tracks — 1 per faction × 5 | Yes | ⬜ |
| 2.08 | World Condition track — 1 | Yes | ⬜ |
| 2.09 | Chorus Portrait board — 1, dry-erase or record-able | Yes | ⬜ |
| 2.10 | 2 × d10 dice | Yes | ⬜ |
| 2.11 | Timer (sand timer, phone, or dedicated countdown device) | Yes | ⬜ |
| 2.12 | Covert operation cards — at least Common set C01–C15 per faction | Yes (waivable: Common only) | ⬜ |
| 2.13 | Political act cards — at least P01–P10 common political acts | Yes (waivable: simplified set) | ⬜ |
| 2.14 | Pass cards — 4 per faction × 5 | Yes | ⬜ |
| 2.15 | Accord forms — minimum 8 | Yes | ⬜ |
| 2.16 | Writing tools and writing surface at ARBITER station | Yes | ⬜ |

### Category 3: ARBITER Preparation

| # | Item | Status |
|---|------|--------|
| 3.01 | ARBITER player has read Artifact 07 in full at least once | ⬜ |
| 3.02 | ARBITER player has read Artifact 03 (round structure) in full | ⬜ |
| 3.03 | ARBITER player has run one dry-run of Resolution solo (Beat 3 and Beat 4) | ⬜ |
| 3.04 | ARBITER player knows all four registers by name and can describe when each applies | ⬜ |
| 3.05 | Translation rate table memorized or printed — Contested = 5:1, no presence = 4:1, Present = 3:1, Established = 2:1 (see 02a §8) | ⬜ |
| 3.06 | ARBITER player has read PRIVATE___True_State.md (private design axioms) | ⬜ |

### Category 4: Logistics

| # | Item | Status |
|---|------|--------|
| 4.01 | Table space sufficient for The Overview plus 6 player stations | ⬜ |
| 4.02 | Session duration blocked: 90–150 min play + 30 min setup/teardown | ⬜ |
| 4.03 | Session Record sheet prepared (PM05 §3 format) | ⬜ |
| 4.04 | Dedicated observer confirmed, or recording assignment distributed among players | ⬜ |

---

## 11. Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|-----------|--------|------------|
| R01 | Core loop is not engaging — factions lack interesting decisions each quarter | Medium | Critical | Early S1 test with experienced game players; post-session question on decision quality. Design fallback: expand Floor Act and Accord system if board play feels thin. |
| R02 | ARBITER cognitive load too high — The ARBITER player cannot run Resolution + Chronicle + Portrait + notifications simultaneously at full table | Medium | High | Run ARBITER dry-session before S1. Simplify S1 by deferring Chronicle; focus on Resolution. ARBITER script pack (Artifact 07) reduces improvisation load. |
| R03 | Ghost asymmetry unbalancing — Ghost's 4-operation rule produces outsized covert output | Medium | Medium | Track V02 in S1. Playtest variable PT-04-03. Design fallback: reduce Ghost to 3 operations if 4 proves dominant by Quarter 5. |
| R04 | Physical production cost exceeds budget | Low | Medium | See WBS 2 cost estimates (§7 above) — total ~$100–230. Early sourcing of poker chips and print services gives accurate cost before committing. |
| R05 | Incomplete card set blocks S1 — political acts or faction-specific cards not ready | High (current) | High | S1 may proceed with Common card set only (C01–C15) and simplified political acts (P01–P10). Accepted S1 scope reduction — note in session records. |
| R06 | Player count limitation — unable to assemble 5 faction players + ARBITER for first session | Medium | Low | Recommended S1 configuration is 3 faction players + ARBITER (PM01 §2). 3-player configuration is validated by design. |
| R07 | Chorus Portrait system doesn't produce meaningful Chronicle moments | Low | High | V12, V13, V14 track this. Monitor Portrait scoring calibration (PT-02-03). Design fallback: increase Portrait deltas (+3/+2/0/−2/−3) if Chronicle feels disconnected from table behavior. |
| R08 | Rulebook insufficient — ARBITER cannot facilitate without frequent rule lookups | High (current) | Medium | Artifact 10 is incomplete. S1 mitigation: designer in the room as rules consultant. Hard requirement: ARBITER guide must support solo operation before S2. |

---

## 12. Go/No-Go Framework for V2 (Electronic Development)

Criteria that must be met before paper prototype development concludes and electronic development begins. This is not a session-level evaluation — it applies to the paper prototype program as a whole after the structured playtest series completes.

### Mandatory — all must be met before Go

| # | Criterion | Notes |
|---|-----------|-------|
| G01 | All design artifacts (00–10) signed off | Not blocking V2 planning, but must be met before V2 development budget commitment |
| G02 | At least 3 playtest sessions completed with structured feedback recorded (PM05 §3 format) | Minimum data set for Go/No-Go evaluation |
| G03 | S1 (session runs in 90–150 min) met in ≥ 2 of 3 sessions | Core session length validated |
| G04 | S2 (ARBITER facilitates without rules reference during resolution) met in ≥ 2 of 3 sessions | ARBITER cognitive load is manageable |
| G05 | S4 (players want to play Session 2 before leaving) met in ≥ 2 of 3 sessions | Core engagement signal |
| G06 | No critical loop failures: V03 (Incursion), V04 (Accords), V07 (Public Standing), V08 (Chorus Node) — at least 3 of 4 targets met across the session series | Core mechanics are working |
| G07 | Faction asymmetry validated: at least 4 of 5 factions played; at least 2 clearly different strategies observed | Five-faction design is differentiated |

### Supporting — strong evidence expected, not blocking

| # | Criterion | Notes |
|---|-----------|-------|
| G08 | S6 (Chronicle resonates at session end) met in ≥ 2 sessions | Narrative system is functional |
| G09 | V12 (Portrait affects final ranking) observed in ≥ 1 session | Dual-track victory system is meaningful |
| G10 | PC-03 (ARBITER role desirable) met — ≥ 50% of players who ran ARBITER would do so again | ARBITER experience is sustainable |
| G11 | No single faction wins more than 2 of 3 sessions with the same strategy | Faction balance is sufficient for first pass |

### Decision owner

Andy — this is a product and project decision, not a design decision. Can be made with designer confidence that the core is validated, regardless of remaining polish items.

**What Go/No-Go is not:** a determination that the paper prototype is "finished." Paper prototype refinement continues in parallel with electronic development. Go/No-Go is a commitment to invest in the next tier, not a declaration that Tier 1 is complete. The criteria above define the minimum bar for confidence, not the maximum level of polish.
