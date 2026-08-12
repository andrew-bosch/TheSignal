# Last Full Card Set Audit — Consolidated Summary

**Audit:** PM05 09-16 steps 4–5, run S156 · **Triage:** PM05 09-17, run S157 · **Verdict:** PM02 L357 (audit), **L358** (triage)

> **This file is ACTIVE and stays in `Whiteboard/` indefinitely** — it is not scratch awaiting migration. It is the standing answer to "what does the card corpus actually look like, and how do we know?" It gets **replaced**, not appended to, by the next full audit.
>
> **Conclusions here are stated as of S157, after triage.** Where the S156 audit reached a conclusion that the S157 re-derivation overturned, this file carries the **corrected** version and says so. The seven source documents (five faction re-audits, the cross-faction synthesis, the findings log's own working tables) were archived to `Retired/Whiteboard_Archive/` at S157 — read them only for the working detail behind a conclusion, never for the conclusion itself.
>
> **Supersedes** `card_analysis_summary_S119-128.md` (the S119–128 program, consolidated S153), archived at the same time. Several of its claims were proven false by this audit.

---

## 1. Methodology

**Denominator — STD+faction.** Every faction was audited against the *full set available to it*: its own faction-specific cards **plus the universal STD CA/PA pool** (16 STD.CA + 9 STD.PA, available to everyone). STD ring modifiers (`STD.MOD.n`, drawn at Upkeep on board conditions) are a *conditional* shared resource, not a faction differentiator — noted where relevant, never enumerated as faction coverage.

This denominator is load-bearing, not bookkeeping. The S119–128 baseline counted only faction-specific cards and consequently read several factions as having thin or missing capability where the shared pool actually covers it — Directorate's expansion engine being the clearest case (see §3). SYS-2 below quantifies how much the STD pool carries.

**Substrate — the database, not the .md.** The audit was run as SQL over `card_body` / `v_card_body` / `card_status` / `card_checklist` in `the_signal_db`, with `.md` remaining SOT and consulted directly on any disagreement. This is what made a full five-faction + cross-faction pass possible in one session rather than the ~6-session read it had been. Two cards are **not** in `card_body` and must be read manually from Part1_Core §12a: **DA-01 SCIFRecord** and **DA-02 PhantomRecord**.

**Governing discipline — re-derive, never inherit.** Two ground rules were adopted mid-audit and are the reason the pass found what it found:

1. **Treat any prior audit as a dated snapshot, not ground truth.** Validate every inherited claim against *current* rules before repeating it, and do not treat baseline *agreement* as independent validation — re-derive regardless. Proven necessary: the S119 baseline's "Guild is zero-cross" and "Ghost cannot trade Intel" were both false.
2. **Resource trade is never a card gap.** Trade of faction/district natives **and Intel tokens** is a verbal table procedure — available anytime, explicitly called out at quarter-end/Debrief, "any terms" (Art 03 §11.0; `ref_procedures.md:191`, `ref_resources.md:18`). Never flag "faction X can't trade/sell/supply resource Y" as a coverage gap.

The S157 triage extended rule 1 to the S156 audit itself, which is why several conclusions below differ from what the faction docs say.

## 2. What was asked of the corpus

Seven dimensions per faction, each rated against Art 04 §5a (Faction Playstyle Reference) as the doctrine source:

| Dimension | The question |
|---|---|
| Deck feel | Does the hand actually produce the feel §5a describes? |
| Doctrine coherence | Is the doctrine mechanically expressed, or only asserted in prose? |
| Layer coverage | Territory / Information / Economy / Submission / Standing / Resolution — where is the faction thick, thin, or deliberately empty? |
| Win-path support | Does the set contain the mechanics the stated win condition requires? |
| §9.2 economics | Cross-resource floor/ceiling behaviour — mono or cross, and is any inversion doctrinal? |
| **Implied strategies** | Every §5a claim rated THICK / ADEQUATE / PARTIAL / BLOCKED against actual cards. *New at S156.* |
| **Leverageable strategies** | Plays the full set enables whether or not §5a named them. *New at S156.* |

Then, across all five (step 5): differentiation, adjacency synergies, opposition counters, matchup asymmetries, and system-level gaps.

---

## 3. Faction conclusions

### Directorate — suppression is bespoke, expansion is generic
Deck feel ✓ full (strongest §5a/mechanics pairing in the set). Win path holds on both legs, but with a distinctive shape: *"no faction Dominant"* is thick and **faction-specific** (deep bespoke suppression: CA.1/5/8, PA.1/3/4/5/7, React MOD.1/2/3/8/9), while *"Established in more districts"* is **adequate via the generic STD pool** (STD.CA.3, STD.PA.1, STD.PA.9 + DIR.PA.9/MOD.7). The baseline's "thin expansion" reading was a denominator artifact. Corrected read: Directorate's expansion engine isn't thin, it's *undifferentiated* — which fits doctrine, since the Directorate doesn't build distinctively, it constrains distinctively.

Emergent lanes §5a doesn't foreground: **reputational suppression** as a second axis (PS-warfare MODs 19/20/23/24 + DIR.PA.10), **threshold-stacking** turning Probabilistic suppression near-automatic, and **self-sourced Intel** via STD.CA.5/14/15 — which softens the Ghost dependency into a self-serviceable loop rather than a hard alliance requirement.

**Delta since baseline:** the modifier deck, the largest S121 gap, is now substantially closed on both the legislative and military lanes.
**Live:** two §5a promises were verified unbuilt — the Core-structure adjacency modifier draw (**cut from §5a at S157**; at real Core adjacency degrees of 4/6/6/4 against a 3-card draw ceiling it would have been a second, larger modifier economy) and the military lane's cost (**→ 04-n222**; DIR.MOD.10–13 carry no cost, no Portrait entry *and* no `ps_framing`, and §5a's "costs Portrait" was ruled doctrinally backwards — military action is Directorate doctrine executing, so it should cost Public Standing and may *earn* Portrait). Mandate single-pool tension is a playtest watch, not a gap.

### Ghost — thick pipeline, one blocked keystone
Deck feel ✓ (precise, patient, self-contained). Doctrine ✓ strong, confirmed structurally: **zero standing board conditions** across the whole set (19 Immediate / 16 None / 1 Transient; no Permanent or Seasonal) — point-disruption, exactly as doctrine demands. Information-dominant by design; minimal Territory is correct, not a gap.

Win path is delay: operation disruption (CA.1/2/3/14/15, PA.2, MOD.9/10) and the intelligence pipeline with deferred payoff (collection CA.7/8 + MOD.2/3/4, conversion CA.6, **SCIF CA.9 → DA-01**, **Phantom CA.13 → DA-02**, Flip CA.10) are both thick. Ghost is the **least STD-dependent faction in the game** — the shared pool mostly duplicates its intel suite or offers tools its doctrine doesn't want. That low STD-leverage is itself a finding, and is consistent with "deliberately small, self-contained."

**Deltas since baseline:** the "single Flip endpoint" gap — the baseline's most significant — is CLOSED (CA.14/PA.1/CA.15 + DA-01/02). Passive Intel generation (04-n143) is CLOSED (MOD.2/3/4). The baseline's "Ghost cannot sell or trade Intel" is **overturned** — it contradicted the free-trade rule, and reframes into Ghost's broker position (§4).
**Live:** **CA.11 Signals Analysis is blocked and flagged for full reimagining** — its mechanism is undefined and it depends on the undesigned Classified Directive subsystem (Art 06 §10 is a non-canonical stub; content home Art 05-vs-08 undecided; no deduction/reveal procedure). It is the doctrinal endpoint — Ghost can gather toward suppressing consensus but cannot yet *act on hidden objectives*. Explicitly **does not gate Art 04**; needs its own session.

### Guild — strongest structural engine, and the baseline's clearest error
Deck feel upgraded Partial → ✓ (heavy, deliberate, permanent, now backed at scale). **Information layer is exactly 0 — the sharpest doctrinal signature in the game**, and correct: Guild cannot operate covertly in principle. Win path is the strongest structural engine audited: Foundation Rights (CA.3, near-auto in Ring 0) → high-tier builds → CA.5 compounds → defense/recovery → salvage.

Emergent identity: a **parasitic construction economy** — React MOD.2/3/4/8/9 turn *every other faction's* building into Guild income, so Guild literally taxes the table's construction. Its passive engine is *coupled* to the STD pool, the exact opposite of Ghost's self-sufficiency. Plus infrastructure-landlord (PA.6 sells structures priced in the buyer's currency) and coalition-builder lanes.

**Deltas since baseline:** Standing absence CLOSED (PA.4/8/9); no-territorial-removal CLOSED (CA.7/CA.8); passive income implemented.
**Live:** **defense may not scale** — CA.1 protects one structure/Quarter and PA.3 recovers only the first loss, so a rival demolishing several structures in a Quarter can outpace protection. Materially deeper than baseline, but a balance/playtest watch. **Passive income diverges from its own specification**: §5a and 04-n2 both gate it on Guild presence and on STD.CA.1 specifically; all five React MODs carry `restriction = None`, fire on any opponent structure placement, and MOD.9 fires on `established_marker.placed` rather than structures at all. Resolved S157 — **the cards are right, the text was wrong**; §5a rewritten, 04-n2 closed as superseded.

### Network — the reactive engine is now self-sustaining
Deck feel upgraded Partial → ✓ (distributed, reactive, increasingly loud). **14 React modifiers, the most in the game.** Resolution layer empty — doctrinally correct: Network broadcasts, it doesn't manipulate dice.

Win path (wide Presence, Baryo outward) was a gap at baseline and is now built on both halves: **reactive presence** (React MOD.1/4/5/6/8 add presence off public events — presence spreads as the city gets loud, rather than by deliberate placement) and the **modifier-deck self-feed** (MOD.7/9/14 + CA.2), which was the largest single §5a gap in the baseline and is the headline delta of the whole audit program. The Q6–8 self-sustaining loop §5a describes now actually exists. Territorial response also closed (PA.4, MOD.10, CA.8).

**Terminology correction (S156, PM02 L355):** "Tripwire" was the pre-ModReact name for certain React effects — stale terminology, not a missing mechanic. §5a rewritten to centre the React modifier engine; no card or procedure to build.
**Live:** NET.PA.3 is a borderline §9.2 inversion and is **toothless against Guild specifically** (forcing "play with your hand visible or forfeit covert submissions" does nothing to a faction with no covert ops) — a dead branch in exactly one matchup.

### Syndicate — every Capital lane carded, clearest win path
Deck feel ✓ full (wealthy, patient, restructures deals from underneath). Win path — Dominant in the Ring 1/2 economic spine — has **the most direct support of any faction** (CA.3/8/9, PA.1/2, MOD.8). Resolution empty and correct: Syndicate *buys past* dice via the CA.4 bypass rather than manipulating them.

Doctrine coherence is the primary positive finding: **every §5a Capital-application lane now has a card** — direct costs (the mono-Capital set), deferred returns (PA.2, CA.8), bypass payments (CA.4), hostile takeover (CA.9, PA.1), Accord transfer (CA.10), proxy funding via Network. Plus a React passive-Capital engine (MOD.2/3/4/5/7) generating Capital off the table's activity.

Emergent identity: **deal restructuring from underneath** — CA.10/11 and MOD.1/11 corrupt or transfer *any two factions'* accords, making every bilateral agreement a potential Syndicate asset.

**Delta since baseline:** the "entirely parasitic, no Accord-formation card" gap is architecturally closed by CA.12 Boilerplate (04-n125 was already closed S130), though CA.12 remains a stub (04-n219).
**Live:** 04-n124's doctrine-documentation requirement is **not** satisfied — the taglines are mechanical descriptions, not doctrine justification — and its spec half is still open: **SYN.CA.7's `on_accept` is debit-only** (`faction(target).resource(native).remove(2)`) with no matching credit expression to Syndicate. That is a mechanical defect, not annotation.

---

## 4. Cross-faction conclusions

**Differentiation ✓ — five distinct decks, no collapse.** Layer signature per faction (effect-bearing, faction-specific counts):

| Layer | DIR | GHO | GUI | NET | SYN | (STD) |
|-------|----:|----:|----:|----:|----:|----:|
| Territory | 13 | 3 | 13 | 10 | 6 | 19 |
| Information | 2 | **18** | **0** | 5 | 4 | 5 |
| Economy | 4 | 4 | 10 | 6 | **13** | 15 |
| Submission | **6** | 3 | 2 | 2 | 3 | 5 |
| Standing | 2 | 2 | 3 | 5 | 2 | **16** |
| Resolution | 1 | 1 | 1 | 0 | 0 | 2 |

Each faction has a unique fingerprint, and no two — adjacent or not — collapse into the same decision pattern. Differentiation is *stronger* than at baseline. Five distinct control poles hold: Directorate = sustained-pressure/suppression · Ghost = point-disruption/intelligence · Guild = fill-space/construction · Network = distributed/broadcast · Syndicate = transactional/economic.

**Ghost is the system's economic pivot.** 19 non-Ghost cards (Network 7, Syndicate 7, Directorate 5) have costs gated on Findings or Intel — Ghost's native output. Because trade is a free verbal procedure, Ghost's over-collection is directly tradeable leverage over three factions' ceilings: it can enable or withhold. The doctrinal ring closes on Ghost from both sides (Ghost→Directorate as ally supply line, Syndicate→Ghost as supplier).

**Adjacency synergies are real, not just philosophical.** Directorate's Core structures *trigger Guild's passive income* ("Directorate builds, Guild invoices"). Network's reactive presence spreads off public events including Guild's visible building. Network↔Syndicate run the §5a proxy-funding bypass around Directorate visibility.

**The sharpest tension is dependency laid over rivalry:** Network attacks Ghost informationally (CA.1/CA.3 expose covert ops, PA.3 opens hands) while *depending on Ghost's Findings* for those very cards. Your supplier is your predator. Elsewhere: Directorate × Syndicate is the head-on antagonism (CA.4 bypass negates Probabilistic suppression without a roll; Syndicate's Ring-1/2 push violates Directorate's win-leg), and Guild's non-scaling defense is a **shared pressure vector** — Syndicate CA.3, Network PA.4 and Directorate PA.3/CA.5 can each outpace it.

### §9.2 economics — no grouping currently survives the data

The baseline grouped Directorate + Guild + Syndicate as mono-economy. S156 corrected that to three buckets (mono {DIR, SYN} / native-cross {GUI} / foreign-gated cross {GHO, NET}). **The S157 triage broke both models against cost-composition queries over the current corpus:**

| Faction | Costed cards | With any foreign resource | Share | Native ceilings (×3+) |
|---|---:|---:|---:|---:|
| Guild | 20 | 10 | **50%** | 2 (CA.10 C×4, PA.9 C×3) |
| Syndicate | 23 | 10 | **43%** | 3 (CA.8 C×6, CA.10 C×3, CA.3 C×3) |
| Directorate | 22 | 9 | **41%** | 1 (PA.2 M×3) |
| Network | 20 | 8 | **40%** | 0 |
| Ghost | 26 | 6 | **23%** | 1 (CA.11 F×3) |

Cross-cost share is essentially flat. Directorate is not mono on either measure; Guild's native ceilings run *deeper* than Directorate's; Ghost is the **least** cross-costed faction, the opposite of "foreign-gated cross." **Stated caveat:** Ghost's flip-cost model spends the *target's* resources, which cost-string parsing does not capture — Ghost's 23% is the least reliable figure and needs a hand check.

**Consequence:** 04-n119, 04-n123 and 04-n126 all rest on counts now demonstrably false ("Guild genuinely mono" — 10 cross-cost cards; "zero cross-resource cards in Syndicate" — 10; "Network has the only cross-ceiling architecture, both cross cards CA.1/CA.2" — 8). **The §9.2 pass must re-derive its grouping from the corpus before running (→ 04-n223); do not run it on either existing model.**

### Other system-level findings

- **Standing is STD-provided.** 16 STD Standing cards against 2–5 per faction. Factions are standing-thin without the shared pool — the clearest proof that the STD+faction denominator is load-bearing.
- **Resolution is the rarest layer.** 5 faction cards total (1 each DIR/GHO/GUI, 0 NET/SYN) + 2 STD. Deliberate niche or system-wide under-use — worth a deliberate call, not yet made.
- **The free-trade rule is load-bearing but uncarded.** Every Ghost-hub dependency resolves through Art 03 §11.0. A core economic subsystem lives in table procedure rather than the card set — fine by design, but it must be prominent in rules teaching.
- **Sub-6-player configuration is undesigned** (→ **00a-80**). Every artifact says 2–6 players; the design assumes 5 factions + ARBITER. Nothing specifies how a smaller game is played — double up factions, scripted stand-in, ARBITER plays them, or exclude them outright — and these are materially different games. The 19 Ghost-gated cards degrade only under "exclude"; the other three options largely dissolve the problem. **The intel-economy question is downstream of this decision, which is why it is not tracked as its own item.** Gates smaller-group playtest; explicitly deferred from gating Art 04 (Andy, S157).

---

## 5. Overall verdict

The five-faction system is **well-differentiated, doctrinally coherent, and materially more complete than at the S119–128 baseline** — the S154 modifier corpus closed nearly every faction's largest baseline gap. Cross-faction play is rich and genuinely asymmetric: matchup-dependent dead branches, dependency-over-rivalry tensions, five distinct control poles. **No differentiation failures and no doctrine incoherence were found.**

What the audit did find, in order of weight: an economic grouping model that does not survive contact with the corpus; an undesigned player-count configuration surfacing as an intel-economy symptom; two §5a promises with no implementation behind them; one doctrinally-central card blocked on an unbuilt subsystem; and a schema-population layer with more corpus-wide gaps than per-faction inspection suggested.

**Method note worth carrying forward:** every conclusion overturned in this program — in both directions, S119→S156 and S156→S157 — was overturned by re-deriving against primary source rather than by inheriting a prior pass's summary. Three separate audit generations each found the previous one's claims partly stale. Assume this one is no different.

---

## 6. Where the live work went

**PM05:** 00a-80 (sub-6-player configuration) · 04-n222 (Directorate military lane) · 04-n223 (§9.2 re-derivation) · 04-n224 (remaining partial cards) · 04-n124 (re-opened in substance) · 04-n217/218/219/220/221 (pre-existing stubs and the procedure-coverage initiative) · Ghost CA.11 reimagining.

**`schema_cleanup_log.md`:** #59 `resolution_type` absent on 46 cards · #60 `value_rating` unset on 8 · #61 `NamedActionType` unregistered · #62 the one live `TBD` · #63 GUI.CA.2 notation residue. **All five gate Art 04 sign-off** (Andy, S157 — no deferrals).

**Deferred from gating Art 04 (the only two on record):** Ghost CA.11 (S156) and 00a-80 (S157).
