## CLOSE QUEUE — Session 112
## Execute every instruction in order. No interpretation. Delete this file last.

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/04___Card_System.md
OLD: **Version:** 0.9.42 Draft
NEW: **Version:** 0.9.43 Draft

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: | 04 | Card System | 0.9.42 | 🔄 In Progress | S111:
NEW: | 04 | Card System | 0.9.43 | 🔄 In Progress | S112: GHO.CA.7 Station / GHO.CA.8 Full Take / GHO.CA.9 SCIF / GHO.CA.10 Flip / GHO.CA.12 Source Substitution — Issues Resolved ✓ S112; Source Substitution redesigned (Automatic re-key; plant mode retired). 04-n6 adjacency restriction added to field collection ops (Station/Full Take/Flip). v0.9.43. S111:

### EDIT
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
OLD: **Last Updated:** 2026-06-21 — Session 111 Close
NEW: **Last Updated:** 2026-06-21 — Session 112 Close

### APPEND
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
AFTER: **Last Updated:** 2026-06-21 — Session 112 Close
CONTENT:
### Session 112 Summary (2026-06-21)

**Focus:** Ghost CA design pass — GHO.CA.7/8/9/10/12 Issues Resolved; Source Substitution redesigned.

**Key work:**
- **GHO.CA.7 Station** ✅ (S112) — Information|Add|IntelToken. d100 threshold 55. Sustained collection platform against named faction; 2 tokens on success / +1 on successcrit. Failcrit: NotificationSlip to target. ring_mod {0:−15, 1:−10, 2:0, 3:+10}. 04-n6 adjacency restriction added. Issues Resolved ✓.
- **GHO.CA.8 Full Take** ✅ (S112) — Information|Add|IntelToken. d100 threshold 40. Variable cost n×Findings declared at submission; success = n×2 tokens / successcrit +n / failcrit = NotificationSlip. 04-n6 adjacency restriction added. Issues Resolved ✓.
- **GHO.CA.9 SCIF** ✅ (S112) — Cleanup pass (Issues Resolved was ✓ S94). Faction-targeted; Automatic; no district target; adjacency rule correctly excluded. Card Story updated.
- **GHO.CA.10 Flip** ✅ (S112) — Information|Reveal|IntelToken. Automatic. Cost: 1 Intel token (target-keyed). Success: 2 of target's native resources (copy model — target pool untouched). 04-n6 adjacency restriction added. Issues Resolved ✓.
- **GHO.CA.12 Source Substitution** ✅ (S112) — REDESIGNED. Information|Corrupt|IntelToken. Automatic. Cost = CA slot only. Alters faction_name field on submitted Intel token; ARBITER returns altered token to Ghost's case. Token can then be used on cards restricting Intel token faction to match the target. Plant mode retired — Intel tokens are valid premium currency regardless of faction field; planting a token doesn't trap the recipient. Issues Resolved ✓.
- **PM05 04-n6:** Field collection op adjacency restrictions fully resolved (Station/Full Take/Flip). SCIF and Source Substitution correctly excluded. Remaining sub-items: 00a rule text update + design_reference.md update (deferred).

**Decisions locked:** Source Substitution re-key model (plant mode retired; Automatic; cost = CA slot) · Flip copy model (target pool untouched; Ghost gains 2 native resources)

**Artifacts updated:** Art 04 (v0.9.43 — GHO.CA.7/8/9/10/12 design passes) · PM05 (04-n6 updated) · SESSION_BRIEF · PM03

### COMMIT
source ~/Projects/credentials.env && git -C ~/Projects/TheSignal add -A && git -C ~/Projects/TheSignal commit -m "session 112 — Ghost CA design passes + Source Substitution redesign" && git -C ~/Projects/TheSignal push

### GEM_CONTEXT
/home/abosch/Projects/TheSignal/generate_gem_context.sh

### DELETE
FILE: /home/abosch/Projects/TheSignal/Session/CLOSE_QUEUE.md
