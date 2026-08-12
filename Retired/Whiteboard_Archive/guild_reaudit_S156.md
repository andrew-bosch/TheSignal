# Guild Card Set Re-Audit — S156 (PM05 09-16 step 4)

**Status:** First-pass analysis, awaiting Andy checkpoint before continuing to Network→Syndicate.
**Trigger to delete:** once findings are triaged via the consolidated review (PM05 09-17) and the faction verdict is logged to PM02.
**Denominator:** 20 Guild operations (10 CA + 10 PA) + 26 Guild MOD (12 Action, 4 Battle, 10 React) + universal STD CA/PA pool. STD ring mods conditional.
**Substrate:** `card_body` / `v_card_body` / `card_status` / `card_checklist`, re-derived, checked against `card_analysis_summary_S119-128.md` (S122, 04-n92) — treated as an S119 snapshot, every claim re-validated against current rules.
**Doctrine source:** Art 04 Part1_Core §5a (Guild); win = *structures on board.* "What you build reveals what you are." Cannot operate covertly in principle. Economy: Capacity, compounded via GUI.CA.5.

---

## Dimension verdicts

| Dimension | Verdict | Note |
|-----------|---------|------|
| Deck feel | ✓ (was "Partial" at S122) | Heavy, deliberate, permanent — now backed at scale. Full 46-card set; only the Information layer is empty (doctrinally correct — Guild isn't covert/informational). Upgrade driven by the modifier corpus + set growth since baseline. |
| Doctrine coherence | ✓ | Build-first / compound-income / permanence-as-win all expressed. CA cards use the shared covert *dispatch* procedure but resolve to public structures/presence — consistent with "the procedure is shared; the doctrine is not." |
| Layer coverage | ✓ | Territory-dominant + Economy (compound) + Standing (PA.4/8/9, filled since baseline) + Submission (CA.4, PA.5) + Resolution (CA.9). Information deliberately empty. |
| Win-path support | ✓ (strongest structural engine in the set) | Foundation Rights → high-tier builds → CA.5 compounds → defense → salvage. One residual balance watch (defense scaling). |
| §9.2 economics | ✗ **baseline overturned** | Guild has an **extensive cross-resource ceiling** — NOT the zero-cross inversion S122 claimed. See below. |
| **Implied strategies** | mostly THICK | One baseline gap (passive income) now closed; defense-scaling the residual. |
| **Leverageable strategies** | rich, high STD-leverage | Parasitic construction economy + infrastructure-landlord + coalition builder. |

---

## §9.2 economics — baseline overturned (primary validation finding)

S122 recorded Guild as a **zero-cross-resource-cost** faction ("§9.2 inversion, same shape as Directorate," 04-n119) and recommended running the cross-resource pass across Directorate/Guild/Syndicate together (04-n118/119/123). **That is no longer true against the current corpus** — Guild is now saturated with cross-costs:

- CA.4 (Capacity+Findings), CA.7 (Capacity+Capital), CA.8 (Capacity+Mandate), CA.9 (Capacity+district-native), CA.10 (Capacity×4+district-native), PA.1 (Capacity+Capital+Mandate), PA.3 (Capacity+Mandate), PA.4 (Capacity+Exposure), PA.5 (Capacity+Findings+Capital), PA.7 (Capacity+Mandate), PA.9 (**Capacity+Capital+Exposure+Mandate** — four types), PA.10 (Capacity+faction-native).

Guild's higher-tier builds **deliberately draw on non-native resources** (materials, permits, labor across currencies), which Guild sources by holding foreign-native districts (`ref_resources.md:18`), trade (Art 03 §11.0), or 4:1 conversion. This is a *real, doctrine-consistent cross-resource ceiling*, not an inversion. **Correction: Guild does not belong in the Directorate/Syndicate mono-economy grouping.** (Clean example of an S119-era baseline claim invalid against current rules.)

---

## Win path — structure engine thick; defense the one watch

Win = structures on board. Support is the strongest structural engine audited so far:
- **Build:** CA.3 Foundation Rights (near-auto Ring 0, thr25) → CA.10 (cost-4 permit), PA.1 (dual-district program, vr4), CA.4 (build-before-established), MOD.6 (React build), CA.9 (both sites).
- **Compound income:** CA.5 Infrastructure Yield (free, draws from built infrastructure) + CA.2/CA.6 salvage (free) + React MOD.2/3/4/8/9 (parasitic — see leverageable).
- **Defense/recovery:** CA.1 Fortify (protect one/Quarter), PA.3 (first-lost-structure returns), MOD.6 (React rebuild — "you can't erase the blueprint").

**Residual balance watch — defense scaling (validated, softened from FLAG 2):** defense is materially deeper than at baseline (3 tools vs. ~1), and MOD.6 now gives a React answer to demolition the baseline said didn't exist. But it may still not *scale* — CA.1 protects a single structure/Quarter, PA.3 recovers the *first* loss; a rival demolishing several Guild structures in a Quarter can still outpace Guild's protection. Balance/playtest question, not a coverage gap.

---

## Implied strategies — §5a claims rated

| §5a claim | Rating | Evidence |
|-----------|--------|----------|
| Build deep, compound via CA.5 | **THICK** | CA.5 + full build suite. |
| Permanence over adaptation | **THICK** | Permanent structures + defense/recovery. |
| Passive income from others' building | **THICK (now)** | React MOD.2/3/4/8/9. **Baseline 04-n2 "unimplemented governing rule" — now implemented as modifier cards.** Verify the trigger fully matches §5a's "+1 Capacity when opponent completes STD.CA.1 in a Guild-presence district" and whether 04-n2 can close. |
| Everything leaves a physical artifact | **THICK** | No Information layer; all Territory/Economy/board-visible. |
| Defense of structures | **ADEQUATE, non-scaling** | See balance watch. |

---

## Leverageable strategies — emergent (feed step-5 cross-faction)

**Faction-internal:**
1. **Parasitic construction economy (high STD-leverage).** React MOD.2/3/4/8/9 turn *every other faction's* building — done via the universal STD.CA.1 — into Guild income. Guild literally taxes the table's construction. Its passive engine is *coupled to the STD pool*, the opposite of Ghost's self-sufficiency.
2. **Infrastructure landlord.** PA.6 (sell a structure to a rival, priced in *their* currency) + PA.2 (extend infrastructure investment as a formal Accord) → Guild monetizes structures cross-faction and converts builds into others' resources.
3. **Ring-expansion override.** PA.5 (blanket override of Ring expansion limits for the Quarter) unlocks aggressive multi-ring building beyond normal placement rules.
4. **Coalition builder.** PA.2 + PA.10 (joint development with an ally) + Accord engine (PA.2 vr4) → Guild forms infrastructure-based coalitions.
5. **Threshold-stacking** (Action MODs) de-risks Guild's few Probabilistic cards (CA.3 thr25, CA.4 thr65, CA.8 thr60, PA.9 thr40, PA.10 thr50).

**Cross-faction (step-5):** Guild's parasitic income means it *benefits* from a build-heavy table (esp. Directorate's Core structures, Syndicate's infrastructure). Its structure-sale (PA.6) and joint-development (PA.10) lanes give it transactional hooks into every faction. Guild↔Directorate is notable: Directorate's Core structures trigger Guild's MOD.3/4 income.

---

## Flags (→ running log `audit_findings_log_S156.md`)

- **[design/balance]** Defense scaling — validated, softened from FLAG 2. Deeper than baseline but may not scale to a large structure count under multi-demolition. Playtest/balance watch.
- **[verify]** §9.2 baseline claim (zero-cross / Directorate-grouping) is **stale** — Guild now has an extensive cross-resource ceiling. Update the §9.2 understanding; Guild is not a mono-economy faction. (Also revisit 04-n119.)
- **[verify]** Passive-income rule 04-n2 — confirm React MOD.2/3/4/8/9 fully implement the §5a trigger and whether 04-n2 can close.
- **[verify]** GUI.CA.2 — baseline flagged a code/comment payout mismatch (2 Capacity vs 1 Capacity+district-native); current cost is `None` (free, payout in effect). Confirm the mismatch is resolved, not just relocated.
- **[schema]** GUI.MOD.10 (React) — `func/subject=None`, `value_rating=None`; GUI.PA.10 — `cost_type=NULL`, `value_rating=None`. Both among the known partial/stub cards.

---

## Convergence with S122 baseline

- Deck feel — **upgraded** Partial → ✓ (set filled, layers covered, defense deepened) since the modifier corpus + set growth.
- Doctrine coherence ✓ — **agree, re-derived.**
- **§9.2 zero-cross (FLAG 5 / 04-n119)** — **OVERTURNED** by current corpus (extensive cross-costs). Primary validation finding.
- **Passive income (04-n2)** — **CLOSED/addressed** (React MOD.2/3/4/8/9).
- **Standing absence (FLAG 3)** — **CLOSED** (PA.4/8/9).
- **No territorial removal (FLAG 4)** — **CLOSED** (CA.7 remove-presence, CA.8 remove-structure).
- **Defense scaling (FLAG 2)** — **persists, softened** (balance watch).
