# THE SIGNAL — Session Brief
**Session 161 next | Updated: 2026-09-06**
**Session start:** —

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

## S160 Accomplishments (closed)

**Two of Art 00c's three cost-model gaps closed, `value_rating` finally defined, and the CA/PA corpus now reads zero drift.**

**Add-vs-Redirect mis-tag sweep (00c gap #2) — all 85 `Function=Add` cards, not the Territory subset 00c scoped.** Art 04b §5.1 defines Redirect as subsuming *"cross-faction resource movement = Transfer (Economy — Redirect)"*, which puts Economy and Information in scope. The discriminator: `faction(target)` is a *type/currency qualifier* in most cards (ARBITER supplies it, nobody loses anything) and a *possessive* in few. The borderline was settled by precedent — GHO.MOD.7 and NET.MOD.10 are already Redirect while implementing the transfer as two separate calls, so a transfer needn't be atomic. **One mis-tag: GD-01 Grant Deed → `Territory/Redirect/StructureBlock`** (v0.5). Verified sole instance by grepping every effect field of all 85. **Toll/cut family ruled mechanics-win (Andy)** — `STD.MOD.104/105/116/117/128/129` narrate a transfer their code never performs; six Card Stories, taglines, `narrative` fields and STD.MOD.104's rationale rewritten, and three names renamed because they asserted a payer: **Toll Collected → Freight Booked**, **Informal Toll → Side Work**, **Cut of the Action → Rents Adjust**. `GHO.CA.10` Flip had three narrative surfaces claiming a Redirect its copy model doesn't do — all corrected, taxonomy untouched.

**`target`-field semantics audit + rewrite (00c gap #1).** The column was assigned by a first-match-wins regex cascade answering "which entity is mentioned," and disagreed with "whose holdings change" on **108 of 355 rows**. All four defect classes fixed — hardcoded `faction(Syndicate)` names now resolve against the card's own faction, the `district` test no longer pre-empts `faction=`, type qualifiers are blanked before the receiver search, and transfers get a destination rule. Distribution moved 106→221 `acting`, 121→90 `target`, 73→17 `other`. **The finding that reframed it: no view read `target` at all** — the gap was never inconsistency, it was the pricing path having no beneficiary axis.

**04-n229 CLOSED — the Redirect double-count.** An `xfer` CTE collapses matched opposing legs into one Redirect unit, fixing the double-count *and* making the two category paths converge on one rate. Exactly 3 of 205 cards moved, all ModReactCards, so no CA/PA rating shifted.

**`value_rating` DEFINED (Andy, L376) — gross effect delivered.** A way to bucket cards by how much of the game they move; `cost` already records what is paid, so it does not subtract. **The definition had never been written down**, and that silence let a signed net-of-payments measure get wired into the tier mid-session — it rated pay-to-impose cards as floor-tier for paying a fair price. Reverted; NET.CA.6 and GUI.PA.10 restored to 3 and 4 (gross puts them at exactly their original tiers). Now recorded as governing in **Art 00c §5** and `design_reference_card_system.md`. The signed axis survives, deliberately outside the tier, in `v_card_value_to_acting`.

**Parser fixes (04-n235, partial):** `find_magnitude` now reads `.native * N`, `IntelToken(...) * N` and `min(N, ...)` — 7 magnitudes recovered; **SYN.CA.3 corrected 20.13 → 7.63**. Re-rated GHO.CA.10 1→3, GHO.CA.6 1→3, GUI.CA.7 3→4. Deliberately not extended to `structure * 1` / `trigger.amount * 2`, where the multiplier applies to a counted thing.

**Infrastructure, both found by the work:** `v_card_pair_uvm_cost` was **defined nowhere on disk** — the cost model's working view existed only in the live DB. Now `Database/view_card_pair_uvm_cost.sql` + `view_card_value_to_acting.sql`. And the sync's drift guard excluded MOD cards by a `card_id` string test that leaked GD-01 into the CA/PA audit; re-keyed to `card_type`.

**Wiki (lev's S159 post-mortem):** `deploy_wiki.sh` hardened — all work now runs with stdout redirected to a log, verified to survive `head -1`, ending in a `curl` 200 check. `trap '' PIPE` was tried first and **does not work** (EPIPE still trips `set -e`).

Art 04 → **v0.9.100**. Detail: PM02 L370–L376.

---

## Current Focus (S161)

**Zero drift across the CA/PA corpus.** The cost model is now internally consistent and its governing definition is written down. What remains on Art 04 is card-audit and content work.

**Two calls still carried, both needing Andy — now second session running:**
- **The Art 00c pointer conflict.** Art 04 §6.2 cites Art 00c §5 as authority for `value_rating` while 00c's header says not to cite it. **This got worse this session** — §5 is now also the canonical home of the `value_rating` definition, so the conflict is load-bearing in two places. Resolutions: move the methodology into Art 04 §6 or a Reference file, or lift the non-canonical status for that one section.
- **GUI.CA.9 Works Guarantee** — possible over-inclusion in the original 13 `PositionalWager` cards. Tracked, not gating.

**Card-audit backlog (front of the queue):** 04-n177 (schema scaffolding + §6 canonical sample) · `ref_board_narrative.md` sync · 04-n221's 95-card procedure list, **still carrying §18.1.1** (04-n227). *(The Add-vs-Redirect sweep and the `target`-field audit both closed this session.)*

**Opened this session, all gating:** 04-n230 (GD-01's GR 8.2 edge — step 4 fires when step 3 is skipped, so a Redirect can redirect nothing) · 04-n231 (GD-01 absent from the §8 index) · 04-n232 (GUI.PA.2 vs STD.CA.9 tagged against each other's logic) · 04-n233 (GHO.PA.5's factionless placement; SYN.CA.8/GUI.CA.10 design_notes stale since GD-01 v0.4; Art 04b §5.1 stale on Modifier taxonomy) · 04-n235 (mixed quantification — now holds one card, GUI.PA.6).

**S157 spin-offs still open:** 00a-80 (sub-6-player configuration) · 04-n222 (Directorate military lane) · 04-n223 (§9.2 re-derive — cross-costs are *desirable*, so this measures distribution) · 04-n224 (remaining partial cards) · 04-n124 (SYN.CA.7's debit-only `on_accept`).

**Design item (own session — do not start cold):** Ghost **CA.11** full reimagining. Not gating Art 04.

**New capability, unused so far:** yakko now runs Ollama on an RX 7600 XT — 12–14B models at ~16K context, offered as free local inference for bulk/mechanical passes. Break-even and verification rules are the same as for agy; the 16K ceiling means chunking, not whole artifacts.

---

## Pending Sign-offs

- **Art 04** — v0.9.100, Draft. Every schema gate CLEARED. Remaining is card-audit and content: **04-n222/223/224**, the card-audit backlog above, and the five items opened this session (04-n230/231/232/233/235). Card-level sign-offs stay gated behind all of it. The governing "UVM rates are calibrated off existing card costs, not playtested" caveat still stands — every rating is a self-consistency read, not a validated power tier. One carve-out: the five bare-prose PAs (NET.PA.4/PA.5/PA.6, SYN.PA.4/PA.5) hold pending 04-n218/n220. **Two explicit deferrals on record:** Ghost **CA.11** (S156) and **00a-80** (S157).
- **Art 00a** — v0.13, Signed Off.
- **Art 00c** — v0.6. §5 now carries the `value_rating` definition; the non-canonical-header conflict above is unresolved.
- **Art 02** — v2.5, Signed Off.
- **Art 03** — v4.15, Signed Off. (Re-opening carries two payloads: 04-n221's per-card procedure gaps **and** §18.1.1's React cost-payment step, 04-n227.)
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
