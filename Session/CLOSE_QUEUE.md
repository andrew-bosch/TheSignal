## CLOSE QUEUE — Session 46
## Execute every instruction in order. No interpretation. Delete this file last.

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: | 04b | Action Taxonomy & Design Analysis | 1.2 | ✅ Reference Document — Active | Companion to 04. Category/Function/Subject taxonomy framework (L136 rename). Coverage gap analysis, faction design recommendations. Subject values updated: Presence → Presence token/Operational marker (L109); C35 → Named action type. Chorus Portrait retired (L84). Ghost doctrine gap flagged. Session 28: §10 added — Pass, Modifier, Emergency Response explicitly excluded from taxonomy as standalone card types. Not playtest-blocking. |
NEW: | 04b | Action Taxonomy & Design Analysis | 1.3 | ✅ Reference Document — Active | Companion to 04. S46: §4 redesigned — physical action taxonomy replaces category/function table. 7 verbs (Add, Remove, Move, Reveal, Conceal, Flip, Corrupt); 25-component × verb matrix sourced from the_signal_db.v_comp_verb_matrix. §3 cleanup pending (04b-04); sign-off pending. Coverage gap analysis, faction design recommendations in §6–§8. |

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM05___Active_Punch_List.md
OLD: **Version:** 2.9
NEW: **Version:** 3.0

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM05___Active_Punch_List.md
OLD: | 04b-03 | **Action Taxonomy Audit — prerequisite to Art 04 continuation (C16+).** Audit Art 04b against the full component set established by Art 01 overhaul to confirm: (1) every known component is accounted for — districts, presence tokens, deployment markers, structure blocks, established markers, control flags, tension markers, dispatch tokens, intel notes, faction Terminals, faction screens, Ring Modifier decks, Session Timeline, Situation Report zone, ARBITER screen, status markers, initiative strips, dispatch cases; (2) for each component, actions that are mechanically possible vs. mechanically valid against it are mapped; (3) "force reveal" action class (L154) — compelling a faction to expose Terminal contents — is added as a named action type with Ghost-primary and cross-faction applicability noted. Art 04b re-sign-off required if taxonomy changes are material. Run after Art 01 overhaul completes. | Material (audit, may cascade to 04b re-sign-off) | L154, Session 39 | 🔄 |
NEW: | 04b-03 | **Action Taxonomy Audit.** Physical primitive model built in the_signal_db (tmp_ tables). Physical verbs reduced 13→7. Art 04b §4 redesigned S46. Pending: §3 cleanup (04b-04) + sign-off. | Material | L154, Session 39 | ✅ S46 — §4 complete, sign-off pending |

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM05___Active_Punch_List.md
OLD: | DB-11 | **`live_state` → `component_positions` — rename table + rename column + add column (agy).** Three DDL changes in one pass: (1) RENAME TABLE `live_state` → `component_positions`. (2) RENAME COLUMN `anchored_to_component_id` → `on_component_id`, change constraint NOT NULL → NULL (FK → components.id unchanged). (3) ADD COLUMN `on_game_zone_id` (bigint, NULL, FK → game_zones.id). Spec: 00b §8. Unblocked S45 after 00b-05 spec complete. | Non-material (DDL) | L156, S45 | 🔄 |
NEW: | DB-11 | **`live_state` → `component_positions` — rename table + rename column + add column (agy).** Three DDL changes in one pass: (1) RENAME TABLE `live_state` → `component_positions`. (2) RENAME COLUMN `anchored_to_component_id` → `on_component_id`, change constraint NOT NULL → NULL (FK → components.id unchanged). (3) ADD COLUMN `on_game_zone_id` (bigint, NULL, FK → game_zones.id). Spec: 00b §8. Unblocked S45 after 00b-05 spec complete. | Non-material (DDL) | L156, S45 | ✅ S46 confirmed — agy executed |

### APPEND
FILE: /home/abosch/Projects/TheSignal/V1/PM05___Active_Punch_List.md
AFTER: | 04b-03 | **Action Taxonomy Audit.** Physical primitive model built in the_signal_db (tmp_ tables). Physical verbs reduced 13→7. Art 04b §4 redesigned S46. Pending: §3 cleanup (04b-04) + sign-off. | Material | L154, Session 39 | ✅ S46 — §4 complete, sign-off pending |
CONTENT:
| 04b-04 | **Art 04b §3 cleanup — prerequisite to v1.3 sign-off.** Update stale verb references throughout §3: Block→Flip, Redirect→Move, Recover→Move, Modify→Corrupt/Reveal. Note React reclassification: React is a modifier card mechanic (timing/interrupt layer), not an action taxonomy verb — remove §3.5 rationale or reframe. Remove §3.3 (Protect) — Protect collapsed into Move. Update §3.4 Corrupt targets to confirm Intel token + Accord agreement (both transform_data=1 in DB). | Non-material (cleanup) | S46 | 🔄 |
| DB-14 | **Decision — promote tmp_ taxonomy tables to permanent the_signal_db schema.** S46 built design workspace tables: tmp_component, tmp_verb, tmp_action, tmp_subject_target, tmp_category, tmp_type, tmp_legal; views: v_object_from, v_validact, v_placement_matrix, v_comp_verb_matrix. Decision: keep as tmp_ (design workspace), promote to permanent (remove tmp_ prefix), or archive DDL and drop. Evaluate after Art 04b sign-off. Also: delete unused tables (tmp_category, tmp_type, tmp_legal — predates S46 primitives work). | Design decision | S46 | 🔄 |
| 04-52 | **Modifier token Beat 4 disposition undefined.** In 03.11 Beat 2, ARBITER places modifier tokens on submitted Covert operation and Political act cards. Beat 3: tokens return to Arbiter Tableau pool. Beat 4: modifier tokens are used but no return-to-pool step is specified. Confirm disposition: return to pool, spent/discarded, or other. Resolve during Art 03 Beat 4 review or Art 04b §3 cleanup. | Design decision | S46 | 🔄 |
| 04-53 | **React card reclassification.** React reclassified S46 as a modifier card mechanic (timing/interrupt), not an action taxonomy verb. Cards currently tagged Action — React (including C12 Materials Acquisition) need new primary taxonomy assignments. Audit §5 Card Taxonomy Index for all React-tagged cards; assign replacement Category — Function. | Non-material (taxonomy sync) | S46 | 🔄 |
| 04-54 | **Modifier card 8 deck types.** Art 04 card schema must distinguish: Ring 1, Ring 2, Ring 3 modifier decks + 5 faction-specific modifier decks (1 per faction). Physical taxonomy uses single "Modifier card" component type — distinction is a card design attribute. Add deck_type field to modifier card schema when Art 04 modifier card section is designed. | Non-material (schema) | S46 | 🔄 |
| 04-55 | **Create card design reference doc in Whiteboard/.** ~/Projects/TheSignal/Whiteboard/ is currently empty. Before the next Art 04 design session, create a working reference doc (card_design.md or equivalent) to capture in-progress card design decisions as a session scratchpad before migration to Art 04. | Reference | S46 | 🔄 |
| DB-15 | **Beats layer — extend tmp_ taxonomy model.** S46 identified that cross-referencing valid beats (Beat 1–4 of 03.11) against the component × verb matrix would reveal design patterns (e.g., Flip is Beat 1, Protect/Move is Beat 2, modifier token return is Beat 3). Extend model with beat validity dimension after Art 04b is signed off and tmp_ table permanence is decided (DB-14). | Design model extension | S46 | 🔄 |

### APPEND
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
AFTER: ### Session 45 Summary — 2026-05-27
CONTENT:

---

### Session 46 Summary — 2026-05-28

**Focus:** 04b-03 action taxonomy audit — complete. Physical action primitive model built in the_signal_db.

**Decisions locked:** None.

**Artifacts changed:**
- Art 04b v1.3 — §4 redesigned: physical action taxonomy replaces category/function table. §4.1: 7 verbs (Add, Remove, Move, Reveal, Conceal, Flip, Corrupt) with primitive definitions. §4.2: 25-component × verb matrix (source: the_signal_db.v_comp_verb_matrix). Version bumped 1.2→1.3. Sign-off pending (§3 cleanup required first — 04b-04).
- SESSION_BRIEF — updated to S46.
- PM03 — 04b row updated to v1.3.
- PM05 v3.0 — 04b-03 ✅; DB-11 ✅ confirmed; new items: 04b-04, DB-14, 04-52 through 04-55.

**DB work (the_signal_db, tmp_ tables — not artifact changes):**
- tmp_component: 38 rows total, 25 actionable. New: Modifier token, Target Profile, ARBITER Dominance Marker. Schema: transform_type ENUM replaced by transform_visibility/transform_orientation/transform_data booleans.
- tmp_verb: 7 verbs (reduced from 13). Removed: React, Copy, Remove Restriction, Recover, Modify, Protect, Block, Shift, Redirect. Added: Conceal, Flip, Move.
- v_validact: 119 rows (subject × action × target).
- v_comp_verb_matrix: 25 components × 7 verbs — source of Art 04b §4.2.

**PM05 changes:** 04b-03 ✅, DB-11 ✅ confirmed, 04b-04 new, DB-14 new, 04-52 through 04-55 new.

### COMMIT
source ~/Projects/credentials.env && git -C /home/abosch/Projects/TheSignal add -A && git -C /home/abosch/Projects/TheSignal commit -m "session 46 — 04b-03 audit complete; §4 redesigned as physical action taxonomy; 7 verbs; 25-component matrix" && git -C /home/abosch/Projects/TheSignal push

### GEM_CONTEXT
/home/abosch/Projects/TheSignal/generate_gem_context.sh

### DELETE
FILE: /home/abosch/Projects/TheSignal/Session/CLOSE_QUEUE.md
