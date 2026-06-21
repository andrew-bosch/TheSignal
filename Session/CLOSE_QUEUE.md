## CLOSE QUEUE — Session 110
## Execute every instruction in order. No interpretation. Delete this file last.

### EDIT
FILE: /home/abosch/Projects/TheSignal/README.md
OLD: **Current phase:** L1 — Paper Prototype (physical-only, no electronics)  
**Active design layer:** `/V1`  
**Design milestone:** Art 03 v4.4 signed off S88 (L207). Art 02 restructured S90 — component content migrated from Art 01; Art 02 sign-off pass (02-n02) next. Art 04 in progress — card design pass complete through C42 + P01–P18; sign-off passes in progress per set.
NEW: **Current phase:** L1 — Paper Prototype (physical-only, no electronics)  
**Active design layer:** `/V1`  
**Design milestone:** Art 03 v4.10 signed off S110 (L232). Art 02 v2.3 signed off S109 (L231). Art 04 in progress — Ghost PA/React design pass complete (GHO.PA.1–5 + GHO.MOD.1); Syndicate gaps next.

### EDIT
FILE: /home/abosch/Projects/TheSignal/README.md
OLD: | 03 | [while session(true): Quarter Structure](<V1/03___Round_Structure___Gameplay.md>) | 4.8 | ✅ Signed off — S104 (L217) |
NEW: | 03 | [while session(true): Quarter Structure](<V1/03___Round_Structure___Gameplay.md>) | 4.10 | ✅ Signed off — S110 (L232). S109–S110: Art 02 DB:48 target-object field (L231); VM-xx lifecycle formalised; §9.2.0 Target Profile placed face-down at PA declaration; §9.4.3.1.1 Target Profile flipped face-up at Apex Check. |

### EDIT
FILE: /home/abosch/Projects/TheSignal/README.md
OLD: | 04 | [Card Set: Action Subroutines](V1/04___Card_System.md) | 0.9.37 | 🔄 In progress — full card design pass complete (C01–C42, P01–P18); set-level sign-off passes in progress |
NEW: | 04 | [Card Set: Action Subroutines](V1/04___Card_System.md) | 0.9.42 | 🔄 In progress — Ghost PA/React design pass complete (GHO.PA.1–5, GHO.MOD.1); set-level sign-off passes in progress |

### EDIT
FILE: /home/abosch/Projects/TheSignal/Whiteboard/ref_procedures.md
OLD: 2. To declare: announce the public act; place card face-up in unresolved PA zone of Faction Resolution Grid with Target Profile and 1 Dispatch Token. Resource tokens remain with the card (not committed until Beat 4).
NEW: 2. To declare: announce the public act; place card face-up in unresolved PA zone of Faction Resolution Grid with 1 Dispatch Token and resource tokens. Place Target Profile **face-down** on the card. Resource tokens remain with the card (not committed until Beat 4).

### EDIT
FILE: /home/abosch/Projects/TheSignal/Whiteboard/ref_procedures.md
OLD: 2. **Apex check / face-down check:** Face-down cards auto-fail.
NEW: 2. **Apex Check (§9.4.3.1.1):** Acting Faction Player flips Target Profile face-up; reads public act card and Target Profile. Face-down PA cards auto-fail (do not flip — they remain face-down and go directly to fail outcome).

### EDIT
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
OLD: **Last Updated:** 2026-06-20 — Session 108 Close
NEW: **Last Updated:** 2026-06-20 — Session 110 Close

### APPEND
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
AFTER: **Last Updated:** 2026-06-20 — Session 110 Close
CONTENT:
### Session 109–110 Summary (2026-06-20)

**Focus:** Ghost PA/React design pass (GHO.PA.3–5 + GHO.MOD.1); Art 03 v4.10 procedural changes (Target Profile face-down model + VM-xx lifecycle).

**Key work:**
- **GHO.PA.3 Declassified Records** ✅ (S109) — Information|Remove|IntelToken (expired). Boost model: expired tokens → BM-xx multiplier ×(1+n). Art 03 §9.4.3.1.0.0 boost detection sub-step added.
- **GHO.PA.4 Public Threat Assessment** ✅ (S109) — Information|Reveal|BroadcastEffectCard. Automatic; GR 10.1b obligates ARBITER reveal. Art 02 DB:48 target-object field added. Art 03 §9.4.3.3.0 / §9.4.3.1.3 clauses added.
- **GHO.MOD.1 Clarify Misinformation** ✅ (S110) — Redesigned from GHO.PA.5 seed → ModifierCard/React. Information|Remove|IntelToken. Trigger: any PA placed with Intel token at §9.2.0. Prediction resolution — Ghost declares faction named on token; correct → PA cancelled, resources drained to Reservoir, Ghost +1 PS. Intelligence-gated: Target Profile face-down at §9.2.0 means Ghost must have prior SIGINT to fire reliably.
- **GHO.PA.5 Agency Recruitment Fair** ✅ (S110) — Territory|Add|PresenceToken. Renumbered from PA.6 (PA.5 slot vacated by MOD.1 redesign). Cost: 1 Findings. Restriction: district.resource_type == Findings (University Perimeter, Data Exchange, Research Institute, Chorus Research). Success: +2 chips. Successcrit +1 PS / Failcrit −1 PS. Ring3 +10 / Ring1 −15.
- **Art 03 v4.10 signed off** (L232, S110) — §9.2.0 Target Profile placed face-down at PA declaration; §9.4.3.1.1 (Apex Check) Target Profile flipped face-up. VM-xx lifecycle formalised: §9.4.1.1 BEC step extended; §9.4.2.2.0 VM-xx placement clause; §9.4.3.1.3 per-PA BEC check; §9.4.3.3.0 generic VM-xx placement. STD.PA.4 + STD.PA.5 arbiter_notes corrected (Phase B → §9.2.0/§9.4.3.1.1). Folded into existing L232 sign-off.
- **Art 02 v2.3 signed off** (L231, S109) — DB:48 Target Profile target-object field added.
- Art 04b §5.2/§7/§8.1 updated: GHO.PA.5 + GHO.MOD.1 added to coverage table and matrix.

**Decisions locked:** L232 (Art 03 v4.10 — Target Profile face-down + VM-xx lifecycle) · L231 (Art 02 v2.3 — Target Profile target-object field)

**Artifacts updated:** Art 03 (v4.10 ✅ L232) · Art 02 (v2.3 ✅ L231) · Art 04 (v0.9.42) · Art 04b (§5.2/§7/§8.1) · ref_procedures.md · README

**Next (S111 Tier 1):** Syndicate gaps — Information|Corrupt|AccordAgreement · Information|Reveal|IntelTokensHeld · Accord Transfer (L227, gate: Art 06)

### COMMIT
source ~/Projects/credentials.env && git -C ~/Projects/TheSignal add -A && git -C ~/Projects/TheSignal commit -m "session 110 — Ghost PA/React design pass complete (GHO.PA.3–5, GHO.MOD.1); Art 03 v4.10" && git -C ~/Projects/TheSignal push

### GEM_CONTEXT
/home/abosch/Projects/TheSignal/generate_gem_context.sh

### DELETE
FILE: /home/abosch/Projects/TheSignal/Session/CLOSE_QUEUE.md
