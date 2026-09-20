# THE SIGNAL — Session Brief
**Session 163 next | Updated: 2026-09-20**
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
## S162 Accomplishments (closed)

**A structural session. Art 00c's canonical conflict resolved by splitting the cost model into its own artifact, then four of the five S160 Art 04 gate items cleared — and a silent tooling defect found that had been weakening every drift check since the sync was built.**

**Art 04c — Card System Cost Model created, signed off at v2.0 (PM02 L378, L379).** Art 00c §5 had become the sole written home of the `value_rating` definition, the UVM methodology and the locked tier boundaries while 00c's own header forbade citing it — **PM05 00c-03, carried since S159, CLOSED.** Andy's ruling was a resolution not among the three logged: split it out entirely, and file it in the 04 series because the model only ever prices card-system content. 04c then widened from `value_rating` alone to card economics entire — **what cards charge** (§3 Principle 15 · §4 vocabulary · §5 cost by card type · §6 cross-resource · §7 Intel Tokens) and **how effects are priced** (§8–§11) — absorbing 00c §8 Derived Cost Analysis as §12. Art 00c is now a pure index (v0.7) with two pointer stubs, and its prohibition holds without exception.

**Established and written down for the first time: no cost magnitude rule is locked for any card type.** Principle 15 is a principle, not a formula; the Balance checklist calls cost *"best-effort until Art 00c economics is built"*; §12 is that analysis and is gated on Art 04 sign-off. The chain is judgement → average → tier, and 04c's ⚠ caveat cannot be lifted until §12 exists. **ModReactCard is the only Modifier subclass that charges resources** (27 of 93 — ModAction folds into its host packet, ModBattle is schema-locked because Art 03 §10.1.2 has no payment step). Its cost convention is recorded as **observed, explicitly not a rule** (PM05 04c-01). **18 cards take an Intel Token as cost** (10 CA, 4 PA, 4 ModReact).

**Four of five S160 gate items CLOSED (PM02 L380); two of their premises were wrong.** **04-n230** — GD-01's step 4 now gated on step 3, so the card never resolves as a bare Remove; the taxonomy settled it, since Redirect is an ownership change and the ungated branch falsified GD-01's own tag. **04-n232 — no defect:** STD.CA.9 moves the same resource (Redirect ✓) while GUI.PA.2 consumes Capacity and creates the *target's* native (Add ✓). The discriminator — *does one and the same element change hands?* — is now governing in **Art 04b §5.1 (v2.7)**. **04-n231** — GD-01 added to §8; its framing question was answered by corpus practice, the other two Issued cards being already indexed. **04-n233** — three defects fixed, two worse than logged. **04-n235 rehomed to 04c-01**, not closed: what remains is a pricing convention, which is a cost-model design ruling.

**PM05 DB-50 — `sync_card_db.sh` extracted `card_effect_component` one cycle stale; found, fixed, verified.** The extractor reads `card_body` *from the database*, but the sync ran it before reloading that table — so the `value_rating` drift guard evaluated the previous state of any edited card, and "✓ no drift" was a weaker claim than it read. Found empirically (an edit appeared only after a second sync), fixed by reordering, and verified by reverting and re-applying. **The corpus reads ✓ no drift under the corrected ordering — no current rating disagrees with freshly-extracted rows — but that is not the same as no rating ever having been set against stale input.**

**Also:** Art 04 → v0.9.101. GHO.PA.5 was the corpus's only presence placement lacking `faction=` *and* its only `game.add(PresenceToken, …)`; normalising it corrected `card_effect_component.target` from `district` to `acting`. `Reference/design_reference_card_system.md`'s `cost` entry said "fungible resources only", which 18 cards disprove — corrected.

---

## Current Focus (S163)

### Card-audit backlog — front of the queue
**04-n177** (schema scaffolding + §6 canonical sample) · **`ref_board_narrative.md` sync** · **04-n221's 95-card procedure list**, still carrying §18.1.1 (**04-n227**).

### S157 spin-offs, still open
**00a-80** (sub-6-player configuration) · **04-n222** (Directorate military lane) · **04-n223** (§9.2 re-derive) · **04-n224** (remaining partial cards) · **04-n124** (SYN.CA.7's debit-only `on_accept`).

### Opened S162
- **04c-01** — no cost magnitude rule is locked for any card type; includes whether ModReact's observed convention should become governing, and **04-n235's** pricing convention for unquantifiable delivered instruments now lives here. Needs Andy. Not gating.
- **04-n237** — 47 Art 04 §8 rows still assert the retired taxonomy exclusion. Each needs its real taxonomy filled from the card spec; wants its own pass, not a sweep. Check §11.1's wording at the same time. Not gating.
- **00c-04** — Art 00c's index sections are mis-provenanced and §3's "Round 1 Totals" table is *wrong*, not stale (§4 carries no Resource Type rule). One deliberate repoint-and-reconcile sweep; do not fix piecemeal. Not gating.
- **DB-49** — `card_status.cost_*` columns stale and hand-maintained; query `card_body` for anything cost-related in the meantime. **DB-50** — fixed, but whether any rating was set against stale input is unassessed.

### Carried, needing Andy
**GUI.CA.9 Works Guarantee** — possible over-inclusion in the original 13 `PositionalWager` cards. Tracked, not gating.

### Design item — own session, do not start cold
Ghost **CA.11** full reimagining. Not gating Art 04.

### World Engine (WBS 4) — chartered, build gated
Do not start 4.01 before Art 04 signs off. lev is on 4.02 only. **PM05 CR-01 and CR-02 need Andy, not code** — the four vignette rewrites, the terminology pass, and the two absorption decisions. Start from WE-01, not the proposal.

---

## Pending Sign-offs

- **Art 04** — v0.9.101, Draft. Every schema gate CLEARED; four of five S160 gate items now closed. Remaining is card-audit and content: **04-n222/223/224**, the backlog above, and **04-n235** (worked under 04c-01). The governing "UVM rates are calibrated off existing card costs, not playtested" caveat still stands. One carve-out: the five bare-prose PAs (NET.PA.4/PA.5/PA.6, SYN.PA.4/PA.5) hold pending 04-n218/n220. **Two explicit deferrals on record:** Ghost **CA.11** (S156) and **00a-80** (S157).
- **Art 04c** — v2.0, ✅ **Signed Off S162 as an initial version.** Explicitly not a finished model — revisit before Art 04 signs off; open questions tracked at 04c-01.
- **Art 04b** — v2.7, Signed Off. Two material §5.1 corrections made and signed off in session S162.
- **Art 00a** — v0.13, Signed Off.
- **Art 00c** — v0.7. Now a true index; the canonical-status conflict is resolved. Content accuracy tracked at 00c-04.
- **Art 02** — v2.5, Signed Off.
- **Art 03** — v4.15, Signed Off. (Re-opening carries two payloads: 04-n221's per-card procedure gaps **and** §18.1.1's React cost-payment step, 04-n227.)
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
- **PM01** — v1.7, Active. WBS 4 (World Engine) added S161. Not a sign-off artifact.
