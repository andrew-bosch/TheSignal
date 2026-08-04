# Card Set Audit Program — Consolidated Summary (S119–S128)

Between S119 and S128, each of the game's five factions had its full CA/PA card set audited against Art 04 §5a (Faction Playstyle Reference) — checking deck feel, doctrine coherence, layer coverage, win-path support, and economic (§9.2 floor/ceiling) compliance. The five per-faction audits (STD+DIR, STD+GHO, STD+GUI, STD+NET, STD+SYN) were followed by a cross-faction synthesis (04-n110, closed S128) comparing deck feel, win-path support, and sustained-pressure posture across all five. This program directly seeded steps 4 and 5 of the later 09-16 full-corpus card review roadmap. The six source files were retired to `Retired/Whiteboard_Archive/` S153; this summary is the readable digest that remains live.

---

## Directorate (04-n89, S121)

**Deck feel:** Match — strongest §5a/mechanics pairing in the L1 set. Institutional/methodical/table-plays-defensively all mechanically realized: 11 of 12 active cards mono-Mandate, 4 of 8 CAs fire at Beat 2 (unique concentration), and three Permanent/Seasonal standing-condition PAs (PA.1 Regulatory Override, PA.3 Entry/Exit Controls, PA.6 Standing Injunction) force the whole table to route around them.

**Doctrine coherence:** Strong. Near-mono economy is read as doctrine statement, not gap — DIR.CA.5 Sanctioned Raid is the sole cross card, positioned exactly where the highest-force removal play should sit.

**Play gaps / design candidates:**
- No Territory|Add card at all — DIR builds presence exclusively through Standard cards; the most doctrinally explicit gap in the game (deliberate, but headline item).
- Both modifier decks §5a promises (legislative: PA cost cuts/world-event extension; military: enforcement) entirely undesigned at L1 — headline §5a gap.
- Win-path resource tension: the same Mandate pool funds suppression (PA.3+PA.6 = M×6) and expansion; Q1–Q2 Mandate starvation flagged as a playtest risk.
- Zero cross-ceiling architecture (11/12 mono) — §9.2 inversion, same pattern later confirmed in GUI and SYN.
- No independent covert Intel generation — DIR.PA.2 Convene an Inquiry is contingent on prior STD PA groundwork, creating a supply-chain dependency for CA.2/CA.5.

**PM05/decisions:** 04-n89 (audit, ✅); 04-n104 (PA.4/PA.5 redesign into Regulatory Downgrade + Zoning Freeze, resolved S131); 04-n108 (Standing card tracking); 04-n118 (§9.2 ceiling gap); feeds 04-n110 gate.

---

## Ghost (04-n87/n88, S119–S120)

**Deck feel:** Match — precise, patient, deliberately small (14 non-blocked cards, deepest intelligence suite in the game: collection, corruption, interception all represented).

**Doctrine coherence:** Strong — point-disruption/reactive doctrine ("understanding must precede action") supported by zero standing board conditions; every card Immediate or Permanent-but-self-executing.

**Play gaps / design candidates:**
- Single Flip endpoint (GHO.CA.4 Deep Cover) — §5a implies multiple higher-tier cards spending Flip-acquired resources; only one spending destination exists. Most significant gap vs. §5a.
- Passive Intel generation ("from game events occurring near Ghost presence") — described in §5a, not implemented by any card or rule.
- §5a text stale post-S113 redesign: called Deep Cover a "burst card" when it's actually intelligence interdiction; Full Take is the real burst card — text corrected S128.
- GHO.CA.11 Signals Analysis blocked (gated on Art 06 Classified Directive) — known missing win-path component.
- No private/named-faction intelligence delivery — all Ghost PA effects are public; Ghost cannot sell or trade Intel, limiting coalition play.
- Open sustained-pressure question at audit time (later resolved by the cross-faction pass: Ghost is the point-disruption pole).

**PM05/decisions:** Card ID/heading-format hygiene items (04-n87/n88); design decisions on CA.1/CA.5/CA.6/STD.CA.12 resolved S119–S120; 04-n143 (new — passive Intel generation implementation, parallel to Guild's 04-n2).

---

## Guild (04-n92, S122)

**Deck feel:** Partial — construction permanence delivered (Permanent structures, Automatic PA.1 dual-build, CA.5 compounding yield), but defense does not scale with structure count, so "heavy, deliberate, permanent" isn't backed at scale. Smallest faction set (9 active cards); 3 of 6 layers (Standing, Information, Resolution) have no faction-specific card.

**Doctrine coherence:** Build-first / compound-income / permanence-as-win-condition all mechanically expressed and coherent.

**Play gaps / design candidates:**
- Defense doesn't scale (FLAG 2, confirmed): GUI.CA.1 Fortify Structure protects one structure per Quarter only; GUI.MOD.1 Night Shift Crew (React) cannot prevent demolition — chip removal is simultaneous with hitting 0, no React window exists.
- §5a passive-income trigger ("+1 Capacity when an opponent completes STD.CA.1 in a Guild-presence district") unimplemented as a governing rule — exists only as unimplemented item 04-n2, referenced directly in GUI.CA.6's design note.
- §9.2 inversion confirmed (FLAG 5): zero cross-resource cost cards. GUI.CA.4 is genuinely mono; GUI.PA.1 is cross-but-waived via Guild affinity. Same inversion shape as Directorate.
- No faction-specific territorial recovery/removal card (FLAG 4) — Guild relies entirely on STD.CA.4 Undermine; left as an open doctrinal-vs-gap decision.
- Standing card absence (FLAG 3) determined non-urgent — STD Standing tools are accessible at Capacity cost, so Guild is not resource-mismatched; enhancement, not survival gap.
- GUI.CA.2 code/comment mismatch on payout (2 Capacity vs. 1 Capacity + district-native) flagged for spec audit.

**PM05/decisions:** 04-n92 (audit, ✅); 04-n2 (passive rule implementation — high priority, blocks §5a stability); 04-n119 (new — §9.2 ceiling gap); 04-n108 (Standing card — low priority); new items opened for defense-scaling and territorial-response decisions.

---

## Network (04-n90, S123)

**Deck feel:** Partial/L1 gap — Broadcaster identity strong (4 Reveal cards, the highest concentration of any faction, covering every disclosure mode: pre-execution cancel, pre-resolution announce, post-resolution attribution, sustained visibility obligation), but "increasingly loud as the game progresses" depends on a modifier-deck self-feed that had only 2 cards at L1 (MOD.1 design-complete/schema-pending; MOD.2 a full stub).

**Doctrine coherence:** Strong on the Broadcaster/transparency axis; credibility-as-capital doctrine (CA.6 Sacrifice: PS→Intel) mechanically expressed.

**Play gaps / design candidates:**
- Win-path expansion gap: no unrestricted faction-specific presence-placement card. Wide-Established win path structurally depends on STD.CA.3/STD.CA.8; faction toolkit only covers initial entry (CA.5, Baryo-restricted), consolidation (PA.2, Established+ only), and opportunistic insertion (MOD.1 React).
- Modifier deck described in design notes as the "true engine" — largely unbuilt at L1; largest §5a gap for Network.
- No territorial response — zero Remove/Block/Move cards; no faction-specific recovery if Network presence is removed.
- Cross-resource dependency: NET.CA.1 Leak and NET.CA.2 Disclosure Loop both cost Findings (Ghost's native) — Network is the *only* faction with an operational cross-ceiling card (CA.1) among all five, but it is Ghost-dependent and degrades to mono in Ghost-absent games.
- NET.PA.3 Live Coverage flagged as a borderline §9.2 inversion (Seasonal covert-disable/hand-open at mono cost); also weakened against Guild specifically (Guild has no covert ops, so the "disable" branch is toothless).

**PM05/decisions:** 04-n90 (audit, ✅); 04-n126 (new — Findings-gated cross architecture); 00a-78 update; 04-n4 (modifier card schema — gates MOD.1/MOD.2).

---

## Syndicate (04-n91, S123)

**Deck feel:** Match — wealthy, patient, restructures deals from underneath; Capital saturation from Q1, Beat 2 patience plays (CA.4/CA.5/CA.6), and the deepest Accord-manipulation suite in the game (CA.10/CA.11/MOD.1). No significant feel gap identified.

**Doctrine coherence:** Strong — economy extraction, resource redirection, and Accord manipulation all directly served by named cards; win path (Ring 1/2 Dominant) has the clearest direct support of any faction audited (4 cards: CA.3, CA.8, CA.9, PA.1).

**Play gaps / design candidates:**
- §9.2 inversion confirmed — zero cross-resource cost cards across the entire 15-card set. Clear inversions: CA.3 (C×5, structure seizure), CA.8 (C×5, territorial claim), CA.10 (C×3, permanent Accord party replacement); CA.9 partial inversion (C×4+Intel, wholesale presence replacement).
- Non-native generation without doctrine justification: CA.1 Leveraged Acquisition and CA.7 Corporate Blackmail can deliver non-Capital resources with no stated rationale, unlike GHO.CA.10 Flip, which states its justification explicitly.
- Accord manipulation suite is entirely parasitic — no Accord-formation card of its own; if the diplomatic layer is thin at a given table, all three cards go dormant simultaneously. Three remedy options proposed (accept as doctrine / add a lightweight passive rule / add a formation card).
- Intel self-sufficiency in question: SYN.CA.6 Parasitic is conditional and keyed to the first submitting faction, not necessarily the CA.9 target — open question whether Syndicate structurally depends on Ghost's Intel surplus.
- Highest open-issue density of any faction audited: only 4 of 15 cards resolved at audit time; bottlenecks include a missing Art 03 Beat 2 procedure, missing ElectPlayer covert procedure, missing NamedActionType definition (blocks CA.5 entirely), and missing DividendMarker registration.

**PM05/decisions:** 04-n91 (audit, ✅); 04-n123 (new — §9.2 ceiling gap); 04-n124 (new — non-native generation doctrine documentation); 04-n125 (new — Accord-formation parasitic posture decision).

---

## Cross-Faction Synthesis (04-n110, closed S128)

**Deck-feel match, all five:** Ghost ✓, Directorate ✓ Full (strongest match in the set), Syndicate ✓ Full, Guild ◐ (defense-scaling gap), Network ◐ L1 gap (modifier self-feed unbuilt). No two adjacent factions produce similar hand textures — cross-faction differentiation at the deck-feel level holds.

**Win-path support:** Syndicate ✓ (clearest delivery — 4 direct cards). The other four are ◐: Ghost (single Flip endpoint thin against the implied tier structure), Guild (mechanically coherent but undercut by the unimplemented passive-income floor and non-scaling defense), Network (structurally dependent on Standard cards for expansion; modifier self-feed unbuilt), Directorate (mechanism coherent but Mandate-allocation tension between suppression and expansion is an open playtest risk).

**Sustained-pressure spectrum:** `DIR [sustained] ← NET (L1 thin) ← GUI (constructive/accretive) ← SYN (episodic high-force) ← GHO [point-disruption]`
- **Directorate** — sustained-pressure pole: three Permanent/Seasonal standing conditions others must route around.
- **Network** — theoretically growing but mechanically thin at L1: the "increasingly loud" character depends on an unbuilt modifier self-feed; PA.3 Live Coverage alone carries the faction's entire sustained-pressure load.
- **Guild** — constructive, not restrictive: better described as sustained-*position* than sustained-*pressure* — it holds ground others must contest rather than imposing conditions others must dismantle.
- **Syndicate** — episodic at high force: powerful single-event territorial plays; Accord tripwires are the closest thing to sustained pressure.
- **Ghost** — point-disruption pole: zero standing board conditions, precise strikes on specific plays.

**Differentiation conclusion:** ✓ — the completed 5-faction synthesis table (04-n90, S123) found no adjacent doctrine pair collapsing into similar decision patterns. Strongest pair: Ghost→Directorate (point-disruption precision vs. institutional sustained constraint). Also distinct: Directorate→Guild (suppression/clear-space vs. construction/fill-space, inverse mechanisms), Guild→Network (information-free/constructive vs. information-dominated/broadcast, orthogonal domains), Network→Syndicate (public broadcast vs. private transactional information — the closest pair, but non-overlapping disclosure models).

**Systemic findings (visible only in comparison):**
- Zero-cross-ceiling §9.2 architecture is systemic across Directorate, Guild, and Syndicate (04-n118/119/123) — all native-mono-economy factions. Network has the one operational cross-ceiling card in the game (CA.1) but it's Findings-gated/Ghost-dependent (04-n126). Ghost alone has no ceiling inversion. Recommendation: run the cross-resource pass across all four together rather than faction-by-faction.
- The unbuilt modifier deck is the single largest §5a implementation gap across the whole set — Directorate (legislative + military decks), Network ("true engine" self-feed), and Ghost (passive Intel generation) all have §5a descriptions dependent on modifier content that barely existed at L1.

**Still open at close (S128):** 04-n143 (Ghost passive Intel generation — governing rule or card implementation, text confirmed correct); gates opened for 04-n127–131 (GUI/NET/SYN Resolution and Standing card design), the coordinated 04-n118/119/123/126 §9.2 cross-resource pass, and 09-06 (the modifier card design pass this whole program was building toward). Four emergent strategic patterns from a separate card-ideas doc were reviewed and closed as no-op (valid strategy exploits under the existing ruleset, not card design seeds).

*Note: the source cross-faction file also carried later sections (H–N, "Post-Audit Modifier Deck Additions," S128–S129+) proposing a specific set of net-new modifier cards and a 53-card deck floor. That proposal doesn't match what was actually built during the real S131–135 modifier design pass (different card names/IDs, no use of the eventual ModActionCard/ModBattleCard/ModReactCard 3-subclass schema, a 53-card floor vs. the actually-locked 54-card floor at PM02 L240) — reviewed and confirmed superseded, safe to leave out of this summary; full text preserved in the archived source file if ever needed.**

---

## Closing Note

This audit program predates the full CA/PA design-review program and the modifier card corpus (ModAction/ModBattle/ModReact) that now exists — none of that had been designed yet when these six files were written. Its conclusions are a useful historical baseline for why later design decisions were made, but they are **not current**. Much of what was flagged here as a gap (the unbuilt modifier decks, missing Standing cards, §9.2 ceiling inversions, territorial-recovery gaps) may already be addressed by cards added since. The planned full-corpus refresh pass that this summary exists to support (PM05 09-16 steps 4–5) needs to re-derive its findings against the current state of the card corpus — not assume anything documented here still holds.
