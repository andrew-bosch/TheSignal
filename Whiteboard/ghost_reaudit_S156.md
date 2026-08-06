# Ghost Card Set Re-Audit — S156 (PM05 09-16 step 4)

**Status:** First-pass analysis, awaiting Andy checkpoint before continuing to Guild→Network→Syndicate.
**Trigger to delete:** once findings are triaged via the consolidated review (PM05 09-17) and the faction verdict is logged to PM02.
**Denominator:** 20 Ghost operations (15 CA + 5 PA) + 27 Ghost MOD (12 Action, 4 Battle, 11 React) + **2 DA cards (DA-01 SCIFRecord, DA-02 PhantomRecord) — NOT in `card_body`, read manually from Part1_Core §12a** + the universal STD CA/PA pool. STD ring mods conditional.
**Substrate:** `card_body` / `v_card_body` / `card_status` / `card_checklist`, re-derived, checked against `card_analysis_summary_S119-128.md` (S119–120, 04-n87/n88).
**Doctrine source:** Art 04 Part1_Core §5a (Ghost); win = *delay — no premature answer to the Chorus; ensure no one else answers prematurely.* No territory required. Economy: Findings → faction-keyed Intel tokens.

---

## Dimension verdicts

| Dimension | Verdict | Note |
|-----------|---------|------|
| Deck feel | ✓ Match | Precise, patient, self-contained. Deepest intelligence suite in the game; the operational core (20 CA/PA) stays small even as the shared modifier corpus adds volume. |
| Doctrine coherence | ✓ Strong | "Understanding must precede action." **Zero standing board conditions confirmed** (19 Immediate / 16 None / 1 Transient PA.2; no Permanent/Seasonal) — point-disruption/reactive, as doctrine demands. |
| Layer coverage | ✓ | Information-dominant (by doctrine); Economy (Intel/Debrief economy); Submission (disrupt covert ops); Standing (disclosure); Territory deliberately minimal (PA.5, MOD.7/8) — "no permanent territory" is correct, not a gap. |
| Win-path support | ◐ | Pipeline + disruption + deferred-payoff all thick; but the doctrinally-central consensus-suppression card is **blocked** — see below. |
| §9.2 economics | ✓ **(deliberate exception)** | Ghost is the one non-mono faction: higher-tier cards carry **flip-acquired cross-costs** (target's own resources — CA.14, PA.1, CA.15, CA.6) by design. No ceiling inversion (baseline 04-n126). Do **not** fold Ghost into the Directorate/Guild/Syndicate zero-cross-ceiling pass. |
| **Implied strategies** | mostly THICK | Two baseline gaps now closed; one blocked. See table. |
| **Leverageable strategies** | rich, self-contained | Attribution warfare + deferred payoff; least STD-dependent faction; coalition/Intel-trade limit persists. |

---

## Win path — thick pipeline, one blocked keystone (primary finding)

Ghost wins by **delay** — degrading others' ability to reach a premature answer while assembling its own Q8 hand. Mechanical support:

- **Operation disruption (the "delay" engine)** — THICK: CA.1 (identify+take an op), CA.3 (tap dispatch/read submitted ops), CA.14 (erase an op entirely), CA.15 (predict+rewrite a rival's move), CA.2 (surveil covert ops), PA.2 (institutional scrutiny on a covert op), MOD.9/10 (remove modifier card / cripple hand).
- **Intelligence pipeline + deferred payoff** — THICK: collection (CA.7 sustained, CA.8 Full Take burst, MOD.2/3/4 passive React), conversion (CA.6), **SCIF (CA.9 → DA-01: draws modifier cards at Debrief scaled to target's building count)**, **Phantom (CA.13 → DA-02: mirrors target's district income to Ghost at Debrief)**, Flip (CA.10). This is the "arrive at Q8 with a hand assembled from others' capabilities" §5a path — now fully built and Art 03 §11-backed.
- **Consensus suppression via Classified-Directive knowledge** — **BLOCKED**: CA.11 Signals Analysis (deduce a target's Classified Directive) is the doctrinally-central "suppress premature consensus" card, and it's gated on **Art 06 Classified Directives** (unbuilt; ties to the Art 03-init sign-off gate). The marquee mechanism of Ghost's entire doctrine is currently unplayable.

**Read:** the pipeline and disruption legs are strong and materially stronger than at baseline. The ◐ is entirely the CA.11 block — Ghost can *gather* toward suppressing consensus but cannot yet *act on hidden objectives*, which is the doctrine's endpoint.

---

## Implied strategies — §5a claims rated

| §5a claim | Rating | Evidence |
|-----------|--------|----------|
| Intelligence pipeline early | **THICK** | CA.7/8, MOD.2/3/4, CA.6. |
| Pre-fund Quarters via Full Take (burst) | **THICK** | CA.8 (saturate / maximum single-op yield). |
| SCIF funds next Quarter's hand | **THICK (now)** | CA.9 → DA-01, built + Art 03 §11 procedure. |
| Flip — target's assets turned against them | **THICK (now)** | CA.10 + higher-tier flip-spenders (CA.14, PA.1, CA.15) + DA-02 phantom income. **Baseline's "single Flip endpoint" gap — CLOSED.** |
| Passive Intel generation near Ghost presence | **THICK (now)** | MOD.2/3/4 React. **Baseline gap 04-n143 — CLOSED** by the modifier corpus. |
| Signals Analysis → deduce Classified Directive | **BLOCKED** | CA.11 gated on Art 06. Doctrinally central, unplayable at L1. |

---

## Leverageable strategies — emergent (feed step-5 cross-faction)

**Faction-internal:**
1. **Attribution warfare (deception sub-game).** CA.12 (alter attribution on a held Intel token — *free*), CA.5 (corrupt Intel), CA.15 (predict+rewrite), MOD.1 (name the faction → end attribution), MOD.11 (hijack a public act). Ghost manipulates *who appears responsible* — a layer §5a doesn't foreground.
2. **Deferred-payoff decoupling.** SCIF (DA-01) + Phantom (DA-02) snapshot at Beat 3 and pay at Debrief — Ghost's tempo is decoupled from immediate board state; it banks Quarters ahead.
3. **Threshold-stacking → reliability.** Action MOD.16–19 (+5/+10/+15/+20) turn Ghost's Probabilistic collection (CA.7 thr55, CA.8 thr40, CA.11 thr30) near-automatic — same reliability engine seen in Directorate.

**STD-combination:**
4. **Least STD-dependent faction (a finding in itself).** Ghost's intel suite is self-sufficient; the STD pool mostly duplicates it (STD.CA.5 add Intel, STD.CA.14/15 remove/redirect Intel) or offers territory/standing tools Ghost's doctrine doesn't want. Low STD-leverage is *consistent* with "deliberately small, self-contained." Where STD helps: STD.PA.4/PA.5 (accuse/attribute) amplify Ghost's disclosure game (PA.1 dual-attribution); STD.CA.13 (covert standing-degrade) fits Ghost's covert profile.
5. **Intel broker / kingmaker (step-5 hook).** Ghost is the table's natural Intel supplier, and Syndicate's high-cost plays (accord transfer, hostile takeover, battle winner) *require* faction-keyed Intel tokens (§5a Syndicate). This transacts freely — **resource trade (native + Intel) is a verbal table procedure, anytime and called out at quarter-end/Debrief (Art 03 §11.0, "any terms"), not a card function.** So Ghost↔Syndicate is a live, transactable supply relationship, and Ghost's over-collection of Intel (deepest suite in the game) becomes tradeable leverage — a broker/kingmaker lane. **Step-5 synthesis item.** (Corrects the S119–120 baseline's "Ghost cannot sell or trade Intel," which was wrong against the free-trade rule.)

---

## Flags (→ running log `audit_findings_log_S156.md`)

- **[design/reimagine]** CA.11 Signals Analysis — **needs full reimagining (Andy S156):** mechanism undefined, card may be invalid, depends on the undesigned Classified Directive subsystem (Art 06 §10 non-canonical stub; content home Art 05-vs-08 undecided). Not a fix or carve-out — reimagine from scratch around Ghost's actual "act on hidden objectives" endpoint. Does NOT gate Art 04 sign-off in its current state.
- **[schema]** GHO.MOD.1: `value_rating` stored as string `"None"` (should be int or NULL). One of the 6 partial cards.
- **[schema, minor]** GHO.CA.11: `value_rating=NULL`. (Note: CA.11 is *no longer* the stale `id=TBD` row from 04-n172 — it's v1.0 with correct `resolution_type=Probabilistic`; memory pointer is outdated.)

---

## Convergence with S119–120 baseline

- Deck feel ✓ Match; doctrine ✓ Strong (zero standing conditions) — **agree, re-derived** (persistence distribution confirms).
- **Single Flip endpoint** (baseline's "most significant gap") — **CLOSED**: multiple flip-spenders (CA.14/PA.1/CA.15) + SCIF/Phantom endpoints (DA-01/02).
- **Passive Intel generation** (baseline 04-n143 unimplemented) — **CLOSED**: MOD.2/3/4 React.
- **CA.11 blocked** — **persists** (Art 06 gate), now the single biggest win-path hole.
- **"No Intel trade / coalition limit"** — **overturned**: the baseline claim contradicts the free-trade rule (Art 03 §11.0). Reframed as a Ghost *strength* (Intel broker) and a step-5 Ghost↔Syndicate relationship, not a limit.
- §9.2: Ghost is the deliberate non-mono exception — **agree** (flip-cost model, no ceiling inversion).
