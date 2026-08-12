# THE SIGNAL — Session Brief
**Session 158 next | Updated: 2026-08-12**
**Session start:** 2026-08-12 09:48

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

## S157 Accomplishments (closed)

**PM05 09-17 COMPLETE — the second and last big Art 04 sign-off gate (PM02 L358).** All 27 S156 audit findings triaged in one pass. Every `[verify]` finding re-derived against primary source rather than against the audit docs — which overturned four conclusions and corrected five claims outright. Headlines: the §9.2 economic grouping fails against corpus data (cross-cost share is flat at GUI 50 / SYN 43 / DIR 41 / NET 40 / GHO 23 %, so neither the baseline nor the S156 three-bucket model survives → **04-n223**); SYS-1 reframed by Andy as a symptom of the **undesigned sub-6-player configuration** → **00a-80**; DIR-3's §5a adjacency modifier-draw cut as unbuildable at stated scale; DIR-4's "costs Portrait" ruled doctrinally backwards → **04-n222**; GUI-3 resolved cards-win, §5a rewritten, 04-n2 closed.

**Schema cleanup: #59–#63 closed, #64–#66 opened.** #59 `resolution_type` populated on all 46 cards that lacked it, and §6.3 rewritten as specification-only after Andy's ruling that schema sections must not carry analysis. #60 `value_rating` — found **two derivation conventions coexisting** (CA/PA on UVM cost per L284; modifier cards on the S132/S134 "mirrors magnitude" rule), which no reference file recorded; 5 now-computable cards rated, 4 drifted cards corrected. #61 `NamedActionType` — Andy ruled `action_type` is not a concept the game wants, so **SYN.CA.5 was rescoped to v2.0** onto real components with a self-exemption (`faction != acting`) that is now its doctrinal core. #62 — Andy reframed NET.MOD.3's TBD as a **boost mechanic**, and chasing the blocker found Art 03 §18 has **no cost-payment step at all** for React cards (26 costed cards affected) → folded into **04-n221**. #63 — not cosmetic: GUI.CA.2/GUI.CA.6 had a live payout defect, and my own S157 closure of GUI-4 was wrong.

**#66 — the cost model was built on sand, now fixed.** `card_effect_component`, the table every `value_rating` derives from, had **no extractor** and was a month stale (32% of rows still used retired `+=` syntax). Built `tools/extract_card_effects.py`, rebuilt the table, wired it in. **18 of 205 cards change tier — not applied**, pending two questions in **04-n228**. DIR.PA.8 was corrected 4→2 earlier in the session against the stale model and now reads 3 — everything tiered before the rebuild is provisional.

**Tooling:** `tools/sync_card_db.sh` — one command rebuilds the monolith and all three DB mirrors, with row-count guards, a `value_rating` drift check, and a taxonomy↔pricing-model sync check. Two silent-drift classes now caught automatically.

**Audit program closed and archived.** Seven S156 audit docs + the superseded S119–128 summary moved to `Retired/Whiteboard_Archive/`; standing digest is **`Whiteboard/last_full_card_set_audit.md`** (methodology, what was asked of the corpus, faction + cross-faction conclusions as corrected at S157).

**Design Pass materiality test confirmed (04-n225)** — resets only when a change alters what a card *does* or how it is *strategically classified*; applied to 7 cards.

Full detail: PM02 L358–L366.

---

## Current Focus (S158)

**Both big Art 04 gates are now cleared** (09-16 steps 4–5 at S156; 09-17 triage at S157). What remains is the spun-off work, in this order — agreed with Andy at S157:

**1. PM05 04-n228 — re-rate against the rebuilt cost model.** 18 of 205 cards changed tier when `card_effect_component` was rebuilt; none applied. Two questions decide the list: (a) does `persistence_effect` count toward `total_pair_cost`? (my extractor includes it — an inference, not evidence; it alone moves SYN.MOD.6 tier 1→4), and (b) the four bare-prose PAs now price at 0.00 and **must not** be re-rated to 1 — they need real MutationExpr first (04-n218/n220). Answer (a) first; it changes the list. `bash tools/sync_card_db.sh` reports current drift every run.

**2. `schema_cleanup_log` #64 — the PositionalWager re-derivation.** Two pending calls: **GHO.CA.1** (item #41 ruled it Transactional as a "deterministic declare-then-verify check" — reasoning that doesn't survive, since "deterministic once resolved" is part of the PositionalWager definition) and **DIR.CA.1** (blocks a named card list at Beat 2 against an unrevealed slate). Then the real work: reading all **72 non-React Automatic card bodies**. A query cannot do this — a syntactic sweep missed 4 of the 8 known instances, and two of three later candidates were found by accident. **Wants a clear session; it suffers badly from interruption.**

**3. `schema_cleanup_log` #65 / 04-n226 — §6 provenance sweep.** The `flat` removal (the only piece with a live consequence) is done. Remaining: 13 `schema_cleanup_log` citations, 10 PM05, 3 PM02, 2 session refs, 17 uses of "confirmed". Keep the Data Dictionary's 14 "Displayed" TBDs — real open spec, gated on Art 04 §7 / Art 09. **Sequenced last deliberately:** §6 documents the schema, so sweeping before #64 lands risks doing it twice.

**Then — the pre-existing card-audit backlog:** Add-vs-Redirect mis-tag sweep · `target`-field audit SYN.PA.1 · 04-n177 · `ref_board_narrative.md` sync · 04-n221's 95-card procedure list, **now also carrying §18.1.1** (React cost-payment + boost, detail at 04-n227).

**Other S157 spin-offs:** 00a-80 (sub-6-player configuration — gates smaller-group playtest, explicitly *not* Art 04) · 04-n222 (Directorate military lane: PS cost + §5a edit) · 04-n223 (§9.2 re-derive — note Andy's ruling that **cross-costs are desirable**, so this measures whether interdependence is well-distributed, not whether factions are mono) · 04-n224 (remaining partial cards) · 04-n124 (SYN.CA.7's debit-only `on_accept`).

**Design item (own session — do not start cold):** Ghost **CA.11 full reimagining**, tied to the undesigned Classified Directive subsystem. Explicitly not gating Art 04.

**Opportunistic backlog (detail in PM05):** schema stragglers 04-n203–04-n212 · content/voice gaps 04-n213/214/216–220 · 04-n180 · MariaDB HNSW RAG ingestion + cron agent-memory sync · smaller carried items (04-n163/164/166/167/168/148/150/26/27, XA-54, 06-n01).

---

## Pending Sign-offs

- **Art 04** — v0.9.96, Draft. **Both original gates CLEARED** — 09-16 steps 4–5 at S156, PM05 09-17 triage at S157. Remaining before any set-level sign-off: the S157 spin-offs (**04-n222/223/224/228**, `schema_cleanup_log` **#64/#65**) and the pre-existing card-audit backlog (mis-tag sweep, target-field audit, 04-n177, board narrative sync, 04-n221's 95-card list now also carrying §18.1.1). Card-level sign-offs stay gated behind all of it. **Two explicit deferrals on record — the only two:** Ghost **CA.11** (S156, flagged for reimagining) and **00a-80** sub-6-player configuration (S157 — gates smaller-group playtest, not Art 04). **Caveat carried into S158:** every `value_rating` predates the S157 cost-model rebuild and is provisional until 04-n228 lands. §5a Directorate + Guild rewritten S157 (L358); §6.1/§6.3 schema edits S157 (L359, L365).
- **Art 00a** — v0.13, Signed Off.
- **Art 02** — v2.5, Signed Off.
- **Art 03** — v4.15, Signed Off. (Re-opening now carries two payloads: 04-n221's per-card procedure gaps **and** the new §18.1.1 React cost-payment + boost step, 04-n227.)
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
