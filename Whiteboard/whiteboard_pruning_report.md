# Whiteboard Pruning Report & Archival Plan

This report provides a systematic audit and recommendations for pruning the `/Whiteboard` directory of **The Signal** to address file bloat. Whiteboard files are intended as scratchpads for active work, but the accumulation of stale summaries, historical proposal drafts, and completed session logs has created a maintenance burden and a source of context bleed or hallucinations for AI design agents.

## Executive Summary & Strategy

Our review of the 33 files in `/home/abosch/Projects/TheSignal/Whiteboard/` reveals three distinct categories of content:
1. **Duplicate or Asset Files (2 files):** Files that are identical copies of active files already stored in canonical paths (like `/V1`).
2. **Stale References & Historical Drafts (29 files):** Content that has been fully integrated into active artifacts, completed session logs, or reference sheets that have drifted out of sync with the canonical rules.
3. **Active Concepts & Future Drafts (2 files):** Scratchpads containing valuable design work for upcoming phases (like Modifier Cards or Covert Messaging) that have not yet been integrated into canonical artifacts.

### The Core Recommendation: Retain Canonical SOT, Prune Summaries
The ten `ref_` files (e.g., `ref_resources.md`, `ref_procedures.md`) and their associated audit reports are particularly problematic. As identified in the overnight audits (`ref_audit_overnight_results.md`), these summaries contain numerous severe contradictions, inaccuracies, and missing rules compared to the canonical V1 documents (like `00a___Governing_Rules___Design_Policy.md`). 

We recommend **archiving all stale references and completed drafts** to a dedicated historical directory (e.g., `Retired/Whiteboard_Archive/`) and relying solely on the canonical V1 files as the source of truth (SOT). This eliminates dual-maintenance overhead and prevents context drift.

---

## Pruning Recommendations Ledger

The table below lists all 33 whiteboard files, their origin, current status, and recommended action.

| File Name | Size (Bytes) | Origin / Session | Status | Recommendation | Rationale & Integration Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Active Concept Scratchpads (Keep)** | | | | | |
| [design_covert_messaging.md](file:///home/abosch/Projects/TheSignal/Whiteboard/design_covert_messaging.md) | 13,796 | S119 (June 2026) | **Active** | **Retain in Whiteboard** | Active design stub for the messaging system. Needs to remain until the `Art 06` design pass begins, after which it should be integrated and deleted. |
| [modifier_card_ideas.md](file:///home/abosch/Projects/TheSignal/Whiteboard/modifier_card_ideas.md) | 9,412 | S58 (June 2026) | **Active** | **Retain in Whiteboard** | Contains mechanics, rules, and faction ideas for Modifier Cards. Keep here until the active Modifier Card design phase begins in `Art 04`. |
| **Duplicate Assets (Archive/Delete)** | | | | | |
| `NM.png` | 4,106,564 | - | **Duplicate** | **Delete from Whiteboard** | Identical copy of `V1/NM.png`. No need to retain duplicates of large binary assets. |
| `NM_Overlay.svg` | 9,245 | - | **Duplicate** | **Delete from Whiteboard** | Identical copy of `V1/NM_Overlay.svg`. |
| **Stale Reference Summaries (Archive)** | | | | | |
| [ref_design_pillars.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_design_pillars.md) | 11,255 | S95 (June 2026) | **Stale** | **Archive** | Out of sync with `V1/00a`. Critical design pillars (4.6b to 4.8d) are missing. |
| [ref_resources.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_resources.md) | 4,226 | S95 (June 2026) | **Stale** | **Archive** | Out of sync with `V1/02`. Contains contradictions on Dispatch Token costs and omits passive generation rules. |
| [ref_board_narrative.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_board_narrative.md) | 5,938 | S95 (June 2026) | **Stale** | **Archive** | Out of sync with `V1/01`. Omits `Residential Quarter` geography and adjacency models. |
| [ref_card_types.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_card_types.md) | 8,285 | S95 (June 2026) | **Stale** | **Archive** | Out of sync with `V1/04`. Contains incorrect critical range boundaries and missing design rules. |
| [ref_procedures.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_procedures.md) | 13,299 | S95 (June 2026) | **Stale** | **Archive** | Out of sync with `V1/03`. Contains wrong beat ranges (0–5 instead of 0–4) and obsolete terminology. |
| [ref_taxonomy.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_taxonomy.md) | 9,897 | S95 (June 2026) | **Stale** | **Archive** | Out of sync with `V1/04b`. Entirely omits the vital Layer × Function validity matrix. |
| [ref_world_narrative.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_world_narrative.md) | 7,386 | S95 (June 2026) | **Stale** | **Archive** | Out of sync with `V1/00`. Omits key consensus facts and ARBITER neutrality guidelines. |
| [ref_components.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_components.md) | 3,705 | S95 (June 2026) | **Stale** | **Archive** | 66 of 70 components have zero coverage. Claims components are "not yet designed" when they are. |
| [ref_tracking.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_tracking.md) | 7,925 | S95 (June 2026) | **Stale** | **Archive** | Out of sync. Lists uncalibrated Portrait scores and undocumented initiative triggers. |
| [ref_special_district_and_ring_rules.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_special_district_and_ring_rules.md) | 5,469 | S95 (June 2026) | **Stale** | **Archive** | Out of sync; rules are canonical in `V1/01` and `V1/03`. |
| [design_reference.md](file:///home/abosch/Projects/TheSignal/Whiteboard/design_reference.md) | 7,516 | S76 (June 2026) | **Stale** | **Archive** | Master index pointing to the stale `ref_` files. Stale summary. |
| [design_reference_card_system.md](file:///home/abosch/Projects/TheSignal/Whiteboard/design_reference_card_system.md) | 27,672 | S95 (June 2026) | **Stale** | **Archive** | Out-of-sync cheat sheet. Uses wrong enum names (e.g. `PublicAct`) and lacks checklist constraints. |
| **Audit Reports & Historical Drafts (Archive)** | | | | | |
| [ref_audit_overnight_results.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_audit_overnight_results.md) | 19,058 | S115 (June 2026) | **Completed** | **Archive** | Report identifying gaps in the `ref_` files. Valuable history, but no longer active once references are archived. |
| [ref_audit_results_S113.md](file:///home/abosch/Projects/TheSignal/Whiteboard/ref_audit_results_S113.md) | 10,954 | S113 (June 2026) | **Completed** | **Archive** | Precursor audit report for the `ref_` files. |
| [card_analysis_STD_DIR.md](file:///home/abosch/Projects/TheSignal/Whiteboard/card_analysis_STD_DIR.md) | 28,894 | S121 (June 2026) | **Completed** | **Archive** | Audit report of the Directorate card set. Fully integrated into `V1/04b` (v2.3) in Session 121. |
| [card_analysis_STD_GHO.md](file:///home/abosch/Projects/TheSignal/Whiteboard/card_analysis_STD_GHO.md) | 23,705 | S119 (June 2026) | **Completed** | **Archive** | Audit report of the Ghost card set. Fully integrated into `V1/04b` (v2.2) in Session 120. |
| [card_analysis_STD_GUI.md](file:///home/abosch/Projects/TheSignal/Whiteboard/card_analysis_STD_GUI.md) | 42,100 | S122 (June 2026) | **Completed** | **Archive** | Audit report of the Guild card set. Fully integrated into `V1/04b` (v2.4) in Session 122. |
| [card_analysis_STD_NET.md](file:///home/abosch/Projects/TheSignal/Whiteboard/card_analysis_STD_NET.md) | 34,798 | S123 (June 2026) | **Completed** | **Archive** | Audit report of the Network card set. Fully integrated into `V1/04b` (v2.6) in Session 123. |
| [card_analysis_STD_SYN.md](file:///home/abosch/Projects/TheSignal/Whiteboard/card_analysis_STD_SYN.md) | 28,611 | S123 (June 2026) | **Completed** | **Archive** | Audit report of the Syndicate card set. Fully integrated into `V1/04b` (v2.5) in Session 123. |
| [faction_pentagram_andy.md](file:///home/abosch/Projects/TheSignal/Whiteboard/faction_pentagram_andy.md) | 10,452 | S54 (June 2026) | **Completed** | **Archive** | Original proposal for the faction pentagram. Fully integrated into `V1/00` and `V1/00a` in S54 and S57. |
| [faction_playstyle_S58.md](file:///home/abosch/Projects/TheSignal/Whiteboard/faction_playstyle_S58.md) | 18,088 | S58 (June 2026) | **Completed** | **Archive** | Draft faction playstyle rules. Fully integrated into active cards in `V1/04` and analyzed in `V1/04b`. |
| [gap_card_sketches_S62.md](file:///home/abosch/Projects/TheSignal/Whiteboard/gap_card_sketches_S62.md) | 24,355 | S62 (June 2026) | **Completed** | **Archive** | Initial sketches for gap cards (e.g. Disprove, Disinformation Campaign). Fully designed and added to `V1/04` in S64. |
| [component_metadata_and_database_strategy.md](file:///home/abosch/Projects/TheSignal/Whiteboard/component_metadata_and_database_strategy.md) | 10,620 | S98 (June 2026) | **Completed** | **Archive** | Strategic proposal for database lookup structures. Option A was confirmed and seeded. |
| [deck_composition_draft.md](file:///home/abosch/Projects/TheSignal/Whiteboard/deck_composition_draft.md) | 796 | S31 (June 2026) | **Completed** | **Archive** | A draft snippet from S31. Deck construction rules have not been implemented in V1 this way. |
| [p_series_pass_S63.md](file:///home/abosch/Projects/TheSignal/Whiteboard/p_series_pass_S63.md) | 2,119 | S63 (June 2026) | **Completed** | **Archive** | Design pass notes for the P-series (P01–P18). Fully integrated into `V1/04`. |
| [implementation_plan.md](file:///home/abosch/Projects/TheSignal/Whiteboard/implementation_plan.md) | 2,215 | S48 (June 2026) | **Completed** | **Archive** | Implementation checklist for S48 database cleanup. Long since executed. |
| [walkthrough.md](file:///home/abosch/Projects/TheSignal/Whiteboard/walkthrough.md) | 2,118 | S48 (June 2026) | **Completed** | **Archive** | Verification log for the S48 database cleanup. Historical only. |
| [researchNotes_CardDesign.md](file:///home/abosch/Projects/TheSignal/Whiteboard/researchNotes_CardDesign.md) | 46,154 | S23 (May 2026) | **Completed** | **Archive** | Research report on card design data structures. Findings have been incorporated in the `V1/04` schema. |
| [scratchpad.txt](file:///home/abosch/Projects/TheSignal/Whiteboard/scratchpad.txt) | 5,373 | Pre-AGY CLI | **Stale** | **Archive** | Historical notes regarding older Drive-sync session protocols, superseded by CLI-to-CLI integration. |

---

## Archival Execution Plan

Following your approval of these recommendations, we propose the following steps for implementation (to be carried out in a future turn, as instructed):

1. **Delete duplicate assets:** Remove `NM.png` and `NM_Overlay.svg` from the `/Whiteboard` directory.
2. **Create Archive folder:** Initialize a subdirectory `/home/abosch/Projects/TheSignal/Retired/Whiteboard_Archive/`.
3. **Move files to Archive:** Move the 29 stale reference and historical files listed above into `/Retired/Whiteboard_Archive/`.
4. **Retain in Whiteboard:** Leave only [design_covert_messaging.md](file:///home/abosch/Projects/TheSignal/Whiteboard/design_covert_messaging.md) and [modifier_card_ideas.md](file:///home/abosch/Projects/TheSignal/Whiteboard/modifier_card_ideas.md) in the root `/Whiteboard` directory.

### Preventing Future Whiteboard Bloat

To prevent the whiteboard from cluttering again:
- **Do not write redundant reference summaries:** Direct agents to read the canonical source artifacts directly. If a quick reference is needed, it should be auto-generated programmatically rather than manually written and maintained.
- **Prune on integration:** When a concept or sketch is merged into the V1 artifacts, immediately delete or archive the scratchpad file.
- **Label stubs clearly:** All temporary whiteboard files should begin with a metadata header specifying their status, trigger, and deletion/migration target (as seen in `design_covert_messaging.md`).
