# THE SIGNAL

**[→ Project Homepage](https://andrew-bosch.github.io/TheSignal/)**

A legacy negotiation and area-control tabletop game for 2–6 players (up to 5 faction players + 1 ARBITER). Factions negotiate humanity's response to a transmission called The Chorus. Set in New Meridian, 2041.

---

## Project Status

**Current phase:** L1 — Paper Prototype (physical-only, no electronics)  
**Active design layer:** `/V1`  
**Design milestone:** S162 — Art 04c (Card System Cost Model) created and signed off at v2.0; four of five S160 gate items closed (04-n230/231/232/233, with two premises corrected); Art 00c cost model split out entirely to 04c due to canonical conflict (two reference files cited 00c despite its own prohibition header); PM02 L380, PM05 00c-03 CLOSED since S159. Silent sync ordering defect fixed: `extract_card_effects.py` ran before `card_body` table reload, weakening every drift check; corrected and verified. Art 03 v4.15 / Art 04 v0.9.101 / Art 04b v2.7 / Art 04c v2.0. Art 00c → v0.7 (pure index). Derived docs synced: Database/schema_reference.md, design_reference*.md, ref_*.md. PM02 L378–L380. Prior — S161 — side session, no Art 04 work: World Engine chartered as PM01 WBS 4 (PM02 L377, constraints in PM05 WE-01, build gated on Art 04 sign-off, lev cleared for 4.02 groundwork only), PM01 §6 exclusion clarified to in-session agent narrative, AI-as-ARBITER logged as FD-07; ten-role review of the Creative/ corpus found 4 of 6 vignettes need rewrites and two informal canon absorptions with no promotion record (PM05 CR-01/CR-02, detail in Whiteboard/creative_role_review_s161.md); yakko context envelope measured at ~128K on a 16GB card. PM01 → v1.7.

---

## Design Artifacts

*Authoritative sign-off status: [PM03 — Master Artifact Index](V1/PM03___Master_Artifact_Index.md)*

*Sections correspond to program architecture. Artifacts are source code. The DB is the runtime representation. Physical components are I/O. ARBITER is the interpreter.*

---

### Governing Constraints

*Narrative is the primary design constraint — not a category alongside constraints but the governing law of the design. All mechanical decisions require a narrative anchor. Design Pillar 6: when narrative and mechanical reasoning conflict, narrative prevails. Read before any other artifact.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 00 | [Factions, World & Narrative Context](V1/00___Factions_World_Narrative_Context.md) | 1.9 | ✅ Signed off — S134 (L255). S134: §6.7 Ring Character (narrative anchor), §15 curriculum extended (Pine Gap). Bundles S99 §14.10, S131 §15, S134 §6.7+Pine Gap. Prior: ✅ S93 (L211). S118: component name sweep. |
| 00a | [Governing Rules & Design Policy](V1/00a___Governing_Rules___Design_Policy.md) | 0.13 | ✅ Signed off — S150 (§7.2c Triggering Conditions Are Exhausted on Resolution). S148: §10.4 Covert Attribution Remains Untraceable. S108: GR 10.1b. S118: component name sweep. |

---

### Logical Data Model

*00b tracks DB migration status — what remains to be modeled for deep analysis and balance work. 00c defines resource types and economic parameters; starting values are seeded by 03-init at game start. Authoritative entity schemas in `Database/schema_reference.md`.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 00b | [Analysis Readiness](V1/00b___Analysis_Readiness.md) | 0.3 | ✅ Signed off — S83 |
| 00c | [Economy Manifest](V1/00c___Economy_Manifest.md) | 0.7 | 🔄 In progress — S162: cost model split to Art 04c; Art 00c now a pure index with two pointer stubs; prohibition ("Do not cite 00c for design decisions or ref files") holds without exception. |

---

### Imports — Game Objects

*Zone and component registries. Implement the logical data model specified in 00b/00c. No execution logic — define what exists and its properties.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 01 | [Zones: Physical & Virtual Geography](V1/01___Game_Board_New_Meridian.md) | 2.3 | ✅ Signed off — S130 (L239). S118: component name sweep. |
| 02 | [Components](V1/02___Components.md) | 2.5 | ✅ Signed off — S149 (Target Profile amendment re-review, PM02 L326). S111: base sign-off (L233). S118: full component name Title Case sweep (headings + metadata + body). |

---

### Main()

*Game entry point and main execution loop. 03-init owns initialization; 03 owns the session while-loop; 03a specifies the execution engine.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 03-init | [Game Initialization](V1/03-init___Game_Initialization.md) | 0.5 | 🔄 In progress. S124: §3.9 Deck Selection added; §3.6 sequencing conflict open (04-n137). |
| 03 | [while session(true): Quarter Structure](V1/03___Round_Structure___Gameplay.md) | 4.15 | ✅ Signed off — S150 (§7.4 Resource Type rule, §18 tiebreak refinement, PM02 L339–L345). S149 (§18.2.2 React default removal, PM02 L332). S146 (L293): §9.4.3.1.0.3 Route zero-payment consequence. Prior: ✅ S132 (L243). §10.1.2 Battlefield Strength redesigned (Boost/Hinder ModBattleCard model, face-down commit/reveal, any faction may commit, Intel Token −2 Hinder); §10.1.4.0/0.2/1 sequential steps + cleanup relocation. Prior: S110 (L232). |
| 03a | [Game Engine Specification](V1/03a___Game_Engine_Specification.md) | 0.99 | 🔄 In progress. S118: component name sweep. |
| 03b | [Component Lifecycle Register](V1/03b___Component_Lifecycle.md) | 0.2 | 🔄 In progress. S118: component name sweep. |

---

### Stored Procedures

*Callable modules dispatched by Main() or its core subroutines. 04b is design analysis proving the Art 04 card metadata schema — companion document, not callable.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 04 | [Card Set: Action Subroutines](V1/04___Card_System___Part1_Core.md) | 0.9.101 | 🔄 In progress — S162: cost model split to Art 04c; four of five S160 gate items closed (04-n230/231/232/233); two premises corrected (04-n230: GD-01 step-4 now gated on step 3; 04-n232: STD.CA.9 vs GUI.PA.2 discriminator recorded in Art 04b §5.1); GHO.PA.5 two defects fixed (missing faction= and game.add target); 04-n235 rehomed to 04c-01 (pricing convention); 04-n237 opened (47 §8 rows still assert retired taxonomy); PM05 DB-50 fixed (sync ordering: extract_card_effects.py now runs after card_body reload, not before; drift guard verified clean); Art 04 → v0.9.101, Art 04b → v2.7. PM02 L378–L380. Prior — S160: Add-vs-Redirect mis-tag sweep (all 85 Function=Add audited, GD-01 retagged), target-field semantics rewrite (108 of 355 rows fixed), 04-n229 closed (Redirect double-count), value_rating defined as gross effect delivered (L376, now locked in Art 04c §9 caveat), Toll/cut family rewritten (three names + six Card Stories), parser fixes (find_magnitude: SYN.CA.3 20.13→7.63; GHO.CA.10/GHO.CA.6 1→3, GUI.CA.7 3→4), corpus zero drift, two infrastructure defects fixed (v_card_pair_uvm_cost versioned to Database/, sync drift-guard re-keyed), opened 04-n230/231/232/233/235 (all gating), closed 04-n229/234/236. PM02 L370–L376. |
| 04b | [Action Taxonomy](V1/04b___Action_Taxonomy_Design_Analysis.md) | 2.7 | ✅ Signed off — S108 (L230 scope policy). S162: §5.1 Add-vs-Redirect discriminator recorded with worked pair (STD.CA.9 Redirect vs GUI.PA.2 Add). S123: §6.4 STD+NET 5-check added; §8.3 Network updated (12-card S123 data). S122: §6.4 STD+GUI added; §8.5 Guild updated. |
| 04c | [Card System Cost Model](V1/04c___Card_System_Cost_Model.md) | 2.0 | ✅ Signed off — S162 (PM02 L378–L379). **What cards charge:** §3 Principle 15 · §4 cost vocabulary · §5 cost by card type · §6 cross-resource costs · §7 Intel Tokens. **How effects are priced:** §8 definition · §9 UVM + ⚠ governing caveat · §10 boundaries · §11 limits · §12 Derived Cost Analysis (gated on Art 04 sign-off). No cost magnitude rule is locked for any card type. ModReactCard is the only Modifier subclass that charges resources (27 of 93). 18 cards take an Intel Token as cost (10 CA, 4 PA, 4 ModReact). |
| 05 | [Operative & Apex Subroutines](V1/05___Operative_Apex_System.md) | 0.2 | ⬜ Placeholder |
| 06 | [Messaging System](V1/06___Messaging_System.md) | 0.5 | 🟡 In progress — §9 Accord governance signed off S83 (L205). S118: component name sweep. |
| 07 | [ARBITER Subroutines](V1/07___ARBITER_Toolkit.md) | 0.2 | ⬜ Placeholder |
| 08 | [Faction Player Subroutines](V1/08___Player_Toolkit.md) | 0.2 | ⬜ Placeholder |
| 10a | [Victory: Game Exit](V1/10a___Victory_System.md) | 0.2 | ⬜ Placeholder |

---

### Documentation

*Human-readable player and production artifacts. The playable, printable, and visual layer built from the source artifacts above.*

| # | Artifact | Ver | Status |
|---|----------|-----|--------|
| 09 | [Card Production Specification](V1/09___Card_Production_Spec.md) | 0.2 | ⬜ Placeholder |
| 10 | [Game Manuals](V1/10___Game_Manuals.md) | 0.2 | ⬜ Placeholder |
| 11 | [Visual Design System](V1/11___Visual_Design_System.md) | 0.2 | ⬜ Placeholder |

---

## Project Management

| Doc | Purpose |
|-----|---------|
| [PM01 — Project Charter & Work Breakdown](V1/PM01___Project_Charter___Work_Breakdown.md) | Charter, WBS, Playtest Readiness Checklist, Risk Register |
| [PM02 — Decision Log & Validation Tracker](V1/PM02___Decision_Log___Validation_Tracker.md) | Locked decisions L01–L236, open decisions, change log |
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
├── Database/     ← DB schema reference (schema_reference.md) and SQL build scripts
├── Whiteboard/   ← Scratch and in-progress design docs not yet in a canonical artifact
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
- **In-world language:** All mechanical terms have canonical in-world equivalents (Districts not Hexes, Presence Tokens not Influence tokens, etc.). PM04 §1 and L236 are the authorities.
- **Terminology sequencing:** No term appears in an artifact before its narrative grounding is established. Art 00 is always read first.
- **Change governance:** Material changes require re-sign-off. Non-material changes (style, terminology, clarification) do not. See PM05 for all pending changes.
- **Vocabulary:** ARBITER, Faction, The ARBITER Player, Faction Player — four distinct terms used precisely. See PM02 L88.

---

## Wiki Maintenance & Deployment

The project wiki is built using `mkdocs` with the `material` theme. It serves as the primary mobile review surface for large artifacts — Art 04 (Card System) in particular is physically split at the source into 8 files (S136) to keep individual chapters small enough for iOS WebKit to render.

*   **Wiki Source Directory:** `wiki_src/` (contains generated docs and `mkdocs.yml`; excluded from git via `.gitignore`).
*   **Build Script:** `python3 tools/build_wiki.py` (wipes `wiki_src/docs/`, copies/flattens files from `V1/`, `Whiteboard/`, `Creative/`, `ClaudeIOS/`, automatically subdivides card system files exceeding 150 KB into pages of at most 12 cards, builds the card-ID slug-routing map, and runs dynamic link/anchor resolution to heal relative links and map legacy/standard card prefixes to their specific sub-pages).
*   **Art 04 Assembly Script:** `python3 tools/assemble_card_system.py` (regenerates `V1/04___Card_System.md` — a generated build artifact, not source of truth — from the 8 Part files, for legacy analysis scripts that expect a single file). Run after editing any Part file.
*   **Deployment Script:** `bash tools/deploy_wiki.sh` (runs the local build, syncs `wiki_src/` via `rsync` to the Pi Zero server at `10.0.1.15`, and triggers `mkdocs build` remotely).
*   **Rebuild & Deploy Command:** Run `./tools/deploy_wiki.sh` from the workspace root.

---

## Version Control

This repository uses git. Commit at the close of each design session with a message describing what was decided or completed.

```
session N — [primary decision or milestone]
```

The `/Retired` folder is tracked in git for historical reference but should not be edited. The `/Session` folder is tracked; `PRIVATE___True_State.md` should remain in `.gitignore` if distributed to collaborators.

