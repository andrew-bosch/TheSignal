# THE SIGNAL — Session Brief
**Session 167 next | Updated: 2026-09-29**
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
## S166 Accomplishments (closed)

**Art 02 v2.6 and Art 03 v4.18 both ✅ SIGNED OFF (PM02 L388, L389); 04-n222, 04-n148, 04-n224 closed.**

- **04-n222 — Directorate military lane priced in Public Standing (L386).** Premise corrected first: every ModBattleCard is free by design, `ps_framing` is unused corpus-wide, and PS is an effect, not a cost (Art 04c). Andy: government force reads as martial law.
  - DIR.MOD.1–3 (Riot Squad, Capital Suppression, City Council Loyalist) now cost **Mandate 1 + PS −1** per removal. All their design flags are closed and all three have narratives.
  - Hinders DIR.MOD.11/13 cost **PS −1/−2 at reveal** (`ModBattleExpr.ps_shift`, schema #68). The Boosts DIR.MOD.10/12 stay free. Portrait on 10–13 stays None. The §5a Portrait line is gone.
- **04-n148 — battlefield conditions (L387).** §10.1.2 Step 1.2.4: players, not ARBITER, claim a condition; if unclaimed it has no effect; it applies in every round, including presses.
  - §18.3.1: every persistent React lives on its player's Faction Resolution Grid.
  - Art 02 §8: React targets are stated aloud, and a Target Profile record is optional.
  - GUI.MOD.10 v0.2 is clean. VR=1 (Andy's judgment) and the notation is `battlefield_strength.add`. The corpus-wide `arbiter.` prefix question is logged as schema #69.
- **Art 03 review rulings:**
  - §18.2 is in numbered steps. Forfeiture is kept, and the voiding player may not re-present.
  - §13.6: an Expired token is always partial payment, provided `about=` holds; Intel Tokens handed over are lost even if invalid.
  - §9.5 signed off as drafted, with holes logged at **03-n27** (paired with Art 06).
- **Tooling:** permission allow rules added to `~/.claude/settings.json` so read-only commands, DB lookups and the sync script run through auto-mode classifier outages.

---

## Current Focus (S167)

### Start here
- **04-n223** — re-derive the economy grouping from corpus data *before* running the pass; all three existing §9.2 items rest on stale counts. Fresh topic, so start from a clean context.

### Open, needs Andy
- **schema #69** — ruling needed: should `arbiter.` mean ARBITER-performed only? It currently prefixes player actions corpus-wide (e.g. `arbiter.remove` on DIR.MOD.1–3).
- **03-n27** — §9.5 Covert Demand redesign (ARBITER keeps the CA card and resolves at N+1 regardless of response). Pair with Art 06.
- **00a-80** — sub-6-player configuration. Explicit deferral on record.

### Carried
- **04-n238** (`is_unique`/`deck_limit`, blocked on 04-n136) · **04-n239** (132 ModActionCards with `perspectives = None`) · **04c-01** (now also: the UVM prices self-PS losses as delivered value) · **04-n237** · **00c-04** · **DB-49** · **schema #67/#68** (§6 proposals, follow the cards).
- **04-n136** now holds the Target Profile supply question (Andy: settle with card counts and component inventory).
- **Unverified:** `card_status.art04_line` looks stale corpus-wide. Not yet logged.

### Sequencing — unchanged
04-n221's 95-card list stays **behind** 09-16 steps 4–5. Ghost **CA.11** needs its own session. World Engine build gated on Art 04; **CR-01/CR-02/CR-03 need Andy, not code**.

---

## Pending Sign-offs

- **Art 04** — v0.9.104, Draft. Every schema gate cleared. Remaining is card-audit and content: 04-n223, schema #67–#69. The "UVM rates are calibrated off existing card costs, not playtested" caveat stands. Carve-out: five bare-prose PAs (NET.PA.4/5/6, SYN.PA.4/5) hold pending 04-n218/n220. Deferrals on record: Ghost **CA.11** (S156), **00a-80** (S157).
- **Art 04c** — v2.0, ✅ Signed Off S162 as an initial version; revisit before Art 04 signs off. Open questions at 04c-01.
- **Art 03** — v4.18, ✅ Signed Off S166 (§9.5 holes at 03-n27). · **Art 02** — v2.6, ✅ Signed Off S166. · **Art 04b** — v2.7, Signed Off. · **Art 00a** — v0.13, Signed Off.
- **Art 00c** — v0.7, a true index; content accuracy tracked at 00c-04.
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
- **PM01** — v1.7, Active. Not a sign-off artifact.
