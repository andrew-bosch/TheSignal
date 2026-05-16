# PM03 — MASTER ARTIFACT INDEX
## THE SIGNAL P1 — Paper Prototype

**Version:** 1.4  
**Status:** 🔄 Updated — Active  
**Last Updated:** 2026-05-15  
**Supersedes:** THE_SIGNAL_P1___Master_Artifact_Index v1.1  
**Sign-off status:** See Design Artifact Registry below for individual artifact status

---

## 1. Narrative Language Convention

All documentation uses in-world narrative terms. Each mechanical term is defined once on first use, then the narrative term is used exclusively throughout all artifacts.

| Mechanical Term | In-World Term | First Defined In |
|----------------|---------------|-----------------|
| Board space | District | 01 §1 |
| Game mat / full shared display | The Overview | 00 §8 |
| Game board / district map (within The Overview) | New Meridian | 01 §1 |
| Influence token | Presence token | 02a §1 |
| Claim marker | Operational marker | 01 §1 |
| Recipe box | Dispatch case | 06 §1 |
| Popularity track | Public Standing track | 02b §1 |
| Portrait score | Chorus Portrait | 02b §1 |
| Proof token | Intelligence token | 02b §1 |
| Modifier card | Working designation — in-world name pending (D04-07) | 04 §11 |
| Counter card | Countermeasure card | 04 §14.2 |
| Private action | Covert operation | 04 §1 |
| Public action | Political act | 04 §1 |
| Hidden objective | Classified directive | 05 §1 |
| Operative card | Field operative dossier | 05 §1 |
| World event card | Situation report | 01 §1 |

| Round (game term) | Quarter (three months of real-world time) | 03 §1 |

*ARBITER and The Table are never renamed — they are already in-world terms.*

### Voice & Typography Convention

Five distinct voices appear in design artifacts and player-facing materials. Each uses a fixed typographic treatment so voice is identifiable at a glance in both markdown source and rendered output.

| Voice | When Used | Markdown Treatment | Visual Design Intent |
|-------|-----------|--------------------|----------------------|
| **The Narrator** | All "Narrative:" fields in design artifacts. Expository prose that describes the world as it is. Identity deliberately unresolvable — see note below. | Plain prose, no attribution, no special formatting | Precise, observational, neither warm nor cold. The reader cannot determine if this is a human chronicler or ARBITER in an expository mode. Both readings must remain valid. |
| **Character quote** | Flavor in Narrative fields — operative, faction member, citizen, witness. Grounds a rule or world-fact in a specific human moment. | `> *"Quote."*` followed by `> — Role, Faction` on next line | Serif pull quote, attributed |
| **ARBITER vocalized** | Spoken aloud at the table — resolution announcements, Translation script, Apex acknowledgment, Debrief. | `> *"Text."*` (blockquote, italic, no attribution) | ARBITER voice style — the register carries the speaker |
| **ARBITER written** | Delivered on paper — notification slips, Chronicle entries, Accord confirmations, dispatch language. | Fenced code block | Monospace / typewriter / dispatch aesthetic |
| **Faction voice** | Faction-specific documents, opening monologues, internal communications. Each faction has a distinct voice. | Per faction voice guide (Artifact 00 §12) | Differentiated by faction doctrine and emotional register |

**The Narrator — design principle (locked, PM02 FD-05):**
The Narrator's identity is deliberately never established. It has access to faction internals, Chorus analysis, ARBITER records, and The Table's proceedings — without explaining how. Its register is precise and observational: it notices the right detail, not the obvious one. It states things directly and lets implications stand without developing them. The test for any Narrator sentence: could this have been written by a human who knows too much, or by ARBITER in an expository mode? If both readings are valid, it is correct. If the sentence resolves the ambiguity in either direction, revise it. The Narrator's unresolvability is not a gap — it is the voice.

**The Character Cast — design principle (locked, PM02 FD-05):**
Character quotes are not generic "faction member" flavor. They build a cast — individuals with implied histories, roles, specific relationships to the events they are describing. Each faction has a differentiated pool of voices: the analyst who has been in the same lab for fifteen years; the field coordinator who grew up in the Sprawl and never left; the trader who learned to read rooms before she learned to read; the structural engineer who thinks in load-bearing walls; the liaison who chose the institution over everything else, and knows what that cost. Unnamed characters carry their world in their attribution line. Named operatives (Artifact 05) carry it in their dossier and their quotes. The reader should be able to hear the difference between a Ghost quote and a Guild quote without reading the attribution — the faction's doctrine should be present in how the person phrases what they saw. The cast is not limited to faction operatives or to New Meridian. Pre-Chorus residents carry knowledge no faction operative has. Voices from outside the city — foreign correspondents, remote academics, officials from other governments, people passing through — imply a world larger than The Table and older than the Chorus. Some characters are trying to win something. Some of them are just people who were there.

**Rules:**
- Narrator fields use no special formatting — plain prose. Never attribute them.
- Character quotes always have attribution (role and faction, not personal name unless the character is a named operative).
- ARBITER vocalized quotes never have attribution — the register identifies the speaker.
- ARBITER written blocks are never italicized — monospace is the signal.
- Faction voice is reserved for faction-authored documents and monologues — it does not appear in design artifact Narrative fields.
- No two character quotes from the same faction should sound interchangeable. If they do, one is wrong.

**Code block (fenced ```)** — Standard format for any content that functions as a map, schematic, or at-a-glance structural summary rather than prose. Use when: (1) content is a structured overview meant to be scanned, not read; (2) the visual distinction from surrounding prose is intentional and meaningful; (3) the content would become a designed diagram or infographic element in final layout. Do not use for prose explanations, rules text, or examples. Applied: Artifact 03 §6 Round Overview.

*First applied: 00a §3–§10 Narrative fields. Propagates to Artifacts 07 (script pack), 10 (manuals), and all future artifacts.*

---

### Information Design Principle — Terminology Sequencing

No term, in-world concept, or named component may appear in an artifact without its narrative grounding having been established first — in a prior artifact or earlier in the same artifact. A reader moving through the artifact set in order should never encounter a term before the world has given it meaning. The mechanics that use a term are downstream of the fiction that defines it.

This applies to: in-world component names, faction concepts, institutional terms, temporal conventions, and named game elements. Violations are not copy problems — they indicate missing narrative foundation.

*Example: "quarter" as the deliberation period must be established in Artifact 00 before it appears in 00a or Artifact 03. The Narrative Language table below is the audit instrument — if a term appears there, verify its narrative grounding in Artifact 00 precedes its first mechanical use.*

Locked as L86 in PM02.

---

## 2. Cross-Artifact Reference Convention

Standard reference format: **[Artifact ID].[Section].[Subsection]**

Examples:
- `Artifact 04 §8` — Section 8 of Artifact 04
- `Artifact 03 §12.3` — Section 12, Subsection 3 of Artifact 03
- `Artifact 02b §8–9` — Sections 8 through 9 of Artifact 02b
- `PM02 §2b` — Section 2b of PM02

Applies to all in-document references, cross-artifact design notes, PM02 blocking decisions, and punch list source citations. Section number changes are a non-material change — references should be audited and updated when an artifact is restructured. Full definition in PM01 §3.

---

## 3. Design Artifact Registry

### Core Rules Artifacts

| ID | Title | Version | Status | Summary |
|----|-------|---------|--------|---------|
| 00 | Factions & World | 1.0 | ✅ Signed Off | Factions, world, narrative context, ARBITER nature, timescale perspectives. Secondary purposes: source material for rulebook sidebar copy, artwork inspiration, and subtle narrative foundation for future expansion. Narrative enrichment pass pending (PM02 §2b 00-03, 00-04). |
| 00a | Governing Rules & Design Policy | 0.2 | 🔄 Draft — Active Review | 45 rules across 8 categories (§3–§10). Full Rule/Narrative/Mechanics/Source/Governs structure applied to all R01–R44+R30a. Governing principles: Narrative and World Consistency; Copy Design (no hardcoded variable values). Pending review and sign-off. |
| 01 | Game Board — New Meridian | 1.2 | ✅ Signed Off | District layout, rings, Chorus Node, track positions, starting configuration. Adjacency table pending (PM02 D04-09). Setup update pending (01-03). |
| 02a | Resource Systems: Board State | 1.2 | ✅ Signed Off | Presence, influence, structures, resource generation — all publicly visible board state. Chorus Node language update pending (02a-03). |
| 02b | Resource Systems: Tracking | 1.5 | ✅ Signed Off | Chorus Portrait, Public Standing, Intel Notes — tracking systems alongside the board. Cross-reference audit with 04 pending (PM02 D04-11) |
| 03 | Round Structure & Gameplay | 1.5 | 🔄 Pending Re-Sign-Off | Six phases, timing, initiative, ARBITER conversion, Apex trigger. Material changes: Beat 2 renamed, Step 6 rewritten, Declaration phase updated. Review PM02 D03-R01 through D03-R03. |
| 04 | Action Card System | 0.9.6 | 🔄 In Progress | Covert operations C01–C15 signed off. Political acts and faction-specific cards C16–C35 pending review. 12 blocking decisions open — see PM02 §2. |
| 04a | Card Reference Table | — | ⬜ Not Started | Condensed tabular view of all cards — one row per card, columns: Card ID, Card Name, Card Type, Card Subtype, Card Faction, Beat, Primary Cost, Difficulty, Taxonomy — Category / Function / Target, Portrait. Full card data stays in Artifact 04; 04a is the lookup and cross-reference layer. Populated after all card reviews complete. Blocked by 04 completion. (Scope confirmed L83.) |
| 04b | Action Taxonomy & Design Analysis | 1.1 | ✅ Active Reference | Companion to 04. Taxonomy framework, coverage gap analysis, faction design recommendations. Not playtest-blocking. |
| 05 | Operative & Apex System | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. System structure, operative data format, Apex procedure, Founding Figure slots per faction. Blocked by 04 completion — no card content finalized. |
| 06 | Messaging System | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. Dispatch case protocol, faction messaging, ARBITER notifications, Accord documents, classified directive delivery, dispute resolution. |
| 07 | ARBITER Toolkit | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. Portrait board tracking, Debrief reward system, resolution beats, three narrative registers (Procedural/Advisory/Reactive), Chronicle, ARBITER script pack. |
| 08 | Player Toolkit | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. Faction board layout, starting assets (provisional), deck selection, classified directives, faction reference card, player setup procedure. |

### Reference Artifacts

| ID | Title | Version | Status | Summary |
|----|-------|---------|--------|---------|
| 09 | Card Specifications | 0.1 | ⬜ Placeholder | Placeholder file created. Structure and 20-field format defined. All content blocked pending 04 completion. |
| 10 | Game Manuals | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. Player Guide, ARBITER Guide (incl. Translation script table), Setup Guide, Components List (provisional quantities). Pending all upstream sign-offs. |
| 10a | Victory System | 0.1 | ⬜ Placeholder | Placeholder file created. VP source categories, Portrait conversion (design decision required), scoring sequence, vote mechanic, tiebreakers. |
| 11 | Visual Design System | 0.1 | ⬜ Placeholder | Placeholder file created. Faction colors per Artifact 00 §7. Three narrative registers framework. Component standards. V01–V19 priority table. Ghost/Network color adjacency flagged. |

### Project Management Artifacts

| ID | Title | Version | Status | Summary |
|----|-------|---------|--------|---------|
| PM01 | Project Charter & Work Breakdown | 1.3 | 🔄 Active | Scope, deliverables, WBS, documentation standards, governance rules, reference convention |
| PM02 | Decision Log & Validation Tracker | 1.4 | 🔄 Active | Locked decisions (L01–L84), open blocking decisions, playtest variables, validation targets, pending changes punch list, change log |
| PM03 | Master Artifact Index (this document) | 1.5 | 🔄 Active | Artifact registry, narrative language convention, reference convention, standard template, retired artifacts |
| PM04 | Glossary & Data Dictionary | 0.1 | ⬜ Placeholder | Single source of truth for all terminology. §1: In-World Data Dictionary. §2: Design Terminology (absorbs PM03 §1 language table, PM01 terminology). See PM02 PM04-01, PW-04. |
| PM04 | Future Phases — Parking Lot | — | ⬜ Not Started | Post-L1 design concepts, layer roadmap, electronic version considerations, ARBITER role redesign, L5 faction vision. Supersedes former PM03. |
| PM (Audit) | Cross-Artifact Inconsistency Audit | 1.0 | 🔄 Active — For Review | 24 inconsistencies and open questions across all signed-off and draft artifacts. Organized by artifact. Items to migrate to PM02 punch list after Andy review. |

### Visual Artifacts (Interactive HTML)

| ID | Title | Status | Notes |
|----|-------|--------|-------|
| V01 | Game Mat / Table Layout | 🔄 Draft | |
| V02 | Public Standing Track | ⬜ Not Started | |
| V03 | Round Phase Slider | ⬜ Not Started | |
| V04 | World Condition Tracks | 🔄 Draft | |
| V05 | Situation Report (World Event) Layout | 🔄 Draft | |
| V06 | Accord Document Layout | ⬜ Not Started | |
| V07 | Card Layouts — all types | 🔄 Draft | Requires 04 completion and 11 Visual Design System |
| V08 | District Hex Layout | ⬜ Not Started | |
| V09 | Player Tools Visual Layouts | ⬜ Not Started | |
| V10 | ARBITER Tools Visual Layouts | ⬜ Not Started | |
| V11 | Dispatch Case / Messaging Layout | ⬜ Not Started | |
| V12 | Quick Reference — Round Phases | ⬜ Not Started | |
| V13 | Quick Reference — Card Types | ⬜ Not Started | |
| V14 | Quick Reference — Difficulty | ⬜ Not Started | |
| V15 | Quick Reference — Covert Operations | ⬜ Not Started | |
| V16 | Quick Reference — Political Acts | ⬜ Not Started | |
| V17 | Quick Reference — Intelligence Tokens | ⬜ Not Started | |
| V18 | Quick Reference — Public Standing | ⬜ Not Started | |
| V19 | Intelligence Token Layout | ⬜ Not Started | |

---

## 4. Standard Artifact Template

Every text-based design artifact (IDs 00–11) follows this structure unless the artifact's nature requires deviation (noted in the artifact itself). Section names are fixed — do not rename them.

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

**Reference convention within artifacts:** `[Artifact ID].[Section].[Subsection]` — see §2 above.

**Card data structure** (Artifact 04 and 09): Cards use a separate 20-field data structure defined in Artifact 04 §6. The standard template above applies to artifact prose sections, not individual card definitions.

---

## 5. Artifact Dependency Map

Reading order reflects dependency — no artifact references a concept not yet introduced in a prior artifact.

```
00 (World & Factions)
 ├─ 00a (Governing Rules & Design Policy — companion, no new mechanics)
 └─ 01 (Game Board)
     └─ 02a (Resource Systems: Board State)
         └─ 02b (Resource Systems: Tracking)
             └─ 03 (Round Structure)
                 └─ 04 (Action Card System)
                 │   └─ 04b (Taxonomy — reference only)
                 └─ 05 (Operative & Apex System)
                     └─ 06 (Messaging System)
                         └─ 07 (ARBITER Toolkit)
                         └─ 08 (Player Toolkit)
                             └─ 09 (Card Specifications)
                             └─ 10 (Game Manuals)
                             │   └─ 10a (Victory System)
                             └─ 11 (Visual Design System)
                                 └─ V01–V19 (Visual Artifacts)
```

PM01, PM02, PM03, PM04 are parallel to this chain — they govern the project but do not introduce game mechanics.

---

## 6. Retired Artifacts

The following artifacts from the working design phase are superseded by the current baseline set. They should not be edited further. Content has been redistributed into the numbered artifact set.

| Former Artifact | Content Moved To |
|----------------|-----------------|
| game_overview | 10 — Game Manuals |
| components | 10 — Game Manuals |
| round_structure | 03 — Round Structure |
| hidden_objectives | 02b — Resource Systems: Tracking, 05 — Operative System |
| card_designs | 09 — Card Specifications |
| arbiter_guide | 07 — ARBITER Toolkit, 10 — Game Manuals |
| player_guide | 08 — Player Toolkit, 10 — Game Manuals |
| reference_sheets | V12–V18 Visual Quick References |
| setup_guide | 10 — Game Manuals |
| event_card_system | 01 — Game Board, 09 — Card Specifications |
| l1_generation | 02a — Resource Systems: Board State |
| action_redesign | 04 — Action Card System (superseded) |
| apex_system | 05 — Operative & Apex System |
| debrief_rewards | 07 — ARBITER Toolkit |
| prototype_to_tech | PM04 — Future Phases |
| influence_system | 02a — Resource Systems: Board State |
| l1_operatives | 05 — Operative & Apex System |
| ghost_actions | 04 — Action Card System |
| layer_roadmap | PM04 — Future Phases |
| arbiter_role_redesign | 07 — ARBITER Toolkit (player-ARBITER mechanics); PM04 — Future Phases (L5 faction vision) |
| popularity_redesign | 02b — Resource Systems: Tracking |
| THE_SIGNAL_P1___Master_Artifact_Index | PM03 — Master Artifact Index (this document) |

---

### Legacy Folder Archive — /Old

Two generations of pre-V1 design documents are archived in `/TheSignal/Retired/`, organized into subfolders as of 2026-05-16. (Folder was `/Old/` prior to 2026-05-16 reorganization.) These files are read-only reference — content has been redistributed into the V1 artifact set. Do not edit.

**`/Old/Electronic/`** — 20 files — Original electronic brainstorming suite (pre-code design phase). Document numbering: 00–20. Uses old faction names (Architect, Warden, Signal). Includes TypeScript game state schema, hardware specifications, network architecture, audio system, website architecture, and full game design documents.

| File | Contents |
|------|----------|
| old__00_PROJECT_INDEX.md | Master index for the electronic design suite |
| old__01_WORLD_AND_NARRATIVE.md | Setting, factions, ARBITER, The Chorus, legacy structure |
| old__02_GAME_RULES.md | Complete formal rulebook written in ARBITER's voice |
| old__03_FACTIONS_AND_OPERATORS.md | All 5 factions, 20 operators, abilities, unlock conditions |
| old__04_CITY_OF_NEW_MERIDIAN.md | Board design, district history, layer system |
| old__05_ECONOMY_AND_RESOURCES.md | All 6 resources, generation rates, costs, trade rules |
| old__06_CARD_SYSTEM.md | Card types, NFC/QR system, production, legacy evolution |
| old__07_ARBITER_SYSTEM.md | ARBITER design, AI integration, voice, stage evolution |
| old__08_DATA_MODEL.md | TypeScript game state schema v0.2 |
| old__09_ACTION_RESOLUTION.md | Resolution pipeline, priority tiers, conflict handling |
| old__10_INFORMATION_HIERARCHY.md | Visibility rules — all game information (ARBITER_ONLY through WEBSITE_PRIVATE) |
| old__11_HARDWARE_SPECIFICATION.md | ESP32 terminals, ARBITER Raspberry Pi unit, laser projector, mat, full BOM |
| old__12_AUDIO_SYSTEM.md | Soundtrack, state cues, ARBITER voice, haptics |
| old__13_NETWORK_ARCHITECTURE.md | Protocol spec (WebSocket), failure modes, OTA updates |
| old__14_WEBSITE_ARCHITECTURE.md | Open Network, Secure Archive, between-session web content |
| old__15_DESIGN_GAPS.md | Remaining design decisions before development — pre-code checklist |
| old__16_DEVELOPMENT_ROADMAP.md | Incremental build sequence, milestone structure |
| old__18_ECONOMY_BALANCE_NOTES.md | Starting resource values, faction economic arcs, balance rationale |
| old__19_PAPER_PROTOTYPE_CORE_DESIGN.md | Paper prototype design philosophy and core requirements |
| old__20_ROUND_WALKTHROUGH_AND_PRODUCTION.md | Complete Round 4 walkthrough for 5-player paper prototype session |

**`/Old/Paper/`** — 6 files + 1 zip — 1st generation Paper (pre-V1) design suite. Uses current V1 naming convention and current faction names. Early versions of V1 artifacts before the current baseline was established.

| File | Contents |
|------|----------|
| old__THE_SIGNAL_P1___Master_Artifact_Index.md | P1 Master Artifact Index v1.1 — superseded by PM03 |
| old__00___Factions_World_Narrative_Context.md | Artifact 00 v1.3 — superseded by current V1/00 |
| old__01___Game_Board_New_Meridian.md | Artifact 01 — superseded by current V1/01 |
| old__02a___Resource_Systems_Board_State.md | Artifact 02a — superseded by current V1/02a |
| old__02b___Resource_Systems_Tracking.md | Artifact 02b — superseded by current V1/02b |
| old__04b___Action_Taxonomy_Design_Analysis.md | Artifact 04b — superseded by current V1/04b |
| files.zip | Snapshot archive of V1 P1 artifacts as of 2026-05-15: PM01, PM02, PM03, 00, 01, 02a, 02b, 03, 04, 04b |

**`/Old/backup.zip`** — Complete backup of the /Old folder prior to reorganization. Contains all 26 files from both the Electronic and Paper generations.

---

*End of PM03 — Master Artifact Index v1.4*
