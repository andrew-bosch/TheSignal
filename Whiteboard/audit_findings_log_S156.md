# Audit Findings Log — 09-16 Steps 4–5 (opened S156)

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

## Triage summary (for PM05 09-17)

**23 findings total** across 5 factions + systemic. Rough routing (to be confirmed at 09-17):
- **design/systemic (Andy + PM02):** SYS-1 (Ghost intel economy), DIR win-path characteristic, GUI-2 defense scaling, NET-2/NET-3 (§9.2 Ghost-gating, PA.3 inversion), SYN-2 (Ghost dependency).
- **verify (confirm against source):** NET-1 tripwire, GUI-1/GUI-3/GUI-4 (§9.2 stale, 04-n2, CA.2), SYN-1/SYN-3/SYN-4 (§9.2 grouping, 04-n125, 04-n124).
- **blocked/gate:** GHO-1 (CA.11 / Art 06 — ties to Art 03-init).
- **schema → `schema_cleanup_log.md`:** DIR-1/DIR-2 (resolution_type), GHO-2/GHO-3, GUI-5, NET-4, SYN-5.
- **§9.2 pass (by bucket):** GUI-1, NET-2/3, SYN-1.
- **observations (no action, record for sign-off narrative):** SYS-2, SYS-3, SYS-4, and the many positive deltas (baseline gaps the modifier corpus closed).
