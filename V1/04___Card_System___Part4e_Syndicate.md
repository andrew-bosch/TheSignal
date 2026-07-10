## Syndicate
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#syndicate-covert-operations) · [Public Acts](#syndicate-public-acts)

---

### Syndicate — Covert Operations
[↑ Syndicate](#syndicate)

| Card | Name |
|------|------|
| [SYN.CA.1](#c31-leveraged-acquisition) | Leveraged Acquisition |
| [SYN.CA.2](#c32-short-the-market) | Short the Market |
| [SYN.CA.3](#c33-hostile-acquisition) | Hostile Acquisition |
| [SYN.CA.4](#c34-golden-parachute) | Golden Parachute |
| [SYN.CA.5](#c35-regulatory-capture) | Regulatory Capture |
| [—](#syndicate-land-title) | Land Title |
| [SYN.CA.9](#syndicate-hostile-takeover) | Hostile Takeover |
| [SYN.CA.10](#syn-ca-10--accord-transfer) | Accord Transfer |
| [—](#syndicate-parasitic) | Parasitic |
| [—](#syndicate-corporate-blackmail) | Corporate Blackmail |
| [SYN.CA.11](#syn-ca-11--redline) | Redline |

### SYN.CA.1 — LEVERAGED ACQUISITION
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's non-presence resource extraction card — Capital buys immediate resource extraction from any district without Syndicate being physically present. Establishes the doctrine that ownership and presence are separate things. Distinguished from Land Title (extended set) by duration: SYN.CA.1 is a per-round transactional play; Land Title creates a permanent revenue claim. Core cost is the action slot itself; the 2:1 Capital:native conversion is a secondary trade rate, not the primary barrier.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Non-presence resource extraction — Capital buys revenue stream from any district; implements "ownership ≠ presence" doctrine; distinct from Land Title (permanent) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×2; no per-round limit; core cost = action slot; affinity boost directed (condition TBD — see Outstanding Issues) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — non-presence extraction is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — deferred upkeep delivery accepted | Art 04b §4, §5 |
| Balance | ✓ | Capital×2 for 1 district native resource at Beat 3 resolution; core cost = action slot. No per-round limit. Boost on affinity TBD. | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: native resource of target district delivered at Beat 3 resolution. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; non-presence extraction aligns with capital intelligence doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource cost + delivery; Immediate at Beat 3; no new component required. | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; Immediate delivery at resolution; no deferred procedure required. | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`ps_framing` (has `doctrine_mod`, `boost`). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Capital only). Uses the `boost` field correctly for its variable-yield mechanic (`boost = True: resource.faction(acting).capital * 2`) — good contrast case against GHO.CA.8's bare-`n` bug (schema_cleanup_log.md #28). | Art 00a §9.2 |

#### Outstanding Issues

- **Schema violations in SYN.CA.7/DIR.CA.5:** `affinity=Syndicate` / `affinity=Directorate` corrected to `affinity=None` — 04-n70 fix pass.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

*v1.4 — S71: boost field added (True: capital×2); affinity=None confirmed; Issues Resolved ✓.*

```python
SYN.CA.1 = Card(
    id      = "SYN.CA.1",  version = "v1.4",
    name    = "Leveraged Acquisition",
    tagline = "Extract resource income from a district without physical presence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,

    layer   = Economy,  function = Add,  subject = NativeResource,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = None,  # scaffolded, not addressed
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).capital * 2,
    boost       = True: resource.faction(acting).capital * 2,
    # submit 2 Capital → 1 native; submit 4 Capital → 2 native; submit 6 Capital → 3 native
    # ARBITER counts n = (submitted − 2) / 2 at Beat 0; success fires (1 + n) times

    success     = game.grant(faction(acting), district(target).resource.native * 1),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Syndicate: PortraitEntry(submitter=+1)},

    narrative    = "The Syndicate does not need to be somewhere to profit from it. Ownership and presence are different things.",
    perspectives = {Syndicate: "We own the revenue stream. Whether we are physically present is irrelevant."},
    design_note  = "Immediate delivery at Beat 3 resolution. Core cost = action slot; 2:1 Capital:native is the unit rate. Boost: player submits multiples of 2 Capital; each unit yields 1 additional native. No declaration required.",
    arbiter_note = "Beat 0: if extra Capital submitted beyond 2, calculate n = (total − 2) / 2; must be whole number or reject. Beat 3: grant Syndicate (1 + n) units of target district's native resource.",
)
```

---

### SYN.CA.2 — SHORT THE MARKET
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's economic disruption card — directly reduces a target faction's native resource supply, impeding their ability to fund actions next round. The "short" framing reflects a deliberate market interference: Syndicate bets against a competitor's economic health and profits from their reduced capacity. Intel restriction (fresh token) requires prior intelligence, creating a two-step play: gather first, short second. Applied silently (no public announcement) reflects the covert nature of market manipulation. Crit success doubles the reduction (−2 native). Failcrit PS −1 represents the institutional embarrassment of a failed financial maneuver.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Economic disruption — direct native resource reduction; "short" framing aligns with Syndicate market interference doctrine; Intel restriction enforces prior intelligence requirement | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×2; Intel restriction creates STD.CA.5→SYN.CA.2 two-step; "applied silently" protocol outstanding (Outstanding Issue); 04-n14 redesign flag | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — covert market interference is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Remove/NativeResource — direct supply reduction | Art 04b §4, §5 |
| Balance | ✓ | Capital×2, threshold 50; Intel prereq adds secondary cost; "applied silently" and floor confirmation outstanding (Outstanding Issues) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: native resource reduced at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; failcrit PS −1 is game effect (not portrait), per DIR.PA.2 | Art 04 §6.2; Art 02 §11 |
| Supported by zones | ✓ | target_district = None — faction-targeted, not district-targeted | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken restriction; NativeResource target; "applied silently" protocol outstanding (Outstanding Issue) | Art 02 §6–§8; Art 02 §11 |
| Supported by game procedure | ✓ | Beat 3 d100; Intel check at Dispatch; silent application and floor outstanding (Outstanding Issues) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing` entirely — see schema_cleanup_log.md #24. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/successcrit/failcrit populated (fail=None), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Capital only, typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **"Applied silently" protocol:** SYN.CA.2 reduces native resource "silently" — the table does not see the effect. Confirm: does ARBITER privately notify the target, or is the loss simply applied to their resource pool with no notification? Distinction matters for game integrity.
- **Floor at minimum 0:** `success = faction(target).resource.native -= 1 # minimum 0` — confirm ARBITER applies a floor of 0 and any excess is simply absorbed without penalty.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
SYN.CA.2 = Card(
    id      = "SYN.CA.2",  version="v1.0",
    name    = "Short the Market",
    tagline = "Reduce a faction's native resource generation for one round.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Remove,  subject = NativeResource,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10},
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction(named_opponent), target_object=NativeResource,
    target_taxonomy=None,
    affinity=None,
    restriction = intel(faction=faction(target), age_rounds<=1) >= 1,
    cost        = resource.faction(acting).capital * 2,
    success     = faction(target).resource.native -= 1,  # minimum 0; applied silently
    successcrit = faction(target).resource.native -= 2,  # minimum 0
    fail=None,
    failcrit    = faction(acting).standing -= 1,
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},
    narrative   = "Capital can suppress as easily as it can produce.",
    perspectives = {Syndicate: "We are not destroying their capacity. We are adjusting market conditions temporarily."},
    design_note  = None,
    arbiter_note = None,
    value_rating = None,  # scaffolded, not addressed
)
```

---

### SYN.CA.3 — HOSTILE ACQUISITION
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's structure takeover card — Capital purchases ownership of an opponent's structure block, transferring it to Syndicate along with the district's native resource compensation to the dispossessed faction. The most expensive Syndicate base card at Capital×5, reflecting that acquiring built infrastructure is a major transaction. The "fair offer" framing in the narrative — Syndicate pays, target receives a resource — positions this as market-legal rather than theft. Guild Protection (GUI.CA.1 active in district) creates a doctrinal carve-out: when Guild has actively asserted its structural permanence in the district, Syndicate cannot override it this round. Successcrit returns Capital×1 (financial efficiency on the acquisition). Failcrit PS −1: a publicly failed acquisition damages Syndicate's financial reputation.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Structure takeover — Capital purchases ownership with compensation; "fair offer" framing positions this as market-legal; Guild Protection carve-out for doctrinal symmetry | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×5 highest base cost; compensation to target; GUI.CA.1 Guild Protection interaction outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — structure ownership purchase is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Redirect/StructureBlock — ownership transfer | Art 04b §4, §5 |
| Balance | ⚠ | Design Rationale states "Capital×5" (the most expensive Syndicate base card); the code's actual `cost = capital*3 + findings*1 + exposure*1` totals 5 resource units but only 3 are Capital specifically — cross-resource, not pure Capital×5. **Flagged S141:** same prose/code cost mismatch pattern as NET.CA.4 (schema_cleanup_log.md #31), not resolved here. Compensation mechanics and GUI.CA.1 interaction outstanding (Outstanding Issues). | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent: structure ownership transferred; compensation delivered once at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; failcrit PS −1 is game effect (not portrait), per DIR.PA.2 | Art 04 §6.2; Art 02 §11 |
| Supported by zones | ✓ | target_district = district.any — presence-free acquisition | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock transfer; NativeResource compensation; GUI.CA.1 interaction outstanding (Outstanding Issue) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 d100; ARBITER re-assigns structure ownership; GUI.CA.1 active-state visibility outstanding (Outstanding Issue) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing` entirely — see schema_cleanup_log.md #24. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/successcrit/failcrit populated (fail=None), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Cross-resource (Capital + Findings + Exposure — three distinct types, all typed correctly). See Balance row above for the "Capital×5" prose mismatch. | Art 00a §9.2 |

#### Outstanding Issues

- **C11 Guild Protection interaction:** Restriction excludes acquisition when `C11.active(district(target), round=game.round)` — confirm C11's "active" state is visible to ARBITER at Beat 3 and that this interaction is symmetrical (C11 blocks C33, but C33 does not block C11 playback in same round). *(C11 = GUI.CA.1 Fortify Structure's legacy sequential-number reference — same low-priority notation category as GUI.CA.2's `id=STD.CA.2` and NET.CA.4's `C06`.)*
- **Compensation mechanics:** `game.dispatch(faction(target), resource.faction(target).native * 1)` delivers 1 native to the dispossessed faction. Confirm this is the target faction's native resource type (not Syndicate's), and that the delivery is immediate.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
SYN.CA.3 = Card(
    id      = "SYN.CA.3",  version="v1.0",
    name    = "Hostile Acquisition",
    tagline = "Purchase ownership of an opponent's structure.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Redirect,  subject = StructureBlock,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10},
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any, target_faction=faction(named_opponent), target_object=StructureBlock,
    target_taxonomy=None,
    affinity=None,
    restriction = (
        district(target).faction(target).structure >= 1
        AND NOT (faction(target) == Guild AND C11.active(district(target), round=game.round))
    ),
    cost        = resource.faction(acting).capital * 3 + resource.faction(acting).findings * 1 + resource.faction(acting).exposure * 1,
    success     = (
        game.transfer(district(target).faction(target).structure(1), faction(acting)),
        game.dispatch(faction(target), resource.faction(target).native * 1),
    ),
    successcrit = resource.faction(acting).capital += 1,
    fail=None,
    failcrit    = faction(acting).standing -= 1,
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},
    narrative   = "Everything in New Meridian has a price. The Syndicate is the only faction honest about this.",
    perspectives = {Syndicate: "We made a fair offer. The market determined the value. We accepted the market's judgment."},
    design_note  = None,
    arbiter_note = None,
    value_rating = None,  # scaffolded, not addressed
)
```

---

### SYN.CA.4 — GOLDEN PARACHUTE
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's bribe card — pays a named faction to nullify their Beat 3 operations against Syndicate. Capital is declared at Dispatch, validated at Beat 0 (retained with card, not drained to Reservoir), and distributed at Beat 2 across the target faction's Beat 3 ops that target Syndicate in submission order until exhausted. At Beat 3: any operation with full Capital coverage is voided and the Capital returns to that faction's case; partial coverage attaches a −50 threshold marker. If the target faction submitted no operations against Syndicate, the Capital arrives in their return case as an unexplained windfall — the bribe worked, or was unnecessary. Either way, the Capital is gone from Syndicate's pool.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Bribe mechanic — Capital always reaches target faction; nullification is conditional on their submitted ops | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective — positional wager is doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Beat 2 Automatic; Capital retained with card (not drained); target_faction = bribe recipient; wager structure (positional vs. faction) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Protect/NativeResource — Capital expenditure protects Syndicate assets from named faction's ops | Art 04b §4, §5 |
| Balance | ⚠ | Variable cost 1–N declared at Dispatch; cost is the effect vehicle — goes to target regardless of outcome; over-payment is wasted Capital. **Flagged S141:** `design_note`'s closing sentence ("Cost reasoning: Exposure and Findings identify the target's vulnerabilities...") references resource types that don't appear anywhere in this card's actual `cost` field (`cost = capital * declared(N, min=1)` — Capital only). Reads like a copy-paste fragment from a different card's design note, not corrected here. | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: Capital distributed at Beat 2, void/partial resolved at Beat 3 | — |
| Persistence | ✓ | Immediate — fully resolved by end of Beat 3 | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; player judgment on whether to submit | — |
| Portrait validity | ✓ | Syndicate +1 submitter — positional wager aligns with capital doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted | Art 01 §6–§7 |
| Supported by components | ✓ | Capital retained with card at Beat 0; distributed Beat 2; returned to target_faction at Beat 3 | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 0 Retained validation; Beat 2 distribution procedure; Beat 3 capital-on-card void/partial — all defined in Art 03 | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing` entirely — see schema_cleanup_log.md #24. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Capital only, variable N). See Balance row above re: the dangling cost-reasoning sentence. | Art 00a §9.2 |

#### Outstanding Issues

*None.*

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

*Pre-convention card — design rationale scaffold added S59. Full redesign S65.*

```python
SYN.CA.4 = Card(
    id      = "SYN.CA.4",  version="v2.0",
    name    = "Golden Parachute",
    tagline = "Declare a bribe. Their operations against you are covered. Windfall or nullification — the Capital leaves either way.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Protect,  subject = NativeResource,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district = None, target_faction = faction(named), target_object = None,
    target_taxonomy=None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(acting).capital * declared(N, min=1),  # retained with card at Beat 0 — does not drain to Reservoir
    success         = game.bribe(capital=declared(N), target=faction(target), against=faction(acting), beat3_ops_first_to_last=True),
    successcrit     = None, fail=None, failcrit=None,
    portrait        = {Syndicate: PortraitEntry(submitter=+1)},
    narrative       = "The Syndicate does not wait to find out. They price the outcome in advance.",
    perspectives    = {Syndicate: "We did not lose those resources. We placed them where the problem would be. There is a difference."},
    design_note     = "Capital declared at Dispatch on target profile. Beat 0: retained (not drained). Beat 2: distributed across target_faction Beat 3 ops targeting Syndicate, first-to-last, until exhausted. Beat 3: full coverage = void + Capital to submitter case; partial = −50 marker + Capital to submitter case. No ops from target_faction = windfall to return case. Wager structure: Syndicate bets positionally — wrong bet wastes Capital, correct bet nullifies threat Cost reasoning: Exposure and Findings identify the target's vulnerabilities and legitimize the aggressive posture.",
    arbiter_note    = "See Art 03 Beat 0 (Retained validation), Beat 2 (Golden Parachute procedure), Beat 3 Step 1.4 (capital-on-card resolution).",
    value_rating = None,  # scaffolded, not addressed
)
```

---

### SYN.CA.5 — REGULATORY CAPTURE
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's submission-layer blocking card — analogous to DIR.CA.1 Invoke Jurisdiction (Directorate) but broader in scope and more expensive. Where DIR.CA.1 is limited to STD.CA.1/STD.CA.3, Regulatory Capture blocks any named action type in a district for one round. This flexibility reflects Syndicate's financial reach into regulatory structures. Capital×3 at Beat 2 Automatic with public announcement makes it a visible table signal — everyone knows Syndicate has blocked this action type. The portrait entry with modifier=-2 when targeting a Guild-primary action type captures the doctrinal tension: buying regulatory outcomes is precisely what Guild's permanence doctrine opposes.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Broad submission-layer block — Capital buys regulatory control over any named action type; broader than DIR.CA.1 (Directorate, STD.CA.1/STD.CA.3 only); public announcement makes it a visible table signal | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design — regulatory capture as market governance | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×3; public announcement; Guild-primary portrait modifier outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — regulatory purchase is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ⚠ | Submission/Block/NamedActionType — NamedActionType definition outstanding (Outstanding Issue). **Flagged S141:** `v_card_mechanical_alignment` (DB) also shows `Non-component Subject` for "NamedActionType" — extends the unregistered-Subject gap (schema_cleanup_log.md #27) with a fourth distinct subject string. | Art 04b §4, §5 |
| Balance | ⚠ | Design Rationale and this row both state "Capital×3," but the code's actual `cost = capital*2 + exposure*1` is Capital×2 + Exposure×1. **Flagged S141:** same prose/code cost mismatch pattern as NET.CA.4/SYN.CA.3 (schema_cleanup_log.md #31). Breadth calibration and NamedActionType scope outstanding (Outstanding Issues). | Art 02 §6–§7 |
| Effect duration | ✓ | One round: block applies for round=game.round only | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 positional wager fires on submission | — |
| Portrait validity | ✓ | Syndicate +1 submitter with modifier=−2 for Guild-primary action type; firing conditions outstanding (Outstanding Issue) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any; ChorusNode excluded | Art 01 §6–§7 |
| Supported by components | ✓ | NamedActionType definition outstanding (Outstanding Issue); no new physical components | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; named action type blocked for round; public announcement by ARBITER | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing` entirely — see schema_cleanup_log.md #24. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Cross-resource (Capital + Exposure, both typed correctly). See Balance row above re: the "Capital×3" prose mismatch. | Art 00a §9.2 |

#### Outstanding Issues

- **`NamedActionType` definition:** What constitutes a "named action type" — is this a card name (e.g., "STD.CA.1"), a taxonomy function (e.g., "Add — StructureBlock"), or a broader category (e.g., "Build")? The breadth of the block changes significantly based on this definition.
- **portrait modifier=-2 for Guild-primary action:** `mod_where=action_type(named).primary_faction == Guild` — confirm "primary_faction" is a defined property of action types, or if this needs to be a player declaration at submission.
- **Comparison to DIR.CA.1:** SYN.CA.5 is explicitly broader than DIR.CA.1 at a 1-Mandate premium. Ensure the gap is documented in design notes for balance review.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
SYN.CA.5 = Card(
    id      = "SYN.CA.5",  version="v1.0",
    name    = "Regulatory Capture",
    tagline = "Block a specific action type in a named district for one round.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Submission,  function = Block,  subject = NamedActionType,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any, target_faction=None, target_object=NamedActionType,
    target_taxonomy=None,
    affinity=None,
    restriction = district(target) != ChorusNode,
    cost        = resource.faction(acting).capital * 2 + resource.faction(acting).exposure * 1,
    success     = game.block(district(target), action_type=named, round=game.round, public=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Syndicate: PortraitEntry(submitter=+1, modifier=-2, mod_where=action_type(named).primary_faction == Guild)},
    narrative   = "If you own enough of the regulatory structure, you define what is permitted. The Syndicate does not see this as corruption. They see it as governance.",
    perspectives = {Syndicate: "The regulatory framework exists. We simply ensure it reflects current market conditions."},
    design_note  = None,
    arbiter_note = None,
    value_rating = None,  # scaffolded, not addressed
)
```

#### Syndicate Gap Concepts — Design Notes

Three capability gaps identified in Artifact 04b §8.4: zero information/intelligence capability; Cross-Category — Corrupt — Accord unused; Resource — Redirect — Accord unused. Concepts below are placeholders for slot assignment and detail design. No full data structure — see D-04-05.

**ALTER THE RECORD** — Cross-Category — Corrupt — Accord agreement.
Design note: Syndicate modifies one numeric value in a registered Accord (Capital, presence, or term). ARBITER records the alteration. Both parties notified by case. Value of this card is that alterations are ARBITER-logged — deniable to the table, visible to the record. Addresses Corrupt — Accord gap. Requires Accord mechanic (Artifact 06) to be finalized before detail design.

**SECONDARY OBLIGATIONS** — Resource — Redirect — Accord agreement.
Design note: Transfer an Accord's obligations from the original party to a named faction. The named faction inherits all terms; original party released. Source faction gains 1 Capital at transfer. Neither party's consent is required — Syndicate controls the paper, not the relationship. Addresses Resource — Redirect — Accord gap. Requires Accord mechanic finalized before detail design.

**PORTFOLIO REVIEW** — Cross-Category — Reveal — Intel tokens held.
Design note: Name a faction; ARBITER announces that faction's current Intel token count to acting faction only (private). Syndicate may immediately offer to purchase one token from that faction at 3 Capital — target faction may decline. Provides Syndicate an information entry point without requiring field presence. Addresses zero information/intelligence gap.

### Syndicate — LAND TITLE
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Land Title files a capital claim on undeveloped land — no faction holds a structure block there yet. The card delivers a Grant Deed (ARBITER-issued card, placed in Syndicate's Dispatch Case, moves to hand at Debrief). Grant Deed is a tripwire React card Syndicate holds until another faction builds in the named district, at which point the deed fires. No board marker from this card; no ongoing ARBITER monitoring. Distinct from SYN.CA.1 Leveraged Acquisition (transactional per-round income): Land Title is a positional play — Syndicate reads the board, registers claims on districts likely to develop, then reacts when the trigger fires. Multiple Grant Deeds on the same district are permitted; cost-governed.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Capital claim on undeveloped district; delivers Grant Deed to hand | Art 00 §7 |
| Voice fit | ✓ | Syndicate-only; paper before patrols | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; undeveloped districts only; ChorusNode excluded; multiple deeds permitted (cost-governed) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Add/StructureBlock — ultimate effect is Syndicate structure placed via Grant Deed | Art 04b §4, §5 |
| Balance | ✓ | Capital×5 per deed; payback contingent on opponent building in target district | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent — Grant Deed held until played or game end | — |
| Trigger validity | ✓ | N/A — trigger = None on this card | — |
| Portrait validity | ✓ | Syndicate +1 submitter | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; ChorusNode excluded | Art 01 §6–§7 |
| Supported by components | ✓ | Grant Deed = new component (SCIF-pattern); stored blank in ARBITER tableau; no marker placed by this card | Art 02 §6–§8 |
| Supported by game procedure | ⚠ | Grant Deed tripwire react window needs Art 03 procedure addition (04-n27 territory) | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`boost`/`ps_framing` (`doctrine_mod=None` present). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Capital×5, typed correctly) — matches its own "Capital×5" Balance-row claim exactly, unlike SYN.CA.3/5/9 elsewhere in this set. | Art 00a §9.2 |

#### Outstanding Issues

- **Grant Deed trigger vocabulary (04-n27):** `structure_block.placed(district=deed.district)` is a district-scoped trigger not yet in confirmed TriggerExpr vocabulary. Extension needed in Art 04 §6.3.
- **Grant Deed component registration (04-n26):** New component; Art 02 entry pending. Physical form: blank card; fill-in fields: `district | holder`. Fire effect: +1 Presence Token + 1 Structure Block for deed holder (GD-01 — Art 04 §12b.2). GR 8.2 governs structure placement.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Redesigned S67 — v2.0*

```python
LandTitle = Card(
    id      = "SYN.CA.8",  version="v2.0",
    name    = "Land Title",
    tagline = "File a capital claim on undeveloped land. Let someone else build. Then collect.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Add,  subject = StructureBlock,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None,
    value_rating = None,  # scaffolded, not addressed
    trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.named, target_faction=None, target_object=None,
    target_taxonomy=None,
    affinity=None,
    restriction = (
        district(target).structure_count == 0
        AND district(target) != ChorusNode
    ),
    cost        = resource.faction(acting).capital * 5,
    success     = arbiter.dispatch(GrantDeed(district=district(target)), faction(acting).case),
    successcrit = None,  fail=None,  failcrit=None,
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},
    narrative   = "The deed was filed before the foundation was poured. That is how the Syndicate prefers it.",
    perspectives = {Syndicate: "We don't need to be there. We just need to be on the paperwork."},
    design_note  = "Delivers Grant Deed (GD-01) component (ARBITER tableau → Syndicate case → hand at Debrief). Grant Deed is a tripwire Issued ModReactCard (acquisition=Issued, S133 — PM02 L245) held in faction hand; fires when any faction places a structure block in the named district. Fire effect: +1 Presence Token + 1 Structure Block for deed holder in named district. GR 8.2 governs structure placement (blocked if holder already has structure there; Presence Token still placed). No board marker from this card. Automatic resolution — no crit or fail. Multiple deeds on same district permitted; cost-governed.",
    arbiter_note = "Take 1 blank Grant Deed (GD-01) from ARBITER tableau. Write target district name and Syndicate as holder. Place in submitting faction's Dispatch Case. Grant Deed moves to hand at Debrief.",
)
```

---

### Syndicate — HOSTILE TAKEOVER
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's presence absorption card — distinct from SYN.CA.3 Hostile Acquisition (which targets structure blocks). Hostile Takeover purchases an opponent's community presence and replaces it with Syndicate presence at the same tier, instantly swinging district control without demolition. The Intel token requirement establishes a Ghost-Syndicate structural link: Syndicate cannot execute a takeover without prior intelligence on the target. Capital×4 + Intel reflects the combined financial and intelligence investment required. The net effect on the district's control tier is neutral — same count of tokens, different faction — making this a covert displacement rather than a destructive act. Successcrit returns 1 Capital (efficient acquisition). Failcrit NotificationSlip to target: a failed takeover attempt alerts the target.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Presence absorption — control swing without demolition; displaces target presence and replaces with Syndicate at equivalent tier; distinct from SYN.CA.3 (StructureBlock) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design — acquisition of relationships, not displacement | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×4 + IntelToken; Ghost-Syndicate structural link; token supply and void-on-Absent outstanding (Outstanding Issues) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) — presence absorption is Syndicate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Add/PresenceToken — replaces target presence at same count | Art 04b §4, §5 |
| Balance | ⚠ | Design Rationale and this row both state "Capital×4 + IntelToken/Intel," but the code's actual `cost = capital*3 + mandate*2` is Capital×3 + Mandate×2 — no IntelToken in the cost at all (the Intel Token requirement lives in `restriction`, not `cost`). **Flagged S141:** fourth confirmed instance of the prose/code cost mismatch pattern (NET.CA.4, SYN.CA.3, SYN.CA.5 are the other three — schema_cleanup_log.md #31). Token replacement count outstanding (Outstanding Issue). | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: presence tokens replaced at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Syndicate +1 submitter; failcrit NotificationSlip is game effect (not portrait), per DIR.PA.2 | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken transfer; IntelToken cost; token supply source and void-on-Absent outstanding (Outstanding Issues) | Art 02 §6, §8; Art 02 §11–§12 |
| Supported by game procedure | ✓ | Beat 3 d100; ARBITER replaces tokens; void-on-Absent resolution outstanding (Outstanding Issue) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `boost`/`ps_framing` (has `card_id`, `doctrine_mod=None`). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/successcrit populated (fail=None), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Missing row, scaffolded S141. Cross-resource (Capital + Mandate, both typed correctly) — but see Balance row above; the cost this row describes doesn't match the card's own stated "Capital×4 + Intel" design intent. | Art 00a §9.2 |

#### Outstanding Issues

- **Token replacement count:** At resolution, ARBITER replaces ALL of target's presence tokens in the district with Syndicate tokens at the same count. Confirm: if target is Dominant (3 tokens), Syndicate places 3 tokens and target drops to Absent. Does Syndicate need those tokens in reserve, or does ARBITER provide them from supply?
- **Self-takeover of Absent district:** If target reaches Absent between Dispatch and Beat 3 resolution (e.g., from a prior Beat 3 action this round), the restriction `presence >= 1` fails at resolution — confirm card is void (slot + resources lost) or triggered on Dispatch state.
- **Ghost-Syndicate link:** This card creates the structural link between Ghost's Intel collection and Syndicate's high-end plays. Confirm with Ghost players that faction-keyed Intel token mechanics are compatible (Ghost generates Syndicate-keyed Intel; Syndicate can purchase or trade for it).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Draft S59 — design pass pending*

```python
HostileTakeover = Card(
    id      = "SYN.CA.9",  card_id = "SYN.CA.9",  version="v1.0",  # corrected S132 — was hardcoded "SYN.MOD.8" (a different card's ID), mismatched card_status and §8 index, which both already had this correctly as SYN.CA.9
    name    = "Hostile Takeover",
    tagline = "Purchase control of a faction's community presence in a district, replacing their tokens with Syndicate's at equivalent tier.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Add,  subject = PresenceToken,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10}, doctrine_mod=None,
    value_rating = None,  # scaffolded, not addressed
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.named, target_faction=faction(named_opponent), target_object=PresenceToken,
    target_taxonomy=None,
    affinity=None,
    restriction = (
        faction(target).presence(district(target)) >= 1
        AND faction(acting).intel_tokens(faction=faction(target)) >= 1
    ),
    cost        = resource.faction(acting).capital * 3 + resource.faction(acting).mandate * 2,
    success     = game.replace_presence(
        faction(target), district(target),
        with_faction=faction(acting),
        count=faction(target).presence_count(district(target)),
    ),
    successcrit = resource.faction(acting).capital += 1,
    fail=None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},
    narrative   = "The Syndicate does not displace people. It acquires their positions. There is a difference, legally speaking.",
    perspectives = {Syndicate: "We purchased the relationship. The people can stay. Their affiliation is now ours."},
    design_note  = "Distinct from SYN.CA.3 Hostile Acquisition (StructureBlock). Replaces ALL target presence in district with Syndicate presence at same count (same control tier — neutral effect on tier, swing in ownership). Requires Ghost-sourced faction-keyed Intel token. Intel token creates structural link between Ghost and Syndicate — neither faction announces it publicly.",
    arbiter_note = "At resolution: count target's presence tokens in district. Remove all of them. Place equal count of Syndicate presence tokens in same district. Net tier unchanged; ownership transferred. Deliver NotificationSlip to target on crit fail. Crit success: +1 Capital to Syndicate.",
)
```

---

### SYN.CA.10 — ACCORD TRANSFER
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's party-substitution card — the mechanism by which every bilateral agreement becomes a potential Syndicate asset. Replaces one named party in an active Accord with any faction (including Syndicate itself), without either party's consent. ARBITER makes the physical alteration on the Accord form and announces the change publicly at Beat 3. On crit success, the incoming party gains a renegotiation right: one numeric term of their choosing is altered at the table. This gives the involuntarily inserted party a single concession — the transfer comes with a term adjustment. Completes the Accord manipulation suite with SYN.CA.11 Redline (Terms). Supersedes gap concept SECONDARY OBLIGATIONS.

#### Card Story
A form that has been in the Accord Placement Area since Debrief is quietly updated between beats. ARBITER announces the change at Beat 3 resolution. The parties to the original agreement have already moved on.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Accord party replacement without consent; fills Economy\|Corrupt\|AccordCard Syndicate gap; distinct from SYN.CA.11 (Terms) and SYN.CA.3 (StructureBlock redirect); supersedes SECONDARY OBLIGATIONS gap | Art 00 §7 |
| Voice fit | ✓ | FactionSpecific Syndicate; full perspectives block; "restructured who holds it" is on-voice | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital(3); no consent required (confirmed — Art 06 §9.10 signed off L205); Syndicate may be outgoing or incoming party | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy\|Corrupt\|AccordCard — party names on Accord form are written records; replacement is a Corrupt operation on the document (taxonomy corrected S107 L227 from Redirect) | Art 04b §4, §5 |
| Balance | ⚠ | d100 threshold 50 with high-impact consent-free effect; crit renegotiation right for incoming party adds table interaction; flag for doctrine review | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent board state change (Accord form altered, stays active); card itself is Immediate | — |
| Persistence | ✓ | Immediate — no lingering card-as-condition | Art 04 §6 |
| Trigger validity | ✓ | Missing row, scaffolded S141. `trigger` not declared in the code (card has no `trigger` field at all) — N/A, consistent with a Beat 3 covert d100 op with no React/trigger mechanic. | — |
| Portrait validity | ⚠ | flat entries only; submitter-bounded claimed, but code shows `Syndicate: PortraitEntry(flat=+1)` for the acting/submitting faction — `flat` fires "on resolution regardless of submitter" (§6.1), which is a different semantic than "submitter-bounded." **Flagged S141:** also applies `flat=-1` to Network and Directorate, who are not acting/submitting factions at all — reacting publicly to news, not making a portrait-worthy choice of their own. Same open question as schema_cleanup_log.md #7 (target-faction flat entries, doctrinally unexamined), now confirmed on a CA card. Not resolved. | Art 04 §6.2 |
| Supported by zones | ✓ | Accord Placement Area (Art 01); Target Profile in Dispatch Case (covert path) | Art 01 §6–§7 |
| Supported by components | ✓ | AccordCard/AccordForm (Art 06 §9); Target Profile DB:48 with declared_params (Art 02 v2.4 — L233); Dispatch Case (Art 02) | Art 02; Art 06 §9 |
| Supported by game procedure | ✓ | Beat 3 covert d100; Art 06 §9.10 Alter/Named Party governs physical alteration; Art 06 §9.10 Alter/Terms governs crit term change (incoming party elects at table); ARBITER announces success publicly | Art 03 §9, §11; Art 06 §9.10 |
| Data schema validation | ⚠ | All fields per §6.1/§6.2. Re-derived S141: missing `boost`/`ps_framing` (has `card_id`, `doctrine_mod=None`). `cost = Capital(3)` also uses a third cost-notation style (bare resource-type-as-callable, no `resource.faction()` wrapper) alongside the corpus' two other styles — see schema_cleanup_log.md #22. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story present | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Four paths (success / crit success / fail / failcrit) each has exactly one outcome | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | **Corrected S141 — row existed but contained the raw guidance template text verbatim, with no actual assessment or Pass value.** Filling in now as scaffolding: mono-resource (`Capital(3)` only, acting faction's own). Bare `Capital(n)` notation flagged above (Data schema validation row) as a schema-vocabulary question, not resolved. | Art 00a §9.2 |

#### Outstanding Issues

- **Balance:** Threshold 50 with consent-free, permanent Accord restructuring is high-impact. Crit renegotiation right for incoming party is untested — could create unexpected table dynamics. Flag for doctrine review.
- **Incoming party renegotiation constraint:** On crit success, incoming party may alter "any" numeric term — no restriction stated on which clause or by how much. Consider whether to bound the new value (e.g., within clause-type vocabulary per Art 06 §9.3) or leave fully free. Non-blocking — Art 06 §9.3 clause vocabulary applies implicitly.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ | |

*v0.1 — S111: full design pass replacing S59 stub. Art 06 §9.10 signed off (L205); taxonomy corrected (L227). Issues Resolved pending balance doctrine review.*

```python
SYN.CA.10 = Card(
    card_id      = "SYN.CA.10",  version = "v0.1",
    name     = "Accord Transfer",
    tagline  = "All terms remain binding. The signatories have been updated.",
    type     = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,

    layer    = Economy,  function = Corrupt,  subject = AccordCard,

    beat         = 3,
    resolution   = d100,
    threshold    = 50,
    ring_mod     = None,
    doctrine_mod = None,
    value_rating = None,  # scaffolded, not addressed

    target_district = None,
    target_faction  = faction(outgoing_party),
    target_object   = AccordCard(state=active, party=target_faction),
    declared_params = (
        incoming_party = faction(any),
        # written on TP declared-parameters line at Covert Dispatch
        # may be Syndicate (self-insertion or self-exit) or any other faction not
        # already a named party on the target Accord
    ),

    affinity    = None,
    restriction = (
        target_object.state == active
        AND target_faction in target_object.parties
        AND declared_params.incoming_party not in target_object.parties
    ),
    cost     = Capital(3),
    boost    = None,

    success = target_object.alter(
        type     = NamedParty,
        outgoing = target_faction,
        incoming = declared_params.incoming_party,
    ),
    # ARBITER strikes outgoing_party on Accord form; writes incoming_party.
    # All obligations and benefits transfer. Accord remains active.
    # ARBITER announces to table: "[Outgoing] replaced by [Incoming] on [Accord]."
    # Art 06 §9.10 Alter/Named Party. No consent required from either party.

    successcrit = faction(declared_params.incoming_party).player.elect(
        target_object.alter(type=Terms, clause=any_numeric, new_value=player_chosen_int),
    ),
    # delta only: named party change (from success) + incoming party elects one
    # numeric term alteration at the table immediately after ARBITER announcement.
    # Incoming party names the clause row and states the new integer value;
    # ARBITER makes the physical alteration per Art 06 §9.10 Alter/Terms.

    fail        = None,
    failcrit    = faction(acting).standing -= 2,
    # no Accord change; cost spent; acting faction announced publicly (Discovery)

    on_accept  = None,
    on_decline = None,

    persistence           = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    portrait = {
        Syndicate:   PortraitEntry(flat=+1),
        Network:     PortraitEntry(flat=-1),
        Directorate: PortraitEntry(flat=-1),
    },

    narrative = "The form in the Accord Placement Area is updated. The parties to the original agreement learn about it at the same time as everyone else.",

    perspectives = {
        Syndicate:   "The agreement was always an asset. We've restructured who holds it.",
        Ghost:       "The Accord changed hands without a handshake. The power to do that is worth understanding.",
        Network:     "A binding agreement — restructured by someone who wasn't party to it, without notice. This is what unaccountable capital does.",
        Directorate: "A covert restructuring of a binding agreement. The incoming party is now bound. Noted.",
        Guild:       "Agreements don't restructure themselves. Someone just demonstrated they can override the process.",
    },

    design_note  = "Completes the Accord manipulation suite with SYN.CA.11 Redline: CA.10 controls who is bound; CA.11 controls what the terms say. Economy|Corrupt|AccordCard — party names on the Accord form are written records; replacement is a Corrupt operation. ARBITER makes the physical alteration at Beat 3 per Art 06 §9.10 and announces publicly (the change is public; the acting faction remains covert). No consent required from either party (Art 06 §9.10, L205). Outgoing_party may be Syndicate (self-exit, forcing obligations onto incoming party). Incoming_party may be Syndicate (self-insertion to acquire another faction's Accord position). Restriction: incoming_party not already a named party on the same Accord. Crit success: incoming party — the involuntarily inserted faction — elects one numeric term change at the table; gives them a single renegotiation concession. Supersedes SECONDARY OBLIGATIONS gap concept.",
    arbiter_note = "Covert Dispatch: acting faction writes on TP declared-parameters line: incoming party. Beat 0: verify restriction — outgoing party is named on target Accord; incoming party is not. Beat 3: roll d100. On success (≤50): locate Accord form in Accord Placement Area; strike outgoing party name; write incoming party name; announce to table: '[Outgoing] replaced by [Incoming] on [Accord]. All terms now bind [Incoming].' On crit success (01–05): apply named party change as above; then address incoming party player: 'You may alter one numeric term in this Accord — name the clause and state the new value.' Apply declared change per Art 06 §9.10 Alter/Terms. On fail: no effect; cost spent. On failcrit (96–00): no Accord change; announce acting faction publicly; apply Syndicate −2 PS.",
)
```

---

### Syndicate — PARASITIC
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate's economic intelligence tap — a positional wager on district activity. At Beat 2, Syndicate bets that someone is already operating in the target district this round. ARBITER checks the Beat 3 dispatch queue; if a Beat 3 card targeting the district exists, Syndicate receives an Intel token keyed to that card's submitting faction (first in resolution order). If no one is operating there, the card fails and Capital is spent. The wager rewards Syndicate for reading the board correctly before operations fire — not for monitoring what happens, but for knowing what's coming. Covert — other factions cannot observe the tap.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intel from reading opponent dispatch queue — positional wager on district activity before Beat 3 fires | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective — infrastructure that reads commerce before it happens | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×2; positional wager; payoff requires correct district read; covert | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/IntelToken — Intel from district activity read | Art 04b §4, §5 |
| Balance | ✓ | Capital×2; fail = cost spent; payoff contingent on opponent operating in district this round | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — resolved fully at Beat 2; no carry, no deferred effects | — |
| Persistence | ✓ | Immediate — no game-state marker persists beyond Beat 2 resolution | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 3 queue check is resolution condition, not a trigger | — |
| Portrait validity | ✓ | Fires on success (Intel delivered); unconditional on success — no mod_where needed | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — Intel token from standard stock | Art 02 §6–§8 |
| Supported by game procedure | ⚠ | ARBITER Beat 3 queue check at Beat 2 resolution — procedure not yet in Art 03 §9.4. Tracks under 04-n27. | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`boost`/`ps_framing` (`doctrine_mod=None` present). Also: `fail` and `failcrit` fields are absent from the code entirely — not `None`, just not declared — the only card in this set missing them outright (design intent per prose is presumably "cost spent, no effect," matching the `None` convention used everywhere else, but it isn't written). Flagged, not fixed. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`; `success` populated, `successcrit=None`; `fail`/`failcrit` undeclared (see Data schema validation) rather than `None` — no `game.choose_one()` regardless. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Capital only, typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **Art 03 Beat 2 procedure:** ARBITER checking the Beat 3 dispatch queue at Beat 2 resolution is not yet proceduralized in Art 03 §9.4. Tracks under 04-n27.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Redesigned S67 — v2.0. Positional wager replacing deferred conditional. No component needed.*

```python
SYN.CA.6 = Card(
    id      = "SYN.CA.6",  version="v2.0",
    name    = "Parasitic",
    tagline = "Wire a district's commerce. Let others do the work.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,

    layer   = Economy,  function = Add,  subject = IntelToken,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = None,  # scaffolded, not addressed
    trigger         = None,
    resolution_type = "Positional wager",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.named,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).capital * 2,

    success     = arbiter.dispatch(
                    IntelToken(faction=game.ops(beat=3, at=district(target)).first(resolution_order).submitter),
                    faction(acting).case
                  ),
    successcrit = None,

    portrait    = {Syndicate: PortraitEntry(submitter=+1)},

    narrative    = "The Syndicate does not steal from the river. They build a weir.",
    perspectives = {Syndicate: "We invested in the district's infrastructure. Why shouldn't we see what moves through it?"},

    design_note  = "Positional wager — resolved fully at Beat 2. ARBITER checks Beat 3 dispatch queue for any card targeting district(target). If found: Intel token keyed to the submitting faction of the first card in resolution order delivered to Syndicate's case. If no Beat 3 card targets the district: cost spent, no effect. Covert — other factions cannot observe.",
    arbiter_note = "At Beat 2 resolution: check Beat 3 dispatch queue for any card targeting district(target). If found: deliver IntelToken keyed to that card's submitting faction (first in resolution order) to Syndicate's case; portrait fires. If none found: cost spent, no effect, portrait does not fire. Covert — do not announce.",
)
```

---

### Syndicate — CORPORATE BLACKMAIL
[↑ Covert Operations](#syndicate-covert-operations)

*Split S70 per PM05 04-n47 (choose_one violation) and 04-n48. Card A (Capital coercion) below. Card B (forced Accord vote) stub follows — mechanics deferred to future session.*

---

### SYN.CA.7 — CORPORATE BLACKMAIL
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate uses covertly gathered intelligence to threaten a faction operating in a named district. ARBITER delivers the blackmail notice privately to the target at Beat 3 — notification is covert, not public. The target faces a binary choice: comply (pay resources and keep their position) or resist (accept consequences). Either way, Syndicate pays a PS cost — operating this way corrodes institutional relationships regardless of outcome. Distinct from SYN.CA.1 Leveraged Acquisition: SYN.CA.1 is transactional extraction (pays Capital, receives native output without interaction); SYN.CA.7 is coercive leverage (threatens loss to extract compliance from a specific target at a specific position).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intel-to-compliance coercion; target choice (pay or suffer) replaces forced transfer; presence restriction grounds the threat in a real position | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Syndicate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; IntelToken cost; flat portrait −1 self-cost; target_district added (S71) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Redirect/NativeResource — compliance payment or presence loss at target district | Art 04b §4, §5 |
| Balance | — | Comply cost (resource amount) TBD; resist consequence (presence tier loss + PS −1) outstanding | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate at Beat 3 resolution | — |
| Persistence | ✓ | Immediate — no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Syndicate flat=−1 regardless of outcome — schema validation outstanding | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — presence restriction is district-specific | Art 01 §6–§7 |
| Supported by components | — | Comply path: resource transfer (amount TBD). Resist path: presence tier reduction + PS — components confirmed; amount outstanding | Art 02 §6–§8 |
| Supported by game procedure | — | Beat 3 covert ElectPlayer: ARBITER whispers to target; target elects comply/resist. No existing Art 03 procedure for covert notification + choice at Beat 3. New procedure required before Issues Resolved. | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`boost`/`ps_framing` (`doctrine_mod=None` present). `on_accept`/`on_decline` correctly used only because `outcome_type=ElectPlayer` — good confirming example of the schema's ElectPlayer-only field group being used correctly. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`; `success`/`successcrit`/`fail`/`failcrit` all `None` by design — the real outcome logic lives in `on_accept`/`on_decline` (ElectPlayer), each resolving to exactly one outcome, no `game.choose_one()`. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Missing row, scaffolded S141. Cost is IntelToken alone, no fungible resource paired — same "starkest form" shape as GHO.CA.9/GHO.CA.10. Same open question as schema_cleanup_log.md #10 (now ~9 confirmed instances corpus-wide), flagged not resolved. | Art 00a §9.2 |

#### Outstanding Issues

- **Comply resource amount:** What does the target pay on compliance? Suggest 2 native of target district (parallel to SYN.CA.1 output rate). Confirm type and amount.
- **Resist consequence — presence loss:** "Lose influence" interpreted as lose 1 presence tier at target_district. Confirm: tier loss vs. token count loss.
- **Covert ElectPlayer procedure:** No Art 03 procedure exists for covert notification + player choice at Beat 3. Must be written as generalizable procedure. Issues Resolved blocked until written.
- **Flat portrait modifier:** `portrait = {Syndicate: PortraitEntry(flat=-1)}` — confirm "flat" is valid schema field. Flag for schema pass if not.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*v2.0 — S71: full redesign. Forced transfer replaced with coercive choice (ElectPlayer). target_district added. Restriction: target presence > 0 at district. Comply/resist model. Covert notification procedure outstanding.*

```python
SYN.CA.7 = Card(
    id      = "SYN.CA.7",  version="v2.0",
    name    = "Corporate Blackmail",
    tagline = "Submit covertly. The target decides what compliance costs less.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Redirect,  subject = NativeResource,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    value_rating = None,  # scaffolded, not addressed
    resolution_type="Transactional", outcome_type=ElectPlayer,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district = district.named,
    target_faction  = faction(named_opponent),
    target_object   = None,
    target_taxonomy=None,
    affinity        = None,
    restriction     = faction(target).presence(district(target_district)) > 0,
    cost            = IntelToken(any) * 1,

    success     = None,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    # ElectPlayer — ARBITER notifies target privately at Beat 3 resolution
    on_accept  = faction(target).resource(native) -= 2,  # amount TBD; placeholder 2 native
    on_decline = (
        faction(target).presence_tier(district(target_district)) -= 1,
        faction(target).standing -= 1,
    ),
    # always: faction(acting).standing -= 1 regardless of outcome (encoded in portrait flat=-1)

    portrait    = {Syndicate: PortraitEntry(flat=-1)},
    narrative   = "The information was gathered properly. What is done with it is simply business.",
    perspectives = {Syndicate: "We don't call it blackmail. We call it an incentive structure with consequences attached."},
    design_note  = "Covert submission; private notification at Beat 3 (ARBITER whispers to target — not public). Target elects comply or resist. Comply: pay resources (amount TBD). Resist: presence tier −1 at target district + PS −1. Syndicate PS −1 always. Covert ElectPlayer procedure required in Art 03 before Issues Resolved.",
    arbiter_note = "Beat 3: whisper privately to target faction — inform them of blackmail attempt. Target elects comply or resist (not announced publicly). On comply: transfer [X native TBD] from target to Syndicate. On resist: reduce target's presence tier at named district by 1; reduce target PS by 1. Regardless of outcome: reduce Syndicate PS by 1.",
)
```

---

### Syndicate — ACCORD LEVERAGE *(placeholder name)*
[↑ Covert Operations](#syndicate-covert-operations)

⚠ **Flagged for redesign (Andy, S133) — see Outstanding Issues.** Current forced-acceptance mechanic duplicates SYN.MOD.11 Signature on File. Redesign direction: corrupt a different, not-yet-described Accord field instead. Design Rationale below is legacy content, retained for reference until the redesign pass.

#### Design Rationale
Syndicate converts gathered intelligence into a forced Accord commitment. The Intel token is the leverage; the effect fires during the Beat 4 Accord formation window. The target cannot negotiate amendments, decline, or counter-propose — they accept the draft as written. Uses Art 06 §9 Lock manipulation type. Distinct from SYN.CA.7 Corporate Blackmail (presence-based coercion in a district): The Fixer operates entirely in the Accord formation layer, with no district dependency. The target must be a named party to the Accord draft being locked.

Typed Issued `ModReactCard` (S133 — retyped twice: originally `ModActionCard`, briefly `ModIssuedCard`, now `acquisition=Issued` on `ModReactCard` under the acquisition-axis model; PM02 L245 revises L241/PM05 04-n154/04-n160): ARBITER-delivered as a consequence of another card's success, not drawn from the Modifier deck — same acquisition pattern as GD-01 Grant Deed and STD.MOD.1 Overture. Acquisition path should be re-confirmed against whatever mechanic the redesign lands on.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence leverage applied to Accord formation — forces yes-vote on existing draft terms | Art 00 §7 |
| Voice fit | — | TBD — single Syndicate perspective minimum | Art 00 §7 |
| Doctrine alignment | — | Syndicate only; IntelToken cost; Art 06 §9 Lock interaction outstanding | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Issued ModReactCard (S133 — retyped twice; see Design Rationale; PM02 L245 revises L241/PM05 04-n154/04-n160) — ARBITER-delivered, not deck-drawn; modifier applied to Accord formation window, not a CovertOperation | Art 04 §6.1, §6.2 |
| Taxonomy fit | — | Modifier card taxonomy — excluded from Layer/Function/Subject taxonomy | Art 04b §5.1, §9 |
| Balance | — | IntelToken × 1; effect = forced acceptance of existing Accord draft; scope and party requirements outstanding | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate at Beat 4 Accord formation | — |
| Persistence | ✓ | Immediate — Accord execution follows standard Art 06 §9 procedure once locked | Art 04 §6 |
| Trigger validity | — | Trigger = named Accord draft exists + not yet executed. Trigger confirmation outstanding. | Art 06 §9 |
| Portrait validity | — | TBD — modifier card portrait model | Art 04 §6.2 |
| Supported by zones | ✓ | No district dependency — Accord-layer effect only | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; AccordDraft as target object (registered Art 06 §9) | Art 02 §6–§8 |
| Supported by game procedure | — | Art 06 §9 Lock manipulation type covers forced acceptance in principle. Interaction between modifier card timing and Beat 4 Accord window not yet written. Procedure required before Issues Resolved. | Art 06 §9; Art 03 §9 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Redesign flagged (Andy, S133) — PM05 04-n158.** Forced-acceptance mechanic is a near-duplicate of SYN.MOD.11 Signature on File (same effect — force Accord acceptance without consent — and Signature on File already has a documented generator, SYN.CA.12 Boilerplate). Andy's direction: keep both cards, but redesign The Fixer to corrupt a different Accord field that hasn't been described yet elsewhere in the set — distinct from SYN.CA.10 Accord Transfer (named party) and SYN.CA.11 Redline (numeric/ordinal fill-in value). Which field is undefined; identify during the 09-06 redesign pass. This supersedes the below issues that are specific to the forced-acceptance mechanic — they stay listed for reference but won't be resolved until the redesign lands on a new effect.
- **Art 03 procedure — modifier card in Accord window:** No procedure written for an Issued ModReactCard played during Beat 4 Accord formation. Superseded by redesign — will need to be re-evaluated against whatever new effect is chosen.
- **Party requirement:** Must Syndicate be a named party to the target Accord? Expected yes — this is leverage, not arbitration. Superseded by redesign.
- **Scope after forced acceptance:** Can the target exercise any standard Accord rights after forced acceptance (dissolution, breach action), or are they fully bound as written? Superseded by redesign.
- **Lock type interaction:** Art 06 §9 Lock applies to a single manipulation within an existing Accord. Confirm whether "forcing acceptance of a draft Accord" is a Lock (modifying the target's vote) or a new manipulation category. Superseded by redesign.
- **Generating card:** Undefined under the current mechanic. Revisit once the redesign lands — Boilerplate is already spoken for (Signature on File); a new generator or acquisition path may be needed.
- **Card name:** Placeholder — confirm before sign-off.
- **Card ID:** TBD — pending PM05 04-n1 numbering pass.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*v1.0 — S71: redesigned as modifier card (Instant). Forced acceptance of Accord draft as written. Replaces deferred "forced Accord vote" stub from S70.*
*v1.1 — S133: retyped ModActionCard → ModIssuedCard (PM02 L241/PM05 04-n154). No field changes — `effect` already used a plain MutationExpr, which the prior ModActionCard typing didn't actually support (its `effect` field requires a ModActionExpr tagged union).*
*v1.2 — S133: retyped again, ModIssuedCard → Issued ModReactCard (`acquisition=Issued`) under the acquisition-axis model (PM02 L245 revises L241/PM05 04-n160). `effect` field renamed `success` to match ModReactCard's field set.*
*Flagged S133 (PM05 04-n158): forced-acceptance mechanic duplicates SYN.MOD.11 Signature on File — redesign to a different, not-yet-described Accord-corrupt field. Python block below is the pre-redesign mechanic, retained for reference.*

```python
# STUB — flagged for redesign (PM05 04-n158): duplicates SYN.MOD.11 Signature on File.
# Below is the pre-redesign mechanic, kept for reference — effect will change.
Card(
    id=TBD,  version="v1.2",
    name        = "The Fixer",  # placeholder
    type        = ModReactCard,  faction = Syndicate,
    beat        = None,  # fires on trigger, not a named beat
    trigger     = AccordDraft(named).status == Draft,  # draft exists, not yet executed
    restriction = AccordDraft(named).party(faction(target)) == True,  # target is named party
    cost        = IntelToken(any) * 1,
    acquisition      = Issued,
    generating_card  = None,  # still undefined — see Outstanding Issues
    success     = AccordDraft(named).lock(faction(target), accept_as_written=True),
    successcrit = None,  fail = None,  failcrit = None,
    # Art 06 §9 Lock manipulation type — target cannot negotiate, decline, or counter-propose
    target_taxonomy=None,
    portrait    = {Syndicate: PortraitEntry(submitter=+1)},  # TBD — modifier card portrait model
)
```

---

### SYN.CA.11 — REDLINE
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
Syndicate quietly alters a numeric or ordinal fill-in value in an active Accord — a resource quantity, an influence tier, a Quarter deadline — while the form sits face-up in the Accord Placement Area. The effect is public (the altered form is visible to all players) but the actor is covert (ARBITER makes the physical change without identifying the submitting faction). Completes the Syndicate Accord manipulation suite: SYN.CA.10 Accord Transfer changes a named party; SYN.CA.11 Redline changes what the terms say. Fills the Information|Corrupt|AccordAgreement gap identified in Art 04b §8.3. Distinct from The Fixer modifier card (which forces acceptance of a draft, not alteration of an active one).

#### Card Story
A Syndicate operative approaches the Accord Placement Area during a recess. They adjust a number in one clause — a quantity, a tier, a deadline. The revision goes unquestioned. By the time anyone re-reads the terms carefully, the original number is simply what everyone thought they agreed to.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Information-layer Accord alteration; Syndicate "small print" doctrine; fills Information\|Corrupt\|AccordAgreement gap (Art 04b §8.3); distinct from SYN.CA.10 (named-party alteration) and The Fixer modifier (forced acceptance of draft) | Art 00 §7 |
| Voice fit | ✓ | FactionSpecific Syndicate; single Syndicate perspective; full perspectives block documented | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital×2; covert; altering written agreements for positional advantage = Capital doctrine ("control comes from positioning early") | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/AccordAgreement — Accord clause fill-in values are physically written records; valid Corrupt target per §4.10/P24 | Art 04b §4, §5 |
| Balance | ✓ | Capital×2; threshold 50 (Average); restriction = active Accord present only; failcrit = Discovery; prospective clause alteration scales with Accord significance | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — one-time physical alteration; no persistent game-state marker; Accord persists with altered terms under its own lifecycle | — |
| Persistence | ✓ | Immediate — alteration committed at Beat 3; no persistence tracking required | Art 04 §6 |
| Trigger validity | ✓ | trigger = None; restriction gates on active Accord count checked at Beat 0 | — |
| Portrait validity | ⚠ | flat entries claimed submitter-bounded, but `flat=+1` on Syndicate (the actual submitter) and `flat=-1` on Network/Directorate (non-acting factions reacting publicly) is the same pattern flagged on SYN.CA.10 — extends schema_cleanup_log.md #7. failcrit = Discovery (not a portrait entry, confirmed correct). | Art 04 §6.2 |
| Supported by zones | ✓ | Accord Placement Area registered zone (Art 06 §9.5) | Art 01 §6–§7 |
| Supported by components | ✓ | AccordAgreement face-up in Accord Placement Area (Art 06 §9); Target Profile declared-parameters blank line added Art 02 §8 (S111) | Art 02 §6–§8; Art 06 §9 |
| Supported by game procedure | ✓ | Alter/Terms covert procedure: Art 06 §9.10 (covert op → ARBITER makes physical alteration); no new Art 03 step required | Art 06 §9.10 |
| Data schema validation | ⚠ | All fields populated per §6.1/§6.2. Re-derived S141: missing `boost`/`ps_framing` (has `card_id`, `doctrine_mod=None`). `cost = Capital(2)` uses the same bare resource-callable notation flagged on SYN.CA.10 (schema_cleanup_log.md #22). `successcrit = standing += 1` also has no `faction(acting).` qualifier, unlike every other card's standing mutations in this corpus — presumably means the acting faction's own standing, but it isn't written explicitly. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story present | Art 04 §5 P26 |
| Outcome determinacy | ✓ | One outcome per tier; no branching; successcrit additive on success; failcrit additive on fail | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | **Corrected S141 — row existed but contained the raw guidance template text verbatim, with no actual assessment or Pass value.** Filling in now as scaffolding: mono-resource (`Capital(2)` only). | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

*v0.1 — S111: new card, fills Information\|Corrupt\|AccordAgreement gap. Art 02 §8 Target Profile declared-parameters field added (S111).*

```python
SYN.CA.11 = Card(
    card_id      = "SYN.CA.11",
    version  = "v0.1",
    name     = "Redline",
    tagline  = "The numbers that matter are the ones no one double-checked.",
    type     = CovertOperation,
    subtype  = FactionSpecific,
    faction  = Syndicate,

    layer    = Information,
    function = Corrupt,
    subject  = AccordAgreement,

    beat         = 3,
    resolution   = d100,
    threshold    = 50,
    ring_mod     = None,
    doctrine_mod = None,
    value_rating = None,  # scaffolded, not addressed

    target_district = None,
    target_faction  = None,
    target_object   = AccordAgreement(state=active, clause_contains=numeric_fill_in),

    affinity    = None,
    restriction = AccordAgreement.count(state=active) >= 1,
    cost        = Capital(2),
    boost       = None,

    success     = target_object.alter(type=Terms, clause=declared_clause,
                                      new_value=declared_value),
    successcrit = standing += 1,
    fail        = None,
    failcrit    = Discovery,

    on_accept  = None,
    on_decline = None,

    persistence           = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    portrait = {
        Syndicate:   PortraitEntry(flat=+1),
        Network:     PortraitEntry(flat=-1),
        Directorate: PortraitEntry(flat=-1),
    },

    narrative = "The document in the placement area is a public record. It has always been a public record. The number in the third clause has always been that number. If it seems different from what you remember — you're probably misremembering.",

    perspectives = {
        Syndicate:   "Leverage doesn't expire. It just changes shape.",
        Ghost:       "We noticed the discrepancy. We are still determining whether it was us, them, or the original terms.",
        Network:     "Someone revised the Accord. No one is claiming it. That's the story.",
        Directorate: "The written record is the law. We will find out who changed this.",
        Guild:       "We build to the spec we signed. If the spec changed, we need to know now.",
    },

    design_note  = "Syndicate's only Information-layer covert op. Effect is public (form changes) but actor is covert — unique table dynamic. Valid clause targets: fill-in values that are numeric or ordinal (resource quantity, influence tier, Quarter number). Prohibited: clause rows with only named entries (district name, PA type) — not numeric alterations. declared_clause and declared_value sourced from Target Profile declared-parameters line.",
    arbiter_note = "Acting faction declares at Covert Dispatch: (a) target Accord by named parties, (b) clause row to alter, (c) replacement value — all written on Target Profile declared-parameters line. On success at Beat 3: locate declared Accord form in Accord Placement Area; apply Alter/Terms per Art 06 §9.10 — write new value; acting faction identity not disclosed. If declared Accord has been removed before Beat 3 resolution, treat as fail. Alteration resolves in submission order; subsequent Beat 3 ops see altered terms.",
)
```

---

### SYN.CA.12 — BOILERPLATE *(stub)*
[↑ Covert Operations](#syndicate-covert-operations)

#### Design Rationale
⚠ Pending design review (09-16). See stub design note below.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ⚠ |  |  |
| Voice fit | ⚠ |  |  |
| Doctrine alignment | ⚠ |  |  |
| Card type fit | ⚠ |  |  |
| Taxonomy fit | ⚠ |  |  |
| Balance | ⚠ |  |  |
| Effect duration | ⚠ |  |  |
| Persistence | ⚠ |  |  |
| Trigger validity | ⚠ |  |  |
| Portrait validity | ⚠ |  |  |
| Supported by zones | ⚠ |  |  |
| Supported by components | ⚠ |  |  |
| Supported by game procedure | ⚠ |  |  |
| Data schema validation | ⚠ | Pending 04-n70. Re-derived S141: `cost = Capital(1) + Mandate(1)` uses the same bare resource-callable notation flagged on SYN.CA.10/11 (schema_cleanup_log.md #22) — third instance. Portrait `flat=+1` on Syndicate (the submitter) is the same pattern flagged on SYN.CA.10/11 (schema_cleanup_log.md #7), though here it's only the acting faction, not a target-faction instance. Missing `card_id`(present)/`boost`/`ps_framing`. Flagged, not fixed. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S130. Syndicate acquires a blank Accord form covertly — outside STD.CA.9 channels. Paired with SYN.MOD.11 Signature on File to produce a non-negotiable unilateral Accord. Closes 04-n125 (Option C: formation capability).*

```python
SYN.CA.12 = Card(
    card_id      = "SYN.CA.12",
    version      = "v0.1",
    name         = "Boilerplate",
    tagline      = "The terms were settled before you sat down.",
    type         = CovertOperation,
    subtype      = FactionSpecific,
    faction      = Syndicate,

    layer        = Economy,
    function     = Add,
    subject      = AccordForm,

    beat         = 3,
    resolution   = Automatic,
    threshold    = None,
    ring_mod     = None,
    doctrine_mod = None,
    value_rating = None,  # scaffolded, not addressed

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = Capital(1) + Mandate(1),

    success     = arbiter.deliver(AccordForm(state=blank), recipient=faction(Syndicate).case),
    successcrit = None,
    fail        = None,
    failcrit    = None,
    on_accept   = None,
    on_decline  = None,

    persistence           = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    portrait = {Syndicate: PortraitEntry(flat=+1)},

    narrative    = None,
    perspectives = None,
    design_note  = "Covert form acquisition — distinct from STD.CA.9 which routes through public Accord channels. Syndicate obtains a blank form privately; fills it in and deploys at Debrief on their own terms, without signaling intent beforehand. Cross-resource cost: Capital×1 (Syndicate native — the commercial motivation) + Mandate×1 (institutional access required to obtain the form — Directorate's procedural domain). Pairs with SYN.MOD.11 Signature on File: Boilerplate provides the form; Signature on File forces acceptance. Closes 04-n125 parasitic posture gap — Syndicate now has Accord-formation capability.",
    arbiter_note = "On success: retrieve one blank Accord form from supply and place it in Syndicate's dispatch case. Syndicate may fill it in and table it at Debrief (Art 06 §9). Covert — do not announce delivery.",
)
```

---

### Syndicate — Public Acts
[↑ Syndicate](#syndicate)

| Card | Name |
|------|------|
| [SYN.PA.1](#p15-acquisition-offer) | Acquisition Offer |
| [SYN.PA.2](#p16-public-dividend) | Public Dividend |
| [SYN.PA.3](#syn-pa-3--data-acquisition) | Data Acquisition |

### SYN.PA.1 — ACQUISITION OFFER
[↑ Public Acts](#syndicate-public-acts)

#### Design Rationale
Syndicate's public territorial acquisition PA — the counterpart to SYN.CA.3 Hostile Acquisition (which is covert and forcible). This card asks first. Scaling: 2 Capital per presence token acquired (n declared at Phase B). Cost scales with the position being purchased: 2 tokens at Established = 4 Capital; 6 tokens at full Dominant = 12 Capital. The offer fee (1 Capital at Phase B) is non-refundable regardless of outcome — the cost of making a public offer. The balance payment (2n Capital) is conditional on acceptance and paid at Beat 4 cleanup. On refusal, Syndicate gains the PS advantage of having made a good-faith offer publicly.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public buyout offers are core Syndicate doctrine — acquire, not take | Art 00 §7 |
| Voice fit | ✓ | Syndicate on-doctrine; Network (aligned): public offer creates public record; Guild (opposed): presence is built, not bought | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Syndicate acquire-not-take doctrine: public offer before forced action. Scaling cost (n × 2 Capital) rewards the target. PS on decline (+1 Syndicate, −1 target) incentivizes acceptance. Portrait +1. Legitimizes acquisition mode vs SYN.CA.3 Hostile's coercive mode | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Syndicate) / ElectPlayer | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Redirect / PresenceToken | Art 04b §4 |
| Balance | ✓ | 1 Capital offer fee (non-refundable) + 2n conditional. Scaling cost makes Dominant buyout expensive (12 Capital). Beat 4 resolution (not Debrief) | Art 02 §6–§7 |
| Effect duration | ✓ | PresenceToken transfer is immediate at Beat 4 acceptance; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card resolved at Beat 4; no game-state marker persists | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Syndicate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid; restriction checks target's Established+ in district (valid zone condition) | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); Capital cost + conditional payment (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Target decides at Beat 4 (not Debrief); token/Capital transfer at Beat 4 cleanup | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`, `outcome_type = ElectPlayer` — `on_accept`/`on_decline` both populated (`success`/`successcrit`/`fail`/`failcrit` correctly `None` for this outcome type), no `game.choose_one()`. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Capital), correctly typed — offer fee mono, balance payment also mono. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
SYN.PA.1 = Card(
    id      = "SYN.PA.1",  card_id = "SYN.PA.1",  version="v1.0",
    name    = "Acquisition Offer",
    tagline = "Publicly offer to purchase another faction's presence position in a district.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,

    layer    = Territory,  function = Redirect,  subject = PresenceToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = None,  # scaffolded, not addressed
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = ElectPlayer,  # target accepts or declines at Beat 4
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(target).influence_tier(target_district) >= Established,
    # declared at Phase B: target faction, district, token count (n)
    cost = resource.faction(Syndicate).capital * 1,  # offer fee; non-refundable regardless of outcome
    boost = None,

    success     = None,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    # ElectPlayer — target faction publicly accepts or declines at Beat 4
    on_accept  = (
        district(target_district).faction(target).presence -= n,
        district(target_district).faction(Syndicate).presence += n,
        faction(target).resource(capital) += (2 * n),  # balance payment from Syndicate
        faction(Syndicate).standing += 1,
        faction(target).standing += 1,
    ),
    on_decline = (
        faction(Syndicate).standing += 1,
        faction(target).standing -= 1,
    ),

    portrait = {Syndicate: PortraitEntry(submitter=+1)},
    ps_framing = None,

    narrative    = "Syndicate does not take what it can buy. The offer is always made first. What the other faction does with it is their business.",
    perspectives = {
        Syndicate: "This is the formal mechanism. We are not here to take — we are here to acquire. The distinction matters.",
        Network:   "Syndicate makes the offer at The Table where everyone watches. Whatever the target decides, their answer is on the record. That is also useful to us.",  # aligned
        Guild:     "Syndicate offers Capital for positions Guild built through construction and sustained through presence. We did not build it to sell. That is not a position the offer changes.",  # opposed
    },
    design_note  = "Public counterpart to SYN.CA.3 Hostile Acquisition. 1 Capital offer fee non-refundable. Balance payment (2n Capital) conditional on acceptance, paid at Beat 4. Scaling: n=2 (Established min) = 4 Capital; n=6 (Dominant max) = 12 Capital. On accept: both PS +1. On decline: Syndicate +1, target −1. Beat 4 resolution — not Debrief.",
    arbiter_note = "Phase B: Syndicate names target faction, district, token count (n). 1 Capital offer fee committed. Beat 0: restriction check (target Established+). Beat 4: target faction publicly accepts or declines. On accept: transfer n presence tokens from target to Syndicate; Syndicate pays 2n Capital to target from supply; both +1 PS. On decline: Syndicate +1 PS, target −1 PS. Offer fee (1 Capital) is not returned in either case.",
)
```

---

### SYN.PA.2 — PUBLIC DIVIDEND
[↑ Public Acts](#syndicate-public-acts)

#### Design Rationale
Syndicate's political leverage PA. Places a Capital-valued marker on a named district. At next Upkeep Step 5, whoever holds Dominant in that district receives the Capital. Syndicate pre-commits 2 Capital (physically placed under the marker as escrow) and gains PS +1 at Beat 4. The card creates a persistent incentive structure that shapes table behavior without Syndicate taking direct action: factions will fight over Dominant in that district because there's Capital to claim. Syndicate may voluntarily withdraw the marker by paying 1 Mandate (removing the incentive, a diplomatic instrument). Persistence = Seasonal (marker stays until claimed or Quarter end).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Capital-as-political-leverage is core Syndicate doctrine | Art 00 §7 |
| Voice fit | ✓ | Syndicate on-doctrine; Ghost (aligned): deferred mechanism patience; Directorate (opposed): unregulated shadow investment | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Capital-as-leverage: 2 Capital escrow shapes table behavior without direct action. PS +1 at Beat 4. Voluntary withdrawal (1 Mandate) as diplomatic instrument. Portfolio +1: submitter-bounded | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Syndicate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Add / NativeResource (deferred, conditional on Dominant at Upkeep) — note: payout resource is Capital; subject label may need schema pass clarification | Art 04b §4 |
| Balance | ✓ | 2 Capital cost + PS +1; 2 Capital at risk if another faction claims Dominant. Maximum loss: 2 Capital + 1 Mandate (withdrawal) | Art 02 §6–§7 |
| Effect duration | ✓ | DividendMarker payout at Upkeep Step 5 — within-Quarter. Seasonal persistence. Phase 21 escrow return if unclaimed. No multi-Quarter effect | Art 04 §5 P19 |
| Persistence | ✓ | Seasonal — DividendMarker stays on district until claimed at Upkeep, withdrawn, or Phase 21 | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Syndicate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone; DividendMarker placed on district (valid zone-based component placement) | Art 01 §6–§7 |
| Supported by components | ⚠ | DividendMarker is a new component — register in Art 02 before production | Art 02 |
| Supported by game procedure | ⚠ | DividendMarker is a new component — register in Art 02. Upkeep Step 5 procedure needs amendment to handle marker resolution | Art 03 §11; Art 02 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`; only `success` populated (a `game.world_condition()` placement, matching the confirmed Seasonal-timed-effect pattern in design_reference_card_system.md) — no `game.choose_one()`. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Capital × 2), correctly typed. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
SYN.PA.2 = Card(
    id      = "SYN.PA.2",  card_id = "SYN.PA.2",  version="v1.0",
    name    = "Public Dividend",
    tagline = "Declare a public capital investment in a district — rewarding whoever holds Dominance at next Upkeep.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,

    layer    = Economy,  function = Add,  subject = NativeResource,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = None,  # scaffolded, not addressed
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Seasonal,  # DividendMarker stays on district until claimed, withdrawn, or Phase 21
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,  # dynamic — whoever holds Dominant at next Upkeep
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = resource.faction(Syndicate).capital * 2,  # placed as escrow under DividendMarker
    boost       = None,

    success = (
        arbiter.place(DividendMarker(value=2, resource=Capital, district=target_district)),
        faction(Syndicate).standing += 1,
        game.world_condition(
            scope    = district(target_district),
            effect   = faction(district(target_district).dominant).resource(Capital) += 2,
            duration = Seasonal,
            trigger  = game.phase == Upkeep,
            clear_on = DividendMarker(district=target_district).claimed == True OR game.phase == EndOfQuarter,
        ),
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Syndicate: PortraitEntry(submitter=+1)},
    ps_framing = None,

    narrative    = "Syndicate backs positions, not factions. The investment is in the district. The winner claims it.",
    perspectives = {
        Syndicate:   "We do not choose who collects. We choose where the capital sits. That is sufficient leverage.",
        Ghost:       "Syndicate places the incentive and removes themselves from the contest. The district will spend three months fighting over two Capital. We understand the patience required to let mechanisms run.",  # aligned
        Directorate: "Syndicate places two Capital in a district and calls it public investment. The Directorate notes there is no permit, no declared ownership, and no regulatory oversight on what the marker represents.",  # opposed
    },
    design_note  = "Persistent economic leverage PA. 2 Capital placed as physical escrow under DividendMarker on district. At next Upkeep Step 5: Dominant faction claims it. If no Dominant (Contested or all Absent): marker stays, recheck next Upkeep. Quarter end: Syndicate recovers unclaimed escrow. Voluntary withdrawal: 1 Mandate public declaration. DividendMarker is a new component — Art 02 registration required.",
    arbiter_note = "Beat 4: place DividendMarker on district with 2 Capital tokens as physical escrow. Syndicate +1 PS. At each Upkeep Step 5 while marker present: check for Dominant in district. If Dominant: transfer 2 Capital to that faction; remove marker. If Contested or Absent: marker remains for next Upkeep. Phase 21: return unclaimed escrow to Syndicate. Voluntary withdrawal: Syndicate declares to ARBITER, pays 1 Mandate; escrow returned.",
)
```

---

### SYN.PA.3 — DATA ACQUISITION
[↑ Public Acts](#syndicate-public-acts)

#### Design Rationale
Syndicate publicly demands a target faction's Intel Token count and offers to purchase them. The demand is a guess — N is committed at Art 03 §9.2 Public Declaration. ElectPlayer resolves publicly at Beat 4 — target faction responds at the table. Three resolution paths: (1) trade — N tokens transfer to Syndicate, card discards; (2) show — target reveals all held tokens face-down (count public, content private), no transfer, card discards; (3) decline — no reveal, no trade, Syndicate −2 PS, card becomes Permanent. As Permanent, the card acts as a standing React: the first time target faction places a PA with a non-blank Target Profile at Art 03 §9.2, Syndicate replaces that Target Profile with one they fill in, then card discards. If target avoids targeted PAs for the rest of the Quarter, the card expires — the threat IS the constraint. Verbal offer is unenforceable; the coercive frame is intentional: this is extortion with a commercial label.

Narrative logic for the decline effect: declining a Syndicate offer in public does not end the relationship — it shifts the leverage. The Syndicate has already demonstrated they know approximately what the target is holding. Refusing to deal signals that the intel position is worth protecting. Syndicate's response: *fine — then we determine how you use it publicly.* The next targeted public act belongs to them. "Control comes from positioning early" — the decline transfers that positioning from the information layer to the target's submission layer.

#### Card Story
A Syndicate representative rises at Beat 4 and addresses the table: "We believe you hold [N] intelligence assets. We are prepared to acquire them at our stated consideration. You may accept our terms, demonstrate you cannot meet them, or decline." The table waits for the answer.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public coercion for intel count disclosure; fills Information\|Reveal\|IntelTokensHeld Syndicate gap; distinct from covert intel gathering (GHO.CA.x); PA-layer — act is the declaration, not the knowledge | Art 00 §7 |
| Voice fit | ✓ | FactionSpecific Syndicate; full perspectives block; verbal offer framing is on-voice | Art 00 §7 |
| Doctrine alignment | ✓ | Syndicate only; Capital(1) cost; intel count as transactional commodity; "control comes from positioning early" — Permanent React transfers positional leverage on decline | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Syndicate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/IntelTokensHeld — surfacing private count via public ElectPlayer; count is information content (not token board position = Economy) | Art 04b §4, §5 |
| Balance | ⚠ | Permanent React potency (PA Target Profile corruption) untested — flag for doctrine review | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent on decline path; accept/cannot-meet paths discard at Beat 4; React fires once then card discards; Quarter-end expiry if React never fires | — |
| Persistence | ✓ | Permanent model applied correctly; persistence_condition clear; card-as-condition sits in Syndicate PA area face-up | Art 04 §6 |
| Trigger validity | ✓ | React trigger: PA with non-blank Target Profile placed at Art 03 §9.2 Public Declaration — publicly observable (P5) | Art 04 §5 P5 |
| Portrait validity | ⚠ | All three entries use `flat=` — Syndicate's own included. Checked against the established `flat=`-misuse pattern: this card's actor is fully public (not covert), so it doesn't fit hypothesis C's "public-effect/covert-actor" shape, but it does fit the plainer original angle — `flat=` on the *submitter's own* entry where `submitter=` looks like the semantically correct field (SYN.CA.7/10/11/12's pattern), plus `flat=` on Network/Directorate who never acted at all, only reacted narratively. 3 more confirmed instances of this pattern. | Art 04 §6.2 |
| Supported by zones | ✓ | Faction Resolution Grid (Art 01/02); faction terminal (Intel Tokens held behind screen — faction-private) | Art 01 §6–§7 |
| Supported by components | ✓ | Intel Token (Art 02 §9); Target Profile with declared-parameters line (Art 02 v2.4 — S111); Faction Resolution Grid (Art 02 §5) | Art 02 §5, §8, §9 |
| Supported by game procedure | ✓ | Beat 4 ElectPlayer: publicly resolved at table — target declares trade, show, or decline openly; standard PA resolution (Art 03 §9.4). React framework (Art 03 §18) covers Permanent persistence_effect; table enforces React timing; no new procedure needed | Art 03 §9.4; §18 |
| Data schema validation | ✓ | All fields populated per §6.1/§6.2 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story present | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Three paths (accept / cannot-meet / decline) — each has exactly one outcome; no branching within paths; Permanent React fires once then discards | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Capital × 1, offer fee), correctly floor-power for a card whose real leverage is the ElectPlayer/Permanent-React mechanism, not the cost. Cost notation `Capital(1)` is the bare `Type(n)` style, a 4th confirmed instance alongside SYN.CA.10/11/12. | Art 00a §9.2 |

#### Outstanding Issues

- **Balance:** Permanent React effect (Target Profile replacement on next targeted PA) has no playtesting baseline. Monitor in doctrine review (04-n88).
- **Consideration non-fulfillment (design note — non-blocking):** Consideration is a verbal offer written on the TP declared-parameters line; it is not held in escrow. If Syndicate cannot deliver at sub-case A, the exchange fails and the card stays Permanent. Bluff mechanic is intentional — Syndicate bears public failure risk. Ruling: sub-case A fails → card stays Permanent (L234).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ | |

*v0.1 — S111: new card, fills Information\|Reveal\|IntelTokensHeld gap. Permanent React model. Issues Resolved pending doctrine review (04-n88).*

```python
SYN.PA.3 = Card(
    card_id      = "SYN.PA.3",
    version  = "v0.1",
    name     = "Data Acquisition",
    tagline  = "We know approximately what you're holding. We're giving you the chance to make this a transaction.",
    type     = PublicAct,
    subtype  = FactionSpecific,
    faction  = Syndicate,

    layer    = Information,
    function = Reveal,
    subject  = IntelTokensHeld,

    beat         = 4,
    resolution   = Automatic,
    threshold    = None,
    ring_mod     = None,
    doctrine_mod = None,
    value_rating = None,  # scaffolded, not addressed
    outcome_type = ElectPlayer,

    target_district = None,
    target_faction  = faction(any, not=Syndicate),
    target_object   = IntelTokensHeld(count=N_declared),
    declared_params = (
        N             = int,                         # tokens requested
        consideration = verbaloffer(faction(acting)), # free-text: Capital | ModifierCard(named) | any combination
        # both written on TP declared-parameters line at Art 03 §9.2 Public Declaration
    ),

    affinity    = None,
    restriction = None,
    cost        = Capital(1),
    boost       = None,

    on_accept  = (
        # sub-case A — trade: bilateral exchange
        consideration.move(faction(acting), faction(target)),          # Syndicate pays
        IntelToken(N_declared).move(faction(target).terminal,
                                    faction(acting).terminal),         # target pays
        # if Syndicate cannot fulfill consideration: exchange fails; card stays Permanent
        # card → PA discard only if both transfers complete

        # sub-case B — show: target voluntarily reveals all held Intel Tokens face-down;
        # count visible, content private; no transfer; tokens returned to terminal
        # card → PA discard (information goal met)
    ),

    on_decline = faction(acting).standing -= 2,
    # full refusal — no reveal, no trade; card → Permanent; stays in Syndicate PA area

    persistence           = Permanent,
    persistence_condition = NOT (Quarter.ended OR react_fired OR terms_accepted),
    # applies on decline path only; sub-case A (completed) and sub-case B both discard at Beat 4
    # terms_accepted: target completes trade OR reveals all tokens face-down (count public)
    # at any point while card is active — either clears card

    persistence_effect    = React(
        trigger = faction(target).PA(target_profile != None).placed_at("Art 03 §9.2.0"),
        effect  = target_profile.replace(Syndicate.written),
        on_fire = SYN_PA_3 → faction_PA_discard,
    ),
    # While Permanent: when target faction places any PA with non-blank Target Profile
    # at Art 03 §9.2 Public Declaration (Art 03 §9.2.0), card fires as React — Syndicate immediately
    # replaces that Target Profile with one they fill in. SYN.PA.3 → PA discard.
    # Table enforces; no ARBITER tracking required.
    # If target submits no PA with Target Profile this Quarter: card expires Quarter end.
    # PAs without Target Profile (e.g., Floor Act) do not trigger — React does not fire.

    portrait = {
        Syndicate:   PortraitEntry(flat=+1),
        Network:     PortraitEntry(flat=-1),
        Directorate: PortraitEntry(flat=-1),
    },
    ps_framing = None,

    narrative = "The offer is made in public, which is unusual for the Syndicate. They prefer quiet transactions. This one is designed to be loud.",

    perspectives = {
        Syndicate:   "Intelligence is a commodity. We're establishing the market price and giving them the chance to sell at it.",
        Ghost:       "The offer is a probe. The response — whatever form it takes — is the data.",
        Network:     "This is how private information becomes public leverage. This is exactly what we exist to counter.",
        Directorate: "A public extortion offer dressed as commerce. We note the terms and the response.",
        Guild:       "Whatever they're buying, they think they need it. That tells us something about their position.",
    },

    design_note  = "Three resolution paths at Beat 4 ElectPlayer: (1) trade — bilateral exchange: consideration moves Syndicate→target, N tokens move target→Syndicate; card discards only if both transfers complete; (2) show — target reveals all held tokens face-down (count public, content private), no transfer, card discards — information goal met; (3) decline — no reveal, no trade, Syndicate −2 PS, card becomes Permanent. Sub-cases 1 (completed) and 2 both satisfy the card; only 3 triggers the stake. Non-fulfillment edge case (sub-case A, Syndicate cannot deliver consideration): exchange fails; card stays Permanent — Syndicate set the terms and failed to meet them. Bluff mechanic is intentional: consideration is a verbal offer written on TP declared-parameters line, not held in escrow; Syndicate bears public failure risk. Show path: target voluntarily reveals count — not compelled, consistent with GR 10.1 (ElectPlayer creates stake; choice is player's). PERMANENT PHASE is fully table-enforced: card is face-up in Syndicate PA area; table observes when target places a PA with Target Profile at Art 03 §9.2.0 and allows Syndicate to replace it (React); table observes if target accepts at any point (trade or show) and card is cleared. No ARBITER involvement required at any stage — Beat 4 ElectPlayer is public; Permanent card is table-enforced. Target may accept at any time to clear the card. Threat is the constraint: target must deal with Syndicate or avoid targeted PAs for the rest of the Quarter. N and consideration declared at Art 03 §9.2 on TP declared-parameters line (Art 02 v2.4).",
    arbiter_note = None,
)
```

---

---

---

---

### SYN.PA.4 — CHARITY GALA *(stub)*
[↑ Public Acts](#syndicate-public-acts)

#### Design Rationale
⚠ Pending design review (09-16). See stub design note below.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public wealth display forcing table-wide reaction fits Syndicate's Capital-as-leverage doctrine | Art 00 §7 |
| Voice fit | ⚠ | No `narrative`/`perspectives` fields at all | Art 00 §7 |
| Doctrine alignment | ✓ | Weaponizing Capital for PR is maximally on-doctrine for Syndicate | Art 00 §7 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Syndicate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Standing / Shift / StandingMarker — matches `card_status` DB directly | Art 04b §4 |
| Balance | ⚠ | Cost set, but the table-wide "every opponent pays or loses PS" effect has no bound or per-faction structure to assess magnitude against | Art 02 §6–§7 |
| Effect duration | ⚠ | No `persistence` field declared at all | Art 04 §5 P19 |
| Persistence | ⚠ | Same gap — field absent | Art 04 §6 |
| Trigger validity | ✓ | No trigger field; Automatic doesn't require one | — |
| Portrait validity | ⚠ | No `portrait` field at all | Art 04 §6.2 |
| Supported by zones | ✓ | No district reference — table-wide effect, correctly no zone dependency | Art 01 §6–§7 |
| Supported by components | ✓ | Public Standing track, Capital — existing components | Art 02 §7–§8 |
| Supported by game procedure | ⚠ | "Every opponent must either pay or lose PS" is a simultaneous table-wide forced choice with no defined resolution order or procedure — new ARBITER-facing behavior, same category as other unconfirmed-procedure gaps flagged elsewhere in this review | Art 03 §9 |
| Data schema validation | ⚠ | `success` is a bare prose string, same defect shape flagged elsewhere in this review. Missing entirely: `outcome_type`, `ring_mod`/`doctrine_mod`/`trigger`/`resolution_type`, `persistence`, targeting fields, `restriction`, `boost`, `successcrit`/`fail`/`failcrit`, `card_id`, `arbiter_note`. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block | Art 04 §5 P26 |
| Outcome determinacy | ⚠ | No structured success/fail split to check against P27 | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Capital × 2), correctly typed. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
SYN.PA.4 = Card(
    id      = "SYN.PA.4",  card_id = "SYN.PA.4",  version = "v1.0",
    name    = "Charity Gala",
    tagline = "A massive display of wealth that forces rivals to pay up or lose face.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Standing,  function = Shift,  subject = StandingMarker,
    beat    = 4,  resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,  trigger = None,
    value_rating = None,  # scaffolded, not addressed
    resolution_type = "Transactional",  outcome_type = None,  # scaffolded, not addressed
    persistence = Immediate,  # scaffolded, not addressed
    persistence_condition = None,  persistence_effect = None,
    target_district = None,  target_faction = None,  target_object = None,  target_taxonomy = None,
    affinity = None,  restriction = None,
    cost    = resource.faction(Syndicate).capital * 2,
    boost   = None,
    success = "Syndicate gains +2 PS. Every opponent must either pay 1 Capital to the supply or immediately lose 1 PS.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept = None,  on_decline = None,
    portrait = {},  # scaffolded, not addressed
    ps_framing = None,
    narrative = None,  perspectives = None,
    design_note = "A public flex of pure capital. Weaponizes Syndicate's wealth to farm PR while forcing opponents to bleed money or take a PR hit just to keep up appearances.",
    arbiter_note = None,
)
```

---

### SYN.PA.5 — PROTECTION RACKET *(stub)*
[↑ Public Acts](#syndicate-public-acts)

#### Design Rationale
⚠ Pending design review (09-16). See stub design note below.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Capital-toll extortion on district development is grounded in Syndicate's leverage doctrine | Art 00 §7 |
| Voice fit | ⚠ | No `narrative`/`perspectives` fields at all | Art 00 §7 |
| Doctrine alignment | ✓ | On-doctrine — Capital positioned as a toll on others' physical expansion | Art 00 §7 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Syndicate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Remove / StructureBlock — matches `card_status` DB directly | Art 04b §4 |
| Balance | ⚠ | Cost set, but the standing toll's actual power (removal threat on any placement) can't be assessed without a structured, bounded effect | Art 02 §6–§7 |
| Effect duration | ⚠ | `persistence = Transient`, but the prose describes the effect lasting "until Quarter+1" — into the *next* Quarter. Same tension as DIR.PA.7 Curfew: a Transient effect (within-Quarter per Art 04 §5's duration discipline) described in prose as spanning a Quarter boundary. Second confirmed instance of this exact tension — worth its own schema_cleanup_log entry now that it's recurred. | Art 04 §5 P19 |
| Persistence | ⚠ | See Effect duration — same tension | Art 04 §6 |
| Trigger validity | ⚠ | The described trigger ("whenever a Structure Block or Presence Token is placed here") maps toward confirmed TriggerExpr vocabulary (`structure_block.placed`/`presence_chip.placed`) but isn't expressed as one — prose inside `success`, same Card-as-Condition gap as GUI.PA.3/8 and DIR.PA.7 | Art 04 §6.3 |
| Portrait validity | ⚠ | No `portrait` field at all | Art 04 §6.2 |
| Supported by zones | ⚠ | No `target_district` field declared — referenced only inside `success` prose | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock, PresenceToken, Capital — existing components | Art 02 §6–§8 |
| Supported by game procedure | ⚠ | The pay-or-lose-asset reactive mechanism has no structured procedural home — same gap as Trigger validity above | Art 03 §9 |
| Data schema validation | ⚠ | `success` is a bare prose string describing what should be a `persistence_effect`, same defect shape flagged elsewhere in this review. Missing entirely: `outcome_type`, `ring_mod`/`doctrine_mod`/`trigger`/`resolution_type`, `target_district`/`target_faction`/`target_object`/`target_taxonomy`, `restriction`, `boost`, `successcrit`/`fail`/`failcrit`, `card_id`, `arbiter_note`. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block | Art 04 §5 P26 |
| Outcome determinacy | ⚠ | No structured success/fail split to check against P27 | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capital + Mandate), correctly typed. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
SYN.PA.5 = Card(
    id      = "SYN.PA.5",  card_id = "SYN.PA.5",  version = "v1.1",
    name    = "Protection Racket",
    tagline = "Publicly leverage capital to extort physical expansion.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Remove,  subject = StructureBlock,
    beat    = 4,  resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,  trigger = None,
    value_rating = None,  # scaffolded, not addressed
    resolution_type = "Transactional",  outcome_type = None,  # scaffolded, not addressed
    persistence = Transient,
    persistence_condition = None,  persistence_effect = None,  # see checklist: prose describes a reactive trigger not structured here
    target_district = district.named,  target_faction = None,  target_object = None,  target_taxonomy = None,
    affinity = None,  restriction = None,
    cost    = resource.faction(Syndicate).capital * 2 + resource.faction(Syndicate).mandate * 1,
    boost   = None,
    success = "Places a Standing Condition on target_district until Quarter+1: Whenever a Structure Block or Presence Token is placed here, the faction that owns it must pay 1 Capital to Syndicate. If they do not, the structure or token is immediately removed.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept = None,  on_decline = None,
    portrait = {},  # scaffolded, not addressed
    ps_framing = None,
    narrative = None,  perspectives = None,
    design_note = "Fixes the covert targeting issue. Physical placement of chips and blocks is public knowledge. Syndicate sets up a toll booth on the district: the owner of the structure pays, or their asset is destroyed.",
    arbiter_note = None,
)
```

### SYN.MOD.1 — THE FIXER

#### Design Rationale
The Fixer has never had a `Card()` definition — tracked only as a design placeholder through PM02 L241/L244/L245 and PM05 04-n154/04-n158/04-n172, briefly miscategorized as a 4th subclass before resolving to "Issued ModReactCard." 04-n158 (S133) set the constraint: The Fixer must corrupt a distinct, not-yet-described Accord field — explicitly not SYN.CA.10 Accord Transfer's Named Party, not SYN.CA.11 Redline's numeric/ordinal Terms, and must not duplicate SYN.MOD.11 Signature on File's forged-acceptance mechanic.

Art 06 §9.10 (Accord Manipulation) enumerates exactly four Alter sub-types: Terms (Redline's domain), Named Party (Accord Transfer's domain), Duration, and Term removal. Of these, Term removal — strike an entire clause row from an active Accord, voiding that obligation or prohibition outright — is the only one neither existing card touches; Duration's numeric fill-in nature sits close enough to Redline's own domain (Redline's design_note already gestures at "a Quarter deadline" as one of its fill-in value types) to make it a weaker candidate. Built here around Term removal, confirmed with Andy (S140): The Fixer doesn't alter a value or swap a party — it makes an inconvenient clause disappear entirely. Cost model mirrors SYN.MOD.11's leverage pattern (an IntelToken keyed to a named party), reflecting the same "we have something on you" throughline.

**Taxonomy re-check (S140, Andy: don't assume checklist entries are correct without verifying).** Function was first written as `Remove`, reasoned only as "not Corrupt, to avoid SYN.MOD.11/Redline's slot." Checking against the actual confirmed verb definitions (ref_taxonomy.md): Remove = "component exits active play to supply or off-board"; Corrupt = "a physically written or recorded value is altered." Striking one clause doesn't remove the AccordAgreement from play — the Accord stays active per §9.10 ("the Accord remains active after alteration"); what changes is written content on a component that stays in play, which is closer to Corrupt's actual definition than Remove's. The "avoid Corrupt to dodge overlap" reasoning doesn't hold up either: 04-n158's actual constraint was to avoid duplicating SYN.MOD.11/Redline's *mechanics* (forged acceptance / numeric value edit), not their taxonomy label — nothing requires a different Function tag. **Left as `Remove` for now, but flagged as a genuine judgment call, not a settled assignment** — same category of self-flagged ambiguity SYN.MOD.11 itself carries ("least-precedented assignment... flag for re-check").

**Open items, flagged not resolved this pass:** `generating_card` is undefined — no CA/PA has yet been identified that delivers this Issued card to a faction (tracked as its own outstanding item, not a blocker for authoring the card itself). Trigger form `accord.activated` is new and unconfirmed against §6.3 TriggerExpr vocabulary, same open category as Overture's `public_act.resolved` and SYN.MOD.11's `accord.tabled`. `TermRemoval` as a value for `.alter(type=...)` is likewise new — parallels Redline's `type=Terms` but has no formal AlterType enum backing it (same ungoverned-MutationExpr gap as the rest of the corpus).

#### Card Story
The clause that would have sunk the deal simply isn't on the page anymore. Nobody remembers negotiating it away — because nobody did.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Post-activation Accord sabotage — strikes a clause the moment the deal takes effect. Fits Syndicate's leverage-based interference doctrine. | Art 00 §7 |
| Voice fit | ⚠ | Perspectives TBD — deferred to modifier card voice pass (D-04-08); `narrative` line written this pass. | Art 00 §9 |
| Doctrine alignment | ✓ | Corrupting/removing Accord terms via leverage (keyed IntelToken) is squarely Syndicate's "we have something on everyone" doctrine — matches sibling cards SYN.MOD.11 and SYN.CA.11. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Issued `ModReactCard` — matches PM02 L245's resolution of this card's category; ARBITER-delivered, not deck-drawn. | Art 04 §6.1, §11.1; PM02 L245 |
| Taxonomy fit | ⚠ | **Downgraded on re-check (S140):** AccordAgreement is confirmed registered (Redline's precedent) and Remove is a confirmed verb, but Remove-vs-Corrupt is a genuine judgment call, not a settled fit — Corrupt's actual definition ("a physically written value is altered") arguably matches "void a clause" better than Remove's ("component exits active play"), since the AccordAgreement itself stays in play. Kept as Remove for now; flagged for re-check, same as SYN.MOD.11's own self-flagged assignment. | ref_taxonomy.md §5.2 |
| Balance | ✓ | `cost = Findings(1) + IntelToken(keyed_to=declared_party)` — lighter than Signature on File's 4-resource stack, appropriate since removing one clause is a smaller violation than forcing whole-Accord acceptance. New cost combination, playtest-flagged like the rest of the corpus's numeric values (04-n94 pattern), not re-litigated further. | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — the strike itself resolves instantly at trigger; the missing clause's absence persists for the remainder of the Accord's term, same durability pattern as Redline's in-place alteration. | Art 04 §5 P19 |
| Persistence | ⚠ | `persistence` field open corpus-wide question (schema_cleanup_log item 2/D), not card-specific. | Art 04 §6.2 |
| Trigger validity | ⚠ | `accord.activated` is a brand-new trigger form, unconfirmed against §6.3 TriggerExpr vocabulary — same open category as Overture's `public_act.resolved` and SYN.MOD.11's `accord.tabled`. | Art 04 §6.3; PM05 04-n158 |
| Portrait validity | ✓ | `{Syndicate: flat=+1}` — matches SYN.CA.11 Redline's portrait structure and magnitude for a comparable Accord-manipulation play. | Art 04 §6.2 |
| Supported by zones | ✓ | No district reference — correct, not a territory effect. | Art 01 §6–§7 |
| Supported by components | ✓ | AccordForm, IntelToken — existing components; no new components needed. | Art 02 §6, §11; Art 06 §9.2 |
| Supported by game procedure | ⚠ | Art 06 §9.10 defines Term removal at the rules level, but no Art 03 procedural pass yet describes exactly when in the sequence an Issued ModReactCard reacts to "Accord activation" — same category of gap as Overture's own flagged Art 07 subroutine pending item. | Art 06 §9.10; PM05 04-n158 |
| Data schema validation | ⚠ | Brand-new card (no prior `Card()` definition existed). `target_object.alter(type=TermRemoval, ...)` parallels Redline's `type=Terms` but `TermRemoval` has no formal AlterType enum backing it — same ungoverned-MutationExpr gap as the rest of the corpus. `generating_card=None` flagged as a separate, still-open item (not a blocker for this pass). Scaffolding fields added (04-n177). | Art 04 §6.1–§6.3; PM05 04-n158 |
| Card narrative | ✓ | Card Story and `narrative` line written this pass (card previously had no content at all). | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic` — deterministic leverage check (does Syndicate hold the right keyed IntelToken), no dice. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | `Findings(1) + IntelToken(keyed_to=declared_party)` — mirrors Signature on File's leverage-cost pattern at a lighter tier appropriate to the smaller violation. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ⚠ | Depends on Accord activation frequency plus Syndicate holding the right keyed IntelToken at the right moment — a fairly narrow combined condition; best-effort, not independently verifiable here. |  |
| Firing window (ModReactCard) | ✓ | No other card shares the `accord.activated` trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Deterministic leverage check, no dice — Automatic is correct. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open corpus-wide question: is a 2nd copy meaningful? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ (N/A) | `ring_constraint=None` — not a district/ring-scoped effect. |  |

#### Outstanding Issues
- **`generating_card` undefined:** No CA/PA has yet been identified that delivers The Fixer to a faction as an Issued card (PM05 04-n154/04-n172 history). Open item, not resolved this pass.
- **Trigger vocab — `accord.activated`:** New trigger form, not yet in confirmed TriggerExpr vocabulary (§6.3). Needs Art 03/06 timing confirmation, same category as Overture's and Signature on File's own flagged trigger gaps.
- **`TermRemoval` AlterType:** Used here as a value for `.alter(type=...)`, paralleling Redline's `type=Terms`, but there is no formal AlterType enum registered anywhere — Art 06 §9.10 names "Term removal" in prose only. Formalizing all four Alter sub-types (Terms/Term removal/Duration/Named Party) into a real enum is a whole-set schema item, not specific to this card.
- **Function `Remove` vs. `Corrupt` (new, S140):** Re-checked against ref_taxonomy.md's actual verb definitions — Corrupt ("a physically written value is altered") arguably fits "void one clause" better than Remove ("component exits active play"), since the AccordAgreement itself stays active. Kept as `Remove`; genuinely open, not a settled call.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (Taxonomy Remove/Corrupt, generating_card, trigger vocab, TermRemoval enum) |  |

```python
SYN.MOD.1 = Card(
    id      = "SYN.MOD.1",  card_id = "SYN.MOD.1",  version = "v1.0",
    name    = "The Fixer",
    tagline = "That clause was always going to be a problem. Now it isn't.",
    type    = ModReactCard,  faction = Syndicate,

    layer   = Information,  function = Remove,  subject = AccordAgreement,  # distinct from SYN.MOD.11 (Corrupt/forged acceptance) and SYN.CA.11 (Corrupt/altered value) — Art 06 §9.10's unclaimed "Term removal" Alter type: void a clause row outright, not alter or replace it

    trigger         = accord.activated,  # NEW trigger form, unconfirmed against §6.3 — fires the moment a drafted Accord becomes active, before its terms take hold. Same open category as Overture's public_act.resolved and SYN.MOD.11's accord.tabled
    beat            = None,
    ring_constraint = None,  ring_origin = None,  value_rating = None,
    resolution      = Automatic,  threshold = None,  resolution_type = "Transactional",  outcome_type = None,
    ring_mod        = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,  # clause removal doesn't require naming a party — the Accord document itself is the target
    target_object   = AccordAgreement(state=active, clause_declared=True),
    affinity        = None,
    restriction     = IntelToken(keyed_to=faction(accord.party_a)) in faction(Syndicate).hand
                       or IntelToken(keyed_to=faction(accord.party_b)) in faction(Syndicate).hand,
    cost            = Findings(1) + IntelToken(keyed_to=declared_party),
    boost           = None,

    acquisition      = Issued,
    generating_card  = None,  # UNDEFINED — no CA/PA yet identified that delivers The Fixer to a faction; open item, tracked separately (see Outstanding Issues), not resolved this pass

    success     = target_object.alter(type=TermRemoval, clause=declared_clause),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Syndicate: PortraitEntry(flat=+1)},
    ps_framing   = None,
    narrative    = "The clause never existed. Neither did the conversation about removing it.",
    perspectives = None,
    design_note  = "Redesigned/authored from scratch S140 per 04-n158 — must be distinct from SYN.CA.10 Accord Transfer (Named Party) and SYN.CA.11 Redline (Terms/numeric value), and must not duplicate SYN.MOD.11 Signature on File (forged acceptance). Built around Art 06 §9.10's fourth and, at the time of this pass, only unclaimed Accord Manipulation type: Term removal — strike an entire clause row from an active Accord, voiding that obligation or prohibition outright. Distinct from Redline (edits a value in place) and Accord Transfer (swaps a bound party): The Fixer deletes the term itself. Leverage cost pattern mirrors Signature on File (IntelToken keyed to a named party), reflecting the same 'we have something on you' Syndicate throughline, while layer/function (Information/Remove) keeps it out of SYN.MOD.11's Information/Corrupt/Accord slot. Confirmed with Andy (S140): build around Term removal.",
    arbiter_note = "On trigger (a drafted Accord becomes active): if Syndicate holds an IntelToken keyed to either named party and pays Findings(1) + that IntelToken: Syndicate declares one clause row on the AccordForm. ARBITER strikes that row; the obligation or prohibition it recorded is void for the remainder of the Accord's term. Remaining clause rows are unaffected (Art 06 §9.10).",
)
```

---

### SYN.MOD.2 — SHELL CORPORATION

#### Design Rationale
First of the SYN.MOD.2/3 Accord-lifecycle income family — fires on Accord formation, no self-fire ambiguity (`accord.placed` isn't faction-scoped). Design_note explicitly contrasts with DIR.MOD.4 (same trigger, different resource) — a deliberate "competing institutional reactions to the same event" pattern, not a redundant duplicate.

#### Card Story
A formal Accord goes up at the table. Syndicate didn't need to be a party to it — the paperwork itself is a market signal, and there's already a shell entity positioned to profit from it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "Economic positioning without needing to be invited" is a clean, doctrinally central Syndicate beat. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1 — correctly expresses doctrine. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Syndicate, real taxonomy (Economy/Add/NativeResource, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy×Add valid per the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Flat, low-value (+1), no cost, table-wide trigger — plausible as a minor engine; final read pending 04-n178. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `accord.placed` — confirmed vocabulary, publicly observable, no faction-scoping ambiguity. | Art 04 §6.3 |
| Portrait validity | ✓ | Submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; Accords have no district dimension. | Art 01 §6–7 |
| Supported by components | ✓ | Standard resource-grant mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing Accord-formation event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set gate as the rest of the corpus. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ⚠ | Entirely dependent on Accord-formation rate, player-driven — same variability flag as DIR.MOD.4 (same trigger). |  |
| Firing window (ModReactCard) | ✓ | No other Syndicate card shares this exact trigger (SYN.MOD.3/7 key off different Accord events — removed/corrupted, not placed). |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat administrative windfall, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; Accords aren't ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. React on Accord formation. Every formal deal creates economic opportunity — Syndicate positions inside it immediately. Pairs with SYN.MOD.3 (Offshore Slush Fund on accord.corrupted). S138: full content-review pass — clean, no new issues beyond the standard schema/cost/stack gaps. Design Pass ✓, Issues Resolved not yet.*

```python
SYN.MOD.2 = Card(
    id      = "SYN.MOD.2",  card_id = "SYN.MOD.2",  version = "v0.1",
    name    = "Shell Corporation",
    tagline = "Every Accord is a market event. Syndicate responds accordingly.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = Economy,  function = Add,  subject = NativeResource,  # assigned S137 (04-n175) — resources.add(1, Capital)

    trigger         = accord.placed,
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = faction(Syndicate).resources.add(1, Capital),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Syndicate: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Accord formation React. Every new Accord at The Table generates 1 Capital for Syndicate — the economic positioning happens before Syndicate is even a party. Delivers §5a 'accord manipulation' at the modifier level: Syndicate doesn't need to be invited to benefit from diplomatic activity. Compare DIR.MOD.4: DIR earns Mandate from the same trigger; SYN earns Capital. Competing institutional reactions to the same event.",
    arbiter_note = None,
)
```

---

### SYN.MOD.3 — OFFSHORE SLUSH FUND

#### Design Rationale
Second card of the Accord-lifecycle family — fires on `accord.removed` (higher yield than SYN.MOD.2's formation trigger). Real open question, already admitted in the card's own design_note, not invented here: should `accord.removed` cover ANY Accord ending (breach or natural completion), or does the "breach creates leverage" framing in the trailing note actually require distinguishing the two? As specced, the card doesn't distinguish — it fires on any Accord removal.

#### Card Story
An Accord collapses — breach, expiry, doesn't matter which. Syndicate already had a clause routing capital out of the wreckage before anyone else finished reading the fine print.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Profiting from diplomatic breakdown is a coherent, doctrinally central Syndicate beat — positioning ahead of collapse. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("Syndicate had a clause for that") lands the doctrine. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1 — correctly expresses doctrine. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Syndicate, real taxonomy (Economy/Add/NativeResource, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Economy×Add cell as SYN.MOD.2. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Real, self-admitted open question: does breach-vs-completion need separate cards, or is a flat 2 Capital on any Accord ending correctly calibrated regardless of cause? Not resolved here. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `accord.removed` — confirmed vocabulary (design_note notes this was corrected from `corrupted` to align with Art 06 physical state — a good catch already made). | Art 04 §6.3 |
| Portrait validity | ✓ | Submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct. | Art 01 §6–7 |
| Supported by components | ✓ | Standard resource-grant mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing Accord-removal event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set gate as the rest of the corpus. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ⚠ | Dependent on Accord-ending rate, same variability as SYN.MOD.2. |  |
| Firing window (ModReactCard) | ✓ | No other Syndicate card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat yield, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. React on Accord breach. Syndicate extracts Capital from diplomatic breakdown. Higher yield than formation — breach creates leverage. Pairs with SYN.MOD.2. S138: full content-review pass — the card's own self-admitted breach-vs-completion question remains open, not resolved. Design Pass ✓, Issues Resolved not yet.*

```python
SYN.MOD.3 = Card(
    id      = "SYN.MOD.3",  card_id = "SYN.MOD.3",  version = "v0.1",
    name    = "Offshore Slush Fund",
    tagline = "When an Accord fails, Syndicate had a clause for that.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = Economy,  function = Add,  subject = NativeResource,  # assigned S137 (04-n175), same shape as SYN.MOD.2

    trigger         = accord.removed,
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = faction(Syndicate).resources.add(2, Capital),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Syndicate: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Accord removal React. 2 Capital yield. Trigger corrected from 'corrupted' to 'removed' to align with Art 06 physical game state. Open question for detail design: Should accord.removed be the sole condition (meaning Syndicate profits off ANY Accord ending, completed or breached), or is a separate mod card needed to distinguish breach vs completion?",
    arbiter_note = None,
)
```

---

### SYN.MOD.4 — INSIDER TRADING

#### Design Rationale
First of the SYN.MOD.4/5 market-speculation family — fires on an opponent's PS increase, explicitly `faction=opponent`-scoped, no self-fire ambiguity.

#### Card Story
A rival scores a public win — their standing climbs in front of the whole table. Syndicate was already positioned on the other side of that trade; the profit lands before the applause fades.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "Public success always creates private wealth" is a sharp, doctrinally coherent Syndicate hook. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; opportunistic market play, not a doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Syndicate, real taxonomy (Economy/Add/NativeResource, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Economy×Add cell as SYN.MOD.2/3. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Flat, low-value, no cost, table-wide (any opponent) — plausible as a minor engine; final read pending 04-n178. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `standing_marker.increased(faction=opponent)` — confirmed vocabulary, correctly scoped, no self-fire ambiguity. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; not a territory effect. | Art 01 §6–7 |
| Supported by components | ✓ | Standard resource-grant mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing PS-increase event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set gate as the rest of the corpus. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Any opponent's PS increase is a recurring event — moderate-to-common. |  |
| Firing window (ModReactCard) | ✓ | No other Syndicate card shares this exact trigger (SYN.MOD.5 is the negative-direction sibling, distinct event). |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat yield, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*Market speculation on positive faction momentum. S138: full content-review pass — clean, no new issues beyond the standard schema/cost/stack gaps. Design Pass ✓, Issues Resolved not yet.*

```python
SYN.MOD.4 = Card(
    id      = "SYN.MOD.4",  card_id = "SYN.MOD.4",  version = "v0.1",
    name    = "Insider Trading",
    tagline = "Public success always creates private wealth.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = Economy,  function = Add,  subject = NativeResource,  # assigned S137 (04-n175), same shape as SYN.MOD.2

    trigger         = standing_marker.increased(faction=opponent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = faction(Syndicate).resources.add(1, Capital),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Market speculation React. Syndicate bets on the political market. When someone else scores a massive PR victory, Syndicate quietly makes a fortune off the back of it.",
    arbiter_note = None,
)
```

---

### SYN.MOD.5 — SHORT SQUEEZE

#### Design Rationale
Negative-direction sibling of SYN.MOD.4 — same opponent-scoped, no-self-fire shape, but with a real cost this time. Cross-resource question: cost spans Capital (Syndicate-native) and Findings (Ghost's) — same pattern flagged repeatedly this session on other factions' cards.

#### Card Story
A rival's public standing craters. Syndicate doesn't wait for the dust to settle — the vulnerability was already priced in, and the position pays out the moment the numbers confirm it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "A reputation in freefall is an undervalued asset" completes a coherent MOD.4/MOD.5 pair covering both directions of political volatility. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable, same as SYN.MOD.4. | Art 04 §6.5 |
| Card type fit | ✓ | Same shape as SYN.MOD.4. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Economy×Add cell. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | Real cost (unlike SYN.MOD.4's free trigger) for the same yield — reasonable given design_note's framing that holding both cards "guarantees income from any volatility." | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `standing_marker.decreased(faction=opponent)` — confirmed vocabulary, correctly scoped. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct. | Art 01 §6–7 |
| Supported by components | ✓ | Standard resource-grant mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing PS-decrease event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Real cost specified, but spans Capital (native) and Findings (Ghost's) — same cross-resource-holding question flagged on several cards this session. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Any opponent's PS decrease is recurring — moderate-to-common. |  |
| Firing window (ModReactCard) | ✓ | No other Syndicate card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat yield, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*Market speculation on negative faction momentum. S138: full content-review pass — cross-resource cost flagged (Findings, not Syndicate-native); otherwise clean. Design Pass ✓, Issues Resolved not yet.*

```python
SYN.MOD.5 = Card(
    id      = "SYN.MOD.5",  card_id = "SYN.MOD.5",  version = "v0.1",
    name    = "Short Squeeze",
    tagline = "A reputation in freefall is just an undervalued asset.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = Economy,  function = Add,  subject = NativeResource,  # assigned S137 (04-n175), same shape as SYN.MOD.2

    trigger         = standing_marker.decreased(faction=opponent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Syndicate).capital * 2 + resource.faction(Syndicate).findings * 1,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = faction(Syndicate).resources.add(1, Capital),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Companion to SYN.MOD.4. Syndicate profits off the downfall of other factions. By holding both MOD.4 and MOD.5, Syndicate guarantees income from any major political volatility at the table Cost reasoning: Findings identify the target's financial vulnerabilities before Capital is deployed to crush them.",
    arbiter_note = None,
)
```

---

### SYN.MOD.6 — BOUNTY CONTRACT

#### Design Rationale
Transactional-warfare React: Syndicate escrows Capital on a named opponent's PA, paying out only if it succeeds — the submitting faction effectively becomes Syndicate's mercenary. Two known issues, both already flagged (04-n175/schema_cleanup_log.md item 2), re-confirmed here not fixed: (1) `success` is a prose string, not a real MutationExpr. (2) The clearing logic for the Seasonal standing condition (Capital transfers when the target PA resolves, either direction) is buried inside that same prose string rather than expressed via `persistence_condition`/`persistence_effect` — this card is one of the 4 named examples in the still-open schema question about how to encode "what ends a standing condition" (item 2/B), alongside GUI.MOD.10, NET.MOD.13-adjacent cases, and DIR.MOD.9.

#### Card Story
Someone's about to make a move Syndicate wants to see succeed — or fail. Either way, there's Capital already on the table, waiting on the outcome, and the faction taking the action doesn't need to know whose money it is.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "Crowdsourcing other factions' offense/defense via escrowed capital" is a sharply doctrinal Syndicate mechanic — mercenary incentive, not direct action. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("I am willing to subsidize the effort") lands the doctrine. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; covert financial mechanism, not a public doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Syndicate, real taxonomy (Submission/Modify/PublicAct, 04-n175, Andy-confirmed as positive-direction sibling of SYN.MOD.10/STD.MOD.103/DIR.MOD.6). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Submission×Modify valid per the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | +20 boost is significant; escrow-and-payout structure is a novel, interesting risk-sharing mechanic, but hard to fully assess while the effect is a prose description rather than a formal expression. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | `persistence=Seasonal` correctly typed for a standing condition that must survive until the target PA resolves. | Art 04 §5 P19 |
| Persistence | ⚠ **(known gap, item 2/B)** | `persistence_condition`/`persistence_effect` both `None` — the actual clearing logic (Capital transfers on target PA resolution, either direction) is described only in prose inside `success`. Re-confirmed as one of the 4 named examples in the still-open schema question. | Art 04 §6.2; schema_cleanup_log.md item 2 |
| Trigger validity | ✓ | `public_act.placed_on_frg(faction=opponent)` — confirmed vocabulary, correctly scoped. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; not a territory effect. | Art 01 §6–7 |
| Supported by components | ⚠ | The "escrowed Capital on the card" mechanism has no defined component-level representation — tied to the same Persistence gap above. | Art 02 §6–8 |
| Supported by game procedure | ⚠ | Same gap — no formal Art 03 procedure step currently reads this card's escrow-and-payout condition at Beat 4; the `arbiter_note` prose describes intent but isn't backed by a defined procedure. | Art 03; GR 6.1 |
| Data schema validation | ⚠ **(known issue)** | `success` is a string literal, not a real MutationExpr — re-confirmed, not fixed. Scaffolding added this session for the fields that were simply absent. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ | The escrow-and-payout structure genuinely branches on the target PA's own outcome — legitimate design, but can't be verified as schema-compliant while it's prose, not a real conditional Expr. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` for the card itself — the 2 Capital is escrowed as part of the effect, not a card cost. Same whole-set gate applies to the card-level `cost` field. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Any opponent PA placement — common, moderate-to-high frequency. |  |
| Firing window (ModReactCard) | ✓ | No other Syndicate card shares this exact trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Automatic is appropriate — the escrow condition, not the card's own resolution, carries the uncertainty. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus, compounded by the unresolved persistence-condition gap. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*Syndicate weaponizes other factions by crowdsourcing their own defense or offense. Taxonomy assigned S137 (04-n175): Submission/Modify/PublicAct. S138: full content-review pass — re-confirmed both known gaps (string-literal success; clearing logic embedded in prose rather than persistence_condition/persistence_effect, item 2/B). Design Pass ✓, Issues Resolved not yet — real schema blockers remain.*

```python
SYN.MOD.6 = Card(
    id      = "SYN.MOD.6",  card_id = "SYN.MOD.6",  version = "v0.1",
    name    = "Bounty Contract",
    tagline = "If someone wants them gone, I am willing to subsidize the effort.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = Submission,  function = Modify,  subject = PublicAct,  # assigned S137 (04-n175, Andy confirmed) — boosts a named opponent's PA, positive-direction sibling of SYN.MOD.10/STD.MOD.103/DIR.MOD.6

    trigger         = public_act.placed_on_frg(faction=opponent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    persistence     = Seasonal,
    persistence_condition = None,  # ⚠ clearing logic is embedded in the success string instead — same gap as GUI.MOD.10/SYN.MOD.6 in schema_cleanup_log.md item 2/B
    persistence_effect    = None,  # ⚠ see above

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = "Syndicate places this card on their FRG as a standing condition and places 2 Capital on it. The target opponent's PA gains boost=+20. When target PA resolves: if success, the 2 Capital is transferred to the acting faction; if failure, the Capital is returned to Syndicate.",  # ⚠ string literal, not a real MutationExpr — flagged 04-n175, confirmed still true
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Transactional warfare. Played onto Syndicate's own FRG with 2 Capital 'escrowed' on the card, preventing any Beat 4 resource-cleanup conflicts with the target PA itself. The submitting faction effectively becomes Syndicate's mercenary, receiving the Capital only if the op succeeds.",
    arbiter_note = None,
)
```

---

### SYN.MOD.7 — RENEGOTIATION FEE

#### Design Rationale
Third Accord-lifecycle income card — fires on `accord.corrupted` (textual alteration, e.g. via SYN.CA.11 Redline), distinct from SYN.MOD.2 (formation) and SYN.MOD.3 (removal). No overlap between the three, each keyed to a distinct Accord event.

#### Card Story
An Accord's fine print quietly changes — someone rewrote a clause. Syndicate's lawyers are already billing for the "procedural friction" of the rewrite, whether or not they had anything to do with it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Profiting from Accord manipulation as procedural friction is a coherent, distinct beat from SYN.MOD.2/3's formation/removal triggers. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("when the fine print changes, the lawyers get paid") lands the doctrine. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; routine economic reaction. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Syndicate, real taxonomy (Economy/Add/NativeResource, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Economy×Add cell as SYN.MOD.2/3/4/5. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Flat, no cost, gated on a specific Accord-corruption event (rarer than formation/removal) — plausible; final read pending 04-n178. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `accord.corrupted` — confirmed vocabulary, publicly observable (per GR 7.2a's Accord-corruption semantics). | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct. | Art 01 §6–7 |
| Supported by components | ✓ | Standard resource-grant mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing Accord-corruption event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set gate as the rest of the corpus. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ | Accord corruption is a specific, less-common event (requires a corrupt-capable card like SYN.CA.11) — low-moderate frequency. |  |
| Firing window (ModReactCard) | ✓ | No other Syndicate card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat yield, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*Reacts to the corruption (textual alteration) of an Accord's terms. S138: full content-review pass — clean, no new issues beyond the standard schema/cost/stack gaps. Design Pass ✓, Issues Resolved not yet.*

```python
SYN.MOD.7 = Card(
    id      = "SYN.MOD.7",  card_id = "SYN.MOD.7",  version = "v0.1",
    name    = "Renegotiation Fee",
    tagline = "When the fine print changes, the lawyers get paid.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = Economy,  function = Add,  subject = NativeResource,  # assigned S137 (04-n175), same shape as SYN.MOD.2

    trigger         = accord.corrupted,
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = faction(Syndicate).resources.add(2, Capital),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Leveraging Accord manipulation. Triggers when ANY faction successfully corrupts an Accord (e.g., via SYN.CA.11 Redline). Syndicate earns 2 Capital from the procedural friction of rewriting the agreement.",
    arbiter_note = None,
)
```

---

### SYN.MOD.8 — VULTURE FUND

#### Design Rationale
Opportunistic dual-effect React: reacts to any opponent's structure removal, immediately placing both a Syndicate chip and a Syndicate structure in the vacated district. Real finding, worse than the typical string-literal gap: `success` here is a single string containing *two* semicolon-joined statements ("arbiter.place(...); arbiter.place(...)") — not just prose describing an effect, but something that reads like it was meant to be a real multi-statement mutation and never got converted to the schema's actual list-of-mutations pattern (compare GHO.MOD.7/NET.MOD.10's `list([...])` form, which is the correct way to express this exact "two placements" shape). Also carries the cross-resource cost question (Exposure, not Syndicate-native) seen repeatedly this session.

#### Card Story
A structure falls somewhere in the city — sabotage, contest, doesn't matter. The paperwork for the vacated ground was drafted before the demolition crew finished clearing the site; Syndicate doesn't wait for the dust to settle.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Opportunistic acquisition of vacated ground (distinct from SYN.CA.9's active-position takeover, per the S132 rename) is a clean, doctrinally coherent beat. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("buy when there's blood in the streets") lands the doctrine. Rare among this set — `narrative` field is actually filled in. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; opportunistic tactical play, not a public doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Syndicate, real taxonomy (Territory/Add/StructureBlock, 04-n175) — dual-effect, structure treated as primary per Andy's confirmation. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory×Add valid per the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Design_note's own "extremely powerful territorial swing" framing is honest — a dual chip+structure placement for 3 resources is significant; can't fully verify power level while the effect is a semicolon-joined string rather than a checkable Expr. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `structure_block.removed(faction=opponent)` — confirmed vocabulary, correctly scoped, no self-fire ambiguity. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district` — correct. | Art 01 §6–7 |
| Supported by components | ✓ | Both chip and structure placement reuse standard mechanisms — the gap is purely in how `success` expresses them, not the underlying components. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing structure-removal event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ **(known issue, sharper instance)** | `success` is a string literal containing 2 semicolon-joined pseudo-statements — a worse case than a single descriptive string, since it reads like unconverted code. The correct form is almost certainly `list([arbiter.place(presence_chip,...), arbiter.place(structure_block,...)])`, matching GHO.MOD.7/NET.MOD.10's precedent. Flagged, not fixed. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | `narrative` field is filled in (rare in this set) and reads well. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch (once the expression form is corrected). | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Real cost specified, but spans Capital (native) and Exposure (Network's) — same cross-resource-holding question flagged on several cards this session. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Gated on any opponent losing a structure — moderate, reactive. |  |
| Firing window (ModReactCard) | ✓ | No other Syndicate card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary acquisition — no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*Renamed S132 from "Hostile Takeover" — duplicate name with SYN.CA.9 (04-n156). Syndicate buys up the territory left behind by destroyed infrastructure. Taxonomy assigned S137 (04-n175): Territory/Add/StructureBlock. S138: full content-review pass — the `success` string-literal gap is sharper than typical (2 semicolon-joined statements, not just prose); cross-resource cost flagged. Design Pass ✓, Issues Resolved not yet.*

```python
SYN.MOD.8 = Card(
    id      = "SYN.MOD.8",  card_id = "SYN.MOD.8",  version = "v0.1",
    name    = "Vulture Fund",
    tagline = "Buy when there's blood in the streets.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = Territory,  function = Add,  subject = StructureBlock,  # assigned S137 (04-n175) — see note above; dual-effect with presence chip, structure treated as primary

    trigger         = structure_block.removed(faction=opponent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Syndicate).resources.has(2, Capital),
    cost            = resource.faction(Syndicate).capital * 2 + resource.faction(Syndicate).exposure * 1,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = "arbiter.place(presence_chip, district=target_district, faction=Syndicate, count=1); arbiter.place(structure_block, district=target_district, faction=Syndicate, count=1)",  # ⚠ string literal containing 2 semicolon-joined statements — worse than a single-literal gap; flagged, not fixed
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = "The paperwork was drafted before the demolition crew finished clearing the site. Syndicate doesn't wait for the dust to settle to make an offer.",
    perspectives = None,
    design_note  = "Renamed S132 from 'Hostile Takeover' — collided with SYN.CA.9, an unrelated card that displaces an opponent's active presence tokens. Vulture Fund is a different mechanic entirely: opportunistic expansion into vacated ground, not a forced acquisition of a going concern. When a structure falls, Syndicate swoops in, paying 2 Capital to immediately place both a presence chip and a structure in the newly cleared real estate. Extremely powerful territorial swing funded entirely by Capital Cost reasoning: Exposure ensures the takeover is recognized publicly, legitimizing the new ownership immediately.",
    arbiter_note = None,
)
```

### SYN.MOD.9 — GOODWILL

#### Design Rationale
Standing floor + boost card: fires whenever Syndicate's own PS decreases, letting Syndicate declare a variable N and pay Capital×N to gain +N PS (N=1 negates the drop, N>1 nets a gain). Two real, unresolved problems, both flagged not fixed: (1) `success = faction(Syndicate).standing += N` uses invalid `+=` syntax — the second confirmed instance of this exact problem (`schema_cleanup_log.md` item 17, after NET.MOD.2). (2) The card explicitly never discards ("remains active for further triggers") — a persistence shape none of the 4 documented values (Immediate/Transient/Seasonal/Permanent) actually fit, since Permanent still requires an eventual clearing condition and this card has none. Logged as a new schema question, item 19. The design_note also self-admits two open questions (N-cap, ElectPlayer-vs-Automatic-payment) — cited directly, not re-derived.

#### Card Story
Syndicate's reputation takes a hit — anywhere, any cause. Before the news finishes circulating, a public-goodwill campaign is already funded and running, buying back exactly as much standing as Syndicate is willing to spend on it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "Reputation is a line item" — treating PS recovery as a scalable, budgeted expense is a sharply doctrinal Syndicate mechanic. | Art 00 §7 |
| Voice fit | ✓ | Tagline lands the doctrine precisely. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; a budgeted defensive mechanism, not a public doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Syndicate, real taxonomy (Standing/Shift/StandingMarker, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Standing×Shift valid per the matrix (04-n173 precedent). | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Scalable N with an admitted-open cap question — could this be abused as unlimited PS-buying if N is uncapped? Design_note flags this itself as unresolved. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ⚠ | No `persistence` value fits — the card is meant to never discard, which none of Immediate/Transient/Seasonal/Permanent actually model. New finding, item 19. | Art 04 §5 P19; schema_cleanup_log.md item 19 |
| Persistence | ⚠ **(new schema gap, item 19)** | Same issue as above — "remains active for further triggers, never discards" has no fitting enum value. Distinct from the item 2/B gap (cards that eventually clear but express the clearing logic inconsistently) — this card structurally never clears at all. | Art 04 §6.2; schema_cleanup_log.md item 19 |
| Trigger validity | ✓ | `standing_marker.decreased(Syndicate)` — confirmed vocabulary, self-scoped, no ambiguity. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; not a territory effect. | Art 01 §6–7 |
| Supported by components | ✓ | PS/standing-marker shift reuses the standard mechanism, once the `+=` syntax issue is resolved. | Art 02 §6–8 |
| Supported by game procedure | ⚠ | Design_note itself flags an unresolved question: does Syndicate ALWAYS pay when the trigger fires, or may they decline (ElectPlayer)? Not resolved here. | Art 03; GR 6.1 |
| Data schema validation | ⚠ **(blocker)** | `success = ... += N` is invalid syntax, not a valid MutationExpr — 2nd confirmed instance of item 17. Scaffolding added this session for the fields that were simply absent. | Art 04 §6.1–§6.3; schema_cleanup_log.md item 17 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch (once the expression syntax is corrected) — N is a declared parameter, not a hidden or probabilistic outcome. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Real, scalable cost (Capital×N) — reasonable in shape, but the balance question (N-cap) is unresolved, so the effective cost/value ratio can't be finalized. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Gated on Syndicate's own PS decreasing — self-limiting, moderate frequency. |  |
| Firing window (ModReactCard) | ✓ | No other Syndicate card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ⚠ | Design_note's own open question: should this be Automatic (always fires, always pays) or ElectPlayer (Syndicate may decline)? Not resolved. |  |
| Stack behavior (ModReactCard) | ⚠ | Compounded by the card never discarding — does holding 2 copies mean 2 independent N-declarations per trigger? Genuinely more consequential here than the generic stack question elsewhere. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S130. ModReactCard — Standing floor. Fires when Syndicate PS decreases; Capital×1 negates the drop. Counters SYN.CA.7 portrait bleed. 04-n131 design decision resolved. S138: full content-review pass — invalid `+=` syntax confirmed as a 2nd instance (item 17); "never discards" persistence shape doesn't fit any of the 4 documented values (new item 19); N-cap and Automatic-vs-ElectPlayer questions re-confirmed still open (self-admitted in the card's own design_note). Design Pass ✓, Issues Resolved not yet — real blockers remain.*

```python
SYN.MOD.9 = Card(
    id      = "SYN.MOD.9",  card_id = "SYN.MOD.9",  version = "v0.1",
    name    = "Goodwill",
    tagline = "Reputation is a line item. We budget for it accordingly.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = Standing,  function = Shift,  subject = StandingMarker,  # assigned S137 (04-n175) — standing += N

    trigger         = standing_marker.decreased(Syndicate),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Syndicate).capital * N,  # N declared at trigger (min 1)
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = faction(Syndicate).standing += N,  # ⚠ INVALID SYNTAX — `+=` is a statement, not an expression; 2nd confirmed instance (schema_cleanup_log.md item 17, after NET.MOD.2)
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Standing floor + boost card. Fires whenever Syndicate's PS decreases (any source — SYN.CA.7 portrait flat −1, failcrit, card effect). At trigger: Syndicate declares N and pays Capital×N; gains +N PS. N=1 negates the decrease (floor). N>1 nets a PS gain above the prior value (boost). Trigger opens the window; spend is scalable. If Capital unavailable: effect does not fire; decrease stands. Card does not discard — remains active for further triggers. Outstanding: (1) N cap — uncapped vs. max-N limit pending design pass. (2) Confirm ElectPlayer or Automatic at trigger time — does Syndicate ALWAYS pay, or may they waive at trigger. 04-n131 design decision → PS floor card selected.",
    arbiter_note = "On trigger (Syndicate's standing marker moved down for any reason): Syndicate declares N (min 1) and pays Capital×N. Apply faction(Syndicate).standing += N. If Capital unavailable or Syndicate declines: decrease stands. Card remains active for further triggers.",
)
```

---

### SYN.MOD.10 — LOBBY

#### Design Rationale
Resolution-layer gap-fill (04-n129): Syndicate pays Capital to apply a −15 threshold penalty to a specifically named faction's PA. Cleaner than its siblings — `success` is a real MutationExpr (`arbiter.apply_modifier`), not a string literal, matching the confirmed STD.MOD.103/DIR.MOD.6/SYN.MOD.6 pattern. Two things worth checking directly rather than assuming: the card's own design_note flags whether `public_act.placed_on_frg(faction(target))` targeting a *specific named* opponent (declared in advance) is procedurally valid, since prior confirmed examples were self-targeting (Network) or generically opponent-scoped (SYN.MOD.6's `faction=opponent`) — naming one faction ahead of time is a sharper requirement than either precedent actually covers. Also: `faction(named_opponent)` is yet another acting-faction-reference term with no established precedent (same category as item 15's `acting` keyword and the Ring set's `holder`).

#### Card Story
A named rival is about to make their move. Before they even declare it, Syndicate has already quietly made the paperwork more expensive — nothing illegal, nothing traceable to a specific hand, just friction that lands exactly where it's aimed.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "We don't oppose your agenda, we make it expensive" is a sharply doctrinal, non-confrontational Syndicate mechanic. | Art 00 §7 |
| Voice fit | ✓ | Tagline lands the doctrine precisely. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; covert financial interference, not a public doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Syndicate, real taxonomy (Submission/Modify/PublicAct, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Submission×Modify valid per the matrix; matches the confirmed −15-modifier pattern from STD.MOD.103/DIR.MOD.6/SYN.MOD.6. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | 1 Capital for a −15 penalty on a named target's PA is meaningful but not overwhelming, consistent with the sibling cards' power level. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Single-fire Immediate per design_note ("discards after triggering"). | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Not explicitly declared as a field (design_note states it in prose) — same open schema question as most of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | Underlying event is genuinely observable, but two open questions, both self-admitted in the design_note: (1) does `public_act.placed_on_frg(faction(target))` validly support naming a *specific* opponent in advance, sharper than the confirmed self-targeting/generic-opponent precedents; (2) `faction(named_opponent)` is an unprecedented acting-faction-reference term, same category as item 15. | Art 04 §6.3; schema_cleanup_log.md item 15 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; this targets a faction's PA, not a district. | Art 01 §6–7 |
| Supported by components | ✓ | Modifier-token application reuses the standard mechanism from STD.MOD.103/DIR.MOD.6/SYN.MOD.6. | Art 02 §6–8 |
| Supported by game procedure | ⚠ | Design_note's own open question: can the target faction be named/tracked pre-§9.2 without inadvertently revealing Syndicate's intent (a private-information-boundary question)? Not resolved here. | Art 03; GR 6.1 |
| Data schema validation | ✓ | `success` is a real MutationExpr, ahead of SYN.MOD.6/8's string-literal gap. Scaffolding added this session for `resolution_type`/`boost`/`ps_framing`. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cost is Capital only, Syndicate-native — no cross-resource question. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Gated on the named target faction placing a PA — moderate, targeted frequency. |  |
| Firing window (ModReactCard) | ✓ | No other Syndicate card shares this exact trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat modifier application, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S130. ModReactCard — Resolution layer gap. Syndicate spends Capital to apply −15 modifier token to a named faction's PA at §9.2. 04-n129 design decision resolved. S138: full content-review pass — this is one of the cleanest cards in the Syndicate set (real MutationExpr, native-resource cost); the card's own self-admitted questions about named-opponent-targeting validity and pre-declaration information boundaries remain genuinely open. Design Pass ✓, Issues Resolved not yet.*

```python
SYN.MOD.10 = Card(
    id      = "SYN.MOD.10",  card_id = "SYN.MOD.10",  version = "v0.1",
    name    = "Lobby",
    tagline = "We don't oppose your agenda. We make it expensive to execute.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = Submission,  function = Modify,  subject = PublicAct,  # assigned S137 (04-n175) — arbiter.apply_modifier(op=trigger.card, modifier=-15), same shape as STD.MOD.103/DIR.MOD.6/SYN.MOD.6

    trigger         = public_act.placed_on_frg(faction(target)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = faction(named_opponent),
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Syndicate).capital * 1,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.apply_modifier(op=trigger.card, modifier=-15),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Resolution layer gap fill (04-n129). Fills 'money-at-the-table' narrative: Syndicate pays Capital to suppress a named faction's PA threshold at the moment of declaration. ARBITER places −15 modifier token on target PA's Beat 4 resolution row. Named target faction declared when card is played/assigned (before §9.2). Single-fire Immediate — discards after triggering. Outstanding: (1) Trigger pattern public_act.placed_on_frg(faction(target)) — existing confirmed examples are self-targeting (Network's own PAs); confirm opponent-targeting variant is procedurally valid. (2) Named faction pre-declaration timing — confirm ARBITER can track the target faction designation without revealing Syndicate's intent.",
    arbiter_note = "On trigger (named target faction places PA at §9.2): Syndicate pays Capital×1. Place modifier token (−15) on target PA's Beat 4 resolution row. Announce modifier publicly (target PA threshold is reduced by 15; acting faction not identified). Card discards after firing.",
)
```

---

### SYN.MOD.11 — SIGNATURE ON FILE

#### Design Rationale
Syndicate's most expensive Accord card — forges a named party's Accord acceptance without their consent, paired with SYN.CA.12 Boilerplate for a fully unilateral Accord combo. Three questions the card's own text already flags, cited directly rather than re-derived: (1) `trigger = accord.tabled` needs Art 06 timing confirmation — this pre-signature event isn't in the confirmed §6.3 vocabulary (which has `accord.placed/corrupted/removed`, all post-formation), so this is a genuinely new trigger stage, not just an unreconciled term. (2) "party_b" (the second named party on the drafted form) needs a precise definition. (3) Portrait magnitude (`flat=+2`) is self-flagged as needing confirmation against Portrait principles. Independently re-verified: the taxonomy (Information/Corrupt/Accord) already flagged as "least-precedented" (04-n175) does hold up against the matrix (Information×Corrupt is valid) — the caution was warranted but the assignment itself is sound. Also worth noting: the cost includes an Intel Token as one of four cost components — same fungibility question as `schema_cleanup_log.md` item 10 (first raised on DIR.MOD.9).

#### Card Story
The Accord draft goes on the table with only one signature. Syndicate already has what it needs from the other party — the form is a formality, and by the time anyone notices, the agreement is already active.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Forcing a binding Accord through leverage rather than negotiation is the sharpest possible expression of Syndicate's "control comes from positioning early" doctrine. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("the form is a formality") lands the doctrine precisely. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait `flat=+2` — functionally equivalent to `submitter=+2` here since only Syndicate can ever hold/play a Syndicate-only card; not an inconsistency, just a stylistic field choice. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Syndicate, real taxonomy (Information/Corrupt/Accord, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Independently re-verified against the matrix (not just inherited from the S137 flag): Information×Corrupt is valid. The "least-precedented" caution was warranted given how novel this mechanic is, but the assignment itself holds. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | Four-resource cost (2 Capital + Findings + Mandate + a keyed Intel Token) for forcing a binding Accord is appropriately "ceiling-power" per its own framing — the most expensive Syndicate card reviewed this session. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate — the Accord becomes active at once; card discards after firing. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Not explicitly declared as a field — same open schema question as most of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | **Genuinely new, not just unreconciled:** `accord.tabled` is a pre-signature-stage event with no confirmed §6.3 form at all (confirmed vocabulary only covers post-formation Accord events — placed/corrupted/removed). The card's own text already flags this needs Art 06 timing confirmation. | Art 04 §6.3 |
| Portrait validity | ✓ | Magnitude (`flat=+2`, vs. the more common `+1`) is self-flagged for confirmation — scale seems proportionate to the card's "ceiling-power" framing, but not independently re-derivable without a numeric Portrait-magnitude standard to check against. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; Accords have no district dimension. | Art 01 §6–7 |
| Supported by components | ✓ | Intel Token consumption and Accord-form marking both reuse existing components. | Art 02 §6–8 |
| Supported by game procedure | ⚠ | Depends on the unconfirmed `accord.tabled` trigger stage — the underlying Art 06 procedure for a "tabled but unsigned" Accord state isn't yet formally described. | Art 03; GR 6.1 |
| Data schema validation | ⚠ | Real MutationExpr (`arbiter.mark_acceptance`) — ahead of SYN.MOD.6/8's string-literal gap. Cost includes an Intel Token — same fungibility question as `schema_cleanup_log.md` item 10. Scaffolding added this session for `resolution_type`/`boost`/`ps_framing`. | Art 04 §6.1–§6.3; schema_cleanup_log.md item 10 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Cost is real and substantial, but one of the four components (Intel Token) has the same open fungibility question as item 10 — is a discrete tracked object a valid "fungible resource" cost component? | Art 00a §9.2; schema_cleanup_log.md item 10 |
| Trigger frequency (ModReactCard) | ✓ | Gated on holding a keyed Intel Token on the specific party — inherently rare, matching the "ceiling-power" framing. |  |
| Firing window (ModReactCard) | ✓ | No other Syndicate card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Deterministic forgery, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S130. ModReactCard — fires when Accord draft is tabled. Syndicate forges party B's acceptance; Accord becomes binding without consent. Ceiling-power card. Paired with SYN.CA.12 Boilerplate for non-negotiable unilateral Accord combo. S138: full content-review pass — taxonomy re-verified sound despite being the least-precedented assignment in the sweep; `accord.tabled` confirmed as a genuinely new (not just unreconciled) pre-signature trigger stage; Intel-Token-as-cost fungibility question cross-referenced to item 10. Design Pass ✓, Issues Resolved not yet.*

```python
SYN.MOD.11 = Card(
    id      = "SYN.MOD.11",  card_id = "SYN.MOD.11",  version = "v0.1",
    name    = "Signature on File",
    tagline = "We already have what we need. The form is a formality.",
    type    = ModReactCard,  faction = Syndicate,
    layer   = Information,  function = Corrupt,  subject = Accord,  # assigned S137 (04-n175) — forges an Accord party's acceptance; closest analog is GHO.MOD.11's Information/Corrupt pattern (falsifying an official record). Least-precedented assignment in this sweep, flag for re-check when this card comes up for content review. Subject corrected from AccordDraft (not a registered subject) to Accord (registered; AccordForm is the established object-type name per Art 06/Overture, but the taxonomy subject list itself only registers Accord/AccordAgreement/AccordCard)

    trigger         = accord.tabled,  # PENDING: confirm trigger expression — fires at draft tabling stage (before party signatures), not accord.placed (which fires when Accord is already active)
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = faction(accord.party_b),
    target_object   = AccordForm(state=drafted),  # corrected S137 (Andy) — was AccordDraft(state=tabled); AccordForm is the established term (Art 06 §9.2, Overture's AccordForm(blank))
    affinity        = None,
    restriction     = IntelToken(keyed_to=faction(accord.party_b)) in faction(Syndicate).hand,
    cost            = Capital(2) + Findings(1) + Mandate(1) + IntelToken(keyed_to=faction(accord.party_b)),
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.mark_acceptance(accord=trigger.accord, party=faction(accord.party_b), state=signed),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Syndicate: PortraitEntry(flat=+2)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Ceiling-power card — the most expensive Syndicate Accord card. Cost rationale: Capital×2 (commercial commitment to force the agreement); Findings×1 (due diligence on party B — they know enough to make this stick); Mandate×1 (institutional authority that makes the forced signing legally enforceable); IntelToken(keyed to party_b) (the specific leverage that makes party B's resistance futile — consumed on play). Effect: ARBITER marks party B's acceptance on the Accord form as signed. Accord becomes active immediately without party B's participation. Party B is notified privately at enforcement, not at tabling. Outstanding: (1) confirm trigger expression accord.tabled — needs Art 06 timing confirmation; must fire at draft placement stage before normal acceptance window opens. (2) Define 'party_b' — the second named party on the Accord form as drafted by Syndicate (or whichever party has not signed). (3) Portrait magnitude: flat=+2 reflects scale of action — confirm against portrait principles. Combo with SYN.CA.12 Boilerplate: Syndicate writes and forces through a unilateral Accord in one session.",
    arbiter_note = "On trigger (Accord draft is tabled): confirm Syndicate holds IntelToken keyed to party_b and can pay Capital×2 + Findings×1 + Mandate×1. If valid: consume the IntelToken and all resource cost; mark party_b's acceptance field on the Accord form as signed. Notify party_b privately. Accord proceeds to active state as if party_b accepted voluntarily. Announce publicly only that the Accord has become active — not the mechanism. Card discards after firing.",
)
```

---

### SYN.MOD.12 — CONTRACTED MUSCLE

#### Design Rationale
Syndicate's ModBattleCard set, replicating the Directorate/Ghost/Network/Guild pattern (2 Boost +1/+2, 2 Hinder −1/−2, S132) — last of the five. Doctrine per §5a is the most explicit of any faction on this exact subclass: "Battle winner modifier cards: rare and costly; serve primarily as deterrent." `cost = None`, matching all four other factions (corrected S132 — Andy): Art 03 §10.1.2 has no cost validation/payment step anywhere in the commit or reveal sequence, so a `cost` field here would be unenforceable content. "Rare and costly" stays true at the deck level (acquisition/rarity), not a per-play resource cost. Weaker Boost tier (+1): a cheap, disposable hire.

#### Card Story
A few names get a call, a rate gets quoted, and by evening there are more people on the block than there were this morning — reinforcing whichever side the playing faction has named.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Hired muscle committed to a live contest is a grounded expression of Syndicate's capital/leverage doctrine (§5a). | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only (`perspectives`/`design_note` schema-locked None); transactional-hire register. | Art 00 §9 |
| Doctrine alignment | ✓ | Boost via paid leverage, not institutional force or intelligence; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Syndicate's Asset-category naming slot (S130). | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Boost tier per locked S132 pattern; no cost step exists for this subclass — "costly" is deck-level rarity, not per-play cost; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (Andy, S140, locked whole-subclass, PM02 L269). | Art 04 §6.1–§6.2; PM02 L269 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None` correct for a faction-deck card. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention (Andy S132) — deck-level rarity substitutes for a per-play cost. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S132. Syndicate's ModBattleCard set, replicating the Directorate/Ghost/Network/Guild pattern (2 Boost +1/+2, 2 Hinder −1/−2, PM05 09-06) — last of the five. Doctrine per §5a is the most explicit of any faction on this exact subclass: "Battle winner modifier cards: rare and costly; serve primarily as deterrent — Directorate's awareness shapes Ring 1/2 calculus without deployment." **`cost = None`, matching all four other factions (corrected S132 — Andy):** Art 03 §10.1.2 has no cost validation/payment step anywhere in the commit or reveal sequence, so a `cost` field here would be unenforceable content, the same class of error 04-n152 exists to prevent on the effect side. "Rare and costly" stays true at the *deck* level — the acquisition/rarity side of that doctrine (how seldom these are drawn, how few exist) rather than a per-play resource cost with no procedure to collect it. Weaker Boost tier (+1): a cheap, disposable hire. Design-reviewed S140 (09-16 step 4) — same disposition as the other 4 factions; portrait resolved same session (PM02 L269).*

```python
SYN.MOD.12 = Card(
    id      = "SYN.MOD.12",  card_id = "SYN.MOD.12",  version = "v0.1",
    name    = "Contracted Muscle",
    tagline = "Paid by the hour, paid up front, gone the moment the money stops.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=1),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 1,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,   # corrected S132 (Andy) — Art 03 §10.1.2 has no cost validation step; "costly" is deck-level rarity, not a per-play resource cost
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "A few names get a call, a rate gets quoted, and by evening there are more people on the block than there were this morning.",
    arbiter_note = "Playable by any faction, not just Syndicate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### SYN.MOD.13 — ARMORED TRANSPORT

#### Design Rationale
Stronger Boost tier (+2) — hardware rather than headcount. `cost = None`, same as SYN.MOD.12 (see that card's note on why "costly" doesn't become a per-play resource cost).

#### Card Story
A convoy rolls in that nobody remembers ordering. It parks, and it stays parked, right where it's most visible — reinforcing whichever side the playing faction has named.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Conspicuous hardware committed to a live contest is a grounded expression of Syndicate's capital/leverage doctrine. | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only; conspicuous-asset register, distinct from SYN.MOD.12's headcount framing. | Art 00 §9 |
| Doctrine alignment | ✓ | Boost via purchased hardware, not force or intelligence; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Syndicate's Equipment-category naming slot. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Boost tier (magnitude 2/value_rating 2) per locked S132 pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (Andy, S140, locked whole-subclass, PM02 L269). | Art 04 §6.1–§6.2; PM02 L269 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None` correct for a faction-deck card. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention (Andy S132). | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S132. Stronger Boost tier (+2) — hardware rather than headcount. `cost = None`, same as SYN.MOD.12 (see that card's note on why "costly" doesn't become a per-play resource cost). Design-reviewed S140 (09-16 step 4) — same disposition as SYN.MOD.12; portrait resolved same session (PM02 L269).*

```python
SYN.MOD.13 = Card(
    id      = "SYN.MOD.13",  card_id = "SYN.MOD.13",  version = "v0.1",
    name    = "Armored Transport",
    tagline = "Nobody asks where it came from. Everybody notices it's there.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=2),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 2,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,   # corrected S132 (Andy) — Art 03 §10.1.2 has no cost validation step; "costly" is deck-level rarity, not a per-play resource cost
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "A convoy rolls in that nobody remembers ordering. It parks, and it stays parked, right where it's most visible.",
    arbiter_note = "Playable by any faction, not just Syndicate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### SYN.MOD.14 — CALLED-IN DEBT

#### Design Rationale
Weaker Hinder tier (−1). Syndicate's suppression is financial leverage, not force — someone the target faction depends on suddenly has other obligations to honor first. `cost = None`, same as SYN.MOD.12/13.

#### Card Story
A supplier who was supposed to show up tonight suddenly has a more urgent invoice to settle first — the named faction's position goes short.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Financial leverage redirecting a rival's dependency is a grounded expression of Syndicate's capital/leverage doctrine. | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only; debt/obligation register, distinct from force-based Hinders elsewhere. | Art 00 §9 |
| Doctrine alignment | ✓ | Hinder via financial leverage, not force; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Syndicate's Tactic-category Hinder slot. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Hinder tier per locked S132 pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (Andy, S140, locked whole-subclass, PM02 L269). | Art 04 §6.1–§6.2; PM02 L269 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None` correct for a faction-deck card. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention (Andy S132). | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S132. Weaker Hinder tier (−1). Syndicate's suppression is financial leverage, not force — someone the target faction depends on suddenly has other obligations to honor first. Design-reviewed S140 (09-16 step 4) — same disposition as SYN.MOD.12/13; portrait resolved same session (PM02 L269).*

```python
SYN.MOD.14 = Card(
    id      = "SYN.MOD.14",  card_id = "SYN.MOD.14",  version = "v0.1",
    name    = "Called-In Debt",
    tagline = "Everyone owes somebody. Tonight, Syndicate collects.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=1),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 1,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,   # corrected S132 (Andy) — Art 03 §10.1.2 has no cost validation step; "costly" is deck-level rarity, not a per-play resource cost
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "A supplier who was supposed to show up tonight suddenly has a more urgent invoice to settle first.",
    arbiter_note = "Playable by any faction, not just Syndicate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### SYN.MOD.15 — BOUGHT OFF

#### Design Rationale
Stronger Hinder tier (−2), completing Syndicate's 2 Boost/2 Hinder pattern and the full five-faction ModBattleCard pattern-set. Escalates Called-In Debt from inconvenience into defection — not people the target hired, but people the target was counting on regardless. `cost = None`, same as the rest of the set.

#### Card Story
The people the target was counting on tonight took a better offer this afternoon. Nobody told them who from — the named faction's position is left short at the worst possible moment.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Bought defection at a critical moment is the escalated form of Syndicate's capital/leverage doctrine. | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only; same leverage register as SYN.MOD.14, escalated to outright defection. | Art 00 §9 |
| Doctrine alignment | ✓ | Hinder via bought-off dependency, not force; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Syndicate's Tactic-category escalated Hinder slot alongside SYN.MOD.14. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Hinder tier (magnitude 2/value_rating 2) per locked S132 pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (Andy, S140, locked whole-subclass, PM02 L269). | Art 04 §6.1–§6.2; PM02 L269 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None` correct for a faction-deck card. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention (Andy S132). | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S132. Stronger Hinder tier (−2), completing Syndicate's 2 Boost/2 Hinder pattern and the full five-faction ModBattleCard pattern-set. Escalates Called-In Debt from inconvenience into defection — not people the target hired, but people the target was counting on regardless. Design-reviewed S140 (09-16 step 4) — same disposition as the rest of the Syndicate set; portrait resolved same session (PM02 L269). Closes Syndicate's ModBattleCard review — all 4 cards (SYN.MOD.12–15) design-passed, no open issues. All 5 factions' ModBattleCard sets (20 cards) now design-reviewed; only the 24-card Ring/Standard set (STD.MOD.2–25) remains for 09-16 step 4.*

```python
SYN.MOD.15 = Card(
    id      = "SYN.MOD.15",  card_id = "SYN.MOD.15",  version = "v0.1",
    name    = "Bought Off",
    tagline = "Everyone has a price. Syndicate found out whose was lowest.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=2),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 2,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,   # corrected S132 (Andy) — Art 03 §10.1.2 has no cost validation step; "costly" is deck-level rarity, not a per-play resource cost
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "The people the target was counting on tonight took a better offer this afternoon. Nobody told them who from.",
    arbiter_note = "Playable by any faction, not just Syndicate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### SYN.MOD.16 — GOLDEN HANDSHAKE

#### Design Rationale
Replicates the faction ModActionCard pattern to Syndicate, last of the 5 factions. Minor threshold_delta tier (+5), self-only, fits capital/leverage doctrine cleanly.

#### Card Story
A well-placed incentive smooths the acting faction's own play — everyone involved walks away satisfied, which is the point.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Incentive-as-lubricant is the clean mechanical expression of Syndicate's capital doctrine. | Art 00 §7 |
| Voice fit | ✓ | `faction=Syndicate`; narrative reads in the capital/leverage register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | ModActionCard, `subtype=FactionSpecific`, correctly excluded from taxonomy. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None for all modifier subclasses. | Art 04 §6.2 |
| Balance | ✓ | Minor tier of the locked 4-value ladder; `value_rating=1` mirrors tier. | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None for ModActionCard. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None — bundled at Dispatch. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` genuinely assessed — no independent doctrinal weight beyond the host action. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct for a faction deck card. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Dispatch-bundling procedure at Art 03 §9.1.1/§9.4.0.1 covers attachment. | Art 03 §9.1.1, §9.4.0.1 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence New Meridian event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | ModActionCard carries no `success`/`fail`-family fields (schema-locked None). | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention; out of scope for 04-n178. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135. Replicates the Directorate ModActionCard pattern (DIR.MOD.14–25, 09-06/04-n157) to Syndicate — locked format: 4 `threshold_delta` (+5/+10/+15/+20) + 2 `success_multiplier` (n=1/n=2) + 4 `ps_shift` (self +1/+2, target −1/−2) + 2 `cost_reduction` (n=1/n=2, PA-only), `cost=None` uniformly, `value_rating` 1–4 mirroring tier. Syndicate voice: capital and leverage, patient accumulation, deterrent-first doctrine — same doctrinal lens as Syndicate's shipped ModBattleCard set (SYN.MOD.12–15). Completes the faction-set pattern-set for all 5 factions (last of five). Minor threshold_delta tier (+5). Design-reviewed S139.*

```python
SYN.MOD.16 = Card(
    id      = "SYN.MOD.16",  card_id = "SYN.MOD.16",  version = "v0.1",
    name    = "Golden Handshake",
    tagline = "A well-placed incentive, offered before anyone had to ask twice.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1, effect is parasitic on host action

    effect          = ModActionExpr.threshold_delta(n=5),  # self-only (§6.3, 04-n170); eases the host CA/PA's own threshold
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,   # splay-display convention, PM02 L256 — same basis as all ModActionCard content
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A well-placed incentive smooths the acting faction's own play — everyone involved walks away satisfied, which is the point.",
    arbiter_note = "Attach at Dispatch to any CA/PA in Syndicate's own submitted packet (Art 03 §9.1.1) — no card-level host restriction.",
)
```

---

### SYN.MOD.17 — INSIDER TERMS

#### Design Rationale
Mid tier (+10). Same structure as SYN.MOD.16, self-only.

#### Card Story
Favorable terms negotiated in advance ease a financial move well before anyone else at the table sees the numbers.

**Design checklist:** Same disposition as SYN.MOD.16.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same capital-doctrine basis. | Art 00 §7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Mid tier; `value_rating=2` mirrors tier. | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135. Mid threshold_delta tier (+10). Design-reviewed S139.*

```python
SYN.MOD.17 = Card(
    id      = "SYN.MOD.17",  card_id = "SYN.MOD.17",  version = "v0.1",
    name    = "Insider Terms",
    tagline = "The terms were negotiated well before the deal ever went public.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=10),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Favorable terms negotiated in advance ease a financial move well before anyone else at the table sees the numbers.",
    arbiter_note = "Self-only, same basis as SYN.MOD.16.",
)
```

---

### SYN.MOD.18 — CLEARED POSITION

#### Design Rationale
Third tier (+15). Reframed from "Market Pressure" (hostile) per 04-n170.

#### Card Story
Pre-arranged leverage removes the friction that would otherwise complicate the acting faction's own financial move.

**Design checklist:** Same disposition as SYN.MOD.16. Narrative independently checked — clean self-only, no hostile residue.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same capital-doctrine basis. | Art 00 §7; PM05 04-n170 |
| Voice fit | ✓ | Clean self-only reframe. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Third tier; `value_rating=3` mirrors tier. | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event, self-only clean. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135. Third of 4 threshold_delta tiers (+15). Reframed from an earlier hostile-flavored seed concept ("Market Pressure" — applying leverage to make a rival's economic action harder, `Whiteboard/modifier_card_ideas.md`) per **04-n170**: threshold_delta carries no faction parameter, so it can only ever ease Syndicate's own host action. Design-reviewed S139 — reframe clean.*

```python
SYN.MOD.18 = Card(
    id      = "SYN.MOD.18",  card_id = "SYN.MOD.18",  version = "v0.1",
    name    = "Cleared Position",
    tagline = "Every lever already pulled before the move is made.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=15),
    value_rating    = 3,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Pre-arranged leverage removes the friction that would otherwise complicate the acting faction's own financial move.",
    arbiter_note = "Reframed from a hostile-flavored seed concept per 04-n170, same basis as NET.MOD.21/GHO.MOD.18/GUI.MOD.17/DIR.MOD.15/16.",
)
```

---

### SYN.MOD.19 — TOTAL LEVERAGE

#### Design Rationale
Capstone tier (+20), closing Syndicate's `threshold_delta` quartet. Clean self-only narrative.

#### Card Story
Every lever available has already been pulled before the move is even made — nothing left in the way.

**Design checklist:** Same disposition as SYN.MOD.16.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same capital-doctrine basis. | Art 00 §7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=4` mirrors tier, +20 unvalidated. | PM02 L258, L259; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Clean self-only event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (+20 playtest flag) |  |

*S135. Capstone threshold_delta tier (+20). Design-reviewed S139.*

```python
SYN.MOD.19 = Card(
    id      = "SYN.MOD.19",  card_id = "SYN.MOD.19",  version = "v0.1",
    name    = "Total Leverage",
    tagline = "Nothing left standing in the way of the move.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=20),
    value_rating    = 4,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Every lever available has already been pulled before the move is even made — nothing left in the way.",
    arbiter_note = "Capstone tier — log actual play outcomes before treating +20 as balanced (04-n157, same playtest caveat as the rest of this set).",
)
```

---

### SYN.MOD.20 — COMPOUND INTEREST

#### Design Rationale
Common tier (n=1) of Syndicate's `success_multiplier` pair. Self-only — "compound interest" is a near-perfect literal fit for Syndicate's patient-accumulation doctrine.

#### Card Story
A resource action's outcome grows the longer it's been quietly set up — patience is the whole strategy.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Compound-interest framing is Syndicate's patient-accumulation doctrine made literal. | Art 00 §7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier; `value_rating=1` mirrors tier. | PM02 L256, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135. Common success_multiplier tier (n=1). Design-reviewed S139.*

```python
SYN.MOD.20 = Card(
    id      = "SYN.MOD.20",  card_id = "SYN.MOD.20",  version = "v0.1",
    name    = "Compound Interest",
    tagline = "The longer it's been set up, the bigger it pays out.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A resource action's outcome grows the longer it's been quietly set up — patience is the whole strategy.",
    arbiter_note = "Self-only, amplifies Syndicate's own host action.",
)
```

---

### SYN.MOD.21 — CONTROLLING STAKE

#### Design Rationale
Capstone tier (n=2) of Syndicate's `success_multiplier` pair. Same unvalidated-magnitude caveat as the rest of the corpus.

#### Card Story
Enough capital already committed turns a modest success into a decisive one — the position was built long before this moment.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "Controlling stake" fits capital doctrine tightly. | Art 00 §7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, n=2 unvalidated. | PM02 L256; PM05 04-n157, 04-n94 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (n=2 playtest flag) |  |

*S135. Rare/capstone success_multiplier tier (n=2). Design-reviewed S139.*

```python
SYN.MOD.21 = Card(
    id      = "SYN.MOD.21",  card_id = "SYN.MOD.21",  version = "v0.1",
    name    = "Controlling Stake",
    tagline = "Enough capital already committed to turn a modest win into a decisive one.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Enough capital already committed turns a modest success into a decisive one — the position was built long before this moment.",
    arbiter_note = "Rare/capstone tier — log actual play outcomes before treating n=2 as balanced (04-n157, same playtest caveat as 04-n94).",
)
```

---

### SYN.MOD.22 — QUIET SETTLEMENT

#### Design Rationale
Self-boost minor tier (+1) of the `ps_shift` matrix. `faction="acting"` needs no host-declared target — no submission-validity dependency.

#### Card Story
A dispute resolved out of public view protects standing that a drawn-out fight would have cost.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Quiet-settlement is squarely Syndicate's discreet-leverage register. | Art 00 §7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier of the 2×2 matrix; `value_rating=1` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | `faction="acting"` resolves cleanly, no target-dependency gap. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135. Self-boost, minor tier (+1) of the `ps_shift` 2×2 matrix. Design-reviewed S139.*

```python
SYN.MOD.22 = Card(
    id      = "SYN.MOD.22",  card_id = "SYN.MOD.22",  version = "v0.1",
    name    = "Quiet Settlement",
    tagline = "A dispute resolved where no one outside the room ever hears about it.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=1),  # self-boost, minor tier
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A dispute resolved out of public view protects standing that a drawn-out fight would have cost.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half resolves to the acting faction.",
)
```

---

### SYN.MOD.23 — PHILANTHROPIC GESTURE

#### Design Rationale
Self-boost major tier (+2) of the `ps_shift` matrix — same basis as SYN.MOD.22, doubled magnitude. Sharp Syndicate voice — goodwill as a cheap transaction.

#### Card Story
A visible donation buys Syndicate a standing boost that costs far less than what it appears to.

**Design checklist:** Same disposition as SYN.MOD.22.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as SYN.MOD.22. | Art 00 §7 |
| Voice fit | ✓ | Excellent Syndicate-specific voice — "costs far less than what it appears to." | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier of the 2×2 matrix; `value_rating=2` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | `faction="acting"` resolves cleanly. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135. Self-boost, major tier (+2) of the `ps_shift` 2×2 matrix. Design-reviewed S139.*

```python
SYN.MOD.23 = Card(
    id      = "SYN.MOD.23",  card_id = "SYN.MOD.23",  version = "v0.1",
    name    = "Philanthropic Gesture",
    tagline = "A visible donation, timed for maximum goodwill.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A visible donation buys Syndicate a standing boost that costs far less than what it appears to.",
    arbiter_note = "Self-boost, major tier — resolves to the acting faction.",
)
```

---

### SYN.MOD.24 — WORD GETS AROUND

#### Design Rationale
Target-hinder minor tier (−1) of the `ps_shift` matrix. Same target-resolution behavior as STD.MOD.34 — resolves via host pairing, not an independent field.

#### Card Story
A quiet mention in the right circles costs a named rival a little standing — nothing traceable, nothing deniable enough to fight.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Discreet-leverage-through-circles fits Syndicate's register. | Art 00 §7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier of the 2×2 matrix; `value_rating=1` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field (Andy, S139; schema_cleanup_log.md #21, closed). |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135. Target-hinder, minor tier (−1) of the `ps_shift` 2×2 matrix. Design-reviewed S139.*

```python
SYN.MOD.24 = Card(
    id      = "SYN.MOD.24",  card_id = "SYN.MOD.24",  version = "v0.1",
    name    = "Word Gets Around",
    tagline = "A quiet mention, in exactly the right circles.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-1),  # target-hinder, minor tier
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A quiet mention in the right circles costs a named rival a little standing — nothing traceable, nothing deniable enough to fight.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA it's packet-paired with names as its target_faction (§6.1) — the modifier's target IS the host action, not an independently-declared field (Andy, S139).",
)
```

---

### SYN.MOD.25 — PREDATORY TERMS EXPOSED

#### Design Rationale
Target-hinder major tier (−2) of the `ps_shift` matrix. Same target-resolution behavior as SYN.MOD.24 (resolves via host pairing, not an independent field), doubled magnitude. Closes the corpus's full 22-card set of target-hinder ModActionCards (Ring: 12, Faction: 10 — 2 per faction × 5).

#### Card Story
A rival's finance practices become public knowledge — Syndicate knows exactly how bad the terms look read aloud.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as SYN.MOD.24. | Art 00 §7 |
| Voice fit | ✓ | Sharp Syndicate-specific voice — "knows exactly how bad the terms look." | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Major tier of the 2×2 matrix; `value_rating=2` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field (Andy, S139; schema_cleanup_log.md #21, closed). |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135. Target-hinder, major tier (−2) of the `ps_shift` 2×2 matrix. Magnitude mirrors the established Intel Token Hinder precedent (PM02 L242). Design-reviewed S139.*

```python
SYN.MOD.25 = Card(
    id      = "SYN.MOD.25",  card_id = "SYN.MOD.25",  version = "v0.1",
    name    = "Predatory Terms Exposed",
    tagline = "The fine print, read aloud, in public.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A rival's finance practices become public knowledge — Syndicate knows exactly how bad the terms look read aloud.",
    arbiter_note = "Same target-resolution behavior as SYN.MOD.24, major tier (Andy, S139).",
)
```

---

### SYN.MOD.26 — BULK CONTRACT

#### Design Rationale
Common tier (n=1) of Syndicate's `cost_reduction` pair, PA-only per §6.3. Standing-agreement framing fits capital doctrine cleanly.

#### Card Story
A standing agreement lowers the price of doing this again — the relationship was worth the investment.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Standing-agreement discounting fits capital doctrine. | Art 00 §7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier; `value_rating=1` mirrors tier. | PM02 L256, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Correctly attaches at §9.2. | Art 03 §9.2 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135. Common cost_reduction tier (n=1). PA-only per §6.3. Design-reviewed S139.*

```python
SYN.MOD.26 = Card(
    id      = "SYN.MOD.26",  card_id = "SYN.MOD.26",  version = "v0.1",
    name    = "Bulk Contract",
    tagline = "A standing agreement makes doing this again considerably cheaper.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=1),  # PA-only (§6.3)
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A standing agreement lowers the price of doing this again — the relationship was worth the investment.",
    arbiter_note = "PA host only. Attach at Dispatch (Art 03 §9.2) alongside the declared PA.",
)
```

---

### SYN.MOD.27 — LINE OF CREDIT

#### Design Rationale
Capstone tier (n=2) of Syndicate's `cost_reduction` pair, closing the faction set and the full 132-card ModActionCard corpus (Ring + all 5 factions). Same flat-vs-proportional caveat as the rest of the corpus's cost_reduction capstones.

#### Card Story
Pre-arranged financing discounts what an action costs to mount — the capital was already standing by.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pre-arranged-financing is capital doctrine at its cleanest. | Art 00 §7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, flat 2-unit reduction not checked against any specific PA's cost — same open question across all 12 cost_reduction capstones in the full corpus. | PM02 L256; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Correctly attaches at §9.2. | Art 03 §9.2 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (flat-vs-proportional cost_reduction magnitude, 04-n157) |  |

*S135. Capstone cost_reduction tier (n=2). Completes the faction-set ModActionCard pattern-set for all 5 factions. **Design-reviewed S139 — closes the Syndicate set (12/12) and, with it, the full 132-card ModActionCard corpus (72 Ring + 60 faction) design-review pass, 09-16 step 3.***

```python
SYN.MOD.27 = Card(
    id      = "SYN.MOD.27",  card_id = "SYN.MOD.27",  version = "v0.1",
    name    = "Line of Credit",
    tagline = "The financing was already arranged. This just draws on it.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Syndicate faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Pre-arranged financing discounts what an action costs to mount — the capital was already standing by.",
    arbiter_note = "Capstone cost_reduction tier — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157). Completes all 5 factions' ModActionCard pattern-set (09-06/04-n157).",
)
```

---

