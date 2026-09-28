# THE SIGNAL — Session Brief
**Session 166 next | Updated: 2026-09-28**
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
## S165 Accomplishments (closed)

**PM05 04-n124 closed: SYN.CA.7 Corporate Blackmail v3.0 redesigned as the first Covert Demand, and Art 03 v4.17 adds §9.5 Covert Demands (PM02 L385).**

- **The defect was fixed.** CA.7's `on_accept` now debits the target's own native and dispatches the same 2 tokens to Syndicate's case, so the Art 04b §5.1 same-element test holds and Redirect is correct. Andy ruled the payment is the target faction's native: the card is Syndicate's route to non-native resources.
- **New governing constraint (Andy): the Dispatch Case is the only covert channel at the table.** Nothing can be whispered or handed over unseen. So the card and Syndicate's Target Profile go into the target's case in Month N. The target returns both in its next case, with payment attached (comply) or empty (resist). It resolves at N+1 Beat 3. **ARBITER tracks nothing**; follow-up is Syndicate's job. Other rulings:
  - The card is Permanent with a clearing trigger, fully covert.
  - A Month 3 demand is answered in the next Quarter's Month 1.
  - A demand unanswered at game end has no effect.
  - A target that can't pay can only resist.
  - Syndicate's cost is the hidden Portrait −1 only.
  - The target's PS −1 on resist stays, and §9.4.2.2.0 is amended to allow it.
  - Resist removes 1 Presence **Token** (a count, not a tier).
- **Playtest:** comply 2 and resist 1 token are the playtest values, tracked as **PM02 PT-04-04**. At value_rating 3 it should bite; the candidate if it doesn't is 2 tokens.
- **Schema:** the §6 proposals are in `schema_cleanup_log` #67. They cover ElectPlayer on covert ops, the on_accept timing, a new `covert_op.resolved(op=X)` TriggerExpr, and covert Permanent.
- **04-n72** was rescoped from the Beat 3 whisper to §9.5 and is drafted.
- **Doctrine:** CA.1's Rationale already carried it. Its Land Title comparison broke L276 and was replaced, as was CA.7's comparison to CA.1.

---

## Current Focus (S166)

### Start here
- **04-n222** — the Directorate military lane (DIR.MOD.10–13) costs nothing in any currency. Needs Andy's PS numbers, the §5a text edit, and a portrait decision, all in one pass. **Andy's pick for S166.**

### S157 spin-offs — still open
- **04-n223** — re-derive the economy grouping from corpus data *before* running the pass; all three existing §9.2 items rest on stale counts.
- **04-n224** — reduced to **GUI.MOD.10's remaining blocker only** (04-n148).
- **00a-80** — sub-6-player configuration. Explicit deferral on record.

### Art 03 §10.1.2 — drafted next, gates GUI.MOD.10
**04-n148** — §10.1.2 has no step that reads a registered condition and applies it to a contesting faction's total. Material edit to Art 03 (already pending re-sign-off), so draft first.

### Carried
- **04-n238** (`is_unique`/`deck_limit`, blocked on 04-n136) · **04-n239** (132 ModActionCards with `perspectives = None`; sequence against 04-n224) · **04c-01** · **04-n237** · **00c-04** · **DB-49** · **schema #67** (Covert Demand §6 proposals).
- **Unverified:** `card_status.art04_line` looks stale corpus-wide. SYN.CA.7 shows 8141 and SYN.CA.1 shows 7360; neither matches the monolith or the Part file. Not yet logged.

### Sequencing — unchanged
04-n221's 95-card list stays **behind** 09-16 steps 4–5. Ghost **CA.11** needs its own session. World Engine build gated on Art 04; **CR-01/CR-02/CR-03 need Andy, not code**.

---

## Pending Sign-offs

- **Art 03 — v4.17, 🔄 Pending re-sign-off.** New in S165: **§9.5 Covert Demands** plus hook lines (Dispatch Token rule, §9.1.1, §9.4.0.1 steps 2/5, §9.4.2.2, §9.4.2.2.0, §9.4.2.3, §9.4.2.4.0, §9.4.2.6.0). From S163: §18.2 Pay Cost, §13.6 Intel Token as Cost, §18 renumbered. One clause Andy should confirm explicitly: a voided React does not exhaust the trigger.
- **Art 04** — v0.9.103, Draft. Every schema gate cleared. Remaining is card-audit and content: 04-n222/223/224, 04-n148, schema #67. The "UVM rates are calibrated off existing card costs, not playtested" caveat stands. Carve-out: five bare-prose PAs (NET.PA.4/5/6, SYN.PA.4/5) hold pending 04-n218/n220. Deferrals on record: Ghost **CA.11** (S156), **00a-80** (S157).
- **Art 04c** — v2.0, ✅ Signed Off S162 as an initial version; revisit before Art 04 signs off. Open questions at 04c-01.
- **Art 04b** — v2.7, Signed Off. · **Art 00a** — v0.13, Signed Off. · **Art 02** — v2.5, Signed Off.
- **Art 00c** — v0.7, a true index; content accuracy tracked at 00c-04.
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
- **PM01** — v1.7, Active. Not a sign-off artifact.
