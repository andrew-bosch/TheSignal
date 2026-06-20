## CLOSE QUEUE — Session 106 (includes deferred S105 tasks)
## Execute every instruction in order. No interpretation. Delete this file last.

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: | 04b | Action Taxonomy & Design Analysis | 1.7 | 🔄 Pending Re-sign-off (04b-19)
NEW: | 04b | Action Taxonomy & Design Analysis | 1.7 | ✅ Signed Off S105 (L221)

### EDIT
FILE: /home/abosch/Projects/TheSignal/V1/PM03___Master_Artifact_Index.md
OLD: | 04 | Card System | 0.9.37 |
NEW: | 04 | Card System | 0.9.41 |

### EDIT
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
OLD: **Last Updated:** 2026-06-19 — Session 104 Close
NEW: **Last Updated:** 2026-06-19 — Session 106 Close

### APPEND
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
AFTER: **Next (S105 Tier 1):** Verify agy completions against live DB and schema_reference.md → ID-04 (full card renumber — new session, large sweep) → Art 04b v1.7 sign-off (04b-19, gated on ID-04).
CONTENT:

---

### Session 105 Summary (between sessions — agy + Claude)

**Focus:** ID-04 full card renumber; Art 04b v1.7 sign-off (L221).

**Key work:**
- agy between-session: ID-01 ✅ (G-ext retired from card_ref), ID-02 ✅ (DebriefActionCard/Grant Deed reclassified), ID-03 ✅ (faction pool faction associations added), ID-05 ✅ (23 DB scripts converted to idempotent), ID-SCHEMA ✅ (L219 documented in schema_reference.md).
- ID-04 ✅ — [FAC].[TYPE].n format applied across Art 04 (678 substitutions), Art 04b (201 substitutions), card_ref DB (27 rows). card_id field added to Art 04 §6.1/§6.2.
- L221: Art 04b v1.7 signed off. §§6/7/8 are living sections — update as gap cards designed, no re-sign-off gate.

**Next (S106):** Card design pass — faction gaps per 04b §8.

---

### Session 106 Summary (2026-06-19)

**Focus:** Card design pass (Directorate, Network, Guild gaps); taxonomy audit finding.

**Key work:**
- DIR.CA.6 Institutional Audit ✅ — Economy|Add|NativeResource(Mandate). Ring Permanent count yield; chip count > 1 restriction.
- DIR.CA.7 Institutional Brief ✅ — Standing|Shift|PublicStanding. Same ring Permanent architecture; PS yield.
- DIR.CA.8 Enhanced Scrutiny ✅ — Resolution|Modify|Difficulty. Beat 2 Automatic; −15 Modifier tokens on all Beat 3 rows in target district; all factions.
- NET.CA.7 Ground Signal ✅ — Standing|Shift|PublicStanding. IL ≤ Established restriction; success +1 PS; successcrit +1 chip + +1 PS.
- NET.MOD.1 Signal Break ✅ — Territory|Add|PresenceToken React Modifier (card_id confirmed). Trigger = PA success causing board state change. Exposure×1; d100 threshold 50.
- GUI.MOD.1 Return to Site stub — Territory|Add|PresenceToken React (formerly Territory|Recover|PresenceToken).
- GUI.CA.6 Labor Contract — card_id GUI.CA.6 assigned (L219).
- **Recover function retired from Art 04b** (04b-20 ✅): 00a 7.2b prohibits retroactive board state reversal — Recover is not a distinct primitive; always resolves to Add + forward action context. GUI.CA.2 and GUI.CA.6 reclassified to Economy|Add|NativeResource. Field Verification BLOCKED (mechanic alters committed token age field — 7.2b violation; fundamental redesign required). L218 annotated in PM02 as consequence of 7.2b, not standalone decision.
- PM05: 04-n101 updated; 04-n102 (Modifier card schema); 04-n103 (Recover Art 04 spec fixes — open); 04b-20 ✅.
- Art 04 v0.9.41 Draft. Art 04b §4/§5.2/§6/§7/§8.3/§8.5 updated.

**Next (S107 Tier 1):** Full 04b audit against 00a — sweep all taxonomy functions/verbs against governing rules before continuing card design pass.

### COMMIT
source ~/Projects/credentials.env && git -C ~/Projects/TheSignal add -A && git -C ~/Projects/TheSignal commit -m "session 106 — card design pass (DIR/NET/GUI); Recover retired from taxonomy (7.2b)" && git -C ~/Projects/TheSignal push

### GEM_CONTEXT
/home/abosch/Projects/TheSignal/generate_gem_context.sh

### DELETE
FILE: /home/abosch/Projects/TheSignal/Session/CLOSE_QUEUE.md
