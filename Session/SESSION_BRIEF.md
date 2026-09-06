# THE SIGNAL — Session Brief
**Session 160 next | Updated: 2026-09-06**
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

## S159 Accomplishments (closed)

**Both remaining Art 04 schema gates closed — `schema_cleanup_log` #64 and #65.**

**#64 — the PositionalWager re-derivation. All 72 non-React `Automatic` bodies read; corpus 13 → 21.** A body-only read could not have done it: GUI.CA.2's `success` is an unconditional two-line resource add and its wager exists only in prose, so every card's Design Rationale and Card Story were read alongside its `Card()` block. Population derived two ways (39 CovertOperation + 33 PublicAct, `card_status.card_type` and `v_card_body.type` agreeing, zero mismatch). Empirical profile of the 13 pre-existing instances, derived not assumed: every one `beat = 2`, CovertOperation, `persistence = Immediate`.

**Two boundary rulings (Andy), both now spec in §6.3:** (1) a contingency carried by `persistence`/`persistence_effect`/`game.world_condition`, or by a delivered instrument, leaves the card **Transactional** — holds 13 cards that would otherwise have flipped; (2) the unrevealed slate **need not belong to a later beat**, only to be unrevealed at commitment — admits STD.CA.12 and NET.CA.1.

**8 recategorisations applied:** GHO.CA.1, DIR.CA.1, GHO.CA.3, DIR.CA.3, GHO.CA.5, STD.CA.12, NET.CA.1, NET.CA.4 — six new. DIR.CA.1 was mislabelled against its own Design Rationale, which already read "Beat 2 Automatic positional wager." **GHO.CA.1 reversed #41's logged ruling** — "deterministic once resolved" is part of the definition, and the appeal to its *"We are not predicting"* perspective line is Ghost's voice asserting competence, not a claim about the mechanism; Design Rationale rewritten and approved before the field changed. **Andy's mechanical clarification, same card:** the stolen operation card returns to its owner's case once it resolves — Ghost takes that Month's execution, not the card. Design Pass reset on all 8 per 04-n225. All 21 instances are CovertOperation; no PublicAct can qualify, which falls out of beat ordering.

**Flagged, not resolved — GUI.CA.9 may be an over-inclusion in the original 13.** It operates on Guild's *own* named Beat 3 CA with district B checked at Beat 0 against board state visible at §9.1, so there may be no unknown at commitment at all. The enumeration was never derived; it can be wrong in this direction too.

**#65 — §6 spec-hygiene sweep.** §6 now carries **zero** `schema_cleanup_log`/PM05/PM02/session citations and **zero** uses of "confirmed" (verified in the Part file and the monolith). Corpus analysis removed — Issued-card inventory, `persistence` example list, `generating_card` examples, three "Confirmed via [card list]" trailers, `ring_constraint`'s "under review" note. The `cost`-is-`None` paragraph rewritten as spec. The 14 "Displayed" TBDs kept, now with a line naming §7 / Art 09 as the gate. Counts were re-derived, not carried: the S157 scan had said 3 PM02 citations where there were 6 — it missed the bare `L219`/`L280`/`L174` forms.

**Four factual defects found while sweeping, all fixed:** `beat: int # 1–5` (wrong on both readings — Art 03 runs Beats 0–4, the corpus uses 2/3/4; now enumerates the real values, §6.2 row aligned) · §6.1 contradicting §6.2 on `value_rating` · "`None` = unassigned (blocked/TBD cards only)" being false (the three are unblocked ModReactCards held `None` by convention) · DIR.PA.1 named as a Permanent example when it is `Seasonal`.

**Art 00c §5 updated (Andy's call), → v0.6** — S158's closure and ten re-ratings, CA/PA-only scope, MOD/React magnitude-convention exemption, the five bare-prose PA carve-out, tier counts re-derived (114/49/23/19 over 205 priced cards, was 107/48/26/19). **`Reference/design_reference_card_system.md` was badly stale** — still called `resolution_type` "str, not enum" and warned authors off `"Positional wager"`, language predating the S147 enum conversion; resynced along with the same `beat` error.

Art 04 → **v0.9.99**. Full detail: PM02 L368/L369, `schema_cleanup_log.md` #64/#65.

---

## Current Focus (S160)

**Every Art 04 *schema* gate is now closed** (09-16 steps 4–5 at S156; 09-17 triage at S157; the cost model at S158; #64 and #65 at S159). What remains before a set-level sign-off is card-audit and content work, not schema work.

**Two calls carried out of S159, both needing Andy:**
- **The Art 00c pointer conflict.** Art 04 §6.2 cites Art 00c §5 as the authority for `value_rating`'s derivation, while Art 00c's own header reads "⚠️ Future Analysis Stub — Not Canonical" and says *"do not cite 00c for design decisions or ref files."* §5's content was brought current, which does not fix the conflict. Resolutions: move the methodology into Art 04 §6 or a Reference file, or lift the non-canonical status for that one section. Both change an artifact's canonical status.
- **GUI.CA.9 Works Guarantee** — possible over-inclusion in the original 13 `PositionalWager` cards (detail in `schema_cleanup_log` #64). Tracked, not gating.

**The card-audit backlog — now the front of the queue:** Add-vs-Redirect mis-tag sweep · `target`-field audit SYN.PA.1 · 04-n177 · `ref_board_narrative.md` sync · 04-n221's 95-card procedure list, **now also carrying §18.1.1** (React cost-payment + boost, detail at 04-n227).

**S157 spin-offs still open:** 00a-80 (sub-6-player configuration — gates smaller-group playtest, explicitly *not* Art 04) · 04-n222 (Directorate military lane: PS cost + §5a edit) · 04-n223 (§9.2 re-derive — note Andy's ruling that **cross-costs are desirable**, so this measures whether interdependence is well-distributed, not whether factions are mono) · 04-n224 (remaining partial cards) · 04-n124 (SYN.CA.7's debit-only `on_accept`).

**Design item (own session — do not start cold):** Ghost **CA.11 full reimagining**, tied to the undesigned Classified Directive subsystem. Explicitly not gating Art 04.

**Opportunistic backlog (detail in PM05):** schema stragglers 04-n203–04-n212 · content/voice gaps 04-n213/214/216–220 · 04-n180 · MariaDB HNSW RAG ingestion + cron agent-memory sync · smaller carried items (04-n163/164/166/167/168/148/150/26/27, XA-54, 06-n01).

---

## Pending Sign-offs

- **Art 04** — v0.9.99, Draft. **Every schema gate is CLEARED** — 09-16 steps 4–5 at S156, PM05 09-17 triage at S157, the cost model at S158, `schema_cleanup_log` #64/#65 at S159. The S157 blanket caveat that every `value_rating` is provisional stays LIFTED; the governing "UVM rates are calibrated off existing card costs, not playtested" caveat still stands, and every rating remains a self-consistency read rather than a validated power tier. One carve-out: the five bare-prose PAs (NET.PA.4/PA.5/PA.6, SYN.PA.4/PA.5) hold pending 04-n218/n220. Remaining before any set-level sign-off is now card-audit and content work only: **04-n222/223/224** and the card-audit backlog (mis-tag sweep, target-field audit, 04-n177, board narrative sync, 04-n221's 95-card list now also carrying §18.1.1). Card-level sign-offs stay gated behind all of it. **Two explicit deferrals on record — the only two:** Ghost **CA.11** (S156) and **00a-80** sub-6-player configuration (S157).
- **Art 00a** — v0.13, Signed Off.
- **Art 02** — v2.5, Signed Off.
- **Art 03** — v4.15, Signed Off. (Re-opening now carries two payloads: 04-n221's per-card procedure gaps **and** the new §18.1.1 React cost-payment + boost step, 04-n227.)
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
