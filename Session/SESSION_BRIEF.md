# THE SIGNAL — Session Brief
**Session 159 next | Updated: 2026-08-24**
**Session start:** 2026-08-24 13:06

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

## S158 Accomplishments (closed)

**PM05 04-n228 CLOSED — the last cost-model gate. `value_rating` is no longer provisional.** Andy ruled `persistence_effect` counts toward `total_pair_cost`, and the "open question" turned out never to have been open: the pre-S157 backup contains five rows literally prefixed `[persistence_effect]` (DIR.PA.3/5/6/11, DIR.MOD.9), and the existing S145 ratings on those cards reconcile *only* with inclusion — excluding it would put them at tiers 2/1/1/1 against ratings of 4/3/3/2. For six further cards the persistence effect is the entire priceable content. Method: the view's inner logic rebuilt as a CTE and run in three regimes (include / exclude / old `board_condition`+NULL encoding); include-mode reproduces `v_card_pair_uvm_cost` row-for-row on all 199 shared cards, and old-vs-new encoding is **tier-neutral corpus-wide**.

**Three S157 claims did not survive re-derivation — same failure mode S157 kept hitting: a claim about the corpus asserted from a derived artifact rather than re-derived from source.** (1) "That single choice drives SYN.MOD.6 tier 1→4" — it computes tier 4 in *all three* regimes, and as a MOD/React card it rates on magnitude and was never UVM-tiered at all; the one argument that made the question look blocking rested on the one card it could not apply to. The choice in fact gated **one** card, SYN.PA.3. (2) "The four bare-prose PAs" — there are **five**; NET.PA.6 is unpriceable on identical grounds and stayed hidden only because its rating of 1 coincides with what the scheme spuriously returns at cost 0.00. (3) "14 cards drifted" — 16, of which 6 are MOD/React and out of scope. S157's enumeration of the **10** re-derivable cards was, however, exactly right, card for card and direction for direction.

**All 10 re-ratings applied** — STD.CA.14 2→1, GHO.CA.6 3→1, GHO.CA.10 3→1, SYN.PA.3 1→2, DIR.CA.4 1→2, STD.CA.7 1→2, DIR.PA.8 2→3, GUI.CA.8 2→3, GUI.CA.7 2→3, NET.PA.1 3→4 — each spot-verified against `uvm_pair_assumptions` (zero rate-table fallbacks, every rate `validated`). Two carry `has_boost`, so their costs are **floors at N=1**: SYN.PA.3's tier 2 could go higher once N is known; NET.PA.1's is already at the tier-4 ceiling.

**Rulings (Andy):** `persistence_effect` counts toward cost · MOD/React cards drifting against UVM tiers are **expected, not defects** (six recorded by name so they are not re-found as findings each sweep) · all five bare-prose PAs **hold** their current ratings — unverifiable rather than wrong — pending real MutationExpr via 04-n218/n220.

**Tooling + drift-guard fix.** `sync_card_db.sh` was counting the bare-prose cards as drift — a permanent false positive that would have masked real drift. Split into its own "unpriceable" bucket; that split is what surfaced NET.PA.6. The check now reads **✓ no drift**. A reverse pointer was added to 04-n218/n220, neither of which mentioned `value_rating`: converting the prose makes those ratings computable for the first time and they must be re-derived at that point — without it, 04-n228's carve-out was a dangling promise.

**Three corrections to my own S158 work, caught before they landed:** a backup-parsing regex that silently dropped 78 of 358 rows (couldn't match negative magnitudes); a Reference claim that S157's four named drifters were "artefacts" when PM02 L361 shows all four were *corrected* (three of those corrections stand against the rebuilt model; only DIR.PA.8 was corrected against bad input); and a stale "3 remain genuinely non-computable" claim — the rebuild made GHO.MOD.1 and STD.MOD.1 computable, though they stay `None` under convention (b).

Art 04 → **v0.9.97**. Full detail: PM02 L367, `schema_cleanup_log.md` #66 (S158 addendum).

---

## Current Focus (S159)

**All three big Art 04 gates are now cleared** (09-16 steps 4–5 at S156; 09-17 triage at S157; the cost model at S158). Remaining, in the order agreed with Andy:

**1. `schema_cleanup_log` #64 — the PositionalWager re-derivation. Next up.** Two pending calls: **GHO.CA.1** (item #41 ruled it Transactional as a "deterministic declare-then-verify check" — reasoning that doesn't survive, since "deterministic once resolved" is part of the PositionalWager definition) and **DIR.CA.1** (blocks a named card list at Beat 2 against an unrevealed slate). Then the real work: reading all **72 non-React Automatic card bodies**. A query cannot do this — a syntactic sweep missed 4 of the 8 known instances, and two of three later candidates were found by accident. **Wants a clear session; it suffers badly from interruption — do not start it as a continuation of other work.**

**2. `schema_cleanup_log` #65 / 04-n226 — §6 provenance sweep.** The `flat` removal (the only piece with a live consequence) is done. Remaining: 13 `schema_cleanup_log` citations, 10 PM05, 3 PM02, 2 session refs, 17 uses of "confirmed". Keep the Data Dictionary's 14 "Displayed" TBDs — real open spec, gated on Art 04 §7 / Art 09. **Sequenced after #64 deliberately:** §6 documents the schema, so sweeping before #64 lands risks doing it twice.

**Then — the pre-existing card-audit backlog:** Add-vs-Redirect mis-tag sweep · `target`-field audit SYN.PA.1 · 04-n177 · `ref_board_narrative.md` sync · 04-n221's 95-card procedure list, **now also carrying §18.1.1** (React cost-payment + boost, detail at 04-n227).

**S157 spin-offs still open:** 00a-80 (sub-6-player configuration — gates smaller-group playtest, explicitly *not* Art 04) · 04-n222 (Directorate military lane: PS cost + §5a edit) · 04-n223 (§9.2 re-derive — note Andy's ruling that **cross-costs are desirable**, so this measures whether interdependence is well-distributed, not whether factions are mono) · 04-n224 (remaining partial cards) · 04-n124 (SYN.CA.7's debit-only `on_accept`).

**Design item (own session — do not start cold):** Ghost **CA.11 full reimagining**, tied to the undesigned Classified Directive subsystem. Explicitly not gating Art 04.

**Opportunistic backlog (detail in PM05):** schema stragglers 04-n203–04-n212 · content/voice gaps 04-n213/214/216–220 · 04-n180 · MariaDB HNSW RAG ingestion + cron agent-memory sync · smaller carried items (04-n163/164/166/167/168/148/150/26/27, XA-54, 06-n01).

---

## Pending Sign-offs

- **Art 04** — v0.9.97, Draft. **All three original gates CLEARED** — 09-16 steps 4–5 at S156, PM05 09-17 triage at S157, the cost model at S158. **The S157 blanket caveat that every `value_rating` is provisional is now LIFTED** — that caveat only; the governing "UVM rates are calibrated off existing card costs, not playtested" caveat still stands, and every rating remains a self-consistency read rather than a validated power tier. One carve-out: the five bare-prose PAs (NET.PA.4/PA.5/PA.6, SYN.PA.4/PA.5) hold pending 04-n218/n220. Remaining before any set-level sign-off: **04-n222/223/224**, `schema_cleanup_log` **#64/#65**, and the pre-existing card-audit backlog (mis-tag sweep, target-field audit, 04-n177, board narrative sync, 04-n221's 95-card list now also carrying §18.1.1). Card-level sign-offs stay gated behind all of it. **Two explicit deferrals on record — the only two:** Ghost **CA.11** (S156) and **00a-80** sub-6-player configuration (S157).
- **Art 00a** — v0.13, Signed Off.
- **Art 02** — v2.5, Signed Off.
- **Art 03** — v4.15, Signed Off. (Re-opening now carries two payloads: 04-n221's per-card procedure gaps **and** the new §18.1.1 React cost-payment + boost step, 04-n227.)
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
