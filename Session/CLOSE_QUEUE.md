## CLOSE QUEUE — Session 75
## Execute every instruction in order. No interpretation. Delete this file last.

### EDIT
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
OLD: **Last Updated:** 2026-06-09 — Session 74
NEW: **Last Updated:** 2026-06-09 — Session 75

### APPEND
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
AFTER: ## Session 68 — 2026-06-05
CONTENT:

## Session 75 — 2026-06-09

**Focus:** XA-46/47/48 — rule ID sweep and Art 04 card design constraints migration

**Accomplished:**
- XA-47 ✅ — Art 04 §5 P19–P25 added (card design constraints migrated from former 00a §7: P19 effect duration types, P20 partial payment, P21 crit cost, P22 portrait card property, P23 ring modifier scope, P24 corrupt scope, P25 standard language conventions). P5 updated with authoritative R26 constraint note. P6 cross-ref to P19. Checklist rows updated (Effect duration → P6/P19; Portrait validity → +P22). Art 04 v0.9.34.
- XA-48 ✅ — Art 07 §9 already contained all four ARBITER registers in full; `00a R02` source ref removed from §9; item closed.
- XA-46 ✅ — ~120 rule ID substitutions across 11 files. All old `00-Rnn` / `00a Rnn` / bare `Rnn` references replaced with contextual labels (Governing Rule n.n, Design Pillar 4.n, Art 04 §5 Pn, Art 03). Files swept: Art 03, Art 04, Art 07, 02a, 02b, PM03, gap_card_sketches, design_reference.md, memory files. PM02 + SESSION_BRIEF preserved as historical records. `00-R29` (Ghost adjacency, PM05 04-n6) flagged `Design Pillar [04-n6 pending]`. Zero `00-R` strings remain across all swept files.
- PM05: 04-n73 (P1–P18 restatement audit), XA-49 (design_reference.md reset) added. XA-46/47/48 marked ✅.

**L-decisions this session:** None (all work non-material).

**Next session:** XA-49 (design_reference.md reset) → 04-n28 (Overture full spec, gates §11) → 04-n40 (C28 Network replacement)

---

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: | 04 | Card System | 0.9.33 | 🔄 In Progress |
NEW: | 04 | Card System | 0.9.34 | 🔄 In Progress |

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: Signals Analysis BLOCKED (Art 06.x). 04-n48 substantially complete. |
NEW: Signals Analysis BLOCKED (Art 06.x). 04-n48 substantially complete. S75: §5 P19–P25 added (card design constraints from 00a §7 — XA-47 ✅). XA-46 rule ID sweep applied. v0.9.34. |

### COMMIT
source ~/Projects/credentials.env && git add -A && git commit -m "session 75 — XA-46/47/48 rule ID sweep complete; Art 04 §5 P19–P25 added" && git push

### GEM_CONTEXT
/home/abosch/Projects/TheSignal/generate_gem_context.sh

### DELETE
FILE: /home/abosch/Projects/TheSignal/Session/CLOSE_QUEUE.md
