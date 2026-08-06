# Directorate Card Set Re-Audit — S156 (PM05 09-16 step 4)

**Status:** First-pass analysis, awaiting Andy checkpoint before replicating to Ghost→Guild→Network→Syndicate.
**Trigger to delete:** once findings are triaged via the consolidated review (PM05 09-17) and the faction verdict is logged to PM02.
**Denominator (corrected S156):** the *full set available to Directorate* = 44 Directorate-specific cards **+ the universal STD pool (16 STD.CA + 9 STD.PA, available to every faction)**. STD ring modifiers (STD.MOD.n, drawn at Upkeep on board conditions) are a *conditional* shared resource, not a faction differentiator — noted where relevant, not enumerated. This matches the 09-16 step-4 definition ("STD+faction") and the original `card_analysis_STD_*` file naming.
**Substrate:** `card_body` / `v_card_body` / `card_status` / `card_checklist` (the_signal_db), re-derived fresh, then checked against `card_analysis_summary_S119-128.md` (S121, 04-n89).
**Doctrine source:** Art 04 Part1_Core §5a (Directorate); win = *Established in more districts than any other faction + no faction Dominant anywhere.*

---

## Dimension verdicts

| Dimension | Verdict | Note |
|-----------|---------|------|
| Deck feel | ✓ Full | Institutional, methodical, defensive. Baseline S121 called this the strongest match in the set; the now-built MOD lanes reinforce it. |
| Doctrine coherence | ✓ | Managed-stability / suppression-as-restraint / mono-Mandate economy all expressed in-corpus. |
| Layer coverage | ✓ | Territory-dominant (expected) + Submission (PublicAct legislative control), Economy (Mandate gen), Standing, Information, Resolution. |
| Win-path support | ✓ (was ◐ before STD pool) | Both legs supported once STD is counted — see below. Distinctive character: suppression is *bespoke*, expansion is *generic-via-STD*. |
| §9.2 economics | ✓ (systemic) | Zero-cross-ceiling: mono-Mandate. Cross-resource costs (Findings/Capital/Capacity) sit at floor, never ceiling. Consistent with the Directorate/Guild/Syndicate native-mono pattern (04-n118/119/123). |
| **Implied strategies** (new) | mixed | See table. |
| **Leverageable strategies** (new) | rich | Faction-internal + STD-combination lanes; feed step-5 synthesis. |

---

## Win path — bespoke suppression, generic expansion (primary finding)

Directorate's win state has two legs. Counting the **full available set** (faction + STD):

- **"No faction Dominant anywhere"** — THICK, and **faction-specific**. Deep bespoke suppression toolkit: DIR.CA.1 (jurisdiction), CA.5 (covert presence removal), CA.8 (institutional review), PA.1 (raise cost of non-Dir ops), PA.3 (displace+block deployment), PA.4 (revoke presence), PA.5 (block settlement), PA.7 (lockdown), + React MOD.1/2/3/8/9. This is Directorate's differentiated identity. The STD pool adds generic removal (STD.CA.4 erode presence, STD.PA.2 challenge presence) that everyone shares.
- **"Established in MORE districts than any other faction"** — SUPPORTED, but via the **generic STD pool**. Presence-adders available to Directorate: STD.CA.3 (build support), STD.PA.1 (declare presence), STD.PA.9 (public forum where already present) — natively Mandate-affordable — plus STD.CA.8 (capital-costed, less native-accessible), and the faction's own DIR.PA.9 (radiate) + DIR.MOD.7 (React). So establishment is *adequately* supported — the earlier "~2 cards / thin" reading was a denominator artifact from counting only the faction-specific set.

**Corrected read:** Directorate does not have a *thin* expansion engine — it has a *generic, undifferentiated* one. Its faction-specific cards lean suppression because that is the doctrinal differentiator; establishment is left to the tools every faction shares. This actually **fits doctrine** ("suppression over construction" — the Directorate doesn't build distinctively, it constrains distinctively).

**Residual playtest-watch (downgraded from "risk"):** Mandate is a single pool funding both bespoke suppression *and* the STD establishment cards (which bill the acting faction's native resource). The tension is real and intended for a control faction — worth watching in playtest, but it is not a card-coverage gap.

---

## Implied strategies — §5a claims rated (against full set)

| §5a claim | Rating | Evidence |
|-----------|--------|----------|
| Suppress Dominant / push tiers down | **THICK** | Deep bespoke toolkit + STD.CA.4/STD.PA.2. |
| Established wide, Core outward | **ADEQUATE (via STD)** | STD.CA.3 / STD.PA.1 / STD.PA.9 + DIR.PA.9 / DIR.MOD.7. Generic, not faction-differentiated — by doctrine. |
| Legislative mode: reduce PA costs, extend world events | **THICK (now)** | Action MOD.21/22 cost_reduction (−1/−2); React MOD.6 world-event dictate; P-D1 Entry/Exit Controls. Largest unbuilt gap at S121 — now substantially closed. |
| Military lane: enforcement, costs Portrait, deterrent | **THICK (now)** | Battle MOD.10–13 (Boost/Hinder mag 1–2). Verify Portrait-cost wiring (§5a says "costs Portrait"). |
| Mandate economy off Core structures + adjacency bonus (+1 modifier card/adjacent district at Established) | **PARTIAL** | CA.6 generates Mandate from active ring directives ✓, but the *Core-structure adjacency modifier-draw* engine isn't visibly a card — verify it lives in Art 03 procedure or is an unbuilt §5a promise. |

---

## Leverageable strategies — emergent (feed step-5 cross-faction)

Plays the *full* set enables whether or not §5a named them:

**Faction-internal:**
1. **Reputational suppression (a second suppression axis).** Action MOD.19/20/23/24 (self +1/+2 PS, target −1/−2 PS) + DIR.PA.10 give Directorate a public-standing attack/defense game §5a doesn't foreground — suppression by *standing*, not just territory.
2. **Threshold-stacking → reliability engine.** Action MOD.14/15/16/25 (threshold_delta +5/+10/+15/+20) turn Probabilistic suppression cards (CA.2 Detain thr50, CA.5 thr65) near-automatic. The assist lanes' real payoff is *de-risking* the suppression core.
3. **Cost-reduction tempo loop.** MOD.21/22 against Mandate×2 sticker costs → out-tempo on institutional acts, distinct from CA.6 generation.

**STD-combination (the reason the denominator matters):**
4. **Standing pincer.** STD.CA.13 / STD.PA.4 / STD.PA.5 (Standing shifts, available to all) *stack on top of* Directorate's PS-warfare MODs (19/20/23/24) — Directorate can drive a rival's PS down through both bespoke and generic channels in one Quarter, harder than either alone.
5. **Self-sourced Intel (softens the Ghost dependency).** Directorate's hardest suppression cards (CA.2/CA.5/PA.8) are Findings/Intel-gated. STD.CA.5 (Add IntelToken) lets Directorate gather its *own* Intel; STD.CA.14/15 (remove/redirect an opponent's Intel) let it deny or steal. So the Intel gate is a self-serviceable loop via STD, not strictly a Ghost-alliance hook — though the alliance route stays the cheaper one (step-5 note).
6. **Submission layering.** STD.CA.6 (dampen public comms) + Directorate's legislative React MODs (MOD.9 block PA, MOD.6 world-event) → stacked Submission-layer control of rivals' public acts.
7. **Accord control.** STD.CA.11 (lock an executed Accord) + DIR.MOD.4 (every Accord = a Directorate admin/Mandate event) → Directorate profits from and freezes the table's agreements.

---

## Flags (→ running log `audit_findings_log_S156.md`)

- **[schema]** CA.6 & CA.7: `resolution=d100`, `threshold=50`, but `resolution_type=NULL` (siblings CA.2/CA.5 tagged `Probabilistic`). Both also `fail=None` → no defined failed-roll outcome. Two-part: mis-tag + undefined failure.
- **[schema, minor]** CA.8: `resolution=Automatic`, `resolution_type=NULL` where CA.1/CA.3/CA.4 carry `Transactional`.
- **[verify]** Core-structure adjacency modifier-draw engine (§5a) — locate in Art 03 or confirm unbuilt.
- **[verify]** Battle-MOD Portrait-cost wiring (§5a "costs Portrait").
- **[playtest-watch]** Mandate single-pool tension between bespoke suppression and STD establishment (intended, not a gap).
- Any Art 03 procedure gaps surfaced during triage → **04-n221**.

---

## Convergence with S121 baseline

- Deck feel ✓ Full — **agree** (strongest match).
- §9.2 zero-cross-ceiling — **agree** (systemic native-mono).
- Win-path: baseline said ◐ "suppression/expansion tension." **Refined, not overturned** — with the STD pool counted, the tension is a Mandate-allocation *playtest-watch*, not a card-coverage gap; the qualitative point (Directorate wins comparatively by constraining others more than climbing itself) stands and is doctrine-consistent.
- Modifier deck "largest §5a gap" at S121 — **now substantially closed** (legislative Action + military Battle lanes built and coherent). Headline delta since baseline.
