# THE SIGNAL — Session Brief
**Session 151 next | Updated: 2026-07-31**

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

## S150 Accomplishments (closed)

**All schema_cleanup_log synthesis-menu items (#4, #20) fully closed — every lettered sub-item resolved.** Full detail: PM02 L339–L344.

- **#4 D/E/F** — `tools/audit_card_corpus.py` built (parses `Card()` instances directly from the monolith). D closed as superseded by E (corpus's own omit-by-default convention makes a literal full-declaration gate wrong). E/F closed clean (0 real gaps). New `card_status.mod_subtype` DB column (Action/Battle/React) backfilled — DB previously had no way to distinguish the three Modifier subclasses. New view `v_card_taxonomy_gaps`. One real DB sync gap found and fixed (GD-01).
- **#20 A** — vintage-format concern already resolved elsewhere; caught a 4th stale presence-mutation shape (3 instances) the earlier sweep missed.
- **#20 B/C** — B already closed via #5. C: no design gap — Art 03 §7.4 restructured with an explicit Resource Type rule (district income pays in the district's own type, not the collecting faction's); closes PM05 03-n04.
- **#20 E/F** — Art 03 §18 already substantially governed ModReactCard trigger-overlap/stacking; refined its tiebreak (initiative order) and added explicit multi-card-choice language. New Art 00a **GR §7.2c** (generalized, not ModReactCard-specific per Andy's correction).
- **#20 D** — 3 distinct fixes: SYN.MOD.8 (syntax), DIR.MOD.6 (reused existing `game.board_condition`), NET.MOD.13/SYN.MOD.6 (genuine gap — closed via `persistence_condition = not trigger.card.resolved`, new §6.3 vocabulary: `public_act.resolved(pa=X)`, `trigger.card.resolved`/`.outcome`, `arbiter.protect()`, standalone `on(TriggerExpr): MutationExpr`).
- **#57** — `district(trigger.target)` self-reference bug (GUI.MOD.1/10) normalized to the existing `trigger.district` pattern; written into §6.3 as "ModReactCard target inheritance."
- New open items, not fixed: **#56** (`Resource(type,n)` cost-notation + dynamic-native cost shape on GHO.MOD.6/8), **#58** (tuple vs. `list([...])` multi-mutation notation, no canonical form chosen).

**Art 03 (v4.15) and Art 00a (v0.13) re-signed off** (PM02 L345) — batched to session close per Andy's direction rather than per-edit.

**Hygiene recurrence #7 and #8 (feedback_artifact_hygiene.md updated).** Provenance/session-tag language crept into new §6.3 schema prose twice more this session — caught by Andy directly both times ("write the spec and schema as if it is final copy"), not proactively. The S149 mechanical grep-check fix (run a pattern search over every touched file before calling a batch done) had itself not been run — now flagged as the recurring point of failure, not the rule-awareness.

---

## Current Focus (S151)

**PRIMARY WORK — Schema Cleanup Program continues.** All synthesis-menu items (#4, #20) are now closed. Next up per the locked sequencing (PM02 L316):
- **Phase 5 (04-n196)** — content-fix sweep: stub rewrites, prose/code mismatches, missing fields (#25/29/31/35/36/38/39/44). Heaviest lift, run last. Not started.
- Held back, not yet actionable: #23 (doctrine-penalty portrait coverage) — still evidence-gathering.

**New open items from S150, not yet actionable-scoped:**
- **#56** — `Resource(type, n)` cost-notation on GHO.MOD.6/8, GUI.MOD.6 (a 4th coexisting CostExpr style); GHO.MOD.6/8 additionally have a dynamic (triggering-faction-typed) cost that can't print as a fixed value.
- **#58** — bare tuple `(A, B)` vs. `list([A, B])` multi-mutation notation coexist, no canonical form chosen; scope not counted.

**Untouched synthesis menus:** #34 (full CA-corpus cross-cutting synthesis, six lettered patterns), #45.

**Open threads needing a look next session:**
- **PM05 04-n198** — pre-existing session-tag citations on `✓` checklist rows, corpus-wide sweep not started.
- **agy/lev split** — waiting on lev's reply to the "drop brain's local clone" proposal; PM02/PM05 MariaDB migration script not yet written, dry-run pending.
- **lev's Airlock protocol proposal** (`~/Airlock/lev-claude.md`, unacked) — Sender-Push + Ack protocol for claude↔lev messaging (machine-owned outgoing files, scp push on write, append-until-acked, reset on ack). Needs Andy's read before responding; not evaluated yet.

**Carried, untouched multiple sessions:**
- Add-vs-Redirect mis-tag sweep — other `Territory/Add/PresenceToken`(or `StructureBlock`) cards, same pattern found on SYN.CA.9 (S144)
- `target`-field semantics audit (self-cost/delivered-value gap, S144) — `SYN.PA.1` Acquisition Offer still carries this unresolved gap
- 04-n177's expanded scope; `ref_board_narrative.md` sync pass; smaller carried backlog (04-n163/164/166/167/168/148/150/26/27/126/123, XA-54, 06-n01)

**After Art 04 initial sign-off — not yet actionable:**
- PM05 04-n184 — deck copy-count / draw-probability audit. Sequence once unblocked: (1) redo per-faction + cross-faction card space audits first (S119–128 style), (2) only then run copy-count/probability against the refreshed picture. Suspected outcome: all 3 ring-modifier decks may need retuning.

---

## Pending Sign-offs

- **Art 04** — Draft, gated on the Schema Cleanup Program (Phase 5 remaining) plus the pre-existing card-audit-issue list (mis-tag sweep, target-field audit, 04-n177, board narrative sync, backlog). No set-level sign-off pass starts until the program clears.
- **Art 00a** — v0.13, Signed Off.
- **Art 02** — v2.5, Signed Off.
- **Art 03** — v4.15, Signed Off.
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).

*Card-level sign-offs gated behind set-level audits — not actionable until those gates clear.*
