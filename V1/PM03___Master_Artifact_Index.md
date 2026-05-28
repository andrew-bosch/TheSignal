# PM03 — MASTER ARTIFACT INDEX
## THE SIGNAL P1 — Paper Prototype

**Version:** 2.4  
**Status:** 🔄 Updated — Active  
**Last Updated:** 2026-05-26  
**Supersedes:** THE_SIGNAL_P1___Master_Artifact_Index v1.1  
**Sign-off status:** See Design Artifact Registry below for individual artifact status

---

## 1. Design Standards & Terminology

→ All design standards and conventions are maintained in PM04 §2: narrative language convention (mechanical → in-world term mapping), voice and typography, code block standard, terminology sequencing principle, and cross-artifact reference convention.

---

## 2. Cross-Artifact Reference Convention

→ See PM04 §2 for the full cross-artifact reference convention. Summary: **[Artifact ID].[Section].[Subsection]** — example: `Artifact 04 §8`, `PM02 §2b`.

---

## 3. Design Artifact Registry

### Core Rules Artifacts

| ID | Title | Version | Status | Summary |
|----|-------|---------|--------|---------|
| 00 | Factions & World | 1.5 | ✅ Signed Off — S40 | Factions, world, narrative context, ARBITER nature, timescale perspectives. Design Pillar 6 (§5), four-register system (§9), §14 Narrative Anchors incorporated. S33: ring renames. S34: re-sign-off. S38: Dispatch Token anchor §14. S39: §5 Pillar 1 revised ("The Overview is Truth"); §8 MIRROR origin narrative, holographic projection metaphor, Terminal definition; 00-04 closed (Quarter fix). S40: 00-07 multicultural texture (§6 Chorus Node first team, §8 season/cycle, §7 Guild generational building); §11 + §14 Faction Representative (L155). Open: 00-09 (World Conditions panel — design question, does not block sign-off). |
| 00a | Governing Rules & Design Policy | 0.3 | ✅ Signed Off — S40 | 42 rules (R01–R39 + R13a, R13b, R29a), §3–§9, Appendix A. S38: R39 (Dispatch Tokens). S40: stale migration notes removed (§4, §6, §8, §9 freestanding narrative anchors removed — content in Art 00); §11 Punch List removed (belongs in PM05); R38 "Session Timeline" terminology fix. |
| 00b | Data Architecture | 0.2 | ✅ Signed Off — S45 | Entity registry (20 types, ID namespaces), L108 data table standard (extends 1NF), 9 lookup tables (DT/RO/RG/RT/IL/PS/PB/F/VS), entity relationship map, schema reference index. S45: §3 renamed (L108 extends 1NF clarified); component_positions table spec added to §8 (formerly live_state — DB-11 unblocked); running game state derivation architecture documented (§8 — all state derives from component_positions, PM05 DB-13); IP-xx source updated to Art 07; entity/schema footers corrected. Open: DB-11 (agy DDL), DB-13 (derivation query spec). |
| 00c | Economy Manifest | 0.4 | 🔄 Partially Populated — Active Reference | Calibration reference aggregating from 02a v1.4, 02b v1.5, 03 v1.7. §3 Starting Assets (resources, components, tracking scales), §4 Resource Generation Rates (district base values, level modifiers, affinity bonus, structure bonus, passive generation, Findings decay, Public Standing drift, Translation rates, Guild Portrait bonus, Residential Quarter multiplier), §6 Operation System (M-01–M-12 modifier table, base difficulty thresholds, critical bands, Public Standing roll reference), §8 Derived Cost Analysis stub (formula and column spec in place; data blocked on Art 04 completion). §9 Round Income Analysis stub (min-income table in place; expected values require probability model — home TBD, see PM05 00c-02). §5 Card Costs blocked pending Art 04 completion. |
| 01 | Game Board — New Meridian | 1.9 | ✅ Signed Off — S44 | Complete physical zone hierarchy (40 zones): Table → P1–P6 → Central Area (8 sub-zones) → City → Ring 0–3 → 21 districts. District tiles with hex resource colors. District adjacency map (101 rows). Starting Configuration (Fixed Setup / Faction Starting Tokens / Track Starting Values). §9–§10 Faction Player/ARBITER Tableau stubs (Art 08). S44: §4 Narrative Function added (component anchors: District Tiles/Civic Grid, Influence Level Marker, Tension Markers, Session Timeline, Initiative Strip, Chorus Activity Track/The Seismograph, Accord Documents, Situation Reports); §6 Physical Environment — Zones and Components (renamed from [NEW]); §7–§12 renumbered; all component narrative cross-refs resolved; forward procedure refs removed (01-08 ✅). Open: DB-09 (district_adjacency); 00b-05 (live_state schema, L156). |
| 02a | Resource Systems: Board State | 1.6 | ✅ Signed Off — S42 | Presence, influence, structures, resource generation — all publicly visible board state. Session 22: Control flag, Established marker, ARBITER Dominance Marker confirmed. Session 38: §8a Dispatch Tokens & The Backlog added — component definition, spend rules (one token per covert op, pass/political exempt), Ghost asymmetry (4 vs 3), The Backlog as named physical token pool distinct from Reservoir. Session 41: §4 Reservoir narrative anchor added; §8a Dispatch Token narrative intro added (executive authorization framing). Session 42: terminology sweep (Quarter, Baryo/The Mid, Deployment marker, Dispatch Case); §8a Narrative Anchor subheader; Art 01 Supply stub resolved; "Round 1" → "Quarter 1" in starting resources table. |
| 02b | Resource Systems: Tracking | 1.5 | ✅ Signed Off | Chorus Portrait, Public Standing, Intel Tokens — tracking systems alongside the board. Cross-reference audit with 04 pending (PM02 D04-11) |
| 03 | Quarter Structure & Gameplay | 2.0 | ✅ Signed Off — S43 | S43: XA-33 rename ("Quarter Structure & Gameplay"); §18 Battlefield Strength — Contested District Resolution (new, L160); Intel Token freshness system replaces decay (L161, M-13); ring adjacency penalty generalized to The Mid + Core (M-12 updated); "Established or higher" convention (XA-36); Chorus Node flat −25; §4 narrative anchors (inner-ring difficulty, Intel in battle, Intel in Apex); §7 Step 6 (decay) removed; Beat 0 + Beat 4 Intel freshness checks; The Dossier named (L164); Battlefield Modifier Cards + Intel Token (+2, L163) in §18; modifier table header fix; M-12 category Ring; M-13 added; sections renumbered (§18–§23). |
| 03a | Game Engine Specification | 0.98 | 🔄 In Progress — Layers 1–3 complete; Layer 4 stub | Code-lite technical companion to Art 03. Layer 1 (State Model): formal game state at each beat boundary using 00b entity IDs. Layer 2 (Phase & Beat Procedures): Quarter_Flow(); Phase_1()–Phase_7() with explicit state mutations for all phases; Beat_0()–Beat_5() for Phase 6 detail (modifier stack summation formula, resolution inequality). Layer 3 (Decision Tables): DT-01–DT-09; Apex_Activation() procedure. Layer 4 stub (modifier balance analysis) — blocked on Art 04 card definitions. |
| 04 | Card System | 0.9.20 | 🔄 In Progress | S35: L144 locked (1NF + snowflake schema). C15 signed off. C16 signed off. C16–C20 schema uplift complete (§6 schema, section headers, ring modifier fields — 4 per card). pool_copies deprecated (04-40). Effects normalization queued (04-39). Ring modifier formula working (XA-32). C18/C19 redesign flagged (D-04-02). C20 not yet reviewed. S37: Intel economy cards C36–C42 drafted (04-47 schema pass queued). C17 sign-off unblocked (04-41 closed). C37 SACRIFICE: direct PS track step cost confirmed (develop at 04-47). |
| 04a | Card Reference Table | — | ⬜ Not Started | Condensed tabular view of all cards — one row per card, columns: Card ID, Card Name, Card Type, Card Subtype, Card Faction, Beat, Primary Cost, Difficulty, Taxonomy — Category / Function / Subject, Portrait. Full card data stays in Artifact 04; 04a is the lookup and cross-reference layer. Populated after all card reviews complete. Blocked by 04 completion. (Scope confirmed L83.) |
| 04b | Action Taxonomy & Design Analysis | 1.3 | ✅ Reference Document — Active | Companion to 04. S46: §4 redesigned — physical action taxonomy replaces category/function table. 7 verbs (Add, Remove, Move, Reveal, Conceal, Flip, Corrupt); 25-component × verb matrix sourced from the_signal_db.v_comp_verb_matrix. §3 cleanup pending (04b-04); sign-off pending. Coverage gap analysis, faction design recommendations in §6–§8. |
| 05 | Operative & Apex System | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. System structure, operative data format, Apex procedure, Founding Figure slots per faction. Blocked by 04 completion — no card content finalized. |
| 06 | Messaging System | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. Dispatch case protocol, faction messaging, ARBITER notifications, Accord documents, classified directive delivery, dispute resolution. |
| 07 | ARBITER Toolkit | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. Portrait board tracking, Debrief reward system, resolution beats, four narrative registers (The Record / The Observation / The Reckoning / The Witness — updated session 11), Chronicle, ARBITER script pack. |
| 08 | Player Toolkit | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. Faction board layout, starting assets (provisional), deck selection, classified directives, faction reference card, player setup procedure. |

### Reference Artifacts

| ID | Title | Version | Status | Summary |
|----|-------|---------|--------|---------|
| 09 | Card Production Spec | 0.1 | ⬜ Placeholder | Placeholder. Production-only — no design content (L115). All content blocked pending 04 completion. |
| 10 | Game Manuals | 0.1 | 🔄 Draft — Placeholder | Placeholder file created. Player Guide, ARBITER Guide (incl. Translation script table), Setup Guide, Components List (provisional quantities). Pending all upstream sign-offs. |
| 10a | Victory System | 0.1 | ⬜ Placeholder | Placeholder file created. VP source categories, Portrait conversion (design decision required), scoring sequence, vote mechanic, tiebreakers. |
| 11 | Visual Design System | 0.1 | ⬜ Placeholder | Placeholder file created. Faction colors per Artifact 00 §7. Three narrative registers framework. Component standards. V01–V19 priority table. Ghost/Network color adjacency flagged. |

### Project Management Artifacts

| ID | Title | Version | Status | Summary |
|----|-------|---------|--------|---------|
| PM01 | Project Charter & Work Breakdown | 1.6 | 🔄 Active | Scope, deliverables, WBS (with production cost estimates), documentation standards, governance rules, reference convention. §§10–12: Playtest Readiness Checklist, Risk Register, Go/No-Go Framework for V2. §2: Replayability core assumption; S3/S4/S6 extended. WBS 2: 40 components (2.01–2.40), $115–270 est. |
| PM02 | Decision Log & Validation Tracker | 4.0 | 🔄 Active | Locked decisions (L01–L150). S37: L145–L150 (Double Case Pass, Dispatch Tokens, Ghost token gate, Intel universal currency, Intel decay, Month canon term). §2b punch list archived — live version in PM05. |
| PM03 | Master Artifact Index (this document) | 2.4 | 🔄 Active | Artifact registry, standard artifact template, dependency map, retired artifacts index (/Retired/). Design standards and conventions moved to PM04 §2. |
| PM04 | Glossary & Data Dictionary | 0.7 | 🔄 Updated — Active | Single source of truth for all terminology and design conventions. §1: In-World Data Dictionary — Component Physical Glossary added (S34); Asset token removed. §2: Design Terminology — Category column pattern (S34), L109 Component Terminology Standard (S34) added alongside existing conventions. |
| PM04b | Future Phases — Parking Lot | — | ⬜ Not Started | Post-L1 design concepts, layer roadmap, electronic version considerations, ARBITER role redesign, L5 faction vision. Companion to PM04 — not yet created. |
| PM05 | Active Punch List | 2.9 | 🔄 Active | Living action queue of all pending changes across all artifacts. S45: 00b-05 ✅, XA-32 scoped to Art 07 only, DB-11 new (agy DDL — component_positions rename + columns), DB-12 closed (L156), DB-13 new (derivation query spec), DB-02 reference updated. |
| PM (Audit) | Cross-Artifact Inconsistency Audit | 1.0 | ✅ Retired — session 10 | All 24 items migrated to PM05 punch list. File deleted. |

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
                 └─ 04 (Card System)
                 │   └─ 04b (Taxonomy — reference only)
                 └─ 05 (Operative & Apex System)
                     └─ 06 (Messaging System)
                         └─ 07 (ARBITER Toolkit)
                         └─ 08 (Player Toolkit)
                             └─ 09 (Card Production Spec)
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
| card_designs | 09 — Card Production Spec |
| arbiter_guide | 07 — ARBITER Toolkit, 10 — Game Manuals |
| player_guide | 08 — Player Toolkit, 10 — Game Manuals |
| reference_sheets | V12–V18 Visual Quick References |
| setup_guide | 10 — Game Manuals |
| event_card_system | 01 — Game Board, 09 — Card Production Spec |
| l1_generation | 02a — Resource Systems: Board State |
| action_redesign | 04 — Card System (superseded) |
| apex_system | 05 — Operative & Apex System |
| debrief_rewards | 07 — ARBITER Toolkit |
| prototype_to_tech | PM04 — Future Phases |
| influence_system | 02a — Resource Systems: Board State |
| l1_operatives | 05 — Operative & Apex System |
| ghost_actions | 04 — Card System |
| layer_roadmap | PM04 — Future Phases |
| arbiter_role_redesign | 07 — ARBITER Toolkit (player-ARBITER mechanics); PM04 — Future Phases (L5 faction vision) |
| popularity_redesign | 02b — Resource Systems: Tracking |
| THE_SIGNAL_P1___Master_Artifact_Index | PM03 — Master Artifact Index (this document) |

---

### Legacy Folder Archive — /Retired

Two generations of pre-V1 design documents are archived in `/TheSignal/Retired/`, organized into subfolders as of 2026-05-16. (Folder was `/Old/` prior to 2026-05-16 reorganization.) These files are read-only reference — content has been redistributed into the V1 artifact set. Do not edit.

**`/Retired/Electronic/`** — 20 files — Original electronic brainstorming suite (pre-code design phase). Document numbering: 00–20. Uses old faction names (Architect, Warden, Signal). Includes TypeScript game state schema, hardware specifications, network architecture, audio system, website architecture, and full game design documents.

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

**`/Retired/Paper/`** — 6 files + 1 zip — 1st generation Paper (pre-V1) design suite. Uses current V1 naming convention and current faction names. Early versions of V1 artifacts before the current baseline was established.

| File | Contents |
|------|----------|
| old__THE_SIGNAL_P1___Master_Artifact_Index.md | P1 Master Artifact Index v1.1 — superseded by PM03 |
| old__00___Factions_World_Narrative_Context.md | Artifact 00 v1.3 — superseded by current V1/00 |
| old__01___Game_Board_New_Meridian.md | Artifact 01 — superseded by current V1/01 |
| old__02a___Resource_Systems_Board_State.md | Artifact 02a — superseded by current V1/02a |
| old__02b___Resource_Systems_Tracking.md | Artifact 02b — superseded by current V1/02b |
| old__04b___Action_Taxonomy_Design_Analysis.md | Artifact 04b — superseded by current V1/04b |
| files.zip | Snapshot archive of V1 P1 artifacts as of 2026-05-15: PM01, PM02, PM03, 00, 01, 02a, 02b, 03, 04, 04b |

**`/Retired/backup.zip`** — Complete backup of the /Retired folder prior to reorganization. Contains all 26 files from both the Electronic and Paper generations.

---

## 7. Creative Content Directory

**`/Creative/`** — World-building source material: characters, vignettes, stories, and quotes generated to deepen the world of THE SIGNAL and provide possible source material for Artifact 00 and player-facing flavor copy.

This directory is **not part of the design artifact set.** Content here is evaluated, not assumed canonical. The brief for writers and AI agents lives at `Creative/CREATIVE_BRIEF.md`. Submission tracking lives at `Creative/README.md`.

| Subdirectory | Contents |
|-------------|---------|
| `Creative/Characters/` | Character profiles, histories, voice sketches |
| `Creative/Vignettes/` | Short scenes (100–600 words) |
| `Creative/Stories/` | Longer narratives (600+ words) |
| `Creative/Quotes/` | Standalone voiced moments (1–5 sentences, attributed) |

**Evaluation to canon:** Canon decisions are recorded in PM02. Flavor copy is tagged with a target artifact location in `Creative/README.md`.

---

*End of PM03 — Master Artifact Index v2.2*
