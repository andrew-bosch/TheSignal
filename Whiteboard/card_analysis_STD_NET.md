# STD + NET Combined Set Audit — S123
*04-n90 · Follows STD+SYN audit (S123). Same structure. STD section is abbreviated — full STD coverage documented in card_analysis_STD_GHO.md §A.*

---

## Pre-Audit Notes (S123)

### Network Set at a Glance

| Card | Layer | Function | Subject | Beat | Cost (DB) |
|------|-------|----------|---------|------|-----------|
| NET.CA.1 Leak | Information | Reveal | District | 3 | cross: E×1 + F×1 |
| NET.CA.2 Disclosure Loop | Economy | Add | Exposure | 3 | cross: F×1 (no Exposure) |
| NET.CA.3 Breaking News | Information | Reveal | CovertOperation | 2 | mono: E×2 |
| NET.CA.4 Network Cascade | Submission | Modify | PublicAct | 2 | mono: E×2 |
| NET.CA.5 Community Anchor | Territory | Add | PresenceToken | 3 | mono: E×1 |
| NET.CA.6 Sacrifice | Economy | Add | IntelToken | 3 | free (PS−2 as success effect) |
| NET.CA.7 Ground Signal | Standing | Shift | PublicStanding | 3 | mono: E×1 |
| NET.MOD.1 Signal Break | (Territory\|Add\|PresenceToken) | React modifier | — | Beat 4 | mono: E×1 |
| NET.MOD.2 Reputational Strike | (Information\|Reveal\|PublicStanding) | React modifier | — | Beat 4 | free + Intel×1 |
| NET.PA.1 Public Disclosure | Information | Reveal | ActionAttribution | 4 | mono: E×2 + Intel×n (scaling) |
| NET.PA.2 Community Rally | Territory | Add | PresenceToken | 4 | variable: E×2+ |
| NET.PA.3 Live Coverage | Information | Reveal | FactionHand | 4 | mono: E×2 |

**Legend:** E = Exposure (Network native). F = Findings (Ghost native — cross resource for Network). MOD cards excluded from taxonomy matrix (Art 04b §9); layer/function/subject shown for spec reference only. NET.MOD.2 Reputational Strike = stub (trigger TBD, schema TBD via 04-n4).

### Layer Coverage (pre-audit)

| Layer | Cards | Notes |
|-------|-------|-------|
| Information | CA.1 · CA.3 · PA.1 · PA.3 | 4 cards — dominant; all Reveal |
| Territory | CA.5 · MOD.1 · PA.2 | 3 cards |
| Economy | CA.2 · CA.6 | 2 cards |
| Submission | CA.4 | 1 card |
| Standing | CA.7 | 1 card |
| Resolution | — | None |

### Pre-Audit Flag Items

**FLAG 1 — Reveal differentiation: 4 Information|Reveal cards**

Network has the highest Reveal concentration of any faction: CA.1 (District), CA.3 (CovertOperation), PA.1 (ActionAttribution), PA.3 (FactionHand). Subjects differ; effects differ — cancel vs. pre-resolve announce vs. scaling PS damage vs. Seasonal compliance obligation. CA.3 and PA.3 each carry an unregistered taxonomy subject (CovertOperation, FactionHand — flagged in checklists, non-gate). Mechanical differentiation must be enforced at the spec level before Issues Resolved sweep.

**FLAG 2 — Cross-resource Findings dependency (CA.1, CA.2)**

Both cross Network cards require Findings (Ghost's native resource). No other faction has a cross-resource cost denominated in a specific other faction's native. Network's ceiling architecture exists (CA.1 is the cross ceiling card) but requires Ghost cooperation or territorial control of Findings-producing districts. In games without Ghost, or without Ghost-Network trade, CA.1 and CA.2 cannot fire regardless of Exposure wealth — Network's §9.2 ceiling degrades to effectively mono.

**FLAG 3 — Modifier card schema gap (MOD.1, MOD.2)**

Both modifier cards are pending 04-n4 (modifier card schema pass). MOD.1 Signal Break has a complete design pass (S106); MOD.2 Reputational Strike is a full stub (trigger TBD, card name TBD). Both appear in DB as active (non-blocked) but cannot reach Issues Resolved until 04-n4 completes.

**FLAG 4 — §8.3 Art 04b staleness**

Art 04b §8.3 Network section lists 7 cards (S104 data). Current set has 12 cards. Five cards missing from enumeration (CA.7, MOD.1, MOD.2, PA.1, PA.2). Major update required alongside this audit.

**FLAG 5 — Win path support: expansion vs. consolidation**

Network win path = Established in more districts than any other faction. Current faction-specific territorial toolkit: CA.5 (Baryo + zero-presence initial entry), MOD.1 (opportunistic React on PA board change), PA.2 (consolidation of Established+ districts only). No unrestricted presence-placement faction card. General new-territory expansion depends entirely on STD.CA.3 Campaign and STD.CA.8 Buy Influence at cross cost (E×1 + district-native each). Assess whether the faction signature of "distributed, community-reach" is expressed by this mix or requires an additional faction-specific expansion card.

---

## Section A — Standard Set (Abbreviated)

*Full STD coverage documented in card_analysis_STD_GHO.md §A.*

**STD coverage in service of NET (what Network relies on):**

| STD Card | Relevance to Network |
|----------|---------------------|
| STD.CA.3 Campaign | Primary general presence-placement (E×1 + district-native cross) |
| STD.CA.8 Buy Influence | Secondary presence-placement (E×1 + district-native) |
| STD.CA.4 Undermine | Network's only territorial disruption card (E×1 + district-native cross) |
| STD.CA.5 Gather Intel | Intel generation without Ghost trade — faction-keyed token if Network needs CA.1/PA.1 fuel |
| STD.CA.6 Broadcast Interference | NET.CA.4 Network Cascade is an explicit mechanical dependent on this card |
| STD.CA.7 Amplify | Exposure-named PA amplification; directly benefits NET.PA.1/PA.2/PA.3 |
| STD.CA.11 Tort Interference | Cross (Mandate + own-native E) — Mandate spending path if Mandate acquired through trade |

**STD floor vs. NET ceiling:**
- *Reveal*: STD has no faction-specific Reveal covert ops. CA.1/CA.3/PA.1/PA.3 all exceed STD scope by faction-specific subject, timing, and effect depth.
- *Presence*: STD.CA.3 + STD.CA.8 are the expansion floor. NET.PA.2 Community Rally (up to 3 simultaneous presence tokens in Established+ districts) is the ceiling.
- *PA interference*: STD.CA.6 Broadcast Interference (one district, +1 PA cost) is the floor. NET.CA.4 Network Cascade (adjacent district extension, requires STD.CA.6 combo) is the ceiling.

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

## Section B — Network Set Analysis

### B1. Coverage Map

| Card | Layer | Function | Subject | Beat | Cost type | IR |
|------|-------|----------|---------|------|-----------|----|
| NET.CA.1 Leak | Information | Reveal | District | 3 | cross | Open |
| NET.CA.2 Disclosure Loop | Economy | Add | Exposure | 3 | cross | Open |
| NET.CA.3 Breaking News | Information | Reveal | CovertOperation | 2 | mono | ✓ S89 |
| NET.CA.4 Network Cascade | Submission | Modify | PublicAct | 2 | mono | Open |
| NET.CA.5 Community Anchor | Territory | Add | PresenceToken | 3 | mono | Open |
| NET.CA.6 Sacrifice | Economy | Add | IntelToken | 3 | free | ✓ |
| NET.CA.7 Ground Signal | Standing | Shift | PublicStanding | 3 | mono | Open |
| NET.MOD.1 Signal Break | (Territory\|Add\|PresenceToken) | — | — | B4 React | mono | Pending 04-n4 |
| NET.MOD.2 Reputational Strike | (stub) | — | — | B4 React | free+Intel | Stub |
| NET.PA.1 Public Disclosure | Information | Reveal | ActionAttribution | 4 | mono+Intel×n | Open |
| NET.PA.2 Community Rally | Territory | Add | PresenceToken | 4 | variable | ✓ |
| NET.PA.3 Live Coverage | Information | Reveal | FactionHand | 4 | mono | ✓ S89 |

**Resolved: 4 of 12** (CA.3, CA.6, PA.2, PA.3). MOD.1 and MOD.2 pending 04-n4 schema.

### B2. Layer Coverage Summary

Information dominant (4 of 12, all Reveal) — the highest Reveal concentration of any faction. Territory secondary (CA.5, MOD.1, PA.2). Economy (CA.2, CA.6) and Submission (CA.4) moderate. Standing gap filled by CA.7 (S106). No Resolution cards — consistent with Network doctrine: the Network affects the conditions under which resolution happens, not the resolution mechanic itself.

No Remove, Block, or Move cards in the faction set. Network's disruption is entirely information-based (CA.1 cancels, CA.3/PA.1/PA.3 reveal, CA.4 raises PA costs). If presence is removed from Network districts, the faction-specific recovery path is zero — STD.CA.4 Undermine at cross cost is the only tool, and it removes opponent chips rather than recovers Network's.

### B3. Beat Timing Distribution

| Beat | Cards | Notes |
|------|-------|-------|
| Beat 2 | CA.3 · CA.4 | Both covert; CA.3 = d100, CA.4 = Automatic; both fire before Beat 3 resolution |
| Beat 3 | CA.1 · CA.2 · CA.5 · CA.6 · CA.7 | Core operative package |
| Beat 4 | PA.1 · PA.2 · PA.3 | Full PA-layer commitment |
| Beat 4 React | MOD.1 · MOD.2 | React modifiers on PA board state changes |

Beat 2 cards (CA.3 Breaking News + CA.4 Network Cascade) create a distinctive initiative-first pattern: Network shapes the information state before any Beat 3 operations resolve. CA.3 reveals target ops before they fire; CA.4 extends PA cost-raise to an adjacent district. Both fire blind against Beat 3 outcomes — high information advantage potential, genuine fizzle risk on empty queues or wrong district targeting.

### B4. Doctrinal Assessment

**Information engine:** The 4-Reveal architecture (CA.1/CA.3/PA.1/PA.3) covers every major disclosure mode in the game: pre-execution cancel (CA.1), pre-resolution reveal (CA.3), post-resolution attribution (PA.1), sustained hand-visibility obligation (PA.3). This is the most comprehensive information toolkit in the game. Ghost generates intelligence privately for asymmetric use; Network broadcasts publicly for accountability.

**Disclosure Loop mechanics:** CA.2 Disclosure Loop creates a self-reinforcing feedback path: reveal activity generates Exposure for more reveals. The loop is intentionally contingent — CA.2 is dead weight without active reveals in the same round, enforcing that Network's Exposure economy is doctrine-conditional, not passive income. This distinguishes Network's income from Ghost's (fieldwork-based), Directorate's (Permanent-scaling), and Guild's (wager-based).

**Intel circuit:** CA.6 Sacrifice converts PS to Intel (PS−2 → IntelToken×1 as a success effect). NET.PA.1 Public Disclosure consumes all held Intel for scaling PS damage. The PS→Intel→PS-damage pipeline is Network's highest-expression play sequence: it requires accumulated PS overhead to spend and accumulated Intel tokens to deploy. The pipeline is doctrinally correct ("standing is a means, not an end") but creates resource tension between PS accumulation for win path and PS expenditure for Intel generation.

**Presence model:** Network's territorial toolkit is restriction-heavy by design. CA.5 Community Anchor targets Baryo + zero-presence only (initial entry, not reinforcement). MOD.1 Signal Break fires opportunistically on PA board changes (no control over timing). PA.2 Community Rally consolidates Established+ only (deepens, doesn't expand). All three are conditional. General new-territory expansion depends entirely on STD.CA.3 and STD.CA.8.

**Win path support (FLAG 5 assessment):** Faction-specific toolkit supports consolidation and opportunistic insertion; it does not support systematic new-territory expansion. The doctrinally correct reading is that Network's broadcast reach means it can establish anywhere STD cards allow — the faction-specific kit then deepens and defends. Whether this is sufficient for a competitive wide-presence win path is a playtest question.

### §6.4 Economic Integration Audit (5-Check Framework)

1. **Generation check:** CA.2 Disclosure Loop conditionally generates +1 Exposure (native) — only fires when a Reveal card resolved this round. CA.6 Sacrifice generates IntelToken×1 as a success effect (PS is non-fungible; this is not generation in the standard Exposure sense). No non-native resource generation in the faction set — no card delivers Mandate, Capital, Capacity, or Findings to Network as an output effect. **Generation verdict: ✓** — native Exposure generation via loop mechanic; Intel via credibility sacrifice; no problematic non-native generation.

2. **Spending check:** Exposure spending paths are saturated — 9 of 12 cards include Exposure in cost (CA.1, CA.3, CA.4, CA.5, CA.7, MOD.1, PA.1, PA.2, PA.3). STD cross cards at Exposure-named (STD.CA.6 Broadcast Interference, STD.CA.7 Amplify) add further paths. Intel token spending: PA.1 (spends all held, scaling effect) and MOD.2 (Intel×1 as activation cost). Findings spending: CA.1 (F×1) and CA.2 (F×1) — if Findings are acquired through Ghost trade or district yield, the spending destinations are these two cards. No STD cross card is denominated in Findings; Findings spends in CA.1/CA.2 only. **Spending verdict: ✓** — Exposure saturated; Intel has two dedicated paths; Findings loops through CA.1/CA.2 (self-referential but architecturally coherent).

3. **Floor calibration:** CA.5 (E×1, Automatic, Baryo-restricted): floor-tier. CA.7 (E×1, d100 threshold 50): floor-tier, fills Standing|Shift gap. CA.2 (F×1, conditional): floor power at cross cost — structurally atypical (cross cost normally implies ceiling power; here it's floor); the cross cost on a floor card reflects genuine design intent (Findings is costly to acquire). CA.3 (E×2, d100 threshold 50): floor-to-mid (pre-resolution reveal). CA.4 (E×2, Automatic): mid-tier with combo requirement (effective total cost E×3+ with STD.CA.6). CA.1 (cross E×1+F×1, Automatic): ceiling-adjacent — cancels costliest target op + public reveal. PA.3 (E×2, d100 threshold 50): **Seasonal hand-visibility or covert-ops-disabled** — persistent, high-leverage effect at moderate mono cost. ✗ Borderline inversion.

4. **Ceiling coverage:** CA.1 Leak is the cross ceiling card — cross cost at ceiling-adjacent power (cancel + reveal). §9.2 architecture is present and correctly structured: the highest-power faction card carries the cross cost. PA.3 (Seasonal persistence, mono E×2) is the borderline inversion — significant sustained effect with no cross commitment. PA.1's Intel-scaling provides proportional cost gating. **Ceiling verdict: ✓ (with note)** — cross ceiling exists in CA.1; PA.3 is the one borderline inversion.

5. **Gap verdict:** No unspendable resources. §9.2 cross architecture present — Network is the only faction with an operational cross-ceiling card. Structural constraint: Findings-gated ceiling means Ghost-dependent architecture; in Ghost-absent games, Network's cross ceiling degrades to mono. PA.3 borderline inversion at mono E×2. Modifier card schema (04-n4) pending for MOD.1/MOD.2. **New PM05 item: 04-n126** (Findings-gated ceiling + PA.3 borderline — address in cross-faction §9.2 pass alongside 04-n118/119/123).

---

## Section C — §5a Alignment

### C1. Doctrine Statement

Network §5a doctrine (Art 04b §8.3): Broadcaster. Transparency as operational doctrine — information is released, not hoarded. Win path through wide presence (Established in more districts than any faction) built on community relationships, not conquest. Deck feel: vocal, distributed, difficult to contain.

### C2. What's Landing

**Broadcaster:** ✓ — 4 Reveal cards across every disclosure mode: pre-execution cancel (CA.1), pre-resolution announce (CA.3), post-resolution attribution (PA.1), sustained visibility obligation (PA.3). No faction approaches this Reveal density.

**Transparency doctrine:** ✓ — All 4 Reveal effects are public (table-broadcast). CA.3 announces to all players; PA.1 releases attribution publicly; PA.3 forces open hand or disables covert ops. Ghost's information is private (IS-xx to one faction); Network's is broadcast to everyone.

**Community relationships:** ✓ — CA.5 Community Anchor (established community contacts → initial presence entry), PA.2 Community Rally (existing foothold → deepened presence), CA.7 Ground Signal (existing presence made legible via distributed street signal). The territorial toolkit is relationship-based, not construction-based (Guild) or coercive (Syndicate).

**Credibility as capital:** ✓ — CA.6 Sacrifice encodes the doctrine that PS is a means, not an end. CA.7's IL ≤ Established restriction reflects that at Dominant, the signal is already established — outreach adds nothing. Both ground game cards model Network's relationship to standing as strategic, not terminal.

### C3. Where It's Thin

**Win path expansion gap (FLAG 5):** §5a implies a wide-presence faction. Faction-specific territorial toolkit only supports initial entry (CA.5 — Baryo + zero-presence restriction), opportunistic insertion (MOD.1 — React on PA board change), and consolidation (PA.2 — Established+ only). No unrestricted expansion card. Network's win path depends structurally on STD.CA.3 + STD.CA.8 for general expansion — doctrinally acceptable (Network reaches everywhere through community), but the faction-specific signature of "distributed reach" is architecturally thin in the CA/PA set.

**Modifier deck (unbuilt):** Network's design notes (Art 04 §11.8) describe the modifier deck as the "true engine" — React and instant modifier cards that make Network louder each Quarter without individual cards growing stronger. Only two modifier cards currently exist: MOD.1 (design complete, schema pending) and MOD.2 (stub). The modifier deck as a structural element is essentially unbuilt at L1. This is the largest gap between §5a architectural intent and L1 implementation for Network.

**Territorial response gap:** No faction-specific counter to presence removal. If another faction removes Network chips, the recovery path is STD-only. The §5a implication of distributed resilience ("difficult to contain") has no mechanical backing at the CA/PA level.

### C4. §5a Verdict

Core Broadcaster doctrine is well-served: 4-Reveal suite covers every disclosure mode; community-relationship territorial model is coherent and distinctive; credibility-as-capital doctrine expressed mechanically. Win path is STD-dependent for expansion — acceptable if doctrinal, but worth flagging. Modifier deck is the largest §5a gap: the "deck grows louder each Quarter" architecture has minimal L1 implementation. Flag for 04-n110 cross-faction §5a alignment pass.

---

## Section D — Cross-Faction Differentiation

### NET vs. STD

CA.4 Network Cascade is mechanically dependent on STD.CA.6 Broadcast Interference (restriction: STD.CA.6 submitted same round). This is the tightest explicit STD→faction dependency in the game — a mechanical prerequisite, not just a thematic tie. CA.1 Leak fires within the Beat 3 initiative queue and benefits from going first (before target ops resolve). Network's core information ops (CA.1, CA.3) operate on STD's action structure itself: the target's submitted STD ops are Breaking News and Leak's payload.

No taxonomy overlap between Network faction-specific cards and STD faction-specific cards. ✓

### NET vs. GHO

Opposite disclosure postures. Ghost generates private intelligence for asymmetric use (IS-xx delivers to one faction; information is Ghost's weapon). Network broadcasts publicly as accountability (CA.3, PA.1, PA.3 all announce to the full table; information is Network's doctrine). Both are information-dominant factions — but Ghost concentrates information; Network distributes it.

Cross-resource dependency (FLAG 2): CA.1 Leak and CA.2 Disclosure Loop both cost Findings (Ghost's native). Network's ceiling architecture is directly denominated in Ghost's resource. When Ghost and Network are both active, Ghost becomes a structural input to Network's highest-power ops — through trade or cooperation. Ghost's private intelligence and Network's public broadcast are architecturally complementary: Ghost gathers what Network releases.

Intel economy distinction: Ghost generates Intel through fieldwork for intelligence capital. Network generates Intel by spending credibility (CA.6 PS−2 → Intel×1) and spends all held Intel in a single public broadcast (PA.1). Ghost's Intel is strategic; Network's Intel is a one-shot broadcast payload.

### NET vs. DIR

Broadcast accountability vs. institutional authority. Network discloses what is happening (CA.3 pre-reveals ops, PA.3 forces hand-open or covert-disabled). Directorate controls what is permitted to happen (CA.1 blocks named card types, PA.3 Entry/Exit Controls blocks deployment, PA.6 Standing Injunction blocks PA taxonomy). Both constrain opponents' action space — through opposite mechanisms.

Scope interaction: DIR.CA.1 Invoke Jurisdiction design question (C1 in DIR audit) includes whether it can block Reveal-type operations. If yes: DIR can suppress NET.CA.1/CA.3 in a named district, directly constraining Network's core disclosure toolkit.

NET.PA.3 Live Coverage targeting Directorate: forces DIR hand-open or covert-ops-disabled per Phase A for the remaining Months of the Quarter. If Directorate resists, its entire Beat 3 covert action slot is voided each Month — all CA.1/CA.2/CA.3/CA.4/CA.5 suppressed. Network's most leveraged single-card pressure against Directorate.

PA cost interference: NET.CA.4 + STD.CA.6 raises PA costs in up to two adjacent districts. DIR runs 3 Permanent PAs (PA.1, PA.3, PA.6) — if Network deploys PA cost-raise in districts where DIR needs to maintain Permanents, the renewal cost increases. Sustained PA cost pressure is Network's indirect institutional-cost tool against DIR's Permanent-footprint strategy.

### NET vs. GUI

NET.CA.4 + STD.CA.6 raises PA costs in districts — this can affect GUI.PA.1 Civic Works Mandate (C×4 + district-native) if deployed in Guild target districts, but Guild's wager income (CA.2/CA.6) triggers on STD.CA.1/CA.2 board state changes, not on PAs — the PA cost raise does not suppress Guild's wager circuit.

MOD.1 Signal Break fires on any PA board state change (influence chip or structure placed or removed). This includes GUI.PA.1 building structures: when Guild builds with PA.1, Network can React to place a chip in the same district. Guild's build events become Network insertion windows — the faction that builds enables the faction that broadcasts.

No resource competition (Exposure vs. Capacity). Guild has zero Information cards — no covert interaction. Network cannot target Guild for Live Coverage without it being fully covert-disabled (Guild has no covert operations to suppress with the resist option; the resist penalty is dead for Guild. Live Coverage against Guild forces open hand only — the disable branch is toothless).

### NET vs. SYN

Intel token intersection. Syndicate generates Intel contingently (CA.6 Parasitic — conditional) and consumes Intel for territorial leverage (CA.7 Corporate Blackmail, CA.9 Hostile Takeover). Network generates Intel by spending credibility (CA.6 Sacrifice — PS−2 → Intel×1) and consumes all held Intel in a single public broadcast (PA.1 Public Disclosure). Different Intel economies: SYN uses Intel as targeted coercion; NET uses Intel as broadcast payload.

SYN.PA.3 Data Acquisition reveals Intel holdings in a named faction's Dispatch Case — a direct counter to NET.CA.6 Sacrifice accumulation. If Syndicate reads Network's Intel payload before PA.1 fires, it learns the broadcast size and can calibrate accordingly. Data Acquisition is Syndicate's intelligence read on Network's threat level.

NET.PA.3 Live Coverage targeting Syndicate: forces SYN hand-open or covert-ops-disabled per Phase A. Syndicate's entire covert manipulation suite (CA.3/CA.7/CA.8/CA.9 are all covert) is suppressed if Syndicate resists. Network can selectively ground SYN's territorial acquisition plays by maintaining Live Coverage — the most targeted single-card disruption available to Network against Syndicate.

### Faction Cross-Reference (5-faction synthesis, complete)

| Faction | Native resource | Income model | Territory posture | §9.2 ceiling gap | Information posture |
|---------|----------------|-------------|------------------|-----------------|---------------------|
| Ghost | Findings | Intel-activity yield (CA.5/CA.7/CA.8) | None — zero territory cards | Not flagged | Dominant private — IS-xx to one faction |
| Directorate | Mandate | Institutional yield (CA.6 Audit, Permanent-scaled) | Suppression — clears space; builds through STD | ✗ 04-n118 — 11/12 mono | External — requires STD PA setup (PA.2 Convene) |
| Guild | Capacity | Wager/passive (CA.2/CA.5/CA.6 on STD triggers) | Construction — Add/Protect; permanence through building | ✗ 04-n119 — zero cross | None — zero Information cards |
| Syndicate | Capital | Extraction/coercion (CA.1 unilateral, CA.7 coercive) | Acquisition — seize/replace (CA.3/CA.8/CA.9/PA.1) | ✗ 04-n123 — zero cross | Transactional — Intel as cost input (CA.7, CA.9) |
| Network | Exposure | Loop/sacrifice (CA.2 Disclosure Loop; CA.6 PS→Intel) | Broadcast reach — restricted expansion (CA.5 Baryo); consolidation (PA.2); opportunistic (MOD.1) | ⚠ 04-n126 — cross exists but Findings-gated | Dominant public — 4 Reveal cards; all table-broadcast |

DIR/GUI/SYN share zero-cross-ceiling architecture — systemic across mono-economy factions. Network is the exception: cross architecture exists in CA.1 (cross ceiling) and CA.2 (cross floor), but both are denominated in Ghost's native resource (Findings). Ghost and Network are the two information-dominant factions with opposite disclosure models: Ghost concentrates; Network distributes. Network completes the 5-faction synthesis; Network (Exposure) joins Ghost (Findings) as the two factions that are NOT Capital-class and NOT flagged for zero-cross-ceiling architecture.

---

## Section E — §9.2 Floor/Ceiling Mapping

| Card | Cost | DB cost_type | Effect tier | §9.2 status |
|------|------|-------------|-------------|-------------|
| NET.CA.1 Leak | E×1 + F×1 | cross | Ceiling — cancel + public reveal of costliest op | ✓ cross ceiling |
| NET.CA.2 Disclosure Loop | F×1 | cross | Floor — conditional +1 Exposure | ✓ (cross at floor; structurally unusual but intentional) |
| NET.CA.3 Breaking News | E×2 | mono | Floor-to-mid — pre-resolution announce; crit = full queue | ✓ |
| NET.CA.4 Network Cascade | E×2 | mono | Mid — PA cost extension; combo requires E×3+ total | ✓ (combo requirement mitigates) |
| NET.CA.5 Community Anchor | E×1 | mono | Floor — 1 presence, Baryo+zero-presence restricted | ✓ |
| NET.CA.6 Sacrifice | free + PS−2 | free | Mid — 1 Intel token; PS track is real gate | ✓ |
| NET.CA.7 Ground Signal | E×1 | mono | Floor — +1 PS; crit chip+PS; IL≤Established restriction | ✓ |
| NET.MOD.1 Signal Break | E×1 | mono | Mid — opportunistic chip placement on PA trigger | ✓ (React timing restriction limits use) |
| NET.MOD.2 Reputational Strike | Intel×1 | free+Intel | Mid — unblockable PS−1 (stub; trigger TBD) | ⚠ stub — governing rule for unblockability pending |
| NET.PA.1 Public Disclosure | E×2 + Intel×n | mono+Intel | Ceiling — scaling PS damage proportional to payload | ✓ (Intel scarcity gates access to ceiling effect) |
| NET.PA.2 Community Rally | E×2–4 | variable | Mid-to-ceiling at E×4 (3 districts) | ✓ (scaling cost matches scaling effect) |
| NET.PA.3 Live Coverage | E×2 | mono | **Ceiling-borderline** — Seasonal covert-disable or hand-open obligation | ✗ borderline inversion |

**Summary:** 1 clear cross ceiling (CA.1). 1 borderline mono inversion (PA.3 — Seasonal persistent effect at mono E×2). Network is the only faction with an operational cross-ceiling card. PA.3 parallels DIR.PA.6 Standing Injunction (similar cost tier, faction-wide Seasonal effect) — if PA.6 was not individually flagged for DIR, PA.3 may be acceptable within the overall §9.2 balance. Tracked as part of 04-n126 for cross-faction §9.2 pass.

---

## Section F — Outstanding Issues Inventory

| Card | IR status | Blocking dependency |
|------|-----------|-------------------|
| CA.1 | Open | ps_framing on target (04-n33/04-n34b pending); initiative-order guarantee for fizzle |
| CA.2 | Open | Conditional cost resolution (Findings cost consumed on no-reveal? confirm); portrait = {} confirmation |
| CA.3 | ✓ S89 | — |
| CA.4 | Open | STD.CA.6 dependency at Dispatch (ordering); target_district derivation from CA.6 target; void-on-CA.6-cancel behavior |
| CA.5 | Open | Baryo zone definition in Art 01; expansion-restriction design confirmation |
| CA.6 | ✓ | — |
| CA.7 | Open | DB registration (id=TBD); IL enum confirmation (InfluenceLevel.Established) |
| MOD.1 | Pending 04-n4 | Modifier card schema pass; DB registration (id=TBD) |
| MOD.2 | Stub | 04-n4 schema; trigger TBD; unblockability governing rule; card name/ID |
| PA.1 | Open | Data schema validation pending 04-n70 sweep |
| PA.2 | ✓ | — |
| PA.3 | ✓ S89 | FactionHand subject (non-gate — taxonomy validation only) |

**Resolved: 4 of 12** (CA.3, CA.6, PA.2, PA.3). Same density as Syndicate.

Dominant bottlenecks:
1. 04-n4 modifier card schema — gates MOD.1 sign-off; gates MOD.2 existence as a real card.
2. ps_framing (04-n33/04-n34b) — gates CA.1.
3. STD.CA.6 dependency resolution — gates CA.4.
4. Baryo zone definition (Art 01) — gates CA.5.
5. DB registration — NET.CA.7 and NET.MOD.1 both id=TBD; id assignment required before Issues Resolved.

---

## Section G — Audit Findings and PM05 Items

### G1. Key Findings

1. **Network is the cross-architecture exception.** CA.1 Leak (cross: E×1+F×1) is the only faction-specific cross-ceiling card across all 5 factions. DIR/GUI/SYN all show zero cross-ceiling architecture. Network's §9.2 compliance is structurally sound — but it requires Ghost cooperation to achieve. The Findings dependency is the central structural design question for the faction.

2. **4 Reveal cards: dominant public information suite.** CA.1/CA.3/PA.1/PA.3 cover pre-execution, pre-resolution, post-resolution, and sustained disclosure. Ghost has the deepest private intelligence suite; Network has the deepest public disclosure suite. These are complementary architectures, not competing ones.

3. **Modifier deck is the §5a gap.** The "deck grows louder each Quarter" architecture has only 2 cards at L1: MOD.1 (design complete, schema pending 04-n4) and MOD.2 (stub). This is Network's primary L1 gap relative to §5a.

4. **Win path depends on STD for expansion.** No unrestricted presence-placement faction card. The faction-specific wide-presence signature is architecturally underdeveloped in the CA/PA set. Whether this is doctrinal ("reach via community") or a gap is a design decision for 04-n110.

5. **PA.3 Live Coverage is Network's highest-leverage single card.** Seasonal hand-visibility or covert-ops-disabled at E×2, threshold 50. Can neutralize Syndicate's entire covert suite or Directorate's covert slot for Months at a time. Borderline §9.2 inversion at mono cost.

6. **Live Coverage vs. Guild is weakened.** Guild has zero covert operations; the "resist" branch of PA.3 (forfeit covert submissions) has no effect on Guild's play. Live Coverage against Guild is hand-open only — one of the two branches is wasted.

7. **§8.3 Art 04b is significantly stale.** S104 data lists 7 cards; current set has 12. Five cards missing. Update required alongside this audit (Section G3).

### G2. PM05 Items

| Item | Description | Priority |
|------|-------------|---------|
| **04-n90 ✅** | STD+NET combined set audit complete (S123) | — |
| **04-n126 (new)** | NET §9.2 cross architecture — Findings-gated ceiling. CA.1 is Network's cross ceiling card (cross: E×1+F×1 — the only cross-ceiling card in the 5-faction set). Findings requirement creates Ghost-dependency: in Ghost-absent games or no-trade scenarios, CA.1/CA.2 cannot fire regardless of Exposure supply. PA.3 Live Coverage is borderline §9.2 inversion — Seasonal covert-disabled or hand-open at mono E×2. Address in cross-faction §9.2 pass alongside 04-n118/119/123. Output of 04-n90 (S123). | Design note — 04-n110 gate |
| **00a-78 update** | Mark STD+NET complete S123 (§6.4 Art 04b). All 5 faction natives have Exposure spending destinations. NET cross architecture present (CA.1, CA.2) — distinct from DIR/GUI/SYN zero-cross pattern. Findings dependency flagged → 04-n126. | Tracking |

### G3. Art 04b Updates Required

**§6.4** — Add STD+NET 5-check results as a new subsection after STD+SYN.

**§8.3 Network section** — Full enumeration update from S104 (7 cards) to S123 (12 cards):
- Add NET.CA.7 Ground Signal (S106), NET.MOD.1 Signal Break (S106), NET.MOD.2 Reputational Strike (stub), NET.PA.1 Public Disclosure, NET.PA.2 Community Rally
- Update design targets: Standing|Shift gap ✓ filled (CA.7); Reveal differentiation note (4 cards, subjects: District/CovertOperation/ActionAttribution/FactionHand); modifier deck gap (MOD.1 complete schema pending, MOD.2 stub — 04-n4 the gate)
- Add cross-ceiling architecture note: CA.1 is the only faction-specific cross-ceiling card in the 5-faction set; Findings-gated (04-n126)

**Cross-faction synthesis table** — Update in GHO, DIR, GUI, SYN audit files: replace "4-faction synthesis, NET pending" with the complete 5-faction table from Section D of this file.

**Version bump** — Art 04b v2.5 → v2.6. Update session header to S123.

---

*Audit complete S123 (04-n90 ✅). Art 04b updates: Section G3. PM05: 04-n126 new, 00a-78 update, 04-n90 ✅.*
