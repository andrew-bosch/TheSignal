# THE SIGNAL

**[→ Project Homepage](https://andrew-bosch.github.io/TheSignal/)**

A legacy negotiation and area-control tabletop game for 2–6 players (up to 5 faction players + 1 ARBITER). Factions negotiate humanity's response to a transmission called The Chorus. Set in New Meridian, 2041.

---

## Project Status

**Current phase:** L1 — Paper Prototype (physical-only, no electronics)  
**Active design layer:** `/V1`  
**Design milestone:** Artifact 03 signed off v1.7 (session 20) — Artifact 04 in progress (C01–C15 signed off; C16–C35 and political acts pending)

---

## Design Artifacts

*Authoritative sign-off status: [PM03 — Master Artifact Index](V1/PM03___Master_Artifact_Index.md)*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 00 | [Factions, World & Narrative Context](V1/00___Factions_World_Narrative_Context.md) | 1.3 | ✅ Signed off |
| 00a | [Governing Rules & Design Policy](V1/00a___Governing_Rules___Design_Policy.md) | 0.2 | ✅ Signed off — session 7 |
| 00b | [Data Architecture](V1/00b___Data_Architecture.md) | 0.1 | ✅ Reference Document — Active |
| 01 | [Game Board: New Meridian](V1/01___Game_Board_New_Meridian.md) | 1.2 | ✅ Signed off |
| 02a | [Resource Systems: Board State](V1/02a___Resource_Systems_Board_State.md) | 1.4 | 🔄 Re-sign-off pending (session 14 material change) |
| 02b | [Resource Systems: Tracking](V1/02b___Resource_Systems_Tracking.md) | 1.5 | ✅ Signed off |
| 03 | [Round Structure & Gameplay](V1/03___Round_Structure___Gameplay.md) | 1.7 | ✅ Signed off — session 20 |
| 03a | [Game Engine Specification](V1/03a___Game_Engine_Specification.md) | 0.97 | 🔄 In Progress — Layers 1–3 drafted |
| 04 | [Action Card System](V1/04___Action_Card_System.md) | 0.9.6 | 🔄 In progress — C01–C15 signed off; C16–C35 and political acts pending |
| 04b | [Action Taxonomy & Design Analysis](V1/04b___Action_Taxonomy_Design_Analysis.md) | 1.1 | ✅ Reference Document — Active |
| 05 | [Operative & Apex System](V1/05___Operative_Apex_System.md) | 0.1 | 🔄 Draft placeholder |
| 06 | [Messaging System](V1/06___Messaging_System.md) | 0.1 | 🔄 Draft placeholder |
| 07 | [ARBITER Toolkit](V1/07___ARBITER_Toolkit.md) | 0.1 | 🔄 Draft placeholder |
| 08 | [Player Toolkit](V1/08___Player_Toolkit.md) | 0.1 | 🔄 Draft placeholder |
| 09 | [Card Specifications](V1/09___Card_Specifications.md) | 0.1 | 🔄 Draft placeholder |
| 10 | [Game Manuals](V1/10___Game_Manuals.md) | 0.1 | 🔄 Draft placeholder |
| 10a | [Victory System](V1/10a___Victory_System.md) | 0.1 | 🔄 Draft placeholder |
| 11 | [Visual Design System](V1/11___Visual_Design_System.md) | 0.1 | ⬜ Placeholder |

**Artifact reading order:** 00 → 00a → 01 → 02a → 02b → 03 → 04 → 04b → 05 → 06 → 07 → 08 → 09 → 10 → 10a → 11

---

## Project Management

| Doc | Purpose |
|-----|---------|
| [PM01 — Project Charter & Work Breakdown](V1/PM01___Project_Charter___Work_Breakdown.md) | Charter, WBS (40+ components), Playtest Readiness Checklist, Risk Register |
| [PM02 — Decision Log & Validation Tracker](V1/PM02___Decision_Log___Validation_Tracker.md) | Locked decisions L01–L114, open decisions, change log |
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

- **In-world language:** All mechanical terms have canonical in-world equivalents (Districts not Hexes, Presence tokens not Influence tokens, etc.). PM04 §1 is the authority.
- **Terminology sequencing:** No term appears in an artifact before its narrative grounding is established. Artifact 00 is always read first.
- **Change governance:** Material changes require re-sign-off. Non-material changes (style, terminology, clarification) do not. See PM05 for all pending changes.
- **Vocabulary:** ARBITER, Faction, The ARBITER Player, Faction Player — four distinct terms used precisely. See PM02 L88.

---

## Version Control

This repository uses git. Commit at the close of each design session with a message describing what was decided or completed.

Suggested commit convention:
```
session N — [primary decision or milestone]

e.g. "session 22 — 03a Layer 3 complete; L114 Layer terminology locked"
```

The `/Retired` folder is tracked in git for historical reference but should not be edited. The `/Session` folder is tracked; `PRIVATE___True_State.md` should remain in `.gitignore` if distributed to collaborators.
