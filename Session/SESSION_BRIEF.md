# THE SIGNAL — Session Brief
**Session 155 next | Updated: 2026-08-04**

Lean startup document. Full session history: `Session/THE_SIGNAL___Project_Save_State.md`

---

## Read These First — Every Session

**Before any design, procedure, or card work:** read `Reference/read_first.md` once per session if you haven't already (explains what this directory is and isn't), then:
- `Reference/design_reference.md` — governing principles, card design rules, schema discipline
- `Reference/design_reference_card_system.md` — Art 04 schema, enums, field conventions
- `Reference/ref_*.md` — pick files relevant to the task (procedures, taxonomy, tracking, card types, components, resources, board narrative)

Terminology, methodology, governing rules, and registered decisions live in those files. Do not rely on SESSION_BRIEF for any of that.

**Art 04 file location (S136):** Card content is split across 8 files — `04___Card_System___Part1_Core.md` (§1–6, §8–15), `Part2_Standard.md`, `Part3_Ring_Modifiers.md`, `Part4a_Guild.md`–`Part4e_Syndicate.md`. Edit these directly. `04___Card_System.md` is a generated build artifact (`tools/assemble_card_system.py`) — never edit it, regenerate it after any Part edit.

**Card design content must stand on its own (locked S142, PM02 L276):** Design Rationale/design_note/arbiter_note must never reference or compare against other cards for explanation — cards are self-contained. A separate strategy-guide artifact is the right home for cross-card comparison, if ever wanted. Checklist Notes: ✓ rows get only the pass-justification (no session numbers, no log-item citations); ⚠ rows describe the issue itself; detailed issues go in an Outstanding Issues section below the checklist, not the Note cell.

**Clean-card rule (locked S154):** A finished card carries **zero** inline `#` comments and **no `arbiter_note`** — printed cards ship with neither. Any comment or note still present is a live signal that Art 03 doesn't yet cover that card's mechanic as a general, printable-independent procedure (or the card needs redesigning to fit one) — not documentation to preserve. The old `# scaffolded, not addressed` marker convention is retired (4,685 instances stripped corpus-wide S154, all confirmed pure noise). "Supported by game procedure" checklist row must be ⚠, not ✓, on any card still carrying either — see PM05 04-n221 for the current tracked list (95 cards, genuine Art 03 gaps after redundancy triage).

---

## Startup Delivery

After reading context files, deliver to Andy:
1. **Last session accomplishments** — summarize from "S[N] Accomplishments" below
2. **Current focus** — list open tracks from "Current Focus" below
3. **Pending sign-offs** — list from "Pending Sign-offs" below

Then prompt: *"What's our focus today?"*

---

## S154 Accomplishments (closed)

**MILESTONE — full corpus-wide genuine Design Checklist review complete: all 385 Art 04 cards, all 6 sets.** Andy's session-defining correction on what "Design Pass" actually means (genuinely re-reviewed against source, not trusting existing ✓ marks) applied hard across the four sets remaining after S138–143's earlier passes: Directorate (44), Network (44), Syndicate (44), Ring Modifiers (133 — Overture + 24 ModBattleCard + 72 ModActionCard + 36 ModReactCard). Recurring defect pattern found and fixed corpus-wide: checklist rows falsely claiming fields (most often `card_id`, sometimes 8–10 fields at once on stub cards) were "missing entirely" when `--dump-d` ground truth showed them genuinely present, just `=None`. Real content gaps found and logged rather than fixed inline (need Andy's design input): NET.CA.8/SYN.CA.12 no voice content + notation issues, NET.PA.4-6/SYN.PA.4-5 bare-prose `success` fields needing MutationExpr conversion (PM05 04-n217–220). One real structural bug fixed (STD.MOD.29's narrative implying a hindering effect its schema-locked self-only mechanic can't deliver, misplaced in Design Rationale instead of Outstanding Issues).

**New systemic finding, mid-session, from Andy's own editorial rule: "a finished card should be clean of all comments and no arbiter_note — printed cards carry neither, so anything left is really flagging an Art 03 procedure gap."** Two-stage execution: (1) stripped **4,685** corpus-wide `# scaffolded, not addressed` boilerplate comments (pure noise, redundant with checklist/PM05 tracking, verified zero non-`None` false positives before the sweep) — required flipping "Supported by game procedure" checklist rows ✓→⚠ on **279 cards** carrying a real `arbiter_note`/comment, reverting **117** Issues Resolved cards to Design Pass. (2) Andy's follow-up — check whether each note is actually redundant with fields already in the same `Card()` block (or an already-written Art 03 section) before assuming it's real missing work. Verified the two largest templates word-for-word against Art 03 §10.1.2/§9.1.1 (both already fully cover what the notes said); **174 of 269** real-note cards turned out to be pure duplication and were removed, **76 re-qualified for Issues Resolved**. Caught and fixed a bug in my own restoration script mid-pass (8 cards, GUI.MOD.11-14/GHO.MOD.12-15, wrongly restored — their Balance row's `✓ ...playtest-flagged (04-n94)` still blocks Issues Resolved per the established Directorate MOD.10-13 precedent, a pattern my ⚠-symbol-only check missed). **The genuine remainder — 95 cards — is the real Art 03 procedure-gap/redesign-candidate list**, tracked at PM05 04-n221 with Andy's sequencing question (relative to the faction/cross-faction re-audit below) still open.

**`card_status` DB fully synced** — found completely stale (0/0 across all 386 rows, pre-existing gap, not from today) and brought current: 384 cards matched by `card_id` and updated (2 skipped — `Backdate`/`Field Verification` still carry placeholder `id="Ghost-ext-TBD"`, no real ID to sync against). Final state: 306 Design Pass only, 77 Issues Resolved, 3 untouched (DA-01/DA-02/GD-01, not standard reviewed `Card()` checklist pages). Andy's call on ongoing sync going forward: worth doing now while context is loaded, but may not need to stay perfectly current if the planned SQL-queryable checklist+`Card()` table (Phase 0 step 5, not started) supersedes `card_status`'s simple two columns.

Full detail: PM02 L350–L351.

---

## Current Focus (S155)

**DECISION NEEDED FIRST — sequencing call from Andy, raised S154, not yet resolved:** where does the new 95-card Art 03 procedure-gap list (PM05 04-n221) sit relative to PM05 09-16 steps 4–5 (faction-level + cross-faction re-audit, below)? Live discussion leaned toward: cheap triage already done (this session); full Art 03 procedure-writing should wait until *after* the faction/cross-faction audit locks final card mechanics, so rules aren't written twice against a moving target — but Andy hadn't confirmed that ordering before close. Ask at session start.

**PRIMARY — PM05 09-16 steps 4–5: faction-level + cross-faction card set re-audit.** Now genuinely unblocked — the full 385-card corpus has a real Design Pass for the first time (S154 closed the last 4 sets: Directorate/Network/Syndicate/Ring). Andy's explicit direction (S153, restated): this pass should surface what's left against the properly-edited full corpus — the original S119–128 audits predate the entire 232-card modifier corpus and the whole CA/PA review program. Baseline for comparison: `Whiteboard/card_analysis_summary_S119-128.md` (historical snapshot only — re-derive, don't assume). Also gates PM05 04-n184 (deck copy-count/draw-probability).

**Secondary — 95-card Art 03 procedure/redesign list, PM05 04-n221.** Not yet started (triage-only this session). Real ARBITER procedure content currently living only in `arbiter_note`/comments, not in Art 03 itself — timing sequences, conditional branching, table-communication protocol. Sequencing vs. the item above is the open question.

**Ten non-gating stragglers from the Schema Cleanup Program + `ca_pa_review_notes.md` retirement, pick up opportunistically:** 04-n203 (#23, doctrine-penalty portrait coverage), 04-n204 (#40, stale "(stub)" header labels), 04-n205 (#50, Ghost FieldVerification cost typing, blocked card), 04-n206 (#53, `target_freeform` on ModReactCards), 04-n207 (#56, 4th CostExpr notation style), 04-n208 (#58, tuple-vs-list mutation notation), 04-n209 (11 Standard CA/PA Portrait-validity rows, stale cross-card citation), 04-n210 (STD.CA.1 Guild affinity flat-assignment notation), 04-n211 (legacy header/variable-naming, handful of old cards), 04-n212 (GUI.CA.9 `target_ca` field, unregistered in Targeting group).

**Content/design gaps surfaced S154, need Andy's input (not mechanical fixes):** 04-n213 (STD.CA.11 "Collective" faction / missing Guild voice), 04-n214 (STD.CA.12 empty perspectives), 04-n216 (GUI.PA.10 empty narrative/perspectives), 04-n217 (NET.CA.8 voice + targeting notation), 04-n218 (NET.PA.4-6 bare-prose `success`), 04-n219 (SYN.CA.12 voice + 3-way Accord naming inconsistency), 04-n220 (SYN.PA.4-5 bare-prose `success`).

**Open threads needing a look next session:**
- PM05 04-n180 — corpus-wide session/log-commentary sweep, still not started.
- **MariaDB HNSW RAG ingestion + cron-based agent-memory git sync** — both still open per `agent-memory/shared/infrastructure_services.md`'s pending item; not started.
- Phase 0 step 5 (SQL-queryable Card()+checklist table) — floated S154 as a reason ongoing `card_status` sync may matter less going forward; not started, no design yet.

**Carried, untouched multiple sessions:**
- Add-vs-Redirect mis-tag sweep — other `Territory/Add/PresenceToken`(or `StructureBlock`) cards, same pattern found on SYN.CA.9 (S144)
- `target`-field semantics audit (self-cost/delivered-value gap, S144) — `SYN.PA.1` Acquisition Offer still carries this unresolved gap
- 04-n177's expanded scope; `ref_board_narrative.md` sync pass; smaller carried backlog (04-n163/164/166/167/168/148/150/26/27/126/123, XA-54, 06-n01)

---

## Pending Sign-offs

- **Art 04** — Draft. Full corpus now has a genuine Design Pass (S154 milestone). Two gates remain before any set-level sign-off: (1) **09-16 steps 4–5** — faction-level + cross-faction card set analysis against the now fully-reviewed corpus (primary focus above); (2) the pre-existing card-audit-issue backlog (mis-tag sweep, target-field audit, 04-n177, board narrative sync, the new 95-card 04-n221 list). Card-level sign-offs stay gated behind both.
- **Art 00a** — v0.13, Signed Off.
- **Art 02** — v2.5, Signed Off.
- **Art 03** — v4.15, Signed Off. (Will need re-opening once 04-n221's procedure-writing starts.)
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
