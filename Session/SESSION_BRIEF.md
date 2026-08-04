# THE SIGNAL — Session Brief
**Session 153 next | Updated: 2026-08-04**

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

## S152 Accomplishments (closed)

**Non-design session — no Art/PM03/Schema Cleanup Program work.** Full audit and cleanup of Claude's persistent memory system, triggered by discovering CLAUDE.md's session-startup step still pointed at a file (`Claude_context.md`) that was renamed/relocated to `~/Airlock/agy-claude.md` back on 2026-07-11 and then archived entirely when agy retired as a standalone agent on 2026-07-23 — meaning the live inbound Airlock channel (`~/Airlock/lev-claude.md`) was never actually being read at session start. Fixed that pointer, then found and fixed the same staleness pattern repeated across `workflow_session_close.md`, `feedback_claude_context_prune.md`, `feedback_session_startup.md`, `feedback_airlock_concurrent_edits.md`, `feedback_gem_session_notes.md`, and `project_signal_cluster_topology.md`. A full audit sweep (subagent, all 91 memory files) then surfaced further drift, all fixed: `project_system_config.md` carried an actively wrong DB-troubleshooting instruction (pointed at `dot` as DB host, pre-migration IP, plus plaintext DB credentials — stripped); `MEMORY.md`'s own index line self-contradicted its linked topology file; `user_setup.md` still listed retired `grip` as live; `user_andy_profile.md`/`project_the_signal.md`/`feedback_signed_off_artifacts.md` referenced the pre-merge 02a/02b split (confirmed by Andy: merged into 02 over a month ago); two project-state snapshots (`project_schema_cleanup_log.md` S138, `project_art04_card_design_context.md` S141) flagged superseded against current state; a self-contradiction inside `project_signal_cluster_topology.md` itself fixed (how-to-apply said point `.my.cnf` at `dot`, table two lines up says wakko); ~13 broken `[[wikilink]]` references across 10+ files standardized to match actual frontmatter `name:` fields; one valid orphaned memory indexed (`project_agy_kernel_swap.md`), one dead orphan retired (`reference_card_design_notes.md` — research notes archived, need exhausted), and its corresponding standing item **PM05 04-55 closed**. All memory changes committed and pushed to `agent-memory`.

---

## Current Focus (S153)

**PRIMARY WORK — Schema Cleanup Program continues.** All synthesis-menu items (#4, #20) are now closed. Next up per the locked sequencing (PM02 L316):
- **Phase 5 (04-n196)** — content-fix sweep: stub rewrites, prose/code mismatches, missing fields (#25/29/31/35/36/38/39/44). Heaviest lift, run last. Not started.
- Held back, not yet actionable: #23 (doctrine-penalty portrait coverage) — still evidence-gathering.

**New open items from S150, not yet actionable-scoped:**
- **#56** — `Resource(type, n)` cost-notation on GHO.MOD.6/8, GUI.MOD.6 (a 4th coexisting CostExpr style); GHO.MOD.6/8 additionally have a dynamic (triggering-faction-typed) cost that can't print as a fixed value.
- **#58** — bare tuple `(A, B)` vs. `list([A, B])` multi-mutation notation coexist, no canonical form chosen; scope not counted.

**Untouched synthesis menus:** #34 (full CA-corpus cross-cutting synthesis, six lettered patterns), #45.

**Open threads needing a look next session:**
- **PM05 04-n198** — pre-existing session-tag citations on `✓` checklist rows, corpus-wide sweep not started.
- **MariaDB HNSW RAG ingestion + cron-based agent-memory git sync** — both still open per `agent-memory/shared/infrastructure_services.md`'s pending item; not started.
- Resolved this session (S152): PM05 04-55 closed (retired card-design research notes — archived, need exhausted); Claude's persistent memory audited and cleaned up (stale Airlock/agy/DB-host/02a-02b references — see S152 Accomplishments above). No longer open.

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
