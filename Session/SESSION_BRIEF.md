# THE SIGNAL — Session Brief
**Session 156 next | Updated: 2026-08-05**

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

## S155 Accomplishments (closed)

**Sequencing decision (PM02 L352):** PM05 09-16 steps 4–5 (faction-level + cross-faction re-audit) confirmed as primary, ahead of the 95-card Art 03 procedure-gap list (04-n221) — closes the open question from S154 close. New procedural/redesign items steps 4–5 surface merge into 04-n221 as found rather than becoming separate items.

**First step on Andy's "DB-queryable Art 04" goal (PM02 L353):** new `card_checklist` table in `the_signal_db` — every card's Design Checklist rows (category/verdict/note), 6,970 rows, 383 cards, joins to `card_status`. Built via agy delegation, then hardened directly after catching a real bug: ~20 cards' markdown headings omit the real card_id (bare faction-name headings), and trusting heading text for card_id silently collided distinct cards onto one fake ID — fixed by resolving from each card's own `Card()` block instead. `.md` stays source of truth; DB is a re-syncable projection via `tools/extract_card_checklist.py`.

**Heading/SOT cleanup + Backdate/Field Verification relocated (PM02 L354):** fixed all 18 cards whose headings were missing their real ID (across Standard/Guild/Ghost/Directorate/Network/Syndicate), plus their TOC anchors. Separately, per Andy's direction, moved Backdate and Field Verification (the two permanently-blocked Ghost fossil cards, GR 7.2b, no real card_id) out of the live §7 corpus into a new **Art 04 Part1_Core.md §15 "Deferred Design — Blocked Cards"** appendix — content unchanged, PM05 04-n205 repointed. Monolith regenerated; checklist re-extracted to confirm zero data drift.

**Steps 4–5 scope refined with Andy, execution approach settled:** see Current Focus below for the full plan — audit format, the new implied-vs-leverageable-strategy dimension, step 4 ordering, and the decision to run the audit as the main loop at Opus/Fable strength (not subagents), sequential with a checkpoint after Directorate.

Full detail: PM02 L352–L354.

---

## Current Focus (S156)

**PRIMARY — start PM05 09-16 steps 4–5: faction-level + cross-faction card set re-audit.** Genuinely unblocked (full corpus Design Pass complete, S154) and fully scoped (S155). Start with **step 4, Directorate** (paired with Standard, matching the old S119–128 grouping), then checkpoint with Andy before replicating across Ghost → Guild → Network → Syndicate, then step 5 (cross-faction synthesis).

**Execution approach, locked S155:** run this as the main loop directly, at Opus or Fable strength (Andy: `/fast` or equivalent model swap before starting) — not subagents. This is collaborative design work done in-conversation, not a report to generate and hand back; the checkpoint-after-Directorate pattern requires the main loop to be the one doing the analysis. Sequential, one faction at a time — S141 already found that batching loses real findings full reference-context review catches.

**Format:** same as the old S119–128 passes — deck feel, doctrine coherence, layer coverage, win-path support, §9.2 floor/ceiling economics, all vs Art 04 §5a — now covering each faction's full CA+PA+MOD set for the first time (old pass only ever saw CA/PA, predates the 232-card modifier corpus). Baseline for comparison only, not ground truth: `Whiteboard/card_analysis_summary_S119-128.md` — re-derive fresh, then check against it.

**New dimension, Andy S155:** explicitly identify (a) *implied* strategies — what §5a/doctrine claims a faction should do, rated thin/thick against actual card support; (b) *leverageable* strategies — plays the card set enables whether or not §5a ever named them. Step 4 = both within one faction's own toolkit; step 5 = cross-faction synergies/counters that only show up in comparison (e.g. the old Network-disable-vs-Guild-no-covert-ops interaction). Folds in what the old cross-faction pass handled ad hoc via a side doc (4 emergent patterns, closed no-op S128).

**Before starting:** load full reference context, not just Art 04 (`ref_components.md`/`ref_procedures.md`/`ref_card_types.md`/`ref_resources.md`/`ref_world_narrative.md`/`ref_board_narrative.md`/`design_reference_card_system.md`) — S141 discipline. `card_checklist` (`the_signal_db`, S155) is the query substrate for the structured/mechanical side (taxonomy, checklist flags, cost axes) — query it instead of re-deriving by hand.

**Secondary — 95-card Art 03 procedure/redesign list, PM05 04-n221.** Not started. Real ARBITER procedure content currently living only in `arbiter_note`/comments, not in Art 03 — now the standing collection point for any new procedure-gap findings steps 4–5 turn up.

**Opportunistic backlog (full detail in PM05):** ten non-gating schema stragglers (04-n203–04-n212); seven content/voice gaps needing Andy's input (04-n213/214/216/217/218/219/220); Add-vs-Redirect mis-tag sweep; `target`-field semantics audit (SYN.PA.1); 04-n180 (session-commentary sweep); MariaDB HNSW RAG ingestion + cron agent-memory sync; 04-n177 expanded scope; `ref_board_narrative.md` sync; smaller carried items (04-n163/164/166/167/168/148/150/26/27/126/123, XA-54, 06-n01).

---

## Pending Sign-offs

- **Art 04** — Draft. Full corpus now has a genuine Design Pass (S154 milestone). Two gates remain before any set-level sign-off: (1) **09-16 steps 4–5** — faction-level + cross-faction card set analysis against the now fully-reviewed corpus (primary focus above); (2) the pre-existing card-audit-issue backlog (mis-tag sweep, target-field audit, 04-n177, board narrative sync, the new 95-card 04-n221 list). Card-level sign-offs stay gated behind both.
- **Art 00a** — v0.13, Signed Off.
- **Art 02** — v2.5, Signed Off.
- **Art 03** — v4.15, Signed Off. (Will need re-opening once 04-n221's procedure-writing starts.)
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
