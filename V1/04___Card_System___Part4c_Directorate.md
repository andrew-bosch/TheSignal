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
| Data schema validation | ⚠ | Pending 04-n70. Also missing `card_id`, `doctrine_mod`, `boost`, `ps_framing` entirely (not just unset) — see schema_cleanup_log.md #24. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Mandate only, typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **Block scope — STD.CA.1/STD.CA.3 only:** DIR.CA.1 blocks STD.CA.1 and STD.CA.3 explicitly. Confirm whether this should extend to STD.CA.4 (Demolition) or STD.CA.8 (Buy Influence) to reflect true jurisdictional authority, or remain limited to the two build/presence cards by design.
- **game.block resolution:** Confirm Beat 2 block mechanic — does a blocked STD.CA.1/STD.CA.3 cost the submitter their action slot and resources, or is it returned? Needs Art 03 §9.4 Beat 2 procedure to confirm.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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
| Data schema validation | ⚠ | Pending 04-n70. Also missing `card_id`, `doctrine_mod`, `boost`, `ps_framing` entirely — see schema_cleanup_log.md #24. Taxonomy note: `function = Move` is not a valid Function-vocabulary value (`ref_taxonomy.md` §Function Vocabulary lists Add/Remove/Redirect/Modify/Protect/Block/Copy/Reveal/Shift/Corrupt only — Move is a physical-verb primitive, not a Function; Redirect and Shift are the Functions that use Move as their underlying primitive). This card's own note claims `function` was deliberately "corrected S107 L226 (Remove → Move)" — flagged, not fixed; see schema_cleanup_log.md #25. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/successcrit/failcrit populated (fail=None), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Cross-faction-resource (Mandate + Findings, both typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **Intel token age interpretation:** `intel(faction=faction(target), age_rounds<=1)` — confirm "age_rounds<=1" means Fresh token (gathered this or last round) per Art 02 §12 aging definitions.
- **Successcrit Mandate recovery:** +3 Mandate on crit success is the highest reward in the Directorate set — confirm this is intentional given Mandate×3 base cost (net zero, but only on crit).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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
| Data schema validation | ⚠ | Pending 04-n70. Also missing `card_id`, `doctrine_mod`, `boost`, `ps_framing` entirely — see schema_cleanup_log.md #24. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Mandate only, typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **Art 03 Beat 2 procedure:** Beat 2 section does not yet include district-surveillance IntelDeliverySlip delivery. Procedure addition required before Issues Resolved (04-n44). Gates Art 03 re-sign-off.
- **Art 02 component entry:** IntelDeliverySlip has no design entry in Art 02. Addition required before Issues Resolved (04-n45). Gates Art 02 re-sign-off.
- **00b IS-xx definition:** IS-xx definition covers Beat 3 delivery only. Update required to include Beat 2 delivery pattern (04-n46). Gates 00b re-sign-off.
- **Card name:** "Placement" implies permanent installation — consider rename (e.g., "Surveillance Order," "District Watch") during naming pass.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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
| Data schema validation | ⚠ | Pending 04-n70. Also missing `card_id`, `doctrine_mod`, `boost`, `ps_framing` entirely — see schema_cleanup_log.md #24. Same `function = Move` taxonomy-vocabulary flag as DIR.CA.2 — see schema_cleanup_log.md #25. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Mandate only, typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **Entry qualification check:** `arbiter_note` states that if Directorate does not qualify for entry at the destination, the card is discarded without effect (resources not refunded). Confirm "qualify for entry" criteria — is there a district-entry restriction in Art 01 or Art 03?
- **Move count vs. restriction:** Restriction requires source.presence >= 1 but the card moves count=2. Can the card be played if source has only 1 token (moving fewer than 2)? Confirm whether count=2 is a maximum or exact.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
)
```

---

### DIR.PA.4 — REGULATORY DOWNGRADE
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Formal, narrow, deterministic revocation of exactly one named presence token — the fix for the original 04-n104 BLOCKED design (which targeted InfluenceTier, a derived, non-targetable state, violating Governing Rule 9.1). The S131 redesign removes the ARBITER-side comparison entirely: ARBITER removes 1 physical token; any resulting tier change is a natural downstream consequence of fewer tokens under the standard influence-level rules, not a direct write. Established+ restriction preserves the original jurisdictional-legitimacy gate.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal, narrow, single-token revocation — legitimate institutional act, distinct in scope from covert disruption cards (STD.CA.4, DIR.CA.2) | Art 00 §7 |
| Voice fit | ⚠ | `narrative = None`, `perspectives = None` — no in-world voice content at all, not even a single Directorate line. Same gap on all 5 of this S131 batch (DIR.PA.4/5/9/10/11) — flagged as a uniform cluster finding, not fixed here. | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate-exclusive; Established+ restriction reflects jurisdictional legitimacy; narrow single-token scope matches "control, restraint, continuity" doctrine (a scalpel, not Sanctioned Raid's maximum-force approach) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Remove / PresenceToken — matches `card_status` DB directly | Art 04b §4 |
| Balance | ✓ | Mandate × 2 for exactly 1 token; design_note locks the mono-cost principle for N=1, cross-resource required for any future N>1 variant | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent token removal; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — no lingering marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate submitter=+1, single entry | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; restriction checks target's influence tier — valid zone condition | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken — existing component; no new component required | Art 02 §6 |
| Supported by game procedure | ✓ | Beat 4; `arbiter.remove(presence_chip, ...)` is a direct token removal, no derived-state write — Governing Rule 9.1-compliant per its own design_note | Art 03 §9.4 |
| Data schema validation | ⚠ | Both `id` and `card_id` set (good — addresses the missing-`card_id` gap flagged elsewhere in this review). `ps_framing = None`, `narrative = None`, `perspectives = None` all explicitly set (not omitted) — cleaner than the corpus norm of silent omission, but the content itself (voice/narrative) is still absent. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block present | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`; only `success` populated (successcrit/fail/failcrit all `None`) — no `game.choose_one()` or conditional branching. `outcome_type = Unilateral` present and non-`None`. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Mandate × 2), correctly typed. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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

### DIR.PA.5 — ZONING FREEZE
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Card-as-condition Permanent PA that auto-reverts any new presence chip placed in the named district — self-inclusive (Directorate's own new chips revert too), reflecting Directorate's "uniform scrutiny" doctrine established by DIR.CA.8. Retaxonomized to Territory/Block/PresenceToken specifically to avoid the original 04-n104 BLOCKED violation (targeting InfluenceTier, a derived state). Reuses the confirmed ModReactCard-style `presence_chip.placed` trigger vocabulary inside a PA's `persistence_effect` — the same established pattern design_reference_card_system.md documents this card as the first example of (S131). Clearing is a public toll any faction may pay, not Directorate-exclusive.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | District-level standing "law" that applies to all factions including the submitter — legitimate institutional-authority act | Art 00 §7 |
| Voice fit | ⚠ | `narrative = None`, `perspectives = None` — no in-world voice content. Same gap across all 5 of this S131 batch (DIR.PA.4/5/9/10/11) — flagged as a uniform cluster finding, not fixed here. | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate-exclusive; self-inclusive enforcement matches DIR.CA.8's uniform-scrutiny doctrine ("scrutiny means something only when it applies uniformly") — directly extends an established doctrinal principle rather than inventing a new one | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Block / PresenceToken — matches `card_status` DB directly; design_note explains the deliberate retaxonomization away from InfluenceTier/Submission | Art 04b §4 |
| Balance | ✓ | Cross-resource cost (Mandate ×2 + district-native ×1 + Capital ×1) for a Permanent, self-inclusive district freeze — design_note reasons through each cost component's narrative fit | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent; clears only when any faction pays the stated toll | Art 04 §5 P19 |
| Persistence | ✓ | Permanent; card-as-condition — no separate marker component | Art 04 §6 |
| Trigger validity | ✓ | `persistence_effect` uses confirmed TriggerExpr vocabulary (`presence_chip.placed(district=...)`) embedded inside a PA — the first confirmed example of this exact pattern per design_reference_card_system.md; correctly applied here | Art 04 §6.3 |
| Portrait validity | ✓ | Directorate submitter=+1, single entry | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named | Art 01 §6–§7 |
| Supported by components | ✓ | Operates on existing presence_chip component; no new component required | Art 02 §6 |
| Supported by game procedure | ✓ | Self-policing per Governing Rule 6.1a; deployment marker itself is never touched, only the resulting chip (Governing Rule 8.3a-compliant, explicitly reasoned in design_note) | Art 03 §9; Governing Rule 6.1a, 8.3a |
| Data schema validation | ⚠ | Both `id` and `card_id` set (addresses the missing-`card_id` gap flagged elsewhere in this review). `narrative = None`, `perspectives = None` explicitly set, content still absent. `resolution_type = "Permanent public act"` — not in the confirmed vocabulary (`"Probabilistic"`/`"Transactional"` only); flagged as an open schema question, same as DIR.PA.6/DIR.PA.11. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block present | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `success = None` — card placement itself IS the effect (card-as-condition pattern); no `game.choose_one()` or conditional branching anywhere in the spec. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Mandate + district-native + Capital, ×1–2 each), correctly typed throughout. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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
| Data schema validation | ⚠ | boost field present; threshold-scaling noted in §6.3; affinity corrected to None (04-n70). Re-derived S141: still missing `card_id`/`ps_framing` (see schema_cleanup_log.md #24). `cost`'s first term `resource.faction(acting) * 1` (and the identical term in `boost`) is missing a resource-type attribute — same corpus pattern as schema_cleanup_log.md #22, now confirmed outside the Standard set. | Art 04 §6.1–§6.3 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; all four tiers populated (success/successcrit/fail/failcrit), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Missing row, scaffolded S141. Triple-component cost (faction resource + district native + IntelToken) — cross-resource tier, consistent with this card's maximum-force framing. But the IntelToken component raises the same open question as schema_cleanup_log.md #10 (Intel Token as fungible `cost`) — third confirmed instance, now across a third card type (Standard CA, Directorate ModReactCard, Directorate CA). Flagged, not resolved. | Art 00a §9.2 |

#### Outstanding Issues

- **IntelToken as restriction:** Should IntelToken(faction=faction(target)) also appear as `restriction =` (card unplayable without it in hand) in addition to appearing in cost? Or is cost placement sufficient? Carry.
- **Intel token faction-keying:** Confirm faction-keyed to target is correct (vs. any held token of the type).
- **Sign-off gates:** 04-n81 (BM-xx registration), 04-n82 (Beat 0 boost procedure), 04-n83 (Beat 2/3 BM-xx resolution), 04-n84 (Discovery mechanic definition).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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
| Supported by game procedure | ⚠ | Re-derived S141: `game.active_permanents(faction=, ring=)` doesn't appear anywhere else in the corpus (grepped all 8 Part files) — the claim "existing permanent card procedure" isn't confirmed; no generalizable Art 03/07 procedure for "count active Permanent cards by ring" was found. Possible tension with Governing Rule 6.1 / Design Pillar 4.7b (new ARBITER-facing behavior should be defined as a general procedure first). Not resolved — flagged alongside DIR.CA.7 (same mechanism). | Art 03 §9 |
| Data schema validation | ⚠ | Fields consistent with §6.1–§6.3, but missing `card_id`, `boost`, `ps_framing` entirely (though `doctrine_mod=None` is declared, unlike DIR.CA.1–4) — see schema_cleanup_log.md #24. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Internal audit — standing record clean, allocation approved | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/successcrit/failcrit populated (fail=None), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Mandate only, typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **DB registration:** New card — requires id assignment in card_ref and component_metadata.
- **game.active_permanents() scope:** Confirm counting mechanism is unambiguous in paper play — ARBITER reads face-up Directorate Permanent cards from Directorate play area where card's target_district.ring == district(target).ring. **(S141: also needs a generalizable Art 03/07 procedure definition — see Supported by game procedure row above.)**

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding — upward PS shift; target = acting faction. **Flagged S141, not corrected:** this row names "PublicStanding," the retired term per `ref_taxonomy.md` (corrected S126 — not a valid card subject); the actual code field (`subject = StandingMarker`) is already correct. Row prose is stale, code is fine — cosmetic mismatch, left as found. | Art 04b §4 |
| Balance | ⚠ | PS yield scales with Permanents — same risk as DIR.CA.6 if Permanents accumulate; Mandate×2 cost higher than CA.6 to reflect PS vs. resource asymmetry | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — PS marker moved once at Beat 3 resolution | — |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Directorate +1 submitter | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; restriction = chip count > 1 | Art 01 §6–§7 |
| Supported by components | ✓ | PS marker (existing); no new component | Art 02 §11–§12 |
| Supported by game procedure | ⚠ | PS movement by ARBITER at Beat 3 resolution is an existing procedure, but `game.active_permanents(faction=, ring=)` (the counting mechanism this card's yield depends on) is the same not-found-elsewhere mechanism flagged on DIR.CA.6 — same open question, not resolved here either. | Art 03 §9 |
| Data schema validation | ⚠ | Fields consistent with §6.1–§6.3, but missing `card_id`, `boost`, `ps_framing` entirely (`doctrine_mod=None` is declared) — see schema_cleanup_log.md #24. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Closed-channel record circulation; public confidence signal without disclosed authorship | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `d100`; success/successcrit/failcrit populated (fail=None), no `game.choose_one()` — resolves deterministically. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Mandate only, typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **DB registration:** New card — requires id assignment.
- **Failcrit narrative:** PS−1 represents the brief being traced back to Directorate — confirm this holds as an institutional embarrassment consequence (vs. a larger penalty).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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
| Taxonomy fit | ⚠ | Resolution / Modify / Difficulty — threshold adjustment before Beat 3 resolution. **Flagged S141:** `v_card_mechanical_alignment` (DB) shows `Non-component Subject` for this card — "Difficulty" is not in `ref_taxonomy.md`'s Subject Vocabulary and is missing from `card_subject_map`, per that same reference's own gap-pattern table ("Subject string missing from card_subject_map → Add row to card_subject_map"). Distinct from the expected/known "Abstract Function" pattern on Modify/Block/Protect cards elsewhere in this set (CA.1/2/4) — this is a genuinely unregistered Subject term, not just an abstract-function non-issue. Not resolved. | Art 04b §4 |
| Balance | ⚠ | −15 to all Beat 3 ops in district is significant suppression at Mandate×2; self-inclusion is the cost; playtesting required | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate (within-month) — tokens placed at Beat 2, consumed at Beat 3 | — |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 2 Automatic | — |
| Portrait validity | ✓ | Directorate +1 submitter | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — no presence requirement | Art 01 §6–§7 |
| Supported by components | ✓ | Uses existing Modifier tokens — no new component | Art 02 §11 |
| Supported by game procedure | ✓ | ARBITER places existing Modifier tokens (−15) on each Beat 3 row targeting district at Beat 2 resolution — within existing modifier placement procedure | Art 03 §9 |
| Data schema validation | ⚠ | Automatic, no threshold/ring_mod; Beat 2. But missing `card_id`, `boost`, `ps_framing` entirely (`doctrine_mod=None` is declared) — see schema_cleanup_log.md #24. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Enhanced institutional review; uniform scrutiny including own ops | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Missing row, scaffolded S141. `Automatic`, single deterministic outcome (`success` only; `successcrit`/`fail`/`failcrit` all `None`). | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Missing row, scaffolded S141. Mono-resource (Mandate only, typed correctly). | Art 00a §9.2 |

#### Outstanding Issues

- **DB registration:** New card — requires id assignment.
- **Beat 2 Automatic + Beat 3 scope:** Confirm ARBITER can identify all Beat 3 rows for the target district at Beat 2 resolution before Beat 3 ops are revealed. Resolution grid rows are placed at Beat 0 — ARBITER has grid visibility. No new tracking required.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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
| Outcome determinacy | ✓ | `Automatic`; only `success` populated — no `game.choose_one()` or conditional branching. `outcome_type = Unilateral` present and non-`None` — passes the PA-wide check flagged going into this phase. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Mandate × 2), correctly typed (`.mandate` attribute present). Design_note's trailing "Cost reasoning: Exposure is necessary..." sentence doesn't match this card's actual Mandate-only cost — same dangling-fragment defect seen elsewhere in this review (e.g. SYN.CA.4). | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
DIR.PA.1 = Card(
    id      = "DIR.PA.1",  card_id="DIR.PA.1",  version="v1.0",
    name    = "Regulatory Override",
    tagline = "Declare a district under Directorate oversight, raising the cost of all non-Directorate presence operations.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer    = Territory,  function = Modify,  subject = PresenceToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = None,  # scaffolded, not addressed
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
    boost       = None,

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
    ps_framing = None,

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
| Outcome determinacy | ✓ | `Automatic`; only `success` populated — no `game.choose_one()` or conditional branching. `outcome_type = Unilateral` present and non-`None`. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Mandate × 3), correctly typed. Design_note's trailing "Cost reasoning: Findings provide the legal precedent and evidence required to sustain the injunction long-term" doesn't match this card at all — wrong resource (Mandate, not Findings) *and* wrong card (references "the injunction," i.e. DIR.PA.6, not this card's own Inquiry mechanic). Clearest confirmed instance yet of the dangling-copy-paste-fragment defect (schema_cleanup_log.md, extends SYN.CA.4). | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

```python
DIR.PA.2 = Card(
    id      = "DIR.PA.2",  card_id="DIR.PA.2",  version="v1.0",
    name    = "Convene an Inquiry",
    tagline = "Commission an ARBITER-mediated institutional investigation into a faction's recent operations.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer    = Information,  function = Add,  subject = IntelToken,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = None,  # scaffolded, not addressed
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
    boost       = None,

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
    ps_framing = None,

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
| Outcome determinacy | ✓ | `Automatic`; only `success` populated — no `game.choose_one()` or conditional branching. `outcome_type = Unilateral` present and non-`None`. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cross-resource (Mandate × 2 + Capacity × 1), correctly typed throughout. | Art 00a §9.2 |

#### Outstanding Issues

- **Counter-card removal:** Card sits in Directorate's PA area as a permanent board condition. Removal by counter-action requires new card type(s) — design TBD. See PM05 04-n29.
- **Art 03 persistence monitoring:** ARBITER needs a defined trigger point to check persistence_condition of all permanent PA cards (e.g., after any influence tier change). See PM05 04-n29. Blocks Issues Resolved.
- **Displaced faction with no presence elsewhere:** `move_to=district.where(faction.has_presence)` has no valid destination if the displaced faction holds no presence outside the named district. Fallback rule needed — e.g., marker is returned to hand (faction skips next placement) or moved to Baryo as unconditional fallback (Governing Rule 8.3b: no elimination).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

*Redesigned S66 — v1.0 (ring-scope) retired*

```python
EntryExitControls = Card(
    id      = "DIR.PA.3",  card_id="DIR.PA.3",  version="v2.0",
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
    boost = None,
    success = (
        for_each(
            deployment_marker(faction=faction.all_except(Directorate), district=district.named),
            arbiter.instruct(marker.owner, move_to=district.where(faction.has_presence), flip_to=Blocked),
        ),
        faction(acting).standing -= 1,
    ),
    successcrit=None,  fail=None,  failcrit=None,
    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = "Movement within the designated zone is now subject to Directorate authorization. Non-compliant presence has been relocated.",
    perspectives = {
        Directorate: "The district is designated. Who enters does so with our permission — or not at all.",
    },
    design_note  = "Persistent PA. Card sits in Directorate's active PA area on the Overview (not on district tile). Immediate: non-Directorate deployment markers in named district displaced to any district where owning faction has presence, flipped to Blocked. Persistent: non-Directorate deployment marker placement blocked in named district. persistence_condition auto-discards card if Directorate falls below Established. PS −1 at resolution (public backlash). Counter-card removal TBD — see PM05 04-n29.",
    arbiter_note = "Name the district. Each non-Directorate deployment marker there: owning faction moves it to any district where they have presence, flip to Blocked.",
    value_rating = None,  # scaffolded, not addressed
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
| Data schema validation | ⚠ | Pending 04-n70. Also: `resolution_type = "Permanent public act"` — not in the confirmed vocabulary (`"Probabilistic"` for d100, `"Transactional"` for Automatic per design_reference_card_system.md). Flagged as a new open question: does Permanent PA need its own confirmed `resolution_type` value in §6.3, or should this normalize to `"Transactional"`? | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`; only `success` populated — no `game.choose_one()` or conditional branching. `outcome_type = Unilateral` present and non-`None`. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Triple cross-resource (Mandate + Capital + Findings, ×1 each), correctly typed throughout — notable as the highest resource-type-diversity cost seen in the corpus so far. | Art 00a §9.2 |

#### Outstanding Issues

None.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ | |

*Redesigned S67 — v2.0. PublicAct → PublicAct. InjunctionMarker removed; card-as-condition pattern. Seasonal → Permanent with dual clearing condition (trigger OR Phase 21). Dispatch Token consumed on trigger per Governing Rule 7.3. target_taxonomy field introduced (§6.1/§6.2). Self-policing per Governing Rule 6.1a.*

```python
P_StandingInjunction = Card(
    id      = "DIR.PA.6",  card_id = "DIR.PA.6",  version = "v2.0",
    name    = "Standing Injunction",
    tagline = "Declare a public restriction on a named faction's next act of a specified type. If triggered, the act is voided.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,

    layer    = Submission,  function = Block,  subject = PublicAct,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    value_rating = None,  # scaffolded, not addressed
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
    boost       = None,

    success     = faction(Directorate).standing += 1,
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Directorate: PortraitEntry(submitter=+1)},
    ps_framing = None,

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
| Action fit | ⚠ | Territorial movement denial thematically fits Directorate doctrine, but the enforcement mechanism (a "Standing Condition") isn't implemented as a structured field — can't confirm the act is mechanically sound, only that it's thematically grounded | Art 00 §7 |
| Voice fit | ⚠ | No `narrative`/`perspectives` fields present at all (not even `None` — absent entirely) | Art 00 §7 |
| Doctrine alignment | ✓ | Design_note frames this correctly as blocking public/enforceable movement rather than blind covert space — consistent with Directorate's institutional-control doctrine | Art 00 §7 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Block / DeploymentMarker — matches `card_status` DB directly | Art 04b §4 |
| Balance | ⚠ | Cost (Mandate×2) is set, but effect magnitude can't be assessed — `success` is prose, not a structured mutation with a measurable scope | Art 02 §6–§7 |
| Effect duration | ⚠ | `persistence = Transient` (a valid enum value, but its first confirmed use anywhere in the CA/PA corpus reviewed so far) — yet the prose `success` text describes the effect lasting "until the end of Quarter+1," i.e. into the *next* Quarter. That reads as a multi-Quarter temporary, which Art 04 §5's duration discipline (P19–P21, design_reference_card_system.md) prohibits ("effects are permanent or within-Quarter"). Real tension between the declared persistence type and the card's own prose — flagged, not resolved. | Art 04 §5 P19 |
| Persistence | ⚠ | See Effect duration above — same tension | Art 04 §6 |
| Trigger validity | ✓ | No trigger field present; Automatic PA doesn't require one — acceptable by omission | — |
| Portrait validity | ⚠ | Scaffolded as `portrait = {}` (was absent entirely) — an empty dict is the neutral placeholder; a real Directorate entry would be a content decision, not made here | Art 04 §6.2 |
| Supported by zones | ⚠ | `target_district` scaffolded as `district.named` (was only referenced inside the prose `success` string, not a real field) | Art 01 §6–§7 |
| Supported by components | ✓ | DeploymentMarker — existing component | Art 02 §6 |
| Supported by game procedure | ⚠ | The Card-as-Condition pattern (design_reference_card_system.md) requires `persistence_condition` + `persistence_effect` as structured fields; this card describes the standing condition in prose inside `success` instead — doesn't follow the confirmed pattern. `persistence_condition`/`persistence_effect` scaffolded as `None` (structurally required placeholders), not filled with real logic. | Art 03 §9 |
| Data schema validation | ⚠ | `success` is a bare prose string, not a structured effect — same defect shape as the bare-string-`success` pattern already tracked on CA-phase stubs, now confirmed in PA phase; left untouched, not resolved. All other previously-absent fields scaffolded this pass: `card_id`, `boost`, `ps_framing`, `threshold`, `ring_mod`, `doctrine_mod`, `trigger`, `resolution_type`, `target_faction`/`target_object`/`target_taxonomy`, `affinity`, `restriction`, `successcrit`/`fail`/`failcrit`, `on_accept`/`on_decline`, `narrative`/`perspectives`, `arbiter_note` — all set to `None` (or the deterministic `"Transactional"` for `resolution_type`, matching every Automatic card in the corpus). `outcome_type` scaffolded as `None` explicitly rather than left silently absent — likely `Unilateral`, not resolved here. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block present | Art 04 §5 P26 |
| Outcome determinacy | ⚠ | No `game.choose_one()` present, but determinacy can't be positively confirmed either — `success` isn't a structured MutationExpr, so there's no tiered success/successcrit/fail/failcrit split to check against P27 at all | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Mandate × 2), correctly typed — the one field in this card structured enough to assess cleanly. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
DIR.PA.7 = Card(
    id      = "DIR.PA.7",  card_id = "DIR.PA.7",  version = "v1.1",
    name    = "Curfew",
    tagline = "Lock down a district to freeze physical movement.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Block,  subject = DeploymentMarker,
    beat    = 4,  resolution = Automatic,  threshold = None,
    ring_mod = None,  doctrine_mod = None,  trigger = None,
    value_rating = None,  # scaffolded, not addressed
    resolution_type = "Transactional",  outcome_type = None,  # scaffolded, not addressed
    persistence = Transient,
    persistence_condition = None,  persistence_effect = None,
    target_district = district.named,  target_faction = None,  target_object = None,  target_taxonomy = None,
    affinity = None,  restriction = None,
    cost    = resource.faction(Directorate).mandate * 2,
    boost   = None,
    success = "Places a Standing Condition on target_district until the end of Quarter+1: Deployment Markers cannot be moved into this district.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept = None,  on_decline = None,
    portrait = {},  # scaffolded, not addressed
    ps_framing = None,
    narrative = None,  perspectives = None,
    design_note = "A massive territorial denial tool. Blocks physical movement (which is public and enforceable) rather than targeting blind covert space.",
    arbiter_note = None,
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
| Action fit | ⚠ | Intelligence-authorized public audit is thematically grounded (Directorate uses institutional process, not covert fieldwork, same mode as DIR.PA.2), but the pay-or-lose-PS mechanism isn't implemented as a structured effect | Art 00 §7 |
| Voice fit | ⚠ | No `narrative`/`perspectives` fields present at all | Art 00 §7 |
| Doctrine alignment | ✓ | Design_note frames the Intel Token cost as "Directorate found out something that justifies the legal action" — consistent with institutional/evidence-based doctrine | Art 00 §7 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Economy / Remove / Capital — matches `card_status` DB directly | Art 04b §4 |
| Balance | ⚠ | Threshold 40 is set, but the actual consequence structure ("must pay 2 Capital or 2 native, or lose 2 PS") is prose, not a structured conditional effect — can't confirm how the choice is adjudicated (player choice at the table vs. an ARBITER-resolved branch) | Art 02 §6–§7 |
| Effect duration | ⚠ | `persistence` scaffolded as `Immediate` (was absent; deterministic default for a non-standing, one-shot PA per corpus convention) | Art 04 §5 P19 |
| Persistence | ⚠ | See Effect duration — scaffolded `Immediate` | Art 04 §6 |
| Trigger validity | ✓ | No trigger field; d100 PA doesn't require one — acceptable by omission | — |
| Portrait validity | ⚠ | Scaffolded as `portrait = {}` (was absent) — empty dict is the neutral placeholder, a real entry would be a content decision | Art 04 §6.2 |
| Supported by zones | ⚠ | `target_district = None` (faction-targeted, no district), `target_faction` scaffolded as `faction.opponent` (was only implied via bare reference inside prose) | Art 01 §6–§7 |
| Supported by components | ✓ | Capital, Intel Token — both existing components | Art 02 §6 |
| Supported by game procedure | ⚠ | The "pay X or lose PS" choice structure has no defined procedural home (not a `game.choose_one()` in the prohibited sense, but also not a structured `MutationExpr` — unclear who adjudicates payment vs. non-payment and when) | Art 03 §9 |
| Data schema validation | ⚠ | `success` is a bare prose string — same defect shape as DIR.PA.7; left untouched, not resolved. All other previously-absent fields scaffolded this pass: `card_id`, `boost`, `ps_framing`, `ring_mod`, `doctrine_mod`, `trigger`, `resolution_type` ("Probabilistic", matching this card's `d100` resolution), `persistence`/`persistence_condition`/`persistence_effect`, `target_district`/`target_faction`/`target_object`/`target_taxonomy`, `affinity`, `restriction`, `successcrit`/`fail`/`failcrit`, `on_accept`/`on_decline`, `narrative`/`perspectives`, `arbiter_note` — all `None` except as noted. `outcome_type` scaffolded as `None` explicitly — likely `Unilateral`, not resolved here. Cost also introduces yet another Intel-Token-as-cost notation variant (`intel_token(faction=target_faction)`), 11th confirmed instance corpus-wide. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block present | Art 04 §5 P26 |
| Outcome determinacy | ⚠ | `d100` with `threshold=40` set, but no structured success/successcrit/fail/failcrit split exists to check against P27 — the prose describes a binary pay/don't-pay branch, unclear if that's independent of the roll or gated by it | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Cross-resource (Mandate + Intel Token), Mandate term correctly typed — whether Intel Token qualifies as a valid fungible cost at all remains an open schema question | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

```python
DIR.PA.8 = Card(
    id      = "DIR.PA.8",  card_id = "DIR.PA.8",  version = "v1.2",
    name    = "Subpoena",
    tagline = "Weaponize target-keyed intelligence into a public audit that bleeds an opponent's finances or reputation.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Economy,  function = Remove,  subject = Capital,
    beat    = 4,  resolution = d100,  threshold = 40,
    ring_mod = None,  doctrine_mod = None,  trigger = None,
    value_rating = None,  # scaffolded, not addressed
    resolution_type = "Probabilistic",  outcome_type = None,  # scaffolded, not addressed
    persistence = Immediate,
    persistence_condition = None,  persistence_effect = None,
    target_district = None,  target_faction = faction.opponent,  target_object = None,  target_taxonomy = None,
    affinity = None,  restriction = None,
    cost    = resource.faction(Directorate).mandate * 1 + intel_token(faction=target_faction) * 1,
    boost   = None,
    success = "Target faction must pay 2 Capital or 2 of their Native Resource to the supply. If they do not, they lose 2 Public Standing.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept = None,  on_decline = None,
    portrait = {},  # scaffolded, not addressed
    ps_framing = None,
    narrative = None,  perspectives = None,
    design_note = "Cost uses a faction-keyed Intel Token: Directorate 'found out something' that justifies the legal action. The target has the choice to pay the fine or take the PR hit.",
    arbiter_note = None,
)
```

---

### DIR.PA.9 — CHARTER GRANT
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Directorate's first Territory|Add|PresenceToken card — closes the audit-flagged win-path gap (04-n89: the faction whose win condition is territorial Established status had zero native presence-placement cards). Ring-spread mechanic (1 token in target district + up to 2 same-ring-adjacent districts) matches Directorate's actual win path (breadth of Established districts, not Dominant depth) and reuses the same Permanent-counting mechanism as DIR.CA.6/CA.7.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal institutional presence-expansion act; ring-spread framing ("radiates, doesn't concentrate") matches Directorate's breadth-over-depth win path | Art 00 §7 |
| Voice fit | ⚠ | `narrative = None`, `perspectives = None` — no in-world voice content. Same gap across all 5 of this S131 batch — flagged as a uniform cluster finding, not fixed here. | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate-exclusive; closes a real, previously-audited doctrinal gap (04-n89) rather than duplicating an existing capability | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken — matches `card_status` DB directly | Art 04b §4 |
| Balance | ✓ | Mandate × 2 for 1–3 tokens depending on N; design_note reasons the ceiling is modest (N caps at 2 by board geometry) and scales naturally from Standard-equivalent (0 Permanents) to Directorate's strongest late-game expansion tool | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent token placement(s); card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate submitter=+1, single entry | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; same-ring-adjacency check via `district.adjacent(...).where(ring==...)` — valid zone condition | Art 01 §6–§7 |
| Supported by components | ✓ | presence_chip — existing component; each placement respects the 6-chip-per-district cap (`cap_check=True`, Governing Rule 8.1) | Art 02 §6 |
| Supported by game procedure | ⚠ | Design_note claims this reuses "the same counting mechanism as CA.6 Institutional Audit / CA.7 Institutional Brief" — checked directly, **true**: same `game.active_permanents(faction=, ring=)` call. That mechanism is itself unconfirmed as a general Art 03/07 procedure — this is a third confirmed instance of the same gap, now in PA phase. | Art 03 §9, §11; Governing Rule 6.1 |
| Data schema validation | ⚠ | Both `id` and `card_id` set (addresses #24). `narrative`/`perspectives` explicitly `None`, content absent. `arbiter_note = None` — unusual; every other reviewed card in this set carries at least a brief arbiter_note. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block present | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`; only `success` populated — no `game.choose_one()` or conditional branching (the `for_each`/`limit` construct iterates deterministically over a fixed board-state count, not a player choice). `outcome_type = Unilateral` present. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Mandate × 2), correctly typed. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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

### DIR.PA.10 — OFFICIAL DEMONSTRATIONS
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Public Standing counterpart to covert DIR.CA.7 Institutional Brief — closes the audit's Standing gap (04-n108: Directorate's only PS card was covert, backwards for an "on the record" faction). N = count of districts where Directorate holds Established+ tier, scaling both success and fail symmetrically — a genuine gamble (bigger claim, bigger swing in both directions) rather than a guaranteed accumulator.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public claim of institutional reach, scaled to actual board presence — fills a real, previously-audited gap (Directorate's only prior PS lever was covert) | Art 00 §7 |
| Voice fit | ⚠ | `narrative = None`, `perspectives = None` — no in-world voice content. Same gap across all 5 of this S131 batch — flagged as a uniform cluster finding, not fixed here. | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate-exclusive; scaling by Established-district count is a direct, on-doctrine measure of institutional reach | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Standing / Shift / StandingMarker — matches `card_status` DB directly | Art 04b §4 |
| Balance | ✓ | Flat threshold 50 (matches CA.2/CA.6/CA.7 precedent); cost kept cheap and mono (Mandate×2) — design_note reasons the real risk lives in the public reaction (N-scaled swing), not the resource spend | Art 02 §6–§7 |
| Effect duration | ✓ | PS shift is immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Directorate submitter=+1, single entry | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — city-wide count, no single-zone reference; N derived from existing board-visible Established/Dominant markers | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — counts existing Established markers already on board | Art 02 §6 |
| Supported by game procedure | ⚠ | Design_note claims N uses "the same counting mechanism CA.6/CA.7 use for Permanents." Checked directly: **not literally the same** — CA.6/CA.7 count active Directorate Permanent cards per ring (`game.active_permanents`), this card counts districts city-wide at Established+ tier (`district.where(influence_tier >= Established)`) — a different count entirely. The shared property is "no ARBITER judgment call, simple physical tally" (true for both), not an identical formula. Softer version of the Overture-pattern cross-card claim check — not confirmed false, but imprecisely worded. | Art 03 §9, §11; Governing Rule 6.1 |
| Data schema validation | ⚠ | Both `id` and `card_id` set (addresses #24). `narrative`/`perspectives` explicitly `None`. **`outcome_type = None`** — this is a real, confirmed instance of exactly the defect flagged as highest-priority going into the PA phase (`ca_pa_review_notes.md` §4): a PublicAct with a real dice-roll resolution and all four tiers populated should carry a real `OutcomeType`, not `None`. Likely correction: `Unilateral`, matching every sibling card in this file. Flagged, not fixed. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block present | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `d100`; all four tiers populated (success/successcrit/fail/failcrit), no `game.choose_one()` — resolves deterministically once N and the roll are known. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Mandate × 2), correctly typed. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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

### DIR.PA.11 — PUBLIC HEARING
[↑ Public Acts](#directorate-public-acts)

#### Design Rationale
Resolves the long-standing counter-card design gap for Permanent PAs (04-n142) — a standing, game-wide due-process institution letting any faction petition to remove one of Directorate's own active standing Public Acts by matching its printed cost plus 1 Intel Token. Atomic resolution (pay + prove, immediate removal) avoids the untracked-exemption-state problem an earlier draft ran into. Extends DIR.CA.8's self-inclusive "uniform scrutiny" doctrine from suppression to due process.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Standing due-process institution — closes a real, long-open counter-card gap (04-n142) for Permanent PAs generally | Art 00 §7 |
| Voice fit | ⚠ | `narrative = None`, `perspectives = None` — no in-world voice content. Same gap across all 5 of this S131 batch — flagged as a uniform cluster finding, not fixed here. | Art 00 §7 |
| Doctrine alignment | ✓ | Directorate-exclusive; design_note explicitly frames this as extending CA.8's uniform-scrutiny principle from "submits to suppression" to "regulations answer to due process" — a genuine doctrinal throughline, not asserted in isolation | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Directorate) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Submission / Remove / PublicAct — matches `card_status` DB directly | Art 04b §4 |
| Balance | ✓ | Directorate profits from every invocation (cost refund + Intel Token) regardless of who invokes it — design_note reasons this as a genuine income mechanism, not a giveaway, and nothing prevents Directorate re-declaring the removed PA later | Art 02 §6–§7 |
| Effect duration | ✓ | Permanent, no clearing condition — a standing institution once established, distinct from the other Permanent PAs it can be used against | Art 04 §5 P19 |
| Persistence | ✓ | Permanent; card-as-condition, `persistence_condition = None` deliberately (no auto-discard — a standing institution, not a conditional one) | Art 04 §6 |
| Trigger validity | ✓ | No confirmed TriggerExpr vocabulary used — `persistence_effect` is a prose-described standing institution rather than a trigger/mutation pair; consistent with "card IS the condition," not a reactive mechanism | Art 04 §6.3 |
| Portrait validity | ✓ | Directorate submitter=+1, single entry | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — game-wide scope, no single zone reference | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — cost-match is a direct read of the target PA's own printed cost | Art 02 §6 |
| Supported by game procedure | ✓ | Self-policing per Governing Rule 6.1a; cost-match is a physical lookup, not an ARBITER calculation (GR 6.1/4.7b-safe, explicitly reasoned in design_note) | Art 03 §9; Governing Rule 6.1, 6.1a |
| Data schema validation | ⚠ | Both `id` and `card_id` set (addresses #24). `narrative`/`perspectives` explicitly `None`. `resolution_type = "Permanent public act"` — not in the confirmed vocabulary, third instance in this file alongside DIR.PA.5/DIR.PA.6 — same open schema question. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79; no Card Story block present | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic`; only `success` populated (a flat PS +1 for establishing the institution) — no `game.choose_one()` or conditional branching. `outcome_type = Unilateral` present. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Mono-resource (Mandate × 2), correctly typed. | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | | |

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
    value_rating = None,  # scaffolded, not addressed
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

### DIR.MOD.1 — RIOT SQUAD

#### Design Rationale
First Directorate React (S128) — establishes the Territory\|Remove\|PresenceToken enforcement family for Directorate: three variants at increasing narrowness/strength — DIR.MOD.1 (generic, Established-gated), DIR.MOD.2 (Syndicate-targeted, same gate), DIR.MOD.3 (Ring 1-locked, no gate — strongest). Mechanically the simplest expression of "Directorate polices unauthorized expansion": any faction's presence placement in a district where Directorate holds Established+ draws an immediate, single-chip institutional response. Two open questions surfaced on genuine re-review (not carried over from the stub): the trigger's `faction=Any` scope is broader than sibling DIR.MOD.7's `opponent` scope and, as written, includes Directorate's own placements; and whether `arbiter.remove(presence_chip, ...)` can legally apply to a Deployment Marker's temporary chip (GR 8.3a — markers move, never removed). Both flagged below, not resolved here.

#### Card Story
A rival faction moves a marker onto ground the Directorate already considers under its administration. Before the ink on the placement is dry, an enforcement team already has its orders — the marker comes back off the map, and no one needed to ask permission first.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional enforcement against unauthorized presence placement fits Directorate's control/continuity doctrine directly. | Art 00 §7 |
| Voice fit | ✓ | Tagline/name read in Directorate's institutional-enforcement register. `narrative` field itself is empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1 rewards Directorate for exercising jurisdictional authority — directly expresses doctrine when played. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Directorate with real taxonomy (Territory/Remove/PresenceToken, 04-n175) — correctly classified per §6.1. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Verified against `ref_taxonomy.md`: PresenceToken's Layer is Territory; Layer×Function matrix confirms Territory×Remove valid. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Single-chip, Immediate, Established-gated — plausible on its face, but cost is an open TBD (see Resource cost positioning); can't finalize balance until 04-n178 resolves the value_rating→cost model. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate — fully resolved at trigger, no lingering marker. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Field absent from spec, same open schema question as the Ring set (implicit-default-Immediate vs. explicit line) — `schema_cleanup_log.md` item 2/D, not resolved here. | Art 04 §6.2 |
| Trigger validity | ⚠ | `presence_chip.placed(faction=X)` is confirmed TriggerExpr vocabulary (§6.3), publicly observable. But `faction=Any` (vs. DIR.MOD.7's `opponent`) means Directorate's own placements also satisfy the trigger — flagged as an open design question (bug vs. intentional self-policing reading), not fixed. | Art 04 §6.3 |
| Portrait validity | ✓ | `{Directorate: submitter=+1}` is submitter-bounded, correctly structured per P16/L178. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district`; no ring constraint, consistent with an Established-gated (not ring-gated) mechanism. | Art 01 §6–7 |
| Supported by components | ⚠ | Presence chip removal reuses the standard mechanism, but the trigger (`presence_chip.placed`, unscoped) may match a Deployment Marker's first-placement temporary chip — GR 8.3a says deployment markers are always moved, never removed. Not confirmed whether `arbiter.remove()` here can legally apply to that case. | Art 02 §6–8; GR 8.3a |
| Supported by game procedure | ✓ (contingent) | Reuses existing chip-removal behavior; no new ARBITER procedure needed once the Supported-by-components flag above is resolved. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177): `ps_framing`/`boost`/`resolution_type` now present as placeholders, not filled with real values; `cost` remains a TBD comment. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Card Story above gives a concrete event, but the in-card `narrative` prose field is still empty — narrative-writing pass still needed. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch, no `game.choose_one()`. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | `cost=None` with a TBD comment ("possibly 1 Mandate") — cannot close this row card-by-card; gated on 04-n178 (Floor Act singularity + value_rating-derived cost, whole-set decision, Andy S138). | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Presence-chip placement is common; Established-gate and single-chip yield keep the effect modest. Final read pending 04-n178. |  |
| Firing window (ModReactCard) | ⚠ | DIR.MOD.2 (Syndicate-narrowed) and DIR.MOD.3 (Ring 1, no gate) share overlapping trigger space with this card. No documented rule on whether all three fire off the same single placement event if Directorate holds the full family. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded institutional-authority action, no execution-quality dimension to model via roll. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the Ring set: does holding 2 copies double-fire on one rival placement? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct, since this variant is gated by Established status, not ring; correctly distinguishes from DIR.MOD.3 (ring-locked). |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. First Directorate React. Military-mode enforcement — institutional authority to reverse unauthorized presence placement. Generic variant (faction=Any). Faction-targeted variant: DIR.MOD.2 (Syndicate). Ring-constrained variant: DIR.MOD.3 (Ring 1 Core). S138: full content-review pass — 5 open flags (trigger self-fire scope, deployment-marker removal edge, cost/04-n178, family firing-window overlap, narrative prose absent), Design Pass ✓ (all 22 rows evaluated), Issues Resolved not yet (real flags remain open).*

```python
DIR.MOD.1 = Card(
    id      = "DIR.MOD.1",  card_id = "DIR.MOD.1",  version = "v0.1",
    name    = "Riot Squad",
    tagline = "Presence placed without Directorate approval can be removed with Directorate authority.",
    type    = ModReactCard,  faction = Directorate,
    layer   = Territory,  function = Remove,  subject = PresenceToken,  # assigned S137 (04-n175) — arbiter.remove(presence_chip,...)

    trigger         = presence_chip.placed(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema (Automatic → Transactional); not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Directorate).influence >= Established,  # jurisdictional authority requires Established presence
    cost            = None,  # card consumed; cost TBD (possibly 1 Mandate)
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=trigger.faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Military-mode enforcement React. Fires when any faction places presence in a district where Directorate has Established presence. Directorate may remove 1 chip immediately. Restriction: Directorate must be Established — jurisdictional authority is earned by presence, not proclaimed. This is the suppression toolkit delivered at React speed: Directorate responds to expansion before Beat 3 resolves. Cost TBD — possibly 1 Mandate (enforcement has institutional overhead).",
    arbiter_note = None,
)
```

---

### DIR.MOD.2 — CAPITAL SUPPRESSION

#### Design Rationale
Second card of the DIR.MOD.1/2/3 Territory\|Remove\|PresenceToken enforcement family — same mechanism as DIR.MOD.1, narrowed from `faction=Any` to `faction=Syndicate` specifically. No self-fire ambiguity here (Directorate can never trigger against itself), so that flag doesn't carry over. Two things genuinely re-examined this pass rather than assumed clean by family resemblance: (1) the added `Syndicate: PortraitEntry(flat=-1)` entry — schema-valid (per L131, `flat` is documented for faction-specific effects on non-submitting factions) but a real judgment question against Portrait Principle 11 (does Syndicate's portrait deserve to move for an action Syndicate didn't choose?); (2) `cost=None` here carries no TBD comment, unlike DIR.MOD.1's explicit "possibly 1 Mandate" flag for the *same* enforcement mechanism — an internal inconsistency worth surfacing rather than silently accepting one sibling's confidence over the other's doubt.

#### Card Story
Syndicate stakes a claim on ground Directorate already administers. The response isn't generic policing — Directorate's doctrine treats Syndicate's gray-market capital expansion as its own category of threat, and the file on Syndicate specifically is already open.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Faction-targeted institutional enforcement; design_note frames Syndicate as Directorate's primary doctrinal territorial adversary — grounded, not arbitrary narrowing. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads in Directorate's register. `narrative` field itself is empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Directorate submitter=+1 correctly expresses doctrine on play. | Art 04 §6.5 |
| Card type fit | ✓ | Same shape as DIR.MOD.1 — ModReactCard/Directorate, real taxonomy, correctly classified. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory/Remove/PresenceToken — same verified matrix cell as DIR.MOD.1. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Narrower trigger than DIR.MOD.1 (Syndicate-only), so lower frequency — plausible, but final read gated on 04-n178 like the rest of the family. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as DIR.MOD.1 (`schema_cleanup_log.md` item 2/D). | Art 04 §6.2 |
| Trigger validity | ✓ | `presence_chip.placed(faction=Syndicate)` — confirmed vocabulary, explicitly scoped, no self-fire ambiguity (Directorate ≠ Syndicate). | Art 04 §6.3 |
| Portrait validity | ⚠ | `{Directorate: submitter=+1}` is fine. `{Syndicate: flat=-1}` is schema-valid (L131 permits `flat` on a named non-submitting faction) but is a genuine design question: Principle 11 ties Portrait movement to an action that strongly expresses *that faction's own* doctrine — here the action is Directorate's, and Syndicate's portrait moves as a consequence, not a choice. Flagged for Andy: intentional "consequences imposed on you move your portrait" pattern, or should target-faction portrait entries require the target's own agency? Logged as a schema-normalization candidate (`schema_cleanup_log.md`). | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same as DIR.MOD.1. | Art 01 §6–7 |
| Supported by components | ⚠ | Same deployment-marker-removal edge as DIR.MOD.1 (GR 8.3a) — family-wide flag, not re-derived per card. | Art 02 §6–8; GR 8.3a |
| Supported by game procedure | ✓ (contingent) | Same as DIR.MOD.1. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177) — placeholders only. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | `cost=None`, no TBD comment — inconsistent with DIR.MOD.1's explicit doubt on the identical mechanism. Both gated on 04-n178; the inconsistency itself is worth flagging so the eventual cost model applies uniformly across the family. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Syndicate-only scope keeps frequency lower than DIR.MOD.1's generic trigger. |  |
| Firing window (ModReactCard) | ⚠ | Same family-overlap flag as DIR.MOD.1 — no documented rule for simultaneous fire if Directorate holds the full 1/2/3 set. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same as DIR.MOD.1. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as DIR.MOD.1. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; this variant is gated by faction identity, not ring. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. Faction-targeted variant of DIR.MOD.1. Trigger narrowed to Syndicate presence placement. Syndicate's capital-driven territorial expansion is Directorate's primary doctrinal adversary in Ring 1/2. S138: full content-review pass — 4 open flags (Syndicate portrait-on-target question, cost-flag inconsistency vs. DIR.MOD.1, deployment-marker removal edge, family firing-window overlap), Design Pass ✓, Issues Resolved not yet.*

```python
DIR.MOD.2 = Card(
    id      = "DIR.MOD.2",  card_id = "DIR.MOD.2",  version = "v0.1",
    name    = "Capital Suppression",
    tagline = "Syndicate presence in regulated territory draws immediate institutional response.",
    type    = ModReactCard,  faction = Directorate,
    layer   = Territory,  function = Remove,  subject = PresenceToken,  # assigned S137 (04-n175), same shape as DIR.MOD.1

    trigger         = presence_chip.placed(faction=Syndicate),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = Syndicate,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Directorate).influence >= Established,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=Syndicate, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1), Syndicate: PortraitEntry(flat=-1)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Syndicate-targeted variant of DIR.MOD.1. Directorate's doctrine makes no distinction between rogue capital and rogue information — Syndicate's gray-market acquisitions are the same institutional threat as Network's broadcasts. Syndicate portrait flat=-1 on fire: the Syndicate's response to having presence removed is public and traceable. Narrower trigger window than generic; reliable in SYN-heavy games.",
    arbiter_note = None,
)
```

---

### DIR.MOD.3 — CITY COUNCIL LOYALIST

#### Design Rationale
Third and strongest card of the DIR.MOD.1/2/3 family — Ring 1 (Core)-locked, and unlike its siblings carries *no* restriction at all: Directorate doesn't even need Established presence to fire. The design_note's justification (Core is institutional home territory; authority there is structural, not earned) is coherent doctrine, but it also means this variant carries DIR.MOD.1's `faction=Any` self-fire ambiguity (`schema_cleanup_log.md` item 5) with the *least* friction of the three — no restriction to even incidentally gate a Directorate self-trigger. Flagged, not fixed, same as DIR.MOD.1.

#### Card Story
In the Core, nobody double-checks Directorate's paperwork. A rival plants a marker in the shadow of the Citadel; the response is already moving before the district tile finishes settling.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Unrestricted home-territory authority is a coherent, distinct escalation from DIR.MOD.1/2 — not a redundant reprint. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("does not require a justification") lands the doctrine cleanly. `narrative` field itself empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1; correctly expresses "Core is structural, not earned" doctrine framing. | Art 04 §6.5 |
| Card type fit | ✓ | Same shape as DIR.MOD.1/2. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory/Remove/PresenceToken — same verified matrix cell. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Strongest of the family (no restriction) — reasonable given Ring-lock narrows scope to Core only, but final read gated on 04-n178 like its siblings; also the one most exposed if the `faction=Any` self-fire question (Item 5) turns out to be a real bug, since there's no restriction to incidentally soften it. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as DIR.MOD.1/2. | Art 04 §6.2 |
| Trigger validity | ⚠ | Same `faction=Any` scope question as DIR.MOD.1 (`schema_cleanup_log.md` item 5) — carried here rather than re-derived, but flagged as the sharper instance since no `restriction` softens it. | Art 04 §6.3 |
| Portrait validity | ✓ | `{Directorate: submitter=+1}` only — no target-faction entry, so DIR.MOD.2's Item 7 question doesn't apply here. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `ring_constraint=1` matches trigger's `ring=1` scope; consistent. | Art 01 §6–7 |
| Supported by components | ⚠ | Same deployment-marker-removal edge as DIR.MOD.1/2 (GR 8.3a) — family-wide flag. | Art 02 §6–8; GR 8.3a |
| Supported by game procedure | ✓ (contingent) | Same as siblings. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177) — placeholders only. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | `cost=None`, no TBD note — same family inconsistency flagged at DIR.MOD.2 (DIR.MOD.1 flags doubt on the identical mechanism, 2/3 don't). Gated on 04-n178. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ⚠ | Ring-locked to Core (fewer districts, but institutionally dense — Core is where most factions eventually push). Combined with no restriction, this may be the highest-frequency card in the family; final read pending 04-n178. |  |
| Firing window (ModReactCard) | ⚠ | Same family-overlap flag as DIR.MOD.1/2 — if a Core placement also satisfies DIR.MOD.1's generic trigger, no documented rule on whether both fire. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same as siblings. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as DIR.MOD.1/2. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=1` correctly matches trigger scope; distinguishes this as the ring-locked family member. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. Ring-constrained variant of DIR.MOD.1. Ring 1 (Core) only. No Established restriction — Directorate has blanket institutional authority in Core ring regardless of presence level. S138: full content-review pass — carries DIR.MOD.1's self-fire and deployment-marker flags plus a frequency flag specific to being both unrestricted and Ring 1-locked; Design Pass ✓, Issues Resolved not yet.*

```python
DIR.MOD.3 = Card(
    id      = "DIR.MOD.3",  card_id = "DIR.MOD.3",  version = "v0.1",
    name    = "City Council Loyalist",
    tagline = "In the Core, the Directorate's authority does not require a justification.",
    type    = ModReactCard,  faction = Directorate,
    layer   = Territory,  function = Remove,  subject = PresenceToken,  # assigned S137 (04-n175), same shape as DIR.MOD.1

    trigger         = presence_chip.placed(faction=Any, ring=1),
    beat            = None,
    ring_constraint = 1,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,  # Core ring: no Established requirement — blanket institutional authority
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.remove(presence_chip, district=trigger.district, faction=trigger.faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Ring 1–constrained variant of DIR.MOD.1. Core ring is institutional home territory — Directorate removes presence without needing Established status. Reflects doctrine: Directorate's authority in the Core is structural, not earned faction by faction. Strongest DIR enforcement React — no restriction to work around.",
    arbiter_note = None,
)
```

---

### DIR.MOD.4 — ADMINISTRATIVE OVERHEAD

#### Design Rationale
First card of a second Directorate family (Economy\|Add\|NativeResource), paired with DIR.MOD.5. Simpler than the enforcement family: no self-fire ambiguity (`accord.placed` isn't faction-scoped the way `presence_chip.placed` is), no restriction, flat +1 Mandate on any Accord forming anywhere. Checked directly against §4.16/GR 9.1 (income generation is untouchable) since "Directorate gets Mandate from other factions' activity" reads adjacent to that rule on a skim — confirmed not a violation: §4.16 protects the Upkeep presence/structure income mechanism specifically; this is a one-time event-triggered grant, same structural category as the many other Economy\|Add ModReactCards already shipped (Ring set, Guild's Capacity-yield cards). Real open question is reliability, not legality: Accord formation frequency is entirely player-driven and could be zero in a low-negotiation game, which the Balance/Trigger-frequency rows flag rather than resolve.

#### Card Story
Two factions shake hands on an Accord. Before the ink dries, a Directorate clerk has already logged it, stamped it, and billed the filing fee — not to either party, just to the general fund.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Bureaucratic rent-seeking on diplomatic activity is a grounded, distinct Directorate income lever — doesn't overlap DIR.MOD.5's shape (permanent-PA-triggered, not Accord-triggered). | Art 00 §7 |
| Voice fit | ✓ | Tagline reads as institutional overhead, not favoritism. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1; Directorate's continuity/control doctrine extends naturally to "we tax the paperwork." | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Directorate, real taxonomy (Economy/Add/NativeResource, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | NativeResource's typical Layer is Economy; Layer×Function matrix confirms Economy×Add valid. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Flat, low-value (+1), no cost — plausible as a minor economic engine, but frequency is entirely dependent on other factions' Accord activity (could be zero in a quiet game). Final read pending 04-n178 alongside the rest of the set. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the enforcement family. | Art 04 §6.2 |
| Trigger validity | ✓ | `accord.placed` is confirmed TriggerExpr vocabulary (§6.3), publicly observable, no faction-scoping ambiguity (unscoped by design — fires on any Accord). | Art 04 §6.3 |
| Portrait validity | ✓ | `{Directorate: submitter=+1}` — submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; Accords have no district dimension. | Art 01 §6–7 |
| Supported by components | ✓ | `faction(Directorate).resources.add()` reuses the standard resource-grant mechanism; no component conflict (unlike the enforcement family's marker-removal edge). | Art 02 §6–8 |
| Supported by game procedure | ✓ | No novel procedure — Accord formation is already a defined board event. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177) — placeholders only. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — plausible for a low-value passive-style engine card, but the eventual Floor Act/value_rating decision (04-n178) determines whether any non-Floor-Act card can carry `cost=None`, this one included. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ⚠ | Entirely dependent on Accord-formation rate, which is player-driven and not guaranteed — genuinely variable, not a design flaw, but worth tracking in playtest. |  |
| Firing window (ModReactCard) | ✓ | No other Directorate card shares this trigger; no overlap with the enforcement family. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat administrative fee, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the set: does holding 2 copies double the yield on one Accord? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; Accords aren't ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. Legislative-mode React. Directorate documents all new Accords — procedural overhead yields Mandate income. S138: full content-review pass — checked against GR 9.1/§4.16 (income generation untouchable), confirmed not a violation (event-triggered grant, not Upkeep income modification); open flags are frequency-reliability and the standard schema/cost/stack gaps shared across the set. Design Pass ✓, Issues Resolved not yet.*

```python
DIR.MOD.4 = Card(
    id      = "DIR.MOD.4",  card_id = "DIR.MOD.4",  version = "v0.1",
    name    = "Administrative Overhead",
    tagline = "Every Accord formed is a Directorate administrative event.",
    type    = ModReactCard,  faction = Directorate,
    layer   = Economy,  function = Add,  subject = NativeResource,  # assigned S137 (04-n175) — resources.add(1, Mandate)

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

    success     = faction(Directorate).resources.add(1, Mandate),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Legislative-mode React on accord.placed. Directorate charges institutional overhead for registering diplomatic agreements — Mandate income regardless of which factions are party to the Accord.",
    arbiter_note = None,
)
```

---

### DIR.MOD.5 — EMERGENCY APPROPRIATION

#### Design Rationale
Second Economy\|Add\|NativeResource card, self-referential by design (unlike DIR.MOD.1's accidental-looking self-fire): `trigger = public_act.placed_on_frg(faction=Directorate, persistence=Permanent)` explicitly names Directorate, so this is a deliberate rebate mechanic, not an ambiguity. Checked for exploitability: this only fires on Directorate's own Permanent PA placements, which are inherently rare/bounded (limited card pool, each with its own real cost) rather than a spammable loop — reads as a genuine subsidy for a documented pain point (design_note calls out "crippling Q1/Q2 cost"), not a balance escape hatch. `portrait = {}` (empty dict, not `None`) — flagged as a minor cross-set schema inconsistency (`schema_cleanup_log.md` item 8), not a defect in this card specifically.

#### Card Story
Directorate commits to a standing policy — the kind that costs real institutional capital to establish. The same session it goes into effect, an emergency appropriation quietly covers part of the bill.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Self-subsidy tied to Directorate's own costly commitment is a coherent "institutional scale needs institutional funding" beat, distinct from DIR.MOD.4's Accord-tax shape. | Art 00 §7 |
| Voice fit | ✓ | Tagline lands the doctrine. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — no entry at all, correctly justified: this is Directorate subsidizing its own already-doctrinal action, nothing new is being expressed about doctrine at the moment of the subsidy itself. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Directorate, real taxonomy (Economy/Add/NativeResource, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Economy×Add cell as DIR.MOD.4. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | Checked for exploit potential: fires only on Directorate's own Permanent PA placements, inherently rare and individually costly — a rebate, not a loop. Reasonable as specced. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate — the subsidy itself resolves once; the triggering PA's own Permanent persistence is a separate card's property. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the set. | Art 04 §6.2 |
| Trigger validity | ✓ | `public_act.placed_on_frg(faction=Directorate, persistence=Permanent)` — confirmed vocabulary (§6.3), explicitly self-scoped by design, no ambiguity. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified — no faction's doctrine is freshly expressed by the subsidy firing (the doctrinal weight is already carried by the underlying Permanent PA). | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; this reacts to an FRG placement, not a district event. | Art 01 §6–7 |
| Supported by components | ✓ | Standard resource-grant mechanism, no component conflict. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses the existing §9.2 Public Declaration/FRG-placement event; no new ARBITER procedure. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177) — placeholders only. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same as DIR.MOD.4, awaiting the whole-set Floor Act/value_rating decision before any non-Floor-Act card's `cost=None` can be confirmed correct. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ | Bounded by how many Permanent PAs Directorate ever places — inherently low-frequency, matching the "rare subsidy" design intent. |  |
| Firing window (ModReactCard) | ✓ | No other Directorate card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat subsidy, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the set: 2 copies → double subsidy per Permanent PA placed? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not a district-scoped effect. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*React to subsidize the heavy Mandate cost of Permanent PAs. S138: full content-review pass — checked for exploit potential (none found; bounded by Permanent PA scarcity), `portrait={}` cross-set inconsistency flagged to schema_cleanup_log.md item 8, remaining flags are the standard schema/cost/stack gaps shared across the set. Design Pass ✓, Issues Resolved not yet.*

```python
DIR.MOD.5 = Card(
    id      = "DIR.MOD.5",  card_id = "DIR.MOD.5",  version = "v0.1",
    name    = "Emergency Appropriation",
    tagline = "Institutional scale requires institutional funding.",
    type    = ModReactCard,  faction = Directorate,
    layer   = Economy,  function = Add,  subject = NativeResource,  # assigned S137 (04-n175), same shape as DIR.MOD.4

    trigger         = public_act.placed_on_frg(faction=Directorate, persistence=Permanent),
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

    success     = faction(Directorate).resources.add(2, Mandate),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Economy fixer. Triggers when Directorate places a Permanent Public Act on their Faction Resolution Grid at Phase 9.2 (before resolution). Instantly yields 2 Mandate, subsidizing the crippling Q1/Q2 cost of laying down their win-condition standing condition PAs.",
    arbiter_note = None,
)
```

---

### DIR.MOD.6 — STATE OF EMERGENCY

#### Design Rationale
A "law" card in the sense confirmed by Andy (S138): a Seasonal standing condition that impacts every opponent broadly, not a specific faction/district — the appropriate shape for a card triggered by a World Event affecting the whole table. Two hard blockers carried from the stub and reconfirmed, not resolved, this pass: (1) `world_event.played` is confirmed TriggerExpr vocabulary, but its real-world frequency is unknowable until Broadcast Card/World Event content exists (XA-54) — the card's Balance/Trigger-frequency rows can't close until then; (2) `success` is a string literal, not a real MutationExpr — the card needs full re-authoring against the current schema when XA-54 unblocks it, not just a taxonomy tag. New finding this pass: `portrait = {}` looks wrong given this is arguably the single strongest doctrinal expression in the whole Directorate ModReactCard set (declaring emergency powers) — flagged below, distinct from DIR.MOD.5's justified-empty case.

#### Card Story
A World Event breaks — a crisis wide enough that no faction's business-as-usual survives it. Directorate doesn't wait for consensus. Within the hour, an emergency order is already shaping how everyone else has to operate.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Directorate declaring a broad emergency constraint off a World Event matches the confirmed principle (S138): standing-condition "law" cards may legitimately affect everybody, unlike Immediate-effect cards which should target specifically. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("the Directorate dictates how") reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ⚠ | `portrait = {}` — no entry. This looks like the wrong call: this is arguably the strongest single doctrinal expression in the set (invoking emergency powers table-wide), and Principle 11 exists precisely for actions that *strongly* express a faction's doctrine. Distinct from DIR.MOD.5's justified-empty case. Flag: should carry at least `{Directorate: submitter=+1}`. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Directorate, `persistence=Seasonal` correctly using the confirmed card-as-standing-condition-on-FRG pattern (04-n145). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Submission/Modify/PublicAct — re-derived directly against DIR.PA.1 rather than assumed (S137); confirmed against the matrix (Submission×Modify valid). Reasoning holds up on re-check. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ (blocked — XA-54) | −10 to any qualifying opponent PA is significant, partially offset by a real Mandate+Exposure cost, but frequency is entirely unknown until Broadcast Card/World Event content exists. Cannot close. | Art 02 §6–7; Art 04 §6.5; PM05 XA-54 |
| Effect duration | ✓ | `persistence = Seasonal` correctly typed for "remains until Quarter end." | Art 04 §5 P19 |
| Persistence | ✓ | Unlike the rest of the set, this card *does* specify `persistence` explicitly and correctly (Seasonal) — not part of the deferred-field gap. | Art 04 §6.2 |
| Trigger validity | ⚠ (blocked — XA-54) | `world_event.played` is confirmed §6.3 vocabulary as a term, but ungrounded — no Broadcast Card taxonomy exists yet to define what qualifies as a "World Event" or how often one occurs. | Art 04 §6.3; PM05 XA-54 |
| Portrait validity | ⚠ | See Doctrine alignment row — same finding, `{}` likely wrong for this card specifically. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; this is a global effect, not district-scoped, matching the "law" framing. | Art 01 §6–7 |
| Supported by components | ✓ | Card-as-condition on FRG, no separate marker needed — reuses the confirmed Seasonal pattern. | Art 02 §6–8 |
| Supported by game procedure | ⚠ (blocked — XA-54) | Depends on a World Event/Broadcast Card reveal procedure that doesn't fully exist; XA-54 also flags the open question of whether "Emergency" should be a formal Broadcast Card subtype (rare, high-narrative-specificity) or any World Event qualifies (fires every Situation Report phase) — a balance-relevant procedural gap, not just content. | Art 03; GR 6.1; PM05 XA-54 |
| Data schema validation | ⚠ | Two distinct issues: (1) scaffolding placeholders added this session (04-n177), same as the rest of the set; (2) `success` is a string literal, not a real MutationExpr — confirmed still true on re-check, needs full re-authoring once XA-54 unblocks. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single branch (establishes a standing condition) — the *effect* the standing condition applies isn't itself probabilistic. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (blocked — XA-54) | Cost is specified (Mandate+Exposure, not the 04-n178 Floor-Act gate this time) — but whether the cost is positioned correctly can't be judged without knowing trigger frequency. | Art 00a §9.2; PM05 XA-54 |
| Trigger frequency (ModReactCard) | ⚠ (blocked — XA-54) | Entirely dependent on undesigned Broadcast Card/World Event content — could be common or vanishingly rare. Cannot close. |  |
| Firing window (ModReactCard) | ✓ | No other Directorate card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Establishing a standing condition is binary; no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | More complex than the rest of the set: since this creates a Seasonal standing condition rather than firing-and-consuming, does a 2nd copy stack a further −10, or is it wasted once the condition already exists? Undocumented, and a sharper question than the generic "2 copies" flag elsewhere. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; global effect, not ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*Creates a standing global difficulty constraint triggered by a World Event. S138: full content-review pass — every row evaluated (Design Pass ✓), but this card cannot reach Issues Resolved this session: `world_event.played` trigger frequency depends entirely on undesigned Broadcast Card taxonomy (XA-54, blocks Balance/Trigger frequency/Supported-by-procedure/Resource-cost-positioning), `success` remains a string literal needing full re-authoring, and `portrait={}` is newly flagged as likely wrong for this specific card (should carry a submitter entry). Taxonomy re-derivation from S137 (checked against DIR.PA.1 directly, not assumed) holds up on re-check.*

```python
DIR.MOD.6 = Card(
    id      = "DIR.MOD.6",  card_id = "DIR.MOD.6",  version = "v0.1",
    name    = "State of Emergency",
    tagline = "The world changes. The Directorate dictates how.",
    type    = ModReactCard,  faction = Directorate,
    layer   = Submission,  function = Modify,  subject = PublicAct,  # assigned S137 (04-n175) — see note above; NOT Territory/Modify/PresenceToken (that's DIR.PA.1's shape, not this card's)

    trigger         = world_event.played,
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    persistence     = Seasonal,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Directorate).mandate * 1 + resource.faction(Directorate).exposure * 1,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = "Card remains in play (persistence=Seasonal) on Directorate FRG. While in play, any opponent Public Act targeting a district where Directorate influence is >= Established suffers boost=-10.",
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Environmental shaping. Triggers when the Arbiter reveals a World Event. The ModReactCard itself is placed face-up on the Directorate's Faction Resolution Grid as a standing condition for the rest of the Quarter. It imposes a -10 difficulty penalty on any opponent PA that targets a district where Directorate is Established or higher. Solves the 'world event extension' gap by letting Directorate piggyback on the World Event phase to declare their own global environmental constraint. Legally escapes Art 00a §9.1 because it modifies action difficulty (9.1a), not resource income Cost reasoning: Exposure represents the widespread public broadcast necessary to enforce an emergency lockdown. ⚠ XA-54: 'world_event.played' assumes 'World Event' is either a defined Broadcast Card subtype or a synonym for all Broadcast Cards — Broadcast Card design is open; trigger frequency depends entirely on how many World Events exist in the Broadcast Deck.",
    arbiter_note = None,
)
```

---

### DIR.MOD.7 — EMINENT DOMAIN

#### Design Rationale
Second Territory\|Add\|PresenceToken card (the Ring set's STD.MOD.98 cites this card as its own precedent — confirmed on re-check, the shapes match). Unlike the DIR.MOD.1/2/3 enforcement family, this one has no restriction and no cost at all, and fires on *any* opponent structure placement, *anywhere* — the design_note's own "win-condition engine" framing is accurate, and on this pass that reads as a genuine balance concern worth flagging on its own terms, not just deferring to 04-n178: structures are placed regularly across all four other factions, so this is likely one of the highest-frequency, lowest-friction cards in the entire Directorate ModReactCard set.

#### Card Story
A rival breaks ground on a structure — permanent, visible, load-bearing. Before the concrete sets, Directorate's jurisdictional oversight has already staked its own claim in the same district, free of charge.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Claiming jurisdictional oversight over new construction is a clean, doctrinally grounded expression of institutional authority. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ⚠ | `portrait = {}` — no entry, but the design_note explicitly frames this as a "win-condition engine" (passive path to Established-in-more-districts). That's a meaningfully doctrinal outcome, softer flag than DIR.MOD.6 but worth the same question: should recurring, strategically significant doctrine-aligned actions carry a portrait entry, or is routine/automatic execution enough to justify `{}`? | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Directorate, real taxonomy (Territory/Add/PresenceToken, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Confirmed as the Ring set's own STD.MOD.98 precedent (04-n175 note) — verified on re-check, not just cited. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | No restriction, no cost, fires on any opponent's structure placement anywhere on the board — the strongest, least-gated card reviewed in this set so far. "Win-condition engine" per its own design_note is not an exaggeration. Flag for real balance attention (not just the generic 04-n178 cost question) — consider whether a restriction (e.g., Established-gate, like the enforcement family) or a ring/frequency limiter belongs here. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the set. | Art 04 §6.2 |
| Trigger validity | ✓ | `structure_block.placed(faction=opponent)` — confirmed vocabulary, correctly opponent-scoped (no self-fire ambiguity, unlike DIR.MOD.1/3). | Art 04 §6.3 |
| Portrait validity | ⚠ | Same question as Doctrine alignment row above. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district` — correct; also naturally excludes Chorus Node since no structures are ever placed there (GR 8.1a), so no special-case needed. | Art 01 §6–7 |
| Supported by components | ✓ | Standard chip-placement mechanism; GR 8.1's 6-chip cap is a generally enforced constraint across all presence-adding cards, not a gap specific to this one. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing structure-placement event and chip-placement mechanism; no new procedure needed. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177) — placeholders only. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | `cost=None` — same 04-n178 gate as the rest of the set, but this card is the strongest candidate for actually needing a real (non-Floor-Act) cost given the Balance flag above. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ⚠ | Structure placement is a common, recurring board event across all 4 other factions — likely the highest-frequency trigger reviewed in this set. Ties directly into the Balance flag. |  |
| Firing window (ModReactCard) | ✓ | No other Directorate card in this set shares this trigger (cross-deck collision against Ring/other-faction content not checked — out of this batch's scope, matching the Ring template's own precedent). |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary claim — no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the set: 2 copies → 2 chips per opponent structure placement? Undocumented, and more balance-relevant here than elsewhere given the Balance flag. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; fires table-wide by design. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*Jurisdictional claim over private development. S138: full content-review pass — confirmed as STD.MOD.98's cited precedent; primary open flag is Balance/Trigger-frequency (no restriction, no cost, fires on any opponent structure placement table-wide — the least-gated card in the set, genuinely worth a design decision beyond the generic 04-n178 cost question). Design Pass ✓, Issues Resolved not yet.*

```python
DIR.MOD.7 = Card(
    id      = "DIR.MOD.7",  card_id = "DIR.MOD.7",  version = "v0.1",
    name    = "Eminent Domain",
    tagline = "Private development is subject to institutional oversight.",
    type    = ModReactCard,  faction = Directorate,
    layer   = Territory,  function = Add,  subject = PresenceToken,  # assigned S137 (04-n175) — arbiter.place(presence_chip,...); this is the card the Ring set's STD.MOD.98 already cites as its own precedent

    trigger         = structure_block.placed(faction=opponent),
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
    restriction     = None,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.place(presence_chip, district=target_district, faction=Directorate, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Win-condition engine. Whenever an opponent builds a structure, Directorate immediately claims jurisdictional oversight, placing a presence chip in that district for free. Helps Directorate passively achieve 'Established in more districts'.",
    arbiter_note = None,
)
```

---

### DIR.MOD.8 — ASSET SEIZURE

#### Design Rationale
First Submission-layer card in the set — interferes with an already-submitted PA rather than a board-state event. Checked directly against the Private Information Gate (00a §10.1): the PA is public on the FRG at the point this fires, so this doesn't reach into any faction's private domain. Checked against Art 04 §5 P20 (actions proceed with whatever's committed; shortfalls carry consequences): removing 1 resource from an already-submitted PA before Beat 4 is exactly the shortfall case P20 already governs — the card's own design_note description (target must replace the resource or suffer partial-payment failure) is an application of an existing rule, not a new mechanic invented ad hoc. One new finding: the trigger's `target_district=where(faction(Directorate).influence >= Established)` uses a `where(...)` conditional wrapper that isn't in §6.3's confirmed parameter forms — flagged to `schema_cleanup_log.md` (item 9), not resolved here.

#### Card Story
A faction declares a public act in territory Directorate already runs. Before Beat 4, an audit team has already impounded one of the resources sitting on the card — not confiscated for Directorate's own coffers, just pulled from circulation. The faction can make up the difference, or eat the shortfall.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Bureaucratic taxation on public acts in Directorate-administered territory is a clean, grounded expression of institutional oversight. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — routine bureaucratic action, not a strong doctrinal statement; empty is justified here (unlike DIR.MOD.6/7's stronger doctrinal actions). | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Directorate, real taxonomy (Submission/Remove/NativeResource, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Impounds a resource off an already-submitted PA — Submission (interferes with submission), not plain Economy; matrix confirms Submission×Remove valid. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | Costs 2 resources (Mandate+Capital) to remove 1 from an opponent's submitted PA — roughly symmetric, not an obvious exploit. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the set. | Art 04 §6.2 |
| Trigger validity | ⚠ | Event itself (`public_act.placed_on_frg`) is confirmed vocabulary, but the `target_district=where(...)` conditional wrapper isn't a confirmed §6.3 parameter form — flagged as a vocabulary gap (`schema_cleanup_log.md` item 9), not a card defect. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Condition is district-scoped via the Directorate-Established filter; consistent with existing zone model. | Art 01 §6–7 |
| Supported by components | ✓ | Resource-token removal off a submitted card reuses the standard payment/submission mechanism; correctly routes to Reservoir (corrected S137), not Directorate income — checked against GR 9.1/§4.16, not a violation. | Art 02 §6–8; GR 9.1 |
| Supported by game procedure | ✓ | Reuses the existing §9.2 FRG-placement event and Beat 4 payment/shortfall procedure (P20) — no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177) — placeholders only. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Real cost specified (Mandate+Capital), not gated on 04-n178 the way the cost-less cards are; reasoning (Capital mobilizes seizure teams, Mandate authorizes it) is sound. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Fires whenever any PA targets a Directorate-Established district — moderate, bounded by how much territory Directorate holds. |  |
| Firing window (ModReactCard) | ✓ | No other Directorate card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat impoundment, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the set: 2 copies → 2 resources impounded per qualifying PA? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; gated by Directorate's Established territory, not a fixed ring. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*Impounds public operational funds in Established territory. S138: full content-review pass — checked against the Private Information Gate (00a §10.1) and Art 04 §5 P20 (shortfall handling), both hold up; new finding is the unconfirmed `where(...)` trigger parameterization (schema_cleanup_log.md item 9). This is the strongest-closing card in the set so far — only the standard deferred-schema and stack-behavior flags remain. Design Pass ✓, Issues Resolved not yet.*

```python
DIR.MOD.8 = Card(
    id      = "DIR.MOD.8",  card_id = "DIR.MOD.8",  version = "v0.1",
    name    = "Asset Seizure",
    tagline = "Unlicensed public operations are subject to immediate fines.",
    type    = ModReactCard,  faction = Directorate,
    layer   = Submission,  function = Remove,  subject = NativeResource,  # assigned S137 (04-n175) — impounds a resource off an already-submitted PA; Submission (interferes with a submitted card), not plain Economy

    trigger         = public_act.placed_on_frg(target_district=where(faction(Directorate).influence >= Established)),
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
    cost            = resource.faction(Directorate).mandate * 1 + resource.faction(Directorate).capital * 1,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.remove(resource_token, target=trigger.card, count=1, to=Reservoir),  # corrected S137 (Andy): impounded resource goes to Reservoir, not to Directorate — this is not income for the submitter
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Bureaucratic taxation. Triggers when a PA is placed on the FRG targeting a Directorate-Established district. Directorate instantly impounds 1 resource token off the card, returned to the Reservoir — not claimed as Directorate income. The acting faction must either add a replacement resource before Beat 4, or suffer partial-payment failure. Cost reasoning: Requires Capital to mobilize the physical impoundment teams while Mandate authorizes the seizure.",
    arbiter_note = None,
)
```

---

### DIR.MOD.9 — FISCAL SANCTION

#### Design Rationale
The most structurally novel card in the set — first Permanent-persistence ModReactCard, combining the card-as-condition pattern with a clearing fine. Four real, unresolved questions surfaced on this pass, none fixed here: (1) `persistence_effect` blocks *all* Public Act submission from the sanctioned faction — Design Pillar 4.8c states the Floor Act is always available and cannot be blocked; a total PA lock appears to cross that line, and this needs a design decision (does "blocked" implicitly exempt the Floor Act, or does this card's scope need narrowing to a taxonomy the way PA.6 Standing Injunction does?) before this card can be considered resolved. (2) This card is one of the 4 examples under the still-open schema question (`schema_cleanup_log.md` item 2/B) of how to encode "what clears a standing condition" — `persistence_condition` is being used to express an event (the fine being paid), not the continuously-evaluated state predicate the field is typed for. (3) `cost = intel_token(...)` — flagged to `schema_cleanup_log.md` item 10: is an Intel Token a valid "fungible resource" per the cost field's own constraint? (4) `trigger = standing_marker.decreased(faction=Any)` carries the same self-fire ambiguity as DIR.MOD.1, but here the consequence (sanctioning yourself) is actively harmful rather than a no-op — flagged to item 11.

#### Card Story
A rival's Public Standing craters — bad press, a broken promise, doesn't matter which. Directorate already has a token on file. The sanction goes up within the hour: pay the fine, or nothing you declare in public reaches the table.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Opportunistic institutional sanction off a rival's public misstep is a grounded Directorate beat, distinct from the enforcement family's territorial focus. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("the public already turned on them") lands the doctrine. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `{Directorate: submitter=+1}` — submitter-bounded, correctly expresses doctrine on play. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Directorate, `persistence=Permanent` — correctly typed for the card-as-condition pattern. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Submission/Block/PublicAct — Andy-confirmed (S137): dominant identity is blocking PA submission, the +1 PS is secondary. Matrix confirms Submission×Block valid. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Cannot close: severity depends directly on the 4.8c question below (a total PA lock is far more severe than a Floor-Act-exempted one) and on the self-fire question (item 11) — both need resolution before this row can be assessed. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | `persistence=Permanent` correctly typed for an explicit-clearing-condition card. | Art 04 §5 P19 |
| Persistence | ⚠ | One of the 4 examples under the open schema question (`schema_cleanup_log.md` item 2/B): `persistence_condition` is written as an event (the fine being paid) rather than the continuously-evaluated `BoolExpr` the field is typed for. Not a card defect — a real schema gap, already logged, awaiting Andy's whole-landscape call. | Art 04 §6.2; schema_cleanup_log.md item 2 |
| Trigger validity | ⚠ | `standing_marker.decreased(faction=Any)` is confirmed vocabulary, but `faction=Any` includes Directorate's own PS drops — same category as DIR.MOD.1 (item 5) but sharper here: firing against Directorate itself would be self-harmful (blocks its own PA channel), not just a no-op. Flagged to item 11. | Art 04 §6.3 |
| Portrait validity | ✓ | `{Directorate: submitter=+1}` justified — opening a sanction is a deliberate, doctrinally-loaded choice (distinct from the Standard-card portrait-absence convention). | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; this isn't a district-scoped effect. | Art 01 §6–7 |
| Supported by components | ✓ | Intel Token consumption and standing-marker reaction both reuse existing components; no new component needed. | Art 02 §6–8 |
| Supported by game procedure | ⚠ | **Real flag (not resolved here):** `persistence_effect = PublicAct(submitter=trigger.faction).blocked_at(phase_b)` blocks *all* PA submission from the sanctioned faction. Design Pillar 4.8c: the Floor Act is always available and cannot be blocked. A total lock appears to conflict with this HARD rule — needs a design decision (implicit Floor Act exemption vs. narrowing this card's scope) before Issues Resolved can close. | Art 03; GR 6.1; Design Pillar 4.8c |
| Data schema validation | ⚠ | Two issues: (1) scaffolding placeholders added this session (04-n177); (2) `cost = intel_token(...)` — flagged to item 10 (is an Intel Token a valid "fungible resource" per the cost field's constraint?). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Real cost specified (Intel Token, not the 04-n178 Floor-Act gate) — but see item 10 on whether the cost *type* itself is schema-valid. | Art 00a §9.2; schema_cleanup_log.md item 10 |
| Trigger frequency (ModReactCard) | ⚠ | PS drift alone (above-13 Quarter-end decay) means `standing_marker.decreased` fires regularly for any faction sitting above Neutral — potentially high-frequency, gated only by holding a matching Intel token. Ties directly into the Balance flag. |  |
| Firing window (ModReactCard) | ✓ | No other Directorate card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Binary sanction-opening, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Since this creates a Permanent standing condition (not fire-and-consume), does a 2nd copy targeting the same faction do anything, or targeting a different faction simultaneously? More consequential here than the set's generic stack question given the severity of the effect. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S131. Reactive React on any faction's Public Standing decrease — Directorate spends a matching, non-Expired Intel token (the payoff for holding tokens from DIR.PA.2 Convene an Inquiry, or any other source) to open a formal sanction. Fills a genuine gap: Directorate previously had zero Economy\|Remove cards. Closes the last 1 of 6 toward the 54-card floor (04-n149). First Permanent-persistence ModReactCard in the set — new combination of two individually-established patterns, flagged in design_note rather than assumed to need a fresh Art 03 procedure. S138: full content-review pass — 4 real open flags, most severe of the set: possible Design Pillar 4.8c conflict (total PA block vs. Floor Act always available), open schema question on persistence_condition-as-event (item 2/B), Intel-Token-as-cost fungibility question (item 10), and the same self-fire trigger ambiguity as DIR.MOD.1 with a self-harmful consequence (item 11). Design Pass ✓ (all 22 rows evaluated), Issues Resolved not yet — cannot close this session.*

```python
DIR.MOD.9 = Card(
    id      = "DIR.MOD.9",  card_id = "DIR.MOD.9",  version = "v0.1",
    name    = "Fiscal Sanction",
    tagline = "The public already turned on them. Directorate just needed the opening.",
    type    = ModReactCard,  faction = Directorate,
    layer   = Submission,  function = Block,  subject = PublicAct,  # assigned S137 (04-n175, Andy confirmed) — card's dominant identity is blocking PA submission from the sanctioned faction; the +1 PS is the secondary effect, not the primary one

    trigger         = standing_marker.decreased(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
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
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = faction(Directorate).standing.add(1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Directorate: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Fills Directorate's Economy|Remove gap (previously zero cards in that cell, §9). Reactive: fires whenever ANY faction's PS decreases, for any reason — the public souring on a faction is the trigger. Gate: Directorate must hold a non-Expired Intel token keyed to the same faction whose PS just dropped, consumed on fire. Effect is two-part: (1) +1 PS to Directorate for opening the sanction (matches PA.6 Standing Injunction's placement-PS precedent); (2) Permanent standing condition blocking ALL Public Act submission from the sanctioned faction — not one taxonomy, the whole class — until they pay a 2-native fine to Reservoir (self-policing per GR 6.1a, same clearing pattern as Zoning Freeze/Standing Injunction). No quarter-end escape valve — this is a debt the target must actively clear, not a deterrent play with a built-in expiry. First Permanent-persistence ModReactCard in the set (existing precedent is Immediate fire-and-consume or Seasonal-until-Quarter-end) — a new but consistent extension of the card-as-condition pattern, not new ARBITER behavior requiring a fresh procedure.",
    arbiter_note = "On trigger (any faction's Standing marker moves down, any cause): if Directorate holds a Fresh or Stale Intel token keyed to that faction, Directorate may spend it to play this card. Directorate PS +1. Place card in Directorate's play area as a standing condition naming the sanctioned faction. From this point forward: the sanctioned faction cannot submit any Public Act at Phase B. Card remains active until the sanctioned faction pays 2 of their native resource to Reservoir, at which point remove the card and announce.",
)
```

---

### DIR.MOD.10 — RIOT CONTROL UNIT

#### Design Rationale
Weak-tier Boost in Directorate's locked 2 Boost/2 Hinder ModBattleCard set (S132) — first ModBattleCard content in the game, 09-06 pattern-setter for the whole subclass. Expresses §5a's literal-force doctrine ("military assets: enforcement personnel and equipment for conflict resolution and presence removal") as a Boost applied to whichever contesting faction the playing side names at commit — not restricted to Directorate itself (Art 03 §10.1.2 Step 1.2.2, S132). No cost: Art 03 §10.1.2 has no payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132, applies uniformly across all 5 factions' sets). Magnitude/value_rating (+1/1) locked as the weaker of the two Boost tiers; playtest-flagged, not treated as final (04-n94). Pairs with DIR.MOD.12 Requisitioned Equipment (the +2 Boost sibling) to complete the Asset/Equipment naming pair (S130); DIR.MOD.11/13 form the Hinder counterpart pair.

#### Card Story
A Directorate enforcement unit moves into the contested district at the moment of confrontation — committed to reinforce whichever side the playing faction has named, which need not be Directorate's own.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Enforcement personnel thrown into a live contest is the textbook literal expression of §5a's "military assets" doctrine. | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only (`perspectives`/`design_note` schema-locked None for ModBattleCard); institutional-enforcement register throughout. | Art 00 §9 |
| Doctrine alignment | ✓ | Boost directly expresses §5a's literal-force doctrine; `doctrine_mod`/`target_faction` correctly None — the target lives in `ModBattleExpr.target`, not a Card-level field. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills the Asset-category naming slot in the locked 2 Boost/2 Hinder pattern (S130/S132). | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None — contest itself is the taxonomy-bearing act, not the modifier (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Boost tier per locked S132 pattern; no cost step exists for this subclass (Art 03 §10.1.2); magnitude/value_rating playtest-flagged (04-n94), not re-litigated here. | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution — fires at commit, discarded at §10.1.4 cleanup, no multi-Quarter persistence. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None — fires at Battlefield Strength commit (§10.1.2 Step 1.2.2), not a trigger condition. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (Andy, S140, locked whole-subclass, PM02 L269). Effect is a mechanical Boost/Hinder with doctrinal alignment already captured via Doctrine alignment/narrative; no independent per-faction scoring needed. | Art 04 §6.1–§6.2; PM02 L269 |
| Supported by zones | ✓ | No `target_district` (schema-locked None); `ring_constraint=None` correct for a faction-deck card (only Ring-modifier-deck cards carry a set ring_constraint, 04-n161). | Art 01 §6–§7 |
| Supported by components | ✓ | No new components invoked; Battlefield Modifier Card mechanic already established. | Art 02 |
| Supported by game procedure | ✓ | Art 03 §10.1.2 Steps 1.2.2 (commit)/1.2.3 (reveal)/1.2.4 (announce) and §10.1.4.0/§10.1.4.1 (cleanup) fully cover this card's mechanic. | Art 03 §10.1.2, §10.1.4 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding, not previously applied to this subclass). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain New Meridian event — target's contribution to the contest, not a mechanic restatement. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None — no success/successcrit/fail/failcrit fields; effect is a printed deterministic value, not a resolution tier. | Art 04 §6.2 |
| Resource cost positioning | N/A | `cost=None` is the locked whole-subclass convention (Andy S132 — Art 03 §10.1.2 has no cost validation/payment step); no mono/cross-resource question applies. | PM05 04-n94 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S132. First ModBattleCard content in the game — 09-06 pattern-setter, establishing the stub format for the whole subclass. Fields follow Art 04 §6.1/§6.2 (ModBattleCard column) and the S132 procedure redesign (Art 03 §10.1.2, PM02 L242): `effect` is a fixed direction printed on the card, `target` is named by whoever plays it at commit (§10.1.2 Step 1.2.2) — not restricted to Directorate or to a contesting faction. Directorate's literal-force doctrine (§5a: "military assets: enforcement personnel and equipment for conflict resolution and presence removal") expressed as a Boost. **Count/magnitude locked S132 (Andy):** 4 cards per faction — 2 Boost + 2 Hinder, magnitudes +1/+2 and −1/−2 respectively; `value_rating` mirrors `magnitude`. Flagged for playtest validation, not treated as final (04-n94 log-to-validate). This is the weaker Boost tier (+1). Design-reviewed S140 (09-16 step 4, ModBattleCard pattern-setter) — confirmed the checklist's N/A set is 6 rows for this subclass (Taxonomy fit, Effect duration, Persistence, Trigger validity, Outcome determinacy, Resource cost positioning), more constrained than ModActionCard's 4 (§6.2's modifier constraints table additionally forces `affinity`/`restriction`/`perspectives`/`design_note` None for ModBattleCard). **Portrait resolved same session (Andy, S140, PM02 L269): ModBattleCard carries no portrait value, permanently — not deferred to the schema session.** Applies to all 44 ModBattleCard stubs (24 Ring/Standard + 20 faction).*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "Directorate enforcement units, deployed not to seize new ground but to hold whatever the institution has already decided should hold.",
    arbiter_note = "Playable by any faction, not just Directorate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### DIR.MOD.11 — EMERGENCY CURFEW

#### Design Rationale
Weak-tier Hinder, completing the pattern-setter's doctrine expression with §5a's other half — "best suppression capability in the game," pushing a named faction's position down rather than building Directorate's own up. A curfew constrains the ground itself rather than adding force to a side, which is why it's a Tactic rather than a deployed Asset (S130 naming convention). Same no-cost/playtest-flagged (04-n94) terms as DIR.MOD.10. DIR.MOD.13 Martial Lockdown is the escalated −2 counterpart.

#### Card Story
A curfew order drops on short notice, checkpoints going up before anyone can react — whichever faction the playing side has named loses the freedom of movement it was counting on.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A curfew imposed on a rival's operating room is a grounded expression of §5a's suppression doctrine. | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only (`perspectives`/`design_note` schema-locked None); administrative-suppression register, vague official reasoning. | Art 00 §9 |
| Doctrine alignment | ✓ | Hinder expresses §5a's "best suppression capability in the game" directly; `doctrine_mod`/`target_faction` correctly None — target lives in `ModBattleExpr.target`. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills the Tactic-category Hinder slot in the locked pattern (S130/S132). | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None — contest itself is the taxonomy-bearing act (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Hinder tier per locked S132 pattern; no cost step exists for this subclass; magnitude playtest-flagged (04-n94), not re-litigated here. | PM05 04-n94 |
| Effect duration | N/A | Immediate-resolution, discarded at §10.1.4 cleanup. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None; fires at Battlefield Strength commit, not a trigger. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` is correct and permanent — ModBattleCard carries no portrait value (Andy, S140, locked whole-subclass, PM02 L269). | Art 04 §6.1–§6.2; PM02 L269 |
| Supported by zones | ✓ | No `target_district` (schema-locked); `ring_constraint=None` correct for a faction-deck card. | Art 01 §6–§7 |
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

*S132. Hinder counterpart to DIR.MOD.10, expressing the other half of §5a's Directorate doctrine: "Suppression toolkit: push other factions' control tiers down rather than building own tiers up — best suppression capability in the game." A curfew doesn't reinforce Directorate's own position in the contest — it makes the named faction's position harder to hold, a Tactic rather than a deployed Asset. Weaker Hinder tier (−1); DIR.MOD.13 Martial Lockdown is the escalated −2 counterpart. Design-reviewed S140 (09-16 step 4) — same disposition as DIR.MOD.10; portrait resolved same session (PM02 L269).*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "A curfew order goes out on short notice — official reasoning vague, timing anything but coincidental.",
    arbiter_note = "Playable by any faction, not just Directorate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### DIR.MOD.12 — REQUISITIONED EQUIPMENT

#### Design Rationale
Escalated Boost tier, rounding out the pattern-setter's Asset/Equipment/Tactic naming trio (S130) before replication to the other four factions. Heavier material commitment than DIR.MOD.10's routine personnel deployment — hardware pulled from storage rather than units dispatched — justifying the stronger +2 tier under the same no-cost, playtest-flagged (04-n94) terms.

#### Card Story
Institutional hardware — barricades, vehicles, surveillance rigs — gets signed out of storage and committed to wherever the tension is highest, reinforcing whichever faction the playing side has named.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Requisitioned material committed to a live contest is a grounded expression of §5a's "equipment for conflict resolution" doctrine. | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only; institutional-logistics register (signed out of storage), distinct from DIR.MOD.10's personnel framing. | Art 00 §9 |
| Doctrine alignment | ✓ | Boost directly expresses §5a's literal-force doctrine; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills the Equipment-category naming slot, completing the trio with DIR.MOD.10 (Asset) and DIR.MOD.11/13 (Tactic). | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Stronger Boost tier (magnitude 2/value_rating 2) per locked S132 pattern; no cost step exists for this subclass; playtest-flagged (04-n94). | PM05 04-n94 |
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

*S132. Second Boost card, Equipment category rather than DIR.MOD.10's human Asset — rounds out the pattern-setter with all three naming-convention categories represented (Asset/Equipment/Tactic, S130 lock) before replicating to the other four factions. Stronger Boost tier (+2) — heavier material commitment than the routine personnel deployment of DIR.MOD.10. Design-reviewed S140 (09-16 step 4) — same disposition as DIR.MOD.10.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "Institutional hardware, signed out of storage on short notice and committed to wherever the tension is highest tonight.",
    arbiter_note = "Playable by any faction, not just Directorate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### DIR.MOD.13 — MARTIAL LOCKDOWN

#### Design Rationale
Escalated Hinder tier, completing the locked 2 Boost/2 Hinder pattern. Where DIR.MOD.11 Emergency Curfew is a routine administrative order, Martial Lockdown is §5a's suppression doctrine turned all the way up — full mobilization against a named faction's position rather than a movement restriction. Same no-cost, playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
Full lockdown comes down from Government Citadel, no explanation offered — whichever faction the playing side has named finds its position in the district untenable overnight.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Full mobilization against a rival's position is the escalated form of §5a's suppression doctrine. | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only; institutional-authority register, no explanation offered. | Art 00 §9 |
| Doctrine alignment | ✓ | Hinder expresses §5a's "best suppression capability in the game" at its escalated tier; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills the Tactic-category escalated Hinder slot alongside DIR.MOD.11. | Art 04 §6.1, §11.1 |
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

*S132. Escalated Hinder counterpart to DIR.MOD.11 Emergency Curfew (−2 vs. −1) — completes the 2 Boost / 2 Hinder pattern locked S132. Where Curfew is a routine administrative order, Lockdown is Directorate's "best suppression capability in the game" (§5a) turned all the way up: full mobilization against the named faction's position, not just restricted movement. Design-reviewed S140 (09-16 step 4) — same disposition as DIR.MOD.11.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "The order comes down from Government Citadel: full lockdown, effective immediately. No one asks who requested it.",
    arbiter_note = "Playable by any faction, not just Directorate (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### DIR.MOD.14 — STANDING ORDER

#### Design Rationale
First faction ModActionCard content in the game (pattern-setter, 09-06/04-n157). Minor tier (+5) of Directorate's `threshold_delta` quartet — pre-cleared procedural advantage, a clean mechanical expression of the institutional-authority doctrine (§5a). Self-only (no faction-target field on this `ModActionExpr` variant).

#### Card Story
A directive already cleared through channels lets a Directorate operation proceed without the friction a fresh request would meet.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pre-cleared procedural advantage is the textbook Directorate mechanical expression (§5a: suppression/control via institutional authority). | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | `faction=Directorate`; narrative reads in the institutional-authority register — a directive, not a favor. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`; no doctrinal relationship in play. | Art 04 §6.2 |
| Card type fit | ✓ | ModActionCard, `subtype=FactionSpecific`; correctly excluded from taxonomy (`layer`/`function`/`subject=None`) per §11.1. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None for all modifier subclasses' `layer`/`function`/`subject`. | Art 04 §6.2 |
| Balance | ✓ | Minor tier of the locked 4-value ladder; `value_rating=1` mirrors tier. | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None for ModActionCard. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None — bundled at Dispatch, not trigger-fired. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` genuinely assessed, not a TBD punt — a procedural ease carries no independent doctrinal weight beyond what the host action already scores. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | No `target_district`; `ring_constraint=None`/`ring_origin=None` correct (faction deck, not ring-sourced). | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Dispatch-bundling procedure at Art 03 §9.1.1/§9.4.0.1 covers attachment; `arbiter_note` cites it. | Art 03 §9.1.1, §9.4.0.1 |
| Data schema validation | ✓ | `ps_framing`/`boost`/`resolution_type` added as explicit None placeholders (04-n177 scaffolding, not previously applied to this corpus). | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence New Meridian event. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | ModActionCard carries no `success`/`fail`-family fields of its own (schema-locked None). | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None` is the closed whole-subclass convention (PM02 L256 — splay-display legibility); out of scope for the 04-n178 Floor Act rule (scoped to CovertOp/PublicAct/ModReact only). | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135. First ModActionCard content in the game exercising the actual `ModActionExpr` menu (09-06/04-n157 pattern-setter — PM02 L256; STD.MOD.1 Overture and SYN.MOD.1 The Fixer, the two prior "ModActionCard" entries, were both migrated to Issued ModReactCard at L245, leaving this slot genuinely empty until now). Establishes the tagged-union call convention for `ModActionExpr` — `ModActionExpr.<variant>(...)`, no prior instance existed to follow. Fields per §6.1/§6.2 (ModActionCard column) and the 04-n157 action-space analysis: **host-binding** is packet-pairing only — attach at Dispatch assembly to any CA/PA in the acting faction's own submitted packet (Art 03 §9.1.1); no card-level restriction field exists or is needed, and a ModActionCard can never reach a rival's sealed Dispatch Case. **Cost** is `None` uniformly — Beat 0 payment validation (Art 03 §9.4.0.1 Step 2) could support a live modifier cost here, unlike ModBattleCard's true no-cost-step case, but the splay-display convention (§9.4.0.1 Step 4) makes a distinct modifier cost illegible, so it folds into the host packet's total drain instead. **Count/format locked S135, revised twice same session:** 12 cards/faction — 4 `threshold_delta` (this tier) + 2 `success_multiplier` + 4 `ps_shift` + 2 `cost_reduction`, asymmetric because the four effect types have genuinely different magnitude-variation room (§6.3): `threshold_delta` runs against the d100 threshold scale (real thresholds 25–65, `ring_mod`/`doctrine_mod` already establish ±10/±15 as meaningful) and supports 4 tiers (+5/+10/+15/+20 — Andy's original example already named 4 values; a first pass compressed it to 3 before he caught it reading back the transcript); `ps_shift` likewise grew from an initial 2-card same-direction reading to a full 2×2 self/target matrix (see DIR.MOD.19); the other two effect types are small-integer/exponential mechanics that stay at 2 tiers. Directorate's institutional-authority doctrine (§5a) expressed as a pre-cleared procedural advantage — this is the weakest tier (+5). Design-reviewed S139 (09-16 step 3, faction ModActionCard pattern-setter).*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # Assessed S139, not a TBD punt — procedural ease carries no independent doctrinal weight beyond the host action's own score
    narrative    = "A directive already cleared through channels lets a Directorate operation proceed without the friction a fresh request would meet.",
    arbiter_note = "Attach at Dispatch assembly to any CA/PA in the same faction's own packet (Art 03 §9.1.1) — no card-level host restriction, narrative fit is advisory only. Effect applies only to the host it's packeted with; cannot reach another faction's operation.",
)
```

---

### DIR.MOD.15 — REGULATORY CLEARANCE

#### Design Rationale
Mid tier (+10) of Directorate's `threshold_delta` quartet. Reframed from an earlier hostile-flavored seed concept ("Regulatory Inspection" — raising a rival's difficulty) per 04-n170, same self-only correction as the Ring set's tier reframes.

#### Card Story
An inspection scheduled and passed well in advance leaves nothing for bad luck — or a rival's tip-off — to catch.

**Design checklist:** Same disposition as DIR.MOD.14. Narrative independently checked — "leaves nothing... to catch" reads self-protective, not a claim of imposing difficulty on a rival; clean.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional-authority reframe fits doctrine. | Art 00 §7; PM05 04-n170 |
| Voice fit | ✓ | Clean self-only narrative, correct register. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Mid tier; `value_rating=2` mirrors tier. | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted — no independent doctrinal weight. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct for a faction deck card. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis as DIR.MOD.14. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event, self-only clean. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135. Mid tier of the 3 `threshold_delta` cards (+10, matching the `ring_mod`/`doctrine_mod` baseline granularity — §6.5). Reframed from an earlier hostile-flavored seed concept ("Regulatory Inspection" — raising a rival's difficulty, `Whiteboard/modifier_card_ideas.md`) per **04-n170**: `threshold_delta` carries no faction parameter (§6.3), so it can only ever ease the acting faction's own host action, never a rival's. Design-reviewed S139 — reframe clean.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "An inspection scheduled and passed well in advance leaves nothing for bad luck — or a rival's tip-off — to catch.",
    arbiter_note = "Reframed from a hostile-flavored seed concept per 04-n170 — self-only, same basis as all threshold_delta cards in this set.",
)
```

---

### DIR.MOD.16 — SHOW OF FORCE

#### Design Rationale
Third of Directorate's 4 `threshold_delta` tiers (+15), not the capstone (DIR.MOD.25 holds +20). Reframed from a hostile-flavored seed concept per 04-n170. **Outstanding issue:** narrative ("resistance tends to evaporate before it fully forms") implies an effect on third-party resistance that the self-only mechanic can't deliver — same shape as STD.MOD.29's flagged dual-purpose framing.

#### Card Story
A visible deployment backs up whatever the Directorate is about to attempt — the operation itself simply meets less friction.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Deterrence-as-ease fits institutional-authority doctrine. | Art 00 §7; PM05 04-n170 |
| Voice fit | ⚠ | Narrative ("resistance tends to evaporate") implies a rival-facing effect the self-only mechanic can't deliver — same category as STD.MOD.29. Minor tighten recommended, not blocking. | Art 00 §9; PM05 04-n170 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Third tier; `value_rating=3` mirrors tier (widened 1–4, L259). | PM02 L258, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ⚠ | See Voice fit — implies dual-purpose effect. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (narrative dual-purpose framing) |  |

*S135, revised same session: third of **4** `threshold_delta` tiers (+15), not the capstone — Andy corrected the tier count from 3 to 4 (+5/+10/+15/+20; his original example already named 4 values, "+5, +10, +25, +20," compressed to 3 in the first pass). DIR.MOD.25 Executive Mandate (+20) is now the true capstone. Also reframed from a hostile-flavored seed concept per 04-n170, same basis as DIR.MOD.15. Magnitude exceeds the ±15 `doctrine_mod` baseline only nominally. **Design-reviewed S139 — narrative implies a rival-facing effect ("resistance evaporates") the self-only mechanic can't deliver; flagged for a light tighten, matching STD.MOD.29.***

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A visible deployment backs up whatever the Directorate is about to attempt — resistance tends to evaporate before it fully forms.",
    arbiter_note = "Reframed from a hostile-flavored seed concept per 04-n170, same basis as DIR.MOD.15. Narrative flagged S139 — implies dual-purpose effect despite self-only mechanic.",
)
```

---

### DIR.MOD.17 — BY THE BOOK

#### Design Rationale
Common tier (n=1) of Directorate's `success_multiplier` pair. Self-only, fits the "procedural correctness compounds" institutional framing cleanly.

#### Card Story
Procedural correctness compounds — an action executed exactly to protocol produces more than the protocol strictly requires.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Procedural-compounding fits institutional-authority doctrine. | Art 00 §7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Common tier of the 2-value pair; `value_rating=1` mirrors tier. | PM02 L256, L259 |
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

*S135. Common tier of the 2 `success_multiplier` cards (n=1) — 04-n157: this effect type supports only 2 tiers, since n=1 already doubles the host's effect and n=2 triples it. Design-reviewed S139.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Procedural correctness compounds — an action executed exactly to protocol produces more than the protocol strictly requires.",
    arbiter_note = "Self-only, same as all non-ps_shift ModActionExpr variants (§6.3, 04-n170) — amplifies the acting faction's own host action, never a rival's.",
)
```

---

### DIR.MOD.18 — OVERWHELMING RESPONSE

#### Design Rationale
Capstone tier (n=2) of Directorate's `success_multiplier` pair. Same unvalidated-magnitude caveat as every n=2 success_multiplier card in the corpus.

#### Card Story
A measured response becomes full institutional mobilization — the outcome lands far past what was ever authorized on paper.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Escalation-as-mobilization fits institutional-authority doctrine. | Art 00 §7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, n=2 unvalidated against play. | PM02 L256; PM05 04-n157, 04-n94 |
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

*S135. Rare/capstone tier of the 2 `success_multiplier` cards (n=2 — triples the host's success effect). Flagged for playtest, same caveat as ModBattleCard's magnitude scale (04-n94) — reserve for high-stakes plays, not routine deployment. Design-reviewed S139.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A measured response becomes full institutional mobilization — the outcome lands far past what was ever authorized on paper.",
    arbiter_note = "Rare/capstone tier — log actual play outcomes before treating n=2 as balanced (04-n157, same playtest caveat as 04-n94).",
)
```

---

### DIR.MOD.19 — MODEL CITIZEN

#### Design Rationale
Self-boost minor tier (+1) of the `ps_shift` 2×2 matrix — the only `ModActionExpr` variant carrying a faction parameter. `faction="acting"` needs no host-declared target, so no submission-validity dependency (contrast DIR.MOD.20/24).

#### Card Story
The Directorate's conduct is cited publicly as the standard — a small, deliberate boost to standing.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public-standard-citation fits institutional-authority doctrine. | Art 00 §7 |
| Voice fit | ✓ | Clean self-only narrative. | Art 00 §9 |
| Doctrine alignment | N/A | `faction="acting"` — no separate target dependency. | Art 04 §6.2, §6.3 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ✓ | Minor tier of the 2×2 `ps_shift` matrix; `value_rating=1` mirrors tier. | PM02 L257, L259 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted — PS shift is the card's whole effect. | Art 04 §6.1–§6.2 |
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

*S135, revised same session: `ps_shift` is a full 2×2 matrix, not a 2-card direction split — 4 cards total (DIR.MOD.19/23/20/24), mirroring ModBattleCard's Boost+1/+2, Hinder−1/−2 structure exactly. Unlike the other three `ModActionExpr` variants, `ps_shift` carries a faction parameter (§6.3: `acting | target | named faction`), so both **direction** (self vs. target) and **magnitude** (±1/±2) vary independently. This card: self, minor (+1). DIR.MOD.23 Commendation: self, major (+2). DIR.MOD.20 Public Reprimand: target, major (−2). DIR.MOD.24 Internal Affairs Referral: target, minor (−1). Faction ModActionCard count revised 9 → **11 cards/faction** (3 threshold_delta + 2 success_multiplier + 4 ps_shift + 2 cost_reduction); Ring ModAction revised 18 → **22 cards/ring** (11 × 2 for Portable/Ring-Locked). See PM02 L257 (revises L256). Design-reviewed S139.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "The Directorate's conduct is cited publicly as the standard — a small, deliberate boost to standing.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half of the pair always resolves to the acting faction.",
)
```

---

### DIR.MOD.20 — PUBLIC REPRIMAND

#### Design Rationale
Target-hinder major tier (−2) of the `ps_shift` matrix — see DIR.MOD.19 for the full structure. `arbiter_note` correctly describes `faction="target"` resolving via whichever faction the host names — the modifier's target is the host it's packet-paired with, not an independently-declared field (Andy, S139).

#### Card Story
An official rebuke lands on whoever the action was aimed at — public, on the record, and costly.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Public rebuke fits institutional-authority doctrine. | Art 00 §7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
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

*S135. Target-hinder, major tier (−2) of the `ps_shift` 2×2 matrix — see DIR.MOD.19 for the full structure. Magnitude mirrors the established Intel Token Hinder precedent (PM02 L242) rather than the ±1 baseline, since a named PS hit reads as a real consequence, not a nudge. This is one of two cards in the set that reach a faction other than the acting one — legitimately, since `ps_shift` is schema-built for it (unlike `threshold_delta`/`success_multiplier`/`cost_reduction`, flagged self-only at 04-n170). Design-reviewed S139 — this card's own `arbiter_note` was initially misread as evidence of an unenforced schema gap (schema_cleanup_log.md #21); closed same session — Andy: the card's target IS the host it's packet-paired with at Dispatch, not an independently-validated field.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "An official rebuke lands on whoever the action was aimed at — public, on the record, and costly.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA it's packet-paired with names as its target_faction (§6.1) — the modifier's target IS the host action, not an independently-declared field (Andy, S139).",
)
```

---

### DIR.MOD.21 — JURISDICTION WAIVER

#### Design Rationale
Common tier (n=1) of Directorate's `cost_reduction` pair, PA-only per §6.3.

#### Card Story
A jurisdictional formality is waived for this faction alone, quietly, ahead of submission.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Waiver-by-authority fits institutional doctrine. | Art 00 §7 |
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

*S135. Common tier of the 2 `cost_reduction` cards (n=1). PA-only per §6.3 — CA cost is committed at dispatch before Beat 0 and cannot be reduced post-submission. Design-reviewed S139.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A jurisdictional formality is waived for this faction alone, quietly, ahead of submission.",
    arbiter_note = "PA host only. Attach at Dispatch (Art 03 §9.2) alongside the declared PA; reduces the resource total owed at Beat 4 by 1 unit.",
)
```

---

### DIR.MOD.22 — REQUISITIONED RESOURCES

#### Design Rationale
Capstone tier (n=2) of Directorate's `cost_reduction` pair. Same flat-vs-proportional caveat as the Ring set's cost_reduction capstones — PA costs sample at 1–4 total units, so a flat 2-unit reduction is a large fraction on cheap PAs.

#### Card Story
Materiel and personnel already committed elsewhere in the institution get redirected — the public act proceeds at a fraction of its nominal cost.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Institutional-redirection fits doctrine. | Art 00 §7 |
| Voice fit | ✓ | Clean narrative. | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | PA-only, correctly restricted. | Art 04 §6.1, §6.3, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | Capstone tier; `value_rating=2` mirrors tier, flat 2-unit reduction not checked against any specific PA's cost (same open question as the Ring set's equivalents). | PM02 L256; PM05 04-n157 |
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

*S135. Capstone tier of the 2 `cost_reduction` cards (n=2). PA costs sample at 1–4 total units (04-n157) — a 2-unit reduction approaches making many PAs nearly free; flagged for playtest same as the rest of this set. Design-reviewed S139.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Materiel and personnel already committed elsewhere in the institution get redirected — the public act proceeds at a fraction of its nominal cost.",
    arbiter_note = "Capstone cost_reduction tier — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157, same playtest caveat as the rest of this set).",
)
```

---

### DIR.MOD.23 — COMMENDATION

#### Design Rationale
Self-boost major tier (+2) of the `ps_shift` matrix — same self-resolution basis as DIR.MOD.19, doubled magnitude.

#### Card Story
A commendation issued through official channels carries more weight than a compliment — it's the institution putting its name behind the outcome.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as DIR.MOD.19. | Art 00 §7 |
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
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ✓ |  |

*S135, added same session as DIR.MOD.24 to complete the `ps_shift` 2×2 matrix (Andy: "we should make 2 more... if ps can be used this way — need +2 ps and −1 ps cards"). Self-boost, major tier (+2) — stronger counterpart to DIR.MOD.19 Model Citizen. See DIR.MOD.19 for the full matrix structure. Design-reviewed S139.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A commendation issued through official channels carries more weight than a compliment — it's the institution putting its name behind the outcome.",
    arbiter_note = "Self-only, resolves to the acting faction. Major tier — flagged for playtest same as the rest of this set (04-n157).",
)
```

---

### DIR.MOD.24 — INTERNAL AFFAIRS REFERRAL

#### Design Rationale
Target-hinder minor tier (−1) of the `ps_shift` matrix, softer counterpart to DIR.MOD.20. Same target-resolution behavior — resolves via host pairing, not an independent field.

#### Card Story
Nothing is announced. A referral goes into a file, and somehow the file's contents find their way into conversation.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as DIR.MOD.20. | Art 00 §7 |
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

*S135, added same session as DIR.MOD.23 to complete the `ps_shift` 2×2 matrix. Target-hinder, minor tier (−1) — softer counterpart to DIR.MOD.20 Public Reprimand: a quiet referral rather than a public rebuke. Drawn from the Faction ModAction seed pool (`Whiteboard/modifier_card_ideas.md`), previously unused when only 2 ps_shift cards were planned. Design-reviewed S139.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Nothing is announced. A referral goes into a file, and somehow the file's contents find their way into conversation.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA itself names as its target_faction (§6.1) — same behavior as DIR.MOD.20, minor tier (Andy, S139).",
)
```

---

### DIR.MOD.25 — EXECUTIVE MANDATE

#### Design Rationale
True capstone (+20) of Directorate's `threshold_delta` quartet, closing the faction set. Clean self-only narrative throughout.

#### Card Story
An executive mandate carries the full authority of Directorate leadership — nothing left to interpret, nothing left to contest.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Top-authority mandate is the clean capstone expression of institutional-authority doctrine. | Art 00 §7 |
| Voice fit | ✓ | Clean self-only narrative — no dual-purpose residue (contrast DIR.MOD.16). | Art 00 §9 |
| Doctrine alignment | N/A | No `target_faction`. | Art 04 §6.2 |
| Card type fit | ✓ | Same basis as set. | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None. | Art 04 §6.2 |
| Balance | ⚠ | True capstone tier; `value_rating=4` correctly mirrors tier (widened 1–4, L259) — +20 unvalidated against play. | PM02 L258, L259; PM05 04-n157 |
| Effect duration | ✓ | Fires with host, consumed on use. | Art 04 §5 P19 |
| Persistence | N/A | Schema-locked None. | Art 04 §6.2 |
| Trigger validity | N/A | Schema-locked None. | Art 04 §6.2 |
| Portrait validity | ✓ | `portrait=None` warranted. | Art 04 §6.1–§6.2 |
| Supported by zones | ✓ | `ring_constraint=None`/`ring_origin=None` correct. | Art 01 §6–§7 |
| Supported by components | ✓ | No new components. | Art 02 |
| Supported by game procedure | ✓ | Same Dispatch-bundling basis. | Art 03 §9.1.1 |
| Data schema validation | ✓ | 04-n177 scaffolding placeholders added. | Art 04 §6.1–§6.3; 04-n177 |
| Card narrative | ✓ | Plain 1-sentence event, correctly self-only. | Art 04 §5 Card Story |
| Outcome determinacy | N/A | Schema-locked None. | Art 04 §6.2 |
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (+20 playtest flag) |  |

*S135, added same session Andy caught the tier count reading back the transcript: `threshold_delta` is 4 tiers, not 3 — his original example ("+5, +10, +25, +20") already named 4 values; the first pass compressed the top two into a single "+15–20 capstone" range. True capstone (+20); DIR.MOD.16 Show of Force (+15) is now the third of four, not the top. `value_rating` **widened schema-wide from 1–3 to 1–4 (§6.1/§6.2, PM02 L259)** so this tier gets its own distinct value (4) instead of sharing DIR.MOD.16's band — Andy's call after weighing it against leaving the two tiers to share `value_rating=3`. Faction ModActionCard count revised again: 11 → **12 cards/faction** (4 threshold_delta + 2 success_multiplier + 4 ps_shift + 2 cost_reduction); Ring ModAction: 22 → **24 cards/ring**. See PM02 L258/L259 (revises L257). Design-reviewed S139 — closes the Directorate ModActionCard set (12/12 cards); one narrative flag carried (DIR.MOD.16); the target-restriction "gap" initially read into DIR.MOD.20/24's `arbiter_note` (schema_cleanup_log.md #21) was closed same session — not a real gap, per Andy.*

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
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "An executive mandate carries the full authority of Directorate leadership — nothing left to interpret, nothing left to contest.",
    arbiter_note = "Capstone threshold_delta tier — log actual play outcomes before treating +20 as balanced (same playtest caveat as the rest of this set, 04-n157).",
)
```

---

