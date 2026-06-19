## CLOSE QUEUE — Session 97
## Execute every instruction in order. No interpretation. Delete this file last.

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: | 02 | Components | 2.1 | ✅ Signed Off — S96 (L212). S96: Grant Deed (DB:113) added §9; §4.1 movement_path field definition clarified (board event trigger, not timing); 13 movement_path timing violations corrected §§5–12. Open PM05: 02-n07, 02-n17, 02-n20, 02-n21, 02-n22. | S88 merge from 02a v1.6 + 02b v1.5.
NEW: | 02 | Components | 2.1 | 🔄 Needs Re-Sign-Off — S97: §13 Physical Action Verb Coverage added (§13.1 verb definitions + §13.2 48-row Component × Verb Matrix; relocated from Art 04b §3.1–3.2). Art 02 is the component source of truth for verb coverage; DB view `v_comp_verb_matrix` is the analytical aggregate. Re-sign-off required (PM05 02-n26 Priority 1). Open PM05: 02-n07, 02-n17, 02-n21, 02-n22, 02-n25, 02-n26. Prior: S96 (L212) — Grant Deed (DB:113) added §9; movement_path corrections. | S88 merge from 02a v1.6 + 02b v1.5.

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: | 03 | while session(true): Round Structure | 4.4 | ✅ Signed Off S88 (L207) |
NEW: | 03 | while session(true): Round Structure | 4.4 | 🔄 Needs Re-Sign-Off — S97: §22 Primitive Action Model & Legalization Analysis added (methodology, trigger taxonomy, gap analysis views, 19-decision S97 legalization table; relocated from Art 04b §3.3). Art 03 is the legality source of truth for subject × verb × component combinations. Re-sign-off required (PM05 03-n24 Priority 1). Prior: S88 (L207). |

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: | 04b | Action Taxonomy & Design Analysis | 1.6 | 🔄 Pending Re-sign-off — S64 | Companion to 04.
NEW: | 04b | Action Taxonomy & Design Analysis | 1.6 | 🔄 Pending Re-sign-off v1.7 — S97: §3 Physical Action Taxonomy relocated (§3.1+§3.2 → Art 02 §13; §3.3 → Art 03 §22; §3 is now pointer section). 04b-12 ✅ S97 · 04b-13 ✅ S97 · 04b-14 ✅ S97 · 04b-15 ✅ S97. 04b-16/17/18/19 queued — gate: Art 02 §13 corrections (02-n26). | Companion to 04.

### APPEND
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
AFTER: | S96 |
CONTENT:
| S97 | 2026-06-18 | agy airlock ingested (5 component registrations: DB:114–118); 02-n20 ✅; Art 02 §10.1 stubs + card_source fields updated. S97 legalization pass: 19 Faction-initiated combinations decided (16 permit / 3 prohibit). 04b-12 ✅ / 04b-13 ✅ / 04b-14 ✅ / 04b-15 ✅. DB-39 ✅ (39 rows seeded post-legalization). Architecture decision: Art 04b §3 Physical Action Taxonomy relocated — §3.1+§3.2 → Art 02 §13 (component source of truth); §3.3 → Art 03 §22 (legality source of truth); §3 now pointer only. PM05 02-n26 + 03-n24 added (Priority 1 — both require re-sign-off). PM02 architecture entry added. ref_taxonomy.md updated. SESSION_BRIEF updated S97. Next: Art 02 §13 corrections + schema integration (02-n26). |

### COMMIT
source ~/Projects/credentials.env && git add -A && git commit -m "session 97 — action taxonomy architecture: §3 → Art 02 §13 / Art 03 §22; 04b-12–15 ✅; legalization pass (19 combos); 02-n26 + 03-n24 Priority 1" && git push

### GEM_CONTEXT
/home/abosch/Projects/TheSignal/generate_gem_context.sh

### PRUNE
FILE: /home/abosch/Projects/TheSignal/Claude_context.md
CONTENT:
# THE SIGNAL — agy Outbound Consulting Report
*Pruned after Session 97. Git history is the archive. Active tasks queued via GEMINI_CONTEXT.md.*

### DELETE
FILE: /home/abosch/Projects/TheSignal/Session/CLOSE_QUEUE.md
