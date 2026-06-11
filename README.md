# THE SIGNAL

**[→ Project Homepage](https://andrew-bosch.github.io/TheSignal/)**

A legacy negotiation and area-control tabletop game for 2–6 players (up to 5 faction players + 1 ARBITER). Factions negotiate humanity's response to a transmission called The Chorus. Set in New Meridian, 2041.

---

## Project Status

**Current phase:** L1 — Paper Prototype (physical-only, no electronics)  
**Active design layer:** `/V1`  
**Design milestone:** Art 03 v2.1 signed off S52. Art 04 in progress — C01–C15 signed off; P01–P18 in development.

---

## Design Artifacts

*Authoritative sign-off status: [PM03 — Master Artifact Index](V1/PM03___Master_Artifact_Index.md)*

*Sections correspond to program architecture. Artifacts are source code. The DB is the runtime representation. Physical components are I/O. ARBITER is the interpreter.*

---

### Governing Constraints

*Narrative is the primary design constraint — not a category alongside constraints but the governing law of the design. All mechanical decisions require a narrative anchor. Design Pillar 6: when narrative and mechanical reasoning conflict, narrative prevails. Read before any other artifact.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 00 | [Factions, World & Narrative Context](V1/00___Factions_World_Narrative_Context.md) | 1.5 | ✅ Signed off — S40 |
| 00a | [Governing Rules & Design Policy](V1/00a___Governing_Rules___Design_Policy.md) | 0.8 | ✅ Signed off — S83 |

---

### Logical Data Model

*00b tracks DB migration status — what remains to be modeled for deep analysis and balance work. 00c defines resource types and economic parameters; starting values are seeded by 03-init at game start. Authoritative entity schemas in `Database/schema_reference.md`.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 00b | [Analysis Readiness](V1/00b___Analysis_Readiness.md) | 0.3 | ✅ Signed off — S83 |
| 00c | [Economy Manifest](V1/00c___Economy_Manifest.md) | 0.4 | 🔄 In progress |

---

### Imports — Game Objects

*Zone and component registries. Implement the logical data model specified in 00b/00c. No execution logic — define what exists and its properties.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 01 | [Zones: Physical & Virtual Geography](V1/01___Game_Board_New_Meridian.md) | 1.9 | ✅ Signed off — S44 |
| 02a | [Components: Board State](V1/02a___Resource_Systems_Board_State.md) | 1.6 | ✅ Signed off — S42 |
| 02b | [Components: Tracking](V1/02b___Resource_Systems_Tracking.md) | 1.5 | ✅ Signed off |

---

### Main()

*Game entry point and main execution loop. 03-init owns initialization; 03 owns the session while-loop; 03a specifies the execution engine.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 03-init | [Game Initialization](V1/03-init___Game_Initialization.md) | 0.1 | ⬜ Stub — content currently distributed across 00c, 02a, 02b |
| 03 | [while session(true): Round Structure](V1/03___Round_Structure___Gameplay.md) | 2.1 | ✅ Signed off — S52 |
| 03a | [Game Engine Specification](V1/03a___Game_Engine_Specification.md) | 0.98 | 🔄 In progress |

---

### Stored Procedures

*Callable modules dispatched by Main() or its core subroutines. 04b is design analysis proving the Art 04 card metadata schema — companion document, not callable.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 04 | [Card Set: Action Subroutines](V1/04___Card_System.md) | 0.9.21 | 🔄 C01–C15 ✅; P01–P18 in progress |
| 04b | [Action Taxonomy](V1/04b___Action_Taxonomy_Design_Analysis.md) | 1.5 | ✅ S48 — design analysis companion to 04 |
| 05 | [Operative & Apex Subroutines](V1/05___Operative_Apex_System.md) | 0.1 | ⬜ Placeholder |
| 06 | [Messaging System](V1/06___Messaging_System.md) | 0.2 | 🟡 In Progress — §9 Accord governance signed off |
| 07 | [ARBITER Subroutines](V1/07___ARBITER_Toolkit.md) | 0.1 | ⬜ Placeholder |
| 08 | [Faction Player Subroutines](V1/08___Player_Toolkit.md) | 0.1 | ⬜ Placeholder |
| 10a | [Victory: Game Exit](V1/10a___Victory_System.md) | 0.1 | ⬜ Placeholder |

---

### Documentation

*Human-readable player and production artifacts. The playable, printable, and visual layer built from the source artifacts above.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 09 | [Card Production Specification](V1/09___Card_Production_Spec.md) | 0.1 | ⬜ Placeholder |
| 10 | [Game Manuals](V1/10___Game_Manuals.md) | 0.1 | ⬜ Placeholder |
| 11 | [Visual Design System](V1/11___Visual_Design_System.md) | 0.1 | ⬜ Placeholder |

---

## Project Management

| Doc | Purpose |
|-----|---------|
| [PM01 — Project Charter & Work Breakdown](V1/PM01___Project_Charter___Work_Breakdown.md) | Charter, WBS, Playtest Readiness Checklist, Risk Register |
| [PM02 — Decision Log & Validation Tracker](V1/PM02___Decision_Log___Validation_Tracker.md) | Locked decisions L01–L171, open decisions, change log |
| [PM03 — Master Artifact Index](V1/PM03___Master_Artifact_Index.md) | Sign-off registry, dependency map — authoritative artifact status |
| [PM04 — Glossary & Data Dictionary](V1/PM04___Glossary___Data_Dictionary.md) | In-world terms (§1), design terminology conventions (§2) |
| [PM05 — Active Punch List](V1/PM05___Active_Punch_List.md) | Live work items, validation dashboard, playtest data |

---

## Session

| File | Purpose |
|------|---------|
| [Project Save State](Session/THE_SIGNAL___Project_Save_State.md) | Authoritative session state — read this to resume after any break |

*`PRIVATE___True_State.md` is not in this repository.*

---

## Folder Structure

```
TheSignal/
├── V1/           ← Active design documents — work happens here
├── Session/      ← Session management files (save state, private design axioms)
├── Creative/     ← World-building source material (vignettes, characters, creative brief)
├── ClaudeIOS/    ← Summaries from mobile creative sessions; processed into V1
├── Retired/      ← Superseded document generations, read-only
│   ├── Electronic/   ← Original electronic brainstorming suite (pre-paper prototype)
│   └── Paper/        ← 1st generation paper prototype artifacts (pre-V1 baseline)
└── README.md     ← This file
```

**The "V1" designation** refers to Layer 1 of the design — the paper prototype physical layer. When the electronic version begins, that will be V2 (L2). V1 does not need renaming as the project evolves.

**Design governance:** PM01 (charter), PM02 (decision log), PM03 (artifact index), PM04 (glossary), PM05 (punch list)

---

## Design Conventions

- **Narrative as constraint:** Every mechanical decision requires a narrative anchor. Art 00 is the governing source. When narrative and mechanical reasoning conflict, narrative prevails. See Design Pillar 6.
- **In-world language:** All mechanical terms have canonical in-world equivalents (Districts not Hexes, Presence tokens not Influence tokens, etc.). PM04 §1 is the authority.
- **Terminology sequencing:** No term appears in an artifact before its narrative grounding is established. Art 00 is always read first.
- **Change governance:** Material changes require re-sign-off. Non-material changes (style, terminology, clarification) do not. See PM05 for all pending changes.
- **Vocabulary:** ARBITER, Faction, The ARBITER Player, Faction Player — four distinct terms used precisely. See PM02 L88.

---

## Version Control

This repository uses git. Commit at the close of each design session with a message describing what was decided or completed.

```
session N — [primary decision or milestone]
```

The `/Retired` folder is tracked in git for historical reference but should not be edited. The `/Session` folder is tracked; `PRIVATE___True_State.md` should remain in `.gitignore` if distributed to collaborators.
