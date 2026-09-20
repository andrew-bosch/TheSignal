# THE SIGNAL — Session Brief
**Session 164 next | Updated: 2026-09-20**
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
## S163 Accomplishments (closed)

**Two Art 04 gates cleared and a React payment procedure written — and the session's own sweep introduced a defect that took three verification passes to surface.**

**04-n177 CLOSED (PM02 L381) — schema scaffolding swept corpus-wide, §6.6 Canonical Card Blocks added.** Andy's ruling: every §6.1 field is explicit on every card, absence is always a defect (the alternatives — documenting omit-defaults in §6.2, or splitting on the `Displayed` column — were rejected). 339 cards, 1,821 fields. **Two of the item's three S140 expansion premises were wrong:** `acquisition`/`generating_card` are not base-class fields at all and have carried an omit-unless-`Issued` default since **S133**, seven sessions before S140 logged them as defects; `outcome_type` was real but inverted (PublicAct 0/46 missing). Its `schema_cleanup_log item D` citation is stale. **§6.6** holds five synthetic exemplars, one per card class — numbered §6.6 because §6.4/§6.5 are taken and §6.5 is cited in hundreds of checklist rows. Art 04 → v0.9.102.

**The sweep corrupted 25 cards, and the fix explains DB-51.** The first insertion pass anchored by line number without tracking paren depth, so on cards with multi-line values it wrote fields *inside* the expression — 66 lines. It surfaced only when scoping 04-n124 returned SYN.CA.7's `on_decline` with a literal `on_discard = None,` embedded. Root cause of the count anomaly too: **a field nested inside an expression produces no `card_body` row** — the extractor folds it into the parent value silently. `card_body` 17,928 → **17,995**. `sync_card_db.sh` is exonerated; DB-50's S162 fix has no sibling. Script is now depth-aware. **Standing lesson, logged in `schema_reference.md`: an extractor that absorbs malformed input reports a smaller number, not an error.**

**Art 03 → v4.16, pending re-sign-off (PM02 L382).** **§18.2 Pay Cost** written — React cards had no payment step at all while **27** ModReactCards carry a real cost (04-n227's recorded 26 was stale). Public, all-or-nothing, `boost` extended to the subclass. Three questions the approved shape left open, all ruled by Andy: numbered **§18.2** not §18.1.1 (so Resolution → §18.3, Resume → §18.4, and §18.2 is written **flat** so no stale `§18.2.2` reference can resolve to a payment clause); a voided React takes **PS −1**; and a void **does not exhaust the trigger** — the next announcer in initiative order may present. **The larger find: Intel cost qualification had no home in Art 03 for any card type.** Three of four Intel-costed React cards demand a *qualified* token (`about=`, and DIR.MOD.9 also `status=`). Written once as **§13.6**, called from both §18.2 and §9.4.3.1.0.1 — 18 cards covered, not 4. **04-n227 RESOLVED; 04-n221's subclass-wide half closed.**

**GUI.MOD.10 unblocked (PM02 L383) — 04-n176 and `schema_cleanup_log` #53 CLOSED.** Andy reversed S137's *"redesign, don't invent a category"* — but by sequence, not force-fit: he **first simplified the card**, striking `direction.named` so the favor only ever *adds* (helping an ally and hindering a rival are the same move from opposite ends of the contest). That removed the shape that resisted classification. Taxonomy is `Resolution / Modify / BattlefieldStrength`, the Subject registered with `component_id = NULL` like `InfluenceTier`. **#53 closes as a side effect** — GUI.MOD.10 was the last ModReactCard carrying a live `target_freeform`; that is the item running out of instances, not the React-declaration design pass it asked for. **04-n148 deliberately NOT closed.**

**Also:** `ref_procedures.md` still said *"ARBITER decides tiebreakers"*, superseded at S150 and never synced — corrected. **04-n224 verified largely stale** (GUI.PA.10 rated, NET.MOD.3's TBD resolved, zero TBDs corpus-wide).

---

## Current Focus (S164)

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
04-n221's 95-card list stays **behind** 09-16 steps 4–5 (faction-level + cross-faction re-audit). Ghost **CA.11** needs its own session. World Engine build gated on Art 04; **CR-01/CR-02 need Andy, not code.**

---

## Pending Sign-offs

- **Art 03 — v4.16, 🔄 Pending re-sign-off.** §18.2 Pay Cost, §13.6 Intel Token as Cost, §18 renumbered (§18.2→§18.3 incl. subsections, §18.3→§18.4). One clause Andy should confirm explicitly: a voided React not exhausting the trigger.
- **Art 04** — v0.9.102, Draft. Every schema gate cleared. Remaining is card-audit and content: 04-n222/223/224, the spin-offs above, 04-n148. The "UVM rates are calibrated off existing card costs, not playtested" caveat stands. Carve-out: five bare-prose PAs (NET.PA.4/5/6, SYN.PA.4/5) hold pending 04-n218/n220. Deferrals on record: Ghost **CA.11** (S156), **00a-80** (S157).
- **Art 04c** — v2.0, ✅ Signed Off S162 as an initial version; revisit before Art 04 signs off. Open questions at 04c-01.
- **Art 04b** — v2.7, Signed Off. · **Art 00a** — v0.13, Signed Off. · **Art 02** — v2.5, Signed Off.
- **Art 00c** — v0.7, a true index; content accuracy tracked at 00c-04.
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
- **PM01** — v1.7, Active. Not a sign-off artifact.
