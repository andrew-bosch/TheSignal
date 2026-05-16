# THE SIGNAL P1 — Master Artifact Index
## Paper Prototype — L1 Physical Layer

**Version:** 1.1 Signed Off  
**Scope:** L1 Physical Layer Paper Prototype only  
**Sign-off Status:** Artifacts 00, 01, 02a, 02b, 03, PM01, PM02 — Signed Off

---

## Narrative Language Convention

All documentation uses in-world narrative terms. Each mechanical term is defined once on first use, then the narrative term is used exclusively throughout all artifacts.

| Mechanical Term | In-World Term | First Defined In |
|----------------|---------------|-----------------|
| Hex / board space | District | 01 — Game Board |
| Game board / mat | New Meridian | 01 — Game Board |
| Influence token | Presence token | 02 — Resource Systems |
| Claim marker | Operational marker | 01 — Game Board |
| Recipe box | Dispatch case | 06 — Messaging System |
| Resource token | Asset token | 02 — Resource Systems |
| Popularity track | Public Standing track | 02 — Resource Systems |
| Portrait score | Chorus Portrait | 02 — Resource Systems |
| Proof token | Intelligence token | 02b — Resource Systems: Tracking |
| Modifier card | Operational intelligence card | 04 — Action Card System |
| Counter card | Countermeasure card | 04 — Action Card System |
| Private action | Covert operation | 04 — Action Card System |
| Public action | Political act | 04 — Action Card System |
| Hidden objective | Classified directive | 05 — Operative System |
| Operative card | Field operative dossier | 05 — Operative System |
| World event card | Situation report | 01 — Game Board |

*ARBITER and The Table are never renamed — they are already in-world terms.*

---

## Design Artifact Registry

### Core Rules Artifacts

| ID | Title | Status | Summary |
|----|-------|--------|---------|
| 00 | Factions & World | ✅ Signed Off | Factions, world, narrative context, ARBITER nature, timescale perspectives |
| 01 | Game Board — New Meridian | ✅ Signed Off | District layout, rings, Chorus Node, track positions, starting configuration |
| 02a | Resource Systems: Board State | ✅ Signed Off | Presence, influence, structures, resource generation — all publicly visible board state |
| 02b | Resource Systems: Tracking | ✅ Signed Off | Chorus Portrait, Public Standing, Intel Notes — tracking systems alongside the board |
| 03 | Round Structure & Gameplay | ✅ Signed Off | Six phases, timing, initiative, ARBITER conversion, Apex trigger |
| 04 | Action Card System | 🔄 Draft | Covert operations, political acts, faction-specific actions for all factions, Pass cards |
| 05 | Operative & Apex System | 🔄 Draft | All operatives, tier progression, cooldowns, Apex costs and sealed powers, Founding Figures |
| 06 | Messaging System | ⬜ Not Started | Dispatch case protocol, ARBITER communications, private notifications, Accord forms |
| 07 | ARBITER Toolkit | 🔄 Draft | Portrait board, Debrief reward system, resolution beats, narrative registers, Chronicle |
| 08 | Player Toolkit | 🔄 Draft | Player components, faction reference, starting assets, classified directives |

### Reference Artifacts

| ID | Title | Status | Summary |
|----|-------|--------|---------|
| 09 | Card Specifications | ⬜ Not Started | Complete card content in table format — all operations, intelligence cards, events, countermeasures |
| 10 | Game Manuals | 🔄 Draft | Player guide, ARBITER guide, setup guide, components list with shopping list |
| 11 | Visual Design System | ⬜ Not Started | Color palette, typography, faction identity system, component visual standards |

### Visual Artifacts (Interactive HTML)

| ID | Title | Status |
|----|-------|--------|
| V01 | Game Mat / Table Layout | 🔄 Draft |
| V02 | Public Standing Track | ⬜ Not Started |
| V03 | Round Phase Slider | ⬜ Not Started |
| V04 | World Condition Tracks | 🔄 Draft |
| V05 | Situation Report (World Event) Layout | 🔄 Draft |
| V06 | Accord Document Layout | ⬜ Not Started |
| V07 | Card Layouts — all types | 🔄 Draft |
| V08 | District Hex Layout | ⬜ Not Started |
| V09 | Player Tools Visual Layouts | ⬜ Not Started |
| V10 | ARBITER Tools Visual Layouts | ⬜ Not Started |
| V11 | Dispatch Case / Messaging Layout | ⬜ Not Started |
| V12 | Quick Reference — Round Phases | ⬜ Not Started |
| V13 | Quick Reference — Card Types | ⬜ Not Started |
| V14 | Quick Reference — Difficulty | ⬜ Not Started |
| V15 | Quick Reference — Covert Operations | ⬜ Not Started |
| V16 | Quick Reference — Political Acts | ⬜ Not Started |
| V17 | Quick Reference — Intelligence Tokens | ⬜ Not Started |
| V18 | Quick Reference — Public Standing | ⬜ Not Started |
| V19 | Intelligence Token Layout | ⬜ Not Started |

### Project Management Artifacts

| ID | Title | Status |
|----|-------|--------|
| PM01 | Project Charter & Work Breakdown | ✅ Signed Off |
| PM02 | Decision Log & Validation Tracker | ✅ Signed Off |
| PM03 | Future Phases — Parking Lot | ⬜ Not Started |

---

## Standard Artifact Template

Every text-based design artifact (IDs 01–11) follows this structure. Section names are fixed — do not rename them.

```
# [ID] — [TITLE]
## THE SIGNAL P1 — Paper Prototype

Version | Status | Last Updated | Supersedes

---

1. Overview
2. Index
3. Game Purpose
4. Narrative Function
5. Design Principles
6. Rules & Constraints
7. Component Description
8. Special Conditions & Gameplay Impacts
9. Examples & Exceptions
```

---

## Retired Artifacts

The following artifacts from the working design phase are superseded by the v1.0 baseline set. They should not be edited further. Content has been redistributed into the numbered artifact set above.

| Former Artifact | Content Moved To |
|----------------|-----------------|
| game_overview | 10 — Game Manuals |
| components | 10 — Game Manuals |
| round_structure | 03 — Round Structure |
| hidden_objectives | 02 — Resource Systems, 05 — Operative System |
| card_designs | 09 — Card Specifications |
| arbiter_guide | 07 — ARBITER Toolkit, 10 — Game Manuals |
| player_guide | 08 — Player Toolkit, 10 — Game Manuals |
| reference_sheets | V12–V18 Visual Quick References |
| setup_guide | 10 — Game Manuals |
| event_card_system | 01 — Game Board, 09 — Card Specifications |
| l1_generation | 02 — Resource Systems |
| action_redesign | 04 — Action Card System |
| apex_system | 05 — Operative & Apex System |
| debrief_rewards | 07 — ARBITER Toolkit |
| prototype_to_tech | PM03 — Future Phases |
| influence_system | 02 — Resource Systems |
| l1_operatives | 05 — Operative & Apex System |
| ghost_actions | 04 — Action Card System |
| layer_roadmap | PM03 — Future Phases |
| arbiter_role_redesign | 07 — ARBITER Toolkit (player-ARBITER role mechanics); PM03 — Future Phases (L5 faction vision) |
| popularity_redesign | 02 — Resource Systems |
