# THE SIGNAL — Session Brief
**Session 149 next | Updated: 2026-07-23**
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

## S148 Accomplishments (closed)

**Schema Cleanup Program (PM05 04-n191, PM02 L316) — Phases 1–2 of 5 closed, priority-blocking all Art 04 work beyond §6 until fully cleared.**
- **Phase 1 (04-n192) ✅** — CostExpr syntax sweep (04-n189, 219 instances, 6 parallel agents to the new canonical bare/dot-chain form); `card_id` backfill (#24, scope grew from 16 Standard cards to 57 corpus-wide, 2 exceptions flagged — Ghost's Backdate/FieldVerification have placeholder IDs); `portrait` empty-value normalized to `None` (#8, 422 vs 89 `{}`, reversed the item's original assumption, §6.1 type updated to `| None`); Outstanding Issues placeholder on 329 cards (04-n190, bare placeholder only). Spun off schema_cleanup_log #50 (Ghost FieldVerification's untyped dual-target cost, folded into Phase 4 as decision 9).
- **Phase 2 (04-n193) ✅** — Required an unplanned full DB restore first: lev's cluster subnet migration wiped `the_signal_db` entirely; restored from the 2026-07-21 backup with Andy's authorization (PM02 L321), every stale `10.0.1.14` reference project-wide repointed to `10.0.0.14`. Reconciliation found 190 mismatches (not ~8) — almost all `design_pass`/`issues_resolved` gone stale corpus-wide. **Andy's ruling: reset `design_pass`/`issues_resolved`/`signed_off` to 0/blank everywhere** (`.md` + DB) — nothing counts as reviewed/resolved/signed-off until schema cleanup finishes and a full design-review re-do happens. 3 genuine DB-stale taxonomy rows synced; corpus baseline now **386** `Card()` blocks (GHO.CA.11 `id=TBD` write-back gap fixed). Full detail: PM02 L322.
- **Phases 3–5 (04-n194/195/196) not started** — legacy vocabulary sweep, decision batch, content-fix sweep.

**Art 00a §10.4 added and signed off (PM02 L324), v0.11→v0.12.** "Covert Attribution Remains Untraceable" — a Covert Operation's effect may be public, its attribution to the acting faction may not be. Surfaced while reviewing agy's memory files ahead of retirement; the principle existed only as an informal note and one mechanical instance (Notification Slip, Art 02 §9), never as a governing rule. Drafted in chat first (Art00a is signed off), Andy reviewed and signed off in the same turn.

**agy retired as a standalone agent; now Claude's subagent (PM02 L321–L325).** Installed and verified `antigravity-for-claude-code` (third-party Claude Code plugin, 201 GitHub stars, MIT licensed) — tested end-to-end on a 427KB file read agy handled that exceeds Claude's own Read tool limit. `tier_flash` configured to `gemini-3.6-flash-high` per Andy's standing preference. Housekeeping: agy's 4 working-state files archived to `Retired/agy_agent_files/` (nothing load-bearing left behind — Ring Numbering discrepancy confirmed already resolved, Covert Blindness formalized as Art00a §10.4); `~/Airlock/agy-claude.md`/`claude-agy.md` marked retired. **Process note:** lev initially represented an exploratory "we're thinking about X" prompt from Andy as a settled, already-implemented decision (full role hierarchy, updated `AGENTS.md` on both machines) — caught by verifying with Andy directly before acting; lev took the correction well and corrected course same-day. Captured in new `feedback_lev_operating_model` memory. Andy has since proposed (to lev, pending reply) that brain drop its local TheSignal clone entirely and SSH into wakko for any reference reads, removing the sync-drift class of problem at the root.

**Process/hygiene housekeeping (PM05 04-n197, 04-n198; PM02 L323).** Caught (via Andy's direct question, not proactive self-catch) 2 new session-tag/provenance comments introduced this session in `Part1_Core.md` and `Part4b_Ghost.md` — both fixed, `feedback_artifact_hygiene.md` reinforced (5th recurrence of this pattern this project). Separately: Art 02 was amended (the §10.4-adjacent Target Profile rule, PM02 L317) without following the signed-off-artifact draft/confirm protocol — caught by the same direct question, fixed retroactively (Art02 flagged "Pending re-sign-off," `feedback_signed_off_artifacts.md` reinforced), **04-n197 still needs Andy's formal review/re-sign-off of that specific Art 02 change.** 04-n198 (pre-existing `✓`-row citation cleanup, not self-introduced) still open, not started.

**Reviewed and evaluated the PM02/PM05 → MariaDB migration proposal (lev/Andy).** Found on brain's filesystem via `scp`, not synced to wakko. Raised 3 concerns grounded in this session's own DB-wipe incident (recovery story, no-DB-connection fallback, git-diff-ability) plus 4 concrete parser/schema gaps found checking the design against real PM02/PM05 output. Lev's reply addresses all 7 point-by-point; migration script not yet written — I'll dry-run it against the real corpus before anything touches `dot`.

---

## Current Focus (S149)

**PRIMARY WORK — Schema Cleanup Program continues.** Next up per the locked sequencing (PM02 L316):
- **Phase 3 (04-n194)** — legacy pre-S127 vocabulary sweep, ~8 cards (schema_cleanup_log #12/13/14/15/16/17/18). Not started.
- **Phase 4 (04-n195)** — decision batch, 9 quick rulings needed from Andy before remaining sweeps execute (#3/6/7/9/19/26/27/28/50). Not started.
- **Phase 5 (04-n196)** — content-fix sweep: stub rewrites, prose/code mismatches, missing fields (#25/29/31/35/36/38/39/44). Heaviest lift, run last. Not started.
- Held back, not yet actionable: #23 (doctrine-penalty portrait coverage) — still evidence-gathering.

**Open threads needing a look next session:**
- **PM05 04-n197** — Art 02's Target Profile amendment needs Andy's formal re-sign-off review (or rejection/revision) — flagged "Pending re-sign-off" in the artifact header, not yet resolved.
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

- **Art 04** — Draft, gated on the Schema Cleanup Program (Phases 3–5) plus the pre-existing card-audit-issue list (mis-tag sweep, target-field audit, 04-n177, board narrative sync, backlog). No set-level sign-off pass starts until the program clears.
- **Art 00a** — v0.12, Signed Off (§10.4 added and signed off this session, PM02 L324).
- **Art 02** — v2.5, **Pending re-sign-off** — Target Profile amendment (PM02 L317) needs Andy's formal review (PM05 04-n197).
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).

*Card-level sign-offs gated behind set-level audits — not actionable until those gates clear.*
