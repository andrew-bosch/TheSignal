# STD + SYN Combined Set Audit — S123
*04-n91 · Follows STD+GUI audit (S122). Same structure. STD section is abbreviated — full STD coverage documented in prior audits (GHO §A · DIR §A · GUI §A).*

---

## Pre-Audit Notes (S123)

*Written before the full audit. These findings are based on the full card-body read of the Syndicate set during the S123 startup sequence. Flag items are hypotheses to test, confirm, or resolve during the audit — they are not conclusions.*

### Syndicate Set at a Glance

15 active cards: 11 CA + 3 PA + 1 MOD stub.

| Card | Layer | Function | Subject | Beat | Cost |
|------|-------|----------|---------|------|------|
| SYN.CA.1 Leveraged Acquisition | Economy | Add | NativeResource | 3 | C×2 |
| SYN.CA.2 Short the Market | Economy | Remove | NativeResource | 3 | C×2 |
| SYN.CA.3 Hostile Acquisition | Territory | Redirect | StructureBlock | 3 | C×5 |
| SYN.CA.4 Golden Parachute | Economy | Protect | NativeResource | 2 | C×N (declared) |
| SYN.CA.5 Regulatory Capture | Submission | Block | NamedActionType | 2 | C×3 |
| SYN.CA.6 Parasitic | Economy | Add | IntelToken | 2 | C×2 |
| SYN.CA.7 Corporate Blackmail | Economy | Redirect | NativeResource | 3 | Intel×1 |
| SYN.CA.8 Land Title | Territory | Add | StructureBlock | 3 | C×5 |
| SYN.CA.9 Hostile Takeover | Territory | Add | PresenceToken | 3 | C×4 + Intel×1 |
| SYN.CA.10 Accord Transfer | Economy | Corrupt | AccordCard | 3 | C×3 |
| SYN.CA.11 Redline | Information | Corrupt | AccordAgreement | 3 | C×2 |
| SYN.MOD.1 Accord Leverage | — | — | — | 4 | Intel×1 (stub) |
| SYN.PA.1 Acquisition Offer | Territory | Redirect | PresenceToken | 4 | C×1 |
| SYN.PA.2 Public Dividend | Economy | Add | NativeResource (cond.) | 4 | C×2 |
| SYN.PA.3 Data Acquisition | Information | Reveal | IntelTokensHeld | 4 | C×1 |

**Legend:** C = Capital (native). Intel = IntelToken (any faction unless noted).

### Layer Coverage (pre-audit)

| Layer | Syndicate cards | Assessment |
|-------|----------------|------------|
| Economy | CA.1 · CA.2 · CA.4 · CA.6 · CA.7 · CA.10 · PA.2 | 7 of 14 — dominant |
| Territory | CA.3 · CA.8 · CA.9 · PA.1 | 4 cards — acquisition suite |
| Information | CA.11 · PA.3 | 2 cards |
| Submission | CA.5 | 1 card |
| Standing | — | **Gap** |
| Resolution | — | **Gap** |

Standing note: PS entries come from portrait fields only (CA.7 Portrait=−1 always; CA.10 crit-fail=−2 PS; CA.11 crit=+1 PS; PA.1 both parties +1 PS on accept). No dedicated faction Standing card.

---

### Pre-Audit Flag Items

Five hypotheses to drive the S123 analysis. Each should be explicitly addressed in Sections B–F.

---

**FLAG 1 — §9.2 inversion: zero cross-resource costs at high power levels**

Every Syndicate cost is Capital (mono) or Intel token. No cross-resource card exists in the faction set. §9.2 rule: mono = floor power; cross = ceiling power.

Highest-power plays by cost: CA.3 Hostile Acquisition (C×5, redirects a structure block), CA.8 Land Title (C×5, tripwire territorial claim), CA.9 Hostile Takeover (C×4 + Intel, replaces all target presence in a district). All three produce structural or positional changes at ceiling-tier effects — yet priced as mono. This is the same inversion pattern flagged in DIR (04-n118) and GUI (04-n119).

**Audit action:** Apply §9.2 floor/ceiling test to all 11 CAs. Document which cards trigger inversion and assess whether a systematic faction-level remedy is warranted.

---

**FLAG 2 — Non-native generation: doctrine justification required**

Two cards deliver non-Capital resources to Syndicate when played against non-Syndicate-native districts:

- **CA.1 Leveraged Acquisition**: grants 1 native resource from any district with no presence required. Played in a non-Capital district = Syndicate receives a non-native resource.
- **CA.7 Corporate Blackmail** (comply path): redirects target's native to Syndicate. If the target holds a non-Capital resource, Syndicate receives non-native.

Every SYN cost is Capital or Intel. Non-native resources acquired via CA.1/CA.7 have no faction-native spending path — usable only through STD cross-resource cards (CA.6–CA.9, CA.11) or plays in matching-native districts. Compare: GHO.CA.10 Flip carries explicit doctrine justification for non-native generation. Syndicate's §5a description (economy extraction · resource redirection · accord manipulation) implies this is intentional, but does not state it.

**Audit action:** Check §5a and §8.4 for explicit doctrine coverage of non-native acquisition. If absent, flag for design decision.

---

**FLAG 3 — Accord manipulation suite without formation capability**

CA.10 + CA.11 + MOD.1 form the deepest Accord manipulation suite across all five factions. CA.10 replaces a party on a live Accord; CA.11 alters a numeric fill-in term; MOD.1 forces acceptance of a draft as written. No other faction has three Accord-targeting cards.

But Syndicate has no Accord-formation card. The suite is entirely parasitic on STD.MOD.1 Overture or STD.PA.8 Table an Accord being executed by other factions. If the diplomatic layer is thin in a given game — few Accords formed, players avoid the mechanism — all three Syndicate tools go dormant simultaneously.

**Question:** Is parasitic Accord entry the intended posture? If so, does it need environmental support (a faction rule or mechanic that rewards Syndicate when Accords exist, beyond the card effects themselves)?

---

**FLAG 4 — Intel economy self-sufficiency**

Syndicate's Intel circuit:

- **Generate:** CA.6 Parasitic (ARBITER delivers Intel keyed to first Beat 3 submitting faction · fires only when another faction targets the district) · PA.3 Data Acquisition (trade or reveal paths)
- **Spend:** CA.7 Corporate Blackmail (Intel×1, any faction) · CA.9 Hostile Takeover (Intel×1, keyed to target faction)

CA.6 is conditional — fires only when another faction commits a Beat 3 card to the same district. CA.9's cost specifically requires Intel keyed to the takeover target. CA.6 delivers Intel keyed to *first submitting faction*, which may not be the intended CA.9 target.

**Question:** Is the Intel circuit reliable enough for CA.7 and CA.9 to be consistently playable? Or does Syndicate depend structurally on Ghost's surplus Intel production (GHO.CA.4/CA.7) to fund its highest-value territory plays?

**Audit action:** Trace the Intel circuit end-to-end; assess whether CA.6's contingent generation creates exploitable gaps in CA.9 availability.

---

**FLAG 5 — SYN vs. GUI economic differentiation**

Both factions are Capital-denominated and economy-primary. §5a distinguishes them:

- Syndicate: economy extraction · resource redirection · accord manipulation
- Guild: permanence of physical form · earnings through construction · sustainable yield

Differentiation risk: CA.1 Leveraged Acquisition extracts native resource from any district with no presence requirement. GUI.CA.2 Materials Acquisition and GUI.CA.5 Infrastructure Yield also yield native resources as faction income. The effect is similar; the mechanism differs (CA.1 = immediate transactional lift; CA.2/CA.5 = conditional positional wager requiring the named faction to act first).

**Audit action:** Confirm the extraction designs hold distinct doctrine justifications. Identify any card pairs across the two sets with mechanically equivalent effects — if any exist, flag for differentiation.

---

### DB Sync Note

**SYN.PA.3 Data Acquisition:** DB previously showed cost_type=free, cost_primary_amount=0, uses_intel_token=0. Corrected during S123 startup sequence: cost_type=mono, cost_primary_amount=1. DB row updated; table above reflects corrected value.

---

## Section A — Standard Set (Abbreviated)

*Full Standard analysis in card_analysis_STD_GHO.md §A. STD economic integration results unchanged from S120 — all five faction natives have STD spending destinations; no unspendable acquired resources. This section notes STD cards with specific Syndicate relevance.*

- **STD.MOD.1 Overture / STD.PA.8 Table an Accord:** The only Accord-formation paths in the game. SYN.CA.10, CA.11, and MOD.1 are all parasitic on one of these being executed first. If no player invests in Accord formation, Syndicate's entire manipulation suite has no targets.
- **STD.CA.9 Fund:** Economy|Add|NativeResource — pushes Capital to a named faction's Dispatch Case. Mechanically inverse to SYN.CA.7 Corporate Blackmail (CA.7 takes native; Fund gives it). Together they express the full Capital mobility spectrum.
- **STD.CA.1 Build Structure / STD.CA.2 Demolish:** SYN.CA.8 Land Title (Grant Deed React) fires specifically when any faction places a structure — STD.CA.1 is its primary trigger. SYN.CA.3 Hostile Acquisition triangulates the same space: CA.1 builds, CA.3 seizes.
- **STD.CA.13 Disinformation Campaign:** Covert Remove|IntelToken. Directly counters SYN.CA.6 Parasitic — removes the Intel token Parasitic just deposited in Syndicate's case.

### Cross-Faction Reference (from STD+GHO §A — S119/S120)

**MOD Inventory (6 cards across all factions)**

| Faction | MOD cards |
|---------|-----------|
| Standard | STD.MOD.1 Overture |
| Ghost | GHO.MOD.1 Clarify Misinformation |
| Network | NET.MOD.1 Signal Break · NET.MOD.2 Reputational Strike |
| Syndicate | SYN.MOD.1 Accord Leverage |
| Guild | GUI.MOD.1 Return to Site |
| **Directorate** | **None** |

MOD design is largely unexplored. Coverage gaps should be evaluated across CA, PA, and MOD before assuming a new CA is required. GHO.MOD.1 is the reference model: a React that fires on a PA submission event rather than a CA consuming a covert slot.

**Standing Gap (04-n108)**

| Faction | Standing cards | Status |
|---------|---------------|--------|
| Standard | CA.13 · PA.4 · PA.7 | Floor — correctly positioned |
| Directorate | DIR.CA.7 Institutional Brief | Calibration check — should outperform CA.13 |
| Network | NET.CA.7 Ground Signal | Calibration check — should outperform CA.13 |
| Ghost | None | Design gap |
| Syndicate | None | Design gap |
| Guild | None | Design gap |

**STD Outstanding Issues**

| Card | IR | Note |
|------|----|------|
| STD.CA.9 Fund | 0 | Art 07 delivery procedure gap — not a design question |
| STD.CA.12 Absolute Compromise | 0 | Design decisions cleared S120; consolidated sign-off pending |
| STD.PA.8 Table an Accord | 1 ✓ | — |
| STD.MOD.1 Overture | 0 | Perspectives · Card ID · Value rating TBD (D-04-08) |

---

## Section B — Syndicate Set Analysis

### §6.4 Economic Integration Audit (5-Check Framework)

1. **Generation check:** Two cards can deliver non-Capital resources to Syndicate. **SYN.CA.1 Leveraged Acquisition** grants 1 native resource from any district with no presence requirement — when played in a non-Capital district, Syndicate receives non-native. **SYN.CA.7 Corporate Blackmail** (comply path, Economy|Redirect|NativeResource) transfers target's native to Syndicate; if target holds a non-Capital resource, Syndicate receives non-native. CA.7 spec gap: `on_accept` has debit-only expression (`faction(target).resource(native) -= 2`); credit line (`faction(Syndicate).resource += X`) absent from spec code; transfer established by arbiter_note + Redirect label. Neither card carries explicit doctrine justification for non-native generation in its spec. Compare: GHO.CA.10 Flip carries the required justification ("intelligence has economic value; target's assets turned against them"). ⚠ Flag for 04-n124.

   **CA.6 Parasitic** generates Intel tokens (not native resources); CA.9 Hostile Takeover acquires presence (not resources). PA.2 Public Dividend injects 2 Capital but delivers it to whoever holds Dominant — may benefit Syndicate or another faction. **Generation verdict: ⚠** — non-native generation present, doctrine doc absent.

2. **Spending check:** Capital (native) has deep spending paths — 13 of 15 cards carry Capital cost. Intel tokens spend via CA.7 (Intel×1 as cost) and CA.9 (Intel×1 keyed to target faction). Non-native resources acquired through CA.1 or CA.7: **no SYN card costs non-native resources**. Spending is only available through STD cross-resource cards (CA.6/CA.7 at Exposure-named, CA.8/CA.9 at Capital-named if acquired Capital, CA.11 at Mandate + own-native) or district-native territory ops in producing districts. Technically no unspendable resource (STD paths exist), but the faction architecture provides no incentive for cross-economy acquisition — every SYN tool costs Capital. ⚠ Architecturally deprioritized. **Spending verdict: ✓** (passes strictly; noted asymmetry with FLAG 2).

3. **Floor calibration (§9.2):** Multiple inversions identified. Mono-Capital cards at elevated power:
   - C×2: CA.11 Redline (permanent Accord term alteration, covert) and CA.2 Short the Market (covert native removal, economic attack) both carry significant effects. Floor-borderline.
   - C×3: CA.10 Accord Transfer — permanent party replacement on a live Accord. This is a ceiling-tier effect at mono cost. **Clear inversion.**
   - C×4 + Intel×1: CA.9 Hostile Takeover — replaces ALL target presence in a district. Both cost components are faction-accessible without cross-economy commitment (Intel via CA.6). Near-ceiling effect, dual-but-same-economy cost. **Inversion.**
   - C×5: CA.3 Hostile Acquisition (structure redirect) and CA.8 Land Title (territorial claim + tripwire). High absolute cost within the faction set; no cross-economy component. **Ceiling effects at mono.** ✗

4. **Ceiling coverage (§9.2):** Zero cross-resource cost cards in the Syndicate faction set. DB confirms all SYN cards are mono or free (Intel-cost cards use a non-native-resource cost class, not a second-faction-native). No cross ceiling exists. Same architecture as GUI (04-n119) and parallel to DIR (04-n118). ✗

5. **Gap verdict:** ⚠ §9.2 inversion on CA.10 (C×3, permanent Accord corruption), CA.9 (C×4+Intel, wholesale presence replacement), CA.3 (C×5, structure seizure), CA.8 (C×5, territorial claim). Zero cross-ceiling cards in faction set. Non-native generation in CA.1 and CA.7 lacks doctrine justification. Three prior audits (DIR, GUI, and now SYN) all show the same §9.2 pattern — this is systemic across Capital-heavy factions. **New PM05 item: 04-n123** (SYN §9.2 ceiling gap). **New PM05 item: 04-n124** (non-native generation doc).

---

## Section C — §5a Alignment

§5a deck-feel: "wealthy, patient, capable of restructuring the table's deals from underneath."

**Wealthy:** The deck runs on Capital entirely. CA.4 Golden Parachute (variable Capital bribe defense) is the signature "wealthy faction" play. Seven Economy cards plus high-cost territorial plays signal Capital saturation. ✓

**Patient:** Beat 2 plays (CA.4, CA.5, CA.6) establish positional investments before Beat 3 resolves. CA.8 Land Title is the clearest patience play — Grant Deed sits on a district and waits for another faction to build, then Syndicate's React fires. CA.10/CA.11 require active Accords that may take multiple Quarters to appear. ✓

**Restructuring deals from underneath:** CA.10 (replace party), CA.11 (alter term), MOD.1 (force acceptance). This is the signature capability and it's well-served. ✓

§5a doctrine: "economy extraction, resource redirection, accord manipulation."

- Economy extraction: CA.1 (unilateral resource pull), CA.2 (opponent removal), CA.7 (coercive redirect). ✓
- Resource redirection: CA.7 (native flow redirect), CA.3 (structure redirect), PA.1 (presence redirect). ✓
- Accord manipulation: CA.10, CA.11, MOD.1 stub. Deepest suite in game. ✓

§5a win path: "Win path: Ring 1/2 Dominant." Four cards serve this directly: CA.3, CA.8, CA.9, PA.1. Territory acquisition is the win-condition delivery mechanism, but it doesn't appear in the §5a doctrine statement. No misalignment — §5a describes economic identity; win path is separately noted. Minor: presence generation is slow (CA.9 does mass replacement in one play; incremental building depends on STD.PA.1). Syndicate cannot gradually accumulate presence the way Ghost or Network can.

**§5a verdict: ✓** Deck feel, doctrine, and win path all coherent.

---

## Section D — Cross-Faction Differentiation

### SYN vs. STD

STD.CA.9 Fund pushes Capital to a named faction; SYN.CA.1 Leveraged Acquisition pulls native from any district. Opposite directions. Distinct. ✓

STD.MOD.1 Overture and STD.PA.8 Table an Accord form Accords. SYN CA.10/CA.11/MOD.1 modify them. Prerequisite relationship, not overlap. ✓

No taxonomy entries shared between STD faction-specific operations and SYN faction-specific cards. ✓

### SYN vs. DIR

Acquisition against suppression. SYN's territorial plays (CA.3 Hostile Acquisition, CA.8 Land Title, CA.9 Hostile Takeover) seize and replace presence; DIR's suppression toolkit (CA.5 Sanctioned Raid, PA.3 Entry/Exit Controls, CA.2 Detain) removes and restricts presence. In contested districts, their operations are directly opposing.

DIR.PA.6 Standing Injunction blocks PA taxonomy at the faction level — if targeted at Syndicate, removes SYN.PA.1 (Acquisition Offer) and SYN.PA.2 (Public Dividend) from Syndicate's play set for that Quarter. DIR.CA.1 Invoke Jurisdiction scope (open design question C1 in DIR audit) includes whether it can block Accord-type operations; if yes, it directly suppresses SYN.CA.10/CA.11/MOD.1 in the named district.

Accord manipulation is SYN's safest operating layer relative to DIR — DIR's territorial toolkit does not touch it. In a DIR-heavy game, SYN's optimal path shifts from territorial acquisition to Accord manipulation.

Economy: Capital vs. Mandate — orthogonal. Both §9.2-gap factions (SYN: 04-n123; DIR: 04-n118). Same zero-cross-ceiling pattern from different native-resource bases.

### SYN vs. GUI

Both Capital-denominated, economy-primary. Key mechanical distinctions:

- **Income model:** Guild wagers on opponent actions (CA.2/CA.5/CA.6 predict another faction's moves). Syndicate extracts directly (CA.1 unilateral, CA.7 coercive). Opposite information-requirement profiles.
- **Territory model:** Guild builds through STD.CA.1 + PA.1 — permanence through construction. Syndicate seizes through CA.3/CA.8/CA.9 — control through acquisition. Mirror operations.
- **CA.1 vs. GUI.CA.2/CA.5:** Both yield native resources, but CA.1 is immediate and unilateral; Guild's income is conditional on another faction's action. Mechanically distinct despite similar economic function.
- **SYN.CA.3 as anti-Guild threat:** Hostile Acquisition targets structure blocks — Guild structures are its primary targets. SYN.CA.8 files claims on undeveloped land before other factions build, pre-positioning against Guild's planned expansion districts.
- **Accord layer:** GUI.PA.2 Infrastructure Bond creates an AccordAgreement. SYN.CA.10/CA.11/MOD.1 can corrupt any live Accord without Guild's consent.

No overlapping faction-specific taxonomy entries. ✓

### SYN vs. GHO

Both use Intel tokens; both have covert-style operations.

- **Intel purpose:** Ghost collects Intel for revelation effects (Information|Reveal — intelligence as weapon). Syndicate uses Intel as transactional cost for territorial plays (CA.7, CA.9). Different spending destinations for the same commodity. ✓
- **Intel depth:** Ghost has 5 Intel-generation cards (CA.5, CA.6, CA.7, CA.8, CA.9) plus IS-xx. Syndicate has CA.6 (contingent) and PA.3 (trade path). Ghost's Intel depth exceeds Syndicate's by design — Syndicate is a downstream Intel consumer, not a primary producer.
- **Non-native generation:** GHO.CA.10 Flip carries explicit doctrine justification. SYN.CA.1/CA.7 do not. Same effect class, different spec completeness (→ 04-n124). Architecturally distinct; spec asymmetry noted. ✓

### Faction Cross-Reference (5-faction synthesis, complete)

| Faction | Native resource | Income model | Territory posture | §9.2 ceiling gap | Information posture |
|---------|----------------|-------------|------------------|-----------------|---------------------|
| Ghost | Findings | Intel-activity yield (CA.5/CA.7/CA.8) | None — zero territory cards | Not flagged | Dominant — 5+ Reveal cards, deep Intel economy |
| Directorate | Mandate | Institutional yield (CA.6 Audit, Permanent-scaled) | Suppression — clears space; builds through STD | ✗ 04-n118 — 11/12 mono | External — requires STD PA setup (PA.2 Convene) |
| Guild | Capacity | Wager/passive (CA.2/CA.5/CA.6 on STD triggers) | Construction — Add/Protect; permanence through building | ✗ 04-n119 — zero cross | None — zero Information cards |
| Syndicate | Capital | Extraction/coercion (CA.1 unilateral, CA.7 coercive) | Acquisition — seize/replace (CA.3/CA.8/CA.9/PA.1) | ✗ 04-n123 — zero cross | Transactional — Intel as cost input (CA.7, CA.9) |
| Network | Exposure | Loop/sacrifice (CA.2 Disclosure Loop; CA.6 PS→Intel) | Broadcast reach — restricted expansion (CA.5 Baryo); consolidation (PA.2); opportunistic (MOD.1) | ⚠ 04-n126 — cross exists but Findings-gated | Dominant public — 4 Reveal cards; all table-broadcast |

DIR/GUI/SYN all show zero-cross-ceiling architecture — systemic across mono-economy factions. Network is the exception: cross ceiling exists in CA.1 (E×1+F×1 — the only faction-specific cross-ceiling card), but Findings-gated (Ghost dependency). Ghost and Network are the two information-dominant factions with opposite disclosure models: Ghost concentrates (private IS-xx); Network distributes (public broadcast to all players). 5-faction synthesis complete S123 (04-n90 ✅).

---

## Section E — §9.2 Floor/Ceiling Mapping

| Card | Cost | DB cost_type | Effect tier | §9.2 status |
|------|------|-------------|-------------|-------------|
| SYN.CA.1 Leveraged Acquisition | C×2 | mono | Floor — 1 native resource, any district | ✓ |
| SYN.CA.2 Short the Market | C×2 | mono | Floor — removes 1 native from target | ✓ |
| SYN.CA.3 Hostile Acquisition | C×5 | mono | **Ceiling** — seizes target's structure block | ✗ inversion |
| SYN.CA.4 Golden Parachute | C×N var | variable | Floor/mid — bribe defense; Capital retained+returned on success | ✓ |
| SYN.CA.5 Regulatory Capture | C×3 | mono | Floor/mid — blocks 1 named action type for 1 round | ✓ (borderline) |
| SYN.CA.6 Parasitic | C×2 | mono | Floor — contingent Intel generation | ✓ |
| SYN.CA.7 Corporate Blackmail | Intel×1 | free+Intel | Mid — coercive ElectPlayer; accept/decline split | ✓ (Intel cost distinct) |
| SYN.CA.8 Land Title | C×5 | mono | **Ceiling** — territorial claim + Grant Deed React tripwire | ✗ inversion |
| SYN.CA.9 Hostile Takeover | C×4 + Intel×1 | mono+Intel | **Ceiling** — replaces ALL target presence in district | ✗ (dual cost partly mitigates; both same-economy accessible) |
| SYN.CA.10 Accord Transfer | C×3 | mono | **Ceiling** — permanent party replacement on live Accord | ✗ inversion |
| SYN.CA.11 Redline | C×2 | mono | Mid — alters Accord numeric term, covert | Borderline (Accord stakes-dependent) |
| SYN.PA.1 Acquisition Offer | C×1 | mono | Mid — presence transfer + PS exchange, ElectPlayer | ✓ (elective structure limits exposure) |
| SYN.PA.2 Public Dividend | C×2 | mono | Floor — seasonal Capital injection, other-conditional | ✓ |
| SYN.PA.3 Data Acquisition | C×1 | mono | Floor — Intel reveal/trade | ✓ |

**Clear inversions:** CA.3, CA.8, CA.10 = 3 definite. CA.9 = partial (dual cost). CA.11 borderline.
**Pattern:** All three prior audits (DIR 04-n118, GUI 04-n119, SYN 04-n123) show zero cross-ceiling architecture. Systemic across Capital-class factions.

---

## Section F — Outstanding Issues Inventory

| Card | IR status | Blocking dependency |
|------|-----------|-------------------|
| CA.1 | ✓ | — |
| CA.2 | Open | Art 03: covert "applied silently" protocol + minimum floor = 0 |
| CA.3 | Open | GUI.CA.1 cross-card interaction design; compensation mechanics |
| CA.4 | ✓ | — |
| CA.5 | Open | NamedActionType definition; Guild-primary action modifier |
| CA.6 | Open | Art 03 Beat 2 procedure (04-n27 remaining item) |
| CA.7 | Open | ElectPlayer covert procedure not in Art 03; comply amount TBD |
| CA.8 | Open | Grant Deed Art 03 §18 trigger timing (04-n27); Art 02 reg complete (DB:113) |
| CA.9 | Open | Token replacement logistics (supply vs. reserve); void-on-Absent edge case |
| CA.10 | ⚠ balance | Balance review (parallel to 04-n88) |
| CA.11 | ✓ | — |
| MOD.1 | Stub | Procedure, scope, party requirement, ID all TBD |
| PA.1 | ✓ | — |
| PA.2 | Open | DividendMarker Art 02 registration |
| PA.3 | ⚠ balance | Balance doctrine review (04-n88); DB corrected S123 (free→mono, C×1) |

**Resolved: 4 of 15** (CA.1, CA.4, CA.11, PA.1). Highest open-issue density of any faction set audited to date.

Dominant bottlenecks:
1. Art 03 Beat 2 procedure (04-n27) — gates CA.6 and CA.8.
2. ElectPlayer covert procedure — gates CA.7 (and extends to SYN.PA.1/SYN.PA.3 if covert context is relevant).
3. NamedActionType definition — gates CA.5 entirely.
4. DividendMarker Art 02 registration — gates PA.2.

---

## Section G — Audit Findings and PM05 Items

**Completed:** STD+SYN combined set audit (04-n91). Full card-body read + §6.4 economic integration audit + §5a alignment + cross-faction differentiation.

### New PM05 Items

**04-n123 — SYN economy: §9.2 cross-resource ceiling gap.** Zero cross-resource cost cards in Syndicate faction set. §9.2 inversions: CA.10 (C×3, permanent Accord party replacement), CA.9 (C×4+Intel, wholesale presence replacement), CA.3 (C×5, structure seizure), CA.8 (C×5, territorial claim) all exceed floor power with zero cross-economy commitment. Same pattern as DIR (04-n118) and GUI (04-n119) — now confirmed systemic across three Capital-adjacent factions. Design action: identify 1–2 SYN cards for cross-resource cost addition at ceiling power tier. Candidates: CA.3 (add Intel or district-native requirement) · CA.9 (Intel is same-economy; consider adding district-native or second-faction-native) · CA.10 (Accord corruption at ceiling power; add Mandate or Intel to reflect political/intel overhead). Address alongside 04-n118 and 04-n119 in cross-faction §9.2 pass. Ref: 00a §9.2; 00a-78. Output of 04-n91 (S123).

**04-n124 — SYN.CA.1/CA.7: non-native generation doctrine documentation.** CA.1 Leveraged Acquisition generates non-native resources when played in non-Capital districts (no presence restriction). CA.7 Corporate Blackmail comply-path redirects target's native to Syndicate — non-Capital when targeting non-Syndicate factions. Neither card carries explicit doctrine justification for non-native generation in its spec (compare: GHO.CA.10 Flip states the justification clearly). §5a framing ("economy extraction, resource redirection") implies intentionality but does not state it. Required action: add brief doctrine justification to CA.1 and CA.7 specs ("Syndicate converts any district's economic output; extraction is faction-doctrine, not incidental") or add a limiting clause if non-native acquisition is not the design intent. Non-blocking — card mechanics are valid; spec annotation needed. Output of 04-n91 (S123).

**04-n125 — SYN Accord manipulation suite: parasitic posture review.** CA.10 + CA.11 + MOD.1 form the deepest Accord manipulation suite in the game (3 cards). None of these can function without a live Accord. Syndicate has no Accord-formation card — the suite is entirely dependent on STD.MOD.1 Overture or STD.PA.8 Table an Accord being played by another faction. Design decision: (A) accept parasitic Accord posture as doctrine — Syndicate is a deal-corruptor, not a deal-maker, and the economic incentive to form Accords means live Accords will usually exist; (B) add a faction rule or Upkeep mechanic that creates lightweight Accord presence when none exists (not a new card — a governing rule); (C) add Accord-formation capability to Syndicate's card set, giving them agency over Accord availability. Gate: MOD.1 stub completion. Output of 04-n91 (S123).

### Artifacts Updated

- `Whiteboard/card_analysis_STD_SYN.md` — this file; sections A–G complete.
- Art 04b §6.4 — STD+SYN audit results section added.
- Art 04b §8.4 — Syndicate section updated to S123 set.
- PM05 — 04-n91 ✅; 04-n123, 04-n124, 04-n125 added; 00a-78 updated.

---

*Stub created S123 pre-audit. Full audit to follow.*
