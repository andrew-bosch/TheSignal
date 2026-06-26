# STD + DIR Combined Set Audit — S121
*04-n89 · Follows STD+GHO audit (S119/S120). Same structure. STD section is abbreviated — full STD coverage documented in card_analysis_STD_GHO.md.*

---

## A. STANDARD SET

Standard set audited in full at S119/S120 (card_analysis_STD_GHO.md §A). Summary carried forward.

**STD coverage in service of DIR (what DIR relies on):**
- Territory|Add|PresenceToken: STD.CA.3 Campaign · STD.CA.8 Buy Influence · STD.PA.1 Open Operations — DIR's entire native presence-building toolkit
- Territory|Add|StructureBlock: STD.CA.1 Build Structure · STD.PA.3 Public Commission — available to DIR, no DIR-specific structure card
- Territory|Remove|PresenceToken: STD.CA.4 Undermine — baseline removal; DIR.CA.5 Sanctioned Raid is the faction-specific, higher-force version
- Standing floor: STD.CA.13 Disinformation Campaign · STD.PA.4 Public Censure · STD.PA.7 Public Address
- Accord lock: STD.CA.11 Tort Interference (Mandate + own-native; one of two STD cards requiring Mandate)
- Economic sanction: STD.PA.6 Economic Sanction (removes NativeResource at mono Mandate×1)
- Attribution groundwork: STD.PA.4 · STD.PA.5 — feed DIR.PA.2 Convene an Inquiry

**STD floor vs. DIR ceiling:** Where STD and DIR share a subject, DIR is the faction-enhanced version:
- Presence removal: STD.CA.4 Undermine (single token, Mandate×3 cross) → DIR.CA.5 Sanctioned Raid (scaled removal, boost model, Intel gate, higher stakes)
- Presence placement cost: STD economy floor → DIR.PA.1 Regulatory Override raises it Seasonally for the whole district
- No STD equivalent for DIR.CA.2 (Detain), DIR.CA.3 (Surveillance), DIR.CA.8 (Enhanced Scrutiny), DIR.PA.3 (Entry/Exit Controls), DIR.PA.6 (Standing Injunction) — all Directorate-exclusive

**Outstanding STD note carried forward:** STD.CA.9 Fund (IR=0) is the only STD card unresolved from design pass perspective. Not a DIR-specific concern.

---

## B. DIRECTORATE SET

### B1. Coverage Map (12 active cards)

| Card | Layer | Function | Subject | Beat | Cost | IR |
|------|-------|----------|---------|------|------|----|
| DIR.CA.1 Invoke Jurisdiction | Submission | Block | CovertOperation | 2 | M×2 | 0 |
| DIR.CA.2 Detain | Territory | Move | DeploymentMarker | 3 | M×3 | 0 |
| DIR.CA.3 Surveillance Placement | Information | Reveal | CovertOperation | 2 | M×2 | 0 |
| DIR.CA.4 Tactical Redirection | Territory | Move | PresenceToken | 2 | M×2 | 0 |
| DIR.CA.5 Sanctioned Raid | Territory | Remove | PresenceToken | 3 | M×1+N×1+Intel | 0 |
| DIR.CA.6 Institutional Audit | Economy | Add | NativeResource | 3 | M×1 | 0 |
| DIR.CA.7 Institutional Brief | Standing | Shift | PublicStanding | 3 | M×2 | 0 |
| DIR.CA.8 Enhanced Scrutiny | Resolution | Modify | Difficulty | 2 | M×2 | 0 |
| DIR.PA.1 Regulatory Override | Territory | Modify | PresenceToken | 4 | M×2 | 0 |
| DIR.PA.2 Convene an Inquiry | Information | Add | IntelToken | 4 | M×3 | 1 |
| DIR.PA.3 Entry/Exit Controls | Territory | Block | DeploymentMarker | 4 | M×3 | 0 |
| DIR.PA.6 Standing Injunction | Submission | Block | PublicAct | 4 | M×3 | 1 |

**Blocked (excluded from audit):** DIR.PA.4 Regulatory Downgrade · DIR.PA.5 Regulatory Freeze — both blocked L223 (InfluenceTier is derived state; direct income modification blocked by GR 9.1). Redesign pair tracked under 04-n104.

**Legend:** M = Mandate (native). N = district NativeResource. 11/12 active DIR cards are mono-Mandate; DIR.CA.5 is cross (M×1 + N×1 + Intel token).

### B2. Layer Coverage Summary

| Layer | DIR cards | Notes |
|-------|-----------|-------|
| Territory | CA.2 · CA.4 · CA.5 · PA.1 · PA.3 | Deep; all suppression or repositioning — no Territory|Add |
| Submission | CA.1 · PA.6 | Block both covert (CA.1) and public (PA.6) — uniquely broad block coverage |
| Information | CA.3 · PA.2 | Intelligence by institutional channel (watching districts, commissioning ARBITER inquiries); no covert fieldwork |
| Economy | CA.6 | Mandate generation through Permanent-audit mechanism; no removal or redirect |
| Standing | CA.7 | Single PS card — covert, Permanent-scaled |
| Resolution | CA.8 | District-wide difficulty suppression |

**No Territory|Add cards**: Intentional. DIR builds presence exclusively through Standard (STD.CA.3, CA.8, PA.1). This is the most doctrinally explicit gap in the game: the faction whose win condition is territorial Established status has zero native presence-placement cards. See §F for assessment.

**No Modifier cards**: L1 design gap. §5a describes two DIR modifier decks (legislative assets cut PA costs / extend world events; military assets for enforcement). Both entirely undesigned at L1. Named as the headline §5a gap — see §F.

### B3. Beat Timing Distribution

| Beat | Cards | Character |
|------|-------|-----------|
| Beat 2 (Automatic) | CA.1 · CA.3 · CA.4 · CA.8 | Proactive positioning — shapes conditions before dice roll |
| Beat 3 (d100) | CA.2 · CA.5 · CA.6 · CA.7 | High-stakes probabilistic outcomes |
| Beat 4 (Automatic PA) | PA.1 · PA.2 · PA.3 · PA.6 | Public standing declarations, standing board conditions |

The Beat 2 cluster is the most distinctive character in the set. Four of eight CAs fire before any Beat 3 dice are rolled. Directorate shapes the operational environment first; other factions navigate within it. This is mechanically consistent with "methodical" in §5a.

### B4. Doctrinal Assessment

**Overwhelmingly mono-Mandate economy:** 11 of 12 active DIR cards cost Mandate only. DIR.CA.5 Sanctioned Raid is the sole cross card: its cost includes district NativeResource — the target district's native resource, which in practice is another faction's native — plus an Intel token. DIR.CA.5 is the faction's highest-force removal play, which is exactly where the §6.4 framework expects a cross card to sit. The near-mono architecture is the strongest economy-doctrine statement in the game: the Directorate operates almost entirely in institutional authority and does not traffic in other factions' currencies. Contrast with Ghost (1 cross card) and the STD set (5 cross cards). Not a gap — see §6.4 below.

**Permanent-investment feedback loop:** DIR.CA.6 Institutional Audit and DIR.CA.7 Institutional Brief both yield Mandate and PS respectively equal to the count of active Directorate Permanents in the target ring. As DIR accumulates standing board conditions (PA.1, PA.3, PA.6), the yield from Audit/Brief increases. Late-game Directorate authority compounds — the faction's economic engine is its standing regulatory presence.

**Suppression architecture — two modes:**
1. *Standing pressure* (board conditions that persist): PA.1 Regulatory Override (Seasonal, +1 cost on presence placement), PA.3 Entry/Exit Controls (Permanent, blocks deployment markers), PA.6 Standing Injunction (Permanent-until-triggered, blocks PA taxonomy)
2. *Episodic suppression* (within-month): CA.1 Invoke Jurisdiction (one-round card-type block), CA.8 Enhanced Scrutiny (one-round −15 to all Beat 3 ops in district)
3. *Hard removal* (permanent piece elimination): CA.2 Detain (deployment marker → Detention), CA.5 Sanctioned Raid (presence tokens removed)

No other faction in the set has standing board conditions of this scope. In a late-game Quarter where DIR holds PA.3 on one district, PA.1 on a second, and PA.6 blocking a faction's expand-PA type — the whole table's play space is constrained. This is "capable of making the whole table play defensively" delivered mechanically.

**Self-inclusive design:** DIR.CA.8 Enhanced Scrutiny applies its −15 modifier to all Beat 3 ops in the named district, including Directorate's own. The design rationale is explicit: "scrutiny means something only when it applies uniformly." This is the institutional restraint register — the Directorate accepts operational friction in exchange for doctrinal legitimacy.

### B5. Win Path Tension

Win path = Established in more districts than any other faction. DIR has no Territory|Add card. Assessment:

The suppression kit enables the win path indirectly: by pushing opponents below Established (Sanctioned Raid removes presence, Detain removes deployment markers, Entry/Exit Controls blocks deployment marker placement, Regulatory Override raises the cost of all presence actions), DIR maintains moderate presence across more districts than any faction can in the constrained environment.

The resource tension is real: spending Mandate×3 on Entry/Exit Controls is Mandate×3 not spent on STD.PA.1 Open Operations (3 Mandate = 3 presence tokens via PA.1). Directorate must allocate between suppression spend and expansion spend from the same mono-Mandate pool. The passive +1 Mandate/Quarter generation plus district Mandate yield provides baseline runway, but DIR.CA.6 Institutional Audit's value is conditional on having Permanents already in play — which requires prior Mandate investment. The feedback loop takes 2–3 Quarters to compound meaningfully.

**Verdict:** Doctrine-coherent but playtest-critical. The win path is mechanically supported; whether Mandate allocation allows simultaneous suppression and expansion at required scale is unknown until playtesting. Flag for 04-n110 cross-faction §5a alignment pass.

### B6. Cross-Faction Differentiation (vs. Ghost — S120 commitment)

S120 audit deferred the Ghost sustained-pressure comparison to this audit. Settling it here.

**Ghost:** Point-disruption / reactive. Every Ghost card is Immediate or Permanent-but-self-executing (no persistent board conditions). Ghost strikes targeted intelligence and operational blows — each op is a discrete event. Ghost has no standing board conditions. The covert toolkit is about depth of intelligence and targeted interception, not environmental shaping.

**Directorate:** Standing pressure / proactive. Three PA cards create persistent board conditions that operate across months. Four Beat 2 cards shape conditions before dice are rolled. The Directorate doesn't react to the table — it installs the framework within which the table operates.

This is the clearest doctrinal differentiation in the design: Ghost sees everything and strikes precisely; Directorate shapes everything and constrains systematically. A Ghost operator decides based on information; a Directorate operator decides first and makes others navigate the constraint.

---

## C. Open Design Decisions

**C1. DIR.CA.1 block scope:** Currently blocks STD.CA.1 (Build Structure) and STD.CA.3 (Campaign) only. Should it extend to STD.CA.4 (Demolish) or STD.CA.8 (Buy Influence) to reflect full jurisdictional authority? Open in outstanding issues. Design call: broader scope strengthens the card but raises cost-value calibration questions.

**C2. DIR.CA.2 Intel token age definition:** `intel(faction=faction(target), age_rounds<=1)` — "Fresh" token requirement. Plausibly clear from Art 02 §12 aging definitions, but not explicitly confirmed. Low-risk interpretation: Fresh = gathered this or last round.

**C3. DIR.CA.4 move count vs. restriction:** `restriction = source.presence >= 1` but `count=2`. Can the card be played if source has only 1 token? Whether count=2 is maximum or exact needs confirmation. Likely maximum (up to 2) — consistent with standard move semantics.

**C4. DIR.PA.3 displaced faction with no presence elsewhere:** Entry/Exit Controls moves deployment markers to `district.where(faction.has_presence)`. If the displaced faction holds no presence outside the named district, there is no valid destination. Governing Rule 8.3b (no elimination): fallback rule needed — marker returned to hand (faction skips next placement) or moved to Ring 3 as unconditional fallback.

**C5. DIR.CA.5 Intel token as restriction vs. cost:** Card body has Intel token in cost field. Should also appear as restriction (card unplayable without Intel in hand, separate from resource payment)? Currently "carry" status per outstanding issues. Carry.

**C6. DIR.CA.6/CA.7 yield scaling at scale:** Both cards yield proportionally to active Permanents in ring. If DIR accumulates 3+ Permanents in a single ring, yield per audit/brief becomes significant. Mandate×1 cost for potentially 3+ Mandate return (net positive) warrants playtest review. Balance flag, not a design error.

**C7. DIR.CA.8 self-inclusion doctrine:** Beat 2 ops in the district (CA.1, CA.3, CA.4) are unaffected — only Beat 3 rows take the −15. Is Directorate's own Beat 3 op inclusion intended? Design note says yes ("scrutiny means something only when it applies uniformly"). Confirmed.

---

## D. Systemic Blockers

**D1. DIR.PA.4/PA.5 (04-n104) — BLOCKED:** Both require InfluenceTier as target, which is derived state. The income-suppression design intent is valid; the implementation path requires board-state manipulation (Territory|Remove|PresenceToken PA pair). The PA version would be a public institutional act — distinct from DIR.CA.5 Sanctioned Raid (covert). Pair redesign required before DIR set is complete.

**D2. DIR.CA.3 infrastructure gates (04-n44/45/46):** Three open infrastructure items block Issues Resolved for Surveillance Placement: Art 03 Beat 2 procedure addition (04-n44), Art 02 IntelDeliverySlip component entry (04-n45), 00b IS-xx definition update (04-n46). All three require cross-artifact work.

**D3. DIR.CA.5 Sanctioned Raid gates (04-n81/82/83/84):** BM-xx registration (Art 02), Beat 0 boost detection procedure (Art 03), Beat 2/3 BM-xx resolution procedure (Art 03), Discovery mechanic definition — all block sign-off.

**D4. DIR.PA.3 persistence monitoring (04-n29):** Art 03 does not define a trigger point for ARBITER to check persistence_condition of Permanent PAs (e.g., after any influence tier change). Blocks Issues Resolved for Entry/Exit Controls. Counter-card removal also TBD.

**D5. DB registration — 3 new S106 cards:** DIR.CA.6, DIR.CA.7, DIR.CA.8 require id assignment in card_ref and component_metadata.

---

## E. Audit Bucket

*Non-blocking hygiene items surfaced during this audit.*

**E1. §8.2 staleness:** Art 04b §8.2 Directorate section is S108-era data. It lists DIR.PA.1 as "⛔ BLOCKED, PM05 04-n99" — this is stale. 04-n99 was resolved S118; DIR.PA.1 is now Territory|Modify|PresenceToken (Regulatory Override). The §8.2 enumeration also omits DIR.PA.1 and DIR.PA.2 from the active card list and does not reflect the S106 additions (CA.6, CA.7, CA.8). §8.2 is a working section — fix in place without re-sign-off.

**E2. DIR.CA.5 DB staleness — two fields:**
- *uses_intel_token=0*: DB records this as 0, but the card body has IntelToken in the cost field. If the column tracks whether a card submits Intel tokens as cost, this is a DB sync error. Verify column semantics; update if needed.
- *cost_type=mono*: DB records cost_type=mono, but the card body includes district NativeResource as a cost component — making CA.5 cross. DB is stale; card body is authoritative (Art 04 §§ = design source of truth). Update cost_type to cross.

**E3. DIR.CA.7 Institutional Brief Standing floor:** Same calibration flag as all Standing cards — should the covert PS card yield beat the STD floor? DIR.CA.7 at Mandate×2 threshold-50 d100 yields +n PS (0 without Permanents, scaling above 0 only with Permanents). Floor comparison: STD.CA.13 Disinformation Campaign (Mandate×2, mono) at a flat −2 PS to target. DIR.CA.7 is upward shift with variable yield — structurally distinct enough not to be directly comparable. Not a flag.

**E4. DIR.CA.1 and DIR.PA.6 — dual Block coverage:** Directorate is the only faction with an explicit Submission|Block at both the covert level (CA.1 blocks named card types in a district) and the public level (PA.6 blocks PA taxonomy faction-wide). This is doctrinal — the Directorate controls what is permitted to happen, not just what happens. No concern; flag as architecture-intentional for 04-n110 cross-faction pass.

---

## F. §5a DIRECTORATE FLAVOR ASSESSMENT

Reference: Art 04 §5a Directorate entry.

**§5a declares:**
- *Doctrine:* "Survival requires control, restraint, and continuity"
- *Economy:* Mandate
- *Deck feel:* institutional, methodical, capable of making the whole table play defensively
- *Win path:* Established in more districts than any other faction
- *Distinguishing feature:* best suppression toolkit in game
- *Modifier deck (L1 gap):* legislative mode (PA cost reduction, world event extension) + military mode (enforcement)

### F1. Deck Feel vs. §5a

**Finding: Strong match.** The Directorate set is the most mechanically coherent faction-doctrine pairing in the L1 set.

*Institutional* — all 12 active cards are Directorate faction-specific, 11 of 12 cost Mandate only (DIR.CA.5 is cross: highest-force removal), none require adjacency or operational footprint except where explicitly doctrine-justified (Established requirement for PA.1/PA.3 = jurisdictional legitimacy; chip count > 1 for CA.6/CA.7 = operational footprint). The Directorate doesn't need to be near something to assert authority over it (CA.1, CA.3, CA.8 have no presence restriction) — institutional authority is not territorial.

*Methodical* — four of eight CAs fire at Beat 2 (Automatic). Directorate acts first, shapes the environment, then lets Beat 3 resolve within the constraints it has set. No other faction has this Beat 2 concentration. The methodical character is embedded in the timing architecture, not just the narrative voice.

*Makes the whole table play defensively* — delivered through the standing-condition PAs. PA.1 Regulatory Override changes the economic cost of all presence operations in a district. PA.3 Entry/Exit Controls hard-blocks a district to deployment markers. PA.6 Standing Injunction pre-empts a PA taxonomy faction-wide. These are not reactive cards — they are environmental constraints. Once in place, all other factions must route around them.

### F2. Win Path Mechanically Supported

**Finding: Supported with a resource tension to flag.**

The suppression kit enables the win path indirectly — Directorate holds Established status in the districts it can reach via Standard cards while preventing other factions from exceeding Established elsewhere. The mechanism is coherent.

The unresolved question is Mandate allocation: the same Mandate pool funds both suppression (PA.3 at M×3, PA.6 at M×3) and expansion (STD.PA.1 Open Operations, STD.CA.3 Campaign at M×3 cross). A Quarter where Directorate fields PA.3 + PA.6 simultaneously has spent M×6 on suppression before any expansion op. Standard presence operations are cross-resource — Campaign requires Mandate + native district resource, which means Directorate needs cross-territory income to run the Standard expansion toolkit at the same time as the faction suppression toolkit.

DIR.CA.6 Institutional Audit exists precisely to address this — it's the Mandate recirculation mechanism funded by established Permanents. The loop is: establish Permanents → generate bonus Mandate → fund expansion ops while maintaining suppression ops. This is the late-game engine.

The loop takes time to compound. In Q1–Q2, Directorate will likely be Mandate-constrained. Flag for 04-n110: verify that the economy model doesn't starve Directorate of expansion capacity in early Quarters.

### F3. Sustained vs. Point-Disruption

**Finding: Directorate is the sustained-pressure pole.** Ghost audit commitment settled.

Ghost (S120 finding): all cards immediate or Permanent-but-self-executing. Zero standing board conditions. Intelligence depth and targeted strikes.

Directorate: three Permanent/Seasonal board conditions (PA.1, PA.3, PA.6), four Beat 2 proactive cards, two permanent-removal CAs (CA.2, CA.5). The standing-condition PAs are what makes Directorate sustained — they persist across months, compound with Audit/Brief, and require counter-action to remove.

The epistodic vs. standing split within the DIR set itself: CA.1 Invoke Jurisdiction (one-round block, within-month) and CA.8 Enhanced Scrutiny (one-month −15 penalty) are episodic. CA.2 Detain (permanent removal) and CA.5 Sanctioned Raid (permanent removal at scale) are point-disruption at high force. The three PAs are the standing machinery. DIR has a more complex internal texture than Ghost — episodic, point-disruption, and sustained elements all present — but the sustained-condition PAs are the doctrinal signature.

### F4. CA/PA Gap and Modifier Deck Gap

**CA/PA balance:** 8 CAs and 4 PAs (2 with IR=1). No glaring CA/PA ratio gap. The PAs are the standing-condition machinery — having 4 at the public level is appropriate for a faction whose doctrine is public institutional authority.

**Modifier deck gap (headline):** §5a describes two Directorate modifier decks: legislative (cuts PA costs, extends world events) and military (enforcement assets). Both are entirely undesigned at L1 — zero modifier cards in the DIR set. This is the largest gap between §5a promise and L1 implementation for Directorate.

The legislative modifier deck would be the highest doctrinal expression: Directorate as the faction that makes public acts cheaper or more powerful through institutional backing. The military modifier deck would be enforcement augmentation for Sanctioned Raid and Detain — boosting the suppression kit.

This gap is structural (L1 scope, not a missed card) and the same category as Ghost's "passive Intel generation unimplemented" from S120. Flag as the primary §5a alignment item for 04-n110.

**Information gap:** DIR has no independent covert Intel generation (DIR.PA.2 Convene an Inquiry is contingent on prior STD.PA.4/PA.5 groundwork). For a faction requiring Intel tokens to play CA.2 and CA.5, the Intel supply chain is a meaningful dependency: Directorate must rely on STD.CA.5 Gather (Ghost-affiliated in doctrine) or trade for Intel. This is doctrinal — Directorate intelligence is institutional review, not fieldwork — but it creates a supply chain constraint not explicitly noted in §5a.

### F5. §5a Summary Verdict

| §5a promise | Built? | Notes |
|-------------|--------|-------|
| Institutional, methodical deck feel | ✓ Full | Beat 2 architecture + all-mono economy |
| Makes the whole table play defensively | ✓ Full | Standing-condition PA trio |
| Economy = Mandate | ✓ Full | 11/12 mono-Mandate; CA.5 is the cross ceiling (highest-force removal) |
| Best suppression toolkit in game | ✓ Full | Block, Remove, Move, Modify presence all covered; both covert and public Block |
| Win path = most Established districts | ◐ | Mechanism coherent; Mandate allocation tension needs playtesting |
| Modifier decks (legislative + military) | ✗ L1 gap | Both undesigned; headline item for 04-n110 |
| Intel supply chain | ◐ | Doctrinal (commission not fieldwork) but STD.CA.5 dependency worth noting |

---

## G. Art 04b §8.2 Update Required

Current §8.2 Directorate section is S108-era data. Fix-in-place items (working section, no re-sign-off):

1. Update set enumeration to S121 — add CA.6, CA.7, CA.8 (added S106); add PA.1 (redesigned S118, 04-n99 ✅), PA.2 (in active set)
2. Remove "DIR.PA.1 (⛔ BLOCKED, PM05 04-n99)" — 04-n99 is resolved; DIR.PA.1 is now Territory|Modify|PresenceToken (Regulatory Override)
3. Update blocked section: retain DIR.PA.4/PA.5 as BLOCKED (04-n104); DIR.PA.1 no longer BLOCKED

---

*Audit complete: STD+DIR combined set (04-n89). Next: STD+NET (04-n90).*
*§6.4 update: apply STD+DIR results to Art 04b §6.4 following Andy review.*
