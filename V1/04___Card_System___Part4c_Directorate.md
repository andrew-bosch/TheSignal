## Directorate
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#directorate-covert-operations) · [Public Acts](#directorate-public-acts)

---

### Directorate — Covert Operations
[↑ Directorate](#directorate)

| Card | Name |
|------|------|
| [DIR.CA.1](#c21-invoke-jurisdiction) | Invoke Jurisdiction |
| [DIR.CA.2](#c22-detain) | Detain |
| [STD.CA.11](#c23-tort-interference) | Tort Interference |
| [DIR.CA.3](#c24-surveillance-placement) | Surveillance Placement |
| [DIR.CA.4](#c25-tactical-redirection) | Tactical Redirection |
| [DIR.CA.5](#directorate-sanctioned-raid) | Sanctioned Raid |
| [DIR.CA.6](#dirca6--institutional-audit) | Institutional Audit |
| [DIR.CA.7](#dirca7--institutional-brief) | Institutional Brief |
| [DIR.CA.8](#dirca8--enhanced-scrutiny) | Enhanced Scrutiny |

### DIR.CA.1 — INVOKE JURISDICTION
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's positional authority card — asserts institutional control over a named district for a full round by blocking the two primary expansion actions (STD.CA.1 Build Structure, STD.CA.3 Campaign). Beat 2 Automatic positional wager: no dice, but the card slot is committed at Dispatch. No restriction means Invoke Jurisdiction can target any district, including ones where Directorate has no presence — the Directorate's authority is institutional, not territorial. Cost Mandate×2 reflects this as a mid-tier operational spend. The block is public (per game.block parameters), signaling to the table exactly which district is under oversight.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional authority assertion over a district — blocks primary expansion actions for one round; distinct from DIR.CA.4 (repositions own presence) and SYN.CA.5 (blocks named action type for a faction) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; no presence requirement — institutional authority is not territorial; Mandate×2 calibrated as mid-tier spend; block scope outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — jurisdictional authority is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Submission/Block/CovertOperation — beats Beat 2 Automatic; block applies to STD.CA.1 and STD.CA.3 in target district for one round | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic, blocks STD.CA.1+STD.CA.3 for one round — block scope calibration outstanding (Outstanding Issue) | Art 02 §6–§7 |
| Effect duration | ✓ | One round: block applies for round=game.round only | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 positional wager fires on STD.CA.1/STD.CA.3 submissions in target district | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; jurisdictional assertion aligns with institutional doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | No new components; game.block() is an existing Beat 2 mechanism | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 positional wager; game.block() applies at Beat 2 resolution; game.block resolution (resources on blocked card) outstanding (Outstanding Issue) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Block scope — STD.CA.1/STD.CA.3 only:** DIR.CA.1 blocks STD.CA.1 and STD.CA.3 explicitly. Confirm whether this should extend to STD.CA.4 (Demolition) or STD.CA.8 (Buy Influence) to reflect true jurisdictional authority, or remain limited to the two build/presence cards by design.
- **game.block resolution:** Confirm Beat 2 block mechanic — does a blocked STD.CA.1/STD.CA.3 cost the submitter their action slot and resources, or is it returned? Needs Art 03 §9.4 Beat 2 procedure to confirm.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
DIR.CA.1 = Card(
    id      = "DIR.CA.1",  version="v1.0",
    name    = "Invoke Jurisdiction",
    tagline = "Assert institutional authority over a target district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Submission,  function = Block,  subject = CovertOperation,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any, target_faction=None, target_object=CovertOperation,
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).mandate * 2,
    success     = game.block(district(target), cards=[STD.CA.1, STD.CA.3], round=game.round, public=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate was here before the other factions arrived. Their jurisdictional authority is not theoretical.",
    perspectives = {Directorate: "This district is under institutional oversight. Expansion requires authorisation. Authorisation has not been granted."},
    design_note  = None,
    arbiter_note = None,
)
```

---

### DIR.CA.2 — DETAIN
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's permanent removal card — eliminates a faction's deployment marker from a district, permanently. The strongest single-target suppression in the Directorate set. Distinct from STD.CA.4 Demolition (removes structure blocks) and DIR.CA.4 Tactical Redirection (moves own presence): Detain removes an opponent's operational anchor. Intel restriction (fresh token required) forces Directorate to have gathered intelligence before arresting — doctrine-consistent and a resource cost beyond the Mandate spend. Successcrit returns +3 Mandate, rewarding efficient institutional execution. Failcrit −1 PS reflects the institutional embarrassment of a failed detention. ChorusNode exclusion reflects ARBITER's deployment marker's special status.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Permanent deployment marker removal — Directorate's strongest single-target suppression; distinct from STD.CA.4 (removes structures) and DIR.CA.4 (repositions own presence); Intel restriction enforces doctrine | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design — detention as institutional process | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Intel token restriction forces prior intelligence collection; ChorusNode exclusion respects ARBITER marker's special status; L183 Detention zone on Directorate public tableau | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — permanent removal is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Move/DeploymentMarker — marker moved to Detention zone (Governing Rule 8.3a compliant); function corrected S107 L226 (Remove → Move; success block uses game.move(), not game.remove()) | Art 04b §4, §5 |
| Balance | ✓ | Mandate×3, threshold 50, permanent removal — highest Directorate covert cost; successcrit Mandate recovery outstanding (Outstanding Issue) | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent: marker remains in Detention for remainder of session | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; failcrit −1 PS is game effect (not portrait), confirmed per DIR.PA.2 | Art 04 §6.2; Art 02 §11 |
| Supported by zones | ✓ | target_district = district.any; ChorusNode.deployment_marker excluded; Detention zone on Directorate public tableau (L183) | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken restriction; DeploymentMarker target; Detention zone is faction Terminal zone per L183; Intel age definition outstanding (Outstanding Issue) | Art 02 §6–§8; Art 02 §11 |
| Supported by game procedure | ✓ | Beat 3 d100 resolution; Intel check at Dispatch; ARBITER moves marker to Detention; visible to all players; no NotificationSlip needed | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Intel token age interpretation:** `intel(faction=faction(target), age_rounds<=1)` — confirm "age_rounds<=1" means Fresh token (gathered this or last round) per Art 02 §12 aging definitions.
- **Successcrit Mandate recovery:** +3 Mandate on crit success is the highest reward in the Directorate set — confirm this is intentional given Mandate×3 base cost (net zero, but only on crit).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
DIR.CA.2 = Card(
    id      = "DIR.CA.2",  version="v1.0",
    name    = "Detain",
    tagline = "Permanently remove a faction's deployment marker from a district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Move,  subject = DeploymentMarker,
    beat=3, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10},
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any, target_faction=faction(named_opponent), target_object=DeploymentMarker,
    target_taxonomy=None,
    affinity=None,
    restriction = (
        district(target).faction(target).deployment_marker >= 1
        AND intel(faction=faction(target), age_rounds<=1) >= 1
        AND district(target) != ChorusNode.deployment_marker
    ),
    cost        = resource.faction(acting).mandate * 2 + resource.faction(acting).findings * 1,
    success     = game.move(faction(target).deployment_marker, from_=district(target), to=Directorate.tableau.detention, public=True),
    successcrit = resource.faction(acting).mandate += 3,
    fail=None,
    failcrit    = faction(acting).standing -= 1,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate does not destroy — it detains. The distinction matters to them.",
    perspectives = {Directorate: "The marker has been detained. Its conversion will not occur."},
    design_note  = "L183. Marker moved to Directorate public tableau Detention zone — Governing Rule 8.3a compliant (moved, not removed from play). Permanent: marker remains in Detention for remainder of session. No NotificationSlip — detention is publicly visible on Directorate tableau. Faction Terminals may be unique per faction (L183) Cost reasoning: Requires Capital to grease the bureaucratic wheels while Mandate provides the authority.",
    arbiter_note = "Consume Intel token. Move named faction's deployment marker from target district to Directorate public tableau Detention zone. Physically place on Detention area — visible to all players. No separate notification. Crit success: return 3 Mandate to Directorate. Crit fail: no marker move; −1 PS to Directorate only.",
)
```

---


### DIR.CA.3 — SURVEILLANCE PLACEMENT
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's active surveillance card — dedicates operational resources to watch a named district this month. Resolves at Beat 2: ARBITER checks the Beat 3 resolution grid for submitted ops targeting that district and delivers an IntelDeliverySlip (op type only, no faction) to Directorate before Beat 3 fires. If no ops target the district, nothing is delivered and resources are spent. Distinct from STD.CA.5 Gather (generates an Intel token about a named faction) and GHO.CA.2 Intercept (targets a named faction's op and disrupts it): DIR.CA.3 watches territory, not actors. Op type only — no faction identity delivered; Directorate learns what is happening in the district, not who is doing it.

Episodic by design: no board marker exists (any covert placement would be public per Governing Rule 7.2a); surveillance cannot persist. Directorate must play the card to surveil. Multiple deck copies flagged for deck design pass (04-n42, 04-n43).

Redesigned S68: original model was permanent passive feed with beat3_pre_resolution delivery — invalidated (Governing Rule 7.2a prohibits covert board markers; ARBITER holds no log in L1 paper game).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Active district surveillance — watches territory this month; distinct from STD.CA.5 (faction-targeted token) and GHO.CA.2 (faction-targeted disruption) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — institutional monitoring doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; no presence requirement; Mandate×2 for intelligence without dice risk; Beat 2 blind commitment (resources spent before knowing if ops are in flight) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information / Reveal / CovertOperation — district-scoped; subject = submitted op type(s) in target district | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic, Beat 2 — no dice risk; blind commitment is the cost; empty district = nothing delivered | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — IntelDeliverySlip delivered once at Beat 2 resolution; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at Beat 2; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — institutional monitoring doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | IntelDeliverySlip (IS-xx) — Art 02 component entry pending (04-n45); 00b definition update pending (04-n46) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; ARBITER reads existing Beat 3 grid row — no new tracking required; Art 03 Beat 2 procedure addition pending (04-n44) | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Art 03 Beat 2 procedure:** Beat 2 section does not yet include district-surveillance IntelDeliverySlip delivery. Procedure addition required before Issues Resolved (04-n44). Gates Art 03 re-sign-off.
- **Art 02 component entry:** IntelDeliverySlip has no design entry in Art 02. Addition required before Issues Resolved (04-n45). Gates Art 02 re-sign-off.
- **00b IS-xx definition:** IS-xx definition covers Beat 3 delivery only. Update required to include Beat 2 delivery pattern (04-n46). Gates 00b re-sign-off.
- **Card name:** "Placement" implies permanent installation — consider rename (e.g., "Surveillance Order," "District Watch") during naming pass.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Redesigned S68 v2.0 — episodic Beat 2 model. Blocking open issues: 04-n44 (Art 03), 04-n45 (Art 02), 04-n46 (00b).*

```python
DIR.CA.3 = Card(
    id      = "DIR.CA.3", version="v2.0",
    name    = "Surveillance Placement",
    tagline = "Watch a named district — learn what has been submitted before it resolves.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Directorate,
    layer   = Information, function = Reveal, subject = CovertOperation,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any, target_faction=None, target_object=None,
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).mandate * 2,
    success     = game.deliver(IntelDeliverySlip(district=district(target), content="op_type_only", source="beat3_grid"), to=faction(acting), private=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate monitors because monitoring is their primary tool for managing what they cannot directly control.",
    perspectives = {Directorate: "We know what moves through that district before it moves. We will respond accordingly."},
    design_note  = "Redesigned S68 v2.0: original permanent passive feed with beat3_pre_resolution delivery invalidated — Governing Rule 7.2a prohibits covert board markers; ARBITER holds no log in L1. Episodic model: Directorate watches one district one month. ARBITER reads existing Beat 3 grid row at Beat 2 resolution — no new tracking. Op type only, no faction. Multiple copies in Directorate deck flagged for deck design pass (04-n42).",
    arbiter_note = "During Beat 2 resolution of this card: check the Beat 3 resolution grid for covert operations targeting district(target). For each operation present, write the operation type on an IntelDeliverySlip and deliver privately to Directorate. Do not include faction identity. If no Beat 3 operations target the district, deliver nothing — Directorate's resources are spent. Procedure pending Art 03 Beat 2 addition (04-n44).",
)
```

---

### DIR.CA.4 — TACTICAL REDIRECTION
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's repositioning card — the only card in the full set using Territory — Move — PresenceToken (Beat 2, Automatic). Designed to fill the gap identified in S51 when DIR.CA.4 Sealed Border was retired. Where most Directorate cards act on opponents, Tactical Redirection acts on Directorate's own presence, moving up to 2 tokens between adjacent districts before Beat 3 outcomes are applied. Beat 2 Automatic makes it a proactive positional adjustment — Directorate anticipates the round's contested districts and pre-positions before dice are rolled. ChorusNode exclusion (both source and destination) prevents repositioning through the central Chorus district. Mandate×2 is a mid-tier cost.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Proactive repositioning — moves up to 2 presence tokens between adjacent districts before Beat 3; fills Territory/Move/PresenceToken gap; only card in full set with this verb+subject at Beat 2 | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective by design — tactical pre-positioning as institutional doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Beat 2 Automatic — proactive, not reactive; ChorusNode exclusion; entry qualification outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — institutional pre-positioning is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Move/PresenceToken — unique taxonomy slot in full card set; Move function correct for same-faction repositioning | Art 04b §4, §5 |
| Balance | ✓ | Mandate×2, Automatic, moves count=2 — move count vs. restriction outstanding (Outstanding Issue) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: tokens moved at Beat 2 resolution; control flags recalculated post-move | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 positional wager fires on submission | — |
| Portrait validity | ✓ | Directorate +1 submitter — single entry; repositioning aligns with tactical doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | source and target both district.named; adjacency enforced in restriction; ChorusNode excluded from both | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken in restriction and as target; Mandate cost; adjacency per district_adjacency table | Art 02 §6; Art 02 §8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; tokens moved before Beat 3 resolution; entry qualification and move count resolution outstanding (Outstanding Issues) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Entry qualification check:** `arbiter_note` states that if Directorate does not qualify for entry at the destination, the card is discarded without effect (resources not refunded). Confirm "qualify for entry" criteria — is there a district-entry restriction in Art 01 or Art 03?
- **Move count vs. restriction:** Restriction requires source.presence >= 1 but the card moves count=2. Can the card be played if source has only 1 token (moving fewer than 2)? Confirm whether count=2 is a maximum or exact.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*S51 redesign — design rationale scaffold added S59. Design pass pending.*

```python
DIR.CA.4 = Card(
    id      = "DIR.CA.4",  version="v1.0",
    name    = "Tactical Redirection",
    tagline = "Reposition institutional presence ahead of a contested exchange.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Move,  subject = PresenceToken,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.adjacent(source), target_faction=faction(acting), target_object=PresenceToken,
    target_taxonomy=None,
    affinity=None,
    restriction = (
        district(source).faction(acting).presence >= 1
        AND district(source).is_adjacent(district(target))
        AND district(source) != ChorusNode
        AND district(target) != ChorusNode
    ),
    cost        = resource.faction(acting).mandate * 2,
    success     = game.move(faction(acting).presence, count=2, from_=district(source), to=district(target)),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "Institutional authority is not static. The Directorate repositions before others recognize the shift.",
    perspectives = {Directorate: "Our presence is where it needs to be. This was always the plan. The redistribution was anticipated."},
    design_note  = "Replaces DIR.CA.4 Sealed Border (retired S51). Fills Territory — Move — Presence token gap; no other card in the full set uses this verb + subject combination. Most impactful before Battlefield Strength when district control margins are tight.",
    arbiter_note = "Move named Directorate presence tokens from source to destination. Adjacency confirmed against district adjacency table. Entry requirements rechecked at destination — if Directorate does not qualify for entry, card is discarded without effect (resources not refunded). Control flags and Established markers recalculated after move.",
)
```

---

### DIR.PA.4 — REGULATORY DOWNGRADE *(stub)*
[↑ Public Acts](#directorate-public-acts)

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S131. Redesigned — resolves 04-n104 BLOCKED status (L223: original targeted InfluenceTier, a derived/non-targetable state, and violated GR 9.1). Simplified per GR 6.1 / Design Pillar 4.7b: no ARBITER calculation — removes exactly 1 named presence token. Closes 1 of 6 toward the 54-card floor (04-n149).*

```python
DIR.PA.4 = Card(
    id      = "DIR.PA.4",  card_id="DIR.PA.4",  version="v3.0",
    name    = "Regulatory Downgrade",
    tagline = "One chip, formally revoked.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer   = Territory,  function = Remove,  subject = PresenceToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.named,
    target_faction  = faction.named_opponent,
    target_object   = None,
    target_taxonomy = None,
    affinity        = None,
    restriction     = faction(target).influence_tier(district(target)) >= Established,
    cost            = resource.faction(Directorate).mandate * 2,
    boost           = None,

    success     = arbiter.remove(presence_chip, district=target_district, faction=target_faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = None,
    perspectives = None,
    design_note  = "Redesigned S131 (v2.0 → v3.0), resolves 04-n104. ARBITER performs no comparison or tier calculation — removes exactly 1 named presence token from target faction in target district; the tier consequence (if any) is a natural downstream effect of fewer tokens under the standard influence-level rules, not a direct write. Established+ restriction preserved from original (one-time boolean gate, not a recurring calculation — compliant with GR 6.1 / Design Pillar 4.7b). Locked cost principle: this base version (N=1) is mono (Mandate×2). Any future variant removing N>1 tokens must use cross-resource cost. Distinct from DIR.CA.5 Sanctioned Raid: public/Automatic/no-roll vs. covert/d100/boost-scaled.",
    arbiter_note = "Beat 4: confirm target faction holds Established+ tier in target district. Remove 1 presence token belonging to target faction from target district (target's choice of which physical chip, if multiple present).",
)
```

---

### DIR.PA.5 — ZONING FREEZE *(stub)*
[↑ Public Acts](#directorate-public-acts)

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S131. Redesigned — resolves 04-n104 BLOCKED status. Retaxonomized Territory|Block|PresenceToken (not InfluenceTier; not Submission — the subject controlled is presence-token accumulation). Permanent standing card, self-inclusive ("a new law"), reactive to any presenceChip addition. Closes 1 of 6 toward the 54-card floor (04-n149).*

```python
DIR.PA.5 = Card(
    id      = "DIR.PA.5",  card_id="DIR.PA.5",  version="v3.0",
    name    = "Zoning Freeze",
    tagline = "New settlement in this district doesn't stick. Not even ours.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer   = Territory,  function = Block,  subject = PresenceToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Permanent public act",
    outcome_type    = Unilateral,
    persistence     = Permanent,
    persistence_condition = faction(Any).pays(
        [Resource(Mandate, 1), Resource(district(target).native, 1)],
        to=Reservoir,
    ),
    persistence_effect = game.board_condition(
        scope  = district(target),
        effect = on(presence_chip.placed(district=district(target))):
                     arbiter.remove(trigger.chip, faction=trigger.faction, district=district(target), count=1),
        # Fires for ANY faction, including Directorate ("a new law" — self-inclusive, per CA.8 uniform-scrutiny doctrine).
        # Catches Upkeep Step 4 conversion chips (Converting marker -> permanent presence chip) and any CA/PA
        # success effect that adds a chip. Does NOT touch the deployment marker itself (GR 8.3a: markers are
        # moved/converted, never removed) — only the resulting presenceChip.
    ),

    target_district = district.named,
    target_faction  = None,
    target_object   = None,
    target_taxonomy = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Directorate).mandate * 2
                     + resource.district(target).native * 1
                     + resource.faction(Directorate).capital * 1,
    boost           = None,

    success     = None,  # card placement IS the effect — card-as-condition pattern
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = None,
    perspectives = None,
    design_note  = "Redesigned S131 (v2.0 → v3.0), resolves 04-n104. Retaxonomized Territory|Block|PresenceToken — sidesteps the InfluenceTier derived-state violation entirely; not Submission|Block since the thing being controlled is presence-token accumulation, not an action taxonomy. Card-as-condition, Permanent. Reactive effect uses a ModReactCard-style trigger (presence_chip.placed) inside a PublicAct's persistence_effect — a new combination of two individually-established patterns (self-policing per GR 6.1a; confirmed §6.3 trigger vocab), not new ARBITER behavior requiring a fresh Art 03 procedure. Self-inclusive: Directorate's own new chips in the district are reverted too. Deployment marker itself is never touched (GR 8.3a) — only genuine presenceChip additions trigger removal. Clearing: ANY faction (not just Directorate or the affected party) may pay 1 Mandate + 1 district-native to Reservoir — a public toll that reopens the district for everyone. Cost is cross (2 Mandate + 1 district-native + 1 Capital): district-native reflects genuine engagement with the target district's specific economy; Capital reflects the standing enforcement apparatus required to auto-revert placements indefinitely, distinct from a one-time legal filing (which would be Findings).",
    arbiter_note = "Beat 4: place card in Directorate's play area as a standing condition on target district. From this point forward: any time a presence chip is added to target district (via any CA/PA success effect, or Upkeep Step 4 deployment marker conversion), immediately remove that chip. Applies to all factions including Directorate. Deployment markers themselves are never touched — only the resulting presence chip. Card remains active until any faction pays 1 Mandate + 1 district(target).native to Reservoir, at which point remove the card and announce.",
)
```

---

### Directorate — SANCTIONED RAID
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's maximum-force territorial removal card. The Intel token is the authorization document; faction + native resource is the operational cost. Cannot bypass countermeasures — clears target faction's modifier cards at the district before removing presence tokens. Scales via boost: each additional unit of faction + native submitted at Phase B removes one more presence token and deepens the threshold (harder to relocate more people in a single op). PS scales symmetrically with n — forced relocation creates resentment proportional to scale; a clean large-scale op generates proportional public support. Distinct from DIR.CA.2 Detain (deployment marker, permanent) and STD.CA.4 Undermine (one token, standard, no Intel gate).

#### Card Story
The Directorate dispatches a team to the district — no announcement, no negotiation. The intel token is the authorization document; the operation runs exactly as filed. When the team leaves, the target faction has fewer people there than it did this morning. Whether the public calls it a cleanup or a crackdown depends entirely on how cleanly it was done.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Scaled-force removal via boost; target faction modifier card clear; PS scales with n in both directions | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — sanctioned institutional action | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Intel gate enforces intelligence-first doctrine; threshold = 65−10n; PS risk/reward scales with ambition | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Remove/PresenceToken — (1 + BM-xx) tokens removed at Beat 3 | Art 04b §4, §5 |
| Card narrative | ✓ | Intel-authorized team clears district; public verdict (PS) scales with scope and execution quality | Art 04 §5 P26 |
| Balance | ⚠ | Boost scaling adds new cost/PS curve — playtesting required | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent: (1 + BM-xx) presence tokens removed; target faction modifier cards cleared | — |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter; PS effects are game effects (not portrait) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named | Art 01 §6–§7 |
| Supported by components | ⚠ | BM-xx not yet registered — gate: 04-n81 | Art 02 §6; Art 02 §11–§12 |
| Supported by game procedure | ⚠ | Beat 0 boost detection (04-n82); Beat 2/3 BM-xx resolution (04-n83); Discovery definition (04-n84) — all gate sign-off | Art 03 §9, §11 |
| Data schema validation | ✓ | boost field present; threshold-scaling noted in §6.3; affinity corrected to None (04-n70) | Art 04 §6.1–§6.3 |

#### Outstanding Issues

- **IntelToken as restriction:** Should IntelToken(faction=faction(target)) also appear as `restriction =` (card unplayable without it in hand) in addition to appearing in cost? Or is cost placement sufficient? Carry.
- **Intel token faction-keying:** Confirm faction-keyed to target is correct (vs. any held token of the type).
- **Sign-off gates:** 04-n81 (BM-xx registration), 04-n82 (Beat 0 boost procedure), 04-n83 (Beat 2/3 BM-xx resolution), 04-n84 (Discovery mechanic definition).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*v2.2 — S79: boost model replaces Phase B n-declaration; base cost = faction×1 + native×1 + IntelToken (Mandate×2 removed); boost = same unit; threshold = 65−10×n_boost; PS scales with (1+n) in both directions; successcrit = PS+(1+n_boost) (public endorsement of clean large-scale op); fail = NotificationSlip; failcrit = Discovery + PS−(1+n_boost); modifier scope = target faction only; 04-n81/82/83/84 gate sign-off.*

```python
DIR.CA.5 = Card(
    id      = "DIR.CA.5",  version="v2.2",
    name    = "Sanctioned Raid",
    tagline = "Not every operation leaves a paper trail.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Remove,  subject = PresenceToken,
    beat=3, resolution=d100,
    threshold = 65 - (10 * n_boost),  # n_boost = BM-xx count; locked at Beat 0
    ring_mod  = {0:-15, 1:-10, 2:0, 3:+10},
    doctrine_mod = None,
    trigger   = None,
    resolution_type = "Probabilistic", outcome_type = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district = district.named, target_faction = faction(named_opponent), target_object = PresenceToken,
    target_taxonomy=None,
    affinity  = None,
    restriction = None,
    cost      = resource.faction(acting) * 1
              + resource.district(native) * 1
              + IntelToken(faction=faction(target)) * 1,
    boost     = True: resource.faction(acting) * 1 + resource.district(native) * 1,
    success   = [game.remove_modifier_cards(district(target_district), faction=faction(target)),
                 game.remove(faction(target).presence_tokens, district(target_district), count=(1 + n_boost)),
                 faction(acting).standing -= (1 + n_boost)],
    successcrit = faction(acting).standing += (1 + n_boost),
    fail      = game.dispatch(faction(target), NotificationSlip),
    failcrit  = [Discovery, faction(acting).standing -= (1 + n_boost)],
    portrait  = {Directorate: PortraitEntry(submitter=+1)},
    narrative = "The Directorate does not ask permission. It records the action and moves on.",
    perspectives = {Directorate: "The intelligence warranted the action. The action was authorised. There is nothing further to say."},
    design_note  = "Boost model: base cost (faction×1 + native×1 + IntelToken) covers removal of 1 token (threshold 65). Each boost unit = 1 BM-xx = 1 additional token removed, threshold −10. PS scales symmetrically with (1+n): success = −(1+n), successcrit = +(1+n), failcrit = Discovery + −(1+n). Modifier clear = target faction's cards only. See 04-n13: Network modifier card auto-triggers off Directorate sweep.",
    arbiter_note = "Beat 0: (1) validate base cost paid; (2) n_boost = excess payment ÷ (faction×1+native×1); (3) place n_boost BM-xx on grid slot; (4) lock threshold = 65−10×n_boost; (5) confirm faction(target) has ≥ (1+n_boost) presence tokens at district — reject if not. Beat 3 success: remove target faction's modifier cards from district; remove (1+n_boost) presence tokens from faction(target); Directorate PS −(1+n_boost); remove BM-xx to supply. Crit success: PS +(1+n_boost) instead of −(1+n_boost). Fail: dispatch NotificationSlip to target. Crit fail: Discovery (Art 03 §9.4 Step 7b.i — 04-n84 pending definition); Directorate PS −(1+n_boost).",
)
```

---

### DIR.CA.6 — INSTITUTIONAL AUDIT
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's institutional resource-generation card — fills the Economy gap left when DIR.CA.4 Tactical Redirection replaced the prior Economy vehicle. The audit targets a district where Directorate has meaningful operational footprint (chip count > 1), and counts active Directorate Permanent cards whose target district is in the same ring. Each unchallenged standing directive in the ring represents continued compliance with institutional authority; the audit converts that compliance record into Mandate. No floor: 0 active Permanents in the target ring yields 0 Mandate on success — the card is only worth submitting when Permanents are in play. Pairs with DIR.CA.7 Institutional Brief (same counting mechanism, PS yield).

#### Card Story
An internal team works through the standing record. Active directives in this ring are in force. Active restrictions are being observed. The documentation is clean. The budget allocation goes through.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional resource generation — fills Economy gap in Directorate set; yield scales with maintained standing authority in ring | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — institutional allocation as procedural validation | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; chip count > 1 restriction requires operational footprint; no floor enforces genuine Permanent investment before yield is meaningful | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — internal budget allocation is not a public declaration | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy / Add / NativeResource — Mandate generation through institutional validation | Art 04b §4 |
| Balance | ⚠ | Yield scales 0–N with active Permanents; Mandate×1 cost is low — may be generous if Permanents accumulate; playtesting required | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — Mandate added once at Beat 3 resolution | — |
| Persistence | ✓ | Immediate — no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter — institutional allocation aligns with authority doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; restriction = chip count > 1 | Art 01 §6–§7 |
| Supported by components | ✓ | Counts face-up Directorate Permanent cards in Directorate play area — no new component | Art 02 §6–§8 |
| Supported by game procedure | ✓ | ARBITER reads board state (face-up Permanents in play area, target ring match) — existing permanent card procedure | Art 03 §9 |
| Data schema validation | ✓ | Fields consistent with §6.1–§6.3 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Internal audit — standing record clean, allocation approved | Art 04 §5 P26 |

#### Outstanding Issues

- **DB registration:** New card — requires id assignment in card_ref and component_metadata.
- **game.active_permanents() scope:** Confirm counting mechanism is unambiguous in paper play — ARBITER reads face-up Directorate Permanent cards from Directorate play area where card's target_district.ring == district(target).ring.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*New card — S106. Fills Economy|Add|NativeResource gap (04b §8.2 HP).*

```python
DIR.CA.6 = Card(
    id      = "DIR.CA.6", version="v1.0",
    name    = "Institutional Audit",
    tagline = "Review the standing record. Active directives in this ring generate institutional capital.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Directorate,
    layer   = Economy, function = Add, subject = NativeResource,
    beat=3, resolution=d100, threshold=50,
    ring_mod=None, doctrine_mod=None, trigger=None,
    outcome_type=None,
    persistence=Immediate, persistence_condition=None, persistence_effect=None,
    target_district = district.named,
    target_faction=None, target_object=None, target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).presence_count(district(target)) > 1,
    cost    = resource.faction(acting).mandate * 1,
    success = resource.faction(acting).mandate.add(
                count(game.active_permanents(faction=acting,
                      ring=district(target).ring))),
    successcrit = resource.faction(acting).mandate.add(1),
    fail        = None,
    failcrit    = resource.faction(acting).mandate.remove(1),
    on_accept=None, on_decline=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate does not improvise. The allocation exists because the framework exists. The framework is intact. The allocation is approved.",
    perspectives = {Directorate: "The standing record in this ring is clean. What was ordered is being carried out. Resources are allocated accordingly."},
    design_note  = "No floor — 0 active Permanents in target ring yields 0 Mandate on success. Count: face-up Directorate Permanent cards in Directorate play area where card.target_district.ring == district(target).ring. Pairs with DIR.CA.7 (same mechanism, PS yield).",
    arbiter_note = "Beat 3: count face-up Directorate Permanent cards in Directorate play area whose target district is in the same ring as district(target). Add that count in Mandate to Directorate supply. Successcrit: +1 Mandate additional. Failcrit: remove 1 Mandate from Directorate supply.",
)
```

---

### DIR.CA.7 — INSTITUTIONAL BRIEF
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's covert Standing card — fills the Standing|Shift gap identified in Art 04b §8.2. The mechanism is grounded in the same architecture as DIR.CA.6: target a district with operational footprint, count active Permanents in that ring, yield scales accordingly. The covert operation circulates the institutional record from the target ring through closed channels — demonstrated compliance with active directives creates a public confidence signal without disclosing authorship. The public receives the signal (stability, competence, maintained order) without knowing the Directorate arranged it. This resolves the PS legitimacy question: the mechanism is covert; the outcome enters public perception through the channels the Permanents already occupy. PS yield = 0 if no Permanents active in ring — players should verify ring Permanent count before submitting.

#### Card Story
Before any version of events could circulate, the Directorate's closed channels had already carried a different one. Active directives in this ring, maintained restrictions, a clean procedural record. The population receives signals they cannot source. The public confidence reading improves.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Covert PS generation — mechanism is hidden authorship of a public signal; distinct from Network PS cards (mass broadcast vs. closed-channel institutional record) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — institutional credibility through demonstrated record, not claimed reputation | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; chip count > 1 restriction; covert type consistent with undisclosed authorship | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — mechanism is covert; effect is public | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding — upward PS shift; target = acting faction | Art 04b §4 |
| Balance | ⚠ | PS yield scales with Permanents — same risk as DIR.CA.6 if Permanents accumulate; Mandate×2 cost higher than CA.6 to reflect PS vs. resource asymmetry | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — PS marker moved once at Beat 3 resolution | — |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; restriction = chip count > 1 | Art 01 §6–§7 |
| Supported by components | ✓ | PS marker (existing); no new component | Art 02 §11–§12 |
| Supported by game procedure | ✓ | PS movement by ARBITER at Beat 3 resolution — existing procedure | Art 03 §9 |
| Data schema validation | ✓ | Fields consistent with §6.1–§6.3 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Closed-channel record circulation; public confidence signal without disclosed authorship | Art 04 §5 P26 |

#### Outstanding Issues

- **DB registration:** New card — requires id assignment.
- **Failcrit narrative:** PS−1 represents the brief being traced back to Directorate — confirm this holds as an institutional embarrassment consequence (vs. a larger penalty).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*New card — S106. Fills Standing|Shift|PublicStanding gap (04b §8.2 HP). Narrative grounding: covert mechanism, public outcome via closed-channel circulation of institutional record.*

```python
DIR.CA.7 = Card(
    id      = "DIR.CA.7", version="v1.0",
    name    = "Institutional Brief",
    tagline = "Circulate the standing record through closed channels. Demonstrated authority in this ring builds public confidence.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Directorate,
    layer   = Standing, function = Shift, subject = StandingMarker,
    beat=3, resolution=d100, threshold=50,
    ring_mod=None, doctrine_mod=None, trigger=None,
    outcome_type=None,
    persistence=Immediate, persistence_condition=None, persistence_effect=None,
    target_district = district.named,
    target_faction=None, target_object=None, target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).presence_count(district(target)) > 1,
    cost    = resource.faction(acting).mandate * 2,
    success = faction(acting).standing.add(
                count(game.active_permanents(faction=acting,
                      ring=district(target).ring))),
    successcrit = faction(acting).standing.add(1),
    fail        = None,
    failcrit    = faction(acting).standing.remove(1),
    on_accept=None, on_decline=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "The Directorate does not announce competence. It demonstrates it — quietly, through the record, through the channels that matter. The public receives the signal without knowing its source.",
    perspectives = {Directorate: "The active directives in this ring speak for themselves. We are not making a claim. We are presenting a record."},
    design_note  = "PS yield = count of active Directorate Permanents in same ring as target district. 0 Permanents → +0 PS on success. Same counting mechanism as DIR.CA.6 (Mandate yield). Failcrit PS−1: brief traced to Directorate — institutional embarrassment.",
    arbiter_note = "Beat 3: count face-up Directorate Permanent cards in Directorate play area whose target district is in the same ring as district(target). Move Directorate PS marker up by that count. Successcrit: +1 PS additional. Failcrit: move PS marker down 1.",
)
```

---

### DIR.CA.8 — ENHANCED SCRUTINY
[↑ Covert Operations](#directorate-covert-operations)

#### Design Rationale
Directorate's difficulty-suppression card — a district-wide threshold penalty applied before Beat 3 resolves. Distinct from DIR.CA.1 Invoke Jurisdiction (blocks specific card types at Beat 2) and STD.CA.10 Protect (shields acting faction's assets only): Enhanced Scrutiny raises the operational cost for everyone in the district, including Directorate. That inclusion is doctrine-consistent — the Directorate accepts its own operational friction in exchange for universal suppression; scrutiny that has exceptions means nothing. Mechanism uses existing Modifier tokens placed by ARBITER on each Beat 3 row targeting the district at Beat 2 resolution. No new component needed. Beat 2 Directorate ops in the district (DIR.CA.1, DIR.CA.3, DIR.CA.4) are unaffected — only Beat 3 ops take the −15.

#### Card Story
The district is under enhanced institutional review. Documentation requirements are elevated. Checkpoint procedures are doubled. The Directorate's own teams work under the same conditions — scrutiny means something only when it applies uniformly.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | District-wide difficulty suppression — all Beat 3 covert ops in named district take −15; distinct from DIR.CA.1 (type-specific block) and STD.CA.10 (faction-specific protect) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — uniform scrutiny as institutional doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; applies to own Beat 3 ops — restraint doctrine; Mandate×2 mid-tier cost | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Directorate) — scrutiny order is institutional, not public | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Resolution / Modify / Difficulty — threshold adjustment before Beat 3 resolution | Art 04b §4 |
| Balance | ⚠ | −15 to all Beat 3 ops in district is significant suppression at Mandate×2; self-inclusion is the cost; playtesting required | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate (within-month) — tokens placed at Beat 2, consumed at Beat 3 | — |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 Automatic | — |
| Portrait validity | ✓ | Directorate +1 submitter | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | Uses existing Modifier tokens — no new component | Art 02 §11 |
| Supported by game procedure | ✓ | ARBITER places existing Modifier tokens (−15) on each Beat 3 row targeting district at Beat 2 resolution — within existing modifier placement procedure | Art 03 §9 |
| Data schema validation | ✓ | Automatic, no threshold/ring_mod; Beat 2 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Enhanced institutional review; uniform scrutiny including own ops | Art 04 §5 P26 |

#### Outstanding Issues

- **DB registration:** New card — requires id assignment.
- **Beat 2 Automatic + Beat 3 scope:** Confirm ARBITER can identify all Beat 3 rows for the target district at Beat 2 resolution before Beat 3 ops are revealed. Resolution grid rows are placed at Beat 0 — ARBITER has grid visibility. No new tracking required.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*New card — S106. Fills Resolution|Modify|Difficulty gap (04b §8.2 MP). No new component — uses existing Modifier tokens placed per-row.*

```python
DIR.CA.8 = Card(
    id      = "DIR.CA.8", version="v1.0",
    name    = "Enhanced Scrutiny",
    tagline = "Place a district under institutional review. All Beat 3 covert operations in this district find conditions harder.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Directorate,
    layer   = Resolution, function = Modify, subject = Difficulty,
    beat=2, resolution=Automatic, threshold=None,
    ring_mod=None, doctrine_mod=None, trigger=None,
    outcome_type=None,
    persistence=Immediate, persistence_condition=None, persistence_effect=None,
    target_district = district.named,
    target_faction=None, target_object=None, target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost    = resource.faction(acting).mandate * 2,
    success = game.apply_modifier(
                ops=game.resolution_grid.beat3(district=district(target)),
                threshold_mod=-15),
    successcrit=None, fail=None, failcrit=None,
    on_accept=None, on_decline=None,
    portrait    = {Directorate: PortraitEntry(submitter=+1)},
    narrative   = "Enhanced scrutiny has been authorised for this district. All activity here is subject to review. All activity. Including ours.",
    perspectives = {Directorate: "The district is under review. Scrutiny means something only when it applies uniformly."},
    design_note  = "Applies to all factions including Directorate. Beat 2 ops in district (DIR.CA.1/CA.3/CA.4) unaffected — only Beat 3 rows. Uses existing Modifier tokens (−15) placed by ARBITER per row, not a district-column flag.",
    arbiter_note = "Beat 2 Automatic resolution: identify all rows in the resolution grid targeting district(target) at Beat 3. Place a standard Modifier token (−15 threshold) on each row. All factions, no exceptions. Tokens are in place when Beat 3 opens — apply −15 to each op's threshold before rolling.",
)
```

---


---

### Directorate — Public Acts
[↑ Directorate](#directorate)

| Card | Name |
|------|------|
| [DIR.PA.1](#p11-regulatory-override) | Regulatory Override |
| [DIR.PA.2](#p12-convene-an-inquiry) | Convene an Inquiry |
| [—](#directorate-entryexit-controls) | Entry/Exit Controls |
| [—](#directorate-standing-injunction) | Standing Injunction |
| [DIR.PA.4](#dirpa4--regulatory-downgrade-stub) | Regulatory Downgrade |
| [DIR.PA.5](#dirpa5--zoning-freeze-stub) | Zoning Freeze |
| [DIR.PA.7](#dirpa7--curfew-stub) | Curfew |
| [DIR.PA.8](#dirpa8--subpoena-stub) | Subpoena |
| [DIR.PA.9](#dirpa9--charter-grant-stub) | Charter Grant |
| [DIR.PA.10](#dirpa10--official-demonstrations-stub) | Official Demonstrations |
| [DIR.PA.11](#dirpa11--public-hearing-stub) | Public Hearing |

### DIR.PA.1 — REGULATORY OVERRIDE
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's district-level regulatory control PA. All non-Directorate presence-placement actions (cards that Add PresenceTokens) in the named district cost +1 native for the remainder of the Quarter. Persistence = Seasonal: the PA card (or RegulatoryOverrideMarker) stays on the table as an active condition marker until Phase 21 or Directorate goes Absent from the district. This is the structural counter to Guild's build pace — raising the cost of the presence prerequisite that enables STD.PA.3/GUI.PA.1. Restriction: Directorate must have Established in the district to invoke jurisdictional authority.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Directorate regulatory authority over district operations is core to their institutional doctrine | Art 00 §7 |
| Voice fit | ✓ | Directorate on-doctrine; Ghost (aligned): observe who stops crossing; Network (opposed): regulation as toll | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Directorate institutional regulatory authority: Mandate × 2 cost, Established restriction (jurisdictional legitimacy), PS +1. Shapes all other factions' territorial economics in the district. Directly serves Directorate control doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Modify / PresenceToken — modifies the cost of PresenceToken placement actions | Art 04b §4 |
| Balance | ⚠ | Seasonal scope at 2 Mandate is strong — affects all remaining Months of Quarter. Single district only. Balance subject to playtesting | Art 02 §6–§7 |
| Effect duration | ✓ | World condition is Seasonal (within-Quarter, cleared at Phase 21 or Directorate Absent). No multi-Quarter duration. Consistent with Art 04 §5 P19 | Art 04 §5 P19 |
| Persistence | ✓ | Seasonal — DIR.PA.1 card / RegulatoryOverrideMarker stays on district until Phase 21 or Directorate Absent | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid; restriction checks Directorate's influence tier in the district (valid zone condition) | Art 01 §6–§7 |
| Supported by components | ⚠ | RegulatoryOverrideMarker is a new component — register in Art 02 before production | Art 02; Art 03 §9.4 |
| Supported by game procedure | ⚠ | World condition application to PresenceToken.Add actions needs ARBITER tracking protocol. RegulatoryOverrideMarker component registration required | Art 03 §9.4; Art 02 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
DIR.PA.1 = Card(
    id      = "DIR.PA.1",  version="v1.0",
    name    = "Regulatory Override",
    tagline = "Declare a district under Directorate oversight, raising the cost of all non-Directorate presence operations.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer    = Territory,  function = Modify,  subject = PresenceToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Seasonal,  # DIR.PA.1 card / RegulatoryOverrideMarker stays on district until Phase 21
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.all_except(Directorate),
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Directorate).influence_tier(target_district) >= Established,
    cost        = resource.faction(Directorate).mandate * 2,

    success = (
        arbiter.place(RegulatoryOverrideMarker, district(target)),
        game.world_condition(
            scope    = district(target),
            effect   = presence_placement_action(faction=faction.all_except(Directorate)).cost += 1,
            duration = Seasonal,
            clear_on = (
                faction(Directorate).influence_tier(target_district) == Absent
                or game.phase == EndOfQuarter
            ),
        ),
        faction(Directorate).standing += 1,
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Directorate: PortraitEntry(submitter=+1)},

    narrative    = "The Directorate does not need to block what it can simply make more expensive.",
    perspectives = {
        Directorate: "Regulatory oversight is the institutional mechanism for managed stability. The cost increase is the signal, not the sanction.",
        Ghost:       "The Directorate taxes the district. We do not need to control the threshold. We only need to observe who stops trying to cross it.",  # aligned
        Network:     "One Mandate and the Directorate makes every other faction pay to exist in the district. They call it regulation. We call it a toll.",  # opposed
    },
    design_note  = "District-level regulatory PA. +1 native cost on all non-Directorate PresenceToken.Add actions in district for remainder of Quarter (Seasonal). Physical marker on district; card stays on table as marker. Counter to Guild STD.PA.3/GUI.PA.1 build chain — raises cost of presence prerequisite. Restriction: Directorate Established+ in district. Multiple P11s may target different districts. Balance review pending playtesting Cost reasoning: Exposure is necessary to enforce the controls publicly, making the restrictions visible across the district.",
    arbiter_note = "Beat 4: place RegulatoryOverrideMarker on declared district. DIR.PA.1 card stays on table as marker. Apply +1 native cost to all non-Directorate presence-placement actions (STD.CA.3 Campaign, STD.PA.1 Open Operations, STD.CA.8 Buy Influence, GUI.PA.1 Civic Works Mandate) targeting this district for remaining Months of Quarter. Directorate PS +1. Clear: Directorate Absent in district (remove immediately) OR Phase 21 cleanup. Multiple markers on different districts tracked independently.",
)
```

---

### DIR.PA.2 — CONVENE AN INQUIRY
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's institutional intelligence-gathering PA. No formal restriction — Directorate can always commission an inquiry. The yield (Intel tokens) is determined by ARBITER's count of publicly attributed covert actions against the target faction in the last 2 months (from resolved STD.PA.4/STD.PA.5 outcomes this Quarter). Zero yield if no prior attribution groundwork was laid — 3 Mandate wasted. This creates a two-step sequence incentive: STD.PA.4/STD.PA.5 → DIR.PA.2. Distinct from Ghost's STD.CA.5 (Gather): Directorate uses ARBITER as the collection mechanism rather than operational fieldwork.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional investigation via ARBITER is Directorate's mode of intelligence — not covert fieldwork | Art 00 §7 |
| Voice fit | ✓ | Directorate on-doctrine; Guild (aligned): institutional process produces verifiable record; Syndicate (opposed): operating margin is what the record cannot reach | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Directorate commissions ARBITER investigation (not covert fieldwork): 3 Mandate, yield contingent on prior STD.PA.4/STD.PA.5 groundwork. Creates two-step sequence incentive (STD.PA.4/STD.PA.5 → DIR.PA.2). Portrait +1: submitter-bounded | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Add / IntelToken | Art 04b §4 |
| Balance | ✓ | 3 Mandate cost is high. Yield 0–2 tokens depending on prior STD.PA.4/STD.PA.5 outcomes. Expensive gamble without groundwork; reliable payoff when chain is set up | Art 02 §6–§7 |
| Effect duration | ✓ | IntelToken delivery and PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no zone reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (yielded by ARBITER from supply, Art 02 §6); Mandate × 3 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | ARBITER tracks STD.PA.4/STD.PA.5 resolution outcomes; yields based on that record | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
DIR.PA.2 = Card(
    id      = "DIR.PA.2",  version="v1.0",
    name    = "Convene an Inquiry",
    tagline = "Commission an ARBITER-mediated institutional investigation into a faction's recent operations.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer    = Information,  function = Add,  subject = IntelToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,  # no public restriction; yield is variable (0–2) based on ARBITER's record
    cost        = resource.faction(Directorate).mandate * 3,

    success = (
        arbiter.provide_intel_tokens(
            target    = target_faction,
            count     = arbiter.count_attributed_actions(target_faction, months=2),  # 0–2; 0 if no prior STD.PA.4/STD.PA.5
            recipient = Directorate,
        ),
        faction(target).standing    -= 1,
        faction(Directorate).standing += 1,
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Directorate: PortraitEntry(submitter=+1)},

    narrative    = "The Directorate does not gather intelligence in the traditional sense. It commissions review.",
    perspectives = {
        Directorate: "We invoke the institutional mechanism for accountability. Whether it yields anything depends on what the target has done publicly.",
        Guild:       "Directorate uses ARBITER to formalize what was publicly attributed. The investigation costs Mandate but produces something the record can verify. Guild respects the process.",  # aligned
        Syndicate:   "Directorate asks ARBITER to count what was already on the record. What was not on the record, ARBITER cannot count. That distinction is our operating margin.",  # opposed
    },
    design_note  = "Directorate intelligence PA via institutional channel. No restriction — always available. Yield: 1 Intel token per publicly attributed covert action against target faction in last 2 months (from successful STD.PA.4 or STD.PA.5 this Quarter). 0 tokens = 3 Mandate wasted (costly gamble without prior groundwork). Distinct from Ghost STD.CA.5 Gather (covert fieldwork). Creates two-step sequence incentive: STD.PA.4/STD.PA.5 → DIR.PA.2 Cost reasoning: Findings provide the legal precedent and evidence required to sustain the injunction long-term.",
    arbiter_note = "Beat 4. Count: how many successful STD.PA.4 or STD.PA.5 resolutions named this target faction this Quarter? Provide Directorate with that many Fresh Intel tokens (max 2). Apply PS: target −1, Directorate +1. If count = 0: no tokens delivered. 3 Mandate spent regardless.",
)
```

---

### Directorate — ENTRY/EXIT CONTROLS
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's persistent territorial control tool — a district-level board condition that displaces non-Directorate deployment markers immediately and blocks future placement in the named district. Distinct from Invoke Jurisdiction (DIR.CA.1), which blocks specific card types in a single district for one Beat: Entry/Exit Controls operates on deployment marker movement, persists across rounds and Quarters, and is self-policing via persistence_condition (auto-discards if Directorate loses Established status). PS −1 at resolution reflects the public backlash of establishing hard movement restrictions. Removal requires a counter-action — new card type TBD (PM05).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | District-level movement control — displaces markers immediately; blocks future placement; distinct from DIR.CA.1 (card-type block) and DIR.CA.4 (repositioning) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Directorate perspective — regulatory authority as territorial infrastructure | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate only; Mandate×3 for permanent district lock; Established restriction (jurisdictional legitimacy requires institutional presence) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) — district-level movement authority is Directorate-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Block/DeploymentMarker — hard block on placement is the function | Art 04b §4, §5 |
| Balance | ✓ | Mandate×3, permanent district lock, PS −1 — cost TBD playtesting | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent — persists until counter-acted or persistence_condition fails | — |
| Persistence | ✓ | Permanent; persistence_condition auto-discards on Directorate falling below Established in named district | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction requires Directorate Established in named district | — |
| Portrait validity | ✓ | Directorate submitter=+1; PS −1 in success field is a game effect, not portrait | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — standard targeting | Art 01 §6–§7 |
| Supported by components | ✓ | Operates on deployment markers (existing component); no new component required | Art 02 §6–§8 |
| Supported by game procedure | ⚠ | Beat 4 PA resolution defined; persistence_condition monitoring trigger not yet in Art 03 (PM05 04-n29 — blocks Issues Resolved) | Art 03 §9 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Counter-card removal:** Card sits in Directorate's PA area as a permanent board condition. Removal by counter-action requires new card type(s) — design TBD. See PM05 04-n29.
- **Art 03 persistence monitoring:** ARBITER needs a defined trigger point to check persistence_condition of all permanent PA cards (e.g., after any influence tier change). See PM05 04-n29. Blocks Issues Resolved.
- **Displaced faction with no presence elsewhere:** `move_to=district.where(faction.has_presence)` has no valid destination if the displaced faction holds no presence outside the named district. Fallback rule needed — e.g., marker is returned to hand (faction skips next placement) or moved to Baryo as unconditional fallback (Governing Rule 8.3b: no elimination).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Redesigned S66 — v1.0 (ring-scope) retired*

```python
EntryExitControls = Card(
    id      = "DIR.PA.3",  version="v2.0",
    name    = "Entry/Exit Controls",
    tagline = "Designate a district as a controlled zone — displacing non-Directorate deployment markers and blocking future placement.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Block,  subject = DeploymentMarker,
    beat=4,  resolution=Automatic,  threshold=None,  ring_mod=None,
    trigger=None,
    resolution_type="Transactional",  outcome_type=Unilateral,
    persistence           = Permanent,
    persistence_condition = faction(acting).influence_tier(district.named) >= Established,
    persistence_effect    = placement(faction.all_except(Directorate), district=district.named, type=DeploymentMarker).blocked,
    target_district = district.named,
    target_faction  = faction.all_except(Directorate),
    target_object   = None,
    target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).influence_tier(district.named) >= Established,
    cost = resource.faction(acting).mandate * 2 + resource.faction(acting).capacity * 1,
    success = (
        for_each(
            deployment_marker(faction=faction.all_except(Directorate), district=district.named),
            arbiter.instruct(marker.owner, move_to=district.where(faction.has_presence), flip_to=Blocked),
        ),
        faction(acting).standing -= 1,
    ),
    successcrit=None,  fail=None,  failcrit=None,
    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    narrative    = "Movement within the designated zone is now subject to Directorate authorization. Non-compliant presence has been relocated.",
    perspectives = {
        Directorate: "The district is designated. Who enters does so with our permission — or not at all.",
    },
    design_note  = "Persistent PA. Card sits in Directorate's active PA area on the Overview (not on district tile). Immediate: non-Directorate deployment markers in named district displaced to any district where owning faction has presence, flipped to Blocked. Persistent: non-Directorate deployment marker placement blocked in named district. persistence_condition auto-discards card if Directorate falls below Established. PS −1 at resolution (public backlash). Counter-card removal TBD — see PM05 04-n29.",
    arbiter_note = "Name the district. Each non-Directorate deployment marker there: owning faction moves it to any district where they have presence, flip to Blocked.",
)
```

---

### DIRECTORATE — STANDING INJUNCTION
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's pre-emptive PA block — distinct from DIR.PA.1 Regulatory Override (which raises presence-placement cost) and DIR.CA.1 Invoke Jurisdiction (which blocks a specific card type for one Beat in one district). Standing Injunction blocks any PA of a named taxonomy (Layer/Function) from a named faction until triggered or until the quarter ends. Permanent persistence with a dual clearing condition: trigger (target submits blocked PA at Phase B) or quarter end (Phase 21). The partial Mandate refund on Phase 21 expiry provides a safety valve against pure deterrent plays that are never triggered. PS +1 at placement reflects the public legitimacy signal of filing the injunction. No operational footprint restriction — 3 Mandate is the gate. Accords excluded: bilateral acts cannot be unilaterally blocked. Card-as-condition: the card placed in the Directorate play area IS the condition; no marker component needed. Enforcement per Governing Rule 6.1a: Directorate monitors Phase B declarations, calls the trigger, ARBITER adjudicates.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pre-emptive institutional block on a named PA taxonomy is Directorate doctrine — controlling the space of permissible action rather than reacting after the fact | Art 00 §7 |
| Voice fit | ✓ | Directorate on-doctrine; Ghost (aligned) recognizes structural pre-emption as correct; Network (opposed) names it as information control | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Directorate exclusive: Mandate×3, PS +1. Pre-emptive control over PA space is core Directorate doctrine. No operational footprint restriction — cost is the gate | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) — institutional act is public; consistent with Regulatory Downgrade/Freeze pattern | Art 04 §6.2 |
| Taxonomy fit | ✓ | Submission/Block/PublicAct — blocks a PA taxonomy from entering the resolution queue | Art 04b §4 |
| Balance | ⚠ | 3 Mandate for a Seasonal taxonomy block. Partial refund (1 Mandate) on Phase 21 expiry reduces deadweight loss. Balance review pending playtesting | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent — dual clearing condition: trigger (target submits blocked PA) or quarter end (Phase 21) | Art 04 §5 P19 |
| Persistence | ✓ | Permanent public act; card on board IS the condition; self-policing per Governing Rule 6.1a | Art 04 §6; Governing Rule 6.1a |
| Trigger validity | ✓ | No beat-timing trigger; reactive condition (target declares blocked taxonomy at Phase B) documented in design_note | — |
| Portrait validity | ✓ | Directorate +1 submitter-bounded; placing a public institutional block is maximum doctrinal expression | Art 04 §6.2 |
| Supported by zones | ✓ | No district target — faction-targeted; no operational footprint restriction | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — card on Overview is the persistent condition | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Phase B void: Dispatch Token returned, target −1 PS, card removed. No resources committed at Phase B (payment is Beat 4 Step 1) — nothing to refund. PAs declared before Injunction resolved (Beat 4) are committed board states; Governing Rule 7.2b governs, no retroactive block applies | Art 03 §9; Governing Rule 7.2b; Governing Rule 7.3 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

None.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Redesigned S67 — v2.0. PublicAct → PublicAct. InjunctionMarker removed; card-as-condition pattern. Seasonal → Permanent with dual clearing condition (trigger OR Phase 21). Dispatch Token consumed on trigger per Governing Rule 7.3. target_taxonomy field introduced (§6.1/§6.2). Self-policing per Governing Rule 6.1a.*

```python
P_StandingInjunction = Card(
    id      = "DIR.PA.6",  version = "v2.0",
    name    = "Standing Injunction",
    tagline = "Declare a public restriction on a named faction's next act of a specified type. If triggered, the act is voided.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer    = Submission,  function = Block,  subject = PublicAct,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Permanent public act",
    outcome_type    = Unilateral,
    persistence     = Permanent,
    persistence_condition = (
        faction(target).submits(PA(taxonomy=target_taxonomy)) OR
        quarter.phase == 21
    ),
    persistence_effect = PA(taxonomy=target_taxonomy, submitter=faction(target)).blocked_at(phase_b),

    target_district  = None,
    target_faction   = faction.named_opponent,
    target_object    = None,
    target_taxonomy  = taxonomy.declared,  # Layer/Function declared at Phase B; BilateralAgreement excluded

    affinity    = None,
    restriction = None,
    cost        = resource.faction(Directorate).mandate * 1 + resource.faction(Directorate).capital * 1 + resource.faction(Directorate).findings * 1,

    success     = faction(Directorate).standing += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Directorate: PortraitEntry(submitter=+1)},

    narrative    = "The Injunction does not prevent the act. It establishes that the act will carry costs the target has not yet calculated.",
    perspectives = {
        Directorate: "The Injunction does not prevent the act. It relocates its costs.",
        Ghost:       "Directorate pre-empts the declaration rather than reacting to it. We recognize this as the structurally correct approach.",
        Network:     "A pre-emptive block on a public act is the Directorate deciding which information enters the record. We have a word for that.",
    },

    design_note = "Card placed in Directorate play area (public, face-up; target faction and target_taxonomy declared at Phase B). Card IS the persistent condition. Enforcement per Governing Rule 6.1a: Directorate monitors Phase B — when target submits a PA matching target_taxonomy, Directorate calls it; ARBITER voids the PA (target −1 PS, Dispatch Token consumed per Governing Rule 7.3, card removed). PA resources not yet committed at Phase B (payment is Beat 4 Step 1) — nothing to refund. PAs declared before Injunction resolved at Beat 4 are unaffected — committed board state per Governing Rule 7.2b. Quarter-end expiry: if untriggered at Phase 21, Directorate removes card and recovers 1 Mandate. target_taxonomy may not be BilateralAgreement — Accords are bilateral and cannot be unilaterally blocked. Distinct from DIR.PA.1 (cost increase on presence placement) and DIR.CA.1 (single-Beat block in one district).",
)
```

---


---


---

---

### DIR.PA.7 — CURFEW *(stub)*
[↑ Public Acts](#directorate-public-acts)

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

```python
DIR.PA.7 = Card(
    id      = "DIR.PA.7",  version = "v1.1",
    name    = "Curfew",
    tagline = "Lock down a district to freeze physical movement.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Block,  subject = DeploymentMarker,
    beat    = 4,  resolution = Automatic,  persistence = Transient,
    cost    = resource.faction(Directorate).mandate * 2,
    success = "Places a Standing Condition on target_district until the end of Quarter+1: Deployment Markers cannot be moved into this district.",
    design_note = "A massive territorial denial tool. Blocks physical movement (which is public and enforceable) rather than targeting blind covert space."
)
```

---

### DIR.PA.8 — SUBPOENA *(stub)*
[↑ Public Acts](#directorate-public-acts)

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

```python
DIR.PA.8 = Card(
    id      = "DIR.PA.8",  version = "v1.2",
    name    = "Subpoena",
    tagline = "Weaponize target-keyed intelligence into a public audit that bleeds an opponent's finances or reputation.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Economy,  function = Remove,  subject = Capital,
    beat    = 4,  resolution = d100,  threshold = 40,
    cost    = resource.faction(Directorate).mandate * 1 + intel_token(faction=target_faction) * 1,
    success = "Target faction must pay 2 Capital or 2 of their Native Resource to the supply. If they do not, they lose 2 Public Standing.",
    design_note = "Cost uses a faction-keyed Intel Token: Directorate 'found out something' that justifies the legal action. The target has the choice to pay the fine or take the PR hit."
)
```

---

### DIR.PA.9 — CHARTER GRANT *(stub)*
[↑ Public Acts](#directorate-public-acts)

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S131. Directorate's first Territory|Add|PresenceToken card — closes the audit-flagged win-path gap (04-n89: "the faction whose win condition is territorial Established status has zero native presence-placement cards"). Closes 1 of 6 toward the 54-card floor (04-n149). Ring-spread mechanic, not single-district stacking — confirmed against Directorate's actual win path (Established in more districts, not Dominant) and the 6-chip-per-district cap. N capped at 2 (max same-ring neighbors per district).*

```python
DIR.PA.9 = Card(
    id      = "DIR.PA.9",  card_id="DIR.PA.9",  version="v0.1",
    name    = "Charter Grant",
    tagline = "Institutional authority doesn't concentrate. It radiates.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer   = Territory,  function = Add,  subject = PresenceToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.named,
    target_faction  = None,
    target_object   = None,
    target_taxonomy = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Directorate).mandate * 2,
    boost           = None,

    success = (
        arbiter.place(presence_chip, district=target_district, faction=Directorate, count=1, cap_check=True),
        for_each(
            district.adjacent(target_district).where(ring == ring(target_district)),  # same-ring neighbors only; max 2 per district
            limit=min(2, count(game.active_permanents(faction=Directorate, ring=ring(target_district)))),
            arbiter.place(presence_chip, district=neighbor, faction=Directorate, count=1, cap_check=True),
        ),
        # cap_check=True: skip any individual district placement if that district is already at 6 chips (GR 8.1) — does not void the rest of the card
    ),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = None,
    perspectives = None,
    design_note  = "First DIR Territory|Add|PresenceToken card — closes 04-n89's headline gap. Places 1 token in target district + 1 token in each same-ring-adjacent district, up to N = min(2, active Directorate Permanents in that ring) — same counting mechanism as CA.6 Institutional Audit / CA.7 Institutional Brief, reinforcing Directorate's compounding-authority engine. Ring-spread (not single-district stack) is deliberate: Directorate's win path is Established (2+, second place) in more districts than any other faction, not Dominant — breadth beats depth. N naturally caps at 2 (max same-ring neighbors per district, confirmed against board geometry), so ceiling is modest: at most 3 districts touched, 1 token each. Each placement independently respects the 6-chip-per-district cap (GR 8.1) — a capped destination is skipped, not a card-voiding failure. Early game (0 Permanents) = ordinary single-district placement, same as Standard; late game = Directorate's strongest expansion tool, consistent with the audit's 'compounds over 2-3 Quarters' finding.",
    arbiter_note = None,
)
```

---

### DIR.PA.10 — OFFICIAL DEMONSTRATIONS *(stub)*
[↑ Public Acts](#directorate-public-acts)

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S131. Public Standing counterpart to covert DIR.CA.7 Institutional Brief — closes the audit's Standing gap (04-n108: Directorate's only PS card was covert, backwards for an 'on the record' faction). Closes 2 of remaining 4 toward the 54-card floor (04-n149). A genuine gamble, not a guaranteed accumulator: government presence reads publicly as either safety or oppression, so the swing (not just the odds) scales with the size of the claim — this also self-balances the 'yield scaling at scale' concern flagged at 04-n116 for CA.6/CA.7, since the downside grows with N too.*

```python
DIR.PA.10 = Card(
    id      = "DIR.PA.10",  card_id="DIR.PA.10",  version="v0.1",
    name    = "Official Demonstrations",
    tagline = "The city gets to decide whether this looks like order or overreach.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer   = Standing,  function = Shift,  subject = StandingMarker,

    beat            = 4,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    target_taxonomy = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Directorate).mandate * 2,
    boost           = None,

    success     = faction(Directorate).standing.add(
                      count(district.where(faction(Directorate).influence_tier >= Established))),  # N = Established+ district count, city-wide
    successcrit = faction(Directorate).standing.add(1),
    fail        = faction(Directorate).standing.remove(
                      count(district.where(faction(Directorate).influence_tier >= Established))),
    failcrit     = faction(Directorate).standing.remove(
                      count(district.where(faction(Directorate).influence_tier >= Established)) + 1),
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = None,
    perspectives = None,
    design_note  = "Public counterpart to DIR.CA.7 Institutional Brief (covert, Permanent-count-scaled, ring-scoped). Distinct scaling basis to avoid duplication: N = count of districts city-wide where Directorate holds Established+ tier — a simple tally of physical Established markers already on the board (same counting mechanism CA.6/CA.7 use for Permanents; no ARBITER judgment call, GR 6.1/4.7b-safe). Flat threshold=50 (matches CA.2/CA.6/CA.7 precedent) — the gamble is in the outcome, not compounded difficulty. Success and fail both scale with N (not the usual 'fail = no effect') — a bigger public show of institutional reach is a bigger bet in both directions: it can read as reassuring stability or as authoritarian overreach. Failcrit's N+1 penalty represents the claim spectacularly backfiring. Cost kept cheap and mono (Mandate x2) — the filing itself is trivial; the risk lives entirely in the public's reaction, not the resource spend.",
    arbiter_note = "Beat 4: count districts where Directorate currently holds Established+ tier (visible via Established/Dominant markers already on board) = N. Roll d100 vs threshold 50. Success: Directorate PS += N. Successcrit: PS += N+1. Fail: Directorate PS -= N. Failcrit: PS -= N+1.",
)
```

---

### DIR.PA.11 — PUBLIC HEARING *(stub)*
[↑ Public Acts](#directorate-public-acts)

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S131. Resolves 04-n142 (S127) — the long-standing counter-card design gap for Permanent PAs, originally named for Entry/Exit Controls. Establishes a standing, game-wide due-process institution: any faction may petition to remove any of Directorate's own currently-active standing Public Acts by matching its printed cost + 1 Intel Token. Atomic resolution (pay + prove, immediate removal) — no untracked exemption state, unlike an earlier draft of the cooperative-PA concept this replaced. Closes the last 1 of 6 toward the 54-card floor (04-n149) — Directorate now at exactly 54.*

```python
DIR.PA.11 = Card(
    id      = "DIR.PA.11",  card_id="DIR.PA.11",  version="v0.1",
    name    = "Public Hearing",
    tagline = "Even our own regulations answer to due process — if you can make the case.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer   = Submission,  function = Remove,  subject = PublicAct,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Permanent public act",
    outcome_type    = Unilateral,
    persistence     = Permanent,
    persistence_condition = None,  # standing institution, once established — no clearing condition; not tied to a single district or faction
    persistence_effect = game.board_condition(
        scope  = game.all_districts,
        effect = "Any faction may petition to remove any currently active Directorate-owned standing Public Act "
                 "(Regulatory Override, Zoning Freeze, Entry/Exit Controls, Standing Injunction, or any future "
                 "Directorate standing PA) by paying Directorate an amount matching that PA's own printed cost, "
                 "plus 1 Intel Token (Fresh or Stale). On payment: the targeted PA is removed immediately.",
    ),

    target_district = None,
    target_faction  = None,
    target_object   = None,
    target_taxonomy = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Directorate).mandate * 2,
    boost           = None,

    success     = faction(Directorate).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = None,
    perspectives = None,
    design_note  = "Resolves 04-n142 (S127) — the long-standing open counter-card design gap for Permanent PAs, originally named specifically for Entry/Exit Controls but generalized here to all Directorate standing PAs. Doctrinal extension of CA.8 Enhanced Scrutiny's self-inclusive principle ('scrutiny means something only when it applies uniformly') from 'Directorate submits to its own suppression' to 'Directorate's regulations answer to due process.' Atomic resolution (pay + prove, immediate removal) — nothing is tracked or remembered across time, avoiding the untracked per-faction exemption-state problem an earlier draft of this card (a Guild-specific construction-permit concept) ran into. Cost-match is a simple physical lookup (read the target PA's own printed cost directly off that card), not an ARBITER calculation — GR 6.1 / Design Pillar 4.7b-safe. Directorate profits from every invocation (full cost refund + an Intel token) regardless of which PA is targeted or by whom — a genuine income mechanism, not a giveaway; nothing prevents Directorate from re-declaring the same regulation later at its own cost. Scoped to Directorate's own standing PAs only, not any faction's — matches 04-n142's original named case and avoids becoming an unscoped general-purpose Permanent-PA-removal tool that would need its own balance pass.",
    arbiter_note = "Beat 4: Directorate plays this card once — establishes the standing due-process institution (no target district; applies game-wide, for the rest of the session). From this point forward: any faction may, at any time, name one currently active Directorate-owned standing Public Act and pay Directorate an amount matching that PA's own printed cost, plus 1 Intel Token (Fresh or Stale), to have it immediately removed. Verify the payment matches the target PA's printed cost and that the Intel Token is not Expired, then remove the targeted PA and announce.",
)
```

---

### DIR.MOD.1 — RIOT SQUAD *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |
| Trigger frequency (ModReactCard) | ⚠ |  |  |
| Firing window (ModReactCard) | ⚠ |  |  |
| Automatic vs. d100 (ModReactCard) | ⚠ |  |  |
| Stack behavior (ModReactCard) | ⚠ |  |  |
| Ring constraint (ModReactCard) | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S128. First Directorate React. Military-mode enforcement — institutional authority to reverse unauthorized presence placement. Generic variant (faction=Any). Faction-targeted variant: DIR.MOD.2 (Syndicate). Ring-constrained variant: DIR.MOD.3 (Ring 1 Core).*

```python
DIR.MOD.1 = Card(
    id      = "DIR.MOD.1",  card_id="DIR.MOD.1",  version="v0.1",
    name    = "Riot Squad",
    tagline = "Presence placed without Directorate approval can be removed with Directorate authority.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = presence_chip.placed(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Directorate).influence >= Established,  # jurisdictional authority requires Established presence
    cost            = None,  # card consumed; cost TBD (possibly 1 Mandate)

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=trigger.faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Military-mode enforcement React. Fires when any faction places presence in a district where Directorate has Established presence. Directorate may remove 1 chip immediately. Restriction: Directorate must be Established — jurisdictional authority is earned by presence, not proclaimed. This is the suppression toolkit delivered at React speed: Directorate responds to expansion before Beat 3 resolves. Cost TBD — possibly 1 Mandate (enforcement has institutional overhead).",
    arbiter_note = None,
)
```

---

### DIR.MOD.2 — CAPITAL SUPPRESSION *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |
| Trigger frequency (ModReactCard) | ⚠ |  |  |
| Firing window (ModReactCard) | ⚠ |  |  |
| Automatic vs. d100 (ModReactCard) | ⚠ |  |  |
| Stack behavior (ModReactCard) | ⚠ |  |  |
| Ring constraint (ModReactCard) | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S128. Faction-targeted variant of DIR.MOD.1. Trigger narrowed to Syndicate presence placement. Syndicate's capital-driven territorial expansion is Directorate's primary doctrinal adversary in Ring 1/2.*

```python
DIR.MOD.2 = Card(
    id      = "DIR.MOD.2",  card_id="DIR.MOD.2",  version="v0.1",
    name    = "Capital Suppression",
    tagline = "Syndicate presence in regulated territory draws immediate institutional response.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = presence_chip.placed(faction=Syndicate),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = Syndicate,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Directorate).influence >= Established,
    cost            = None,

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=Syndicate, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1), Syndicate: PortraitEntry(flat=-1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Syndicate-targeted variant of DIR.MOD.1. Directorate's doctrine makes no distinction between rogue capital and rogue information — Syndicate's gray-market acquisitions are the same institutional threat as Network's broadcasts. Syndicate portrait flat=-1 on fire: the Syndicate's response to having presence removed is public and traceable. Narrower trigger window than generic; reliable in SYN-heavy games.",
    arbiter_note = None,
)
```

---

### DIR.MOD.3 — CITY COUNCIL LOYALIST *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |
| Trigger frequency (ModReactCard) | ⚠ |  |  |
| Firing window (ModReactCard) | ⚠ |  |  |
| Automatic vs. d100 (ModReactCard) | ⚠ |  |  |
| Stack behavior (ModReactCard) | ⚠ |  |  |
| Ring constraint (ModReactCard) | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S128. Ring-constrained variant of DIR.MOD.1. Ring 1 (Core) only. No Established restriction — Directorate has blanket institutional authority in Core ring regardless of presence level.*

```python
DIR.MOD.3 = Card(
    id      = "DIR.MOD.3",  card_id="DIR.MOD.3",  version="v0.1",
    name    = "City Council Loyalist",
    tagline = "In the Core, the Directorate's authority does not require a justification.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = presence_chip.placed(faction=Any, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,  # Core ring: no Established requirement — blanket institutional authority
    cost            = None,

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=trigger.faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Ring 1–constrained variant of DIR.MOD.1. Core ring is institutional home territory — Directorate removes presence without needing Established status. Reflects doctrine: Directorate's authority in the Core is structural, not earned faction by faction. Strongest DIR enforcement React — no restriction to work around.",
    arbiter_note = None,
)
```

---

### DIR.MOD.4 — ADMINISTRATIVE OVERHEAD *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |
| Trigger frequency (ModReactCard) | ⚠ |  |  |
| Firing window (ModReactCard) | ⚠ |  |  |
| Automatic vs. d100 (ModReactCard) | ⚠ |  |  |
| Stack behavior (ModReactCard) | ⚠ |  |  |
| Ring constraint (ModReactCard) | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S128. Legislative-mode React. Directorate documents all new Accords — procedural overhead yields Mandate income.*

```python
DIR.MOD.4 = Card(
    id      = "DIR.MOD.4",  card_id="DIR.MOD.4",  version="v0.1",
    name    = "Administrative Overhead",
    tagline = "Every Accord formed is a Directorate administrative event.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = accord.placed,
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(Directorate).resources.add(1, Mandate),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Legislative-mode React on accord.placed. Directorate charges institutional overhead for registering diplomatic agreements — Mandate income regardless of which factions are party to the Accord.",
    arbiter_note = None,
)
```

---

### DIR.MOD.5 — EMERGENCY APPROPRIATION *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |
| Trigger frequency (ModReactCard) | ⚠ |  |  |
| Firing window (ModReactCard) | ⚠ |  |  |
| Automatic vs. d100 (ModReactCard) | ⚠ |  |  |
| Stack behavior (ModReactCard) | ⚠ |  |  |
| Ring constraint (ModReactCard) | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*React to subsidize the heavy Mandate cost of Permanent PAs.*

```python
DIR.MOD.5 = Card(
    id      = "DIR.MOD.5",  card_id="DIR.MOD.5",  version="v0.1",
    name    = "Emergency Appropriation",
    tagline = "Institutional scale requires institutional funding.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = public_act.placed_on_frg(faction=Directorate, persistence=Permanent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = faction(Directorate).resources.add(2, Mandate),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Economy fixer. Triggers when Directorate places a Permanent Public Act on their Faction Resolution Grid at Phase 9.2 (before resolution). Instantly yields 2 Mandate, subsidizing the crippling Q1/Q2 cost of laying down their win-condition standing condition PAs.",
    arbiter_note = None,
)
```

---

### DIR.MOD.6 — STATE OF EMERGENCY *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |
| Trigger frequency (ModReactCard) | ⚠ |  |  |
| Firing window (ModReactCard) | ⚠ |  |  |
| Automatic vs. d100 (ModReactCard) | ⚠ |  |  |
| Stack behavior (ModReactCard) | ⚠ |  |  |
| Ring constraint (ModReactCard) | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*Creates a standing global difficulty constraint triggered by a World Event. ⚠ `world_event.played` trigger depends on undesigned Broadcast Card taxonomy — see XA-54.*

```python
DIR.MOD.6 = Card(
    id      = "DIR.MOD.6",  card_id="DIR.MOD.6",  version="v0.1",
    name    = "State of Emergency",
    tagline = "The world changes. The Directorate dictates how.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = world_event.played,
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    persistence     = Seasonal,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Directorate).mandate * 1 + resource.faction(Directorate).exposure * 1,

    success     = "Card remains in play (persistence=Seasonal) on Directorate FRG. While in play, any opponent Public Act targeting a district where Directorate influence is >= Established suffers boost=-10.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Environmental shaping. Triggers when the Arbiter reveals a World Event. The ModReactCard itself is placed face-up on the Directorate's Faction Resolution Grid as a standing condition for the rest of the Quarter. It imposes a -10 difficulty penalty on any opponent PA that targets a district where Directorate is Established or higher. Solves the 'world event extension' gap by letting Directorate piggyback on the World Event phase to declare their own global environmental constraint. Legally escapes Art 00a §9.1 because it modifies action difficulty (9.1a), not resource income Cost reasoning: Exposure represents the widespread public broadcast necessary to enforce an emergency lockdown. ⚠ XA-54: 'world_event.played' assumes 'World Event' is either a defined Broadcast Card subtype or a synonym for all Broadcast Cards — Broadcast Card design is open; trigger frequency depends entirely on how many World Events exist in the Broadcast Deck.",
    arbiter_note = None,
)
```

---

### DIR.MOD.7 — EMINENT DOMAIN *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |
| Trigger frequency (ModReactCard) | ⚠ |  |  |
| Firing window (ModReactCard) | ⚠ |  |  |
| Automatic vs. d100 (ModReactCard) | ⚠ |  |  |
| Stack behavior (ModReactCard) | ⚠ |  |  |
| Ring constraint (ModReactCard) | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*Jurisdictional claim over private development.*

```python
DIR.MOD.7 = Card(
    id      = "DIR.MOD.7",  card_id="DIR.MOD.7",  version="v0.1",
    name    = "Eminent Domain",
    tagline = "Private development is subject to institutional oversight.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = structure_block.placed(faction=opponent),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,

    success     = arbiter.place(presence_chip, district=target_district, faction=Directorate, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Win-condition engine. Whenever an opponent builds a structure, Directorate immediately claims jurisdictional oversight, placing a presence chip in that district for free. Helps Directorate passively achieve 'Established in more districts'.",
    arbiter_note = None,
)
```

---

### DIR.MOD.8 — ASSET SEIZURE *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |
| Trigger frequency (ModReactCard) | ⚠ |  |  |
| Firing window (ModReactCard) | ⚠ |  |  |
| Automatic vs. d100 (ModReactCard) | ⚠ |  |  |
| Stack behavior (ModReactCard) | ⚠ |  |  |
| Ring constraint (ModReactCard) | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*Impounds public operational funds in Established territory.*

```python
DIR.MOD.8 = Card(
    id      = "DIR.MOD.8",  card_id="DIR.MOD.8",  version="v0.1",
    name    = "Asset Seizure",
    tagline = "Unlicensed public operations are subject to immediate fines.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = public_act.placed_on_frg(target_district=where(faction(Directorate).influence >= Established)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Directorate).mandate * 1 + resource.faction(Directorate).capital * 1,

    success     = arbiter.remove(resource_token, target=trigger.card, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    narrative    = None,
    perspectives = None,
    design_note  = "Bureaucratic taxation. Triggers when a PA is placed on the FRG targeting a Directorate-Established district. Directorate instantly removes (impounds) 1 resource token off the card. The acting faction must either add a replacement resource before Beat 4, or suffer partial-payment failure Cost reasoning: Requires Capital to mobilize the physical impoundment teams while Mandate authorizes the seizure.",
    arbiter_note = None,
)
```

---

### DIR.MOD.9 — FISCAL SANCTION *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |
| Trigger frequency (ModReactCard) | ⚠ |  |  |
| Firing window (ModReactCard) | ⚠ |  |  |
| Automatic vs. d100 (ModReactCard) | ⚠ |  |  |
| Stack behavior (ModReactCard) | ⚠ |  |  |
| Ring constraint (ModReactCard) | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S131. Reactive React on any faction's Public Standing decrease — Directorate spends a matching, non-Expired Intel token (the payoff for holding tokens from DIR.PA.2 Convene an Inquiry, or any other source) to open a formal sanction. Fills a genuine gap: Directorate previously had zero Economy\|Remove cards. Closes the last 1 of 6 toward the 54-card floor (04-n149). First Permanent-persistence ModReactCard in the set — new combination of two individually-established patterns, flagged in design_note rather than assumed to need a fresh Art 03 procedure.*

```python
DIR.MOD.9 = Card(
    id      = "DIR.MOD.9",  card_id="DIR.MOD.9",  version="v0.1",
    name    = "Fiscal Sanction",
    tagline = "The public already turned on them. Directorate just needed the opening.",
    type    = ModReactCard,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    trigger         = standing_marker.decreased(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,

    persistence = Permanent,
    persistence_condition = faction(trigger.faction).pays(2, resource.native, to=Reservoir),
    persistence_effect    = PublicAct(submitter=trigger.faction).blocked_at(phase_b),
    # Blocks ALL Public Act submission from the sanctioned faction (broader than PA.6 Standing Injunction's
    # single-taxonomy block) — clears only when the fine is paid; no quarter-end auto-expiry (deliberate:
    # distinct from PA.6's dual-clear pattern — this is a debt, not a deterrent).

    target_district = None,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = intel_token(faction=trigger.faction, age__in=[Fresh, Stale]) * 1,

    success     = faction(Directorate).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    narrative    = None,
    perspectives = None,
    design_note  = "Fills Directorate's Economy|Remove gap (previously zero cards in that cell, §9). Reactive: fires whenever ANY faction's PS decreases, for any reason — the public souring on a faction is the trigger. Gate: Directorate must hold a non-Expired Intel token keyed to the same faction whose PS just dropped, consumed on fire. Effect is two-part: (1) +1 PS to Directorate for opening the sanction (matches PA.6 Standing Injunction's placement-PS precedent); (2) Permanent standing condition blocking ALL Public Act submission from the sanctioned faction — not one taxonomy, the whole class — until they pay a 2-native fine to Reservoir (self-policing per GR 6.1a, same clearing pattern as Zoning Freeze/Standing Injunction). No quarter-end escape valve — this is a debt the target must actively clear, not a deterrent play with a built-in expiry. First Permanent-persistence ModReactCard in the set (existing precedent is Immediate fire-and-consume or Seasonal-until-Quarter-end) — a new but consistent extension of the card-as-condition pattern, not new ARBITER behavior requiring a fresh procedure.",
    arbiter_note = "On trigger (any faction's Standing marker moves down, any cause): if Directorate holds a Fresh or Stale Intel token keyed to that faction, Directorate may spend it to play this card. Directorate PS +1. Place card in Directorate's play area as a standing condition naming the sanctioned faction. From this point forward: the sanctioned faction cannot submit any Public Act at Phase B. Card remains active until the sanctioned faction pays 2 of their native resource to Reservoir, at which point remove the card and announce.",
)
```

---

### DIR.MOD.10 — RIOT CONTROL UNIT *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S132. First ModBattleCard content in the game — 09-06 pattern-setter, establishing the stub format for the whole subclass. Fields follow Art 04 §6.1/§6.2 (ModBattleCard column) and the S132 procedure redesign (Art 03 §10.1.2, PM02 L242): `effect` is a fixed direction printed on the card, `target` is named by whoever plays it at commit (§10.1.2 Step 1.2.2) — not restricted to Directorate or to a contesting faction. Directorate's literal-force doctrine (§5a: "military assets: enforcement personnel and equipment for conflict resolution and presence removal") expressed as a Boost. **Count/magnitude locked S132 (Andy):** 4 cards per faction — 2 Boost + 2 Hinder, magnitudes +1/+2 and −1/−2 respectively; `value_rating` mirrors `magnitude`. Flagged for playtest validation, not treated as final (04-n94 log-to-validate). This is the weaker Boost tier (+1).*

```python
DIR.MOD.10 = Card(
    id      = "DIR.MOD.10",  card_id = "DIR.MOD.10",  version = "v0.1",
    name    = "Riot Control Unit",
    tagline = "Institutional muscle, committed to hold whatever line the institution has already drawn.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=1),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 1,      # mirrors magnitude — resolves 04-n94's "do these move together" question for this pattern
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).

    portrait     = None,   # TBD — modifier card portrait model still open (same open note as SYN.MOD.1 The Fixer)
    narrative    = "Directorate enforcement units, deployed not to seize new ground but to hold whatever the institution has already decided should hold.",
    arbiter_note = "Playable by any faction, not just Directorate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### DIR.MOD.11 — EMERGENCY CURFEW *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S132. Hinder counterpart to DIR.MOD.10, expressing the other half of §5a's Directorate doctrine: "Suppression toolkit: push other factions' control tiers down rather than building own tiers up — best suppression capability in the game." A curfew doesn't reinforce Directorate's own position in the contest — it makes the named faction's position harder to hold, a Tactic rather than a deployed Asset. Weaker Hinder tier (−1); DIR.MOD.13 Martial Lockdown is the escalated −2 counterpart.*

```python
DIR.MOD.11 = Card(
    id      = "DIR.MOD.11",  card_id = "DIR.MOD.11",  version = "v0.1",
    name    = "Emergency Curfew",
    tagline = "Movement restricted, checkpoints up — whoever needed the street tonight doesn't get it.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=1),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 1,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).

    portrait     = None,   # TBD — modifier card portrait model still open (same open note as SYN.MOD.1 The Fixer)
    narrative    = "A curfew order goes out on short notice — official reasoning vague, timing anything but coincidental.",
    arbiter_note = "Playable by any faction, not just Directorate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### DIR.MOD.12 — REQUISITIONED EQUIPMENT *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S132. Second Boost card, Equipment category rather than DIR.MOD.10's human Asset — rounds out the pattern-setter with all three naming-convention categories represented (Asset/Equipment/Tactic, S130 lock) before replicating to the other four factions. Stronger Boost tier (+2) — heavier material commitment than the routine personnel deployment of DIR.MOD.10.*

```python
DIR.MOD.12 = Card(
    id      = "DIR.MOD.12",  card_id = "DIR.MOD.12",  version = "v0.1",
    name    = "Requisitioned Equipment",
    tagline = "Barricades, vehicles, surveillance rigs — whatever the depot had on hand.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=2),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 2,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).

    portrait     = None,   # TBD — modifier card portrait model still open (same open note as SYN.MOD.1 The Fixer)
    narrative    = "Institutional hardware, signed out of storage on short notice and committed to wherever the tension is highest tonight.",
    arbiter_note = "Playable by any faction, not just Directorate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### DIR.MOD.13 — MARTIAL LOCKDOWN *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S132. Escalated Hinder counterpart to DIR.MOD.11 Emergency Curfew (−2 vs. −1) — completes the 2 Boost / 2 Hinder pattern locked S132. Where Curfew is a routine administrative order, Lockdown is Directorate's "best suppression capability in the game" (§5a) turned all the way up: full mobilization against the named faction's position, not just restricted movement.*

```python
DIR.MOD.13 = Card(
    id      = "DIR.MOD.13",  card_id = "DIR.MOD.13",  version = "v0.1",
    name    = "Martial Lockdown",
    tagline = "Full mobilization. Whatever ground they were counting on tonight, they don't get to hold it.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=2),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 2,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).

    portrait     = None,   # TBD — modifier card portrait model still open (same open note as SYN.MOD.1 The Fixer)
    narrative    = "The order comes down from Government Citadel: full lockdown, effective immediately. No one asks who requested it.",
    arbiter_note = "Playable by any faction, not just Directorate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### DIR.MOD.14 — STANDING ORDER *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135. First ModActionCard content in the game exercising the actual `ModActionExpr` menu (09-06/04-n157 pattern-setter — PM02 L256; STD.MOD.1 Overture and SYN.MOD.1 The Fixer, the two prior "ModActionCard" entries, were both migrated to Issued ModReactCard at L245, leaving this slot genuinely empty until now). Establishes the tagged-union call convention for `ModActionExpr` — `ModActionExpr.<variant>(...)`, no prior instance existed to follow. Fields per §6.1/§6.2 (ModActionCard column) and the 04-n157 action-space analysis: **host-binding** is packet-pairing only — attach at Dispatch assembly to any CA/PA in the acting faction's own submitted packet (Art 03 §9.1.1); no card-level restriction field exists or is needed, and a ModActionCard can never reach a rival's sealed Dispatch Case. **Cost** is `None` uniformly — Beat 0 payment validation (Art 03 §9.4.0.1 Step 2) could support a live modifier cost here, unlike ModBattleCard's true no-cost-step case, but the splay-display convention (§9.4.0.1 Step 4) makes a distinct modifier cost illegible, so it folds into the host packet's total drain instead. **Count/format locked S135, revised twice same session:** 12 cards/faction — 4 `threshold_delta` (this tier) + 2 `success_multiplier` + 4 `ps_shift` + 2 `cost_reduction`, asymmetric because the four effect types have genuinely different magnitude-variation room (§6.3): `threshold_delta` runs against the d100 threshold scale (real thresholds 25–65, `ring_mod`/`doctrine_mod` already establish ±10/±15 as meaningful) and supports 4 tiers (+5/+10/+15/+20 — Andy's original example already named 4 values; a first pass compressed it to 3 before he caught it reading back the transcript); `ps_shift` likewise grew from an initial 2-card same-direction reading to a full 2×2 self/target matrix (see DIR.MOD.19); the other two effect types are small-integer/exponential mechanics that stay at 2 tiers. Directorate's institutional-authority doctrine (§5a) expressed as a pre-cleared procedural advantage — this is the weakest tier (+5).*

```python
DIR.MOD.14 = Card(
    id      = "DIR.MOD.14",  card_id = "DIR.MOD.14",  version = "v0.1",
    name    = "Standing Order",
    tagline = "A directive already on file, cleared before anyone thought to ask.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1, effect is parasitic on host action

    effect          = ModActionExpr.threshold_delta(n=5),  # eases the host CA/PA's own threshold; self-only — no faction param on this variant (§6.3, 04-n170)
    value_rating    = 1,      # minor tier of 3 (04-n157: threshold_delta supports 3 magnitude tiers — +5/+10/+15)
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModActionCard column) — no trigger, no beat, no resolution, no target_* fields.
    cost            = None,   # locked S135 (04-n157) — splay-display convention (Art 03 §9.4.0.1 Step 4) makes a distinct modifier cost illegible; folds into host packet's total drain instead.

    portrait     = None,   # TBD — modifier card portrait model still open (same open note as ModBattleCard stubs)
    narrative    = "A directive already cleared through channels lets a Directorate operation proceed without the friction a fresh request would meet.",
    arbiter_note = "Attach at Dispatch assembly to any CA/PA in the same faction's own packet (Art 03 §9.1.1) — no card-level host restriction, narrative fit is advisory only. Effect applies only to the host it's packeted with; cannot reach another faction's operation.",
)
```

---

### DIR.MOD.15 — REGULATORY CLEARANCE *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135. Mid tier of the 3 `threshold_delta` cards (+10, matching the `ring_mod`/`doctrine_mod` baseline granularity — §6.5). Reframed from an earlier hostile-flavored seed concept ("Regulatory Inspection" — raising a rival's difficulty, `Whiteboard/modifier_card_ideas.md`) per **04-n170**: `threshold_delta` carries no faction parameter (§6.3), so it can only ever ease the acting faction's own host action, never a rival's.*

```python
DIR.MOD.15 = Card(
    id      = "DIR.MOD.15",  card_id = "DIR.MOD.15",  version = "v0.1",
    name    = "Regulatory Clearance",
    tagline = "The paperwork already says yes.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=10),
    value_rating    = 2,      # mid tier of 3
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    cost            = None,   # see DIR.MOD.14 — splay-display convention, not a per-card exception

    portrait     = None,
    narrative    = "An inspection scheduled and passed well in advance leaves nothing for bad luck — or a rival's tip-off — to catch.",
    arbiter_note = "Reframed from a hostile-flavored seed concept per 04-n170 — self-only, same basis as all threshold_delta cards in this set.",
)
```

---

### DIR.MOD.16 — SHOW OF FORCE *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135, revised same session: third of **4** `threshold_delta` tiers (+15), not the capstone — Andy corrected the tier count from 3 to 4 (+5/+10/+15/+20; his original example already named 4 values, "+5, +10, +25, +20," compressed to 3 in the first pass). DIR.MOD.25 Executive Mandate (+20) is now the true capstone. Also reframed from a hostile-flavored seed concept per 04-n170, same basis as DIR.MOD.15. Magnitude exceeds the ±15 `doctrine_mod` baseline only nominally.*

```python
DIR.MOD.16 = Card(
    id      = "DIR.MOD.16",  card_id = "DIR.MOD.16",  version = "v0.1",
    name    = "Show of Force",
    tagline = "The uniforms are visible before the operation even starts.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=15),
    value_rating    = 3,      # third of 4 tiers (widened value_rating range to 1–4, S135/L259 — see DIR.MOD.25)
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "A visible deployment backs up whatever the Directorate is about to attempt — resistance tends to evaporate before it fully forms.",
    arbiter_note = "Reframed from a hostile-flavored seed concept per 04-n170, same basis as DIR.MOD.15.",
)
```

---

### DIR.MOD.17 — BY THE BOOK *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135. Common tier of the 2 `success_multiplier` cards (n=1) — 04-n157: this effect type supports only 2 tiers, since n=1 already doubles the host's effect and n=2 triples it.*

```python
DIR.MOD.17 = Card(
    id      = "DIR.MOD.17",  card_id = "DIR.MOD.17",  version = "v0.1",
    name    = "By the Book",
    tagline = "Every form filed correctly. Every step accounted for.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=1),  # fires the host's success effect an additional time
    value_rating    = 1,      # common tier of 2
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "Procedural correctness compounds — an action executed exactly to protocol produces more than the protocol strictly requires.",
    arbiter_note = "Self-only, same as all non-ps_shift ModActionExpr variants (§6.3, 04-n170) — amplifies the acting faction's own host action, never a rival's.",
)
```

---

### DIR.MOD.18 — OVERWHELMING RESPONSE *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135. Rare/capstone tier of the 2 `success_multiplier` cards (n=2 — triples the host's success effect). Flagged for playtest, same caveat as ModBattleCard's magnitude scale (04-n94) — reserve for high-stakes plays, not routine deployment.*

```python
DIR.MOD.18 = Card(
    id      = "DIR.MOD.18",  card_id = "DIR.MOD.18",  version = "v0.1",
    name    = "Overwhelming Response",
    tagline = "What began as routine escalates into something the whole city notices.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=2),
    value_rating    = 2,      # capstone tier of 2
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "A measured response becomes full institutional mobilization — the outcome lands far past what was ever authorized on paper.",
    arbiter_note = "Rare/capstone tier — log actual play outcomes before treating n=2 as balanced (04-n157, same playtest caveat as 04-n94).",
)
```

---

### DIR.MOD.19 — MODEL CITIZEN *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135, revised same session: `ps_shift` is a full 2×2 matrix, not a 2-card direction split — 4 cards total (DIR.MOD.19/23/20/24), mirroring ModBattleCard's Boost+1/+2, Hinder−1/−2 structure exactly. Unlike the other three `ModActionExpr` variants, `ps_shift` carries a faction parameter (§6.3: `acting | target | named faction`), so both **direction** (self vs. target) and **magnitude** (±1/±2) vary independently. This card: self, minor (+1). DIR.MOD.23 Commendation: self, major (+2). DIR.MOD.20 Public Reprimand: target, major (−2). DIR.MOD.24 Internal Affairs Referral: target, minor (−1). Faction ModActionCard count revised 9 → **11 cards/faction** (3 threshold_delta + 2 success_multiplier + 4 ps_shift + 2 cost_reduction); Ring ModAction revised 18 → **22 cards/ring** (11 × 2 for Portable/Ring-Locked). See PM02 L257 (revises L256).*

```python
DIR.MOD.19 = Card(
    id      = "DIR.MOD.19",  card_id = "DIR.MOD.19",  version = "v0.1",
    name    = "Model Citizen",
    tagline = "Compliance, held up publicly as the standard everyone else should meet.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=1),  # self-boost half of the direction-split pair (04-n157)
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "The Directorate's conduct is cited publicly as the standard — a small, deliberate boost to standing.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half of the pair always resolves to the acting faction.",
)
```

---

### DIR.MOD.20 — PUBLIC REPRIMAND *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135. Target-hinder, major tier (−2) of the `ps_shift` 2×2 matrix — see DIR.MOD.19 for the full structure. Magnitude mirrors the established Intel Token Hinder precedent (PM02 L242) rather than the ±1 baseline, since a named PS hit reads as a real consequence, not a nudge. This is one of two cards in the set that reach a faction other than the acting one — legitimately, since `ps_shift` is schema-built for it (unlike `threshold_delta`/`success_multiplier`/`cost_reduction`, flagged self-only at 04-n170).*

```python
DIR.MOD.20 = Card(
    id      = "DIR.MOD.20",  card_id = "DIR.MOD.20",  version = "v0.1",
    name    = "Public Reprimand",
    tagline = "A formal rebuke, on the record, addressed to exactly the faction that earned it.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-2),  # target-hinder half of the pair
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "An official rebuke lands on whoever the action was aimed at — public, on the record, and costly.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA itself names as its target_faction (§6.1) — only attachable to a host that has one; unattachable to a host with target_faction=None.",
)
```

---

### DIR.MOD.21 — JURISDICTION WAIVER *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135. Common tier of the 2 `cost_reduction` cards (n=1). PA-only per §6.3 — CA cost is committed at dispatch before Beat 0 and cannot be reduced post-submission.*

```python
DIR.MOD.21 = Card(
    id      = "DIR.MOD.21",  card_id = "DIR.MOD.21",  version = "v0.1",
    name    = "Jurisdiction Waiver",
    tagline = "A procedural waiver clears part of the overhead before the request is even filed.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=1),  # PA-only (§6.3)
    value_rating    = 1,      # common tier of 2
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "A jurisdictional formality is waived for this faction alone, quietly, ahead of submission.",
    arbiter_note = "PA host only. Attach at Dispatch (Art 03 §9.2) alongside the declared PA; reduces the resource total owed at Beat 4 by 1 unit.",
)
```

---

### DIR.MOD.22 — REQUISITIONED RESOURCES *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135. Capstone tier of the 2 `cost_reduction` cards (n=2). PA costs sample at 1–4 total units (04-n157) — a 2-unit reduction approaches making many PAs nearly free; flagged for playtest same as the rest of this set.*

```python
DIR.MOD.22 = Card(
    id      = "DIR.MOD.22",  card_id = "DIR.MOD.22",  version = "v0.1",
    name    = "Requisitioned Resources",
    tagline = "Institutional supply lines make this considerably cheaper than it should be.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=2),
    value_rating    = 2,      # capstone tier of 2
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "Materiel and personnel already committed elsewhere in the institution get redirected — the public act proceeds at a fraction of its nominal cost.",
    arbiter_note = "Capstone cost_reduction tier — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157, same playtest caveat as the rest of this set).",
)
```

---

### DIR.MOD.23 — COMMENDATION *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135, added same session as DIR.MOD.24 to complete the `ps_shift` 2×2 matrix (Andy: "we should make 2 more... if ps can be used this way — need +2 ps and −1 ps cards"). Self-boost, major tier (+2) — stronger counterpart to DIR.MOD.19 Model Citizen. See DIR.MOD.19 for the full matrix structure.*

```python
DIR.MOD.23 = Card(
    id      = "DIR.MOD.23",  card_id = "DIR.MOD.23",  version = "v0.1",
    name    = "Commendation",
    tagline = "Official recognition, delivered with the full weight of the institution behind it.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=2),  # self-boost, major tier of the 2×2 matrix
    value_rating    = 2,      # mirrors magnitude, same convention as ModBattleCard
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "A commendation issued through official channels carries more weight than a compliment — it's the institution putting its name behind the outcome.",
    arbiter_note = "Self-only, resolves to the acting faction. Major tier — flagged for playtest same as the rest of this set (04-n157).",
)
```

---

### DIR.MOD.24 — INTERNAL AFFAIRS REFERRAL *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135, added same session as DIR.MOD.23 to complete the `ps_shift` 2×2 matrix. Target-hinder, minor tier (−1) — softer counterpart to DIR.MOD.20 Public Reprimand: a quiet referral rather than a public rebuke. Drawn from the Faction ModAction seed pool (`Whiteboard/modifier_card_ideas.md`), previously unused when only 2 ps_shift cards were planned.*

```python
DIR.MOD.24 = Card(
    id      = "DIR.MOD.24",  card_id = "DIR.MOD.24",  version = "v0.1",
    name    = "Internal Affairs Referral",
    tagline = "A rival's conduct is quietly referred for review, and word gets out.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-1),  # target-hinder, minor tier of the 2×2 matrix
    value_rating    = 1,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "Nothing is announced. A referral goes into a file, and somehow the file's contents find their way into conversation.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA itself names as its target_faction (§6.1) — same constraint as DIR.MOD.20, minor tier.",
)
```

---

### DIR.MOD.25 — EXECUTIVE MANDATE *(stub)*

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
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 Card Story |
| Outcome determinacy | ⚠ |  |  |
| Resource cost positioning | ⚠ |  |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  |  |  |

*S135, added same session Andy caught the tier count reading back the transcript: `threshold_delta` is 4 tiers, not 3 — his original example ("+5, +10, +25, +20") already named 4 values; the first pass compressed the top two into a single "+15–20 capstone" range. True capstone (+20); DIR.MOD.16 Show of Force (+15) is now the third of four, not the top. `value_rating` **widened schema-wide from 1–3 to 1–4 (§6.1/§6.2, PM02 L259)** so this tier gets its own distinct value (4) instead of sharing DIR.MOD.16's band — Andy's call after weighing it against leaving the two tiers to share `value_rating=3`. Faction ModActionCard count revised again: 11 → **12 cards/faction** (4 threshold_delta + 2 success_multiplier + 4 ps_shift + 2 cost_reduction); Ring ModAction: 22 → **24 cards/ring**. See PM02 L258/L259 (revises L257).*

```python
DIR.MOD.25 = Card(
    id      = "DIR.MOD.25",  card_id = "DIR.MOD.25",  version = "v0.1",
    name    = "Executive Mandate",
    tagline = "When the order comes from the top, nothing further needs to be cleared.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=20),  # capstone tier of 4
    value_rating    = 4,      # true capstone — value_rating widened to 1–4 (S135/L259) so this tier gets its own distinct value instead of sharing DIR.MOD.16's band
    ring_constraint = None,
    ring_origin     = None,   # Directorate faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "An executive mandate carries the full authority of Directorate leadership — nothing left to interpret, nothing left to contest.",
    arbiter_note = "Capstone threshold_delta tier — log actual play outcomes before treating +20 as balanced (same playtest caveat as the rest of this set, 04-n157).",
)
```

---

