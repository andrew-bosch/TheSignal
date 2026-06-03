## CLOSE QUEUE — Session 66
## Execute every instruction in order. No interpretation. Delete this file last.

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: | 03 | while session(true): Round Structure | 3.1 | ✅ Signed Off — S65 (L185) |
NEW: | 03 | while session(true): Round Structure | 3.2 | ✅ Signed Off — S66 (L186) |

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: Duration taxonomy 5→4 types (Tripwire collapsed into Permanent). Signed off v3.0 (L181). |
NEW: Duration taxonomy 5→4 types (Tripwire collapsed into Permanent). Signed off v3.0 (L181). S65: Beat 0 Retained validation; Beat 2 Golden Parachute bribe procedure; Beat 3 partial payment marker source. Signed off v3.1 (L185). S66: Beat 2 pre_loss_calc block removed (schema addition predated sign-off). Signed off v3.2 (L186). |

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: | 04 | Card System | 0.9.27 (S65) |
NEW: | 04 | Card System | 0.9.28 (S66) |

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: 04-n23 added. Next: 04-n23; C-series re-sign-off; 04-n18. |
NEW: 04-n23 added. Next: 04-n23; C-series re-sign-off; 04-n18. S64: gap card specs complete (Disinformation Campaign, Standing Injunction, Disprove, Intel Extraction, Modifier Raid). Art 04b §5.2 +5 rows. S65: §6.2 cost field redefined (fungible only). §6.6 Expression Parameters added (pre_loss_calc). C37 Sacrifice v1.1 (cost=None; PS in success). C34 Golden Parachute v2.0 (bribe mechanic; retained payment). v0.9.27. S66: Entry/Exit Controls redesigned v2.0 (district target; permanent deployment marker block; persistence_condition). §6.6 removed. persistence_condition added to §6.1/§6.2. C37 affinity=None. 04-n25 closed. 04-n29 + 04-n30 added. v0.9.28. |

### EDIT
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
OLD: **Last Updated:** 2026-06-03 (S65)
NEW: **Last Updated:** 2026-06-03 (S66)

### APPEND
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
AFTER: **Next session:** 04-n25 remaining: `target_ring` (Entry/Exit Controls — needs Art 01 ring-scope definition + §6 field). Then 04-n26 → 04-n27 → 04-n28.
CONTENT:

## Session 66 — 2026-06-03

**Focus:** 04-n25 completion; Entry/Exit Controls full redesign

**Accomplished:**
- Entry/Exit Controls redesigned v2.0 — district target (not ring); permanent deployment marker placement block; non-Directorate markers displaced to any district where faction has presence (Blocked face); persistence_condition auto-discard when Directorate loses Established; PS −1; card sits in Directorate's PA area on the Overview
- Art 04 §6.1/§6.2: persistence_condition field added (BoolExpr | None — card discarded immediately when evaluates False)
- Art 04 §6.6 Expression Parameters removed — pre_loss_calc was added ahead of card sign-off; schema additions must follow sign-off
- Art 03 v3.2 signed off (L186) — Beat 2 pre_loss_calc block removed
- C37 Sacrifice: affinity=None (stale field on a cost=None card)
- 04-n25 ✅ fully closed (all 3 items: target_ring moot; pre_loss_calc orphaned+removed; PS-as-cost already fixed in S65)
- PM05: 04-n29 added (counter-card design + Art 03 persistence monitoring); 04-n30 added (persistence_condition sweep on all card specs)
- Entry/Exit Controls: design pass ✓; Issues Resolved blocked by 04-n29 and no-presence-elsewhere edge case

**L-decisions this session:**
- L186: Art 03 v3.2 signed off. Beat 2 pre_loss_calc procedure block removed (C34 uses game.bribe(); no card uses pre_loss_calc). Art 04 §6.6 removed. Schema additions must follow card sign-off.

**Next session:** 04-n26 (component interaction design pass).

### COMMIT
source ~/Projects/credentials.env && git add -A && git commit -m "session 66 — 04-n25 closed; Entry/Exit Controls v2.0; Art 03 v3.2 (L186)" && git push

### GEM_CONTEXT
/home/abosch/Projects/TheSignal/generate_gem_context.sh

### DELETE
FILE: /home/abosch/Projects/TheSignal/Session/CLOSE_QUEUE.md
