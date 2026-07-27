# THE SIGNAL — Session Brief
**Session 150 next | Updated: 2026-07-27**
**Session start:** TBD

Lean startup document. Full session history: `Session/THE_SIGNAL___Project_Save_State.md`

---

## Read These First — Every Session

**Before any design, procedure, or card work:**
- `Whiteboard/design_reference.md` — governing principles, card design rules, schema discipline
- `Whiteboard/design_reference_card_system.md` — Art 04 schema, enums, field conventions
- `Whiteboard/ref_*.md` — pick files relevant to the task (procedures, taxonomy, tracking, card types, components, resources, board narrative)

Terminology, methodology, governing rules, and registered decisions live in those files. Do not rely on SESSION_BRIEF for any of that.

**Art 04–09 card work:** Also read `Whiteboard/modifier_card_ideas.md` (if modifier design) or `Whiteboard/gap_card_sketches_S62.md` (if gap card work).

**Art 04 file location (S136):** Card content is split across 8 files — `04___Card_System___Part1_Core.md` (§1–6, §8–15), `Part2_Standard.md`, `Part3_Ring_Modifiers.md`, `Part4a_Guild.md`–`Part4e_Syndicate.md`. Edit these directly. `04___Card_System.md` is a generated build artifact (`tools/assemble_card_system.py`) — never edit it, regenerate it after any Part edit.

**Card design content must stand on its own (locked S142, PM02 L276):** Design Rationale/design_note/arbiter_note must never reference or compare against other cards for explanation — cards are self-contained. A separate strategy-guide artifact is the right home for cross-card comparison, if ever wanted. Checklist Notes: ✓ rows get only the pass-justification (no session numbers, no log-item citations); ⚠ rows describe the issue itself; detailed issues go in an Outstanding Issues section below the checklist, not the Note cell. Python `Card()` blocks carry zero commentary except a short `# scaffolded, not addressed` marker on genuinely-unaddressed placeholder fields. Full-corpus retroactive sweep (CA phase + all 3 modifier subclasses) tracked at PM05 04-n180 — not started.

---

## Startup Delivery

After reading context files, deliver to Andy:
1. **Last session accomplishments** — summarize from "S[N] Accomplishments" below
2. **Current focus** — list open tracks from "Current Focus" below
3. **Pending sign-offs** — list from "Pending Sign-offs" below

Then prompt: *"What's our focus today?"*

---

## S149 Accomplishments (closed)

**Art 02 re-signed off (PM02 L326), 04-n197 closed.** Andy reviewed the Target Profile amendment (PM02 L317, §8 Gameplay Requirements) and confirmed the copy as-is.

**Schema Cleanup Program — Phases 3 and 4 of 5 closed (PM05 04-n191).**
- **Phase 3 (04-n194) ✅ (PM02 L327/L328)** — 4/7 legacy pre-S127 cards fixed with direct vocabulary swaps: GHO.MOD.5, NET.MOD.9, NET.MOD.2, SYN.MOD.9. Remaining 3 (GHO.MOD.1, NET.MOD.1, NET.MOD.8) had no confirmed-vocabulary drop-in — folded into Phase 4.
- **Phase 4 (04-n195) ✅ (PM02 L329–L332)** — 9 of 12 decision-batch items ruled and executed. New §6.3 vocabulary: `board_state.changed(component=, change=, cause=, faction=, district=, ring=)` — a general-purpose TriggerExpr primitive for cards needing more than one component type or direction of change, added specifically for GHO.MOD.1/NET.MOD.1/NET.MOD.8; `cause=` added after catching that the primitive's first draft silently widened NET.MOD.1's trigger past its original PA-only scope. **Art 03 §18.2.2 added and signed off (v4.13→v4.14, PM02 L332)** — React cards are permanently removed from the game by default once resolved unless card text states otherwise; this rule existed nowhere in writing before this session. DIR.CA.8/GUI.CA.9/GHO.CA.15 Subject taxonomy reclassified off the invalid "Difficulty" term (`card_subject_map` DB synced, re-verified against `v_card_mechanical_alignment`). GHO.CA.8 normalized to the schema's `boost=` field. 3 items scoped as follow-ups rather than executed: **04-n199** (Portrait `flat=`/`submitter=`, both patterns), **04-n200** (`where()` TriggerExpr vocabulary — reopened for a second look, not settled), **04-n201** (`game.active_permanents` — flagged for deeper review). New finding, not fixed: **04-n202** (DIR.CA.5 has the same invalid `-=`/`+=` statement-as-value defect as the already-closed #17; corpus-wide grep for more instances hasn't run).
- **Phase 5 (04-n196)** — content-fix sweep, not started. Next in sequence.

**Hygiene recurrence #6 (feedback_artifact_hygiene.md updated with the failure-mode diagnosis).** Introduced session-tag/log-citation provenance into artifact prose at scale (~12 instances across 16 cards) during Phase 4 execution — caught via an advisor review pass after declaring the work done, not proactively. Stripped; all provenance now lives in PM02 only. Memory updated: having read the rule at boot didn't prevent the violation, because the impulse to cite fires while writing an edit, not when recalling the rule abstractly — the fix logged is a mechanical grep pass over touched files before calling a batch done, not another re-read of the rule.

---

## Current Focus (S150)

**PRIMARY WORK — Schema Cleanup Program continues.** Next up per the locked sequencing (PM02 L316):
- **Phase 5 (04-n196)** — content-fix sweep: stub rewrites, prose/code mismatches, missing fields (#25/29/31/35/36/38/39/44). Heaviest lift, run last. Not started.
- Held back, not yet actionable: #23 (doctrine-penalty portrait coverage) — still evidence-gathering.

**4 items spun off Phase 4, need attention before or alongside Phase 5:**
- **04-n199** — Portrait `flat=`/`submitter=` fix on SYN.CA.7/10/11/12/PA.3, plus a corpus-wide audit for other target-faction `flat=` instances.
- **04-n200** — `where(BoolExpr)` TriggerExpr vocabulary, reopened — Andy flagged his initial "don't confirm" read needs a second look.
- **04-n201** — `game.active_permanents(faction=,ring=)` (DIR.CA.6/CA.7/PA.9) flagged for deeper review, not ruled on.
- **04-n202** — DIR.CA.5 has the same invalid `-=`/`+=` statement-as-value defect as the already-closed #17; corpus-wide grep for more instances hasn't run.

**Open threads needing a look next session:**
- **PM05 04-n198** — pre-existing session-tag citations on `✓` checklist rows, corpus-wide sweep not started.
- **agy/lev split** — waiting on lev's reply to the "drop brain's local clone" proposal; PM02/PM05 MariaDB migration script not yet written, dry-run pending.

**Carried, untouched multiple sessions:**
- Add-vs-Redirect mis-tag sweep — other `Territory/Add/PresenceToken`(or `StructureBlock`) cards, same pattern found on SYN.CA.9 (S144)
- `target`-field semantics audit (self-cost/delivered-value gap, S144) — `SYN.PA.1` Acquisition Offer still carries this unresolved gap
- 04-n177's expanded scope; `ref_board_narrative.md` sync pass; smaller carried backlog (04-n163/164/166/167/168/148/150/26/27/126/123, XA-54, 06-n01)

**After Art 04 initial sign-off — not yet actionable:**
- PM05 04-n184 — deck copy-count / draw-probability audit. Sequence once unblocked: (1) redo per-faction + cross-faction card space audits first (S119–128 style), (2) only then run copy-count/probability against the refreshed picture. Suspected outcome: all 3 ring-modifier decks may need retuning.

---

## Pending Sign-offs

- **Art 04** — Draft, gated on the Schema Cleanup Program (Phase 5 remaining) plus the pre-existing card-audit-issue list (mis-tag sweep, target-field audit, 04-n177, board narrative sync, backlog). No set-level sign-off pass starts until the program clears.
- **Art 00a** — v0.12, Signed Off.
- **Art 02** — v2.5, Signed Off.
- **Art 03** — v4.14, Signed Off.
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).

*Card-level sign-offs gated behind set-level audits — not actionable until those gates clear.*
