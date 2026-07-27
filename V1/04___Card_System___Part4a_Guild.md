## Guild
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#guild-covert-operations) · [Public Acts](#guild-public-acts)

---

### Guild — Covert Operations
[↑ Guild](#guild)

| Card | Name |
|------|------|
| [GUI.CA.1](#c11-fortify-structure) | Fortify Structure |
| [GUI.CA.2](#c12-materials-acquisition) | Materials Acquisition |
| [GUI.CA.3](#c13-foundation-rights) | Foundation Rights |
| [GUI.CA.4](#c14-construction-crew) | Construction Crew |
| [GUI.CA.5](#c15-infrastructure-yield) | Infrastructure Yield |
| [—](#guild-labor-contract) | Labor Contract |
| [GUI.CA.10](#guica10--development-order) | Development Order |

### GUI.CA.1 — FORTIFY STRUCTURE
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive structural defense card. The hardest counter to STD.CA.2 Demolish in the set — not a threshold reduction (STD.CA.10 Protect) but total immunity. Cost vs reward: 1 Capacity is relatively cheap for full immunity; the Beat 2 commitment is the real cost, since you're betting a slot that your structure will be targeted this round. Guild's structural investment is its primary territorial asset; this card formalizes that the Guild defends what it has built.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Structural reinforcement as covert preparation — fortification work is done quietly before Beat 3 resolution window. Guild-exclusive competency; no other faction has the structural standing to claim total demolition immunity. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | "The Guild does not abandon what it has built" is the doctrine statement. Network's "what's inside them" is the sharpest counter-perspective. Three perspectives only (Guild, Network, Directorate) — FactionSpecific card; Ghost and Syndicate absence acceptable. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild-exclusive card; structural defense is core Guild doctrine. Portrait submitter=+1 captures this. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: fortification is covert prep. FactionSpecific (Guild): total immunity is Guild's unique structural competency, not available to others. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Territory` — per Art 04b §4.6, Protect distributes to target's layer; target is StructureBlock (Territory). `function = Protect`, `subject = StructureBlock` — correctly scoped. | Art 04b §4.6, §5 |
| Balance | ✓ | Beat 2 positional wager; wrong-read wastes slot. 1 Capacity cost. Immunity is total but Quarter-limited; one play protects one structure only. | Art 02 §7, §8 |
| Effect duration | ✓ | Quarter-limited: immune flag persists until end of Quarter. Appropriate for a structural defense card. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` — Automatic at Beat 2. | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). Guild's structural-investment doctrine grounds the affinity. | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: Guild structure in target district. | Art 01 §6, §7 |
| Supported by components | ✓ | StructureBlock (restriction + immunity target); Capacity cost. | Art 02 §7, §8 |
| Supported by game procedure | ⚠ | Submitted at Dispatch (Art 03 §9.1); Beat 2 row (Art 03 §9.4.0 Beat 0); immunity flag applied at Beat 3 when STD.CA.2 Demolish resolves (Art 03 §9.4.2 Beat 3). **Open:** Art 03 §9.4.2 Beat 2 covers Countermeasures and Protect only — no procedure defined for Fortify Structure immunity flag. Gap in Art 03. | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing` entirely. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Capacity only, typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **Art 03 §9.4 procedure gap:** §11 Beat 2 section does not include a procedure for applying the Fortify Structure immunity flag. Extension required before GUI.CA.1 can be fully procedurally supported.
- **Arbiter note:** ARBITER retains awareness after Beat 2 opens. Immunity applied when STD.CA.2 Demolish resolves in Beat 3. Verify Art 03 §9.4.2 Beat 2 extension covers this step.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.CA.1 = Card(
    id      = "GUI.CA.1",  card_id="GUI.CA.1",  version = "v1.1",
    name    = "Fortify Structure",
    tagline = "Reinforce a structure against demolition this Quarter.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Protect,  subject = StructureBlock,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = 1,
    trigger         = None,
    resolution_type = PositionalWager,
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = StructureBlock,

    target_taxonomy=None,
    affinity    = None,
    restriction = district(target).faction(acting).structure > 0,
    cost        = Capacity * 1,

    success     = district(target).faction(acting).structure.set_flag(immune_to_demolish=True),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "The Guild does not abandon what it has built.",
    perspectives = {
        Guild:       "Reinforcement is not fear. It is preparation.",
        Network:     "Hardened walls are preparation. What's inside them decides whether the cost was worth it.",
        Directorate: "A structure immune to demolition is a structure immune to code review. We notice these arrangements.",
    },
)
```

---

### GUI.CA.2 — MATERIALS ACQUISITION
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive economic counter to demolition — not a defense card but a revenue card. The Guild names a target faction at submission, betting a Beat 2 slot that this faction will execute STD.CA.2 this Quarter. Cost vs reward: zero resource cost; the action slot itself is the bet. Success mirrors STD.CA.2's cost exactly (1 native + 1 district native) — intentionally self-calibrating; if STD.CA.2's cost changes in playtesting, GUI.CA.2's reward scales automatically. A wrong read wastes the slot with no other loss.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Positioning to recover demolition costs before demolition happens — uniquely Guild, fits the game's economic-intelligence frame. Beat 2 commitment watching for opponent's Beat 3 action is a clean trigger structure. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Three perspectives (Guild, Syndicate, Ghost) — FactionSpecific card; acceptable. Syndicate's "we simply call it by a different name" and Ghost's "already told us what it knows" both provide doctrinal depth. | Art 00 §7 |
| Doctrine alignment | ✓ | `target_faction = faction.opponent`, `doctrine_mod = None` — explicit design choice. Recovery amount mirrors STD.CA.2's cost regardless of doctrinal distance; the Guild gets paid the same whoever demolished. Correct. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: observation and positioning is covert; payment materializes via case mechanism. FactionSpecific (Guild): treating demolition as a Guild service is uniquely Guild doctrine. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Economy` — returning NativeResource is capital flow, correctly Economy under Art 04b §4.4. `function = Add`, `subject = NativeResource` — trigger-context Add is the correct primitive. | Art 04b §4, §5 |
| Balance | ✓ | Zero resource cost; action slot is the only cost. Trigger-contingent — wrong read wastes slot with no other penalty. First qualifying Demolish from named faction only. | Art 02 §8 |
| Effect duration | ✓ | Instantaneous: resources delivered once when trigger fires. No persistent state. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | `trigger = faction(target).completes(CovertOp, id=STD.CA.2)` — well-defined; ARBITER confirms at Beat 3. Note: `id=STD.CA.2` uses variable name, not integer — update to `id=2` when DB integers assigned (non-material; carry). | Art 04 (STD.CA.2) |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). | Art 04 §6.2 |
| Supported by zones | N/A | `target_district = None` — trigger monitors named opponent globally, not district-specific. | — |
| Supported by components | ✓ | NativeResource (Art 02 §8); STD.CA.2 Demolish as trigger source. | Art 02 §8; Art 04 (STD.CA.2) |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); placed in Beat 2 row (Art 03 §9.4.0 Beat 0); trigger fires when named faction completes STD.CA.2 at Beat 3 (Art 03 §9.4.2 Beat 3); delivery via ARBITER case (Art 07). | Art 03 §9, §11; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing` entirely. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None` — the action slot itself is the wager. | Art 00a §9.2 |

#### Outstanding Issues

- **Arbiter note:** ARBITER confirms trigger at Beat 3. Only the first qualifying Demolish from the named faction this Quarter triggers. Effect delivered in case.
- **Trigger notation (non-material):** `id=STD.CA.2` is a variable name reference. Update to `id=2` when DB integers are assigned.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.CA.2 = Card(
    id      = "GUI.CA.2",  card_id="GUI.CA.2",  version = "v1.1",
    name    = "Materials Acquisition",
    tagline = "Recover the costs of demolition as subcontract payment.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Economy,  function = Add,  subject = NativeResource,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = 3,
    trigger         = faction(target).completes(CovertOp, id=STD.CA.2),
    resolution_type = PositionalWager,
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = NativeResource,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = None,

    success     = (
        faction(acting).resource.native += 1,
        faction(acting).resource.native += 1
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "In New Meridian, even demolition is a Guild service.",
    perspectives = {
        Guild:     "We do not need to swing the hammer ourselves. We simply ensure we are paid when someone else does.",
        Syndicate: "Positioning to profit from someone else's action before they take it. The instinct is sound. We simply call it by a different name.",
        Ghost:     "A faction that announces it expects demolition before demolition happens has already told us what it knows.",
    },
)
```

---

### GUI.CA.3 — FOUNDATION RIGHTS
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive first-entry card for unclaimed districts. Unclaimed territory has no established resource infrastructure, hence Capacity-only cost. Threshold 25 reflects genuine first-mover difficulty — unclaimed territory resists entry even for the faction with the deepest historical claim. Crit success upgrades presence to presence+structure (immediate foothold). Crit fail is politically the most sensitive outcome: a failed foundation claim is a regulatory event, and the Directorate receives an Intel Token silently. Guild never knows the paper trail was created.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | First-entry territorial claim as covert operation — unannounced land assertion fits Guild's historical-precedence doctrine. The Directorate's jurisdictional counter makes the doctrinal tension mechanical rather than just narrative. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | "The Guild was here before the city had a name" is the doctrine statement. Three perspectives (Guild, Network, Directorate) — FactionSpecific card; acceptable. Directorate's "legal process, not archive" is the sharpest counter. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild territorial-precedence doctrine (first-mover claim). Crit fail delivers Intel Token to Directorate — Directorate's regulatory oversight role is doctrinal, not incidental. Guild portrait submitter=+1 captures alignment. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Guild) — unannounced territorial claim. Covert until established. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Territory` — placing first presence is a territorial operation. `function = Add`, `subject = PresenceToken` — correctly scoped. Crit success adds StructureBlock (stacks with success; same layer). | Art 04b §4, §5 |
| Balance | ⚠ | Threshold 25 + ring_mod {0: −15} = effective threshold 10 in Ring 0. **Open:** Near-automatic for unclaimed Ring 0 districts — should first-entry be that easy? Consider raising base to 35–40. Crit success (presence + structure simultaneously) is a significant leap; confirm intent. | Art 01 §7; Art 02 §6, §7 |
| Effect duration | ✓ | Permanent: presence and structure persist until removed. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). `failcrit` dispatches IntelToken to Directorate — game effect, not Portrait shift (DIR.PA.2 clear). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: total presence == 0 (unclaimed only). | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken (success); StructureBlock (crit success); Capacity cost; IntelToken to Directorate on crit fail. | Art 02 §6, §7, §8; Art 02 §12 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); Beat 3 row (Art 03 §9.4.0 Beat 0); d100 threshold 25 with ring_mod; ARBITER silent IntelToken delivery to Directorate on crit fail (Art 03 §9.4.2 Beat 3; Art 07). | Art 03 §9, §11; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing` entirely. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `d100`; success/successcrit/failcrit populated (fail=None), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Capacity only, typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **Balance — Ring 0 threshold:** Effective threshold 10 in Ring 0 (25 − 15). Near-automatic for unclaimed city-center districts. Consider raising base threshold to 35–40. Confirm before v1.2.
- **Crit success design:** Success = presence only; crit success stacks +structure. Verify this is the intended "presence + structure" foothold, not just structure replacing presence.
- **Arbiter note:** On crit fail: deliver 1 Intel Token naming Guild to Directorate via case. Do not notify Guild.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.CA.3 = Card(
    id      = "GUI.CA.3",  card_id="GUI.CA.3",  version = "v1.1",
    name    = "Foundation Rights",
    tagline = "Claim a foothold in territory no other faction has entered.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Add,  subject = PresenceToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 25,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    value_rating = 1,
    trigger         = None,
    resolution_type = Probabilistic,
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = district(target).presence.total == 0,
    cost        = Capacity * 1,

    success     = district(target).faction(acting).presence += 1,
    successcrit = district(target).faction(acting).structure += 1,
    fail        = None,
    failcrit    = game.dispatch(Directorate, IntelToken(faction=acting, quarter=game.quarter)),

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "The Guild was here before the city had a name.",
    perspectives = {
        Guild:       "Unclaimed territory is not unknown to us. We have records going back further than anyone else at this table.",
        Network:     "The Guild's records go back further than ours. What they do with that history is what we watch.",
        Directorate: "Precedence is established through legal process, not through whoever kept the longer archive.",
    },
)
```

---

### GUI.CA.4 — CONSTRUCTION CREW
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive rush-construction card — bypasses STD.CA.1's presence prerequisite at premium cost and elevated difficulty. Threshold 65 models that unauthorized construction (without prior presence) is significantly harder than licensed work. Cost: 3 Capacity vs STD.CA.1's 1 faction native + 1 district native — a premium for skipping the prerequisite. Crit fail is deliberately multi-faction: failed unauthorized construction triggers both Ghost surveillance and Syndicate resource extraction — the city's two most opportunistic actors benefit from the Guild's overreach.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Rush construction without prior presence — unauthorized build is covert, high-risk, and distinctly Guild. Ghost and Syndicate as crit-fail beneficiaries is doctrinally perfect (the two most opportunistic actors). | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Three perspectives (Guild, Network, Ghost) — FactionSpecific card; acceptable. Ghost's "better at covert operations than they admit" is the sharpest outside read. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild construction doctrine (rush, without permission). Crit fail rewards Ghost (Intel Token) and Syndicate (district native) — explicitly doctrinal: the two most opportunistic actors benefit from Guild overreach. No opponent target → doctrine_mod N/A. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: unauthorized construction is covert until established. FactionSpecific (Guild): rush-build without prerequisites is exclusively Guild. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ⚠ | `layer = Submission` — primary design intent is removing the STD.CA.1 presence prerequisite (a restriction on a CovertOperation). Territorial outcomes (presence + structure) are the consequence, not the driver. `function = RemoveRestriction` is not in `ref_taxonomy.md`'s Function Vocabulary (Add/Remove/Redirect/Modify/Protect/Block/Copy/Reveal/Shift/Corrupt only) — confirmed by `v_card_mechanical_alignment` (DB), which shows Abstract Function for this card. `Modify` ("alters cost, value, or attribute without changing fundamental state") looks like the closer documented fit for "removes a restriction," but not changed here. | Art 04b §4, §5 |
| Balance | ✓ | High cost (3 Capacity), high threshold (65). Crit fail rewards both Ghost (Intel Token) and Syndicate (district native) — asymmetric penalty for overreach. Net: saves STD.CA.3+STD.CA.1 sequential plays at the cost of one high-risk probabilistic slot. | Art 02 §6, §7, §8; Art 02 §12 |
| Effect duration | ✓ | Permanent: presence and structure placed on success persist. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). `failcrit` delivers IntelToken/native to opponents — game effects, not Portrait shifts (DIR.PA.2 clear). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: no existing Guild structure in target district. Ring mods apply normally. | Art 01 §6, §7 |
| Supported by components | ✓ | PresenceToken + StructureBlock on success; Capacity cost; IntelToken to Ghost + district native to Syndicate on crit fail. | Art 02 §6, §7, §8; Art 02 §12 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); Beat 3 row (Art 03 §9.4.0 Beat 0); d100 threshold 65 with ring_mod; ARBITER delivers crit fail rewards to Ghost and Syndicate (Art 03 §9.4.2 Beat 3; Art 07). | Art 03 §9, §11; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing` entirely. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `d100`; success/successcrit/failcrit populated (fail=None), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capacity + Findings, both typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **Arbiter note:** Crit fail: deliver 1 Guild Intel Token → Ghost and 1 district native → Syndicate via case. Do not notify Guild.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.CA.4 = Card(
    id      = "GUI.CA.4",  card_id="GUI.CA.4",  version = "v1.1",
    name    = "Construction Crew",
    tagline = "Build a structure before your presence is fully established.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Submission,  function = RemoveRestriction,  subject = CovertOperation,

    beat            = 3,
    resolution      = d100,
    threshold       = 65,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    value_rating = 3,
    trigger         = None,
    resolution_type = Probabilistic,
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = district(target).faction(acting).structure == 0,
    cost        = Capacity * 2 + Findings * 1,

    success     = (
        district(target).faction(acting).presence += 1,
        district(target).faction(acting).structure += 1
    ),
    successcrit = district(target).faction(acting).presence += 1,
    fail        = None,
    failcrit    = (
        game.dispatch(Ghost, IntelToken(faction=acting, quarter=game.quarter)),
        game.transfer(district(target).resource.native, 1, faction(Syndicate))
    ),

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "The Guild does not always wait for permission.",
    perspectives = {
        Guild:    "Sometimes the crews arrive before the paperwork. This is not an accident.",
        Network:  "We know this method. Presence before permission is how this city was actually built.",
        Ghost:    "Establishing presence before authorization is requested — the Guild is better at covert operations than they admit.",
    },
    design_note  = "Cost reasoning: 2 Capacity + 1 Findings (Mid-tier). Findings identify the un-zoned loopholes necessary to bypass prerequisites and break ground immediately.",
)
```

---

### GUI.CA.5 — INFRASTRUCTURE YIELD
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild-exclusive passive income card — the economic expression of territorial control. Zero cost reflects that drawing from established infrastructure is not a new expenditure; it is the return on prior investment. The sole gate (Established or Dominant control tier) makes this card valuable precisely because it rewards maintained territorial control. Counter-lever is territorial: the card becomes unplayable if the Guild loses control tier, creating natural interdependence with STD.CA.1/STD.CA.3.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Passive income from controlled infrastructure is the natural economic expression of Guild territorial control. Covert framing (yield not publicly attributed) fits the operations register. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Three perspectives (Guild, Syndicate, Directorate) — FactionSpecific card; acceptable. Syndicate's "billing us for the water" is the sharpest outside read. | Art 00 §7 |
| Doctrine alignment | ✓ | Guild infrastructure-ownership doctrine — return on prior investment. Guild↔Syndicate are Opposed: Syndicate believes it should capture this yield, not the Guild ("billing us for the water"). No opponent target → doctrine_mod N/A; Syndicate portrait entry warrants consideration (see Portrait validity). | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: yield is not publicly attributed. FactionSpecific (Guild): infrastructure-ownership income is exclusively Guild. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Economy` — adding NativeResource is capital flow, correctly Economy under Art 04b §4.4. `function = Add`, `subject = NativeResource` — correctly scoped. | Art 04b §4, §5 |
| Balance | ⚠ | Zero cost + Automatic + no fail state + repeatable each Quarter. **Open:** Multiple Established/Dominant districts → multiple free native resources per Quarter, uncapped. Consider per-Quarter activation cap (e.g., max 2). Flag for playtesting. | Art 02 §6, §8 |
| Effect duration | ✓ | Instantaneous: +1 native delivered per play. No persistent state; card is re-playable each Quarter if restriction still met. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Guild `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any`. Restriction: Guild must hold Established or Dominant control tier in target district. | Art 01 §6, §7 |
| Supported by components | ✓ | NativeResource (Art 02 §8); control_tier states Established/Dominant (Art 02 §6). | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); Beat 3 row (Art 03 §9.4.0 Beat 0); Automatic resolution at Beat 3 (Art 03 §9.4.2 Beat 3). | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing` entirely. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None` — passive income, no resource spent. | Art 00a §9.2 |

#### Outstanding Issues

- **Balance — per-Quarter cap:** Zero cost + Automatic means uncapped income at scale. Guild controlling 3+ Established/Dominant districts earns 3+ free native resources per Quarter. Consider cap of 2 activations per Quarter; flag for playtesting.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.CA.5 = Card(
    id      = "GUI.CA.5",  card_id="GUI.CA.5",  version = "v1.1",
    name    = "Infrastructure Yield",
    tagline = "Draw resources from infrastructure you have already built.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Economy,  function = Add,  subject = NativeResource,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = 1,
    trigger         = None,
    resolution_type = Transactional,
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = district(target).faction(acting).control_tier IN [Established, Dominant],
    cost        = None,

    success     = faction(acting).resource.native += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "The Guild built New Meridian's infrastructure. Drawing from it is not theft. It is dividend.",
    perspectives = {
        Guild:       "We built this. Every unit we draw from it was always ours.",
        Syndicate:   "The Guild built the pipes. They are billing us for the water. We respect the position even if we resent the rate.",
        Directorate: "Infrastructure built under city contract belongs to New Meridian, not to the builder. We have the original agreements.",
    },
)
```

---

### Guild — LABOR CONTRACT
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Construction analogue to GUI.CA.2 Materials Acquisition — GUI.CA.2 covers demolition revenue, Labor Contract covers construction revenue. Together they implement the Guild doctrine that no structural change to New Meridian happens without Guild being paid. Beat 2 positional wager: Guild names a faction and bets an action slot on that faction building this Quarter. Zero resource cost means a wrong read loses only the slot. Payout mirrors STD.CA.1's cost (2 Capacity), making the card self-calibrating if STD.CA.1's cost changes in playtesting.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Construction fee mechanic — Guild monetises any faction's STD.CA.1 play; analogue to GUI.CA.2 Materials Acquisition (demolition revenue) completing the Guild doctrine that no structural change to New Meridian happens without Guild payment | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; limited perspectives in current spec — full voice set expected (confirm complete in code block) | Art 00 §7 |
| Doctrine alignment | ✓ | Guild only; zero resource cost (slot IS the bet); payout 2 Capacity mirrors STD.CA.1.cost — self-calibrating on balance pass; Beat 2 positional wager fits the "bet on opponent building" play style | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Guild) — Guild's passive revenue model | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/NativeResource — trigger-context Add is the correct primitive; STD.CA.3 exclusion confirmed | Art 04b §4, §5 |
| Balance | ✓ | Payout 2 Capacity mirrors STD.CA.1.cost — self-calibrating | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: Capacity delivered at Beat 3 when trigger fires | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | Trigger = STD.CA.1 completion by named faction; first qualifying play only; Beat 2 positional wager monitors trigger across the round | Art 04 (STD.CA.1) |
| Portrait validity | ✓ | Confirm portrait entries present in code block — Guild faction-specific expected | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None; trigger monitors named faction globally | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource (Capacity); STD.CA.1 as trigger source; no new components | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 submission; trigger confirmed at Beat 3; ARBITER case delivery | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing`. Also missing `persistence`/`persistence_condition`/`persistence_effect` entirely — not just unset, absent from the code block (unlike every other Guild CA card, which at least declares `persistence=Immediate`). Flagged, not fixed. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None` — the action slot itself is the wager, same shape as GUI.CA.2. | Art 00a §9.2 |

#### Outstanding Issues

- **STD.CA.3 scope confirmed excluded:** Labor Contract is a financial claim on physical construction (STD.CA.1) only. Campaign (STD.CA.3) does not trigger — no labor fee on presence/influence activity.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.CA.6 = Card(
    id      = "GUI.CA.6",  card_id="GUI.CA.6",  version="v1.0",  # ID pending PM05 04-n1
    name    = "Labor Contract",
    tagline = "Collect subcontract payment when a faction develops district infrastructure.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Economy,  function = Add,  subject = NativeResource,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = 3,
    trigger         = faction(target).completes(CovertOp, id=STD.CA.1),
    resolution_type = PositionalWager,
    outcome_type    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = NativeResource,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = None,

    success     = (
        faction(acting).resource.native += 1,
        faction(acting).resource.native += 1,
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = "In New Meridian, every foundation poured is a Guild invoice.",
    perspectives = {
        Guild:       "We do not ask to be compensated. We ensure that we are.",
        Directorate: "The Guild has found a way to treat infrastructure development as a private revenue stream. This requires a regulatory response.",
        Network:     "Every build is a Guild fee. Every fee is a constraint. The city grows on Guild's terms.",
    },
    design_note  = "Construction analogue to GUI.CA.2 Materials Acquisition. Together with GUI.CA.2 and 04-n2 passive rule: no faction demolishes or builds in New Meridian without Guild being paid. Trigger is STD.CA.1 only — Labor Contract is a financial claim on physical construction, not influence or presence activity. Payout mirrors STD.CA.1.cost (2 Capacity). First qualifying STD.CA.1 from named faction only.",
    arbiter_note = "At Beat 3: confirm whether named faction completed STD.CA.1 this Quarter. First qualifying play only. If triggered: deliver 2 Capacity to Guild's Dispatch Case.",
)
```

---


---

### Guild — Public Acts
[↑ Guild](#guild)

| Card | Name |
|------|------|
| [GUI.PA.1](#p09-civic-works-mandate) | Civic Works Mandate |
| [GUI.PA.2](#p10-infrastructure-bond) | Infrastructure Bond |
| [GUI.PA.9](#guipa9--city-ledger) | City Ledger |
| [GUI.PA.10](#guipa10--joint-development) | Joint Development |

---

### GUI.CA.7 — BUYOUT CLAUSE *(stub)*
[↑ Covert Operations](#guild-covert-operations)

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
| Data schema validation | ⚠ | Pending 04-n70. `success` field is a bare string literal instead of a MutationExpr — same fossil-card pattern flagged on GHO.CA.13/14/15. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing`/`ring_mod`/`persistence`/`portrait`/`perspectives` entirely. Flagged, not fixed. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

```python
GUI.CA.7 = Card(
    id      = "GUI.CA.7",  card_id="GUI.CA.7",  version = "v1.0",
    name    = "Buyout Clause",
    tagline = "Liquidate an opponent's real estate through an unblockable coercive eviction.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Remove,  subject = PresenceToken,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    trigger         = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    cost        = Capacity * 2 + Capital * 1,

    success     = "Guild pays 2 target.native resources to target_faction; arbiter.remove(presence_chip, district=target_district, faction=target_faction, count=1)",
    
    design_note = "Guild's territorial response gap filled. Coercive eviction via buyout. Cost reasoning: 2 Capacity + 1 Capital (Mid-tier). Liquidating real estate out from under an opponent."
    value_rating = 2,
)
```

---

---

### GUI.CA.8 — BUILDING INSPECTION *(stub)*
[↑ Covert Operations](#guild-covert-operations)

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
| Data schema validation | ⚠ | Pending 04-n70. `success` field is a bare string literal instead of a MutationExpr — same fossil-card pattern flagged on GHO.CA.13/14/15 and GUI.CA.7. Missing `card_id`/`doctrine_mod`/`boost`/`ps_framing`/`ring_mod`/`persistence`/`portrait`/`perspectives` entirely. Design note mentions a retired "Bribe" mechanic with no other trace in the spec. Flagged, not fixed. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

```python
GUI.CA.8 = Card(
    id      = "GUI.CA.8",  card_id="GUI.CA.8",  version = "v1.1",
    name    = "Building Inspection",
    tagline = "Condemn an opponent's building via weaponized zoning code.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,
    layer   = Territory,  function = Remove,  subject = StructureBlock,
    beat    = 3,  resolution = d100,  threshold = 60,
    cost    = Capacity * 1 + Mandate * 1,
    success = "Remove 1 target Structure Block. Guild gains +1 PS.",
    design_note = "A thematic variant of STD.CA.2 (Demolish). Bribe removed to keep resolution strictly blind via Arbiter."
    value_rating = 2,
)
```

### GUI.CA.9 — WORKS GUARANTEE
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild's construction certainty card — a Beat 2 positional play that suppresses the dice on a named Guild Beat 3 d100 CA and fires that CA's full success+successcrit outcome in two districts simultaneously. The target profile carries two declarations: the CA being guaranteed (by card ID) and a second district. At Beat 3 the named CA resolves without a roll — success+successcrit applies to the CA's own declared district AND to Works Guarantee's declared district. The d100 is not rolled; failcrit consequences of the named CA are suppressed.

Best target: GUI.CA.4 Construction Crew (success+successcrit = 2 presence + 1 structure). Double-fire yields 4 presence + 2 structures across two districts in one Beat 3 slot — immediate Established presence in two districts where Guild had none. Total cost (CA.4 + Works Guarantee + 2 dispatch slots) is high; this is an early-game land-grab or a late-game disruption play. CA.3 Foundation Rights is the cheaper-target variant (two unclaimed districts each receiving 1 presence + 1 structure).

Distinct from STD.CA.10 Protect (raises attacker threshold on incoming CAs) and GUI.CA.1 Fortify Structure (protects existing structure). This card does not defend — it guarantees construction output.

#### Card Story
⚠ Story pending.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Guild's institutional weight guaranteeing a construction commitment in two districts — doctrinal expression of "when Guild commits, it gets built" | Art 00 §7 |
| Voice fit | ✓ | Five perspectives: Guild matter-of-fact certainty; Directorate notes the institutional channel; Ghost reads it as operational pre-commitment; Network clocks the dual announcement; Syndicate prices the certainty premium | Art 00 §7 |
| Doctrine alignment | ✓ | Guild ceiling Resolution card; Beat 2 Automatic; Portrait +1; construction certainty is the Guild doctrine made mechanical | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Guild) — the guarantee is covert; no public announcement of which CA is being backed | Art 04 §6.2 |
| Taxonomy fit | ✓ | Resolution / Modify / CovertOperation — suppresses d100 roll on a named target CA, converting it to guaranteed success+successcrit; the card modifies another Covert Operation's resolution, so Subject=CovertOperation is correctly-scoped, already-valid vocabulary. | Art 04b §4 |
| Balance | ⚠ | High total cost (CA cost + 2C + 1 district native + 2 dispatch slots); ceiling output (4 presence + 2 structures for CA.4); restriction checks at Beat 0 limit abuse — playtesting required | Art 02 §6–§7 |
| Effect duration | ✓ | Beat 2 effect (guarantee registered); Beat 3 CA output is Permanent (structures/presence placed) | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — guarantee resolves at Beat 3 with the target CA; no lingering marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Guild +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district B; named CA's own target_district = district A; both validated at Beat 0 per Art 01 §6.5 | Art 01 §6.5 |
| Supported by components | ✓ | PresenceToken + StructureBlock output via named CA; no new components; cost from Guild resource pool. The card also declares `target_ca = ca.guild.beat3.d100` — a targeting field not in `design_reference_card_system.md`'s documented Targeting field group (`target_district`/`target_faction`/`target_object`/`target_taxonomy`/`declared_params`). Whether this needs to be a confirmed schema extension or should be re-expressed via `declared_params` (which already exists for exactly this "faction-declared free-form parameter" purpose) isn't resolved. | Art 02 §6–§8 |
| Supported by game procedure | ⚠ | Beat 0: ARBITER validates named CA and district B restriction; Beat 2: guarantee registered; Beat 3: named CA resolves without roll, output fires twice. Double-fire procedure is new — confirm against Art 03 §9.4 | Art 03 §9.4 |
| Data schema validation | ⚠ | New card — DB registration required. Also missing `card_id`/`boost`/`ps_framing` (`doctrine_mod=None` is present). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`) — the "double-fire" is two applications of the same success outcome, not a second resolution tier. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capacity + district native, both typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.CA.9 = Card(
    id      = "GUI.CA.9",  card_id="GUI.CA.9",  version = "v0.1",
    name    = "Works Guarantee",
    tagline = "Commit to both sites. Both get built.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Resolution,  function = Modify,  subject = CovertOperation,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = 3,
    trigger         = None,
    resolution_type = PositionalWager,
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.named,       # district B — second fire location
    target_faction  = None,
    target_object   = None,
    target_ca       = ca.guild.beat3.d100,  # named Guild Beat 3 d100 CA (declared in target profile)

    affinity    = None,
    restriction = (
        target_ca in game.dispatch.guild.beat3                       # named CA is submitted this Month
        and target_ca.restriction(district=target_district) == True  # district B satisfies CA's own restriction
    ),
    cost = Capacity * 2
         + district.target_district.native * 1,

    success = (
        target_ca.resolve(district=target_ca.target_district, outcome=success_and_successcrit),
        target_ca.resolve(district=target_district,           outcome=success_and_successcrit),
        # d100 roll suppressed; named CA's failcrit consequences do not fire
    ),

    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    narrative    = None,
    perspectives = {
        Guild:       "Both sites are committed. The crews are already moving. The question was never whether — only where.",
        Directorate: "The Guild has pre-authorized both sites through the same institutional channel. Efficient. We note the district selections.",
        Ghost:       "Pre-committed construction at two sites simultaneously. We mark both districts as active before Beat 3 opens.",
        Network:     "Guild's already decided. Whatever goes in the grid tonight, those two districts are getting built. We're watching which ones.",
        Syndicate:   "Certainty commands a premium. Guild is paying it. The output justifies the cost — barely, but it does.",
    },
    design_note  = "Construction certainty card. Target profile = {target_ca (named Guild Beat 3 d100 CA), target_district (district B)}. Beat 2 Automatic: registers guarantee. Beat 3: named CA resolves without roll — success+successcrit fires in CA's own district A AND in district B. Named CA's failcrit suppressed. Best target: GUI.CA.4 (success+crit = 2 presence + 1 structure per district; double-fire = 4 presence + 2 structures). CA.3 variant: 2 presence + 2 structures in two unclaimed districts. District B must satisfy the named CA's own restriction (checked at Beat 0). Total cost: this card (2C + 1 district native) + named CA cost + 2 dispatch slots.",
    arbiter_note = "Phase B: Guild declares Works Guarantee with target profile = {CA-ID, district B}. Beat 0: (1) confirm named CA is Guild-submitted and d100; (2) confirm district B satisfies named CA's restriction (e.g., for CA.4: no existing Guild structure in district B; for CA.3: total presence in district B = 0). If either check fails: Works Guarantee void, cost returned. Beat 2: Works Guarantee resolves — record guarantee against named CA. Beat 3: named CA does NOT roll d100. Apply named CA's success+successcrit outcomes to district A (CA's declared target), then apply the same success+successcrit outcomes to district B. Named CA's failcrit consequences (Intel Tokens, resource transfers) are suppressed.",
)
```

---

### GUI.CA.10 — DEVELOPMENT ORDER
[↑ Covert Operations](#guild-covert-operations)

#### Design Rationale
Guild's Grant Deed card — parallel to SYN.CA.8 Land Title in mechanism, distinct in doctrine. Land Title is a capital claim: "let someone else build, then collect." Development Order is a construction rights filing: "when this district develops, Guild is the builder of record." Both deliver GD-01 Grant Deed to the acting faction's Dispatch Case via ARBITER; both fire when any faction places a structure block in the named district.

Cost: 4 Capacity + 1 `district(target).native` — a modest bump reflecting that GD-01's fire effect is trigger-conditional, not a guaranteed payoff, so cost scales sub-proportionally to the deed's raw value — the district-native term is the cross-resource commitment that satisfies the §9.2 ceiling gap (04-n119). Guild must engage with the target district's resource economy to file the order. Restriction: no Guild structure in target district (same gate as GUI.CA.4) and not Chorus Node. Automatic resolution — filing a development order doesn't require a roll. Multiple orders on the same district permitted; cost-governed.

Doctrinal distinction from SYN.CA.8: Guild's deed doesn't extract value from others' development. It establishes Guild's right to participate. The fire effect (+1 Presence Token + 1 Structure Block per GD-01) reflects Guild crews arriving to execute the build — not just a claim on paper.

#### Card Story
The Guild files the development order before a single wall goes up. The district is undeveloped — for now. When any faction breaks ground, the permit is already on file. The crews arrive with the first delivery truck.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Construction rights filing on undeveloped district; Guild doctrine-coherent — "builder of record" rather than Syndicate's extractive claim | Art 00 §7 |
| Voice fit | ⚠ | Perspectives pending | Art 00 §7 |
| Doctrine alignment | ✓ | Capacity + district-native cost addresses 04-n119 §9.2 ceiling gap; construction rights framing is Guild-exclusive | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / StructureBlock — ultimate effect is Guild structure + Presence Token via GD-01 fire. The card's own code declares this taxonomy correctly and it's a valid Territory+Add cell, but `card_status` (DB) shows `layer`/`function`/`subject` all `NULL` for GUI.CA.10, flagged `Abstract / No Subject` in `v_card_mechanical_alignment` — a DB/MD sync gap (per `feedback_card_status_sync.md`), not a card content defect. | Art 04b §4 |
| Balance | ⚠ | Payback contingent on any faction building in named district; district-native cost throttles casual play — playtesting required | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent — Grant Deed held until fired or game end | — |
| Persistence | ✓ | Card persistence = Immediate; GD-01 persists in hand | Art 04 §6 |
| Trigger validity | ✓ | trigger = None on this card; trigger lives on GD-01 | — |
| Portrait validity | ✓ | Guild submitter=+1; filing construction rights is doctrine-consistent | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; ChorusNode excluded | Art 01 §6 |
| Supported by components | ✓ | GD-01 Grant Deed (Art 04 §12b.2); component registration pending 04-n26 | Art 02 §6–§8 |
| Supported by game procedure | ⚠ | GD-01 trigger vocab (district-scoped) pending 04-n27; React window pending Art 03 addition | Art 03 §9.4 |
| Data schema validation | ⚠ | New card — DB registration required. `card_id`/`ps_framing` missing from code (has `doctrine_mod`/`boost` as `None`). | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story above | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capacity + district native, both typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **04-n26:** Grant Deed component registration in Art 02 pending.
- **04-n27:** GD-01 trigger vocab (district-scoped `structure_block.placed`) and Art 03 React window pending.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.CA.10 = Card(
    id      = "GUI.CA.10",  card_id="GUI.CA.10",  version = "v0.2",
    name    = "Development Order",
    tagline = "File construction rights before ground is broken. The permit is already on file.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Add,  subject = StructureBlock,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = None,  # scaffolded, not addressed
    trigger         = None,
    resolution_type = Transactional,
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.named,
    target_faction  = None,
    target_object   = None,
    declared_params = None,

    affinity    = None,
    restriction = (faction(Guild).structure_block.count(district(target)) == 0
               and district(target) != ChorusNode),
    cost = Capacity * 4
         + district.target.native * 1,
    boost = None,

    success     = arbiter.dispatch(GrantDeed(district=district(target), holder=faction(acting)), faction(acting).case),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},

    ps_framing   = None,

    narrative    = None,
    perspectives = None,
    design_note  = "Delivers GD-01 Grant Deed (Art 04 §12b.2). Addresses 04-n119 §9.2 ceiling gap: Capacity + district-native cost creates cross-resource commitment SYN.CA.8 Land Title lacks. Restriction (no Guild structure, not Chorus Node) parallels CA.4. Automatic — no roll, no fail. Multiple orders on same district permitted; cost-governed. Doctrinal distinction from SYN.CA.8: Guild establishes construction rights (crews arrive to build); Syndicate files ownership claim (extraction).",
    arbiter_note = "Beat 3: take 1 blank Grant Deed (GD-01) from ARBITER tableau; write target district name in 'district' field and Guild in 'holder' field; place in Guild's Dispatch Case. Card moves to Guild's hand at Debrief.",
)
```

---

### GUI.PA.1 — CIVIC WORKS MANDATE
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
Guild's prestige structure PA — a simultaneous double build in two named districts. One PA slot for two structures is the core value; the cost (2 Capacity + 1 Capital + 1 Mandate) reflects the single-slot efficiency gain of building twice in one PA rather than two sequential single-district builds across two Months. The PS reward (+3) is the highest of any standard or faction-specific single build card, reflecting the scale of the public commitment. Primary counter: Directorate's DIR.PA.1 (Regulatory Override) raises the cost of presence prerequisites; DIR.PA.1 (Issue Directive in prior design, now Regulatory Override) can be deployed against the district beforehand.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Simultaneous dual construction is Guild's maximum public commitment | Art 00 §7 |
| Voice fit | ✓ | Guild on-doctrine; Network (aligned): public commitment scale; Ghost (opposed): acting before the question is answered | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Guild-exclusive: 2 Capacity + 1 Capital + 1 Mandate cross-resource cost, portrait +2 (double structure = doctrinal maximum). Directly serves permanence doctrine. No target_faction → doctrine_mod not applicable | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / StructureBlock — two targets | Art 04b §4 |
| Balance | ⚠ | Cost 2 Capacity + 1 Capital + 1 Mandate (cross-resource, Ceiling-tier). PS +3. Single slot for two structures is efficient — balance review after playtesting | Art 02 §6–§7 |
| Effect duration | ✓ | StructureBlocks = Permanent board state; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Guild +2: submitter-bounded; double structure = maximum doctrinal expression | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.two — both named districts valid; restriction checks each independently | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock (Art 02 §7); PresenceToken — restriction (Art 02 §6); 4 Capacity — Guild faction native (Art 02 §8) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Both districts declared at Phase B; restriction checked at Beat 0; both-or-nothing rule | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`; only `success` populated — no `game.choose_one()` or conditional branching. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capacity ×2 + Capital ×1 + Mandate ×1), correctly typed. Design_note's trailing "Cost reasoning: 2 Capacity + 1 Capital + 1 Mandate (Ceiling-tier)" checked against the dangling-fragment pattern — **correct**, matches the actual cost exactly. | Art 00a §9.2 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.PA.1 = Card(
    id      = "GUI.PA.1",  card_id = "GUI.PA.1",  version="v1.0",
    name    = "Civic Works Mandate",
    tagline = "Declare a public infrastructure program across two districts simultaneously.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Add,  subject = StructureBlock,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = 4,
    trigger         = None,
    resolution_type = Transactional,
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.two,  # both named at Phase B
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = (
        district(target1).faction(Guild).presence > 0 and
        district(target2).faction(Guild).presence > 0 and
        district(target1).faction(Guild).structure == 0 and
        district(target2).faction(Guild).structure == 0
    ),
    cost = Capacity * 2 + Capital * 1 + Mandate * 1,
    boost = None,

    success     = (
        district(target1).faction(Guild).structure += 1,
        district(target2).faction(Guild).structure += 1,
        faction(Guild).standing += 3,
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+2)},
    ps_framing = None,

    narrative    = "The Civic Works Mandate is Guild's strongest public statement: we are not here to compete. We are here to build what New Meridian requires.",
    perspectives = {
        Guild:   "This is the declaration. Two districts, simultaneous, public. This is what we came here to do.",
        Network: "Two districts at once. When Guild commits at this scale, the announcement becomes the infrastructure. The public knows before the cement sets.",  # aligned
        Ghost:   "Guild builds when we have not yet established whether what is being built belongs in the answer. The structures will outlast the certainty they were built on.",  # opposed
    },
    design_note  = "Guild's prestige build PA. Cost reasoning: 2 Capacity + 1 Capital + 1 Mandate (Ceiling-tier). Capital secures the massive land footprint, while Mandate bypasses zoning laws to fast-track construction. Both-or-nothing: if either district fails restriction at Beat 0, full PA is voided. PS +3: highest single-card build reward. Portrait +2: double structure = doctrinal maximum. Counter: Directorate DIR.PA.1 Regulatory Override applied to either district beforehand raises presence-placement costs, potentially blocking prerequisite presence for this card.",
    arbiter_note = "Phase B: two distinct districts named. Beat 0: both restrictions checked simultaneously. If either fails (no Guild presence, or existing structure), entire PA voided; 4 Capacity returned; Guild takes Public Pass. Beat 4: place 1 structure in each declared district; Guild +3 PS.",
)
```

---

### GUI.PA.2 — INFRASTRUCTURE BOND
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
Guild's economic relationship PA. Distinct from STD.CA.9 (Fund) in cost currency (Capacity vs Capital) and mechanism (ongoing income Accord vs one-time payment). Guild pays 1 Capacity (form price, equitable with STD.PA.8 per L200/L201) and delivers 2 native resources to the target as a sweetener — the upfront investment that makes the Accord terms credible and acceptance worthwhile. ARBITER then delivers a blank AccordForm to Guild. Guild drafts the Infrastructure Bond terms (target pays 1 Capacity per Upkeep while Accord active) and places the completed form in the Accord Placement Area at their discretion per Art 06 §9.4. On acceptance, Guild recovers the sweetener over 2 Quarters and profits thereafter. Addresses 04-n11 (Guild↔Network neighbor cooperation): Network is the natural target given pentagram proximity.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Guild public investment in another faction's territory is narratively grounded — infrastructure serves both | Art 00 §7 |
| Voice fit | ✓ | Guild on-doctrine; Directorate (aligned): structural partnership recognition; Syndicate (opposed): extraction reframed as partnership | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Guild investment economy: 2 Capacity upfront, 1 Capacity/Upkeep return. Restriction (Guild Established adjacent) keeps it doctrinally grounded. Portrait +1. Addresses 04-n11 (Guild↔Network neighbor cooperation) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Add / AccordAgreement — the Accord is the primary artifact; resource delivery is the trigger | Art 04b §4 |
| Balance | ✓ | Cost 1 Capacity (form price, per L200/L201) + 2 native delivered to target (sweetener). Income 1 Capacity/Upkeep from target on Accord execution — net positive over 2+ Quarters. PA slot is the primary gate. L201. | Art 02 §6–§7 |
| Effect duration | ✓ | Resource delivery Immediate. AccordForm delivery Immediate; form lifecycle and cross-Quarter persistence governed by Art 06 §9.4. | Art 04 §5 P19; Art 06 §9.4 |
| Persistence | ✓ | Immediate — resource delivery and AccordForm delivery both resolve at Beat 4; form lifecycle governed by Art 06 §9.4. | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Guild +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; restriction uses Guild Established adjacency to target's presence (valid zone-based check) | Art 01 §6–§7 |
| Supported by components | ✓ | NativeResource (target delivery, Art 02 §8); AccordForm (Art 06 §9.2); Capacity × 2 cost (Art 02 §8). | Art 02 §8; Art 06 §9.2 |
| Supported by game procedure | ⚠ | Phase B: target faction named publicly. Beat 4: 2 native delivered; blank AccordForm delivered to Guild. Guild drafts bond terms; places per Art 06 §9.4. Upkeep income tracking requires Accord execution confirmation. | Art 03 Phase B; Art 06 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`; only `success` populated — no `game.choose_one()` or conditional branching. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capacity ×1 + native ×2), correctly typed. | Art 00a §9.2 |

#### Outstanding Issues

- **Upkeep income tracking:** Confirm Accord income procedure (target pays 1 Capacity/Upkeep to Guild at Upkeep Step 6 while Accord active) against Art 06 §9.4 execution model.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.PA.2 = Card(
    id      = "GUI.PA.2",  card_id = "GUI.PA.2",  version="v1.0",
    name    = "Infrastructure Bond",
    tagline = "Publicly extend Guild infrastructure investment to another faction, establishing a formal economic relationship.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Economy,  function = Add,  subject = AccordAgreement,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,  # Neighbor relationship noted for narrative — no threshold variance (Automatic)
    value_rating = 4,
    trigger         = None,
    resolution_type = Transactional,
    outcome_type    = BilateralAgreement,
    persistence     = Immediate,  # resource delivery and AccordForm delivery resolve at Beat 4; form lifecycle governed by Art 06 §9.4
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Guild).influence_tier(district.any_adjacent_to(faction(target).presence)) >= Established,
    cost        = Capacity * 1  # form price → Reservoir
              + Capacity * 2,   # sweetener → delivered to target at success
    boost       = None,

    success = (
        faction(target).resource(native) += 2,  # immediate delivery
        arbiter.deliver(Guild, AccordForm(blank)),  # Guild drafts Infrastructure Bond terms per Art 06 §9.3
    ),

    # BilateralAgreement resolution at Debrief: PS consequences per Art 06 §9.4

    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Guild: PortraitEntry(submitter=+1)},
    ps_framing = None,

    narrative    = "Guild does not give resources away. The Infrastructure Bond is an investment — the terms make that clear.",
    perspectives = {
        Guild:       "We extend this partnership because the infrastructure serves both of us. The terms reflect that.",
        Directorate: "Guild formalizes the relationship before the need becomes urgent. The Accord terms are what the investment was always going to require. This is how structural partners communicate.",  # aligned
        Syndicate:   "Guild packages the extraction as partnership. The initial delivery is cover. The recurring return is the structure. We recognize this.",  # opposed
    },
    design_note  = "Guild economic relationship PA. Cost: 1 Capacity (form price, per L200/L201) + 2 native delivered to target (sweetener — makes Accord terms credible). Accord on acceptance includes 1 Capacity/Upkeep income from target; net positive for Guild in 2+ Quarters. Restriction: Guild must have Established adjacent to target's operations. Distinct from STD.CA.9 Fund (Capital, covert, two-action route). Distinct from STD.PA.8 (bare form, no sweetener). Addresses 04-n11 (Guild↔Network neighbor cooperation).",
    arbiter_note = "Phase B: target faction named publicly. Beat 4: deliver 2 native resources to target immediately; deliver blank AccordForm from ARBITER tableau supply to Guild. No timing constraint on drafting or placement — form queued for next Debrief when placed in Accord Placement Area. At Debrief: target reviews, accepts or declines per Art 06 §9.4. PS consequences per Art 06 §9.4. On accept: track Accord income (target pays Guild 1 Capacity at each Upkeep Step 6 while Accord active).",
)
```

---

---

---

---

### GUI.PA.3 — HERITAGE REGISTRY *(stub)*
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
⚠ Pending design review (09-16). See stub design note below.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Historical-protection declaration thematically fits Guild's permanence doctrine — protecting what's already built | Art 00 §7 |
| Voice fit | ⚠ | No `narrative`/`perspectives` fields at all | Art 00 §7 |
| Doctrine alignment | ✓ | Consistent with "permanence through building" — protecting structures from removal | Art 00 §7 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Protect / StructureBlock — matches `card_status` DB directly | Art 04b §4 |
| Balance | ⚠ | Cost (Capacity×2 + Mandate×1) set, but the one-time-trigger-then-clear effect's actual power level can't be fully assessed — `success` is prose, not a structured mutation | Art 02 §6–§7 |
| Effect duration | ✓ | `persistence = Permanent`, but self-clearing after one trigger per its own prose — a one-shot Permanent, not standing indefinitely | Art 04 §5 P19 |
| Persistence | ⚠ | `persistence = Permanent` set, but no `persistence_condition`/`persistence_effect` fields — the Card-as-Condition pattern (design_reference_card_system.md) requires both as structured fields; this card describes the standing condition in prose inside `success` instead | Art 04 §6 |
| Trigger validity | ✓ | No trigger field; Automatic doesn't require one | — |
| Portrait validity | ⚠ | No `portrait` field at all | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any` | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock — existing component | Art 02 §6 |
| Supported by game procedure | ⚠ | The "restore on removal, once" mechanism has no defined procedural home — not a confirmed TriggerExpr/persistence_effect pattern | Art 03 §9 |
| Data schema validation | ⚠ | `success` is a bare prose string — same bare-string-literal-effects defect shape seen elsewhere in this review, now confirmed a third faction. Missing entirely: `outcome_type`, `threshold`, `ring_mod`, `doctrine_mod`, `trigger`, `resolution_type`, `target_object`/`target_taxonomy`, `restriction`, `boost`, `successcrit`/`fail`/`failcrit`, `on_accept`/`on_decline`, `card_id`, `arbiter_note`. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block | Art 04 §5 P26 |
| Outcome determinacy | ⚠ | No `game.choose_one()`, but no structured success/fail split exists to check against P27 either — `success` is unstructured prose | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capacity + Mandate), correctly typed. Design_note's trailing "Cost reasoning: 2 Capacity + 1 Mandate (Mid-tier)" checked — correct, matches actual cost. | Art 00a §9.2 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.PA.3 = Card(
    id      = "GUI.PA.3",  card_id = "GUI.PA.3",  version = "v1.0",
    name    = "Heritage Registry",
    tagline = "Declare a district's structures historically protected.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Protect,  subject = StructureBlock,

    beat            = 4,
    resolution      = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,  trigger = None,
    value_rating = 1,
    resolution_type = Transactional,  outcome_type = None,  # scaffolded, not addressed
    persistence     = Permanent,
    persistence_condition = None,  persistence_effect = None,  # see checklist: prose describes a card-as-condition effect not structured here

    target_district = district.any,
    target_faction  = None,
    target_object   = None,  target_taxonomy = None,

    affinity = None,  restriction = None,
    cost = Capacity * 2 + Mandate * 1,
    boost = None,

    success = "Places standing condition on target_district: If a structure block is removed for any reason (unless due to influence token reaching 0), add the structure block back to the district. Remove this standing effect after it triggers once.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept = None,  on_decline = None,

    portrait = None,  # scaffolded, not addressed
    ps_framing = None,
    narrative = None,  perspectives = None,
    design_note = "Defense scaling gap addressed. Cost reasoning: 2 Capacity + 1 Mandate (Mid-tier). Mandate provides the legal shield to protect the concrete.",
    arbiter_note = None,
)
```

---

### GUI.PA.4 — CIVIC UNVEILING *(stub)*
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
⚠ Pending design review (09-16). See stub design note below.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ribbon-cutting scaled to structural density is thematically grounded — public credibility earned from demonstrated building | Art 00 §7 |
| Voice fit | ⚠ | No `narrative`/`perspectives` fields at all | Art 00 §7 |
| Doctrine alignment | ✓ | PS scaling directly off Guild's own structure count in the district is maximally on-doctrine (standing earned through building, not rhetoric) | Art 00 §7 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Standing / Shift / StandingMarker — matches `card_status` DB directly | Art 04b §4 |
| Balance | ⚠ | Cost (Capacity + Exposure) set, but can't confirm magnitude without a real district structure count at review time | Art 02 §6–§7 |
| Effect duration | ⚠ | No `persistence` field declared at all | Art 04 §5 P19 |
| Persistence | ⚠ | Same gap — field absent | Art 04 §6 |
| Trigger validity | ✓ | No trigger field; Automatic doesn't require one | — |
| Portrait validity | ⚠ | No `portrait` field at all | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any` | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock (count read), Public Standing track — existing components | Art 02 §6–§7 |
| Supported by game procedure | ✓ | Straightforward count-and-apply at Beat 4 — no new procedure needed | Art 03 §9.4 |
| Data schema validation | ⚠ | `success` is a bare string — but notably **looks like valid Python expression syntax quoted as a string literal** (`"faction(Guild).standing += ..."`), a distinct sub-shape from GUI.PA.3/5's English-prose strings: this reads like real code that was accidentally left inside quotes rather than never structured at all. Missing entirely: `outcome_type`, `ring_mod`/`doctrine_mod`/`trigger`/`resolution_type`, `persistence`, targeting fields beyond `target_district`, `restriction`, `boost`, `successcrit`/`fail`/`failcrit`, `card_id`, `arbiter_note`. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block | Art 04 §5 P26 |
| Outcome determinacy | ⚠ | No structured success/fail split to check against P27 — `success` is a quoted string, not executable | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capacity + Exposure), correctly typed. Design_note's trailing "Cost reasoning: 1 Capacity + 1 Exposure (Mid-tier)" checked — correct, matches actual cost; Exposure use explained coherently ("broadcasting the ribbon-cutting"), same pattern as GHO.PA.4. | Art 00a §9.2 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.PA.4 = Card(
    id      = "GUI.PA.4",  card_id = "GUI.PA.4",  version = "v1.0",
    name    = "Civic Unveiling",
    tagline = "A highly publicized ribbon-cutting ceremony that compounds structural density into public adoration.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Standing,  function = Shift,  subject = StandingMarker,

    beat            = 4,
    resolution      = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,  trigger = None,
    value_rating = 1,
    resolution_type = Transactional,  outcome_type = None,  # scaffolded, not addressed
    persistence     = Immediate,  # scaffolded — deterministic default for a non-standing, one-shot PA
    persistence_condition = None,  persistence_effect = None,

    target_district = district.any,
    target_faction  = None,  target_object = None,  target_taxonomy = None,

    affinity = None,  restriction = None,
    cost = Capacity * 1 + Exposure * 1,
    boost = None,

    success = "faction(Guild).standing += district(target_district).faction(Guild).structure * 1",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept = None,  on_decline = None,

    portrait = None,  # scaffolded, not addressed
    ps_framing = None,
    narrative = None,  perspectives = None,
    design_note = "Standing / PS Compounding gap filled. Cost reasoning: 1 Capacity + 1 Exposure (Mid-tier). Broadcasting the massive ribbon-cutting to the city.",
    arbiter_note = None,
)
```

---

### GUI.PA.5 — ZONING EXEMPTION *(stub)*
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
⚠ Pending design review (09-16). See stub design note below.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Blanket regulatory exemption for expansion thematically fits Guild's builder doctrine | Art 00 §7 |
| Voice fit | ⚠ | No `narrative`/`perspectives` fields at all | Art 00 §7 |
| Doctrine alignment | ✓ | Removing a structural obstacle to building is maximally on-doctrine for Guild | Art 00 §7 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ⚠ | `subject = District` — checked against `ref_taxonomy.md`'s Subject vocabulary; "District" as a bare subject (rather than a specific component like PresenceToken/StructureBlock) is unusual — worth confirming this is a registered Subject term, same open question as items #27's unregistered-subject pattern (Difficulty, TargetProfile, etc.), though not confirmed DB-flagged here. | Art 04b §4 |
| Balance | ⚠ | Cost (Capacity + Findings + Capital) set, but "regardless of Ring limitations or connectivity rules" is a sweeping, unquantified effect — can't assess power level against a prose description | Art 02 §6–§7 |
| Effect duration | ⚠ | No `persistence` field declared; prose says "for the next Quarter" (Seasonal-shaped), but no structured duration field confirms this | Art 04 §5 P19 |
| Persistence | ⚠ | Same gap — field absent | Art 04 §6 |
| Trigger validity | ✓ | No trigger field; Automatic doesn't require one | — |
| Portrait validity | ⚠ | No `portrait` field at all | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district = district.any` | Art 01 §6–§7 |
| Supported by components | ⚠ | "Ring limitations or connectivity rules" bypass has no defined component/procedure hook — this would need to interact with the Ring Entry Rules (ref_special_district_and_ring_rules.md) directly, not clearly supported | Art 01 §6 |
| Supported by game procedure | ⚠ | No confirmed Art 03 procedure for a temporary Ring-entry-rule bypass — new ARBITER-facing behavior, same category as other unconfirmed-procedure gaps flagged elsewhere in this review | Art 03 §9 |
| Data schema validation | ⚠ | `success` is a bare prose string, same defect shape flagged elsewhere in this review. Missing entirely: `outcome_type`, `ring_mod`/`doctrine_mod`/`trigger`/`resolution_type`, `persistence`, most targeting/effect fields, `card_id`, `arbiter_note`. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block | Art 04 §5 P26 |
| Outcome determinacy | ⚠ | No structured success/fail split to check against P27 | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capacity + Findings + Capital), correctly typed. Design_note's trailing "Cost reasoning: 2 Capacity + 1 Findings + 1 Capital" checked — correct, matches actual cost. | Art 00a §9.2 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.PA.5 = Card(
    id      = "GUI.PA.5",  card_id = "GUI.PA.5",  version = "v1.0",
    name    = "Zoning Exemption",
    tagline = "Secure a blanket override of Ring expansion limitations.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Submission,  function = RemoveRestriction,  subject = District,

    beat            = 4,
    resolution      = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,  trigger = None,
    value_rating = 2,
    resolution_type = Transactional,  outcome_type = None,  # scaffolded, not addressed
    persistence     = Seasonal,  # scaffolded — matches prose "for the next Quarter"
    persistence_condition = None,  persistence_effect = None,

    target_district = district.any,
    target_faction  = None,  target_object = None,  target_taxonomy = None,

    affinity = None,  restriction = None,
    cost = Capacity * 2 + Findings * 1 + Capital * 1,
    boost = None,

    success = "For the next Quarter, Guild may place structures in the target district regardless of Ring limitations or connectivity rules.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept = None,  on_decline = None,

    portrait = None,  # scaffolded, not addressed
    ps_framing = None,
    narrative = None,  perspectives = None,
    design_note = "Ceiling-tier expansion enabler. Cost reasoning: 2 Capacity + 1 Findings + 1 Capital. Finding the bureaucratic loop-hole and buying the necessary judges to skip the physical expansion limits.",
    arbiter_note = None,
)
```

---

---

### GUI.PA.6 — ASSET TRANSFER *(stub)*
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
⚠ Pending design review (09-16). See stub design note below.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Trading a structure for a resource windfall is a plausible economic act, though the "legal asset flip" framing is thin | Art 00 §7 |
| Voice fit | ⚠ | No `narrative`/`perspectives` fields at all | Art 00 §7 |
| Doctrine alignment | ⚠ | Giving up a Structure Block (Guild's core permanence asset) for resources cuts against "permanence through building" — not clearly on-doctrine; no design_note reasoning addresses this tension | Art 00 §7 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Modify / StructureBlock — matches `card_status` DB directly | Art 04b §4 |
| Balance | ⚠ | Cost is cheap (Capacity×1) for removing a Guild structure, granting the target a structure, and gaining 3 of the target's native — can't fully assess without a structured effect to check magnitudes against | Art 02 §6–§7 |
| Effect duration | ⚠ | No `persistence` field declared at all | Art 04 §5 P19 |
| Persistence | ⚠ | Same gap — field absent | Art 04 §6 |
| Trigger validity | ✓ | No trigger field; Automatic doesn't require one | — |
| Portrait validity | ⚠ | No `portrait` field at all | Art 04 §6.2 |
| Supported by zones | ⚠ | No `target_district` field declared — referenced only inside the `restriction`/`success` strings | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock, native resources — existing components | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Straightforward transfer-and-payment at Beat 4 — no new procedure needed | Art 03 §9.4 |
| Data schema validation | ⚠ | **Both `restriction` and `success` are bare strings** — extends the bare-string defect beyond `success` alone to `restriction` too, the first confirmed instance on a non-`success` field. The restriction string also uses English `AND` rather than Python `and`. Missing entirely: `outcome_type`, `ring_mod`/`doctrine_mod`/`trigger`/`resolution_type`, `persistence`, `target_district`/`target_faction`/`target_object`/`target_taxonomy`, `boost`, `successcrit`/`fail`/`failcrit`, `card_id`, `arbiter_note`. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block | Art 04 §5 P26 |
| Outcome determinacy | ⚠ | No structured success/fail split to check against P27 | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Capacity × 1), correctly typed — the only cleanly-structured field on this card. | Art 00a §9.2 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.PA.6 = Card(
    id      = "GUI.PA.6",  card_id = "GUI.PA.6",  version = "v1.1",
    name    = "Asset Transfer",
    tagline = "Liquidate Guild property into another faction's hands for massive resource injection.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Territory,  function = Modify,  subject = StructureBlock,
    beat    = 4,  resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,  trigger = None,
    value_rating = 1,
    resolution_type = Transactional,  outcome_type = None,  # scaffolded, not addressed
    persistence = Immediate,  # scaffolded, not addressed
    persistence_condition = None,  persistence_effect = None,
    target_district = district.named,  target_faction = faction.opponent,  target_object = None,  target_taxonomy = None,
    affinity = None,
    cost    = Capacity * 1,
    boost   = None,
    restriction = "district(target).faction(Guild).structure > 0 AND district(target).faction(target_faction).presence > 0",
    success = "Guild removes 1 of their Structure Blocks in target_district and replaces it with 1 Structure Block of the target_faction. Guild gains 3 of the target_faction's native resource from the supply.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept = None,  on_decline = None,
    portrait = None,  # scaffolded, not addressed
    ps_framing = None,
    narrative = None,  perspectives = None,
    design_note = "A powerful, legal asset flip. Leverages existing footprint to extract deep foreign resource pockets.",
    arbiter_note = None,
)
```

---

### GUI.PA.7 — EMINENT DOMAIN PETITION *(stub)*
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
⚠ Pending design review (09-16). See stub design note below.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Forcing presence expansion from an existing foothold is thematically grounded — Guild's blunt-force building tool | Art 00 §7 |
| Voice fit | ⚠ | No `narrative`/`perspectives` fields at all | Art 00 §7 |
| Doctrine alignment | ✓ | Direct presence expansion is on-doctrine for Guild's builder identity | Art 00 §7 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken — matches `card_status` DB directly | Art 04b §4 |
| Balance | ⚠ | Cost (Capacity×2 + Mandate×1) for +2 presence tokens with a foothold restriction — comparable in shape to STD.PA.1's dual-native cost for +2 presence, but can't confirm relative balance without the "crack Established status" framing being made concrete | Art 02 §6–§7 |
| Effect duration | ✓ | Presence tokens are Permanent board state; the card itself is a one-shot act | Art 04 §5 P19 |
| Persistence | ⚠ | No `persistence` field declared at all | Art 04 §6 |
| Trigger validity | ✓ | No trigger field; Automatic doesn't require one | — |
| Portrait validity | ⚠ | No `portrait` field at all | Art 04 §6.2 |
| Supported by zones | ⚠ | No `target_district` field declared — referenced only inside the `restriction`/`success` strings | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken — existing component | Art 02 §6 |
| Supported by game procedure | ✓ | Straightforward placement at Beat 4 — no new procedure needed | Art 03 §9.4 |
| Data schema validation | ⚠ | Both `restriction` and `success` are bare strings — same defect shape as GUI.PA.6. Missing entirely: `outcome_type`, `ring_mod`/`doctrine_mod`/`trigger`/`resolution_type`, `persistence`, `target_district`/`target_faction`/`target_object`/`target_taxonomy`, `boost`, `successcrit`/`fail`/`failcrit`, `card_id`, `arbiter_note`. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block | Art 04 §5 P26 |
| Outcome determinacy | ⚠ | No structured success/fail split to check against P27 | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capacity + Mandate), correctly typed. | Art 00a §9.2 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.PA.7 = Card(
    id      = "GUI.PA.7",  card_id = "GUI.PA.7",  version = "v1.1",
    name    = "Eminent Domain Petition",
    tagline = "Force massive influence into a district to pave the way for expansion.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Territory,  function = Add,  subject = PresenceToken,
    beat    = 4,  resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,  trigger = None,
    value_rating = 2,
    resolution_type = Transactional,  outcome_type = None,  # scaffolded, not addressed
    persistence = Immediate,  # scaffolded, not addressed
    persistence_condition = None,  persistence_effect = None,
    target_district = district.named,  target_faction = None,  target_object = None,  target_taxonomy = None,
    affinity = None,
    cost    = Capacity * 2 + Mandate * 1,
    boost   = None,
    restriction = "district(target).faction(Guild).presence > 0",
    success = "Place 2 Guild Presence Tokens in target_district.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept = None,  on_decline = None,
    portrait = None,  # scaffolded, not addressed
    ps_framing = None,
    narrative = None,  perspectives = None,
    design_note = "Requires existing foothold. A blunt-force legal maneuver to crack an opponent's Established status.",
    arbiter_note = None,
)
```

---

### GUI.PA.8 — STRUCTURAL SUBSIDY *(stub)*
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
⚠ Pending design review (09-16). See stub design note below.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Converting opponents' construction into Guild PS is a distinctive, doctrinally-grounded standing condition | Art 00 §7 |
| Voice fit | ⚠ | No `narrative`/`perspectives` fields at all | Art 00 §7 |
| Doctrine alignment | ✓ | Reframes any faction's building as validation of Guild's permanence doctrine — on-doctrine | Art 00 §7 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Standing / Shift / StandingMarker — matches `card_status` DB directly | Art 04b §4 |
| Balance | ⚠ | Cost (Capacity×2) for an indefinite standing PS-generation condition — can't confirm power level without a structured, bounded effect | Art 02 §6–§7 |
| Effect duration | ✓ | `persistence = Permanent`, consistent with a standing reactive condition | Art 04 §5 P19 |
| Persistence | ⚠ | `persistence = Permanent` set, but no `persistence_condition`/`persistence_effect` fields — the Card-as-Condition pattern requires both as structured fields; this card describes the standing trigger in prose inside `success` instead, same gap as GUI.PA.3 | Art 04 §6 |
| Trigger validity | ⚠ | The described trigger ("whenever an opponent places a Structure Block here") maps to the confirmed `structure_block.placed(faction=X, ring=Z)` TriggerExpr vocabulary, but isn't expressed as one — it's prose inside `success` | Art 04 §6.3 |
| Portrait validity | ⚠ | No `portrait` field at all | Art 04 §6.2 |
| Supported by zones | ✓ | `target_district` implied by prose, not declared as a field | Art 01 §6–§7 |
| Supported by components | ✓ | StructureBlock, Public Standing track — existing components | Art 02 §6–§7 |
| Supported by game procedure | ⚠ | Reactive PS-on-opponent-build has no structured trigger — same gap as Trigger validity above | Art 03 §9 |
| Data schema validation | ⚠ | `success` is a bare prose string describing what should be a `persistence_effect` — same Card-as-Condition-pattern gap as DIR.PA.7 Curfew. Missing entirely: `outcome_type`, `ring_mod`/`doctrine_mod`/`trigger`/`resolution_type`, `target_district`/`target_faction`/`target_object`/`target_taxonomy`, `restriction`, `boost`, `successcrit`/`fail`/`failcrit`, `card_id`, `arbiter_note`. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block | Art 04 §5 P26 |
| Outcome determinacy | ⚠ | No structured success/fail split to check against P27 | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Capacity × 2), correctly typed. | Art 00a §9.2 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.PA.8 = Card(
    id      = "GUI.PA.8",  card_id = "GUI.PA.8",  version = "v1.1",
    name    = "Structural Subsidy",
    tagline = "Turn a district's development into a PR engine.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Standing,  function = Shift,  subject = StandingMarker,
    beat    = 4,  resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,  trigger = None,
    value_rating = 1,
    resolution_type = Transactional,  outcome_type = None,  # scaffolded, not addressed
    persistence = Permanent,
    persistence_condition = None,  persistence_effect = None,  # see checklist: prose describes a reactive trigger not structured here
    target_district = district.any,  target_faction = None,  target_object = None,  target_taxonomy = None,
    affinity = None,  restriction = None,
    cost    = Capacity * 2,
    boost   = None,
    success = "Places standing condition on target_district: 'Whenever an opponent places a Structure Block here, Guild gains +1 PS.'",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept = None,  on_decline = None,
    portrait = None,  # scaffolded, not addressed
    ps_framing = None,
    narrative = None,  perspectives = None,
    design_note = "A standing effect. Guild weaponizes other factions' construction efforts to build their own prestige.",
    arbiter_note = None,
)
```

### GUI.PA.9 — CITY LEDGER
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
Guild's ceiling Standing card — a public presentation of the full construction record across a district cluster. N = count of districts in {target ∪ adjacent} where Guild holds a structure block (max 9: target + 8 adjacencies by board geometry). Success: +N PS. The card is self-calibrating — the more Guild has built in the cluster, the larger the PS swing. Failcrit is symmetric: −N PS. A faction that bets its entire construction record on a public declaration that fails pays proportionally.

Cost: 3 Capacity (show of strength), 1 Capital (broadcast), 1 Exposure (public act), 1 Mandate (record). Total cross-cost gate is high; this card is not played early. Distinct from GUI.PA.4 Civic Unveiling (Automatic, single-district, shallow PS ceiling): PA.4 is the floor version; City Ledger is the d100 ceiling gamble. Successcrit adds the harvest: for each qualifying district, Guild receives +1 of that district's native resource — a heterogeneous yield matching the actual resource character of each district in the cluster. At full cluster (N=9), successcrit can return a mix of Findings, Mandate, Capacity, and Exposure depending on which districts Guild has built in. Portrait +2 (Guild's maximum public commitment).

#### Card Story
⚠ Story pending.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public declaration of construction record across a district cluster; Guild doctrine-coherent — standing earned through demonstrated building, not rhetoric | Art 00 §7 |
| Voice fit | ✓ | Five perspectives distinct: Guild matter-of-fact accounting; Network acknowledges the ledger as signal; Ghost reads it as structural dependency data; Directorate contests the figures; Syndicate notes standing built on structures as the most durable kind | Art 00 §7 |
| Doctrine alignment | ✓ | Guild ceiling card, d100, high cost — consistent with "heavy, deliberate, permanent" playstyle; Portrait +2 (Guild's doctrinal maximum) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Standing / Shift / StandingMarker | Art 04b §4 |
| Balance | ⚠ | N scales with board position; cost 3C+1Cap+1E+1M is ceiling tier; failcrit symmetric to success — playtesting required | Art 02 §6–§7 |
| Effect duration | ✓ | PS shifts Immediate; resource delivery Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — all effects resolve at Beat 4 | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Guild +2: submitter-bounded; ceiling public commitment = doctrinal maximum | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; N calculated across target + all adjacent districts per Art 01 §6.5 adjacency map | Art 01 §6.5 |
| Supported by components | ✓ | PS tracked on Public Standing track (Art 02 §7); resources from existing resource system; StructureBlocks already on board — no new components | Art 02 §7–§8 |
| Supported by game procedure | ⚠ | Beat 0: N-lock — ARBITER counts qualifying districts and records N; Beat 4: resolution. N-lock at Beat 0 is new procedure; confirm against Art 03 §9.4 | Art 03 §9.4 |
| Data schema validation | ⚠ | New card — DB registration required | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `d100`; all four tiers populated (success/successcrit/fail/failcrit), no `game.choose_one()` — resolves deterministically once N is locked at Beat 0. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capacity ×3 + Capital + Exposure + Mandate, ×1 each), correctly typed — ceiling-tier cost matching this card's high-variance design. | Art 00a §9.2 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.PA.9 = Card(
    id      = "GUI.PA.9",  card_id = "GUI.PA.9",  version = "v0.1",
    name    = "City Ledger",
    tagline = "Present the full construction record. Let the district account for what has been built.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Standing,  function = Shift,  subject = StandingMarker,

    beat            = 4,
    resolution      = d100,
    threshold       = 40,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = 1,
    trigger         = None,
    resolution_type = Probabilistic,
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.named,
    target_faction  = None,
    target_object   = None,
    target_taxonomy = None,

    affinity    = None,
    restriction = count(d in ([district(target)] + district(target).adjacent)
                        where d.faction(Guild).structure > 0) >= 1,
    cost = Capacity * 3
         + Capital  * 1
         + Exposure * 1
         + Mandate  * 1,
    boost = None,

    success = faction(Guild).standing.add(
                  count(d in ([district(target)] + district(target).adjacent)
                        where d.faction(Guild).structure > 0)),

    successcrit = [faction(Guild).resource(d.native).add(1)
                   for d in ([district(target)] + district(target).adjacent)
                   if d.faction(Guild).structure > 0],

    fail     = None,

    failcrit = faction(Guild).standing.remove(
                   count(d in ([district(target)] + district(target).adjacent)
                         where d.faction(Guild).structure > 0)),

    portrait = {Guild: PortraitEntry(submitter=+2)},
    ps_framing = None,

    narrative    = None,
    perspectives = {
        Guild:       "The survey is not a campaign. It is a count. The city has been watching us build for years. Now they see the total.",
        Network:     "Guild puts the ledger on the table. No spin, no campaign — just the number. Occasionally the number is the signal.",
        Ghost:       "Quantified construction output translates to community dependency. The city's response is structural, not emotional. The leverage is already embedded in the districts.",
        Directorate: "A public record of physical presence submitted to general attention. We maintain our own records. Guild's version of the total is, predictably, generous.",
        Syndicate:   "Standing built on structures doesn't decay with the news cycle. Guild has been building this position for years. The ledger just makes it legible.",
    },
    design_note  = "Ceiling Standing card. N = count of districts in {target ∪ adjacent} where Guild holds a structure block; max 9 (target + 8 adjacencies for Research Institute, per Art 01 §6.5 adjacency map). Success = +N PS. Failcrit = −N PS: symmetric, bet big/fail big. Successcrit adds +1 district.native per qualifying district — heterogeneous resource harvest; each district pays its own native type. Cost: 3C (show of strength) + 1 Capital (broadcast) + 1 Exposure (public act) + 1 Mandate (record). Distinct from GUI.PA.4 Civic Unveiling (Automatic, single-district, shallow PS ceiling): PA.4 is floor; City Ledger is d100 ceiling gamble. N-lock at Beat 0: ARBITER counts and records qualifying districts before Beat 3–4 resolution.",
    arbiter_note = "Phase B: Guild declares City Ledger and names target district publicly. Beat 0: identify qualifying set = {target district} + {all adjacent districts}; count Guild structure blocks across that set = N. If N = 0, PA voided, cost returned. Record N. Beat 4: d100 vs 40. Success: Guild +N PS. Successcrit (01–05): Guild +N PS AND for each qualifying district yield +1 of that district's native resource to Guild. Fail: no effect (cost sunk). Failcrit (96–00): Guild −N PS.",
)
```

---

### GUI.PA.10 — JOINT DEVELOPMENT
[↑ Public Acts](#guild-public-acts)

#### Design Rationale
Cooperative PA. Cost: 2 Capacity + 1 native resource of the target faction's type — both paid by the Guild submitter, who must have acquired the target faction's native resource beforehand (through trade or prior economy cards). This is a standard cost structure; the target type specification narrows what's acceptable but imposes no procedural novelty. Both factions must already be Present in the district, and neither may hold a structure block there yet (first-infrastructure frame: both parties are establishing, not entrenching).

Success: target faction gains a structure block (Guild builds FOR the ally). Guild receives the larger PS reward (+2) as the acting faction bearing the roll risk; target receives +1 as participant. Successcrit adds Guild's own structure block in the same district — both factions become infrastructure-holders simultaneously — plus 1 Presence Token for Guild (crew who stayed to anchor the work). Failcrit destabilizes both positions: −1 Presence Token each, reflecting that a failed public coordination is worse than no coordination.

Portfolio position: Doctrine-consistent — Guild's maximum aspiration is demonstrating collective human capacity, not self-interest. The card's asymmetric PS reward (Guild leads) reflects risk differential, not hierarchy.

#### Card Story
The Guild moves its crews into a district where another faction already has a foothold, not to compete but to build alongside them. The foundation goes down; both faction colors appear in the same block. New Meridian doesn't miss it. Neither does the Chronicle.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Guild crews building infrastructure for an ally in a jointly-held district; Guild doctrine-coherent — demonstrated collective capacity over self-interest | Art 00 §7 |
| Voice fit | ⚠ | Perspectives pending | Art 00 §7 |
| Doctrine alignment | ✓ | Cooperative build is Guild's doctrinal ceiling aspiration; bilateral cost + bilateral PS reward encode mutual commitment; portrait submitter=+1 for Guild | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Guild) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / StructureBlock — primary effect is structure block placement for target faction | Art 04b §4 |
| Balance | ⚠ | Successcrit dual structure + presence token is significant payoff; cost gate (Guild must hold target faction's native resource type) is an implicit throttle — playtesting required | Art 02 §6–§7 |
| Effect duration | ✓ | Structure block placements Permanent (board state); PS shifts Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Card persistence = Immediate; structure blocks persist as board state per GR 8.2 | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Guild submitter=+1; submitter-bounded; public cooperative act is doctrine-consistent | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; both factions' presence_token.count evaluated at declared district | Art 01 §6 |
| Supported by components | ✓ | Structure Block (GR 8.2 — max 1 per faction per district; restriction ensures 0 for both before play); Presence Token; Public Standing track | Art 02 §7–§8 |
| Supported by game procedure | ✓ | All resources submitted by Guild (submitter) at §9.2; standard Beat 4 payment procedure applies | Art 03 §9.2, §9.4.3 |
| Data schema validation | ⚠ | New card — DB registration required. **`card_status` DB shows `layer`/`function`/`subject` all `NULL`** despite the code correctly declaring `Territory/Add/StructureBlock` — same NULL-taxonomy-but-valid-code desync as GUI.CA.10, now a second confirmed Guild-set instance (one CA, one PA). Not reconciled — flagged only. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story above | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `d100`; all four tiers populated (success/successcrit/fail/failcrit), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Capacity ×2 + target faction's native ×1), correctly typed. | Art 00a §9.2 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | | |

```python
GUI.PA.10 = Card(
    id      = "GUI.PA.10",  card_id = "GUI.PA.10",  version = "v0.1",
    name    = "Joint Development",
    tagline = "Guild and an allied faction commit jointly to structural development in a shared district.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,

    layer    = Territory,  function = Add,  subject = StructureBlock,

    beat            = 4,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = {Ring3: +10, Ring2: 0, Ring1: -10, Ring0: -15},
    doctrine_mod    = {Neighbor: +15, Opposed: -15},
    value_rating = None,  # scaffolded, not addressed
    trigger         = None,
    resolution_type = Probabilistic,
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.named,
    target_faction  = faction.named,
    target_object   = None,
    declared_params = None,

    affinity    = None,
    restriction = (faction(Guild).structure_block.count(district(target)) == 0
               and faction(target).structure_block.count(district(target)) == 0
               and faction(Guild).presence_token.count(district(target)) > 0
               and faction(target).presence_token.count(district(target)) > 0),
    cost = Capacity * 2
         + faction.target.native * 1,
    boost = None,

    success = [faction(target).structure_block.add(district(target), 1),
               faction(Guild).standing.add(2),
               faction(target).standing.add(1)],

    successcrit = [faction(Guild).structure_block.add(district(target), 1),
                   faction(Guild).presence_token.add(district(target), 1)],

    fail     = None,

    failcrit = [faction(Guild).presence_token.remove(district(target), 1),
                faction(target).presence_token.remove(district(target), 1)],

    portrait = {Guild: PortraitEntry(submitter=+1)},

    ps_framing = "Public cooperation between Guild and allied faction is visible to New Meridian; Guild leads (+2 PS) as acting faction bearing roll risk; target faction participates (+1 PS).",

    narrative    = None,
    perspectives = None,
    design_note  = "Restriction (both Present, neither has structure) frames this as a first-infrastructure moment — neither party is entrenching, both are establishing. Success: target gets structure block. Successcrit: both factions get structure blocks simultaneously + Guild gains 1 Presence Token. Failcrit: both lose 1 Presence Token — failed public coordination is worse than no coordination. PS asymmetry (Guild +2, target +1) reflects risk differential, not hierarchy.",
    arbiter_note = None,
)
```

---

### GUI.MOD.1 — NIGHT SHIFT CREW

#### Design Rationale
Guild's React presence card: when a Guild chip is removed from a district, Guild may immediately respond by placing a chip back. "Established communities don't abandon positions — they return." The return is reflexive, not planned — trigger is the chip removal itself (publicly observable resolved action). No structure dependency: structure may be simultaneously removed when chips hit 0, so the trigger window must not require it — taxonomy is Territory|Add|PresenceToken, not Recover, since "Recover" is not a valid primitive per 00a §7.2. `cost=None` reflects the reflexive framing (playtest-flagged, not a final balance call); `successcrit`/`failcrit` are correctly `None` since `resolution=Automatic` carries no dice roll to critical on.

#### Card Story
A structure block goes dark and the district looks abandoned for exactly as long as it takes someone to walk back in and turn the lights back on.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Reflexive territorial recovery — Guild doctrine of institutional permanence, "we don't leave." | Art 00 §7 |
| Voice fit | ⚠ | Perspectives TBD — deferred to modifier card voice pass (D-04-08). | Art 00 §9 |
| Doctrine alignment | ✓ | Established communities returning after displacement is core Guild doctrine. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Guild — trigger-based, fires on chip removal. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken — 04b-20 (Recover verb validity audit) closed, confirming this assignment. | Art 04b §4; PM05 04b-20 |
| Balance | ✓ | `cost = None` — reflexive, not a planned play; playtest-flagged (04-n94 pattern), not final. | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — chip placed back at trigger. | Art 04 §5 P19 |
| Persistence | ⚠ | `persistence` field open corpus-wide question (schema_cleanup_log item 2/D), not card-specific. | Art 04 §6.2 |
| Trigger validity | ⚠ | Uses `presence_chip.removed(faction=Guild, district=X)`, not yet confirmed against §6.3 TriggerExpr vocabulary. Trigger scope (any chip removal vs. specific action types) also remains an open design question. | Art 04 §6.3; PM05 04-n174 |
| Portrait validity | ✓ | `{Guild: submitter=+1}` — unchanged from fossil, already correctly structured. | Art 04 §6.2 |
| Supported by zones | ✓ | District-scoped by design — the whole point is returning to the specific district that lost the chip. | Art 01 §6–§7 |
| Supported by components | ✓ | Presence chips — existing component. | Art 02 §6, §11 |
| Supported by game procedure | ✓ | Chip removal is a publicly observable resolved action; no new ARBITER behavior needed. | Art 03 §18 |
| Data schema validation | ⚠ | `presence_chip.removed(...)` has no confirmed TriggerExpr vocabulary — same open gap as the rest of the corpus. | Art 04 §6.1–§6.3; PM05 04-n174 |
| Card narrative | ✓ | Card Story present. | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic` — deterministic reflex, no dice. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | `cost=None` — free reflexive response, matching the "we don't leave" framing. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ⚠ | Depends on how often Guild chips get removed district-wide; best-effort, not independently verifiable here. |  |
| Firing window (ModReactCard) | ✓ | No other Guild card shares this exact trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Deterministic reflex, no dice — Automatic is correct. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open corpus-wide question: is a 2nd copy meaningful? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ (N/A) | `ring_constraint=None` — not ring-scoped (district-scoped instead, via `target_district`). |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | |  |  |

```python
GUI.MOD.1 = Card(
    id      = "GUI.MOD.1",  card_id = "GUI.MOD.1",  version = "v0.2",
    name    = "Night Shift Crew",
    tagline = "Established communities don't abandon positions — they return.",
    type    = ModReactCard,  faction = Guild,

    layer   = Territory,  function = Add,  subject = PresenceToken,

    trigger         = presence_chip.removed(faction=Guild, district=district(trigger.target)),
    beat            = None,
    ring_constraint = None,  ring_origin = None,  value_rating = 1,
    resolution      = Automatic,  threshold = None,  resolution_type = Transactional,  outcome_type = None,
    ring_mod        = None,  doctrine_mod = None,
    acquisition     = Deck,  generating_card = None,

    target_district = district(trigger.target),
    target_faction  = None,
    target_object   = None,
    affinity        = None,  restriction = None,
    cost            = None,  # reflexive return, not a planned play — playtest-flagged (04-n94 pattern), not final
    boost           = None,

    success     = faction(acting).presence_chips(district(target_district)).add(1),
    successcrit = None,  fail = None,  failcrit = None,  # no dice under Automatic resolution — deterministic reflex, not a probabilistic outcome
    on_accept   = None,  on_decline = None,

    portrait     = {Guild: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = None,  perspectives = None,
    design_note  = "Guild's React presence card: when a Guild chip is removed from a district, Guild may immediately place a chip back. \"Established communities don't abandon positions — they return.\" The return is reflexive, not planned; no structure dependency, since structure may be removed simultaneously when chips hit 0 and the trigger window must not require it. cost=None reflects the reflexive framing — playtest-flagged, not a final balance call.",
    arbiter_note = "On trigger (a Guild presence chip is removed from a district): Guild may immediately place one presence chip back in that same district, no cost. Resolves before the acting faction's turn continues.",
)
```

---

### GUI.MOD.2 — UNION REPRESENTATIVE

#### Design Rationale
First of Guild's build-side passive income family (GUI.MOD.2/3/4). No self-fire ambiguity (`faction=opponent`, explicitly excludes Guild). Real finding: no restriction and no cost, fires on any opponent structure placement citywide — the same "least-gated, likely-high-frequency" shape flagged as a real balance concern on DIR.MOD.7 (Directorate's structurally identical card), not just deferred to the generic 04-n178 cost question. Design_note's own reference to "04-n2 (unimplemented passive income governing rule)" is worth surfacing as context, not resolved here.

#### Card Story
A rival breaks ground somewhere in the city. The crew on-site is Guild labor, same as always — and the invoice goes out whether or not the client asked for it by name.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "Construction is Guild's domain regardless of who commissions it" is a clean, doctrinally central Guild beat. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1 — correctly expresses doctrine. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Guild, real taxonomy (Economy/Add/NativeResource, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy×Add is valid per the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | No restriction, no cost, fires on any opponent structure placement anywhere — same "least-gated, likely-high-frequency" shape as DIR.MOD.7. Real balance attention warranted beyond the generic 04-n178 gate. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `structure_block.placed(faction=opponent)` — confirmed vocabulary, correctly scoped. | Art 04 §6.3 |
| Portrait validity | ✓ | Submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district` — correct. | Art 01 §6–7 |
| Supported by components | ✓ | Standard resource-grant mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing structure-placement event; no new ARBITER behavior. Connects to 04-n2 (unimplemented passive-income governing rule) per its own design_note — worth checking that rule's status doesn't conflict once it's implemented. | Art 03; GR 6.1; PM05 04-n2 |
| Data schema validation | ⚠ (deferred) | Scaffolded (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above covers P26. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | `cost=None` — same whole-set gate as the rest of the corpus (04-n178), but this card is a strong candidate for actually needing a real cost given the Balance flag above. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ⚠ | Structure placement is a common, recurring board event across all 4 other factions. Ties directly into the Balance flag. |  |
| Firing window (ModReactCard) | ⚠ | GUI.MOD.3/4 (faction/ring-narrowed variants of this same family) likely share overlapping trigger space — same family-overlap flag as the Directorate/Ghost sets. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat yield, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; fires table-wide by design (ring-constrained variant is GUI.MOD.4). |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | |  |  |

```python
GUI.MOD.2 = Card(
    id      = "GUI.MOD.2",  card_id = "GUI.MOD.2",  version = "v0.1",
    name    = "Union Representative",
    tagline = "Other factions build with Guild labor. Guild gets paid.",
    type    = ModReactCard,  faction = Guild,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = structure_block.placed(faction=opponent),  # any non-Guild faction places structure
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating = 1,

    resolution = Automatic,  threshold = None,  resolution_type = Transactional,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,  # no presence requirement — Guild workforce is citywide
    cost            = None,
    boost           = None,  # scaffolded, not addressed

    success     = faction(Guild).resources.add(1, Capacity),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Guild: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolded, not addressed
    narrative    = None,
    perspectives = None,
    design_note  = "Passive income React. Any opponent structure placement triggers 1 Capacity yield to Guild. Guild's doctrine: construction is Guild's domain regardless of who commissions it. Companion to 04-n2 (unimplemented passive income governing rule) — this delivers the same income as a ModReactCard rather than an Art 03 procedural rule. No presence restriction: Guild labor operates citywide.",
    arbiter_note = None,
)
```

---

### GUI.MOD.3 — INSTITUTIONAL CONTRACT

#### Design Rationale
Second card of the GUI.MOD.2/3/4 family — narrowed to Directorate, no self-fire ambiguity.

#### Card Story
Directorate breaks ground on an institutional facility. The crews are Guild's, same as every government contract before it — Guild invoices the moment the block goes up.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Directorate-narrowed variant grounded in a real doctrinal tension (design_note cites DIR.PA.1 raising Guild's costs) — not an arbitrary narrowing. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1 — correctly expresses doctrine. | Art 04 §6.5 |
| Card type fit | ✓ | Same shape as GUI.MOD.2. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Economy×Add cell. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Narrower than GUI.MOD.2 (Directorate-only), lower frequency — plausible; final read pending 04-n178. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `structure_block.placed(faction=Directorate)` — explicitly scoped, no ambiguity. | Art 04 §6.3 |
| Portrait validity | ✓ | Submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same as GUI.MOD.2. | Art 01 §6–7 |
| Supported by components | ✓ | Same as GUI.MOD.2. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same as GUI.MOD.2. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above covers P26. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set gate as GUI.MOD.2. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Directorate-only scope keeps frequency lower than GUI.MOD.2's generic trigger. |  |
| Firing window (ModReactCard) | ⚠ | Same family-overlap flag as GUI.MOD.2/4. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same as GUI.MOD.2. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; gated by faction identity, not ring. |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | |  |  |

```python
GUI.MOD.3 = Card(
    id      = "GUI.MOD.3",  card_id = "GUI.MOD.3",  version = "v0.1",
    name    = "Institutional Contract",
    tagline = "Directorate builds. Guild crews and invoices.",
    type    = ModReactCard,  faction = Guild,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = structure_block.placed(faction=Directorate),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating = 1,

    resolution = Automatic,  threshold = None,  resolution_type = Transactional,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,
    boost           = None,  # scaffolded, not addressed

    success     = faction(Guild).resources.add(1, Capacity),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Guild: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolded, not addressed
    narrative    = None,
    perspectives = None,
    design_note  = "Directorate-targeted variant of GUI.MOD.2 (Union Representative). Same trigger/effect, faction-narrowed to Directorate. Guild–Directorate tension: Directorate controls Guild's operating environment (PA.1 Regulatory Override raises construction costs); Guild charges Directorate for every structure it commissions. Narrower trigger window than generic variant; reliable in DIR-heavy games.",
    arbiter_note = None,
)
```

---

### GUI.MOD.4 — CORE PREMIUM

#### Design Rationale
Third card of the GUI.MOD.2/3/4 family — Ring 1-locked, double yield (2 Capacity vs. 1). No self-fire ambiguity (`opponent`-scoped).

#### Card Story
A rival's crew breaks ground in the Core — denser infrastructure, scarcer labor, higher stakes. Guild's invoice reflects it: double the standard rate, same as every Core job before it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Premium rate for Core construction is a coherent escalation, matches DIR.MOD.3's "Core is the strongest tier" pattern from the Directorate family. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1 — correctly expresses doctrine. | Art 04 §6.5 |
| Card type fit | ✓ | Same shape as GUI.MOD.2/3. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Economy×Add cell. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Design_note calls this "strongest Guild passive income trigger" — double yield, Ring-locked but still no restriction/cost within Core. Same balance-attention flag as GUI.MOD.2, sharper given the 2x multiplier. Final read pending 04-n178. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `structure_block.placed(faction=opponent, ring=1)` — confirmed vocabulary, correctly scoped. | Art 04 §6.3 |
| Portrait validity | ✓ | Submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `ring_constraint=1` matches trigger's `ring=1` scope. | Art 01 §6–7 |
| Supported by components | ✓ | Same as GUI.MOD.2/3. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same as GUI.MOD.2/3. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above covers P26. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | `cost=None` on the set's highest-yield card — strongest candidate in the family for actually needing a real cost. Gated on 04-n178. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ⚠ | Ring-locked to Core (fewer districts) but Core is dense/contested — could still be meaningful frequency combined with the 2x yield. Ties into the Balance flag. |  |
| Firing window (ModReactCard) | ⚠ | Same family-overlap flag as GUI.MOD.2/3 — if a Core structure placement satisfies both GUI.MOD.2's generic trigger and this Ring-1 variant, no documented rule on whether both fire. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same as GUI.MOD.2/3. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=1` correctly matches trigger scope; distinguishes this as the Ring-locked family member. |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | |  |  |

```python
GUI.MOD.4 = Card(
    id      = "GUI.MOD.4",  card_id = "GUI.MOD.4",  version = "v0.1",
    name    = "Core Premium",
    tagline = "Core construction pays Guild at institutional rates.",
    type    = ModReactCard,  faction = Guild,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = structure_block.placed(faction=opponent, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = None,
    value_rating = 3,

    resolution = Automatic,  threshold = None,  resolution_type = Transactional,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,
    boost           = None,  # scaffolded, not addressed

    success     = faction(Guild).resources.add(2, Capacity),  # double rate for Core ring
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Guild: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolded, not addressed
    narrative    = None,
    perspectives = None,
    design_note  = "Ring 1–constrained variant of GUI.MOD.2. Core construction yields 2 Capacity (vs. 1 for generic). Scarcity and complexity of Core construction means Guild commands premium rates. Strongest Guild passive income trigger — incentivizes Guild to maintain Core presence to capture premium construction income from all factions.",
    arbiter_note = None,
)
```

---

### GUI.MOD.5 — COMPANY TOWN

#### Design Rationale
First "draw a card" ModReactCard effect in the Guild set — reacts to opponent presence placement near a Guild structure. Open balance flag: `count=1` is likely a null effect since a single random modifier draw isn't a guaranteed benefit — recommend `count=2`, not yet applied. Also an instance of the unconfirmed `where(...)` trigger-parameter form used elsewhere in the corpus.

#### Card Story
An opponent moves into ground shadowed by a Guild structure. Nothing overt happens — but somewhere in the building, someone's already talking, and Guild walks away from the conversation with something useful.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Guild's structural footprint as a passive intelligence/asset network is a coherent, non-obvious doctrine beat. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = None` — reasonable; this is a passive economic engine, not a doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Guild, real taxonomy (Economy/Add/ModifierCard, 04-n175) — first precedent for this effect shape. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy×Add valid; ModifierCard-as-subject is a reasonable extension (an acquired asset), consistent with how GHO.MOD.2's IntelToken-Add is handled. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | `count=1` is likely a null effect — recommend `count=2`. Not fixed here, still open. | Art 02 §6–7; Art 04 §6.5; PM05 04-n175 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | Base event (`presence_chip.placed`) is confirmed vocabulary, but `district=where(...)` is an instance of the unconfirmed §6.3 parameter form. | Art 04 §6.3; schema_cleanup_log.md item 9 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Condition is district-scoped via the Guild-structure filter. | Art 01 §6–7 |
| Supported by components | ✓ | Modifier card draw reuses the standard Upkeep-draw mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing chip-placement event and modifier-draw mechanism; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above covers P26. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set gate as the rest of the corpus. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Gated on Guild having a structure in the affected district — moderate, tied to Guild's own board footprint. |  |
| Firing window (ModReactCard) | ✓ | No other Guild card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat draw effect, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus: 2 copies → 2 separate draws per qualifying placement? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; gated by Guild's structure presence, not ring. |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | |  |  |

```python
GUI.MOD.5 = Card(
    id      = "GUI.MOD.5",  card_id = "GUI.MOD.5",  version = "v0.1",
    name    = "Company Town",
    tagline = "Our people built the walls. We hear who whispers behind them.",
    type    = ModReactCard,  faction = Guild,
    layer   = Economy,  function = Add,  subject = ModifierCard,  # first "draw a card" ModReactCard effect; no existing taxonomy precedent for this shape, treating a drawn card as an acquired asset

    trigger         = presence_chip.placed(faction=opponent, district=where(faction(Guild).structure > 0)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating = 1,

    resolution = Automatic,  threshold = None,  resolution_type = Transactional,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,
    boost           = None,  # scaffolded, not addressed

    success     = arbiter.draw_modifier(faction=Guild, count=1),  # balance flag: count=1 is a null effect unless the drawn card has independent value — recommend count=2
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    ps_framing   = None,  # scaffolded, not addressed
    narrative    = None,
    perspectives = None,
    design_note  = "Passive intelligence engine. Guild's massive labor footprint acts as an informant network. When an opponent expands into a district where Guild has a structure, Guild draws modifier card(s). Turns their win-condition (structures) into a territorial tax on opponent expansion. Count currently 1, flagged as likely needing to be 2 — a single random modifier card draw isn't a guaranteed benefit on its own.",
    arbiter_note = None,
)
```

---

### GUI.MOD.6 — EMERGENCY RECONSTRUCTION

#### Design Rationale
First of Guild's two structure-resilience Reacts (paired with GUI.MOD.7): when Guild loses a structure, Guild immediately rebuilds in an adjacent district rather than the same one (physically consistent — the original slot may now be contested or hostile). Real finding: the cost spans Capacity (Guild-native) and Capital (Syndicate's) — same cross-resource-holding question raised on several Ghost cards, now confirmed recurring across factions, not Ghost-specific.

#### Card Story
A structure comes down — sabotage, a lost contest, doesn't matter. Guild's crews don't wait for instructions; they're already breaking ground next door, paid for out of an emergency fund that exists for exactly this.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Structural resilience under attack is a clean, doctrinally central Guild beat — "our people build permanence" made mechanical. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("you can't erase the blueprint") lands the doctrine. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = None` — reasonable; this is a defensive/economic reflex, not a doctrinal statement scored per Principle 11. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Guild, real taxonomy (Territory/Add/StructureBlock, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory×Add valid per the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | 2-resource cost for a structure replacement is meaningful but not prohibitive; player-choice targeting (adjacent district, Guild's pick) keeps it flexible without being unconstrained. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `structure_block.removed(faction=Guild)` — confirmed vocabulary, self-scoped by design (reacting to Guild's own loss, not the `faction=Any` ambiguity pattern). | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district` is a player choice among Guild-adjacent districts — a normal targeting mechanic, not a determinacy issue (see Outcome determinacy row). | Art 01 §6–7 |
| Supported by components | ✓ | Structure block placement reuses the standard mechanism; GR 8.2 (max 1 structure/faction/district) is a generically enforced constraint, not a gap specific to this card. | Art 02 §6–8; GR 8.2 |
| Supported by game procedure | ✓ | Reuses existing structure-removal event and placement mechanism; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above covers P26. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch; the acting-choice target selection is a declared parameter, not a probabilistic or hidden outcome. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Real cost specified, but spans Capacity (Guild-native) and Capital (Syndicate's) — same cross-resource-holding question flagged on several Ghost cards, confirmed recurring across factions. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Gated on Guild losing a structure — inherently reactive/defensive, moderate frequency in aggressive games. |  |
| Firing window (ModReactCard) | ⚠ | GUI.MOD.7 shares the identical trigger (`structure_block.removed(faction=Guild)`) — both fire off the same event; no documented rule on sequencing or whether both resolve simultaneously. | | 
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary replacement — no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not ring-scoped. |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | |  |  |

```python
GUI.MOD.6 = Card(
    id      = "GUI.MOD.6",  card_id = "GUI.MOD.6",  version = "v0.1",
    name    = "Emergency Reconstruction",
    tagline = "You can knock down the building, but you can't erase the blueprint.",
    type    = ModReactCard,  faction = Guild,
    layer   = Territory,  function = Add,  subject = StructureBlock,

    trigger         = structure_block.removed(faction=Guild),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating = 1,

    resolution = Automatic,  threshold = None,  resolution_type = Transactional,
    ring_mod = None,  doctrine_mod = None,

    target_district = faction(Guild).district.adjacent_to(trigger.district).acting_choice,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Guild).presence_in(target_district),
    cost            = list([Resource(Capacity, 1), Resource(Capital, 1)]),
    boost           = None,  # scaffolded, not addressed

    success     = arbiter.place(structure_block, district=target_district, faction=Guild, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    ps_framing   = None,  # scaffolded, not addressed
    narrative    = None,
    perspectives = None,
    design_note  = "Scaling structural defense. Reacts to the physical removal of a Guild structure (whether by covert Demolish or public act). Guild spends heavy resources to instantly place a replacement structure in an adjacent district. Ensures their structure count remains constant even under heavy attack.",
    arbiter_note = None,
)
```

---

### GUI.MOD.7 — WORKER RETALIATION

#### Design Rationale
Second of Guild's structure-resilience Reacts — shares GUI.MOD.6's exact trigger (`structure_block.removed(faction=Guild)`) but responds with presence flooding in the *same* district rather than rebuilding adjacent. Confirms the firing-window overlap flagged from GUI.MOD.6's side: both cards fire off the identical event, with no documented sequencing or exclusivity rule.

#### Card Story
The structure's gone, but the workers who built it haven't left. They flood the site — no equipment, no permits, just numbers — and the attacker who cleared the ground finds it re-occupied before they can claim it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "Denial through presence flooding" is a distinct, coherent response from GUI.MOD.6's "rebuild elsewhere" — different tactical answer to the same threat. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = None` — reasonable, same reflexive-defense reasoning as GUI.MOD.6. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Guild, real taxonomy (Territory/Add/PresenceToken, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory×Add valid per the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | 1-resource cost for 2 chips in the same district is efficient but bounded by GR 8.1's 6-chip cap (generically enforced); reasonable as a denial tool. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | Same confirmed, self-scoped trigger as GUI.MOD.6. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district` — correct, same-district response (contrast with GUI.MOD.6's adjacent-district choice). | Art 01 §6–7 |
| Supported by components | ✓ | Chip placement reuses the standard mechanism; GR 8.1 cap generically enforced. | Art 02 §6–8; GR 8.1 |
| Supported by game procedure | ✓ | Reuses existing structure-removal event and chip-placement mechanism. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above covers P26. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cost is Capacity only (Guild-native) — no cross-resource question, unlike GUI.MOD.6. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Same as GUI.MOD.6 — gated on Guild losing a structure. |  |
| Firing window (ModReactCard) | ⚠ | Confirmed overlap with GUI.MOD.6 — identical trigger, no documented rule on whether both fire on the same removal event (rebuild-adjacent + flood-same-district simultaneously would be a strong combined response). |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary placement — no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct. |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | |  |  |

```python
GUI.MOD.7 = Card(
    id      = "GUI.MOD.7",  card_id = "GUI.MOD.7",  version = "v0.1",
    name    = "Worker Retaliation",
    tagline = "The site is clear, but the workers are still here.",
    type    = ModReactCard,  faction = Guild,
    layer   = Territory,  function = Add,  subject = PresenceToken,

    trigger         = structure_block.removed(faction=Guild),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating = 2,

    resolution = Automatic,  threshold = None,  resolution_type = Transactional,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = Resource(Capacity, 1),
    boost           = None,  # scaffolded, not addressed

    success     = arbiter.place(presence_chip, district=target_district, faction=Guild, count=2),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    ps_framing   = None,  # scaffolded, not addressed
    narrative    = None,
    perspectives = None,
    design_note  = "Scaling structural defense. If an opponent manages to remove a Guild structure, Guild burns Capacity to flood the district with 2 presence chips. The territory becomes completely infested with Guild influence, preventing the attacker from claiming the space they just cleared.",
    arbiter_note = None,
)
```

---

### GUI.MOD.8 — SITE CLEARANCE

#### Design Rationale
Reacts to *any* structure removal, including Guild's own — deliberately inclusive by design (design_note: "pairs with GUI.MOD.2 to ensure Guild profits on both ends of a structure's lifecycle"), not the same "possible bug" pattern as the `faction=Any` self-fire questions flagged elsewhere in the corpus. Real finding: when Guild's own structure is removed, this card, GUI.MOD.6, and GUI.MOD.7 could all fire off the same single event if Guild holds all three — a three-way firing-window overlap, sharper than the two-way overlap already flagged between GUI.MOD.6/7.

#### Card Story
A structure comes down somewhere in the city — anyone's structure, any cause. Guild already has the demolition and cleanup contract on file. The check clears regardless of who's crying about the wreckage.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "Guild profits on both ends of a structure's lifecycle" (paired with GUI.MOD.2) is a clean, cynical-but-coherent doctrine beat. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("we built it... you blew it up, we get paid to clean it up") lands the doctrine precisely. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = None` — reasonable; routine passive income, not a doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Guild, real taxonomy (Economy/Add/NativeResource, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy×Add valid per the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Broadest trigger in the Guild set (any structure removal, any faction) — no restriction, no cost. Same "least-gated" balance concern as GUI.MOD.2/4/7. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `structure_block.removed(faction=Any)` — confirmed vocabulary; the broad scope is intentional per the design_note, not the same ambiguity pattern as other cards' `faction=Any`. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` at the field level, but the mutation itself reads `trigger.district`'s native resource — correct. | Art 01 §6–7 |
| Supported by components | ✓ | Dynamic resource-type resolution (`district(...).native_resource`) reuses existing district metadata; no new component. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing structure-removal event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above covers P26. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | `cost=None` — same whole-set gate as the rest of the corpus (04-n178), sharpened by the Balance flag above (broadest trigger, no cost). | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ⚠ | Broadest trigger in the set — any structure removal, any faction, any cause. High potential frequency; ties directly into the Balance flag. |  |
| Firing window (ModReactCard) | ⚠ | Real 3-way overlap: when Guild's own structure is removed, this card fires alongside GUI.MOD.6 and GUI.MOD.7 off the identical underlying event (`structure_block.removed`, this card's `faction=Any` superset includes Guild) — sharper than the 6/7 pairwise overlap already flagged. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat yield, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; fires table-wide by design. |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | |  |  |

```python
GUI.MOD.8 = Card(
    id      = "GUI.MOD.8",  card_id = "GUI.MOD.8",  version = "v0.1",
    name    = "Site Clearance",
    tagline = "We built it, we get paid. You blew it up, we get paid to clean it up.",
    type    = ModReactCard,  faction = Guild,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = structure_block.removed(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating = 1,

    resolution = Automatic,  threshold = None,  resolution_type = Transactional,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,
    boost           = None,  # scaffolded, not addressed

    success     = faction(Guild).resources.add(1, district(trigger.district).native_resource),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = None,
    ps_framing   = None,  # scaffolded, not addressed
    narrative    = None,
    perspectives = None,
    design_note  = "Passive demolition income. Whenever ANY structure is removed, Guild takes the cleanup contract and receives 1 of the district's native resource type from the Reservoir. Pairs with GUI.MOD.2 to ensure Guild profits on both ends of a structure's lifecycle.",
    arbiter_note = None,
)
```

---

### GUI.MOD.9 — FIELD SUPERVISOR
[↑ Guild](#guild)

#### Design Rationale
Guild's certification-network income card, keyed to a different trigger surface than MOD.2/MOD.3/MOD.4 (structure placement) or MOD.8 (structure removal). Every faction's climb to Established influence in a district is a public administrative milestone — a Silver Established Marker placed on the board. Guild's inspection and permitting offices are the ones who process that filing, regardless of whether the settling faction has built anything yet. No structure requirement means this card fires even in districts Guild's other income cards never reach — pure presence accumulation by an opponent is enough.

This completes a four-angle passive-income doctrine across the Guild MOD set: build (MOD.2/3/4), demolish (MOD.8), and now settle (MOD.9). Each keys to a distinct, unambiguous, publicly observable board-state delta — no overlap, no redundant coverage. This card uses the standard 22-row checklist format used elsewhere in the corpus.

#### Card Story
A Network survey team finally holds enough ground in a Baryo block to call it theirs — the second marker that tips them to Established. Within the day, a Guild inspector is on-site with a checklist and a fee schedule. Nobody's foothold in New Meridian goes unrecorded, and unrecorded means uncharged.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | certification/permitting income keyed to a territorial milestone is a distinct, coherent fourth angle alongside build/demolish. | Art 00 §7 |
| Voice fit | ✓ | Tagline and perspectives all read in Guild's transactional-but-thorough register. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Guild submitter=+1 matches the scale of MOD.2/3/4/8. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/FactionSpecific (Guild), real taxonomy (Economy/Add/NativeResource, 04-n175) — matches MOD.2/3/4/8's shape. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy×Add valid per the matrix, checked directly rather than just inherited from the family. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | Flat +1 Capacity, no restriction, but keyed to a genuinely bounded event (Established-marker placement, one per faction per district, capped by 21 districts × 4 opponents) — less exposed to the "least-gated/high-frequency" concern flagged on GUI.MOD.2/4/8 since the trigger itself is inherently bounded. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate — explicitly stated in the spec (`persistence=Immediate`), unlike most of the corpus where this field is absent. | Art 04 §5 P19 |
| Persistence | ✓ | Explicitly declared (`persistence=Immediate, persistence_condition=None, persistence_effect=None`) — this card is ahead of the rest of the corpus on this field, not part of the deferred-field gap. | Art 04 §6.2 |
| Trigger validity | ✓ | `established_marker.placed(faction=opponent)` — confirmed vocabulary, correctly scoped, no self-fire ambiguity. | Art 04 §6.3 |
| Portrait validity | ✓ | submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district` — correct. | Art 01 §6–7 |
| Supported by components | ✓ | Standard resource-grant mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing Established-marker-placement event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ✓ | Already scaffolding-complete — `ps_framing`, `boost`, `target_taxonomy` all explicitly declared (ahead of the rest of the corpus, which needed 04-n177 scaffolding added). Only `resolution_type` absent. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story is concrete and well-formed (unlike most of the corpus, this was never a placeholder). `narrative` field itself is still `None`, but Card Story satisfies P26. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | `cost=None` — same whole-set Floor Act/value_rating gate as the rest of the corpus (04-n178). | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ | moderate, front-loaded, bounded by 21 districts × 4 opponents — holds up. |  |
| Firing window (ModReactCard) | ✓ | no other Guild MOD reacts to `established_marker.placed`; distinct from MOD.2's `structure_block.placed`. Holds up. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | unambiguous trigger, bounded flat yield. |  |
| Stack behavior (ModReactCard) | ⚠ | Whether multiple copies fire independently is asserted, not derived from a documented rule — same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | citywide, matching MOD.2's baseline. |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | |  |  |

```python
GUI.MOD.9 = Card(
    id      = "GUI.MOD.9",  card_id = "GUI.MOD.9",  version = "v0.1",
    name    = "Field Supervisor",
    tagline = "Every foothold in this city gets inspected. Guild does the inspecting.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = Economy,  function = Add,  subject = NativeResource,

    trigger         = established_marker.placed(faction=opponent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating = 1,

    resolution = Automatic,  threshold = None,  resolution_type = Transactional,
    ring_mod = None,  doctrine_mod = None,

    persistence = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    target_taxonomy = None,
    affinity        = None,
    restriction     = None,  # no presence requirement — Guild's certification network is citywide
    cost            = None,
    boost           = None,

    success     = faction(Guild).resources.add(1, Capacity),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Guild: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = None,
    perspectives = {
        Guild:       "Somebody's putting down roots. That means permits, inspections, code review. That means us.",
        Directorate: "Guild's paperwork trail on every Established filing is, admittedly, more thorough than ours.",
        Ghost:       "A structure-independent income trigger. Notable — Guild reads territory before it reads construction.",
        Network:     "Guild's inspectors show up before our own press release does. Efficient, if a little presumptuous.",
        Syndicate:   "A fee nobody negotiated and everybody pays. That's a business model we respect.",
    },
    design_note  = "Fourth angle of Guild's passive-income quartet (MOD.2 build / MOD.8 demolish / MOD.9 settle / MOD.4 premium-rate variant). Fires on any opponent's Established Marker placement, citywide, no structure or presence requirement. Flat +1 Capacity, Automatic, Immediate. Distinct trigger object from MOD.2 (structure_block.placed) — no overlap or double-count risk even if a single covert op both adds presence past the Established threshold and places a structure in the same beat.",
    arbiter_note = None,
)
```

---

### GUI.MOD.10 — CONTRACTOR'S FAVOR
[↑ Guild](#guild)

#### Design Rationale
Guild's only mechanic that reaches into Contested District Resolution (Art 03 §10) without Guild itself being a contesting faction. When a district goes Contested, Guild — already present or adjacent, already the district's contractor of record — commits its crews and material schedule to favor one side. That commitment is registered immediately (Guild doesn't wait for the battle to declare it) and stands as a Seasonal condition until §10 actually resolves that district, whenever in the Quarter that happens.

This is new mechanical ground: the existing ModBattleCard subclass lets a *contesting* faction modify its own or a *named opponent's* total, played live during §10.1.2. Contractor's Favor is a *ModReactCard* — it fires earlier, off a different trigger (`tension_marker.placed`, not the Battlefield Strength declaration step), and its effect targets a named faction's total regardless of whether Guild itself is contesting that district. The tradeoff for committing early is fizzle risk: if the named faction is no longer a contesting (Dominant) faction by the time §10.1.1 actually identifies contestants, Guild's condition has no effect — the political ground shifted out from under an early bet. This is the narrative engine of the card, not a bug: Guild reads the room the moment it goes tense, and sometimes reads it wrong.

Restriction (Guild Present in the district or an adjacent district) keeps this tied to actual territorial investment — Guild needs to already have people nearby to know whose crews to prioritize. Target is any Dominant/contesting faction, no doctrinal constraint (Art 00 §7 pentagram) — Guild's doctrine here is transactional, not political: contracts go to whoever Guild backs, not to an ally by default.

**Outstanding Issue:** Applying this card's registered condition requires a new ARBITER-facing step in Art 03 §10.1.2 (Calculate and Declare Totals) — check for active Guild Seasonal conditions on the contested district and apply the registered delta to the named faction's total, alongside Step 1.2.2 (Commit) and Step 1.2.3 (Reveal & Validate), where Battlefield Modifier Cards and Intel Tokens are now handled. No such step currently exists. Per Governing Rule 6.1 / Design Pillar 4.7b, this must be defined as a generalizable Art 03 procedure before the card is fully executable at the table — tracked as new PM05 item 04-n148. The registered condition is public board state (Governing Rule 7.2a — no hidden board surface state), so contesting factions will know a Guild condition is active on the district before they declare their own totals; this is intended, not an oversight.

**Deeper issue (04-n176):** No Layer/Function/Subject assignment was attempted here, and not because tagging was skipped — `arbiter.register_battlefield_modifier(...)` doesn't correspond to any effect shape the taxonomy system (Territory/Economy/Information/Submission/Standing × the Layer×Function matrix) actually supports. This is a level deeper than 04-n148's gap (missing Art 03 procedure): even once §10.1.2 knows how to apply a registered modifier, the card's fundamental mechanic — a third-party faction pre-committing a Battlefield Strength delta to a named contesting faction, off-cycle from the battle itself — has no home in the current taxonomy at all. Direction: this needs redesign, not a new taxonomy category invented to fit it. See 04-n176.

#### Card Story
Tension breaks out over a contested block, and every material order in the district suddenly has two delivery dates — one for the faction Guild's crews like working with, one for everyone else. By the time the district actually goes to the wire, one side got their scaffolding early.

04-n148 (missing Art 03 procedure) and 04-n176 (no taxonomy home) are structurally serious: this card fails Card type fit/Taxonomy fit outright (not just "pending"), and Supported by game procedure is a real Governing Rule 6.1/Design Pillar 4.7b violation as currently drafted (new ARBITER behavior used before being defined as a generalizable procedure). Flagged in full, not force-closed.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Guild committing construction priority to a contesting faction, transactionally rather than doctrinally, is a coherent, distinct mechanic from anything else in the set. | Art 00 §7 |
| Voice fit | ✓ | tagline and all 5 perspectives read correctly in-voice. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Guild submitter=+1 only, no doctrine_mod — correctly reflects "transactional, not political." | Art 04 §6.5 |
| Card type fit | ⚠ | ModReactCard/FactionSpecific is the right subclass, but `layer=None, function=None, subject=None` isn't a taxonomy gap to close later — it's a symptom of the deeper problem below. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ⚠ **(blocker, 04-n176)** | `arbiter.register_battlefield_modifier(...)` doesn't correspond to any Layer×Function pairing the taxonomy system supports. Direction: redesign, not a new category invented to fit it. This is the card's core blocker. | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n176 |
| Balance | ⚠ | Fizzle risk (named faction may not still be contesting at §10) is a deliberate design tension, not a flaw — but genuinely hard to finalize while the taxonomy/mechanic itself is unresolved. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Seasonal correctly fits "ongoing condition across multiple subsequent actions." | Art 04 §5 P19 |
| Persistence | ✓ | Explicitly declared (`persistence=Seasonal`) — ahead of the rest of the corpus on this field. | Art 04 §6.2 |
| Trigger validity | ✓ | `tension_marker.placed` confirmed §6.3 vocabulary. | Art 04 §6.3 |
| Portrait validity | ✓ | submitter-bounded only, correctly excludes the named target_faction per P16. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | district + adjacency-based restriction ties this to real territorial investment. | Art 01 §6–7 |
| Supported by components | ⚠ | No physical marker/component represents the "registered condition" on the board beyond the card itself — tied to the same gap as the row below. | Art 02 §6–8 |
| Supported by game procedure | ⚠ **(blocker, 04-n148)** | Art 03 §10.1.2 has no step that reads a registered Guild condition and applies it. Per Governing Rule 6.1/Design Pillar 4.7b, new ARBITER behavior must be defined as a generalizable procedure *before* the card is finalized — as currently drafted, the card's `arbiter_note` describes behavior that doesn't yet exist as a defined procedure. | Art 03 §10.1.2; GR 6.1; Design Pillar 4.7b; PM05 04-n148 |
| Data schema validation | ⚠ | `layer/function/subject=None` (deliberate, tied to 04-n176) plus missing `resolution_type` (added as scaffolding). | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story is concrete and well-formed — the fizzle-risk narrative tension is genuinely the point, not a gap. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic; the fizzle-risk contingency is a real-world board-state dependency, not a hidden or probabilistic outcome — doesn't violate P27. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Real cost specified (Capacity×1) — not gated on 04-n178 the way cost-less cards are, but whether 1 Capacity is correctly priced for a ±2 Battlefield Strength swing can't be finalized while the mechanic itself is blocked on 04-n176. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Contested is a specific, less-common board state — low-moderate frequency holds up. |  |
| Firing window (ModReactCard) | ✓ | no race with other Guild MODs. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Guild's registration action is unconditional; the eventual d10 battle roll is untouched. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as originally flagged — still open, not resolved. |  |
| Ring constraint (ModReactCard) | ✓ | redundant with the presence/adjacency restriction, correctly omitted. |  |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | |  |  |

```python
GUI.MOD.10 = Card(
    id      = "GUI.MOD.10",  card_id = "GUI.MOD.10",  version = "v0.1",
    name    = "Contractor's Favor",
    tagline = "We don't pick sides. We pick delivery dates.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    trigger         = tension_marker.placed(district=district(trigger.target)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = Transactional,
    ring_mod = None,  doctrine_mod = None,

    persistence = Seasonal,
    persistence_condition = None,
    persistence_clearing_trigger = None,
    persistence_effect    = None,

    target_district = trigger.district,
    target_faction  = faction.named,   # declared at trigger — must be a Dominant (contesting) faction in target_district at time of declaration
    target_object   = None,
    target_taxonomy = None,
    declared_params = direction.named, # "Support" (+2 to target_faction's Battlefield Strength total) or "Withhold" (−2); declared alongside target_faction
    affinity        = None,
    restriction     = (
        faction(Guild).presence_in(target_district)
        or faction(Guild).presence_in(district.adjacent_to(target_district))
    ),
    cost            = Capacity * 1,
    boost           = None,

    success = arbiter.register_battlefield_modifier(
        district=target_district,
        faction=target_faction,
        magnitude=magnitude_from(declared_params),  # Support = +2, Withhold = −2
    ),
    # Applied at Art 03 §10.1.2 (Calculate and Declare Totals) if target_faction is still a contesting
    # (Dominant) faction in target_district when §10.1.1 identifies contestants; otherwise the condition
    # lapses with no effect. Condition clears at Phase 21 (End of Quarter) regardless of outcome.
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Guild: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = None,
    perspectives = {
        Guild:       "We don't fight for the block. We decide who gets the scaffolding on time.",
        Directorate: "An unlicensed thumb on the scale before the contest even opens. Noted, not actionable.",
        Ghost:       "A public commitment with private timing risk. Guild bets on today's map holding through the Quarter.",
        Network:     "Everyone can see who Guild backed. That's a story whether the bet pays off or not.",
        Syndicate:   "Guild's monetizing uncertainty before the dice even get picked up. Professionally, we approve.",
    },
    design_note  = "First Guild card to influence Battlefield Strength (§10) without Guild itself contesting the district. New mechanical pattern: a Seasonal ModReactCard registers a delta against a named contesting faction's total, resolved later at §10.1.2 rather than played live like a ModBattleCard. Fizzle risk (named faction may no longer be contesting when §10 actually resolves) is the cost of early commitment and is the card's core narrative tension. Restriction requires Guild Present or adjacent in the district. Target is any Dominant faction — no doctrine_mod; Guild's construction contracts are transactional, not political. Requires new Art 03 §10.1.2 procedure step — tracked 04-n148 (Outstanding Issue). `persistence_clearing_trigger` is None — the card clears at Phase 21 (End of Quarter) regardless of outcome, the default Seasonal expiry already implied by `persistence`; no discrete clearing event exists for this card.",
    arbiter_note = "On trigger (Tension Marker placed in any district): if Guild satisfies restriction, Guild may declare target_faction (must currently be Dominant/tied in the district) and direction (Support +2 / Withhold −2), and pay Capacity×1. ARBITER records the condition publicly against the district. At §10.1.1 (Identify Contesting Factions), if target_faction is among the identified contestants: apply the registered magnitude to target_faction's declared total at §10.1.2, alongside Battlefield Modifier Cards and Intel Tokens. If target_faction is not contesting: condition lapses, no effect, no refund. Condition clears automatically at Phase 21 if §10 does not resolve the district this Quarter. Procedure step formalization pending 04-n148.",
)
```

---

### GUI.MOD.11 — SITE FOREMAN

#### Design Rationale
Guild's ModBattleCard set, replicating the Directorate/Ghost/Network pattern (2 Boost +1/+2, 2 Hinder −1/−2). Doctrine per §5a and modifier_card_ideas.md's provisional voice seed: "construction crews, material stockpiles, structural expertise — physical commitment of resources to hold ground." Distinct from Contractor's Favor (GUI.MOD.10, a ModReactCard, pre-registered before §10 opens) — these are live-played at §10.1.2 like any other ModBattleCard. Weaker Boost tier (+1): experienced crew leadership, not yet material commitment. Same no-cost/playtest-flagged (04-n94) terms as the rest of the subclass.

#### Card Story
A foreman who's worked this district before shows up, clipboard in hand, and starts telling people where to stand — reinforcing whichever side the playing faction has named.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Experienced crew leadership committed to a live contest is a grounded expression of Guild's construction doctrine (§5a). | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only (`perspectives`/`design_note` schema-locked None); construction-expertise register. | Art 00 §9 |
| Doctrine alignment | ✓ | Boost via physical construction expertise; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Guild's Asset-category naming slot; distinct from ModReactCard GUI.MOD.10. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Boost tier per the locked Boost/Hinder pattern; no cost step exists for this subclass; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value, locked whole-subclass. | Art 04 §6.1–§6.2; PM02 L269 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None` correct for a faction-deck card. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.11 = Card(
    id      = "GUI.MOD.11",  card_id = "GUI.MOD.11",  version = "v0.1",
    name    = "Site Foreman",
    tagline = "Someone who's run a hundred jobs like this one knows exactly where to put the weight.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A foreman who's worked this district before shows up, clipboard in hand, and starts telling people where to stand.",
    arbiter_note = "Playable by any faction, not just Guild (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### GUI.MOD.12 — MATERIAL STOCKPILE

#### Design Rationale
Stronger Boost tier (+2) — physical material committed to the contest, not just labor. The escalation from Site Foreman's expertise to Material Stockpile's tonnage is the same logic as Guild's economy generally: everything Guild does ends up as a physical, visible commitment. Same no-cost/playtest-flagged (04-n94) terms as GUI.MOD.11.

#### Card Story
Pallets of material that were supposed to go somewhere else get rerouted here instead — nobody asks who authorized it, and the named faction's position is reinforced.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Committed physical material is a grounded expression of Guild's "everything leaves a physical artifact" doctrine (§5a). | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only; material-logistics register, distinct from GUI.MOD.11's labor framing. | Art 00 §9 |
| Doctrine alignment | ✓ | Boost via physical material commitment; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Guild's Equipment-category naming slot. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Boost tier (magnitude 2/value_rating 2) per the locked Boost/Hinder pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value, locked whole-subclass. | Art 04 §6.1–§6.2; PM02 L269 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None` correct for a faction-deck card. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.12 = Card(
    id      = "GUI.MOD.12",  card_id = "GUI.MOD.12",  version = "v0.1",
    name    = "Material Stockpile",
    tagline = "Whatever the job needs, it's already on site, already paid for.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Pallets of material that were supposed to go somewhere else get rerouted here instead. Nobody asks who authorized it.",
    arbiter_note = "Playable by any faction, not just Guild (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### GUI.MOD.13 — PERMIT DELAY

#### Design Rationale
Weaker Hinder tier (−1). Guild "cannot operate covertly in principle" (§5a) — even its suppression tools are procedural and visible, not sabotage. A permit delay is bureaucratic friction, not an attack. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
A signature is missing from a form nobody remembers filing — work on the named faction's position stops until someone finds it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Bureaucratic/procedural friction is the grounded expression of Guild's "cannot operate covertly in principle" doctrine (§5a). | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only; procedural-friction register, no sabotage language. | Art 00 §9 |
| Doctrine alignment | ✓ | Hinder via visible procedural friction, not covert action; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Guild's Tactic-category Hinder slot. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Hinder tier per the locked Boost/Hinder pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value, locked whole-subclass. | Art 04 §6.1–§6.2; PM02 L269 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None` correct for a faction-deck card. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.13 = Card(
    id      = "GUI.MOD.13",  card_id = "GUI.MOD.13",  version = "v0.1",
    name    = "Permit Delay",
    tagline = "The paperwork isn't wrong. It's just going to take a while.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A signature is missing from a form nobody remembers filing. Work stops until someone finds it.",
    arbiter_note = "Playable by any faction, not just Guild (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### GUI.MOD.14 — STRUCTURAL CONDEMNATION

#### Design Rationale
Stronger Hinder tier (−2), completing Guild's 2 Boost/2 Hinder pattern. Escalates Permit Delay from friction into a formal finding — Guild's engineers declare something structurally compromised, and the declaration itself is the weapon. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
Guild's engineers sign off on a finding: unsafe as built. It's technically true. It's also exactly what was needed to make the named faction's position untenable.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A formal, procedural finding used as leverage is the escalated form of Guild's "cannot operate covertly" doctrine — still visible, still on the record. | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only; same procedural register as GUI.MOD.13, escalated to a formal finding. | Art 00 §9 |
| Doctrine alignment | ✓ | Hinder via visible, on-the-record procedure, not covert action; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Guild's Tactic-category escalated Hinder slot alongside GUI.MOD.13. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Hinder tier (magnitude 2/value_rating 2) per the locked Boost/Hinder pattern; playtest-flagged (04-n94). | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value, locked whole-subclass. | Art 04 §6.1–§6.2; PM02 L269 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None` correct for a faction-deck card. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2/1.2.3/1.2.4 and §10.1.4 cleanup fully cover this card. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event, no mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention. | PM05 04-n94 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.14 = Card(
    id      = "GUI.MOD.14",  card_id = "GUI.MOD.14",  version = "v0.1",
    name    = "Structural Condemnation",
    tagline = "The inspection report is thorough, professional, and devastating.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Guild's engineers sign off on a finding: unsafe as built. It's technically true. It's also exactly what was needed.",
    arbiter_note = "Playable by any faction, not just Guild (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### GUI.MOD.15 — STRUCTURAL SURVEY

#### Design Rationale
Replicates the Directorate ModActionCard pattern (DIR.MOD.14–25, 09-06/04-n157) to Guild — locked format: 4 `threshold_delta` (+5/+10/+15/+20) + 2 `success_multiplier` (n=1/n=2) + 4 `ps_shift` (self +1/+2, target −1/−2) + 2 `cost_reduction` (n=1/n=2, PA-only), `cost=None` uniformly, `value_rating` 1–4 mirroring tier. Guild voice: construction and material, visible-by-doctrine (§5a) — same doctrinal lens as Guild's shipped ModBattleCard set (GUI.MOD.11–14). This card: minor threshold_delta tier (+5), self-only, fits construction/material doctrine cleanly.

#### Card Story
An engineering assessment, filed in advance, clears the ground before the first shovel goes in.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pre-cleared engineering assessment is the clean mechanical expression of Guild's construction doctrine. | Art 00 §7 |
| Voice fit | ✓ | `faction=Guild`; narrative reads in the material/construction register. | Art 00 §9 |
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
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass; out of scope for 04-n178. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.15 = Card(
    id      = "GUI.MOD.15",  card_id = "GUI.MOD.15",  version = "v0.1",
    name    = "Structural Survey",
    tagline = "The engineering assessment comes back clean before anyone asks for one.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=5),  # self-only — no faction param on this variant (§6.3). Tracked at PM05 04-n170; remove this comment once resolved.
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "An engineering assessment, filed in advance, clears the ground before the first shovel goes in.",
    arbiter_note = "Attach at Dispatch to any CA/PA in Guild's own submitted packet (Art 03 §9.1.1) — no card-level host restriction.",
)
```

---

### GUI.MOD.16 — LOAD-BEARING CONFIDENCE

#### Design Rationale
Mid tier (+10). Same structure as GUI.MOD.15, self-only.

#### Card Story
Verified material integrity means nothing on this build is guesswork — the crew already knows it'll hold.

**Design checklist:** Same disposition as GUI.MOD.15.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same construction-doctrine basis. | Art 00 §7 |
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
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.16 = Card(
    id      = "GUI.MOD.16",  card_id = "GUI.MOD.16",  version = "v0.1",
    name    = "Load-Bearing Confidence",
    tagline = "Every material on site has already been tested and certified.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=10),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Verified material integrity means nothing on this build is guesswork — the crew already knows it'll hold.",
    arbiter_note = "Self-only, same basis as GUI.MOD.15.",
)
```

---

### GUI.MOD.17 — PERMIT FAST-TRACK

#### Design Rationale
Third tier (+15). Reframed from "Permit Delay Imposed" (hostile) per 04-n170.

#### Card Story
A favorable review clears part of the build in advance — nothing left for an inspector to hold up.

**Design checklist:** Same disposition as GUI.MOD.15. Narrative independently checked — clean self-only, no hostile residue.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same construction-doctrine basis. | Art 00 §7; PM05 04-n170 |
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
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.17 = Card(
    id      = "GUI.MOD.17",  card_id = "GUI.MOD.17",  version = "v0.1",
    name    = "Permit Fast-Track",
    tagline = "The review board signs off before the ink on the application dries.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=15),
    value_rating    = 3,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A favorable review clears part of the build in advance — nothing left for an inspector to hold up.",
    arbiter_note = "Reframed from a hostile-flavored seed concept per 04-n170, same basis as DIR.MOD.15/16.",
)
```

---

### GUI.MOD.18 — CERTIFIED TO CODE

#### Design Rationale
Capstone tier (+20), closing Guild's `threshold_delta` quartet. Clean self-only narrative.

#### Card Story
Every code requirement cleared ahead of time — there's nothing left for an inspection to catch.

**Design checklist:** Same disposition as GUI.MOD.15.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same construction-doctrine basis. | Art 00 §7 |
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
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.18 = Card(
    id      = "GUI.MOD.18",  card_id = "GUI.MOD.18",  version = "v0.1",
    name    = "Certified to Code",
    tagline = "Full regulatory sign-off, in hand, before the first beam goes up.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=20),
    value_rating    = 4,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Every code requirement cleared ahead of time — there's nothing left for an inspection to catch.",
    arbiter_note = "Capstone tier — log actual play outcomes before treating +20 as balanced (04-n157, same playtest caveat as the rest of this set).",
)
```

---

### GUI.MOD.19 — UNION CREW

#### Design Rationale
Common tier (n=1) of Guild's `success_multiplier` pair. Self-only, skilled-labor framing fits doctrine cleanly.

#### Card Story
An experienced crew doesn't just meet the spec — they turn a routine build into an exceptional one.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Skilled-labor amplification fits construction doctrine. | Art 00 §7 |
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
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.19 = Card(
    id      = "GUI.MOD.19",  card_id = "GUI.MOD.19",  version = "v0.1",
    name    = "Union Crew",
    tagline = "Experienced hands turn a routine job into something better than scheduled.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "An experienced crew doesn't just meet the spec — they turn a routine build into an exceptional one.",
    arbiter_note = "Self-only, amplifies Guild's own host action.",
)
```

---

### GUI.MOD.20 — OVERBUILT

#### Design Rationale
Capstone tier (n=2) of Guild's `success_multiplier` pair. Same unvalidated-magnitude caveat as every n=2 success_multiplier card.

#### Card Story
A structure goes up well past the minimum required — the extra margin amplifies what the build was already meant to do.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "Overbuilt" is a strong Guild-specific concept — excess-as-doctrine. | Art 00 §7 |
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
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.20 = Card(
    id      = "GUI.MOD.20",  card_id = "GUI.MOD.20",  version = "v0.1",
    name    = "Overbuilt",
    tagline = "It goes up stronger than the minimum ever required.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A structure goes up well past the minimum required — the extra margin amplifies what the build was already meant to do.",
    arbiter_note = "Rare/capstone tier — log actual play outcomes before treating n=2 as balanced (04-n157, same playtest caveat as 04-n94).",
)
```

---

### GUI.MOD.21 — COMMUNITY GROUNDBREAKING

#### Design Rationale
Self-boost minor tier (+1) of the `ps_shift` matrix. `faction="acting"` needs no host-declared target — no submission-validity dependency.

#### Card Story
Visible investment in a neighborhood buys goodwill Guild doesn't have to ask for.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Visible-investment fits Guild's "visible by doctrine" framing (§5a). | Art 00 §7 |
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
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.21 = Card(
    id      = "GUI.MOD.21",  card_id = "GUI.MOD.21",  version = "v0.1",
    name    = "Community Groundbreaking",
    tagline = "Visible investment in the neighborhood, announced before the first day of work.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Visible investment in a neighborhood buys goodwill Guild doesn't have to ask for.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half resolves to the acting faction.",
)
```

---

### GUI.MOD.22 — RIBBON CUTTING

#### Design Rationale
Self-boost major tier (+2) of the `ps_shift` matrix — same basis as GUI.MOD.21, doubled magnitude.

#### Card Story
A completed project gets the full ceremony — cameras, officials, and Guild's name front and center.

**Design checklist:** Same disposition as GUI.MOD.21.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as GUI.MOD.21. | Art 00 §7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
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
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.22 = Card(
    id      = "GUI.MOD.22",  card_id = "GUI.MOD.22",  version = "v0.1",
    name    = "Ribbon Cutting",
    tagline = "A completed project, celebrated publicly, with the Guild's name on the plaque.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A completed project gets the full ceremony — cameras, officials, and Guild's name front and center.",
    arbiter_note = "Self-boost, major tier — resolves to the acting faction.",
)
```

---

### GUI.MOD.23 — INSPECTION NOTED

#### Design Rationale
Target-hinder minor tier (−1) of the `ps_shift` matrix. Same target-resolution behavior as STD.MOD.34 — resolves via host pairing, not an independent field. Separately, confirmed on review: the stub's own note that Guild's CA/PA set skews toward self/territory-directed hosts, so this card and GUI.MOD.24 have fewer eligible hosts than the equivalent Directorate/Syndicate cards — genuine faction-specific playtest question, not something this review resolves.

#### Card Story
A minor code observation gets logged against a rival's project — nothing dramatic, just on the record.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Discreet-citation fits Guild's procedural/visible register. | Art 00 §7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Minor tier; `value_rating=1` mirrors tier, but confirmed low-eligibility concern (see Design Rationale) — Guild's own CA/PA mix has fewer `target_faction`-bearing hosts than other factions' equivalents. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.23 = Card(
    id      = "GUI.MOD.23",  card_id = "GUI.MOD.23",  version = "v0.1",
    name    = "Inspection Noted",
    tagline = "A minor observation, quietly logged against someone else's project.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A minor code observation gets logged against a rival's project — nothing dramatic, just on the record.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA it's packet-paired with names as its target_faction (§6.1) — the modifier's target IS the host action, not an independently-declared field.",
)
```

---

### GUI.MOD.24 — CODE VIOLATION CITED

#### Design Rationale
Target-hinder major tier (−2) of the `ps_shift` matrix. Same target-resolution behavior and Guild-specific low-eligibility flag as GUI.MOD.23, doubled magnitude. Magnitude mirrors the established Intel Token Hinder precedent.

#### Card Story
A rival's construction gets flagged publicly for cutting corners — consistent with Guild's doctrine of keeping everything procedural and visible.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as GUI.MOD.23. | Art 00 §7 |
| Voice fit | ✓ | Strong Guild-specific voice — "procedural and visible" doctrine explicitly named. | Art 00 §9 |
| Doctrine alignment | ✓ | `faction="target"` resolves to whichever faction the host names. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Major tier; `value_rating=2` mirrors tier, same Guild-specific low-eligibility concern as GUI.MOD.23. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Card's target is the host CA/PA it's packet-paired with at Dispatch (Art 03 §9.1.1) — `faction="target"` is definitionally the host's target, not a separately-validated field. |  |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.24 = Card(
    id      = "GUI.MOD.24",  card_id = "GUI.MOD.24",  version = "v0.1",
    name    = "Code Violation Cited",
    tagline = "A rival's construction, publicly flagged for cutting corners.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "A rival's construction gets flagged publicly for cutting corners — consistent with Guild's doctrine of keeping everything procedural and visible.",
    arbiter_note = "Same target-resolution behavior as GUI.MOD.23, major tier.",
)
```

---

### GUI.MOD.25 — MATERIAL SURPLUS

#### Design Rationale
Common tier (n=1) of Guild's `cost_reduction` pair, PA-only per §6.3. Leftover-material framing fits doctrine cleanly.

#### Card Story
Leftover stock from a prior job discounts the next one — nothing wasted.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Material-reuse fits Guild's construction/material doctrine. | Art 00 §7 |
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
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.25 = Card(
    id      = "GUI.MOD.25",  card_id = "GUI.MOD.25",  version = "v0.1",
    name    = "Material Surplus",
    tagline = "Leftover stock from the last job covers most of this one.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Leftover stock from a prior job discounts the next one — nothing wasted.",
    arbiter_note = "PA host only. Attach at Dispatch (Art 03 §9.2) alongside the declared PA.",
)
```

---

### GUI.MOD.26 — IN-HOUSE FABRICATION

#### Design Rationale
Capstone tier (n=2) of Guild's `cost_reduction` pair, closing the faction set. Same flat-vs-proportional caveat as the rest of the corpus's cost_reduction capstones.

#### Card Story
Fabricating the components in-house cuts out the markup a third-party supplier would otherwise charge.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | In-house fabrication fits construction doctrine tightly. | Art 00 §7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, flat 2-unit reduction not checked against any specific PA's cost. | PM02 L256; PM05 04-n157 |
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
| Resource cost positioning | ✓ | `cost=None` — closed convention for this subclass. | PM02 L256; PM05 04-n178 |

#### Outstanding Issues

None

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | | |  |

```python
GUI.MOD.26 = Card(
    id      = "GUI.MOD.26",  card_id = "GUI.MOD.26",  version = "v0.1",
    name    = "In-House Fabrication",
    tagline = "Doing the work internally cuts out the markup entirely.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Guild,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,
    cost            = None,
    resolution_type = None,  # scaffolded, not addressed
    boost           = None,  # scaffolded, not addressed
    ps_framing      = None,  # scaffolded, not addressed

    portrait     = None,
    narrative    = "Fabricating the components in-house cuts out the markup a third-party supplier would otherwise charge.",
    arbiter_note = "Capstone cost_reduction tier — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157).",
)
```

---

