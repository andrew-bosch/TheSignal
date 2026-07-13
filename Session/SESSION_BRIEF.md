# THE SIGNAL — Session Brief
**Session 145 complete | Updated: 2026-07-13**
**Session start:** (stamped at next boot — see CLAUDE.md Session Startup step 1)

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

## S145 Accomplishments

**`value_rating` (1–4) definition locked and applied corpus-wide — 04-n178/04-n183 closed, the deliverable this whole thread has been building toward since S143.** Full detail: PM02 L283/L284 · `Whiteboard/cost_baseline_recommendations.md` §5 · `Database/schema_reference.md` §6.7.

**Tier scheme:** natural-break on `total_pair_cost` (<3.0→1, 3.0–4.99→2, 5.0–6.99→3, ≥7.0→4) — a pyramid shape matching "1=floor, 4=end-game-ceiling," not equal-population quartiles (checked and rejected). 164 cards tiered by a two-pass batch script (`Database/apply_value_rating.py`, saved for reuse — self-contained, idempotent, queries the DB live); 27 ring-modifier cards already matched via the separate S132/S134 magnitude-mirror convention; **9 disagreed and were overridden to the pricing-model tier on Andy's call** ("value is based on effect value") — STD.MOD.99/111/123 1→2, STD.MOD.101/103/113/115/125/127 2→1, Balance rows rewritten to match. 8 cards remain unaddressed (no computable `total_pair_cost` — blocked/TBD cards, not a scheme gap). `GHO.CA.11` stays excluded (unfinalized, own spec still `id=TBD`).

**GHO.PA.1/STD.PA.5 taxonomy-corrected and repriced along the way** (both were tagged `Reveal/ActionAttribution` when their real effect is a PS swing — retagged to `Shift/StandingMarker`, precedented S126/S137). STD.PA.5: threshold 35→30 closed the delta to −2.4%. GHO.PA.1: cost restructured (Findings/Exposure/target-native/Intel Tokens, 8.00→10.00 effective); still +45.2% — **locked as intentional Ghost doctrinal advantage**, not a further pricing defect (the 2-token prior-investment gate isn't visible to the raw-cost model).

**Documented the model's governing caveat everywhere it needs to travel:** UVM base rates are calibrated by averaging *existing* card costs (only 7/28 Subject and 25/58 pair rates are even "validated" in that limited sense), not playtested. Added to `schema_reference.md` §6.7, `cost_baseline_recommendations.md` (new top-of-doc section), `design_reference_card_system.md`'s `value_rating` field definition, and `project_db_design_intent.md` memory — this follows any future use of `v_card_pair_uvm_cost` or anything downstream of it.

**New open item: PM05 04-n184** — deck copy-count/draw-probability calculation, now unblocked by value_rating closing but explicitly scoped by Andy as coming *after* a redo of the per-faction/cross-faction card space audits (S119–128 style), not a standalone exercise. Andy flagged a real chance all 3 ring-modifier decks need retuning once copy-count accounts for the value_rating spread.

**Airlock:** ingested and pruned an unread `lev-claude.md` handoff (wiki build script upgrade — card subdivision, nav links, anchor healing; deployed on `pinky`, no action needed this side).

---

## Current Focus (S146)

**PM05 04-n184 — deck copy-count / draw-probability audit.** Per Andy's S145 direction, do NOT start this cold. Sequence: (1) redo the per-faction + cross-faction card space audits first (S119–128 style — 04-n50 Ghost, 04-n53 Standard, etc. consolidated passes), (2) only then run the copy-count/probability pass against the refreshed picture. Suspected outcome: all 3 ring-modifier decks (`Part3_Ring_Modifiers.md`, 133 cards) may need retuning. Scope not yet defined — copy-count-per-tier baseline, inverse-scaling-with-value_rating question, and whether faction MOD/CA/PA decks need the same treatment are all open.

**Also open, carried from S142–144, not yet scheduled:**
- PM05 04-n180 — full-corpus sweep of embedded session/log commentary, incremental "as we do issue review."
- 04-n177's expanded scope; 04-n165/04-n169 (Art 04 sign-off gates); 04-n171 (ModReactCard syntax reconciliation); `ref_board_narrative.md` sync pass; smaller carried backlog (04-n163/164/166/167/168/148/150/26/27/126/123, XA-54, 06-n01).
- `schema_cleanup_log.md` items #10 (Intel Token as cost), #41 (resolution_type vocabulary), #2/#5 (persistence/trigger semantics) — independent of the value_rating thread, still open.
- Light sweep worth scheduling: other `Territory/Add/PresenceToken`(or `StructureBlock`) cards for the same Add-should-be-Redirect mis-tag found on SYN.CA.9 (S144).
- `target`-field semantics audit (self-cost/delivered-value gap, S144) — needed before the pricing model can be trusted on cards using self-payment or opponent-benefit patterns. `SYN.PA.1` Acquisition Offer specifically still carries this unresolved gap.

---

## Pending Sign-offs

- **Art 04** — Draft, gated on 04-n165 + 04-n169 (copy/content sweeps). Full CA+PA phase content-reviewed, value_rating now fully defined/populated (04-n178/n183 closed) — remaining gate is the whole-set schema decisions (#10/#22, #41, #2/#5) before any set-level sign-off pass can start.
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).

*Card-level sign-offs gated behind set-level audits — not actionable until those gates clear.*
