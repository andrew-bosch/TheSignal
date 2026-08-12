# Syndicate Card Set Re-Audit — S156 (PM05 09-16 step 4)

**Status:** First-pass analysis complete (final faction). Awaiting Andy checkpoint before step 5 (cross-faction synthesis).
**Trigger to delete:** once findings are triaged via the consolidated review (PM05 09-17) and the faction verdict is logged to PM02.
**Denominator:** 17 Syndicate operations (12 CA + 5 PA) + 27 Syndicate MOD (12 Action, 4 Battle, 11 React) + universal STD CA/PA pool. STD ring mods conditional.
**Substrate:** `card_body` / `v_card_body` / `card_status` / `card_checklist`, re-derived, checked against `card_analysis_summary_S119-128.md` (S123, 04-n91) — baseline treated as an S119 snapshot, re-validated.
**Doctrine source:** Art 04 Part1_Core §5a (Syndicate); win = *Dominant in Ring 1/2 economic spine.* Capital-only economy (no native secondary); infrastructure ownership; "control comes from positioning early."

---

## Dimension verdicts

| Dimension | Verdict | Note |
|-----------|---------|------|
| Deck feel | ✓ Full | Wealthy, patient, restructures deals from underneath. Capital saturation, deepest Accord-manipulation suite (CA.10/11, MOD.1/11), Beat-2 patience, + a React passive-Capital engine. Baseline's strongest match, held. |
| Doctrine coherence | ✓ Strong | Every §5a Capital-application lane is now carded — see below. |
| Layer coverage | ✓ | Economy-dominant + Territory (acquisition) + Submission (CA.5, MOD.6/10) + Information (PA.3, CA.11, MOD.11) + Standing (PA.4, MOD.9). Resolution empty — doctrinally correct (Syndicate *buys past* dice via CA.4 bypass, doesn't manipulate them). |
| Win-path support | ✓ (clearest in the set) | Ring 1/2 Dominant has the most direct support of any faction: CA.3, CA.8, CA.9, PA.1, PA.2, MOD.8. |
| §9.2 economics | mono-Capital (inversion by doctrine) | Confirmed mono group with **Directorate** — **not** Guild. See below. |
| **Implied strategies** | THICK across the board | All Capital lanes carded; Accord-formation gap now addressed. |
| **Leverageable strategies** | rich, transactional | Deal-restructuring, hostile takeover, Ghost-Intel-fed premium plays. |

---

## Doctrine coherence — every §5a Capital lane now has a card (primary finding)

§5a lists Syndicate's Capital-application lanes; all are now implemented:
- **Direct card costs** — the whole set (mono-Capital).
- **Deferred investment returns** — PA.2 (rewards whoever holds Dominance next Upkeep), CA.8 Land Title (C×6: "let someone else build, then collect").
- **Bypass payments (negate enforcement without a dice roll)** — CA.4 ("declare a bribe… windfall or nullification — the Capital leaves either way").
- **Hostile takeover (replace presence at equivalent tier)** — CA.9 ("purchase control… replacing their tokens with Syndicate's at equivalent tier"), PA.1 (public purchase offer).
- **Accord Transfer (Syndicate alone transfers accords)** — CA.10 ("all terms remain binding; the signatories have been updated").
- **Proxy funding via Network** — the shadow relationship (step-5).

Plus a React passive-Capital engine (MOD.2/3/4/5/7 — "every Accord is a market event," "public success creates private wealth") that generates Capital off the table's activity, reinforcing the Q1-saturation feel.

---

## §9.2 economics — mono-Capital, and the grouping correction

Syndicate is a **Capital-only economy (no native secondary)**, so it pays Capital for nearly everything — the §9.2 inversion pattern (expensive effects at single-resource cost). The big inversions persist: **CA.8 (C×6, land claim), CA.10 (C×3, permanent Accord party swap)**. A handful of cards gained cross-costs (CA.3 Capital+Findings+Exposure, CA.5 Capital+Exposure, CA.9 Capital+Mandate, CA.12 Capital+Mandate) and the Ghost-linked ones use Intel (CA.7) / Findings (CA.3).

**Grouping correction for the §9.2 pass / step 5:** the baseline recommended a mono-economy cross-resource pass over **Directorate + Guild + Syndicate**. This audit series finds the real mono group is **{Directorate, Syndicate}** — Guild is now cross (GUI-1). Ghost and Network are the two cross-ceiling exceptions (Ghost by flip-cost design; Network Findings-gated). So §9.2 sorts into three buckets: **mono {Directorate, Syndicate}** · **native-cross {Guild}** · **foreign-gated cross {Ghost flip, Network Findings}**.

---

## Implied strategies — §5a claims rated

| §5a claim | Rating | Evidence |
|-----------|--------|----------|
| Capital accumulation, Q1 saturation | **THICK** | Mono-Capital economy + React passive Capital (MOD.2/3/4/5/7). |
| Infrastructure ownership / Ring 1/2 Dominant | **THICK** | CA.3/8/9, PA.1/2, MOD.8 — clearest win-path support in the set. |
| Deepest Accord manipulation | **THICK** | CA.10/11, MOD.1/11 (corrupt/transfer/remove). |
| Accord *formation* (baseline gap: parasitic-only) | **ADDRESSED (stub)** | CA.12 Boilerplate now forms Accords — architecturally closes 04-n125's "no formation card," but CA.12 is the known stub (04-n219). |
| Bypass / hostile takeover / Accord transfer | **THICK** | CA.4 / CA.9 / CA.10. |
| Ghost structural link (Intel-gated premium plays) | **PRESENT** | CA.3 (Findings), CA.7 (Intel). Step-5. |

---

## Leverageable strategies — emergent (feed step-5 cross-faction)

**Faction-internal:**
1. **Deal restructuring from underneath.** Accord suite (CA.10 transfer, CA.11 corrupt, MOD.1 remove, MOD.11 corrupt) lets Syndicate rewrite the table's agreements — every bilateral Accord is a potential Syndicate asset. Signature identity.
2. **Buy the board.** CA.3 (seize structure), CA.8 (land claim), CA.9 (hostile takeover), PA.1 (purchase presence), MOD.8 ("buy when there's blood in the streets") — Capital converts directly to territory/Dominance without dice.
3. **Enforcement immunity.** CA.4 bypass makes Syndicate hard to police for factions relying on Probabilistic enforcement (esp. Directorate's suppression) — Capital buys out risk.

**Cross-faction (step-5):**
4. **Syndicate↔Ghost (the §5a structural link).** Premium plays (CA.3, CA.7, + battle-winner mods) need Findings/Intel — Ghost's native. Ghost is thus the Intel hub for **both** Syndicate and Network (see NET-2), a major cross-faction pattern: Ghost's over-collection becomes leverage over two factions' ceilings, transacted via free trade.
5. **Syndicate↔Network proxy funding** (§5a "lateral bypass around Directorate visibility") — shadow economic link.
6. **Syndicate↔Directorate tension.** CA.4 bypass directly counters Directorate's Probabilistic suppression; CA.9 (needs Mandate) and Syndicate's Ring-1/2 push collide with Directorate's "no faction Dominant" win-leg. A natural antagonism for step 5.

---

## Flags (→ running log `audit_findings_log_S156.md`)

- **[verify/§9.2]** Mono-Capital confirmed; grouping correction — mono = {Directorate, Syndicate}, not Guild. Feed the §9.2 pass. CA.3 gained cross-costs since baseline (partial de-inversion); CA.8/CA.10 inversions persist.
- **[design]** Ghost-Intel dependency for premium plays (CA.3 Findings, CA.7 Intel) — §5a Ghost link; mirrors Network. Step-5 (Ghost = Intel hub for two factions).
- **[verify]** Accord-formation CA.12 addresses 04-n125 architecturally but is a stub (04-n219) — confirm 04-n125 can close once CA.12 completed.
- **[verify]** Non-native generation doctrine documentation (04-n124, CA.1/CA.7) — taglines now carry narrative rationale; confirm the documentation item is satisfied.
- **[schema/blocked]** CA.5 subject `NamedActionType` still unregistered (schema_cleanup #27) — §5a bottleneck (blocks the block-action-type play). Plus known stubs: SYN.CA.12 (04-n219), SYN.PA.4/5 bare-prose success (04-n220), Portrait `flat=` misuse (schema_cleanup #7), SYN.MOD.1 The Fixer value_rating None.

---

## Convergence with S123 baseline

- Deck feel ✓ Full, doctrine ✓ Strong, win-path clearest — **agree, re-derived.**
- **§9.2 zero-cross / mono (04-n123)** — **agree** (mono-Capital), with the grouping correction (Guild leaves the mono set; Syndicate stays with Directorate).
- **Accord parasitic / no formation card (04-n125)** — **addressed**: CA.12 Boilerplate is now a formation card (stub-gated on 04-n219).
- **Non-native generation rationale (04-n124)** — taglines now carry rationale; **verify** the documentation item.
- **Intel self-sufficiency question** — resolves into the step-5 Ghost-Intel-hub pattern (Ghost supplies both Syndicate and Network via free trade).
- **High open-issue density (S123)** — largely worked down since the S154 full-corpus Design Pass; residual items are the tracked stubs/schema flags above.
