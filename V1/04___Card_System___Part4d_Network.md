## Network
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#network-covert-operations) · [Public Acts](#network-public-acts)

---

### Network — Covert Operations
[↑ Network](#network)

| Card | Name |
|------|------|
| [NET.CA.1](#c26-leak) | Leak |
| [NET.CA.2](#c27-disclosure-loop) | Disclosure Loop |
| [NET.CA.3](#c28-breaking-news) | Breaking News |
| [NET.CA.4](#c29-network-cascade) | Network Cascade |
| [NET.CA.5](#c30-community-anchor) | Community Anchor |
| [NET.CA.6](#network-sacrifice) | Sacrifice |
| [—](#network-weaponized-transparency) | Weaponized Transparency (Retired S70) |
| [NET.CA.7](#netca7--ground-signal) | Ground Signal |
| [NET.CA.8](#netca8--fake-news) | Fake News |

### NET.CA.1 — LEAK
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's pre-execution discovery card — spends 1 Exposure + 1 Findings to expose a target faction's most resource-costly unresolved covert operation before it fires, cancelling it in the process. Full discovery mechanic applies: ARBITER publicly announces operation type, acting faction, and targets; target faction suffers PS reduction; the operation does not resolve. Resources the target submitted are lost. Beat 3 timing is intentional — Network has a strategic incentive to go first in initiative order so Leak fires before the target's operation resolves; going late risks a fizzle if all valid targets have already been processed. The Findings cost requires Network to have a trade relationship with Ghost or hold Findings-generating territory — cross-resource by design. Pairs with NET.CA.2 Disclosure Loop (successful Reveal → +1 Exposure) to make revelation self-sustaining.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pre-execution discovery + cancellation — distinct from NET.CA.3 (faction communications) and all post-resolution reveal cards; Network burns the plan before it fires | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective — selective, precision disclosure as doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; 1 Exposure + 1 Findings cross-resource; Automatic; fizzle risk on low initiative creates meaningful cost beyond resources | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — broadcast-based pre-execution discovery is Network-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/District — what is made public is geographic (district + operation type); subject corrected from ActionAttribution S68 | Art 04b §4, §5 |
| Balance | ✓ | 1 Exposure + 1 Findings; can cancel a costly op — cross-resource cost is the primary gate; fizzle risk and initiative dependency add further constraint; flag for 04-n34c sweep | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — discovery announced and cancellation applied at resolution; no lingering state | — |
| Persistence | ✓ | Immediate — card resolves fully at Beat 3; cancelled op leaves no residual game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Network +1 submitter — discovery operation aligns with transparency doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — operation district is revealed as part of discovery, not targeted as a zone | Art 01 §6–§7 |
| Supported by components | ✓ | CovertOperation (unresolved, in Beat 3 grid) as target — physically verifiable by ARBITER at resolution | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; initiative order determines valid targets; ps_framing on target pending 04-n33/04-n34b | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **ps_framing on target:** Target faction PS reduction on discovery is the standard failcrit consequence — pending 04-n33 schema addition and 04-n34b sweep to formalise in spec.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Redesigned S68: subject ActionAttribution → District; pre-execution discovery + cancellation model; cross-resource cost; beat=3 initiative incentive confirmed.*

```python
NET.CA.1 = Card(
    id      = "NET.CA.1",  version="v1.1",
    name    = "Leak",
    tagline = "Expose and cancel a rival's most costly unresolved operation before it fires.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Information,  function = Reveal,  subject = CovertOperation,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction(named_opponent), target_object=CovertOperation(faction=faction(target), beat=3, unresolved=True),
    target_taxonomy=None,
    affinity=None,
    restriction = faction(target).op(beat=3, unresolved=True).count >= 1,
    cost        = resource.faction(acting).exposure * 1 + resource.faction(acting).findings * 1,
    success     = [
        game.announce(faction(target).op(beat=3, unresolved=True, selection=highest_cost), discovery=True, public=True),
        game.cancel(faction(target).op(beat=3, unresolved=True, selection=highest_cost)),
    ],
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The Network does not need to know everything — only enough to make the right question public.",
    perspectives = {Network: "We do not reveal everything. We reveal the piece that makes everything else visible."},
    design_note  = "Redesigned S68: subject corrected to District (was ActionAttribution — taxonomy mismatch); pre-execution discovery + cancellation model confirmed (target op cancelled, resources lost, PS reduction applies); cross-resource cost 1 Exposure + 1 Findings by design to force trade dependency. Beat 3 initiative incentive: Network benefits from going first; fizzle risk if target ops resolve before Leak fires. ps_framing for target PS reduction pending 04-n33/04-n34b. S126 agy audit: subject corrected to CovertOperation (District was also a mismatch — DistrictTile has no Reveal in comp_verb_phase; the card reveals and cancels a CovertOperation, not the district itself).",
    arbiter_note = "Among target faction's unresolved covert operations in the Beat 3 grid, identify the operation with the highest total resource cost submitted. Publicly announce: operation name, acting faction, target district. Cancel the operation — it does not resolve; resources submitted are lost. Target faction PS reduction applies (discovery consequence — ps_framing pending 04-n33). If no unresolved operations remain for target faction at time of Leak's resolution, operation has no effect — Network's resources spent. Network's acting faction identity is not announced at resolution.",
)
```

---

### NET.CA.2 — DISCLOSURE LOOP
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's Exposure generation card — converts the act of revealing into additional broadcast capacity. Spends 1 Finding; if Network successfully resolved any Reveal card this round, delivers +1 Exposure. The loop is the mechanic: reveal with NET.CA.1 or NET.CA.3, then play NET.CA.2 to convert that act into more Exposure for future reveals. Replaced NET.CA.2 Source Protection (S51) which was doctrinally misaligned — protecting attribution is Ghost's register. The conditional success (`if reveal_resolved_this_round >= 1`) means NET.CA.2 only pays out when Network is actively broadcasting; a NET.CA.2 played in isolation does nothing, burning only the Finding cost.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Exposure generation from reveal activity — self-sustaining broadcast loop; dead-weight if used in isolation, which is the intended design | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — loop as resource doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Findings×1 low cost; conditional payoff requires active reveal this round; replaces retired Source Protection (doctrinally misaligned) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — Exposure amplification is Network infrastructure | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/Exposure — converts reveal activity to resource; Economy layer correct | Art 04b §4, §5 |
| Balance | ✓ | Findings×1 for conditional Exposure — low cost; isolation dead-weight is intentional cost gate; conditional cost resolution outstanding (Outstanding Issue) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: Exposure delivered at Beat 3 cleanup | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | Conditional success — `reveal_resolved_this_round >= 1` is inline trigger; trigger vs. success field distinction outstanding (Outstanding Issue) | — |
| Portrait validity | ✓ | portrait = {} — Disclosure Loop is internal resource infrastructure, not a visible doctrinal act; absence confirmed intentional (Outstanding Issue) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — self-targeting; no district context | Art 01 §6–§7 |
| Supported by components | ✓ | Exposure as subject; Findings cost; no new components | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 cleanup; ARBITER tracks Reveal card resolutions this round; conditional resolution outstanding (Outstanding Issue) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Conditional success modelling:** `success = exposure += 1 if reveal_resolved_this_round >= 1 else None` — confirm whether the "else None" path consumes the Finding cost (card slot and Findings are spent, no outcome) or refunds it. Current design note says "the slot cost was the investment" — confirm.
- **portrait = {} justification:** Empty portrait for a Network FactionSpecific card is uncommon. Confirm intentional — Disclosure Loop is an internal resource mechanism, not a visible doctrinal act.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*S51 redesign — design rationale scaffold added S59. Design pass pending.*

```python
NET.CA.2 = Card(
    id      = "NET.CA.2",  version="v1.0",
    name    = "Disclosure Loop",
    tagline = "Transparency is self-sustaining. Revealing information generates the capacity to reveal more.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Economy,  function = Add,  subject = Exposure,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction(acting), target_object=None,
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).findings * 1,
    success     = resource.faction(acting).exposure += 1 if faction(acting).reveal_resolved_this_round >= 1 else None,
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "The act of disclosure is not only a tactic. It is a resource. The Network learned this before anyone else at this table.",
    perspectives = {Network: "We revealed something. Now we can reveal something more. The loop is already running."},
    design_note  = "Replaces NET.CA.2 Source Protection (retired S51). Source Protection was doctrinally misaligned — protecting attribution is Ghost's register, not Network's. Pairs with NET.CA.1 Leak and NET.CA.3 Breaking News.",
    arbiter_note = "At Beat 3 cleanup, check whether any Network Reveal card resolved successfully this round. If yes, deliver 1 Exposure to Network's resource pool. If no Reveal resolved, card takes effect but produces nothing — the slot cost was the investment.",
)
```

---

### NET.CA.3 — BREAKING NEWS
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's forced-transparency Beat 2 card — submits into the Beat 2 row to force public revelation of the target faction's first committed Beat 3 operation before the round fires. The operation still resolves; it simply does so with the table informed. Exposure×2 is the price of intelligence at this scale; threshold 50 introduces a risk the table can observe and react to.

Distinct from NET.CA.1 Leak: Leak cancels before firing (Beat 3), with the revelation as a side effect of destruction. Breaking News reveals before firing (Beat 2), with no cancellation — the operation proceeds in public. Two different Network postures: *stop it* vs. *ensure everyone watches it happen*.

Distinct from GHO.CA.2 Intercept: GHO.CA.2 delivers a private IntelDeliverySlip to Ghost — intelligence for one faction's use. Breaking News announces publicly — the whole table knows.

Crit success reveals the full queue, a significant information advantage that resets all players' tactical picture before Beat 3.

*Replaces NET.CA.3 Open Channel (retired S68). Open Channel required ARBITER to maintain a notification redirect state from Beat 2 through Beat 3 — proactive cross-beat tracking, Governing Rule 6.1 violation. Breaking News is point-in-time: ARBITER announces at Beat 2 and places a Visibility Marker (VM-xx); no state to carry forward.*

#### Card Story

A Network operative submits intelligence on a target faction's committed operation — and instead of keeping it, broadcasts it. Before Beat 3 fires, the table knows what's coming. The operation proceeds; it just does so in public.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Beat 2 forced public reveal before Beat 3 fires — distinct from NET.CA.1 (pre-execution cancel, Beat 3, no public announcement) and GHO.CA.2 (private IS-xx to Ghost, Beat 2) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective — forced transparency at the moment of commitment | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Exposure×2; threshold 50; fizzle risk if target has no committed ops; crit reveals full queue | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — forced public reveal of committed ops is Network-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ⚠ | Information/Reveal/CovertOperation — subject = CovertOperation needs 04b validation; no registered grid-card subject type currently | Art 04b §4, §5 |
| Balance | ✓ | Exposure×2 at threshold 50; fizzle risk on empty queue; crit is high-value (full queue exposure) — appropriate variance for Network initiative card | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — announcement fires at Beat 2; VM-xx handles Beat 3 public resolution flag; VM-xx is transient game-state on the grid card, not a card-level persistence field | — |
| Persistence | ✓ | Immediate — card fully resolved at Beat 2; VM-xx is physical game state managed per Art 03 procedure | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Network +1 submitter — forced transparency is core doctrine; FactionSpecific card, no other portrait entries | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no zone restriction | Art 01 §6–§7 |
| Supported by components | ✓ | VM-xx registered in 00b §4 (S82, 04-n76 ✅) | Art 02 §6–§8; Art 07 |
| Supported by game procedure | ✓ | Beat 2 d100 procedure added Art 03 §9.4 (S81, 04-n75 ✅); VM-xx Beat 3 public resolution clause added (S81, 04-n76 ✅) | Art 03 §9, §11 |
| Data schema validation | ✓ | All §6.1 fields present; subject = CovertOperation flagged for 04b taxonomy validation | Art 04 §6.1 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Taxonomy subject:** subject = CovertOperation — no registered grid-card subject type exists. Needs 04b validation pass. (Non-gate — tracked in taxonomy checklist row.)

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ S89 | |

```python
NET.CA.3 = Card(
    id      = "NET.CA.3", version="v2.0",
    name    = "Breaking News",
    tagline = "Force ARBITER to publicly reveal the target faction's first committed operation before Beat 3 resolves.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Network,
    layer   = Information, function = Reveal, subject = CovertOperation,  # 04b validation needed
    beat=2, resolution=d100, threshold=50, ring_mod=None, trigger=None,
    resolution_type = "Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district = None,
    target_faction  = faction(named_opponent),
    target_object   = None,
    target_taxonomy=None,
    affinity        = None,
    restriction     = "target_faction != acting_faction",
    cost        = resource.faction(acting).exposure * 2,
    success     = [
        game.announce(faction(target).beat3_queue[0], fields=[name, type, targets], destination=public),
        game.place(VM_xx, on=faction(target).beat3_queue[0]),
    ],
    successcrit = [
        game.announce(faction(target).beat3_queue[:], fields=[name, type, targets], destination=public),
        game.place(VM_xx, on=faction(target).beat3_queue[:]),
    ],
    fail        = None,
    failcrit    = game.dispatch(NotificationSlip(recipient=faction(target))),
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The story was going to come out. We simply chose the timing.",
    perspectives = {
        Network: "We don't ask permission to broadcast. We decide when.",
    },
    design_note  = "Replaces NET.CA.3 Open Channel (retired S68 — Governing Rule 6.1 cross-beat state violation). Fills Network's forced-transparency FactionSpecific slot at L1. Beat 2: ARBITER announces target's first Beat 3 queue entry to all players; VM-xx placed to flag public Beat 3 resolution. Distinct from NET.CA.1 Leak (Beat 3 cancel + reveal) and GHO.CA.2 Intercept (private IS-xx to Ghost). Fizzle: if target has no committed Beat 3 ops at Beat 2, announce fizzle; cost spent. Second Beat 2 d100 card alongside GHO.CA.2 — procedure gap in Art 03 tracked in 04-n75.",
    arbiter_note = "Network has played Breaking News targeting faction X. Roll d100 (threshold 50 + PS modifier). Success: check faction X's Beat 3 queue. If empty: announce 'No operations queued for faction X — Breaking News fizzles'; cost spent, no further effect. Otherwise: identify faction X's first entry in Beat 3 resolution order; announce to all players: card name, type, declared targets; place VM-xx on that card in the grid. VM-xx procedure at Beat 3: when this card is reached, announce it publicly, roll d100 visibly, announce outcome to table, then remove VM-xx. Do not announce Network as acting faction. Crit success: reveal and place VM-xx on ALL of faction X's Beat 3 queue entries. Fail: cost spent, no announcement. Crit fail: dispatch NotificationSlip to faction X only. Do not announce Network.",
)
```

---

### NET.CA.4 — NETWORK CASCADE
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's signal propagation card — extends STD.CA.6 Broadcast Interference's Public Act cost increase to an adjacent district on the same round. Mechanically ties the two cards together: STD.CA.6 must be submitted in the same round for NET.CA.4 to fire. This creates a planned two-card combo: pay the STD.CA.6 Exposure cost to disrupt PA activity in one district, then pay NET.CA.4's Exposure×2 to extend that disruption to an adjacent district. The "signal propagation" framing is doctrinally exact — The Network understands that broadcast interference is not bounded by administrative district lines. Beat 2 Automatic means both disruption effects land before Beat 4 PA resolution.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Signal propagation — extends STD.CA.6 Broadcast Interference to adjacent district; mechanically implements "broadcast doesn't stop at district borders" doctrine | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — signal propagation as operational reality | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; requires STD.CA.6 same round (restriction); Exposure×2; Beat 2 Automatic — both disruption effects land before Beat 4 PA resolution | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — signal propagation is Network-exclusive two-card mechanic | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Submission/Modify/PublicAct — extends STD.CA.6's PA cost increase to adjacent district | Art 04b §4, §5 |
| Balance | ✓ | Exposure×2 for adjacency extension; total combo cost outstanding calibration noted; STD.CA.6 dependency limits use | Art 02 §6–§7 |
| Effect duration | ✓ | One round: PA cost increase applies this round's Beat 4 PA phase only | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | STD.CA.6 submission as restriction prerequisite; submission ordering and void-on-STD.CA.6-cancel outstanding (Outstanding Issues) | — |
| Portrait validity | ✓ | Network +1 submitter; signal extension aligns with broadcast doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = adjacent to STD.CA.6.target_district; dependency resolution outstanding (Outstanding Issue) | Art 01 §6–§7 |
| Supported by components | ✓ | PublicAct as target_object; Exposure cost; no new components | Art 02 §6–§8; Art 04b §5 |
| Supported by game procedure | ✓ | Beat 2 Automatic; PA cost increase at Beat 4; STD.CA.6 submission ordering outstanding (Outstanding Issue) | Art 03 §9, §9.4, §10 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **STD.CA.6 dependency at Dispatch:** Restriction requires `submitted(STD.CA.6, round=game.round) == True`. Confirm: can NET.CA.4 be submitted before STD.CA.6 in the same round (with STD.CA.6 submission validated later), or must STD.CA.6 already be submitted when NET.CA.4 is checked?
- **target_district dependency:** NET.CA.4's target is derived from STD.CA.6's target district. If STD.CA.6 is cancelled or discarded after NET.CA.4 is submitted, what happens to NET.CA.4? Confirm void or independent resolution.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
NET.CA.4 = Card(
    id      = "NET.CA.4",  version="v1.0",
    name    = "Network Cascade",
    tagline = "Extend Broadcast Interference to an adjacent district.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Submission,  function = Modify,  subject = PublicAct,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.adjacent(C06.target_district), target_faction=None, target_object=PublicAct,
    target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).submitted(STD.CA.6, round=game.round) == True,
    cost        = resource.faction(acting).exposure * 1 + resource.faction(acting).findings * 1,
    success     = district(target).political_act_cost += 1,
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The Network understands signal propagation better than anyone at this table.",
    perspectives = {Network: "The signal does not stop at district borders. Neither do we."},
    design_note  = None,
    arbiter_note = None,
)
```

---

### NET.CA.5 — COMMUNITY ANCHOR
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's Baryo-targeted presence card — specialized version of STD.CA.3 Campaign, restricted to Baryo ring districts where Network has zero presence. The restriction enforces the narrative: Community Anchor is how Network establishes a beachhead through existing relationships, not how it expands from existing territory. Cheaper than STD.CA.3 (Exposure×1 vs dual-cost) because the card is zone-restricted and fires only on initial entry — once Network has any presence in the district, the card cannot target it again. Baryo focus aligns with Network's win path (wide Presence coverage from New Meridian, Baryo outward).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Network's Baryo entry mechanic — initial beachhead via existing relationships; distinct from STD.CA.3 Campaign (general presence) by Baryo restriction and zero-presence gate | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design — community-based entry as doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Exposure×1 (cheaper than STD.CA.3 dual-cost); Baryo+zero-presence restriction enforces narrative; aligns with Network's wide-presence win path | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — Baryo-targeted entry is Network-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Territory/Add/PresenceToken — Baryo-restricted variant of STD.CA.3 Campaign pattern | Art 04b §4, §5 |
| Balance | ✓ | Exposure×1, Automatic, Baryo+zero-presence restriction — narrower and cheaper than STD.CA.3; Baryo entry advantage calibration noted | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: +1 presence token at Beat 3; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces zero-presence condition | — |
| Portrait validity | ✓ | Network +1 submitter; community-based entry aligns with broadcast doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any(zone=Baryo) — Baryo zone definition outstanding (Outstanding Issue) | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken; Exposure cost; no new components | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 3 Automatic; ARBITER places presence token; zone check at Dispatch | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Baryo zone definition:** `district.any(zone=Baryo)` — confirm Baryo as a defined zone in Art 01. If Baryo includes multiple rings' districts, the zone boundary needs to be explicit.
- **Expansion beyond initial entry:** Once Network has 1 presence in a Baryo district (via Community Anchor), the restriction blocks reuse in that district. Confirm this is the intended scarcity design — Community Anchor establishes but does not reinforce.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Pre-convention card — design rationale scaffold added S59. Design pass pending.*

```python
NET.CA.5 = Card(
    id      = "NET.CA.5",  version="v1.0",
    name    = "Community Anchor",
    tagline = "Establish presence in a Baryo district through existing relationships.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Territory,  function = Add,  subject = PresenceToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=district.any(zone=Baryo), target_faction=None, target_object=None,
    target_taxonomy=None,
    affinity=None,
    restriction = district(target).faction(acting).presence == 0 AND district(target).zone == Baryo,
    cost        = resource.faction(acting).exposure * 1,
    success     = district(target).faction(acting).presence += 1,
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The Network did not arrive in New Meridian through official channels. They arrived through people.",
    perspectives = {Network: "We already have contacts there. This is formalising what already exists."},
    design_note  = None,
    arbiter_note = None,
)
```

---

### Network — SACRIFICE
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's credibility-to-Intel conversion card. Reflects the Network doctrine that institutional standing is a means, not an end: when The Network needs intelligence on a specific faction and has no other path to it, it trades credibility for operational capability. The PS loss is a success effect — not a submission cost — because Public Standing is a non-fungible marker, not a tradeable resource (Art 04 §6.2). Single use per play, 2 PS per token. Faction target is required: tokens must be keyed to a faction at Dispatch ("no blank checks").

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | PS-to-Intel conversion — Network doctrine: standing is a means, not an end; deliberate sacrifice for targeted intelligence | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective by design | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; free submission; PS loss as success effect; target_faction required for token keying; 2 PS per token calibrated as real doctrine commitment | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/IntelToken — PS effect generates faction-keyed Intel; Economy layer correct | Art 04b §4, §5 |
| Balance | ✓ | Free cost; 2 PS for 1 IntelToken; single use per play — PS track scarcity is the gate; 2:1 ratio prevents cheap arbitrage vs. Weaponized Transparency | Art 02 §6–§7; Art 02 §11 |
| Effect duration | ✓ | Immediate: PS reduced and token delivered at Beat 3 resolution | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | portrait = {} — PS loss is a success effect, not a portrait track shift; absence confirmed intentional | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — no district context | Art 01 §6–§7 |
| Supported by components | ✓ | target_faction required; IntelToken keyed to target_faction at Dispatch | Art 02 §6–§8; Art 02 §11 |
| Supported by game procedure | ✓ | Beat 3 Automatic; PS loss and IntelToken delivery handled by Art 03 apply effect | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

*None.*

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Migrated from Art 04 §8 (retired) Intel Economy block to Network extended section S59. Pre-convention flat format — full schema pass pending (04-47).*

```python
NET.CA.6 = Card(
    id      = "NET.CA.6",  version="v1.1",
    name    = "Sacrifice",
    tagline = "Spend two steps of credibility. Receive one piece of intelligence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Economy,  function = Add,  subject = IntelToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction.any, target_object=None,
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = None,
    success     = faction(acting).standing -= 2, IntelToken(target_faction) += 1,
    successcrit=None, fail=None, failcrit=None,
    portrait    = {},
    narrative   = "The Network knows: sometimes you spend credibility like currency. This is one of those times.",
    perspectives = {Network: "What we have built is not a goal. It is a tool. And sometimes a tool must be spent."},
    design_note  = "PS −2 is a success effect, not a cost — PS is non-fungible and cannot appear in the cost field (Art 04 §6.2). target_faction required: tokens must be keyed at Dispatch. Single use per play; 2:1 ratio prevents cheap IntelToken arbitrage Cost reasoning: Findings are needed to identify the exact weak points in adjacent district firewalls for the signal to jump.",
    arbiter_note = None,
)
```

---

### Network — WEAPONIZED TRANSPARENCY
[↑ Covert Operations](#network-covert-operations)

*Retired S70 — split into two successor cards per PM05 04-n47 (choose_one on success violation) and 04-n48. Successor A: React modifier stub below. Successor B: PA stub in Network PA section.*

---

### NET.CA.7 — GROUND SIGNAL
[↑ Covert Operations](#network-covert-operations)

#### Design Rationale
Network's public standing card — fills the Standing|Shift gap identified in Art 04b §8.3. Available only when Network IL is ≤ Established in the target district: at Dominant, the street already knows who Network is; outreach adds nothing. The card activates Network's existing chip presence to generate a legible public signal — the people carrying the message are already part of the district's daily traffic. No new infrastructure, no announcement. On a successcrit the signal lands hard enough to convert: +1 chip placed in target district alongside additional +1 PS.

#### Card Story
The message doesn't travel because Network announced it. It travels because Network is already there.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | PS generation when not Dominant — fills Standing|Shift gap in Network set; successcrit converts signal to physical presence | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Network perspective — presence made legible, not announced | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; IL ≤ Established restriction is doctrinal (no outreach needed at Dominant); Exposure×1 cost calibrated to PS yield | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Network) — street-level signal is unannounced, deniable | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Standing / Shift / PublicStanding — PS generation via distributed presence signal | Art 04b §4 |
| Balance | ⚠ | Successcrit +1 chip placement strong at Established threshold — validate against chip economy in playtesting | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — PS and chip effects resolve at Beat 3 | — |
| Persistence | ✓ | Immediate — no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Network +1 submitter — visible-but-deniable public signal aligns with Broadcaster doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named; IL restriction checked at resolution | Art 01 §6–§7 |
| Supported by components | ✓ | Successcrit places 1 chip — standard chip placement, no new component | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 d100; IL check and chip placement handled by Art 03 apply effect | Art 03 §9, §11 |
| Data schema validation | ✓ | Fields consistent with §6.1–§6.3 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Street-level signal; presence made legible without announcement | Art 04 §5 P26 |

#### Outstanding Issues

- **DB registration:** New card — requires id assignment in card_ref and component_metadata.
- **IL enum value:** Confirm `InfluenceLevel.Established` is the correct enum identifier in schema.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*New card — S106. Fills Standing|Shift|PublicStanding gap (04b §8.3 HP).*

```python
NET.CA.7 = Card(
    id      = "NET.CA.7", version="v1.0",
    name    = "Ground Signal",
    tagline = "Put the message on the street. Presence here is readable. Let it be read.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Network,
    layer   = Standing, function = Shift, subject = StandingMarker,
    beat=3, resolution=d100, threshold=50,
    ring_mod=None, doctrine_mod=None, trigger=None,
    outcome_type=None,
    persistence=Immediate, persistence_condition=None, persistence_effect=None,
    target_district = district.named,
    target_faction=None, target_object=None, target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).influence_level(district(target)) <= InfluenceLevel.Established,
    cost    = resource.faction(acting).exposure * 1,
    success = faction(acting).standing.add(1),
    successcrit = (faction(acting).presence_chips(district(target)).add(1),
                   faction(acting).standing.add(1)),
    fail=None,
    failcrit    = faction(acting).standing.remove(1),
    on_accept=None, on_decline=None,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "No one announces this. The message moves because the people carrying it are already there, already part of the district's daily traffic. The signal is readable only to those who know how to read it.",
    perspectives = {Network: "We're not running outreach. We're making our existing presence legible to people who've been ignoring it."},
    design_note  = "Restriction: Network IL in target district ≤ Established (Dominant excluded — at Dominant, the street already knows). Successcrit delta: +1 chip in target district + +1 PS additional on top of success's +1 PS (total on successcrit: +2 PS, +1 chip placed).",
    arbiter_note = "Beat 3: Network IL in target district must be ≤ Established (Dominant: card invalid, do not resolve). On success: +1 PS to Network. On successcrit: additionally place 1 Network chip in target district AND +1 PS (total: +2 PS, +1 chip placed). Failcrit: −1 PS.",
)
```

---

### NET.CA.8 — FAKE NEWS *(stub)*

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

*S130. Network plants false intelligence to redirect an opponent's DeploymentMarker to a useless district. 04-n134.*

```python
NET.CA.8 = Card(
    id      = "NET.CA.8",  card_id="NET.CA.8",  version="v0.1",
    name    = "Fake News",
    tagline = "Plant a false story. Watch where the marker goes.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Network,
    layer   = Territory,  function = Move,  subject = DeploymentMarker,

    beat    = 2,
    resolution = d100,  threshold = 50,
    persistence = Immediate,
    persistence_condition = None,  persistence_effect = None,

    target_district = None,  # source district declared in TargetProfile target_district field
    target_faction  = faction(named_opponent),
    target_object   = DeploymentMarker,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Network).exposure * 1 + resource.faction(Network).findings * 1,

    success = [
        arbiter.move(DeploymentMarker(faction=target_faction, district=target_profile.target_district),
                     to=target_profile.freeform_destination),
        arbiter.flip(DeploymentMarker(faction=target_faction), status=Unconverted),
    ],
    successcrit = None,  fail = None,  failcrit = None,

    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = None,  perspectives = None,
    design_note = "Network fabricates a story pointing to a destination district with no strategic value. The target faction's DeploymentMarker follows — their deployment is wasted. TargetProfile: target_faction and target_district identify the marker and its current location; freeform field specifies destination district. ARBITER executes the move and flips marker to Unconverted status. Chain play: Beat 2 covert move → same Quarter Leak or Live Coverage exposing the displaced position.",
    arbiter_note = "Read TargetProfile: target_faction and target_district identify whose marker and from which district. Freeform field specifies destination. Beat 2: move marker from source to destination; flip to Unconverted face. Announce marker has moved — do not announce acting faction. Fail: no effect, cost spent.",
)
```

---

### Network — Public Acts
[↑ Network](#network)

| Card | Name |
|------|------|
| [NET.PA.1](#p13-public-disclosure) | Public Disclosure |
| [NET.PA.2](#p14-community-rally) | Community Rally |
| [—](#network-live-coverage) | Live Coverage |

### NET.PA.1 — PUBLIC DISCLOSURE
[↑ Public Acts](#network-public-acts)

#### Design Rationale
Network's signature information-attack PA — a coordinated release of all substantiated intelligence against a target faction. Scaling mechanic: each Intel token spent contributes both to the threshold calculation (more tokens = more credible = easier to land) and to the damage on both success and fail (more tokens = more damage, even when the full release fails). The partial damage on fail ("the dirt still gets out") reflects that even a botched broadcast releases something. High investment ceiling makes this Network's most powerful single card when fully loaded.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Coordinated multi-attribution broadcast is Network's highest-expression public act | Art 00 §7 |
| Voice fit | ✓ | Network on-doctrine; Guild (aligned): disclosure makes attribution permanent; Ghost (opposed): sequenced release vs. full dump | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Maximum-expression Network broadcast: all held Intel tokens spent; Exposure × 2 (Network's resource). Network +2 PS on success. Intel token scarcity (Ghost pipeline or covert gathering) is the natural ceiling on doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Network) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Reveal / ActionAttribution | Art 04b §4 |
| Balance | ⚠ | Threshold scales with token count (30 + 10n). Damage scales per token (−2 PS each on success, −1 on fail). High cost (2 Exposure + all tokens). Intel tokens are scarce (require Ghost cooperation or covert gathering) — natural limiter | Art 02 §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted broadcast; no zone reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (all held, faction-keyed to target; Art 02 §6); Exposure × 2 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Token count calculated at Beat 4; all tokens spent regardless of outcome | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
NET.PA.1 = Card(
    id      = "NET.PA.1",  version="v1.0",
    name    = "Public Disclosure",
    tagline = "Network broadcasts all substantiated intelligence about a faction's operations in a single coordinated release.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,

    layer    = Information,  function = Reveal,  subject = ActionAttribution,

    beat            = 4,
    resolution      = d100,
    threshold       = 30 + (10 * count(intel_token(target=faction(target)).held)),  # +10 per token held naming target
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Contested",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Network).holds_intel_token(faction=target, count=1),
    cost        = resource.faction(Network).exposure * 2 + intel_token(target=faction(target)).all_held,

    success = (
        faction(target).standing  -= (2 * count(intel_token(target=faction(target)).spent)),
        faction(Network).standing += 2,
    ),
    successcrit = None,
    fail = (
        faction(target).standing  -= (1 * count(intel_token(target=faction(target)).spent)),  # partial — dirt still gets out
        faction(Network).standing -= 1,
    ),
    failcrit = None,

    portrait = {Network: PortraitEntry(submitter=+1)},

    narrative    = "Network does not sit on what it knows. When the moment is right, everything comes out at once.",
    perspectives = {
        Network: "We have been patient. This is the release.",
        Guild:   "Network makes the attribution permanent. Everyone knew some of this. After the disclosure, no one can pretend otherwise. That is the kind of outcome Guild recognizes.",  # aligned
        Ghost:   "Network releases everything it has. We would have sequenced it. You do not exhaust an intelligence reserve in a single action — you do not know what the next month requires.",  # opposed
    },
    design_note  = "Network's highest-damage information PA. Threshold: 30 base + 10 per token held (1 token=40, 2=50, 3=60). All held tokens spent regardless. Success: −2 PS per token, Network +2 flat. Fail: −1 PS per token (partial release), Network −1. Token scarcity (Ghost pipeline or covert gathering) is natural limiter. Beat 4 timing: benefits from covert ops having resolved at Beat 3.",
    arbiter_note = "Count Network's held Intel tokens naming target. Threshold = 30 + (10 × count). All tokens spent at resolution. On success: target loses (2 × count) PS; Network +2 PS. On fail: target loses (1 × count) PS (partial release announced); Network −1 PS. Token count cannot be zero (restriction enforces minimum 1).",
)
```

---

### NET.PA.2 — COMMUNITY RALLY
[↑ Public Acts](#network-public-acts)

#### Design Rationale
Network's broadcast-derived presence PA — scaling territorial expansion built on established foothold. Network names up to 3 districts where they are already Established or Dominant; 1 presence token is placed in each. Cost scales with district count (2 Exposure + 1 per additional district). This is not expansion into new territory — it is deepening existing presence through community mobilisation, the most on-doctrine territorial act for Network. Replaces Open Record Request, which had unworkable mechanical premises.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Broadcast-derived community presence growth is Network's primary win-condition mechanism | Art 00 §7 |
| Voice fit | ✓ | Network on-doctrine; Syndicate (aligned): acquisition-free consolidation; Directorate (opposed): unregulated expansion | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Network deepens existing foothold (Established+) — consolidation, not expansion. Scaling Exposure cost (Network's resource). Portrait +1. Directly serves Network's community-relationship territorial doctrine | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Network) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory / Add / PresenceToken | Art 04b §4 |
| Balance | ✓ | Scales: 2 Exposure (1 district), 3 Exposure (2), 4 Exposure (3 max). Restricted to Established+ (not expansion). Partial resolution if some districts fail restriction | Art 02 §6–§7 |
| Effect duration | ✓ | PresenceToken placement = Permanent board state; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Network +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.up_to_three — valid zone references; restriction checks Established+ per district (valid zone conditions) | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); Exposure × 2+ cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Districts named at Phase B; restriction per district at Beat 0 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
NET.PA.2 = Card(
    id      = "NET.PA.2",  version="v1.0",
    name    = "Community Rally",
    tagline = "Mobilize communities across Network's established presence network.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,

    layer    = Territory,  function = Add,  subject = PresenceToken,

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

    target_district = district.up_to_three,  # 1–3 districts named at Phase B; each must be Established+
    target_faction  = None,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Network).influence_tier(district.each_target) >= Established,
    cost        = resource.faction(Network).exposure * 2 + resource.district(each_target).native * 1,
    # cost = 2 Exposure + 1 district native per targeted district

    success     = (
        district.each(target).faction(Network).presence += 1,
        faction(Network).standing += 1,
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Network: PortraitEntry(submitter=+1)},

    narrative    = "Network presence does not require a march. It requires a broadcast and the communities that were already listening.",
    perspectives = {
        Network:     "We are already there. This makes it visible.",
        Syndicate:   "Network deepens without purchasing. No Accord, no offer fee, no formal mechanism. The community already listening becomes the position. Efficient.",  # aligned
        Directorate: "Network consolidates three Established positions simultaneously without a single permit or notification. The Directorate marks this as unregulated expansion and files accordingly.",  # opposed
    },
    design_note  = "Broadcast-derived presence PA. Deepens existing foothold (Established+) rather than expanding into new territory. Scaling cost: 2 Exposure (1 district), 3 (2 districts), 4 (3 districts). Partial resolution: if a named district fails Established+ restriction at Beat 0, that district is dropped from resolution; remaining valid districts proceed; cost already committed. Replaces Open Record Request (unworkable) Cost reasoning: District native resources represent the local on-the-ground support required to organize a massive rally.",
    arbiter_note = "Phase B: Network names 1–3 districts. Cost calculated (2 + extras) and committed. Beat 0: check each named district for Established+ restriction. Drop invalid districts from resolution. Beat 4: place 1 presence token in each valid district. Network +1 PS.",
)
```

---

### Network — LIVE COVERAGE
[↑ Public Acts](#network-public-acts)

#### Design Rationale
Network's forced-transparency PA — the broadcaster turns its full institutional reach on a named faction and makes them The Story. The declaration is public and immediate: from the next Covert Dispatch, the named faction is under live coverage. They must choose each Covert Dispatch whether to cooperate (hand face-up on the table, covert ops proceed) or go dark (dispatch case disabled this Month, hand stays hidden). The scrutiny doesn't end by fighting it; it ends when the faction gives the interview.

Comply for one full Covert Dispatch → card clears. The faction has been transparent enough; Network moves on. The strategic question is *when* to give the interview — a faction holding strong ops for Month 3 may choose to absorb the disability in Month 2 to protect the play, then comply in Month 3 when there's less to expose.

*Note: cards laid face-up during compliance are still "in hand" for all game purposes — card counts, submittability, and eligibility are unchanged. The open hand is a visibility state, not a mechanical restriction.*

*Successor to C40 Option B (Weaponized Transparency, retired S70). Replaces dispatch-case forced-reveal mechanism — hand visibility is the simpler, more narratively grounded L1 mechanism.*

#### Card Story

Network turns its full broadcast infrastructure on a named faction, making them The Story. Under live coverage, that faction faces a choice each Covert Dispatch: open their hand to the table and operate in full view, or go dark and forfeit covert submissions entirely. The scrutiny doesn't end by fighting it — it ends when the faction gives the interview.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Unique PA effect — Seasonal hand-visibility obligation on named faction; comply/resist model with genuine decision friction per Month | Art 00 §7 |
| Voice fit | ✓ | Network perspective (accountability as doctrine) + Directorate counter (institutional authority contested); FactionSpecific PA — two perspectives sufficient | Art 00 §7 |
| Doctrine alignment | ✓ | Network only; Exposure×2; threshold 50; Seasonal persistence; comply-once clearing models natural media-cycle end | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Network) — public declaration of broadcast accountability; Network-exclusive institutional leverage | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ⚠ | Information / Reveal / FactionHand — FactionHand not a registered subject type; needs 04b validation | Art 04b §4, §5 |
| Balance | ✓ | Exposure×2 at threshold 50; comply-to-clear limits maximum duration; resist penalty (covert ops disabled) is real cost; crit adds immediate PS pressure | Art 02 §6–§7 |
| Effect duration | ✓ | Seasonal — clears at Quarter end OR when target complies once (whichever is first) | — |
| Persistence | ✓ | Seasonal; `persistence_condition` = target complied for one Covert Dispatch; `persistence_effect` = Covert Dispatch comply/resist obligation | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Network +1 submitter; FailCrit Network −1 (failed broadcast backfires — reckless accusation without traction); FactionSpecific, no other entries | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no zone restriction | Art 01 §6–§7 |
| Supported by components | ✓ | No new component required — open hand is a physical visibility state, not a board marker; comply/resist is self-policing per Governing Rule 6.1a | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Art 03 §9.0 (Start of Month) provides generalizable Covert Dispatch obligation procedure — Steps 0–2 cover comply/resist for any active PA with this obligation type (04-n77 ✅) | Art 03 §9.0 |
| Data schema validation | ✓ | All §6.1 fields present; FactionHand subject flagged for 04b validation | Art 04 §6.1 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Taxonomy subject:** subject = FactionHand — not a registered subject type. Needs 04b validation pass. (Non-gate — tracked in taxonomy checklist row.)
- **Card ID:** TBD — pending PM05 04-n1 numbering pass. (Non-gate.)

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ S89 | |

```python
NET.PA.3 = Card(
    id      = "NET.PA.3", version="v1.0",
    name    = "Live Coverage",
    tagline = "Force a named faction to play with their hand visible or forfeit covert submissions, each Covert Dispatch for the remaining Months of the Quarter.",
    type    = PublicAct, subtype = FactionSpecific, faction = Network,
    layer   = Information, function = Reveal, subject = FactionHand,  # 04b validation needed
    beat=4, resolution=d100, threshold=50, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type = "Probabilistic", outcome_type=None,
    persistence     = Seasonal,
    persistence_condition = "target_faction complied (open hand) for one full Covert Dispatch this Quarter → card clears at end of that Covert Dispatch; or Quarter end",
    persistence_effect    = "Each Covert Dispatch of remaining Months: target faction elects comply (lay all held cards face-up on table; covert ops proceed normally this Covert Dispatch) or resist (dispatch case disabled this Month — no covert submissions). Comply once → card clears.",
    target_district = None,
    target_faction  = faction(named_opponent),
    target_object   = None,
    target_taxonomy=None,
    affinity        = None,
    restriction     = "target_faction != Network",
    cost        = resource.faction(acting).exposure * 2,
    success     = game.activate(LiveCoverage_obligation, target=faction(target)),
    successcrit = (
        game.activate(LiveCoverage_obligation, target=faction(target)),
        faction(target).standing -= 1,
    ),
    fail        = None,
    failcrit    = faction(acting).standing -= 1,
    portrait    = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The story is already written. The only question is whether the subject chooses the cameras or the consequences.",
    perspectives = {
        Network:     "We are not exposing secrets. We are establishing accountability. The distinction matters to us.",
        Directorate: "Network has appointed itself an oversight authority. The Directorate notes this. It will not be forgotten.",
    },
    design_note  = "Successor to C40 Option B (Weaponized Transparency, retired S70). Hand-visibility model replaces dispatch-case forced-reveal — simpler L1 execution, genuine comply/resist decision friction. Comply once → card clears (the faction gave the interview; Network moves on). Resist → covert submissions disabled that Month; card persists. Natural expiry: Quarter end. SuccessCrit: obligation activates + target −1 PS (story breaks big). FailCrit: Network −1 PS (reckless broadcast, story didn't land). Art 03 Covert Dispatch procedure required (04-n77). Subject = FactionHand — 04b validation needed.",
    arbiter_note = "Network has declared Live Coverage against faction X. Place card in Network's active PA area, face-up; faction X announced. Effect begins next Covert Dispatch. Each Covert Dispatch while Live Coverage is active: at start of Covert Dispatch announce — 'Live Coverage is active against [Faction X]. Faction X: comply (lay all held cards face-up on your table area for Covert Dispatch — cards remain in hand; covert ops proceed) or resist (forfeit covert submissions this Month).' If faction X complies: covert submissions proceed normally; at end of Covert Dispatch, remove Live Coverage from Network's active PA area. If faction X resists: faction X does not open their dispatch case this Covert Dispatch; Live Coverage remains in play. Cards laid face-up during compliance are still counted as in hand. Network identity as declaring faction is already public (Phase B declaration).",
)
```

---


---


---

### NET.MOD.2 — TROLL FARM

*Successor to C40 Option A (Weaponized Transparency). React modifier card — Network faction.*

#### Design Rationale
Network deploys gathered intelligence to damage a faction's reputation at the moment a visible trigger fires. The PS reduction is unblockable — once Network activates the information, the reputational damage cannot be countered or retracted. Operates as a React modifier card per Art 03 §18: Network announces and presents the card on the trigger condition; ARBITER confirms and pauses play.

**S138 format migration + re-verification:** converted from the old dash-placeholder checklist and prose Status to the standard format. This card carries more open issues than a typical format-migration case — three real, unresolved problems, none fixed here: (1) `success = faction(trigger.faction).standing -= 1` is not valid — `-=` is a statement, not an expression, and cannot legally appear as a field value (`schema_cleanup_log.md` item 17, more severe than the fossil-card string-literal gap). (2) Unblockability has no governing rule yet — the card's own prior text already states "Issues Resolved cannot be set until the rule is written"; re-confirmed here, still true. (3) The name itself is still an unconfirmed placeholder. Also carries the cross-resource cost question (Capital, not Network-native) seen on several cards this session.

#### Card Story
A rival's public standing ticks upward — a win, a moment of visibility. Network already has the dossier open. The counter-narrative isn't a rumor; it's sourced, timed, and impossible to walk back once it's live.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence-to-reputation conversion at an opponent's highest-visibility moment fits Network's "no one decides in the dark" doctrine. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `perspectives` field is `None` — no faction-specific reactions written yet. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1 — correctly expresses doctrine. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Network, real taxonomy (Standing/Shift/StandingMarker, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Standing×Shift is the correct cell per the matrix (Add/Remove subsumed by Shift, 04-n173 precedent). | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Unblockable PS −1 is a strong, precedent-setting effect — genuinely can't be finalized while the unblockability governing rule itself doesn't exist. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate at trigger point. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Field not explicitly declared — same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `standing_marker.increased(faction=Any, except=Network)` — confirmed vocabulary, correctly self-excluding (no self-fire ambiguity — the `except=Network` clause already handles what other cards leave implicit). | Art 04 §6.3 |
| Portrait validity | ✓ | Submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | No district reference — correct; this is a Standing-layer effect. | Art 01 §6–7 |
| Supported by components | ⚠ | PS/Standing marker shift would reuse the standard mechanism — but see Supported by game procedure; unblockability itself has no defined component-level enforcement. | Art 02 §6–8 |
| Supported by game procedure | ⚠ **(blocker)** | No Art 03 governing rule exists yet for "unblockable" effects — the card's own prior text already flagged this ("Issues Resolved cannot be set until the rule is written"), re-confirmed on this pass, not resolved. | Art 03 §18; PM05 (unblockability governing rule, untracked by number) |
| Data schema validation | ⚠ **(blocker)** | `success = ... -= 1` is invalid syntax, not a valid MutationExpr (`schema_cleanup_log.md` item 17) — more severe than a missing-field gap; scaffolding added this session for the fields that were simply absent (targets, successcrit/failcrit, ps_framing, boost, resolution_type). | Art 04 §6.1–§6.3; schema_cleanup_log.md item 17 |
| Card narrative | ⚠ | `narrative` field empty; no Card Story existed before this pass — added below. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch (once the expression syntax is eventually corrected). | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Cost spans Exposure (Network-native) and Capital (Syndicate's) — same cross-resource-holding question flagged repeatedly this session. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Any other faction's PS increase is a recurring event — moderate-to-common frequency. |  |
| Firing window (ModReactCard) | ✓ | No other Network card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Automatic is appropriate — deterministic reputational strike, no execution-quality dimension modeled. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not ring-scoped. |  |

**Outstanding Issues (carried, pre-S138):**
- **Card name:** "Troll Farm" is still a placeholder — confirm before sign-off.
- **Unblockability formalization:** Art 03 governing rule still doesn't exist — gates Issues Resolved.
- **Invalid expression syntax (new, S138):** `success` field needs a real MutationExpr, not `-=`.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

```python
NET.MOD.2 = Card(
    id      = "NET.MOD.2",  card_id = "NET.MOD.2",  version = "v0.1",
    name    = "Troll Farm",  # placeholder name — confirm before sign-off
    tagline = "The narrative was already moving. We just changed where it was going.",
    type    = ModReactCard,  faction = Network,
    layer   = Standing,  function = Shift,  subject = StandingMarker,  # assigned S137 (04-n175) — fields were entirely undeclared before, not just None; effect is standing -= 1
    trigger = standing_marker.increased(faction=Any, except=Network),
              # fires when any other faction's standing marker increases (publicly observable)
    ring_constraint = None,  ring_origin = None,  value_rating = None,
    beat    = None,  resolution = Automatic,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    target_district = None,  target_faction = trigger.faction,  target_object = None,  target_taxonomy = None,  # scaffolding only — added S138 (04-n177)
    cost    = resource.faction(Network).exposure * 1 + resource.faction(Network).capital * 1,
    boost   = None,  # scaffolding only — added S138 (04-n177)
    success = faction(trigger.faction).standing -= 1,  # ⚠ INVALID SYNTAX — `-=` is a statement, not an expression; flagged, not fixed (schema_cleanup_log.md item 17). Unblockable — governing rule TBD; see Outstanding Issues
    successcrit = None,  fail = None,  failcrit = None,  on_accept = None,  on_decline = None,  # scaffolding only — added S138 (04-n177)
    restriction = None,
    portrait = {Network: PortraitEntry(submitter=+1)},
    ps_framing = None,  # scaffolding only — added S138 (04-n177)
    narrative = None,  perspectives = None,  arbiter_note = None,
    design_note = "Network activates an Intel dossier the moment a faction's standing increases — converting gathered intelligence into immediate reputational damage at the opponent's highest-visibility moment. PS −1 is unblockable: once the information releases, retraction is impossible. Governing rule for unblockability outstanding — address alongside any second bypass-capable card. Trigger is standing_marker.increased (publicly observable, §5 P5 compliant). Does not fire on Network's own standing increases. card_id = NET.MOD.2 Cost reasoning: Capital funds the server farms and botnets needed to rapidly manufacture the public narrative.",
)
```

---

---

### NET.PA.4 — GRASSROOTS PROTEST *(stub)*
[↑ Public Acts](#network-public-acts)

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
NET.PA.4 = Card(
    id      = "NET.PA.4",  version = "v1.1",
    name    = "Grassroots Protest",
    tagline = "Mobilize the masses to physically drown out an opponent's influence.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Territory,  function = Remove,  subject = PresenceToken,
    beat    = 4,  resolution = d100,  threshold = 60,
    cost    = resource.faction(Network).exposure * 1 + district_native(target_district) * 1,
    success = "Remove 1 target_faction's Presence Token from target_district. Target faction loses 1 PS. Network gains +1 PS.",
    design_note = "A loud territorial disruption. Burns Exposure and local resources to physically remove an opponent's token while shifting the PR balance."
)
```

---

### NET.PA.5 — VIRAL OUTRAGE *(stub)*
[↑ Public Acts](#network-public-acts)

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
NET.PA.5 = Card(
    id      = "NET.PA.5",  version = "v1.1",
    name    = "Viral Outrage",
    tagline = "Weaponize an opponent's own assets against them to tank their standing.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Standing,  function = Shift,  subject = StandingMarker,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Network).exposure * 2 + resource.faction(target_faction).native * 1,
    success = "Target faction loses 3 Public Standing. Network gains +1 PS.",
    design_note = "Pure PR assassination. Network burns the opponent's own native resource to fuel the smear campaign."
)
```

---

### NET.PA.6 — CROWDFUNDING CAMPAIGN *(stub)*
[↑ Public Acts](#network-public-acts)

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
NET.PA.6 = Card(
    id      = "NET.PA.6",  version = "v1.1",
    name    = "Crowdfunding Campaign",
    tagline = "Convert public goodwill into hard resources.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Economy,  function = Add,  subject = AnyResource,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Network).exposure * 1,
    success = "Network names a resource type. Network gains 1 of that resource type for every 4 points of positive Public Standing they currently have.",
    design_note = "Network's economy is driven by their audience. This rewards them for maintaining a high, positive PS track by converting it into any resource they need."
)
```

### NET.MOD.1 — PIRATE TRANSMITTER

*S106. Network React Modifier — Territory|Add|PresenceToken. Successor B to Weaponized Transparency (retired S70, 04-n47/04-n48).*

#### Design Rationale
Network's opportunistic presence card. Fires when any PA success causes a board state change (influence chip or structure block placed or removed) in a district. The act of change is publicly observable — qualifying trigger. Network announces Pirate Transmitter and rolls d100. On success: 1 Network chip placed in the changed district. The card does not require Network to have existing presence; the PA's visibility is the only entry condition. On successcrit: additional +1 PS — the signal lands publicly as well as physically. Failcrit: −1 PS — the insertion attempt is noticed and goes badly.

**S138 format migration + re-verification:** this card (S106-vintage) predates the current 4-block format (`structure_pass=0`) — converted here, not just reformatted. This is the first genuinely d100-resolution ModReactCard seen in the full review pass (everything else has been `Automatic`) — `resolution=d100, threshold=50` is schema-valid (unlike GHO.MOD.1's invalid `Prediction`), a legitimate design choice for modeling execution risk on a covert insertion. Two real findings on re-verification: the old Taxonomy fit row claimed Modifier cards are excluded from the taxonomy matrix (Art 04b §9) — the same stale claim already corrected elsewhere via 04-n175/S133 (ModReactCard is the exception, not excluded); and the trigger's `PA_success.where(...)` syntax and the bare `acting` keyword both predate confirmed §6.3 vocabulary — logged as `schema_cleanup_log.md` item 15.

#### Card Story
The district was already moving. Network didn't start the change — it arrived at the same time the change did.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Re-verified: opportunistic chip placement on any publicly-observable PA board-state change fits Network's reach-first doctrine. | Art 00 §7 |
| Voice fit | ✓ | Re-verified: perspective ("we don't need to create the disruption...") lands the doctrine. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Re-verified: no prior presence required — doctrinal reach-first, matches Network's "no one gets to decide this in the dark" identity. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | Re-verified: ModReactCard, correctly not a CovertOperation. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | **Corrected on re-verification:** the old row claimed Modifier cards are matrix-excluded (Art 04b §9) — stale, same category as the claim already corrected on GHO.MOD.1/other cards at S133/04-n175. Real taxonomy (Territory/Add/PresenceToken) is valid: Territory×Add confirmed in the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Re-verified, flag still open: broad trigger (any PA board-state change table-wide) + no presence requirement is a real balance question, same shape as the "least-gated" cards flagged elsewhere this session (DIR.MOD.7, GUI.MOD.2/8). | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate — chip placed at the Beat 4 trigger point. | Art 04 §5 P19 |
| Persistence | ✓ | Explicitly declared (`persistence=Immediate`) — ahead of most of the corpus on this field. | Art 04 §6.2 |
| Trigger validity | ⚠ | Downgraded on re-verification: the underlying event (a PA causing a board-state change) is genuinely publicly observable, but `PA_success.where(...)` is legacy syntax predating confirmed §6.3 forms — item 15. | Art 04 §6.3; schema_cleanup_log.md item 15 |
| Portrait validity | ✓ | Re-verified: submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Re-verified: `target_district` fixed by trigger, not a free choice. | Art 01 §6–7 |
| Supported by components | ✓ | Re-verified: chip placement and Exposure cost both standard. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Re-verified: Beat 4 React, reuses existing Art 03 §18 React rules. | Art 03 §18 |
| Data schema validation | ⚠ | Scaffolding-complete on the fields it has (`persistence`, `outcome_type`, targets all explicitly declared — ahead of most of the corpus), but `PA_success.where(...)`/`acting` legacy syntax (item 15) is a real, unresolved schema-currency gap, not just missing placeholders. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Re-verified: Card Story + `narrative` field both present and well-formed — ahead of most of the corpus, which needed a Card Story written this session. | Art 04 §5 P26 |
| Outcome determinacy | ✓ | Genuine two-branch outcome via a real d100 roll (not the invalid `Prediction` pattern GHO.MOD.1 used) — success/successcrit/fail/failcrit all properly structured. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Exposure×1, Network-native — no cross-resource question. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ⚠ | Any PA board-state change table-wide is a broad, likely-frequent trigger. Ties into the Balance flag. |  |
| Firing window (ModReactCard) | ✓ | No other Network card shares this exact trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | d100 is the right call here — this models a genuine insertion-attempt risk (crit/fail bands shift PS), unlike the flat Automatic effects seen elsewhere in the corpus. First such example reviewed this session. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus: 2 copies → 2 independent rolls per qualifying PA? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint` unset/None — correct; fires table-wide by design. |  |

**Outstanding Issues (carried, pre-S138):**
- Board state change definition (influence chip vs. structure block vs. PS/resource/Intel changes) — not resolved by this content-review pass, out of scope here.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

```python
NET.MOD.1 = Card(
    id      = "NET.MOD.1",  card_id = "NET.MOD.1",  version = "v1.0",
    name    = "Pirate Transmitter",
    tagline = "A public action changes the district. The signal finds the opening.",
    type    = ModReactCard,  faction = Network,
    layer   = Territory,  function = Add,  subject = PresenceToken,  # assigned S137 (04-n175) — fields were entirely undeclared before, not just None; effect is presence_chips.add(1)
    trigger = PA_success.where(effect.causes_board_state_change(district)),
              # fires on any PA success that places or removes an influence chip
              # or structure block in any district; target = that district
    target_district = district(trigger.target),
    beat    = 4,  resolution = d100,  threshold = 50,
    ring_mod=None,  doctrine_mod=None,  outcome_type=None,
    persistence=Immediate,  persistence_condition=None,  persistence_effect=None,
    target_faction=None,  target_object=None,  target_taxonomy=None,
    affinity=None,  restriction=None,
    cost    = resource.faction(acting).exposure * 1,
    success = faction(acting).presence_chips(district(target)).add(1),
    successcrit = faction(acting).standing.add(1),
    fail    = None,
    failcrit = faction(acting).standing.remove(1),
    on_accept=None,  on_decline=None,
    portrait = {Network: PortraitEntry(submitter=+1)},
    narrative   = "The district was already moving. Network didn't start the change — it arrived at the same time the change did. Two signals crossing in the open.",
    perspectives = {Network: "We don't need to create the disruption. We need to be in position when it happens."},
    design_note  = "Trigger: any PA success that causes a board state change (influence chip or structure block placed or removed in district). Target district fixed by trigger — not a free choice. No restriction on Network existing presence. Modifier card schema fields are CA-convention placeholders pending 04-n4.",
    arbiter_note = "Beat 4: when a PA success produces a board state change in district X (influence chip count changes, or structure block placed/removed), Network may announce Pirate Transmitter. Confirm trigger validity. Network spends 1 Exposure and rolls d100 (threshold 50, usual modifiers). Success: place 1 Network chip in district X. Successcrit: +1 PS additional. Fail: no effect. Failcrit: −1 PS.",
)
```

---

### NET.MOD.3 — BACKUP SERVER RACKS

#### Design Rationale
Standing-recovery React: fires on Network's own PS decrease and negates some or all of it. Real gap, already flagged in the card's own comment, not invented here: `success = faction(Network).standing.add(TBD)` — the magnitude is a literal placeholder, not a real number. `cost=None` also carries an unresolved TBD note, same as DIR.MOD.1's family.

#### Card Story
Network's standing takes a public hit. Before the damage settles, the redundant infrastructure kicks in — a backup narrative, already staged, absorbing some of the fallout before anyone finishes reacting to the first one.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Self-directed PS recovery enabling a designed sacrifice-and-recover arc (pairs with NET.CA.2/NET.CA.6) is a coherent, doctrinally central Network beat. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; this is a mechanical recovery valve, not a doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Network, real taxonomy (Standing/Shift/StandingMarker, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Standing×Shift valid per the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Cannot assess: the recovery magnitude is a literal `TBD`, and `cost` is an unresolved TBD comment. Real design work needed before this row can close. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `standing_marker.decreased(faction=Network)` — confirmed vocabulary, self-scoped, no ambiguity. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; not a territory effect. | Art 01 §6–7 |
| Supported by components | ✓ | Standard PS/standing-marker mechanism, once the magnitude is resolved. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing PS-decrease event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ | `success` magnitude is a literal `TBD` — not a schema-format issue (the field is present and correctly typed as a mutation call), but a genuine unresolved content gap. Scaffolding added this session (04-n177) for the fields that were simply absent. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch (once the magnitude is resolved). | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | `cost=None` with an unresolved TBD comment — cannot close; ties to 04-n178 (whole-set Floor Act/value_rating decision) but also has its own unresolved magnitude question independent of that. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Gated on Network's own PS decreasing — frequency depends on how often Network takes PS hits, reasonably self-limiting. |  |
| Firing window (ModReactCard) | ✓ | No other Network card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat recovery, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. React on Network PS loss. Enables Sacrifice (NET.CA.2 Disclosure Loop) + recovery arc. Network manages its own signal — what the public hears is what Network decides they hear. S138: full content-review pass — Balance/Resource cost positioning cannot close (magnitude is a literal TBD, cost is an unresolved TBD note); this is genuinely unfinished design work, not a formatting gap. Design Pass ✓, Issues Resolved not yet.*

```python
NET.MOD.3 = Card(
    id      = "NET.MOD.3",  card_id = "NET.MOD.3",  version = "v0.1",
    name    = "Backup Server Racks",
    tagline = "When Network loses standing, redirect the narrative before it lands.",
    type    = ModReactCard,  faction = Network,
    layer   = Standing,  function = Shift,  subject = StandingMarker,  # assigned S137 (04-n175) — magnitude is a literal TBD in the effect below, real gap not invented here

    trigger         = standing_marker.decreased(faction=Network),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = Network,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,  # card consumed; cost TBD (possibly 1 Exposure)
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = faction(Network).standing.add(TBD),  # negate some or all of triggering decrease; magnitude TBD
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "PS recovery React. Fires when Network's own PS decreases by any cause. Partially or fully negates the loss — magnitude TBD at design pass. Enables Disclosure Loop (NET.CA.2) sacrifice + immediate recovery as a designed arc rather than a liability. Pairs with NET.CA.6 Sacrifice (PS→Intel) — the spend-and-recover cycle makes Network's PS expenditure feel controlled rather than punitive.",
    arbiter_note = None,
)
```

---

### NET.MOD.4 — AMPLIFICATION ARRAY

#### Design Rationale
First of the NET.MOD.4/5 broadcast-driven expansion family: fires on `broadcast_card.placed` (db25, the public SitRep card), a table-wide event with no faction-scoping at all (no self-fire question — it's not tied to any faction's action, just a phase event). Network extends into a district where it already has presence, player's choice among qualifying districts.

#### Card Story
The Situation Report lands — public, unavoidable, read by everyone at the table. Network's existing footholds don't need new orders; the signal simply reaches further the moment the news does.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "Every public information event is a Network signal event" is a clean, doctrinally central beat. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; routine passive expansion, not a doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Network, real taxonomy (Territory/Add/PresenceToken, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory×Add valid per the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Fires 1–2 times/Quarter (Upkeep SitRep + possible Beat 5) per design_note — bounded, moderate; final read pending 04-n178. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | `broadcast_card.placed` — confirmed §6.3 vocabulary (db25, fires at Upkeep phase 1 and Beat 5 phase 18). Not faction-scoped, so no self-fire ambiguity applies. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Player-choice targeting among Network's existing-presence districts — a normal targeting mechanic. | Art 01 §6–7 |
| Supported by components | ✓ | Standard chip-placement mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses the existing Broadcast Card placement event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch; player-choice target isn't a probabilistic outcome. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set gate as the rest of the corpus. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ | Bounded: 1–2 fires/Quarter per design_note (Upkeep SitRep + possible Beat 5) — not underfire or overfire. |  |
| Firing window (ModReactCard) | ⚠ | NET.MOD.5 (Ring-2 variant of this same family) shares the identical `broadcast_card.placed` trigger — same family-overlap flag as other multi-card families this session. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat expansion, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; unconstrained (ring-constrained variant is NET.MOD.5). |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. React on broadcast_card.placed (db25 — public SitRep card in Situation Report Zone). Fires at Upkeep SitRep and Beat 5. Generic variant — any district where Network already has presence. Ring-constrained variant: NET.MOD.5 (Mid ring). S138: full content-review pass — confirmed no self-fire ambiguity (trigger isn't faction-scoped); family firing-window overlap with NET.MOD.5 flagged. Design Pass ✓, Issues Resolved not yet.*

```python
NET.MOD.4 = Card(
    id      = "NET.MOD.4",  card_id = "NET.MOD.4",  version = "v0.1",
    name    = "Amplification Array",
    tagline = "When news breaks publicly, the Network's signal extends.",
    type    = ModReactCard,  faction = Network,
    layer   = Territory,  function = Add,  subject = PresenceToken,  # assigned S137 (04-n175) — arbiter.place(presence_chip,...)

    trigger         = broadcast_card.placed,  # db25 — SitRep card placed in Situation Report Zone
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = faction(Network).district.any,  # any district where Network has presence
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Network).any_presence,  # must have at least 1 district with presence
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.place(presence_chip, district=faction(Network).district.acting_choice, faction=Network, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Presence expansion React on broadcast_card.placed (db25, public SitRep card). Every public information event is a Network signal event — the story expanding means the Network's reach expands. Network selects which existing-presence district receives the chip. Fires 1–2 times per Quarter (Upkeep SitRep + possible Beat 5). Delivers §5a 'broadcast-derived presence' at the modifier card level.",
    arbiter_note = None,
)
```

---

### NET.MOD.5 — INFRASTRUCTURE SIGNAL

#### Design Rationale
Ring 2-constrained variant of NET.MOD.4 — same broadcast trigger, narrowed to Mid ring presence. No self-fire ambiguity (trigger isn't faction-scoped).

#### Card Story
The same public broadcast reaches everywhere, but Network's Mid-ring footholds — the infrastructure districts — are where the signal has the most to build on. The reach deepens exactly where Network is already consolidated.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Consolidating reach in Mid-ring infrastructure districts is a coherent, distinct escalation from NET.MOD.4's generic scope. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — same reasoning as NET.MOD.4. | Art 04 §6.5 |
| Card type fit | ✓ | Same shape as NET.MOD.4. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Territory×Add cell. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | Same bounded frequency as NET.MOD.4, narrower scope (Ring 2 only) — reasonable tiering. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ✓ | Same confirmed `broadcast_card.placed` trigger as NET.MOD.4. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `ring_constraint=2` matches the restriction's Ring-2 presence check. | Art 01 §6–7 |
| Supported by components | ✓ | Same as NET.MOD.4. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same as NET.MOD.4. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set gate as NET.MOD.4. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ | Same bounded frequency as NET.MOD.4, gated additionally on Ring 2 presence. |  |
| Firing window (ModReactCard) | ⚠ | Confirmed overlap with NET.MOD.4 — identical `broadcast_card.placed` trigger; if Network holds both and qualifies for both, no documented rule on whether both fire on the same event. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same as NET.MOD.4. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=2` correctly matches the restriction's scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. Ring-constrained variant of NET.MOD.4. Fires only when SitRep fires and Network has presence in a Mid ring (Ring 2) district. Mid ring is the consolidation zone — this card deepens Network's reach in established infrastructure. S138: full content-review pass — confirmed firing-window overlap with NET.MOD.4 (identical trigger). Design Pass ✓, Issues Resolved not yet.*

```python
NET.MOD.5 = Card(
    id      = "NET.MOD.5",  card_id = "NET.MOD.5",  version = "v0.1",
    name    = "Infrastructure Signal",
    tagline = "Public broadcasts amplify Network reach in established infrastructure districts.",
    type    = ModReactCard,  faction = Network,
    layer   = Territory,  function = Add,  subject = PresenceToken,  # assigned S137 (04-n175), same shape as NET.MOD.4

    trigger         = broadcast_card.placed,  # db25
    beat            = None,
    ring_constraint = 2,  # fires only in context of Ring 2 (Mid ring) districts
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = faction(Network).district.ring(2).any,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Network).presence_in_ring(2),
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.place(presence_chip, district=faction(Network).district.ring(2).acting_choice, faction=Network, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Ring 2–constrained variant of NET.MOD.4 (Amplification Array). Same trigger (broadcast_card.placed, db25) but fires only if Network has Mid ring presence; places chip in a Mid ring district. Deepens Network's Mid ring footprint each time public information spreads — Infrastructure districts amplify the signal.",
    arbiter_note = None,
)
```

---

### NET.MOD.6 — STREET-LEVEL AGITATOR

#### Design Rationale
Opportunistic Baryo (Ring 3) expansion React. Real findings this pass: (1) `faction=Any` in the trigger carries the same self-fire question as items 5/6/7/8/10/11 across the Directorate/Ghost/Guild sets — Network placing its own chip in Baryo would trigger this against itself. (2) An internal inconsistency between fields: `target_district = ...adjacent_to(trigger.district)` declares adjacency-based targeting, but the `success` mutation actually reads `faction(Network).district.ring(3).acting_choice` — any Ring-3 district with Network presence, not specifically adjacent ones. The design_note itself already flags this as unresolved ("adjacent — TBD at design pass"), confirming this isn't invented here — but the `target_district` field and the `success` field currently disagree with each other, which is sharper than a simple TBD.

#### Card Story
Someone moves a piece in the Baryo — anyone, doesn't matter who. Network's community network doesn't need an invitation; where there's motion in the slums, Network's people are already talking to someone.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Opportunistic community-network expansion in Baryo fits Network's "territorial signature" per the design_note. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; routine opportunistic expansion. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Network, real taxonomy (Territory/Add/PresenceToken, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory×Add valid per the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Cannot fully assess: the target scope itself is internally inconsistent (adjacency-declared vs. any-Ring-3-district-actual) — the effective power of this card depends on which scope is correct. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | `presence_chip.placed(faction=Any, ring=3)` — confirmed vocabulary, but `faction=Any` carries the same self-fire question as items 5/11 (Network triggering on its own Baryo placement). | Art 04 §6.3; schema_cleanup_log.md item 5 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ⚠ | **Real inconsistency:** `target_district` field declares `adjacent_to(trigger.district)`, but `success` actually resolves against `faction(Network).district.ring(3).acting_choice` — any Ring-3 Network-presence district, not specifically adjacent ones. The two fields disagree; not resolved here. | Art 01 §6–7 |
| Supported by components | ✓ | Standard chip-placement mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing chip-placement event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set gate as the rest of the corpus. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ⚠ | Any faction's Baryo placement is common — potentially high frequency; ties into the Balance flag. |  |
| Firing window (ModReactCard) | ✓ | No other Network card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat expansion, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=3` matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. React on any presence placement in Baryo (Ring 3). When any faction moves in Baryo, Network's community reach follows — opportunistic Baryo expansion is Network's territorial signature. S138: full content-review pass — confirmed the design_note's own admitted adjacency-vs-own-district gap is a real field-level inconsistency (target_district says adjacent, success reads any Ring-3 district); self-fire question flagged (item 5 family). Design Pass ✓, Issues Resolved not yet.*

```python
NET.MOD.6 = Card(
    id      = "NET.MOD.6",  card_id = "NET.MOD.6",  version = "v0.1",
    name    = "Street-level Agitator",
    tagline = "When anyone moves in the Baryo, Network's voice follows.",
    type    = ModReactCard,  faction = Network,
    layer   = Territory,  function = Add,  subject = PresenceToken,  # assigned S137 (04-n175), same shape as NET.MOD.4/5

    trigger         = presence_chip.placed(faction=Any, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = faction(Network).district.ring(3).adjacent_to(trigger.district),
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Network).any_presence,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.place(presence_chip, district=faction(Network).district.ring(3).acting_choice, faction=Network, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Opportunistic Baryo expansion React. When any faction places presence in Ring 3 (Baryo), Network may place 1 chip in any Ring 3 district where it has presence (or adjacent — TBD at design pass). Network's community-relationship model means others' activity in Baryo draws Network in. Delivers §5a 'wide Presence coverage, Baryo outward' at the modifier deck level.",
    arbiter_note = None,
)
```

---

### NET.MOD.7 — COMMUNITY AMPLIFIERS

#### Design Rationale
Hand-growth engine reacting to any PA resolution, with a differential yield (3 vs. 2) if Network itself was the resolving faction — a deliberate self-inclusive design (not the "possible bug" self-fire pattern), rewarding Network's own activity more than others'. Real finding: `public_act.resolved(faction=Any)` is not confirmed §6.3 vocabulary — the confirmed submission-time event is `public_act.placed_on_frg`; a resolution-time event is a documented, still-pending gap (design_reference_card_system.md's "still pending" list flags `public_act.resolved(pa=X)` by name, in the context of Overture). Also: `if_acting_faction=Network, then_count=3` is a conditional-branching argument form with no established MutationExpr precedent.

#### Card Story
A public act resolves — anyone's, doesn't matter whose. The city gets louder, and Network's monitoring apparatus pulls something useful out of the noise every time. When it's Network's own act landing, the take is even better.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Turning public state changes into hand advantage, self-preferential but table-wide, fits Network's "feed on the noise" doctrine. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("the louder the city gets, the more they listen") lands the doctrine. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; passive economic engine, not a doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Network, real taxonomy (Economy/Add/ModifierCard, 04-n175), matches GUI.MOD.5's shape. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy×Add valid; ModifierCard-as-subject consistent with the established precedent from GUI.MOD.5/NET.MOD.9/14. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Any-PA-resolution is a very broad, likely-frequent trigger with no cost — real balance attention warranted, similar shape to the "least-gated" flags elsewhere this session. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | `public_act.resolved(faction=Any)` is not confirmed §6.3 vocabulary — a resolution-time PA event is a documented, still-open gap (design_reference_card_system.md's pending list), distinct from the confirmed submission-time `public_act.placed_on_frg`. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; not a territory effect. | Art 01 §6–7 |
| Supported by components | ✓ | Modifier card draw reuses the standard Upkeep-draw mechanism. | Art 02 §6–8 |
| Supported by game procedure | ⚠ | Depends on the same unconfirmed resolution-time trigger noted above — the underlying event (PA resolving at Beat 4) is real, but the trigger term isn't yet formalized. | Art 03; GR 6.1 |
| Data schema validation | ⚠ | Scaffolded this session (04-n177). Also: `if_acting_faction=Network, then_count=3` is a conditional-branching MutationExpr argument form with no established precedent — worth a look alongside the broader "no confirmed MutationExpr vocabulary" gap (schema_cleanup_log.md item A). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch (the count itself branches on a board-state fact, not a hidden or probabilistic outcome). | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` on a very broad, frequent trigger — same whole-set gate, sharpened by the Balance flag. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ⚠ | Any PA resolving, table-wide, every Month — likely one of the highest-frequency triggers reviewed this session. Ties directly into the Balance flag. |  |
| Firing window (ModReactCard) | ✓ | No other Network card shares this exact trigger (contrast with NET.MOD.9/14, which key off different events). |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat draw with a conditional count, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*React on any Public Act resolution. Feeds the Network's hand when the board gets loud. S138: full content-review pass — `public_act.resolved` confirmed as an already-documented pending vocabulary gap (not newly found); real balance concern given the broad, cost-less, high-frequency trigger. Design Pass ✓, Issues Resolved not yet.*

```python
NET.MOD.7 = Card(
    id      = "NET.MOD.7",  card_id = "NET.MOD.7",  version = "v0.1",
    name    = "Community Amplifiers",
    tagline = "The louder the city gets, the more they listen.",
    type    = ModReactCard,  faction = Network,
    layer   = Economy,  function = Add,  subject = ModifierCard,  # assigned S137 (04-n175) — arbiter.draw_modifier(count=2/3), matches GUI.MOD.5's shape

    trigger         = public_act.resolved(faction=Any),
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

    success     = arbiter.draw_modifier(faction=Network, count=2, if_acting_faction=Network, then_count=3),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Net growth engine. Draws 2 cards on any PA, or 3 if Network resolved it. Transforms public state changes into hand advantage.",
    arbiter_note = None,
)
```

---

### NET.MOD.8 — FREQUENCY SPLITTER

#### Design Rationale
Chain-enabler React: fires on a Network modifier card being placed and replaces itself while dropping a Baryo chip. Two real findings: (1) `modifier_card.placed(faction=Network)` is not confirmed §6.3 vocabulary. (2) More significant — the design_note's "replaces itself" framing raises a genuine question of whether this card's own placement re-triggers itself, creating an unbounded recursive draw-and-place loop rather than a bounded chain. Logged as `schema_cleanup_log.md` item 18, flagged not resolved. Also worth noting: the district scope (Ring 3/Baryo) isn't motivated by anything in the trigger or restriction itself (`restriction=faction(Network).any_presence`, not Ring-3-specific) — the Baryo targeting reads as an arbitrary design choice rather than a mechanically justified one.

#### Card Story
One signal splits into a dozen relays, and each relay is capable of splitting again. Every time Network plays one of these cards, another is already queued up behind it — the noise doesn't stop, it compounds.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A self-sustaining "noise compounds" engine fits Network's broadcast-volume doctrine, distinct from the other passive-expansion cards. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("a single broadcast splinters into a dozen channels") lands the doctrine. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; mechanical chain engine, not a doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Network, real taxonomy (Territory/Add/PresenceToken, 04-n175 — Andy's correction that the chip is the primary gain, the modifier draw is the chain-enabler). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory×Add valid per the matrix. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ **(potential blocker)** | Cannot assess until the self-triggering question is resolved: if this card's own placement re-triggers itself, the effective yield is unbounded per Quarter, a materially different balance profile than a single bounded chain link. | Art 02 §6–7; Art 04 §6.5; schema_cleanup_log.md item 18 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | `modifier_card.placed(faction=Network)` isn't confirmed §6.3 vocabulary — item 18. | Art 04 §6.3; schema_cleanup_log.md item 18 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ⚠ | District scope (Ring 3/Baryo) isn't motivated by the trigger or restriction — reads as an arbitrary choice, not a mechanically grounded one. | Art 01 §6–7 |
| Supported by components | ✓ | Modifier draw and chip placement both reuse standard mechanisms. | Art 02 §6–8 |
| Supported by game procedure | ⚠ | Same self-triggering-loop question as Balance — if unbounded, this needs an explicit ARBITER-facing limiter procedure that doesn't currently exist. | Art 03; GR 6.1; schema_cleanup_log.md item 18 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch (bundled mutation list, not a choose_one). | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set gate, sharpened by the potential-loop concern above. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ⚠ | Cannot assess without resolving the self-triggering question — could be a single chain link or a recursive loop. |  |
| Firing window (ModReactCard) | ✓ | No other Network card shares this exact trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat draw-and-place, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus, compounded by the self-triggering question. |  |
| Ring constraint (ModReactCard) | ✓ (N/A) | `ring_constraint` not set — the Ring 3 targeting is baked into `success`/`target_district`, not expressed via this field; consistent field usage, if not a well-motivated design choice (see Supported by zones). |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*React on Network Modifier card placed. Links Reacts together sequentially. S138: full content-review pass — real finding: the "replaces itself" framing may describe an unbounded self-triggering loop rather than a bounded chain (item 18); this blocks Balance/Trigger frequency/Supported-by-procedure from closing. Design Pass ✓, Issues Resolved not yet.*

```python
NET.MOD.8 = Card(
    id      = "NET.MOD.8",  card_id = "NET.MOD.8",  version = "v0.1",
    name    = "Frequency Splitter",
    tagline = "A single broadcast splinters into a dozen channels.",
    type    = ModReactCard,  faction = Network,
    layer   = Territory,  function = Add,  subject = PresenceToken,  # assigned S137 (04-n175, Andy's correction) — the presence chip is the net gain; the count=1 modifier draw is the self-replacing chain-enabler, not the card's primary identity

    trigger         = modifier_card.placed(faction=Network),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = faction(Network).district.ring(3).acting_choice,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Network).any_presence,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = list([arbiter.draw_modifier(faction=Network, count=1), arbiter.place(presence_chip, district=target_district, faction=Network, count=1)]),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Chain enabler. Triggers off Network placing a ModReact card. Replaces itself and drops Baryo presence, letting them stack noise sequentially.",
    arbiter_note = None,
)
```

---

### NET.MOD.9 — BANDWIDTH OVERRIDE

#### Design Rationale
High-yield hand-flooder reacting to a district going Contested. Real finding: `status_marker.contested.placed()` is legacy syntax for the same event confirmed §6.3 vocabulary already calls `tension_marker.placed` (used correctly by GUI.MOD.10 and others) — logged as `schema_cleanup_log.md` item 16. Also carries the cross-resource cost question (Findings, not Network-native) seen repeatedly this session.

#### Card Story
A district tips into open contest — three or more factions locked at a tie, no clear winner. The chaos itself is signal. Network's monitoring floods with usable material the moment the board gets messy.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | "Conflict creates the ultimate engagement metric" is a sharp, doctrinally coherent hook for a high-yield draw engine. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; mechanical engine, not a doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Network, real taxonomy (Economy/Add/ModifierCard, 04-n175), clean single-effect. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Economy×Add cell as GUI.MOD.5/NET.MOD.7/14. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | Real 2-resource cost for a 4-card draw, gated on the genuinely rare Contested board state — design_note's "no hand limit, hold indefinitely" framing is consistent with a deliberate stockpiling design. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | Underlying event (district goes Contested) is genuinely publicly observable, but `status_marker.contested.placed()` is legacy syntax — confirmed vocabulary is `tension_marker.placed` (item 16). | Art 04 §6.3; schema_cleanup_log.md item 16 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; the effect isn't district-scoped even though the trigger is. | Art 01 §6–7 |
| Supported by components | ✓ | Modifier card draw reuses the standard mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses the existing Contested/Tension-marker event; no new ARBITER behavior once the trigger term is normalized. | Art 03; GR 6.1 |
| Data schema validation | ⚠ | Scaffolded this session (04-n177); legacy trigger term also a schema-currency gap (item 16). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Real cost specified, but spans Exposure (Network-native) and Findings (Ghost's) — same cross-resource-holding question flagged on several cards this session. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ | Contested is a specific, less-common board state — low-moderate frequency, matching the "high-yield, rare trigger" design intent. |  |
| Firing window (ModReactCard) | ✓ | No other Network card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat draw, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; Contested can occur in any ring. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*React on district becoming Contested. High-yield payload when the board gets messy. S138: full content-review pass — confirmed `status_marker.contested.placed()` as legacy syntax for the already-confirmed `tension_marker.placed` event (item 16); cross-resource cost flagged. Otherwise one of the cleaner cards in the Network set. Design Pass ✓, Issues Resolved not yet.*

```python
NET.MOD.9 = Card(
    id      = "NET.MOD.9",  card_id = "NET.MOD.9",  version = "v0.1",
    name    = "Bandwidth Override",
    tagline = "Conflict creates the ultimate engagement metric.",
    type    = ModReactCard,  faction = Network,
    layer   = Economy,  function = Add,  subject = ModifierCard,  # assigned S137 (04-n175) — arbiter.draw_modifier(count=4), clean single-effect

    trigger         = status_marker.contested.placed(),
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
    cost            = resource.faction(Network).exposure * 1 + resource.faction(Network).findings * 1,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.draw_modifier(faction=Network, count=4),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "The massive hand-flooder. Triggered by a high-tension public state change. Since there is no hand limit, Network holds these cards indefinitely to fund their cascading react chain Cost reasoning: Findings pinpoint the opponent's exact communication frequencies to successfully jam them.",
    arbiter_note = None,
)
```

---

### NET.MOD.10 — LOCAL ORGANIZERS

#### Design Rationale
Opportunistic Baryo chip-swap React — same Redirect shape as GHO.MOD.7 (confirmed precedent). Real finding: `faction=Any` in the trigger carries the same self-fire question as items 5/6/11 across this session — Network placing its own chip in Baryo would trigger this against itself, paying 1 Exposure to swap its own chip for its own chip, a costed no-op.

#### Card Story
A rival sends operatives into the Baryo. Network sends neighbors instead — people who were already there, already trusted, already positioned to take the ground the moment it's contested.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Grassroots co-option of opponent momentum in Network's home territory (Baryo) is a sharply doctrinal beat — "we sent neighbors" vs. an opponent's "operatives." | Art 00 §7 |
| Voice fit | ✓ | Tagline is one of the strongest in the Network set. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; opportunistic tactical play, not a doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Network, real taxonomy (Territory/Redirect/PresenceToken, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory×Redirect valid; matches the confirmed GHO.MOD.7 precedent for same-slot chip swaps. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | 1-resource cost for a chip swap in Baryo only — bounded, reasonable given the Redirect precedent's established power level. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | `presence_chip.placed(faction=Any, ring=3)` — confirmed vocabulary, but `faction=Any` carries the same self-fire question as items 5/6/11 (Network triggering on its own Baryo placement, a costed no-op). | Art 04 §6.3; schema_cleanup_log.md item 5 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district` — correct, same-district swap (contrast with NET.MOD.6's inconsistent adjacency). | Art 01 §6–7 |
| Supported by components | ✓ | Chip remove+place reuses the standard mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing chip-placement event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | Cost is Exposure only, Network-native — no cross-resource question. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ⚠ | Any faction's Baryo placement is common — moderate-to-high frequency. |  |
| Firing window (ModReactCard) | ✓ | No other Network card shares this trigger (distinct from NET.MOD.6's separate Baryo reaction). |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary swap — no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=3` matches trigger scope. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*React on any presence placement in Baryo (Ring 3). Grassroots co-option of opponent territorial momentum. S138: full content-review pass — self-fire question flagged (item 5 family); otherwise clean (cost is Network-native only, taxonomy matches confirmed Redirect precedent). Design Pass ✓, Issues Resolved not yet.*

```python
NET.MOD.10 = Card(
    id      = "NET.MOD.10",  card_id = "NET.MOD.10",  version = "v0.1",
    name    = "Local Organizers",
    tagline = "They sent operatives. We sent neighbors.",
    type    = ModReactCard,  faction = Network,
    layer   = Territory,  function = Redirect,  subject = PresenceToken,  # assigned S137 (04-n175) — swaps 1 opponent chip for 1 Network chip in the same district, same shape as GHO.MOD.7's corrected Redirect

    trigger         = presence_chip.placed(faction=Any, ring=3),
    beat            = None,
    ring_constraint = 3,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = Resource(Exposure, 1),
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = list([arbiter.remove(presence_chip, district=target_district, faction=target_faction, count=1), arbiter.place(presence_chip, district=target_district, faction=Network, count=1)]),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Opportunistic Baryo swap. When any faction places a presence chip in Ring 3 (Baryo), Network pays 1 Exposure to immediately swap it for a Network chip. Represents grassroots community organizing co-opting the opponent's momentum. Creates brutal point-disruption in the slums without requiring a Dispatch Token.",
    arbiter_note = None,
)
```

---

---

### NET.MOD.11 — CANCEL CAMPAIGN *(stub)*
[↑ Modifier & React Cards](#network-modifier-and-react-cards)

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

```python
NET.MOD.11 = Card(
    id      = "NET.MOD.11",  version = "v1.1",
    name    = "Cancel Campaign",
    tagline = "Hijack the narrative of an opponent's public action.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Network,
    layer   = Standing,  function = Shift,  subject = StandingMarker,
    trigger = "public_act.submitted",
    cost    = resource.faction(Network).exposure * 1,
    success = "The target faction's PA resolves normally, but their PS is reduced by 2 due to extreme public backlash. Network gains 1 Exposure.",
    design_note = "Network doesn't block the legal act (Directorate's job). Instead, Network weaponizes the public's reaction to the act, ensuring the target pays a heavy PR price for whatever they just did."
)
```

---

### NET.MOD.12 — FORCED TRANSPARENCY *(stub)*
[↑ Modifier & React Cards](#network-modifier-and-react-cards)

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

```python
NET.MOD.12 = Card(
    id      = "NET.MOD.12",  version = "v1.0",
    name    = "Forced Transparency",
    tagline = "Broadcast their intended target before they are ready.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Network,
    layer   = Information,  function = Reveal,  subject = TargetProfile,
    trigger = "public_act.placed_with_target_profile",
    cost    = resource.faction(Network).exposure * 1,
    success = "The Target Profile is immediately flipped face-up for the table to see.",
    arbiter_note = "Reacts at Art 03 §9.2.0 when an opponent places a PA with a face-down Target Profile. Network announces the React and spends 1 Exposure. The Target Profile is flipped face-up immediately. The PA is locked in and will resolve normally at Beat 4, but the target is now public knowledge for the rest of the round.",
    design_note = "A direct counter to hidden targets. By spending 1 Exposure, Network strips the opponent's tactical ambiguity for the entire round. This allows other factions to prepare defenses or negotiate before Beat 4."
)
```

---

### NET.MOD.13 — PRESS CREDENTIALS

#### Design Rationale
"Ceiling-power" Protect card: shields Network's own PA and all attached components from any targeting until Beat 4 resolution. Real, already-known issue (04-n175, re-confirmed here, not newly found): `success` is a string literal describing the immunity in prose, not a real MutationExpr — a smaller version of the fossil-card gap (GHO.MOD.9/10/11, 04-n174). New finding this pass: the cost spans three resource types (Exposure, Findings, Mandate) — only Exposure is Network-native; Findings is Ghost's and Mandate is Directorate's. This is the sharpest cross-resource-holding instance reviewed this session — two foreign resource types required for a single card, more than GHO.MOD.7's one-foreign-of-three.

#### Card Story
Network's public act goes up with full press credentials attached — sourced, verified, backed by the kind of institutional cover that makes interference legally indefensible. Nobody touches it before it resolves.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Protecting Network's own high-stakes PA with a credentialed-immunity framing is a coherent, high-power doctrinal statement. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("no one pulls a credentialed signal off the air") lands the doctrine precisely. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1 — correctly expresses doctrine on a deliberate, high-stakes play. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Network, real taxonomy (Submission/Protect/PublicAct, 04-n175). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Submission×Protect valid per the matrix; Protect correctly assigns to the layer of the protected target (Construction Logic rule 3). | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | "Ceiling-power" per its own design_note — total immunity from targeting is a strong, precedent-setting effect. Real cost (3 resources, 2 foreign) partially offsets it, but the effective cost depends on whether Network can reliably hold Findings/Mandate — see Resource cost positioning. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate (the protection window itself lasts until Beat 4, but the card's own resolution is Immediate). | Art 04 §5 P19 |
| Persistence | ✓ | Explicitly declared (`persistence=Immediate`) — ahead of most of the corpus on this field. | Art 04 §6.2 |
| Trigger validity | ✓ | `public_act.placed_on_frg(faction=Network)` — confirmed vocabulary, self-scoped, no ambiguity. | Art 04 §6.3 |
| Portrait validity | ✓ | Submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; this isn't a territory effect. | Art 01 §6–7 |
| Supported by components | ✓ | No new component needed — protection is a rules-state condition on an existing PA. | Art 02 §6–8 |
| Supported by game procedure | ✓ | `arbiter_note` gives a clear procedural description (record protected PA, block targeting until Beat 4, clear on resolution) — even though `success` itself isn't a formal Expr, the procedure is well-specified in prose. | Art 03; GR 6.1 |
| Data schema validation | ⚠ **(known issue, confirmed)** | `success` is a string literal, not a real MutationExpr — re-confirmed on this pass, not fixed (04-n175/04-n174-adjacent gap). Scaffolding added this session for `resolution_type`/`boost`/`ps_framing`. | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story above is concrete; `narrative` field itself is still `None`. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single effect (no branching) — the prose-vs-Expr issue is a schema-format problem, not a determinacy problem. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Real cost specified, but requires TWO foreign resource types (Findings/Ghost, Mandate/Directorate) alongside Network's own Exposure — the sharpest cross-resource-holding instance reviewed this session (sharper than GHO.MOD.7's one-of-three). Design_note frames this as intentional ("requires trade relationships with Ghost and Directorate") — a real design choice, but one that makes this card's actual accessibility highly dependent on diplomacy. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Gated on Network placing a PA — moderate, self-limiting frequency. |  |
| Firing window (ModReactCard) | ✓ | No other Network card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Deterministic protection, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S130. Protect a Network PA and all attached components from targeting until Beat 4 resolution. 04-n128. Taxonomy assigned S137 (04-n175): Submission/Protect/PublicAct. S138: full content-review pass — re-confirmed the known `success`-string-literal gap (not fixed); new finding is the two-foreign-resource cost, the sharpest cross-resource-holding instance reviewed this session. Design Pass ✓, Issues Resolved not yet — the string-literal success field is a real blocker.*

```python
NET.MOD.13 = Card(
    id      = "NET.MOD.13",  card_id = "NET.MOD.13",  version = "v0.1",
    name    = "Press Credentials",
    tagline = "The broadcast is live. No one pulls a credentialed signal off the air.",
    type    = ModReactCard,  faction = Network,
    layer   = Submission,  function = Protect,  subject = PublicAct,  # assigned S137 (04-n175) — shields the PA and attached components from targeting until Beat 4

    trigger         = public_act.placed_on_frg(faction=Network),
    beat            = None,
    ring_constraint = None,  ring_origin = None,  value_rating = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Network).exposure * 1 + resource.faction(Network).findings * 1 + resource.faction(Network).mandate * 1,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    persistence = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    success     = "PA and all attached components (TargetProfile, submitted resources, ModActionCard) are immune from any targeting until the PA resolves at Beat 4.",  # ⚠ string literal, not a real MutationExpr — flagged 04-n175, confirmed still true, needs re-authoring against §6.3
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Network: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,  perspectives = None,
    design_note  = "Asset — human/institutional. Fires at §9.2 when Network places any PA on FRG. Effect: PA + all attached components immune from targeting until Beat 4 resolution. Ceiling-power card. Cost: Exposure×1 (signal is live) + Findings×1 (threat intelligence on who might try to jam it) + Mandate×1 (institutional authorization making interference legally indefensible). Three cross-resource cost requires trade relationships with Ghost and Directorate. 04-n128.",
    arbiter_note = "Network places PA on FRG at §9.2 and plays Press Credentials. Collect Exposure×1, Findings×1, Mandate×1. Record the protected PA. Until that PA resolves at Beat 4: no card or procedure may target the PA, its TargetProfile, its submitted resources, or any attached ModActionCard. On PA resolution: effect clears.",
)
```

---

### NET.MOD.14 — SUBSCRIBER NETWORK

#### Design Rationale
Completes the standing-interaction trilogy: MOD.2 (attacks when an opponent gains PS), MOD.3 (recovers when Network loses PS), MOD.14 (compounds when Network itself gains PS). Self-scoped trigger, no ambiguity. `cost=None` is explicitly intentional per its own design_note ("standing growth is Network's reward... amplifies without economic friction") — same category of deliberate free-cost design as DIR.MOD.5's self-subsidy, not an unexamined gap, though it's still subject to the same whole-set 04-n178 decision as every other card.

#### Card Story
Network's public standing climbs — a win, visible to the whole table. The subscriber base follows the same curve: more attention means more material flowing in, no extra effort required.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Compounding on Network's own PS gain completes a coherent three-card trilogy with MOD.2/MOD.3 — no redundant coverage. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("the audience grows, so does the signal") lands the doctrine. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; mechanical compounding engine, not a doctrinal statement. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Network, real taxonomy (Economy/Add/ModifierCard, 04-n175), same shape as NET.MOD.7/9. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Economy×Add cell. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ✓ | Free cost is explicitly intentional (design_note's own reasoning), not an oversight — consistent with the trilogy's "PS growth is the reward" framing across all three cards. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ✓ | Explicitly declared (`persistence=Immediate`) — ahead of most of the corpus on this field. | Art 04 §6.2 |
| Trigger validity | ✓ | `standing_marker.increased(faction=Network)` — confirmed vocabulary, self-scoped, no ambiguity. | Art 04 §6.3 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; not a territory effect. | Art 01 §6–7 |
| Supported by components | ✓ | Modifier card draw reuses the standard mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing PS-increase event; no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | `cost=None` is deliberate design (see Design Rationale), not an unresolved TBD like several other cards this session — still subject to 04-n178's whole-set decision, but not flagged as an oversight. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Gated on Network's own PS increasing — self-limiting, reasonable frequency. |  |
| Firing window (ModReactCard) | ✓ | No other Network card shares this trigger (distinct from NET.MOD.7/9, which key off different events despite the shared "draw modifiers" effect type). |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat draw, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S130. Hand-growth React on Network PS gain. Completes the standing-interaction trilogy (MOD.2/MOD.3/MOD.14). S138: full content-review pass — cost=None confirmed intentional (not an oversight); firing-window distinct from NET.MOD.7/9 despite shared draw-modifier effect type. Design Pass ✓, Issues Resolved not yet.*

```python
NET.MOD.14 = Card(
    id      = "NET.MOD.14",  card_id = "NET.MOD.14",  version = "v0.1",
    name    = "Subscriber Network",
    tagline = "The audience grows. So does the signal.",
    type    = ModReactCard,  faction = Network,
    layer   = Economy,  function = Add,  subject = ModifierCard,  # assigned S137 (04-n175) — arbiter.draw_modifier(count=2), same shape as NET.MOD.7/9

    trigger         = standing_marker.increased(faction=Network),
    beat            = None,
    ring_constraint = None,  ring_origin = None,  value_rating = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    persistence = Immediate,
    persistence_condition = None,  persistence_effect = None,

    success     = arbiter.draw_modifier(faction=Network, count=2),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,  perspectives = None,
    design_note  = "Asset — business. Hand-growth React on Network PS gain. When Network's standing increases, the subscriber base grows: Network draws 2 modifier cards. Completes the standing-interaction trilogy: MOD.2 Troll Farm (attacks when opponent gains PS), MOD.3 Backup Server Racks (recovers when Network loses PS), MOD.14 Subscriber Network (compounds when Network gains PS). Free cost — standing growth is Network's reward; this card amplifies without economic friction. Draw 2 (not 1) makes this a meaningful engine card across multiple triggers per Quarter.",
    arbiter_note = None,
)
```

---

### NET.MOD.15 — COMMUNITY TURNOUT *(stub)*

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

*S132. Network's ModBattleCard set, replicating the Directorate/Ghost pattern (2 Boost +1/+2, 2 Hinder −1/−2, PM05 09-06). Doctrine per §5a and modifier_card_ideas.md's provisional voice seed: "broadcast/exposure-based: public attention and narrative pressure as a form of contest weight" — not personnel or intelligence, but mobilized public attention. Weaker Boost tier (+1): ordinary residents, not Network operatives, showing up in visible numbers.*

```python
NET.MOD.15 = Card(
    id      = "NET.MOD.15",  card_id = "NET.MOD.15",  version = "v0.1",
    name    = "Community Turnout",
    tagline = "Word got around. People showed up.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=1),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 1,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).

    portrait     = None,   # TBD — modifier card portrait model still open (same open note as SYN.MOD.1 The Fixer)
    narrative    = "A few calls, a few posts, and the block is suddenly full of people who care how tonight goes.",
    arbiter_note = "Playable by any faction, not just Network (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### NET.MOD.16 — LIVE BROADCAST *(stub)*

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

*S132. Stronger Boost tier (+2) — infrastructure rather than a bigger crowd. Cameras and a real-time feed turn public attention into sustained leverage instead of a one-time gathering.*

```python
NET.MOD.16 = Card(
    id      = "NET.MOD.16",  card_id = "NET.MOD.16",  version = "v0.1",
    name    = "Live Broadcast",
    tagline = "The feed goes live. Everyone at the table knows the whole city is watching now.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=2),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 2,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).

    portrait     = None,   # TBD — modifier card portrait model still open (same open note as SYN.MOD.1 The Fixer)
    narrative    = "A camera crew sets up on the corner and starts streaming. Whatever happens next, it happens on the record.",
    arbiter_note = "Playable by any faction, not just Network (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### NET.MOD.17 — STREET PRESSURE *(stub)*

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

*S132. Weaker Hinder tier (−1). Network's suppression is public and visible, not covert — organized pushback that makes a position harder to hold in the open, not a hidden attack.*

```python
NET.MOD.17 = Card(
    id      = "NET.MOD.17",  card_id = "NET.MOD.17",  version = "v0.1",
    name    = "Street Pressure",
    tagline = "Signs, chants, a crowd that isn't going home. Hard to hold ground while explaining yourself.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=1),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 1,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).

    portrait     = None,   # TBD — modifier card portrait model still open (same open note as SYN.MOD.1 The Fixer)
    narrative    = "A crowd gathers outside, loud enough that whatever's happening inside has to happen slower, and worse, than planned.",
    arbiter_note = "Playable by any faction, not just Network (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### NET.MOD.18 — PUBLIC OUTCRY *(stub)*

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

*S132. Stronger Hinder tier (−2), completing Network's 2 Boost/2 Hinder pattern. Escalates Street Pressure from a local crowd into a citywide story — the reputational damage of the coverage itself, not just the presence of a crowd.*

```python
NET.MOD.18 = Card(
    id      = "NET.MOD.18",  card_id = "NET.MOD.18",  version = "v0.1",
    name    = "Public Outcry",
    tagline = "By morning, everyone at The Table has seen the footage. That's the whole play.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=2),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 2,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).

    portrait     = None,   # TBD — modifier card portrait model still open (same open note as SYN.MOD.1 The Fixer)
    narrative    = "The clip is everywhere by morning. Nobody needed to lie about what it shows.",
    arbiter_note = "Playable by any faction, not just Network (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### NET.MOD.19 — GROUNDSWELL *(stub)*

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

*S135. Replicates the Directorate ModActionCard pattern (DIR.MOD.14–25, 09-06/04-n157) to Network — locked format: 4 `threshold_delta` (+5/+10/+15/+20) + 2 `success_multiplier` (n=1/n=2) + 4 `ps_shift` (self +1/+2, target −1/−2) + 2 `cost_reduction` (n=1/n=2, PA-only), `cost=None` uniformly, `value_rating` 1–4 mirroring tier. Network voice: broadcast and exposure, transparency doctrine — same doctrinal lens as Network's shipped ModBattleCard set (NET.MOD.15–18). Minor threshold_delta tier (+5).*

```python
NET.MOD.19 = Card(
    id      = "NET.MOD.19",  card_id = "NET.MOD.19",  version = "v0.1",
    name    = "Groundswell",
    tagline = "Organic public interest builds before the story is even filed.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1, effect is parasitic on host action

    effect          = ModActionExpr.threshold_delta(n=5),  # self-only (§6.3, 04-n170); eases the host CA/PA's own threshold
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,   # splay-display convention, PM02 L256 — same basis as all ModActionCard content

    portrait     = None,
    narrative    = "Organic public interest builds ahead of the story — by the time Network runs it, the audience is already listening.",
    arbiter_note = "Attach at Dispatch to any CA/PA in Network's own submitted packet (Art 03 §9.1.1) — no card-level host restriction.",
)
```

---

### NET.MOD.20 — ADVANCE COVERAGE *(stub)*

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

*S135. Mid threshold_delta tier (+10).*

```python
NET.MOD.20 = Card(
    id      = "NET.MOD.20",  card_id = "NET.MOD.20",  version = "v0.1",
    name    = "Advance Coverage",
    tagline = "The piece is already written. It just needs an outcome to run with.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=10),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "Pre-positioned attention eases a public action — the story's already primed, waiting only for the result.",
    arbiter_note = "Self-only, same basis as NET.MOD.19.",
)
```

---

### NET.MOD.21 — CLEAR SIGNAL *(stub)*

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

*S135. Third of 4 threshold_delta tiers (+15). Reframed from an earlier hostile-flavored seed concept ("Signal Jammed" — disrupting a rival's broadcast-dependent action, `Whiteboard/modifier_card_ideas.md`) per **04-n170**: threshold_delta carries no faction parameter, so it can only ever ease Network's own host action.*

```python
NET.MOD.21 = Card(
    id      = "NET.MOD.21",  card_id = "NET.MOD.21",  version = "v0.1",
    name    = "Clear Signal",
    tagline = "No interference, no dropped frames — the broadcast goes out exactly as planned.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=15),
    value_rating    = 3,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "A scrubbed broadcast channel removes the interference that would otherwise complicate getting the message out clean.",
    arbiter_note = "Reframed from a hostile-flavored seed concept per 04-n170, same basis as GHO.MOD.18/GUI.MOD.17/DIR.MOD.15/16.",
)
```

---

### NET.MOD.22 — FULL SATURATION *(stub)*

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

*S135. Capstone threshold_delta tier (+20).*

```python
NET.MOD.22 = Card(
    id      = "NET.MOD.22",  card_id = "NET.MOD.22",  version = "v0.1",
    name    = "Full Saturation",
    tagline = "Every channel, every feed, the same story at once.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=20),
    value_rating    = 4,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "Coverage reaches every channel at once — nothing about the outcome is left to chance when the whole city is already watching.",
    arbiter_note = "Capstone tier — log actual play outcomes before treating +20 as balanced (04-n157, same playtest caveat as the rest of this set).",
)
```

---

### NET.MOD.23 — CROSS-POSTED *(stub)*

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

*S135. Common success_multiplier tier (n=1).*

```python
NET.MOD.23 = Card(
    id      = "NET.MOD.23",  card_id = "NET.MOD.23",  version = "v0.1",
    name    = "Cross-Posted",
    tagline = "The same story, running on every channel that'll take it.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "Coverage across multiple channels amplifies an outcome further than any single placement would.",
    arbiter_note = "Self-only, amplifies Network's own host action.",
)
```

---

### NET.MOD.24 — VIRAL MOMENT *(stub)*

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

*S135. Rare/capstone success_multiplier tier (n=2).*

```python
NET.MOD.24 = Card(
    id      = "NET.MOD.24",  card_id = "NET.MOD.24",  version = "v0.1",
    name    = "Viral Moment",
    tagline = "Nobody planned for it to travel this far. It travels this far anyway.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "An action catches unexpected attention and lands far harder than the plan ever accounted for.",
    arbiter_note = "Rare/capstone tier — log actual play outcomes before treating n=2 as balanced (04-n157, same playtest caveat as 04-n94).",
)
```

---

### NET.MOD.25 — OFF-AIR *(stub)*

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

*S135. Self-boost, minor tier (+1) of the `ps_shift` 2×2 matrix.*

```python
NET.MOD.25 = Card(
    id      = "NET.MOD.25",  card_id = "NET.MOD.25",  version = "v0.1",
    name    = "Off-Air",
    tagline = "A story, deliberately not run.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=1),  # self-boost, minor tier
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "A story that could have run doesn't — quietly protecting standing that a different editorial call would have cost.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half resolves to the acting faction.",
)
```

---

### NET.MOD.26 — EXCLUSIVE ACCESS *(stub)*

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

*S135. Self-boost, major tier (+2) of the `ps_shift` 2×2 matrix.*

```python
NET.MOD.26 = Card(
    id      = "NET.MOD.26",  card_id = "NET.MOD.26",  version = "v0.1",
    name    = "Exclusive Access",
    tagline = "First to the story, and everyone knows it.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "Being first to a story earns standing no follow-up coverage ever quite matches.",
    arbiter_note = "Self-boost, major tier — resolves to the acting faction.",
)
```

---

### NET.MOD.27 — FOLLOW-UP QUESTION *(stub)*

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

*S135. Target-hinder, minor tier (−1) of the `ps_shift` 2×2 matrix.*

```python
NET.MOD.27 = Card(
    id      = "NET.MOD.27",  card_id = "NET.MOD.27",  version = "v0.1",
    name    = "Follow-Up Question",
    tagline = "One pointed question, asked in front of everyone.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-1),  # target-hinder, minor tier
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "A pointed follow-up question at a public event costs a named faction some standing — small, but on the record.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA itself names as its target_faction (§6.1) — only attachable to a host that has one.",
)
```

---

### NET.MOD.28 — RETRACTION DEMANDED *(stub)*

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

*S135. Target-hinder, major tier (−2) of the `ps_shift` 2×2 matrix. Magnitude mirrors the established Intel Token Hinder precedent (PM02 L242).*

```python
NET.MOD.28 = Card(
    id      = "NET.MOD.28",  card_id = "NET.MOD.28",  version = "v0.1",
    name    = "Retraction Demanded",
    tagline = "A public claim, publicly discredited.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "A rival's claim gets publicly discredited — Network doesn't have to lie, just cover the correction as prominently as the original story.",
    arbiter_note = "Same target-resolution constraint as NET.MOD.27, major tier.",
)
```

---

### NET.MOD.29 — VOLUNTEER STRINGERS *(stub)*

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

*S135. Common cost_reduction tier (n=1). PA-only per §6.3.*

```python
NET.MOD.29 = Card(
    id      = "NET.MOD.29",  card_id = "NET.MOD.29",  version = "v0.1",
    name    = "Volunteer Stringers",
    tagline = "Community contributors cover the ground a paid crew would have charged for.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=1),  # PA-only (§6.3)
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "Volunteer contributors cut the cost of coverage that a professional crew would otherwise charge for.",
    arbiter_note = "PA host only. Attach at Dispatch (Art 03 §9.2) alongside the declared PA.",
)
```

---

### NET.MOD.30 — EXISTING AIRTIME *(stub)*

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

*S135. Capstone cost_reduction tier (n=2).*

```python
NET.MOD.30 = Card(
    id      = "NET.MOD.30",  card_id = "NET.MOD.30",  version = "v0.1",
    name    = "Existing Airtime",
    tagline = "The slot was already booked. Using it costs almost nothing extra.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Network,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Network faction modifier deck
    cost            = None,

    portrait     = None,
    narrative    = "A standing broadcast slot lowers the cost of getting a message out — the infrastructure's already paid for.",
    arbiter_note = "Capstone cost_reduction tier — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157).",
)
```

---

