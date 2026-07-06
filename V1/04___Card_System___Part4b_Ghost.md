## Ghost
[↑ 7. Card Specifications](#7-card-specifications)

[Covert Operations](#ghost-covert-operations) · [Public Acts](#ghost-public-acts)

---

### Ghost — Covert Operations
[↑ Ghost](#ghost)

| Card | Name |
|------|------|
| [GHO.CA.1](#c16-pattern-match) | Pattern Match |
| [GHO.CA.2](#c17-intercept) | Intercept |
| [GHO.CA.3](#c18-dossier-breach) | Dossier Breach |
| [GHO.CA.4](#c19-deep-cover) | Deep Cover |
| [GHO.CA.5](#c20-misdirection) | Misdirection |
| [GHO.CA.7](#ghost-station) | Station |
| [GHO.CA.8](#ghost-full-take) | Full Take |
| [GHO.CA.9](#ghost-scif) | SCIF |
| [GHO.CA.10](#ghost-flip) | Flip |
| [—](#ghost-signals-analysis) | Signals Analysis |
| [—](#ghost-synthesize) | Synthesize |
| [GHO.CA.12](#ghost-source-substitution) | Source Substitution |
| [—](#ghost-backdate) | Backdate |
| [—](#ghost-field-verification) | Field Verification |

### GHO.CA.1 — PATTERN MATCH
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost-exclusive intelligence-into-action card — the only card with Predictive resolution in the set. Ghost submits a prediction at §9.1: target faction, target district, and the operation they believe that faction has dispatched. At Beat 2, ARBITER checks all three against the covert grid. A correct match causes ARBITER to move the matched operation from the target faction's Beat 3 lane into Ghost's lane. The target faction loses the operation entirely: their case returns empty, resources spent, Dispatch Token consumed.

This is not a copy. The operation executes once, for Ghost.

Ghost resolves the stolen operation at Beat 3 as `faction(acting)`. Same target district, same Target Profile as originally submitted — but Ghost is the actor and Ghost receives the benefit. Any op, any faction — if Ghost can identify and execute it, Ghost keeps it. Effects that reference `faction(acting)` now reference Ghost; Ghost receives whatever the op produces, including off-faction resources.

Executability check precedes the move: if Ghost cannot execute the stolen op (restriction failure, resource type mismatch), Pattern Match fizzles. The op stays in the target's lane. Ghost gains nothing; 2 Findings spent. The risk of a wrong prediction — or an unexecutable steal — is real.

Prediction bar is high: all three elements (faction + district + operation name) must match. Intelligence depth is the enabler — Intel Tokens, prior observations, pattern analysis. At that depth, the interception is earned.

Fills `Submission | Redirect | CovertOperation` — a function unique to Ghost in the card set. No standard equivalent (Art 04 §5 P17). The Redirect taxonomy needs Art 04b §5.1 validity matrix confirmation (PM05 flagged).

#### Card Story
A faction submits their operation. Ghost, watching, named all three things in advance. At Beat 2, ARBITER finds Ghost's prediction in the grid, finds the matching operation, and moves it. The faction's case comes back lighter than they expected. The operation resolves — but not for them.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence-into-action via operational interception — Ghost's prediction accuracy converts to execution, not just information. Fits Ghost doctrine: understanding precedes action, and in this case enables theft. | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | Ghost only; single perspective — interception as doctrine. Extended in v2.0 to include the "theft" framing. | Art 00 §7 |
| Doctrine alignment | ✓ | target_faction = faction.named; doctrine_mod = None — prediction accuracy is about intelligence depth, not doctrinal proximity. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — operation interception is Ghost-exclusive; no Standard equivalent. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ⚠ | Submission/Redirect/CovertOperation — Redirect communicates the mechanism (op moves from target lane to Ghost lane; no duplication). Needs Art 04b §5.1 validity matrix check (PM05 queued). | Art 04b §4, §5 |
| Balance | ✓ | 2 Findings for a triple-prediction. High prediction bar (faction + district + operation name) is the gate. Stolen op is free to Ghost — original faction bore the cost. Fizzle risk (wrong prediction OR can't execute) is the downside. | Art 02 §8 |
| Effect duration | ✓ | Immediate: stolen op resolves at Beat 3, no persistent state from Pattern Match itself. | — |
| Persistence | ✓ | Immediate — fully resolved at Beat 3; no lingering game-state marker from Pattern Match. | Art 04 §6 |
| Trigger validity | N/A | trigger = None — Predictive resolution: ARBITER checks prediction against grid at Beat 2. | — |
| Portrait validity | ⚠ | Ghost submitter=+1, modifier=+1, mod_where=game.outcome == Success. Portrait AND/OR semantics still open (see Outstanding Issues). Additional open: does Portrait also fire when the stolen op resolves at Beat 3 under Ghost's lane? | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.named — Ghost names a specific district in the prediction. No adjacency restriction (analytical op). | Art 01 §6 |
| Supported by components | ✓ | Findings cost; CovertOperation as redirect target; stolen op's components governed by that op's spec. Ghost may receive off-faction resources (Mandate, Capacity, etc.) — tradeable at Debrief. | Art 02 §8 |
| Supported by game procedure | ⚠ | Beat 2 resolution; ARBITER checks prediction against covert grid; if match + executable: lane redirect. Art 03 gap: Pattern Match redirect procedure not yet written in Art 03 §9.4 — simpler than the prior copy-injection model but still unwritten. | Art 03 §9 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S119 | Art 04 §5 P26 |

#### Outstanding Issues

- **Portrait AND/OR semantics:** `modifier=+1, mod_where=game.outcome == Success` — confirm AND semantics: `submitter` always fires on play; `modifier` fires additionally on Success. Confirm OR is not intended.
- **Portrait from stolen op:** The moved op has its own portrait block (keyed to original faction). When it resolves in Ghost's lane, does ARBITER fire those portrait entries for the original faction (who didn't submit it) or not at all? Rule needed.
- **Art 03 procedure gap:** Pattern Match redirect (Beat 2 lane move) not yet written in Art 03. Simpler than copy-injection — just a grid lane transfer — but still requires a new sub-step in §9.4.2. Blocked on Art 03 edit.
- **Submission|Redirect L×F validity:** Art 04b §5.1 matrix check required. PM05 queued.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*S119 v2.0 redesign — mechanism changed from Copy (Beat 3) to Redirect/steal (Beat 2 intercept → Beat 3 execution). Original faction loses op, cost, and Dispatch Token. Ghost is actor on stolen op; effects reference Ghost as faction(acting). Prediction now requires all three: faction + district + operation name.*

```python
GHO.CA.1 = Card(
    id      = "GHO.CA.1",  card_id = "GHO.CA.1",  version = "v2.0",
    name    = "Pattern Match",
    tagline = "Identify a faction's operation and location — then take it.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Submission,  function = Redirect,  subject = CovertOperation,

    beat            = 2,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Predictive",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.named,
    target_faction  = faction.named,
    target_object   = CovertOperation,
    declared_params = operation.named,

    target_taxonomy=None,
    affinity    = None,
    restriction = None,
    cost        = resource.faction(acting).findings * 2,
    boost       = None,

    success     = game.redirect(
        op        = faction(target).beat3_row.op(district=target_district, name=declared_params.operation),
        to        = faction(acting).beat3_lane,
        condition = game.can_execute(faction(acting), op),
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1, modifier=+1, mod_where=game.outcome == Success)},
    ps_framing = None,

    narrative    = "Ghost does not guess. Ghost identifies what is already in motion — and takes it.",
    perspectives = {
        Ghost: "We are not predicting. We are recognising a pattern we have already seen. And then we are keeping it.",
    },
    design_note  = "Steal not copy: matched op moves from target faction's Beat 3 lane to Ghost's. Original faction loses the op, the cost, and the Dispatch Token — no compensation. Ghost resolves the stolen op as faction(acting) at Beat 3; same target as originally submitted; Ghost receives all effects including off-faction resources. Executability check precedes the move: if Ghost cannot execute (restriction failure, wrong resource type), Pattern Match fizzles and the op stays in target's lane. Taxonomy: Submission|Redirect — Art 04b §5.1 L×F validity check pending (PM05 queued).",
    arbiter_note = "At Beat 2: (1) Check Ghost's declared_params (target faction + target district + operation name) against the Beat 3 grid. (2) If all three match: check whether Ghost can execute the matched op — if restriction or resource type blocks execution, Pattern Match fizzles (2 Findings spent; op stays in target lane; no notification). (3) If match AND executable: move the op and its Target Profile from target faction's Beat 3 lane to Ghost's Beat 3 lane. Target faction's committed cost resources and Dispatch Token are consumed — not returned. (4) At Beat 3: the moved op resolves in Ghost's lane with Ghost as faction(acting). The original Target Profile governs targeting (same district, same target faction as originally submitted). All effects referencing faction(acting) now reference Ghost.",
)
```

---

### GHO.CA.2 — INTERCEPT
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost-exclusive active-surveillance card — distinguishes from GHO.CA.3 Dossier Breach by targeting submitted operations, not hand contents. Intel Token cost consumed at submission regardless of outcome: you spend what you know to learn what they're doing. Cost structure (Intel Token + 2 Findings) reflects active operational depth — harder to execute than Gather, rewarded with real-time intelligence rather than historical data. Failure notifies the target; crit fail triggers a PS loss.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Active surveillance of submitted operations — direct expression of Ghost's real-time intelligence doctrine. Distinct from STD.CA.5 Gather (historical intel) and GHO.CA.3 Dossier Breach (hand contents). | Art 00 §7; Art 04b §5 |
| Voice fit | ✓ | One perspective (Ghost only) — FactionSpecific; acceptable. "We do not wait for the after-action report." Ghost's active-vs-passive intelligence distinction is clear. | Art 00 §7 |
| Doctrine alignment | ✓ | `target_faction = faction(named_opponent)`, `doctrine_mod = None` — explicit design choice: surveillance effectiveness is about intelligence quality, not doctrinal proximity. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation: active surveillance is covert. FactionSpecific (Ghost): real-time operational intel is Ghost's exclusive capability. | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | `layer = Information` — revealing the content of a submitted operation is Information layer. `function = Reveal`, `subject = CovertOperation` — correctly scoped. | Art 04b §4, §5 |
| Balance | ✓ | Intel Token consumed at submission regardless of outcome — meaningful downside for failed surveillance. Double-resource cost (IntelToken + 2 Findings). Crit success stacks additional IntelToken on top of IntelDeliverySlip. | Art 02 §8; Art 02 §12 |
| Effect duration | ✓ | Instantaneous: IntelDeliverySlip delivered once at Beat 2 resolution; reads target faction's Beat 3 grid column. IntelToken on crit. No persistent state beyond the delivered token. | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | N/A | `trigger = None` | — |
| Portrait validity | ✓ | Ghost `submitter=+1`. Fires on submission (DIR.PA.1). Submitter-scoped (DIR.PA.2). Single entry (NET.PA.1). `failcrit = standing -= 2` is a PS shift (not Portrait — DIR.PA.2 clear). | Art 04 §6.2; Art 02 §11 |
| Supported by zones | N/A | `target_district = None` — Intercept operates on submitted ops in the Resolution Grid, not a specific district. | — |
| Supported by components | ✓ | IntelToken cost; Findings cost; IntelDeliverySlip (success); IntelToken (crit success); NotificationSlip (fail); PS −2 (failcrit). | Art 02 §8; Art 02 §11, §8 |
| Supported by game procedure | ✓ | Submitted at Dispatch (Art 03 §9.1); resolves Beat 2; reads Beat 3 grid column; d100 threshold 50; ARBITER delivers IS-xx via case (Art 07). Art 03 §9.4 Beat 2 Step 7a covers IS-xx delivery; Step 7b covers NotificationSlip; Step 7b.i covers failcrit. | Art 03 §9, §11; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Arbiter note:** Crit success: deliver IntelToken (faction=target) to acting faction's case. Success: write target faction's first submitted op type and district on Intel Delivery Slip; deliver to acting faction's case. Fail: deliver Notification Slip to target faction's case. Crit fail: apply PS −2.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | ⚠ pending re-sign-off (v1.1 — beat timing correction) |

```python
GHO.CA.2 = Card(
    id      = "GHO.CA.2",  version="v1.1",
    name    = "Intercept",
    tagline = "Surveil a faction's covert operations in real time.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Reveal,  subject = CovertOperation,
    beat=2, resolution=d100, threshold=50, ring_mod={0:-15,1:-10,2:0,3:+10}, doctrine_mod=None,
    trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction(named_opponent), target_object=CovertOperation,
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = IntelToken(faction=faction(target)) * 1 + resource.faction(acting).findings * 2,
    success     = game.dispatch(faction(acting), IntelDeliverySlip(faction=faction(target), op_type=faction(target).op(beat=3).type, district=faction(target).op(beat=3).district)),
    successcrit = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)),
    fail        = game.dispatch(faction(target), NotificationSlip),
    failcrit    = faction(acting).standing -= 2,
    portrait    = {Ghost: PortraitEntry(submitter=+1)},
    narrative   = "To know what they are doing while they are doing it — that is the only intelligence that matters.",
    perspectives = {Ghost: "We do not wait for the after-action report. We read the operation as it happens."},
)
```

---

### GHO.CA.3 — DOSSIER BREACH
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
SIGINT tap on a named faction's dispatch channel. Ghost submits at Beat 2 — establishing the tap before Beat 3 fires. At Beat 2 resolution, ARBITER reads the target faction's Beat 3 grid column (all submitted ops for that faction: name and declared target only; modifier cards excluded — splayed edge not readable) and delivers an IntelDeliverySlip to Ghost privately. No interaction with the target player. Covert attribution preserved throughout.

GHO.CA.3 reads a faction column from the Beat 3 grid; DIR.CA.3 reads a district row. Both use IntelDeliverySlip — the content varies by card procedure.

Redesigned S68: original target was the unplayed hand (CardHandContents) — requires physical access to the target player's cards during Beat 3, which breaks covert attribution at the paper table. The SIGINT model removes that constraint: Ghost's tap is in ARBITER's domain (dispatch cases), not the target player's private domain. Information target shifts from planning pool to committed operations — what the faction decided to do, not what they could do. Beat 2 commitment is the risk: 2 Findings spent before Ghost knows what the target will submit.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | SIGINT tap on dispatch channel — faction column read from Beat 3 grid; distinct from GHO.CA.2 (disrupts one submitted op), DIR.CA.3 (district row read), and STD.CA.5 (generates intel tokens); Ghost reads committed operations, not planning pool | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — covert channel interception is Ghost-exclusive doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; Beat 2 commitment is the risk (spends before knowing target's submission); Automatic resolution fits signals intelligence work | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — covert channel access is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/IntelDeliverySlip — subject updated S68 (DR-xx collapsed into IS-xx) | Art 04b §4, §5 |
| Balance | ✓ | 2 Findings, Automatic, Beat 2 — information advantage without dice risk; Beat 2 blind commitment is the cost; empty case = resources spent | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: IntelDeliverySlip delivered at Beat 2 resolution; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at Beat 2; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — intelligence operation confirms Ghost operational activity | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — operates on Beat 3 grid faction column; no district context required | Art 01 §6–§7 |
| Supported by components | ✓ | IntelDeliverySlip (IS-xx) — Art 02 component entry pending (04-n45); 00b definition update pending (04-n46) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 2 Automatic; ARBITER reads existing Beat 3 grid faction column — no new tracking required; Art 03 Beat 2 procedure addition pending (04-n44) | Art 03 §9, §9.4; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Art 03 Beat 2 procedure:** Beat 2 section does not yet cover IntelDeliverySlip delivery for intelligence cards. Procedure addition required before Issues Resolved (04-n44).
- **Art 02 component entry:** IntelDeliverySlip has no design entry in Art 02. Addition required before Issues Resolved (04-n45).
- **00b IS-xx definition:** IS-xx definition needs updating to cover Beat 2 delivery and faction column reads (04-n46).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*S68 redesign — SIGINT tap model*

```python
GHO.CA.3 = Card(
    id      = "GHO.CA.3", version="v1.2",
    name    = "Dossier Breach",
    tagline = "Tap a rival's dispatch channel — read their submitted operations at Beat 2 resolution.",
    type    = CovertOperation, subtype = FactionSpecific, faction = Ghost,
    layer   = Information, function = Reveal, subject = IntelDeliverySlip,
    beat=2, resolution=Automatic, threshold=None, ring_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction(named_opponent), target_object=DispatchCase(faction=faction(target)),
    target_taxonomy=None,
    affinity=None,
    restriction=None,
    cost        = resource.faction(acting).findings * 2,
    success     = game.deliver(IntelDeliverySlip(faction=faction(target), content=resolution_grid(month=current, beat=3, faction=faction(target)).operations(fields=[name, target])), to=faction(acting), private=True),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Ghost: PortraitEntry(submitter=+1)},
    narrative   = "Understanding the operation before it begins. That is the only tactical advantage worth having.",
    perspectives = {Ghost: "We did not take their cards. We simply read their intentions. They will act on plans we already know."},
    design_note  = "Redesigned S68: original target was unplayed hand (CardHandContents) — requires physical access to target player's cards, not executable covertly at paper table. Redesigned to SIGINT tap model: Ghost taps faction X's dispatch channel at Beat 2. ARBITER reads faction X's Beat 3 grid column at Beat 2 resolution (name + declared target only; modifier cards excluded). IntelDeliverySlip delivered to Ghost at Beat 2 resolution. Beat 2 commitment is the risk. Empty case = empty slip — resources spent. DR-xx (DispatchReport) collapsed into IS-xx S68 — column read is IntelDeliverySlip with list content.",
    arbiter_note = "During Beat 2 resolution of this card: read faction X's Beat 3 resolution grid column. Write an IntelDeliverySlip listing each operation by name and declared target (district, faction, or object). Modifier cards not included. Deliver privately to Ghost at Beat 2 resolution. Do not notify faction X. If faction X has no Beat 3 operations, deliver an empty slip — Ghost's resources are spent. Procedure pending Art 03 Beat 2 addition (04-n44).",
)
```

---

### GHO.CA.4 — DEEP COVER
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's intelligence interdiction card — operational disruption rather than evidence destruction. At Art 03 §9.1 Covert Dispatch, Ghost names a target faction and pays 1 unit of that faction's native resource (the operational prerequisite — Ghost must already be embedded in the target's systems). At Beat 3, ARBITER checks the first PA in the target faction's Faction Resolution Grid queue: if an IntelToken is submitted on it, Ghost removes it before Beat 4 processes the PA. Two disruption outcomes depending on how the token was used: if it was the PA's cost payment, the PA is voided; if it was a modifier, the PA loses that modifier and resolves blind. Threshold 25 (Challenging) reflects the difficulty of locating and intercepting live intelligence before a public act proceeds. Redesigned S113: prior design (S68) targeted rival-held private IntelTokens — violated 00a Art 02 §10.1 (ARBITER reaching into a faction's private domain). Faction Resolution Grid is the only valid targeting location for another faction's IntelToken.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence interdiction — Ghost removes a rival's submitted IntelToken from the Faction Resolution Grid before Beat 4; voids PA or strips modifier depending on how token was used; distinct from GHO.CA.3 (reads plans) and STD.CA.5 (gathers intel) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective — interdiction as doctrine, not tactic | Art 00 §7 |
| Doctrine alignment | ✓ | Cost = 1 native resource of target faction — Ghost must be embedded in the target's operational systems; threshold 25 reflects difficulty of live intelligence interdiction; targets the intelligence that was meant to precede the rival's action | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence interdiction is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information / Remove / IntelToken — IntelToken submitted on PA in Faction Resolution Grid is the only valid cross-faction IntelToken target (00a Art 02 §10.1); confirmed S113 | Art 04b §4, §5 |
| Balance | ✓ | 1 native resource (target faction), threshold 25 — cost requires prior economic embedding; Challenging roll is the difficulty gate; disruption ceiling (PA void) is high-stakes but gated behind both cost and roll | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: token removed at Beat 3; PA outcome resolved at Beat 4 | — |
| Persistence | ✓ | Immediate — card fully resolved at Beat 3; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; Beat 3 timing is default for covert ops | — |
| Portrait validity | ✓ | No portrait entry — Ghost interdicting live intelligence is tradecraft, not doctrine; absence intentional (confirmed S113) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — operates on Faction Resolution Grid, not a district | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken as target_object — component registered; Faction Resolution Grid is ARBITER-maintained procedure | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Art 03 §9.1 names target at Covert Dispatch; Beat 3 ARBITER checks first PA in target's Faction Resolution Grid queue; Beat 4 PA resolves without token (or is voided) | Art 03 §9.1, §9.4.2, §9.4.3; Art 07 |
| Data schema validation | ✓ | Validated S113: card_id, doctrine_mod, boost, ps_framing added; resolution=d100, resolution_type=Probabilistic, fail=None corrected | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*S113 redesign — Issues Resolved pending sign-off review*

```python
GHO.CA.4 = Card(
    card_id      = "GHO.CA.4",
    id="GHO.CA.4",  version="v1.2",
    name    = "Deep Cover",
    tagline = "Intercept and destroy the intelligence behind a rival's public act.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Remove,  subject = IntelToken,
    beat=3, resolution=d100, threshold=25, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Probabilistic", outcome_type=None,
    persistence           = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None,
    target_faction=faction(named_opponent),  # declared at Art 03 §9.1 Covert Dispatch
    target_object=IntelToken(submitted_on=faction(target).resolution_grid.pa_queue[0]),
    target_taxonomy=None,
    affinity=None,
    restriction=None,  # target condition evaluated at Beat 3 — see arbiter_note
    cost=resource.faction(target).native * 1,
    boost=None,
    success  = game.remove(target_object),
    # If token was PA cost payment: PA is voided (auto-fail at Beat 4, Dispatch Token returned)
    # If token was PA modifier: PA loses modifier, resolves at Beat 4 without it
    successcrit=None,  fail=None,  failcrit=None,
    portrait    = {},
    ps_framing  = None,
    narrative   = "The act has no foundation once the intelligence beneath it is removed.",
    perspectives = {Ghost: "They submitted their evidence expecting it to do what evidence does. We made sure it did not arrive."},
    design_note  = "Cost is 1 native resource of the target faction — Ghost must already hold it, meaning prior economic embedding in the target's operations. This is the operational prerequisite, not a doctrinal gate (doctrine_mod=None). The Faction Resolution Grid is the only location where another faction's IntelToken is a valid card target (00a Art 02 §10.1); privately held tokens are untouchable. Two disruption tiers: token as cost voids the PA; token as modifier strips it. Both are significant; the ceiling (PA void) is the rare case where the target committed their token as payment.",
    arbiter_note = "At Art 03 §9.1: Ghost names target faction. At Beat 3: (1) confirm Ghost holds 1 unit of target faction's native resource — if not, case is invalid, return to Ghost, no effect. (2) Check first PA in target faction's Faction Resolution Grid queue for a submitted IntelToken. If none present: announce 'no valid target,' operation has no effect, cost spent, no roll. (3) If IntelToken present: collect cost, roll d100 vs. 25 (+/− PS modifier). On success: remove IntelToken (recycle or dispose per component physical design). If token was cost payment, mark PA as voided — at Beat 4 it auto-fails; Dispatch Token returned to target faction. If token was a modifier, PA continues at Beat 4 without it. On fail: no effect.",
)
```

---

### GHO.CA.5 — MISDIRECTION
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Evidence corruption — Ghost alters the faction attribution on an Intel Token a target faction has submitted on an active Public Act. The token remains in place; its `faction_name` field now identifies a different source. Any resolution depending on that attribution — Flip eligibility, Debrief gate access, attribution-based inference work — proceeds from a corrupted record.

Unlike GHO.CA.12 Source Substitution (which re-keys Ghost's own held tokens as an internal analytical step), Misdirection is offensive: Ghost corrupts the record while it is in active play. The target faction submitted this token believing they know what it says. Ghost has changed what it says.

1 Findings cost, Automatic — the corruption is technically simple once Ghost is in position; the difficulty is timing the operation against the target's PA submission. Fills Information|Corrupt|IntelToken at the offensive targeting scope that Source Substitution does not cover. L222 compliant — targets publicly placed tokens in the Faction Resolution Grid only (Beat 0–4 window). `declared_params` carries the replacement faction name declared at §9.1.

#### Card Story
A faction submits intelligence alongside their public declaration — an Intel Token they believe says exactly what they think it says. By the time their declaration resolves, the attribution on that token has been quietly changed. The intelligence is genuine. The source is not.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Offensive evidence corruption — Ghost alters attribution on a token publicly submitted by a target faction; fills Information|Corrupt|IntelToken at offensive scope (distinct from Source Substitution's self-directed re-keying) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — record alteration as operational doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; 1 Finding cost reflects precision operation; Automatic resolution reflects Ghost's technical competence in field correction | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence record manipulation is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/IntelToken — alters faction_name field on publicly placed token; L222 compliant (FRG submission, Beat 0–4 window) | Art 04b §4, §5 |
| Balance | ✓ | 1 Finding — low cost reflects precision play; power is timing-dependent (target must have PA with Intel Token) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: token field altered at Beat 3; no card-level lingering effect | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — evidence corruption aligns with Ghost intelligence manipulation doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — token is in Faction Resolution Grid, not district-anchored | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (publicly placed on PA in FRG); Findings cost; no new components; declared_params carries replacement faction name | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 resolution; ARBITER checks FRG for qualifying token; alters faction_name; if no qualifying token: fizzle | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S119 | Art 04 §5 P26 |

#### Outstanding Issues

None. (Taxonomy resolved S119 — Corrupt function confirmed; content=false retired; self-token restriction removed.)

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*S119 redesign — taxonomy changed from Information|Add to Information|Corrupt; targeting model changed from fabrication/plant to FRG attribution corruption. L222 compliant.*

```python
GHO.CA.5 = Card(
    id      = "GHO.CA.5",  card_id="GHO.CA.5",  version="v2.0",
    name    = "Misdirection",
    tagline = "Ghost has been thinking about what they think they know.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Corrupt,  subject = IntelToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=faction.named, target_object=IntelToken,
    target_taxonomy=None,
    declared_params = FactionName,
    affinity=None,
    restriction = faction(target).FRG.active_PA.intel_token.count >= 1,
    cost        = resource.faction(acting).findings * 1,
    boost       = None,
    success     = game.corrupt(field=faction_name, target=faction(target).FRG.active_PA.intel_token, new_value=declared_params.faction),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Ghost: PortraitEntry(submitter=+1)},
    ps_framing  = None,
    narrative   = "Ghost has been considering what the record says. It is never quite right.",
    perspectives = {Ghost: "The attribution is wrong. Systematically, deliberately wrong. By the time anyone checks, it will have been wrong for a while."},
    design_note  = "Fills Information|Corrupt|IntelToken at the offensive targeting scope: alters faction attribution on a token publicly placed on an active PA. Distinct from GHO.CA.12 Source Substitution (which re-keys Ghost's own held tokens). L222 compliant — targets publicly placed tokens in FRG only (Beat 0–4 window). declared_params carries the replacement faction name declared at §9.1.",
    arbiter_note = "At Beat 3: check whether target faction has any Intel Token submitted on an active PA in the Faction Resolution Grid. If yes: alter the faction_name field on that token to the faction named in declared_params. Token remains face-down on the PA; target faction is not notified. If no qualifying token: card fizzles, 1 Findings spent, no effect.",
)
```

---

### Ghost — STATION
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's dedicated faction-specific gather platform. Distinct from STD.CA.5 Gather (standard, adjacency-exempt, 1 token yield) by higher yield (2 tokens on success) at higher cost (2 Findings). STD.CA.5 is Ghost's remote general-purpose sweep; Station is a deployed collection platform sustaining coverage against a named faction over a Quarter. Two deck copies make Station Ghost's primary Intel generation card. Threshold 55 — above STD.CA.5 base (50), reflecting Station's reliability as a sustained platform. Adjacency restriction applies per 04-n6 direction: a deployed node requires physical proximity, unlike Ghost's analytical ops (GHO.CA.1–5).

#### Card Story
Ghost installs a passive collection node in the target faction's operational district. A sweep goes looking; Station waits. By Quarter's end, the target has brought everything past it at least once.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Dedicated gather platform — Ghost's high-yield intelligence collection card; distinct from STD.CA.5 (standard, 1 token) by sustained multi-token output | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — Station as deployed platform, not remote sweep | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; 2 Findings cost for 2-token yield reflects sustained collection investment; threshold 55 — above STD.CA.5 base (50), Station is a reliable sustained platform | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — Ghost's primary Intel generation card beyond standard STD.CA.5 | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Add/IntelToken — same taxonomy as STD.CA.5; faction-specific variant with higher yield | Art 04b §4, §5 |
| Balance | ✓ | Threshold 55, cost 2 Findings, yield 2 tokens — calibrated above STD.CA.5 base; deferred full balance validation to playtest | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: Intel tokens dispatched at Beat 3; durable resource, no card-level duration | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — collection operations align with Ghost intelligence doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | Adjacency restriction applied per 04-n6 direction — deployed collection node requires Ghost presence in target district or adjacent; no exemption (unlike analytical ops) | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Art 02 §12); Findings cost; no new components | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 3 d100 resolution; tokens dispatched to Ghost case on success; failcrit NotificationSlip per standard | Art 03 §9, §11 |
| Data schema validation | ✓ | 04-n70 ✅ S95 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S112 | Art 04 §5 P26 |

#### Outstanding Issues

None.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Issues Resolved S112*

```python
GHO.CA.7 = Card(
    card_id      = "GHO.CA.7",  version = "v1.1",
    name    = "Station",
    tagline = "Deploy a sustained intelligence collection platform against a named faction.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Add,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 55,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy = None,
    affinity        = None,
    restriction     = district(self|adjacent).faction(acting).presence > 0,
    cost            = resource.faction(acting).findings * 2,

    success     = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)) * 2,
    successcrit = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)),  # +1 = 3 total
    fail        = None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Every asset leaves a signal. Ghost listens until the signal becomes a pattern.",
    perspectives = {Ghost: "A station does not move. It waits until the target walks past it again."},
    design_note  = "Ghost's dedicated gather platform. Higher yield than STD.CA.5 (2 tokens vs 1 on success) at double Findings cost. Threshold 55 calibrated above STD.CA.5 base (50) — Station is a reliable sustained platform. Adjacency restriction per 04-n6: deployed node requires Ghost presence in target district or adjacent. Cards stack: STD.CA.5 and Station may both target same faction in same Quarter.",
)
```

---

### Ghost — FULL TAKE
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Burst gather for pre-loading multi-Quarter intelligence sequences. Single copy representing a total-collection operation: Ghost declares n Findings at submission, receives 2n Intel tokens on success (3n on crit). The slot commitment plus n Findings is the bet — fail returns nothing. Variable cost makes the card self-scaling: a small Full Take (n=1) is conservative; a large Full Take (n=3+) pre-loads an entire SCIF/Flip sequence. Reserved for mid-to-late game plays when Ghost has Findings reserves to invest. Singleton enforces scarcity. Threshold 40 is intentional: variable cost and fail=nothing are the risk floor; low threshold is the compensating upside. Adjacency restriction applies per 04-n6 direction — field collection op requires Ghost presence in target district or adjacent.

#### Card Story
Ghost counts the Findings and commits: all of it against one target, declared before the case is sealed. The return is proportional. The loss, if it comes, is total — investment gone, target notified.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Burst intelligence collection — pre-loads multi-Quarter sequences (SCIF, Flip, Signals Analysis); singleton scarcity enforces mid-to-late game use | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — maximum-yield operation as Ghost doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; variable cost scales with investment; singleton forces strategic commitment; adjacency restriction applied per 04-n6 | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — burst intelligence platform; no Standard equivalent | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Add/IntelToken — higher-yield variant of Station/STD.CA.5 pattern | Art 04b §4, §5 |
| Balance | ✓ | Variable cost n × 2 yield (3n crit) — singleton scarcity limits use; Intel holding guideline (4, not HARD) tolerates high-n plays; fail=nothing is the correct floor; threshold 40 confirmed | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: Intel tokens dispatched at Beat 3; durable resource, no card-level duration | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — maximum-yield collection aligns with Ghost intelligence doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | Adjacency restriction applied per 04-n6 — field collection op requires Ghost presence in target district or adjacent | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Art 02 §12); Findings cost; n validated at Beat 0 via arbiter_note (Art 04 §5 P20) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Beat 0: arbiter_note specifies ARBITER records declared n and validates Findings present; Beat 3 resolution per Art 03 §9, §11 | Art 03 §9, §11 |
| Data schema validation | ✓ | 04-n70 ✅ S95 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S112 | Art 04 §5 P26 |

#### Outstanding Issues

None.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Issues Resolved S112*

```python
GHO.CA.8 = Card(
    card_id      = "GHO.CA.8",  version = "v1.1",
    name    = "Full Take",
    tagline = "Saturate collection against a single target — maximum yield from a single operation.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Add,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 40,
    ring_mod        = {0: -15, 1: -10, 2: 0, 3: +10},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy = None,
    affinity        = None,
    restriction     = district(self|adjacent).faction(acting).presence > 0,
    cost            = resource.faction(acting).findings * n,  # n declared at submission; n >= 1; all n Findings physically present (Art 04 §5 P20)

    success     = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)) * (n * 2),
    successcrit = game.dispatch(faction(acting), IntelToken(faction=faction(target), quarter=game.quarter)) * n,   # +n = 3n total
    fail        = None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Some intelligence is gathered patiently. Some is taken all at once.",
    perspectives = {Ghost: "The take was complete. Everything they transmitted this Quarter. We have it."},
    design_note  = "Singleton. Variable cost: Ghost declares n at submission; cost = n Findings; success = 2n Intel tokens; crit success = 3n. Fail = nothing. Threshold 40 confirmed — variable cost and fail=nothing are sufficient risk; low threshold is the compensating upside. Adjacency restriction per 04-n6. Intel holding guideline is 4 (not HARD); high-n plays may exceed guideline.",
    arbiter_note = "At Beat 0: record declared n; validate n Findings present in case. At Beat 3: success = dispatch 2n IntelToken(faction=target) to Ghost's case; crit success = dispatch 3n; fail = nothing; crit fail = NotificationSlip to target.",
)
```

---

### GHO.CA.15 — ROUTING OVERRIDE *(stub)*
[↑ Covert Operations](#ghost-covert-operations)

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
GHO.CA.15 = Card(
    id      = "GHO.CA.15",  version = "v1.0",
    name    = "Routing Override",
    tagline = "Blindly intercept and redirect an opponent's covert operation.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Corrupt,  subject = TargetProfile,
    beat    = 2,  resolution = Automatic,
    cost    = resource.faction(Ghost).findings * 1 + intel_token * 1,
    success = "Ghost corrupts the first CA in target faction's Beat 3 resolution queue if it matches Ghost's specified parameters.",
    arbiter_note = "At Covert Dispatch, Ghost writes a target field (e.g., 'target_district') and expected value (e.g., 'Core'), plus a replacement value (e.g., 'Baryo'), in their Target Profile freeform space. At Beat 2: ARBITER checks target faction's first CA in the ARG. If that CA's Target Profile contains the exact field and value Ghost named, ARBITER silently crosses it out and writes Ghost's new value. If it does not match, Ghost's operation fizzles. The target faction executes their CA at Beat 3 against the new corrupted target.",
    design_note = "Beat 2 positional wager against a Beat 3 CA. Ghost must correctly predict a parameter of the opponent's first queued operation. The corruption is entirely silent until the operation resolves at Beat 3."
)
```


---

### Ghost — SCIF
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Converts existing faction-keyed Intel into future modifier capability. Spends one Intel token; ARBITER records the target faction's current structure block count in a SCIF Record card placed in Ghost's Dispatch Case. At Debrief, Ghost draws modifier cards equal to that count. Ghost is always building next Quarter's hand rather than spending this one. Yield scales with target development: SCIF against a lightly-built faction early game is modest; against a heavily-built Directorate or Guild late game it fills Ghost's modifier hand. The deferred payoff creates a planning horizon that no other faction can directly interrupt.

#### Card Story
Ghost cashes one piece of intelligence for something more durable. ARBITER records how deeply the target has built — and next Quarter, that depth becomes Ghost's tactical hand.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Converts Intel into future modifier capability — Ghost builds next Quarter's tactical hand rather than spending this one; deferred payoff no other faction can directly interrupt | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — intelligence as infrastructure for future action | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; IntelToken cost gates use on prior collection; yield scales with target development — balance concern flagged (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — deferred modifier economy is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Add/DebriefActionCard — SCIFRecord is a subtype; DA-01; registered in 00b §4 (agy S88, DB-34 ✅) | Art 04b §4, §5 |
| Balance | ✓ | Yield scales with target's structure count per ring; balance assessment deferred until Art 03 procedure locked | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: SCIFRecord instantiated at Beat 3; Debrief draw is Art 03 procedure, not a card-level lingering effect — compliant with Art 04 §5 P19 | — |
| Persistence | ✓ | Immediate — card fully resolved at Beat 3; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — Automatic resolution; restriction enforces Intel token presence | — |
| Portrait validity | ✓ | Ghost +1 submitter — intelligence-to-modifier conversion aligns with Ghost doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted operation; no district required | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; DebriefActionCard (type, DB:100) / SCIFRecord (DA-01) — registered in 00b §4 and Art 02 §13 | Art 02 §6–§8 |
| Supported by game procedure | ✓ | SCIFRecord instantiated at Beat 3 (Art 03 §9.4); Debrief draw procedure in Art 03 §11; DA-01 fields and procedure in Art 04 §12a | Art 03 §9, §11; Art 04 §12a |
| Data schema validation | ✓ | 04-n70 ✅ S95 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S112 | Art 04 §5 P26 |

#### Outstanding Issues

- **Balance — yield scaling:** SCIF yield grows as Guild and Directorate build. Playtest flag — non-blocking.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ S94 | |

```python
GHO.CA.9 = Card(
    card_id      = "GHO.CA.9",  version = "v1.1",
    name    = "SCIF",
    tagline = "Turn intelligence into operational assets.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Add,  subject = DebriefActionCard,  # subtype = SCIFRecord

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(acting).intel_tokens(faction=faction(target)) >= 1,
    cost        = IntelToken(faction=faction(target)) * 1,

    success     = DebriefActionCard(subtype=SCIFRecord, target=faction(target)),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "The structure count is the number of ways they have committed themselves. Ghost counts carefully.",
    perspectives = {Ghost: "We do not need to be inside their operation. We need to know how large it is."},
    design_note  = "Converts held intelligence into future modifier capability — Ghost builds next Quarter's hand from this Quarter's intelligence. Pairs with Station, Full Take, and Synthesize: the SCIF pipeline is the destination for accumulated faction-keyed Intel. Yield scales with target development, creating an intelligence premium on heavily-built opponents.",
    arbiter_note = "SCIFRecord procedure: Beat 3 instantiation (Art 03 §9.4); Debrief draw in Art 03 §11; DA-01 fields and procedure in Art 04 §12a.",
)
```

---

### Ghost — FLIP
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Economic arm of Ghost's intelligence pipeline. One faction-keyed Intel token consumed; ARBITER places 2 of the target faction's native resource in Ghost's Dispatch Case at Beat 3. Resources return at month-end with normal case contents — no deferred procedure required. Flip is the unlock for Ghost's higher-tier cards, which carry a secondary cost of Flip-acquired faction resources (the "target faction's assets turned against them" design direction, per GHO.CA.2 model). Layer is Economy per L175: primary effect is resource acquisition despite the Intel gating. Copy model confirmed: target's resource pool is not reduced. Quantity 2 confirmed as working value; final calibration deferred to playtest. Adjacency restriction applies per 04-n6 — field collection op requires Ghost presence in target district or adjacent.

#### Card Story
One Intel token, two of their resources. The target's reserves are untouched — Ghost didn't take from them. Ghost learned where the tap was.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Economic arm of Ghost's intelligence pipeline — converts faction-keyed Intel into target faction's native resource; unlock for higher-tier Ghost cards | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — resource redirection as intelligence exploitation | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; IntelToken cost enforces intelligence pipeline dependency; quantity 2 confirmed (playtest calibration) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence-gated resource acquisition is Ghost-exclusive | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/FactionNativeResource — Layer = Economy per L175 confirmed; copy model, not transfer | Art 04b §4, §5 |
| Balance | ✓ | Quantity 2 confirmed as working value; playtest calibration item. Copy model confirmed — target pool unchanged | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: resources dispatched at Beat 3; available at month-end via normal case return (Art 04 §5 P19 compliant) | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — Automatic resolution | — |
| Portrait validity | ✓ | Ghost +1 submitter — resource acquisition via intelligence pipeline aligns with Ghost doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | Adjacency restriction applied per 04-n6 — field collection op requires Ghost presence in target district or adjacent | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost; target faction native resource type delivered to case; no new components | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Resources in Dispatch Case returned at month-end per normal procedure — no new Art 03 step required | Art 03 §9, §11 |
| Data schema validation | ✓ | 04-n70 ✅ S95 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S112 | Art 04 §5 P26 |

#### Outstanding Issues

None.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Issues Resolved S112*

```python
GHO.CA.10 = Card(
    card_id      = "GHO.CA.10",  version = "v1.1",
    name    = "Flip",
    tagline = "Redirect a target faction's operational resources through Ghost supply channels.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Economy,  function = Add,  subject = FactionNativeResource,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy = None,
    affinity        = None,
    restriction     = (
        faction(acting).intel_tokens(faction=faction(target)) >= 1 and
        district(self|adjacent).faction(acting).presence > 0
    ),
    cost            = IntelToken(faction=faction(target)) * 1,

    success     = game.dispatch(faction(acting), resource.faction(target).native * 2),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Ghost does not steal. Ghost redirects what was already in motion.",
    perspectives = {Ghost: "Their resource. Our pipeline. They built something worth taking."},
    design_note  = "Layer=Economy per L175 — primary effect is resource acquisition despite intelligence gating. Copy model confirmed: target faction does NOT lose resources. Quantity 2 confirmed working value; final calibration deferred to playtest. Adjacency restriction per 04-n6 (combined with Intel token restriction). Resources dispatched to Ghost's Dispatch Case at Beat 3; returned at month-end. Higher-tier Ghost cards carry secondary cost = faction(target).native consumed on play (GHO.CA.2 model).",
    arbiter_note = "At Beat 3: consume IntelToken(faction=target) from Ghost's case. Dispatch 2 units of target faction's native resource type to Ghost's Dispatch Case. Target faction's resource pool is not reduced. Resources available to Ghost at month-end with normal case return.",
)
```

---

### Ghost — SIGNALS ANALYSIS
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's strategically decisive card. Reveals the target faction's Classified Directive privately to Ghost, enabling Ghost to engineer situations where pursuing a hidden objective requires betraying visible doctrine — Ghost's core win vector. Highest cost in the Ghost set (2 faction-keyed Intel tokens + 3 Findings) with the lowest threshold (30%), reflecting that this is a rare, high-investment play not available until Ghost has accumulated significant Intel reserves. Analytical work — no adjacency required, consistent with the GHO.CA.1-GHO.CA.5 pattern. Portrait modifier on success (+2 total) captures Ghost's doctrine that intelligence is only vindicated by operational use.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost's strategically decisive card — reveals Classified Directive enabling Ghost to engineer doctrine-betrayal situations; Ghost's core win vector | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — intelligence as strategic leverage | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; highest cost in Ghost set (2 Intel + 3 Findings); threshold 30 — reserved for Ghost players with Intel reserves; portrait AND semantics outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — Directive reveal is Ghost-exclusive win-condition card | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Reveal/ClassifiedDirective — component registration outstanding (Outstanding Issue) | Art 04b §4, §5 |
| Balance | ✓ | Threshold 30 + cost 2 Intel + 3 Findings — rarity level appropriate for Directive reveal; singleton | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: private information revealed once at Beat 3; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces Intel token floor (≥2) | — |
| Portrait validity | ✓ | submitter=+1 unconditional + modifier=+1 on success — AND semantics outstanding (Outstanding Issue) | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — no district target; operates on abstract ClassifiedDirective object | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken cost (×2); ClassifiedDirective as target_object — component registration outstanding (Outstanding Issue) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Private reveal via ARBITER screen; private faction-to-faction reveal procedure outstanding (Outstanding Issue) | Art 03 §9, §11; Art 07 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **BLOCKED — Classified Directive record-keeping procedure required.** The success mechanism requires ARBITER to hold a setup record of each faction's Classified Directive. This infrastructure does not exist. A Classified Directive management procedure (Art 06.x or equivalent) must be designed independently before this execution model can be finalized — do not build this procedure to support a single card. All other outstanding issues are secondary to this blocker.
- **ClassifiedDirective component:** `target_object = ClassifiedDirective` — confirm this is a registered component type in Art 02 series. May need to be added.
- **Private reveal procedure:** ARBITER reveals Directive across screen to Ghost player. Confirm Art 07 has or will have a procedure for private faction reveals (same mechanism as GHO.CA.2 IntelDeliverySlip?).
- **Portrait AND semantics:** `submitter=+1, modifier=+1, mod_where=game.outcome==Success` — confirm same model as GHO.CA.1 Pattern Match (submitter always fires; modifier fires additionally on success).

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Draft S59 — design pass pending*

```python
Card(
    id=TBD,  version="v1.0",  # ID pending PM05 04-n1
    name    = "Signals Analysis",
    tagline = "Deduce a target faction's Classified Directive from accumulated intelligence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Reveal,  subject = ClassifiedDirective,

    beat            = 3,
    resolution      = d100,
    threshold       = 30,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Probabilistic",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = ClassifiedDirective,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(acting).intel_tokens(faction=faction(target)) >= 2,
    cost        = IntelToken(faction=faction(target)) * 2 + resource.faction(acting).findings * 3,

    success     = game.reveal_private(
                    faction(target).classified_directive,
                    to  = faction(acting),
                    via = arbiter
                  ),
    successcrit = None,
    fail        = None,
    failcrit    = game.dispatch(faction(target), NotificationSlip),

    portrait = {Ghost: PortraitEntry(submitter=+1, modifier=+1, mod_where=game.outcome==Success)},

    narrative    = "The Directive is not a secret. It is a pattern. Ghost reads patterns.",
    perspectives = {Ghost: "We are not guessing. We have read enough of their decisions to know what they are trying to protect."},
    design_note  = "Ghost's highest-cost card. Cost: 2 faction-keyed Intel tokens + 3 Findings, all physically present (Art 04 §5 P20). Threshold 30 — reserved for Ghost players who have built Intel reserves. No adjacency restriction (analytical work — consistent with GHO.CA.1-GHO.CA.5 pattern). Portrait: submitter=+1 unconditional + modifier=+1 on success. ClassifiedDirective component type pending verification in Art 02 series.",
    arbiter_note = "Privately reveal target faction's Classified Directive to Ghost player across screen. Do not announce to table. Ghost may not publicly prove knowledge. Crit fail: NotificationSlip to target only — do not reveal what Ghost was attempting.",
)
```

---

### Ghost — SYNTHESIZE
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost's intelligence amplification card — converts one held Intel token into three, netting +2. Designed for the GATHER→SYNTHESIZE Double Case Pass combo (L145): play STD.CA.5 Gather in Month 1 to acquire an Intel token, then play Synthesize in Month 2 or 3 to multiply it before a high-cost operation (SCIF, Flip, Signals Analysis). The consumed token can be any faction-keyed token — Synthesize is processing, not targeting. Findings×1 is the analytical cost of converting raw surveillance into operational signal. The result is Ghost building Intel reserves without needing to place additional Gather operations.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Intelligence amplification — converts 1 token into 3 (net +2); enables GATHER→SYNTHESIZE combo that pre-loads high-cost operations (SCIF, Flip, Signals Analysis) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — processing as doctrine, not just collection | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; Findings×1 cost reflects analytical work; consumed token is any held token; generated token faction-keying outstanding (Outstanding Issue) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence processing is Ghost-exclusive pipeline capability | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Economy/Add/IntelToken — net amplification of Intel supply; Economy layer correct for resource generation effect | Art 04b §4, §5 |
| Balance | ✓ | Findings×1 + 1 IntelToken → 3 IntelTokens (net +2) — amplification rate reasonable; token faction-keying affects SCIF/Flip gate eligibility (Outstanding Issue) | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: tokens delivered at Beat 3; durable resource | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter only; submitter-bounded per SYN.PA.2 | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — internal intel processing; no district context | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken as both cost and subject; Findings cost; no new components | Art 02 §6–§8; Art 02 §12 |
| Supported by game procedure | ✓ | Beat 3 Automatic; tokens delivered at Beat 3; SCIF/Flip gate eligibility of generated tokens outstanding (Outstanding Issue) | Art 03 §9, §11 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **GATHER→SYNTHESIZE combo L145:** Confirm L145 is still the canonical reference for this combo — if L145 has been superseded or renumbered, update reference.

*Token faction-keying resolved S119: generated tokens carry the consumed token's faction key. Ghost consumes an X-keyed token and receives three X-keyed tokens. Enables the Gather→Synthesize→Flip pipeline (collect X-keyed token; amplify; use Flip to access Faction X's resources).*

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

*Migrated from Art 04 §8 (retired) Intel Economy block to Ghost extended section S59. Pre-convention flat format — full schema pass pending (04-47). Token keying resolved S119.*

```python
GHO.CA.6 = Card(
    id      = "GHO.CA.6",  card_id="GHO.CA.6",  version="v1.1",
    name    = "Synthesize",
    tagline = "Convert raw intelligence into operational clarity.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Economy,  function = Add,  subject = IntelToken,
    beat=3, resolution=Automatic, threshold=None, ring_mod=None, doctrine_mod=None, trigger=None,
    resolution_type="Transactional", outcome_type=None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,
    target_district=None, target_faction=None, target_object=IntelToken,
    target_taxonomy=None,
    affinity=None,
    restriction = faction(acting).intel_tokens.count >= 1,
    cost        = resource.faction(acting).findings * 1 + IntelToken(any) * 1,
    boost       = None,
    success     = game.dispatch(faction(acting), IntelToken(faction=consumed_token.faction) * 3),
    successcrit=None, fail=None, failcrit=None,
    portrait    = {Ghost: PortraitEntry(submitter=+1)},
    ps_framing  = None,
    narrative   = "Raw surveillance is noise. What Ghost does to it — that is signal.",
    perspectives = {Ghost: "We don't just gather. We process. The difference is what we are."},
    design_note  = "GATHER→SYNTHESIZE Double Case Pass combo (L145): Gather in Month 1, Synthesize in Month 2/3. Consumed token is any held token — not required to be faction-keyed. Generated tokens carry the consumed token's faction key (S119 decision) — enables Gather→Synthesize→Flip pipeline for any target faction.",
    arbiter_note = "Consume 1 held Intel token (any faction key) and 1 Findings from Ghost's supply. Deliver 3 Intel tokens keyed to the consumed token's faction to Ghost's Dispatch Case.",
)
```

---

### Ghost — SOURCE SUBSTITUTION
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Pure utility card — re-keys a held Intel token from its current faction attribution to a different faction. Ghost submits a token in their dispatch case; ARBITER alters the faction field and returns it. Quarter field unchanged; freshness carries over. Cost is the CA slot — no Findings spent. The tradeoff is opportunity cost: spending a covert action on re-keying rather than direct collection. Primary use: Ghost accumulates tokens on accessible targets but needs tokens keyed to specific factions to unlock higher-tier plays (SCIF, Flip, Intercept all require faction-matched tokens). Automatic — no dice, no risk.

Standard equivalent: PM05 04-n15.

#### Card Story
Ghost submits a token from their case. ARBITER alters the name on it. The token returns — it now says what Ghost needs it to say.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Token re-keying enables Ghost's intelligence pipeline — converts available tokens into faction-matched currency for higher-tier plays | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective — record alteration as operational routine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; no Findings cost — CA slot is the gate; Automatic reflects Ghost's precision (no chance of failure on a technical alteration) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence record manipulation is Ghost-exclusive; standard equivalent flagged PM05 04-n15 | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/IntelToken — alters the faction field on an existing token; Corrupt is correct (field modification of an existing component) | Art 04b §4 |
| Balance | ✓ | Cost = CA slot only; Automatic resolution; restriction = must hold a token. Opportunity cost is the constraint | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: token altered and returned at Beat 3; no lingering game-state marker | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat | Art 04 §6 |
| Trigger validity | ✓ | N/A — Automatic; trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter — intelligence manipulation is core Ghost doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — no district involvement; token is held asset, faction-targeted re-key only | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken as target_object; no new physical components; quarter field preserved | Art 02 §12 |
| Supported by game procedure | ✓ | Token submitted in case; ARBITER alters faction field at Beat 3; returns to Ghost case — covered by standard Beat 3 cleanup | Art 03 §9.4 |
| Data schema validation | ✓ | 04-n70 ✅ S95 | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Card Story written S112 | Art 04 §5 P26 |

#### Outstanding Issues

None.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

*Redesigned S112 — plant mode retired; Automatic resolution; cost = CA slot*

```python
GHO.CA.12 = Card(
    card_id      = "GHO.CA.12",  version = "v1.0",
    name    = "Source Substitution",
    tagline = "Alter the faction attribution on a held Intel token.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Corrupt,  subject = IntelToken,

    beat            = 3,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.opponent,
    target_object   = IntelToken(held, faction(acting)),

    target_taxonomy = None,
    affinity        = None,
    restriction     = faction(acting).intel_tokens() >= 1,
    cost            = None,

    success     = arbiter.corrupt(target_object, field=faction_name, value=faction(target)),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    on_accept  = None,
    on_decline = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "The record says what Ghost needs it to say.",
    perspectives = {Ghost: "The attribution is wrong. It will stay wrong. What matters is what Ghost does with it next."},
    design_note  = "Re-keys an Intel token's faction field to faction(target). Quarter field unchanged — freshness carries over. Cost = CA slot (no Findings). Automatic — no dice, no risk. Token is target_object: submitted in case alongside card, returned after alteration. Standard equivalent: PM05 04-n15.",
    arbiter_note = "Token submitted in Ghost's case alongside card. At Beat 3: alter faction_name field on token to faction(target); return altered token to Ghost's case. No announcement.",
)
```

---

### Ghost — BACKDATE 🚫 BLOCKED
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Intelligence poisoning — alter the quarter field on a held Intel token to make it appear older. A Fresh token can be degraded to Stale or Expired. The primary use is the poisoned gift (plant mode): deliver a degraded token to a target faction who will discover — when they attempt to use it — that their intelligence is stale or worthless. The acting faction sacrifices a functional token to waste a future opposing action. Keep mode has narrower use: Ghost may want to make an operation appear to have occurred earlier (strategic alibi). Threshold 30 is harder than Source Substitution (45) because temporal records are more verifiable — altering when something happened is more conspicuous than altering who. Fail destroys the token; failcrit notifies the originally-named faction. Ghost adjacency applies in plant mode.

Standard equivalent: PM05 04-n15.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Temporal falsification of intelligence records — primary use is poisoned gift (plant Expired token on target to waste their attribution play) | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — temporal record manipulation as operational doctrine | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; threshold 30 (harder than Source Substitution 45) reflects temporal records are more verifiable; same keep/plant dual mode as Source Substitution | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Corrupt/IntelToken (quarter field) — distinct from Source Substitution (faction field) | Art 04b §4 |
| Balance | ✓ | Threshold 30 — harder than Source Substitution; temporal records more verifiable; fail destroys token — real cost | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: token altered and returned/planted at Beat 3; fail destroys token at Beat 3 | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces Intel token presence | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — faction-targeted; no adjacency restriction. Plant mode retired S112. Card 🚫 BLOCKED (L222). | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken as both cost and target; requires two writable fields (faction + quarter) outstanding (Outstanding Issue); instructions slip in case | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Plant mode delivery protocol same as Source Substitution — outstanding (Outstanding Issue) | Art 02 §6–§8; Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Outstanding Issues

- **Token writable fields:** Intel token component must support two writable fields (faction name + quarter). Confirm component design in Art 02.
- **Plant mode delivery protocol:** Same as Source Substitution — discreet delivery to target terminal during Beat 3 cleanup; procedure not yet defined in Art 03/07.
- **🚫 BLOCKED (S107, L222):** Two permanent constraints. (1) Location: Intel token in private terminal zone is not reachable by opposing card. (2) GR 7.2b: the quarter field records when the token was committed — a committed fact; retroactive alteration violates the finality principle. The provenance-field approach is permanently closed. Fundamental redesign required; design path must be additive. Cross-ref: Art 04b §8.1 item 3, PM05 04-n103.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | 🚫 BLOCKED | — | — |

```python
Backdate = Card(
    id      = "Ghost-ext-TBD",  version = "v1.0",
    name    = "Backdate",
    tagline = "Corrupt the quarter field on a held Intel token — make it appear older than it is.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Corrupt,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 30,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Deceptive",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = faction.any_or_none,  # None = keep; named = plant
    target_object   = intel_token.held,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Ghost).holds_intel_token(count=1),
    cost        = resource.faction(Ghost).findings * 2 + intel_token.held * 1,

    # Instructions slip in case: [new quarter — must be earlier than current] | [return: self / named faction]
    success = (
        arbiter.corrupt(intel_token.held, field=quarter, value=declared_earlier_quarter),
        if target_faction == None:
            arbiter.return_to_case(intel_token),
        else:
            arbiter.deliver_discreet(intel_token, target_faction),
    ),
    successcrit = None,
    fail        = arbiter.destroy(intel_token),
    failcrit    = (
        arbiter.destroy(intel_token),
        arbiter.dispatch(NotificationSlip, recipient=intel_token.faction_named),
    ),

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "The question is not what the token says. The question is when it says it happened.",
    perspectives = {
        Ghost: "An old record is a useless record. We are making it old.",
    },
    design_note  = "Temporal falsification — quarter field only. Distinct from Source Substitution (faction field). Threshold 30 vs 45: altering when is harder than altering who. Primary use: plant mode to deliver degraded/Expired token as poisoned gift — target wastes a future attribution play. Keep mode: make own operations appear to have occurred earlier. Intel token component must support two writable fields (faction + quarter). Standard equivalent PM05 04-n15.",
    arbiter_note = "Instructions slip in case: new quarter number (must pre-date current Quarter) + keep or plant destination. Beat 3: d100 vs 30. On success: alter quarter field; token age reclassified accordingly (may shift Fresh → Stale, Stale → Expired, or Fresh → Expired depending on magnitude). Keep: return in case. Plant: discreet delivery to target terminal (same protocol as Source Substitution). On fail: destroy token. On failcrit: destroy + NotificationSlip to faction named on token.",
)
```

---

### Ghost — FIELD VERIFICATION 🚫 BLOCKED
[↑ Covert Operations](#ghost-covert-operations)

#### Design Rationale
Ghost re-validates expired intelligence. An Expired Intel token is submitted in the dispatch case with no instructions — the question posed to ARBITER is simply: is this still current? On success, the token's quarter is updated to the present Quarter and its classification becomes Fresh. On fail, the token is returned Expired and Ghost has lost only the dispatch slot. No Findings cost — the slot IS the investment. Threshold 35 reflects genuine uncertainty: intelligence gathered 4+ quarters ago may or may not still describe reality; there is no guarantee the world has not changed. This is not falsification — Ghost is genuinely re-checking a cold lead. Self-operation only; no adjacency required. Distinct from Source Substitution and Backdate (which falsify; this verifies).

Standard equivalent: PM05 04-n15 (hired investigator reopening cold case — same mechanic, costs Findings, lower threshold).

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost re-validating aged intelligence — "understanding must precede action" includes verifying that old understanding is still current; Expired → Fresh recovery | Art 00 §7 |
| Voice fit | ✓ | Faction-specific; single Ghost perspective by design — verification as discipline, not just collection | Art 00 §7 |
| Doctrine alignment | ✓ | Ghost only; no Findings cost — slot IS the investment; self-operation only; distinct from Source Substitution/Backdate (falsification vs. verification) | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | CovertOperation / FactionSpecific (Ghost) — intelligence pipeline methodology; standard equivalent flagged PM05 04-n15 | Art 04 §6.2; Art 04b §5 |
| Taxonomy fit | ✓ | Information/Recover/IntelToken — Recover returns a degraded element to active play; Expired → Fresh is a recovery | Art 04b §4 |
| Balance | ✓ | No Findings cost; dispatch slot only; fail = slot wasted, token returned (no token loss); threshold 35 creates meaningful failure rate | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate: token updated or returned at Beat 3; no persistent state | — |
| Persistence | ✓ | Immediate — card fully resolved at resolution beat; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | N/A — trigger = None; restriction enforces Expired token in case | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded; re-validation before acting is Ghost's core doctrine | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — self-operation on held token; no district context | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (Expired) as cost and target; requires writable quarter field (same as Backdate — see Backdate Outstanding Issue) | Art 02 §6–§8 |
| Supported by game procedure | ✓ | Self-operation; no adjacency required; ARBITER updates quarter field on success, returns token on fail | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

- **🚫 BLOCKED (S107, L222):** GR 7.2b — the quarter field records when the token was committed; updating it to the current Quarter alters a committed provenance field. The field-update approach is permanently closed. Fundamental redesign required. Cross-ref: Art 04b §8.1 item 3, PM05 04-n103.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | 🚫 BLOCKED | — | — |

```python
FieldVerification = Card(
    id      = "Ghost-ext-TBD",  version = "v1.0",
    name    = "Field Verification",
    tagline = "Re-validate an Expired Intel token — confirm the intelligence is still current.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Recover,  subject = IntelToken,

    beat            = 3,
    resolution      = d100,
    threshold       = 35,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Verification",
    outcome_type    = None,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,  # self-operation; no adjacency required
    target_faction  = None,
    target_object   = intel_token.held,  # must be Expired; submitted in case

    target_taxonomy=None,
    affinity    = None,
    restriction = intel_token.held.age == Expired,
    cost        = None,  # no resource cost; dispatch slot is the investment (Governing Rule 7.3c)

    success = (
        arbiter.update(intel_token.held, field=quarter, value=game.current_quarter),
        arbiter.return_to_case(intel_token),
        # token reclassified Fresh (0–1 quarters old = current Quarter)
    ),
    successcrit = None,
    fail        = arbiter.return_to_case(intel_token),  # token returned Expired; no loss
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "The intelligence is old. The question is whether it is still true.",
    perspectives = {
        Ghost: "We go back to check. The answer determines whether we can use this at all.",
    },
    design_note  = "Self-operation to re-validate cold intelligence. No Findings cost — dispatch slot only. Fail returns the token Expired (no loss beyond the slot). Success advances token to Fresh (current Quarter). d100 threshold 35 reflects genuine uncertainty about whether aged intelligence still describes reality. Not falsification — Ghost is actually checking. Distinct from Source Substitution and Backdate. Standard equivalent (hired PI, higher cost) flagged PM05 04-n15.",
    arbiter_note = "Token submitted in case. Restriction: token must be Expired. No instructions slip needed. Beat 3: d100 vs 35. On success: update token's quarter field to current Quarter; token is now Fresh; return in case. On fail: return token in case unchanged (still Expired). No resource consumed either outcome.",
)
```

---


---

---

### GHO.CA.13 — PHANTOM ACCOUNTS *(stub)*
[↑ Covert Operations](#ghost-covert-operations)

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
GHO.CA.13 = Card(
    id      = "GHO.CA.13",  version = "v1.1",
    name    = "Phantom Accounts",
    tagline = "Siphon a shadow copy of an opponent's influence-based resource generation.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Economy,  function = Add,  subject = DebriefActionCard,
    beat    = 3,  resolution = d100,  threshold = 50,
    cost    = resource.faction(Ghost).findings * 2,
    success = "Arbiter places 1 DA-02 (PhantomRecord) in Ghost's Dispatch Case. At debrief, Ghost gains district native resources equal to target_faction's influence-based generation.",
    design_note = "A financial twin to SCIF. Instead of generating Modifier cards off of structural density, this converts Findings into a mirrored payout of the target's passive district income."
)
```

---

### GHO.CA.14 — GHOST PROTOCOL *(stub)*
[↑ Covert Operations](#ghost-covert-operations)

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
GHO.CA.14 = Card(
    id      = "GHO.CA.14",  version = "v1.1",
    name    = "Ghost Protocol",
    tagline = "Completely erase an opponent's operation from existence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Submission,  function = Block,  subject = CovertOperation,
    beat    = 2,  resolution = Automatic,
    cost    = resource.faction(Ghost).findings * 2 + resource.faction(Ghost).exposure * 1 + resource.faction(Ghost).capital * 1 + intel_token * 1,
    success = "The Arbiter invalidates and removes the first Covert Operation submitted by target_faction in Beat 3.",
    design_note = "Massive multi-resource cost to justify an unblockable, blind veto of an opponent's action."
)
```

### Ghost — Public Acts
[↑ Ghost](#ghost)

| Card | Name |
|------|------|
| [GHO.PA.1](#p17-publish-analysis) | Publish Analysis |
| [GHO.PA.2](#p18-signal-review-request) | Signal Review Request |
| [GHO.PA.3](#ghopa3--declassified-records) | Declassified Records |
| [GHO.PA.4](#ghopa4--public-threat-assessment) | Public Threat Assessment |
| [GHO.PA.5](#ghopa5--agency-recruitment-fair) | Agency Recruitment Fair |

### GHO.PA.1 — PUBLISH ANALYSIS
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Ghost's highest-cost PA — a simultaneous public attribution of two factions using two Intel tokens as evidence. The token requirement is the certainty check: Ghost does not publish speculation. Two tokens naming different factions are spent; both attributions are announced at Beat 4. Each named faction loses −2 PS; Ghost gains +2 PS flat. Ghost pays 3 Findings (their core intelligence currency) plus two Intel tokens for a decisive multi-target public strike — the cost reflects that going public is doctrinally expensive for Ghost even when the intelligence justifies it. Portrait +1: Ghost acts on doctrine when understanding precedes the disclosure decision.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost publishing curated analysis is a calculated, rare public act — the cost enforces rarity | Art 00 §7 |
| Voice fit | ✓ | Ghost on-doctrine; Directorate (aligned): verified, sequenced disclosure; Network (opposed): held both when one was enough | Art 00 §7, §9 |
| Doctrine alignment | ✓ | "Understanding must precede action" — Ghost publishes only when two tokens confirm both attributions. Portrait +1: calculated disclosure from position of knowledge. 3 Findings cost reflects that public disclosure is doctrinally expensive for Ghost | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Reveal / ActionAttribution (multi-target) | Art 04b §4 |
| Balance | ✓ | 3 Findings + 2 Intel tokens; Automatic; two targets −2 PS each; Ghost +2 PS. High cost, high yield. Token acquisition is the natural limiter | Art 02 §6–§7 |
| Effect duration | ✓ | PS shifts are immediate; card persistence = Immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; no lingering game-state marker | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded. Published from position of knowledge — doctrine affirmed | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — two faction targets; no district reference. N/A | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken (two, faction-keyed to different targets; Art 02 §6); Findings × 3 cost (Art 02 §8) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Two targets named at Phase B; both tokens submitted; Automatic Beat 4 | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
GHO.PA.1 = Card(
    id      = "GHO.PA.1",  version="v1.0",
    name    = "Publish Analysis",
    tagline = "Release curated intelligence simultaneously attributing operations to two factions — a calculated, costly disclosure.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Reveal,  subject = ActionAttribution,

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
    target_faction  = faction.two_opponents,  # two different factions named at Phase B
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = (
        faction(Ghost).holds_intel_token(faction=target1) and
        faction(Ghost).holds_intel_token(faction=target2) and
        target1 != target2
    ),
    cost = (
        resource.faction(Ghost).findings * 3
        + intel_token(target=faction(target1)) * 1
        + intel_token(target=faction(target2)) * 1
    ),

    success = (
        arbiter.announce(attribution=target1, context=intel_token_1.quarter),
        arbiter.announce(attribution=target2, context=intel_token_2.quarter),
        faction(target1).standing -= 2,
        faction(target2).standing -= 2,
        faction(Ghost).standing   += 2,
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Ghost does not publish because it wants credit. Ghost publishes because the analysis is complete and the disclosure serves more than the concealment.",
    perspectives = {
        Ghost:       "We have done the work. Both attributions are supported. The timing is correct. We publish.",
        Directorate: "Ghost discloses both attributions from verified position. The timing was chosen. The evidence was held until both targets were confirmed. This is how intelligence should enter the record.",  # aligned
        Network:     "Ghost waited for both confirmations. We published after the first. The second attribution was true by the time Ghost released it — and so was all the damage that came between.",  # opposed
    },
    design_note  = "Ghost's highest-cost PA. 3 Findings + 2 Intel tokens (different factions). Automatic — token requirement is the certainty check (Ghost does not publish speculation). Simultaneous dual attribution: each target −2 PS, Ghost +2 PS flat. Portrait +1: calculated disclosure affirms 'understanding must precede action' doctrine. Option 3 (operational blackout mechanic) flagged as PM05 item for potential Network PA extension.",
    arbiter_note = "Phase B: Ghost names two target factions. Both Intel tokens submitted with case. Beat 4: announce '[Ghost] attributes [op type, quarter] to [target1]' and '[Ghost] attributes [op type, quarter] to [target2].' Each target −2 PS. Ghost +2 PS. Both tokens spent.",
)
```

---

### GHO.PA.2 — SIGNAL REVIEW REQUEST
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Ghost uses institutional channels to apply operational pressure on a named faction. The effect is a −15 threshold penalty on that faction's covert operations in the named district next Month (Transient). Ghost gains no PS — this is a tool, not a stage. Ghost adjacency applies — Ghost must have presence in a district adjacent to the target. Persistence = Transient: the GHO.PA.2 card stays face-up on the table with a marker on the target district until Close Month of next Month, serving as the active condition indicator. ARBITER removes the card and returns it to Ghost at Close Month.

#### Card Story
⚠ Story pending 04-n79.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost using institutional accountability to enforce operational scrutiny is on-doctrine and narratively grounded | Art 00 §7 |
| Voice fit | ✓ | Ghost on-doctrine; Syndicate (aligned): institutional tool with no exposure cost; Guild (opposed): bureaucratic delay vs. direct action | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Ghost uses the institutional channel as a tool, not a stage — no PS gain. Adjacency requirement grounds the card in Ghost's operational footprint. Portrait +1: submitter-bounded | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Resolution / Modify / CovertOperation (difficulty) | Art 04b §4 |
| Balance | ✓ | 2 Findings; −15 threshold (meaningful but not absolute block); Transient. Ghost adjacency limits targeting range | Art 02 §6–§7 |
| Effect duration | ✓ | Threshold modifier is Transient (until Close Month of next Month — within-Quarter). No multi-Quarter duration | Art 04 §5 P19 |
| Persistence | ✓ | Transient — card stays face-up on table with district marker until Close Month next Month | Art 04 §6 |
| Trigger validity | ✓ | trigger = None — N/A | — |
| Portrait validity | ✓ | Ghost +1: submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = district.any — valid zone; restriction: Ghost presence in district adjacent to target | Art 01 §6–§7 |
| Supported by components | ✓ | No new component — threshold modifier is a world condition tracked by ARBITER; Findings × 2 cost (Art 02 §8) | Art 02 §8 |
| Supported by game procedure | ✓ | Physical tracking: GHO.PA.2 card face-up + district marker; ARBITER removes at Close Month next Month | Art 03 §9.4 |
| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | ✓ | |

```python
GHO.PA.2 = Card(
    id      = "GHO.PA.2",  version="v1.0",
    name    = "Signal Review Request",
    tagline = "Formally request institutional scrutiny on a faction's next covert operation in a named district.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Resolution,  function = Modify,  subject = CovertOperation,

    beat            = 4,
    resolution      = Automatic,
    threshold       = None,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Transient,  # card stays on table with district marker until Close Month next Month
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any,
    target_faction  = faction.opponent,
    target_object   = None,

    target_taxonomy=None,
    affinity    = None,
    restriction = faction(Ghost).presence(district.adjacent_to(target_district)) > 0,
    cost        = resource.faction(Ghost).findings * 2,

    success = game.world_condition(
        scope    = district(target),
        target   = covert_op(faction=target_faction),
        effect   = threshold -= 15,
        duration = Transient,  # Close Month of next Month
    ),
    # Ghost does not gain PS — uses the channel as a tool, not a stage

    successcrit = None,
    fail        = None,
    failcrit    = None,

    portrait = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Ghost does not need credit for this. The scrutiny is the point.",
    perspectives = {
        Ghost:     "We are not making an accusation. We are requesting that the process do what the process is designed to do.",
        Syndicate: "Ghost asks ARBITER to enforce the review. No exposure, no escalation, no record beyond the request itself. We recognize the structure. The target carries the friction. Ghost carries nothing.",  # aligned
        Guild:     "Ghost routes the pressure through ARBITER rather than holding the position itself. The district gets harder to operate in. Nothing is built. Ghost calls this strategy. Guild calls it avoidance.",  # opposed
    },
    design_note  = "Ghost operational pressure PA. Uses institutional scrutiny (ARBITER) to apply −15 threshold to target faction's covert ops in named district next Month. No PS gain for Ghost — the channel is a tool. Ghost adjacency: must have presence in district adjacent to target. Persistence = Transient: GHO.PA.2 card face-up on table + district marker until Close Month of next Month. Multiple P18s from different Months can stack. Distinct from GHO.PA.1 (attribution) — GHO.PA.2 creates ongoing pressure without disclosure.",
    arbiter_note = "Beat 4: place GHO.PA.2 card face-up on table with marker on target district. Apply −15 threshold penalty to all covert operations submitted by target faction in target district next Month (Beat 3). Card expires Close Month that Month — announce removal, return card to Ghost. Multiple GHO.PA.2 cards on same district from different Months stack (each tracked independently). Ghost adjacency enforced at Beat 0.",
)
```

---

### GHO.PA.3 — DECLASSIFIED RECORDS
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Declassified Records converts accumulated expired Intel tokens into Public Standing through formal public disclosure. The base card (+1 PS, threshold 50, cost 1 Findings) is playable on its own; the boost mechanic is the amplifier. Each expired token submitted adds one BM-xx marker — the standard BM-xx mechanism then multiplies all effects by (1+n). Three expired tokens turns a +1 PS play into +4 PS, and the failcrit into −4 PS. The design rewards multi-Quarter Intel discipline: Ghost factions that run intelligence operations over time without spending their tokens covertly build a deferred credibility reserve. The restriction (at least 1 expired token) keeps the card grounded narratively — Ghost releases *something*; a blank disclosure is not this card. The Faction Player may optionally give a brief in-character account of what records are being released; this is not a procedure step.

#### Card Story
Ghost submits the case files in order — sequential, dated, attributed. The records are expired. The intelligence is cold. The point is that Ghost kept them, and kept them clean, and is releasing them now because the moment is right. Each file laid on the table is a demonstration that the agency did the work while others were reacting.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Formal release of archived intelligence as institutional credibility play — information is power, including cold information released on Ghost's terms | Art 00 §7 |
| Voice fit | ✓ | Ghost on-doctrine; Directorate (aligned): sequenced formal disclosure is the proper channel; Network (opposed): "publish when you have it" conflicts with Ghost's timing discipline | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Patience and sequenced disclosure are Ghost doctrine. Portrait +1 submitter. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Remove / IntelToken — expired qualifier handled via restriction + boost field | Art 04b §4 |
| Balance | ✓ | Base: 1 Findings, +1 PS at threshold 50. Boost: each expired token ×(1+n). Risk scales with depth — failcrit = −(1+n) PS | Art 02 §6–§7 |
| Effect duration | ✓ | PS shift immediate | Art 04 §5 P19 |
| Persistence | ✓ | Immediate | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None — tokens are held, not placed | Art 01 §6–§7 |
| Supported by components | ✓ | IntelToken expired (Art 02 §9); BM-xx (Art 02 §12); Findings × 1 (Art 02 §8) | Art 02 §8–§9, §12 |
| Supported by game procedure | ✓ | BM-xx at Beat 4: boost detection added Art 03 §9.4.3.1.0.0 (S109); threshold at Art 03 §9.4.3.2.0; effect multiplication at Art 03 §9.4.3.3 | Art 03 §9.4.3 |
| Data schema validation | ✓ | All §6.1 fields present | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Story block above | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
GHO.PA.3 = Card(
    id      = "GHO.PA.3",  version="v1.0",
    name    = "Declassified Records",
    tagline = "Release expired intelligence as institutional record — each file compounds the disclosure.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Remove,  subject = IntelToken,

    beat            = 4,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = None,
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = None,
    target_faction  = None,
    target_object   = None,
    target_taxonomy = None,

    affinity    = None,
    restriction = count(intel_token(holder=Ghost, status=Expired)) >= 1,
    cost        = resource.faction(Ghost).findings * 1,
    boost       = intel_token(holder=Ghost, status=Expired),  # 1 expired token = 1 BM-xx; BM-xx ×(1+n) all effects at Art 03 §9.4.3.3

    success     = faction(Ghost).standing.add(1),
    successcrit = faction(Ghost).standing.add(1),  # +1 PS additional delta; also ×(1+n) via BM-xx
    fail        = None,
    failcrit    = faction(Ghost).standing.remove(1),  # delta from fail; also ×(1+n) via BM-xx

    on_accept  = None,
    on_decline = None,

    portrait   = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Ghost does not release because it ran out of options. Ghost releases because it chose this moment, these records, and this account. The archive is not empty — this is a selection.",
    perspectives = {
        Ghost:       "The tokens are expired. The operations they document are closed. We are not losing intelligence by releasing this — we are spending it correctly.",
        Directorate: "Ghost held these until the moment suited them. The records are verified. The disclosure is formal. This is how intelligence should enter the public domain.",
        Network:     "Ghost sat on this for three Quarters and then picked their moment. We published when we had it. Ghost published when it helped Ghost.",
    },
    design_note  = "Base success = +1 PS; successcrit = +1 PS additional. Boost = expired Intel tokens (status=Expired, holder=Ghost); each submitted token = 1 BM-xx at Art 02 §9.4.3.1.0.0. BM-xx ×(1+n) multiplies all effects: n tokens → +(1+n) PS on success; +(1+n)+1 PS on successcrit (success + crit both multiplied); −(1+n) PS on failcrit. Restriction ensures at least 1 expired token present (narrative grounding). Faction Player may optionally narrate what records are being declassified — this is not a procedure step.",
    arbiter_note = "Phase B: Ghost declares expired tokens (status=Expired) being submitted as boost — record count as n. Beat 4 Art 03 §9.4.3.1.0.0: place n BM-xx on card; expired tokens deposited to Dossier at Art 02 §9.4.3.1.0.1. Art 03 §9.4.3.3: effects ×(1+n). Success: Ghost +(1+n) PS. Successcrit: Ghost +(1+n) PS success + +(1+n) PS crit delta = +(2+2n) PS total. Fail: no effect. Failcrit: Ghost −(1+n) PS.",
)
```

---

### GHO.PA.4 — PUBLIC THREAT ASSESSMENT
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Ghost forces ARBITER to publicly reveal a Broadcast Effect Card. The Broadcast Card (public face) is already visible in the Situation Report Zone — Ghost is naming the thing the table can already see. The BEC (mechanical face, ARBITER Tableau) is what Ghost is extracting. GR 10.1b obligates ARBITER to disclose from its own domain when a valid trigger is submitted, so resolution is Automatic. The +1 PS reflects that forcing institutional transparency is itself a credibility act. BC/BEC linking is already established at Art 02 §7.2.1 — no new mechanism required. The named BC is recorded on the Target Profile at Phase B (target object field, S109).

#### Card Story
Ghost files the request before Beat 4. The Broadcast Card has been face-up all Quarter — its name, its narrative, its presence. What Ghost is asking for is the other half. ARBITER opens the file. The table reads the effect for the first time. Ghost already knew what to ask.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Forcing disclosure of hidden mechanical effects — Ghost doctrine: information asymmetry is a threat to be corrected | Art 00 §7 |
| Voice fit | ✓ | Ghost on-doctrine; Directorate (aligned): formal disclosure through proper channel; Network (opposed): "we'd have published it sooner" | Art 00 §7, §9 |
| Doctrine alignment | ✓ | Disclosure from institutional authority is on-doctrine. Portrait +1 submitter. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Information / Reveal / BroadcastEffectCard — GR 10.1b governs; ARBITER performs the reveal | Art 04b §4 |
| Balance | ✓ | Automatic. Cost: 1 Findings + PA slot. Reward: table-wide BEC information + +1 PS. Limiter: requires active BC. | Art 02 §6–§7 |
| Effect duration | ✓ | Reveal immediate; PS immediate; BEC stays in Tableau | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — BEC returned to Tableau; mechanical effects continue per Art 03 §9.4.1.1 / Art 03 §9.4.3.0.1 | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | target_district = None; target_object = BroadcastCard (Situation Report Zone) | Art 01 §6–§7 |
| Supported by components | ✓ | BroadcastCard (DB:25, Art 02 §10); BroadcastEffectCard (DB:98, Art 02 §10); Target Profile target-object field (DB:48, Art 02 §8 — S109); Findings × 1 (Art 02 §8) | Art 02 §8, §10 |
| Supported by game procedure | ✓ | §7.2.1 establishes BC/BEC link at setup. Art 03 §9.4.3.3.0 VM-xx placement clause; Art 03 §9.4.3.1.3 BEC public resolution step (S110). | Art 03 §7.2.1, §9.4.3.1.3, §9.4.3.3 |
| Data schema validation | ✓ | All §6.1 fields present | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Story block above | Art 04 §5 P26 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
GHO.PA.4 = Card(
    id      = "GHO.PA.4",  version="v1.0",
    name    = "Public Threat Assessment",
    tagline = "Name a Situation Report. ARBITER opens the file.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Ghost,

    layer    = Information,  function = Reveal,  subject = BroadcastEffectCard,

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
    target_faction  = None,
    target_object   = BroadcastCard.named,  # declared at Phase B on Target Profile; must be active in Situation Report Zone
    target_taxonomy = None,

    affinity    = None,
    restriction = count(broadcast_card(zone=SituationReportZone, status=Active)) >= 1,
    cost        = resource.faction(Ghost).findings * 1 + resource.faction(Ghost).exposure * 1,
    boost       = None,

    success = (
        arbiter.place_vm(broadcast_effect_card(linked_to=target_object)),
        faction(Ghost).standing.add(1),
    ),
    successcrit = None,
    fail        = None,
    failcrit    = None,

    on_accept  = None,
    on_decline = None,

    portrait   = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = "Ghost does not wait to find out what the Situation Report means. Ghost asks ARBITER, on the record, in front of everyone.",
    perspectives = {
        Ghost:       "The broadcast is public. The effect is not. That asymmetry is not information — it's concealment. We are correcting the record.",
        Directorate: "Ghost has formalized the disclosure request. ARBITER complied. The effect was known to us already, but now it is known to everyone. We note this.",
        Network:     "We would have published that two weeks ago if we had it. Ghost had the institutional standing to ask. That's the difference.",
    },
    design_note  = "Automatic — GR 10.1b obligates ARBITER to disclose from own domain when a valid trigger is submitted. Ghost names a Broadcast Card at Phase B (recorded on Target Profile target-object field); ARBITER places VM-xx on the linked BEC at Art 03 §9.4.3.3.0. BEC resolves publicly at Art 03 §9.4.3.1.3 when the next PA in initiative order is reached, or at Art 03 §9.4.1.1 next Quarter if Ghost plays last. BC/BEC link established at Art 02 §7.2.1; no new mechanism required. +1 PS: forcing institutional transparency is a credibility act. Portrait +1: disclosure from institutional authority is on-doctrine Cost reasoning: Exposure represents the deliberate unmasking of the threat to the public, amplifying the raw intelligence.",
    arbiter_note = None,
)
```

---

### GHO.PA.5 — AGENCY RECRUITMENT FAIR
[↑ Public Acts](#ghost-public-acts)

#### Design Rationale
Ghost's only territory PA — operates entirely in the open, targeting districts where the analytical workforce already lives. Career fairs, public outreach, visible institutional presence. Distinct from STD.CA.3 Campaign (covert, +1 chip, any district): this is public (+2 chips, declared at Phase B, React-able), costs Ghost's own resource, and is restricted to the 4 Findings-generating districts where Ghost's doctrine is most legible. PA slot + 1 Findings justifies the +2 chip output. Ring modifier: easier in Baryo (University Perimeter — Ghost's natural Baryo anchor), harder in Core (Chorus Research — high-prestige, contested institutional space). Successcrit +1 PS: a well-attended fair is a public credibility event. Failcrit −1 PS: low turnout in public is an embarrassment. Ghost adjacency applies — must have presence in a district adjacent to the target Findings district.

#### Card Story
Ghost files the act at Phase B. A table. A banner. Printed materials no other faction would bother preparing. The researchers in this district have been watching Ghost operate for two Quarters — they know what the work is. By Beat 4 the conversations have happened. Ghost has presence now, not just access. The district noted the distinction.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost operating in public in knowledge districts — recruitment = institutional legitimacy, not covert expansion | Art 00 §7 |
| Voice fit | ✓ | Ghost-specific; Directorate (aligned) watches but doesn't interfere — this is procedure, not threat; Network (opposed) notes Ghost is building in the open what they normally build in the shadows | Art 00 §7, §9 |
| Doctrine alignment | ✓ | "Understanding must precede action" — public presence in research districts is Ghost anchoring where understanding is produced; Portrait +1 submitter | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | PublicAct / FactionSpecific (Ghost) | Art 04 §6.2 |
| Taxonomy fit | ✓ | Territory \| Add \| PresenceToken — places Ghost presence chips in target district | Art 04b §4 |
| Balance | ✓ | 1 Findings + PA slot → +2 chips; restricted to 4 districts, public/React-able, adjacency required | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — chips placed on board are permanent board state (not a Permanent card) | Art 04 §5 P19 |
| Persistence | ✓ | Immediate — card fully resolved at Beat 4; chips remain per normal board rules | Art 04 §6 |
| Trigger validity | ✓ | trigger = None | — |
| Portrait validity | ✓ | Ghost +1 submitter-bounded | Art 04 §6.2 |
| Supported by zones | ✓ | Findings districts (University Perimeter, Data Exchange, Research Institute, Chorus Research) — all valid board zones | Art 01 §6–§7 |
| Supported by components | ✓ | PresenceToken (Art 02 §6); Findings × 1 (Art 02 §8); max 6 chips/faction/district enforced at game.add() (GR 8.1) | Art 02 §6, §8 |
| Supported by game procedure | ✓ | Beat 4 PA resolution; game.add() for presence chips; GR 8.1 chip cap | Art 03 §9.4 |
| Data schema validation | ✓ | All §6.1 fields present | Art 04 §6.1–§6.3 |
| Card narrative | ✓ | Story block above | Art 04 §5 P26 |
| Outcome determinacy | ✓ | success = exactly one outcome; successcrit = additive delta; fail = None; failcrit = additive delta | Art 04 §5 P27 |
| Resource cost positioning | Is this card's cost mono-resource (acting faction's own native resource only) or cross-faction-resource (two or more distinct native resources)? Confirm power level matches: mono-resource = floor-power; cross-faction-resource = ceiling-power. Flag if mono-resource and high-power, or cross-resource and underpowered. If cost generates non-native resources as an effect, flag — requires doctrine justification. *(P28)* | Art 00a §9.2 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status |  | | |

```python
GHO.PA.5 = Card(
    id      = "GHO.PA.5",  version="v1.0",
    name    = "Agency Recruitment Fair",
    tagline = "The agency operates in the open. The interested are watching.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Ghost,

    layer   = Territory,  function = Add,  subject = PresenceToken,

    beat            = 4,
    resolution      = d100,
    threshold       = 50,
    ring_mod        = {Ring3: +10, Ring1: -15},
    doctrine_mod    = None,
    trigger         = None,
    resolution_type = "Transactional",
    outcome_type    = Unilateral,
    persistence     = Immediate,
    persistence_condition = None,
    persistence_effect    = None,

    target_district = district.any(resource_type=Findings),
    target_faction  = None,
    target_object   = None,
    target_taxonomy = None,

    affinity    = None,
    restriction = district.resource_type == Findings and faction(Ghost).presence(district.adjacent_to(target_district)) > 0,
    cost        = resource.faction(Ghost).findings * 1,
    boost       = None,

    success     = game.add(PresenceToken, to=target_district, count=2),
    successcrit = faction(Ghost).standing.add(1),
    fail        = None,
    failcrit    = faction(Ghost).standing.sub(1),

    on_accept  = None,
    on_decline = None,

    portrait   = {Ghost: PortraitEntry(submitter=+1)},

    narrative    = None,  # pending D-04-08
    perspectives = None,  # pending D-04-08
    design_note  = "Ghost's only territory PA. Adds 2 presence chips in a Findings-generating district (University Perimeter, Data Exchange, Research Institute, Chorus Research — 4 districts). PA slot + 1 Findings cost justifies +2 output over STD.CA.3 Campaign's covert +1; public declaration means opponents see the target at Phase B and can React. Ring modifier: easier in Baryo (University Perimeter, familiar academic ground), harder in Core (Chorus Research, contested institutional space). Successcrit +1 PS: a well-attended fair is a public credibility event. Failcrit −1 PS: low turnout is a public embarrassment. Ghost adjacency applies at Beat 0. card_id = GHO.PA.5.",
    arbiter_note = "Restriction check at Beat 0: confirm target district resource_type = Findings AND Ghost has presence in a district adjacent to target. On success: place 2 Ghost presence chips in target district (enforce GR 8.1 max 6). On successcrit: additionally move Ghost's PS marker +1. On failcrit: move Ghost's PS marker −1. Cost (1 Findings) submitted to Reservoir regardless of outcome.",
)
```

---


---


---

### GHO.MOD.1 — SLEEPER ANALYST

#### Design Rationale
Ghost's counter-attribution React. When any faction places a PA with an Intel token in the Faction Resolution Grid at Art 03 §9.2.0, Ghost may announce React and declare the faction they believe is named on that token. ARBITER checks the token's faction field. If Ghost's declaration matches: the Intel token is removed, the PA is cancelled, all resource tokens on the PA drain to the Reservoir (no refund), and Ghost gains +1 PS. If Ghost is wrong: card consumed, no effect, PA proceeds.

The intelligence test is genuine: because Target Profiles are placed face-down at Art 03 §9.2.0 (revealing at Art 03 §9.4.3.1.1), and Intel token content is always ARBITER-private, Ghost cannot guess from publicly visible information. Prior intelligence work is required — SIGINT taps, Source Substitution plant mode, or other intelligence that revealed the token's faction field. The chain play is: plant or observe the token → hold React → fire when the attribution PA is declared.

Ghost's portrait −2 on STD.PA.5 documents that public attribution violates Ghost's doctrine across all factions. Sleeper Analyst makes that doctrine actionable: Ghost can mechanically suppress any attribution they have intelligence on. Works against corrupted tokens (planted by Ghost via Source Substitution) and legitimate ones alike — Ghost believes no covert attribution belongs on the public record.

**S138 format migration + re-verification:** this card (S110-vintage) predates the current 4-block review format (structure_pass=0) — converted here, not just reformatted. Re-checking the existing ✓ verdicts (verification-audit mandate, not rubber-stamp) surfaced two real problems the S110-era review didn't have vocabulary to catch: `resolution = Prediction` and `resolution_type = "Conditional"` are not valid enum values (confirmed vocabulary is `d100 | Automatic` and `"Probabilistic" | "Transactional"` respectively — verified directly against Part1_Core.md §6.3) — logged as `schema_cleanup_log.md` item 12. The `trigger` field's method-call syntax (`faction(opponent).places(...)`) also predates confirmed §6.3 TriggerExpr forms entirely — item 13. Both flagged, not fixed; the underlying mechanic (Ghost declares a guess, ARBITER checks it against private data, no dice) most likely resolves to `resolution=Automatic` once corrected, but that's a content call for a future pass, not made here.

#### Card Story
A faction places a public act backed by an Intel token, confident the attribution is buried. Ghost already knows whose name is on it — and says so, out loud, before the table ever finds out. The attribution ends there; so does the act.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Counter-attribution at PA placement — Ghost doctrine: operational anonymity across the full table. Re-verified, holds up. | Art 00 §7 |
| Voice fit | ⚠ | Perspectives TBD — deferred to modifier card voice pass (D-04-08); status of D-04-08 itself not re-checked this pass. | Art 00 §9 |
| Doctrine alignment | ✓ | Ghost +1 portrait: publicly demonstrating intelligence superiority while suppressing attribution is Ghost doctrine at peak visibility. Re-verified. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/FactionSpecific (Ghost) — trigger is a publicly visible board-state change. Re-verified. | Art 04 §6.1, §6.2; Art 03 §18 |
| Taxonomy fit | ✓ | Information/Remove/IntelToken (04-n175, S137) — re-verified against the matrix directly this pass: IntelToken is a dual-aspect component (count=Economy, content=Information per Construction Logic rule 2); Information×Remove is valid. Holds up. | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n175 |
| Balance | ✓ | No activation cost, card consumed on fire (success or misfire), requires genuine prior intelligence to use reliably. Re-verified. | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — PA cancellation and PS shift resolve at trigger. | Art 04 §5 P19 |
| Persistence | ⚠ | Downgraded on re-verification: the S110 note reasoned correctly in prose ("Immediate, no lingering marker") but the `persistence` field itself is still absent from the spec — same open schema question as the rest of the corpus (`schema_cleanup_log.md` item 2/D), not a card-specific issue. | Art 04 §6.2 |
| Trigger validity | ⚠ | Downgraded on re-verification: the trigger fires on a genuinely public board event, but its syntax predates confirmed §6.3 TriggerExpr forms entirely (item 13) — not the same as the Directorate set's `faction=Any` ambiguity, this is an unreconciled legacy construction. | Art 04 §6.3; schema_cleanup_log.md item 13 |
| Portrait validity | ✓ | `{Ghost: submitter=+1}` — submitter-bounded, correctly structured. Re-verified. | Art 04 §6.2 |
| Supported by zones | ✓ | No district reference — correct, this isn't a territory effect. | Art 01 §6–§7 |
| Supported by components | ✓ | Intel Token (on the placed PA) and PS shift both reuse existing components. | Art 02 §6, §11 |
| Supported by game procedure | ✓ | React timing at Art 03 §9.2.0, Target Profile face-down mechanism, Ghost Source Substitution as the intelligence-generation chain — all pre-existing procedure, no new ARBITER behavior. | Art 03 §18; Art 03 §9.2.0 |
| Data schema validation | ⚠ | New finding, not the old "pending 04-n70" note (that reference is stale — superseded by the concrete issues below): `resolution=Prediction` and `resolution_type="Conditional"` are invalid enum values (item 12); scaffolding fields added this session (ring_constraint/ring_origin/value_rating/boost/ps_framing, 04-n177). | Art 04 §6.1–§6.3; schema_cleanup_log.md item 12 |
| Card narrative | ⚠ | `narrative` field still empty; Card Story above is new this pass. | Art 04 §5 P26 |
| Outcome determinacy | ⚠ | Genuine two-branch outcome (declaration matches / doesn't), but modeled via the invalid `Prediction` resolution value rather than a confirmed enum — can't fully assess determinacy until item 12 resolves. | Art 04 §5 P27 |
| Resource cost positioning | ✓ (N/A) | `cost=None` — reasonable; the real cost is the intelligence-gathering prerequisite (Source Substitution/SIGINT chain), and misfire risk (card consumed on a wrong guess) already balances free activation. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ⚠ | Depends on how often PAs are placed with Intel tokens attached — a fairly specific combined event; best-effort, not independently verifiable here. |  |
| Firing window (ModReactCard) | ✓ | No other Ghost card shares this exact trigger (PA + Intel Token at placement). |  |
| Automatic vs. d100 (ModReactCard) | ⚠ | Directly tied to item 12 — this reads as a deterministic ARBITER check (no dice), which argues for `Automatic`, but the card as specced uses neither valid enum value. Can't close until resolved. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus: is a 2nd copy meaningful, or does the first copy's misfire consume the only useful attempt regardless of copies held? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ (N/A) | `ring_constraint=None` (added this session, 04-n177) — correct; not a district/ring-scoped effect. |  |

**Outstanding Issues (carried, pre-S138):**
- Card name pending voice pass (D-04-08); Card ID pending 04-n1 numbering pass — both unresolved by this content-review pass, out of scope here.

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

```python
GHO.MOD.1 = Card(
    id      = "GHO.MOD.1",  card_id = "GHO.MOD.1",  version = "v1.0",
    name    = "Sleeper Analyst",
    tagline = "Name the faction on the Intel token. If correct: the attribution ends here.",
    type    = ModReactCard,  faction = Ghost,
    layer   = Information,  function = Remove,  subject = IntelToken,  # assigned S137 (04-n175) — corrects the stale "§11.1 excluded" claim in the checklist above; ModReactCard isn't exempt (S133 correction)

    trigger = faction(opponent).places(PA, with=IntelToken(any), at=Art 03 §9.2.0),  # ⚠ legacy syntax, predates confirmed §6.3 TriggerExpr vocabulary — flagged, not fixed (schema_cleanup_log.md item 13)
    beat    = None,  # React — fires at Art 03 §9.2.0, not in initiative
    ring_constraint = None,  # scaffolding only — added S138 (04-n177)
    ring_origin     = None,  # scaffolding only — added S138 (04-n177)
    value_rating    = None,  # scaffolding only — added S138 (04-n177)
    resolution = Prediction,  # ⚠ NOT a valid Resolution enum value (d100 | Automatic only) — flagged, not fixed (schema_cleanup_log.md item 12)
    threshold  = None,
    ring_mod   = None,  doctrine_mod = None,  resolution_type = "Conditional",  # ⚠ NOT a valid resolution_type value (Probabilistic | Transactional only) — same flag as above

    target_district = None,
    target_faction  = None,
    target_object   = IntelToken(on=target_PA),
    target_taxonomy = None,
    affinity    = None,
    restriction = None,
    cost        = None,  # card consumed on fire (success or misfire)
    boost       = None,  # scaffolding only — added S138 (04-n177)

    success = (
        arbiter.remove(IntelToken, from=target_PA),
        arbiter.cancel(target_PA),   # flip face-down; drain all resource tokens to Reservoir
        faction(Ghost).standing.add(1),
    ),
    successcrit = None,
    fail        = None,   # card consumed; no board effect; PA proceeds normally
    failcrit    = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Ghost: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolding only — added S138 (04-n177)

    narrative    = None,  # pending 04-n79
    perspectives = None,  # pending D-04-08

    design_note  = "Counter-attribution React payoff for Ghost's intelligence chain. Fires when any faction places a PA with Intel token at Art 02 §9.2.0. Ghost announces React and declares the faction they believe is on the token. ARBITER checks (Prediction resolution). Match → token removed, PA cancelled (resources drained to Reservoir, no refund), Ghost +1 PS. No match → card consumed, PA proceeds. Intelligence-gated: Target Profile face-down at Art 03 §9.2.0 means Ghost cannot derive the target from visible information — requires prior SIGINT or Source Substitution plant mode. Works against corrupted and legitimate tokens alike — Ghost doctrine: no attribution belongs on the public record. card_id = GHO.MOD.1.",
    arbiter_note = "React at Art 03 §9.2.0 when opponent places any PA with an Intel token. Ghost announces React; states the faction they believe is named on the token's faction field. Pause Art 03 §9.2.0 declaration sequence. Check token faction field (do not reveal to table). If Ghost's declared faction matches token: React succeeds — remove token; flip PA face-down (cancelled); drain all resource tokens from PA card to Reservoir; Ghost +1 PS; resume Art 03 §9.2.0. If no match: React misfires — consume Sleeper Analyst card; no board effect; resume Art 03 §9.2.0; placed PA proceeds normally.",
)
```

---

### GHO.MOD.2 — PERIMETER SENSORS

#### Design Rationale
First of a three-card family (GHO.MOD.2/3/4) delivering §5a's "passive Intel generation near Ghost presence" — generic variant, faction-targeted variants follow. Same self-fire question as the Directorate set's item 5: `faction=Any` in the trigger includes Ghost's own presence placements, so Ghost placing a chip in a district it already holds would generate Intel on itself. Likely harmless (self-Intel isn't exploitable the way DIR.MOD.9's self-sanction would be) but flagged for consistency with the established pattern, not silently assumed fine. `district=where(faction(Ghost).presence > 0)` is the second confirmed instance of the unconfirmed `where(...)` trigger-parameter form (schema_cleanup_log.md item 9, first seen on DIR.MOD.8).

#### Card Story
Someone moves a piece onto ground Ghost already quietly holds. Nothing dramatic happens — no confrontation, no announcement. But the sensors were already there, and now Ghost knows exactly who just arrived.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Passive intelligence generation from proximity is a clean, low-key expression of Ghost's "understanding without acting" doctrine. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1; passive observation is core Ghost doctrine. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Ghost, real taxonomy (Information/Add/IntelToken, 04-n175), matches STD.MOD.101's shape. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | IntelToken's dual-aspect content-half is Information; matrix confirms Information×Add valid. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Free Intel generation gated only by Ghost holding presence somewhere active — plausible as a low-key passive engine, final read pending the same whole-set cost/value_rating decision (04-n178) as the Directorate set. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus (`schema_cleanup_log.md` item 2/D). | Art 04 §6.2 |
| Trigger validity | ⚠ | Base event (`presence_chip.placed`) is confirmed vocabulary, but the `district=where(...)` filter isn't a confirmed §6.3 parameter form — 2nd instance of item 9. Also carries the same `faction=Any` self-fire question as item 5/11 (Ghost could trigger this on its own placement). | Art 04 §6.3; schema_cleanup_log.md items 9, 5 |
| Portrait validity | ✓ | `{Ghost: submitter=+1}` — submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district` — correct. | Art 01 §6–7 |
| Supported by components | ✓ | Intel Token delivery reuses the standard mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Reuses existing chip-placement event and Intel Token delivery; no new ARBITER procedure. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolding to be added consistent with 04-n177 (this card already has ring_constraint/ring_origin/value_rating declared — only `ps_framing`/`boost`/`resolution_type` need adding). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set Floor Act/value_rating gate as the Directorate cards. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Fires whenever any faction places presence near existing Ghost presence — moderate-to-common depending on board spread. |  |
| Firing window (ModReactCard) | ⚠ | GHO.MOD.3/4 (faction-targeted variants of this same family) likely share overlapping trigger space — same family-overlap flag as the Directorate enforcement family. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat passive generation, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus: 2 copies → 2 Intel tokens per qualifying placement? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; gated by Ghost's own presence, not ring. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. Delivers §5a "passive generation: Intel tokens from game events near Ghost presence" as a ModReactCard. Output of 04-n143. Generic variant (faction=Any). Faction-targeted variants: GHO.MOD.3 (Directorate), GHO.MOD.4 (Network). S138: full content-review pass — self-fire question flagged (same category as Directorate item 5), `where(...)` trigger parameter confirmed as a 2nd instance (item 9), remaining flags are the standard schema/cost/stack gaps. Design Pass ✓, Issues Resolved not yet.*

```python
GHO.MOD.2 = Card(
    id      = "GHO.MOD.2",  card_id = "GHO.MOD.2",  version = "v0.1",
    name    = "Perimeter Sensors",
    tagline = "Faction activity near Ghost presence generates automatic intelligence.",
    type    = ModReactCard,  faction = Ghost,
    layer   = Information,  function = Add,  subject = IntelToken,  # assigned S137 (04-n175) — arbiter.deliver(...IntelToken...), matches STD.MOD.101

    trigger         = presence_chip.placed(faction=Any, district=where(faction(Ghost).presence > 0)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    value_rating    = None,   # TBD

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Ghost).presence > 0,  # Ghost must be present in triggered district
    cost            = None,  # card consumed on fire
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.deliver(faction(Ghost), IntelToken(faction=trigger.faction)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Ghost: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,  # pending
    perspectives = None,  # pending
    design_note  = "Passive Intel generation from nearby faction activity. Trigger: any faction places presence in a Ghost-present district (publicly observable). Ghost receives 1 Intel token keyed to the placing faction. Intelligence-minimal design: Ghost learns who is expanding near its positions without taking any action. Output of 04-n143.",
    arbiter_note = None,  # TBD
)
```

---

### GHO.MOD.3 — INSTITUTIONAL TRACE

#### Design Rationale
Second card of the GHO.MOD.2/3/4 family — narrowed to Directorate specifically, no self-fire ambiguity (Ghost ≠ Directorate). Third confirmed instance of the unconfirmed `where(...)` trigger-parameter form (`schema_cleanup_log.md` item 9).

#### Card Story
Directorate expands into ground Ghost already quietly watches. The sensors don't care about the politics — they log it, and Ghost gets a name attached to the movement.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Faction-targeted passive intelligence; design_note frames Directorate as Ghost's doctrinal suppressor — grounded narrowing, same reasoning pattern as DIR.MOD.2's Syndicate narrowing. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1 — correctly expresses doctrine. | Art 04 §6.5 |
| Card type fit | ✓ | Same shape as GHO.MOD.2. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Information×Add cell as GHO.MOD.2. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Narrower than GHO.MOD.2 (Directorate-only), so lower frequency — plausible; final read pending 04-n178. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | `presence_chip.placed(faction=Directorate, ...)` — explicitly scoped, no self-fire ambiguity. But `district=where(...)` is the 3rd confirmed instance of the unconfirmed parameter form (item 9). | Art 04 §6.3; schema_cleanup_log.md item 9 |
| Portrait validity | ✓ | Submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same as GHO.MOD.2. | Art 01 §6–7 |
| Supported by components | ✓ | Same as GHO.MOD.2. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same as GHO.MOD.2. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (`ps_framing`/`boost`/`resolution_type` added). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | `cost=None` — same whole-set gate as GHO.MOD.2. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Directorate-only scope keeps frequency lower than GHO.MOD.2's generic trigger. |  |
| Firing window (ModReactCard) | ⚠ | Same family-overlap flag as GHO.MOD.2 — GHO.MOD.2/3/4 share overlapping trigger space if Ghost holds the full family. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same as GHO.MOD.2. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; gated by faction identity, not ring. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. Faction-targeted variant of GHO.MOD.2. Trigger narrowed to Directorate presence placement. Directorate expansion near Ghost positions is the highest-value intelligence signal — institutional authority is Ghost's primary constraint. S138: full content-review pass — 3rd confirmed instance of the unconfirmed `where(...)` trigger form (item 9); remaining flags are the standard schema/cost/stack/family-overlap gaps. Design Pass ✓, Issues Resolved not yet.*

```python
GHO.MOD.3 = Card(
    id      = "GHO.MOD.3",  card_id = "GHO.MOD.3",  version = "v0.1",
    name    = "Institutional Trace",
    tagline = "Directorate expansion near Ghost presence generates targeted intelligence.",
    type    = ModReactCard,  faction = Ghost,
    layer   = Information,  function = Add,  subject = IntelToken,  # assigned S137 (04-n175), same shape as GHO.MOD.2

    trigger         = presence_chip.placed(faction=Directorate, district=where(faction(Ghost).presence > 0)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = Directorate,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Ghost).presence > 0,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.deliver(faction(Ghost), IntelToken(faction=Directorate)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Ghost: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Directorate-targeted variant of GHO.MOD.2 (Perimeter Sensors). Same trigger/effect, faction-narrowed. Directorate expansion near Ghost positions is a high-priority intelligence signal — Directorate is Ghost's doctrinal suppressor. Narrower window than generic variant; more reliable in Directorate-heavy games.",
    arbiter_note = None,
)
```

---

### GHO.MOD.4 — SIGNAL BLEED

#### Design Rationale
Third card of the GHO.MOD.2/3/4 family — narrowed to Network, no self-fire ambiguity. 4th confirmed instance of the unconfirmed `where(...)` trigger-parameter form (`schema_cleanup_log.md` item 9).

#### Card Story
Network's broadcast infrastructure creeps into ground Ghost already watches. The signal bleed itself is the tell — Ghost logs the expansion as an exposure risk to its own covert footing in that district.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Network's broadcast expansion is a natural, distinct intelligence trigger from Directorate's institutional one — design_note frames it correctly as exposure risk rather than mere activity tracking. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | Portrait submitter=+1 — correctly expresses doctrine. | Art 04 §6.5 |
| Card type fit | ✓ | Same shape as GHO.MOD.2/3. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Same verified Information×Add cell. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Same as GHO.MOD.3 — narrower than the generic variant, final read pending 04-n178. | Art 02 §6–7; Art 04 §6.5 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | Explicitly Network-scoped, no self-fire ambiguity. 4th confirmed instance of the unconfirmed `where(...)` form (item 9). | Art 04 §6.3; schema_cleanup_log.md item 9 |
| Portrait validity | ✓ | Submitter-bounded, correctly structured. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | Same as GHO.MOD.2/3. | Art 01 §6–7 |
| Supported by components | ✓ | Same as GHO.MOD.2/3. | Art 02 §6–8 |
| Supported by game procedure | ✓ | Same as GHO.MOD.2/3. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session. | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ (N/A pending 04-n178) | Same whole-set gate as the rest of the family. | Art 00a §9.2; PM05 04-n178 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Network-only scope, moderate frequency depending on Network's board presence. |  |
| Firing window (ModReactCard) | ⚠ | Same family-overlap flag as GHO.MOD.2/3. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Same as GHO.MOD.2/3. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*S128. Faction-targeted variant of GHO.MOD.2. Trigger narrowed to Network presence placement. Network broadcast reach expanding into Ghost-present districts is an operational exposure risk. S138: full content-review pass — 4th confirmed instance of the `where(...)` trigger form (item 9); remaining flags are the standard schema/cost/stack/family-overlap gaps. Design Pass ✓, Issues Resolved not yet.*

```python
GHO.MOD.4 = Card(
    id      = "GHO.MOD.4",  card_id = "GHO.MOD.4",  version = "v0.1",
    name    = "Signal Bleed",
    tagline = "Network expansion near Ghost presence generates exposure intelligence.",
    type    = ModReactCard,  faction = Ghost,
    layer   = Information,  function = Add,  subject = IntelToken,  # assigned S137 (04-n175), same shape as GHO.MOD.2

    trigger         = presence_chip.placed(faction=Network, district=where(faction(Ghost).presence > 0)),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = Network,
    target_object   = None,
    affinity        = None,
    restriction     = faction(Ghost).presence > 0,
    cost            = None,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.deliver(faction(Ghost), IntelToken(faction=Network)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Ghost: PortraitEntry(submitter=+1)},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Network-targeted variant of GHO.MOD.2 (Perimeter Sensors). Network presence placement near Ghost positions generates Network-keyed Intel — Ghost tracks the broadcast infrastructure expanding into shared territory. Network expansion = exposure risk for Ghost covert ops in those districts.",
    arbiter_note = None,
)
```

---

### GHO.MOD.5 — FALSE FLAG

#### Design Rationale
Ghost's Flip-doctrine payoff: reacts to *any* faction's positive PS shift and inverts it into a net loss, funded by spending the target's... no, Ghost's own resources (Findings + Exposure). Real finding this pass: the trigger uses `public_standing.shifted(faction=Any, direction=Positive)` — a retired term. PM05 04-n144 (closed S130) already normalized this exact form to `standing_marker.increased/decreased(faction=X)` for its known instances (SYN.MOD.4/5); GHO.MOD.5 uses the identical retired syntax and was missed by that sweep. Confirmed via grep (S138) that this is the *only* remaining instance across all 8 Art 04 Part files — logged to `schema_cleanup_log.md` item 14, not fixed here (content decision belongs to a future pass). Also worth noting: the cost spends Exposure, which isn't Ghost's native resource (Findings is) — not illegal (cross-resource costs are an established pattern elsewhere in the game), but worth flagging whether Ghost realistically has Exposure on hand without a prior conversion/trade step.

#### Card Story
A rival claims a public win — the kind that moves their standing up in front of the whole table. Ghost already has the counter-narrative ready. By the time anyone checks the record again, the "victory" reads as the opposite.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Reversing a rival's public narrative gain is a clean expression of Ghost's information-warfare doctrine — distinct from the passive-intel family (GHO.MOD.2–4). | Art 00 §7 |
| Voice fit | ✓ | Tagline ("let them claim the victory, then rewrite the headline") lands the doctrine precisely. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — reasonable; Ghost doctrine favors invisibility, an empty portrait for a covert narrative-manipulation play is consistent, not a gap like DIR.MOD.6's. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Ghost, real taxonomy (Standing/Shift/StandingMarker, 04-n175/04-n173 precedent). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Standing×Shift is the correct cell per the matrix (Standing×Add/Remove is invalid, subsumed by Shift — 04-n173); `subject=StandingMarker` matches the S126 correction, not the retired `PublicStanding`. | Art 04b §4; ref_taxonomy.md §5.1; PM05 04-n173 |
| Balance | ⚠ | Doubles the trigger amount to invert a gain into an equal-magnitude loss — mechanically sound (verified the math: net effect from pre-trigger baseline is −X on a +X gain), but real cost (Findings+Exposure) and value_rating aren't set; final read pending 04-n178. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | `public_standing.shifted(direction=Positive)` is a retired term (schema_cleanup_log.md item 14) — confirmed via grep as the sole remaining instance across the whole card system. Flagged, not fixed. | Art 04 §6.3; schema_cleanup_log.md item 14 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; this isn't a territory effect. | Art 01 §6–7 |
| Supported by components | ✓ | PS/Standing marker shift reuses the standard mechanism. | Art 02 §6–8 |
| Supported by game procedure | ✓ | React timing after the triggering PS shift resolves — no new ARBITER behavior. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch, deterministic doubling formula. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Real cost specified (Findings+Exposure) — but Exposure isn't Ghost's native resource; worth checking whether Ghost realistically holds it without a prior conversion step (cross-resource cost design, not illegal per se). | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Any faction's positive PS shift is a recurring event; gated by Ghost having the resources on hand to fire. |  |
| Firing window (ModReactCard) | ✓ | No other Ghost card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Deterministic inversion formula, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus: 2 copies → quadruple the inversion? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*React on positive PS shift. The "Flip" point-disruption payoff. Reverse the opponent's public narrative. S138: full content-review pass — confirmed retired trigger term (`public_standing.shifted`, item 14, sole remaining instance); cross-resource cost (Exposure, not Ghost-native) flagged for Resource cost positioning. Design Pass ✓, Issues Resolved not yet.*

```python
GHO.MOD.5 = Card(
    id      = "GHO.MOD.5",  card_id = "GHO.MOD.5",  version = "v0.1",
    name    = "False Flag",
    tagline = "Let them claim the victory, then rewrite the headline.",
    type    = ModReactCard,  faction = Ghost,
    layer   = Standing,  function = Shift,  subject = StandingMarker,  # assigned S137 (04-n175) — arbiter.shift(public_standing,...), matches the S126/04-n173 StandingMarker precedent

    trigger         = public_standing.shifted(faction=Any, direction=Positive),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Ghost).findings * 1 + resource.faction(Ghost).exposure * 1,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.shift(public_standing, faction=trigger.faction, amount=-(trigger.amount * 2)),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Late-game Flipped intel sink. Ghost spends the target's native resource to invert their public victory into a disaster. Since Reacts occur after the state change (the positive shift), this effectively applies a negative shift equal to double the trigger amount to achieve the inversion Cost reasoning: Exposure is expended to actively seed the manufactured narrative into the public consciousness.",
    arbiter_note = None,
)
```

---

### GHO.MOD.6 — SUPPLY CHAIN TAP

#### Design Rationale
Parasitic economy React: Ghost pays 1 unit of the triggering faction's native resource type to mirror-copy that faction's entire Upkeep resource draw. Two real findings on this pass: (1) `trigger = resource.drawn_from_reservoir(faction=Any)` is a known, already-documented gap — `design_reference_card_system.md`'s "Still pending" note calls this out by name as "not in TriggerExpr schema — needs component classification," so this isn't a new discovery, just confirmed still open. (2) `faction=Any` carries the same self-fire question as items 5/11/9(GHO.MOD.2) — if Ghost's own Upkeep draw triggers this, Ghost would pay 1 Findings to "copy" a delivery it's already receiving, a costed no-op. Also worth flagging: the cost is denominated in the *triggering faction's* native resource type, which Ghost may not hold without a prior conversion — same cross-resource question as GHO.MOD.5.

#### Card Story
An opponent's Upkeep resources land in their reserve. Ghost's tap on their supply line means the exact same shipment quietly lands in Ghost's reserve too — paid for, not stolen.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Parasitic mirroring of a rival's economy fits Ghost's "extract value without confrontation" doctrine. | Art 00 §7 |
| Voice fit | ✓ | Tagline ("their infrastructure is our logistics") lands the doctrine. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — consistent with Ghost's invisibility preference for covert economic plays, same reasoning as GHO.MOD.5. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Ghost, real taxonomy (Economy/Copy/NativeResource, 04-n175) — correctly Copy, not Add, per the design_note's own "mirrored duplicate, not a transfer" framing. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Economy×Copy is valid per the matrix; Copy is the correct Function since this duplicates an effect chain rather than moving or creating new supply. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Full mirrored draw for a 1-resource cost is potentially strong depending on the triggering faction's Upkeep yield — final read needs 04-n178 plus resolution of the cross-resource-holding question below. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | `resource.drawn_from_reservoir(faction=Any)` is a confirmed, already-documented gap (design_reference_card_system.md "Still pending" list) — not in the TriggerExpr schema at all. Also carries the same `faction=Any` self-fire question as items 5/9/11. | Art 04 §6.3; schema_cleanup_log.md items 5, 9 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=None` — correct; not a territory effect. | Art 01 §6–7 |
| Supported by components | ✓ | Resource delivery reuses the standard mechanism. | Art 02 §6–8 |
| Supported by game procedure | ⚠ | Depends on Upkeep's resource-collection step being a detectable, reactable event — plausible given Upkeep is a defined phase, but the exact hook point isn't confirmed since the trigger term itself is unconfirmed (see Trigger validity). | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Cost is denominated in the *triggering faction's* native resource — Ghost may not hold that resource type without a prior conversion/trade, same open question as GHO.MOD.5's Exposure cost. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ⚠ | Every faction draws resources at Upkeep every Quarter — potentially very high frequency if the trigger term is confirmed broadly. Ties directly into the Balance flag. |  |
| Firing window (ModReactCard) | ✓ | No other Ghost card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Flat mirrored copy, no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus: 2 copies → 2x the mirrored draw? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; not ring-scoped. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*React on resource generation. Precision economic disruption via mirrored draw. S138: full content-review pass — confirmed `resource.drawn_from_reservoir` as an already-documented schema gap (not newly found), flagged the `faction=Any` self-fire question and the cross-resource cost-holding question (same shape as GHO.MOD.5). Design Pass ✓, Issues Resolved not yet.*

```python
GHO.MOD.6 = Card(
    id      = "GHO.MOD.6",  card_id = "GHO.MOD.6",  version = "v0.1",
    name    = "Supply Chain Tap",
    tagline = "Their infrastructure is our logistics.",
    type    = ModReactCard,  faction = Ghost,
    layer   = Economy,  function = Copy,  subject = NativeResource,  # assigned S137 (04-n175) — Copy, not Add: design_note explicitly calls this a "mirrored" duplicate of the opponent's draw, not a transfer from them

    trigger         = resource.drawn_from_reservoir(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = None,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = Resource(faction(trigger.faction).native, 1),
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.deliver(faction(Ghost), trigger.resources),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Ghost pays 1 cross-faction resource to copy the entire resource draw of an opponent's Upkeep phase. Pure mirrored parasitic economy.",
    arbiter_note = None,
)
```

---

### GHO.MOD.7 — SLEEPER CELL

#### Design Rationale
Ghost's endgame disruption React: swaps 1 opponent chip for 1 Ghost chip in the same district the instant a Dominant marker is placed there, stripping the fresh Dominant status back to Established. Correctly taxonomied as Redirect (Andy's catch, S137) rather than Remove — it's a same-slot allegiance change, not a plain removal. Two real findings: (1) `faction=Any` carries the same self-fire question as items 5/6/9/11 — if Ghost itself achieves Dominant somewhere, this would fire and have Ghost swap its own chip for its own chip, paying the full 3-resource cost for a literal no-op. (2) The cost spans three resource types (Findings, Capacity, Capital) — only Findings is Ghost-native; Capacity and Capital are Guild's and Syndicate's respectively. This is the sharpest instance yet of the cross-resource-holding question raised at GHO.MOD.5/6 — two of the three cost components require Ghost to already hold resources it doesn't natively generate.

#### Card Story
A rival's chip count finally tips them into Dominant — the marker goes down, the table sees it land. Before anyone reacts, a presence nobody knew was there activates, and the marker's claim evaporates as fast as it arrived.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Endgame power-spike disruption via a dormant asset activating is a strong, doctrinally coherent Ghost beat — "total control is just a convenient illusion" lands the point precisely. | Art 00 §7 |
| Voice fit | ✓ | Tagline is one of the strongest in the set. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — consistent with Ghost's invisibility preference. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Ghost, real taxonomy (Territory/Redirect/PresenceToken, 04-n175 — Andy's specific correction from an initially-assumed Remove). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory×Redirect is valid per the matrix; Redirect is correct since ownership changes on the same chip-slot, matching the verb's definition ("changes ownership, destination, or allegiance"). | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Powerful, precisely-timed disruption of a Dominant achievement — high 3-resource cost plausibly balances it, but see the cross-resource-holding flag below; if Ghost can't reliably afford two foreign resource types, the effective cost (and thus balance) is unclear. Final read pending 04-n178. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | `dominant_marker.placed(faction=X)` is confirmed vocabulary, but `faction=Any` carries the same self-fire question as items 5/6/11 — sharpest instance yet, since firing against Ghost's own Dominant achievement would cost 3 resources for a literal no-op swap. | Art 04 §6.3; schema_cleanup_log.md item 5 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district` — correct. | Art 01 §6–7 |
| Supported by components | ⚠ | Same deployment-marker-removal edge as the Directorate enforcement family (`schema_cleanup_log.md` item 6) — the removed chip could be a Deployment Marker's temporary presence (GR 8.3a: markers move, never removed). | Art 02 §6–8; GR 8.3a; schema_cleanup_log.md item 6 |
| Supported by game procedure | ✓ | Reuses existing chip removal/placement mechanisms and the Dominant-marker-placement event; no new ARBITER procedure. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch (two sequential mutations, no choose_one). | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Real cost specified but spans 3 resource types, 2 of which (Capacity, Capital) aren't Ghost-native — the sharpest instance of the cross-resource-holding question raised at GHO.MOD.5/6. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ✓ (best-effort) | Dominant-marker placement is inherently rare (endgame-adjacent), matching the design_note's own "massive late-game state change" framing — low frequency by design, not a flaw. |  |
| Firing window (ModReactCard) | ✓ | No other Ghost card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary swap — no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus, though less consequential here given the trigger's inherent rarity. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct; fires wherever a Dominant marker lands. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*React on Dominant marker placement. Point-disruption targeting end-game power spikes. S138: full content-review pass — self-fire question (item 5 family, sharpest instance — full-cost no-op if self-triggered), cross-resource cost-holding question (2 of 3 resource types not Ghost-native), and the deployment-marker removal edge (item 6) all flagged. Design Pass ✓, Issues Resolved not yet.*

```python
GHO.MOD.7 = Card(
    id      = "GHO.MOD.7",  card_id = "GHO.MOD.7",  version = "v0.1",
    name    = "Sleeper Cell",
    tagline = "Total control is just a convenient illusion.",
    type    = ModReactCard,  faction = Ghost,
    layer   = Territory,  function = Redirect,  subject = PresenceToken,  # assigned S137 (04-n175, Andy's catch) — Redirect ("changes ownership, destination, or allegiance"), not Remove: the effect swaps 1 opponent chip for 1 Ghost chip in the same district, a same-slot allegiance change, not a plain removal

    trigger         = dominant_marker.placed(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = resource.faction(Ghost).findings * 1 + resource.faction(Ghost).capacity * 1 + resource.faction(Ghost).capital * 1,
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = list([arbiter.remove(presence_chip, district=target_district, faction=target_faction, count=1), arbiter.place(presence_chip, district=target_district, faction=Ghost, count=1)]),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Reacts to a massive late-game state change. By physically swapping 1 of the target's chips for 1 Ghost chip, Ghost instantly drops the opponent's chip count, stripping the Dominant marker the moment it is placed and forcing them back to Established. Delays the endgame condition Cost reasoning: Requires Capacity to house the cell and Capital to fund their sudden activation, backed by precise intelligence.",
    arbiter_note = None,
)
```

---

### GHO.MOD.8 — LOCAL SYMPATHIZERS

#### Design Rationale
Mid-game counterpart to GHO.MOD.7's endgame disruption: reacts to any faction reaching Established (IL-02) and immediately strips 1 chip, downgrading them back to Present. Same shape as DIR.MOD.1's enforcement family (Territory/Remove/PresenceToken), carrying the same open questions: `faction=Any` self-fire (item 5 family — Ghost achieving Established would trigger this against itself), the deployment-marker-removal edge (item 6), and the cross-resource cost-holding question (cost denominated in the *triggering faction's* native resource, same as GHO.MOD.6/7).

#### Card Story
A faction plants its second foothold in a district and calls it secured. The neighborhood disagrees — quietly, and on someone else's payroll. One chip comes back off the board before the ink on "Established" dries.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Mid-game expansion disruption via unnamed local assets fits Ghost's "influence without visible presence" doctrine, distinct from GHO.MOD.7's endgame-scale disruption. | Art 00 §7 |
| Voice fit | ✓ | Tagline reads correctly. `narrative` field empty — see Card narrative row. | Art 00 §6.7 |
| Doctrine alignment | ✓ | `portrait = {}` — consistent with the rest of Ghost's covert-action cards. | Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Ghost, real taxonomy (Territory/Remove/PresenceToken, 04-n175), matches DIR.MOD.1's shape. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Territory×Remove — same verified matrix cell as the Directorate enforcement family. | Art 04b §4; ref_taxonomy.md §5.1 |
| Balance | ⚠ | Cheaper than GHO.MOD.7 (1 resource vs. 3) but also less severe (Established→Present vs. Dominant→Established) — plausible tiering, final read pending 04-n178. | Art 02 §6–7; Art 04 §6.5; PM05 04-n178 |
| Effect duration | ✓ | Immediate. | Art 04 §5 P19 |
| Persistence | ⚠ (deferred) | Same open schema question as the rest of the corpus. | Art 04 §6.2 |
| Trigger validity | ⚠ | `established_marker.placed(faction=X)` is confirmed vocabulary, but `faction=Any` carries the same self-fire question as items 5/6/7/11. | Art 04 §6.3; schema_cleanup_log.md item 5 |
| Portrait validity | ✓ | Empty `{}` justified per Doctrine alignment row. | Art 04 §6.2 P11 |
| Supported by zones | ✓ | `target_district=trigger.district` — correct. | Art 01 §6–7 |
| Supported by components | ⚠ | Same deployment-marker-removal edge as DIR.MOD.1/2/3 and GHO.MOD.7 (`schema_cleanup_log.md` item 6). | Art 02 §6–8; GR 8.3a; schema_cleanup_log.md item 6 |
| Supported by game procedure | ✓ | Reuses existing chip-removal mechanism and Established-marker-placement event; no new ARBITER procedure. | Art 03; GR 6.1 |
| Data schema validation | ⚠ (deferred) | Scaffolded this session (04-n177). | Art 04 §6.1–§6.3 |
| Card narrative | ⚠ | `narrative` field empty; Card Story above is new this pass. | Art 04 §5 Card Story |
| Outcome determinacy | ✓ | Automatic, single success branch. | Art 04 §5 P27 |
| Resource cost positioning | ⚠ | Same cross-resource-holding question as GHO.MOD.6/7: cost denominated in the triggering faction's native resource, which Ghost may not hold without prior conversion. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ⚠ | Reaching Established is a common mid-game milestone across all factions — likely higher-frequency than GHO.MOD.7's Dominant trigger. Ties into the Balance flag. |  |
| Firing window (ModReactCard) | ✓ | No other Ghost card shares this trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Bounded, binary removal — no execution-quality dimension. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open question as the rest of the corpus. |  |
| Ring constraint (ModReactCard) | ✓ | `ring_constraint=None` — correct. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

*React on Established marker placement. Point-disruption targeting mid-game expansion. S138: full content-review pass — same self-fire (item 5), deployment-marker (item 6), and cross-resource cost-holding flags as the rest of the Ghost ModReactCard set. Design Pass ✓, Issues Resolved not yet.*

```python
GHO.MOD.8 = Card(
    id      = "GHO.MOD.8",  card_id = "GHO.MOD.8",  version = "v0.1",
    name    = "Local Sympathizers",
    tagline = "They thought this neighborhood belonged to them.",
    type    = ModReactCard,  faction = Ghost,
    layer   = Territory,  function = Remove,  subject = PresenceToken,  # assigned S137 (04-n175) — arbiter.remove(presence_chip,...), matches DIR.MOD.1

    trigger         = established_marker.placed(faction=Any),
    beat            = None,
    ring_constraint = None,
    ring_origin     = None,
    value_rating    = None,

    resolution = Automatic,  threshold = None,  resolution_type = "Transactional",  # mechanical per schema; not a design blank
    ring_mod = None,  doctrine_mod = None,

    target_district = trigger.district,
    target_faction  = trigger.faction,
    target_object   = None,
    affinity        = None,
    restriction     = None,
    cost            = Resource(faction(trigger.faction).native, 1),
    boost           = None,  # scaffolding only — real value pending 04-n177 focused session

    success     = arbiter.remove(presence_chip, district=target_district, faction=target_faction, count=1),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {},
    ps_framing   = None,  # scaffolding only — real value pending 04-n177 focused session
    narrative    = None,
    perspectives = None,
    design_note  = "Reacts to a faction reaching IL-02 (Established). Ghost burns 1 cross-faction resource to immediately remove one of their chips, instantly downgrading them back to IL-01. Slows the table's structural expansion.",
    arbiter_note = None,
)
```

---

---

### GHO.MOD.9 — BURN NOTICE
[↑ Modifier & React Cards](#ghost-modifier-and-react-cards)

#### Design Rationale
Ghost's punitive React against factions trying to brute-force a Public Act using Intel Tokens as payment. Fires the moment such a PA is submitted; on success, every Modifier card riding that PA is stripped — not just the submitter's own boosts, but any other faction's cards attached to the same PA. This is a genuinely harsh, full-stack wipe: Ghost's doctrine of operational anonymity extends to punishing anyone who thinks Intel currency buys them a clean filing. Confirmed as intended, not softened (Andy, S140) — bigger swing than most single-card React effects in the corpus, deliberately so. Pre-schema fossil (04-n174): trigger and success re-expressed in current Expr syntax this pass; underlying mechanic unchanged from the S135/S137-era design.

#### Card Story
The token changes hands quietly, the paperwork goes through — and by the time anyone checks, every favor riding on that filing has already gone up in smoke. Ghost doesn't say who tipped them off. They don't have to.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Punitive counter-play against Intel-Token-funded PA submission; fits Ghost's information-as-leverage doctrine. | Art 00 §7 |
| Voice fit | ⚠ | Perspectives TBD — deferred to modifier card voice pass (D-04-08). | Art 00 §9 |
| Doctrine alignment | ✓ | Punishing information misuse (Intel currency spent to force a PA through) is squarely Ghost's anonymity/leverage doctrine. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Ghost — trigger-based, fires on a publicly visible board event (PA submission). | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Submission / Remove / ModifierCard — confirmed registered pairing. | ref_taxonomy.md §5.2 |
| Balance | ✓ | `cost = Findings(1)`, one-time punitive strip triggered by the opponent's own aggressive play. Full-stack-wipe magnitude confirmed intended (Andy, S140), not re-litigated further. | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — modifiers removed at trigger, no lingering effect. | Art 04 §5 P19 |
| Persistence | ⚠ | `persistence` field open corpus-wide question (schema_cleanup_log item 2/D), not card-specific. | Art 04 §6.2 |
| Trigger validity | ⚠ | `public_act.submitted(uses_intel_token=True)` unconfirmed against §6.3 TriggerExpr vocabulary — same open category as the rest of this fossil set. | Art 04 §6.3; PM05 04-n174 |
| Portrait validity | ✓ | `{Ghost: submitter=+1}` — added this pass; fossil carried no portrait entry. | Art 04 §6.2 |
| Supported by zones | ✓ | No district reference — correct, not a territory effect. | Art 01 §6–§7 |
| Supported by components | ✓ | Modifier cards and Intel Token both reuse existing components. | Art 02 §6, §11 |
| Supported by game procedure | ✓ | PA submission at Covert Dispatch/Phase B; standard Ghost React window. | Art 03 §18; Art 03 §9.2.0 |
| Data schema validation | ⚠ | Trigger/success re-expressed from string-literal fossil to Expr syntax this pass (04-n174). `arbiter.remove(...)` has no confirmed MutationExpr vocabulary — same open gap as the rest of the corpus. Scaffolding fields added (ring_constraint/ring_origin/value_rating/boost/ps_framing, 04-n177). | Art 04 §6.1–§6.3; PM05 04-n174 |
| Card narrative | ✓ | Card Story written this pass (was empty). | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic` — deterministic ARBITER check (was an Intel Token used at submission), no dice appropriate. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | `Findings(1)` — light cost for a punitive strip triggered by the opponent's own play, not Ghost's initiative. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ⚠ | Depends on how often PAs are submitted with Intel Token payment — best-effort, not independently verifiable here. |  |
| Firing window (ModReactCard) | ✓ | No other Ghost card shares this exact trigger. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Deterministic condition check, no dice — Automatic is correct. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open corpus-wide question: is a 2nd copy meaningful? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ (N/A) | `ring_constraint=None` — not a district/ring-scoped effect. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

```python
GHO.MOD.9 = Card(
    id      = "GHO.MOD.9",  card_id = "GHO.MOD.9",  version = "v1.2",
    name    = "Burn Notice",
    tagline = "Incinerate an opponent's intelligence assets as they try to use them.",
    type    = ModReactCard,  faction = Ghost,

    layer   = Submission,  function = Remove,  subject = ModifierCard,  # confirmed registered pairing — ref_taxonomy.md §5.2 (Modifier Card: Economy/Submission)

    trigger         = public_act.submitted(uses_intel_token=True),  # unconfirmed against §6.3 TriggerExpr vocabulary — same open category as Overture's trigger and SYN.MOD.11's accord.tabled (04-n174)
    beat            = None,
    ring_constraint = None,  ring_origin = None,  value_rating = None,
    resolution      = Automatic,  threshold = None,  resolution_type = "Transactional",  outcome_type = None,
    ring_mod        = None,  doctrine_mod = None,
    acquisition     = Deck,  generating_card = None,

    target_district = None,
    target_faction  = None,  # not needed — trigger.public_act uniquely identifies the target PA regardless of which faction(s) attached modifiers to it
    target_object   = trigger.public_act,
    affinity        = None,  restriction = None,
    cost            = Findings(1),
    boost           = None,

    success     = arbiter.remove(ModifierCard, attached_to=trigger.public_act),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Ghost: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = None,  perspectives = None,
    design_note  = "Punishes brute-forcing a PA with Intel Tokens by stripping every Modifier card riding it — full-stack wipe, not just the submitter's. Confirmed as intended (Andy, S140): this is a bigger swing than most single-card React effects in the corpus, deliberately so.",
    arbiter_note = "On trigger (a PA is submitted using an Intel Token as payment): confirm Ghost pays Findings(1). Remove every Modifier card currently attached to that PA, regardless of owner.",
)
```

---

### GHO.MOD.10 — DATA WIPE
[↑ Modifier & React Cards](#ghost-modifier-and-react-cards)

#### Design Rationale
Ghost's most disruptive React: forces a target faction to discard their entire hand of unplayed Covert Operation and Public Act cards, clearing their operational runway for the rest of the Quarter (they redraw normally at Debrief). Confirmed as intended, not softened (Andy, S140) — the steepest cost in this fossil set (`Findings(2) + IntelToken(1)`) reflects the swing. Pre-schema fossil (04-n174): trigger and success re-expressed in current Expr syntax this pass; underlying mechanic unchanged.

#### Card Story
No warning, no negotiation — just a hand suddenly empty and a faction scrambling to rebuild a plan that doesn't exist anymore.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Ghost's heaviest disruption React — clears an opponent's operational hand outright. | Art 00 §7 |
| Voice fit | ⚠ | Perspectives TBD — deferred to modifier card voice pass (D-04-08). | Art 00 §9 |
| Doctrine alignment | ✓ | Information warfare against an opponent's operational capacity — Ghost doctrine at its most aggressive. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Ghost — trigger-based, fires on PA submission. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ⚠ | Information / Remove / FactionHand — FactionHand not a registered subject type; same non-gate flag already carried by NET.PA.3 Live Coverage, pending 04b validation. | ref_taxonomy.md §5.2; PM05 04-n174 |
| Balance | ✓ | `cost = Findings(2) + IntelToken(1)` — steepest cost in the fossil set, matching the swing (full hand discard). Confirmed intended (Andy, S140). | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — discard resolves at trigger; target redraws normally at next Debrief. | Art 04 §5 P19 |
| Persistence | ⚠ | `persistence` field open corpus-wide question (schema_cleanup_log item 2/D), not card-specific. | Art 04 §6.2 |
| Trigger validity | ⚠ | `public_act.submitted` unconfirmed against §6.3 TriggerExpr vocabulary. | Art 04 §6.3; PM05 04-n174 |
| Portrait validity | ✓ | `{Ghost: submitter=+1}` — added this pass; fossil carried no portrait entry. | Art 04 §6.2 |
| Supported by zones | ✓ | No district reference — correct, not a territory effect. | Art 01 §6–§7 |
| Supported by components | ✓ | Faction Hand, Findings, Intel Token — existing components. | Art 02 §6, §11 |
| Supported by game procedure | ✓ | PA submission at Covert Dispatch/Phase B; standard Ghost React window; Debrief redraw per standard procedure. | Art 03 §18; Art 03 §9.2.0 |
| Data schema validation | ⚠ | Trigger/success re-expressed from string-literal fossil to Expr syntax this pass (04-n174). `arbiter.discard_hand(...)` has no confirmed MutationExpr vocabulary — same open gap as the rest of the corpus. Scaffolding fields added (04-n177). | Art 04 §6.1–§6.3; PM05 04-n174 |
| Card narrative | ✓ | Card Story written this pass (was empty). | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic` — deterministic, no dice. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | `Findings(2) + IntelToken(1)` — heaviest cost among the fossil set, matching effect magnitude. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ⚠ | Any PA submission qualifies — broad trigger window; best-effort, not independently verifiable here. |  |
| Firing window (ModReactCard) | ✓ | No other Ghost card shares this exact trigger + effect combination. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Deterministic condition check, no dice — Automatic is correct. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open corpus-wide question: is a 2nd copy meaningful? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ (N/A) | `ring_constraint=None` — not a district/ring-scoped effect. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

```python
GHO.MOD.10 = Card(
    id      = "GHO.MOD.10",  card_id = "GHO.MOD.10",  version = "v1.2",
    name    = "Data Wipe",
    tagline = "A devastating cyber-attack that cripples a faction's operational hand.",
    type    = ModReactCard,  faction = Ghost,

    layer   = Information,  function = Remove,  subject = FactionHand,  # FactionHand not a registered subject type — same non-gate flag as NET.PA.3 Live Coverage (04b validation pending)

    trigger         = public_act.submitted,  # unconfirmed against §6.3 TriggerExpr vocabulary (04-n174)
    beat            = None,
    ring_constraint = None,  ring_origin = None,  value_rating = None,
    resolution      = Automatic,  threshold = None,  resolution_type = "Transactional",  outcome_type = None,
    ring_mod        = None,  doctrine_mod = None,
    acquisition     = Deck,  generating_card = None,

    target_district = None,
    target_faction  = faction(trigger.public_act.submitter),
    target_object   = None,
    affinity        = None,  restriction = None,
    cost            = Findings(2) + IntelToken(1),
    boost           = None,

    success     = arbiter.discard_hand(target_faction, card_types=[CovertOperation, PublicAct]),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Ghost: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = None,  perspectives = None,
    design_note  = "Hugely disruptive — clears the target's entire unplayed CA/PA hand; they redraw normally at Debrief. Confirmed as intended (Andy, S140), not softened. Steepest cost in the fossil set (Findings(2) + IntelToken(1)) reflects the swing.",
    arbiter_note = "On trigger (any faction submits a PA): confirm Ghost pays Findings(2) + IntelToken(1) and names the submitting faction as target. Target discards all unplayed Covert Operation and Public Act cards from hand; they redraw normally at next Debrief per standard draw procedure.",
)
```

---

### GHO.MOD.11 — MANUFACTURED EVIDENCE
[↑ Modifier & React Cards](#ghost-modifier-and-react-cards)

#### Design Rationale
A public hijacking: when an opponent places a PA with a face-down Target Profile, Ghost may swap it for one of their own choosing before Beat 4. Because Target Profiles are placed face-down, no one — not even the table — knows what Ghost changed the target to until the Apex Check reveals it. Pre-schema fossil (04-n174): trigger and success re-expressed in current Expr syntax this pass; underlying mechanic, cost, and arbiter procedure unchanged.

#### Card Story
The table watches Ghost trade one sealed envelope for another. Nobody objects — the rules allow it — but nobody knows what's inside the new one either, and won't until the dust settles at Beat 4.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Anonymous hijacking of an opponent's PA targeting — Ghost doctrine of operating unseen inside someone else's action. | Art 00 §7 |
| Voice fit | ⚠ | Perspectives TBD — deferred to modifier card voice pass (D-04-08). | Art 00 §9 |
| Doctrine alignment | ✓ | Corrupting a Target Profile without public disclosure is squarely Ghost's covert-manipulation doctrine. | Art 00 §7; Art 04 §6.5 |
| Card type fit | ✓ | ModReactCard/Ghost — trigger-based, fires on PA placement with a face-down Target Profile. | Art 04 §6.1, §6.2 |
| Taxonomy fit | ✓ | Information / Corrupt / TargetProfile — confirmed Corrupt target. | ref_taxonomy.md §5.2 |
| Balance | ✓ | `cost = Findings(1) + Exposure(1)` — moderate cost, unchanged from fossil. | Art 02 §6–§7 |
| Effect duration | ✓ | Immediate — swap resolves at trigger; corrupted target then resolves normally at Beat 4. | Art 04 §5 P19 |
| Persistence | ⚠ | `persistence` field open corpus-wide question (schema_cleanup_log item 2/D), not card-specific. | Art 04 §6.2 |
| Trigger validity | ⚠ | `public_act.placed_with_target_profile` unconfirmed against §6.3 TriggerExpr vocabulary — shared form with NET.MOD.12 (same open item, both fossils). | Art 04 §6.3; PM05 04-n174 |
| Portrait validity | ✓ | `{Ghost: submitter=+1}` — added this pass; fossil carried no portrait entry. | Art 04 §6.2 |
| Supported by zones | ✓ | No district reference — correct, not a territory effect. | Art 01 §6–§7 |
| Supported by components | ✓ | Target Profile (face-down mechanism) — existing component. | Art 02 §6, §11 |
| Supported by game procedure | ✓ | Reacts at Art 03 §9.2.0; face-down Target Profile mechanism and Beat 4 Apex Check both pre-existing procedure. | Art 03 §9.2.0; Art 03 §14 |
| Data schema validation | ⚠ | Trigger/success re-expressed from string-literal fossil to Expr syntax this pass (04-n174). `arbiter.swap_target_profile(...)` has no confirmed MutationExpr vocabulary — same open gap as the rest of the corpus. Scaffolding fields added (04-n177). | Art 04 §6.1–§6.3; PM05 04-n174 |
| Card narrative | ✓ | Card Story written this pass (was empty). | Art 04 §5 P26 |
| Outcome determinacy | ✓ | `Automatic` — deterministic, no dice. | Art 04 §5 P27 |
| Resource cost positioning | ✓ | `Findings(1) + Exposure(1)` — moderate cost for a covert, undisclosed swap. | Art 00a §9.2 |
| Trigger frequency (ModReactCard) | ⚠ | Depends on how often opponents place PAs with face-down Target Profiles — best-effort, not independently verifiable here. |  |
| Firing window (ModReactCard) | ✓ | Shares its trigger with NET.MOD.12 (Network's Forced Transparency) but the two effects don't overlap in resolution. |  |
| Automatic vs. d100 (ModReactCard) | ✓ | Deterministic condition check, no dice — Automatic is correct. |  |
| Stack behavior (ModReactCard) | ⚠ | Same open corpus-wide question: is a 2nd copy meaningful? Undocumented. |  |
| Ring constraint (ModReactCard) | ✓ (N/A) | `ring_constraint=None` — not a district/ring-scoped effect. |  |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ |  |  |

```python
GHO.MOD.11 = Card(
    id      = "GHO.MOD.11",  card_id = "GHO.MOD.11",  version = "v1.1",
    name    = "Manufactured Evidence",
    tagline = "Hijack a public act before the ink dries.",
    type    = ModReactCard,  faction = Ghost,

    layer   = Information,  function = Corrupt,  subject = TargetProfile,  # confirmed Corrupt target — ref_taxonomy.md §5.2 ("Corrupt targets are strictly: ... Target Profile")

    trigger         = public_act.placed_with_target_profile,  # unconfirmed against §6.3 TriggerExpr vocabulary — shared form with NET.MOD.12 (04-n174)
    beat            = None,
    ring_constraint = None,  ring_origin = None,  value_rating = None,
    resolution      = Automatic,  threshold = None,  resolution_type = "Transactional",  outcome_type = None,
    ring_mod        = None,  doctrine_mod = None,
    acquisition     = Deck,  generating_card = None,

    target_district = None,
    target_faction  = None,  # not declared — the swap is anonymous even to the table until Beat 4
    target_object   = trigger.public_act,
    affinity        = None,  restriction = None,
    cost            = Findings(1) + Exposure(1),
    boost           = None,

    success     = arbiter.swap_target_profile(pa=trigger.public_act, new_profile=declared_profile),
    successcrit = None,  fail = None,  failcrit = None,
    on_accept   = None,  on_decline = None,

    portrait     = {Ghost: PortraitEntry(submitter=+1)},
    ps_framing   = None,
    narrative    = None,  perspectives = None,
    design_note  = "A public hijacking. The table sees Ghost swap the paperwork, but because Target Profiles are placed face-down, no one — not even the table — knows what Ghost changed the target to until Beat 4.",
    arbiter_note = "Reacts at Art 03 §9.2.0 when an opponent places a PA with a face-down Target Profile. Ghost announces the React, pays Findings(1) + Exposure(1), and declares a replacement Target Profile privately to ARBITER. ARBITER discards the opponent's original face-down Target Profile and places Ghost's declared_profile face-down in its place. At Beat 4 Apex Check, the PA resolves against Ghost's corrupted target.",
)
```

---

### GHO.MOD.12 — EMBEDDED CONTACT

#### Design Rationale
Ghost's ModBattleCard set, replicating the Directorate pattern (2 Boost +1/+2, 2 Hinder −1/−2, S132). Ghost's doctrine here is deliberately not literal force — §5a and modifier_card_ideas.md's provisional voice seed both frame Ghost's battlefield weight as "what they know about the contest, not what they bring to it." Weaker Boost tier (+1): a source already positioned in the district, not a deployed asset. Same no-cost/playtest-flagged (04-n94) terms as the rest of the subclass.

#### Card Story
A contact who was already embedded in the district long before the tension marker went down passes along what they've seen — reinforcing whichever side the playing faction has named.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | An informant already in place feeding intelligence into a live contest is a grounded, non-literal expression of Ghost's epistemic doctrine (§5a). | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only (`perspectives`/`design_note` schema-locked None); intelligence-sourcing register, no combat language. | Art 00 §9 |
| Doctrine alignment | ✓ | Boost expresses "understanding must precede action" through an intelligence asset, not force; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Ghost's Asset-category naming slot (S130). | Art 04 §6.1, §11.1 |
| Taxonomy fit | N/A | Schema-locked None (§11.1). | Art 04 §6.2, §11.1 |
| Balance | ✓ | Weak Boost tier per locked S132 pattern; no cost step exists for this subclass; playtest-flagged (04-n94). | PM05 04-n94 |
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

*S132. Ghost's ModBattleCard set, replicating the Directorate pattern (2 Boost + 1/+2, 2 Hinder −1/−2, PM05 09-06). Ghost's doctrine here is deliberately not literal force — §5a and modifier_card_ideas.md's provisional voice seed both frame Ghost's battlefield weight as "what they know about the contest, not what they bring to it." Weaker Boost tier (+1): a source already positioned in the district, not a deployed asset. Design-reviewed S140 (09-16 step 4) — same disposition as the Directorate pattern-set; portrait resolved same session (PM02 L269).*

```python
GHO.MOD.12 = Card(
    id      = "GHO.MOD.12",  card_id = "GHO.MOD.12",  version = "v0.1",
    name    = "Embedded Contact",
    tagline = "Someone already there tells the right people what's actually happening.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=1),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 1,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "A contact who was already in the district long before the tension marker went down passes along what they've seen.",
    arbiter_note = "Playable by any faction, not just Ghost (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### GHO.MOD.13 — SIGNALS PACKAGE

#### Design Rationale
Stronger Boost tier (+2) — a technical/surveillance escalation rather than a bigger human asset, consistent with Ghost's "Perimeter Sensors" precedent (GHO.MOD.2) for treating equipment as passive listening infrastructure, not deployed muscle. Same no-cost/playtest-flagged (04-n94) terms as GHO.MOD.12.

#### Card Story
Weeks of passive signals collection get compiled and handed over at the exact moment it's useful, reinforcing whichever side the playing faction has named.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Compiled surveillance handed over at the decisive moment is a grounded, non-literal expression of Ghost's epistemic doctrine. | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only; passive-collection register, consistent with GHO.MOD.2 equipment framing. | Art 00 §9 |
| Doctrine alignment | ✓ | Boost via technical intelligence infrastructure, not force; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Ghost's Equipment-category naming slot. | Art 04 §6.1, §11.1 |
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

*S132. Stronger Boost tier (+2) — a technical/surveillance escalation rather than a bigger human asset, consistent with Ghost's "Perimeter Sensors" precedent (GHO.MOD.2) for treating equipment as passive listening infrastructure, not deployed muscle. Design-reviewed S140 (09-16 step 4) — same disposition as GHO.MOD.12; portrait resolved same session (PM02 L269).*

```python
GHO.MOD.13 = Card(
    id      = "GHO.MOD.13",  card_id = "GHO.MOD.13",  version = "v0.1",
    name    = "Signals Package",
    tagline = "Everything the listening posts picked up, handed over at once.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Boost, target=None, magnitude=2),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 2,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "Weeks of passive collection, compiled and handed over at the moment it's actually useful.",
    arbiter_note = "Playable by any faction, not just Ghost (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### GHO.MOD.14 — PLANTED DOUBT

#### Design Rationale
Weaker Hinder tier (−1). Ghost's suppression is informational, never physical — this is a rumor or a manufactured inconsistency, not an attack. Fits the same register as GHO.MOD.5 False Flag and GHO.MOD.11 Manufactured Evidence (existing Ghost ModReactCards built on the same disinformation logic). Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
A detail that doesn't add up surfaces at exactly the wrong moment — nothing is proven, but the named faction's position stops holding together when it matters.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A manufactured inconsistency undermining a rival's position is a grounded, non-literal expression of Ghost's disinformation doctrine. | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only; disinformation register, matching GHO.MOD.5/GHO.MOD.11. | Art 00 §9 |
| Doctrine alignment | ✓ | Hinder via information warfare, not force; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Ghost's Tactic-category Hinder slot. | Art 04 §6.1, §11.1 |
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

*S132. Weaker Hinder tier (−1). Ghost's suppression is informational, never physical — this is a rumor or a manufactured inconsistency, not an attack. Fits the same register as GHO.MOD.5 False Flag and GHO.MOD.11 Manufactured Evidence (existing Ghost ModReactCards built on the same disinformation logic). Design-reviewed S140 (09-16 step 4) — same disposition as GHO.MOD.12/13; portrait resolved same session (PM02 L269).*

```python
GHO.MOD.14 = Card(
    id      = "GHO.MOD.14",  card_id = "GHO.MOD.14",  version = "v0.1",
    name    = "Planted Doubt",
    tagline = "A detail that doesn't add up, surfaced at exactly the wrong moment.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=1),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 1,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "Nothing is proven. Nothing needs to be — the timeline just stops holding together, right when it matters.",
    arbiter_note = "Playable by any faction, not just Ghost (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### GHO.MOD.15 — BLOWN COVER

#### Design Rationale
Stronger Hinder tier (−2), completing Ghost's 2 Boost/2 Hinder pattern. Escalates Planted Doubt from a rumor into something confirmed and specific — a position Ghost knew was fragile and chose to expose. Same no-cost/playtest-flagged (04-n94) terms as the rest of the set.

#### Card Story
Ghost knew exactly which detail would unravel the named faction's position if it surfaced now. It surfaces now.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | A deliberately exposed, confirmed weakness is the escalated form of Ghost's disinformation doctrine. | Art 00 §7; Art 04 §5a |
| Voice fit | ✓ | Scoped to `narrative`/`arbiter_note` only; same disinformation register as GHO.MOD.14, escalated to confirmed exposure. | Art 00 §9 |
| Doctrine alignment | ✓ | Hinder via deliberate exposure, not force; `doctrine_mod`/`target_faction` correctly None. | Art 04 §6.2 |
| Card type fit | ✓ | ModBattleCard/FactionSpecific correct; fills Ghost's Tactic-category escalated Hinder slot alongside GHO.MOD.14. | Art 04 §6.1, §11.1 |
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

*S132. Stronger Hinder tier (−2), completing Ghost's 2 Boost/2 Hinder pattern. Escalates Planted Doubt from a rumor into something confirmed and specific — a position Ghost knew was fragile and chose to expose. Design-reviewed S140 (09-16 step 4) — same disposition as the rest of the Ghost set; portrait resolved same session (PM02 L269). Closes Ghost's ModBattleCard review — all 4 cards (GHO.MOD.12–15) design-passed, no open issues.*

```python
GHO.MOD.15 = Card(
    id      = "GHO.MOD.15",  card_id = "GHO.MOD.15",  version = "v0.1",
    name    = "Blown Cover",
    tagline = "Whatever they were counting on staying hidden isn't hidden anymore.",
    type    = ModBattleCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1

    effect          = ModBattleExpr(direction=Hinder, target=None, magnitude=2),  # target named at commit (Art 03 §10.1.2 Step 1.2.2); magnitude playtest-flagged (04-n94, log to validate)
    value_rating    = 2,      # mirrors magnitude
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    # All other Card fields None per §6.2 Modifier Subclass Field Constraints (ModBattleCard column) — no trigger, no restriction, no beat, no resolution.
    cost            = None,   # not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction (confirmed S132 — Andy, applies uniformly, including Syndicate SYN.MOD.12–15).
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,   # ModBattleCard carries no portrait value — locked whole-subclass (Andy, S140, PM02 L269), not TBD
    narrative    = "Ghost knew exactly which detail would unravel them if it surfaced now. It surfaces now.",
    arbiter_note = "Playable by any faction, not just Ghost (Art 03 §10.1.2 Step 1.2.2) — commit face-down in front of the named target.",
)
```

---

### GHO.MOD.16 — PRE-ANALYSIS

#### Design Rationale
Replicates the Directorate ModActionCard pattern to Ghost. Minor threshold_delta tier (+5) — self-only, fits Ghost's epistemic doctrine ("understanding must precede action") cleanly.

#### Card Story
Advance modeling means Ghost already knows how this plays out before committing to it.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Pre-modeling advantage is the clean mechanical expression of Ghost's epistemic doctrine. | Art 00 §7 |
| Voice fit | ✓ | `faction=Ghost`; narrative reads in the intelligence/certainty register, not another faction's voice. | Art 00 §9 |
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

*S135. Replicates the Directorate ModActionCard pattern (DIR.MOD.14–25, 09-06/04-n157) to Ghost — locked format: 4 `threshold_delta` (+5/+10/+15/+20) + 2 `success_multiplier` (n=1/n=2) + 4 `ps_shift` (self +1/+2, target −1/−2) + 2 `cost_reduction` (n=1/n=2, PA-only), `cost=None` uniformly, `value_rating` 1–4 mirroring tier. Ghost voice: intelligence and leverage, epistemic doctrine — same doctrinal lens as Ghost's shipped ModBattleCard set (GHO.MOD.12–15). Minor threshold_delta tier (+5). Design-reviewed S139 (09-16 step 3).*

```python
GHO.MOD.16 = Card(
    id      = "GHO.MOD.16",  card_id = "GHO.MOD.16",  version = "v0.1",
    name    = "Pre-Analysis",
    tagline = "The modeling was already done before the operation was even submitted.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,  # modifier card — taxonomy excluded §11.1, effect is parasitic on host action

    effect          = ModActionExpr.threshold_delta(n=5),  # self-only (§6.3, 04-n170); eases the host CA/PA's own threshold
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,   # splay-display convention, PM02 L256 — same basis as all ModActionCard content
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Advance modeling means Ghost already knows how this plays out before committing to it.",
    arbiter_note = "Attach at Dispatch to any CA/PA in Ghost's own submitted packet (Art 03 §9.1.1) — no card-level host restriction.",
)
```

---

### GHO.MOD.17 — KNOWN VARIABLE

#### Design Rationale
Mid tier (+10). Same structure as GHO.MOD.16, self-only.

#### Card Story
Removing an unknown smooths the acting faction's own play — Ghost prefers certainty to speed.

**Design checklist:** Same disposition as GHO.MOD.16.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same epistemic-doctrine basis. | Art 00 §7 |
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
GHO.MOD.17 = Card(
    id      = "GHO.MOD.17",  card_id = "GHO.MOD.17",  version = "v0.1",
    name    = "Known Variable",
    tagline = "One fewer unknown in the equation, and the whole operation gets simpler.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=10),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Removing an unknown smooths the acting faction's own play — Ghost prefers certainty to speed.",
    arbiter_note = "Self-only, same basis as GHO.MOD.16.",
)
```

---

### GHO.MOD.18 — CLEAN CHANNEL

#### Design Rationale
Third tier (+15). Reframed from "Compromised Model" (hostile) per 04-n170, same self-only correction as the rest of the corpus's reframed tiers.

#### Card Story
A scrubbed data channel removes the noise that would otherwise complicate the operation.

**Design checklist:** Same disposition as GHO.MOD.16. Narrative independently checked — clean self-only, no hostile residue.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same epistemic-doctrine basis. | Art 00 §7; PM05 04-n170 |
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

*S135. Third of 4 threshold_delta tiers (+15). Reframed from an earlier hostile-flavored seed concept ("Compromised Model" — planting bad data to raise a rival's difficulty, `Whiteboard/modifier_card_ideas.md`) per **04-n170**: threshold_delta carries no faction parameter, so it can only ever ease Ghost's own host action. Design-reviewed S139 — reframe clean.*

```python
GHO.MOD.18 = Card(
    id      = "GHO.MOD.18",  card_id = "GHO.MOD.18",  version = "v0.1",
    name    = "Clean Channel",
    tagline = "No noise in the data, no ambiguity in the read.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=15),
    value_rating    = 3,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A scrubbed data channel removes the noise that would otherwise complicate the operation.",
    arbiter_note = "Reframed from a hostile-flavored seed concept per 04-n170, same basis as GUI.MOD.17/DIR.MOD.15/16.",
)
```

---

### GHO.MOD.19 — TOTAL PICTURE

#### Design Rationale
Capstone tier (+20), closing Ghost's `threshold_delta` quartet. Clean self-only narrative — full intelligence picture as the epistemic doctrine's purest expression.

#### Card Story
A fully assembled intelligence picture leaves nothing to chance — the operation proceeds on certainty, not estimate.

**Design checklist:** Same disposition as GHO.MOD.16.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same epistemic-doctrine basis. | Art 00 §7 |
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

*S135. Capstone threshold_delta tier (+20). Design-reviewed S139 — narrative clean.*

```python
GHO.MOD.19 = Card(
    id      = "GHO.MOD.19",  card_id = "GHO.MOD.19",  version = "v0.1",
    name    = "Total Picture",
    tagline = "Every piece assembled, nothing left to infer.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.threshold_delta(n=20),
    value_rating    = 4,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A fully assembled intelligence picture leaves nothing to chance — the operation proceeds on certainty, not estimate.",
    arbiter_note = "Capstone tier — log actual play outcomes before treating +20 as balanced (04-n157, same playtest caveat as the rest of this set).",
)
```

---

### GHO.MOD.20 — CLEAN DATA

#### Design Rationale
Common tier (n=1) of Ghost's `success_multiplier` pair. Self-only, verified-data framing fits doctrine cleanly.

#### Card Story
An operation run on verified information performs better than the plan ever assumed.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Verification-as-amplifier fits epistemic doctrine. | Art 00 §7 |
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
GHO.MOD.20 = Card(
    id      = "GHO.MOD.20",  card_id = "GHO.MOD.20",  version = "v0.1",
    name    = "Clean Data",
    tagline = "Verified information, and the operation performs better for it.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=1),
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "An operation run on verified information performs better than the plan ever assumed.",
    arbiter_note = "Self-only, amplifies Ghost's own host action.",
)
```

---

### GHO.MOD.21 — LAYERED ANALYSIS

#### Design Rationale
Capstone tier (n=2) of Ghost's `success_multiplier` pair. Same unvalidated-magnitude caveat as every n=2 success_multiplier card.

#### Card Story
Multiple independent confirmations amplify an outcome well past what a single source would support.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Cross-verification-as-amplifier fits epistemic doctrine tightly. | Art 00 §7 |
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
GHO.MOD.21 = Card(
    id      = "GHO.MOD.21",  card_id = "GHO.MOD.21",  version = "v0.1",
    name    = "Layered Analysis",
    tagline = "Three independent sources say the same thing. That doesn't happen by accident.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.success_multiplier(n=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Multiple independent confirmations amplify an outcome well past what a single source would support.",
    arbiter_note = "Rare/capstone tier — log actual play outcomes before treating n=2 as balanced (04-n157, same playtest caveat as 04-n94).",
)
```

---

### GHO.MOD.22 — QUIET CORRECTION

#### Design Rationale
Self-boost minor tier (+1) of the `ps_shift` matrix. `faction="acting"` needs no host-declared target — no submission-validity dependency.

#### Card Story
An error is quietly fixed before anyone notices it was ever there — a small, deliberate protection of standing.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Quiet-correction fits Ghost's discreet epistemic doctrine. | Art 00 §7 |
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
GHO.MOD.22 = Card(
    id      = "GHO.MOD.22",  card_id = "GHO.MOD.22",  version = "v0.1",
    name    = "Quiet Correction",
    tagline = "The error gets fixed before anyone thinks to look for it.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=1),  # self-boost, minor tier
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "An error is quietly fixed before anyone notices it was ever there — a small, deliberate protection of standing.",
    arbiter_note = "ps_shift is the only ModActionExpr variant with a faction parameter — this half resolves to the acting faction.",
)
```

---

### GHO.MOD.23 — FINDINGS PUBLISHED

#### Design Rationale
Self-boost major tier (+2) of the `ps_shift` matrix — same basis as GHO.MOD.22, doubled magnitude.

#### Card Story
A selective disclosure earns Ghost credibility and standing — true as far as it goes, and it goes exactly as far as intended.

**Design checklist:** Same disposition as GHO.MOD.22.

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as GHO.MOD.22. | Art 00 §7 |
| Voice fit | ✓ | Clean narrative — "true as far as it goes" is genuinely Ghost's voice. | Art 00 §9 |
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
GHO.MOD.23 = Card(
    id      = "GHO.MOD.23",  card_id = "GHO.MOD.23",  version = "v0.1",
    name    = "Findings Published",
    tagline = "A selective disclosure, timed for maximum credibility.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="acting", delta=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A selective disclosure earns Ghost credibility and standing — true as far as it goes, and it goes exactly as far as intended.",
    arbiter_note = "Self-boost, major tier — resolves to the acting faction.",
)
```

---

### GHO.MOD.24 — DISCREET LEAK

#### Design Rationale
Target-hinder minor tier (−1) of the `ps_shift` matrix. Same target-resolution behavior as STD.MOD.34 — resolves via host pairing, not an independent field.

#### Card Story
A detail reaches exactly the right ears — quiet, deniable, and costly to whoever it's about.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Discreet-leak is squarely Ghost's mechanical/narrative register. | Art 00 §7 |
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
GHO.MOD.24 = Card(
    id      = "GHO.MOD.24",  card_id = "GHO.MOD.24",  version = "v0.1",
    name    = "Discreet Leak",
    tagline = "A detail reaches exactly the right ears, and no further.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-1),  # target-hinder, minor tier
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A detail reaches exactly the right ears — quiet, deniable, and costly to whoever it's about.",
    arbiter_note = "`faction=\"target\"` resolves to whichever faction the host CA/PA it's packet-paired with names as its target_faction (§6.1) — the modifier's target IS the host action, not an independently-declared field (Andy, S139).",
)
```

---

### GHO.MOD.25 — MODEL FAILURE EXPOSED

#### Design Rationale
Target-hinder major tier (−2) of the `ps_shift` matrix. Same target-resolution behavior as GHO.MOD.24 (resolves via host pairing, not an independent field), doubled magnitude. Strong Ghost voice — "didn't lie, just let the truth land."

#### Card Story
A rival's flawed analysis becomes public — Ghost didn't lie, it just let the truth land at the worst possible time.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Same basis as GHO.MOD.24. | Art 00 §7 |
| Voice fit | ✓ | Excellent Ghost-specific register — truth-as-weapon, not fabrication. | Art 00 §9 |
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
GHO.MOD.25 = Card(
    id      = "GHO.MOD.25",  card_id = "GHO.MOD.25",  version = "v0.1",
    name    = "Model Failure Exposed",
    tagline = "A rival's analysis, wrong in public, on the record.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.ps_shift(faction="target", delta=-2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "A rival's flawed analysis becomes public — Ghost didn't lie, it just let the truth land at the worst possible time.",
    arbiter_note = "Same target-resolution behavior as GHO.MOD.24, major tier (Andy, S139).",
)
```

---

### GHO.MOD.26 — EXISTING DATASET

#### Design Rationale
Common tier (n=1) of Ghost's `cost_reduction` pair, PA-only per §6.3. Prior-research framing fits epistemic doctrine cleanly.

#### Card Story
Prior research lowers the cost of new analysis — nothing here starts from zero.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Prior-research reuse fits epistemic doctrine. | Art 00 §7 |
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
GHO.MOD.26 = Card(
    id      = "GHO.MOD.26",  card_id = "GHO.MOD.26",  version = "v0.1",
    name    = "Existing Dataset",
    tagline = "The research was already done. This just draws on it.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=1),  # PA-only (§6.3)
    value_rating    = 1,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Prior research lowers the cost of new analysis — nothing here starts from zero.",
    arbiter_note = "PA host only. Attach at Dispatch (Art 03 §9.2) alongside the declared PA.",
)
```

---

### GHO.MOD.27 — SHARED INFRASTRUCTURE

#### Design Rationale
Capstone tier (n=2) of Ghost's `cost_reduction` pair, closing the faction set. Same flat-vs-proportional caveat as the rest of the corpus's cost_reduction capstones.

#### Card Story
Borrowed analytical tools cut the overhead of building anything from scratch.

**Design checklist:**

| Category | Pass | Note | Artifact ref |
|----------|------|------|--------------|
| Action fit | ✓ | Shared-infrastructure reuse fits epistemic doctrine. | Art 00 §7 |
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
| Resource cost positioning | ✓ | `cost=None`, closed PM02 L256 convention. | PM02 L256; PM05 04-n178 |

#### Status

| | Design Pass | Issues Resolved | Signed off |
|--|-------------|-----------------|------------|
| Status | ✓ | ⚠ (flat-vs-proportional cost_reduction magnitude, 04-n157) |  |

*S135. Capstone cost_reduction tier (n=2). Design-reviewed S139 — closes the Ghost ModActionCard set (12/12 cards); GHO.MOD.24/25's target-restriction "gap" (schema_cleanup_log.md #21) closed same session — not a real gap, per Andy; no narrative flags.*

```python
GHO.MOD.27 = Card(
    id      = "GHO.MOD.27",  card_id = "GHO.MOD.27",  version = "v0.1",
    name    = "Shared Infrastructure",
    tagline = "The analytical tools were already built. Borrowing them costs almost nothing.",
    type    = ModActionCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = None,  function = None,  subject = None,

    effect          = ModActionExpr.cost_reduction(n=2),
    value_rating    = 2,
    ring_constraint = None,
    ring_origin     = None,   # Ghost faction modifier deck
    cost            = None,
    resolution_type = None,   # 04-n177 scaffolding placeholder
    boost           = None,   # 04-n177 scaffolding placeholder
    ps_framing      = None,   # 04-n177 scaffolding placeholder

    portrait     = None,
    narrative    = "Borrowed analytical tools cut the overhead of building anything from scratch.",
    arbiter_note = "Capstone cost_reduction tier — log actual play outcomes before treating a 2-unit reduction as balanced (04-n157).",
)
```

---


