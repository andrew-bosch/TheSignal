# Audit Findings Log — 09-16 Steps 4–5 (opened S156)

> **✅ TRIAGED S157 — PM05 09-17 closed. Verdict: PM02 L358.** This file is now a historical record of what was found, not a live worklist. Per-finding dispositions are in the Triage Summary at the bottom. **Several findings below were overturned or corrected during triage** — do not cite a finding from the tables above without checking its disposition first. **Deletion trigger:** delete once the S157 spin-off items (00a-80, 04-n222/223/224, `schema_cleanup_log.md` #59–#63) are themselves closed, or sooner if PM02 L358 is judged to carry enough of the record.

**Purpose:** running collector for every issue surfaced during the faction-level (step 4) and cross-faction (step 5) card-set re-audits. Findings are **logged, not resolved** here (per `feedback_review_pass_scope`). Triage happens once, in the consolidated review (**PM05 09-17**), which then spins off reactive actions (schema fixes, design changes, Art 03 procedure items → 04-n221, etc.).

**Denominator for all audits:** faction-specific set **+ universal STD CA/PA pool** (STD ring mods conditional). Per 09-16 step-4 "STD+faction."

**Categories:** `[schema]` field/enum/notation · `[design]` balance/win-path/coverage question for Andy · `[verify]` claim to confirm against Art 03/other artifact · `[procedure]` Art 03 ARBITER-procedure gap (→ 04-n221) · `[playtest-watch]` intended tension to observe, not a defect.

**Audit ground rules (non-findings — do not flag as card gaps):**
- **Resource trade** (faction/district native **and** Intel tokens) is a **verbal table procedure** — anytime, and explicitly a quarter-end/Debrief activity, "any terms" (Art 03 §11.0; `ref_procedures.md:191`, `ref_resources.md:18`). It is *not* a card function. Never flag "faction X can't trade/sell/supply resource Y" as a card-set gap — trade is always available. (Corrects a stale S119–120 baseline claim about Ghost Intel.)
- **Treat the S119–128 baseline as "how the game was understood at S119," not ground truth.** The original audit writers did not necessarily have the full ruleset in view (the Intel-trade error is one proven case). Validate every baseline claim against *current* rules before repeating it, and do not treat baseline *agreement* as independent validation — re-derive regardless (`feedback_design_review_verification`).

---

## Directorate (S156)

| # | Cat | Finding | Detail |
|---|-----|---------|--------|
| DIR-1 | schema | CA.6 / CA.7 resolution mis-tag + undefined failure | Both `resolution=d100`, `threshold=50`, but `resolution_type=NULL` (siblings CA.2/CA.5 = `Probabilistic`). Both `fail=None` → no defined failed-roll outcome. |
| DIR-2 | schema | CA.8 resolution_type NULL | `resolution=Automatic` but `resolution_type=NULL` where CA.1/CA.3/CA.4 carry `Transactional`. Minor consistency. |
| DIR-3 | verify | Core-structure adjacency modifier-draw engine | §5a promises "+1 modifier card per adjacent district at Established." No card visibly implements it — confirm it's an Art 03 procedure or flag as unbuilt §5a promise. |
| DIR-4 | verify | Battle-MOD Portrait cost | §5a says the military lane "costs Portrait." Confirm Battle MOD.10–13 actually wire a Portrait cost. |
| DIR-5 | playtest-watch | Mandate single-pool tension | Suppression (bespoke) and establishment (STD cards billing native Mandate) draw the same pool. Intended tension for a control faction; watch in playtest, not a coverage gap. |
| DIR-6 | design | Expansion is generic, not differentiated | Directorate establishes via the shared STD pool; only suppression is faction-specific. Doctrine-consistent ("suppression over construction") — logged as a deliberate characteristic to confirm with Andy, not a defect. |

## Ghost (S156)

| # | Cat | Finding | Detail |
|---|-----|---------|--------|
| GHO-1 | design/reimagine | CA.11 Signals Analysis needs full reimagining | **Andy S156: the card may not even be valid — its mechanism isn't defined, and it depends on the undesigned Classified Directive subsystem (Art 06 §10 is a non-canonical stub; content home Art 05-vs-08 undecided; no deduction/reveal procedure).** Not a fix or a carve-out — CA.11 needs to be *reimagined from scratch*, tied to whatever Ghost's "act on hidden objectives / suppress premature consensus" endpoint should mechanically be. **Does NOT gate Art 04 sign-off in its current undefined state.** Redesign item for a future session. |
| GHO-2 | schema | GHO.MOD.1 value_rating string | Stored as string `"None"` rather than int/NULL. One of the 6 partial cards. |
| GHO-3 | schema-minor | GHO.CA.11 value_rating NULL | Minor. NB: CA.11 is *no longer* the stale `id=TBD` row (04-n172) — now v1.0, `resolution_type=Probabilistic` correct; the memory pointer is outdated. |

*(Dropped a provisional "no Intel-trade card" finding — free trade is a verbal procedure, see ground rules above. Ghost↔Syndicate Intel supply is a step-5 relationship, not a gap.)*

**Positive deltas since baseline (not flags — record for the step-5 / sign-off narrative):** single-Flip-endpoint gap CLOSED (CA.14/PA.1/CA.15 + DA-01/DA-02); passive-Intel-generation gap 04-n143 CLOSED (MOD.2/3/4). Both closed by the modifier corpus that postdates the S119–120 baseline.

## Guild (S156)

| # | Cat | Finding | Detail |
|---|-----|---------|--------|
| GUI-1 | verify | §9.2 baseline stale — Guild has a real cross-resource ceiling | S122 recorded Guild as zero-cross ("inversion, same as Directorate," 04-n119) and grouped it with Directorate/Syndicate for a mono-economy pass. Current corpus has 12 cross-cost cards (PA.9 uses 4 resource types). Guild is NOT mono. Update the §9.2 understanding; revisit 04-n119 and the grouping recommendation. |
| GUI-2 | design/balance | Defense may not scale | Validated & softened from S122 FLAG 2. CA.1 protects one structure/Quarter, PA.3 recovers first-lost, MOD.6 React-rebuilds — deeper than baseline, but a rival demolishing several Guild structures in a Quarter can outpace protection. Playtest/balance watch, not a coverage gap. |
| GUI-3 | verify | Passive-income rule 04-n2 status | React MOD.2/3/4/8/9 now implement "others build → Guild paid." Confirm the trigger fully matches §5a ("+1 Capacity when opponent completes STD.CA.1 in a Guild-presence district") and whether the governing-rule item 04-n2 can close. |
| GUI-4 | verify | GUI.CA.2 payout mismatch | S122 flagged code/comment payout mismatch (2 Capacity vs 1 Capacity+district-native). Current cost `None` (payout in effect). Confirm resolved, not relocated. |
| GUI-5 | schema | Partial/stub cards | GUI.MOD.10 (`func/subject=None`, `value_rating=None`); GUI.PA.10 (`cost_type=NULL`, `value_rating=None`). Among the known partial cards. |

**Positive deltas since baseline:** Standing absence (FLAG 3) CLOSED (PA.4/8/9); no-territorial-removal (FLAG 4) CLOSED (CA.7/CA.8); passive income (04-n2) implemented; deck feel upgraded Partial→✓.

## Network (S156)

| # | Cat | Finding | Detail |
|---|-----|---------|--------|
| NET-1 | design/§5a | Tripwire = stale terminology → §5a rewrite | ✅ **DONE (S156, PM02 L355).** "Tripwire" was the pre-ModReact name for certain React effects — predates the ModReact card set; no separate mechanic to build. §5a Network section rewritten in Part1_Core (dropped the tripwire bullet + "tripwire fires"; centered the React modifier engine as Network's defining system). Monolith regenerated. Not a 09-17 item — closed. |
| NET-2 | design/§9.2 | Structural Findings-dependency (Ghost-linked) | CA.1/2/4/8 — Network's core broadcaster cards all cost Findings (Ghost's native). Deeper than S123 (was CA.1/2). Degrades toward mono in Ghost-absent games (04-n126). Intended Ghost-link? Step-5 (Network↔Ghost). |
| NET-3 | design/§9.2 | NET.PA.3 borderline inversion + anti-Guild toothlessness | Seasonal covert-disable at mono Exposure×2; toothless vs Guild (no covert ops to forfeit). Persists from S123. Validate in §9.2 pass. |
| NET-4 | schema/stub | Known stubs | NET.CA.8 Fake News (`cost` amount NULL; 04-n217); NET.MOD.3 (`cost_primary_amount` NULL). |

**Positive deltas since baseline:** modifier self-feed "true engine" (largest §5a gap) BUILT (MOD.7/9/14 + CA.2); reactive presence engine BUILT (MOD.1/4/5/6/8); territorial response CLOSED (PA.4, MOD.10, CA.8); deck feel upgraded Partial→✓.

## Syndicate (S156)

| # | Cat | Finding | Detail |
|---|-----|---------|--------|
| SYN-1 | verify/§9.2 | Mono-Capital confirmed; grouping correction | Mono-economy §9.2 group is {Directorate, Syndicate}, NOT Guild (per GUI-1). Big mono inversions persist (CA.8 C×6, CA.10 C×3); CA.3 gained cross-costs since baseline (partial de-inversion). Feed the §9.2 pass. |
| SYN-2 | design | Ghost-Intel dependency for premium plays | CA.3 (Findings), CA.7 (Intel) — §5a "Ghost structural link." Mirrors NET-2. Step-5: Ghost is the Intel hub for BOTH Syndicate and Network. |
| SYN-3 | verify | Accord-formation now exists (04-n125) | CA.12 Boilerplate architecturally closes the "entirely parasitic / no formation card" gap, but is a stub (04-n219). Confirm 04-n125 can close once CA.12 is completed. |
| SYN-4 | verify | Non-native generation documentation (04-n124) | CA.1/CA.7 taglines now carry narrative rationale. Confirm the doctrine-documentation item is satisfied. |
| SYN-5 | schema/blocked | CA.5 NamedActionType + known stubs | CA.5 subject `NamedActionType` still unregistered (schema_cleanup #27) — §5a bottleneck. Also: SYN.CA.12 (04-n219), SYN.PA.4/5 bare-prose success (04-n220), Portrait `flat=` misuse (schema_cleanup #7), SYN.MOD.1 The Fixer value_rating None. |

**Positive deltas since baseline:** Accord-formation card added (CA.12, addresses 04-n125); React passive-Capital engine built (MOD.2/3/4/5/7); all §5a Capital-application lanes now carded (bypass CA.4, hostile takeover CA.9, deferred PA.2, Accord transfer CA.10).

---

## §9.2 grouping (cross-audit synthesis, for the §9.2 pass / step 5)

The baseline's mono-economy grouping (Directorate+Guild+Syndicate) is corrected to three buckets:
- **Mono (inversion by doctrine):** Directorate (Mandate), Syndicate (Capital).
- **Native-cross:** Guild (Capacity + Capital/Mandate/Findings/Exposure on big builds) — left the mono set.
- **Foreign-gated cross:** Ghost (flip-cost model — target's own resources), Network (Findings-gated — Ghost's native).

## Cross-faction / systemic (S156, step 5) — doc `Whiteboard/cross_faction_synthesis_S156.md`

| # | Cat | Finding | Detail |
|---|-----|---------|--------|
| SYS-1 | design/systemic | Intel economy assumes Ghost at the table | 19 non-Ghost cards (Network 7, Syndicate 7, Directorate 5) are gated on Findings/Intel — Ghost's native output. Ghost is the resource hub/broker (via free trade). In Ghost-absent 2–4p games these 19 cards degrade (4:1 conversion / foreign-district only). Generalizes NET-2 / 04-n126 — needs a deliberate design decision. |
| SYS-2 | observation | Standing is STD-provided | 16 STD Standing cards vs 2–5 per faction. Factions are standing-thin without the shared pool — confirms the STD+faction denominator is load-bearing. Not a defect; validates the scope correction. |
| SYS-3 | observation/design | Resolution is the rarest layer | 5 faction cards total (1 each DIR/GHO/GUI; 0 NET/SYN) + 2 STD. Deliberate niche or system-wide under-use — worth a deliberate call. |
| SYS-4 | observation | Free-trade rule is load-bearing but uncarded | All the Ghost-hub dependencies resolve through Art 03 §11.0 verbal trade. A core economic subsystem lives in table procedure, not the card set (by design) — ensure prominence in rules teaching. |

**Differentiation verdict:** ✓ five distinct decks/control poles, no adjacent-pair collapse (stronger than baseline). **§9.2 buckets:** mono {DIR, SYN} · native-cross {GUI} · foreign-gated cross {GHO, NET}. **Two genuine open items above schema noise:** GHO CA.11 (Art 06 block), NET Tripwire (verify).

---

## Triage summary — COMPLETE S157 (PM05 09-17 closed; verdict PM02 L358)

**Corrected count: 27 findings logged, 26 live** (NET-1 closed at S156). The original "23 findings total" below counted only the five faction tables and omitted SYS-1..4; SESSION_BRIEF's "22" was that 23 minus NET-1.

### Dispositions

| # | Disposition |
|---|---|
| DIR-1 | **Split.** `resolution_type` half → `schema_cleanup_log.md` **#59**, reframed corpus-wide (46 cards). "`fail = None` leaves failure undefined" half **dropped — not a defect**: 35 of 44 d100 cards use `fail = None`, including DIR.CA.2, the sibling this finding cites as correct. |
| DIR-2 | → **#59** (same item). |
| DIR-3 | **CONFIRMED UNBUILT → resolved by cutting the claim.** The §5a line was the only occurrence in all of V1. At real Core adjacency degrees (4/6/6/4) against a 3-card draw ceiling it would have been a second, larger modifier economy. Andy: cut. Executed S157. |
| DIR-4 | **CONFIRMED UNBUILT → 04-n222.** Verified `cost`, `portrait` *and* `ps_framing` all `None` on DIR.MOD.10–13. Andy overturned the §5a premise: military action is Directorate doctrine executing — it should cost **Public Standing**, not Portrait, and may earn Portrait. Scoped as one pass (§5a edit + 4 cards). |
| DIR-5 | Playtest-watch, unchanged. No action. |
| DIR-6 | Folded into 04-n223's economy re-derivation — "expansion is generic" is a claim about Directorate's economic profile, which the cost data now contradicts. |
| GHO-1 | Unchanged — CA.11 reimagining, own session, explicitly non-gating. `value_rating` half → **#60**. |
| GHO-2 | → **#60**. |
| GHO-3 | → **#60**. Its note that CA.11 is no longer the stale `id=TBD` row **verified correct** (`d100`/`Probabilistic`). |
| GUI-1 | **CONFIRMED STALE — and its replacement is stale too.** → **04-n223**. Guild has 10 cross-cost cards (not the 12 claimed), 50% of its costed set, highest of any faction; PA.9's four resource types confirmed. |
| GUI-2 | Defense scaling — carried as a balance/playtest watch, unchanged. |
| GUI-3 | **CONFIRMED DIVERGENT → cards win.** All five MODs carry `restriction = None`; no presence gate, no STD.CA.1 specificity, MOD.9 not structure-triggered at all. Andy: fix the text. §5a rewritten S157; **04-n2 closed as superseded**. |
| GUI-4 | **RESOLVED → closed.** Payout mismatch genuinely gone (v1.1, `cost = None`, flat 2 Capacity). Notation residue only → **#63**. |
| GUI-5 | **Split and partly corrected.** `value_rating` → **#60**; GUI.MOD.10's unassigned taxonomy → **04-n224**. Its `cost_type = NULL` claim is **wrong** — cost is populated and `cost_type` is not a schema field. |
| NET-1 | Closed S156 (§5a rewrite, PM02 L355). Not a 09-17 item. |
| NET-2 | **Downstream of configuration → 00a-80** (systemic half) and 04-n223 (economy half). |
| NET-3 | → **04-n223**. |
| NET-4 | **Corrected.** Both field citations wrong (NET.CA.8's cost is populated; `cost_primary_amount` is not a schema field). Real defect is NET.MOD.3's `add(TBD)` → **#62** and **04-n224**. NET.CA.8's actual gaps stay at 04-n217. |
| SYN-1 | **Partly stale → 04-n223.** Deep inversions confirmed (CA.8 C×6, CA.10 C×3, CA.3 C×3), but the mono framing does not survive: Syndicate has 10 cross-cost cards, and 04-n123's "zero" is false. |
| SYN-2 | → **00a-80** (mirrors NET-2). |
| SYN-3 | **Closed.** 04-n125 was already ✅ S130; CA.12's stub state is 04-n219's scope, nothing new. |
| SYN-4 | **NOT satisfied → 04-n124 stays open.** Taglines are mechanical descriptions, not doctrine justification. And the live half: SYN.CA.7's `on_accept` is still debit-only, with no credit expression to Syndicate — a mechanical defect. |
| SYN-5 | **Split; two citations corrected.** `NamedActionType` → new **#61** (it was routed to #27, which is DIR.CA.8's `Difficulty` — different card). Portrait `flat=` **dropped**: schema #7 fully closed S150, zero instances remain corpus-wide. SYN.MOD.1 `value_rating` → #60. CA.12 → 04-n219; PA.4/5 → 04-n220 (and NET.PA.4/5/6 → 04-n218). |
| SYS-1 | **REFRAMED by Andy → 00a-80.** Not an intel-economy defect — the first concrete symptom of the undesigned sub-6-player configuration. The card degradation is real only under "exclude the faction"; the other three candidate configurations largely dissolve it. Gates smaller-group playtest, not Art 04. |
| SYS-2 | Observation, recorded for the sign-off narrative. No action. |
| SYS-3 | Observation (Resolution is the rarest layer) — worth a deliberate call eventually, not spun off this pass. |
| SYS-4 | Observation (free-trade rule load-bearing but uncarded) — carry into rules teaching. No action. |

### Spun-off items

**PM05:** 00a-80 (sub-6-player configuration) · 04-n222 (Directorate military lane) · 04-n223 (§9.2 re-derivation) · 04-n224 (remaining partial cards) · 04-n2 closed · 04-n119 premise-noted · 04-n123/126 flagged stale · 04-n124 re-opened in substance · 09-17 closed.

**`schema_cleanup_log.md`:** #59 `resolution_type` absent (46 cards) · #60 `value_rating` unset (8) · #61 `NamedActionType` unregistered · #62 the one live `TBD` · #63 GUI.CA.2 notation residue.

**Art 03 procedure gaps → 04-n221:** none. No finding in this log turned out to be an Art 03 coverage gap — DIR-3 was cut rather than proceduralised, and GUI-3 resolved to card-carried rather than a standing rule.
