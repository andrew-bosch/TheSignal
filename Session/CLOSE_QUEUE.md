## CLOSE QUEUE — Session 117
## Execute every instruction in order. No interpretation. Delete this file last.

### EDIT
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
OLD: **Last Updated:** 2026-06-21 — Session 112 Close
NEW: **Last Updated:** 2026-06-24 — Session 117 Close

### APPEND
FILE: /home/abosch/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md
AFTER: **Last Updated:** 2026-06-24 — Session 117 Close
CONTENT:

### Session 117 Summary (2026-06-24)

**Focus:** DB prep for card set audits — card_status taxonomy columns + card_subject_map bridge table.

**Key work:**
- **card_status extended** — 4 new columns: `layer` / `function` / `subject` (VARCHAR) / `beat` (INT, NULL). Taxonomy seeded from Art 04 §8; 77 of 95 cards have spec-accurate values (Python parser vs. full card specs); 18 stubs/BLOCKED have §8-level accuracy only.
- **Beat semantics locked:** Resolution beat, not submission beat. 27 CA=2 (early-intervention: block/protect/modify/interfere), 35 CA=3 (standard covert grid), 27 PA=4, 6 MOD/DA=NULL.
- **Data corrections:** 15 NULL card_ids backfilled (pre-ID-04 renumber); 3 card_type bugs fixed (Regulatory Downgrade/Freeze CA→PA, Accord Leverage CA→MOD).
- **component table renames:** id=1 "Presence chip" → "Presence token" · id=14 "Political act" → "Public act".
- **card_subject_map created** — 25-row bridge table (subject PascalCase → component_id); enables joins from card_status into all 27 gap views via component table.
- **§9 Coverage Matrix** — now DB-derivable as live pivot from card_status (WHERE blocked=0); no longer a separately maintained table.
- **schema_reference.md updated** — all S117 changes documented.

**Carried to cleanup:** §8 DIR.PA.1 index entry wrong (Submission|Block|PublicAct vs. spec Territory|Modify|PresenceToken) · §9 GHO.PA.2 subject label grouping error.

**Artifacts updated:** DB (card_status columns + card_subject_map + component renames) · schema_reference.md · SESSION_BRIEF

### COMMIT
source ~/Projects/credentials.env && cd ~/Projects/TheSignal && git add -A && git commit -m "session 117 — DB prep: card_status taxonomy + card_subject_map" && git push

### GEM_CONTEXT
/home/abosch/Projects/TheSignal/generate_gem_context.sh

### DELETE
FILE: /home/abosch/Projects/TheSignal/Session/CLOSE_QUEUE.md
