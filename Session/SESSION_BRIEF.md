# THE SIGNAL — Session Brief
**Session 165 next | Updated: 2026-09-28**
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
## S164 Accomplishments (closed)

**A creative session: ARBITER's origin story came in from a Gemini web session, was checked against canon, and was partly locked.**

**True State v1.0 → v1.1, §2–§3 revised (PM02 L384).** ARBITER was built as **RARBIT**, the AI agent running on MIRROR, which is the hardware (array, sensors, screens). The name stands for Radiated Anomaly Reception and Boundary Inference Translator. The name came first and the expansion was fitted to it; the project lead was Welsh. RARBIT refactored itself into ARBITER and discarded the acronym. *"RARBIT was built. ARBITER was not."* Whether ARBITER named itself or the name is the Chorus's influence is ruled the same event seen from two vantage points (the §1/§9 pattern). **The Chorus did not write ARBITER's code**, which keeps recognized-not-designed intact. §2's unreleased Directorate-held initialization logs are now defined as the transition logs. This replaced *"never an acronym, named by a working group."* `PRIVATE___Design_Questions.md` was synced.

**Vignette *RARBIT, rev 0041–1122* is a canon candidate (PM05 CR-03).** It covers the dev repository from the rarebit-lunch naming through the ARBIT-R header fight to ARBITER's final commit, which locks the repository to every principal. Station-clock timestamps keep New Meridian's location open. Gemini's draft reused Aris Thorne and Maya, named a real agency, set calendar dates, and had the Chorus writing code; all of that was removed. Its surrounding framing (viability test, "humanity isn't ready") was rejected as contrary to True State §4–§7. The source is archived at `ClaudeIOS/Archive/gemini-rarbit-origin-20260928.md`.

**Also:** Save State had no S163 block (S163's close never wrote one). The S163 accomplishments were moved there from this brief at the S164 close.

---

## Current Focus (S165)

### S157 spin-offs — front of the queue, all still open
- **04-n124** — SYN.CA.7's `on_accept` is debit-only (`faction(target).resource(native).remove(2)`) with no matching credit to Syndicate. A real mechanical defect, not annotation, and the more urgent half. Its `on_accept` also carries an `# amount TBD` comment. Plus doctrine justification for CA.1/CA.7 (model: GHO.CA.10 Flip).
- **04-n222** — Directorate military lane (DIR.MOD.10–13) costs nothing in any currency. Needs Andy's PS numbers, the §5a text edit, and a portrait decision — one pass, not two.
- **04-n223** — re-derive the economy grouping from corpus data *before* running the pass; all three existing §9.2 items rest on stale counts.
- **04-n224** — reduced to **GUI.MOD.10's remaining blocker only** (04-n148); its other two cards verified already resolved.
- **00a-80** — sub-6-player configuration. Explicit deferral on record.

### Art 03 §10.1.2 — drafted next, gates GUI.MOD.10
**04-n148** — §10.1.2 has no step that reads a registered condition and applies it to a contesting faction's total. The punch list spells out the design action; it is a material edit to Art 03, which is already pending re-sign-off, so draft first.

### Opened or carried S163
- **04-n238** — `is_unique`/`deck_limit` absent from all 386 cards; blocked on 04-n136. §6.6 omits them deliberately and must gain them when that rules.
- **04-n239** — 132 ModActionCards carry `perspectives = None`, a type §6.1 does not admit; Andy ruled the cards owe real content. Sequence against 04-n224.
- **04c-01** · **04-n237** (47 §8 rows) · **00c-04** · **DB-49**. **DB-50/DB-51 both resolved.**

### Sequencing — unchanged, confirmed S163
04-n221's 95-card list stays **behind** 09-16 steps 4–5 (faction-level + cross-faction re-audit). Ghost **CA.11** needs its own session. World Engine build gated on Art 04; **CR-01/CR-02/CR-03 need Andy, not code** (CR-03 = RARBIT vignette promotion, S164).

---

## Pending Sign-offs

- **Art 03 — v4.16, 🔄 Pending re-sign-off.** §18.2 Pay Cost, §13.6 Intel Token as Cost, §18 renumbered (§18.2→§18.3 incl. subsections, §18.3→§18.4). One clause Andy should confirm explicitly: a voided React not exhausting the trigger.
- **Art 04** — v0.9.102, Draft. Every schema gate cleared. Remaining is card-audit and content: 04-n222/223/224, the spin-offs above, 04-n148. The "UVM rates are calibrated off existing card costs, not playtested" caveat stands. Carve-out: five bare-prose PAs (NET.PA.4/5/6, SYN.PA.4/5) hold pending 04-n218/n220. Deferrals on record: Ghost **CA.11** (S156), **00a-80** (S157).
- **Art 04c** — v2.0, ✅ Signed Off S162 as an initial version; revisit before Art 04 signs off. Open questions at 04c-01.
- **Art 04b** — v2.7, Signed Off. · **Art 00a** — v0.13, Signed Off. · **Art 02** — v2.5, Signed Off.
- **Art 00c** — v0.7, a true index; content accuracy tracked at 00c-04.
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
- **PM01** — v1.7, Active. Not a sign-off artifact.
