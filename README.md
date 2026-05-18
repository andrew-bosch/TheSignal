# THE SIGNAL

**[→ Project Homepage](https://andrew-bosch.github.io/TheSignal/)**

A legacy tabletop board game for 5 players + ARBITER. Factions negotiate humanity's response to a transmission called The Chorus. Set in New Meridian, 2041.

---

## Quick Navigation

**[→ Full Artifact Index with status](V1/README.md)**

### Design Artifacts

- [00 — Factions, World & Narrative Context](V1/00___Factions_World_Narrative_Context.md)
- [00a — Governing Rules & Design Policy](V1/00a___Governing_Rules___Design_Policy.md)
- [01 — Game Board: New Meridian](V1/01___Game_Board_New_Meridian.md)
- [02a — Resource Systems: Board State](V1/02a___Resource_Systems_Board_State.md)
- [02b — Resource Systems: Tracking](V1/02b___Resource_Systems_Tracking.md)
- [03 — Round Structure & Gameplay](V1/03___Round_Structure___Gameplay.md)
- [04 — Action Card System](V1/04___Action_Card_System.md)
- [04b — Action Taxonomy & Design Analysis](V1/04b___Action_Taxonomy_Design_Analysis.md)
- [05 — Operative & Apex System](V1/05___Operative_Apex_System.md)
- [06 — Messaging System](V1/06___Messaging_System.md)
- [07 — ARBITER Toolkit](V1/07___ARBITER_Toolkit.md)
- [08 — Player Toolkit](V1/08___Player_Toolkit.md)
- [09 — Card Specifications](V1/09___Card_Specifications.md)
- [10 — Game Manuals](V1/10___Game_Manuals.md)
- [10a — Victory System](V1/10a___Victory_System.md)
- [11 — Visual Design System](V1/11___Visual_Design_System.md)

### Project Management

- [PM01 — Project Charter & Work Breakdown](V1/PM01___Project_Charter___Work_Breakdown.md)
- [PM02 — Decision Log & Validation Tracker](V1/PM02___Decision_Log___Validation_Tracker.md)
- [PM03 — Master Artifact Index](V1/PM03___Master_Artifact_Index.md)
- [PM04 — Glossary & Data Dictionary](V1/PM04___Glossary___Data_Dictionary.md)
- [PM05 — Active Punch List](V1/PM05___Active_Punch_List.md)

### Session

- [Project Save State](Session/THE_SIGNAL___Project_Save_State.md)

---

## Project Status

**Current phase:** L1 — Paper Prototype (physical-only, no electronics)
**Active design layer:** `/V1`
**Design milestone:** Artifact 03 sign-off in progress — §§13–16 pending; Phase 6 Beats 0–5 signed off (session 19)

---

## Folder Structure

```
TheSignal/
├── V1/           ← Active design documents — work happens here
├── Session/      ← Session management files (save state, private design axioms)
├── Retired/      ← Superseded document generations, read-only
│   ├── Electronic/   ← Original electronic brainstorming suite (pre-paper prototype)
│   └── Paper/        ← 1st generation paper prototype artifacts (pre-V1 baseline)
└── README.md     ← This file
```

### /V1 — Active Design Layer

The complete L1 paper prototype design suite. All active artifact editing happens here. Start with `/V1/README.md` for a navigation index, or `/V1/PM03___Master_Artifact_Index.md` for the full artifact registry with status.

**Artifact reading order:** 00 → 00a → 01 → 02a → 02b → 03 → 04 → 04b → 05 → 06 → 07 → 08 → 09 → 10 → 10a → 11

**Design governance:** PM01 (charter), PM02 (decision log + punch list), PM03 (artifact index), PM04 (glossary)

The "V1" designation refers to Layer 1 of the design — the paper prototype physical layer. When the electronic version begins, that will be V2 (L2). V1 does not need renaming as the project evolves.

### /Session

Files that govern the working design session but are not part of the artifact set:

- `THE_SIGNAL___Project_Save_State.md` — tracks where each session ended, what's in progress, recommended next steps. Read this to resume after any break.
- `PRIVATE___True_State.md` — design axioms and private worldbuilding known only to the designer. Not for distribution.

### /Retired

Two generations of pre-V1 design documents. Read-only reference — content has been redistributed into the V1 artifact set. See PM03 §6 for a full file-level index.

- `Electronic/` — Original electronic brainstorming suite (20 documents). Uses old faction names (Architect, Warden, Signal). Includes TypeScript schemas, hardware specs, network architecture.
- `Paper/` — 1st generation paper prototype artifacts. Early versions of V1 documents under current naming conventions.
- `backup.zip` — Complete archive of the Retired folder prior to reorganization.

---

## Design Conventions

- **In-world language:** All mechanical terms have canonical in-world equivalents (Districts not Hexes, Presence tokens not Influence tokens, etc.). PM03 §1 is the authority.
- **Terminology sequencing:** No term appears in an artifact before its narrative grounding is established. Artifact 00 is always read first.
- **Change governance:** Material changes require re-sign-off. Non-material changes (style, terminology, clarification) do not. See PM02 §2b punch list for all pending changes.
- **Vocabulary:** ARBITER, Faction, The ARBITER Player, Faction Player — four distinct terms used precisely. See PM02 L88.

---

## Version Control

This repository uses git. Commit at the close of each design session with a message describing what was decided or completed.

Suggested commit convention:
```
session N — [primary decision or milestone]

e.g. "session 10 — L88 four-term convention; 03 phases 2-6 conventions applied"
```

The `/Retired` folder is tracked in git for historical reference but should not be edited. The `/Session` folder is tracked; `PRIVATE___True_State.md` should remain in `.gitignore` if distributed to collaborators.
